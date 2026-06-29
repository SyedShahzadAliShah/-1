import { useParams, useNavigate } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import { recipes } from '../data/recipes';
import { useLang } from '../hooks/useLang';
import { useTts } from '../hooks/useTts';
import { buildRecipeNarration } from '../services/tts';
import { exportRecipePdf } from '../services/pdf';
import { useState } from 'react';

export default function RecipeDetailPage() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const { t } = useTranslation();
  const lang = useLang();
  const { speaking, activeId, error, clearError, toggle } = useTts();
  const [exporting, setExporting] = useState(false);

  const recipe = recipes.find((r) => r.id === id);
  if (!recipe) return <p>{t('common.noResults')}</p>;

  const narration = buildRecipeNarration(
    recipe.title[lang],
    recipe.ingredients.map((i) => i[lang]),
    recipe.instructions.map((s) => s[lang]),
    recipe.healingNotes[lang],
    lang,
  );

  const handleListen = () => {
    clearError();
    void toggle(narration, { title: recipe.title[lang], id: `recipe-detail-${recipe.id}` });
  };

  const handleExport = async () => {
    setExporting(true);
    await exportRecipePdf(recipe, lang);
    setExporting(false);
  };

  return (
    <div>
      <button className="back-btn" onClick={() => navigate(-1)}>
        ← {t('common.back')}
      </button>

      <div className="detail-header">
        <h1 className="detail-title">{recipe.title[lang]}</h1>
        <div className="detail-meta">
          <span>{t(`cuisines.${recipe.cuisine}`)}</span>
          <span>{t('recipes.prepTime')}: {recipe.prepTime} {t('common.minutes')}</span>
          <span>{t('recipes.cookTime')}: {recipe.cookTime} {t('common.minutes')}</span>
          <span>{t('recipes.servings')}: {recipe.servings}</span>
        </div>
        <div style={{ marginTop: '0.5rem' }}>
          {recipe.ailments.map((a) => (
            <span key={a} className="badge">{t(`ailments.${a}`)}</span>
          ))}
        </div>
      </div>

      <p style={{ lineHeight: 1.6, color: '#c8d8c8' }}>{recipe.description[lang]}</p>

      <h3 className="section-title" style={{ fontSize: '0.95rem' }}>{t('recipes.macros')}</h3>
      <div className="macro-grid">
        <div className="macro-item">
          <div className="macro-value">{recipe.macros.calories}</div>
          <div className="macro-label">{t('recipes.calories')}</div>
        </div>
        <div className="macro-item">
          <div className="macro-value">{recipe.macros.protein}g</div>
          <div className="macro-label">{t('recipes.protein')}</div>
        </div>
        <div className="macro-item">
          <div className="macro-value">{recipe.macros.fat}g</div>
          <div className="macro-label">{t('recipes.fat')}</div>
        </div>
        <div className="macro-item">
          <div className="macro-value">{recipe.macros.carbs}g</div>
          <div className="macro-label">{t('recipes.carbs')}</div>
        </div>
        <div className="macro-item">
          <div className="macro-value">{recipe.macros.fiber}g</div>
          <div className="macro-label">{t('recipes.fiber')}</div>
        </div>
      </div>

      <div className="content-section">
        <h3>{t('recipes.ingredients')}</h3>
        <ul>
          {recipe.ingredients.map((ing, i) => (
            <li key={i}>{ing[lang]}</li>
          ))}
        </ul>
      </div>

      <div className="content-section">
        <h3>{t('recipes.instructions')}</h3>
        <ol>
          {recipe.instructions.map((step, i) => (
            <li key={i}>{step[lang]}</li>
          ))}
        </ol>
      </div>

      <div className="content-section">
        <h3>{t('recipes.healingNotes')}</h3>
        <p style={{ lineHeight: 1.6 }}>{recipe.healingNotes[lang]}</p>
      </div>

      {error && <p className="tts-error" role="alert">{error}</p>}

      <div className="btn-group">
        <button className="btn btn-audio" onClick={handleListen}>
          {speaking && activeId === `recipe-detail-${recipe.id}`
            ? `⏹ ${t('recipes.stopAudio')}`
            : `🔊 ${t('recipes.listenRecipe')}`}
        </button>
        <button className="btn btn-primary" onClick={handleExport} disabled={exporting}>
          📄 {t('recipes.exportPdf')}
        </button>
      </div>
    </div>
  );
}
