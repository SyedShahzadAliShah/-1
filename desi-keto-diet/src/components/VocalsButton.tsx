import { useTranslation } from 'react-i18next';
import { useVocals } from '../context/VocalsContext';
import type { Language } from '../types';
import './VocalsButton.css';

interface Props {
  text: string;
  title?: string;
  language?: Language;
  id?: string;
  compact?: boolean;
  className?: string;
}

export default function VocalsButton({
  text,
  title,
  language,
  id,
  compact = false,
  className = '',
}: Props) {
  const { t } = useTranslation();
  const { speaking, activeId, prefs, toggle, clearError } = useVocals();
  const itemId = id ?? text.slice(0, 80);
  const isActive = speaking && activeId === itemId;

  if (!prefs.enabled) return null;

  const handleClick = (e: React.MouseEvent) => {
    e.preventDefault();
    e.stopPropagation();
    clearError();
    void toggle({ text, title, language, id: itemId });
  };

  return (
    <button
      type="button"
      className={`vocals-btn ${compact ? 'vocals-btn-compact' : ''} ${className}`.trim()}
      onClick={handleClick}
      aria-label={isActive ? t('recipes.stopAudio') : t('vocals.listen')}
      title={isActive ? t('recipes.stopAudio') : t('vocals.listen')}
    >
      {isActive ? '⏹' : '🔊'}
      {!compact && (
        <span className="vocals-btn-label">
          {isActive ? t('recipes.stopAudio') : t('vocals.listen')}
        </span>
      )}
    </button>
  );
}
