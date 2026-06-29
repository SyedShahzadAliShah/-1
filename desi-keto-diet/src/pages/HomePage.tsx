import { Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { recipes } from '../data/recipes';
import { ailmentGuides } from '../data/ailments';
import { fitnessRoutines } from '../data/fitness';
import { useLang } from '../hooks/useLang';

const ailmentIcons: Record<string, string> = {
  gastric: '🫃', gyne: '🌸', psyche: '🧠', cardiac: '❤️',
  diabetic: '🩸', thyroid: '🦋', joint: '🦴', liver: '🫁', kidney: '💧',
};

const cuisineIcons: Record<string, string> = {
  pakistani: '🇵🇰', bbq: '🔥', chinese: '🥢', continental: '🍽️',
  mughlai: '👑', punjabi: '🌾', sindhi: '🏺', balochi: '🏜️',
};

export default function HomePage() {
  const { t } = useTranslation();
  const lang = useLang();

  return (
    <div>
      <div className="hero-card">
        <h2>{t('home.welcome')}</h2>
        <p>{t('home.intro')}</p>
      </div>

      <h2 className="section-title">{t('home.ailmentFocus')}</h2>
      <div className="grid-2">
        {ailmentGuides.slice(0, 6).map((guide) => (
          <Link key={guide.id} to={`/health/${guide.id}`} className="grid-item">
            <div className="grid-item-icon">{ailmentIcons[guide.id]}</div>
            <div className="grid-item-label">{t(`ailments.${guide.id}`)}</div>
          </Link>
        ))}
      </div>

      <h2 className="section-title">{t('home.cuisineExplore')}</h2>
      <div className="grid-2">
        {(['pakistani', 'bbq', 'chinese', 'continental', 'mughlai', 'punjabi'] as const).map((c) => (
          <Link key={c} to={`/recipes?cuisine=${c}`} className="grid-item">
            <div className="grid-item-icon">{cuisineIcons[c]}</div>
            <div className="grid-item-label">{t(`cuisines.${c}`)}</div>
          </Link>
        ))}
      </div>

      <h2 className="section-title">{t('home.featuredRecipes')}</h2>
      {recipes.slice(0, 3).map((recipe) => (
        <Link key={recipe.id} to={`/recipes/${recipe.id}`} className="card card-link">
          <strong>{recipe.title[lang]}</strong>
          <div style={{ marginTop: '0.35rem' }}>
            <span className="badge">{t(`cuisines.${recipe.cuisine}`)}</span>
            {recipe.ailments.slice(0, 2).map((a) => (
              <span key={a} className="badge">{t(`ailments.${a}`)}</span>
            ))}
          </div>
        </Link>
      ))}

      <h2 className="section-title">{t('home.startFitness')}</h2>
      {fitnessRoutines.slice(0, 3).map((routine) => (
        <Link key={routine.id} to={`/fitness/${routine.id}`} className="card card-link">
          <strong>{routine.title[lang]}</strong>
          <div style={{ marginTop: '0.35rem' }}>
            <span className="badge">{t(`fitnessTypes.${routine.type}`)}</span>
            <span className="badge">{routine.duration} {t('common.minutes')}</span>
          </div>
        </Link>
      ))}
    </div>
  );
}
