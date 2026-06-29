/** Shared SVG gradient/filter defs — unique per instance via prefix */
export function HumanFigureDefs({ prefix }: { prefix: string }) {
  return (
    <defs>
      <radialGradient id={`${prefix}-skin`} cx="40%" cy="30%" r="65%">
        <stop offset="0%" stopColor="#f0c9a0" />
        <stop offset="55%" stopColor="#d4a574" />
        <stop offset="100%" stopColor="#b8845a" />
      </radialGradient>
      <linearGradient id={`${prefix}-skin-limb`} x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stopColor="#c9956b" />
        <stop offset="45%" stopColor="#e8b88a" />
        <stop offset="100%" stopColor="#b8845a" />
      </linearGradient>
      <linearGradient id={`${prefix}-tank`} x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stopColor="#74c69d" />
        <stop offset="50%" stopColor="#52b788" />
        <stop offset="100%" stopColor="#2d6a4f" />
      </linearGradient>
      <linearGradient id={`${prefix}-leggings`} x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stopColor="#40916c" />
        <stop offset="100%" stopColor="#1b4332" />
      </linearGradient>
      <linearGradient id={`${prefix}-shoe`} x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stopColor="#3d5a45" />
        <stop offset="100%" stopColor="#1a2e1a" />
      </linearGradient>
      <linearGradient id={`${prefix}-hair`} x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stopColor="#5c3d2e" />
        <stop offset="100%" stopColor="#2d1f14" />
      </linearGradient>
      <radialGradient id={`${prefix}-glow`} cx="50%" cy="80%" r="50%">
        <stop offset="0%" stopColor="rgba(82,183,136,0.35)" />
        <stop offset="100%" stopColor="rgba(82,183,136,0)" />
      </radialGradient>
      <filter id={`${prefix}-soft`} x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur in="SourceAlpha" stdDeviation="1.5" result="blur" />
        <feOffset dy="2" result="offset" />
        <feComponentTransfer>
          <feFuncA type="linear" slope="0.25" />
        </feComponentTransfer>
        <feMerge>
          <feMergeNode />
          <feMergeNode in="SourceGraphic" />
        </feMerge>
      </filter>
      <filter id={`${prefix}-glow-filter`}>
        <feGaussianBlur stdDeviation="3" result="blur" />
        <feMerge>
          <feMergeNode in="blur" />
          <feMergeNode in="SourceGraphic" />
        </feMerge>
      </filter>
    </defs>
  );
}
