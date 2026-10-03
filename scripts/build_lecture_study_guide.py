#!/usr/bin/env python3
"""Build lecture-wise study guide structure for Teacher's Edition JSON assets."""

from __future__ import annotations

import json
import re
from pathlib import Path

LECTURE_TITLES = {
    "cs_xi": {
        1: "Computer Systems",
        2: "Computational Thinking & Problem Solving",
        3: "Programming Fundamentals",
        4: "Data & Database Concepts",
        5: "Computer Networks & Internet",
        6: "Digital Literacy & Citizenship",
    },
    "cs_xii": {
        1: "Computer Systems (HCI)",
        2: "Algorithms & Problem Solving",
        3: "Programming & Software Development",
        4: "Data Analysis & Visualization",
        5: "Digital Collaboration & Equity",
        6: "Digital Entrepreneurship",
    },
}

CHAPTER_RE = re.compile(r"^(\d+)\.\d+")
BOILER_LINE = re.compile(
    r"(BILINGUAL TEACHER'S EDITION|High-Yielding Lecture Notes|TABLE OF CONTENTS|Based on New Sindh)",
    re.I,
)


def chapter_number(title: str) -> int | None:
    m = CHAPTER_RE.match(title.strip())
    return int(m.group(1)) if m else None


def section_sort_key(title: str) -> tuple:
    nums = [int(x) for x in re.findall(r"\d+", title.split()[0] if title else "")]
    return tuple(nums) if nums else (999,)


def clean_descriptive_english(text: str) -> str:
    lines: list[str] = []
    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped:
            if lines and lines[-1] != "":
                lines.append("")
            continue
        if BOILER_LINE.search(stripped):
            continue
        if stripped.startswith("COMPUTER SCIENCE") and "CHAPTER" in stripped:
            continue
        lines.append(stripped)
    cleaned = "\n".join(lines).strip()
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned


def lecture_urdu_overview(topics: list[dict]) -> str:
    parts: list[str] = []
    for topic in topics[:4]:
        ur = (topic.get("urdu_narration") or "").strip()
        if ur:
            parts.append(ur.split("۔")[0] + "۔")
    if not parts and topics:
        parts.append(topics[0].get("title", ""))
    return " ".join(parts)[:900]


def build_lectures(book_id: str, topics: list[dict]) -> list[dict]:
    titles = LECTURE_TITLES[book_id]
    grouped: dict[int, list[dict]] = {}
    for topic in topics:
        ch = chapter_number(topic.get("title", ""))
        if ch is None:
            continue
        grouped.setdefault(ch, []).append(topic)

    lectures: list[dict] = []
    for ch in sorted(grouped.keys()):
        lecture_topics = sorted(grouped[ch], key=lambda t: section_sort_key(t.get("title", "")))
        title = titles.get(ch, f"Chapter {ch}")
        lectures.append(
            {
                "id": f"{book_id}_lecture_{ch}",
                "chapter": ch,
                "title": f"Lecture {ch}: {title}",
                "english_summary": (
                    f"Teacher's Edition study guide — {title}. "
                    f"{len(lecture_topics)} bilingual lecture units (English notes, Urdu class narration)."
                ),
                "urdu_narration": lecture_urdu_overview(lecture_topics),
                "topic_ids": [t["id"] for t in lecture_topics],
                "topic_count": len(lecture_topics),
                "golden_count": sum(1 for t in lecture_topics if t.get("golden")),
            }
        )
    return lectures


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    asset_dir = root / "app" / "src" / "main" / "assets" / "cs_teacher"
    for book_id in LECTURE_TITLES:
        path = asset_dir / f"{book_id}.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        for topic in payload["topics"]:
            topic["english"] = clean_descriptive_english(topic.get("english", ""))
        payload["lectures"] = build_lectures(book_id, payload["topics"])
        payload["study_guide_label"] = "Lecture-wise Bilingual Teacher's Edition Study Guide"
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"{book_id}: {len(payload['lectures'])} lectures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
