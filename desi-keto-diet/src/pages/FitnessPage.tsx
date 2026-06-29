import { useState } from 'react';
import { Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { fitnessRoutines } from '../data/fitness';
import { useLang } from '../hooks/useLang';
import VocalsButton from '../components/VocalsButton';
import FitnessFigureEmbed from '../components/FitnessFigureEmbed';
import { buildPreviewNarration } from '../services/tts';
import type { FitnessType } from '../types';
import '../components/FitnessFigureEmbed.css';

export default function FitnessPage() {
  const { t } = useTranslation();
  const lang = useLang();
  const [typeFilter, setTypeFilter] = useState<FitnessType | 'all'>('all');

  const types: (FitnessType | 'all')[] = ['all', 'aerobic', 'yoga', 'hiit', 'walking', 'strength', 'stretching', 'pilates'];

  const filtered = typeFilter === 'all'
    ? fitnessRoutines
    : fitnessRoutines.filter((r) => r.type === typeFilter);

  return (
    <div>
      <h2 className="section-title">{t('fitness.title')}</h2>
      <p className="section-subtitle">{t('fitness.subtitle')}</p>

      <div className="filter-bar">
        {types.map((type) => (
          <button
            key={type}
            className={`filter-chip ${typeFilter === type ? 'active' : ''}`}
            onClick={() => setTypeFilter(type)}
          >
            {type === 'all' ? t('recipes.all') : t(`fitnessTypes.${type}`)}
          </button>
        ))}
      </div>

      {filtered.map((routine) => (
        <Link key={routine.id} to={`/fitness/${routine.id}`} className="card card-link">
          <div className="fitness-card-layout">
            <FitnessFigureEmbed routineId={routine.id} label={t('fitness.animatedRoutine')} />
            <div className="fitness-card-body">
              <strong>{routine.title[lang]}</strong>
              <p style={{ fontSize: '0.82rem', color: '#8fa88f', margin: '0.3rem 0 0.4rem', lineHeight: 1.4 }}>
                {routine.description[lang].slice(0, 90)}…
              </p>
              <div>
                <span className="badge">{t(`fitnessTypes.${routine.type}`)}</span>
                <span className="badge">{routine.duration} {t('common.minutes')}</span>
                <span className="badge">{t(`fitness.${routine.difficulty}`)}</span>
              </div>
            </div>
            <div className="fitness-card-actions">
              <VocalsButton
                compact
                id={`fitness-${routine.id}`}
                title={routine.title[lang]}
                text={buildPreviewNarration(routine.title[lang], routine.description[lang])}
              />
            </div>
          </div>
        </Link>
      ))}
    </div>
  );
}
