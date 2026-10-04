/** Embedded SVG lecture diagrams — MathJax handles formulas in text. */
export const DIAGRAMS = {
  courseMap: `<svg viewBox="0 0 640 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CS XII chapter map">
  <defs><linearGradient id="g1" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#5eead4"/><stop offset="100%" stop-color="#ffd166"/></linearGradient></defs>
  <rect width="640" height="320" fill="#0f172a" rx="12"/>
  <text x="320" y="36" fill="#e2e8f0" font-size="18" text-anchor="middle" font-family="Georgia,serif">CS XII — Self-Taught Cinema Path</text>
  ${[
    [80, 90, "Ch1 HCI"],
    [220, 90, "Ch2 Algorithms"],
    [360, 90, "Ch3 Python"],
    [500, 90, "Ch4 Data"],
    [150, 200, "Ch5 AI/ML"],
    [410, 200, "Ch6 Digital Biz"],
  ]
    .map(
      ([x, y, label]) =>
        `<rect x="${x - 55}" y="${y}" width="110" height="44" rx="8" fill="url(#g1)" opacity="0.85"/><text x="${x}" y="${y + 28}" fill="#0f172a" font-size="11" text-anchor="middle" font-weight="bold">${label}</text>`
    )
    .join("")}
  <text x="320" y="280" fill="#94a3b8" font-size="13" text-anchor="middle">★ = Golden (exam-critical) — start here if motivation is low</text>
</svg>`,

  sensoryChannels: `<svg viewBox="0 0 520 280" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sensory channels HCI">
  <rect width="520" height="280" fill="#0f172a" rx="10"/>
  <circle cx="260" cy="130" r="48" fill="#1e293b" stroke="#5eead4" stroke-width="2"/>
  <text x="260" y="135" fill="#5eead4" text-anchor="middle" font-size="14" font-weight="bold">HUMAN</text>
  ${[
    [260, 40, "Sight", "#fbbf24"],
    [420, 130, "Touch", "#fb7185"],
    [260, 220, "Hearing", "#a78bfa"],
    [100, 130, "Voice", "#34d399"],
  ]
    .map(
      ([x, y, label, c]) =>
        `<line x1="260" y1="130" x2="${x}" y2="${y}" stroke="${c}" stroke-width="2" opacity="0.7"/><circle cx="${x}" cy="${y}" r="32" fill="#1e293b" stroke="${c}"/><text x="${x}" y="${y + 5}" fill="${c}" text-anchor="middle" font-size="11">${label}</text>`
    )
    .join("")}
  <rect x="160" y="248" width="200" height="24" rx="6" fill="#334155"/><text x="260" y="264" fill="#e2e8f0" text-anchor="middle" font-size="11">Computer responds on each channel</text>
</svg>`,

  tradVsNatural: `<svg viewBox="0 0 560 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Traditional vs natural interaction">
  <rect width="560" height="240" fill="#0f172a" rx="10"/>
  <rect x="24" y="40" width="240" height="160" rx="12" fill="#1e3a5f" stroke="#94a3b8"/>
  <text x="144" y="68" fill="#94a3b8" text-anchor="middle" font-size="14" font-weight="bold">Traditional</text>
  <text x="144" y="100" fill="#e2e8f0" text-anchor="middle" font-size="11">Mouse · Keyboard</text>
  <text x="144" y="120" fill="#e2e8f0" text-anchor="middle" font-size="11">Touchscreen tap/swipe</text>
  <rect x="296" y="40" width="240" height="160" rx="12" fill="#134e4a" stroke="#5eead4"/>
  <text x="416" y="68" fill="#5eead4" text-anchor="middle" font-size="14" font-weight="bold">Natural</text>
  <text x="416" y="100" fill="#e2e8f0" text-anchor="middle" font-size="11">Voice (Alexa, Siri)</text>
  <text x="416" y="120" fill="#e2e8f0" text-anchor="middle" font-size="11">Gesture · Face ID · VR</text>
</svg>`,

  hciApplications: `<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="HCI application domains">
  <rect width="400" height="400" fill="#0f172a" rx="10"/>
  <circle cx="200" cy="200" r="55" fill="#422006" stroke="#ffd166" stroke-width="2"/>
  <text x="200" y="205" fill="#ffd166" text-anchor="middle" font-size="16" font-weight="bold">HCI</text>
  ${[
    [200, 60, "Healthcare"],
    [340, 200, "Banking"],
    [200, 340, "Education"],
    [60, 200, "Networking"],
  ]
    .map(
      ([x, y, t]) =>
        `<line x1="200" y1="200" x2="${x}" y2="${y}" stroke="#475569"/><circle cx="${x}" cy="${y}" r="38" fill="#1e293b" stroke="#5eead4"/><text x="${x}" y="${y + 4}" fill="#e2e8f0" text-anchor="middle" font-size="10">${t}</text>`
    )
    .join("")}
</svg>`,

  hciComponents: `<svg viewBox="0 0 520 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="HCI components">
  <rect width="520" height="300" fill="#0f172a" rx="10"/>
  ${[
    [90, 80, "User"],
    [260, 80, "Computer System"],
    [430, 80, "Task"],
    [175, 200, "Interaction"],
    [345, 200, "UI + Feedback"],
  ]
    .map(
      ([x, y, t], i) =>
        `<rect x="${x - 70}" y="${y - 28}" width="140" height="56" rx="10" fill="#1e293b" stroke="${i === 1 ? "#ffd166" : "#64748b"}"/><text x="${x}" y="${y + 5}" fill="#e2e8f0" text-anchor="middle" font-size="12">${t}</text>`
    )
    .join("")}
  <path d="M160 108 H220 M300 108 H360 M430 136 V172 M345 172 H175" stroke="#5eead4" fill="none" stroke-width="2" marker-end="url(#arr)"/>
  <defs><marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="#5eead4"/></marker></defs>
</svg>`,

  hciImportance: `<svg viewBox="0 0 480 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Importance of HCI">
  <rect width="480" height="200" fill="#0f172a" rx="10"/>
  <text x="240" y="36" fill="#ffd166" text-anchor="middle" font-size="15">Good HCI → Productivity · Inclusivity · Innovation</text>
  <rect x="40" y="60" width="120" height="100" rx="8" fill="#14532d"/><text x="100" y="115" fill="#bbf7d0" text-anchor="middle" font-size="11">Simple</text>
  <rect x="180" y="60" width="120" height="100" rx="8" fill="#713f12"/><text x="240" y="115" fill="#fde68a" text-anchor="middle" font-size="11">Usable</text>
  <rect x="320" y="60" width="120" height="100" rx="8" fill="#7f1d1d"/><text x="380" y="115" fill="#fecaca" text-anchor="middle" font-size="11">Risk if poor</text>
</svg>`,

  accessibility: `<svg viewBox="0 0 460 180" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Accessibility principles">
  <rect width="460" height="180" fill="#0f172a" rx="10"/>
  ${["Contrast", "Readable fonts", "Keyboard nav", "Captions"].map(
    (t, i) =>
      `<rect x="${24 + i * 108}" y="50" width="96" height="90" rx="8" fill="#1e293b" stroke="#a78bfa"/><text x="${72 + i * 108}" y="100" fill="#e2e8f0" text-anchor="middle" font-size="10">${t}</text>`
  ).join("")}
</svg>`,

  hciProblems: `<svg viewBox="0 0 500 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="HCI problems and fixes">
  <rect width="500" height="220" fill="#0f172a" rx="10"/>
  <text x="130" y="32" fill="#fb7185" text-anchor="middle" font-size="13">Problems</text>
  <text x="370" y="32" fill="#5eead4" text-anchor="middle" font-size="13">Improvements (1.8)</text>
  ${["Complex UI", "No feedback", "Inconsistent"].map(
    (t, i) => `<text x="40" y="${70 + i * 28}" fill="#94a3b8" font-size="11">• ${t}</text>`
  ).join("")}
  ${["Clear nav", "Show results", "UCD + test"].map(
    (t, i) => `<text x="280" y="${70 + i * 28}" fill="#94a3b8" font-size="11">→ ${t}</text>`
  ).join("")}
</svg>`,

  uiUx: `<svg viewBox="0 0 520 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="UI vs UX">
  <rect width="520" height="200" fill="#0f172a" rx="10"/>
  <rect x="40" y="50" width="200" height="120" rx="12" fill="#312e81" stroke="#818cf8"/>
  <text x="140" y="85" fill="#c7d2fe" text-anchor="middle" font-size="14" font-weight="bold">UI</text>
  <text x="140" y="110" fill="#e2e8f0" text-anchor="middle" font-size="11">Buttons, layout, colors</text>
  <rect x="280" y="50" width="200" height="120" rx="12" fill="#064e3b" stroke="#34d399"/>
  <text x="380" y="85" fill="#a7f3d0" text-anchor="middle" font-size="14" font-weight="bold">UX</text>
  <text x="380" y="110" fill="#e2e8f0" text-anchor="middle" font-size="11">Feel, speed, satisfaction</text>
</svg>`,

  figmaProto: `<svg viewBox="0 0 480 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Wireframe to prototype">
  <rect width="480" height="200" fill="#0f172a" rx="10"/>
  <rect x="40" y="40" width="140" height="120" rx="6" fill="none" stroke="#94a3b8" stroke-dasharray="6 4"/>
  <text x="110" y="105" fill="#94a3b8" text-anchor="middle" font-size="12">Lo-Fi</text>
  <text x="250" y="105" fill="#ffd166" text-anchor="middle" font-size="20">→</text>
  <rect x="300" y="40" width="140" height="120" rx="6" fill="#1e293b" stroke="#5eead4"/>
  <rect x="320" y="60" width="100" height="20" rx="4" fill="#334155"/>
  <rect x="320" y="90" width="60" height="24" rx="6" fill="#ea580c"/>
  <text x="370" y="145" fill="#5eead4" text-anchor="middle" font-size="12">Hi-Fi / Figma</text>
</svg>`,

  testing: `<svg viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="HCI testing methods">
  <rect width="520" height="220" fill="#0f172a" rx="10"/>
  <rect x="40" y="50" width="200" height="130" rx="10" fill="#1e293b" stroke="#94a3b8"/>
  <text x="140" y="80" fill="#e2e8f0" text-anchor="middle" font-size="12">Version A</text>
  <rect x="280" y="50" width="200" height="130" rx="10" fill="#1e293b" stroke="#5eead4"/>
  <text x="380" y="80" fill="#e2e8f0" text-anchor="middle" font-size="12">Version B</text>
  <text x="260" y="200" fill="#ffd166" text-anchor="middle" font-size="12">A/B Testing — higher clicks/sign-ups wins</text>
</svg>`,

  traceTable: `<svg viewBox="0 0 540 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Trace table">
  <rect width="540" height="200" fill="#0f172a" rx="10"/>
  <text x="270" y="28" fill="#5eead4" text-anchor="middle" font-size="13">Trace Table (dry run)</text>
  ${["Step", "Total", "Height", "Condition"].map(
    (h, i) =>
      `<rect x="${40 + i * 120}" y="40" width="115" height="28" fill="#334155"/><text x="${97 + i * 120}" y="58" fill="#e2e8f0" text-anchor="middle" font-size="10">${h}</text>`
  ).join("")}
  ${[
    ["2", "0", "—", "—"],
    ["6", "1", "1.91", "T"],
    ["6", "2", "1.87", "T"],
  ].map((row, ri) =>
    row.map(
      (cell, ci) =>
        `<rect x="${40 + ci * 120}" y="${78 + ri * 32}" width="115" height="28" fill="#1e293b" stroke="#475569"/><text x="${97 + ci * 120}" y="${96 + ri * 32}" fill="#94a3b8" text-anchor="middle" font-size="10">${cell}</text>`
    ).join("")
  ).join("")}
</svg>`,

  bigO: `<svg viewBox="0 0 480 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Big O growth curves">
  <rect width="480" height="260" fill="#0f172a" rx="10"/>
  <line x1="60" y1="220" x2="420" y2="220" stroke="#64748b"/>
  <line x1="60" y1="220" x2="60" y2="40" stroke="#64748b"/>
  <text x="430" y="225" fill="#94a3b8" font-size="11">n</text>
  <text x="45" y="45" fill="#94a3b8" font-size="11">time</text>
  <path d="M60 210 L400 205" stroke="#34d399" stroke-width="2" fill="none"/>
  <text x="400" y="200" fill="#34d399" font-size="10">O(1)</text>
  <path d="M60 210 L400 120" stroke="#fbbf24" stroke-width="2" fill="none"/>
  <text x="400" y="115" fill="#fbbf24" font-size="10">O(n)</text>
  <path d="M60 210 Q200 200 400 50" stroke="#fb7185" stroke-width="2" fill="none"/>
  <text x="400" y="55" fill="#fb7185" font-size="10">O(n²)</text>
</svg>`,

  dataStructures: `<svg viewBox="0 0 520 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Stack and queue">
  <rect width="520" height="240" fill="#0f172a" rx="10"/>
  <text x="130" y="30" fill="#5eead4" text-anchor="middle" font-size="12">Stack (LIFO)</text>
  ${[0, 1, 2].map(
    (i) =>
      `<rect x="70" y="${160 - i * 36}" width="120" height="32" rx="4" fill="#334155" stroke="#94a3b8"/><text x="130" y="${180 - i * 36}" fill="#e2e8f0" text-anchor="middle" font-size="11">Data ${i + 1}</text>`
  ).join("")}
  <text x="390" y="30" fill="#ffd166" text-anchor="middle" font-size="12">Queue (FIFO)</text>
  ${["A", "B", "C"].map(
    (l, i) =>
      `<rect x="${300 + i * 44}" y="120" width="40" height="40" rx="4" fill="#334155" stroke="#5eead4"/><text x="${320 + i * 44}" y="145" fill="#e2e8f0" text-anchor="middle">${l}</text>`
  ).join("")}
  <text x="320" y="190" fill="#94a3b8" font-size="10">Front → Dequeue</text>
</svg>`,

  pythonCollections: `<svg viewBox="0 0 480 180" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Python collections">
  <rect width="480" height="180" fill="#0f172a" rx="10"/>
  ${[
    ["List []", "#3776ab"],
    ["Tuple ()", "#ffd166"],
    ["Set {}", "#34d399"],
    ["Dict {}", "#fb7185"],
  ]
    .map(
      ([t, c], i) =>
        `<rect x="${24 + i * 115}" y="50" width="105" height="90" rx="10" fill="#1e293b" stroke="${c}"/><text x="${76 + i * 115}" y="100" fill="#e2e8f0" text-anchor="middle" font-size="11">${t}</text>`
    )
    .join("")}
</svg>`,

  dataAnalysis: `<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Data analysis pipeline">
  <rect width="500" height="200" fill="#0f172a" rx="10"/>
  ${["SQLite DB", "Pandas", "DataFrame", "Insights"].map(
    (t, i) =>
      `<rect x="${30 + i * 118}" y="70" width="100" height="60" rx="8" fill="#1e293b" stroke="#5eead4"/><text x="${80 + i * 118}" y="105" fill="#e2e8f0" text-anchor="middle" font-size="10">${t}</text>${
        i < 3 ? `<text x="${142 + i * 118}" y="105" fill="#ffd166" font-size="16">→</text>` : ""
      }`
  ).join("")}
</svg>`,

  mlNn: `<svg viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Neural network">
  <rect width="520" height="220" fill="#0f172a" rx="10"/>
  ${[
    [80, 3],
    [260, 4],
    [440, 2],
  ]
    .map(([x, n]) =>
      Array.from({ length: n }, (_, i) => {
        const y = 60 + i * 35;
        return `<circle cx="${x}" cy="${y}" r="14" fill="#1e293b" stroke="#a78bfa"/>`;
      }).join("")
    )
    .join("")}
  <text x="80" y="30" fill="#94a3b8" text-anchor="middle" font-size="10">Input</text>
  <text x="260" y="30" fill="#94a3b8" text-anchor="middle" font-size="10">Hidden</text>
  <text x="440" y="30" fill="#94a3b8" text-anchor="middle" font-size="10">Output</text>
</svg>`,

  entrepreneurship: `<svg viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Entrepreneurship cycle">
  <rect width="500" height="200" fill="#0f172a" rx="10"/>
  ${["Problem", "Idea", "Prototype", "Launch"].map(
    (t, i) =>
      `<circle cx="${100 + i * 100}" cy="100" r="36" fill="#1e293b" stroke="#ffd166"/><text x="${100 + i * 100}" y="105" fill="#e2e8f0" text-anchor="middle" font-size="10">${t}</text>`
  ).join("")}
</svg>`,
};

export function renderDiagram(key) {
  return DIAGRAMS[key] || "";
}
