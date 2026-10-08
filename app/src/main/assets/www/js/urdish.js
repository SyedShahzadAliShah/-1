(function (root) {
  const ARABIC = /[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]/;
  const LATIN = /[A-Za-z]/;

  function scriptOf(ch) {
    if (ARABIC.test(ch)) return "ur";
    if (LATIN.test(ch)) return "en";
    return "neutral";
  }

  function segmentUrdish(text) {
    const source = String(text || "").replace(/\s+/g, " ").trim();
    if (!source) return [];
    const segments = [];
    let current = "";
    let lang = "en";
    for (const ch of source) {
      const script = scriptOf(ch);
      if (script === "neutral") {
        current += ch;
        continue;
      }
      if (!current) {
        lang = script;
        current = ch;
        continue;
      }
      if (script !== lang) {
        const trimmed = current.trim();
        if (trimmed) segments.push({ l: lang, t: trimmed });
        current = ch;
        lang = script;
      } else {
        current += ch;
      }
    }
    const trimmed = current.trim();
    if (trimmed) segments.push({ l: lang, t: trimmed });
    return mergeTiny(segments);
  }

  function mergeTiny(segments) {
    const out = [];
    for (const seg of segments) {
      const prev = out[out.length - 1];
      if (prev && (seg.t.length < 2 || /^[.,:;!?()/+%-]+$/.test(seg.t))) {
        prev.t = (prev.t + " " + seg.t).replace(/\s+/g, " ").trim();
      } else if (prev && prev.l === seg.l) {
        prev.t = (prev.t + " " + seg.t).replace(/\s+/g, " ").trim();
      } else {
        out.push({ l: seg.l, t: seg.t });
      }
    }
    return out;
  }

  function mixUrdish(en, ur) {
    const english = String(en || "").trim();
    const urdu = String(ur || "").trim();
    if (english && urdu) return segmentUrdish(english + " یعنی " + urdu);
    if (urdu) return segmentUrdish(urdu);
    return segmentUrdish(english);
  }

  root.Urdish = { segmentUrdish, mixUrdish, scriptOf };
})(typeof window !== "undefined" ? window : globalThis);

if (typeof module !== "undefined") {
  module.exports = globalThis.Urdish;
}
