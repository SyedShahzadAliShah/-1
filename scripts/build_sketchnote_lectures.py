#!/usr/bin/env python3
"""Add sketchnote lecture frames + PDF page art to existing CS teacher JSON assets."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pymupdf

VISUALS = ("concept", "flow", "compare", "logic", "network", "wave", "idea")
KEYWORD_VISUAL = {
    "gate": "logic",
    "boolean": "logic",
    "k-map": "logic",
    "karnaugh": "logic",
    "sort": "flow",
    "algorithm": "flow",
    "loop": "flow",
    "network": "network",
    "osi": "network",
    "tcp": "network",
    "signal": "wave",
    "analog": "wave",
    "digital": "wave",
    "hci": "concept",
    "interface": "concept",
    "compare": "compare",
    "vs": "compare",
    "difference": "compare",
}


def pick_visual(line: str, index: int) -> str:
    lower = line.lower()
    for key, visual in KEYWORD_VISUAL.items():
        if key in lower:
            return visual
    return VISUALS[index % len(VISUALS)]


def split_english_lines(english: str, max_frames: int = 7) -> list[str]:
    lines: list[str] = []
    for raw in english.split("\n"):
        line = re.sub(r"\s+", " ", raw).strip()
        if len(line) < 12:
            continue
        if re.fullmatch(r"[\(\)\*:★]+", line):
            continue
        lines.append(line[:240])
    if not lines:
        compact = re.sub(r"\s+", " ", english).strip()
        if compact:
            lines = [compact[:240]]
    if len(lines) > max_frames:
        chunk = max(1, len(lines) // max_frames)
        merged = []
        for i in range(0, len(lines), chunk):
            merged.append(" ".join(lines[i : i + chunk])[:240])
        lines = merged[:max_frames]
    return lines[:max_frames]


def split_urdu_segments(urdu: str, count: int) -> list[str]:
    parts = [p.strip() for p in re.split(r"(?<=[۔!\?])\s+", urdu) if p.strip()]
    if not parts:
        parts = [p.strip() for p in urdu.split("\n") if p.strip()]
    if not parts:
        return [""] * count
    if len(parts) >= count:
        return parts[:count]
    while len(parts) < count:
        parts.append(parts[-1])
    return parts


def build_frames(topic: dict) -> list[dict]:
    en_lines = split_english_lines(topic.get("english", ""))
    ur_parts = split_urdu_segments(topic.get("urdu_narration", ""), len(en_lines))
    frames = []
    for i, en in enumerate(en_lines):
        ur = ur_parts[i][:600] if i < len(ur_parts) else ""
        if not ur.strip():
            ur = ur_parts[-1][:600] if ur_parts else ""
        frames.append(
            {
                "index": i,
                "english": en,
                "urdu": ur,
                "visual": pick_visual(en, i),
            }
        )
    return frames


def export_page_images(doc: pymupdf.Document, book_id: str, pages: set[int], out_root: Path) -> None:
    page_dir = out_root / "pages" / book_id
    page_dir.mkdir(parents=True, exist_ok=True)
    matrix = pymupdf.Matrix(1.35, 1.35)
    for page_num in sorted(pages):
        if page_num < 1 or page_num > len(doc):
            continue
        target = page_dir / f"page_{page_num:03d}.jpg"
        if target.exists():
            continue
        pix = doc[page_num - 1].get_pixmap(matrix=matrix, alpha=False)
        pix.save(target)


def page_asset(book_id: str, page_num: int) -> str:
    return f"cs_teacher/pages/{book_id}/page_{page_num:03d}.jpg"


def process_book(book_id: str, pdf_path: Path, json_path: Path, out_root: Path) -> None:
    payload = json.loads(json_path.read_text(encoding="utf-8"))
    doc = pymupdf.open(pdf_path)
    pages: set[int] = set()
    for topic in payload["topics"]:
        page = int(topic.get("source_page", 0))
        if page > 0:
            pages.add(page)
        topic["sketchnote_frames"] = build_frames(topic)
        if page > 0:
            topic["page_image"] = page_asset(book_id, page)
    export_page_images(doc, book_id, pages, out_root)
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Updated {json_path.name}: {len(payload['topics'])} topics, {len(pages)} page images")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    uploads = Path("/home/ubuntu/.cursor/projects/workspace/uploads")
    out_root = root / "app" / "src" / "main" / "assets" / "cs_teacher"
    mapping = {
        "cs_xi": uploads / "XI-compressed_6ca2.pdf",
        "cs_xii": uploads / "XII-compressed_57fb.pdf",
    }
    for book_id, pdf in mapping.items():
        process_book(book_id, pdf, out_root / f"{book_id}.json", out_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
