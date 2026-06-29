import type { Posture } from '../data/postures';
import { PostureIllustration } from './Illustrations';

interface PostureCardProps {
  posture: Posture;
  onClick: () => void;
}

export function PostureCard({ posture, onClick }: PostureCardProps) {
  return (
    <button className="posture-card" onClick={onClick} type="button">
      <div className="posture-card-illustration">
        <PostureIllustration type={posture.illustration} />
        <span className="video-badge">▶ ویڈیو</span>
      </div>
      <div className="posture-card-body">
        <h3>{posture.nameUrdu}</h3>
        <p className="posture-card-en">{posture.nameEnglish}</p>
        <div className="posture-card-meta">
          <span className="badge category">{posture.categoryUrdu}</span>
          <span className={`badge difficulty ${posture.difficulty === 'آسان' ? 'easy' : posture.difficulty === 'درمیانہ' ? 'medium' : 'hard'}`}>
            {posture.difficulty}
          </span>
        </div>
      </div>
    </button>
  );
}
