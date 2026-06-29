/**
 * ExerciseFigure — Female fitness model illustrations.
 *
 * Illustrated SVG female figures with:
 *   • Warm South-Asian skin tones
 *   • Dark hair in high ponytail
 *   • Emerald sports crop-top + forest leggings
 *   • Feminine proportions (narrow shoulders, defined waist, curved hips)
 *   • Expressive face: almond eyes, arched brows, full lips
 *
 * Four pose modes share all CSS animation class names so
 * ExerciseFigure.css drives all movement without layout knowledge.
 */

import { useId } from 'react';
import type { ExerciseAnimation } from '../types';
import { HumanFigureDefs } from './HumanFigureDefs';
import './ExerciseFigure.css';

interface Props { animation: ExerciseAnimation; compact?: boolean }

type PoseMode = 'standing' | 'seated' | 'prone' | 'supine';

function getPoseMode(a: ExerciseAnimation): PoseMode {
  if (['butterfly', 'breathe'].includes(a))                                    return 'seated';
  if (['plank', 'mountain-climber', 'cobra', 'pushup', 'cat-cow'].includes(a)) return 'prone';
  if (['rest', 'hundred', 'roll-up', 'leg-stretch', 'child-pose'].includes(a)) return 'supine';
  return 'standing';
}

/** Colour bundle threaded into every pose component */
interface FC {
  skin: string; slim: string; hair: string;
  top: string;  leg:  string; shoe: string;
}

/* ═══════════════════════════════════════════════════════════════
   FEMALE HEAD  — used by standing & seated (floor poses inline)
   ═══════════════════════════════════════════════════════════════ */
function FemaleHead({
  cx, cy, rx = 14, ry = 16, c,
}: { cx: number; cy: number; rx?: number; ry?: number; c: FC }) {
  const fx = cx, fy = cy + 2;
  return (
    <g className="fig-head human-head">
      {/* hair behind skull */}
      <ellipse cx={cx} cy={cy - 1} rx={rx + 1.5} ry={ry + 2}    fill={c.hair} />
      {/* skull */}
      <ellipse cx={cx}  cy={cy}     rx={rx}        ry={ry}        fill={c.skin} />
      {/* hair top cap */}
      <path fill={c.hair}
        d={`M ${cx - rx + 1} ${cy - ry * 0.45}
            C ${cx - rx - 1} ${cy - ry - 7} ${cx + rx + 1} ${cy - ry - 7} ${cx + rx - 1} ${cy - ry * 0.45}
            C ${cx + rx + 2} ${cy - ry * 0.05} ${cx + rx - 1} ${cy + ry * 0.6} ${cx} ${cy + ry + 1}
            C ${cx - rx + 1} ${cy + ry * 0.6} ${cx - rx - 2} ${cy - ry * 0.05} ${cx - rx + 1} ${cy - ry * 0.45} Z`}
      />
      {/* high ponytail */}
      <path fill={c.hair}
        d={`M ${cx + rx - 4} ${cy - ry * 0.35}
            C ${cx + rx + 8} ${cy - ry * 0.1} ${cx + rx + 14} ${cy + ry * 0.55} ${cx + rx + 8} ${cy + ry + 10}
            C ${cx + rx + 3} ${cy + ry * 0.3} ${cx + rx - 1} ${cy + ry * 0.1} ${cx + rx - 4} ${cy - ry * 0.35} Z`}
      />
      {/* hair tie dot */}
      <circle cx={cx + rx + 5} cy={cy - 1} r="2.2" fill="#2d6a4f" />
      {/* face */}
      <ellipse cx={fx} cy={fy}  rx={rx - 2.5} ry={ry - 2}   fill={c.skin} />
      {/* ears */}
      <ellipse cx={cx - rx + 1} cy={fy} rx="2.8" ry="4"     fill={c.skin} />
      <ellipse cx={cx + rx - 1} cy={fy} rx="2.8" ry="4"     fill={c.skin} />
      {/* blush */}
      <ellipse cx={fx - 6} cy={fy + 6} rx="4" ry="2.5" fill="#e89898" opacity="0.32" />
      <ellipse cx={fx + 6} cy={fy + 6} rx="4" ry="2.5" fill="#e89898" opacity="0.32" />
      {/* eyebrows — arched, feminine */}
      <path d={`M ${fx - 10} ${fy - 4} Q ${fx - 6} ${fy - 7} ${fx - 2} ${fy - 4}`}
        fill="none" stroke="#3a2210" strokeWidth="1.8" strokeLinecap="round" />
      <path d={`M ${fx + 2}  ${fy - 4} Q ${fx + 6} ${fy - 7} ${fx + 10} ${fy - 4}`}
        fill="none" stroke="#3a2210" strokeWidth="1.8" strokeLinecap="round" />
      {/* eyes — almond, white sclera */}
      <ellipse cx={fx - 6} cy={fy - 1} rx="4.2" ry="3.2" fill="#fff" />
      <ellipse cx={fx + 6} cy={fy - 1} rx="4.2" ry="3.2" fill="#fff" />
      <circle  cx={fx - 6} cy={fy - 1} r="2.3"            fill="#1c1410" />
      <circle  cx={fx + 6} cy={fy - 1} r="2.3"            fill="#1c1410" />
      <circle  cx={fx - 5.1} cy={fy - 1.9} r="0.85"       fill="#fff"    />
      <circle  cx={fx + 6.9} cy={fy - 1.9} r="0.85"       fill="#fff"    />
      {/* upper lashes — short strokes */}
      {[-10.5,-8.5,-6.5].map((dx, i) => (
        <line key={i}
          x1={fx + dx} y1={fy - 3.8} x2={fx + dx - 0.4} y2={fy - 5.5}
          stroke="#1c1410" strokeWidth="1.1" strokeLinecap="round" />
      ))}
      {[2.5,4.5,6.5].map((dx, i) => (
        <line key={i + 3}
          x1={fx + dx} y1={fy - 3.8} x2={fx + dx + 0.4} y2={fy - 5.5}
          stroke="#1c1410" strokeWidth="1.1" strokeLinecap="round" />
      ))}
      {/* nose */}
      <path d={`M ${fx} ${fy + 2} L ${fx - 2} ${fy + 6} Q ${fx} ${fy + 7} ${fx + 2} ${fy + 6} L ${fx} ${fy + 2}`}
        fill="#c0844a" opacity="0.5" />
      {/* lips — fuller */}
      <path d={`M ${fx - 6} ${fy + 10} Q ${fx} ${fy + 8} ${fx + 6} ${fy + 10}`}
        fill="none" stroke="#c86060" strokeWidth="1.6" strokeLinecap="round" />
      <path d={`M ${fx - 6} ${fy + 10} Q ${fx} ${fy + 14} ${fx + 6} ${fy + 10}`}
        fill="#c07070" opacity="0.72" />
    </g>
  );
}

/* helper: sport shoe */
function FShoe({ x, y, dir = 1, c }: { x: number; y: number; dir?: 1 | -1; c: FC }) {
  const tip = x + dir * 15, back = x - dir * 9;
  return (
    <>
      <ellipse cx={x + dir * 2} cy={y}     rx="14" ry="5"  fill={c.skin} />
      <path    d={`M ${back} ${y} L ${tip} ${y} L ${tip - dir * 2} ${y + 7} L ${back + dir * 2} ${y + 7} Z`}
        fill={c.shoe} />
      <rect x={Math.min(back + dir * 2, tip - dir * 4)} y={y + 6}
        width="19" height="3" rx="1.5" fill="rgba(30,60,40,0.8)" />
    </>
  );
}

/* ═══════════════════════════════════════════════════════════════
   STANDING female model
   ═══════════════════════════════════════════════════════════════ */
function StandingFemale({ c, animation }: { c: FC; animation: ExerciseAnimation }) {
  const S = c.slim; // skin stroke shorthand
  return (
    <>
      {/* neck — slender */}
      <rect className="fig-neck" x="93" y="40" width="14" height="14" rx="7"
        fill={c.skin} stroke="rgba(180,120,60,0.4)" strokeWidth="0.8" />

      {/* ── SPORTS CROP TOP ── */}
      <path className="fig-torso human-torso" fill={c.top}
        d="M 82 54 C 90 47 110 47 118 54
           L 116 78 C 108 83 92 83 84 78 L 82 54 Z" />
      {/* chest highlight */}
      <ellipse cx="100" cy="63" rx="10" ry="8" fill="rgba(255,255,255,0.1)" />

      {/* ── TORSO WAIST — feminine curve ── */}
      <path fill={c.leg}
        d="M 84 78 C 80 88 78 98 82 110
           C 82 114 82 116 84 118
           L 116 118
           C 118 116 118 114 118 110
           C 122 98 120 88 116 78
           L 84 78 Z" />
      {/* waist highlight */}
      <ellipse cx="100" cy="96" rx="9" ry="12" fill="rgba(255,255,255,0.06)" />

      {/* ── LEGGINGS WAISTBAND & HIP ── */}
      <path fill={c.leg}
        d="M 82 118 L 118 118 L 115 134 C 106 140 94 140 85 134 Z"
        stroke="rgba(82,183,136,0.35)" strokeWidth="1" />

      {/* shoulder joints */}
      <circle cx="84"  cy="56" r="5.5" fill={c.skin} />
      <circle cx="116" cy="56" r="5.5" fill={c.skin} />

      {/* ── left arm ── */}
      <g className="fig-arm-l">
        <path d="M 84 56 L 68 86"  fill="none" stroke={S} strokeWidth="11" strokeLinecap="round" />
        <circle cx="68" cy="86"   r="4.8" fill={c.skin} />
        <path d="M 68 86 L 58 112" fill="none" stroke={S} strokeWidth="9"  strokeLinecap="round" />
        <ellipse cx="56" cy="116" rx="6.5" ry="5" fill={c.skin} />
      </g>

      {/* ── right arm ── */}
      <g className="fig-arm-r">
        <path d="M 116 56 L 132 86"  fill="none" stroke={S} strokeWidth="11" strokeLinecap="round" />
        <circle cx="132" cy="86"     r="4.8" fill={c.skin} />
        <path d="M 132 86 L 142 112" fill="none" stroke={S} strokeWidth="9"  strokeLinecap="round" />
        <ellipse cx="144" cy="116"   rx="6.5" ry="5" fill={c.skin} />
      </g>

      {/* hip joints */}
      <circle cx="86"  cy="130" r="6.5" fill={c.skin} stroke="rgba(180,120,60,0.3)" strokeWidth="0.8" />
      <circle cx="114" cy="130" r="6.5" fill={c.skin} stroke="rgba(180,120,60,0.3)" strokeWidth="0.8" />

      {/* ── left leg ── */}
      <g className="fig-leg-l">
        <path d="M 86 130 L 77 174"  fill="none" stroke={c.leg} strokeWidth="14" strokeLinecap="round" />
        <circle cx="77" cy="174" r="6" fill={c.skin} />
      </g>
      <g className="fig-shin-l">
        <path d="M 77 174 L 70 213"  fill="none" stroke={c.leg} strokeWidth="11" strokeLinecap="round" />
        <FShoe x={64} y={216} dir={-1} c={c} />
      </g>

      {/* ── right leg ── */}
      <g className="fig-leg-r">
        <path d="M 114 130 L 123 174" fill="none" stroke={c.leg} strokeWidth="14" strokeLinecap="round" />
        <circle cx="123" cy="174" r="6" fill={c.skin} />
      </g>
      <g className="fig-shin-r">
        <path d="M 123 174 L 130 213" fill="none" stroke={c.leg} strokeWidth="11" strokeLinecap="round" />
        <FShoe x={136} y={216} dir={1} c={c} />
      </g>

      {/* butterfly leg overlay */}
      {animation === 'butterfly' && (
        <g className="pose-overlay butterfly-legs">
          <path d="M 100 130 L 61 161" fill="none" stroke={c.leg} strokeWidth="13" strokeLinecap="round" />
          <circle cx="61" cy="161" r="5.5" fill={c.skin} />
          <path d="M 61 161 L 51 179" fill="none" stroke={c.leg} strokeWidth="10" strokeLinecap="round" />
          <path d="M 100 130 L 139 161" fill="none" stroke={c.leg} strokeWidth="13" strokeLinecap="round" />
          <circle cx="139" cy="161" r="5.5" fill={c.skin} />
          <path d="M 139 161 L 149 179" fill="none" stroke={c.leg} strokeWidth="10" strokeLinecap="round" />
        </g>
      )}
    </>
  );
}

/* ═══════════════════════════════════════════════════════════════
   SEATED female model  — cross-legged (butterfly, breathe)
   ═══════════════════════════════════════════════════════════════ */
function SeatedFemale({ c }: { c: FC }) {
  const S = c.slim;
  return (
    <>
      {/* neck */}
      <rect className="fig-neck" x="93" y="55" width="14" height="13" rx="6.5"
        fill={c.skin} stroke="rgba(180,120,60,0.35)" strokeWidth="0.8" />

      {/* crop top — upright */}
      <path className="fig-torso human-torso" fill={c.top}
        d="M 82 68 C 90 62 110 62 118 68 L 116 90 C 108 96 92 96 84 90 L 82 68 Z" />
      <ellipse cx="100" cy="77" rx="10" ry="8" fill="rgba(255,255,255,0.1)" />

      {/* waist/torso continuation */}
      <path fill={c.leg}
        d="M 84 90 C 80 100 80 108 82 116
           C 82 120 82 124 84 126
           L 116 126
           C 118 124 118 120 118 116
           C 120 108 120 100 116 90
           L 84 90 Z" />
      <ellipse cx="100" cy="108" rx="9" ry="12" fill="rgba(255,255,255,0.06)" />

      {/* waistband */}
      <path fill={c.leg}
        d="M 82 126 L 118 126 L 115 140 C 107 146 93 146 85 140 Z"
        stroke="rgba(82,183,136,0.35)" strokeWidth="1" />

      {/* shoulder joints */}
      <circle cx="84"  cy="70" r="5.5" fill={c.skin} />
      <circle cx="116" cy="70" r="5.5" fill={c.skin} />

      {/* left arm resting on knee */}
      <g className="fig-arm-l">
        <path d="M 84 70 L 67 98"   fill="none" stroke={S} strokeWidth="11" strokeLinecap="round" />
        <circle cx="67" cy="98"     r="4.5" fill={c.skin} />
        <path d="M 67 98 L 59 130"  fill="none" stroke={S} strokeWidth="9"  strokeLinecap="round" />
        <circle cx="58" cy="134"    r="5"   fill={c.skin} />
      </g>

      {/* right arm resting on knee */}
      <g className="fig-arm-r">
        <path d="M 116 70 L 133 98"  fill="none" stroke={S} strokeWidth="11" strokeLinecap="round" />
        <circle cx="133" cy="98"     r="4.5" fill={c.skin} />
        <path d="M 133 98 L 141 130" fill="none" stroke={S} strokeWidth="9"  strokeLinecap="round" />
        <circle cx="142" cy="134"    r="5"   fill={c.skin} />
      </g>

      {/* cross-legged left */}
      <g className="fig-leg-l">
        <path d="M 86 140 L 54 168"  fill="none" stroke={c.leg} strokeWidth="13" strokeLinecap="round" />
        <circle cx="54" cy="168" r="5.5" fill={c.skin} />
      </g>
      <g className="fig-shin-l">
        <path d="M 54 168 L 80 181"  fill="none" stroke={c.leg} strokeWidth="10" strokeLinecap="round" />
        <ellipse cx="82" cy="183" rx="9" ry="4.5" fill={c.skin} />
      </g>

      {/* cross-legged right */}
      <g className="fig-leg-r">
        <path d="M 114 140 L 146 168" fill="none" stroke={c.leg} strokeWidth="13" strokeLinecap="round" />
        <circle cx="146" cy="168" r="5.5" fill={c.skin} />
      </g>
      <g className="fig-shin-r">
        <path d="M 146 168 L 120 181" fill="none" stroke={c.leg} strokeWidth="10" strokeLinecap="round" />
        <ellipse cx="118" cy="183" rx="9" ry="4.5" fill={c.skin} />
      </g>

      {/* yoga mat */}
      <rect x="36" y="186" width="128" height="8" rx="4"
        fill="rgba(82,183,136,0.3)" stroke="rgba(82,183,136,0.55)" strokeWidth="1" />
    </>
  );
}

/* ═══════════════════════════════════════════════════════════════
   PRONE female model  — face-down horizontal
   (plank, mountain-climber, pushup, cobra, cat-cow)
   ═══════════════════════════════════════════════════════════════ */
function ProneFemale({ c, animation }: { c: FC; animation: ExerciseAnimation }) {
  const S   = c.slim;
  const GY  = 196;
  const BY  = animation === 'pushup' ? 168 : 162;
  const isPlank = animation === 'plank' || animation === 'mountain-climber';
  const isPushup = animation === 'pushup';
  const isCobra  = animation === 'cobra';
  const isCatCow = animation === 'cat-cow';

  /* ── inline head for floor poses ── */
  function FloorHead({ hx, hy, hr = 12 }: { hx: number; hy: number; hr?: number }) {
    const fx = hx, fy = hy + 1;
    return (
      <g className="fig-head human-head">
        <ellipse cx={hx} cy={hy - 1} rx={hr + 1} ry={hr + 2} fill={c.hair} />
        <ellipse cx={hx} cy={hy}     rx={hr}      ry={hr + 1} fill={c.skin} />
        <path fill={c.hair}
          d={`M ${hx - hr} ${hy - hr * 0.3}
              C ${hx - hr - 1} ${hy - hr - 5} ${hx + hr + 1} ${hy - hr - 5} ${hx + hr} ${hy - hr * 0.3}
              C ${hx + hr + 2} ${hy - hr * 0.1} ${hx + hr - 1} ${hy + hr * 0.55} ${hx} ${hy + hr}
              C ${hx - hr + 1} ${hy + hr * 0.55} ${hx - hr - 2} ${hy - hr * 0.1} ${hx - hr} ${hy - hr * 0.3} Z`}
        />
        <ellipse cx={fx} cy={fy}  rx={hr - 2}   ry={hr - 1} fill={c.skin} />
        <circle  cx={fx - 5}  cy={fy - 1} r="2"  fill="#1c1410" />
        <circle  cx={fx + 5}  cy={fy - 1} r="2"  fill="#1c1410" />
        <circle  cx={fx - 4.3} cy={fy - 1.6} r="0.7" fill="#fff" />
        <circle  cx={fx + 5.7} cy={fy - 1.6} r="0.7" fill="#fff" />
        <path d={`M ${fx - 7} ${fy - 3.5} Q ${fx - 5} ${fy - 5.5} ${fx - 2} ${fy - 3.5}`}
          fill="none" stroke="#3a2210" strokeWidth="1.5" strokeLinecap="round" />
        <path d={`M ${fx + 2} ${fy - 3.5} Q ${fx + 5} ${fy - 5.5} ${fx + 7} ${fy - 3.5}`}
          fill="none" stroke="#3a2210" strokeWidth="1.5" strokeLinecap="round" />
        <path d={`M ${fx - 4} ${fy + 7} Q ${fx} ${fy + 10} ${fx + 4} ${fy + 7}`}
          fill="none" stroke="#c06060" strokeWidth="1.4" strokeLinecap="round" />
      </g>
    );
  }

  return (
    <>
      {/* exercise mat */}
      <rect x="10" y={GY} width="180" height="9" rx="4.5"
        fill="rgba(82,183,136,0.28)" stroke="rgba(82,183,136,0.52)" strokeWidth="1" />

      {/* ── PLANK / PUSHUP ── */}
      {(isPlank || isPushup) && (
        <>
          <FloorHead hx={24} hy={BY - 6} />
          {/* neck */}
          <rect x="35" y={BY - 9} width="12" height="11" rx="5.5"
            fill={c.skin} stroke="rgba(180,120,60,0.35)" strokeWidth="0.8" />
          {/* torso — crop top horizontal */}
          <path className="fig-torso human-torso" fill={c.top}
            d={`M 45 ${BY - 10} L 120 ${BY - 8} L 120 ${BY + 8} L 45 ${BY + 10} Z`} />
          {/* hip — leggings horizontal */}
          <path fill={c.leg}
            d={`M 120 ${BY - 8} L 178 ${BY - 4} L 178 ${BY + 7} L 120 ${BY + 8} Z`} />

          {/* support arms */}
          <g className="fig-arm-l">
            <path d={`M 52 ${BY} L 52 ${GY}`}    fill="none" stroke={S} strokeWidth="11" strokeLinecap="round" />
            <circle cx="52" cy={GY} r="6" fill={c.skin} />
          </g>
          <g className="fig-arm-r">
            <path d={`M 86 ${BY} L 86 ${GY}`}    fill="none" stroke={S} strokeWidth="11" strokeLinecap="round" />
            <circle cx="86" cy={GY} r="6" fill={c.skin} />
          </g>

          {/* hip joint */}
          <circle cx="152" cy={BY} r="6" fill={c.skin} />

          {/* legs → toes */}
          <g className="fig-leg-l">
            <path d={`M 152 ${BY} L 164 ${BY + 5}`}   fill="none" stroke={c.leg} strokeWidth="13" strokeLinecap="round" />
            <circle cx="164" cy={BY + 5} r="5.5" fill={c.skin} />
          </g>
          <g className="fig-shin-l">
            <path d={`M 164 ${BY + 5} L 172 ${GY}`}   fill="none" stroke={c.leg} strokeWidth="10" strokeLinecap="round" />
            <ellipse cx="176" cy={GY} rx="8" ry="4" fill={c.skin} />
          </g>
          <g className="fig-leg-r">
            <path d={`M 152 ${BY} L 162 ${BY + 8}`}   fill="none" stroke={c.leg} strokeWidth="13" strokeLinecap="round" />
            <circle cx="162" cy={BY + 8} r="5.5" fill={c.skin} />
          </g>
          <g className="fig-shin-r">
            <path d={`M 162 ${BY + 8} L 168 ${GY}`}   fill="none" stroke={c.leg} strokeWidth="10" strokeLinecap="round" />
            <ellipse cx="172" cy={GY} rx="8" ry="4" fill={c.skin} />
          </g>
        </>
      )}

      {/* ── COBRA ── */}
      {isCobra && (
        <>
          {/* flat lower body */}
          <g className="fig-leg-l">
            <path d="M 106 184 L 148 191" fill="none" stroke={c.leg} strokeWidth="13" strokeLinecap="round" />
            <circle cx="148" cy="191" r="5.5" fill={c.skin} />
          </g>
          <g className="fig-shin-l">
            <path d="M 148 191 L 174 196" fill="none" stroke={c.leg} strokeWidth="10" strokeLinecap="round" />
          </g>
          <g className="fig-leg-r">
            <path d="M 106 187 L 156 193" fill="none" stroke={c.leg} strokeWidth="13" strokeLinecap="round" />
            <circle cx="156" cy="193" r="5.5" fill={c.skin} />
          </g>
          <g className="fig-shin-r">
            <path d="M 156 193 L 182 197" fill="none" stroke={c.leg} strokeWidth="10" strokeLinecap="round" />
          </g>
          {/* hip oval */}
          <ellipse cx="108" cy="183" rx="14" ry="7" fill={c.leg} stroke="rgba(82,183,136,0.35)" strokeWidth="1" />
          {/* arching torso */}
          <path className="fig-torso human-torso" fill={c.top}
            d="M 100 180 Q 72 156 50 134 Q 40 124 38 114
               L 46 108 Q 60 120 72 132 Q 90 150 108 174 Z" />
          {/* shoulder joint */}
          <circle cx="45" cy="110" r="6" fill={c.skin} />
          {/* pushing arms */}
          <g className="fig-arm-l">
            <path d="M 45 110 L 43 144" fill="none" stroke={S} strokeWidth="11" strokeLinecap="round" />
            <circle cx="43" cy="144" r="5" fill={c.skin} />
            <path d="M 43 144 L 41 196" fill="none" stroke={S} strokeWidth="9"  strokeLinecap="round" />
            <circle cx="41" cy={GY}     r="5.5" fill={c.skin} />
          </g>
          <g className="fig-arm-r">
            <path d="M 66 136 L 63 168" fill="none" stroke={S} strokeWidth="11" strokeLinecap="round" />
            <circle cx="63" cy="168" r="5" fill={c.skin} />
            <path d="M 63 168 L 62 196" fill="none" stroke={S} strokeWidth="9"  strokeLinecap="round" />
            <circle cx="62" cy={GY}     r="5.5" fill={c.skin} />
          </g>
          {/* raised head */}
          <FloorHead hx={34} hy={108} hr={12} />
        </>
      )}

      {/* ── CAT-COW (all fours) ── */}
      {isCatCow && (
        <>
          <FloorHead hx={24} hy={BY - 24} hr={12} />
          {/* neck */}
          <path d={`M 36 ${BY - 16} L 50 ${BY}`}
            fill="none" stroke={S} strokeWidth="9" strokeLinecap="round" />
          {/* back / torso */}
          <path className="fig-torso human-torso" fill={c.top}
            d={`M 50 ${BY - 8} Q 100 ${BY - 20} 142 ${BY - 6}
                L 142 ${BY + 9} Q 100 ${BY + 21} 50 ${BY + 7} Z`} />
          {/* hip */}
          <ellipse cx="142" cy={BY} rx="12" ry="10" fill={c.leg} />
          {/* front shoulder joints */}
          <circle cx="56" cy={BY} r="6" fill={c.skin} />
          <circle cx="80" cy={BY} r="6" fill={c.skin} />
          {/* front arms */}
          <g className="fig-arm-l">
            <path d={`M 56 ${BY} L 54 ${GY}`}  fill="none" stroke={S} strokeWidth="11" strokeLinecap="round" />
            <circle cx="54" cy={GY} r="6" fill={c.skin} />
          </g>
          <g className="fig-arm-r">
            <path d={`M 80 ${BY} L 78 ${GY}`}  fill="none" stroke={S} strokeWidth="11" strokeLinecap="round" />
            <circle cx="78" cy={GY} r="6" fill={c.skin} />
          </g>
          {/* back knee joints */}
          <circle cx="146" cy={BY} r="6" fill={c.skin} />
          <circle cx="158" cy={BY + 2} r="6" fill={c.skin} />
          <g className="fig-leg-l">
            <path d={`M 146 ${BY} L 148 ${GY}`}    fill="none" stroke={c.leg} strokeWidth="13" strokeLinecap="round" />
            <circle cx="148" cy={GY} r="6" fill={c.skin} />
          </g>
          <g className="fig-leg-r">
            <path d={`M 158 ${BY + 2} L 161 ${GY}`} fill="none" stroke={c.leg} strokeWidth="13" strokeLinecap="round" />
            <circle cx="161" cy={GY} r="6" fill={c.skin} />
          </g>
        </>
      )}
    </>
  );
}

/* ═══════════════════════════════════════════════════════════════
   SUPINE female model  — lying on back
   (rest, hundred, roll-up, leg-stretch, child-pose)
   ═══════════════════════════════════════════════════════════════ */
function SupineFemale({ c, animation }: { c: FC; animation: ExerciseAnimation }) {
  const S  = c.slim;
  const GY = 199;
  const BY = 172;
  const isChild = animation === 'child-pose';

  /* inline compact head for floor lying */
  function LyingHead({ hx, hy, hr = 12 }: { hx: number; hy: number; hr?: number }) {
    const fx = hx, fy = hy + 1;
    return (
      <g className="fig-head human-head">
        <ellipse cx={hx} cy={hy - 1} rx={hr + 1} ry={hr + 2} fill={c.hair} />
        <ellipse cx={hx} cy={hy}     rx={hr}      ry={hr + 1} fill={c.skin} />
        <path fill={c.hair}
          d={`M ${hx - hr} ${hy - hr * 0.3}
              C ${hx - hr - 1} ${hy - hr - 5} ${hx + hr + 1} ${hy - hr - 5} ${hx + hr} ${hy - hr * 0.3}
              C ${hx + hr + 2} ${hy - hr * 0.1} ${hx + hr - 1} ${hy + hr * 0.55} ${hx} ${hy + hr}
              C ${hx - hr + 1} ${hy + hr * 0.55} ${hx - hr - 2} ${hy - hr * 0.1} ${hx - hr} ${hy - hr * 0.3} Z`}
        />
        <ellipse cx={fx} cy={fy}  rx={hr - 2}   ry={hr - 1} fill={c.skin} />
        <circle  cx={fx - 5}   cy={fy - 1} r="2"   fill="#1c1410" />
        <circle  cx={fx + 5}   cy={fy - 1} r="2"   fill="#1c1410" />
        <circle  cx={fx - 4.2} cy={fy - 1.6} r="0.7" fill="#fff" />
        <circle  cx={fx + 5.8} cy={fy - 1.6} r="0.7" fill="#fff" />
        <path d={`M ${fx - 4} ${fy + 7} Q ${fx} ${fy + 10} ${fx + 4} ${fy + 7}`}
          fill="none" stroke="#c06060" strokeWidth="1.3" strokeLinecap="round" />
      </g>
    );
  }

  if (isChild) {
    return (
      <>
        <rect x="16" y={GY} width="170" height="9" rx="4.5"
          fill="rgba(82,183,136,0.28)" stroke="rgba(82,183,136,0.52)" strokeWidth="1" />
        <LyingHead hx={33} hy={BY - 12} hr={12} />
        {/* curved back */}
        <path className="fig-torso human-torso" fill={c.top}
          d="M 42 170 Q 70 152 100 150 Q 130 148 148 156
             L 148 167 Q 130 160 100 162 Q 70 165 42 182 Z" />
        <path fill={c.leg}
          d="M 148 156 L 168 160 L 168 171 L 148 167 Z" />
        {/* arms stretched forward */}
        <g className="fig-arm-l">
          <path d="M 58 168 L 37 174" fill="none" stroke={S} strokeWidth="11" strokeLinecap="round" />
          <circle cx="37" cy="174" r="5" fill={c.skin} />
          <path d="M 37 174 L 21 177" fill="none" stroke={S} strokeWidth="9"  strokeLinecap="round" />
          <circle cx="17" cy="179" r="5.5" fill={c.skin} />
        </g>
        <g className="fig-arm-r">
          <path d="M 64 166 L 44 171" fill="none" stroke={S} strokeWidth="11" strokeLinecap="round" />
          <circle cx="44" cy="171" r="5" fill={c.skin} />
          <path d="M 44 171 L 28 174" fill="none" stroke={S} strokeWidth="9"  strokeLinecap="round" />
          <circle cx="24" cy="176" r="5.5" fill={c.skin} />
        </g>
        <g className="fig-leg-l">
          <path d="M 148 159 L 155 199" fill="none" stroke={c.leg} strokeWidth="13" strokeLinecap="round" />
          <circle cx="155" cy={GY} r="6" fill={c.skin} />
        </g>
        <g className="fig-shin-l">
          <path d="M 155 199 L 168 199" fill="none" stroke={c.leg} strokeWidth="10" strokeLinecap="round" />
        </g>
        <g className="fig-leg-r">
          <path d="M 154 163 L 162 199" fill="none" stroke={c.leg} strokeWidth="13" strokeLinecap="round" />
          <circle cx="162" cy={GY} r="6" fill={c.skin} />
        </g>
        <g className="fig-shin-r">
          <path d="M 162 199 L 178 199" fill="none" stroke={c.leg} strokeWidth="10" strokeLinecap="round" />
        </g>
      </>
    );
  }

  /* supine — lying on back, head at left */
  return (
    <>
      <rect x="8" y={GY - 5} width="186" height="9" rx="4.5"
        fill="rgba(82,183,136,0.28)" stroke="rgba(82,183,136,0.52)" strokeWidth="1" />

      <LyingHead hx={22} hy={BY - 3} hr={12} />

      {/* neck */}
      <rect x="33" y={BY - 7} width="11" height="11" rx="5.5"
        fill={c.skin} stroke="rgba(180,120,60,0.35)" strokeWidth="0.8" />

      {/* torso horizontal — crop top section */}
      <path className="fig-torso human-torso" fill={c.top}
        d={`M 42 ${BY - 10} L 120 ${BY - 8} L 120 ${BY + 8} L 42 ${BY + 10} Z`} />
      {/* hip — leggings section */}
      <path fill={c.leg}
        d={`M 120 ${BY - 8} L 178 ${BY - 5} L 178 ${BY + 7} L 120 ${BY + 8} Z`} />

      {/* shoulder joint */}
      <circle cx="55" cy={BY} r="6" fill={c.skin} />

      {/* arms at side */}
      <g className="fig-arm-l">
        <path d={`M 55 ${BY + 2} L 56 ${GY - 5}`}
          fill="none" stroke={S} strokeWidth="11" strokeLinecap="round" />
        <circle cx="56" cy={GY - 5} r="5" fill={c.skin} />
        <path d={`M 56 ${GY - 5} L 54 ${GY + 2}`}
          fill="none" stroke={S} strokeWidth="9" strokeLinecap="round" />
      </g>
      <g className="fig-arm-r">
        <path d={`M 75 ${BY - 2} L 76 ${GY - 5}`}
          fill="none" stroke={S} strokeWidth="11" strokeLinecap="round" />
        <circle cx="76" cy={GY - 5} r="5" fill={c.skin} />
        <path d={`M 76 ${GY - 5} L 74 ${GY + 2}`}
          fill="none" stroke={S} strokeWidth="9" strokeLinecap="round" />
      </g>

      {/* hip joint */}
      <circle cx="144" cy={BY} r="6" fill={c.skin} />

      {/* legs extended */}
      <g className="fig-leg-l">
        <path d={`M 144 ${BY} L 162 ${BY + 2}`}
          fill="none" stroke={c.leg} strokeWidth="13" strokeLinecap="round" />
        <circle cx="162" cy={BY + 2} r="5.5" fill={c.skin} />
      </g>
      <g className="fig-shin-l">
        <path d={`M 162 ${BY + 2} L 181 ${BY + 4}`}
          fill="none" stroke={c.leg} strokeWidth="10" strokeLinecap="round" />
        <ellipse cx="187" cy={BY + 5} rx="10" ry="4" fill={c.skin} />
      </g>
      <g className="fig-leg-r">
        <path d={`M 144 ${BY + 5} L 160 ${BY + 7}`}
          fill="none" stroke={c.leg} strokeWidth="13" strokeLinecap="round" />
        <circle cx="160" cy={BY + 7} r="5.5" fill={c.skin} />
      </g>
      <g className="fig-shin-r">
        <path d={`M 160 ${BY + 7} L 179 ${BY + 9}`}
          fill="none" stroke={c.leg} strokeWidth="10" strokeLinecap="round" />
        <ellipse cx="185" cy={BY + 10} rx="10" ry="4" fill={c.skin} />
      </g>

      {/* hundred: legs lifted */}
      {animation === 'hundred' && (
        <>
          <path d={`M 144 ${BY} L 163 ${BY - 22}`}
            fill="none" stroke={c.leg} strokeWidth="13" strokeLinecap="round" />
          <circle cx="163" cy={BY - 22} r="5.5" fill={c.skin} />
          <path d={`M 163 ${BY - 22} L 182 ${BY - 20}`}
            fill="none" stroke={c.leg} strokeWidth="10" strokeLinecap="round" />
        </>
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

  const c: FC = {
    skin: `url(#${p}-skin)`,
    slim: `url(#${p}-slim)`,
    hair: `url(#${p}-hair)`,
    top:  `url(#${p}-top)`,
    leg:  `url(#${p}-leg)`,
    shoe: `url(#${p}-shoe)`,
  };

  const mode     = getPoseMode(animation);
  const isSeated = mode === 'seated';
  const isProne  = mode === 'prone';
  const isSupine = mode === 'supine';

  /* head position for standing / seated (floor poses include their own head) */
  const headCy = isSeated ? 40 : 22;
  const headRx = isSeated ? 13 : 14;
  const headRy = isSeated ? 15 : 16;

  return (
    <div
      className={`exercise-stage exercise-${animation}${compact ? ' exercise-stage-compact' : ''}`}
      aria-hidden="true"
    >
      <div className="stage-floor" />
      <div className="stage-glow" />

      <svg viewBox="0 0 200 240" className="exercise-svg">
        <HumanFigureDefs prefix={p} />

        {/* ambient floor glow */}
        <ellipse cx="100" cy="200" rx="86" ry="50" fill={`url(#${p}-glow)`} />

        {/* cast shadow */}
        <ellipse
          className="human-shadow"
          cx="100"
          cy={isProne || isSupine ? 208 : 228}
          rx={isProne || isSupine ? 82 : 36}
          ry={7}
        />

        <g
          className={[
            'figure-body human-figure',
            isSeated ? 'human-seated' : '',
            isProne  ? 'human-prone'  : '',
            isSupine ? 'human-supine' : '',
          ].join(' ').trim()}
          filter={`url(#${p}-shadow)`}
        >
          {/* head rendered here for upright poses; floor poses include their own */}
          {!isProne && !isSupine && (
            <FemaleHead cx={100} cy={headCy} rx={headRx} ry={headRy} c={c} />
          )}

          {mode === 'standing' && <StandingFemale c={c} animation={animation} />}
          {mode === 'seated'   && <SeatedFemale   c={c} />}
          {mode === 'prone'    && <ProneFemale    c={c} animation={animation} />}
          {mode === 'supine'   && <SupineFemale   c={c} animation={animation} />}
        </g>

        {/* energy sparks for explosive moves */}
        {(animation === 'burpee' || animation === 'jumping-jack') && (
          <>
            <circle cx="100" cy="8"  r="5.5" className="motion-dot"    filter={`url(#${p}-spark)`} />
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
