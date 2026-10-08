/* Inline SVG figures for the Teach Yourself lectures. */
(function () {
  const ink = "#14233a";
  const teal = "#0f6e6b";
  const gold = "#a15c12";
  const clay = "#c4491d";
  const paper = "#fffdf8";

  function box(x, y, w, h, fill, label, sub) {
    return `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="10" fill="${fill}" stroke="${ink}" stroke-width="1.5"/>
      <text x="${x + w / 2}" y="${y + (sub ? 28 : 36)}" text-anchor="middle" fill="${ink}" font-size="15" font-family="sans-serif">${label}</text>
      ${sub ? `<text x="${x + w / 2}" y="${y + 48}" text-anchor="middle" fill="${ink}" font-size="12" font-family="sans-serif">${sub}</text>` : ""}`;
  }

  const diagrams = {
    channels: () => `<svg viewBox="0 0 420 250" role="img" aria-label="Sensory channels">
      <circle cx="210" cy="125" r="46" fill="${teal}"/>
      <text x="210" y="122" text-anchor="middle" fill="white" font-size="16" font-family="sans-serif">Human</text>
      <text x="210" y="140" text-anchor="middle" fill="white" font-size="12" font-family="sans-serif">+ Computer</text>
      ${[
        [70, 40, "Sight"],
        [330, 40, "Touch"],
        [50, 190, "Hearing"],
        [350, 190, "Voice"],
        [210, 28, "Spatial"]
      ].map(([x, y, name]) => `<g><rect x="${x - 48}" y="${y - 16}" width="96" height="32" rx="8" fill="${paper}" stroke="${gold}"/>
        <text x="${x}" y="${y + 5}" text-anchor="middle" font-size="13" font-family="sans-serif" fill="${ink}">${name}</text></g>`).join("")}
    </svg>`,

    trad: () => `<svg viewBox="0 0 420 180" role="img" aria-label="Traditional and natural interaction">
      ${box(16, 30, 180, 120, "#e7f3f2", "Traditional", "mouse · keyboard")}
      ${box(224, 30, 180, 120, "#fff4e4", "Natural", "voice · gesture")}
    </svg>`,

    domains: () => `<svg viewBox="0 0 420 200" role="img" aria-label="HCI domains">
      ${box(16, 20, 180, 70, "#e7f3f2", "Health", "portal · telemedicine")}
      ${box(224, 20, 180, 70, "#fff4e4", "Banking", "app · ATM")}
      ${box(16, 110, 180, 70, "#fde8e4", "Education", "LMS · exam")}
      ${box(224, 110, 180, 70, "#e8eef8", "Network", "chat · Zoom")}
    </svg>`,

    ui: () => `<svg viewBox="0 0 420 200" role="img" aria-label="Interface types">
      ${box(12, 16, 120, 70, paper, "GUI", "windows")}
      ${box(150, 16, 120, 70, paper, "CLI", "text")}
      ${box(288, 16, 120, 70, paper, "Touch", "tap")}
      ${box(80, 108, 120, 70, "#fff4e4", "VUI", "speech")}
      ${box(220, 108, 120, 70, "#e7f3f2", "NUI", "gesture")}
    </svg>`,

    wire: () => `<svg viewBox="0 0 420 210" role="img" aria-label="Low and high fidelity">
      <rect x="30" y="20" width="140" height="170" rx="12" fill="white" stroke="${ink}"/>
      <rect x="46" y="40" width="108" height="16" fill="#ddd"/>
      <rect x="46" y="70" width="108" height="36" fill="none" stroke="${ink}"/>
      <rect x="46" y="120" width="108" height="28" fill="none" stroke="${ink}"/>
      <text x="100" y="206" text-anchor="middle" font-size="12" font-family="sans-serif">Lo-fi</text>
      <rect x="230" y="20" width="150" height="170" rx="16" fill="#14233a"/>
      <rect x="246" y="40" width="118" height="18" rx="4" fill="${teal}"/>
      <rect x="246" y="72" width="118" height="40" rx="6" fill="white"/>
      <rect x="246" y="126" width="118" height="32" rx="8" fill="${clay}"/>
      <text x="305" y="206" text-anchor="middle" font-size="12" font-family="sans-serif">Hi-fi</text>
    </svg>`,

    bigo: () => `<svg viewBox="0 0 420 220" role="img" aria-label="Big O growth">
      <line x1="50" y1="180" x2="390" y2="180" stroke="${ink}"/>
      <line x1="50" y1="180" x2="50" y2="20" stroke="${ink}"/>
      <text x="390" y="198" font-size="12" font-family="sans-serif">n</text>
      <path d="M50 150 H390" fill="none" stroke="${teal}" stroke-width="3"/>
      <text x="300" y="142" font-size="12" fill="${teal}" font-family="sans-serif">O(1)</text>
      <path d="M50 168 C 150 160, 250 120, 390 70" fill="none" stroke="${gold}" stroke-width="3"/>
      <text x="300" y="78" font-size="12" fill="${gold}" font-family="sans-serif">O(n)</text>
      <path d="M50 172 C 140 170, 220 150, 390 24" fill="none" stroke="${clay}" stroke-width="3"/>
      <text x="330" y="36" font-size="12" fill="${clay}" font-family="sans-serif">O(n²)</text>
    </svg>`,

    array: () => `<svg viewBox="0 0 420 120" role="img" aria-label="Array cells">
      ${[0, 1, 2, 3, 4].map((i) => `<g>
        <rect x="${20 + i * 78}" y="30" width="70" height="50" fill="${i === 2 ? "#fff4e4" : "white"}" stroke="${ink}"/>
        <text x="${55 + i * 78}" y="60" text-anchor="middle" font-family="sans-serif" font-size="16">${10 + i * 10}</text>
        <text x="${55 + i * 78}" y="100" text-anchor="middle" font-family="sans-serif" font-size="12" fill="${teal}">[${i}]</text>
      </g>`).join("")}
    </svg>`,

    list: () => `<svg viewBox="0 0 420 130" role="img" aria-label="Linked list">
      ${[0, 1, 2].map((i) => {
        const x = 20 + i * 130;
        return `<rect x="${x}" y="36" width="90" height="48" rx="8" fill="white" stroke="${ink}"/>
          <text x="${x + 32}" y="66" font-family="sans-serif" font-size="16">${["Ali", "Sara", "Omar"][i]}</text>
          <polygon points="${x + 78},52 ${x + 88},60 ${x + 78},68" fill="${teal}"/>
          ${i < 2 ? `<line x1="${x + 90}" y1="60" x2="${x + 130}" y2="60" stroke="${teal}" stroke-width="2"/>` : `<text x="${x + 96}" y="64" font-size="12" font-family="sans-serif">null</text>`}`;
      }).join("")}
    </svg>`,

    stack: () => `<svg viewBox="0 0 420 220" role="img" aria-label="Stack LIFO">
      <text x="70" y="24" font-family="sans-serif" font-size="14" fill="${clay}">POP ↑</text>
      <text x="150" y="24" font-family="sans-serif" font-size="14" fill="${teal}">PUSH ↓</text>
      ${box(40, 40, 160, 42, "#fff4e4", "C  ← top", "")}
      ${box(40, 90, 160, 42, "white", "B", "")}
      ${box(40, 140, 160, 42, "white", "A", "")}
      <text x="280" y="110" font-family="sans-serif" font-size="16">LIFO</text>
      <text x="250" y="136" font-family="sans-serif" font-size="13">last in, first out</text>
    </svg>`,

    queue: () => `<svg viewBox="0 0 420 140" role="img" aria-label="Queue FIFO">
      <text x="30" y="24" font-family="sans-serif" font-size="13" fill="${clay}">front / dequeue</text>
      <text x="270" y="24" font-family="sans-serif" font-size="13" fill="${teal}">rear / enqueue</text>
      ${["A", "B", "C", "D"].map((name, i) => box(24 + i * 96, 46, 84, 56, i === 0 ? "#fde8e4" : "white", name, "")).join("")}
    </svg>`,

    tree: () => `<svg viewBox="0 0 420 210" role="img" aria-label="Tree">
      <line x1="210" y1="48" x2="110" y2="100" stroke="${ink}"/>
      <line x1="210" y1="48" x2="310" y2="100" stroke="${ink}"/>
      <line x1="110" y1="116" x2="60" y2="164" stroke="${ink}"/>
      <line x1="110" y1="116" x2="160" y2="164" stroke="${ink}"/>
      ${[
        [210, 36, "Root"],
        [110, 108, "Left"],
        [310, 108, "Right"],
        [60, 176, "L1"],
        [160, 176, "L2"]
      ].map(([x, y, name]) => `<g><circle cx="${x}" cy="${y}" r="22" fill="${name === "Root" ? teal : paper}" stroke="${ink}"/>
        <text x="${x}" y="${y + 4}" text-anchor="middle" font-size="11" font-family="sans-serif" fill="${name === "Root" ? "white" : ink}">${name}</text></g>`).join("")}
    </svg>`,

    graph: () => `<svg viewBox="0 0 420 200" role="img" aria-label="Graph">
      <line x1="80" y1="60" x2="210" y2="40" stroke="${ink}"/>
      <line x1="210" y1="40" x2="330" y2="80" stroke="${ink}"/>
      <line x1="80" y1="60" x2="120" y2="150" stroke="${ink}"/>
      <line x1="120" y1="150" x2="250" y2="150" stroke="${ink}"/>
      <line x1="250" y1="150" x2="330" y2="80" stroke="${ink}"/>
      <line x1="210" y1="40" x2="250" y2="150" stroke="${gold}"/>
      ${[[80, 60, "A"], [210, 40, "B"], [330, 80, "C"], [120, 150, "D"], [250, 150, "E"]].map(([x, y, name]) =>
        `<g><circle cx="${x}" cy="${y}" r="18" fill="white" stroke="${teal}" stroke-width="2"/>
          <text x="${x}" y="${y + 4}" text-anchor="middle" font-family="sans-serif">${name}</text></g>`).join("")}
    </svg>`,

    sets: () => `<svg viewBox="0 0 420 180" role="img" aria-label="Set union and intersection">
      <circle cx="170" cy="90" r="60" fill="#0f6e6b" fill-opacity="0.25" stroke="${teal}" stroke-width="2"/>
      <circle cx="240" cy="90" r="60" fill="${gold}" fill-opacity="0.25" stroke="${gold}" stroke-width="2"/>
      <text x="130" y="94" font-family="sans-serif" font-size="16">A</text>
      <text x="270" y="94" font-family="sans-serif" font-size="16">B</text>
      <text x="198" y="94" font-family="sans-serif" font-size="13">A∩B</text>
    </svg>`,

    func: () => `<svg viewBox="0 0 420 120" role="img" aria-label="Function input and output">
      ${box(16, 34, 100, 52, paper, "input", "")}
      <polygon points="130,60 160,50 160,70" fill="${teal}"/>
      ${box(170, 28, 110, 64, "#e7f3f2", "function", "")}
      <polygon points="294,60 324,50 324,70" fill="${teal}"/>
      ${box(330, 34, 74, 52, "#fff4e4", "return", "")}
    </svg>`,

    file: () => `<svg viewBox="0 0 420 140" role="img" aria-label="File modes">
      ${box(16, 36, 120, 70, paper, "r", "read")}
      ${box(150, 36, 120, 70, "#fde8e4", "w", "write")}
      ${box(284, 36, 120, 70, "#e7f3f2", "a", "append")}
    </svg>`,

    db: () => `<svg viewBox="0 0 420 160" role="img" aria-label="Database connection">
      ${box(16, 48, 110, 60, paper, "Python", "")}
      <line x1="126" y1="78" x2="160" y2="78" stroke="${ink}" stroke-width="2"/>
      ${box(160, 40, 110, 76, "#fff4e4", "connect", "cursor")}
      <line x1="270" y1="78" x2="300" y2="78" stroke="${ink}" stroke-width="2"/>
      <ellipse cx="350" cy="70" rx="46" ry="18" fill="${teal}"/>
      <rect x="304" y="70" width="92" height="36" fill="${teal}"/>
      <ellipse cx="350" cy="106" rx="46" ry="18" fill="#0b4f4d"/>
      <text x="350" y="78" text-anchor="middle" fill="white" font-size="12" font-family="sans-serif">SQLite</text>
    </svg>`,

    frame: () => `<svg viewBox="0 0 420 150" role="img" aria-label="DataFrame">
      <rect x="20" y="20" width="380" height="110" fill="white" stroke="${ink}"/>
      ${["name", "marks", "city"].map((h, i) => `<text x="${80 + i * 120}" y="48" text-anchor="middle" font-family="sans-serif" font-size="14" fill="${teal}">${h}</text>`).join("")}
      <line x1="20" y1="60" x2="400" y2="60" stroke="${ink}"/>
      ${["Ayesha", "78", "Hyderabad"].map((v, i) => `<text x="${80 + i * 120}" y="92" text-anchor="middle" font-family="sans-serif" font-size="14">${v}</text>`).join("")}
      ${["Bilal", "NaN", "Sukkur"].map((v, i) => `<text x="${80 + i * 120}" y="116" text-anchor="middle" font-family="sans-serif" font-size="14" fill="${v === "NaN" ? clay : ink}">${v}</text>`).join("")}
    </svg>`,

    charts: () => `<svg viewBox="0 0 420 180" role="img" aria-label="Chart types">
      <rect x="30" y="90" width="24" height="60" fill="${teal}"/>
      <rect x="60" y="60" width="24" height="90" fill="${gold}"/>
      <rect x="90" y="110" width="24" height="40" fill="${clay}"/>
      <line x1="150" y1="150" x2="250" y2="40" stroke="${teal}" stroke-width="3"/>
      <circle cx="170" cy="128" r="4" fill="${ink}"/>
      <circle cx="210" cy="84" r="4" fill="${ink}"/>
      <circle cx="250" cy="40" r="4" fill="${ink}"/>
      <path d="M300 150 A 50 50 0 0 1 380 90 L 340 90 Z" fill="${teal}"/>
      <path d="M300 150 A 50 50 0 0 0 360 150 L 340 90 Z" fill="${gold}"/>
      <text x="70" y="172" font-size="11" font-family="sans-serif">bar</text>
      <text x="185" y="172" font-size="11" font-family="sans-serif">line</text>
      <text x="320" y="172" font-size="11" font-family="sans-serif">pie</text>
    </svg>`,

    neuron: () => `<svg viewBox="0 0 420 200" role="img" aria-label="Neuron weighted sum">
      ${[40, 90, 140].map((y, i) => `<g>
        <circle cx="50" cy="${y}" r="16" fill="white" stroke="${ink}"/>
        <text x="50" y="${y + 4}" text-anchor="middle" font-size="12" font-family="sans-serif">x${i + 1}</text>
        <line x1="66" y1="${y}" x2="190" y2="100" stroke="${teal}"/>
      </g>`).join("")}
      <circle cx="210" cy="100" r="28" fill="${teal}"/>
      <text x="210" y="96" text-anchor="middle" fill="white" font-size="11" font-family="sans-serif">Σw x</text>
      <text x="210" y="112" text-anchor="middle" fill="white" font-size="11" font-family="sans-serif">+ b</text>
      <line x1="238" y1="100" x2="300" y2="100" stroke="${ink}" stroke-width="2"/>
      <rect x="300" y="76" width="90" height="48" rx="10" fill="#fff4e4" stroke="${gold}"/>
      <text x="345" y="105" text-anchor="middle" font-size="13" font-family="sans-serif">σ(z)</text>
    </svg>`,

    layers: () => `<svg viewBox="0 0 420 200" role="img" aria-label="Neural network layers">
      ${[
        [40, [50, 100, 150], "input"],
        [160, [40, 80, 120, 160], "hidden"],
        [280, [60, 120, 160], "hidden"],
        [380, [100], "output"]
      ].map(([x, ys, kind]) => ys.map((y) => {
        const prev = kind === "input" ? [] : [40, 80, 120];
        return `<circle cx="${x}" cy="${y}" r="12" fill="${kind === "output" ? clay : kind === "input" ? teal : paper}" stroke="${ink}"/>`;
      }).join("")).join("")}
      <line x1="52" y1="50" x2="148" y2="40" stroke="#9bb" />
      <line x1="52" y1="100" x2="148" y2="80" stroke="#9bb"/>
      <line x1="52" y1="150" x2="148" y2="160" stroke="#9bb"/>
      <line x1="172" y1="80" x2="268" y2="60" stroke="#9bb"/>
      <line x1="172" y1="120" x2="268" y2="120" stroke="#9bb"/>
      <line x1="292" y1="120" x2="368" y2="100" stroke="${gold}" stroke-width="2"/>
      <text x="40" y="190" font-size="11" font-family="sans-serif">input</text>
      <text x="180" y="190" font-size="11" font-family="sans-serif">hidden</text>
      <text x="360" y="190" font-size="11" font-family="sans-serif">out</text>
    </svg>`,

    shield: () => `<svg viewBox="0 0 420 180" role="img" aria-label="Protection layers">
      <path d="M210 20 L320 55 V100 C320 145 210 168 210 168 C210 168 100 145 100 100 V55 Z" fill="#e7f3f2" stroke="${teal}" stroke-width="2"/>
      <text x="210" y="90" text-anchor="middle" font-family="sans-serif" font-size="16">auth</text>
      <text x="210" y="112" text-anchor="middle" font-family="sans-serif" font-size="14">encrypt · backup</text>
    </svg>`,

    equity: () => `<svg viewBox="0 0 420 170" role="img" aria-label="Equal access and equity">
      ${box(16, 30, 180, 110, paper, "Equal access", "same login")}
      ${box(220, 30, 180, 110, "#fff4e4", "Equity", "captions + support")}
    </svg>`,

    cycle: () => `<svg viewBox="0 0 420 180" role="img" aria-label="Prototype cycle">
      ${["Design", "Build", "Test", "Iterate"].map((name, i) => {
        const x = 20 + (i % 4) * 100;
        return `${box(x, 50, 90, 64, i === 3 ? "#fff4e4" : "white", name, "")}
          ${i < 3 ? `<polygon points="${x + 92},82 ${x + 102},74 ${x + 102},90" fill="${teal}"/>` : ""}`;
      }).join("")}
    </svg>`,

    mvp: () => `<svg viewBox="0 0 420 160" role="img" aria-label="Prototype versus MVP">
      ${box(20, 36, 170, 90, paper, "Prototype", "show the idea")}
      ${box(220, 36, 180, 90, "#e7f3f2", "MVP", "smallest working use")}
    </svg>`,

    beach: () => `<svg viewBox="0 0 420 170" role="img" aria-label="Beachhead market">
      <circle cx="210" cy="88" r="70" fill="none" stroke="#ddd" stroke-width="10"/>
      <circle cx="210" cy="88" r="42" fill="none" stroke="#e2d6c4" stroke-width="10"/>
      <circle cx="210" cy="88" r="18" fill="${clay}"/>
      <text x="210" y="92" text-anchor="middle" fill="white" font-size="10" font-family="sans-serif">first</text>
      <text x="210" y="20" text-anchor="middle" font-size="12" font-family="sans-serif">everyone</text>
    </svg>`
  };

  window.DIAGRAMS = diagrams;
})();
