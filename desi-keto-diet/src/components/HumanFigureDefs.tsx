/**
 * Classic figurine gradient / filter defs.
 * Each ExerciseFigure instance gets a unique `prefix` so multiple
 * instances on the same page never share SVG IDs.
 */
export function HumanFigureDefs({ prefix: p }: { prefix: string }) {
  return (
    <defs>
      {/* ── Body & torso fill — mint-to-forest vertical ── */}
      <linearGradient id={`${p}-body`} x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%"   stopColor="#b7e4c7" />
        <stop offset="50%"  stopColor="#52b788" />
        <stop offset="100%" stopColor="#1b4332" />
      </linearGradient>

      {/* ── Limb stroke — same palette, slight diagonal sheen ── */}
      <linearGradient id={`${p}-limb`} x1="0%" y1="0%" x2="60%" y2="100%">
        <stop offset="0%"   stopColor="#95d5b2" />
        <stop offset="100%" stopColor="#2d6a4f" />
      </linearGradient>

      {/* ── Head circle — radial spotlight ── */}
      <radialGradient id={`${p}-head`} cx="38%" cy="32%" r="65%">
        <stop offset="0%"   stopColor="#d8f3dc" />
        <stop offset="55%"  stopColor="#74c69d" />
        <stop offset="100%" stopColor="#2d6a4f" />
      </radialGradient>

      {/* ── Joint highlight (ball joints / ends) ── */}
      <radialGradient id={`${p}-joint`} cx="35%" cy="30%" r="65%">
        <stop offset="0%"   stopColor="#f0faf4" />
        <stop offset="60%"  stopColor="#95d5b2" />
        <stop offset="100%" stopColor="#40916c" />
      </radialGradient>

      {/* ── Stage ambient glow ── */}
      <radialGradient id={`${p}-glow`} cx="50%" cy="88%" r="55%">
        <stop offset="0%"   stopColor="rgba(82,183,136,0.48)" />
        <stop offset="100%" stopColor="rgba(82,183,136,0)"    />
      </radialGradient>

      {/* ── Soft drop shadow on the whole figure ── */}
      <filter id={`${p}-shadow`} x="-20%" y="-15%" width="140%" height="135%">
        <feDropShadow dx="1" dy="3" stdDeviation="2.5"
          floodColor="rgba(15,26,15,0.55)" />
      </filter>

      {/* ── Energy glow for motion dots ── */}
      <filter id={`${p}-glow-f`} x="-60%" y="-60%" width="220%" height="220%">
        <feGaussianBlur stdDeviation="3.5" result="b" />
        <feMerge>
          <feMergeNode in="b" />
          <feMergeNode in="SourceGraphic" />
        </feMerge>
      </filter>
    </defs>
  );
}
