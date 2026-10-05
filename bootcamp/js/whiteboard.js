/** A lecture board that draws itself, one chalk stroke at a time. */

import { esc } from "./mathtext.js";

const WIDTH = 520;
const HEIGHT = 210;

function label(x, y, text, index, anchor) {
  return `<text class="ink-label" style="--i:${index}" x="${x}" y="${y}" text-anchor="${anchor}">${esc(text)}</text>`;
}

function arrowPath(mark) {
  const x1 = mark.x1;
  const y1 = mark.y1;
  const x2 = mark.x2;
  const y2 = mark.y2;
  const angle = Math.atan2(y2 - y1, x2 - x1);
  const head = 11;
  const left = angle + Math.PI * 0.8;
  const right = angle - Math.PI * 0.8;
  const hx1 = (x2 + Math.cos(left) * head).toFixed(1);
  const hy1 = (y2 + Math.sin(left) * head).toFixed(1);
  const hx2 = (x2 + Math.cos(right) * head).toFixed(1);
  const hy2 = (y2 + Math.sin(right) * head).toFixed(1);
  return `M ${x1} ${y1} L ${x2} ${y2} M ${hx1} ${hy1} L ${x2} ${y2} L ${hx2} ${hy2}`;
}

function penClass(mark) {
  if (mark.pen === "gold") return "ink-gold";
  if (mark.pen === "teal") return "ink-teal";
  return "ink";
}

export function whiteboardSvg(ink = []) {
  const rules = [46, 92, 138, 184].map((y) =>
    `<line class="board-rule" x1="16" y1="${y}" x2="${WIDTH - 16}" y2="${y}" />`
  ).join("");
  const marks = ink.map((mark, index) => {
    const style = `--i:${index}`;
    const pen = penClass(mark);
    if (mark.t === "box") {
      const caption = mark.label
        ? label(mark.x + mark.w / 2, mark.y + mark.h / 2 + 6, mark.label, index, "middle")
        : "";
      return `<rect class="${pen}" style="${style}" pathLength="100" x="${mark.x}" y="${mark.y}" width="${mark.w}" height="${mark.h}" rx="10" />${caption}`;
    }
    if (mark.t === "line") {
      return `<line class="${pen}" style="${style}" pathLength="100" x1="${mark.x1}" y1="${mark.y1}" x2="${mark.x2}" y2="${mark.y2}" />`;
    }
    if (mark.t === "arrow") {
      return `<path class="${pen}" style="${style}" pathLength="100" d="${arrowPath(mark)}" />`;
    }
    if (mark.t === "circ") {
      const caption = mark.label ? label(mark.x, mark.y + mark.r + 16, mark.label, index, "middle") : "";
      return `<circle class="${pen}" style="${style}" pathLength="100" cx="${mark.x}" cy="${mark.y}" r="${mark.r}" />${caption}`;
    }
    if (mark.t === "dot") {
      return `<circle class="ink-dot ${pen}" style="${style}" cx="${mark.x}" cy="${mark.y}" r="${mark.r || 5}" />`;
    }
    if (mark.t === "text") {
      return label(mark.x, mark.y, mark.label || "", index, mark.anchor || "start");
    }
    if (mark.t === "path") {
      return `<path class="${pen}" style="${style}" pathLength="100" d="${mark.d}" />`;
    }
    return "";
  }).join("");
  return `<svg viewBox="0 0 ${WIDTH} ${HEIGHT}" class="whiteboard" role="img">${rules}${marks}</svg>`;
}
