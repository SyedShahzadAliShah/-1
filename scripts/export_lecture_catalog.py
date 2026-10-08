#!/usr/bin/env python3
"""Build lectures.json and cinematic English classroom whiteboards."""
from __future__ import annotations

import html as html_lib
import importlib.util
import json
import os
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "booklets" / "build.py"
JSON_OUT = ROOT / "lectures" / "src" / "main" / "assets" / "lectures.json"
CSS_SRC = ROOT / "lectures" / "src" / "main" / "assets" / "whiteboards" / "whiteboard.css"
JS_SRC = ROOT / "lectures" / "src" / "main" / "assets" / "whiteboards" / "board.js"
MJAX_SRC = ROOT / "booklets" / "assets" / "mathjax" / "tex-svg.js"
WB_OUT = Path(os.environ.get("WHITEBOARD_OUT", ROOT / "lectures" / "src" / "main" / "assets" / "whiteboards"))

spec = importlib.util.spec_from_file_location("booklets_build", BUILD)
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)


def plain(text: str) -> str:
    text = b.unescape(b.strip_tags(text))
    text = text.replace("★ Golden", "").replace("★", "")
    return re.sub(r"\s+", " ", text).strip()


def bold_terms(html: str, limit: int = 8) -> list[str]:
    found = [plain(x) for x in re.findall(r"<b>(.*?)</b>", html, flags=re.S)]
    out, seen = [], set()
    for term in found:
        if 2 < len(term) < 48:
            key = term.lower()
            if key not in seen:
                seen.add(key)
                out.append(term)
        if len(out) >= limit:
            break
    return out


AR_WORD = r"[\u0621-\u065F\u0670-\u06D3]+"
AR_CONNECTOR = r"(?:اور|یا|کہ|کا|کی|کے|میں|سے|پہ|پر|ہے|ہیں|اس|یہ|جیسے|یعنی|مثلا)"
PAREN_TERM = re.compile(
    rf"(?<![\u0621-\u06D3])(?:(?!{AR_CONNECTOR}\s){AR_WORD}\s+){{0,3}}{AR_WORD}\s*\(\s*([A-Za-z0-9][^)]{{0,48}})\)"
)


def urdishize_urdu(urdu: str) -> str:
    """Classroom Urdish for the voice only — not printed on the board."""
    text = PAREN_TERM.sub(lambda m: m.group(1).strip(), urdu)
    for src, dst in (
        ("مقداریں", "quantities"),
        ("مقدار", "quantity"),
        ("درجۂ حرارت", "temperature"),
        ("درجہ حرارت", "temperature"),
        ("ڈیجیٹل نظام", "digital system"),
        ("منفصل", "Discrete"),
        ("مسلسل", "Continuous"),
        ("بِٹ", "bit"),
        ("سچائی جدول", "truth table"),
        ("قطاریں", "rows"),
        ("متغیرات", "variables"),
        ("ایکسپریشن", "expression"),
    ):
        text = text.replace(src, dst)
    return re.sub(r"\s+", " ", text).strip()


def box_inners(block: str, kind: str) -> list[str]:
    out: list[str] = []
    for div in b.extract_class_divs(block, kind):
        if not re.search(rf'class="[^"]*\bbox\b[^"]*\b{re.escape(kind)}\b', div[:160]):
            continue
        inner = re.sub(r"^<div[^>]*>", "", div, count=1)
        inner = re.sub(r"</div>\s*$", "", inner)
        inner = re.sub(r'<div class="ans">.*?</div>', "", inner, flags=re.S)
        out.append(inner.strip())
    return out


def topic_inner(block: str) -> str:
    inner = re.sub(r"^<div[^>]*>", "", block, count=1)
    inner = re.sub(r"</div>\s*$", "", inner)
    inner = re.sub(r"<h2[^>]*>.*?</h2>", "", inner, count=1, flags=re.S)
    inner = re.sub(r'<div class="ans">.*?</div>', "", inner, flags=re.S)
    return b.texify_math(inner.strip())


def english_stage(block: str) -> str:
    """One English copy of the lecture. Urdu boxes stay off the board (voice only)."""
    html = topic_inner(block)
    for div in b.extract_class_divs(html, "urdu"):
        if re.search(r'class="[^"]*\bbox\b[^"]*\burdu\b', div[:160]):
            html = html.replace(div, "\n", 1)
    return html.strip()


def spoken_urdish(
    title: str,
    chapter: str,
    golden: bool,
    urdu: str,
    terms: list[str],
    extra_on_board: bool,
) -> str:
    """Urdish teacher voice. Does not re-read English already on the board."""
    bits = [
        "Students, السلام علیکم۔",
        "Cinematic classroom: English lecture board par write ho raha hai, diagrams draw ho rahe hain.",
        "Main Urdish میں explain karti hon — Urdu grammar, computer terms English میں. Formal Urdu ترجمہ نہیں۔",
        f"Topic: {title}. Chapter: {chapter}.",
    ]
    if golden:
        bits.append("Yeh Golden topic hai — extra dhyan se dekho.")
    mixed = urdishize_urdu(urdu) if urdu else ""
    if mixed:
        bits.append(mixed.rstrip("۔") + "۔")
    if terms:
        bits.append("Board par yeh terms circle karo: " + ", ".join(terms) + ".")
    if extra_on_board:
        bits.append(
            "Remember-it, common-mistake aur exam note English میں board par already written hain. Unhe copy karo — main English dobara nahi padhti."
        )
    bits.append("Copy Definition, Explain, Example, Diagram aur Working. اللہ حافظ.")
    return " ".join(bits)


def board_html(title: str, chapter: str, golden: bool, stage: str) -> str:
    star = '<span class="chip gold">★ Golden</span>' if golden else ""
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html_lib.escape(title)}</title>
<link rel="stylesheet" href="../../whiteboard.css">
<script>
window.MathJax = {{
  tex: {{
    inlineMath: [['\\\\(', '\\\\)']],
    displayMath: [['\\\\[', '\\\\]']],
    processEscapes: true,
    processEnvironments: true
  }},
  svg: {{ fontCache: 'global', displayAlign: 'left', scale: 0.95 }},
  options: {{
    skipHtmlTags: ['script','noscript','style','textarea','pre','code','svg'],
    ignoreHtmlClass: 'diagram'
  }},
  startup: {{ typeset: true }}
}};
</script>
<script src="../../mathjax/tex-svg.js"></script>
</head>
<body>
<div class="cinema">
<article class="board">
  <div class="lamp"></div>
  <div class="rail">
    <span class="chip live">Live classroom</span>
    <span class="chip">{html_lib.escape(chapter)}</span>
    {star}
  </div>
  <h1>{html_lib.escape(title)}</h1>
  {stage}
</article>
</div>
<script src="../../board.js" defer></script>
</body></html>
"""


def topics_from(fragment: str, grade: str, ch_num: int, ch_title: str) -> list[dict]:
    rows = []
    ch_dir = WB_OUT / grade / str(ch_num)
    ch_dir.mkdir(parents=True, exist_ok=True)
    for i, block in enumerate(b.extract_class_divs(fragment, "topic"), 1):
        raw = b.topic_title(block)
        title = re.sub(r"\s*★.*", "", raw).strip()
        golden = b.topic_is_golden(raw, block)
        learn_html = "".join(box_inners(block, "learn"))
        learn = plain(learn_html)
        urdu = b.topic_urdu(block)
        exam = plain(" ".join(box_inners(block, "exam")))
        tip = plain(" ".join(box_inners(block, "tip")))
        warn = plain(" ".join(box_inners(block, "warn")))
        terms = bold_terms(learn_html)
        chapter_label = f"{grade.upper()} · Chapter {ch_num} · {ch_title}"
        rel = f"whiteboards/{grade}/{ch_num}/{i:02d}.html"
        (ch_dir / f"{i:02d}.html").write_text(
            board_html(title, chapter_label, golden, english_stage(block)),
            encoding="utf-8",
        )
        rows.append({
            "id": f"{grade}-{ch_num}-{i}",
            "title": title,
            "golden": golden,
            "learn": learn[:2500],
            "urdu": urdu,
            "spokenUrdu": spoken_urdish(
                title,
                ch_title,
                golden,
                urdu,
                terms,
                extra_on_board=bool(tip or warn or exam),
            ),
            "terms": terms,
            "board": rel,
        })
    return rows


def main() -> int:
    WB_OUT.mkdir(parents=True, exist_ok=True)
    if CSS_SRC.exists() and (WB_OUT / "whiteboard.css").resolve() != CSS_SRC.resolve():
        shutil.copy2(CSS_SRC, WB_OUT / "whiteboard.css")
    if JS_SRC.exists() and (WB_OUT / "board.js").resolve() != JS_SRC.resolve():
        shutil.copy2(JS_SRC, WB_OUT / "board.js")
    mjax_dir = WB_OUT / "mathjax"
    mjax_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(MJAX_SRC, mjax_dir / "tex-svg.js")

    grades = []
    for key, book in b.BOOKS.items():
        folder = b.SRC / key
        chapters = []
        for f in sorted(folder.glob("ch*.html"), key=lambda p: int(re.search(r"\d+", p.stem).group())):
            text = f.read_text(encoding="utf-8")
            num, title, _ = b.chapter_meta(text)
            chapters.append({
                "num": num,
                "title": title,
                "topics": topics_from(text, key, num, title),
            })
        grades.append({
            "id": key,
            "title": book["title"],
            "urdu": book["urdu"],
            "curriculum": book["curriculum"],
            "chapters": chapters,
        })
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(json.dumps({"grades": grades}, ensure_ascii=False, indent=2), encoding="utf-8")
    n = sum(len(c["topics"]) for g in grades for c in g["chapters"])
    print(f"wrote {JSON_OUT} and {n} whiteboards -> {WB_OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
