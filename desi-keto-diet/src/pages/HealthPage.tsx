import { Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { ailmentGuides } from '../data/ailments';
import { useLang } from '../hooks/useLang';
import VocalsButton from '../components/VocalsButton';
import { buildPreviewNarration } from '../services/tts';

const icons: Record<string, string> = {
  gastric: '🫃', gyne: '🌸', psyche: '🧠', cardiac: '❤️',
  diabetic: '🩸', thyroid: '🦋', joint: '🦴', liver: '🫁', kidney: '💧',
};

export default function HealthPage() {
  const { t } = useTranslation();
  const lang = useLang();

  return (
    <div>
      <h2 className="section-title">{t('health.title')}</h2>
      <p className="section-subtitle">{t('health.subtitle')}</p>

      {ailmentGuides.map((guide) => (
        <Link key={guide.id} to={`/health/${guide.id}`} className="card card-link">
          <div className="card-with-vocals">
            <div className="card-with-vocals-body" style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
              <span style={{ fontSize: '1.75rem' }}>{icons[guide.id]}</span>
              <div>
                <strong>{guide.title[lang]}</strong>
                <p style={{ fontSize: '0.85rem', color: '#8fa88f', margin: '0.25rem 0 0' }}>
                  {guide.summary[lang].slice(0, 120)}...
                </p>
              </div>
            </div>
            <VocalsButton
              compact
              id={`health-${guide.id}`}
              title={guide.title[lang]}
              text={buildPreviewNarration(guide.title[lang], guide.summary[lang])}
            />
          </div>
        </Link>
      ))}

      <p className="disclaimer">{t('health.disclaimer')}</p>
    </div>
  );
}
