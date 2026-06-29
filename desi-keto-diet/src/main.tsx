import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { TextToSpeech } from '@capacitor-community/text-to-speech';
import './i18n';
import { setDocumentDirection } from './i18n';
import App from './App';
import './index.css';

const savedLang = localStorage.getItem('desi-keto-lang') || 'en';
import i18n from './i18n';
i18n.changeLanguage(savedLang);
setDocumentDirection(savedLang);

// Warm up TTS engine so first playback is not silent
TextToSpeech.getSupportedLanguages().catch(() => {});
if ('speechSynthesis' in window) {
  window.speechSynthesis.getVoices();
  window.speechSynthesis.addEventListener('voiceschanged', () => {
    window.speechSynthesis.getVoices();
  }, { once: true });
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
