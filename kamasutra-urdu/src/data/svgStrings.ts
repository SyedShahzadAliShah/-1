export function getPostureSvgString(type: string): string {
  const svgs: Record<string, string> = {
    missionary: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 120"><ellipse cx="100" cy="95" rx="70" ry="8" fill="#e8d5c4" opacity="0.4"/><path d="M55 75 Q70 55 100 50 Q130 55 145 75" fill="none" stroke="#6b2d3c" stroke-width="2"/><circle cx="100" cy="42" r="8" fill="none" stroke="#6b2d3c" stroke-width="2"/></svg>`,
    spooning: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 120"><ellipse cx="100" cy="95" rx="70" ry="8" fill="#e8d5c4" opacity="0.4"/><path d="M40 70 Q60 55 90 58 Q120 60 140 72" fill="none" stroke="#6b2d3c" stroke-width="2"/><path d="M50 65 Q75 52 105 55 Q130 58 150 70" fill="none" stroke="#6b2d3c" stroke-width="2" opacity="0.7"/></svg>`,
    lotus: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 120"><circle cx="85" cy="45" r="9" fill="none" stroke="#6b2d3c" stroke-width="2"/><circle cx="115" cy="45" r="9" fill="none" stroke="#6b2d3c" stroke-width="2"/><path d="M70 85 Q100 90 130 85" fill="none" stroke="#6b2d3c" stroke-width="2"/></svg>`,
    cowgirl: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 120"><path d="M50 78 L150 78" fill="none" stroke="#6b2d3c" stroke-width="2"/><circle cx="100" cy="35" r="8" fill="none" stroke="#6b2d3c" stroke-width="2"/></svg>`,
    side: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 120"><circle cx="70" cy="60" r="8" fill="none" stroke="#6b2d3c" stroke-width="2"/><circle cx="130" cy="60" r="8" fill="none" stroke="#6b2d3c" stroke-width="2"/></svg>`,
    standing: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 120"><circle cx="100" cy="30" r="8" fill="none" stroke="#6b2d3c" stroke-width="2"/><path d="M100 38 L100 85" fill="none" stroke="#6b2d3c" stroke-width="2"/></svg>`,
    doggy: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 120"><path d="M45 70 Q70 55 100 58 Q130 55 155 68" fill="none" stroke="#6b2d3c" stroke-width="2"/></svg>`,
    reverse: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 120"><path d="M50 78 L150 78" fill="none" stroke="#6b2d3c" stroke-width="2"/><circle cx="100" cy="35" r="8" fill="none" stroke="#6b2d3c" stroke-width="2"/></svg>`,
    butterfly: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 120"><path d="M50 75 L150 75" fill="none" stroke="#6b2d3c" stroke-width="2"/><path d="M90 50 L80 35 M110 50 L120 35" fill="none" stroke="#6b2d3c" stroke-width="2"/></svg>`,
    yabyum: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 120"><circle cx="100" cy="35" r="8" fill="none" stroke="#6b2d3c" stroke-width="2"/><circle cx="100" cy="55" r="7" fill="none" stroke="#6b2d3c" stroke-width="2"/></svg>`,
    scissors: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 120"><circle cx="75" cy="55" r="8" fill="none" stroke="#6b2d3c" stroke-width="2"/><circle cx="125" cy="55" r="8" fill="none" stroke="#6b2d3c" stroke-width="2"/></svg>`,
    bridge: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 120"><path d="M60 78 Q100 45 140 78" fill="none" stroke="#6b2d3c" stroke-width="2"/></svg>`,
  };
  return svgs[type] ?? svgs.missionary;
}

export function svgStringToElement(svgString: string): SVGSVGElement {
  const parser = new DOMParser();
  const doc = parser.parseFromString(svgString, 'image/svg+xml');
  return doc.documentElement as unknown as SVGSVGElement;
}
