import { useState, useMemo } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { recipes } from '../data/recipes';
import { useLang } from '../hooks/useLang';
import type { AilmentCategory, CuisineType } from '../types';

export default function RecipesPage() {
  const { t } = useTranslation();
  const lang = useLang();
  const [searchParams] = useSearchParams();
  const [search, setSearch] = useState('');
  const [cuisineFilter, setCuisineFilter] = useState<CuisineType | 'all'>(
    (searchParams.get('cuisine') as CuisineType) || 'all'
  );
  const [ailmentFilter, setAilmentFilter] = useState<AilmentCategory | 'all'>('all');

  const cuisines: (CuisineType | 'all')[] = ['all', 'pakistani', 'bbq', 'chinese', 'continental', 'mughlai', 'punjabi', 'sindhi', 'balochi'];
  const ailments: (AilmentCategory | 'all')[] = ['all', 'gastric', 'gyne', 'psyche', 'cardiac', 'diabetic', 'thyroid', 'joint', 'liver', 'kidney'];

  const filtered = useMemo(() => {
    return recipes.filter((r) => {
      const matchSearch = !search || r.title[lang].toLowerCase().includes(search.toLowerCase());
      const matchCuisine = cuisineFilter === 'all' || r.cuisine === cuisineFilter;
      const matchAilment = ailmentFilter === 'all' || r.ailments.includes(ailmentFilter);
      return matchSearch && matchCuisine && matchAilment;
    });
  }, [search, cuisineFilter, ailmentFilter, lang]);

  return (
    <div>
      <h2 className="section-title">{t('recipes.title')}</h2>
      <input
        className="search-input"
        type="search"
        placeholder={t('common.search')}
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      <p className="section-subtitle">{t('recipes.filterCuisine')}</p>
      <div className="filter-bar">
        {cuisines.map((c) => (
          <button
            key={c}
            className={`filter-chip ${cuisineFilter === c ? 'active' : ''}`}
            onClick={() => setCuisineFilter(c)}
          >
            {c === 'all' ? t('recipes.all') : t(`cuisines.${c}`)}
          </button>
        ))}
      </div>

      <p className="section-subtitle">{t('recipes.filterAilment')}</p>
      <div className="filter-bar">
        {ailments.map((a) => (
          <button
            key={a}
            className={`filter-chip ${ailmentFilter === a ? 'active' : ''}`}
            onClick={() => setAilmentFilter(a)}
          >
            {a === 'all' ? t('recipes.all') : t(`ailments.${a}`)}
          </button>
        ))}
      </div>

      {filtered.length === 0 && <p>{t('common.noResults')}</p>}

      {filtered.map((recipe) => (
        <Link key={recipe.id} to={`/recipes/${recipe.id}`} className="card card-link">
          <strong>{recipe.title[lang]}</strong>
          <p style={{ fontSize: '0.85rem', color: '#8fa88f', margin: '0.35rem 0' }}>
            {recipe.description[lang].slice(0, 100)}...
          </p>
          <div>
            <span className="badge">{t(`cuisines.${recipe.cuisine}`)}</span>
            <span className="badge">{recipe.macros.calories} cal</span>
            <span className="badge">{recipe.prepTime + recipe.cookTime} {t('common.minutes')}</span>
          </div>
        </Link>
      ))}
    </div>
  );
}
