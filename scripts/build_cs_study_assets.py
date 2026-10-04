#!/usr/bin/env python3
"""Build CS Lecture-Notes Study Guide assets from teacher PDFs."""

from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
UPLOADS = Path("/home/ubuntu/.cursor/projects/workspace/uploads")
ASSETS = ROOT / "app/src/main/assets/lecture_notes"
DRAWABLE = ROOT / "app/src/main/res/drawable-nodpi"

CHAPTER_SPECS = {
    "xi": {
        "pdf_src": UPLOADS / "XI-compressed_7487.pdf",
        "asset_pdf": "cs_xi_lecture_notes.pdf",
        "starts": [1, 27, 44, 70, 96, 111],
        "titles_en": [
            "Computer Systems",
            "Computational Thinking & Algorithms",
            "Programming Fundamentals",
            "Data and Analysis",
            "Application and Impacts of Computing",
            "Digital Literacy",
        ],
        "titles_ur": [
            "کمپیوٹر سسٹمز",
            "Computational Thinking اور الگورتھم",
            "پروگرامنگ کی بنیادیں",
            "ڈیٹا اور تجزیہ",
            "Computing کے اطلاقات و اثرات",
            "ڈیجیٹل literacy",
        ],
    },
    "xii": {
        "pdf_src": UPLOADS / "XII-compressed_6812.pdf",
        "asset_pdf": "cs_xii_lecture_notes.pdf",
        "starts": [1, 22, 48, 76, 103, 124],
        "titles_en": [
            "Computer Systems (HCI)",
            "Computational Thinking & Algorithms",
            "Programming Fundamentals",
            "Data and Analysis",
            "Application and Impacts of Computing",
            "Entrepreneurship in the Digital Age",
        ],
        "titles_ur": [
            "کمپیوٹر سسٹمز (HCI)",
            "Computational Thinking اور الگورتھم",
            "Programming کی بنیادیں",
            "ڈیٹا اور تجزیہ",
            "Computing کے اطلاقات و اثرات",
            "ڈیجیٹل دور میں کاروباریت",
        ],
    },
}


def clean_page_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    text = re.sub(r"Page \d+$", "", text).strip()
    text = re.sub(r"-- \d+ of \d+ --", "", text).strip()
    return text


def extract_urdu_fragments(text: str) -> str:
    """Pull Arabic-script runs from noisy PDF extraction."""
    parts = re.findall(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+(?:\s+[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+)*", text or "")
    joined = " ".join(p.strip() for p in parts if len(p.strip()) > 3)
    return re.sub(r"\s+", " ", joined).strip()


def summarize_en(text: str, max_len: int = 900) -> str:
    text = clean_page_text(text)
    if len(text) <= max_len:
        return text
    cut = text[:max_len]
    last = cut.rfind(". ")
    if last > 200:
        return cut[: last + 1]
    return cut + "…"


def build_page_index(reader: PdfReader) -> list[dict]:
    pages = []
    for i, page in enumerate(reader.pages, start=1):
        raw = page.extract_text() or ""
        pages.append(
            {
                "page": i,
                "en": summarize_en(raw),
                "ur": extract_urdu_fragments(raw),
            }
        )
    return pages


def write_chapter_covers(prefix: str, titles_en: list[str]) -> None:
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("Pillow not installed; skipping cover images", file=sys.stderr)
        return

    colors = [
        (25, 55, 109),
        (34, 87, 122),
        (18, 94, 86),
        (92, 58, 122),
        (140, 74, 28),
        (120, 32, 64),
    ]
    DRAWABLE.mkdir(parents=True, exist_ok=True)
    for idx, title in enumerate(titles_en, start=1):
        img = Image.new("RGB", (960, 540), colors[(idx - 1) % len(colors)])
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 42)
            small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
        except OSError:
            font = ImageFont.load_default()
            small = font
        grade = prefix.upper()
        draw.text((48, 48), f"CS {grade} — Chapter {idx}", fill=(255, 255, 255), font=small)
        draw.multiline_text((48, 120), title, fill=(255, 255, 255), font=font, spacing=8)
        draw.text((48, 460), "Lecture Notes ★ Golden Topics", fill=(230, 230, 230), font=small)
        out = DRAWABLE / f"pic_cs_{prefix}_ch{idx}.png"
        img.save(out, optimize=True)
        print("Wrote", out)


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    meta = {"classes": []}

    for key, spec in CHAPTER_SPECS.items():
        src = spec["pdf_src"]
        if not src.exists():
            raise SystemExit(f"Missing PDF: {src}")

        reader = PdfReader(str(src))
        total = len(reader.pages)
        starts = spec["starts"] + [total + 1]

        dest_pdf = ASSETS / spec["asset_pdf"]
        shutil.copy2(src, dest_pdf)
        print("Copied", dest_pdf)

        page_index = build_page_index(reader)
        index_path = ASSETS / f"cs_{key}_pages.json"
        index_path.write_text(json.dumps(page_index, ensure_ascii=False, indent=0), encoding="utf-8")
        print("Wrote", index_path, "entries", len(page_index))

        chapters = []
        for i, title_en in enumerate(spec["titles_en"], start=1):
            start = starts[i - 1]
            end = starts[i] - 1
            chapters.append(
                {
                    "number": i,
                    "titleEn": title_en,
                    "titleUr": spec["titles_ur"][i - 1],
                    "pdfPageStart": start,
                    "pdfPageEnd": end,
                }
            )

        meta["classes"].append(
            {
                "id": key,
                "gradeLabel": key.upper(),
                "pdfAsset": f"lecture_notes/{spec['asset_pdf']}",
                "pageIndexAsset": f"lecture_notes/cs_{key}_pages.json",
                "totalPages": total,
                "chapters": chapters,
            }
        )

        write_chapter_covers(key, spec["titles_en"])

    meta_path = ASSETS / "study_guide_meta.json"
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote", meta_path)


if __name__ == "__main__":
    main()
