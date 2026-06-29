import { useId } from 'react';
import type { ExerciseAnimation } from '../types';
import { HumanFigureDefs } from './HumanFigureDefs';
import './ExerciseFigure.css';

interface Props {
  animation: ExerciseAnimation;
  compact?: boolean;
}

/** Articulated athletic human figure with pose-specific overlays */
export default function ExerciseFigure({ animation, compact = false }: Props) {
  const rawId = useId();
  const prefix = `hf${rawId.replace(/:/g, '')}`;
  const skin = `url(#${prefix}-skin)`;
  const skinLimb = `url(#${prefix}-skin-limb)`;
  const tank = `url(#${prefix}-tank)`;
  const leggings = `url(#${prefix}-leggings)`;
  const shoe = `url(#${prefix}-shoe)`;
  const hair = `url(#${prefix}-hair)`;

  const isSeated = ['butterfly', 'breathe', 'rest', 'knee-lift', 'ankle-circle'].includes(animation);
  const isFloor = ['cobra', 'cat-cow', 'child-pose', 'plank', 'mountain-climber', 'hundred', 'leg-stretch', 'pushup'].includes(animation);

  return (
    <div
      className={`exercise-stage exercise-${animation}${compact ? ' exercise-stage-compact' : ''}`}
      aria-hidden="true"
    >
      <div className="stage-floor" />
      <div className="stage-glow" />

      <svg viewBox="0 0 200 240" className="exercise-svg">
        <HumanFigureDefs prefix={prefix} />

        <ellipse className="ambient-glow" cx="100" cy="185" rx="70" ry="45" fill={`url(#${prefix}-glow)`} />

        {isSeated && (
          <rect className="human-mat" x="48" y="178" width="104" height="10" rx="5" />
        )}

        <ellipse className="human-shadow" cx="100" cy="220" rx="36" ry="7" />

        <g
          className={`figure-body human-figure ${isFloor ? 'human-floor' : ''} ${isSeated ? 'human-seated' : ''}`}
          filter={`url(#${prefix}-soft)`}
        >
          {/* Head */}
          <g className="fig-head human-head">
            <ellipse className="human-neck-back" cx="100" cy="46" rx="9" ry="7" fill={skin} />
            <ellipse className="human-skull" cx="100" cy="28" rx="17" ry="20" fill={skin} />
            <path
              className="human-hair"
              fill={hair}
              d="M 80 20 C 78 6 122 6 120 20 C 123 34 118 44 100 46 C 82 44 77 34 80 20 Z"
            />
            <path
              className="human-ponytail"
              fill={hair}
              d="M 115 24 C 128 28 132 42 126 58 C 122 48 118 38 114 32 Z"
            />
            <ellipse className="human-face" cx="100" cy="30" rx="14" ry="16" fill={skin} />
            <ellipse className="human-ear" cx="84" cy="30" rx="3" ry="4.5" fill={skin} />
            <ellipse className="human-ear" cx="116" cy="30" rx="3" ry="4.5" fill={skin} />
            <path className="human-headband" d="M 84 18 Q 100 14 116 18 L 115 24 Q 100 20 85 24 Z" fill="#40916c" />
            <ellipse className="human-cheek" cx="90" cy="34" rx="4" ry="2.5" opacity="0.35" fill="#e8a090" />
            <ellipse className="human-cheek" cx="110" cy="34" rx="4" ry="2.5" opacity="0.35" fill="#e8a090" />
            <ellipse className="human-eye-white" cx="93" cy="28" rx="3.5" ry="3" fill="#fff" />
            <ellipse className="human-eye-white" cx="107" cy="28" rx="3.5" ry="3" fill="#fff" />
            <circle className="human-eye" cx="93" cy="28" r="2" fill="#1a2e1a" />
            <circle className="human-eye" cx="107" cy="28" r="2" fill="#1a2e1a" />
            <circle className="human-eye-shine" cx="93.8" cy="27.2" r="0.8" fill="#fff" />
            <circle className="human-eye-shine" cx="107.8" cy="27.2" r="0.8" fill="#fff" />
            <path className="human-brow" d="M 88 23 Q 93 20 97 23" />
            <path className="human-brow" d="M 103 23 Q 107 20 112 23" />
            <path className="human-nose" d="M 100 30 L 99 34 L 101 34 Z" fill="#c9956b" opacity="0.6" />
            <path className="human-smile" d="M 92 36 Q 100 40 108 36" />
          </g>

          <rect className="fig-neck human-neck" x="92" y="44" width="16" height="12" rx="6" fill={skin} />

          {/* Torso — athletic tank */}
          <path
            className="fig-torso human-torso"
            fill={tank}
            d="M 74 56 C 88 50 112 50 126 56 L 124 74 L 126 108
               C 112 116 88 116 74 108 L 76 74 Z"
          />
          <path className="human-tank-strap-l" d="M 76 56 L 82 108" stroke="rgba(255,255,255,0.2)" strokeWidth="2" />
          <path className="human-tank-strap-r" d="M 124 56 L 118 108" stroke="rgba(255,255,255,0.2)" strokeWidth="2" />
          <ellipse className="human-abs" cx="100" cy="95" rx="8" ry="5" fill="rgba(255,255,255,0.08)" />

          {/* Leggings */}
          <path
            className="human-leggings"
            fill={leggings}
            d="M 74 108 L 126 108 L 123 128 C 112 132 88 132 77 128 Z"
          />

          {/* Left arm */}
          <g className="fig-arm-l human-limb">
            <circle className="human-joint" cx="86" cy="58" r="5" fill={skin} />
            <path className="human-upper-arm" d="M 86 58 L 66 84" stroke={skinLimb} />
            <circle className="human-joint" cx="66" cy="84" r="4.5" fill={skin} />
            <path className="human-forearm" d="M 66 84 L 54 108" stroke={skinLimb} />
            <ellipse className="human-hand" cx="52" cy="112" rx="7" ry="5.5" fill={skin} />
          </g>

          {/* Right arm */}
          <g className="fig-arm-r human-limb">
            <circle className="human-joint" cx="114" cy="58" r="5" fill={skin} />
            <path className="human-upper-arm" d="M 114 58 L 134 84" stroke={skinLimb} />
            <circle className="human-joint" cx="134" cy="84" r="4.5" fill={skin} />
            <path className="human-forearm" d="M 134 84 L 146 108" stroke={skinLimb} />
            <ellipse className="human-hand" cx="148" cy="112" rx="7" ry="5.5" fill={skin} />
          </g>

          {/* Left leg */}
          <g className="fig-leg-l human-limb">
            <circle className="human-joint" cx="88" cy="128" r="5.5" fill={skin} />
            <path className="human-thigh" d="M 88 128 L 76 172" stroke={skinLimb} />
          </g>
          <g className="fig-shin-l human-limb">
            <circle className="human-joint" cx="76" cy="172" r="4.5" fill={skin} />
            <path className="human-calf" d="M 76 172 L 68 206" stroke={skinLimb} />
            <ellipse className="human-foot" cx="62" cy="210" rx="13" ry="5.5" fill={skin} />
            <path className="human-shoe" fill={shoe} d="M 48 210 L 76 210 L 74 216 L 50 216 Z" />
            <rect className="human-sole" x="50" y="214" width="24" height="3" rx="1" fill="#0f1a0f" />
          </g>

          {/* Right leg */}
          <g className="fig-leg-r human-limb">
            <circle className="human-joint" cx="112" cy="128" r="5.5" fill={skin} />
            <path className="human-thigh" d="M 112 128 L 124 172" stroke={skinLimb} />
          </g>
          <g className="fig-shin-r human-limb">
            <circle className="human-joint" cx="124" cy="172" r="4.5" fill={skin} />
            <path className="human-calf" d="M 124 172 L 132 206" stroke={skinLimb} />
            <ellipse className="human-foot" cx="138" cy="210" rx="13" ry="5.5" fill={skin} />
            <path className="human-shoe" fill={shoe} d="M 124 210 L 152 210 L 150 216 L 126 216 Z" />
            <rect className="human-sole" x="126" y="214" width="24" height="3" rx="1" fill="#0f1a0f" />
          </g>
        </g>

        {/* Pose overlays */}
        {animation === 'butterfly' && (
          <g className="pose-overlay butterfly-legs">
            <path className="human-thigh butterfly-leg" d="M 100 130 L 64 162" stroke={skinLimb} />
            <path className="human-thigh butterfly-leg" d="M 100 130 L 136 162" stroke={skinLimb} />
            <path className="human-calf butterfly-leg" d="M 64 162 L 54 178" stroke={skinLimb} />
            <path className="human-calf butterfly-leg" d="M 136 162 L 146 178" stroke={skinLimb} />
          </g>
        )}

        {animation === 'cobra' && (
          <g className="pose-overlay cobra-pose" filter={`url(#${prefix}-soft)`}>
            <path className="cobra-torso" d="M 78 198 Q 50 148 92 118 Q 100 112 108 118" stroke={skinLimb} />
            <g className="fig-head human-head cobra-head">
              <ellipse className="human-skull" cx="110" cy="116" rx="15" ry="17" fill={skin} />
              <ellipse className="human-face" cx="110" cy="118" rx="12" ry="14" fill={skin} />
              <circle className="human-eye" cx="106" cy="116" r="1.8" fill="#1a2e1a" />
              <circle className="human-eye" cx="114" cy="116" r="1.8" fill="#1a2e1a" />
            </g>
          </g>
        )}

        {(animation === 'plank' || animation === 'mountain-climber') && (
          <g className="pose-overlay plank-pose" filter={`url(#${prefix}-soft)`}>
            <ellipse className="plank-head" cx="42" cy="118" rx="12" ry="14" fill={skin} />
            <path className="plank-body" d="M 52 120 L 158 118" stroke={tank} />
            <path className="plank-arm" d="M 52 120 L 48 145" stroke={skinLimb} />
            <path className="plank-leg" d="M 158 118 L 168 145" stroke={skinLimb} />
            <path className="plank-leg" d="M 158 118 L 148 145" stroke={skinLimb} />
          </g>
        )}

        {animation === 'pushup' && (
          <g className="pose-overlay pushup-pose" filter={`url(#${prefix}-soft)`}>
            <ellipse className="pushup-head" cx="55" cy="145" rx="11" ry="13" fill={skin} />
            <path className="pushup-torso-line" d="M 64 148 L 140 140" stroke={tank} />
            <path className="pushup-arm" d="M 64 148 L 58 168" stroke={skinLimb} />
            <path className="pushup-arm" d="M 140 140 L 148 168" stroke={skinLimb} />
          </g>
        )}

        {animation === 'child-pose' && (
          <g className="pose-overlay child-pose-overlay" filter={`url(#${prefix}-soft)`}>
            <ellipse className="child-head" cx="88" cy="168" rx="14" ry="16" fill={skin} />
            <path className="child-back" d="M 98 172 Q 130 155 145 175" stroke={tank} />
            <path className="child-arms" d="M 98 175 L 70 185" stroke={skinLimb} />
            <path className="child-arms" d="M 98 175 L 125 188" stroke={skinLimb} />
          </g>
        )}

        {animation === 'burpee' && (
          <circle cx="100" cy="10" r="6" className="motion-dot" filter={`url(#${prefix}-glow-filter)`} />
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
