#!/usr/bin/env python3
"""Build lectures.json and HTML whiteboards (MathJax + SVG + flexbox)."""
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
MJAX_SRC = ROOT / "booklets" / "assets" / "mathjax" / "tex-svg.js"
WB_OUT = Path(os.environ.get("WHITEBOARD_OUT", ROOT / "lectures" / "src" / "main" / "assets" / "whiteboards"))

spec = importlib.util.spec_from_file_location("booklets_build", BUILD)
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)


def plain(text: str) -> str:
    text = b.unescape(b.strip_tags(text))
    text = text.replace("★ Golden", "").replace("★", "")
    return re.sub(r"\s+", " ", text).strip()


def bold_terms(html: str) -> list[str]:
    found = [plain(x) for x in re.findall(r"<b>(.*?)</b>", html, flags=re.S)]
    out, seen = [], set()
    for term in found:
        if 2 < len(term) < 48:
            key = term.lower()
            if key not in seen:
                seen.add(key)
                out.append(term)
        if len(out) >= 8:
            break
    return out


SENT_SPLIT = re.compile(r"(?<=[.!?۔])\s+")
# Only the short Arabic label immediately before "(English Term)".
AR_WORD = r"[\u0621-\u065F\u0670-\u06D3]+"
AR_CONNECTOR = r"(?:اور|یا|کہ|کا|کی|کے|میں|سے|پہ|پر|ہے|ہیں|اس|یہ|جیسے|یعنی|مثلا)"
PAREN_TERM = re.compile(
    rf"(?<![\u0621-\u06D3])(?:(?!{AR_CONNECTOR}\s){AR_WORD}\s+){{0,3}}{AR_WORD}\s*\(\s*([A-Za-z0-9][^)]{{0,48}})\)"
)
URDISH_GLUE = (
    "دیکھو، English board پہ لکھا ہے:",
    "Matlab یہ ہوا کہ",
    "اگلی بات یہ ہے:",
    "Example سے سمجھو:",
    "یاد رکھنا:",
    "ایک اور point:",
    "Board کے لیے یہ line important ہے:",
)


def sentences(text: str, limit: int = 7) -> list[str]:
    parts = SENT_SPLIT.split(re.sub(r"\s+", " ", text).strip())
    out: list[str] = []
    for part in parts:
        part = part.strip(" ;")
        if len(part) > 12:
            out.append(part)
        if len(out) >= limit:
            break
    return out


def urdishize_urdu(urdu: str) -> str:
    """Classroom Urdish: keep Urdu verbs, promote English CS terms out of parentheses."""
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


def spoken_urdish(
    title: str,
    chapter: str,
    golden: bool,
    learn: str,
    urdu: str,
    terms: list[str],
    exam: str,
) -> str:
    """College-teacher Urdish: Urdu grammar + English computer terms, not literary Urdu."""
    bits = [
        "Students, السلام علیکم۔",
        "آج ہم English lecture کو Urdish میں explain کر رہے ہیں۔",
        "Urdish یعنی class والی language: بات Urdu میں، computer کی terms English میں — formal Urdu ترجمہ نہیں۔",
        f"Topic کا title ہے: {title}۔",
        f"یہ chapter {chapter} سے ہے۔",
        "Whiteboard پر diagrams، tables اور formulae دیکھتے رہو۔",
    ]
    if golden:
        bits.append(
            "یہ Golden topic ہے۔ Board exam میں زیادہ marks اسی سے آتے ہیں۔ دھیان سے سنو۔"
        )
    bits.append("اب lecture Urdish میں سنو۔")
    mixed = urdishize_urdu(urdu) if urdu else ""
    if mixed:
        bits.append(mixed.rstrip("۔") + "۔")
    learn_sents = sentences(learn, 6)
    if learn_sents:
        bits.append("English note کی key lines یہ ہیں:")
        for i, sent in enumerate(learn_sents):
            prefix = URDISH_GLUE[i] if i < len(URDISH_GLUE) else "اور:"
            bits.append(f"{prefix} {sent}")
    if terms:
        bits.append("Exam میں یہ terms English میں ہی لکھو: " + ", ".join(terms) + "۔")
        bits.append("ان کا مکمل Urdu ترجمہ examiner نہیں مانگتا۔")
    if exam:
        bits.append("Board پہ سوال English میں یوں آتا ہے: " + exam.rstrip("۔.") + ".")
    bits.append(
        "Answer میں Definition، Explain، Example، Diagram اور Working لکھنا۔ اللہ حافظ۔"
    )
    return " ".join(bits)


def topic_inner(block: str) -> str:
    inner = re.sub(r"^<div[^>]*>", "", block, count=1)
    inner = re.sub(r"</div>\s*$", "", inner)
    inner = re.sub(r"<h2[^>]*>.*?</h2>", "", inner, count=1, flags=re.S)
    inner = re.sub(r'<div class="ans">.*?</div>', "", inner, flags=re.S)
    return b.texify_math(inner.strip())


def board_html(title: str, chapter: str, golden: bool, body: str) -> str:
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
<article class="board">
  <div class="rail">
    <span class="chip">Whiteboard</span>
    <span class="chip">{html_lib.escape(chapter)}</span>
    {star}
  </div>
  <h1>{html_lib.escape(title)}</h1>
  {body}
</article>
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
        learn_html = b.extract_box_html(block, "learn") or ""
        learn = plain(learn_html)[:1800]
        urdu = b.topic_urdu(block)
        exam = b.clip_text(b.extract_box_text(block, "exam"), 220)
        terms = bold_terms(learn_html)
        rel = f"whiteboards/{grade}/{ch_num}/{i:02d}.html"
        (ch_dir / f"{i:02d}.html").write_text(
            board_html(title, f"{grade.upper()} · Chapter {ch_num} · {ch_title}", golden, topic_inner(block)),
            encoding="utf-8",
        )
        rows.append({
            "id": f"{grade}-{ch_num}-{i}",
            "title": title,
            "golden": golden,
            "learn": learn,
            "urdu": urdu,
            "spokenUrdu": spoken_urdish(title, ch_title, golden, learn, urdu, terms, exam),
            "terms": terms,
            "board": rel,
        })
    return rows


def main() -> int:
    WB_OUT.mkdir(parents=True, exist_ok=True)
    if CSS_SRC.exists() and (WB_OUT / "whiteboard.css").resolve() != CSS_SRC.resolve():
        shutil.copy2(CSS_SRC, WB_OUT / "whiteboard.css")
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
