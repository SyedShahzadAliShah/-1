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
  if (['butterfly', 'breathe'].includes(a))                                         return 'seated';
  if (['plank', 'mountain-climber', 'cobra', 'pushup', 'cat-cow'].includes(a))     return 'prone';
  if (['rest', 'hundred', 'roll-up', 'leg-stretch', 'child-pose'].includes(a))     return 'supine';
  return 'standing';
}

/* ─── Sub-components ─────────────────────────────────────────── */

/** Detailed face + head used by all poses */
function Head({
  cx, cy, rx = 16, ry = 18,
  sk, hr,
}: { cx: number; cy: number; rx?: number; ry?: number; sk: string; hr: string }) {
  const fx = cx; const fy = cy + 2;
  return (
    <g className="fig-head human-head">
      {/* Skull */}
      <ellipse cx={cx} cy={cy} rx={rx} ry={ry} fill={sk} />
      {/* Hair */}
      <path fill={hr}
        d={`M ${cx-rx+2} ${cy-ry*0.5}
            C ${cx-rx} ${cy-ry-8} ${cx+rx} ${cy-ry-8} ${cx+rx-2} ${cy-ry*0.5}
            C ${cx+rx+3} ${cy+ry*0.1} ${cx+rx-2} ${cy+ry*0.7} ${cx} ${cy+ry+2}
            C ${cx-rx+2} ${cy+ry*0.7} ${cx-rx-3} ${cy+ry*0.1} ${cx-rx+2} ${cy-ry*0.5} Z`}
      />
      {/* Side ponytail */}
      <path fill={hr}
        d={`M ${cx+rx-4} ${cy-ry*0.4}
            C ${cx+rx+10} ${cy} ${cx+rx+14} ${cy+ry*0.8} ${cx+rx+6} ${cy+ry+8}
            C ${cx+rx+2} ${cy+ry*0.3} ${cx+rx-2} ${cy+ry*0.1} ${cx+rx-4} ${cy-ry*0.4} Z`}
      />
      {/* Headband */}
      <path fill="#40916c"
        d={`M ${cx-rx+1} ${cy-ry*0.6} Q ${cx} ${cy-ry-4} ${cx+rx-1} ${cy-ry*0.6}
            L ${cx+rx-1} ${cy-ry*0.3} Q ${cx} ${cy-ry} ${cx-rx+1} ${cy-ry*0.3} Z`}
      />
      {/* Face */}
      <ellipse cx={fx} cy={fy} rx={rx-3} ry={ry-3} fill={sk} />
      {/* Ears */}
      <ellipse cx={cx-rx+1}  cy={fy} rx="3" ry="4.5" fill={sk} />
      <ellipse cx={cx+rx-1}  cy={fy} rx="3" ry="4.5" fill={sk} />
      {/* Cheeks */}
      <ellipse cx={fx-5}  cy={fy+5} rx="4" ry="2.5" fill="#e09090" opacity="0.28" />
      <ellipse cx={fx+5}  cy={fy+5} rx="4" ry="2.5" fill="#e09090" opacity="0.28" />
      {/* Eyes */}
      <ellipse cx={fx-5}  cy={fy-1} rx="3.5" ry="3"   fill="#fff" />
      <ellipse cx={fx+5}  cy={fy-1} rx="3.5" ry="3"   fill="#fff" />
      <circle  cx={fx-5}  cy={fy-1} r="2.1"          fill="#1a2e1a" />
      <circle  cx={fx+5}  cy={fy-1} r="2.1"          fill="#1a2e1a" />
      <circle  cx={fx-4.2} cy={fy-1.8} r="0.8"       fill="#fff"    />
      <circle  cx={fx+5.8} cy={fy-1.8} r="0.8"       fill="#fff"    />
      {/* Brows */}
      <path d={`M ${fx-8} ${fy-5} Q ${fx-5} ${fy-7} ${fx-2} ${fy-5}`}
        fill="none" stroke="#4a3020" strokeWidth="1.5" strokeLinecap="round" />
      <path d={`M ${fx+2} ${fy-5} Q ${fx+5} ${fy-7} ${fx+8} ${fy-5}`}
        fill="none" stroke="#4a3020" strokeWidth="1.5" strokeLinecap="round" />
      {/* Nose */}
      <path d={`M ${fx} ${fy+2} L ${fx-2} ${fy+6} L ${fx+2} ${fy+6}`}
        fill="none" stroke="#b87450" strokeWidth="1" strokeLinecap="round" />
      {/* Smile */}
      <path d={`M ${fx-6} ${fy+8} Q ${fx} ${fy+13} ${fx+6} ${fy+8}`}
        fill="none" stroke="#8b5a3c" strokeWidth="1.6" strokeLinecap="round" />
    </g>
  );
}

/** Running shoe for standing figure */
function Shoe({ x, y, dir = 1, sh }: { x: number; y: number; dir?: number; sh: string }) {
  const tip = x + dir * 16;
  const back = x - dir * 10;
  return (
    <g>
      <ellipse cx={x + dir * 3} cy={y} rx="14" ry="5.5" fill="#d4a570" />
      <path fill={sh}
        d={`M ${back} ${y} L ${tip} ${y} L ${tip-dir*2} ${y+7} L ${back+dir*2} ${y+7} Z`} />
      <rect x={Math.min(back+dir*2, tip-dir*4)} y={y+6}
        width="20" height="3.5" rx="1.5" fill="#0d1a0d" />
      <path d={`M ${x-dir*2} ${y} L ${x+dir*4} ${y-1}`}
        fill="none" stroke="rgba(255,255,255,0.35)" strokeWidth="1.5" strokeLinecap="round" />
    </g>
  );
}

/* ─── STANDING body ───────────────────────────────────────────── */
function StandingBody({
  sk, sl, to, lg, sh,
  animation,
}: { sk: string; sl: string; to: string; lg: string; sh: string; animation: ExerciseAnimation }) {
  return (
    <>
      {/* Neck */}
      <rect className="fig-neck human-neck" x="92" y="44" width="16" height="13" rx="6" fill={sk} />

      {/* Torso — sports top */}
      <path className="fig-torso human-torso" fill={to}
        d="M 73 56 C 85 49 115 49 127 56 L 125 80 L 127 118
           C 113 126 87 126 73 118 L 75 80 Z" />
      {/* Shoulder highlights */}
      <ellipse cx="77" cy="63" rx="5" ry="9" fill="rgba(255,255,255,0.07)" />
      <ellipse cx="123" cy="63" rx="5" ry="9" fill="rgba(255,255,255,0.07)" />
      {/* Core */}
      <ellipse cx="100" cy="97" rx="9" ry="11" fill="rgba(255,255,255,0.05)" />
      {/* Strap lines */}
      <path d="M 77 56 L 79 118" fill="none" stroke="rgba(255,255,255,0.18)" strokeWidth="2" />
      <path d="M 123 56 L 121 118" fill="none" stroke="rgba(255,255,255,0.18)" strokeWidth="2" />

      {/* Leggings */}
      <path className="human-leggings" fill={lg}
        d="M 73 118 L 127 118 L 124 135 C 112 142 88 142 76 135 Z" />

      {/* Shoulder joints */}
      <circle cx="77" cy="58" r="5.5" fill={sk} />
      <circle cx="123" cy="58" r="5.5" fill={sk} />

      {/* Left arm */}
      <g className="fig-arm-l">
        <path className="human-upper-arm" d={`M 77 58 L 61 88`}
          stroke={sl} strokeWidth="12" strokeLinecap="round" fill="none" />
        <circle cx="61" cy="88" r="5" fill={sk} />
        <path className="human-forearm" d={`M 61 88 L 52 114`}
          stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
        <ellipse className="human-hand" cx="50" cy="118" rx="7" ry="5.5" fill={sk} />
      </g>

      {/* Right arm */}
      <g className="fig-arm-r">
        <path className="human-upper-arm" d={`M 123 58 L 139 88`}
          stroke={sl} strokeWidth="12" strokeLinecap="round" fill="none" />
        <circle cx="139" cy="88" r="5" fill={sk} />
        <path className="human-forearm" d={`M 139 88 L 148 114`}
          stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
        <ellipse className="human-hand" cx="150" cy="118" rx="7" ry="5.5" fill={sk} />
      </g>

      {/* Hip joints */}
      <circle cx="87" cy="131" r="6" fill={sk} />
      <circle cx="113" cy="131" r="6" fill={sk} />

      {/* Left leg */}
      <g className="fig-leg-l">
        <path className="human-thigh" d={`M 87 131 L 78 175`}
          stroke={sl} strokeWidth="14" strokeLinecap="round" fill="none" />
        <circle cx="78" cy="175" r="5.5" fill={sk} />
      </g>
      <g className="fig-shin-l">
        <path className="human-calf" d={`M 78 175 L 70 212`}
          stroke={sl} strokeWidth="11" strokeLinecap="round" fill="none" />
        <Shoe x={64} y={215} dir={-1} sh={sh} />
      </g>

      {/* Right leg */}
      <g className="fig-leg-r">
        <path className="human-thigh" d={`M 113 131 L 122 175`}
          stroke={sl} strokeWidth="14" strokeLinecap="round" fill="none" />
        <circle cx="122" cy="175" r="5.5" fill={sk} />
      </g>
      <g className="fig-shin-r">
        <path className="human-calf" d={`M 122 175 L 130 212`}
          stroke={sl} strokeWidth="11" strokeLinecap="round" fill="none" />
        <Shoe x={136} y={215} dir={1} sh={sh} />
      </g>

      {/* Butterfly pose overlay */}
      {animation === 'butterfly' && (
        <g className="pose-overlay butterfly-legs">
          <path className="human-thigh butterfly-leg"
            d="M 100 132 L 62 162" stroke={sl} strokeWidth="13" strokeLinecap="round" fill="none" />
          <path className="human-thigh butterfly-leg"
            d="M 100 132 L 138 162" stroke={sl} strokeWidth="13" strokeLinecap="round" fill="none" />
          <path className="human-calf butterfly-leg"
            d="M 62 162 L 52 180" stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
          <path className="human-calf butterfly-leg"
            d="M 138 162 L 148 180" stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
        </g>
      )}
    </>
  );
}

/* ─── SEATED cross-legged body ────────────────────────────────── */
function SeatedBody({
  sk, sl, to, lg,
}: { sk: string; sl: string; to: string; lg: string; animation?: ExerciseAnimation }) {
  return (
    <>
      {/* Neck */}
      <rect className="fig-neck human-neck" x="92" y="58" width="16" height="13" rx="6" fill={sk} />

      {/* Torso — upright seated */}
      <path className="fig-torso human-torso" fill={to}
        d="M 76 70 C 87 63 113 63 124 70 L 122 92 L 124 128
           C 112 136 88 136 76 128 L 78 92 Z" />
      <ellipse cx="100" cy="108" rx="9" ry="11" fill="rgba(255,255,255,0.05)" />
      <path d="M 79 70 L 81 128" fill="none" stroke="rgba(255,255,255,0.18)" strokeWidth="2" />
      <path d="M 121 70 L 119 128" fill="none" stroke="rgba(255,255,255,0.18)" strokeWidth="2" />

      {/* Waistband */}
      <path className="human-leggings" fill={lg}
        d="M 76 128 L 124 128 L 122 142 C 110 148 90 148 78 142 Z" />

      {/* Shoulders */}
      <circle cx="80" cy="72" r="5.5" fill={sk} />
      <circle cx="120" cy="72" r="5.5" fill={sk} />

      {/* Arms resting on knees */}
      <g className="fig-arm-l">
        <path className="human-upper-arm" d="M 80 72 L 64 100"
          stroke={sl} strokeWidth="12" strokeLinecap="round" fill="none" />
        <circle cx="64" cy="100" r="4.5" fill={sk} />
        <path className="human-forearm" d="M 64 100 L 58 130"
          stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
        <ellipse className="human-hand" cx="57" cy="135" rx="7" ry="5" fill={sk} />
      </g>
      <g className="fig-arm-r">
        <path className="human-upper-arm" d="M 120 72 L 136 100"
          stroke={sl} strokeWidth="12" strokeLinecap="round" fill="none" />
        <circle cx="136" cy="100" r="4.5" fill={sk} />
        <path className="human-forearm" d="M 136 100 L 142 130"
          stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
        <ellipse className="human-hand" cx="143" cy="135" rx="7" ry="5" fill={sk} />
      </g>

      {/* Cross-legged pose — left */}
      <g className="fig-leg-l">
        <path className="human-thigh" d="M 86 142 L 56 168"
          stroke={sl} strokeWidth="13" strokeLinecap="round" fill="none" />
        <circle cx="56" cy="168" r="5" fill={sk} />
      </g>
      <g className="fig-shin-l">
        <path className="human-calf" d="M 56 168 L 80 180"
          stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
        <ellipse cx="82" cy="182" rx="9" ry="5" fill={sk} />
      </g>

      {/* Cross-legged pose — right */}
      <g className="fig-leg-r">
        <path className="human-thigh" d="M 114 142 L 144 168"
          stroke={sl} strokeWidth="13" strokeLinecap="round" fill="none" />
        <circle cx="144" cy="168" r="5" fill={sk} />
      </g>
      <g className="fig-shin-r">
        <path className="human-calf" d="M 144 168 L 120 180"
          stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
        <ellipse cx="118" cy="182" rx="9" ry="5" fill={sk} />
      </g>

      {/* Yoga mat */}
      <rect x="40" y="186" width="120" height="9" rx="4.5"
        fill="rgba(82,183,136,0.3)" stroke="rgba(82,183,136,0.55)" strokeWidth="1" />
    </>
  );
}

/* ─── PRONE horizontal body ───────────────────────────────────── */
function ProneBody({
  sk, sl, to, lg, animation,
}: { sk: string; sl: string; to: string; lg: string; sh?: string; animation: ExerciseAnimation }) {
  const isPlank   = animation === 'plank' || animation === 'mountain-climber';
  const isCobra   = animation === 'cobra';
  const isPushup  = animation === 'pushup';
  const isCatCow  = animation === 'cat-cow';

  // Ground level, body center y
  const GY  = 195;  // ground
  const BAY = isCobra ? 155 : 165;  // body (arms) attachment Y

  return (
    <>
      {/* Yoga/exercise mat */}
      <rect x="15" y={GY} width="175" height="10" rx="5"
        fill="rgba(82,183,136,0.28)" stroke="rgba(82,183,136,0.5)" strokeWidth="1" />

      {/* ── Plank / Mountain-climber ── */}
      {(isPlank || isPushup) && (
        <>
          {/* Head */}
          <Head cx={26} cy={BAY - 5} rx={13} ry={15} sk={sk} hr="url(#no-hr)" />
          {/* Body */}
          <path className="fig-torso human-torso" fill={to}
            d={`M 38 ${BAY - 9} L 148 ${BAY - 7} L 148 ${BAY + 9} L 38 ${BAY + 11} Z`} />
          <path className="human-leggings" fill={lg}
            d={`M 148 ${BAY - 7} L 175 ${BAY - 3} L 175 ${BAY + 10} L 148 ${BAY + 9} Z`} />
          {/* Support arms */}
          <g className="fig-arm-l">
            <path className="human-upper-arm"
              d={`M 52 ${BAY} L 52 ${GY}`}
              stroke={sl} strokeWidth="12" strokeLinecap="round" fill="none" />
            <circle cx="52" cy={GY} r="6" fill={sk} />
          </g>
          <g className="fig-arm-r">
            <path className="human-upper-arm"
              d={`M 88 ${BAY} L 88 ${GY}`}
              stroke={sl} strokeWidth="12" strokeLinecap="round" fill="none" />
            <circle cx="88" cy={GY} r="6" fill={sk} />
          </g>
          {/* Legs */}
          <g className="fig-leg-l">
            <path className="human-thigh"
              d={`M 148 ${BAY} L 164 ${BAY + 4}`}
              stroke={sl} strokeWidth="13" strokeLinecap="round" fill="none" />
          </g>
          <g className="fig-shin-l">
            <path className="human-calf"
              d={`M 164 ${BAY + 4} L 172 ${GY}`}
              stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
            <ellipse cx="176" cy={GY + 1} rx="8" ry="4" fill={sk} />
          </g>
          <g className="fig-leg-r">
            <path className="human-thigh"
              d={`M 148 ${BAY} L 162 ${BAY + 6}`}
              stroke={sl} strokeWidth="13" strokeLinecap="round" fill="none" />
          </g>
          <g className="fig-shin-r">
            <path className="human-calf"
              d={`M 162 ${BAY + 6} L 168 ${GY}`}
              stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
            <ellipse cx="172" cy={GY + 1} rx="8" ry="4" fill={sk} />
          </g>
        </>
      )}

      {/* ── Cobra ── */}
      {isCobra && (
        <>
          {/* Lower body flat */}
          <path className="fig-leg-l human-thigh"
            d="M 108 185 L 148 192" stroke={sl} strokeWidth="13" strokeLinecap="round" fill="none" />
          <path className="fig-leg-r human-thigh"
            d="M 108 188 L 155 195" stroke={sl} strokeWidth="13" strokeLinecap="round" fill="none" />
          <path className="fig-shin-l human-calf"
            d="M 148 192 L 172 196" stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
          <path className="fig-shin-r human-calf"
            d="M 155 195 L 180 198" stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
          {/* Hips/waist flat */}
          <path fill={lg}
            d="M 100 182 L 162 190 L 160 198 L 98 190 Z" />
          {/* Arching torso */}
          <path className="fig-torso human-torso cobra-body" fill={to}
            d="M 98 182 Q 68 158 48 138 Q 38 128 36 118
               L 44 112 Q 60 124 72 136 Q 90 154 110 176 Z" />
          {/* Arms pushing up */}
          <g className="fig-arm-l">
            <path className="human-upper-arm"
              d="M 48 138 L 44 168" stroke={sl} strokeWidth="12" strokeLinecap="round" fill="none" />
            <path className="human-forearm"
              d="M 44 168 L 42 195" stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
            <ellipse cx="42" cy={GY} rx="7" ry="5" fill={sk} />
          </g>
          <g className="fig-arm-r">
            <path className="human-upper-arm"
              d="M 70 152 L 66 178" stroke={sl} strokeWidth="12" strokeLinecap="round" fill="none" />
            <path className="human-forearm"
              d="M 66 178 L 64 195" stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
            <ellipse cx="64" cy={GY} rx="7" ry="5" fill={sk} />
          </g>
          {/* Head raised */}
          <Head cx={34} cy={108} rx={13} ry={15} sk={sk} hr="url(#no-hr)" />
        </>
      )}

      {/* ── Cat-cow ── */}
      {isCatCow && (
        <>
          {/* On all-fours — hands and knees */}
          <Head cx={28} cy={BAY - 22} rx={13} ry={15} sk={sk} hr="url(#no-hr)" />
          {/* Neck */}
          <path d={`M 40 ${BAY - 15} L 55 ${BAY}`}
            stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
          {/* Back */}
          <path className="fig-torso human-torso" fill={to}
            d={`M 55 ${BAY - 7} Q 100 ${BAY - 18} 140 ${BAY - 5}
                L 140 ${BAY + 9} Q 100 ${BAY + 20} 55 ${BAY + 7} Z`} />
          {/* Front arms (hands on floor) */}
          <g className="fig-arm-l">
            <path className="human-upper-arm"
              d={`M 62 ${BAY - 2} L 58 ${GY}`}
              stroke={sl} strokeWidth="12" strokeLinecap="round" fill="none" />
            <circle cx="58" cy={GY} r="6" fill={sk} />
          </g>
          <g className="fig-arm-r">
            <path className="human-upper-arm"
              d={`M 82 ${BAY - 4} L 78 ${GY}`}
              stroke={sl} strokeWidth="12" strokeLinecap="round" fill="none" />
            <circle cx="78" cy={GY} r="6" fill={sk} />
          </g>
          {/* Back legs (knees on floor) */}
          <path fill={lg}
            d={`M 140 ${BAY - 5} L 150 ${BAY - 2} L 150 ${BAY + 12} L 140 ${BAY + 9} Z`} />
          <g className="fig-leg-l">
            <path className="human-thigh"
              d={`M 145 ${BAY} L 148 ${GY}`}
              stroke={sl} strokeWidth="13" strokeLinecap="round" fill="none" />
            <circle cx="148" cy={GY} r="6" fill={sk} />
          </g>
          <g className="fig-leg-r">
            <path className="human-thigh"
              d={`M 155 ${BAY + 2} L 160 ${GY}`}
              stroke={sl} strokeWidth="13" strokeLinecap="round" fill="none" />
            <circle cx="160" cy={GY} r="6" fill={sk} />
          </g>
        </>
      )}
    </>
  );
}

/* ─── SUPINE (lying on back) body ─────────────────────────────── */
function SupineBody({
  sk, sl, to, lg, sh, animation,
}: { sk: string; sl: string; to: string; lg: string; sh: string; animation: ExerciseAnimation }) {
  const GY   = 198;  // ground / mat level
  const BY   = 172;  // body center Y (lying flat)
  const isChildPose = animation === 'child-pose';

  if (isChildPose) {
    // Child pose: kneeling, body folded forward
    return (
      <>
        <rect x="20" y={GY} width="165" height="10" rx="5"
          fill="rgba(82,183,136,0.28)" stroke="rgba(82,183,136,0.5)" strokeWidth="1" />
        {/* Head bowed */}
        <Head cx={36} cy={BY - 10} rx={13} ry={14} sk={sk} hr="url(#no-hr)" />
        {/* Curved back/spine */}
        <path className="fig-torso human-torso" fill={to}
          d="M 46 168 Q 72 152 100 150 Q 128 148 148 155
             L 148 166 Q 128 160 100 162 Q 72 164 46 180 Z" />
        <path fill={lg}
          d="M 148 155 L 168 158 L 168 170 L 148 166 Z" />
        {/* Arms stretched forward */}
        <g className="fig-arm-l">
          <path className="human-upper-arm"
            d="M 62 165 L 42 172" stroke={sl} strokeWidth="12" strokeLinecap="round" fill="none" />
          <path className="human-forearm"
            d="M 42 172 L 26 175" stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
          <ellipse cx="20" cy="177" rx="8" ry="5" fill={sk} />
        </g>
        <g className="fig-arm-r">
          <path className="human-upper-arm"
            d="M 68 163 L 48 168" stroke={sl} strokeWidth="12" strokeLinecap="round" fill="none" />
          <path className="human-forearm"
            d="M 48 168 L 30 171" stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
          <ellipse cx="24" cy="173" rx="8" ry="5" fill={sk} />
        </g>
        {/* Knees/shins on floor */}
        <g className="fig-leg-l">
          <path className="human-thigh"
            d="M 148 158 L 155 198" stroke={sl} strokeWidth="13" strokeLinecap="round" fill="none" />
        </g>
        <g className="fig-shin-l">
          <path className="human-calf"
            d="M 155 198 L 168 198" stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
        </g>
        <g className="fig-leg-r">
          <path className="human-thigh"
            d="M 154 162 L 162 198" stroke={sl} strokeWidth="13" strokeLinecap="round" fill="none" />
        </g>
        <g className="fig-shin-r">
          <path className="human-calf"
            d="M 162 198 L 177 198" stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
        </g>
      </>
    );
  }

  // Supine — lying on back, head at left
  return (
    <>
      {/* Mat */}
      <rect x="10" y={GY - 4} width="180" height="10" rx="5"
        fill="rgba(82,183,136,0.28)" stroke="rgba(82,183,136,0.5)" strokeWidth="1" />

      {/* Head */}
      <Head cx={24} cy={BY - 4} rx={13} ry={15} sk={sk} hr="url(#no-hr)" />

      {/* Torso horizontal */}
      <path className="fig-torso human-torso" fill={to}
        d={`M 37 ${BY - 10} L 140 ${BY - 8} L 140 ${BY + 10} L 37 ${BY + 12} Z`} />
      <path className="human-leggings" fill={lg}
        d={`M 140 ${BY - 8} L 175 ${BY - 5} L 175 ${BY + 8} L 140 ${BY + 10} Z`} />

      {/* Arms along sides */}
      <g className="fig-arm-l">
        <path className="human-upper-arm"
          d={`M 60 ${BY + 2} L 60 ${GY - 6}`}
          stroke={sl} strokeWidth="12" strokeLinecap="round" fill="none" />
        <path className="human-forearm"
          d={`M 60 ${GY - 6} L 58 ${GY + 2}`}
          stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
      </g>
      <g className="fig-arm-r">
        <path className="human-upper-arm"
          d={`M 80 ${BY - 2} L 82 ${GY - 6}`}
          stroke={sl} strokeWidth="12" strokeLinecap="round" fill="none" />
        <path className="human-forearm"
          d={`M 82 ${GY - 6} L 80 ${GY + 2}`}
          stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
      </g>

      {/* Legs */}
      <g className="fig-leg-l">
        <path className="human-thigh"
          d={`M 140 ${BY} L 160 ${BY + 2}`}
          stroke={sl} strokeWidth="13" strokeLinecap="round" fill="none" />
        <circle cx="160" cy={BY + 2} r="5" fill={sk} />
      </g>
      <g className="fig-shin-l">
        <path className="human-calf"
          d={`M 160 ${BY + 2} L 178 ${BY + 4}`}
          stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
        <Shoe x={182} y={BY + 5} dir={1} sh={sh} />
      </g>
      <g className="fig-leg-r">
        <path className="human-thigh"
          d={`M 140 ${BY + 4} L 158 ${BY + 6}`}
          stroke={sl} strokeWidth="13" strokeLinecap="round" fill="none" />
        <circle cx="158" cy={BY + 6} r="5" fill={sk} />
      </g>
      <g className="fig-shin-r">
        <path className="human-calf"
          d={`M 158 ${BY + 6} L 176 ${BY + 8}`}
          stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
        <Shoe x={180} y={BY + 9} dir={1} sh={sh} />
      </g>

      {/* Hundred pose: legs lifted */}
      {animation === 'hundred' && (
        <g className="fig-leg-l hundred-lift" style={{ transformOrigin: '140px 172px' }}>
          <path className="human-thigh"
            d={`M 140 ${BY} L 158 ${BY - 18}`}
            stroke={sl} strokeWidth="13" strokeLinecap="round" fill="none" />
          <circle cx="158" cy={BY - 18} r="5" fill={sk} />
          <path className="human-calf"
            d={`M 158 ${BY - 18} L 176 ${BY - 16}`}
            stroke={sl} strokeWidth="10" strokeLinecap="round" fill="none" />
        </g>
      )}

      {/* Roll-up: head and shoulders lifted */}
      {animation === 'roll-up' && (
        <g className="fig-torso-lift roll-up-upper" style={{ transformOrigin: '140px 172px' }}>
          <path
            d={`M 70 ${BY - 25} Q 100 ${BY - 42} 130 ${BY - 30}
                L 135 ${BY - 18} Q 105 ${BY - 30} 72 ${BY - 14} Z`}
            fill={to} />
        </g>
      )}
    </>
  );
}

/* ─── Main component ──────────────────────────────────────────── */
export default function ExerciseFigure({ animation, compact = false }: Props) {
  const rawId = useId();
  const p = `hf${rawId.replace(/[^a-zA-Z0-9]/g, '')}`;

  const sk = `url(#${p}-sk)`;
  const sl = `url(#${p}-sl)`;
  const to = `url(#${p}-to)`;
  const lg = `url(#${p}-lg)`;
  const sh = `url(#${p}-sh)`;
  const hr = `url(#${p}-hr)`;

  const mode = getPoseMode(animation);

  const isSeated = mode === 'seated';
  const isProne  = mode === 'prone';
  const isSupine = mode === 'supine';

  // Head position per mode
  const headCx = isProne || isSupine ? -999 : 100; // floor heads drawn inside body components
  const headCy = isSeated ? 40 : 24;
  const headRx = isSeated ? 15 : 16;
  const headRy = isSeated ? 17 : 18;

  return (
    <div
      className={`exercise-stage exercise-${animation}${compact ? ' exercise-stage-compact' : ''}`}
      aria-hidden="true"
    >
      <div className="stage-floor" />
      <div className="stage-glow" />

      <svg viewBox="0 0 200 240" className="exercise-svg">
        <HumanFigureDefs prefix={p} />

        {/* Ambient radial glow on stage */}
        <ellipse cx="100" cy="195" rx="80" ry="50" fill={`url(#${p}-gl)`} />

        {/* Ground shadow */}
        <ellipse
          className={`human-shadow ${isProne || isSupine ? 'shadow-floor' : ''}`}
          cx={isProne ? 100 : (isSupine ? 100 : 100)}
          cy={isProne ? 206 : (isSupine ? 204 : 226)}
          rx={isProne ? 80 : (isSupine ? 80 : 38)}
          ry={isProne ? 7  : (isSupine ? 7  : 7)}
        />

        <g
          className={`figure-body human-figure${isSeated ? ' human-seated' : ''}${isProne ? ' human-prone' : ''}${isSupine ? ' human-supine' : ''}`}
          filter={`url(#${p}-sf)`}
        >
          {/* Head (for standing & seated) */}
          {!isProne && !isSupine && (
            <Head cx={headCx} cy={headCy} rx={headRx} ry={headRy} sk={sk} hr={hr} />
          )}

          {/* Body */}
          {mode === 'standing' && (
            <StandingBody sk={sk} sl={sl} to={to} lg={lg} sh={sh} animation={animation} />
          )}
          {mode === 'seated' && (
            <SeatedBody sk={sk} sl={sl} to={to} lg={lg} animation={animation} />
          )}
          {mode === 'prone' && (
            <ProneBody sk={sk} sl={sl} to={to} lg={lg} animation={animation} />
          )}
          {mode === 'supine' && (
            <SupineBody sk={sk} sl={sl} to={to} lg={lg} sh={sh} animation={animation} />
          )}
        </g>

        {/* Motion dot for high-energy moves */}
        {(animation === 'burpee' || animation === 'jumping-jack') && (
          <g>
            <circle cx="100" cy="8" r="6" className="motion-dot" filter={`url(#${p}-eg)`} />
            <circle cx="85"  cy="14" r="3.5" className="motion-dot-sm" />
            <circle cx="115" cy="14" r="3.5" className="motion-dot-sm" />
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
