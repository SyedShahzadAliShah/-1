#!/usr/bin/env python3
"""Extract CS Teacher's Edition topics: English body + Urdu narration from PDFs."""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

import argostranslate.translate
import pymupdf

ARABIC_RE = re.compile(r"[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]")
LATIN_RE = re.compile(r"[A-Za-z]")
TOPIC_RE = re.compile(r"^(\d+\.\d+(?:\.\d+)?(?:\s*-\s*\d+\.\d+(?:\.\d+)?)?)\s+(.+)$")
GOLDEN_RE = re.compile(r"★|GOLDEN TOPIC", re.I)
PAGE_RE = re.compile(r"^Page\s+\d+$", re.I)


@dataclass
class Topic:
    id: str
    title: str
    english: str
    urdu_narration: str
    golden: bool
    source_page: int


def is_arabic_text(text: str) -> bool:
    if not text.strip():
        return False
    ar = len(ARABIC_RE.findall(text))
    return ar >= max(2, len(text.strip()) // 3)


def spans_from_page(page: pymupdf.Page) -> list[dict]:
    spans: list[dict] = []
    data = page.get_text("dict")
    for block in data.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            for sp in line.get("spans", []):
                text = (sp.get("text") or "").strip()
                if not text:
                    continue
                bbox = sp.get("bbox") or (0, 0, 0, 0)
                spans.append(
                    {
                        "text": text,
                        "x0": bbox[0],
                        "y0": bbox[1],
                        "x1": bbox[2],
                        "y1": bbox[3],
                        "arabic": is_arabic_text(text),
                    }
                )
    return spans


def group_line_spans(spans: list[dict], y_tol: float = 4.0) -> list[list[dict]]:
    if not spans:
        return []
    sorted_spans = sorted(spans, key=lambda s: (s["y0"], s["x0"]))
    groups: list[list[dict]] = []
    current: list[dict] = []
    current_y = None
    for sp in sorted_spans:
        y = sp["y0"]
        if current_y is None or abs(y - current_y) <= y_tol:
            current.append(sp)
            current_y = y if current_y is None else (current_y + y) / 2
        else:
            groups.append(current)
            current = [sp]
            current_y = y
    if current:
        groups.append(current)
    return groups


def line_from_group(group: list[dict], arabic: bool, split_x: float) -> str:
    if arabic:
        parts = [g for g in group if g["arabic"] and g["x0"] >= split_x - 40]
    else:
        parts = [g for g in group if (not g["arabic"]) or g["x0"] < split_x - 40]
    if not parts:
        return ""
    if arabic:
        parts.sort(key=lambda s: (-s["x0"], s["y0"]))
        raw = "".join(p["text"] for p in parts)
        raw = re.sub(r"\s+", " ", raw).strip()
        # PDF stores Urdu glyphs in visual order; reverse grapheme clusters approximately.
        return raw[::-1].strip()
    parts.sort(key=lambda s: (s["y0"], s["x0"]))
    raw = " ".join(p["text"] for p in parts)
    return re.sub(r"\s+", " ", raw).strip()


def english_lines_from_page(page: pymupdf.Page) -> list[str]:
    lines: list[str] = []
    for line in (page.get_text() or "").split("\n"):
        line = line.strip()
        if not line or PAGE_RE.match(line) or line.startswith("--"):
            continue
        cleaned = ARABIC_RE.sub("", line)
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        if len(cleaned) > 2 and LATIN_RE.search(cleaned):
            lines.append(cleaned)
    return lines


def urdu_lines_from_page(page: pymupdf.Page) -> list[str]:
    spans = spans_from_page(page)
    split_x = page.rect.width * 0.40
    ur_lines: list[str] = []
    for group in group_line_spans(spans):
        ur = line_from_group(group, arabic=True, split_x=split_x)
        if ur and len(ur) > 5:
            ur_lines.append(ur)
    return ur_lines


def page_lines(page: pymupdf.Page) -> tuple[list[str], list[str]]:
    return english_lines_from_page(page), urdu_lines_from_page(page)


def slugify(text: str) -> str:
    base = re.sub(r"[^a-zA-Z0-9]+", "_", text.lower()).strip("_")
    return base[:60] or "topic"


def clean_english(text: str) -> str:
    skip_fragments = {
        "Advantage",
        "English Detail",
        "Urdu Translation ()",
        "Feature",
        "Nature",
        "Reliability",
    }
    lines: list[str] = []
    for line in text.split("\n"):
        line = re.sub(r"\s+", " ", line).strip()
        if not line:
            continue
        if line in skip_fragments:
            continue
        if re.fullmatch(r"[\(\)\*:★]+", line):
            continue
        if line.startswith(":)") or line.endswith(":)Discrete(") or line.endswith(":)Continuous("):
            continue
        if len(line) < 4 and not TOPIC_RE.match(line):
            continue
        lines.append(line)
    return "\n".join(lines)


def translate_to_urdu(english: str) -> str:
    english = clean_english(english)
    if not english:
        return ""
    paragraphs = [p.strip() for p in english.split("\n") if p.strip()]
    translated_paragraphs: list[str] = []
    for paragraph in paragraphs:
        paragraph = re.sub(r"\s+", " ", paragraph).strip()
        if not paragraph:
            continue
        sentences = re.split(r"(?<=[.!?])\s+", paragraph)
        chunks: list[str] = []
        current = ""
        for sentence in sentences:
            if not sentence:
                continue
            if len(current) + len(sentence) + 1 <= 380:
                current = f"{current} {sentence}".strip()
            else:
                if current:
                    chunks.append(current)
                current = sentence
        if current:
            chunks.append(current)

        translated: list[str] = []
        for chunk in chunks:
            try:
                translated.append(argostranslate.translate.translate(chunk, "en", "ur"))
            except Exception:
                translated.append(chunk)
        if translated:
            translated_paragraphs.append(" ".join(t for t in translated if t.strip()))
    return "\n".join(translated_paragraphs)


def merge_topics(topics: list[Topic]) -> list[Topic]:
    merged: list[Topic] = []
    for topic in topics:
        if merged and not TOPIC_RE.match(topic.title) and len(topic.english) < 120:
            prev = merged[-1]
            prev.english = f"{prev.english}\n{topic.english}".strip()
            if topic.urdu_narration:
                prev.urdu_narration = f"{prev.urdu_narration}\n{topic.urdu_narration}".strip()
            prev.golden = prev.golden or topic.golden
            continue
        merged.append(topic)
    return merged


def extract_pdf(pdf_path: Path, book_id: str) -> list[Topic]:
    doc = pymupdf.open(pdf_path)
    topics: list[Topic] = []
    current: Topic | None = None
    topic_index = 0

    for page_num in range(len(doc)):
        page = doc[page_num]
        en_lines, ur_lines = page_lines(page)
        if not en_lines and not ur_lines:
            continue

        full_en = "\n".join(en_lines)
        full_ur = "\n".join(ur_lines)
        golden = bool(GOLDEN_RE.search(full_en))

        started_new = False
        for line in en_lines:
            m = TOPIC_RE.match(line.strip())
            if m and len(m.group(2)) > 3:
                if current:
                    topics.append(current)
                topic_index += 1
                section = m.group(1).replace(" ", "")
                title = f"{m.group(1)} {m.group(2).strip()}"
                tid = f"{book_id}_{section.replace('.', '_')}_{topic_index}"
                current = Topic(
                    id=tid,
                    title=title,
                    english="",
                    urdu_narration="",
                    golden=golden,
                    source_page=page_num + 1,
                )
                started_new = True
                break

        if current is None:
            topic_index += 1
            current = Topic(
                id=f"{book_id}_intro_{topic_index}",
                title=en_lines[0][:120],
                english="",
                urdu_narration="",
                golden=golden,
                source_page=page_num + 1,
            )

        if not started_new or len(en_lines) > 1:
            body_en = "\n".join(en_lines[1:] if started_new else en_lines)
            body_en = clean_english(body_en)
            if body_en.strip():
                current.english = f"{current.english}\n{body_en}".strip() if current.english else body_en.strip()
        if full_ur.strip():
            current.urdu_narration = (
                f"{current.urdu_narration}\n{full_ur}".strip()
                if current.urdu_narration
                else full_ur.strip()
            )
        current.golden = current.golden or golden

    if current:
        topics.append(current)

    merged = merge_topics(topics)
    for topic in merged:
        topic.urdu_narration = translate_to_urdu(topic.english)
    return merged


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    uploads = Path("/home/ubuntu/.cursor/projects/workspace/uploads")
    sources = {
        "cs_xi": uploads / "XI-compressed_6ca2.pdf",
        "cs_xii": uploads / "XII-compressed_57fb.pdf",
    }
    out_dir = root / "app" / "src" / "main" / "assets" / "cs_teacher"
    out_dir.mkdir(parents=True, exist_ok=True)

    catalog: dict = {"books": []}
    for book_id, pdf_path in sources.items():
        if not pdf_path.exists():
            print(f"Missing PDF: {pdf_path}", file=sys.stderr)
            return 1
        topics = extract_pdf(pdf_path, book_id)
        book_file = out_dir / f"{book_id}.json"
        payload = {
            "id": book_id,
            "title": "Computer Science XI" if book_id == "cs_xi" else "Computer Science XII",
            "subtitle": "Bilingual Teacher's Edition — Sindh Curriculum",
            "topicCount": len(topics),
            "topics": [asdict(t) for t in topics],
        }
        book_file.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        catalog["books"].append(
            {
                "id": book_id,
                "title": payload["title"],
                "asset": f"cs_teacher/{book_id}.json",
                "topicCount": len(topics),
            }
        )
        print(f"Wrote {book_file} ({len(topics)} topics)")

    (out_dir / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
