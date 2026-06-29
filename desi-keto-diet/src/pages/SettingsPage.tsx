import { useTranslation } from 'react-i18next';
import { setDocumentDirection } from '../i18n';
import { useVocals } from '../context/VocalsContext';
import '../components/VocalsButton.css';

function Toggle({
  on,
  onChange,
  label,
}: {
  on: boolean;
  onChange: (value: boolean) => void;
  label: string;
}) {
  return (
    <div className="vocals-settings-row">
      <span className="vocals-settings-label">{label}</span>
      <button
        type="button"
        className={`vocals-toggle ${on ? 'on' : ''}`}
        onClick={() => onChange(!on)}
        aria-pressed={on}
        aria-label={label}
      >
        <span className="vocals-toggle-knob" />
      </button>
    </div>
  );
}

function SliderRow({
  label,
  value,
  min,
  max,
  step,
  onChange,
  format,
}: {
  label: string;
  value: number;
  min: number;
  max: number;
  step: number;
  onChange: (value: number) => void;
  format: (value: number) => string;
}) {
  return (
    <div className="vocals-settings-row">
      <span className="vocals-settings-label">{label}</span>
      <input
        type="range"
        className="vocals-slider"
        min={min}
        max={max}
        step={step}
        value={value}
        onChange={(e) => onChange(parseFloat(e.target.value))}
        aria-label={label}
      />
      <span className="vocals-slider-value">{format(value)}</span>
    </div>
  );
}

export default function SettingsPage() {
  const { t, i18n } = useTranslation();
  const { prefs, updatePrefs, installVoices } = useVocals();

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
          {t('vocals.title')}
        </h3>
        <p style={{ fontSize: '0.8rem', color: '#8fa88f', margin: '0 0 0.75rem' }}>
          {t('vocals.subtitle')}
        </p>

        <Toggle
          label={t('vocals.enabled')}
          on={prefs.enabled}
          onChange={(enabled) => updatePrefs({ enabled })}
        />

        <SliderRow
          label={t('vocals.rate')}
          value={prefs.rate}
          min={0.5}
          max={1.5}
          step={0.05}
          onChange={(rate) => updatePrefs({ rate })}
          format={(v) => `${Math.round(v * 100)}%`}
        />
        <SliderRow
          label={t('vocals.pitch')}
          value={prefs.pitch}
          min={0.5}
          max={2}
          step={0.05}
          onChange={(pitch) => updatePrefs({ pitch })}
          format={(v) => `${Math.round(v * 100)}%`}
        />
        <SliderRow
          label={t('vocals.volume')}
          value={prefs.volume}
          min={0.1}
          max={1}
          step={0.05}
          onChange={(volume) => updatePrefs({ volume })}
          format={(v) => `${Math.round(v * 100)}%`}
        />

        <button
          type="button"
          className="btn btn-secondary"
          style={{ marginTop: '0.75rem', width: '100%' }}
          onClick={() => void installVoices()}
        >
          {t('vocals.installVoices')}
        </button>
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
          <li>200 Keto recipes (Pakistani, BBQ, Chinese, Continental, Mughlai, Punjabi, Sindhi, Balochi)</li>
          <li>9 condition-specific health guides (Gastric, Gyne, Psyche, Cardiac, Diabetic, Thyroid, Joint, Liver, Kidney)</li>
          <li>8 fitness routines (Aerobic, Yoga, HIIT, Walking, Strength, Stretching, Pilates)</li>
          <li>Bilingual English/Urdu with RTL support</li>
          <li>Built-in vocals — listen anywhere in the app</li>
          <li>PDF export for recipes, health guides, and fitness routines</li>
          <li>In-depth knowledge articles on keto science and desi healing</li>
        </ul>
      </div>

      <p className="disclaimer">{t('health.disclaimer')}</p>
    </div>
  );
}
