#!/usr/bin/env python3
"""Build CS XII Teach Yourself boards: Urdish-only lectures, MathJax SVG, Flexbox, TTS beats."""
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
WB_OUT = Path(
    os.environ.get(
        "WHITEBOARD_OUT", ROOT / "lectures" / "src" / "main" / "assets" / "whiteboards"
    )
)

spec = importlib.util.spec_from_file_location("booklets_build", BUILD)
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)

CHAPTER_URDU = {
    1: "کمپیوٹر سسٹمز — HCI",
    2: "Computational Thinking اور Algorithms",
    3: "Programming Fundamentals",
    4: "Data اور Analysis",
    5: "Computing کے Applications اور Impacts",
    6: "Digital Age میں Entrepreneurship",
}

AR_WORD = r"[\u0621-\u065F\u0670-\u06D3]+"
AR_CONNECTOR = r"(?:اور|یا|کہ|کا|کی|کے|میں|سے|پہ|پر|ہے|ہیں|اس|یہ|جیسے|یعنی|مثلا)"
PAREN_TERM = re.compile(
    rf"(?<![\u0621-\u06D3])(?:(?!{AR_CONNECTOR}\s){AR_WORD}\s+){{0,3}}{AR_WORD}\s*\(\s*([A-Za-z0-9][^)]{{0,48}})\)"
)
P_TAG = re.compile(r"<p\b([^>]*)>(.*?)</p>", re.S | re.I)
LI_TAG = re.compile(r"<li\b([^>]*)>(.*?)</li>", re.S | re.I)
BEAT_TAG = re.compile(
    r"<h1\b[^>]*>|<h3\b[^>]*>|<table\b[^>]*>|<pre\b[^>]*>|"
    r"<figure\b[^>]*class=\"[^\"]*\bdiagram\b[^\"]*\"[^>]*>|"
    r"<div\b[^>]*class=\"[^\"]*\b(?:box|flow|two-col|term-row)\b[^\"]*\"[^>]*>",
    re.I,
)

TERM_KEEP = (
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
    ("فہرست", "List"),
    ("اوسط", "mean"),
    ("میڈین", "median"),
    ("ویرینس", "variance"),
    ("معیاری انحراف", "standard deviation"),
)

PHRASES: list[tuple[str, str]] = [
    (r"\bFor example\b", "مثلاً"),
    (r"\bfor example\b", "مثلاً"),
    (r"\bThat is an HCI failure, not a banking failure\b", "یہ banking failure نہیں، HCI failure ہے"),
    (r"\bA common mistake is\b", "عام غلطی یہ ہے کہ"),
    (r"\bCommon mistake\b", "عام غلطی"),
    (r"\bRemember\b", "یاد رکھو"),
    (r"\bThis means\b", "اس کا مطلب"),
    (r"\bit means\b", "اس کا مطلب ہے"),
    (r"\bmeans that\b", "کا مطلب ہے کہ"),
    (r"\brefers to\b", "سے مراد ہے"),
    (r"\bis called\b", "کہلاتا ہے"),
    (r"\bare called\b", "کہلاتے ہیں"),
    (r"\bis the process of\b", "وہ عمل ہے جس میں"),
    (r"\bis the study of\b", "کا مطالعہ ہے"),
    (r"\bMake sure\b", "یقینی بناؤ کہ"),
    (r"\bDo not\b", "مت"),
    (r"\bYou will\b", "تم"),
    (r"\bStudents should\b", "طلبہ کو چاہیے کہ"),
    (r"\bIn other words\b", "یعنی"),
    (r"\bNote:\b", "نوٹ:"),
    (r"\bWhy\b", "کیوں"),
    (r"\bbecause\b", "کیونکہ"),
    (r"\band then\b", "پھر"),
    (r"\binstead of\b", "کی بجائے"),
    (r"\bwithout\b", "کے بغیر"),
    (r"\bwith real users\b", "اصل users کے ساتھ"),
]


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


def keep_english_terms(urdu: str) -> str:
    """Classroom Urdish: Urdu grammar, CS terms in English."""
    text = PAREN_TERM.sub(lambda m: m.group(1).strip(), urdu)
    for src, dst in TERM_KEEP:
        text = text.replace(src, dst)
    return re.sub(r"\s+", " ", text).strip()


def spoken_seconds(text: str) -> float:
    words = max(1, len(text.split()))
    pauses = len(re.findall(r"[۔.!?]", text)) * 0.32
    pauses += len(re.findall(r"[،,;:]", text)) * 0.12
    return round(words / 112.0 * 60.0 + pauses + 0.8, 1)


def has_arabic(text: str) -> bool:
    return bool(re.search(r"[\u0600-\u06FF]", text))


def english_terms(text: str, limit: int = 8) -> list[str]:
    stop = {
        "the", "and", "for", "that", "this", "with", "from", "your", "you", "are",
        "was", "were", "have", "has", "not", "but", "can", "into", "when", "then",
        "than", "its", "also", "only", "each", "such", "using", "used", "use",
        "does", "done", "being", "been", "will", "them", "they", "their", "about",
        "after", "before", "over", "under", "between", "because", "which", "what",
        "how", "why", "where", "while", "more", "most", "some", "any", "all",
        "one", "two", "three", "true", "false", "step", "example", "common",
        "mistake", "remember", "check", "yourself", "exam", "tip", "work",
    }
    out, seen = [], set()
    for word in re.findall(r"[A-Za-z][A-Za-z0-9+#._\-()]{1,}", text):
        if word.lower() in stop or len(word) < 2:
            continue
        key = word.lower()
        if key not in seen:
            seen.add(key)
            out.append(word)
        if len(out) >= limit:
            break
    return out


def classroom_urdish(en: str) -> str:
    text = re.sub(r"\s+", " ", en).strip()
    if not text:
        return ""
    if has_arabic(text):
        return keep_english_terms(text)
    mixed = text
    for pat, repl in PHRASES:
        mixed = re.sub(pat, repl, mixed)
    mixed = keep_english_terms(mixed)
    letters = len(re.findall(r"[A-Za-z]", mixed))
    if has_arabic(mixed) and letters < max(12, int(len(mixed) * 0.45)):
        return mixed
    terms = english_terms(text)
    term_bit = "، ".join(terms[:8])
    if term_bit:
        return f"Urdish میں سمجھو — exam terms English میں: {term_bit}۔ پوری lecture TTS سے سنو۔"
    return "یہ نکتہ Urdish lecture اور سیکھیں card میں سمجھو۔"


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
    return b.texify_math(inner.strip())


def rewrite_paragraphs(html: str) -> str:
    def swap(match: re.Match) -> str:
        attrs, inner = match.group(1), match.group(2)
        if re.search(r'class="[^"]*\bur\b', attrs) or has_arabic(inner):
            if has_arabic(inner) and 'class="' in attrs and "ur" not in attrs:
                attrs = re.sub(r'class="([^"]*)"', r'class="\1 ur"', attrs, count=1)
            elif has_arabic(inner) and "class=" not in attrs:
                attrs += ' class="ur"'
            return f"<p{attrs}>{inner}</p>"
        mixed = classroom_urdish(plain(inner))
        return f'<p class="ur">{html_lib.escape(mixed)}</p>'

    html = P_TAG.sub(swap, html)

    def swap_li(match: re.Match) -> str:
        attrs, inner = match.group(1), match.group(2)
        if has_arabic(inner) or re.search(r"<(?:pre|code|svg|table)\b", inner, re.I):
            return match.group(0)
        mixed = classroom_urdish(plain(inner))
        return f"<li{attrs}><span class=\"ur\">{html_lib.escape(mixed)}</span></li>"

    return LI_TAG.sub(swap_li, html)


def keep_visuals(div: str) -> str:
    bits: list[str] = []
    for tag in ("table", "pre", "figure", "ul", "ol"):
        for m in re.finditer(rf"<{tag}\b.*?</{tag}>", div, flags=re.S | re.I):
            bits.append(m.group(0))
    for cls in ("flow", "two-col"):
        bits.extend(b.extract_class_divs(div, cls))
    return "\n".join(bits)


def replace_learn_box(div: str, urdu: str, terms: list[str]) -> str:
    chips = "".join(
        f'<span class="chip">{html_lib.escape(term)}</span>' for term in terms[:8]
    )
    term_row = f'<div class="term-row">{chips}</div>' if chips else ""
    body = f'<p class="ur">{html_lib.escape(keep_english_terms(urdu) or classroom_urdish(plain(div)))}</p>'
    visuals = keep_visuals(div)
    return f'<div class="box learn">\n{body}\n{term_row}\n{visuals}\n</div>'


def urdish_stage(block: str, urdu: str, terms: list[str]) -> str:
    html = topic_inner(block)
    for div in b.extract_class_divs(html, "learn"):
        cls = div[:180]
        if re.search(r'class="[^"]*\bbox\b[^"]*\blearn\b', cls) and "urdu" not in cls:
            html = html.replace(div, replace_learn_box(div, urdu, terms), 1)
    for div in b.extract_class_divs(html, "urdu"):
        if re.search(r'class="[^"]*\bbox\b[^"]*\burdu\b', div[:160]):
            html = html.replace(div, "\n", 1)
    html = rewrite_paragraphs(html)
    cap_re = re.compile(r"<figcaption\b[^>]*>(.*?)</figcaption>", re.S | re.I)

    def cap(m: re.Match) -> str:
        text = classroom_urdish(plain(m.group(1)))
        return f'<figcaption class="ur">{html_lib.escape(text)}</figcaption>'

    return cap_re.sub(cap, html)


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
    if "term-row" in low:
        return "terms"
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
    local = bold_terms(inner, 5)
    if kind == "title":
        bits = [
            "طلبہ، السلام علیکم۔",
            "Teach Yourself lecture صرف Urdish میں ہے۔ CS اصطلاحات English میں رہیں گی۔",
            f"موضوع: {title}۔ باب: {chapter}۔",
        ]
        if golden:
            bits.append("یہ Golden topic ہے، paper میں اکثر آتا ہے۔")
        return " ".join(bits)
    if kind == "learn":
        expl = keep_english_terms(urdu) if urdu else classroom_urdish(plain(inner))
        return "سیکھیں card دیکھو۔ " + (expl.rstrip("۔") + "۔" if expl else "")
    if kind == "terms":
        chips = "، ".join(local) if local else "English terms"
        return f"Flexbox chips دیکھو — یہ exam terms English میں ہیں: {chips}۔"
    if kind == "diagram":
        cap = plain(" ".join(re.findall(r"<figcaption>(.*?)</figcaption>", inner, flags=re.S)))
        extra = f" {classroom_urdish(cap)}" if cap else ""
        return f"SVG diagram draw ہو رہی ہے۔{extra}"
    if kind == "table":
        headers = [plain(x) for x in re.findall(r"<th[^>]*>(.*?)</th>", inner, flags=re.S)]
        heads = "، ".join(h for h in headers if h)[:120]
        return f"Table Flexbox board پر دیکھو: {heads}۔" if heads else "Table board پر ہے۔"
    if kind == "example":
        return "مثال card دیکھو۔ Steps Urdish میں سمجھو، code اور numbers English رہیں گے۔"
    if kind == "tip":
        terms = f" Circled کرو: {', '.join(local)}۔" if local else ""
        return f"یاد رکھیں card دیکھو۔{terms}"
    if kind == "warn":
        return "عام غلطی card دیکھو — exam میں یہ trap آتی ہے۔"
    if kind == "check":
        return "خود پرکھیں — سوال سوچو، پھر جواب card کھولو۔"
    if kind == "exam":
        return "Exam tip: paper پر یہی English terms لکھنا۔ Urdish صرف سمجھنے کے لیے ہے۔"
    if kind == "code":
        return "Python code LTR میں ہے۔ Line by line پڑھو، میں code دوبارہ نہیں بولتی۔"
    if kind == "flow":
        return "Flow Flexbox دیکھو — steps left-to-right ہیں۔"
    terms = f" {', '.join(local)}۔" if local else ""
    return f"اگلا panel دیکھو۔{terms}"


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
        inner = article[match.end() : nxt]
        line = urdish_beat(beat_kind(tag), inner, title, chapter, golden, urdu)
        if line:
            lines.append(line)
    chunks.append(article[last:])
    return "".join(chunks), lines


def board_html(title: str, chapter: str, golden: bool, article_inner: str) -> str:
    star = '<span class="chip gold">★ Golden</span>' if golden else ""
    return f"""<!DOCTYPE html>
<html lang="ur" dir="rtl"><head>
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
  svg: {{ fontCache: 'global', displayAlign: 'center', scale: 0.95 }},
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
    <span class="chip live">Teach Yourself</span>
    <span class="chip">Urdish</span>
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
    ur_chapter = CHAPTER_URDU.get(ch_num, ch_title)
    for i, block in enumerate(b.extract_class_divs(fragment, "topic"), 1):
        raw = b.topic_title(block)
        title = re.sub(r"\s*★.*", "", raw).strip()
        golden = b.topic_is_golden(raw, block)
        learn_html = "".join(box_inners(block, "learn"))
        learn = plain(learn_html)
        urdu = b.topic_urdu(block)
        terms = bold_terms(learn_html)
        chapter_label = f"XII · باب {ch_num} · {ur_chapter}"
        rel = f"whiteboards/{grade}/{ch_num}/{i:02d}.html"
        article = f"<h1>{html_lib.escape(title)}</h1>\n{urdish_stage(block, urdu, terms)}"
        stamped, beats = stamp_beats(article, title, ch_title, golden, urdu)
        if not beats:
            beats = [
                " ".join(
                    [
                        "طلبہ، السلام علیکم۔ Teach Yourself lecture صرف Urdish میں ہے۔",
                        f"موضوع: {title}۔ باب: {ch_title}۔",
                        keep_english_terms(urdu),
                    ]
                )
            ]
        spoken = " ".join(beats)
        (ch_dir / f"{i:02d}.html").write_text(
            board_html(title, chapter_label, golden, stamped),
            encoding="utf-8",
        )
        rows.append(
            {
                "id": f"{grade}-{ch_num}-{i}",
                "title": title,
                "urduTitle": keep_english_terms(urdu)[:80] if urdu else title,
                "golden": golden,
                "learn": learn[:2500],
                "urdu": urdu,
                "spokenUrdu": spoken,
                "beats": beats,
                "readSeconds": int(round(spoken_seconds(spoken))),
                "terms": terms,
                "board": rel,
            }
        )
    return rows


def write_preview(grades: list[dict]) -> None:
    items = []
    for g in grades:
        for ch in g["chapters"]:
            items.append(f'<h2 dir="rtl">{ch["num"]:02d} · {html_lib.escape(ch["title"])}</h2><div class="cards">')
            for t in ch["topics"]:
                star = " ★" if t["golden"] else ""
                items.append(
                    f'<a class="card" href="{html_lib.escape(t["board"])}">{html_lib.escape(t["title"])}{star}</a>'
                )
            items.append("</div>")
    html = f"""<!DOCTYPE html>
<html lang="ur" dir="rtl"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CS XII Teach Yourself — Urdish</title>
<style>
body {{ margin:0; font-family: "Noto Naskh Arabic", sans-serif; background:#07090d; color:#f8fafc; }}
main {{ max-width: 920px; margin: 0 auto; padding: 24px; display:flex; flex-direction:column; gap:16px; }}
.cards {{ display:flex; flex-wrap:wrap; gap:10px; }}
.card {{ flex:1 1 240px; background:#151b24; color:#ccfbf1; text-decoration:none; padding:12px 14px; border-radius:12px; }}
h1,h2 {{ font-weight:800; }}
</style>
</head>
<body>
<main>
  <h1>CS XII Teach Yourself Edition</h1>
  <p>Lectures صرف Urdish میں۔ MathJax SVG · Flexbox · TTS beats۔</p>
  {''.join(items)}
</main>
</body></html>
"""
    (WB_OUT.parent / "preview.html").write_text(html, encoding="utf-8")


def validate(grades: list[dict]) -> None:
    n = 0
    for g in grades:
        for ch in g["chapters"]:
            for t in ch["topics"]:
                n += 1
                path = WB_OUT.parent / t["board"]
                if not path.is_file():
                    raise SystemExit(f"missing board {path}")
                html = path.read_text(encoding="utf-8")
                if "mathjax/tex-svg.js" not in html:
                    raise SystemExit(f"MathJax missing in {path}")
                if 'lang="ur"' not in html:
                    raise SystemExit(f"not Urdish html {path}")
                if not t["beats"]:
                    raise SystemExit(f"no TTS beats {t['id']}")
                joined = " ".join(t["beats"])
                if "بورڈ پر English میں" in joined or "میں English دوبارہ نہیں پڑھتی" in joined:
                    raise SystemExit(f"English-board phrasing leaked into {t['id']}")
                if not has_arabic(joined):
                    raise SystemExit(f"beats not Urdish {t['id']}")
    css = (WB_OUT / "whiteboard.css").read_text(encoding="utf-8")
    if "display: flex" not in css:
        raise SystemExit("Flexbox missing from whiteboard.css")
    if not (WB_OUT / "mathjax" / "tex-svg.js").is_file():
        raise SystemExit("embedded MathJax SVG bundle missing")
    print(f"validated {n} Urdish lectures")


def main() -> int:
    if not MJAX_SRC.is_file():
        raise SystemExit(f"MathJax bundle missing: {MJAX_SRC}")
    WB_OUT.mkdir(parents=True, exist_ok=True)
    if CSS_SRC.exists() and (WB_OUT / "whiteboard.css").resolve() != CSS_SRC.resolve():
        shutil.copy2(CSS_SRC, WB_OUT / "whiteboard.css")
    if JS_SRC.exists() and (WB_OUT / "board.js").resolve() != JS_SRC.resolve():
        shutil.copy2(JS_SRC, WB_OUT / "board.js")
    mjax_dir = WB_OUT / "mathjax"
    mjax_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(MJAX_SRC, mjax_dir / "tex-svg.js")

    folder = b.SRC / "xii"
    chapters = []
    for f in sorted(folder.glob("ch*.html"), key=lambda p: int(re.search(r"\d+", p.stem).group())):
        text = f.read_text(encoding="utf-8")
        num, title, _ = b.chapter_meta(text)
        chapters.append(
            {
                "num": num,
                "title": title,
                "urdu": CHAPTER_URDU.get(num, title),
                "topics": topics_from(text, "xii", num, title),
            }
        )
    book = b.BOOKS["xii"]
    grades = [
        {
            "id": "xii",
            "title": "Computer Science XII — Teach Yourself",
            "urdu": "کمپیوٹر سائنس XII — خود سیکھو Edition، lectures صرف Urdish میں",
            "curriculum": book["curriculum"],
            "chapters": chapters,
        }
    ]
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(json.dumps({"grades": grades}, ensure_ascii=False, indent=2), encoding="utf-8")
    write_preview(grades)
    validate(grades)
    n = sum(len(c["topics"]) for c in chapters)
    print(f"wrote {JSON_OUT} and {n} Urdish boards -> {WB_OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
