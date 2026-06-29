/**
 * Female model SVG defs — skin, hair, outfit, stage.
 * Unique `prefix` per instance prevents shared-ID collisions.
 */
export function HumanFigureDefs({ prefix: p }: { prefix: string }) {
  return (
    <defs>
      {/* ─ Skin — warm South Asian ─ */}
      <radialGradient id={`${p}-skin`} cx="38%" cy="30%" r="68%">
        <stop offset="0%"   stopColor="#f8d5b0" />
        <stop offset="45%"  stopColor="#e8a870" />
        <stop offset="100%" stopColor="#bf8450" />
      </radialGradient>

      {/* ─ Limb skin — side-lit cylinder ─ */}
      <linearGradient id={`${p}-slim`} x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%"   stopColor="#c08850" />
        <stop offset="35%"  stopColor="#f0bc88" />
        <stop offset="65%"  stopColor="#f8d0a8" />
        <stop offset="100%" stopColor="#c89060" />
      </linearGradient>

      {/* ─ Hair — rich dark brown ─ */}
      <linearGradient id={`${p}-hair`} x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%"   stopColor="#5c3820" />
        <stop offset="60%"  stopColor="#3a2214" />
        <stop offset="100%" stopColor="#22140c" />
      </linearGradient>

      {/* ─ Sports crop-top — bright mint / emerald ─ */}
      <linearGradient id={`${p}-top`} x1="0%" y1="0%" x2="10%" y2="100%">
        <stop offset="0%"   stopColor="#a8e8c8" />
        <stop offset="45%"  stopColor="#52b788" />
        <stop offset="100%" stopColor="#2d6a4f" />
      </linearGradient>

      {/* ─ Leggings — deep forest green ─ */}
      <linearGradient id={`${p}-leg`} x1="0%" y1="0%" x2="5%" y2="100%">
        <stop offset="0%"   stopColor="#3a8060" />
        <stop offset="100%" stopColor="#1a3028" />
      </linearGradient>

      {/* ─ Shoe ─ */}
      <linearGradient id={`${p}-shoe`} x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%"   stopColor="#e0e8e4" />
        <stop offset="100%" stopColor="#8ab09a" />
      </linearGradient>

      {/* ─ Stage glow ─ */}
      <radialGradient id={`${p}-glow`} cx="50%" cy="90%" r="56%">
        <stop offset="0%"   stopColor="rgba(82,183,136,0.46)" />
        <stop offset="100%" stopColor="rgba(82,183,136,0)"    />
      </radialGradient>

      {/* ─ Soft figure drop-shadow ─ */}
      <filter id={`${p}-shadow`} x="-22%" y="-18%" width="144%" height="140%">
        <feDropShadow dx="1" dy="3" stdDeviation="2.5"
          floodColor="rgba(12,24,12,0.5)" />
      </filter>

      {/* ─ Energy glow for sparks / motion dots ─ */}
      <filter id={`${p}-spark`} x="-60%" y="-60%" width="220%" height="220%">
        <feGaussianBlur stdDeviation="3.5" result="b" />
        <feMerge>
          <feMergeNode in="b" />
          <feMergeNode in="SourceGraphic" />
        </feMerge>
      </filter>
    </defs>
  );
}
