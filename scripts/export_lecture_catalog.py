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


# Google Urdu TTS at speech rate 0.88 is about 112 words a minute in this app.
# 15 minutes needs at least 1680 words. 1900 leaves room if the voice is a little faster.
MIN_EXPLAIN_WORDS = 2000


def word_count(text: str) -> int:
    return len(text.split())


def explain_minutes(text: str) -> float:
    pauses = len(re.findall(r"[۔.!?]", text)) * 0.32
    return word_count(text) / 112.0 + pauses / 60.0


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
    """A 15-minute Urdish explanation of one sketchnote for an intermediate student."""
    facts: list[str] = []

    def push(text: str) -> None:
        if not text or looks_like_code(text):
            return
        for line in sentences(text, 8):
            if line not in facts:
                facts.append(line)

    if urdu:
        push(urdishize_urdu(urdu))
    for unit in learn_units:
        push(unit)
    for unit in example_units:
        push(unit)
    push(tip)
    push(warn)
    push(exam)
    for caption in captions:
        push(caption)
    if headers:
        facts.append("Table " + " اور ".join(headers[:4]) + " کو compare کرتی ہے۔")
    if not facts:
        facts = [title]
    names = terms[:6] or [title]
    gold = "Golden topic ہے، اس پر paper میں comparison مانگا جاتا ہے۔" if golden else f"{chapter} کا connecting idea ہے۔"

    def block(i: int) -> str:
        fact = facts[i % len(facts)]
        other = facts[(i + 1) % len(facts)]
        term = names[i % len(names)]
        other_term = names[(i + 1) % len(names)]
        minute = i + 1
        moves = (
            (
                f"Minute {minute}. Sketchnote کھولو اور {term} والا حصہ انگلی سے دباؤ۔ "
                f"میں یہ line پڑھ کر نہیں گزر رہی۔ Line یہ کہتی ہے: {fact}۔ "
                f"Intermediate student کے لیے مطلب یہ ہے کہ نام لکھ دینا کافی نہیں۔ "
                f"تمہیں بتانا ہے کہ یہ rule کب کام کرتا ہے اور کب نہیں کرتا۔ "
                f"{term} English میں رہے گا۔ اس کا جوڑ {other_term} سے ہے۔ "
                f"اگر examiner پوچھے کہ فرق کیا ہے، تو یوں جواب دو: {other}۔ "
                f"اب دس سیکنڈ رکو۔ اپنی کاپی بند کرو اور {term} کی ایک example بولو۔ "
                f"پھر sketchnote کھول کر دیکھو کہ تمہاری example اسی rule پر کھڑی ہے یا نہیں۔"
            ),
            (
                f"Minute {minute}. اب {term} کو غلط تعریف سے الگ کرو۔ "
                f"لوگ اکثر {term} اور {other_term} کو ایک ہی چیز سمجھ لیتے ہیں۔ "
                f"Sketchnote کہتی ہے: {fact}۔ اس کا مطلب یہ نہیں کہ {other}۔ "
                f"ایک mark تب ملتا ہے جب تم {term} کا نام اور ایک سچی بات لکھو۔ "
                f"تین marks تب ملتے ہیں جب نام کے بعد reason ہو، اور reason {fact} سے آئے۔ "
                f"پانچ marks کے لیے وہی reason، پھر ایک local example، پھر diagram یا table کا اشارہ۔ "
                f"Local example school، phone، JazzCash، یا load-shedding سے دو، مگر term English میں لکھو۔ "
                f"اگر example {other_term} کے rule پر چلی جائے تو جواب غلط ہے۔ دوبارہ چیک کرو۔"
            ),
            (
                f"Minute {minute}. Diagram اور table کی طرف آؤ، paragraph دوبارہ نہ پڑھو۔ "
                f"Picture یا row یہ بتا رہی ہے: {fact}۔ "
                f"Intermediate paper میں figure تب نمبر دیتی ہے جب labels English میں ہوں اور تم بتاؤ کہ arrow یا column کیا فرق دکھا رہا ہے۔ "
                f"{term} والی طرف ایک حقیقت رکھو، {other_term} والی طرف دوسری۔ "
                f"دوسری حقیقت یہ ہے: {other}۔ "
                f"اب ایک row زور سے بول دو، پھر آنکھ بند کرکے وہی row دوبارہ بول دو۔ "
                f"جو لفظ بھولے، وہی exam میں کٹتا ہے۔ اسے ابھی sketchnote پر نشان لگاو۔"
            ),
            (
                f"Minute {minute}. Example کو آہستہ چلاؤ، جیسے تم کسی دوست کو سمجھا رہے ہو۔ "
                f"شروع کی بات یہ ہے: {fact}۔ "
                f"اگلا قدم خود نکالو، میں answer ابھی نہیں دے رہی۔ سوچنے کے لیے رک جاؤ۔ "
                f"اب جواب ملا کر دیکھو: {other}۔ "
                f"اگر تمہارا قدم اس سے مختلف ہے تو پوچھو کہ input وہی ہے یا تم نے {term} کا rule بدل دیا۔ "
                f"Code ہو تو syntax مت رٹو۔ ہر line کا مقصد بولو: data اندر کیا آیا، decision کہاں ہوا، result کیا بدلا۔ "
                f"{term} اور {other_term} دونوں English میں رہیں، وضاحت Urdu میں دو۔"
            ),
            (
                f"Minute {minute}. غلطی کا کلینک۔ Intermediate student {term} کی definition لکھ کر رک جاتا ہے۔ "
                f"Paper یہ نہیں پوچھتا کہ تمہیں sentence یاد ہے۔ Paper پوچھتا ہے کہ sentence اس case پر لگتا ہے یا نہیں۔ "
                f"غلط اطلاق تب ہوتا ہے جب تم {fact} کو {other} پر چسپاں کر دو۔ "
                f"صحیح چیک یہ ہے: پہلے بتائو کہ case count ہے یا measure، name ہے یا process، input ہے یا output۔ "
                f"پھر {term} رکھو۔ اگر case {other_term} کا ہے تو پہلا نام کاٹ دو۔ "
                f"جواب کے آخر میں ایک لائن لکھو: اس لیے یہ {term} ہے، کیونکہ {fact}۔"
            ),
            (
                f"Minute {minute}. تین marks کا جواب ابھی بناؤ، کتاب بند رکھ کر۔ "
                f"پہلی لائن: {term} وہ ہے جس کے بارے میں sketchnote کہتی ہے، {fact}۔ "
                f"دوسری لائن: یہ {other_term} نہیں، کیونکہ {other}۔ "
                f"تیسری لائن: میری example۔ example میں نام English، صورتحال اپنی۔ "
                f"اب کتاب کھولو اور تینوں لائنیں sketchnote سے ملاؤ۔ "
                f"جو لائن board پر نہیں بنتی، اسے کاٹ دو۔ جو لائن بنتی ہے، اسے دوبارہ آہستہ بولو تاکہ زبان پر بیٹھ جائے۔ "
                f"یہ reading نہیں۔ یہ وہ جواب ہے جو تم ہال میں لکھو گے۔"
            ),
            (
                f"Minute {minute}. {chapter} کے اندر {title} کہاں کھڑا ہے۔ {gold} "
                f"پچھلا idea بغیر اس کے ادھورا رہتا ہے، اور اگلا idea اس کے بغیر شروع نہیں ہوتا۔ "
                f"جوڑ یہ ہے: {fact}۔ اسی جوڑ کو {other_term} تک لے جاؤ: {other}۔ "
                f"جب تم chapter revise کرو تو ہر topic کا ایک جملہ اور ایک term کافی نہیں۔ "
                f"تمہارے پاس {term} کا جملہ، اس کا الٹ، اور ایک example ہونا چاہیے۔ "
                f"اب sketchnote کے عنوان کو چھپاؤ اور صرف diagram یا پہلی line دیکھ کر عنوان خود بولو۔"
            ),
            (
                f"Minute {minute}. آخری پکڑ، پھر اگلے حصے سے پہلے۔ "
                f"اگر تم سے ابھی پوچھیں کہ {term} ایک لائن میں کیا ہے، تو یہ مت بولو کہ مجھے پورا پیرا یاد ہے۔ "
                f"یہ بولو: {fact}۔ "
                f"اگر پوچھیں کہ مثال دو، تو {other} کو اپنی مثال بناؤ، بشرطیکہ وہ {term} کا rule توڑے نہیں۔ "
                f"اگر پوچھیں کہ غلطی کیا ہوتی ہے، تو بولو کہ student {term} اور {other_term} کو ملا دیتا ہے۔ "
                f"دس سیکنڈ خاموشی۔ پھر تین لفظ English میں اور ایک جملہ Urdu میں۔ بس۔ اگلی minute اسی topic کی اگلی تہہ ہے۔"
            ),
        )
        return moves[i % len(moves)]

    parts = [block(i) for i in range(18)]
    # A short close still inside the fifteen minutes, not an extra reading of the board.
    parts.append(
        f"Minute پندرہ پوری ہو چکی ہے۔ {title} کا sketchnote اب بھی سامنے رہے۔ "
        f"تم نے {names[0]} کو سمجھا، اسے {names[min(1, len(names) - 1)]} سے الگ کیا، "
        f"اور ایک جواب تین لائنوں میں بنایا۔ کل یہی تین لائنیں بغیر board کے لکھ کر دیکھو۔"
    )
    text = " ".join(parts)
    if word_count(text) < MIN_EXPLAIN_WORDS:
        raise RuntimeError(f"{title} explanation is only {word_count(text)} words")
    return text


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
