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
    if "bootcamp" in low:
        return "bootcamp"
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


def urdu_sentences(urdu: str) -> list[str]:
    text = keep_english_terms(urdu)
    parts = re.split(r"(?<=[۔!?])\s+", text)
    return [part.strip() for part in parts if part.strip()]


def take_sentence(pool: list[str]) -> str:
    if not pool:
        return ""
    sentence = pool.pop(0)
    if len(sentence) < 42 and pool:
        sentence = sentence.rstrip("۔") + "۔ " + pool.pop(0)
    return sentence


def clip_sentence(inner: str, limit: int = 140) -> str:
    text = plain(re.sub(r'<div class="ans">.*?</div>', "", inner, flags=re.S))
    parts = re.split(r"(?<=[.!?])\s+", text)
    line = parts[0].strip() if parts else text
    if len(line) > limit:
        line = line[: limit - 1].rstrip() + "…"
    return line.rstrip(".!? ")


def finish(line: str) -> str:
    line = re.sub(r"\s+", " ", line).strip().rstrip(".!?۔")
    return f"{line}۔" if line else ""


def ensure_urdish(line: str, terms: str = "") -> str:
    """Keep every vocal line mixed: Urdu wording plus at least one English term."""
    text = re.sub(r"\s+", " ", line).strip()
    has_urdu = bool(re.search(r"[\u0600-\u06FF]", text))
    has_english = bool(re.search(r"[A-Za-z]", text))
    if has_urdu and has_english:
        return text if text.endswith(("۔", ".", "!", "?")) else text + "۔"
    if has_urdu:
        term = terms or "sketchnote"
        return finish(f"{text.rstrip('۔. ')}، term English میں {term}")
    if text:
        return finish(f"مطلب Urdish میں سنو، الفاظ English میں رہتے ہیں: {text.rstrip('. ')}")
    return "Sketchnote full-scale دیکھو، آواز Urdish ہے۔"


def panel_fallback(kind: str, inner: str) -> str:
    """Urdish line: Urdu explains, the CS term stays English. Never English-only or Urdu-only."""
    local = [term.rstrip(".!? ") for term in bold_terms(inner, 3)]
    if not local:
        words = re.findall(r"[A-Za-z][A-Za-z0-9+\-]{2,24}", plain(inner))
        skip = {"the", "and", "for", "with", "this", "that", "from", "your", "you", "are", "not"}
        local = []
        for word in words:
            if word.lower() in skip or word in local:
                continue
            local.append(word)
            if len(local) == 3:
                break
    terms = " ".join(local) or "sketchnote"
    if kind == "diagram":
        cap = plain(" ".join(re.findall(r"<figcaption>(.*?)</figcaption>", inner, flags=re.S)))
        label = cap or terms
        return finish(f"یہ SVG diagram دیکھو، label English میں ہے: {label}")
    if kind == "table":
        headers = [plain(x) for x in re.findall(r"<th[^>]*>(.*?)</th>", inner, flags=re.S)]
        heads = "، ".join(h for h in headers if h)[:90] or terms
        return finish(f"Table کا فرق Urdish میں سنو، headings English میں: {heads}")
    if kind == "example":
        return finish(f"Example sketchnote پر English میں ہے، میں Urdish میں steps سمجھا رہی ہوں: {terms}")
    if kind == "tip":
        return finish(f"یاد رکھو، یہ نکتہ English sketchnote پر ہے: {terms}")
    if kind == "warn":
        return finish(f"عام غلطی سے بچو۔ غلط term English میں لکھا ہے: {terms}")
    if kind == "check":
        return finish(f"اب خود check کرو، سوال English sketchnote پر ہے: {terms}")
    if kind == "exam":
        return finish(f"امتحان میں Define, Explain, Example, Diagram لکھنا ہے: {terms}")
    if kind == "code":
        return finish(f"یہ code English میں ہے، logic Urdish میں سنو: {terms}")
    if kind == "flow":
        return finish(f"Steps English sketchnote پر ہیں، ترتیب Urdish میں: {terms}")
    if kind == "bootcamp":
        return finish(f"Self-Taught Bootcamp block، coaching class کی جگہ: {terms}")
    return finish(f"Sketchnote full-scale دیکھو، وضاحت Urdish میں، term English میں: {terms}")


def urdish_beat(
    kind: str,
    inner: str,
    title: str,
    chapter: str,
    golden: bool,
    pool: list[str],
) -> str:
    """One Urdish line: Urdu carries the meaning, CS terms stay English."""
    if kind == "title":
        star = " یہ Golden topic ہے، coaching class کی پوری block یہی لیتی ہے۔" if golden else ""
        return (
            f"Lecture {title}۔ Self-Taught Bootcamp، coaching academy کی جگہ۔"
            f"{star} نوٹس Urdish میں، اصطلاحات English میں۔"
        )
    if kind == "bootcamp":
        minutes = "90" if golden else "45"
        return (
            f"یہ {minutes} minute Self-Taught block ہے، coaching academy class کی جگہ خود پڑھو۔ "
            f"Sketchnote full-scale screen پر رہے گا۔ آواز Urdish ہے، terms English میں: {title}۔"
        )
    sentence = take_sentence(pool)
    if sentence:
        terms = "، ".join(term.rstrip(".!? ") for term in bold_terms(inner, 2))
        return ensure_urdish(sentence, terms)
    return panel_fallback(kind, inner)


def stamp_tag(tag: str, index: int, note: str) -> str:
    note_attr = html_lib.escape(note, quote=True)
    if "data-beat=" not in tag:
        if tag.endswith("/>"):
            tag = f'{tag[:-2]} data-beat="{index}" data-note="{note_attr}" />'
        else:
            tag = f'{tag[:-1]} data-beat="{index}" data-note="{note_attr}">'
    elif "data-note=" not in tag:
        tag = tag[:-1] + f' data-note="{note_attr}">' if tag.endswith(">") else tag
    if 'class="' in tag:
        if "panel" not in tag.split('class="', 1)[1].split('"', 1)[0]:
            tag = tag.replace('class="', 'class="panel ', 1)
    elif tag.endswith(">"):
        tag = tag[:-1] + ' class="panel">'
    return tag


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
    pool = urdu_sentences(urdu)
    chunks: list[str] = []
    lines: list[str] = []
    last = 0
    for i, match in enumerate(matches):
        chunks.append(article[last:match.start()])
        last = match.end()
        nxt = matches[i + 1].start() if i + 1 < len(matches) else len(article)
        inner = article[match.end():nxt]
        line = urdish_beat(beat_kind(match.group(0)), inner, title, chapter, golden, pool)
        chunks.append(stamp_tag(match.group(0), i, line))
        if line:
            lines.append(line)
    chunks.append(article[last:])
    return "".join(chunks), lines


def fallback_diagram(title: str, terms: list[str]) -> str:
    """One inline SVG sketchnote when the lesson has no authored diagram."""
    labels = [term.strip() for term in terms if term.strip()][:3] or [title]
    chunks: list[str] = []
    x = 16
    for index, label in enumerate(labels):
        shown = label if len(label) <= 22 else label[:21] + "…"
        chunks.append(
            f'<rect x="{x}" y="28" width="148" height="52" rx="12" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2.4"/>'
        )
        chunks.append(
            f'<text x="{x + 74}" y="59" text-anchor="middle" font-size="13" font-family="Inter, sans-serif">{html_lib.escape(shown)}</text>'
        )
        if index + 1 < len(labels):
            chunks.append(
                f'<line x1="{x + 152}" y1="54" x2="{x + 176}" y2="54" stroke="#0e7490" stroke-width="2.4"/>'
            )
            chunks.append(
                f'<polygon points="{x + 176},48 {x + 188},54 {x + 176},60" fill="#0e7490"/>'
            )
        x += 196
    width = 16 + 196 * len(labels)
    svg = (
        f'<svg viewBox="0 0 {width} 108" width="{width}" xmlns="http://www.w3.org/2000/svg">'
        + "".join(chunks)
        + "</svg>"
    )
    caption = html_lib.escape(title)
    return f'<figure class="diagram">{svg}<figcaption>{caption}</figcaption></figure>'


def bootcamp_box(item: dict, total_sessions: int) -> str:
    """Student card for the block that used to be a coaching-academy class."""
    minutes = 90 if item["golden"] or item["share"] == "full" else 45
    star = ' <span class="star">★ Golden</span>' if item["golden"] else ""
    partner = item.get("partner") or ""
    if item["share"] == "first-half" and partner:
        when = f"first {minutes} min of block {item['session']} · then {html_lib.escape(partner)}"
    elif item["share"] == "second-half" and partner:
        when = f"second half of block {item['session']} · after {html_lib.escape(partner)}"
    else:
        when = f"{minutes} min block {item['session']} of {total_sessions}"
    return f"""<div class="box bootcamp">
      <p><b>Self-Taught Bootcamp</b>{star} · {when}. This block replaces the coaching-academy class.</p>
      <p>You: keep the sketchnote full size, listen to the Urdish note, then do the check with the book closed.</p>
    </div>"""


def board_html(title: str, chapter: str, golden: bool, article_inner: str) -> str:
    star = '<span class="chip gold">★ Golden</span>' if golden else ""
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
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
  svg: {{ fontCache: 'global', displayAlign: 'left', scale: 1 }},
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
  <div class="note-bar">
    <p class="note-label">Urdish note</p>
    <p id="urdishNote" class="note-urdish" dir="rtl"></p>
  </div>
<article class="board sketchnote">
  <div class="lamp"></div>
  <div class="rail">
    <span class="chip live">Self-Taught Bootcamp</span>
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
    topics = list(b.extract_class_divs(fragment, "topic"))
    items = b.assign_academy_sessions(topics) if topics else []
    total_sessions = items[-1]["session"] if items else 0
    for i, item in enumerate(items, 1):
        block = item["block"]
        raw = b.topic_title(block)
        title = re.sub(r"\s*★.*", "", raw).strip()
        golden = bool(item["golden"])
        learn_html = "".join(box_inners(block, "learn"))
        learn = plain(learn_html)
        urdu = b.topic_urdu(block)
        exam = plain(" ".join(box_inners(block, "exam")))
        tip = plain(" ".join(box_inners(block, "tip")))
        warn = plain(" ".join(box_inners(block, "warn")))
        terms = bold_terms(learn_html)
        chapter_label = f"{grade.upper()} · Chapter {ch_num} · {ch_title}"
        rel = f"whiteboards/{grade}/{ch_num}/{i:02d}.html"
        article = (
            f"<h1>{html_lib.escape(title)}</h1>\n"
            f"{bootcamp_box(item, total_sessions)}\n"
            f"{english_stage(block)}"
        )
        if "<svg" not in article.lower():
            article += "\n" + fallback_diagram(title, terms)
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
