import { esc } from "./scenes.js";
import { rich, typeset } from "./mathtext.js";

const GATE_EXPR = {
  AND: "$Y = A \\cdot B$",
  OR: "$Y = A + B$",
  NOT: "$Y = \\overline{A}$",
  NAND: "$Y = \\overline{A \\cdot B}$",
  NOR: "$Y = \\overline{A + B}$",
  XOR: "$Y = A \\oplus B$",
  XNOR: "$Y = \\overline{A \\oplus B}$",
};

const GATES = {
  AND: (a, b) => (a && b ? 1 : 0),
  OR: (a, b) => (a || b ? 1 : 0),
  NOT: (a) => (a ? 0 : 1),
  NAND: (a, b) => (a && b ? 0 : 1),
  NOR: (a, b) => (a || b ? 0 : 1),
  XOR: (a, b) => (a !== b ? 1 : 0),
  XNOR: (a, b) => (a === b ? 1 : 0),
};

export const labs = [
  {
    id: "gates",
    level: "XI",
    title: "Logic gate bench",
    summary: "Flip inputs and watch AND, OR, NOT, NAND, NOR, XOR, and XNOR decide the output.",
    say: "Pick a gate, then turn input A and input B on or off. The lamp shows the output. NAND and NOR are universal gates because every other gate can be built from them.",
  },
  {
    id: "search",
    level: "XI",
    title: "Binary search bench",
    summary: "Step through a sorted list and watch the search throw away half the remaining items.",
    say: "Binary search only works on a sorted list. Each step checks the middle value. If the target is larger, the left half is ignored. If it is smaller, the right half is ignored.",
  },
  {
    id: "structures",
    level: "XII",
    title: "Stack and queue bench",
    summary: "Push and pop a stack, then enqueue and dequeue a queue, and see which item leaves first.",
    say: "A stack is last in, first out, like a pile of plates. A queue is first in, first out, like a line at a counter. Use a stack for undo. Use a queue when the first arrival should be served first.",
  },
];

function gateView(state) {
  const fn = GATES[state.gate];
  const y = fn(state.a, state.b);
  const unary = state.gate === "NOT";
  const combos = unary ? [0, 1] : [[0, 0], [0, 1], [1, 0], [1, 1]];
  const rows = combos.map((combo) => {
    const a = unary ? combo : combo[0];
    const b = unary ? 0 : combo[1];
    const out = fn(a, b);
    const hot = a === state.a && (unary || b === state.b);
    return `<tr class="${hot ? "hot" : ""}"><td>${a}</td>${unary ? "" : `<td>${b}</td>`}<td>${out}</td></tr>`;
  }).join("");
  const hint = {
    AND: "Y is 1 only when A and B are both 1.",
    OR: "Y is 1 when A or B is 1.",
    NOT: "Y is the opposite of A.",
    NAND: "Y is 0 only when A and B are both 1.",
    NOR: "Y is 1 only when A and B are both 0.",
    XOR: "Y is 1 when A and B differ.",
    XNOR: "Y is 1 when A and B match.",
  }[state.gate];
  return `<div class="bench" data-lab="gates">
    <p class="kicker">Class XI bench</p>
    <h2>Logic gate bench</h2>
    <label>Gate <select data-gate>${Object.keys(GATES).map((name) => `<option ${name === state.gate ? "selected" : ""}>${name}</option>`).join("")}</select></label>
    <div class="switch-row">
      <div><span>A ${state.a}</span><button class="switch" data-input="a" aria-pressed="${state.a ? "true" : "false"}" aria-label="Toggle input A"><i></i></button></div>
      ${unary ? "" : `<div><span>B ${state.b}</span><button class="switch" data-input="b" aria-pressed="${state.b ? "true" : "false"}" aria-label="Toggle input B"><i></i></button></div>`}
    </div>
    <div class="out-row"><div class="lamp ${y ? "lit" : ""}"><span>Y</span><b>${y}</b></div><p>${esc(hint)}</p></div>
    <p class="expr">${rich(GATE_EXPR[state.gate] || "")}</p>
    <table class="truth"><thead><tr><th>A</th>${unary ? "" : "<th>B</th>"}<th>Y</th></tr></thead><tbody>${rows}</tbody></table>
  </div>`;
}

function searchView(state) {
  const values = [2, 5, 8, 12, 16, 23, 31, 42];
  const cells = values.map((value, index) => {
    const dim = index < state.low || index > state.high;
    const mid = index === state.mid;
    const found = state.found === index;
    return `<div class="acell ${dim ? "dim" : ""} ${mid ? "mid" : ""} ${found ? "found" : ""}"><small>${index}</small><b>${value}</b></div>`;
  }).join("");
  return `<div class="bench" data-lab="search">
    <p class="kicker">Class XI bench</p>
    <h2>Binary search</h2>
    <p>Sorted list. Find a target by checking the middle only.</p>
    <div class="stepper">
      <label>Target <input class="num-input" data-target type="number" value="${state.target}" /></label>
      <button class="solid-btn" data-step type="button">Step</button>
      <button class="ghost-btn" data-reset type="button" style="color:white">Reset</button>
    </div>
    <div class="acells" style="margin-top:16px">${cells}</div>
    <p class="frame-note">${esc(state.note)}</p>
  </div>`;
}

function structuresView(state) {
  const stack = [...state.stack].reverse().map((item, index) =>
    `<div class="stack-item ${index === 0 ? "top" : ""}">${esc(item)}</div>`
  ).join("") || `<div class="empty">empty stack</div>`;
  const queue = state.queue.map((item, index) =>
    `<div class="q-item ${index === 0 ? "front" : ""}">${esc(item)}</div>`
  ).join("") || `<div class="empty">empty queue</div>`;
  return `<div class="bench" data-lab="structures">
    <p class="kicker">Class XII bench</p>
    <h2>Stack and queue</h2>
    <div class="stepper">
      <input class="num-input" data-value placeholder="value" value="${esc(state.draft)}" />
      <button class="solid-btn" data-op="push" type="button">Push</button>
      <button class="ghost-btn" data-op="pop" type="button" style="color:white">Pop</button>
      <button class="solid-btn" data-op="enq" type="button">Enqueue</button>
      <button class="ghost-btn" data-op="deq" type="button" style="color:white">Dequeue</button>
    </div>
    <div class="split" style="margin-top:16px">
      <article class="split-col"><h3>Stack</h3><div class="stack-col">${stack}</div></article>
      <article class="split-col"><h3>Queue</h3><div class="queue-row">${queue}</div></article>
    </div>
    <p class="frame-note">${esc(state.note)}</p>
  </div>`;
}

export function renderLab(labId) {
  if (labId === "gates") return gateView({ gate: "AND", a: 1, b: 0 });
  if (labId === "search") return searchView({ target: 23, low: 0, high: 7, mid: null, found: null, note: "Press Step. The first middle is index 3." });
  if (labId === "structures") return structuresView({ stack: ["plate"], queue: ["Ayesha"], draft: "Sara", note: "Push adds to the top. Enqueue joins the rear." });
  return "";
}

export function bindLab(root, labId, narrator, getSpeech) {
  const lab = labs.find((item) => item.id === labId);
  if (!lab) return () => {};
  const state = labId === "gates"
    ? { gate: "AND", a: 1, b: 0 }
    : labId === "search"
      ? { target: 23, low: 0, high: 7, mid: null, found: null, note: "Press Step. The first middle is index 3." }
      : { stack: ["plate"], queue: ["Ayesha"], draft: "Sara", note: "Push adds to the top. Enqueue joins the rear." };

  const paint = () => {
    const html = labId === "gates" ? gateView(state) : labId === "search" ? searchView(state) : structuresView(state);
    root.innerHTML = html;
    typeset(root);
  };

  const onClick = (event) => {
    const input = event.target.closest("[data-input]");
    if (input && labId === "gates") {
      state[input.dataset.input] = state[input.dataset.input] ? 0 : 1;
      paint();
      return;
    }
    if (event.target.matches("[data-step]") && labId === "search") {
      const values = [2, 5, 8, 12, 16, 23, 31, 42];
      state.target = Number(root.querySelector("[data-target]")?.value || state.target);
      if (state.found != null || state.low > state.high) {
        state.note = "Search is finished. Reset to try another target.";
        paint();
        return;
      }
      const mid = Math.floor((state.low + state.high) / 2);
      state.mid = mid;
      const value = values[mid];
      if (value === state.target) {
        state.found = mid;
        state.note = `Found ${state.target} at index ${mid}.`;
      } else if (state.target > value) {
        state.low = mid + 1;
        state.note = `${value} is too small. Ignore indexes below ${state.low}.`;
      } else {
        state.high = mid - 1;
        state.note = `${value} is too large. Ignore indexes above ${state.high}.`;
      }
      if (state.found == null && state.low > state.high) state.note = `${state.target} is not in the list.`;
      paint();
      return;
    }
    if (event.target.matches("[data-reset]") && labId === "search") {
      state.low = 0;
      state.high = 7;
      state.mid = null;
      state.found = null;
      state.target = Number(root.querySelector("[data-target]")?.value || 23);
      state.note = "Reset. Press Step to start from the full list.";
      paint();
      return;
    }
    const op = event.target.closest("[data-op]")?.dataset.op;
    if (op && labId === "structures") {
      const raw = root.querySelector("[data-value]")?.value.trim() || "";
      if ((op === "push" || op === "enq") && raw) {
        if (op === "push") {
          state.stack.push(raw);
          state.note = `Pushed ${raw}. It is now the top, so it would leave first.`;
        } else {
          state.queue.push(raw);
          state.note = `Enqueued ${raw} at the rear. The front is still ${state.queue[0]}.`;
        }
        state.draft = "";
      } else if (op === "pop") {
        const item = state.stack.pop();
        state.note = item ? `Popped ${item}.` : "The stack is empty.";
      } else if (op === "deq") {
        const item = state.queue.shift();
        state.note = item ? `Dequeued ${item} from the front.` : "The queue is empty.";
      }
      paint();
    }
  };

  const onChange = (event) => {
    if (event.target.matches("[data-gate]")) {
      state.gate = event.target.value;
      paint();
    }
    if (event.target.matches("[data-target]")) state.target = Number(event.target.value);
    if (event.target.matches("[data-value]")) state.draft = event.target.value;
  };

  const explain = document.querySelector("[data-explain]");
  const onExplain = () => {
    const speech = getSpeech();
    narrator.speak(lab.say, { lang: speech.lang === "ur" ? "en" : "en", rate: speech.rate, fallbackText: lab.say });
  };

  paint();
  root.addEventListener("click", onClick);
  root.addEventListener("change", onChange);
  explain?.addEventListener("click", onExplain);
  return () => {
    root.removeEventListener("click", onClick);
    root.removeEventListener("change", onChange);
    explain?.removeEventListener("click", onExplain);
    narrator.cancel();
  };
}
