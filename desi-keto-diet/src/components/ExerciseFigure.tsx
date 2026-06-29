/**
 * ExerciseFigure — Classic instructional figurine style.
 *
 * Design language: clean geometric shapes, single green palette,
 * no skin tones or facial detail — like fitness-equipment instruction manuals.
 *
 * Four pose modes:
 *   standing — upright exercises (walk, squat, press, etc.)
 *   seated   — cross-legged floor (butterfly, breathe)
 *   prone    — face-down floor (plank, cobra, pushup, cat-cow)
 *   supine   — on-back floor (rest, hundred, roll-up, child-pose)
 *
 * CSS animations target the same class names (.fig-arm-l, .fig-leg-r, …)
 * so ExerciseFigure.css drives all movement without knowing the shape.
 */

import { useId } from 'react';
import type { ExerciseAnimation } from '../types';
import { HumanFigureDefs } from './HumanFigureDefs';
import './ExerciseFigure.css';

interface Props {
  animation: ExerciseAnimation;
  compact?: boolean;
}

type PoseMode = 'standing' | 'seated' | 'prone' | 'supine';

function getPoseMode(a: ExerciseAnimation): PoseMode {
  if (['butterfly', 'breathe'].includes(a)) return 'seated';
  if (['plank', 'mountain-climber', 'cobra', 'pushup', 'cat-cow'].includes(a)) return 'prone';
  if (['rest', 'hundred', 'roll-up', 'leg-stretch', 'child-pose'].includes(a)) return 'supine';
  return 'standing';
}

/* colours threaded into every sub-component */
interface C { body: string; limb: string; head: string; joint: string; out: string }

/* ── Classic head — plain circle, no facial features ───────────── */
function FigHead({ cx, cy, r = 16, c }: { cx: number; cy: number; r?: number; c: C }) {
  return (
    <g className="fig-head human-head">
      <circle cx={cx} cy={cy} r={r}
        fill={c.head} stroke={c.out} strokeWidth="1.5" />
      {/* subtle inner highlight — gives the ball-joint feel */}
      <circle cx={cx - r * 0.28} cy={cy - r * 0.3} r={r * 0.28}
        fill="rgba(255,255,255,0.22)" />
    </g>
  );
}

/* ── Figurine foot — simple elongated oval ─────────────────────── */
function FigFoot({ cx, cy }: { cx: number; cy: number; c: C }) {
  return <ellipse cx={cx} cy={cy} rx="11" ry="4.5" fill="rgba(45,106,79,0.8)" />;
}

/* ─────────────────────────────────────────────────────────────────
   STANDING (default) — upright classic figurine
   ───────────────────────────────────────────────────────────────── */
function StandingFig({ c, animation }: { c: C; animation: ExerciseAnimation }) {
  const J = c.joint; // joint ball colour shorthand
  return (
    <>
      {/* neck */}
      <rect className="fig-neck" x="93" y="37" width="14" height="14" rx="7"
        fill={c.body} stroke={c.out} strokeWidth="1" />

      {/* torso — tapered hourglass */}
      <path className="fig-torso human-torso"
        d="M 76 52 C 86 46 114 46 124 52
           L 122 82 L 124 118
           C 112 124 88 124 76 118
           L 78 82 Z"
        fill={c.body} stroke={c.out} strokeWidth="1.5" />

      {/* inner body highlight */}
      <ellipse cx="100" cy="85" rx="12" ry="18" fill="rgba(255,255,255,0.08)" />

      {/* hip block */}
      <path d="M 76 118 L 124 118 L 120 134 C 110 140 90 140 80 134 Z"
        fill={c.body} stroke={c.out} strokeWidth="1.5" />

      {/* ── shoulder joints ── */}
      <circle cx="78"  cy="54" r="7"   fill={J} stroke={c.out} strokeWidth="1" />
      <circle cx="122" cy="54" r="7"   fill={J} stroke={c.out} strokeWidth="1" />

      {/* ── left arm ── */}
      <g className="fig-arm-l">
        <path d="M 78 54 L 62 86"
          fill="none" stroke={c.limb} strokeWidth="13" strokeLinecap="round" />
        <circle cx="62" cy="86" r="6"  fill={J} stroke={c.out} strokeWidth="1" />
        <path d="M 62 86 L 52 113"
          fill="none" stroke={c.limb} strokeWidth="11" strokeLinecap="round" />
        <circle cx="50" cy="117" r="6" fill={J} stroke={c.out} strokeWidth="1" />
      </g>

      {/* ── right arm ── */}
      <g className="fig-arm-r">
        <path d="M 122 54 L 138 86"
          fill="none" stroke={c.limb} strokeWidth="13" strokeLinecap="round" />
        <circle cx="138" cy="86" r="6"  fill={J} stroke={c.out} strokeWidth="1" />
        <path d="M 138 86 L 148 113"
          fill="none" stroke={c.limb} strokeWidth="11" strokeLinecap="round" />
        <circle cx="150" cy="117" r="6" fill={J} stroke={c.out} strokeWidth="1" />
      </g>

      {/* ── hip joints ── */}
      <circle cx="87"  cy="130" r="7.5" fill={J} stroke={c.out} strokeWidth="1" />
      <circle cx="113" cy="130" r="7.5" fill={J} stroke={c.out} strokeWidth="1" />

      {/* ── left leg ── */}
      <g className="fig-leg-l">
        <path d="M 87 130 L 78 175"
          fill="none" stroke={c.limb} strokeWidth="14" strokeLinecap="round" />
        <circle cx="78" cy="175" r="6.5" fill={J} stroke={c.out} strokeWidth="1" />
      </g>
      <g className="fig-shin-l">
        <path d="M 78 175 L 70 214"
          fill="none" stroke={c.limb} strokeWidth="11" strokeLinecap="round" />
        <FigFoot cx={64} cy={217} c={c} />
      </g>

      {/* ── right leg ── */}
      <g className="fig-leg-r">
        <path d="M 113 130 L 122 175"
          fill="none" stroke={c.limb} strokeWidth="14" strokeLinecap="round" />
        <circle cx="122" cy="175" r="6.5" fill={J} stroke={c.out} strokeWidth="1" />
      </g>
      <g className="fig-shin-r">
        <path d="M 122 175 L 130 214"
          fill="none" stroke={c.limb} strokeWidth="11" strokeLinecap="round" />
        <FigFoot cx={136} cy={217} c={c} />
      </g>

      {/* butterfly leg overlay */}
      {animation === 'butterfly' && (
        <g className="pose-overlay butterfly-legs">
          <circle cx="100" cy="130" r="7.5" fill={J} stroke={c.out} strokeWidth="1" />
          <path d="M 100 130 L 62 162"
            fill="none" stroke={c.limb} strokeWidth="13" strokeLinecap="round" />
          <circle cx="62" cy="162" r="6" fill={J} stroke={c.out} strokeWidth="1" />
          <path d="M 62 162 L 52 180"
            fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
          <path d="M 100 130 L 138 162"
            fill="none" stroke={c.limb} strokeWidth="13" strokeLinecap="round" />
          <circle cx="138" cy="162" r="6" fill={J} stroke={c.out} strokeWidth="1" />
          <path d="M 138 162 L 148 180"
            fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
        </g>
      )}
    </>
  );
}

/* ─────────────────────────────────────────────────────────────────
   SEATED — cross-legged meditation / butterfly
   ───────────────────────────────────────────────────────────────── */
function SeatedFig({ c }: { c: C }) {
  const J = c.joint;
  return (
    <>
      {/* neck */}
      <rect className="fig-neck" x="93" y="54" width="14" height="13" rx="6.5"
        fill={c.body} stroke={c.out} strokeWidth="1" />

      {/* upright torso */}
      <path className="fig-torso human-torso"
        d="M 78 68 C 88 62 112 62 122 68
           L 120 92 L 122 128
           C 110 134 90 134 78 128
           L 80 92 Z"
        fill={c.body} stroke={c.out} strokeWidth="1.5" />
      <ellipse cx="100" cy="100" rx="11" ry="16" fill="rgba(255,255,255,0.07)" />

      {/* waist */}
      <path d="M 78 128 L 122 128 L 119 142 C 109 148 91 148 81 142 Z"
        fill={c.body} stroke={c.out} strokeWidth="1.5" />

      {/* shoulder joints */}
      <circle cx="80"  cy="70" r="7" fill={J} stroke={c.out} strokeWidth="1" />
      <circle cx="120" cy="70" r="7" fill={J} stroke={c.out} strokeWidth="1" />

      {/* left arm — resting on knee */}
      <g className="fig-arm-l">
        <path d="M 80 70 L 63 100"
          fill="none" stroke={c.limb} strokeWidth="12" strokeLinecap="round" />
        <circle cx="63" cy="100" r="5.5" fill={J} stroke={c.out} strokeWidth="1" />
        <path d="M 63 100 L 56 132"
          fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
        <circle cx="55" cy="136" r="5.5" fill={J} stroke={c.out} strokeWidth="1" />
      </g>

      {/* right arm — resting on knee */}
      <g className="fig-arm-r">
        <path d="M 120 70 L 137 100"
          fill="none" stroke={c.limb} strokeWidth="12" strokeLinecap="round" />
        <circle cx="137" cy="100" r="5.5" fill={J} stroke={c.out} strokeWidth="1" />
        <path d="M 137 100 L 144 132"
          fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
        <circle cx="145" cy="136" r="5.5" fill={J} stroke={c.out} strokeWidth="1" />
      </g>

      {/* hip joints */}
      <circle cx="87"  cy="142" r="7" fill={J} stroke={c.out} strokeWidth="1" />
      <circle cx="113" cy="142" r="7" fill={J} stroke={c.out} strokeWidth="1" />

      {/* cross-legged left leg */}
      <g className="fig-leg-l">
        <path d="M 87 142 L 55 170"
          fill="none" stroke={c.limb} strokeWidth="13" strokeLinecap="round" />
        <circle cx="55" cy="170" r="6" fill={J} stroke={c.out} strokeWidth="1" />
      </g>
      <g className="fig-shin-l">
        <path d="M 55 170 L 80 182"
          fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
        <ellipse cx="82" cy="184" rx="9" ry="4.5" fill="rgba(45,106,79,0.75)" />
      </g>

      {/* cross-legged right leg */}
      <g className="fig-leg-r">
        <path d="M 113 142 L 145 170"
          fill="none" stroke={c.limb} strokeWidth="13" strokeLinecap="round" />
        <circle cx="145" cy="170" r="6" fill={J} stroke={c.out} strokeWidth="1" />
      </g>
      <g className="fig-shin-r">
        <path d="M 145 170 L 120 182"
          fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
        <ellipse cx="118" cy="184" rx="9" ry="4.5" fill="rgba(45,106,79,0.75)" />
      </g>

      {/* yoga mat */}
      <rect x="38" y="188" width="124" height="8" rx="4"
        fill="rgba(82,183,136,0.28)" stroke="rgba(82,183,136,0.55)" strokeWidth="1" />
    </>
  );
}

/* ─────────────────────────────────────────────────────────────────
   PRONE — face-down horizontal (plank, pushup, cobra, cat-cow)
   ───────────────────────────────────────────────────────────────── */
function ProneFig({ c, animation }: { c: C; animation: ExerciseAnimation }) {
  const J  = c.joint;
  const GY = 197; // ground level

  const isPlank      = animation === 'plank' || animation === 'mountain-climber';
  const isPushup     = animation === 'pushup';
  const isCobra      = animation === 'cobra';
  const isCatCow     = animation === 'cat-cow';
  const bodyY        = isPushup ? 168 : 162; // body centerline Y

  return (
    <>
      {/* exercise mat */}
      <rect x="12" y={GY} width="178" height="9" rx="4.5"
        fill="rgba(82,183,136,0.28)" stroke="rgba(82,183,136,0.52)" strokeWidth="1" />

      {/* ── PLANK / MOUNTAIN-CLIMBER ── */}
      {(isPlank || isPushup) && (
        <>
          <FigHead cx={24} cy={bodyY - 6} r={13} c={c} />
          {/* neck */}
          <rect x="35" y={bodyY - 9} width="12" height="11" rx="5.5"
            fill={c.body} stroke={c.out} strokeWidth="1" />
          {/* horizontal torso */}
          <path className="fig-torso human-torso"
            d={`M 45 ${bodyY - 10} L 148 ${bodyY - 8}
                L 148 ${bodyY + 10} L 45 ${bodyY + 12} Z`}
            fill={c.body} stroke={c.out} strokeWidth="1.5" />
          {/* hips extension */}
          <path d={`M 148 ${bodyY - 8} L 178 ${bodyY - 4}
                    L 178 ${bodyY + 8} L 148 ${bodyY + 10} Z`}
            fill={c.body} stroke={c.out} strokeWidth="1.5" />

          {/* shoulder joints */}
          <circle cx="50" cy={bodyY} r="6.5" fill={J} stroke={c.out} strokeWidth="1" />
          <circle cx="88" cy={bodyY} r="6.5" fill={J} stroke={c.out} strokeWidth="1" />

          {/* support arms → hands on floor */}
          <g className="fig-arm-l">
            <path d={`M 50 ${bodyY} L 50 ${GY}`}
              fill="none" stroke={c.limb} strokeWidth="12" strokeLinecap="round" />
            <circle cx="50" cy={GY} r="6.5" fill={J} stroke={c.out} strokeWidth="1" />
          </g>
          <g className="fig-arm-r">
            <path d={`M 88 ${bodyY} L 88 ${GY}`}
              fill="none" stroke={c.limb} strokeWidth="12" strokeLinecap="round" />
            <circle cx="88" cy={GY} r="6.5" fill={J} stroke={c.out} strokeWidth="1" />
          </g>

          {/* hip joint */}
          <circle cx="155" cy={bodyY} r="6.5" fill={J} stroke={c.out} strokeWidth="1" />

          {/* legs → toes on floor */}
          <g className="fig-leg-l">
            <path d={`M 155 ${bodyY} L 164 ${bodyY + 5}`}
              fill="none" stroke={c.limb} strokeWidth="13" strokeLinecap="round" />
            <circle cx="164" cy={bodyY + 5} r="6" fill={J} stroke={c.out} strokeWidth="1" />
          </g>
          <g className="fig-shin-l">
            <path d={`M 164 ${bodyY + 5} L 172 ${GY}`}
              fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
            <ellipse cx="176" cy={GY} rx="8" ry="4" fill="rgba(45,106,79,0.8)" />
          </g>
          <g className="fig-leg-r">
            <path d={`M 155 ${bodyY} L 162 ${bodyY + 8}`}
              fill="none" stroke={c.limb} strokeWidth="13" strokeLinecap="round" />
            <circle cx="162" cy={bodyY + 8} r="6" fill={J} stroke={c.out} strokeWidth="1" />
          </g>
          <g className="fig-shin-r">
            <path d={`M 162 ${bodyY + 8} L 168 ${GY}`}
              fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
            <ellipse cx="172" cy={GY} rx="8" ry="4" fill="rgba(45,106,79,0.8)" />
          </g>
        </>
      )}

      {/* ── COBRA ── */}
      {isCobra && (
        <>
          {/* flat lower body */}
          <g className="fig-leg-l">
            <path d="M 105 185 L 148 192"
              fill="none" stroke={c.limb} strokeWidth="13" strokeLinecap="round" />
            <circle cx="148" cy="192" r="6" fill={J} stroke={c.out} strokeWidth="1" />
          </g>
          <g className="fig-shin-l">
            <path d="M 148 192 L 173 196"
              fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
            <ellipse cx="178" cy={GY} rx="7" ry="3.5" fill="rgba(45,106,79,0.8)" />
          </g>
          <g className="fig-leg-r">
            <path d="M 105 188 L 155 194"
              fill="none" stroke={c.limb} strokeWidth="13" strokeLinecap="round" />
            <circle cx="155" cy="194" r="6" fill={J} stroke={c.out} strokeWidth="1" />
          </g>
          <g className="fig-shin-r">
            <path d="M 155 194 L 182 198"
              fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
          </g>

          {/* hip/waist */}
          <ellipse cx="108" cy="185" rx="14" ry="7" fill={c.body} stroke={c.out} strokeWidth="1.5" />

          {/* arched torso rising from hips */}
          <path className="fig-torso human-torso"
            d="M 100 182 Q 72 158 50 136 Q 40 125 38 116
               L 46 110 Q 58 122 70 134 Q 90 152 108 176 Z"
            fill={c.body} stroke={c.out} strokeWidth="1.5" />

          {/* shoulder joints */}
          <circle cx="46" cy="112" r="6.5" fill={J} stroke={c.out} strokeWidth="1" />

          {/* pushing-up arms */}
          <g className="fig-arm-l">
            <path d="M 46 112 L 43 145"
              fill="none" stroke={c.limb} strokeWidth="12" strokeLinecap="round" />
            <circle cx="43" cy="145" r="5.5" fill={J} stroke={c.out} strokeWidth="1" />
            <path d="M 43 145 L 41 GY"
              fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
            <circle cx="41" cy={GY} r="6" fill={J} stroke={c.out} strokeWidth="1" />
          </g>
          <g className="fig-arm-r">
            <path d="M 66 138 L 63 168"
              fill="none" stroke={c.limb} strokeWidth="12" strokeLinecap="round" />
            <circle cx="63" cy="168" r="5.5" fill={J} stroke={c.out} strokeWidth="1" />
            <path d="M 63 168 L 61 197"
              fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
            <circle cx="61" cy={GY} r="6" fill={J} stroke={c.out} strokeWidth="1" />
          </g>

          {/* raised head */}
          <FigHead cx={34} cy={108} r={13} c={c} />
        </>
      )}

      {/* ── CAT-COW — on all fours ── */}
      {isCatCow && (
        <>
          <FigHead cx={26} cy={bodyY - 24} r={13} c={c} />
          {/* neck */}
          <path d={`M 38 ${bodyY - 16} L 52 ${bodyY}`}
            fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />

          {/* back / torso — arching shape driven by cat-cow animation */}
          <path className="fig-torso human-torso"
            d={`M 52 ${bodyY - 8} Q 100 ${bodyY - 20} 142 ${bodyY - 6}
                L 142 ${bodyY + 10} Q 100 ${bodyY + 22} 52 ${bodyY + 8} Z`}
            fill={c.body} stroke={c.out} strokeWidth="1.5" />

          {/* hip block */}
          <ellipse cx="142" cy={bodyY} rx="12" ry="10" fill={c.body} stroke={c.out} strokeWidth="1.5" />

          {/* front shoulder joints */}
          <circle cx="57" cy={bodyY} r="6.5" fill={J} stroke={c.out} strokeWidth="1" />
          <circle cx="80" cy={bodyY} r="6.5" fill={J} stroke={c.out} strokeWidth="1" />

          {/* front arms → hands on floor */}
          <g className="fig-arm-l">
            <path d={`M 57 ${bodyY} L 55 ${GY}`}
              fill="none" stroke={c.limb} strokeWidth="12" strokeLinecap="round" />
            <circle cx="55" cy={GY} r="6.5" fill={J} stroke={c.out} strokeWidth="1" />
          </g>
          <g className="fig-arm-r">
            <path d={`M 80 ${bodyY} L 78 ${GY}`}
              fill="none" stroke={c.limb} strokeWidth="12" strokeLinecap="round" />
            <circle cx="78" cy={GY} r="6.5" fill={J} stroke={c.out} strokeWidth="1" />
          </g>

          {/* back knee joints */}
          <circle cx="146" cy={bodyY} r="6.5" fill={J} stroke={c.out} strokeWidth="1" />
          <circle cx="158" cy={bodyY + 2} r="6.5" fill={J} stroke={c.out} strokeWidth="1" />

          {/* back legs → knees on floor */}
          <g className="fig-leg-l">
            <path d={`M 146 ${bodyY} L 148 ${GY}`}
              fill="none" stroke={c.limb} strokeWidth="13" strokeLinecap="round" />
            <circle cx="148" cy={GY} r="6.5" fill={J} stroke={c.out} strokeWidth="1" />
          </g>
          <g className="fig-leg-r">
            <path d={`M 158 ${bodyY + 2} L 161 ${GY}`}
              fill="none" stroke={c.limb} strokeWidth="13" strokeLinecap="round" />
            <circle cx="161" cy={GY} r="6.5" fill={J} stroke={c.out} strokeWidth="1" />
          </g>
        </>
      )}
    </>
  );
}

/* ─────────────────────────────────────────────────────────────────
   SUPINE — on-back horizontal (rest, hundred, roll-up, child-pose)
   ───────────────────────────────────────────────────────────────── */
function SupineFig({ c, animation }: { c: C; animation: ExerciseAnimation }) {
  const J  = c.joint;
  const GY = 200;
  const BY = 173; // body centre Y
  const isChild = animation === 'child-pose';

  if (isChild) {
    /* child pose: kneeling, curled forward */
    return (
      <>
        <rect x="18" y={GY} width="166" height="9" rx="4.5"
          fill="rgba(82,183,136,0.28)" stroke="rgba(82,183,136,0.52)" strokeWidth="1" />
        <FigHead cx={34} cy={BY - 12} r={13} c={c} />
        {/* curved back */}
        <path className="fig-torso human-torso"
          d="M 44 170 Q 70 152 100 150 Q 130 148 148 156
             L 148 167 Q 130 160 100 162 Q 70 165 44 182 Z"
          fill={c.body} stroke={c.out} strokeWidth="1.5" />
        {/* hip block */}
        <path d="M 148 156 L 168 160 L 168 171 L 148 167 Z"
          fill={c.body} stroke={c.out} strokeWidth="1.5" />
        {/* arms stretched forward */}
        <g className="fig-arm-l">
          <path d="M 60 168 L 38 174"
            fill="none" stroke={c.limb} strokeWidth="12" strokeLinecap="round" />
          <circle cx="38" cy="174" r="5.5" fill={J} stroke={c.out} strokeWidth="1" />
          <path d="M 38 174 L 22 177"
            fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
          <circle cx="18" cy="179" r="6" fill={J} stroke={c.out} strokeWidth="1" />
        </g>
        <g className="fig-arm-r">
          <path d="M 66 166 L 46 171"
            fill="none" stroke={c.limb} strokeWidth="12" strokeLinecap="round" />
          <circle cx="46" cy="171" r="5.5" fill={J} stroke={c.out} strokeWidth="1" />
          <path d="M 46 171 L 30 174"
            fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
          <circle cx="26" cy="176" r="6" fill={J} stroke={c.out} strokeWidth="1" />
        </g>
        {/* shins on floor */}
        <g className="fig-leg-l">
          <path d="M 148 159 L 155 200"
            fill="none" stroke={c.limb} strokeWidth="13" strokeLinecap="round" />
          <circle cx="155" cy={GY} r="6" fill={J} stroke={c.out} strokeWidth="1" />
        </g>
        <g className="fig-shin-l">
          <path d="M 155 200 L 168 200"
            fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
        </g>
        <g className="fig-leg-r">
          <path d="M 154 163 L 162 200"
            fill="none" stroke={c.limb} strokeWidth="13" strokeLinecap="round" />
          <circle cx="162" cy={GY} r="6" fill={J} stroke={c.out} strokeWidth="1" />
        </g>
        <g className="fig-shin-r">
          <path d="M 162 200 L 178 200"
            fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
        </g>
      </>
    );
  }

  /* default supine — lying on back, head left */
  return (
    <>
      {/* mat */}
      <rect x="8" y={GY - 5} width="184" height="9" rx="4.5"
        fill="rgba(82,183,136,0.28)" stroke="rgba(82,183,136,0.52)" strokeWidth="1" />

      <FigHead cx={22} cy={BY - 3} r={13} c={c} />

      {/* neck */}
      <rect x="33" y={BY - 7} width="11" height="11" rx="5.5"
        fill={c.body} stroke={c.out} strokeWidth="1" />

      {/* horizontal torso */}
      <path className="fig-torso human-torso"
        d={`M 42 ${BY - 10} L 145 ${BY - 8} L 145 ${BY + 10} L 42 ${BY + 12} Z`}
        fill={c.body} stroke={c.out} strokeWidth="1.5" />

      {/* hip/legs block */}
      <path d={`M 145 ${BY - 8} L 178 ${BY - 5} L 178 ${BY + 8} L 145 ${BY + 10} Z`}
        fill={c.body} stroke={c.out} strokeWidth="1.5" />

      {/* shoulder joint */}
      <circle cx="56" cy={BY} r="6.5" fill={J} stroke={c.out} strokeWidth="1" />

      {/* arms loosely at sides */}
      <g className="fig-arm-l">
        <path d={`M 56 ${BY + 2} L 57 ${GY - 5}`}
          fill="none" stroke={c.limb} strokeWidth="12" strokeLinecap="round" />
        <circle cx="57" cy={GY - 5} r="5.5" fill={J} stroke={c.out} strokeWidth="1" />
        <path d={`M 57 ${GY - 5} L 55 ${GY + 2}`}
          fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
      </g>
      <g className="fig-arm-r">
        <path d={`M 76 ${BY - 2} L 78 ${GY - 5}`}
          fill="none" stroke={c.limb} strokeWidth="12" strokeLinecap="round" />
        <circle cx="78" cy={GY - 5} r="5.5" fill={J} stroke={c.out} strokeWidth="1" />
        <path d={`M 78 ${GY - 5} L 76 ${GY + 2}`}
          fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
      </g>

      {/* hip joints */}
      <circle cx="145" cy={BY} r="6.5" fill={J} stroke={c.out} strokeWidth="1" />

      {/* legs */}
      <g className="fig-leg-l">
        <path d={`M 145 ${BY} L 162 ${BY + 2}`}
          fill="none" stroke={c.limb} strokeWidth="13" strokeLinecap="round" />
        <circle cx="162" cy={BY + 2} r="6" fill={J} stroke={c.out} strokeWidth="1" />
      </g>
      <g className="fig-shin-l">
        <path d={`M 162 ${BY + 2} L 180 ${BY + 4}`}
          fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
        <ellipse cx="186" cy={BY + 5} rx="10" ry="4" fill="rgba(45,106,79,0.8)" />
      </g>
      <g className="fig-leg-r">
        <path d={`M 145 ${BY + 5} L 160 ${BY + 7}`}
          fill="none" stroke={c.limb} strokeWidth="13" strokeLinecap="round" />
        <circle cx="160" cy={BY + 7} r="6" fill={J} stroke={c.out} strokeWidth="1" />
      </g>
      <g className="fig-shin-r">
        <path d={`M 160 ${BY + 7} L 178 ${BY + 9}`}
          fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
        <ellipse cx="184" cy={BY + 10} rx="10" ry="4" fill="rgba(45,106,79,0.8)" />
      </g>

      {/* hundred: legs lifted */}
      {animation === 'hundred' && (
        <g style={{ transformOrigin: '145px 173px' }}>
          <path d={`M 145 ${BY} L 163 ${BY - 20}`}
            fill="none" stroke={c.limb} strokeWidth="13" strokeLinecap="round" />
          <circle cx="163" cy={BY - 20} r="6" fill={J} stroke={c.out} strokeWidth="1" />
          <path d={`M 163 ${BY - 20} L 181 ${BY - 18}`}
            fill="none" stroke={c.limb} strokeWidth="10" strokeLinecap="round" />
        </g>
      )}
    </>
  );
}

/* ═══════════════════════════════════════════════════════════════
   Main exported component
   ═══════════════════════════════════════════════════════════════ */
export default function ExerciseFigure({ animation, compact = false }: Props) {
  const rawId = useId();
  const p = `hf${rawId.replace(/[^a-zA-Z0-9]/g, '')}`;

  const c: C = {
    body:  `url(#${p}-body)`,
    limb:  `url(#${p}-limb)`,
    head:  `url(#${p}-head)`,
    joint: `url(#${p}-joint)`,
    out:   'rgba(27,67,50,0.6)',
  };

  const mode     = getPoseMode(animation);
  const isSeated = mode === 'seated';
  const isProne  = mode === 'prone';
  const isSupine = mode === 'supine';

  const headCy = isSeated ? 40 : 22;
  const headR  = isSeated ? 15 : 16;

  return (
    <div
      className={`exercise-stage exercise-${animation}${compact ? ' exercise-stage-compact' : ''}`}
      aria-hidden="true"
    >
      <div className="stage-floor" />
      <div className="stage-glow" />

      <svg viewBox="0 0 200 240" className="exercise-svg">
        <HumanFigureDefs prefix={p} />

        {/* ambient ground glow */}
        <ellipse cx="100" cy="198" rx="85" ry="48" fill={`url(#${p}-glow)`} />

        {/* cast shadow */}
        <ellipse
          className="human-shadow"
          cx="100"
          cy={isProne || isSupine ? 207 : 228}
          rx={isProne || isSupine ? 82 : 38}
          ry={isProne || isSupine ? 7  : 7}
        />

        {/* ── figure group (CSS animations target children) ── */}
        <g
          className={[
            'figure-body human-figure',
            isSeated ? 'human-seated' : '',
            isProne  ? 'human-prone'  : '',
            isSupine ? 'human-supine' : '',
          ].join(' ').trim()}
          filter={`url(#${p}-shadow)`}
        >
          {/* head drawn here for standing + seated; floor poses include their own */}
          {!isProne && !isSupine && (
            <FigHead cx={100} cy={headCy} r={headR} c={c} />
          )}

          {mode === 'standing' && <StandingFig c={c} animation={animation} />}
          {mode === 'seated'   && <SeatedFig   c={c} />}
          {mode === 'prone'    && <ProneFig    c={c} animation={animation} />}
          {mode === 'supine'   && <SupineFig   c={c} animation={animation} />}
        </g>

        {/* energy sparks for explosive moves */}
        {(animation === 'burpee' || animation === 'jumping-jack') && (
          <>
            <circle cx="100" cy="8"  r="5.5" className="motion-dot"    filter={`url(#${p}-glow-f)`} />
            <circle cx="84"  cy="15" r="3.5" className="motion-dot-sm" />
            <circle cx="116" cy="15" r="3.5" className="motion-dot-sm" />
          </>
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
