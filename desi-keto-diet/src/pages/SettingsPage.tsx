import { useTranslation } from 'react-i18next';
import { setDocumentDirection } from '../i18n';

export default function SettingsPage() {
  const { t, i18n } = useTranslation();

  const changeLanguage = (lang: string) => {
    i18n.changeLanguage(lang);
    setDocumentDirection(lang);
    localStorage.setItem('desi-keto-lang', lang);
  };

  return (
    <div>
      <h2 className="section-title">{t('settings.title')}</h2>

      <div className="card">
        <h3 style={{ margin: '0 0 0.75rem', color: '#95d5b2', fontSize: '0.95rem' }}>
          {t('settings.language')}
        </h3>
        <div className="lang-toggle">
          <button
            className={`lang-btn ${i18n.language === 'en' ? 'active' : ''}`}
            onClick={() => changeLanguage('en')}
          >
            {t('settings.english')}
          </button>
          <button
            className={`lang-btn ${i18n.language === 'ur' ? 'active' : ''}`}
            onClick={() => changeLanguage('ur')}
          >
            {t('settings.urdu')}
          </button>
        </div>
      </div>

      <div className="card">
        <h3 style={{ margin: '0 0 0.75rem', color: '#95d5b2', fontSize: '0.95rem' }}>
          {t('settings.about')}
        </h3>
        <p className="about-text">{t('settings.aboutText')}</p>
      </div>

      <div className="card">
        <h3 style={{ margin: '0 0 0.5rem', color: '#95d5b2', fontSize: '0.95rem' }}>Features</h3>
        <ul style={{ margin: 0, paddingInlineStart: '1.25rem', fontSize: '0.85rem', color: '#c8d8c8' }}>
          <li>10+ Keto recipes (Pakistani, BBQ, Chinese, Continental, Mughlai, Sindhi, Balochi)</li>
          <li>9 condition-specific health guides (Gastric, Gyne, Psyche, Cardiac, Diabetic, Thyroid, Joint, Liver, Kidney)</li>
          <li>8 fitness routines (Aerobic, Yoga, HIIT, Walking, Strength, Stretching, Pilates)</li>
          <li>Bilingual English/Urdu with RTL support</li>
          <li>Text-to-speech audio narration</li>
          <li>PDF export for recipes, health guides, and fitness routines</li>
          <li>In-depth knowledge articles on keto science and desi healing</li>
        </ul>
      </div>

      <p className="disclaimer">{t('health.disclaimer')}</p>
    </div>
  );
}
