/**
 * Saving the study book. In a browser, print() opens the print dialog and save()
 * downloads a self-contained HTML file. Inside the Android app window.print() is
 * a no-op and blob downloads go nowhere, so both calls hand off to the
 * BootcampBook bridge, which opens the system print sheet (with "Save as PDF")
 * or a file picker.
 */

const FILE_NAME = "self-taught-bootcamp-study-book.html";
let cssText = null;

function bridge() {
  if (typeof window === "undefined" || !window.BootcampBook) return null;
  return typeof window.BootcampBook.save === "function" ? window.BootcampBook : null;
}

export function canPrint() {
  return Boolean(bridge()) || typeof window.print === "function";
}

async function stylesheet() {
  if (cssText !== null) return cssText;
  try {
    const response = await fetch("css/bootcamp.css");
    cssText = response.ok ? await response.text() : "";
  } catch {
    cssText = "";
  }
  return cssText;
}

/** A standalone HTML document holding the book as currently rendered (math already typeset to SVG). */
export async function bookDocument(bookEl, { title = "The study book", subtitle = "" } = {}) {
  const css = await stylesheet();
  const mathCss = document.getElementById("MJX-SVG-styles")?.textContent || "";
  // With fontCache "global" every formula's <use> points at glyphs in one shared hidden SVG.
  const glyphCache = document.getElementById("MJX-SVG-global-cache")?.outerHTML || "";
  const fonts = document.querySelector('link[href*="fonts.googleapis"]')?.outerHTML || "";
  const stamp = new Date().toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric" });
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>${escapeHtml(title)} · Self-taught Bootcamp</title>
${fonts}
<style>${css}</style>
<style>${mathCss}</style>
<style>
  body { background: white; }
  .wrap-book { max-width: 1040px; margin: 0 auto; padding: 24px; }
  .book-head { margin: 0 0 18px; }
  .book-head h1 { margin: 0 0 6px; font-family: var(--serif); font-size: 2.2rem; }
  .book-head p { margin: 0; color: var(--ink-soft); }
  @media print { .wrap-book { padding: 0; } }
</style>
</head>
<body>
<main class="wrap wrap-book">
  <header class="book-head">
    <h1>${escapeHtml(title)}</h1>
    <p>Self-taught Bootcamp · Computer Science XI &amp; XII${subtitle ? ` · ${escapeHtml(subtitle)}` : ""} · saved ${escapeHtml(stamp)}</p>
  </header>
  <div class="book">${bookEl.innerHTML}</div>
</main>
${glyphCache}
</body>
</html>`;
}

/** Print the book, or open the Android print sheet whose options include Save as PDF. */
export function printBook(title = "Study book") {
  const native = bridge();
  if (native && typeof native.print === "function") {
    native.print(title);
    return "native";
  }
  window.print();
  return "browser";
}

/** Save the book as an HTML file. Resolves to how it was delivered. */
export async function saveBook(bookEl, options = {}) {
  const html = await bookDocument(bookEl, options);
  const native = bridge();
  if (native) {
    native.save(FILE_NAME, html);
    return "native";
  }
  const blob = new Blob([html], { type: "text/html;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = FILE_NAME;
  document.body.appendChild(link);
  link.click();
  link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 10000);
  return "download";
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"]/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[ch]));
}
