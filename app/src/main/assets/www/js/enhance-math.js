(function (root) {
  const REPLACEMENTS = [
    { re: /\bY\s*=\s*A\s*·\s*B\s*·\s*C\b/g, to: "\\(Y = A \\cdot B \\cdot C\\)" },
    { re: /\bY\s*=\s*A\s*·\s*B\b/g, to: "\\(Y = A \\cdot B\\)" },
    { re: /\bY\s*=\s*A\s*\+\s*B\b/g, to: "\\(Y = A + B\\)" },
    { re: /\bY\s*=\s*A'\b/g, to: "\\(Y = A'\\)" },
    { re: /\bY\s*=\s*A\s*⊕\s*B\b/g, to: "\\(Y = A \\oplus B\\)" },
    { re: /\bO\(n²\)/g, to: "\\(O(n^2)\\)" },
    { re: /\bO\(n\s*log\s*n\)/g, to: "\\(O(n\\log n)\\)" },
    { re: /\bO\(log\s*n\)/g, to: "\\(O(\\log n)\\)" },
    { re: /\bO\(n\)/g, to: "\\(O(n)\\)" },
    { re: /\bO\(1\)/g, to: "\\(O(1)\\)" },
    { re: /2<sup>n<\/sup>/gi, to: "\\(2^{n}\\)" },
    { re: /2<sup>3<\/sup>/gi, to: "\\(2^{3}\\)" },
    { re: /2<sup>4<\/sup>/gi, to: "\\(2^{4}\\)" }
  ];

  function enhanceMath(rootEl) {
    if (!rootEl) return;
    rootEl.querySelectorAll("p, li, td, th, h2, h3, figcaption, .box").forEach((node) => {
      if (node.closest("svg, pre, code, .diagram")) return;
      let html = node.innerHTML;
      if (!html || html.indexOf("\\(") !== -1) return;
      REPLACEMENTS.forEach((rule) => {
        html = html.replace(rule.re, rule.to);
      });
      if (html !== node.innerHTML) node.innerHTML = html;
    });
  }

  function typeset(rootEl) {
    enhanceMath(rootEl);
    if (root.MathJax && MathJax.typesetPromise) {
      return MathJax.typesetPromise([rootEl]).catch(() => {});
    }
    return Promise.resolve();
  }

  root.EnhanceMath = { enhanceMath, typeset };
})(typeof window !== "undefined" ? window : globalThis);
