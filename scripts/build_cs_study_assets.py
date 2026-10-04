#!/usr/bin/env python3
"""Build CS Lecture-Notes Study Guide assets from teacher PDFs."""

from __future__ import annotations

import json
import re
import shutil
import sys
import time
from pathlib import Path

from pypdf import PdfReader

try:
    import pymupdf as fitz
except ImportError:
    fitz = None  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
UPLOADS = Path("/home/ubuntu/.cursor/projects/workspace/uploads")
ASSETS = ROOT / "app/src/main/assets/lecture_notes"
DRAWABLE = ROOT / "app/src/main/res/drawable-nodpi"

MAX_EN_TTS_CHARS = 120_000
TRANSLATE_CHUNK = 3500
TRANSLATE_SLEEP_SEC = 0.15

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
        "grade_label": "گیارہویں",
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
        "grade_label": "بارہویں",
    },
}

ARABIC_RE = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]+")


def clean_page_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    text = re.sub(r"Page \d+$", "", text).strip()
    text = re.sub(r"-- \d+ of \d+ --", "", text).strip()
    return text


def clean_english_for_tts(text: str) -> str:
    """Legacy helper; prefer [english_embed_tts] for bundled embed narration."""
    return english_embed_tts(text)


def english_embed_tts(raw: str) -> str:
    """Full-page English embed text from PDF extract (no line filtering, no truncation)."""
    text = clean_page_text(raw)
    text = ARABIC_RE.sub(" ", text)
    return re.sub(r"\s+", " ", text).strip()


def split_bilingual_lines(raw: str) -> tuple[str, str]:
    en_parts: list[str] = []
    ur_parts: list[str] = []
    for line in (raw or "").splitlines():
        line = line.strip()
        if not line or re.match(r"^Page \d+$", line) or "--" in line and " of " in line:
            continue
        arabic = len(ARABIC_RE.findall(line))
        latin = len(re.findall(r"[A-Za-z]", line))
        if arabic > latin and arabic >= 4:
            ur_parts.append(ARABIC_RE.sub(" ", line))
        elif latin >= 3:
            en_parts.append(line)
    en_raw = " ".join(en_parts)
    ur_raw = re.sub(r"\s+", " ", " ".join(ur_parts)).strip()
    return en_raw, ur_raw


_argos_en_ur = None


def get_argos_en_ur():
    global _argos_en_ur
    if _argos_en_ur is None:
        import argostranslate.translate

        installed = argostranslate.translate.get_installed_languages()
        from_lang = next((lang for lang in installed if lang.code == "en"), None)
        to_lang = next((lang for lang in installed if lang.code == "ur"), None)
        if not from_lang or not to_lang:
            raise SystemExit("Argos en→ur package not installed")
        _argos_en_ur = from_lang.get_translation(to_lang)
    return _argos_en_ur


def is_valid_ur_tts(ur: str, en: str) -> bool:
    ur = (ur or "").strip()
    en = (en or "").strip()
    if not ur or not en or ur == en:
        return False
    min_len = min(80, max(40, int(len(en) * 0.25)))
    if len(ur) < min_len:
        return False
    arabic = sum(len(m) for m in ARABIC_RE.findall(ur))
    if arabic < 24:
        return False
    return True


def translate_en_to_ur(text: str) -> str:
    text = text.strip()
    if not text:
        return ""
    translation = get_argos_en_ur()
    chunks: list[str] = []
    remaining = text
    while remaining:
        piece = remaining[:TRANSLATE_CHUNK]
        if len(remaining) > TRANSLATE_CHUNK:
            split = piece.rfind(". ")
            if split > TRANSLATE_CHUNK // 2:
                piece = remaining[: split + 1]
        try:
            translated = translation.translate(piece).strip()
        except Exception as exc:
            print(f"  argos translate warning: {exc}", file=sys.stderr)
            return ""
        if not translated:
            return ""
        chunks.append(translated)
        remaining = remaining[len(piece) :].strip()
        if remaining:
            time.sleep(TRANSLATE_SLEEP_SEC)
    return " ".join(chunks).strip()


def extract_page_raw(pdf_path: Path, page_number: int) -> str:
    if fitz is not None:
        doc = fitz.open(str(pdf_path))
        try:
            return doc[page_number - 1].get_text("text") or ""
        finally:
            doc.close()
    reader = PdfReader(str(pdf_path))
    return reader.pages[page_number - 1].extract_text() or ""


def is_chapter_divider(en_tts: str) -> bool:
    return bool(re.search(r"CHAPTER\s+\d+:", en_tts, re.I)) and len(en_tts) < 280


def synthetic_chapter_ur(class_key: str, en_tts: str) -> str:
    match = re.search(r"CHAPTER\s+(\d+):", en_tts, re.I)
    chapter_num = int(match.group(1)) if match else 1
    spec = CHAPTER_SPECS[class_key]
    title_ur = spec["titles_ur"][chapter_num - 1]
    grade = spec["grade_label"]
    return (
        f"کمپیوٹر سائنس جماعت {grade}، باب {chapter_num}: {title_ur}. "
        "یہ دو لسانی ٹیچر ایڈیشن کے اعلیٰ پیداوار لیکچر نوٹس اور امتحانی گولڈن ٹاپکس ہیں، "
        "جو نئے سندھ نصاب دو ہزار چھ بیس کے مطابق تیار کیے گئے ہیں۔"
    )


def enrich_page_tts(page: dict, translate: bool, class_key: str | None = None) -> dict:
    raw = page.get("_raw", "") or ""
    if not raw and page.get("en_tts"):
        raw = page["en_tts"]
    en_tts = english_embed_tts(raw)
    _, ur_pdf = split_bilingual_lines(raw)
    ur_tts = (page.get("ur_tts") or "").strip()
    if class_key and is_chapter_divider(en_tts):
        ur_tts = synthetic_chapter_ur(class_key, en_tts)
    elif translate and en_tts and not is_valid_ur_tts(ur_tts, en_tts):
        for attempt in range(3):
            candidate = translate_en_to_ur(en_tts)
            if is_valid_ur_tts(candidate, en_tts):
                ur_tts = candidate
                break
            if attempt < 2:
                time.sleep(0.75 * (attempt + 1))
    elif not ur_tts:
        ur_tts = ur_pdf if is_valid_ur_tts(ur_pdf, en_tts) else ""
    ur_display = ur_tts if ur_tts else ur_pdf
    return {
        "page": page["page"],
        "en": en_tts,
        "ur": ur_display,
        "en_tts": en_tts,
        "ur_tts": ur_tts,
    }


def embed_index_up_to_date(cached: dict | None, raw: str, translate: bool) -> bool:
    if not cached or not cached.get("en_tts"):
        return False
    new_en = english_embed_tts(raw)
    if cached.get("en_tts", "").strip() != new_en:
        return False
    if not translate:
        return True
    return is_valid_ur_tts(cached.get("ur_tts", ""), new_en)


def load_existing_index(path: Path) -> dict[int, dict]:
    if not path.exists():
        return {}
    try:
        rows = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return {int(row["page"]): row for row in rows}


def build_page_index(
    pdf_path: Path,
    translate: bool,
    existing: dict[int, dict],
    index_path: Path | None = None,
    checkpoint: bool = False,
    class_key: str | None = None,
    force_reextract: bool = False,
) -> list[dict]:
    reader = PdfReader(str(pdf_path))
    total = len(reader.pages)
    pages: list[dict | None] = [None] * total

    for page_num, row in existing.items():
        if 1 <= page_num <= total:
            pages[page_num - 1] = row

    for i in range(1, total + 1):
        raw = extract_page_raw(pdf_path, i)
        cached = pages[i - 1]
        if not force_reextract and embed_index_up_to_date(cached, raw, translate):
            continue

        row = enrich_page_tts(
            {
                "page": i,
                "_raw": raw,
                "ur_tts": (cached or {}).get("ur_tts", ""),
            },
            translate=translate,
            class_key=class_key,
        )
        pages[i - 1] = row

        if checkpoint and index_path is not None and (i % 5 == 0 or i == total):
            snapshot = [p for p in pages if p is not None]
            if len(snapshot) == total:
                index_path.write_text(json.dumps(snapshot, ensure_ascii=False, indent=0), encoding="utf-8")
        if i % 10 == 0 or i == total:
            print(f"  page {i}/{total}", flush=True)

    result = [p for p in pages if p is not None]
    if index_path is not None and len(result) == total:
        index_path.write_text(json.dumps(result, ensure_ascii=False, indent=0), encoding="utf-8")
    return result


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


def embed_full_page() -> None:
    translate = True
    only_class = None
    for arg in sys.argv[1:]:
        if arg.startswith("--class="):
            only_class = arg.split("=", 1)[1].strip().lower()
    ASSETS.mkdir(parents=True, exist_ok=True)
    for key, spec in CHAPTER_SPECS.items():
        if only_class and key != only_class:
            continue
        dest_pdf = ASSETS / spec["asset_pdf"]
        if not dest_pdf.exists():
            src = spec["pdf_src"]
            if not src.exists():
                raise SystemExit(f"Missing PDF: {src}")
            shutil.copy2(src, dest_pdf)
        index_path = ASSETS / f"cs_{key}_pages.json"
        existing = load_existing_index(index_path)
        total = len(PdfReader(str(dest_pdf)).pages)
        if len(existing) != total:
            print(
                f"Embed rebuild {key.upper()}: index {len(existing)}/{total} pages — rebuilding all from PDF",
                flush=True,
            )
            existing = {}
        else:
            print(f"Embed rebuild {key.upper()} ({total} pages)", flush=True)
        page_index = build_page_index(
            dest_pdf,
            translate=translate,
            existing=existing,
            index_path=index_path,
            checkpoint=False,
            class_key=key,
            force_reextract=True,
        )
        valid = sum(1 for p in page_index if is_valid_ur_tts(p.get("ur_tts", ""), p.get("en_tts", "")))
        print(
            f"Wrote {index_path} entries {len(page_index)} valid ur_tts {valid}/{len(page_index)}",
            flush=True,
        )


def ur_fill_only() -> None:
    translate = True
    only_class = None
    for arg in sys.argv[1:]:
        if arg.startswith("--class="):
            only_class = arg.split("=", 1)[1].strip().lower()
    ASSETS.mkdir(parents=True, exist_ok=True)
    for key, spec in CHAPTER_SPECS.items():
        if only_class and key != only_class:
            continue
        dest_pdf = ASSETS / spec["asset_pdf"]
        if not dest_pdf.exists():
            src = spec["pdf_src"]
            if not src.exists():
                raise SystemExit(f"Missing PDF: {src}")
            shutil.copy2(src, dest_pdf)
        index_path = ASSETS / f"cs_{key}_pages.json"
        existing = load_existing_index(index_path)
        total = len(PdfReader(str(dest_pdf)).pages)
        if len(existing) != total:
            print(
                f"Urdu TTS fill {key.upper()}: index {len(existing)}/{total} pages — rebuilding embed from PDF",
                flush=True,
            )
            existing = {}
        else:
            print(f"Urdu TTS fill: {key.upper()} ({len(existing)} cached pages)", flush=True)
        page_index = build_page_index(
            dest_pdf,
            translate=translate,
            existing=existing,
            index_path=index_path,
            checkpoint=False,
            class_key=key,
            force_reextract=True,
        )
        valid = sum(1 for p in page_index if is_valid_ur_tts(p.get("ur_tts", ""), p.get("en_tts", "")))
        print(f"Wrote {index_path} entries {len(page_index)} valid ur_tts {valid}/{len(page_index)}", flush=True)


def main() -> None:
    if "--embed-full-page" in sys.argv:
        embed_full_page()
        return
    if "--ur-fill-only" in sys.argv:
        ur_fill_only()
        return

    translate = "--no-translate" not in sys.argv
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

        index_path = ASSETS / f"cs_{key}_pages.json"
        existing = load_existing_index(index_path)

        page_index = build_page_index(
            dest_pdf,
            translate=translate,
            existing=existing,
            index_path=index_path,
            checkpoint=False,
            class_key=key,
            force_reextract=True,
        )
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
                "ttsIndexAsset": f"lecture_notes/cs_{key}_pages.json",
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
