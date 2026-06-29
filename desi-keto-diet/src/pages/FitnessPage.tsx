import { useState } from 'react';
import { Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { fitnessRoutines } from '../data/fitness';
import { useLang } from '../hooks/useLang';
import type { FitnessType } from '../types';

const icons: Record<string, string> = {
  aerobic: '🏃', yoga: '🧘', hiit: '⚡', walking: '🚶',
  strength: '💪', stretching: '🤸', pilates: '🎯',
};

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
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
            <span style={{ fontSize: '1.5rem' }}>{icons[routine.type]}</span>
            <div>
              <strong>{routine.title[lang]}</strong>
              <div style={{ marginTop: '0.35rem' }}>
                <span className="badge">{t(`fitnessTypes.${routine.type}`)}</span>
                <span className="badge">{routine.duration} {t('common.minutes')}</span>
                <span className="badge">{t(`fitness.${routine.difficulty}`)}</span>
                <span className="badge badge-animated">▶ {t('fitness.animatedRoutine')}</span>
              </div>
            </div>
          </div>
        </Link>
      ))}
    </div>
  );
}
