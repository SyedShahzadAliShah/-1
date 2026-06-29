import { TextToSpeech } from '@capacitor-community/text-to-speech';
import { Capacitor } from '@capacitor/core';
import type { Language } from '../types';

let isSpeaking = false;

export async function speakText(text: string, lang: Language): Promise<void> {
  if (!text.trim()) return;

  const locale = lang === 'ur' ? 'ur-PK' : 'en-US';

  if (Capacitor.isNativePlatform()) {
    await TextToSpeech.speak({
      text,
      lang: locale,
      rate: 0.9,
      pitch: 1.0,
      volume: 1.0,
    });
  } else if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = locale;
    utterance.rate = 0.9;
    isSpeaking = true;
    utterance.onend = () => { isSpeaking = false; };
    window.speechSynthesis.speak(utterance);
  }
}

export async function stopSpeaking(): Promise<void> {
  if (Capacitor.isNativePlatform()) {
    await TextToSpeech.stop();
  } else if ('speechSynthesis' in window) {
    window.speechSynthesis.cancel();
  }
  isSpeaking = false;
}

export function getIsSpeaking(): boolean {
  return isSpeaking;
}

export function buildRecipeNarration(
  title: string,
  ingredients: string[],
  instructions: string[],
  healingNotes: string,
  lang: Language
): string {
  const labels = lang === 'ur'
    ? { ing: 'اجزاء', steps: 'طریقہ', notes: 'شفا یابی نوٹس' }
    : { ing: 'Ingredients', steps: 'Instructions', notes: 'Healing notes' };

  const parts = [
    title,
    `${labels.ing}: ${ingredients.join('. ')}`,
    `${labels.steps}: ${instructions.join('. ')}`,
    `${labels.notes}: ${healingNotes}`,
  ];
  return parts.join('. ');
}

export function buildFitnessNarration(
  title: string,
  description: string,
  steps: string[],
  lang: Language
): string {
  const label = lang === 'ur' ? 'اقدامات' : 'Steps';
  return `${title}. ${description}. ${label}: ${steps.join('. ')}`;
}
