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


def spoken_urdu(title: str, chapter: str, golden: bool, urdu: str, terms: list[str], exam: str) -> str:
    bits = [
        "طلبہ، السلام علیکم۔",
        "آج ہم کالج کے طالب علموں کو انگریزی لیکچر نوٹس اردو میں سمجھا رہے ہیں۔",
        f"سبق کا عنوان ہے: {title}۔",
        f"یہ باب {chapter} سے ہے۔",
        "بورڈ پر خاکے، جدول اور فارمولے دیکھتے رہو۔",
    ]
    if golden:
        bits.append("یہ گولڈن موضوع ہے۔ بورڈ امتحان میں زیادہ نمبر اسی سے آتے ہیں۔ پوری توجہ سے سنو۔")
    if urdu:
        bits.append("اب سبق کی وضاحت سنو۔")
        bits.append(urdu.rstrip("۔") + "۔")
    if terms:
        bits.append("انگریزی نوٹ میں یہ اصطلاحات یاد رکھو: " + "، ".join(terms) + "۔")
    if exam:
        bits.append("بورڈ میں یہ یوں پوچھا جاتا ہے: " + exam.rstrip("۔") + "۔")
    bits.append("جواب میں تعریف، وضاحت، مثال، خاکہ اور ورکنگ لکھنا۔ اللہ حافظ۔")
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
            "spokenUrdu": spoken_urdu(title, ch_title, golden, urdu, terms, exam),
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
