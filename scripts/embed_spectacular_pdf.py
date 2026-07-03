#!/usr/bin/env python3
"""Extract move photos from Spectacular Sex Moves PDF and embed in Android drawable-nodpi."""
from __future__ import annotations

import os
import sys

import fitz
import numpy as np
from PIL import Image, ImageDraw

PDF_PATH = os.environ.get(
    "PDF_PATH",
    "/home/ubuntu/.cursor/projects/workspace/uploads/sex__1_-compressed__1__6e7c.pdf",
)
OUT = "/workspace/app/src/main/res/drawable-nodpi"
TARGET_W, TARGET_H = 960, 600
BG = (252, 246, 238)

# (drawable_suffix, pdf_page_1based, crop_top_fraction)
# Intro pages use top photo; instruction pages use full frame.
MOVES = [
    ("move_01", 2, 0.52),
    ("move_02", 3, 0.52),
    ("move_03", 5, 0.52),
    ("move_04", 6, 0.52),
    ("move_05", 9, 0.52),
    ("move_06", 10, 0.52),
    ("move_07", 13, 0.52),
    ("move_08", 15, 0.52),
    ("move_09", 17, 0.55),  # Go Green — sprinkler instruction photo
    ("move_10", 18, 0.52),
    ("move_11", 20, 0.52),
    ("move_12", 21, 0.55),  # Oh My Gondola — seated ball photo
    ("move_13", 22, 0.55),  # Balls Out — ball position photos
    ("move_14", 23, 0.52),
    ("move_15", 24, 0.52),
    ("move_16", 25, 0.52),
    ("move_17", 26, 0.52),
    ("move_18", 28, 0.52),
    ("move_19", 30, 0.52),
    ("move_20", 32, 0.52),
    ("move_21", 34, 0.52),
    ("move_22", 36, 0.52),
    ("move_23", 37, 0.52),
    ("move_24", 39, 0.52),
    ("move_25", 41, 0.52),
    ("move_26", 42, 0.52),
    ("move_27", 43, 0.52),
    ("move_28", 45, 0.52),
    ("move_29", 46, 0.52),
    ("move_30", 47, 0.52),
]
COVER_PAGE = 1
COVER_CROP = 0.52


def render_page_region(doc: fitz.Document, page_num: int, top_fraction: float) -> np.ndarray:
    page = doc[page_num - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    w, h = img.size
    crop_h = int(h * top_fraction)
    cropped = img.crop((0, 0, w, crop_h))
    return np.array(cropped)


def fit_on_canvas(rgb: np.ndarray) -> np.ndarray:
    h, w = rgb.shape[:2]
    scale = min(TARGET_W / w, TARGET_H / h) * 0.92
    new_w, new_h = max(1, int(w * scale)), max(1, int(h * scale))
    pil = Image.fromarray(rgb).resize((new_w, new_h), Image.Resampling.LANCZOS)

    canvas = Image.new("RGB", (TARGET_W, TARGET_H), BG)
    draw = ImageDraw.Draw(canvas)
    for row in range(TARGET_H):
        t = row / TARGET_H
        color = (
            int(BG[0] * (1 - t) + 238 * t),
            int(BG[1] * (1 - t) + 226 * t),
            int(BG[2] * (1 - t) + 212 * t),
        )
        draw.line([(0, row), (TARGET_W, row)], fill=color)

    x_off = (TARGET_W - new_w) // 2
    y_off = (TARGET_H - new_h) // 2
    canvas.paste(pil, (x_off, y_off))
    draw.rounded_rectangle((8, 8, TARGET_W - 8, TARGET_H - 8), radius=12, outline=(138, 100, 80), width=2)
    return np.array(canvas)


def save_canvas(canvas: np.ndarray, name: str) -> None:
    path = os.path.join(OUT, f"pic_{name}.png")
    Image.fromarray(canvas).save(path, "PNG", optimize=True)
    print(f"saved {path} ({os.path.getsize(path)} bytes)")


def main() -> None:
    if not os.path.isfile(PDF_PATH):
        print(f"PDF not found: {PDF_PATH}", file=sys.stderr)
        sys.exit(1)

    os.makedirs(OUT, exist_ok=True)
    doc = fitz.open(PDF_PATH)

    cover = fit_on_canvas(render_page_region(doc, COVER_PAGE, COVER_CROP))
    save_canvas(cover, "guide_cover")

    for suffix, page_num, crop in MOVES:
        raw = render_page_region(doc, page_num, crop)
        canvas = fit_on_canvas(raw)
        save_canvas(canvas, suffix)

    doc.close()
    print(f"done — cover + {len(MOVES)} move photos embedded from PDF")


if __name__ == "__main__":
    main()
