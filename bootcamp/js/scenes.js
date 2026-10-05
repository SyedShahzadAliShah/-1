/** Animated lecture boards. Each scene is drawn from lecture data and cleaned up on the next beat. */

import { esc, rich, typeset } from "./mathtext.js";
import { chartMarkup, erSvg, kmapSvg, renderDiagram, treeSvg } from "./diagrams.js";

export { esc };

export const SCENE_TYPES = [
  "board",
  "split",
  "wave",
  "bits",
  "gate",
  "table",
  "kmap",
  "layers",
  "pipeline",
  "bars",
  "cells",
  "flow",
  "code",
  "cards",
  "er",
  "stack",
  "queue",
  "tree",
  "graph",
  "network",
  "chart",
  "cycle",
  "callout",
  "compare",
  "diagram",
];

function reducedMotion() {
  return typeof window !== "undefined" && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
}

function playFrames(frames, { loop = false, ms = 900 } = {}, render) {
  return (container) => {
    const host = container.querySelector("[data-frames]");
    if (!host || !frames?.length) return () => {};
    let index = 0;
    const draw = () => {
      host.innerHTML = render(frames[index], index);
      typeset(host);
    };
    if (reducedMotion()) {
      index = frames.length - 1;
      draw();
      return () => {};
    }
    draw();
    const id = setInterval(() => {
      if (index >= frames.length - 1) {
        if (!loop) {
          clearInterval(id);
          return;
        }
        index = 0;
      } else {
        index += 1;
      }
      draw();
    }, ms);
    return () => clearInterval(id);
  };
}

function shell(title, body, note = "") {
  return `<div class="scene">
    ${title ? `<h3 class="scene-title">${rich(title)}</h3>` : ""}
    <div class="scene-body">${body}</div>
    ${note ? `<div class="scene-note">${rich(note)}</div>` : ""}
  </div>`;
}

function sinePath(width = 560, height = 160, cycles = 2.5) {
  const mid = height / 2;
  const amp = height * 0.38;
  const pts = [];
  for (let x = 0; x <= width; x += 6) {
    const y = mid - Math.sin((x / width) * Math.PI * 2 * cycles) * amp;
    pts.push(`${x},${y.toFixed(1)}`);
  }
  return `M ${pts.join(" L ")}`;
}

function squarePath(width = 560, height = 160) {
  const top = 28;
  const bottom = height - 28;
  const step = width / 4;
  let d = `M 0 ${bottom}`;
  for (let i = 0; i < 4; i += 1) {
    const x0 = i * step;
    const x1 = (i + 1) * step;
    const y = i % 2 === 0 ? bottom : top;
    const next = i % 2 === 0 ? top : bottom;
    d += ` L ${x0} ${y} L ${x1} ${y} L ${x1} ${next}`;
  }
  return d;
}

const GATE_EXPR = {
  AND: "$Y = A \\cdot B$",
  OR: "$Y = A + B$",
  NOT: "$Y = \\overline{A}$",
  NAND: "$Y = \\overline{A \\cdot B}$",
  NOR: "$Y = \\overline{A + B}$",
  XOR: "$Y = A \\oplus B$",
  XNOR: "$Y = \\overline{A \\oplus B}$",
};

function gateSvg(name) {
  const bubble = `<circle cx="118" cy="60" r="8" class="bubble" />`;
  if (name === "NOT") {
    return `<svg viewBox="0 0 140 120" class="gate-svg" aria-hidden="true">
      <path d="M22 22 L22 98 L104 60 Z" />
      <circle cx="114" cy="60" r="8" class="bubble" />
    </svg>`;
  }
  if (name === "OR" || name === "NOR" || name === "XOR" || name === "XNOR") {
    const extra = name === "XOR" || name === "XNOR" ? `<path d="M28 22 Q48 60 28 98" class="xor-line" />` : "";
    return `<svg viewBox="0 0 150 120" class="gate-svg" aria-hidden="true">
      ${extra}
      <path d="M24 22 Q52 60 24 98 Q78 98 120 60 Q78 22 24 22 Z" />
      ${name === "NOR" || name === "XNOR" ? `<circle cx="130" cy="60" r="8" class="bubble" />` : ""}
    </svg>`;
  }
  return `<svg viewBox="0 0 140 120" class="gate-svg" aria-hidden="true">
    <path d="M22 22 H68 C112 22 112 98 68 98 H22 Z" />
    ${name === "NAND" ? bubble : ""}
  </svg>`;
}

function gateFrame(spec, step) {
  const a = step.a ? 1 : 0;
  const b = step.b ? 1 : 0;
  const y = step.y ? 1 : 0;
  const unary = spec.gate === "NOT";
  return `<div class="gate-bench">
    <div class="wires">
      <div class="wire ${a ? "is-on" : ""}"><span>A</span><b>${a}</b></div>
      ${unary ? "" : `<div class="wire ${b ? "is-on" : ""}"><span>B</span><b>${b}</b></div>`}
    </div>
    <div class="gate-shape">${gateSvg(spec.gate)}<em>${esc(spec.gate)}</em></div>
    <div class="lamp ${y ? "lit" : ""}"><span>Y</span><b>${y}</b></div>
  </div>
  <p class="expr">${rich(spec.expr || GATE_EXPR[spec.gate] || "")}</p>
  <p class="frame-note">${rich(step.note || "")}</p>`;
}

function chartSvg(spec) {
  return chartMarkup(spec);
}

const builders = {
  board(spec) {
    const points = (spec.points || []).map((point, index) =>
      `<li style="--i:${index}">${rich(point)}</li>`
    ).join("");
    return {
      html: `<div class="scene scene-board">
        ${spec.kicker ? `<p class="kicker">${rich(spec.kicker)}</p>` : ""}
        <h3>${rich(spec.title || "")}</h3>
        ${spec.formula ? rich(spec.formula) : ""}
        ${points ? `<ul class="rise-list">${points}</ul>` : ""}
      </div>`,
    };
  },
  split(spec) {
    const col = (side) => `<article class="split-col">
      <p class="kicker">${rich(side.eyebrow || "")}</p>
      <h3>${rich(side.title || "")}</h3>
      <ul>${(side.lines || []).map((line) => `<li>${rich(line)}</li>`).join("")}</ul>
    </article>`;
    return { html: shell(spec.title, `<div class="split">${col(spec.left || {})}${col(spec.right || {})}</div>`, spec.note) };
  },
  wave(spec) {
    const mode = spec.mode || "both";
    const showAnalog = mode === "analog" || mode === "both";
    const showDigital = mode === "digital" || mode === "both";
    const analog = showAnalog ? `<figure class="wave-card"><figcaption>Analog · smooth</figcaption><svg viewBox="0 0 560 160" class="wave-svg"><path class="draw analog" d="${sinePath()}" /></svg></figure>` : "";
    const digital = showDigital ? `<figure class="wave-card"><figcaption>Digital · HIGH / LOW</figcaption><svg viewBox="0 0 560 160" class="wave-svg"><path class="draw digital" d="${squarePath()}" /></svg><div class="level-key"><span>HIGH = 1</span><span>LOW = 0</span></div></figure>` : "";
    return { html: shell(spec.title || "Signals", `<div class="wave-grid">${analog}${digital}</div>`, spec.note) };
  },
  bits(spec) {
    const rows = (spec.rows || []).map((row) =>
      `<article class="bit-card ${row.bit === "1" || row.bit === 1 ? "on" : ""}"><b>${rich(row.bit)}</b><div>${(row.meanings || []).map((m) => `<span>${rich(m)}</span>`).join("")}</div></article>`
    ).join("");
    return { html: shell(spec.title || "Two values only", `<div class="bit-row">${rows}</div>`, spec.note) };
  },
  gate(spec) {
    const steps = spec.steps?.length ? spec.steps : [{ a: 0, b: 0, y: 0 }];
    return {
      html: shell(spec.title || `${spec.gate} gate`, `<div data-frames></div>`),
      start: playFrames(steps, { loop: true, ms: 1100 }, (step) => gateFrame(spec, step)),
    };
  },
  table(spec) {
    const head = `<tr>${(spec.headers || []).map((h) => `<th>${rich(h)}</th>`).join("")}</tr>`;
    const rows = (spec.rows || []).map((row, index) =>
      `<tr style="--i:${index}">${row.map((cell) => `<td>${rich(cell)}</td>`).join("")}</tr>`
    ).join("");
    return { html: shell(spec.title, `<div class="table-wrap"><table class="reveal-table"><thead>${head}</thead><tbody>${rows}</tbody></table></div>`, spec.note) };
  },
  kmap(spec) {
    return {
      html: shell(spec.title || "Karnaugh map", `${kmapSvg(spec)}<p class="expr">${rich(spec.expr || "")}</p>`, spec.note),
    };
  },
  layers(spec) {
    const layers = spec.layers || [];
    const rows = layers.map((layer, index) =>
      `<li class="osi-row" style="--i:${index}"><b>${rich(layer.name)}</b><span>${rich(layer.job || "")}</span><em>${rich(layer.tag || "")}</em></li>`
    ).join("");
    return {
      html: shell(spec.title, `<ol class="osi">${rows}<i class="packet"></i></ol>`, spec.note),
      start(container) {
        const rowsEl = [...container.querySelectorAll(".osi-row")];
        if (!rowsEl.length || reducedMotion()) {
          rowsEl.forEach((row) => row.classList.add("hot"));
          return () => {};
        }
        let index = rowsEl.length - 1;
        const tick = () => {
          rowsEl.forEach((row, i) => row.classList.toggle("hot", i === index));
          index = index <= 0 ? rowsEl.length - 1 : index - 1;
        };
        tick();
        const id = setInterval(tick, 850);
        return () => clearInterval(id);
      },
    };
  },
  pipeline(spec) {
    const steps = spec.steps || [];
    return {
      html: shell(spec.title, `<div data-frames></div>`),
      start: playFrames(steps, { loop: spec.loop !== false, ms: 1000 }, (step, index) => {
        const items = steps.map((item, i) =>
          `<li class="${i === index ? "hot" : i < index ? "done" : ""}"><b>${i + 1}</b><strong>${rich(item.name)}</strong><span>${rich(item.detail || "")}</span></li>`
        ).join("");
        return `<ol class="pipeline">${items}</ol><p class="frame-note">${rich(step.note || step.detail || "")}</p>`;
      }),
    };
  },
  bars(spec) {
    const frames = spec.frames || [{ values: spec.values || [], hi: [], note: spec.note || "" }];
    return {
      html: shell(spec.title, `<div data-frames></div>`),
      start: playFrames(frames, { loop: false, ms: spec.ms || 850 }, (frame) => {
        const max = Math.max(...frame.values, 1);
        const bars = frame.values.map((value, index) => {
          const hot = (frame.hi || []).includes(index);
          const placed = (frame.placed || []).includes(index);
          return `<div class="sbar ${hot ? "hot" : ""} ${placed ? "placed" : ""}"><i style="--h:${Math.round((value / max) * 100)}%"></i><span>${rich(value)}</span></div>`;
        }).join("");
        return `<div class="sbars">${bars}</div><p class="frame-note">${rich(frame.note || "")}</p>`;
      }),
    };
  },
  cells(spec) {
    const frames = spec.frames || [{ note: spec.note || "" }];
    return {
      html: shell(spec.title, `<div data-frames></div>`),
      start: playFrames(frames, { loop: false, ms: spec.ms || 1100 }, (frame) => {
        const cells = (spec.values || []).map((value, index) => {
          const classes = [
            frame.mid === index ? "mid" : "",
            frame.focus?.includes(index) ? "focus" : "",
            frame.found === index ? "found" : "",
            Number.isInteger(frame.low) && Number.isInteger(frame.high) && (index < frame.low || index > frame.high) ? "dim" : "",
          ].filter(Boolean).join(" ");
          return `<div class="acell ${classes}"><small>${index}</small><b>${rich(value)}</b></div>`;
        }).join("");
        const range = Number.isInteger(frame.low) ? `low ${frame.low} · high ${frame.high}${Number.isInteger(frame.mid) ? ` · mid ${frame.mid}` : ""}` : "";
        return `<div class="acells">${cells}</div><p class="range-label">${rich(range)}</p><p class="frame-note">${rich(frame.note || "")}</p>`;
      }),
    };
  },
  flow(spec) {
    const nodes = spec.nodes || [];
    const order = spec.order || nodes.map((node) => node.id);
    return {
      html: shell(spec.title, `<div data-frames></div>`),
      start: playFrames(order, { loop: true, ms: 900 }, (id) => {
        const html = nodes.map((node) =>
          `<div class="fnode ${node.kind || "step"} ${node.id === id ? "hot" : ""}">${rich(node.text)}</div>`
        ).join(`<i class="farrow" aria-hidden="true"></i>`);
        return `<div class="flow">${html}</div>`;
      }),
    };
  },
  code(spec) {
    const lines = (spec.lines || []).map((line, index) => {
      const text = typeof line === "string" ? line : line.text;
      const on = Array.isArray(spec.active) ? spec.active.includes(index) : Boolean(line.on);
      return `<div class="code-line ${on ? "on" : ""}" style="--i:${index}"><span>${index + 1}</span><code>${esc(text)}</code></div>`;
    }).join("");
    return { html: shell(spec.title, `<div class="code-card">${lines}</div>`, spec.note) };
  },
  cards(spec) {
    const cards = (spec.items || []).map((item, index) =>
      `<article class="info-card" style="--i:${index}"><p class="kicker">${rich(item.tag || "")}</p><h4>${rich(item.title)}</h4><p>${rich(item.body)}</p></article>`
    ).join("");
    return { html: shell(spec.title, `<div class="card-grid">${cards}</div>`, spec.note) };
  },
  er(spec) {
    return { html: shell(spec.title || "Entity relationship", erSvg(spec), spec.note) };
  },
  stack(spec) {
    const frames = spec.frames || [];
    return {
      html: shell(spec.title || "Stack · last in, first out", `<div data-frames></div>`),
      start: playFrames(frames, { loop: false, ms: 900 }, (frame) => {
        const items = [...(frame.items || [])].reverse().map((item, index) =>
          `<div class="stack-item ${index === 0 ? "top" : ""}">${rich(item)}${index === 0 ? "<i>top</i>" : ""}</div>`
        ).join("");
        return `<div class="stack-wrap"><div class="stack-col">${items || `<div class="empty">empty</div>`}</div></div><p class="frame-note">${rich(frame.note || "")}</p>`;
      }),
    };
  },
  queue(spec) {
    const frames = spec.frames || [];
    return {
      html: shell(spec.title || "Queue · first in, first out", `<div data-frames></div>`),
      start: playFrames(frames, { loop: false, ms: 900 }, (frame) => {
        const items = (frame.items || []).map((item, index, arr) =>
          `<div class="q-item ${index === 0 ? "front" : ""} ${index === arr.length - 1 ? "rear" : ""}">${rich(item)}</div>`
        ).join("");
        return `<div class="queue-wrap"><span>front</span><div class="queue-row">${items || `<div class="empty">empty</div>`}</div><span>rear</span></div><p class="frame-note">${rich(frame.note || "")}</p>`;
      }),
    };
  },
  tree(spec) {
    return { html: shell(spec.title || "Tree", treeSvg(spec.levels || []), spec.note) };
  },
  graph(spec) {
    const nodes = spec.nodes || [];
    const edges = spec.edges || [];
    const lines = edges.map((edge) => {
      const a = nodes.find((node) => node.id === edge[0]);
      const b = nodes.find((node) => node.id === edge[1]);
      if (!a || !b) return "";
      return `<line x1="${a.x}" y1="${a.y}" x2="${b.x}" y2="${b.y}" />`;
    }).join("");
    const dots = nodes.map((node, index) =>
      `<div class="gnode" style="left:${node.x}%;top:${node.y}%;--i:${index}">${rich(node.label)}</div>`
    ).join("");
    return { html: shell(spec.title || "Graph", `<div class="graph"><svg viewBox="0 0 100 100" preserveAspectRatio="none">${lines}</svg>${dots}</div>`, spec.note) };
  },
  network(spec) {
    const layers = spec.layers || [];
    const cols = layers.map((layer, index) =>
      `<div class="nn-col" style="--i:${index}">${layer.map((label) => `<span class="neuron">${rich(label)}</span>`).join("")}</div>`
    ).join("");
    return { html: shell(spec.title || "Neural network", `<div class="nn">${cols}</div>`, spec.note) };
  },
  chart(spec) {
    return { html: shell(spec.title, chartSvg(spec), spec.note) };
  },
  cycle(spec) {
    const steps = spec.steps || [];
    const items = steps.map((step, index) =>
      `<li style="--i:${index}"><b>${index + 1}</b><strong>${rich(step.name || step)}</strong><span>${rich(step.detail || "")}</span></li>`
    ).join("");
    return { html: shell(spec.title, `<ol class="cycle">${items}</ol>`, spec.note) };
  },
  callout(spec) {
    return {
      html: `<div class="scene scene-callout">
        <p class="kicker">${rich(spec.eyebrow || "Remember")}</p>
        <h3>${rich(spec.title || "")}</h3>
        <p>${rich(spec.body || "")}</p>
        ${spec.formula ? rich(spec.formula) : ""}
      </div>`,
    };
  },
  diagram(spec) {
    return { html: shell(spec.title, renderDiagram(spec.diagram), spec.note) };
  },
  compare(spec) {
    const headers = spec.headers || [];
    const head = headers.map((header) => `<th>${rich(header)}</th>`).join("");
    const rows = (spec.rows || []).map((row, index) =>
      `<tr style="--i:${index}">${row.map((cell) => `<td>${rich(cell)}</td>`).join("")}</tr>`
    ).join("");
    return { html: shell(spec.title, `<div class="table-wrap"><table class="reveal-table"><thead><tr>${head}</tr></thead><tbody>${rows}</tbody></table></div>`, spec.note) };
  },
};

export function mountScene(container, spec) {
  const draw = builders[spec?.type] || builders.board;
  let built;
  try {
    built = draw(spec || { title: "Lecture", points: [] });
  } catch (error) {
    container.innerHTML = `<div class="scene scene-callout"><h3>This board could not be drawn.</h3><p>${esc(error.message)}</p></div>`;
    return () => {};
  }
  container.innerHTML = built.html;
  const stop = built.start?.(container) || (() => {});
  typeset(container);
  return stop;
}
