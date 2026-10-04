#!/usr/bin/env python3
"""One-time PDF → chapters_raw.json extract (requires pymupdf)."""
from __future__ import annotations

import json
import re
from pathlib import Path

import pymupdf

PDF = Path(__file__).resolve().parents[2] / "uploads" / "XII-compressed_1e38.pdf"
if not PDF.exists():
    PDF = Path("/home/ubuntu/.cursor/projects/workspace/uploads/XII-compressed_1e38.pdf")

OUT = Path(__file__).resolve().parents[1] / "data" / "chapters_raw.json"
chapter_starts = [1, 22, 48, 76, 103, 124, 148]
section_pat = re.compile(r"\n(?=(?:\d+\.)+\d*\s+[A-Z\u0600-\u06FF])")


def clean(t: str) -> str:
    t = re.sub(r"Page \d+\s*", "", t)
    t = re.sub(r"-- \d+ of \d+ --", "", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def main() -> None:
    doc = pymupdf.open(PDF)
    chapters = []
    for idx in range(len(chapter_starts) - 1):
        start, end = chapter_starts[idx], chapter_starts[idx + 1]
        text = "\n".join(doc[p].get_text() for p in range(start - 1, end - 1))
        text = clean(text)
        parts = section_pat.split(text)
        sections = []
        for part in parts:
            part = part.strip()
            if len(part) < 80:
                continue
            sections.append(
                {
                    "heading": part.split("\n", 1)[0][:120],
                    "golden": "★" in part[:200] or "GOLDEN" in part[:200],
                    "length": len(part),
                    "body": part[:8000],
                }
            )
        chapters.append(
            {
                "id": idx + 1,
                "title": text.split("\n")[2] if text else f"Chapter {idx+1}",
                "sections": sections,
            }
        )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(chapters, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote", OUT)


if __name__ == "__main__":
    main()
