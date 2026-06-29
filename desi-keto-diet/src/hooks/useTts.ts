import { useVocals } from '../context/VocalsContext';
import type { Language } from '../types';

export interface TtsOptions {
  title?: string;
  id?: string;
  language?: Language;
}

export function useTts() {
  const { speaking, activeId, error, clearError, speak, stop, toggle, prefs } = useVocals();

  return {
    speaking,
    activeId,
    error,
    clearError,
    speak: (text: string, options?: TtsOptions) => speak({ text, ...options }),
    stop,
    toggle: (text: string, options?: TtsOptions) => toggle({ text, ...options }),
    vocalsEnabled: prefs.enabled,
  };
}
