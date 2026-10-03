#!/usr/bin/env python3
"""Extract English text lines and render Urdu-free page images from the source PDF.

Outputs (relative to teachers-edition/):
  work/extract/pNNN.txt          English lines with layout metadata (input for content authoring)
  work/orig/pNNN.png             Original page render (contains Urdu, used only for authoring)
  app/src/main/assets/pages/pNNN.webp  Page render with Urdu glyphs removed (English only)
"""
import os
import re
import sys

import pymupdf
from PIL import Image

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PDF = os.path.join(ROOT, "source", "XI_8518.pdf")
AR = re.compile("[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]")
LATIN = re.compile("[A-Za-z0-9]")
ENGLISH_FONTS = ("Poppins", "DroidSans")


def is_urdu_font(font):
    return font.startswith(("Type3", "NotoNaskh"))


def pad(rect, m=1.5):
    return pymupdf.Rect(rect.x0 - m, rect.y0 - 0.5, rect.x1 + m, rect.y1 + 0.5)


def classify_lines(page):
    """Yield (line_dict, english_text, urdu_spans)."""
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            spans = line["spans"]
            full = "".join(s["text"] for s in spans)
            has_arabic = bool(AR.search(full))
            eng_parts, urdu_spans = [], []
            for s in spans:
                font = s["font"]
                if has_arabic:
                    if font.startswith(ENGLISH_FONTS):
                        eng_parts.append(s["text"])
                    else:
                        urdu_spans.append(s)
                else:
                    t = s["text"]
                    if is_urdu_font(font) and not t.strip() :
                        urdu_spans.append(s)
                    else:
                        eng_parts.append(t)
            yield line, "".join(eng_parts), urdu_spans


def main():
    doc = pymupdf.open(PDF)
    os.makedirs(os.path.join(ROOT, "work", "extract"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "work", "orig"), exist_ok=True)
    pages_dir = os.path.join(ROOT, "app", "src", "main", "assets", "pages")
    os.makedirs(pages_dir, exist_ok=True)

    for idx, page in enumerate(doc):
        n = idx + 1
        page.get_pixmap(dpi=100).save(os.path.join(ROOT, "work", "orig", f"p{n:03d}.png"))

        out = []
        for line, eng, urdu_spans in classify_lines(page):
            spans = [s for s in line["spans"] if s["font"].startswith(ENGLISH_FONTS) or LATIN.search(s["text"])]
            if not eng.strip():
                continue
            first = spans[0] if spans else line["spans"][0]
            bold = "B" if "Bold" in first["font"] else "R"
            mono = "M" if first["font"].startswith("DroidSansMono") else ""
            out.append(
                f"[y={line['bbox'][1]:.0f} x={line['bbox'][0]:.0f} {bold}{mono}{first['size']:.1f}] {eng.strip()}"
            )
        with open(os.path.join(ROOT, "work", "extract", f"p{n:03d}.txt"), "w") as f:
            f.write(f"PAGE {n}\n" + "\n".join(out) + "\n")

        for attempt, margin in enumerate((1.5, 3.0, 6.0)):
            rects = []
            for block in page.get_text("dict")["blocks"]:
                for line in block.get("lines", []):
                    full = "".join(s["text"] for s in line["spans"])
                    has_arabic = bool(AR.search(full))
                    for s in line["spans"]:
                        if not is_urdu_font(s["font"]):
                            continue
                        t = s["text"]
                        if AR.search(t) or (attempt == 0 and (not t.strip() or has_arabic)):
                            rects.append(pad(pymupdf.Rect(s["bbox"]), margin))
            if not rects:
                break
            for r in rects:
                page.add_redact_annot(r, fill=False)
            page.apply_redactions(
                images=pymupdf.PDF_REDACT_IMAGE_NONE,
                graphics=pymupdf.PDF_REDACT_LINE_ART_NONE,
                text=pymupdf.PDF_REDACT_TEXT_REMOVE,
            )
        stray = [pad(pymupdf.Rect(w[:4]), 1.0) for w in page.get_text("words") if AR.search(w[4])]
        pix = page.get_pixmap(dpi=130)
        png_tmp = os.path.join(ROOT, "work", "tmp_page.png")
        pix.save(png_tmp)
        img = Image.open(png_tmp).convert("RGB")
        scale = 130 / 72.0
        for r in stray:
            box = tuple(int(round(v * scale)) for v in (r.x0, r.y0, r.x1, r.y1))
            sx, sy = max(box[0] - 3, 0), max(box[1] - 3, 0)
            img.paste(img.getpixel((sx, sy)), box)
        img.save(os.path.join(pages_dir, f"p{n:03d}.webp"), "WEBP", quality=70, method=6)
        if stray:
            print(f"page {n}: painted over {len(stray)} stray Urdu glyph(s)")
    print("done", len(doc), "pages")


if __name__ == "__main__":
    sys.exit(main())
