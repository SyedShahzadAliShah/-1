import { useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { ailmentGuides } from '../data/ailments';
import { useLang } from '../hooks/useLang';
import { speakText, stopSpeaking } from '../services/tts';
import { exportHealthGuidePdf } from '../services/pdf';

export default function HealthDetailPage() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const { t } = useTranslation();
  const lang = useLang();
  const [speaking, setSpeaking] = useState(false);

  const guide = ailmentGuides.find((g) => g.id === id);
  if (!guide) return <p>{t('common.noResults')}</p>;

  const handleListen = async () => {
    if (speaking) {
      await stopSpeaking();
      setSpeaking(false);
      return;
    }
    setSpeaking(true);
    const text = [
      guide.title[lang],
      guide.summary[lang],
      guide.ketoApproach[lang],
      guide.medicationAlternatives[lang],
    ].join('. ');
    await speakText(text, lang);
    setSpeaking(false);
  };

  return (
    <div>
      <button className="back-btn" onClick={() => navigate(-1)}>← {t('common.back')}</button>

      <h1 className="detail-title">{guide.title[lang]}</h1>
      <p style={{ lineHeight: 1.6, color: '#c8d8c8' }}>{guide.summary[lang]}</p>

      <div className="content-section">
        <h3>{t('health.ketoApproach')}</h3>
        <p style={{ lineHeight: 1.6 }}>{guide.ketoApproach[lang]}</p>
      </div>

      <div className="content-section">
        <h3>{t('health.foodsToEat')}</h3>
        <ul>
          {guide.foodsToEat.map((item, i) => <li key={i}>{item[lang]}</li>)}
        </ul>
      </div>

      <div className="content-section">
        <h3>{t('health.foodsToAvoid')}</h3>
        <ul>
          {guide.foodsToAvoid.map((item, i) => <li key={i}>{item[lang]}</li>)}
        </ul>
      </div>

      <div className="content-section">
        <h3>{t('health.lifestyleTips')}</h3>
        <ul>
          {guide.lifestyleTips.map((item, i) => <li key={i}>{item[lang]}</li>)}
        </ul>
      </div>

      <div className="content-section">
        <h3>{t('health.medicationNote')}</h3>
        <p style={{ lineHeight: 1.6 }}>{guide.medicationAlternatives[lang]}</p>
      </div>

      <div className="btn-group">
        <button className="btn btn-audio" onClick={handleListen}>
          {speaking ? `⏹ ${t('recipes.stopAudio')}` : `🔊 ${t('recipes.listenRecipe')}`}
        </button>
        <button className="btn btn-primary" onClick={() => exportHealthGuidePdf(guide, lang)}>
          📄 {t('recipes.exportPdf')}
        </button>
      </div>

      <p className="disclaimer">{t('health.disclaimer')}</p>
    </div>
  );
}
