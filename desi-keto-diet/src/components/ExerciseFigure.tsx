import type { ExerciseAnimation } from '../types';
import './ExerciseFigure.css';

interface Props {
  animation: ExerciseAnimation;
}

export default function ExerciseFigure({ animation }: Props) {
  return (
    <div className={`exercise-stage exercise-${animation}`} aria-hidden="true">
      <div className="stage-floor" />
      <svg viewBox="0 0 200 220" className="exercise-svg">
        <g className="figure-body">
          <circle className="fig-head" cx="100" cy="28" r="16" />
          <line className="fig-neck" x1="100" y1="44" x2="100" y2="54" />
          <line className="fig-torso" x1="100" y1="54" x2="100" y2="110" />
          <line className="fig-arm fig-arm-l" x1="100" y1="68" x2="68" y2="92" />
          <line className="fig-arm fig-arm-r" x1="100" y1="68" x2="132" y2="92" />
          <line className="fig-leg fig-leg-l" x1="100" y1="110" x2="78" y2="170" />
          <line className="fig-leg fig-leg-r" x1="100" y1="110" x2="122" y2="170" />
          <line className="fig-shin fig-shin-l" x1="78" y1="170" x2="72" y2="205" />
          <line className="fig-shin fig-shin-r" x1="122" y1="170" x2="128" y2="205" />
        </g>
        {animation === 'butterfly' && (
          <g className="pose-overlay butterfly-legs">
            <line x1="100" y1="110" x2="70" y2="150" strokeWidth="5" />
            <line x1="100" y1="110" x2="130" y2="150" strokeWidth="5" />
          </g>
        )}
        {animation === 'cobra' && (
          <g className="pose-overlay cobra-torso">
            <path d="M 85 110 Q 60 80 100 55" fill="none" strokeWidth="5" />
          </g>
        )}
        {animation === 'plank' && (
          <g className="pose-overlay plank-body">
            <line x1="50" y1="120" x2="150" y2="118" strokeWidth="6" />
          </g>
        )}
        {animation === 'burpee' && (
          <g className="pose-overlay burpee-jump">
            <circle cx="100" cy="15" r="4" className="motion-dot" />
          </g>
        )}
      </svg>
      <div className="motion-particles">
        <span className="particle p1" />
        <span className="particle p2" />
        <span className="particle p3" />
      </div>
    </div>
  );
}
