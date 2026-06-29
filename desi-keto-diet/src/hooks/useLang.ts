import { useTranslation } from 'react-i18next';
import type { Language } from '../types';

export function useLang(): Language {
  const { i18n } = useTranslation();
  return (i18n.language === 'ur' ? 'ur' : 'en') as Language;
}

export function useLocalizedText() {
  const lang = useLang();
  return <T extends { en: string; ur: string }>(text: T): string => text[lang];
}
