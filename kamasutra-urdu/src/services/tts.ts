import { TextToSpeech } from '@capacitor-community/text-to-speech';
import { Capacitor } from '@capacitor/core';

let isSpeaking = false;

export async function speakUrdu(text: string): Promise<void> {
  if (!text.trim()) return;

  try {
    if (Capacitor.isNativePlatform()) {
      await TextToSpeech.stop();
      await TextToSpeech.speak({
        text,
        lang: 'ur-PK',
        rate: 0.85,
        pitch: 1.0,
        volume: 1.0,
        category: 'ambient',
      });
      isSpeaking = true;
      return;
    }

    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = 'ur-PK';
      utterance.rate = 0.85;
      utterance.pitch = 1.0;

      const voices = window.speechSynthesis.getVoices();
      const urduVoice = voices.find(
        (v) => v.lang.startsWith('ur') || v.lang.includes('Urdu') || v.name.includes('Urdu')
      );
      if (urduVoice) utterance.voice = urduVoice;

      isSpeaking = true;
      utterance.onend = () => {
        isSpeaking = false;
      };
      window.speechSynthesis.speak(utterance);
    }
  } catch (err) {
    console.error('TTS error:', err);
    isSpeaking = false;
  }
}

export async function stopSpeaking(): Promise<void> {
  try {
    if (Capacitor.isNativePlatform()) {
      await TextToSpeech.stop();
    } else if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
  } finally {
    isSpeaking = false;
  }
}

export function getIsSpeaking(): boolean {
  return isSpeaking;
}
