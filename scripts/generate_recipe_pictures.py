#!/usr/bin/env python3
"""Generate food illustrations for Karachi Buffet Recipes app."""
from __future__ import annotations

import os
from typing import Dict, List, Tuple

from PIL import Image, ImageDraw, ImageFont

OUT = "/workspace/app/src/main/res/drawable-nodpi"
W, H = 960, 600

BG = (255, 248, 240)
BG2 = (245, 230, 215)
PRIMARY = (139, 69, 19)
SECONDARY = (178, 102, 38)
ACCENT = (34, 139, 34)
PLATE = (250, 245, 235)
PLATE_RIM = (210, 180, 140)

DISH_COLORS: Dict[str, Tuple[Tuple[int, int, int], Tuple[int, int, int]]] = {
    "biryani": ((218, 165, 90), (139, 90, 43)),
    "bbq": ((120, 60, 30), (200, 100, 50)),
    "karahi": ((200, 80, 40), (160, 50, 30)),
    "curry": ((220, 140, 60), (180, 100, 40)),
    "appetizer": ((240, 200, 80), (200, 150, 50)),
    "seafood": ((100, 160, 200), (60, 120, 160)),
    "dessert": ((255, 200, 220), (220, 120, 160)),
    "soup": ((180, 140, 100), (140, 100, 70)),
    "guide": ((100, 140, 100), (70, 110, 70)),
}


def new_canvas(title: str) -> Tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for row in range(H):
        t = row / H
        r = int(BG[0] * (1 - t) + BG2[0] * t)
        g = int(BG[1] * (1 - t) + BG2[1] * t)
        b = int(BG[2] * (1 - t) + BG2[2] * t)
        draw.line([(0, row), (W, row)], fill=(r, g, b))
    draw.rounded_rectangle((12, 12, W - 12, H - 12), radius=14, outline=SECONDARY, width=2)
    draw.rounded_rectangle((18, 18, W - 18, 52), radius=8, fill=(255, 252, 248, 230), outline=SECONDARY, width=1)
    draw.text((30, 24), title, fill=SECONDARY)
    return img, draw


def draw_plate(draw: ImageDraw.ImageDraw, cx: int, cy: int, radius: int = 180):
    draw.ellipse((cx - radius, cy - radius + 20, cx + radius, cy + radius + 20), fill=PLATE_RIM)
    draw.ellipse((cx - radius + 12, cy - radius + 32, cx + radius - 12, cy + radius + 8), fill=PLATE)


def draw_biryani(draw: ImageDraw.ImageDraw, cx: int, cy: int):
    draw_plate(draw, cx, cy)
    for i in range(40):
        x = cx - 120 + (i % 10) * 26
        y = cy - 60 + (i // 10) * 22
        c = (218, 165, 90) if i % 3 else (139, 90, 43)
        draw.ellipse((x, y, x + 18, y + 14), fill=c)
    draw.ellipse((cx - 30, cy - 20, cx + 30, cy + 20), fill=(255, 220, 180))
    draw.text((cx - 40, cy + 80), "Karachi Style", fill=PRIMARY)


def draw_bbq(draw: ImageDraw.ImageDraw, cx: int, cy: int):
    draw.rectangle((cx - 160, cy + 60, cx + 160, cy + 90), fill=(80, 50, 30))
    for i, xoff in enumerate([-80, 0, 80]):
        draw.rectangle((cx + xoff - 8, cy - 80, cx + xoff + 8, cy + 60), fill=(100, 60, 30))
        draw.ellipse((cx + xoff - 35, cy - 30, cx + xoff + 35, cy + 30), fill=(120 + i * 20, 60, 30))


def draw_karahi(draw: ImageDraw.ImageDraw, cx: int, cy: int):
    draw.ellipse((cx - 150, cy - 20, cx + 150, cy + 120), fill=(60, 60, 60))
    draw.ellipse((cx - 130, cy, cx + 130, cy + 100), fill=(200, 80, 40))
    draw.ellipse((cx - 100, cy + 10, cx + 100, cy + 80), fill=(180, 60, 30))
    draw.rectangle((cx - 20, cy - 60, cx + 20, cy - 20), fill=(80, 80, 80))


def draw_curry(draw: ImageDraw.ImageDraw, cx: int, cy: int):
    draw_plate(draw, cx, cy, 160)
    draw.ellipse((cx - 100, cy - 40, cx + 100, cy + 60), fill=(220, 140, 60))
    for i in range(8):
        draw.ellipse((cx - 70 + i * 20, cy - 10, cx - 55 + i * 20, cy + 5), fill=(160, 80, 40))


def draw_appetizer(draw: ImageDraw.ImageDraw, cx: int, cy: int):
    draw_plate(draw, cx, cy, 150)
    for i in range(6):
        x = cx - 60 + (i % 3) * 55
        y = cy - 30 + (i // 3) * 50
        draw.polygon([(x, y + 30), (x + 20, y), (x + 40, y + 30)], fill=(240, 200, 80))


def draw_seafood(draw: ImageDraw.ImageDraw, cx: int, cy: int):
    draw_plate(draw, cx, cy)
    draw.ellipse((cx - 80, cy - 20, cx + 80, cy + 40), fill=(200, 160, 120))
    draw.polygon([(cx - 100, cy), (cx - 60, cy - 50), (cx - 20, cy)], fill=(100, 160, 200))
    draw.polygon([(cx + 20, cy), (cx + 60, cy - 50), (cx + 100, cy)], fill=(100, 160, 200))


def draw_dessert(draw: ImageDraw.ImageDraw, cx: int, cy: int):
    draw_plate(draw, cx, cy, 150)
    draw.ellipse((cx - 70, cy - 30, cx + 70, cy + 50), fill=(255, 200, 220))
    draw.ellipse((cx - 50, cy - 10, cx + 50, cy + 30), fill=(220, 120, 160))
    for i in range(5):
        draw.ellipse((cx - 40 + i * 20, cy - 50, cx - 28 + i * 20, cy - 38), fill=(255, 220, 100))


def draw_soup(draw: ImageDraw.ImageDraw, cx: int, cy: int):
    draw.ellipse((cx - 120, cy - 40, cx + 120, cy + 80), fill=(200, 200, 200))
    draw.ellipse((cx - 100, cy - 20, cx + 100, cy + 60), fill=(180, 140, 100))
    draw.rectangle((cx - 15, cy - 80, cx + 15, cy - 40), fill=(180, 180, 180))


def draw_guide(draw: ImageDraw.ImageDraw, cx: int, cy: int):
    draw.rounded_rectangle((cx - 140, cy - 80, cx + 140, cy + 100), radius=12, fill=(255, 252, 245), outline=SECONDARY, width=2)
    for i in range(5):
        draw.rectangle((cx - 110, cy - 50 + i * 28, cx + 80, cy - 30 + i * 28), fill=(230, 220, 200))
    draw.ellipse((cx + 100, cy - 60, cx + 130, cy - 30), fill=ACCENT)


DRAWERS = {
    "biryani": draw_biryani,
    "bbq": draw_bbq,
    "karahi": draw_karahi,
    "curry": draw_curry,
    "appetizer": draw_appetizer,
    "seafood": draw_seafood,
    "dessert": draw_dessert,
    "soup": draw_soup,
    "guide": draw_guide,
}


RECIPES: List[Tuple[str, str, str]] = [
    ("pic_guide_cover", "guide", "Karachi Buffet Guide"),
    ("pic_chapter_buffet_culture", "guide", "Buffet Culture"),
    ("pic_chapter_planning", "guide", "Buffet Planning"),
    ("pic_chapter_timing", "guide", "Serving Order"),
    ("pic_chapter_safety", "guide", "Food Safety"),
    ("pic_beef_biryani", "biryani", "Beef Biryani"),
    ("pic_chicken_biryani", "biryani", "Chicken Biryani"),
    ("pic_mutton_karahi", "karahi", "Mutton Karahi"),
    ("pic_chicken_karahi", "karahi", "Chicken Karahi"),
    ("pic_seekh_kebab", "bbq", "Seekh Kebab"),
    ("pic_chicken_tikka", "bbq", "Chicken Tikka"),
    ("pic_chapli_kebab", "bbq", "Chapli Kebab"),
    ("pic_nihari", "soup", "Nihari"),
    ("pic_haleem", "curry", "Haleem"),
    ("pic_aloo_gosht", "curry", "Aloo Gosht"),
    ("pic_daal_chawal", "curry", "Daal Chawal"),
    ("pic_fried_fish", "seafood", "Fried Fish"),
    ("pic_prawn_masala", "seafood", "Prawn Masala"),
    ("pic_samosa_chaat", "appetizer", "Samosa Chaat"),
    ("pic_dahi_bhalla", "appetizer", "Dahi Bhalla"),
    ("pic_gulab_jamun", "dessert", "Gulab Jamun"),
    ("pic_kheer", "dessert", "Kheer"),
    ("pic_zarda", "dessert", "Zarda"),
    ("pic_gajar_halwa", "dessert", "Gajar Halwa"),
    ("pic_raita", "appetizer", "Raita"),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    for filename, style, title in RECIPES:
        img, draw = new_canvas(title)
        DRAWERS[style](draw, W // 2, H // 2 + 20)
        path = os.path.join(OUT, f"{filename}.png")
        img.save(path, "PNG")
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
