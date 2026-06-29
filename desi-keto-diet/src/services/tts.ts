import { TextToSpeech, QueueStrategy } from '@capacitor-community/text-to-speech';
import { Capacitor } from '@capacitor/core';
import type { Language } from '../types';
import { DEFAULT_VOCALS_PREFS, type VocalsPrefs } from './vocalsSettings';

export interface SpeakOptions {
  rate?: number;
  pitch?: number;
  volume?: number;
}

const MAX_CHUNK = 3500;
const LANG_CANDIDATES: Record<Language, string[]> = {
  en: ['en-US', 'en-GB', 'en-IN', 'en'],
  ur: ['ur-PK', 'ur', 'hi-IN', 'en-US'],
};

let abortRequested = false;
let isSpeaking = false;
const listeners = new Set<(speaking: boolean) => void>();

function setSpeaking(value: boolean) {
  isSpeaking = value;
  listeners.forEach((fn) => fn(value));
}

export function onSpeakingChange(fn: (speaking: boolean) => void): () => void {
  listeners.add(fn);
  fn(isSpeaking);
  return () => listeners.delete(fn);
}

export function getIsSpeaking(): boolean {
  return isSpeaking;
}

async function waitForVoices(): Promise<void> {
  if (!('speechSynthesis' in window)) return;
  const synth = window.speechSynthesis;
  if (synth.getVoices().length > 0) return;
  await new Promise<void>((resolve) => {
    const done = () => {
      clearTimeout(timer);
      resolve();
    };
    const timer = setTimeout(done, 1500);
    synth.addEventListener('voiceschanged', done, { once: true });
  });
}

async function waitForTtsReady(): Promise<void> {
  for (let attempt = 0; attempt < 15; attempt++) {
    try {
      await TextToSpeech.getSupportedLanguages();
      return;
    } catch (err) {
      const message = err instanceof Error ? err.message : String(err);
      if (!message.includes('Not yet initialized') && !message.includes('not available')) {
        throw err;
      }
      await delay(250);
    }
  }
  await waitForVoices();
}

async function resolveLocale(lang: Language): Promise<string> {
  for (const candidate of LANG_CANDIDATES[lang]) {
    try {
      const { supported } = await TextToSpeech.isLanguageSupported({ lang: candidate });
      if (supported) return candidate;
    } catch {
      // try next candidate
    }
  }
  return 'en-US';
}

async function findVoiceIndex(locale: string): Promise<number | undefined> {
  try {
    const { voices } = await TextToSpeech.getSupportedVoices();
    if (!voices?.length) return undefined;

    const prefix = locale.split('-')[0].toLowerCase();
    const exact = voices.findIndex((v) => v.lang?.toLowerCase() === locale.toLowerCase());
    if (exact >= 0) return exact;

    const partial = voices.findIndex((v) => v.lang?.toLowerCase().startsWith(prefix));
    if (partial >= 0) return partial;

    const local = voices.findIndex((v) => v.localService && v.lang?.toLowerCase().startsWith(prefix));
    return local >= 0 ? local : undefined;
  } catch {
    return undefined;
  }
}

function chunkText(text: string): string[] {
  const normalized = text.replace(/\s+/g, ' ').trim();
  if (normalized.length <= MAX_CHUNK) return [normalized];

  const chunks: string[] = [];
  let rest = normalized;

  while (rest.length > MAX_CHUNK) {
    let cut = rest.lastIndexOf('. ', MAX_CHUNK);
    if (cut < MAX_CHUNK / 2) cut = rest.lastIndexOf(' ', MAX_CHUNK);
    if (cut < MAX_CHUNK / 3) cut = MAX_CHUNK;
    chunks.push(rest.slice(0, cut + 1).trim());
    rest = rest.slice(cut + 1).trim();
  }
  if (rest) chunks.push(rest);
  return chunks;
}

function delay(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export class TtsError extends Error {
  code: 'unsupported' | 'unavailable' | 'utterance' | 'aborted';

  constructor(
    message: string,
    code: 'unsupported' | 'unavailable' | 'utterance' | 'aborted' = 'unavailable',
  ) {
    super(message);
    this.name = 'TtsError';
    this.code = code;
  }
}

function resolveSpeakOptions(lang: Language, options?: SpeakOptions): SpeakOptions {
  const baseRate = lang === 'ur' ? 0.82 : DEFAULT_VOCALS_PREFS.rate;
  return {
    rate: options?.rate ?? baseRate,
    pitch: options?.pitch ?? DEFAULT_VOCALS_PREFS.pitch,
    volume: options?.volume ?? DEFAULT_VOCALS_PREFS.volume,
  };
}

export function prefsToSpeakOptions(prefs: VocalsPrefs, lang: Language): SpeakOptions {
  const baseRate = lang === 'ur' ? Math.min(prefs.rate, 0.9) : prefs.rate;
  return { rate: baseRate, pitch: prefs.pitch, volume: prefs.volume };
}

export async function openVoiceInstall(): Promise<void> {
  if (Capacitor.getPlatform() !== 'android') return;
  try {
    await TextToSpeech.openInstall();
  } catch {
    // installer may be unavailable
  }
}

export async function speakText(
  text: string,
  lang: Language,
  options?: SpeakOptions,
): Promise<void> {
  if (!text.trim()) return;

  await stopSpeaking();
  abortRequested = false;
  setSpeaking(true);

  try {
    await waitForTtsReady();
    const locale = await resolveLocale(lang);
    const voice = await findVoiceIndex(locale);

    if (lang === 'ur' && !locale.startsWith('ur') && locale !== 'hi-IN') {
      if (Capacitor.getPlatform() === 'android') {
        try {
          await TextToSpeech.openInstall();
        } catch {
          // installer may be unavailable
        }
      }
      throw new TtsError('Urdu voice data is not installed on this device.', 'unsupported');
    }

    const chunks = chunkText(text);
    for (let i = 0; i < chunks.length; i++) {
      if (abortRequested) throw new TtsError('Playback stopped.', 'aborted');

      const speech = resolveSpeakOptions(lang, options);
      await TextToSpeech.speak({
        text: chunks[i],
        lang: locale,
        rate: speech.rate!,
        pitch: speech.pitch!,
        volume: speech.volume!,
        voice,
        queueStrategy: QueueStrategy.Flush,
      });
    }
  } catch (err) {
    if (err instanceof TtsError) throw err;
    const message = err instanceof Error ? err.message : String(err);
    if (message.includes('not supported') || message.includes('Unsupported')) {
      if (Capacitor.getPlatform() === 'android') {
        try {
          await TextToSpeech.openInstall();
        } catch {
          // ignore
        }
      }
      throw new TtsError('Voice language not supported. Install speech data in device settings.', 'unsupported');
    }
    if (message.includes('Failed to read') || message.includes('utterance')) {
      throw new TtsError('Could not read text aloud. Try again.', 'utterance');
    }
    throw new TtsError(message || 'Text-to-speech is unavailable.', 'unavailable');
  } finally {
    setSpeaking(false);
  }
}

export async function stopSpeaking(): Promise<void> {
  abortRequested = true;
  try {
    await TextToSpeech.stop();
  } catch {
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
  }
  setSpeaking(false);
}

export function buildRecipeNarration(
  title: string,
  ingredients: string[],
  instructions: string[],
  healingNotes: string,
  lang: Language,
): string {
  const labels = lang === 'ur'
    ? { ing: 'اجزاء', steps: 'طریقہ', notes: 'شفا یابی نوٹس' }
    : { ing: 'Ingredients', steps: 'Instructions', notes: 'Healing notes' };

  return [
    title,
    `${labels.ing}: ${ingredients.join('. ')}`,
    `${labels.steps}: ${instructions.join('. ')}`,
    `${labels.notes}: ${healingNotes}`,
  ].join('. ');
}

export function buildFitnessNarration(
  title: string,
  description: string,
  steps: string[],
  lang: Language,
): string {
  const label = lang === 'ur' ? 'اقدامات' : 'Steps';
  return `${title}. ${description}. ${label}: ${steps.join('. ')}`;
}

export function buildHealthNarration(
  title: string,
  summary: string,
  ketoApproach: string,
  medicationAlternatives: string,
): string {
  return [title, summary, ketoApproach, medicationAlternatives].join('. ');
}

export function buildPreviewNarration(title: string, description: string): string {
  return `${title}. ${description}`;
}
