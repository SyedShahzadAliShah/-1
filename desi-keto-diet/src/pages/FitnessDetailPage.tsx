import { useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { fitnessRoutines } from '../data/fitness';
import { useLang } from '../hooks/useLang';
import { speakText, stopSpeaking, buildFitnessNarration } from '../services/tts';
import { exportFitnessPdf } from '../services/pdf';

export default function FitnessDetailPage() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const { t } = useTranslation();
  const lang = useLang();
  const [speaking, setSpeaking] = useState(false);

  const routine = fitnessRoutines.find((r) => r.id === id);
  if (!routine) return <p>{t('common.noResults')}</p>;

  const handleListen = async () => {
    if (speaking) {
      await stopSpeaking();
      setSpeaking(false);
      return;
    }
    setSpeaking(true);
    const text = buildFitnessNarration(
      routine.title[lang],
      routine.description[lang],
      routine.steps.map((s) => s[lang]),
      lang
    );
    await speakText(text, lang);
    setSpeaking(false);
  };

  return (
    <div>
      <button className="back-btn" onClick={() => navigate(-1)}>← {t('common.back')}</button>

      <h1 className="detail-title">{routine.title[lang]}</h1>
      <div className="detail-meta">
        <span>{t('fitness.duration')}: {routine.duration} {t('common.minutes')}</span>
        <span>{t('fitness.difficulty')}: {t(`fitness.${routine.difficulty}`)}</span>
        <span>{t('fitness.caloriesBurn')}: ~{routine.caloriesBurn}</span>
      </div>

      <p style={{ lineHeight: 1.6, color: '#c8d8c8', marginTop: '0.75rem' }}>{routine.description[lang]}</p>

      <div className="content-section">
        <h3>{t('fitness.benefits')}</h3>
        <ul>
          {routine.benefits.map((b, i) => <li key={i}>{b[lang]}</li>)}
        </ul>
      </div>

      <div className="content-section">
        <h3>{t('fitness.steps')}</h3>
        <ol>
          {routine.steps.map((step, i) => <li key={i}>{step[lang]}</li>)}
        </ol>
      </div>

      <div style={{ marginTop: '0.5rem' }}>
        {routine.ailments.map((a) => (
          <span key={a} className="badge">{t(`ailments.${a}`)}</span>
        ))}
      </div>

      <div className="btn-group">
        <button className="btn btn-audio" onClick={handleListen}>
          {speaking ? `⏹ ${t('recipes.stopAudio')}` : `🔊 ${t('fitness.listenRoutine')}`}
        </button>
        <button className="btn btn-primary" onClick={() => exportFitnessPdf(routine, lang)}>
          📄 {t('recipes.exportPdf')}
        </button>
      </div>
    </div>
  );
}
