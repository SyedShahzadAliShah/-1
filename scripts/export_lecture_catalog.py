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
    "دیکھو، sketchnote پہ لکھا ہے:",
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


LATIN_RUN = re.compile(r"[A-Za-z][A-Za-z0-9 +/._'()%-]{0,48}")


def bidi_mix(text: str) -> str:
    """Keep English CS terms LTR inside RTL Urdish sentences."""
    parts: list[str] = []
    last = 0
    for m in LATIN_RUN.finditer(text):
        if m.start() > last:
            parts.append(esc(text[last:m.start()]))
        parts.append(f'<span dir="ltr">{esc(m.group(0))}</span>')
        last = m.end()
    parts.append(esc(text[last:]))
    return "".join(parts)


def norm_key(text: str) -> str:
    key = plain(text).lower()
    key = re.sub(r"[^a-z0-9\u0600-\u06ff]+", " ", key)
    return re.sub(r"\s+", " ", key).strip()


def fresh(text: str, seen: set[str]) -> bool:
    """True when this line is not already on the sketchnote."""
    key = norm_key(text)
    if len(key) < 8:
        return False
    for prev in seen:
        if key == prev or (len(key) > 28 and (key in prev or prev in key)):
            return False
    seen.add(key)
    return True


def unique_units(units: list[str], seen: set[str]) -> list[str]:
    return [unit for unit in units if fresh(unit, seen)]


def urdish_depth(units: list[str]) -> str:
    parts = []
    for i, unit in enumerate(units):
        parts.append(f'<p class="urdish"><span class="sk-n">{i + 1}</span> {esc(unit)}</p>')
    return "\n".join(parts)


def table_row_cards(html: str) -> str:
    return "\n".join(re.findall(r"<table\b[^>]*>.*?</table>", html, flags=re.S))


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


def sketch_card(kind: str, heading: str, html: str, seen: set[str]) -> str:
    units = unique_units(text_units(html), seen)
    extra = extras_html(html)
    if not units and not extra:
        return ""
    body = urdish_depth(units) if units else ""
    return (
        f'<article class="sk-card {kind}">'
        f"<h3>{esc(heading)}</h3>"
        f"{body}{extra}"
        f"</article>"
    )


def lead_line(text: str, limit: int = 160) -> str:
    parts = sentences(text, 1)
    line = parts[0] if parts else text
    line = re.sub(r"\s+", " ", line).strip()
    if len(line) > limit:
        line = line[:limit].rsplit(" ", 1)[0]
    return line.rstrip(".۔")


def looks_like_code(text: str) -> bool:
    return text.count("\n") > 1 or len(re.findall(r"[{}();=<>]", text)) >= 4


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
    captions: list[str],
    headers: list[str],
) -> str:
    """Explain the sketchnote in Urdish. Do not read the board aloud."""
    bits = [
        f"Students، {title} کا sketchnote سامنے رکھو۔ میں sentences نہیں پڑھوں گی، idea explain کروں گی۔",
        "Terms English میں رہیں گی، بات class والی Urdu میں ہوگی۔",
    ]
    if golden:
        bits.append(
            "یہ Golden topic ہے۔ Intermediate paper میں صرف definition کافی نہیں، comparison اور ایک example بھی چاہیے۔"
        )
    else:
        bits.append(f"یہ {chapter} کا ایک connecting idea ہے۔ اگلے topic سے جوڑ کر رکھو۔")

    mixed = urdishize_urdu(urdu) if urdu else ""
    if mixed:
        bits.append("اپنے الفاظ میں idea یہ ہے: " + mixed.rstrip("۔") + "۔")
        bits.append("Sketchnote کی ہر line اسی idea کی ایک شکل ہے۔ پوری line رٹنے کے بجائے پوچھو کہ یہ idea کیوں true ہے۔")
    elif learn_units and not looks_like_code(learn_units[0]):
        bits.append("Sketchnote کی پہلی line کا مطلب یہ ہے: " + lead_line(learn_units[0]) + "۔")

    if terms:
        shown = ", ".join(terms[:4])
        bits.append(
            f"Board پر نام English میں ہیں: {shown}۔ "
            "امتحان میں نام English میں لکھو، اور ہر نام کے ساتھ ایک reason دو۔"
        )

    if captions:
        bits.append(
            "Diagram definition کی کاپی نہیں۔ Picture یہ کہہ رہی ہے: "
            + lead_line(captions[0])
            + "۔ خود بتاؤ کہ یہ picture idea کے کس حصے کو دکھا رہی ہے۔"
        )
    if headers:
        heads = " اور ".join(headers[:3])
        bits.append(
            f"Table {heads} کو compare کرتی ہے۔ ایک row لے کر فرق بول دو۔ پوری table memorize نہ کرو۔"
        )

    if example_units:
        sample = example_units[0]
        if looks_like_code(sample):
            bits.append(
                "Example code ہے۔ Syntax مت پڑھو۔ ہر line کا مقصد بولو: input کیا ہے، decision کہاں ہے، output کیا بدل گیا۔"
            )
        else:
            bits.append(
                "Example اس لیے ہے کہ rule کو ایک case پر چلاؤ۔ شروع یوں ہوتا ہے: "
                + lead_line(sample)
                + "۔ اب answer چھپا کر next step خود بولو۔"
            )

    if tip and not looks_like_code(tip):
        bits.append("یاد رکھنے کی چابی سارا پیرا نہیں۔ چابی یہ ہے: " + lead_line(tip) + "۔")
    if warn and not looks_like_code(warn):
        bits.append(
            "Intermediate student یہ غلطی کرتا ہے: "
            + lead_line(warn)
            + "۔ اس لیے جواب میں reason بھی لکھنا۔"
        )
    if exam and not looks_like_code(exam):
        bits.append(
            "Board سوال کی شکل یہ ہوتی ہے: "
            + lead_line(exam)
            + "۔ جواب میں Define، فرق، اور ایک example۔"
        )
    bits.append("اب sketchnote دیکھ کر دو جملوں میں بتاؤ کہ یہ topic کیا فرق سکھا رہا ہے۔")
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
    seen: set[str] = set()
    fresh(title, seen)
    cards = []
    for i, html in enumerate(learns, 1):
        label = "Learn" if len(learns) == 1 else f"Learn {i}"
        cards.append(sketch_card("learn", label, html, seen))
    if leftover and (plain(leftover) or "<svg" in leftover or "<table" in leftover or "<pre" in leftover):
        vis = extras_html(leftover)
        heads = re.findall(r"<h3\b[^>]*>.*?</h3>", leftover, flags=re.S)
        lists = re.findall(r"<[ou]l\b[^>]*>.*?</[ou]l>", leftover, flags=re.S)
        if vis or heads or lists:
            cards.append(
                '<article class="sk-card visual"><h3>Diagram</h3>'
                + "".join(heads)
                + vis
                + "".join(lists)
                + "</article>"
            )
    for i, html in enumerate(examples, 1):
        label = "Example" if len(examples) == 1 else f"Example {i}"
        cards.append(sketch_card("example", label, html, seen))
    for i, html in enumerate(tips, 1):
        label = "Remember" if len(tips) == 1 else f"Remember {i}"
        cards.append(sketch_card("tip", label, html, seen))
    for i, html in enumerate(warns, 1):
        label = "Mistake" if len(warns) == 1 else f"Mistake {i}"
        cards.append(sketch_card("warn", label, html, seen))
    for html in exams:
        cards.append(sketch_card("exam", "Exam", html, seen))
    for html in checks:
        cards.append(sketch_card("check", "Check", html, seen))
    cards = [card for card in cards if card]
    sketch = f"""
<section class="sketchnote" aria-label="Urdish lecture sketchnote">
  <header class="sk-head">
    <div class="sk-badge-row">
      <span class="sk-badge sk-ur">Urdish sketchnote</span>
      {star}
    </div>
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


def board_html(title: str, chapter: str, golden: bool, sketch: str) -> str:
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
        captions = [plain(x) for x in re.findall(r"<figcaption>(.*?)</figcaption>", block, flags=re.S)]
        headers = [plain(x) for x in re.findall(r"<th\b[^>]*>(.*?)</th>", block, flags=re.S)]
        terms = bold_terms("".join(learn_htmls) + "".join(example_htmls))
        chapter_label = f"{grade.upper()} · Chapter {ch_num} · {ch_title}"
        sketch = sketchnote_html(title, chapter_label, golden, block, urdu, terms)
        rel = f"whiteboards/{grade}/{ch_num}/{i:02d}.html"
        (ch_dir / f"{i:02d}.html").write_text(
            board_html(title, chapter_label, golden, sketch),
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
                tip, warn, urdu, terms, exam, captions, headers[:4],
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
