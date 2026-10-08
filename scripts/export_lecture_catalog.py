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


def bold_terms(html: str, limit: int = 12) -> list[str]:
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


COACH = (
    "Class Urdish: yeh definition hai — English terms ke sath likho.",
    "Class Urdish: example ya diagram se is line ko lock karo.",
    "Class Urdish: comparison / table ki row banao.",
    "Class Urdish: working steps number kar ke likho.",
    "Class Urdish: reason ya advantage ko because se joddo.",
    "Class Urdish: exam favourite point — underline karo.",
)


def text_units(html: str) -> list[str]:
    units: list[str] = []
    for p in re.findall(r"<p\b[^>]*>(.*?)</p>", html, flags=re.S):
        t = plain(p)
        if t:
            units.append(t)
    for li in re.findall(r"<li\b[^>]*>(.*?)</li>", html, flags=re.S):
        t = plain(li)
        if t:
            units.append(t)
    if not units:
        t = plain(html)
        if t:
            units.append(t)
    return units


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


def strip_boxes(html: str) -> str:
    leftover = html
    for kind in ("learn", "example", "tip", "warn", "check", "urdu", "exam", "golden"):
        for div in b.extract_class_divs(leftover, kind):
            if re.search(rf'class="[^"]*\bbox\b[^"]*\b{re.escape(kind)}\b', div[:160]):
                leftover = leftover.replace(div, "\n", 1)
    return leftover.strip()


def esc(text: str) -> str:
    return html_lib.escape(text, quote=True)


def urdish_depth(units: list[str]) -> str:
    parts = []
    for i, unit in enumerate(units):
        coach = COACH[i % len(COACH)]
        parts.append(
            f'<p class="urdish"><span class="sk-n">{i + 1}</span> {esc(unit)}'
            f"<em>{esc(coach)}</em></p>"
        )
    return "\n".join(parts)


def table_row_cards(html: str) -> str:
    tables = re.findall(r"<table\b[^>]*>.*?</table>", html, flags=re.S)
    if not tables:
        return ""
    chunks = []
    for table in tables:
        rows = re.findall(r"<tr\b[^>]*>(.*?)</tr>", table, flags=re.S)
        if len(rows) < 2:
            chunks.append(table)
            continue
        headers = [plain(c) for c in re.findall(r"<t[hd]\b[^>]*>(.*?)</t[hd]>", rows[0], flags=re.S)]
        cards = [table]
        for row in rows[1:]:
            cells = [plain(c) for c in re.findall(r"<t[hd]\b[^>]*>(.*?)</t[hd]>", row, flags=re.S)]
            if not cells:
                continue
            bits = []
            for idx, cell in enumerate(cells):
                label = headers[idx] if idx < len(headers) else f"Col {idx + 1}"
                bits.append(
                    f'<div class="sk-cell"><b>{esc(label)}</b><span>{esc(cell)}</span>'
                    f'<i class="urdish">Urdish: {esc(label)} یعنی {esc(cell)}</i></div>'
                )
            mid = "".join(
                bits[j] + ('<span class="sk-vs">→</span>' if j < len(bits) - 1 else "")
                for j in range(len(bits))
            )
            cards.append(f'<div class="sk-row">{mid}</div>')
        chunks.append("".join(cards))
    return "\n".join(chunks)


def extras_html(html: str) -> str:
    bits = []
    for fig in re.findall(r"<figure\b[^>]*>.*?</figure>", html, flags=re.S):
        bits.append(fig)
    tables = table_row_cards(html)
    if tables:
        bits.append(tables)
    for pre in re.findall(r"<pre\b[^>]*>.*?</pre>", html, flags=re.S):
        bits.append(pre)
    for flow in re.findall(r'<div class="flow">.*?</div>', html, flags=re.S):
        bits.append(flow)
    for col in re.findall(r'<div class="two-col">.*?</div>', html, flags=re.S):
        bits.append(col)
    return "\n".join(bits)


def sketch_card(kind: str, heading: str, html: str) -> str:
    units = text_units(html)
    extra = extras_html(html)
    body = urdish_depth(units) if units else ""
    return (
        f'<article class="sk-card {kind}">'
        f"<h3>{esc(heading)}</h3>"
        f"{body}{extra}"
        f"</article>"
    )


def spoken_urdish(
    title: str,
    chapter: str,
    golden: bool,
    learn_units: list[str],
    example_units: list[str],
    tip: str,
    warn: str,
    urdu: str,
    terms: list[str],
    exam: str,
    leftover: str,
) -> str:
    """College-teacher Urdish covering the full lecture sketchnote."""
    bits = [
        "Students, السلام علیکم۔",
        "آج کا lecture sketchnote Urdish میں ہے — poori topic ki in-depth explanation.",
        "Urdish یعنی class والی language: بات Urdu میں، computer کی terms English میں — formal Urdu ترجمہ نہیں۔",
        f"Topic کا title ہے: {title}۔",
        f"یہ chapter {chapter} سے ہے۔",
        "Sketchnote پر diagrams، tables، formulae aur har point ki depth دیکھتے رہو۔",
    ]
    if golden:
        bits.append(
            "یہ Golden topic ہے۔ Board exam میں زیادہ marks اسی سے آتے ہیں۔ دھیان سے سنو۔"
        )
    mixed = urdishize_urdu(urdu) if urdu else ""
    if mixed:
        bits.append("Big idea Urdish میں: " + mixed.rstrip("۔") + "۔")
    bits.append("Ab sketchnote ki poori lecture Urdish میں سنو۔")
    for i, unit in enumerate(learn_units):
        bits.append(f"{URDISH_GLUE[i % len(URDISH_GLUE)]} {unit}")
    if leftover:
        bits.append("Board sketches aur tables bhi sketchnote کا part ہیں: " + leftover)
    for i, unit in enumerate(example_units, 1):
        bits.append(f"Worked example sketchnote {i}: {unit}")
    if tip:
        bits.append("Yaad rakhna: " + tip)
    if warn:
        bits.append("Common mistake: " + warn)
    if terms:
        bits.append("Exam میں یہ terms English میں ہی لکھو: " + ", ".join(terms) + "۔")
        bits.append("ان کا مکمل Urdu ترجمہ examiner نہیں مانگتا۔")
    if exam:
        bits.append("Board پہ سوال English میں یوں آتا ہے: " + exam.rstrip("۔.") + ".")
    bits.append(
        "Answer میں Definition، Explain، Example، Diagram اور Working لکھنا۔ اللہ حافظ۔"
    )
    return " ".join(bits)


def sketchnote_html(
    title: str,
    chapter: str,
    golden: bool,
    block: str,
    urdu: str,
    terms: list[str],
) -> str:
    star = '<span class="sk-badge gold">★ Golden</span>' if golden else ""
    learns = box_inners(block, "learn")
    examples = box_inners(block, "example")
    tips = box_inners(block, "tip")
    warns = box_inners(block, "warn")
    exams = box_inners(block, "exam")
    checks = box_inners(block, "check")
    leftover = strip_boxes(topic_inner(block))
    leftover = re.sub(r"<h2[^>]*>.*?</h2>", "", leftover, flags=re.S)
    mixed = urdishize_urdu(urdu) if urdu else ""
    first = text_units(learns[0])[0] if learns and text_units(learns[0]) else title
    big = mixed or first
    stickies = "".join(f'<span class="sk-sticky">{esc(t)}</span>' for t in terms[:10])
    cards = []
    for i, html in enumerate(learns, 1):
        label = "Concept depth" if len(learns) == 1 else f"Concept depth {i}"
        cards.append(sketch_card("learn", f"{label} · Urdish", html))
    if leftover and (plain(leftover) or "<svg" in leftover or "<table" in leftover or "<pre" in leftover):
        vis = extras_html(leftover)
        heads = re.findall(r"<h3\b[^>]*>.*?</h3>", leftover, flags=re.S)
        lists = re.findall(r"<[ou]l\b[^>]*>.*?</[ou]l>", leftover, flags=re.S)
        cards.append(
            '<article class="sk-card visual"><h3>Board sketches · tables · formulae</h3>'
            + "".join(heads)
            + vis
            + "".join(lists)
            + "</article>"
        )
    for i, html in enumerate(examples, 1):
        cards.append(sketch_card("example", f"Worked example {i} · sketchnote", html))
    if tips or warns:
        t = sketch_card("tip", "Yaad rakhna", tips[0]) if tips else ""
        w = sketch_card("warn", "Common mistake", warns[0]) if warns else ""
        extra_tips = "".join(sketch_card("tip", f"Yaad rakhna {i+1}", x) for i, x in enumerate(tips[1:]))
        extra_warns = "".join(sketch_card("warn", f"Common mistake {i+1}", x) for i, x in enumerate(warns[1:]))
        cards.append(f'<div class="sk-split">{t}{w}</div>{extra_tips}{extra_warns}')
    for html in exams:
        cards.append(sketch_card("exam", "Board exam · English wording", html))
    for html in checks:
        cards.append(sketch_card("check", "Check yourself", html))
    sketch = f"""
<section class="sketchnote" aria-label="Urdish lecture sketchnote">
  <div class="sk-tape"></div>
  <header class="sk-head">
    <div class="sk-badge-row">
      <span class="sk-badge">Lecture-wise Sketchnote</span>
      <span class="sk-badge sk-ur">Urdish · in-depth</span>
      <span class="sk-badge">{esc(chapter)}</span>
      {star}
    </div>
    <p class="sk-kicker">Poora topic class sketchnote — har point, example, table aur diagram.</p>
    <h2 class="sk-title">{esc(title)}</h2>
    <div class="sk-bigidea urdish"><b>Big idea:</b> {esc(big)}</div>
    <div class="sk-terms">{stickies}</div>
  </header>
  <div class="sk-stack">
    {"".join(cards)}
  </div>
</section>
"""
    return b.texify_math(sketch)


def topic_inner(block: str) -> str:
    inner = re.sub(r"^<div[^>]*>", "", block, count=1)
    inner = re.sub(r"</div>\s*$", "", inner)
    inner = re.sub(r"<h2[^>]*>.*?</h2>", "", inner, count=1, flags=re.S)
    inner = re.sub(r'<div class="ans">.*?</div>', "", inner, flags=re.S)
    return b.texify_math(inner.strip())


def board_html(title: str, chapter: str, golden: bool, sketch: str, body: str) -> str:
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
  {sketch}
  <h2 class="eng-board">English board · exam wording</h2>
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
        learn_htmls = box_inners(block, "learn")
        example_htmls = box_inners(block, "example")
        learn_units = [u for html in learn_htmls for u in text_units(html)]
        example_units = [u for html in example_htmls for u in text_units(html)]
        learn = " ".join(learn_units)
        urdu = b.topic_urdu(block)
        exam = " ".join(u for html in box_inners(block, "exam") for u in text_units(html))
        tip = " ".join(u for html in box_inners(block, "tip") for u in text_units(html))
        warn = " ".join(u for html in box_inners(block, "warn") for u in text_units(html))
        leftover_plain = plain(strip_boxes(topic_inner(block)))[:1200]
        terms = bold_terms("".join(learn_htmls) + "".join(example_htmls))
        chapter_label = f"{grade.upper()} · Chapter {ch_num} · {ch_title}"
        sketch = sketchnote_html(title, chapter_label, golden, block, urdu, terms)
        rel = f"whiteboards/{grade}/{ch_num}/{i:02d}.html"
        (ch_dir / f"{i:02d}.html").write_text(
            board_html(title, chapter_label, golden, sketch, topic_inner(block)),
            encoding="utf-8",
        )
        rows.append({
            "id": f"{grade}-{ch_num}-{i}",
            "title": title,
            "golden": golden,
            "learn": learn[:4000],
            "urdu": urdu,
            "spokenUrdu": spoken_urdish(
                title, ch_title, golden, learn_units, example_units,
                tip, warn, urdu, terms, exam, leftover_plain,
            ),
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
