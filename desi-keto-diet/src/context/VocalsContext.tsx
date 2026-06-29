import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useState,
  type ReactNode,
} from 'react';
import { useTranslation } from 'react-i18next';
import {
  speakText,
  stopSpeaking,
  getIsSpeaking,
  onSpeakingChange,
  prefsToSpeakOptions,
  openVoiceInstall,
  TtsError,
} from '../services/tts';
import {
  loadVocalsPrefs,
  saveVocalsPrefs,
  type VocalsPrefs,
} from '../services/vocalsSettings';
import { useLang } from '../hooks/useLang';
import type { Language } from '../types';

export interface SpeakRequest {
  text: string;
  title?: string;
  language?: Language;
  id?: string;
}

interface VocalsContextValue {
  speaking: boolean;
  activeId: string | null;
  currentTitle: string | null;
  error: string | null;
  prefs: VocalsPrefs;
  updatePrefs: (patch: Partial<VocalsPrefs>) => void;
  speak: (request: SpeakRequest) => Promise<void>;
  stop: () => Promise<void>;
  toggle: (request: SpeakRequest) => Promise<void>;
  clearError: () => void;
  installVoices: () => Promise<void>;
}

const VocalsContext = createContext<VocalsContextValue | null>(null);

export function VocalsProvider({ children }: { children: ReactNode }) {
  const { t } = useTranslation();
  const lang = useLang();
  const [speaking, setSpeaking] = useState(getIsSpeaking());
  const [activeId, setActiveId] = useState<string | null>(null);
  const [currentTitle, setCurrentTitle] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [prefs, setPrefs] = useState<VocalsPrefs>(() => loadVocalsPrefs());

  useEffect(() => onSpeakingChange(setSpeaking), []);

  const updatePrefs = useCallback((patch: Partial<VocalsPrefs>) => {
    setPrefs((prev) => {
      const next = { ...prev, ...patch };
      saveVocalsPrefs(next);
      return next;
    });
  }, []);

  const clearError = useCallback(() => setError(null), []);

  const stop = useCallback(async () => {
    setError(null);
    setCurrentTitle(null);
    setActiveId(null);
    await stopSpeaking();
  }, []);

  const speak = useCallback(async ({ text, title, language, id }: SpeakRequest) => {
    if (!prefs.enabled || !text.trim()) return;

    setError(null);
    setCurrentTitle(title ?? null);
    setActiveId(id ?? text.slice(0, 80));
    try {
      await speakText(text, language ?? lang, prefsToSpeakOptions(prefs, language ?? lang));
    } catch (err) {
      if (err instanceof TtsError && err.code === 'aborted') return;
      const key = err instanceof TtsError && err.code === 'unsupported'
        ? 'tts.unsupported'
        : 'tts.error';
      setError(t(key));
    } finally {
      setCurrentTitle(null);
      setActiveId(null);
    }
  }, [lang, prefs, t]);

  const toggle = useCallback(async (request: SpeakRequest) => {
    const itemId = request.id ?? request.text.slice(0, 80);
    if (speaking && activeId === itemId) {
      await stop();
      return;
    }
    if (speaking) {
      await stopSpeaking();
      setActiveId(null);
      setCurrentTitle(null);
    }
    await speak(request);
  }, [activeId, speak, speaking, stop]);

  const installVoices = useCallback(async () => {
    await openVoiceInstall();
  }, []);

  const value = useMemo(
    () => ({
      speaking,
      activeId,
      currentTitle,
      error,
      prefs,
      updatePrefs,
      speak,
      stop,
      toggle,
      clearError,
      installVoices,
    }),
    [speaking, activeId, currentTitle, error, prefs, updatePrefs, speak, stop, toggle, clearError, installVoices],
  );

  return <VocalsContext.Provider value={value}>{children}</VocalsContext.Provider>;
}

export function useVocals(): VocalsContextValue {
  const ctx = useContext(VocalsContext);
  if (!ctx) throw new Error('useVocals must be used within VocalsProvider');
  return ctx;
}
