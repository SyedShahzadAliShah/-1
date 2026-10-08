/** Inline SVG diagrams — no external images. */

const C = {
  bg: "#12202c",
  line: "#3dd6f5",
  gold: "#f0b429",
  text: "#e8edf4",
  fill: "#0f172a"
};

function wrap(inner, w = 420, h = 200, label = "") {
  return `<svg viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="${label}">
    <rect width="${w}" height="${h}" fill="${C.bg}" rx="10"/>
    ${inner}
  </svg>`;
}

function gateBody(kind) {
  if (kind === "or") {
    return `<path d="M70,40 Q108,70 70,100 Q118,70 70,40" fill="none" stroke="${C.line}" stroke-width="2.4"/>`;
  }
  if (kind === "not") {
    return `<polygon points="70,45 70,95 118,70" fill="none" stroke="${C.line}" stroke-width="2.4"/>
      <circle cx="126" cy="70" r="7" fill="${C.bg}" stroke="${C.line}" stroke-width="2"/>`;
  }
  return `<path d="M70,40 L70,100 L108,100 Q138,70 108,40 Z" fill="none" stroke="${C.line}" stroke-width="2.4"/>`;
}

function twoInputGate(name, expr, kind, bubble = false) {
  const outX = bubble || kind === "not" ? 136 : 138;
  const bub = bubble
    ? `<circle cx="146" cy="70" r="7" fill="${C.bg}" stroke="${C.gold}" stroke-width="2"/>`
    : "";
  const y1 = kind === "not" ? 70 : 52;
  const y2 = kind === "not" ? 70 : 88;
  const inB = kind === "not"
    ? ""
    : `<line x1="18" y1="${y2}" x2="70" y2="${y2}" stroke="${C.line}" stroke-width="2"/><text x="8" y="${y2 + 4}" fill="${C.text}" font-size="12">B</text>`;
  return wrap(`
    <text x="210" y="24" fill="${C.gold}" font-size="14" text-anchor="middle">${name} · ${expr}</text>
    <line x1="18" y1="${y1}" x2="70" y2="${y1}" stroke="${C.line}" stroke-width="2"/>
    <text x="8" y="${y1 + 4}" fill="${C.text}" font-size="12">A</text>
    ${inB}
    ${gateBody(kind)}
    ${bub}
    <line x1="${outX}" y1="70" x2="250" y2="70" stroke="${C.line}" stroke-width="2"/>
    <text x="258" y="75" fill="${C.text}" font-size="13">Y</text>
  `, 320, 140, name);
}

function tableSvg(rows, caption) {
  const cw = 54;
  const ch = 26;
  const cells = rows.map((row, ri) => row.map((cell, ci) => `
    <rect x="${20 + ci * cw}" y="${36 + ri * ch}" width="${cw}" height="${ch}" fill="${ri === 0 ? C.fill : "none"}" stroke="${C.line}"/>
    <text x="${20 + ci * cw + cw / 2}" y="${54 + ri * ch}" fill="${C.text}" font-size="12" text-anchor="middle">${cell}</text>
  `).join("")).join("");
  return wrap(`<text x="50%" y="22" fill="${C.gold}" font-size="13" text-anchor="middle">${caption}</text>${cells}`, 20 + rows[0].length * cw + 20, 50 + rows.length * ch, caption);
}

const DIAGRAMS = {
  stairsRamp: {
    caption: "Discrete = سیڑھیاں (مقرر قدم)۔ Continuous = ramp پر کوئی بھی نقطہ۔",
    svg: wrap(`
      <text x="105" y="28" fill="${C.gold}" font-size="13" text-anchor="middle">Discrete</text>
      <polyline points="24,168 24,138 58,138 58,108 92,108 92,78 126,78 126,48" fill="none" stroke="${C.line}" stroke-width="3"/>
      <text x="310" y="28" fill="${C.gold}" font-size="13" text-anchor="middle">Continuous</text>
      <line x1="210" y1="168" x2="400" y2="42" stroke="${C.gold}" stroke-width="3"/>
    `, 420, 190, "Stairs vs ramp")
  },
  binaryBits: {
    caption: "ڈیجیٹل سسٹم صرف bit: 0 (OFF/FALSE) اور 1 (ON/TRUE)۔",
    svg: wrap(`
      <circle cx="110" cy="90" r="42" fill="${C.fill}" stroke="${C.line}" stroke-width="2"/>
      <text x="110" y="100" fill="${C.text}" font-size="32" text-anchor="middle">0</text>
      <text x="110" y="150" fill="${C.text}" font-size="12" text-anchor="middle">OFF / LOW / FALSE</text>
      <circle cx="300" cy="90" r="42" fill="${C.fill}" stroke="${C.gold}" stroke-width="2"/>
      <text x="300" y="100" fill="${C.gold}" font-size="32" text-anchor="middle">1</text>
      <text x="300" y="150" fill="${C.text}" font-size="12" text-anchor="middle">ON / HIGH / TRUE</text>
    `, 420, 180, "Bits")
  },
  analogDigitalWaves: {
    caption: "Analog: sine wave۔ Digital: square wave HIGH/LOW۔",
    svg: wrap(`
      <text x="110" y="24" fill="${C.gold}" font-size="13" text-anchor="middle">Analog</text>
      <path d="M20,110 Q55,40 90,110 T160,110 T230,110" fill="none" stroke="${C.line}" stroke-width="2.4"/>
      <text x="330" y="24" fill="${C.gold}" font-size="13" text-anchor="middle">Digital</text>
      <polyline points="250,150 250,60 290,60 290,150 330,150 330,60 370,60 370,150 410,150" fill="none" stroke="${C.gold}" stroke-width="2.4"/>
      <text x="300" y="52" fill="${C.text}" font-size="10">HIGH(1)</text>
      <text x="300" y="168" fill="${C.text}" font-size="10">LOW(0)</text>
    `, 430, 190, "Analog vs digital")
  },
  gateAND: { caption: "AND: آؤٹ پٹ 1 صرف جب تمام ان پٹ 1 ہوں۔", svg: twoInputGate("AND", "Y = A · B", "and") },
  gateOR: { caption: "OR: کوئی ایک ان پٹ 1 ہو تو آؤٹ پٹ 1۔", svg: twoInputGate("OR", "Y = A + B", "or") },
  gateNOT: { caption: "NOT: unary — ان پٹ الٹ جاتا ہے۔", svg: twoInputGate("NOT", "Y = A'", "not") },
  gateNAND: { caption: "NAND = NOT AND — یونیورسل گیٹ۔", svg: twoInputGate("NAND", "Y = (A · B)'", "and", true) },
  gateNOR: { caption: "NOR = NOT OR — یونیورسل گیٹ۔", svg: twoInputGate("NOR", "Y = (A + B)'", "or", true) },
  gateXOR: { caption: "XOR: ان پٹ مختلف ہوں تو 1۔", svg: twoInputGate("XOR", "Y = A ⊕ B", "or") },
  gatesOverview: {
    caption: "لاجک گیٹس ڈیجیٹل سرکٹ کی اینٹیں ہیں۔",
    svg: wrap(["AND", "OR", "NOT", "NAND", "XOR"].map((n, i) => `
      <g transform="translate(${18 + i * 80},70)">
        <rect width="70" height="44" rx="8" fill="${C.fill}" stroke="${i === 3 ? C.gold : C.line}"/>
        <text x="35" y="28" fill="${C.text}" font-size="13" text-anchor="middle">${n}</text>
      </g>`).join(""), 420, 170, "Gates")
  },
  truthTable2: {
    caption: "n ان پٹ → قطاریں 2^n۔",
    svg: tableSvg([["A", "B", "Y"], ["0", "0", "0"], ["0", "1", "0"], ["1", "0", "0"], ["1", "1", "1"]], "AND truth table")
  },
  kmap3var: {
    caption: "K-Map: ملحق 1s کو 2 کی طاقتوں میں گروپ کریں۔",
    svg: wrap(`
      <text x="210" y="22" fill="${C.gold}" font-size="13" text-anchor="middle">3-variable K-Map · Gray code</text>
      <text x="70" y="58" fill="${C.text}" font-size="11">C\\AB</text>
      ${["00", "01", "11", "10"].map((t, i) => `<text x="${130 + i * 50}" y="58" fill="${C.text}" font-size="12">${t}</text>`).join("")}
      ${["0", "1"].map((r, ri) => `
        <text x="78" y="${88 + ri * 40}" fill="${C.text}" font-size="12">${r}</text>
        ${[0, 1, 1, 0].map((v, ci) => `
          <rect x="${112 + ci * 50}" y="${68 + ri * 40}" width="44" height="34" fill="${C.fill}" stroke="${C.line}"/>
          <text x="${134 + ci * 50}" y="${90 + ri * 40}" fill="${v && ri ? C.gold : C.text}" font-size="14" text-anchor="middle">${ri === 0 ? [0, 1, 1, 0][ci] : [0, 1, 1, 0][ci]}</text>
        `).join("")}
      `).join("")}
      <rect x="158" y="104" width="96" height="40" fill="none" stroke="${C.gold}" stroke-dasharray="4" stroke-width="2"/>
    `, 420, 200, "K-map")
  },
  logicDiagram: {
    caption: "Y = A · B + C — پہلے AND (اعلیٰ precedence)، پھر OR۔",
    svg: wrap(`
      <text x="30" y="48" fill="${C.text}">A</text><line x1="48" y1="44" x2="110" y2="44" stroke="${C.line}"/>
      <text x="30" y="88" fill="${C.text}">B</text><line x1="48" y1="84" x2="110" y2="84" stroke="${C.line}"/>
      <rect x="110" y="34" width="70" height="60" rx="8" fill="${C.fill}" stroke="${C.line}"/><text x="145" y="68" fill="${C.text}" text-anchor="middle">AND</text>
      <text x="30" y="150" fill="${C.text}">C</text>
      <line x1="180" y1="64" x2="240" y2="64" stroke="${C.line}"/>
      <line x1="48" y1="146" x2="240" y2="146" stroke="${C.line}"/>
      <rect x="240" y="50" width="70" height="110" rx="8" fill="${C.fill}" stroke="${C.gold}"/><text x="275" y="110" fill="${C.gold}" text-anchor="middle">OR</text>
      <line x1="310" y1="105" x2="380" y2="105" stroke="${C.line}"/><text x="388" y="110" fill="${C.text}">Y</text>
    `, 430, 180, "Logic diagram")
  },
  logisim: {
    caption: "Logisim: گیٹ رکھیں، تار جوڑیں، Poke سے 0/1 چیک کریں۔",
    svg: wrap(`
      <rect x="30" y="40" width="90" height="40" rx="6" fill="${C.fill}" stroke="${C.line}"/><text x="75" y="65" fill="${C.text}" text-anchor="middle" font-size="12">Input A</text>
      <rect x="30" y="110" width="90" height="40" rx="6" fill="${C.fill}" stroke="${C.line}"/><text x="75" y="135" fill="${C.text}" text-anchor="middle" font-size="12">Input B</text>
      <rect x="170" y="70" width="90" height="50" rx="6" fill="${C.fill}" stroke="${C.gold}"/><text x="215" y="100" fill="${C.gold}" text-anchor="middle">AND</text>
      <rect x="310" y="75" width="90" height="40" rx="6" fill="${C.fill}" stroke="${C.line}"/><text x="355" y="100" fill="${C.text}" text-anchor="middle" font-size="12">Output</text>
      <line x1="120" y1="60" x2="170" y2="85" stroke="${C.line}"/>
      <line x1="120" y1="130" x2="170" y2="105" stroke="${C.line}"/>
      <line x1="260" y1="95" x2="310" y2="95" stroke="${C.line}"/>
    `, 430, 180, "Logisim")
  },
  sdlc: {
    caption: "SDLC: Requirement → Design → Code → Test → Deploy → Maintain",
    svg: wrap(["Req", "Design", "Code", "Test", "Deploy", "Fix"].map((l, i) => `
      <rect x="${12 + i * 68}" y="70" width="62" height="44" rx="8" fill="${C.fill}" stroke="${i % 2 ? C.gold : C.line}"/>
      <text x="${43 + i * 68}" y="97" fill="${C.text}" font-size="11" text-anchor="middle">${l}</text>
    `).join(""), 430, 170, "SDLC")
  },
  waterfallAgile: {
    caption: "Waterfall ترتیب وار؛ Agile چھوٹے sprint چکروں میں۔",
    svg: wrap(`
      <text x="100" y="28" fill="${C.gold}" font-size="13" text-anchor="middle">Waterfall</text>
      ${[0, 1, 2, 3].map((i) => `<rect x="40" y="${46 + i * 32}" width="120" height="24" rx="5" fill="${C.fill}" stroke="${C.line}"/>`).join("")}
      <text x="310" y="28" fill="${C.gold}" font-size="13" text-anchor="middle">Agile</text>
      <circle cx="310" cy="110" r="52" fill="none" stroke="${C.gold}" stroke-width="2.4"/>
      <text x="310" y="114" fill="${C.text}" font-size="12" text-anchor="middle">Sprint</text>
    `, 430, 190, "Waterfall vs Agile")
  },
  osi7: {
    caption: "OSI: Application سے Physical تک سات پرتیں۔",
    svg: wrap(
      ["Application", "Presentation", "Session", "Transport", "Network", "Data Link", "Physical"].map((l, i) => `
        <rect x="80" y="${18 + i * 28}" width="220" height="24" rx="4" fill="${C.fill}" stroke="${i === 0 || i === 3 || i === 6 ? C.gold : C.line}"/>
        <text x="190" y="${35 + i * 28}" fill="${C.text}" font-size="12" text-anchor="middle">${7 - i}. ${l}</text>
      `).join(""),
      380, 230, "OSI"
    )
  },
  tcpOsi: {
    caption: "TCP/IP چار پرتیں OSI سات پرتوں پر map ہوتی ہیں۔",
    svg: wrap(`
      <text x="90" y="24" fill="${C.gold}" font-size="13" text-anchor="middle">TCP/IP</text>
      <text x="280" y="24" fill="${C.gold}" font-size="13" text-anchor="middle">OSI 7</text>
      <rect x="30" y="40" width="120" height="70" rx="6" fill="${C.fill}" stroke="${C.line}"/><text x="90" y="80" fill="${C.text}" font-size="11" text-anchor="middle">Application</text>
      <rect x="30" y="118" width="120" height="28" rx="6" fill="${C.fill}" stroke="${C.line}"/><text x="90" y="137" fill="${C.text}" font-size="11" text-anchor="middle">Transport</text>
      <rect x="30" y="154" width="120" height="28" rx="6" fill="${C.fill}" stroke="${C.gold}"/><text x="90" y="173" fill="${C.text}" font-size="11" text-anchor="middle">Internet</text>
      <rect x="220" y="40" width="120" height="150" rx="6" fill="${C.fill}" stroke="${C.line}"/><text x="280" y="120" fill="${C.text}" font-size="11" text-anchor="middle">7 layers</text>
    `, 380, 210, "TCP/IP vs OSI")
  },
  decomposition: {
    caption: "بڑا مسئلہ چھوٹے sub-tasks میں توڑیں۔",
    svg: wrap(`
      <rect x="150" y="16" width="120" height="32" rx="8" fill="${C.fill}" stroke="${C.gold}"/><text x="210" y="37" fill="${C.text}" text-anchor="middle">مسئلہ</text>
      <line x1="210" y1="48" x2="210" y2="70" stroke="${C.line}"/>
      <line x1="70" y1="70" x2="350" y2="70" stroke="${C.line}"/>
      ${[70, 210, 350].map((x, i) => `
        <line x1="${x}" y1="70" x2="${x}" y2="90" stroke="${C.line}"/>
        <rect x="${x - 48}" y="90" width="96" height="36" rx="6" fill="${C.fill}" stroke="${C.line}"/>
        <text x="${x}" y="113" fill="${C.text}" font-size="12" text-anchor="middle">حصہ ${i + 1}</text>
      `).join("")}
    `, 420, 160, "Decomposition")
  },
  bubbleSort: {
    caption: "Bubble sort: ملحق جوڑے swap جب تک ترتیب نہ ہو۔",
    svg: wrap([8, 4, 1, 9, 3].map((n, i) => `
      <rect x="${30 + i * 76}" y="${140 - n * 10}" width="58" height="${n * 10}" fill="${i < 2 ? C.gold : "#334155"}"/>
      <text x="${59 + i * 76}" y="168" fill="${C.text}" text-anchor="middle">${n}</text>
    `).join(""), 420, 190, "Bubble sort")
  },
  selectionSort: {
    caption: "Selection sort: باقی فہرست سے سب سے چھوٹا چنیں۔",
    svg: wrap([1, 4, 8, 9, 3].map((n, i) => `
      <rect x="${30 + i * 76}" y="${140 - n * 10}" width="58" height="${n * 10}" fill="${i === 0 ? C.gold : "#334155"}"/>
      <text x="${59 + i * 76}" y="168" fill="${C.text}" text-anchor="middle">${n}</text>
    `).join(""), 420, 190, "Selection sort")
  },
  binarySearch: {
    caption: "Binary search: ترتیب شدہ فہرست — درمیان کاٹیں۔",
    svg: wrap(
      [1, 2, 3, 4, 5, 6, 7, 8].map((n, i) => `
        <rect x="${18 + i * 48}" y="60" width="40" height="40" fill="${n === 3 ? C.gold : C.fill}" stroke="${C.line}"/>
        <text x="${38 + i * 48}" y="86" fill="${n === 3 ? "#12202c" : C.text}" text-anchor="middle">${n}</text>
      `).join("") + `<text x="210" y="140" fill="${C.gold}" font-size="12" text-anchor="middle">mid → بائیں یا دائیں</text>`,
      420, 170, "Binary search"
    )
  },
  pythonIO: {
    caption: "Python: input() اندر، print() باہر۔",
    svg: wrap(`
      <rect x="30" y="50" width="110" height="70" rx="8" fill="${C.fill}" stroke="${C.line}"/><text x="85" y="90" fill="${C.text}" text-anchor="middle">input()</text>
      <rect x="155" y="40" width="110" height="90" rx="8" fill="${C.fill}" stroke="${C.gold}"/><text x="210" y="90" fill="${C.gold}" text-anchor="middle">Program</text>
      <rect x="280" y="50" width="110" height="70" rx="8" fill="${C.fill}" stroke="${C.line}"/><text x="335" y="90" fill="${C.text}" text-anchor="middle">print()</text>
    `, 420, 160, "Python I/O")
  },
  erModel: {
    caption: "ER: Rectangle = Entity، Oval = Attribute، Diamond = Relationship۔",
    svg: wrap(`
      <rect x="40" y="70" width="110" height="46" fill="${C.fill}" stroke="${C.line}"/><text x="95" y="98" fill="${C.text}" text-anchor="middle">STUDENT</text>
      <polygon points="210,60 270,93 210,126 150,93" fill="${C.fill}" stroke="${C.gold}"/><text x="210" y="98" fill="${C.gold}" text-anchor="middle" font-size="12">enrolls</text>
      <rect x="290" y="70" width="110" height="46" fill="${C.fill}" stroke="${C.line}"/><text x="345" y="98" fill="${C.text}" text-anchor="middle">COURSE</text>
      <ellipse cx="95" cy="40" rx="50" ry="18" fill="${C.fill}" stroke="${C.line}"/><text x="95" y="44" fill="${C.text}" font-size="11" text-anchor="middle">RollNo</text>
    `, 430, 160, "ER")
  },
  keys: {
    caption: "Primary Key منفرد؛ Foreign Key دوسری ٹیبل سے جوڑتی ہے۔",
    svg: wrap(`
      <rect x="30" y="40" width="160" height="110" rx="8" fill="${C.fill}" stroke="${C.line}"/>
      <text x="110" y="64" fill="${C.gold}" text-anchor="middle">Student</text>
      <text x="110" y="92" fill="${C.text}" font-size="12" text-anchor="middle">PK · RollNo</text>
      <text x="110" y="118" fill="${C.text}" font-size="12" text-anchor="middle">Name</text>
      <rect x="230" y="40" width="160" height="110" rx="8" fill="${C.fill}" stroke="${C.gold}"/>
      <text x="310" y="64" fill="${C.gold}" text-anchor="middle">Enrollment</text>
      <text x="310" y="92" fill="${C.text}" font-size="12" text-anchor="middle">FK · RollNo</text>
      <text x="310" y="118" fill="${C.text}" font-size="12" text-anchor="middle">CourseID</text>
    `, 420, 180, "Keys")
  },
  iot: {
    caption: "IoT: Sensor → Connectivity → Data → Action۔",
    svg: wrap(["Sensor", "Wi-Fi", "Cloud", "Actuator"].map((l, i) => `
      <rect x="${18 + i * 100}" y="70" width="90" height="48" rx="8" fill="${C.fill}" stroke="${i === 2 ? C.gold : C.line}"/>
      <text x="${63 + i * 100}" y="99" fill="${C.text}" font-size="12" text-anchor="middle">${l}</text>
    `).join(""), 420, 170, "IoT")
  },
  dataTypes: {
    caption: "Qualitative = الفاظ/زمرے؛ Quantitative = اعداد۔",
    svg: wrap(`
      <rect x="30" y="50" width="170" height="90" rx="10" fill="${C.fill}" stroke="${C.line}"/>
      <text x="115" y="90" fill="${C.text}" text-anchor="middle">Qualitative</text>
      <text x="115" y="114" fill="${C.gold}" font-size="12" text-anchor="middle">رنگ، رائے، ہاں/نہیں</text>
      <rect x="220" y="50" width="170" height="90" rx="10" fill="${C.fill}" stroke="${C.gold}"/>
      <text x="305" y="90" fill="${C.text}" text-anchor="middle">Quantitative</text>
      <text x="305" y="114" fill="${C.gold}" font-size="12" text-anchor="middle">عمر، مارکس، گھنٹے</text>
    `, 420, 170, "Data types")
  }
};

function renderDiagram(id) {
  const d = DIAGRAMS[id];
  if (!d) return null;
  return { html: d.svg, caption: d.caption };
}

window.DIAGRAMS = DIAGRAMS;
window.renderDiagram = renderDiagram;
window.DIAGRAM_IDS = Object.keys(DIAGRAMS);
