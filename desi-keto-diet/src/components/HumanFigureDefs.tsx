/** Shared SVG gradient + filter defs — each instance gets a unique prefix so
 *  multiple ExerciseFigure components on the same page don't share IDs. */
export function HumanFigureDefs({ prefix: p }: { prefix: string }) {
  return (
    <defs>
      {/* Skin — warm South Asian tone */}
      <radialGradient id={`${p}-sk`} cx="38%" cy="28%" r="68%">
        <stop offset="0%"   stopColor="#f5cfa8" />
        <stop offset="45%"  stopColor="#e0a870" />
        <stop offset="100%" stopColor="#bc7845" />
      </radialGradient>

      {/* Limb skin — side-lit cylinder look */}
      <linearGradient id={`${p}-sl`} x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%"   stopColor="#bc7845" />
        <stop offset="30%"  stopColor="#e8b88a" />
        <stop offset="65%"  stopColor="#f0c89a" />
        <stop offset="100%" stopColor="#c98a52" />
      </linearGradient>

      {/* Sports top — bright green */}
      <linearGradient id={`${p}-to`} x1="0%" y1="0%" x2="10%" y2="100%">
        <stop offset="0%"   stopColor="#95e6be" />
        <stop offset="40%"  stopColor="#52b788" />
        <stop offset="100%" stopColor="#2d6a4f" />
      </linearGradient>

      {/* Leggings — deep green */}
      <linearGradient id={`${p}-lg`} x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%"   stopColor="#3a8060" />
        <stop offset="100%" stopColor="#1b3326" />
      </linearGradient>

      {/* Shoe upper */}
      <linearGradient id={`${p}-sh`} x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%"   stopColor="#3e6050" />
        <stop offset="100%" stopColor="#1a2e1a" />
      </linearGradient>

      {/* Hair — dark brown */}
      <linearGradient id={`${p}-hr`} x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%"   stopColor="#6b4226" />
        <stop offset="100%" stopColor="#2d1f14" />
      </linearGradient>

      {/* Stage glow */}
      <radialGradient id={`${p}-gl`} cx="50%" cy="90%" r="55%">
        <stop offset="0%"   stopColor="rgba(82,183,136,0.45)" />
        <stop offset="100%" stopColor="rgba(82,183,136,0)"    />
      </radialGradient>

      {/* Soft drop shadow */}
      <filter id={`${p}-sf`} x="-25%" y="-25%" width="150%" height="150%">
        <feGaussianBlur in="SourceAlpha" stdDeviation="2" result="b" />
        <feOffset dx="1" dy="3" result="off" />
        <feComponentTransfer result="shadow">
          <feFuncA type="linear" slope="0.28" />
        </feComponentTransfer>
        <feMerge>
          <feMergeNode in="shadow" />
          <feMergeNode in="SourceGraphic" />
        </feMerge>
      </filter>

      {/* Energy glow (for particles, impact dots) */}
      <filter id={`${p}-eg`} x="-50%" y="-50%" width="200%" height="200%">
        <feGaussianBlur stdDeviation="3" result="b" />
        <feMerge>
          <feMergeNode in="b" />
          <feMergeNode in="SourceGraphic" />
        </feMerge>
      </filter>
    </defs>
  );
}
