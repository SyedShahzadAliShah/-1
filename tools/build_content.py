#!/usr/bin/env python3
"""Copy Teach Yourself booklets into the sketchnote WebView and emit curriculum.json."""

from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOKLETS = ROOT / "booklets/src"
WWW = ROOT / "app/src/main/assets/www"
CONTENT = WWW / "content"
CURRICULUM = WWW / "data" / "curriculum.json"

STRIP_TAGS = re.compile(r"<[^>]+>")
WS = re.compile(r"\s+")
STAR = re.compile(r"★|\s*Golden\s*", re.I)


def text_of(fragment: str) -> str:
    cleaned = STRIP_TAGS.sub(" ", fragment)
    cleaned = html.unescape(cleaned)
    return WS.sub(" ", cleaned).strip()


def first_box(topic_html: str, kind: str) -> str:
    match = re.search(
        rf'<div class="box {kind}">(.*?)</div>',
        topic_html,
        re.S | re.I,
    )
    return text_of(match.group(1)) if match else ""


def parse_chapter(path: Path, grade: str) -> dict:
    raw = path.read_text(encoding="utf-8")
    dest_dir = CONTENT / grade
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / path.name
    dest.write_text(raw, encoding="utf-8")

    h1 = text_of(re.search(r"<h1>(.*?)</h1>", raw, re.S).group(1)) if re.search(r"<h1>", raw) else path.stem
    opener_ur = ""
    ur = re.search(r'<p class="ur"[^>]*>(.*?)</p>', raw, re.S)
    if ur:
        opener_ur = text_of(ur.group(1))
    first_en = re.search(r'<p(?![^>]*class="ur")[^>]*>(.*?)</p>', raw, re.S)
    opener_en = text_of(first_en.group(1)) if first_en else h1

    topics = [
        {
            "id": f"{grade}-{path.stem}-opener",
            "selector": ".ch-opener, .front, h3, ul.objectives",
            "kind": "opener",
            "titleEn": h1,
            "titleUr": opener_ur[:80] if opener_ur else h1,
            "golden": False,
            "speakEn": opener_en[:900],
            "speakUr": opener_ur[:900],
        }
    ]
    topics.extend(parse_topics(raw, grade, path.stem))
    golden_count = sum(1 for t in topics if t.get("golden"))
    svg_count = raw.count("<svg")
    return {
        "id": f"{grade}-{path.stem}",
        "file": f"content/{grade}/{path.name}",
        "number": 0 if path.stem == "final" else int(re.sub(r"\D", "", path.stem) or "0"),
        "kind": "recap" if path.stem == "final" else "chapter",
        "titleEn": h1,
        "titleUr": opener_ur[:90] if opener_ur else h1,
        "topicCount": max(0, len(topics) - 1),
        "goldenCount": golden_count,
        "svgCount": svg_count,
        "topics": topics,
    }


def parse_topics(raw: str, grade: str, stem: str) -> list[dict]:
    topics = []
    marker = '<div class="topic">'
    starts = [m.start() for m in re.finditer(re.escape(marker), raw)]
    for i, start in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else len(raw)
        block = raw[start:end]
        h2 = re.search(r"<h2>(.*?)</h2>", block, re.S)
        title = text_of(h2.group(1)) if h2 else f"Topic {i + 1}"
        golden = "star" in block or "★" in title
        title_clean = STAR.sub("", title).strip()
        learn = first_box(block, "learn")
        urdu = first_box(block, "urdu")
        example = first_box(block, "example")
        speak_en = " ".join(part for part in (title_clean + ".", learn, example) if part)[:1100]
        speak_ur = urdu[:1100] if urdu else ""
        topics.append(
            {
                "id": f"{grade}-{stem}-t{i + 1}",
                "index": i + 1,
                "kind": "topic",
                "titleEn": title_clean,
                "titleUr": (urdu[:70] + "…") if len(urdu) > 70 else (urdu or title_clean),
                "golden": golden,
                "speakEn": speak_en,
                "speakUr": speak_ur,
            }
        )
    if not topics:
        # recap / mock pages
        for i, h2 in enumerate(re.findall(r"<h2>(.*?)</h2>", raw, re.S)):
            title = text_of(h2)
            topics.append(
                {
                    "id": f"{grade}-{stem}-h{i + 1}",
                    "index": i + 1,
                    "kind": "section",
                    "titleEn": title,
                    "titleUr": title,
                    "golden": False,
                    "speakEn": title,
                    "speakUr": "",
                }
            )
    return topics


def studio_chapter() -> dict:
    return {
        "id": "studio-method",
        "file": "studio/sketchnotes.html",
        "number": 0,
        "kind": "studio",
        "titleEn": "Sketchnote Studio",
        "titleUr": "سکیچ نوٹ اسٹوڈیو",
        "topicCount": 7,
        "goldenCount": 2,
        "svgCount": 6,
        "topics": [
            {
                "id": "studio-1",
                "index": 0,
                "kind": "opener",
                "titleEn": "Teach Yourself Sketchnotes",
                "titleUr": "خود سیکھیں — سکیچ نوٹس",
                "golden": False,
                "speakEn": "Sketchnotes are visual notes that mix drawings, arrows, boxes and a few well-chosen words. This studio teaches you the method, then you apply it to Computer Science XI and XII.",
                "speakUr": "سکیچ نوٹس تصویری نوٹس ہیں جن میں خاکے، تیر، خانے اور چند منتخب الفاظ ہوتے ہیں۔ پہلے طریقہ سیکھیں، پھر کمپیوٹر سائنس پر لگائیں۔",
            },
            {
                "id": "studio-2",
                "index": 1,
                "kind": "topic",
                "titleEn": "Visual vocabulary",
                "titleUr": "بصری الفاظ",
                "golden": True,
                "speakEn": "Every sketchnote uses containers, connectors, icons and emphasis. A box groups an idea. An arrow shows flow. A star marks a golden exam topic.",
                "speakUr": "ہر سکیچ نوٹ میں خانے، تیر، آئیکن اور زور ہوتا ہے۔ خانہ خیال جوڑتا ہے، تیر بہاؤ دکھاتا ہے، ستارہ امتحانی گولڈن ٹاپک ہے۔",
            },
            {
                "id": "studio-3",
                "index": 2,
                "kind": "topic",
                "titleEn": "Flexbox is how the page thinks",
                "titleUr": "فلیکس باکس صفحے کی سوچ",
                "golden": True,
                "speakEn": "Flexbox lays notes in a row or a column, then wraps them like sticky notes on a desk. Main axis, cross axis, grow and wrap — that is the layout engine of this teaching app.",
                "speakUr": "فلیکس باکس نوٹس کو قطار یا کالم میں جماتا ہے اور لپیٹ کر اسٹکی نوٹ کی طرح بچھاتا ہے۔ یہی اس تدریسی ایپ کا لے آؤٹ انجن ہے۔",
            },
            {
                "id": "studio-4",
                "index": 3,
                "kind": "topic",
                "titleEn": "Urdish voice",
                "titleUr": "اردش آواز",
                "golden": False,
                "speakEn": "Urdish means English technical words inside Urdu explanation. Boolean algebra یعنی بولین الجبرا. The app switches voice language at each script change.",
                "speakUr": "اردش کا مطلب ہے انگریزی اصطلاحات کے ساتھ اردو وضاحت۔ ایپ رسم الخط بدلتے ہی آواز کی زبان بدل دیتی ہے۔",
            },
            {
                "id": "studio-5",
                "index": 4,
                "kind": "topic",
                "titleEn": "MathJax formulas",
                "titleUr": "میث جیکس فارمولے",
                "golden": False,
                "speakEn": "Formulas stay as real mathematics, not screenshots. Truth table rows equal 2 to the n. AND is Y equals A times B.",
                "speakUr": "فارمولے اصلی ریاضی رہتے ہیں، تصویر نہیں۔ ٹروتھ ٹیبل کی قطاریں دو کی طاقت n ہوتی ہیں۔",
            },
            {
                "id": "studio-6",
                "index": 5,
                "kind": "topic",
                "titleEn": "SVG diagrams",
                "titleUr": "ایس وی جی خاکے",
                "golden": False,
                "speakEn": "SVG diagrams stay sharp on any phone. Logic gates, OSI layers, stacks and neural nets are drawn as vectors you can zoom.",
                "speakUr": "ایس وی جی خاکے ہر فون پر تیز رہتے ہیں۔ لاجک گیٹس اور او ایس آئی تہیں ویکٹر ہیں، زوم کرنے سے خراب نہیں ہوتیں۔",
            },
            {
                "id": "studio-7",
                "index": 6,
                "kind": "topic",
                "titleEn": "Board-exam sketchnote method",
                "titleUr": "بورڈ امتحان کا طریقہ",
                "golden": False,
                "speakEn": "Preview the title. Listen in Urdish. Copy the diagram on paper. Answer check-yourself from memory. Repeat after one, three and seven days.",
                "speakUr": "عنوان دیکھیں، اردش میں سنیں، خاکہ کاغذ پر اتاریں، سوالات یاد سے حل کریں، ایک تین اور سات دن بعد دہرائیں۔",
            },
        ],
    }


def main() -> None:
    if not BOOKLETS.exists():
        raise SystemExit(f"Missing booklet sources at {BOOKLETS}")
    CONTENT.mkdir(parents=True, exist_ok=True)
    (WWW / "data").mkdir(parents=True, exist_ok=True)

    tracks = [
        {
            "id": "studio",
            "titleEn": "Sketchnote Studio",
            "titleUr": "سکیچ نوٹ اسٹوڈیو",
            "subtitleEn": "Method · Flexbox · Urdish · MathJax · SVG",
            "subtitleUr": "طریقہ · فلیکس باکس · اردش · فارمولے · خاکے",
            "chapters": [studio_chapter()],
        }
    ]

    for grade, title_en, title_ur, sub_en, sub_ur in [
        (
            "xi",
            "Computer Science XI",
            "کمپیوٹر سائنس یازدہم",
            "Sindh Curriculum 2026 · Teach Yourself",
            "سندھ نصاب 2026 · خود سیکھیں",
        ),
        (
            "xii",
            "Computer Science XII",
            "کمپیوٹر سائنس دوازدہم",
            "Sindh Curriculum 2024 / 2025–27 · Teach Yourself",
            "سندھ نصاب · خود سیکھیں",
        ),
    ]:
        files = sorted((BOOKLETS / grade).glob("*.html"), key=lambda p: (p.stem != "ch1", p.stem == "final", p.stem))
        chapters = [parse_chapter(path, grade) for path in files]
        tracks.append(
            {
                "id": grade,
                "titleEn": title_en,
                "titleUr": title_ur,
                "subtitleEn": sub_en,
                "subtitleUr": sub_ur,
                "chapters": chapters,
            }
        )

    payload = {
        "version": "1.0.0",
        "app": "Teach Yourself Sketchnotes",
        "voice": "urdish",
        "layout": "flexbox",
        "diagrams": "svg",
        "math": "mathjax-tex-svg",
        "tracks": tracks,
    }
    CURRICULUM.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    topic_total = sum(len(ch["topics"]) for t in tracks for ch in t["chapters"])
    print(f"Wrote {CURRICULUM} with {topic_total} sketchnote beats")


if __name__ == "__main__":
    main()
