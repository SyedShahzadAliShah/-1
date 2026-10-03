#!/usr/bin/env python3
"""Extract English display text and Urdu narration from the CS XI Teacher's Edition PDF."""

from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PDF = Path("/home/ubuntu/.cursor/projects/workspace/uploads/XI_c966.pdf")
ASSET_DIR = ROOT / "app/src/main/assets/cs_xi_teacher"
OUT_JSON = ASSET_DIR / "guide.json"
OUT_PDF = ASSET_DIR / "XI_c966.pdf"

CHAPTER_BLOCKS = [
    ("ch1", "Chapter 1: Computer Systems", 2, 3, 27),
    ("ch2", "Chapter 2: Computational Thinking & Algorithms", 28, 29, 44),
    ("ch3", "Chapter 3: Python Programming", 45, 46, 70),
    ("ch4", "Chapter 4: Database Systems", 71, 72, 96),
    ("ch5", "Chapter 5: Impacts of Computing", 97, 98, 111),
    ("ch6", "Chapter 6: Digital Literacy & Research", 112, 113, 127),
]

ARABIC_RE = re.compile(r"[\u0600-\u06FF\u0750-\u077F]")


def is_urdu_line(line: str) -> bool:
    ar = len(ARABIC_RE.findall(line))
    lat = sum(1 for c in line if c.isascii() and c.isalpha())
    return ar > lat and ar >= 3


def is_english_line(line: str) -> bool:
    line = line.strip()
    if not line or line.startswith("Page "):
        return False
    if line in {"★ GOLDEN TOPIC", "TABLE OF CONTENTS"}:
        return False
    if re.match(r"^[\d\.\s&★👨‍🏫💡]+$", line):
        return False
    if len(ARABIC_RE.findall(line)) > 5:
        return False
    lat = sum(1 for c in line if c.isascii() and (c.isalpha() or c in ".,:;()-+/='\""))
    return lat >= 8


def parse_toc(doc: pymupdf.Document, toc_page_index: int) -> list[tuple[str, bool]]:
    text = doc[toc_page_index].get_text()
    topics: list[tuple[str, bool]] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line == "TABLE OF CONTENTS":
            continue
        m = re.match(r"^\d+\.\s+(.+)$", line)
        if not m:
            continue
        title = m.group(1).strip()
        critical = "★" in title
        title = title.replace("★", "").strip()
        topics.append((title, critical))
    return topics


def extract_page_text(doc: pymupdf.Document, page_index: int) -> tuple[list[str], list[str]]:
    english: list[str] = []
    urdu: list[str] = []
    for line in doc[page_index].get_text().splitlines():
        line = line.strip()
        if not line:
            continue
        if is_english_line(line):
            english.append(line)
        elif is_urdu_line(line):
            urdu.append(line)
    return english, urdu


def split_topic_pages(total_pages: int, topic_count: int) -> list[tuple[int, int]]:
    if topic_count <= 0:
        return []
    base = total_pages // topic_count
    remainder = total_pages % topic_count
    ranges: list[tuple[int, int]] = []
    cursor = 0
    for i in range(topic_count):
        span = base + (1 if i < remainder else 0)
        start = cursor
        end = cursor + span - 1
        ranges.append((start, end))
        cursor = end + 1
    return ranges


def build_guide(pdf_path: Path) -> dict:
    doc = pymupdf.open(pdf_path)
    chapters_out = []

    for ch_id, ch_title, toc_page, content_start, content_end in CHAPTER_BLOCKS:
        topics_meta = parse_toc(doc, toc_page - 1)
        page_count = content_end - content_start + 1
        spans = split_topic_pages(page_count, len(topics_meta))

        topics_out = []
        for idx, ((title, critical), (rel_start, rel_end)) in enumerate(zip(topics_meta, spans)):
            abs_start = content_start + rel_start
            abs_end = content_start + rel_end
            en_lines: list[str] = []
            ur_lines: list[str] = []
            for page in range(abs_start - 1, abs_end):
                if page < 0 or page >= doc.page_count:
                    continue
                en, ur = extract_page_text(doc, page)
                en_lines.extend(en)
                ur_lines.extend(ur)

            topics_out.append(
                {
                    "id": f"{ch_id}_t{idx + 1:02d}",
                    "title": title,
                    "critical": critical,
                    "englishText": "\n\n".join(en_lines),
                    "urduNarration": " ".join(ur_lines),
                    "startPage": abs_start,
                    "endPage": abs_end,
                }
            )

        chapters_out.append(
            {
                "id": ch_id,
                "title": ch_title,
                "topics": topics_out,
            }
        )

    return {
        "title": "Computer Science XI — Bilingual Teacher's Edition",
        "subtitle": "High-Yielding Lecture Notes & Golden Topics",
        "curriculum": "New Sindh Curriculum 2026",
        "displayLanguage": "en",
        "narrationLanguage": "ur",
        "referenceNote": (
            "These notes are prepared specifically for teachers. For reference, consult the "
            "textbook PDF file named exactly \"CS XI (1 & 2).pdf\". Topics marked with ★ are "
            "highly critical for examinations."
        ),
        "chapters": chapters_out,
    }


def main() -> int:
    pdf_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PDF
    if not pdf_path.is_file():
        print(f"PDF not found: {pdf_path}", file=sys.stderr)
        return 1

    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    guide = build_guide(pdf_path)
    OUT_JSON.write_text(json.dumps(guide, ensure_ascii=False, indent=2), encoding="utf-8")
    shutil.copy2(pdf_path, OUT_PDF)

    topic_count = sum(len(ch["topics"]) for ch in guide["chapters"])
    print(f"Wrote {OUT_JSON} ({topic_count} topics across {len(guide['chapters'])} chapters)")
    print(f"Copied PDF to {OUT_PDF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
