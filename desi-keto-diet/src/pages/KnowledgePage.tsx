import { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { knowledgeArticles } from '../data/knowledge';
import { useLang } from '../hooks/useLang';
import { useTts } from '../hooks/useTts';

export default function KnowledgePage() {
  const { t } = useTranslation();
  const lang = useLang();
  const { speaking, error, clearError, speak, stop } = useTts();
  const [expandedId, setExpandedId] = useState<string | null>(null);
  const [activeId, setActiveId] = useState<string | null>(null);

  const handleListen = async (id: string, text: string) => {
    clearError();
    if (speaking && activeId === id) {
      await stop();
      setActiveId(null);
      return;
    }
    setActiveId(id);
    await speak(text);
    setActiveId(null);
  };

  return (
    <div>
      <h2 className="section-title">{t('knowledge.title')}</h2>
      <p className="section-subtitle">{t('knowledge.subtitle')}</p>

      {error && <p className="tts-error" role="alert">{error}</p>}

      {knowledgeArticles.map((article) => (
        <div key={article.id} className="card">
          <strong
            style={{ cursor: 'pointer', display: 'block' }}
            onClick={() => setExpandedId(expandedId === article.id ? null : article.id)}
          >
            {article.title[lang]} {expandedId === article.id ? '▼' : '▶'}
          </strong>

          {expandedId === article.id && (
            <>
              <div className="article-content" style={{ marginTop: '0.75rem' }}>
                {article.content[lang]}
              </div>

              <div className="content-section">
                <h3>{t('knowledge.keyTakeaways')}</h3>
                <ul>
                  {article.keyTakeaways.map((item, i) => (
                    <li key={i}>{item[lang]}</li>
                  ))}
                </ul>
              </div>

              <button
                className="btn btn-audio"
                onClick={() => handleListen(article.id, article.content[lang])}
              >
                {speaking && activeId === article.id
                  ? `⏹ ${t('recipes.stopAudio')}`
                  : `🔊 ${t('recipes.listenRecipe')}`}
              </button>
            </>
          )}
        </div>
      ))}
    </div>
  );
}
