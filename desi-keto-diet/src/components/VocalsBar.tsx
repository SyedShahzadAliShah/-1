import { useTranslation } from 'react-i18next';
import { useVocals } from '../context/VocalsContext';
import './VocalsBar.css';

export default function VocalsBar() {
  const { t } = useTranslation();
  const { speaking, currentTitle, error, stop } = useVocals();

  if (!speaking && !error) return null;

  return (
    <div className="vocals-bar" role="region" aria-live="polite">
      <div className="vocals-bar-inner">
        <span className="vocals-bar-icon" aria-hidden="true">
          {speaking ? '🔊' : '⚠️'}
        </span>
        <div className="vocals-bar-text">
          <span className="vocals-bar-label">
            {speaking ? currentTitle || '…' : error}
          </span>
        </div>
        {speaking && (
          <button
            type="button"
            className="vocals-bar-stop"
            onClick={() => void stop()}
            aria-label={t('recipes.stopAudio')}
          >
            ⏹
          </button>
        )}
      </div>
    </div>
  );
}
