import type { ExerciseAnimation } from '../types';
import './ExerciseFigure.css';

interface Props {
  animation: ExerciseAnimation;
}

/** Articulated human figure — limb groups keep legacy class names for CSS animations */
export default function ExerciseFigure({ animation }: Props) {
  const isSeated = ['butterfly', 'breathe', 'rest', 'knee-lift', 'ankle-circle'].includes(animation);
  const isFloor = ['cobra', 'cat-cow', 'child-pose', 'plank', 'mountain-climber', 'hundred', 'leg-stretch'].includes(animation);

  return (
    <div className={`exercise-stage exercise-${animation}`} aria-hidden="true">
      <div className="stage-floor" />
      {isSeated && <rect className="human-mat" x="55" y="175" width="90" height="8" rx="4" />}

      <svg viewBox="0 0 200 230" className="exercise-svg">
        <defs>
          <linearGradient id="skinGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stopColor="#e8b88a" />
            <stop offset="100%" stopColor="#c9956b" />
          </linearGradient>
          <linearGradient id="shirtGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stopColor="#52b788" />
            <stop offset="100%" stopColor="#2d6a4f" />
          </linearGradient>
          <linearGradient id="shortsGrad" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stopColor="#40916c" />
            <stop offset="100%" stopColor="#1b4332" />
          </linearGradient>
        </defs>

        <ellipse className="human-shadow" cx="100" cy="215" rx="34" ry="6" />

        <g className={`figure-body human-figure ${isFloor ? 'human-floor' : ''} ${isSeated ? 'human-seated' : ''}`}>
          {/* ── Head ── */}
          <g className="fig-head human-head">
            <ellipse className="human-skull" cx="100" cy="27" rx="16" ry="19" />
            <path
              className="human-hair"
              d="M 82 22 C 82 8 118 8 118 22 C 120 32 115 40 100 42 C 85 40 80 32 82 22 Z"
            />
            <ellipse className="human-face" cx="100" cy="29" rx="13" ry="15" />
            <circle className="human-eye" cx="93" cy="27" r="2.2" />
            <circle className="human-eye" cx="107" cy="27" r="2.2" />
            <circle className="human-eye-shine" cx="93.8" cy="26.2" r="0.7" />
            <circle className="human-eye-shine" cx="107.8" cy="26.2" r="0.7" />
            <path className="human-brow" d="M 89 23 Q 93 21 97 23" />
            <path className="human-brow" d="M 103 23 Q 107 21 111 23" />
            <path className="human-smile" d="M 93 34 Q 100 38 107 34" />
          </g>

          {/* ── Neck ── */}
          <rect className="fig-neck human-neck" x="93" y="44" width="14" height="11" rx="5" />

          {/* ── Torso (shirt) ── */}
          <path
            className="fig-torso human-torso"
            d="M 76 55 C 88 50 112 50 124 55 L 122 72 L 124 108
               C 112 114 88 114 76 108 L 78 72 Z"
          />
          <path className="human-collar" d="M 88 55 Q 100 62 112 55" />

          {/* ── Shorts ── */}
          <path
            className="human-shorts"
            d="M 76 108 L 124 108 L 122 126 C 112 130 88 130 78 126 Z"
          />

          {/* ── Left arm ── */}
          <g className="fig-arm-l human-limb">
            <path className="human-upper-arm" d="M 86 58 L 68 82" />
            <path className="human-forearm" d="M 68 82 L 58 104" />
            <ellipse className="human-hand" cx="56" cy="108" rx="6" ry="5" />
          </g>

          {/* ── Right arm ── */}
          <g className="fig-arm-r human-limb">
            <path className="human-upper-arm" d="M 114 58 L 132 82" />
            <path className="human-forearm" d="M 132 82 L 142 104" />
            <ellipse className="human-hand" cx="144" cy="108" rx="6" ry="5" />
          </g>

          {/* ── Left leg ── */}
          <g className="fig-leg-l human-limb">
            <path className="human-thigh" d="M 88 126 L 78 170" />
          </g>
          <g className="fig-shin-l human-limb">
            <path className="human-calf" d="M 78 170 L 70 202" />
            <ellipse className="human-foot" cx="64" cy="206" rx="12" ry="5" />
            <path className="human-shoe" d="M 52 206 L 76 206 L 74 210 L 54 210 Z" />
          </g>

          {/* ── Right leg ── */}
          <g className="fig-leg-r human-limb">
            <path className="human-thigh" d="M 112 126 L 122 170" />
          </g>
          <g className="fig-shin-r human-limb">
            <path className="human-calf" d="M 122 170 L 130 202" />
            <ellipse className="human-foot" cx="136" cy="206" rx="12" ry="5" />
            <path className="human-shoe" d="M 124 206 L 148 206 L 146 210 L 126 210 Z" />
          </g>
        </g>

        {/* Pose-specific overlays */}
        {animation === 'butterfly' && (
          <g className="pose-overlay butterfly-legs">
            <path className="human-thigh butterfly-leg" d="M 100 128 L 68 158" />
            <path className="human-thigh butterfly-leg" d="M 100 128 L 132 158" />
            <path className="human-calf butterfly-leg" d="M 68 158 L 58 175" />
            <path className="human-calf butterfly-leg" d="M 132 158 L 142 175" />
          </g>
        )}

        {animation === 'cobra' && (
          <g className="pose-overlay cobra-pose">
            <path className="cobra-torso" d="M 80 195 Q 55 150 95 120 Q 100 115 105 120" />
            <g className="fig-head human-head cobra-head">
              <ellipse className="human-skull" cx="108" cy="118" rx="14" ry="16" />
              <ellipse className="human-face" cx="108" cy="120" rx="11" ry="13" />
            </g>
          </g>
        )}

        {animation === 'plank' && (
          <g className="pose-overlay plank-pose">
            <path className="plank-body" d="M 40 125 L 160 123" />
          </g>
        )}

        {animation === 'burpee' && (
          <circle cx="100" cy="12" r="5" className="motion-dot" />
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
