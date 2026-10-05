/** Turn lecture strings into HTML, with $...$ and $$...$$ left for MathJax. */

export function esc(value) {
  return String(value ?? "").replace(/[&<>"']/g, (ch) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;",
  }[ch]));
}

function tex(source) {
  return String(source).replace(/[&<>]/g, (ch) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
  }[ch]));
}

/** Escape prose and wrap TeX so MathJax can typeset it after the board is mounted. */
export function rich(value) {
  const text = String(value ?? "");
  if (!text.includes("$")) return esc(text);
  return text.split(/(\$\$[\s\S]+?\$\$)/g).map((block) => {
    if (block.startsWith("$$") && block.endsWith("$$") && block.length > 4) {
      return `<div class="math-display">\\[${tex(block.slice(2, -2).trim())}\\]</div>`;
    }
    return block.split(/(\$[^$\n]+?\$)/g).map((part) => {
      if (part.startsWith("$") && part.endsWith("$") && part.length > 2) {
        return `<span class="math-inline">\\(${tex(part.slice(1, -1).trim())}\\)</span>`;
      }
      return esc(part);
    }).join("");
  }).join("");
}

function typesetNow(root) {
  const mathjax = window.MathJax;
  if (!root?.isConnected || !mathjax?.typesetPromise) return;
  try {
    mathjax.typesetClear?.([root]);
  } catch {
    /* A replaced board has nothing left to clear. */
  }
  mathjax.typesetPromise([root]).catch(() => {});
}

/** Typeset MathJax inside root once the local tex-svg build is ready. */
export function typeset(root) {
  if (!root || typeof window === "undefined") return;
  const run = () => typesetNow(root);
  const pending = window.MathJax?.startup?.promise;
  if (pending?.then) {
    pending.then(run).catch(() => {});
    return;
  }
  if (window.MathJax?.typesetPromise) {
    run();
    return;
  }
  const started = Date.now();
  const timer = setInterval(() => {
    if (window.MathJax?.startup?.promise || window.MathJax?.typesetPromise) {
      clearInterval(timer);
      typeset(root);
    } else if (Date.now() - started > 8000) {
      clearInterval(timer);
    }
  }, 40);
}
