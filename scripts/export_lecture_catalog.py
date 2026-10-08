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


def keep_english_terms(urdu: str) -> str:
    """Urdu explanation for the voice; critical CS terms stay English."""
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
        ("الگورتھم", "algorithm"),
        ("فلو چارٹ", "flowchart"),
        ("ڈیٹا بیس", "database"),
        ("نیٹ ورک", "network"),
        ("آپریٹنگ سسٹم", "operating system"),
        ("پروگرامنگ", "programming"),
        ("فنکشن", "function"),
        ("لوپ", "loop"),
        ("اریے", "array"),
        ("آبجیکٹ", "object"),
    ):
        text = text.replace(src, dst)
    return re.sub(r"\s+", " ", text).strip()


def spoken_seconds(text: str) -> float:
    """Wall-clock for Google Urdu TTS at speech rate 0.88 (Urdish classroom pace)."""
    words = max(1, len(text.split()))
    pauses = len(re.findall(r"[۔.!?]", text)) * 0.32
    pauses += len(re.findall(r"[،,;:]", text)) * 0.12
    return round(words / 112.0 * 60.0 + pauses + 0.8, 1)


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


def spoken_urdu(
    title: str,
    chapter: str,
    golden: bool,
    urdu: str,
    terms: list[str],
    extra_on_board: bool,
) -> str:
    """Fallback single-block Urdish if a topic has no sketchnote beats."""
    bits = [
        "طلبہ، السلام علیکم۔",
        "Sketchnote lecture Urdish میں سمجھا رہی ہوں، اصطلاحات English میں رہیں گی۔",
        f"موضوع: {title}۔ باب: {chapter}۔",
    ]
    if golden:
        bits.append("یہ Golden topic ہے، اس پر خاص توجہ دو۔")
    mixed = keep_english_terms(urdu) if urdu else ""
    if mixed:
        bits.append(mixed.rstrip("۔") + "۔")
    if terms:
        bits.append("Sketchnote پر یہ اصطلاحات English میں ہیں: " + "، ".join(terms) + "۔")
    if extra_on_board:
        bits.append("Remember-it اور common-mistake sketchnotes بورڈ پر English میں ہیں۔ میں English دوبارہ نہیں پڑھتی۔")
    bits.append("Sketchnote کے ساتھ سنو۔ اللہ حافظ۔")
    return " ".join(bits)


BEAT_TAG = re.compile(
    r"<h1\b[^>]*>|<h3\b[^>]*>|<table\b[^>]*>|<pre\b[^>]*>|"
    r"<figure\b[^>]*class=\"[^\"]*\bdiagram\b[^\"]*\"[^>]*>|"
    r"<div\b[^>]*class=\"[^\"]*\b(?:box|flow|two-col)\b[^\"]*\"[^>]*>",
    re.I,
)


def beat_kind(tag: str) -> str:
    low = tag.lower()
    if low.startswith("<h1"):
        return "title"
    if "learn" in low:
        return "learn"
    if "example" in low:
        return "example"
    if "tip" in low:
        return "tip"
    if "warn" in low:
        return "warn"
    if "check" in low:
        return "check"
    if "exam" in low:
        return "exam"
    if "diagram" in low:
        return "diagram"
    if low.startswith("<table"):
        return "table"
    if low.startswith("<pre"):
        return "code"
    if "flow" in low:
        return "flow"
    return "note"


def urdish_beat(
    kind: str,
    inner: str,
    title: str,
    chapter: str,
    golden: bool,
    urdu: str,
) -> str:
    """One Urdish line locked to one sketchnote panel. English terms stay English."""
    local = bold_terms(inner, 5)
    if kind == "title":
        bits = [
            "طلبہ، السلام علیکم۔",
            "Sketchnote lecture Urdish میں سمجھا رہی ہوں، اصطلاحات English میں رہیں گی۔",
            f"موضوع: {title}۔ باب: {chapter}۔",
        ]
        if golden:
            bits.append("یہ Golden topic ہے۔")
        return " ".join(bits)
    if kind == "learn":
        expl = keep_english_terms(urdu) if urdu else ""
        if expl:
            return "Learn-it sketchnote بورڈ پر آ رہی ہے۔ " + expl.rstrip("۔") + "۔"
        return "Learn-it sketchnote بورڈ پر English میں لکھی ہے۔"
    if kind == "diagram":
        cap = plain(" ".join(re.findall(r"<figcaption>(.*?)</figcaption>", inner, flags=re.S)))
        extra = f" {cap}" if cap else ""
        terms = f" اصطلاحات: {', '.join(local)}۔" if local else ""
        return f"Diagram sketchnote draw ہو رہی ہے۔{extra}{terms}"
    if kind == "table":
        headers = [plain(x) for x in re.findall(r"<th[^>]*>(.*?)</th>", inner, flags=re.S)]
        heads = "، ".join(h for h in headers if h)[:120]
        return f"Table sketchnote دیکھو: {heads}۔" if heads else "Table sketchnote بورڈ پر ہے۔"
    if kind == "example":
        terms = f" Steps: {', '.join(local)}۔" if local else ""
        return f"Worked-example sketchnote بورڈ پر English میں ہے۔{terms}"
    if kind == "tip":
        terms = f" {', '.join(local)} English میں circled کرو۔" if local else ""
        return f"Remember-it sketchnote دیکھو۔{terms} میں English دوبارہ نہیں پڑھتی۔"
    if kind == "warn":
        return "Common-mistake sketchnote — غلط فہمی بورڈ پر English میں لکھی ہے۔"
    if kind == "check":
        return "Check-yourself sketchnote — سوالات English میں بورڈ پر ہیں۔ جواب سوچو۔"
    if kind == "exam":
        return "Exam sketchnote بورڈ پر English میں ہے۔"
    if kind == "code":
        return "Code sketchnote بورڈ پر English میں لکھا ہے۔"
    if kind == "flow":
        return "Flow sketchnote دیکھو — steps بورڈ پر English میں ہیں۔"
    terms = f" {', '.join(local)}۔" if local else ""
    return f"Sketchnote بورڈ پر آ رہی ہے۔{terms}"


def stamp_beats(
    article: str,
    title: str,
    chapter: str,
    golden: bool,
    urdu: str,
) -> tuple[str, list[str]]:
    matches = list(BEAT_TAG.finditer(article))
    if not matches:
        return article, []
    chunks: list[str] = []
    lines: list[str] = []
    last = 0
    for i, match in enumerate(matches):
        chunks.append(article[last:match.start()])
        tag = match.group(0)
        if "data-beat=" in tag:
            stamped = tag
        elif tag.endswith("/>"):
            stamped = f'{tag[:-2]} data-beat="{i}" />'
        else:
            stamped = f'{tag[:-1]} data-beat="{i}">'
        chunks.append(stamped)
        last = match.end()
        nxt = matches[i + 1].start() if i + 1 < len(matches) else len(article)
        inner = article[match.end():nxt]
        line = urdish_beat(beat_kind(tag), inner, title, chapter, golden, urdu)
        if line:
            lines.append(line)
    chunks.append(article[last:])
    return "".join(chunks), lines


def board_html(title: str, chapter: str, golden: bool, article_inner: str) -> str:
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
  {article_inner}
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
        article = f"<h1>{html_lib.escape(title)}</h1>\n{english_stage(block)}"
        stamped, beats = stamp_beats(article, title, ch_title, golden, urdu)
        if not beats:
            beats = [spoken_urdu(title, ch_title, golden, urdu, terms, bool(tip or warn or exam))]
        spoken = " ".join(beats)
        (ch_dir / f"{i:02d}.html").write_text(
            board_html(title, chapter_label, golden, stamped),
            encoding="utf-8",
        )
        rows.append({
            "id": f"{grade}-{ch_num}-{i}",
            "title": title,
            "golden": golden,
            "learn": learn[:2500],
            "urdu": urdu,
            "spokenUrdu": spoken,
            "beats": beats,
            "readSeconds": int(round(spoken_seconds(spoken))),
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
