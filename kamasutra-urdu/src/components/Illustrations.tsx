import type { ReactElement } from 'react';

interface IllustrationProps {
  type: string;
  className?: string;
}

const baseStyle = { fill: 'none', stroke: 'currentColor', strokeWidth: 2, strokeLinecap: 'round' as const };

export function PostureIllustration({ type, className = '' }: IllustrationProps) {
  const illustrations: Record<string, ReactElement> = {
    missionary: (
      <svg viewBox="0 0 200 120" className={className} aria-hidden="true">
        <ellipse cx="100" cy="95" rx="70" ry="8" fill="#e8d5c4" opacity="0.4" />
        <path d="M55 75 Q70 55 100 50 Q130 55 145 75" style={baseStyle} />
        <circle cx="100" cy="42" r="8" style={baseStyle} />
        <path d="M70 70 L55 85 M130 70 L145 85" style={baseStyle} />
        <path d="M85 55 Q100 48 115 55" style={{ ...baseStyle, strokeWidth: 1.5 }} opacity="0.6" />
      </svg>
    ),
    spooning: (
      <svg viewBox="0 0 200 120" className={className} aria-hidden="true">
        <ellipse cx="100" cy="95" rx="70" ry="8" fill="#e8d5c4" opacity="0.4" />
        <path d="M40 70 Q60 55 90 58 Q120 60 140 72" style={baseStyle} />
        <path d="M50 65 Q75 52 105 55 Q130 58 150 70" style={{ ...baseStyle, opacity: 0.7 }} />
        <circle cx="145" cy="62" r="7" style={baseStyle} />
        <circle cx="42" cy="62" r="7" style={baseStyle} />
      </svg>
    ),
    lotus: (
      <svg viewBox="0 0 200 120" className={className} aria-hidden="true">
        <ellipse cx="100" cy="105" rx="40" ry="6" fill="#e8d5c4" opacity="0.4" />
        <circle cx="85" cy="45" r="9" style={baseStyle} />
        <circle cx="115" cy="45" r="9" style={baseStyle} />
        <path d="M75 55 L70 85 M85 55 L80 85 M115 55 L120 85 M125 55 L130 85" style={baseStyle} />
        <path d="M70 85 Q100 90 130 85" style={baseStyle} />
        <path d="M85 50 Q100 42 115 50" style={{ ...baseStyle, strokeWidth: 1.5 }} opacity="0.5" />
      </svg>
    ),
    cowgirl: (
      <svg viewBox="0 0 200 120" className={className} aria-hidden="true">
        <ellipse cx="100" cy="95" rx="70" ry="8" fill="#e8d5c4" opacity="0.4" />
        <path d="M50 78 L150 78" style={baseStyle} />
        <circle cx="75" cy="72" r="7" style={baseStyle} />
        <path d="M95 55 Q100 40 105 55 L105 70" style={baseStyle} />
        <circle cx="100" cy="35" r="8" style={baseStyle} />
        <path d="M95 70 L90 78 M105 70 L110 78" style={baseStyle} />
      </svg>
    ),
    side: (
      <svg viewBox="0 0 200 120" className={className} aria-hidden="true">
        <ellipse cx="100" cy="95" rx="70" ry="8" fill="#e8d5c4" opacity="0.4" />
        <circle cx="70" cy="60" r="8" style={baseStyle} />
        <circle cx="130" cy="60" r="8" style={baseStyle} />
        <path d="M65 68 L60 85 M75 68 L80 85" style={baseStyle} />
        <path d="M125 68 L120 85 M135 68 L140 85" style={baseStyle} />
        <path d="M78 62 Q100 55 122 62" style={{ ...baseStyle, strokeWidth: 1.5 }} opacity="0.5" />
      </svg>
    ),
    standing: (
      <svg viewBox="0 0 200 120" className={className} aria-hidden="true">
        <rect x="155" y="20" width="8" height="80" fill="#d4c4b0" opacity="0.5" rx="2" />
        <circle cx="100" cy="30" r="8" style={baseStyle} />
        <circle cx="130" cy="35" r="7" style={baseStyle} />
        <path d="M100 38 L100 85 M130 42 L130 85" style={baseStyle} />
        <path d="M95 50 L85 65 M105 50 L115 60" style={baseStyle} />
        <path d="M125 50 L135 55" style={baseStyle} />
      </svg>
    ),
    doggy: (
      <svg viewBox="0 0 200 120" className={className} aria-hidden="true">
        <ellipse cx="100" cy="95" rx="70" ry="8" fill="#e8d5c4" opacity="0.4" />
        <path d="M45 70 Q70 55 100 58 Q130 55 155 68" style={baseStyle} />
        <circle cx="42" cy="65" r="7" style={baseStyle} />
        <path d="M150 65 L160 75 L155 85" style={baseStyle} />
        <path d="M55 68 L50 82 M65 66 L60 80" style={baseStyle} />
      </svg>
    ),
    reverse: (
      <svg viewBox="0 0 200 120" className={className} aria-hidden="true">
        <ellipse cx="100" cy="95" rx="70" ry="8" fill="#e8d5c4" opacity="0.4" />
        <path d="M50 78 L150 78" style={baseStyle} />
        <circle cx="75" cy="72" r="7" style={baseStyle} />
        <path d="M95 55 Q100 40 105 55 L105 70" style={baseStyle} />
        <circle cx="100" cy="35" r="8" style={{ ...baseStyle, opacity: 0.5 }} />
        <path d="M100 35 L100 25" style={baseStyle} />
      </svg>
    ),
    butterfly: (
      <svg viewBox="0 0 200 120" className={className} aria-hidden="true">
        <ellipse cx="100" cy="95" rx="70" ry="8" fill="#e8d5c4" opacity="0.4" />
        <path d="M50 75 L150 75" style={baseStyle} />
        <circle cx="75" cy="68" r="7" style={baseStyle} />
        <path d="M95 50 L95 68 M105 50 L105 68" style={baseStyle} />
        <path d="M90 50 L80 35 M110 50 L120 35" style={baseStyle} />
        <circle cx="100" cy="42" r="8" style={baseStyle} />
      </svg>
    ),
    yabyum: (
      <svg viewBox="0 0 200 120" className={className} aria-hidden="true">
        <ellipse cx="100" cy="105" rx="35" ry="6" fill="#e8d5c4" opacity="0.4" />
        <circle cx="100" cy="35" r="8" style={baseStyle} />
        <circle cx="100" cy="55" r="7" style={baseStyle} />
        <path d="M85 63 L80 90 M100 62 L100 90 M115 63 L120 90" style={baseStyle} />
        <path d="M80 90 Q100 95 120 90" style={baseStyle} />
        <path d="M92 38 Q100 32 108 38" style={{ ...baseStyle, strokeWidth: 1.5 }} opacity="0.5" />
      </svg>
    ),
    scissors: (
      <svg viewBox="0 0 200 120" className={className} aria-hidden="true">
        <ellipse cx="100" cy="95" rx="70" ry="8" fill="#e8d5c4" opacity="0.4" />
        <circle cx="75" cy="55" r="8" style={baseStyle} />
        <circle cx="125" cy="55" r="8" style={baseStyle} />
        <path d="M70 63 L55 85 M80 63 L90 85" style={baseStyle} />
        <path d="M130 63 L145 85 M120 63 L110 85" style={baseStyle} />
        <path d="M85 75 L115 70" style={{ ...baseStyle, strokeWidth: 1.5 }} opacity="0.5" />
      </svg>
    ),
    bridge: (
      <svg viewBox="0 0 200 120" className={className} aria-hidden="true">
        <ellipse cx="100" cy="95" rx="70" ry="8" fill="#e8d5c4" opacity="0.4" />
        <path d="M50 78 L150 78" style={baseStyle} />
        <path d="M60 78 Q100 45 140 78" style={baseStyle} />
        <circle cx="75" cy="72" r="7" style={baseStyle} />
        <circle cx="100" cy="48" r="8" style={baseStyle} />
        <path d="M95 56 L90 65 M105 56 L110 65" style={baseStyle} />
      </svg>
    ),
  };

  return illustrations[type] ?? illustrations.missionary;
}
