export interface VocalsPrefs {
  enabled: boolean;
  rate: number;
  pitch: number;
  volume: number;
  autoReadFitness: boolean;
}

const STORAGE_KEY = 'desi-keto-vocals';

export const DEFAULT_VOCALS_PREFS: VocalsPrefs = {
  enabled: true,
  rate: 0.92,
  pitch: 1.0,
  volume: 1.0,
  autoReadFitness: true,
};

export function loadVocalsPrefs(): VocalsPrefs {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return { ...DEFAULT_VOCALS_PREFS };
    const parsed = JSON.parse(raw) as Partial<VocalsPrefs>;
    return {
      enabled: parsed.enabled ?? DEFAULT_VOCALS_PREFS.enabled,
      rate: clamp(parsed.rate ?? DEFAULT_VOCALS_PREFS.rate, 0.5, 1.5),
      pitch: clamp(parsed.pitch ?? DEFAULT_VOCALS_PREFS.pitch, 0.5, 2.0),
      volume: clamp(parsed.volume ?? DEFAULT_VOCALS_PREFS.volume, 0.1, 1.0),
      autoReadFitness: parsed.autoReadFitness ?? DEFAULT_VOCALS_PREFS.autoReadFitness,
    };
  } catch {
    return { ...DEFAULT_VOCALS_PREFS };
  }
}

export function saveVocalsPrefs(prefs: VocalsPrefs): void {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(prefs));
}

function clamp(value: number, min: number, max: number): number {
  return Math.min(max, Math.max(min, value));
}
