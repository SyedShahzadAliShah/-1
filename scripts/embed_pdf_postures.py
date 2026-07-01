#!/usr/bin/env python3
"""Extract posture illustrations from the 23 Fun Positions PDF, remove censorship, embed in app."""
from __future__ import annotations

import os
import sys

import cv2
import fitz
import numpy as np
from PIL import Image, ImageDraw

PDF_PATH = os.environ.get(
    "PDF_PATH",
    "/workspace/uploads/guide-to-23-fun-positions_compress_bc58.pdf",
)
OUT = "/workspace/app/src/main/res/drawable-nodpi"
TARGET_W, TARGET_H = 960, 600
BG = (252, 246, 238)

# PDF page (1-based) -> output drawable name (without pic_ prefix)
POSITIONS = [
    (2, "bicycle"),
    (3, "face_to_face"),
    (4, "the_plug"),
    (5, "lying_dog"),
    (6, "spooning"),
    (7, "bridge_69"),
    (8, "waterfall"),
    (9, "one_up"),
    (10, "cowgirl"),
    (11, "hot_seat"),
    (12, "pole_position"),
    (13, "david_copperfield"),
    (14, "the_throne"),
    (15, "the_pretzel"),
    (16, "the_shelf"),
    (17, "butter"),
    (18, "wheelbarrow"),
    (19, "mountain_climber"),
    (20, "spork"),
    (21, "the_x"),
    (22, "angel_of_snows"),
    (23, "the_spider"),
    (24, "the_standard"),
]


def build_censorship_mask(img: np.ndarray) -> np.ndarray:
    h, w = img.shape[:2]
    censor = np.zeros((h, w), dtype=np.uint8)

    not_bg = ~((img[:, :, 0] > 252) & (img[:, :, 1] > 252) & (img[:, :, 2] > 252))
    figure_zone = cv2.dilate(not_bg.astype(np.uint8) * 255, np.ones((20, 20), np.uint8), iterations=2)

    skin = (
        ((img[:, :, 0] > 140) & (img[:, :, 0] < 250) & (img[:, :, 1] > 50) & (img[:, :, 1] < 220))
        | ((img[:, :, 0] > 180) & (img[:, :, 1] > 100) & (img[:, :, 2] > 70) & (img[:, :, 2] < 210))
    )
    skin_near = cv2.dilate(skin.astype(np.uint8) * 255, np.ones((9, 9), np.uint8), iterations=2)

    def add_small_components(mask_bool: np.ndarray, min_area: int = 15, max_area: int = 40000) -> np.ndarray:
        m = (mask_bool & (figure_zone > 0)).astype(np.uint8) * 255
        n, labels, stats, _ = cv2.connectedComponentsWithStats(m, 8)
        out = np.zeros((h, w), dtype=np.uint8)
        for i in range(1, n):
            area = stats[i, cv2.CC_STAT_AREA]
            if min_area <= area <= max_area:
                out[labels == i] = 255
        return out

    pure_white = (img[:, :, 0] > 253) & (img[:, :, 1] > 253) & (img[:, :, 2] > 253)
    censor |= add_small_components(pure_white)

    # White scribbles / lines on skin (slightly off-white)
    light_on_skin = (img[:, :, 0] >= 238) & (img[:, :, 1] >= 238) & (img[:, :, 2] >= 238) & (skin_near > 0)
    censor |= add_small_components(light_on_skin, 3, 12000)

    pure_black = (img[:, :, 0] <= 3) & (img[:, :, 1] <= 3) & (img[:, :, 2] <= 3)
    censor |= add_small_components(pure_black, 5, 6000)

    return cv2.dilate(censor, np.ones((3, 3), np.uint8), iterations=1)


def process_image(img: np.ndarray) -> np.ndarray:
    h, w = img.shape[:2]
    censor_mask = build_censorship_mask(img)
    if censor_mask.sum() > 0:
        result = cv2.inpaint(img, censor_mask, 7, cv2.INPAINT_TELEA)
    else:
        result = img.copy()

    scale = min(TARGET_W / w, TARGET_H / h) * 0.90
    new_w, new_h = int(w * scale), int(h * scale)
    resized = cv2.resize(result, (new_w, new_h), interpolation=cv2.INTER_LANCZOS4)

    canvas = np.full((TARGET_H, TARGET_W, 3), BG, dtype=np.uint8)
    for row in range(TARGET_H):
        t = row / TARGET_H
        canvas[row, :] = [
            int(BG[0] * (1 - t) + 238 * t),
            int(BG[1] * (1 - t) + 226 * t),
            int(BG[2] * (1 - t) + 212 * t),
        ]

    x_off = (TARGET_W - new_w) // 2
    y_off = (TARGET_H - new_h) // 2
    canvas[y_off : y_off + new_h, x_off : x_off + new_w] = resized
    return canvas


def extract_page_image(doc: fitz.Document, page_num: int) -> np.ndarray:
    page = doc[page_num - 1]
    images = page.get_images(full=True)
    if not images:
        raise RuntimeError(f"No images on page {page_num}")
    # Use the largest image on the page (skip small logos)
    best = None
    best_area = 0
    for img in images:
        xref = img[0]
        base = doc.extract_image(xref)
        area = base["width"] * base["height"]
        if area > best_area:
            best_area = area
            best = base
    arr = np.frombuffer(best["image"], dtype=np.uint8)
    bgr = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    return cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)


def save_canvas(canvas: np.ndarray, name: str) -> None:
    pil = Image.fromarray(canvas)
    draw = ImageDraw.Draw(pil)
    draw.rounded_rectangle((8, 8, TARGET_W - 8, TARGET_H - 8), radius=12, outline=(138, 100, 80), width=2)
    path = os.path.join(OUT, f"{name}.png")
    pil.save(path, "PNG", optimize=True)
    print(f"saved {path} ({os.path.getsize(path)} bytes)")


def main() -> None:
    if not os.path.isfile(PDF_PATH):
        print(f"PDF not found: {PDF_PATH}", file=sys.stderr)
        sys.exit(1)

    os.makedirs(OUT, exist_ok=True)
    doc = fitz.open(PDF_PATH)

    # Cover from page 1
    cover = process_image(extract_page_image(doc, 1))
    save_canvas(cover, "pic_guide_cover")

    for page_num, posture_id in POSITIONS:
        raw = extract_page_image(doc, page_num)
        canvas = process_image(raw)
        save_canvas(canvas, f"pic_{posture_id}")

    doc.close()
    print("done — 23 posture photos + cover embedded")


if __name__ == "__main__":
    main()
