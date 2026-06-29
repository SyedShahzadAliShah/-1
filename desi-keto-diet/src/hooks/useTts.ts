import { useEffect, useState, useCallback } from 'react';
import { useTranslation } from 'react-i18next';
import {
  speakText,
  stopSpeaking,
  getIsSpeaking,
  onSpeakingChange,
  TtsError,
} from '../services/tts';
import { useLang } from './useLang';
import type { Language } from '../types';

export function useTts() {
  const { t } = useTranslation();
  const lang = useLang();
  const [speaking, setSpeaking] = useState(getIsSpeaking());
  const [error, setError] = useState<string | null>(null);

  useEffect(() => onSpeakingChange(setSpeaking), []);

  const clearError = useCallback(() => setError(null), []);

  const speak = useCallback(async (text: string, language: Language = lang) => {
    setError(null);
    try {
      await speakText(text, language);
    } catch (err) {
      if (err instanceof TtsError && err.code === 'aborted') return;
      const key = err instanceof TtsError && err.code === 'unsupported'
        ? 'tts.unsupported'
        : 'tts.error';
      setError(t(key));
    }
  }, [lang, speaking, t]);

  const stop = useCallback(async () => {
    setError(null);
    await stopSpeaking();
  }, []);

  const toggle = useCallback(async (text: string, language: Language = lang) => {
    if (speaking) {
      await stop();
    } else {
      await speak(text, language);
    }
  }, [lang, speak, speaking, stop]);

  return { speaking, error, clearError, speak, stop, toggle };
}
