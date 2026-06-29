import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './i18n';
import { setDocumentDirection } from './i18n';
import App from './App';
import './index.css';

const savedLang = localStorage.getItem('desi-keto-lang') || 'en';
import i18n from './i18n';
i18n.changeLanguage(savedLang);
setDocumentDirection(savedLang);

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
