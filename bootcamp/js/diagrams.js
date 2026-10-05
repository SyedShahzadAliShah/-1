/** SVG figures for lecture boards. Labels that need algebra stay in HTML for MathJax. */

import { esc, rich } from "./mathtext.js";

const COLORS = ["#2dd4bf", "#f2c48a", "#fb7185", "#93c5fd", "#c4b5fd"];

function svg(body, width, height, extra = "") {
  return `<svg viewBox="0 0 ${width} ${height}" class="diagram-svg ${extra}" role="img">${body}</svg>`;
}

function sampleDiagram() {
  const width = 640;
  const height = 210;
  const mid = 78;
  const pts = [];
  for (let x = 24; x <= 616; x += 6) {
    const y = mid - Math.sin((x - 24) / 592 * Math.PI * 2 * 2.25) * 46;
    pts.push(`${x.toFixed(1)},${y.toFixed(1)}`);
  }
  const samples = [];
  for (let i = 0; i < 8; i += 1) {
    const x = 48 + i * 76;
    const y = mid - Math.sin((x - 24) / 592 * Math.PI * 2 * 2.25) * 46;
    const level = y < mid ? 150 : 186;
    samples.push(`<line x1="${x}" y1="${y.toFixed(1)}" x2="${x}" y2="${level}" class="stem" />`);
    samples.push(`<circle cx="${x}" cy="${y.toFixed(1)}" r="4.5" class="sample-dot" />`);
    const x2 = x + 76;
    samples.push(`<path d="M ${x} ${level} H ${Math.min(x2, 616)}" class="digital-step" />`);
  }
  return svg(`
    <text x="24" y="22" class="dim">analog voice</text>
    <text x="24" y="142" class="dim">stored samples</text>
    <path class="stroke draw" d="M ${pts.join(" L ")}" />
    ${samples.join("")}
  `, width, height, "sample-svg");
}

function circuitDiagram() {
  return svg(`
    <text x="18" y="64">A</text>
    <text x="18" y="142">B</text>
    <line x1="40" y1="58" x2="250" y2="58" />
    <line x1="40" y1="136" x2="118" y2="136" />
    <path d="M118 112 L118 160 L176 136 Z" class="fill-lamp" />
    <circle cx="186" cy="136" r="8" class="bubble" />
    <line x1="194" y1="136" x2="250" y2="136" />
    <text x="132" y="108" class="dim">NOT</text>
    <path d="M250 28 H330 C410 28 410 166 330 166 H250 Z" class="fill-lamp" />
    <text x="318" y="104" text-anchor="middle">AND</text>
    <line x1="404" y1="97" x2="520" y2="97" />
    <text x="532" y="102">Y</text>
  `, 640, 190);
}

function growthDiagram() {
  const width = 640;
  const height = 230;
  const left = 44;
  const top = 16;
  const bottom = 36;
  const innerW = width - left - 24;
  const innerH = height - top - bottom;
  const xs = [1, 2, 4, 8];
  const maxY = 20;
  const xAt = (index) => left + (index / (xs.length - 1)) * innerW;
  const yAt = (value) => top + (1 - value / maxY) * innerH;
  const pathFor = (fn) => xs.map((n, index) => `${index ? "L" : "M"}${xAt(index).toFixed(1)},${yAt(fn(n)).toFixed(1)}`).join(" ");
  const ticks = xs.map((n, index) => `<text x="${xAt(index)}" y="${height - 12}" text-anchor="middle" class="dim">${n}</text>`).join("");
  const figure = svg(`
    <defs><clipPath id="growth-plot"><rect x="${left}" y="${top}" width="${innerW + 8}" height="${innerH}" /></clipPath></defs>
    <line x1="${left}" y1="${top}" x2="${left}" y2="${height - bottom}" class="axis" />
    <line x1="${left}" y1="${height - bottom}" x2="${width - 16}" y2="${height - bottom}" class="axis" />
    <text x="8" y="14" class="dim">work</text>
    <text x="${width - 70}" y="${height - 14}" class="dim">n</text>
    ${ticks}
    <g clip-path="url(#growth-plot)">
      <path class="stroke-blue" d="${pathFor(() => 1)}" />
      <path class="stroke-teal" d="${pathFor((n) => Math.log2(n) + 1)}" />
      <path class="stroke" d="${pathFor((n) => n)}" />
      <path class="stroke-rose" d="${pathFor((n) => n * n)}" />
    </g>
    <text x="${xAt(2) + 8}" y="${top + 18}" class="dim">n² leaves the chart</text>
  `, width, height, "growth-svg");
  const legend = [
    ["#93c5fd", "$O(1)$"],
    ["#2dd4bf", "$O(\\log n)$"],
    ["#f2c48a", "$O(n)$"],
    ["#fb7185", "$O(n^2)$"],
  ].map(([color, label]) => `<li><i style="background:${color}"></i>${rich(label)}</li>`).join("");
  return `${figure}<ul class="diagram-legend">${legend}</ul>`;
}

function bell(center, sigma, amp, base) {
  const pts = [];
  for (let x = 36; x <= 604; x += 8) {
    const z = (x - center) / sigma;
    const y = base - Math.exp(-0.5 * z * z) * amp;
    pts.push(`${x},${y.toFixed(1)}`);
  }
  return `M ${pts.join(" L ")}`;
}

function spreadDiagram() {
  const figure = svg(`
    <line x1="36" y1="150" x2="604" y2="150" class="axis" />
    <line x1="320" y1="36" x2="320" y2="150" class="mean-line" />
    <path class="stroke-teal" d="${bell(320, 38, 96, 150)}" />
    <path class="stroke-rose" d="${bell(320, 120, 52, 150)}" />
    <text x="320" y="172" text-anchor="middle" class="dim">same mean</text>
    <text x="96" y="28" class="dim">wide spread</text>
    <text x="430" y="28" class="dim">tight cluster</text>
  `, 640, 188);
  return `${figure}
    <div class="formula-row">
      <div class="math-display">\\[\\bar{x}=\\frac{\\sum x_i}{n}\\]</div>
      <div class="math-display">\\[\\mathrm{range}=\\max-\\min\\]</div>
      <div class="math-display">\\[s=\\sqrt{\\frac{\\sum (x_i-\\bar{x})^2}{n}}\\]</div>
    </div>`;
}

export const DIAGRAMS = {
  sample: sampleDiagram,
  circuit: circuitDiagram,
  growth: growthDiagram,
  spread: spreadDiagram,
};

export const DIAGRAM_NAMES = Object.keys(DIAGRAMS);

export function renderDiagram(name) {
  const draw = DIAGRAMS[name];
  if (!draw) return `<p class="scene-note">This diagram is not in the set.</p>`;
  return `<div class="diagram-frame">${draw()}</div>`;
}

function pieSvg(spec) {
  const values = spec.values || [];
  const total = values.reduce((sum, n) => sum + Number(n), 0) || 1;
  const cx = 90;
  const cy = 90;
  const r = 70;
  let angle = -Math.PI / 2;
  const slices = values.map((value, index) => {
    const sweep = (Number(value) / total) * Math.PI * 2;
    const start = angle;
    angle += sweep;
    const large = sweep > Math.PI ? 1 : 0;
    const x1 = cx + Math.cos(start) * r;
    const y1 = cy + Math.sin(start) * r;
    const x2 = cx + Math.cos(angle) * r;
    const y2 = cy + Math.sin(angle) * r;
    return `<path d="M ${cx} ${cy} L ${x1.toFixed(2)} ${y1.toFixed(2)} A ${r} ${r} 0 ${large} 1 ${x2.toFixed(2)} ${y2.toFixed(2)} Z" fill="${COLORS[index % COLORS.length]}" />`;
  }).join("");
  const legend = (spec.labels || []).map((label, index) =>
    `<li><i style="background:${COLORS[index % COLORS.length]}"></i>${esc(label)} <b>${esc(values[index])}</b></li>`
  ).join("");
  return `<div class="pie-wrap">${svg(slices, 180, 180, "pie-svg")}<ul class="legend">${legend}</ul></div>`;
}

function lineSvg(spec) {
  const values = (spec.values || []).map(Number);
  const max = Math.max(...values, 1);
  const w = 560;
  const h = 180;
  const pts = values.map((value, index) => {
    const x = values.length === 1 ? w / 2 : (index / (values.length - 1)) * (w - 36) + 18;
    const y = h - 24 - (value / max) * (h - 48);
    return [x, y];
  });
  const d = pts.map((p, i) => `${i ? "L" : "M"}${p[0].toFixed(1)},${p[1].toFixed(1)}`).join(" ");
  const dots = pts.map((p) => `<circle cx="${p[0].toFixed(1)}" cy="${p[1].toFixed(1)}" r="4" />`).join("");
  const labels = (spec.labels || []).map((label) => `<span>${esc(label)}</span>`).join("");
  return `${svg(`<path d="${d}" />${dots}`, w, h, "line-chart")}<div class="axis-labels">${labels}</div>`;
}

function boxSvg(spec) {
  const min = Number(spec.min ?? 0);
  const q1 = Number(spec.q1 ?? 25);
  const median = Number(spec.median ?? 50);
  const q3 = Number(spec.q3 ?? 75);
  const max = Number(spec.max ?? 100);
  const span = Math.max(1, max - min);
  const x = (n) => 36 + ((n - min) / span) * 520;
  const figure = svg(`
    <line x1="${x(min)}" y1="48" x2="${x(max)}" y2="48" class="stroke" />
    <line x1="${x(min)}" y1="34" x2="${x(min)}" y2="62" class="stroke" />
    <line x1="${x(max)}" y1="34" x2="${x(max)}" y2="62" class="stroke" />
    <rect x="${x(q1)}" y="28" width="${Math.max(8, x(q3) - x(q1))}" height="40" rx="6" class="fill-soft" />
    <line x1="${x(median)}" y1="24" x2="${x(median)}" y2="72" class="stroke" />
  `, 600, 88, "box-svg");
  const caption = [["min", min], ["Q1", q1], ["median", median], ["Q3", q3], ["max", max]]
    .map(([name, value]) => `<span>${name} ${esc(value)}</span>`).join("");
  return `${figure}<div class="axis-labels">${caption}</div>`;
}

function scatterSvg(spec) {
  const points = spec.points || [];
  const dots = points.map((point) => {
    const x = 40 + (Number(point.x) / 100) * 520;
    const y = 170 - (Number(point.y) / 100) * 140;
    return `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="5" class="sample-dot"><title>${esc(point.label || "")}</title></circle>`;
  }).join("");
  return svg(`
    <line x1="36" y1="16" x2="36" y2="176" class="axis" />
    <line x1="36" y1="176" x2="580" y2="176" class="axis" />
    <text x="44" y="18" class="dim">${esc(spec.yLabel || "y")}</text>
    <text x="540" y="168" class="dim">${esc(spec.xLabel || "x")}</text>
    ${dots}
  `, 600, 190);
}

function barsSvg(spec, histogram) {
  const values = (spec.values || []).map(Number);
  const labels = spec.labels || [];
  const max = Math.max(...values, 1);
  const gap = histogram ? 2 : 18;
  const left = 28;
  const width = Math.max(320, left + values.length * 72);
  const height = 220;
  const barW = (width - left - 16 - gap * values.length) / Math.max(1, values.length);
  const bars = values.map((value, index) => {
    const h = (value / max) * 150;
    const x = left + gap + index * (barW + gap);
    const y = 176 - h;
    return `<rect x="${x.toFixed(1)}" y="${y.toFixed(1)}" width="${barW.toFixed(1)}" height="${h.toFixed(1)}" rx="${histogram ? 1 : 6}" class="${histogram ? "hist-bar" : "bar-fill"}" />
      <text x="${(x + barW / 2).toFixed(1)}" y="${(y - 6).toFixed(1)}" text-anchor="middle">${esc(value)}</text>
      <text x="${(x + barW / 2).toFixed(1)}" y="198" text-anchor="middle" class="dim">${esc(labels[index] || "")}</text>`;
  }).join("");
  return svg(`<line x1="20" y1="176" x2="${width - 8}" y2="176" class="axis" />${bars}`, width, height, histogram ? "hist-svg" : "bar-svg");
}

export function chartMarkup(spec) {
  const kind = spec.kind || "bar";
  if (kind === "pie") return pieSvg(spec);
  if (kind === "line") return lineSvg(spec);
  if (kind === "box") return boxSvg(spec);
  if (kind === "scatter") return scatterSvg(spec);
  return barsSvg(spec, kind === "hist");
}

export function kmapSvg(spec) {
  const cells = spec.cells || [0, 0, 0, 0];
  const three = cells.length > 4;
  const cols = three ? 4 : 2;
  const rows = Math.ceil(cells.length / cols);
  const size = 68;
  const left = 56;
  const top = 36;
  const width = left + cols * size + 20;
  const height = top + rows * size + 16;
  const colLabels = three ? ["00", "01", "11", "10"] : ["0", "1"];
  const rowLabels = rows === 2 ? ["0", "1"] : ["0"];
  const heads = colLabels.slice(0, cols).map((label, index) =>
    `<text x="${left + index * size + size / 2}" y="22" text-anchor="middle" class="dim">${three ? "BC " : "B="}${label}</text>`
  ).join("");
  const sides = rowLabels.map((label, index) =>
    `<text x="8" y="${top + index * size + size / 2 + 4}" class="dim">A=${label}</text>`
  ).join("");
  const boxes = cells.map((cell, index) => {
    const c = index % cols;
    const r = Math.floor(index / cols);
    const x = left + c * size;
    const y = top + r * size;
    return `<rect x="${x + 4}" y="${y + 4}" width="${size - 8}" height="${size - 8}" rx="8" class="${cell ? "k-one" : "k-zero"}" />
      <text x="${x + size / 2}" y="${y + size / 2 + 6}" text-anchor="middle">${esc(cell)}</text>`;
  }).join("");
  const groups = (spec.groups || []).map((group, groupIndex) => {
    const picked = (group.cells || []).map((index) => ({
      c: index % cols,
      r: Math.floor(index / cols),
    }));
    if (!picked.length) return "";
    const c0 = Math.min(...picked.map((cell) => cell.c));
    const c1 = Math.max(...picked.map((cell) => cell.c));
    const r0 = Math.min(...picked.map((cell) => cell.r));
    const r1 = Math.max(...picked.map((cell) => cell.r));
    const x = left + c0 * size + 8;
    const y = top + r0 * size + 8;
    const w = (c1 - c0 + 1) * size - 16;
    const h = (r1 - r0 + 1) * size - 16;
    return `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="12" class="k-group g${groupIndex % 2}" />`;
  }).join("");
  return svg(`${heads}${sides}${boxes}${groups}`, width, height, "kmap-svg");
}

export function treeSvg(levels) {
  const rows = levels || [];
  const width = 640;
  const rowH = 96;
  const height = 36 + Math.max(1, rows.length) * rowH;
  const nodes = rows.map((level, li) => level.map((label, i) => ({
    label,
    x: ((i + 1) / (level.length + 1)) * width,
    y: 28 + li * rowH,
  })));
  const lines = [];
  for (let li = 0; li < nodes.length - 1; li += 1) {
    const parents = nodes[li];
    const children = nodes[li + 1];
    children.forEach((child, i) => {
      const parent = parents[Math.min(parents.length - 1, Math.floor((i * parents.length) / children.length))];
      lines.push(`<line x1="${parent.x}" y1="${parent.y + 36}" x2="${child.x}" y2="${child.y - 12}" />`);
    });
  }
  const dots = nodes.flat().map((node) =>
    `<circle cx="${node.x}" cy="${node.y}" r="7" class="sample-dot" /><text x="${node.x}" y="${node.y + 28}" text-anchor="middle">${esc(node.label)}</text>`
  ).join("");
  return svg(`${lines.join("")}${dots}`, width, height, "tree-svg");
}

export function erSvg(spec) {
  const entities = spec.entities || [];
  const count = Math.max(1, entities.length);
  const width = Math.max(640, count * 220);
  const boxes = entities.map((entity, index) => {
    const attrs = (entity.attrs || []).map((attr) => (typeof attr === "string" ? { name: attr } : attr));
    const x = ((index + 0.5) * width) / count;
    const top = 28;
    const h = 36 + attrs.length * 18;
    const body = attrs.map((attr, i) =>
      `<text x="${x}" y="${top + 40 + i * 18}" text-anchor="middle" class="${attr.key ? "" : "dim"}">${attr.key ? "• " : ""}${esc(attr.name)}</text>`
    ).join("");
    return {
      x,
      right: x + 78,
      left: x - 78,
      mid: top + 18,
      html: `<rect x="${x - 78}" y="${top}" width="156" height="${h}" rx="12" class="entity-box" />
        <text x="${x}" y="${top + 22}" text-anchor="middle">${esc(entity.name)}</text>${body}`,
    };
  });
  const links = spec.links || [];
  const boxBottom = 28 + 36 + Math.max(...entities.map((entity) => (entity.attrs || []).length), 1) * 18;
  const connectors = [];
  for (let i = 0; i < boxes.length - 1; i += 1) {
    const a = boxes[i];
    const b = boxes[i + 1];
    const mx = (a.x + b.x) / 2;
    const my = 46;
    connectors.push(`<line x1="${a.right}" y1="${my}" x2="${mx - 22}" y2="${my}" />`);
    connectors.push(`<line x1="${mx + 22}" y1="${my}" x2="${b.left}" y2="${my}" />`);
    connectors.push(`<polygon points="${mx},${my - 16} ${mx + 22},${my} ${mx},${my + 16} ${mx - 22},${my}" class="rel-diamond" />`);
  }
  const height = boxBottom + 24;
  const caption = links.map((link) => `<span>${esc(link)}</span>`).join("");
  return `${svg(`${connectors.join("")}${boxes.map((box) => box.html).join("")}`, width, height, "er-svg")}<div class="axis-labels">${caption}</div>`;
}
