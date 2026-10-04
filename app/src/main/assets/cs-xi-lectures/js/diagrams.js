/** Inline SVG diagrams for lecture slides (no external assets). */

const stroke = '#3dd6f5';
const fill = '#1a2230';
const accent = '#f0b429';
const text = '#e8edf4';

export const DIAGRAMS = {
  stairsRamp: {
    captionEn: 'Discrete = fixed steps (stairs). Continuous = any value on a ramp.',
    captionUr: 'الگ الگ = سیڑھیاں۔ مسلسل = ڈھال پر کوئی بھی نقطہ۔',
    svg: `<svg viewBox="0 0 420 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Stairs vs ramp">
      <rect width="420" height="200" fill="${fill}" rx="8"/>
      <text x="105" y="24" fill="${accent}" font-size="13" text-anchor="middle" font-family="sans-serif">Discrete (Stairs)</text>
      <polyline points="20,170 20,140 50,140 50,110 80,110 80,80 110,80 110,50 140,50" fill="none" stroke="${stroke}" stroke-width="3"/>
      <text x="315" y="24" fill="${accent}" font-size="13" text-anchor="middle" font-family="sans-serif">Continuous (Ramp)</text>
      <line x1="220" y1="170" x2="400" y2="40" stroke="${stroke}" stroke-width="3"/>
    </svg>`
  },
  binaryBits: {
    captionEn: 'Digital systems use only 0 (OFF/FALSE) and 1 (ON/TRUE).',
    captionUr: 'ڈیجیٹل سسٹم صرف 0 اور 1 استعمال کرتے ہیں۔',
    svg: `<svg viewBox="0 0 360 160" xmlns="http://www.w3.org/2000/svg">
      <rect width="360" height="160" fill="${fill}" rx="8"/>
      <circle cx="90" cy="80" r="36" fill="#0f172a" stroke="${stroke}" stroke-width="2"/>
      <text x="90" y="88" fill="${text}" font-size="28" text-anchor="middle" font-family="monospace">0</text>
      <text x="90" y="130" fill="${text}" font-size="11" text-anchor="middle">OFF / LOW</text>
      <circle cx="270" cy="80" r="36" fill="#0f172a" stroke="${accent}" stroke-width="2"/>
      <text x="270" y="88" fill="${accent}" font-size="28" text-anchor="middle" font-family="monospace">1</text>
      <text x="270" y="130" fill="${text}" font-size="11" text-anchor="middle">ON / HIGH</text>
    </svg>`
  },
  analogDigitalWaves: {
    captionEn: 'Analog: smooth sine wave. Digital: square wave between HIGH and LOW.',
    captionUr: 'اینالاگ: ہموار لہر۔ ڈیجیٹل: مربع لہر۔',
    svg: `<svg viewBox="0 0 440 220" xmlns="http://www.w3.org/2000/svg">
      <rect width="440" height="220" fill="${fill}" rx="8"/>
      <text x="110" y="22" fill="${accent}" font-size="12" text-anchor="middle">Analog (sine)</text>
      <path d="M20,100 Q50,40 80,100 T140,100 T200,100" fill="none" stroke="${stroke}" stroke-width="2"/>
      <line x1="20" y1="100" x2="200" y2="100" stroke="#445" stroke-dasharray="4"/>
      <text x="330" y="22" fill="${accent}" font-size="12" text-anchor="middle">Digital (square)</text>
      <polyline points="220,140 220,60 260,60 260,140 300,140 300,60 340,60 340,140 380,140 380,60 420,60" fill="none" stroke="${accent}" stroke-width="2"/>
      <text x="250" y="55" fill="${text}" font-size="9">HIGH(1)</text>
      <text x="250" y="155" fill="${text}" font-size="9">LOW(0)</text>
    </svg>`
  },
  gateAND: {
    captionEn: 'AND gate: output 1 only when all inputs are 1.',
    captionUr: 'AND گیٹ: آؤٹ پٹ 1 صرف جب تمام ان پٹ 1 ہوں۔',
    svg: gateSvg('AND', 'Y = A · B', 'and')
  },
  gateOR: {
    captionEn: 'OR gate: output 1 when any input is 1.',
    captionUr: 'OR گیٹ: آؤٹ پٹ 1 جب کوئی ان پٹ 1 ہو۔',
    svg: gateSvg('OR', 'Y = A + B', 'or')
  },
  gateNOT: {
    captionEn: 'NOT gate inverts the input.',
    captionUr: 'NOT گیٹ ان پٹ کو الٹ دیتا ہے۔',
    svg: `<svg viewBox="0 0 280 120" xmlns="http://www.w3.org/2000/svg">
      <rect width="280" height="120" fill="${fill}" rx="8"/>
      <text x="140" y="18" fill="${accent}" font-size="12" text-anchor="middle">NOT · Y = A'</text>
      <line x1="20" y1="60" x2="70" y2="60" stroke="${stroke}" stroke-width="2"/><text x="8" y="55" fill="${text}" font-size="11">A</text>
      <polygon points="70,45 70,75 110,60" fill="none" stroke="${stroke}" stroke-width="2"/>
      <circle cx="118" cy="60" r="6" fill="${fill}" stroke="${stroke}" stroke-width="2"/>
      <line x1="124" y1="60" x2="200" y2="60" stroke="${stroke}" stroke-width="2"/><text x="205" y="65" fill="${text}" font-size="11">Y</text>
    </svg>`
  },
  gatesOverview: {
    captionEn: 'Logic gates are building blocks of digital circuits.',
    captionUr: 'لاجک گیٹس ڈیجیٹل سرکٹ کی بنیاد ہیں۔',
    svg: `<svg viewBox="0 0 400 140" xmlns="http://www.w3.org/2000/svg">
      <rect width="400" height="140" fill="${fill}" rx="8"/>
      <g transform="translate(30,50)"><rect width="50" height="40" rx="4" fill="#0f172a" stroke="${stroke}"/><text x="25" y="26" fill="${text}" font-size="11" text-anchor="middle">AND</text></g>
      <g transform="translate(120,50)"><rect width="50" height="40" rx="4" fill="#0f172a" stroke="${stroke}"/><text x="25" y="26" fill="${text}" font-size="11" text-anchor="middle">OR</text></g>
      <g transform="translate(210,50)"><rect width="50" height="40" rx="4" fill="#0f172a" stroke="${stroke}"/><text x="25" y="26" fill="${text}" font-size="11" text-anchor="middle">NOT</text></g>
      <g transform="translate(300,50)"><rect width="50" height="40" rx="4" fill="#0f172a" stroke="${accent}"/><text x="25" y="26" fill="${accent}" font-size="10" text-anchor="middle">NAND</text></g>
    </svg>`
  },
  truthTable2: {
    captionEn: 'For n inputs, truth table has 2^n rows.',
    captionUr: 'n ان پٹس کے لیے ٹرٹھ ٹیبل میں 2^n قطاریں۔',
    svg: `<svg viewBox="0 0 200 140" xmlns="http://www.w3.org/2000/svg">
      <rect width="200" height="140" fill="${fill}" rx="8"/>
      <text x="100" y="18" fill="${accent}" font-size="11" text-anchor="middle">2-input · 2² = 4 rows</text>
      ${gridTable([['A','B','Y'],['0','0','0'],['0','1','0'],['1','0','0'],['1','1','1']], 40, 28)}
    </svg>`
  },
  kmap3var: {
    captionEn: 'K-Map groups adjacent 1s to simplify Boolean expressions.',
    captionUr: 'کے میپ ملحق 1s کو گروپ کر کے سادہ کرتا ہے۔',
    svg: `<svg viewBox="0 0 260 180" xmlns="http://www.w3.org/2000/svg">
      <rect width="260" height="180" fill="${fill}" rx="8"/>
      <text x="130" y="20" fill="${accent}" font-size="12" text-anchor="middle">3-variable K-Map (AB · C)</text>
      <rect x="60" y="40" width="140" height="100" fill="none" stroke="${stroke}"/>
      <text x="75" y="58" fill="${text}" font-size="10">0</text><text x="115" y="58" fill="${text}" font-size="10">1</text>
      <text x="155" y="58" fill="${text}" font-size="10">1</text><text x="175" y="58" fill="${text}" font-size="10">0</text>
      <text x="75" y="88" fill="${text}" font-size="10">0</text><text x="115" y="88" fill="${accent}" font-size="10">1</text>
      <text x="155" y="88" fill="${accent}" font-size="10">1</text><text x="175" y="88" fill="${text}" font-size="10">0</text>
      <rect x="105" y="68" width="70" height="35" fill="none" stroke="${accent}" stroke-width="2" stroke-dasharray="4"/>
      <text x="130" y="155" fill="${text}" font-size="10" text-anchor="middle">Group → simpler term</text>
    </svg>`
  },
  sdlc: {
    captionEn: 'SDLC phases from planning to maintenance.',
    captionUr: 'SDLC کے مراحل منصوبہ بندی سے دیکھ بھال تک۔',
    svg: `<svg viewBox="0 0 400 120" xmlns="http://www.w3.org/2000/svg">
      <rect width="400" height="120" fill="${fill}" rx="8"/>
      ${['Plan','Design','Build','Test','Deploy','Maintain'].map((l,i)=>`
        <rect x="${10+i*64}" y="40" width="58" height="36" rx="6" fill="#0f172a" stroke="${i%2?accent:stroke}" stroke-width="1.5"/>
        <text x="${39+i*64}" y="63" fill="${text}" font-size="8" text-anchor="middle">${l}</text>
      `).join('')}
      <path d="M68,58 L74,58" stroke="${text}" marker-end="url(#ar)"/>
      <defs><marker id="ar" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="${text}"/></marker></defs>
    </svg>`
  },
  waterfallAgile: {
    captionEn: 'Waterfall: sequential phases. Agile: iterative cycles.',
    captionUr: 'واٹرفال: ترتیب وار۔ ایجائل: دہرائی والے چکر۔',
    svg: `<svg viewBox="0 0 420 160" xmlns="http://www.w3.org/2000/svg">
      <rect width="420" height="160" fill="${fill}" rx="8"/>
      <text x="100" y="22" fill="${accent}" font-size="11" text-anchor="middle">Waterfall</text>
      ${[0,1,2,3].map(i=>`<rect x="40" y="${35+i*28}" width="120" height="22" rx="4" fill="#0f172a" stroke="${stroke}"/>`).join('')}
      <text x="100" y="310" fill="transparent">.</text>
      <text x="310" y="22" fill="${accent}" font-size="11" text-anchor="middle">Agile (sprints)</text>
      <circle cx="310" cy="90" r="45" fill="none" stroke="${accent}" stroke-width="2"/>
      <text x="310" y="94" fill="${text}" font-size="10" text-anchor="middle">Plan→Build→Review</text>
    </svg>`
  },
  osi7: {
    captionEn: 'OSI reference model — 7 layers (exam favourite).',
    captionUr: 'OSI ماڈل — 7 پرتیں (امتحانی موضوع)۔',
    svg: `<svg viewBox="0 0 200 280" xmlns="http://www.w3.org/2000/svg">
      <rect width="200" height="280" fill="${fill}" rx="8"/>
      ${['Application','Presentation','Session','Transport','Network','Data Link','Physical'].map((l,i)=>{
        const y=24+i*34;
        return `<rect x="30" y="${y}" width="140" height="28" rx="4" fill="#0f172a" stroke="${i===0||i===3||i===6?accent:stroke}" stroke-width="1.5"/>
        <text x="100" y="${y+18}" fill="${text}" font-size="9" text-anchor="middle">${7-i}. ${l}</text>`;
      }).join('')}
    </svg>`
  },
  tcpOsi: {
    captionEn: 'TCP/IP has 4 layers mapped onto OSI.',
    captionUr: 'TCP/IP کی 4 پرتیں OSI سے منسلک ہیں۔',
    svg: `<svg viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg">
      <rect width="320" height="200" fill="${fill}" rx="8"/>
      <text x="80" y="20" fill="${accent}" font-size="11" text-anchor="middle">TCP/IP</text>
      <text x="240" y="20" fill="${accent}" font-size="11" text-anchor="middle">OSI</text>
      ${[[50,'Application',3], [90,'Transport',1], [130,'Internet',1], [170,'Network Access',2]].map(([y,t,c])=>`
        <rect x="20" y="${y}" width="100" height="${c*28+8}" rx="4" fill="#0f172a" stroke="${stroke}"/>
        <text x="70" y="${y+18}" fill="${text}" font-size="8" text-anchor="middle">${t}</text>
      `).join('')}
    </svg>`
  },
  decomposition: {
    captionEn: 'Break a complex problem into smaller sub-tasks.',
    captionUr: 'مشکل مسئلہ کو چھوٹے حصوں میں تقسیم کریں۔',
    svg: `<svg viewBox="0 0 360 160" xmlns="http://www.w3.org/2000/svg">
      <rect width="360" height="160" fill="${fill}" rx="8"/>
      <rect x="140" y="15" width="80" height="32" rx="6" fill="#0f172a" stroke="${accent}"/>
      <text x="180" y="35" fill="${text}" font-size="10" text-anchor="middle">Problem</text>
      <line x1="180" y1="47" x2="180" y2="65" stroke="${stroke}"/>
      <line x1="60" y1="65" x2="300" y2="65" stroke="${stroke}"/>
      ${[60,180,300].map((x,i)=>`
        <line x1="${x}" y1="65" x2="${x}" y2="80" stroke="${stroke}"/>
        <rect x="${x-40}" y="80" width="80" height="28" rx="4" fill="#0f172a" stroke="${stroke}"/>
        <text x="${x}" y="98" fill="${text}" font-size="9" text-anchor="middle">Part ${i+1}</text>
      `).join('')}
    </svg>`
  },
  bubbleSort: {
    captionEn: 'Bubble sort: swap adjacent pairs until sorted.',
    captionUr: 'بلبل سورٹ: جوڑوں کو تب تک تبدیل کریں جب تک ترتیب نہ ہو۔',
    svg: `<svg viewBox="0 0 300 100" xmlns="http://www.w3.org/2000/svg">
      <rect width="300" height="100" fill="${fill}" rx="8"/>
      ${[5,2,8,1].map((n,i)=>`<rect x="${30+i*60}" y="${60-n*6}" width="40" height="${n*6}" fill="${i===1?accent:'#334155'}"/>
      <text x="${50+i*60}" y="88" fill="${text}" font-size="11" text-anchor="middle">${n}</text>`).join('')}
    </svg>`
  },
  binarySearch: {
    captionEn: 'Binary search halves the search space each step (sorted list).',
    captionUr: 'بائنری سرچ ہر قدم پر تلاش کا علاقہ آدھا کرتی ہے۔',
    svg: `<svg viewBox="0 0 320 80" xmlns="http://www.w3.org/2000/svg">
      <rect width="320" height="80" fill="${fill}" rx="8"/>
      ${[2,5,8,12,16,23,38,45,56,72].map((n,i)=>{
        const x=20+i*28;
        return `<rect x="${x}" y="25" width="24" height="30" fill="${n===23?'#f0b429':'#334155'}"/>
        <text x="${x+12}" y="45" fill="${n===23?'#000':'#fff'}" font-size="8" text-anchor="middle">${n}</text>`;
      }).join('')}
      <text x="160" y="72" fill="${accent}" font-size="9" text-anchor="middle">mid → compare → left or right</text>
    </svg>`
  }
};

function gateSvg(name, expr, type) {
  const path = type === 'or'
    ? `<path d="M70,45 Q95,60 70,75 Q110,60 70,45" fill="none" stroke="${stroke}" stroke-width="2"/>`
    : `<path d="M70,45 L70,75 L110,60 Z" fill="none" stroke="${stroke}" stroke-width="2"/>`;
  return `<svg viewBox="0 0 280 120" xmlns="http://www.w3.org/2000/svg">
    <rect width="280" height="120" fill="${fill}" rx="8"/>
    <text x="140" y="18" fill="${accent}" font-size="12" text-anchor="middle">${name} · ${expr}</text>
    <line x1="20" y1="50" x2="70" y2="50" stroke="${stroke}" stroke-width="2"/><text x="8" y="45" fill="${text}" font-size="10">A</text>
    <line x1="20" y1="70" x2="70" y2="70" stroke="${stroke}" stroke-width="2"/><text x="8" y="75" fill="${text}" font-size="10">B</text>
    ${path}
    <line x1="110" y1="60" x2="200" y2="60" stroke="${stroke}" stroke-width="2"/><text x="205" y="65" fill="${text}" font-size="11">Y</text>
  </svg>`;
}

function gridTable(rows, cellW, cellH) {
  return rows.map((row, ri) =>
    row.map((cell, ci) =>
      `<rect x="${ci*cellW}" y="${ri*cellH+24}" width="${cellW}" height="${cellH}" fill="${ri===0?'#0f172a':'none'}" stroke="${stroke}"/>
       <text x="${ci*cellW+cellW/2}" y="${ri*cellH+24+cellH/2+4}" fill="${text}" font-size="10" text-anchor="middle">${cell}</text>`
    ).join('')
  ).join('');
}

export function renderDiagram(id) {
  const d = DIAGRAMS[id];
  if (!d) return null;
  return { html: d.svg, captionEn: d.captionEn, captionUr: d.captionUr };
}
