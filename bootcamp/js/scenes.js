/** Animated lecture boards. Each scene is drawn from lecture data and cleaned up on the next beat. */

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
];

export function esc(value) {
  return String(value ?? "").replace(/[&<>"']/g, (ch) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;",
  }[ch]));
}

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
    ${title ? `<h3 class="scene-title">${esc(title)}</h3>` : ""}
    <div class="scene-body">${body}</div>
    ${note ? `<p class="scene-note">${esc(note)}</p>` : ""}
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
  AND: "Y = A AND B",
  OR: "Y = A OR B",
  NOT: "Y = NOT A",
  NAND: "Y = NOT (A AND B)",
  NOR: "Y = NOT (A OR B)",
  XOR: "Y = A XOR B",
  XNOR: "Y = NOT (A XOR B)",
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
  <p class="expr">${esc(spec.expr || GATE_EXPR[spec.gate] || "")}</p>
  <p class="frame-note">${esc(step.note || "")}</p>`;
}

function chartSvg(spec) {
  const kind = spec.kind || "bar";
  if (kind === "pie") {
    const values = spec.values || [];
    const total = values.reduce((sum, n) => sum + n, 0) || 1;
    const colors = ["#2dd4bf", "#f3c27a", "#fb7185", "#93c5fd", "#c4b5fd"];
    let angle = 0;
    const stops = values.map((value, index) => {
      const start = angle;
      angle += (value / total) * 360;
      return `${colors[index % colors.length]} ${start}deg ${angle}deg`;
    });
    const legend = (spec.labels || []).map((label, index) =>
      `<li><i style="background:${colors[index % colors.length]}"></i>${esc(label)} <b>${esc(values[index])}</b></li>`
    ).join("");
    return `<div class="pie-wrap"><div class="pie" style="background:conic-gradient(${stops.join(",")})"></div><ul class="legend">${legend}</ul></div>`;
  }
  if (kind === "line") {
    const values = spec.values || [];
    const max = Math.max(...values, 1);
    const w = 520;
    const h = 180;
    const pts = values.map((value, index) => {
      const x = values.length === 1 ? w / 2 : (index / (values.length - 1)) * (w - 24) + 12;
      const y = h - 20 - (value / max) * (h - 40);
      return [x, y];
    });
    const d = pts.map((p, i) => `${i ? "L" : "M"}${p[0]},${p[1]}`).join(" ");
    const dots = pts.map((p) => `<circle cx="${p[0]}" cy="${p[1]}" r="4" />`).join("");
    const labels = (spec.labels || []).map((label) => `<span>${esc(label)}</span>`).join("");
    return `<svg viewBox="0 0 ${w} ${h}" class="line-chart"><path d="${d}" />${dots}</svg><div class="axis-labels">${labels}</div>`;
  }
  if (kind === "box") {
    const { min = 0, q1 = 25, median = 50, q3 = 75, max = 100 } = spec;
    const span = Math.max(1, max - min);
    const pct = (n) => ((n - min) / span) * 100;
    return `<div class="box-plot">
      <div class="whisker" style="left:${pct(min)}%;width:${pct(max) - pct(min)}%"></div>
      <div class="box" style="left:${pct(q1)}%;width:${Math.max(4, pct(q3) - pct(q1))}%"></div>
      <div class="median" style="left:${pct(median)}%"></div>
      <div class="box-labels"><span>min ${esc(min)}</span><span>Q1 ${esc(q1)}</span><span>median ${esc(median)}</span><span>Q3 ${esc(q3)}</span><span>max ${esc(max)}</span></div>
    </div>`;
  }
  if (kind === "scatter") {
    const points = spec.points || [];
    const dots = points.map((point) =>
      `<i style="left:${point.x}%;bottom:${point.y}%" title="${esc(point.label || "")}"></i>`
    ).join("");
    return `<div class="scatter"><div class="plot">${dots}</div><div class="axis-labels"><span>${esc(spec.xLabel || "x")}</span><span>${esc(spec.yLabel || "y")}</span></div></div>`;
  }
  const values = spec.values || [];
  const max = Math.max(...values, 1);
  const bars = values.map((value, index) => {
    const h = Math.round((value / max) * 100);
    return `<div class="vbar ${kind === "hist" ? "hist" : ""}"><b>${esc(value)}</b><i style="--h:${h}%"></i><span>${esc((spec.labels || [])[index] || "")}</span></div>`;
  }).join("");
  return `<div class="vbars ${kind === "hist" ? "is-hist" : ""}">${bars}</div>`;
}

const builders = {
  board(spec) {
    const points = (spec.points || []).map((point, index) =>
      `<li style="--i:${index}">${esc(point)}</li>`
    ).join("");
    return {
      html: `<div class="scene scene-board">
        ${spec.kicker ? `<p class="kicker">${esc(spec.kicker)}</p>` : ""}
        <h3>${esc(spec.title || "")}</h3>
        ${points ? `<ul class="rise-list">${points}</ul>` : ""}
      </div>`,
    };
  },
  split(spec) {
    const col = (side) => `<article class="split-col">
      <p class="kicker">${esc(side.eyebrow || "")}</p>
      <h3>${esc(side.title || "")}</h3>
      <ul>${(side.lines || []).map((line) => `<li>${esc(line)}</li>`).join("")}</ul>
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
      `<article class="bit-card ${row.bit === "1" || row.bit === 1 ? "on" : ""}"><b>${esc(row.bit)}</b><div>${(row.meanings || []).map((m) => `<span>${esc(m)}</span>`).join("")}</div></article>`
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
    const head = `<tr>${(spec.headers || []).map((h) => `<th>${esc(h)}</th>`).join("")}</tr>`;
    const rows = (spec.rows || []).map((row, index) =>
      `<tr style="--i:${index}">${row.map((cell) => `<td>${esc(cell)}</td>`).join("")}</tr>`
    ).join("");
    return { html: shell(spec.title, `<div class="table-wrap"><table class="reveal-table"><thead>${head}</thead><tbody>${rows}</tbody></table></div>`, spec.note) };
  },
  kmap(spec) {
    const cells = spec.cells || [0, 0, 0, 0];
    const boxes = cells.map((cell, index) => `<div class="kcell ${cell ? "one" : ""}" style="--i:${index}">${esc(cell)}</div>`).join("");
    const labels = spec.vars?.length === 3
      ? `<div class="khead"><span></span><span>BC=00</span><span>01</span><span>11</span><span>10</span></div>`
      : `<div class="khead two"><span></span><span>B = 0</span><span>B = 1</span></div>`;
    return {
      html: shell(spec.title || "Karnaugh map", `${labels}<div class="kgrid ${cells.length > 4 ? "three" : "two"}">${boxes}</div><p class="expr">${esc(spec.expr || "")}</p>`, spec.note),
    };
  },
  layers(spec) {
    const layers = spec.layers || [];
    const rows = layers.map((layer, index) =>
      `<li class="osi-row" style="--i:${index}"><b>${esc(layer.name)}</b><span>${esc(layer.job || "")}</span><em>${esc(layer.tag || "")}</em></li>`
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
          `<li class="${i === index ? "hot" : i < index ? "done" : ""}"><b>${i + 1}</b><strong>${esc(item.name)}</strong><span>${esc(item.detail || "")}</span></li>`
        ).join("");
        return `<ol class="pipeline">${items}</ol><p class="frame-note">${esc(step.note || step.detail || "")}</p>`;
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
          return `<div class="sbar ${hot ? "hot" : ""} ${placed ? "placed" : ""}"><i style="--h:${Math.round((value / max) * 100)}%"></i><span>${esc(value)}</span></div>`;
        }).join("");
        return `<div class="sbars">${bars}</div><p class="frame-note">${esc(frame.note || "")}</p>`;
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
          return `<div class="acell ${classes}"><small>${index}</small><b>${esc(value)}</b></div>`;
        }).join("");
        const range = Number.isInteger(frame.low) ? `low ${frame.low} · high ${frame.high}${Number.isInteger(frame.mid) ? ` · mid ${frame.mid}` : ""}` : "";
        return `<div class="acells">${cells}</div><p class="range-label">${esc(range)}</p><p class="frame-note">${esc(frame.note || "")}</p>`;
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
          `<div class="fnode ${node.kind || "step"} ${node.id === id ? "hot" : ""}">${esc(node.text)}</div>`
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
      `<article class="info-card" style="--i:${index}"><p class="kicker">${esc(item.tag || "")}</p><h4>${esc(item.title)}</h4><p>${esc(item.body)}</p></article>`
    ).join("");
    return { html: shell(spec.title, `<div class="card-grid">${cards}</div>`, spec.note) };
  },
  er(spec) {
    const entities = (spec.entities || []).map((entity, index) =>
      `<article class="entity" style="--i:${index}"><h4>${esc(entity.name)}</h4><ul>${(entity.attrs || []).map((attr) => `<li class="${attr.key ? "key" : ""}">${esc(attr.name || attr)}</li>`).join("")}</ul></article>`
    ).join("");
    const links = (spec.links || []).map((link) => `<span class="rel">${esc(link)}</span>`).join("");
    return { html: shell(spec.title || "Entity relationship", `<div class="er">${entities}</div><div class="rels">${links}</div>`, spec.note) };
  },
  stack(spec) {
    const frames = spec.frames || [];
    return {
      html: shell(spec.title || "Stack · last in, first out", `<div data-frames></div>`),
      start: playFrames(frames, { loop: false, ms: 900 }, (frame) => {
        const items = [...(frame.items || [])].reverse().map((item, index) =>
          `<div class="stack-item ${index === 0 ? "top" : ""}">${esc(item)}${index === 0 ? "<i>top</i>" : ""}</div>`
        ).join("");
        return `<div class="stack-wrap"><div class="stack-col">${items || `<div class="empty">empty</div>`}</div></div><p class="frame-note">${esc(frame.note || "")}</p>`;
      }),
    };
  },
  queue(spec) {
    const frames = spec.frames || [];
    return {
      html: shell(spec.title || "Queue · first in, first out", `<div data-frames></div>`),
      start: playFrames(frames, { loop: false, ms: 900 }, (frame) => {
        const items = (frame.items || []).map((item, index, arr) =>
          `<div class="q-item ${index === 0 ? "front" : ""} ${index === arr.length - 1 ? "rear" : ""}">${esc(item)}</div>`
        ).join("");
        return `<div class="queue-wrap"><span>front</span><div class="queue-row">${items || `<div class="empty">empty</div>`}</div><span>rear</span></div><p class="frame-note">${esc(frame.note || "")}</p>`;
      }),
    };
  },
  tree(spec) {
    const levels = spec.levels || [];
    const html = levels.map((level, index) =>
      `<div class="tree-level" style="--i:${index}">${level.map((label) => `<span>${esc(label)}</span>`).join("")}</div>`
    ).join("");
    return { html: shell(spec.title || "Tree", `<div class="tree">${html}</div>`, spec.note) };
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
      `<div class="gnode" style="left:${node.x}%;top:${node.y}%;--i:${index}">${esc(node.label)}</div>`
    ).join("");
    return { html: shell(spec.title || "Graph", `<div class="graph"><svg viewBox="0 0 100 100" preserveAspectRatio="none">${lines}</svg>${dots}</div>`, spec.note) };
  },
  network(spec) {
    const layers = spec.layers || [];
    const cols = layers.map((layer, index) =>
      `<div class="nn-col" style="--i:${index}">${layer.map((label) => `<span class="neuron">${esc(label)}</span>`).join("")}</div>`
    ).join("");
    return { html: shell(spec.title || "Neural network", `<div class="nn">${cols}</div>`, spec.note) };
  },
  chart(spec) {
    return { html: shell(spec.title, chartSvg(spec), spec.note) };
  },
  cycle(spec) {
    const steps = spec.steps || [];
    const items = steps.map((step, index) =>
      `<li style="--i:${index}"><b>${index + 1}</b><strong>${esc(step.name || step)}</strong><span>${esc(step.detail || "")}</span></li>`
    ).join("");
    return { html: shell(spec.title, `<ol class="cycle">${items}</ol>`, spec.note) };
  },
  callout(spec) {
    return {
      html: `<div class="scene scene-callout">
        <p class="kicker">${esc(spec.eyebrow || "Remember")}</p>
        <h3>${esc(spec.title || "")}</h3>
        <p>${esc(spec.body || "")}</p>
      </div>`,
    };
  },
  compare(spec) {
    const headers = spec.headers || [];
    const head = headers.map((header) => `<th>${esc(header)}</th>`).join("");
    const rows = (spec.rows || []).map((row, index) =>
      `<tr style="--i:${index}">${row.map((cell) => `<td>${esc(cell)}</td>`).join("")}</tr>`
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
  return stop;
}
