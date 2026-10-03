#!/usr/bin/env python3
"""Apply official Teacher's Edition metadata and lecture-only topic lists."""

from __future__ import annotations

import json
import re
from pathlib import Path

LECTURE_TITLE = re.compile(r"^\d+\.\d+")

BOOK_META = {
    "cs_xi": {
        "display_title": "Computer Science XI — Chapter 1: Computer Systems",
        "edition_title": "Bilingual Teacher's Edition",
        "tagline": "High-Yielding Lecture Notes & Golden Topics",
        "curriculum": "New Sindh Curriculum 2026",
        "textbook_reference": "CS XI (1 & 2).pdf",
        "teacher_guidelines_english": (
            "These notes are prepared specifically for teachers. For reference, please "
            "consult the textbook PDF file named exactly \"CS XI (1 & 2).pdf\", which has "
            "been followed verbatim. Topics marked with a ★ are highly critical for examinations."
        ),
        "teacher_guidelines_urdu": (
            "یہ نوٹس خاص طور پر اساتذہ کے لیے تیار کیے گئے ہیں۔ حوالہ کے لیے براہِ کرم "
            "\"CS XI (1 & 2).pdf\" نامی درسی کتاب کی PDF فائل دیکھیں؛ اسی پر مکمل عمل کیا گیا ہے۔ "
            "★ نشان والے موضوعات امتحانات کے لیے انتہائی اہم ہیں۔"
        ),
    },
    "cs_xii": {
        "display_title": "Computer Science XII — Chapter 1: Computer Systems (HCI)",
        "edition_title": "Bilingual Teacher's Edition",
        "tagline": "High-Yielding Lecture Notes & Golden Topics",
        "curriculum": "New Sindh Curriculum 2024 / 2025–27",
        "textbook_reference": "CS XII (1 & 2).pdf",
        "teacher_guidelines_english": (
            "These notes are prepared specifically for teachers. For reference, please "
            "consult the textbook PDF file named exactly \"CS XII (1 & 2).pdf\", which has "
            "been followed verbatim. Topics marked with a ★ are highly critical for examinations."
        ),
        "teacher_guidelines_urdu": (
            "یہ نوٹس خاص طور پر اساتذہ کے لیے تیار کیے گئے ہیں۔ حوالہ کے لیے براہِ کرم "
            "\"CS XII (1 & 2).pdf\" نامی درسی کتاب کی PDF فائل دیکھیں؛ اسی پر مکمل عمل کیا گیا ہے۔ "
            "★ نشان والے موضوعات امتحانات کے لیے انتہائی اہم ہیں۔"
        ),
    },
}


def is_lecture_topic(title: str) -> bool:
    return bool(LECTURE_TITLE.match(title.strip()))


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    asset_dir = root / "app" / "src" / "main" / "assets" / "cs_teacher"
    catalog_updates: dict[str, int] = {}
    for book_id, meta in BOOK_META.items():
        path = asset_dir / f"{book_id}.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        guidelines = {
            "edition_title": meta["edition_title"],
            "tagline": meta["tagline"],
            "curriculum": meta["curriculum"],
            "textbook_reference": meta["textbook_reference"],
            "english": meta["teacher_guidelines_english"],
            "urdu_narration": meta["teacher_guidelines_urdu"],
            "golden_topic_note": "Topics marked with ★ are highly critical for examinations.",
        }
        payload["title"] = meta["display_title"]
        payload["subtitle"] = f"{meta['edition_title']} · {meta['tagline']}"
        payload["teacher_guidelines"] = guidelines
        lectures = [t for t in payload["topics"] if is_lecture_topic(t.get("title", ""))]
        payload["topics"] = lectures
        payload["topicCount"] = len(lectures)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        catalog_updates[book_id] = len(lectures)
        print(f"{book_id}: {len(lectures)} lecture guidelines (official teacher topics)")
    catalog_path = asset_dir / "catalog.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    for entry in catalog.get("books", []):
        bid = entry.get("id")
        if bid in catalog_updates:
            entry["topicCount"] = catalog_updates[bid]
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
