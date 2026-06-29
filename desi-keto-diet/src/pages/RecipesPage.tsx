import { useState, useMemo } from 'react';
import { Link, useSearchParams } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { recipes, recipeCount } from '../data/recipes';
import { useLang } from '../hooks/useLang';
import VocalsButton from '../components/VocalsButton';
import { buildPreviewNarration } from '../services/tts';
import type { AilmentCategory, CuisineType } from '../types';

const PAGE_SIZE = 20;

export default function RecipesPage() {
  const { t } = useTranslation();
  const lang = useLang();
  const [searchParams] = useSearchParams();
  const [search, setSearch] = useState('');
  const [page, setPage] = useState(0);
  const [cuisineFilter, setCuisineFilter] = useState<CuisineType | 'all'>(
    (searchParams.get('cuisine') as CuisineType) || 'all'
  );
  const [ailmentFilter, setAilmentFilter] = useState<AilmentCategory | 'all'>('all');

  const cuisines: (CuisineType | 'all')[] = ['all', 'pakistani', 'bbq', 'chinese', 'continental', 'mughlai', 'punjabi', 'sindhi', 'balochi'];
  const ailments: (AilmentCategory | 'all')[] = ['all', 'gastric', 'gyne', 'psyche', 'cardiac', 'diabetic', 'thyroid', 'joint', 'liver', 'kidney'];

  const filtered = useMemo(() => {
    return recipes.filter((r) => {
      const matchSearch = !search || r.title[lang].toLowerCase().includes(search.toLowerCase())
        || r.description[lang].toLowerCase().includes(search.toLowerCase());
      const matchCuisine = cuisineFilter === 'all' || r.cuisine === cuisineFilter;
      const matchAilment = ailmentFilter === 'all' || r.ailments.includes(ailmentFilter);
      return matchSearch && matchCuisine && matchAilment;
    });
  }, [search, cuisineFilter, ailmentFilter, lang]);

  const totalPages = Math.max(1, Math.ceil(filtered.length / PAGE_SIZE));
  const safePage = Math.min(page, totalPages - 1);
  const paged = filtered.slice(safePage * PAGE_SIZE, (safePage + 1) * PAGE_SIZE);

  const resetFilters = () => {
    setPage(0);
  };

  return (
    <div>
      <h2 className="section-title">{t('recipes.title')}</h2>
      <p className="section-subtitle">{t('recipes.totalCount', { count: recipeCount })}</p>

      <input
        className="search-input"
        type="search"
        placeholder={t('common.search')}
        value={search}
        onChange={(e) => { setSearch(e.target.value); setPage(0); }}
      />

      <p className="section-subtitle">{t('recipes.filterCuisine')}</p>
      <div className="filter-bar">
        {cuisines.map((c) => (
          <button
            key={c}
            className={`filter-chip ${cuisineFilter === c ? 'active' : ''}`}
            onClick={() => { setCuisineFilter(c); resetFilters(); }}
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
            onClick={() => { setAilmentFilter(a); resetFilters(); }}
          >
            {a === 'all' ? t('recipes.all') : t(`ailments.${a}`)}
          </button>
        ))}
      </div>

      <p className="recipe-results-count">
        {t('recipes.showing', { shown: paged.length, total: filtered.length })}
      </p>

      {filtered.length === 0 && <p>{t('common.noResults')}</p>}

      {paged.map((recipe) => (
        <Link key={recipe.id} to={`/recipes/${recipe.id}`} className="card card-link">
          <div className="card-with-vocals">
            <div className="card-with-vocals-body">
              <strong>{recipe.title[lang]}</strong>
              <p style={{ fontSize: '0.85rem', color: '#8fa88f', margin: '0.35rem 0' }}>
                {recipe.description[lang].slice(0, 100)}...
              </p>
              <div>
                <span className="badge">{t(`cuisines.${recipe.cuisine}`)}</span>
                <span className="badge">{recipe.macros.calories} cal</span>
                <span className="badge">{recipe.prepTime + recipe.cookTime} {t('common.minutes')}</span>
              </div>
            </div>
            <VocalsButton
              compact
              id={`recipe-${recipe.id}`}
              title={recipe.title[lang]}
              text={buildPreviewNarration(recipe.title[lang], recipe.description[lang])}
            />
          </div>
        </Link>
      ))}

      {totalPages > 1 && (
        <div className="pagination">
          <button
            className="btn btn-secondary"
            disabled={safePage === 0}
            onClick={() => setPage((p) => p - 1)}
          >
            {t('recipes.prevPage')}
          </button>
          <span className="page-indicator">
            {t('recipes.pageOf', { page: safePage + 1, total: totalPages })}
          </span>
          <button
            className="btn btn-secondary"
            disabled={safePage >= totalPages - 1}
            onClick={() => setPage((p) => p + 1)}
          >
            {t('recipes.nextPage')}
          </button>
        </div>
      )}
    </div>
  );
}
