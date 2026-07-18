#!/usr/bin/env python3
"""Generate stylized food illustrations for the Lal Qila Buffet Recipe app."""
from __future__ import annotations

import math
import os
from typing import Callable, List, Tuple

from PIL import Image, ImageDraw, ImageFont

OUT = "/workspace/app/src/main/res/drawable-nodpi"
W, H = 960, 600

# Lal Qila inspired palette — warm reds, golds, cream
BG = (255, 248, 240)
BG2 = (245, 230, 215)
PRIMARY = (139, 26, 26)       # Deep Lal Qila red
SECONDARY = (180, 120, 50)    # Gold/bronze
ACCENT = (200, 50, 40)
PLATE = (250, 245, 238)
PLATE_RIM = (210, 190, 170)
BOWL = (248, 240, 230)
SHADOW = (200, 180, 160, 80)


def new_canvas(title: str = "Lal Qila Buffet") -> Tuple[Image.Image, ImageDraw.ImageDraw]:
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
    draw.text((30, 22), title, fill=SECONDARY)
    return img, draw


def plate(draw: ImageDraw.ImageDraw, cx: int, cy: int, rx: int, ry: int):
    draw.ellipse((cx - rx - 4, cy - ry + 8, cx + rx + 4, cy + ry + 14), fill=(180, 160, 145, 60))
    draw.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=PLATE, outline=PLATE_RIM, width=3)
    draw.ellipse((cx - rx + 12, cy - ry + 8, cx + rx - 12, cy + ry - 6), fill=(255, 252, 248))


def bowl(draw: ImageDraw.ImageDraw, cx: int, cy: int, w: int, h: int, liquid: Tuple[int, int, int]):
    draw.ellipse((cx - w, cy - h // 3, cx + w, cy + h), fill=BOWL, outline=PLATE_RIM, width=2)
    draw.ellipse((cx - w + 8, cy - h // 3 + 4, cx + w - 8, cy + h - 12), fill=liquid)


def steam(draw: ImageDraw.ImageDraw, x: int, y: int):
    for i, dx in enumerate([-20, 0, 20]):
        pts = []
        for t in range(6):
            px = x + dx + math.sin(t * 0.8 + i) * 8
            py = y - t * 18
            pts.append((px, py))
        if len(pts) > 1:
            draw.line(pts, fill=(220, 220, 220, 120), width=3)


def rice_mound(draw: ImageDraw.ImageDraw, cx: int, cy: int, color: Tuple[int, int, int], garnish: Tuple[int, int, int] = (40, 120, 40)):
    for layer in range(4):
        r = 90 - layer * 12
        y = cy - layer * 8
        draw.ellipse((cx - r, y - 30, cx + r, y + 30), fill=color)
    for i in range(8):
        angle = i * math.pi / 4
        gx = cx + int(50 * math.cos(angle))
        gy = cy - 20 + int(15 * math.sin(angle))
        draw.ellipse((gx - 6, gy - 4, gx + 6, gy + 4), fill=garnish)
    draw.ellipse((cx - 8, cy - 45, cx + 8, cy - 29), fill=(220, 180, 60))  # lemon


def curry_pool(draw: ImageDraw.ImageDraw, cx: int, cy: int, color: Tuple[int, int, int], chunks: int = 5):
    draw.ellipse((cx - 100, cy - 40, cx + 100, cy + 50), fill=color)
    for i in range(chunks):
        angle = i * 2 * math.pi / chunks
        px = cx + int(55 * math.cos(angle))
        py = cy + int(20 * math.sin(angle))
        draw.ellipse((px - 18, py - 12, px + 18, py + 12), fill=(min(color[0] + 30, 255), min(color[1] + 20, 255), color[2]))


def kebab_skewer(draw: ImageDraw.ImageDraw, cx: int, cy: int):
    draw.line([(cx - 120, cy + 40), (cx + 120, cy - 40)], fill=(160, 130, 90), width=4)
    for i, t in enumerate([-0.7, -0.35, 0, 0.35, 0.7]):
        px = cx + int(120 * t)
        py = cy - int(40 * t)
        c = (180 + i * 15, 90 + i * 10, 60)
        draw.ellipse((px - 22, py - 16, px + 22, py + 16), fill=c, outline=(120, 60, 30), width=2)


def naan_bread(draw: ImageDraw.ImageDraw, cx: int, cy: int, spots: bool = True):
    draw.ellipse((cx - 110, cy - 55, cx + 110, cy + 55), fill=(230, 200, 140), outline=(180, 140, 80), width=3)
    if spots:
        for dx, dy in [(-40, -10), (30, 5), (-10, 20), (50, -15)]:
            draw.ellipse((cx + dx - 8, cy + dy - 6, cx + dx + 8, cy + dy + 6), fill=(200, 160, 90))


def dessert_sphere(draw: ImageDraw.ImageDraw, cx: int, cy: int, color: Tuple[int, int, int], syrup: bool = False):
    draw.ellipse((cx - 45, cy - 45, cx + 45, cy + 45), fill=color, outline=(min(color[0], 180), min(color[1], 120), 40), width=2)
    if syrup:
        draw.arc((cx - 50, cy - 10, cx + 50, cy + 60), 0, 180, fill=(200, 120, 30), width=6)


def drink_glass(draw: ImageDraw.ImageDraw, cx: int, cy: int, color: Tuple[int, int, int]):
    draw.polygon([(cx - 35, cy - 60), (cx + 35, cy - 60), (cx + 28, cy + 50), (cx - 28, cy + 50)], fill=(240, 240, 250, 180), outline=(180, 180, 200))
    draw.rectangle((cx - 30, cy - 20, cx + 30, cy + 45), fill=color)
    draw.ellipse((cx - 32, cy - 28, cx + 32, cy - 8), fill=(min(color[0] + 20, 255), min(color[1] + 20, 255), color[2]))


def salad_bowl(draw: ImageDraw.ImageDraw, cx: int, cy: int):
    bowl(draw, cx, cy + 20, 110, 70, (60, 140, 70))
    for dx, dy, c in [(-40, -10, (200, 50, 50)), (30, 0, (220, 200, 60)), (0, -20, (80, 160, 80)), (-20, 10, (240, 240, 240))]:
        draw.ellipse((cx + dx - 12, cy + dy - 8, cx + dx + 12, cy + dy + 8), fill=c)


def pasta_swirl(draw: ImageDraw.ImageDraw, cx: int, cy: int):
    plate(draw, cx, cy + 20, 130, 50)
    for r in range(5):
        draw.arc((cx - 60 + r * 5, cy - 40 + r * 3, cx + 60 - r * 5, cy + 30 - r * 3), 200, 340, fill=(240, 220, 160), width=8)
    draw.ellipse((cx - 20, cy - 30, cx + 20, cy + 10), fill=(255, 240, 200))


def grill_marks(draw: ImageDraw.ImageDraw, x1: int, y1: int, x2: int, y2: int):
    for i in range(4):
        t = i / 3
        x = int(x1 + (x2 - x1) * t)
        draw.line([(x, y1), (x + 15, y2)], fill=(80, 40, 20), width=3)


def save(name: str, drawer: Callable[[ImageDraw.ImageDraw], None], title: str):
    img, draw = new_canvas(title)
    drawer(draw)
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, f"{name}.png")
    img.save(path, "PNG")
    print(f"  {path}")


# ── Cover & chapters ──────────────────────────────────────────────────────────

def draw_cover(d: ImageDraw.ImageDraw):
    d.rounded_rectangle((W // 2 - 200, 100, W // 2 + 200, 480), radius=20, fill=(139, 26, 26))
    d.rounded_rectangle((W // 2 - 185, 115, W // 2 + 185, 465), radius=16, fill=(180, 50, 40))
    d.text((W // 2 - 80, 200), "LAL QILA", fill=(255, 220, 150))
    d.text((W // 2 - 60, 260), "BUFFET", fill=(255, 248, 230))
    plate(d, W // 2, 380, 100, 35)
    rice_mound(d, W // 2, 360, (220, 190, 120))
    steam(d, W // 2, 280)


def draw_chapter_about(d: ImageDraw.ImageDraw):
    d.rounded_rectangle((120, 120, 380, 480), radius=12, fill=(139, 26, 26, 200))
    d.text((160, 200), "LAL", fill=(255, 220, 150))
    d.text((160, 250), "QILA", fill=(255, 248, 230))
    plate(d, 620, 340, 120, 45)
    curry_pool(d, 620, 330, (200, 100, 40))
    kebab_skewer(d, 620, 180)


def draw_chapter_buffet(d: ImageDraw.ImageDraw):
    for i, (x, drawer) in enumerate([(200, lambda dd: rice_mound(dd, 200, 300, (220, 190, 120))),
                                      (480, lambda dd: (plate(dd, 480, 320, 90, 35), curry_pool(dd, 480, 310, (180, 80, 30)))),
                                      (760, lambda dd: dessert_sphere(dd, 760, 300, (200, 120, 50), True))]):
        drawer(d)


def draw_chapter_stations(d: ImageDraw.ImageDraw):
    labels = ["BBQ", "Desi", "Chinese", "Dessert"]
    for i, lbl in enumerate(labels):
        x = 160 + i * 190
        plate(d, x, 340, 70, 28)
        d.text((x - 25, 380), lbl, fill=SECONDARY)
        if i == 0:
            kebab_skewer(d, x, 300)
        elif i == 1:
            rice_mound(d, x, 320, (220, 190, 120))
        elif i == 2:
            bowl(d, x, 330, 60, 40, (240, 210, 100))
        else:
            dessert_sphere(d, x, 320, (220, 160, 200))


def draw_chapter_tips(d: ImageDraw.ImageDraw):
    plate(d, W // 2, 340, 130, 48)
    for angle in range(0, 360, 60):
        rad = math.radians(angle)
        px = W // 2 + int(80 * math.cos(rad))
        py = 300 + int(50 * math.sin(rad))
        d.ellipse((px - 15, py - 12, px + 15, py + 12), fill=(200, 80 + angle % 80, 50))


# ── Station education cards ───────────────────────────────────────────────────

def draw_edu_bbq(d: ImageDraw.ImageDraw):
    kebab_skewer(d, W // 2 - 80, 280)
    kebab_skewer(d, W // 2 + 80, 300)
    steam(d, W // 2, 200)
    d.ellipse((W // 2 - 150, 400, W // 2 + 150, 430), fill=(255, 200, 100, 100))


def draw_edu_pakistani(d: ImageDraw.ImageDraw):
    plate(d, W // 2, 350, 120, 42)
    rice_mound(d, W // 2 - 60, 330, (220, 190, 120))
    curry_pool(d, W // 2 + 60, 340, (190, 90, 35), 3)


def draw_edu_chinese(d: ImageDraw.ImageDraw):
    bowl(d, W // 2, 340, 100, 55, (240, 210, 100))
    for dx in [-50, 0, 50]:
        d.ellipse((W // 2 + dx - 10, 290, W // 2 + dx + 10, 310), fill=(220, 60, 50))


def draw_edu_dessert(d: ImageDraw.ImageDraw):
    dessert_sphere(d, W // 2 - 70, 320, (200, 120, 50), True)
    dessert_sphere(d, W // 2 + 70, 310, (255, 240, 220))
    d.rounded_rectangle((W // 2 - 40, 360, W // 2 + 40, 400), radius=8, fill=(180, 100, 50))


def draw_edu_salad(d: ImageDraw.ImageDraw):
    salad_bowl(d, W // 2, 300)


def draw_edu_bread(d: ImageDraw.ImageDraw):
    naan_bread(d, W // 2 - 80, 320)
    naan_bread(d, W // 2 + 80, 330, spots=False)


# ── Recipe dishes ─────────────────────────────────────────────────────────────

DISHES: List[Tuple[str, str, Callable[[ImageDraw.ImageDraw], None]]] = [
    # Pakistani
    ("pic_biryani", "Chicken Biryani", lambda d: (plate(d, W // 2, 350, 125, 45), rice_mound(d, W // 2, 320, (230, 200, 130)), steam(d, W // 2, 240))),
    ("pic_nihari", "Beef Nihari", lambda d: bowl(d, W // 2, 340, 110, 60, (120, 70, 40))),
    ("pic_karahi", "Mutton Karahi", lambda d: (plate(d, W // 2, 350, 120, 42), curry_pool(d, W // 2, 330, (200, 70, 30), 6))),
    ("pic_handi", "Chicken Handi", lambda d: bowl(d, W // 2, 330, 100, 65, (220, 150, 80))),
    ("pic_haleem", "Haleem", lambda d: bowl(d, W // 2, 340, 115, 58, (160, 100, 50))),
    # BBQ
    ("pic_seekh_kebab", "Seekh Kebab", lambda d: kebab_skewer(d, W // 2, 300)),
    ("pic_chicken_tikka", "Chicken Tikka", lambda d: (plate(d, W // 2, 360, 110, 40), d.ellipse((W//2-60, 300, W//2+60, 360), fill=(220, 160, 100)), grill_marks(d, W//2-50, 310, W//2+50, 350))),
    ("pic_malai_boti", "Malai Boti", lambda d: (plate(d, W // 2, 360, 110, 40), d.ellipse((W//2-55, 305, W//2+55, 355), fill=(255, 240, 220)))),
    ("pic_grilled_fish", "Grilled Fish", lambda d: (plate(d, W // 2, 360, 120, 42), d.ellipse((W//2-80, 300, W//2+80, 350), fill=(200, 180, 140)), grill_marks(d, W//2-60, 310, W//2+60, 340))),
    ("pic_bbq_wings", "BBQ Wings", lambda d: (plate(d, W // 2, 360, 115, 40), *[d.ellipse((W//2-50+i*35, 300, W//2-20+i*35, 340), fill=(180, 80, 40)) for i in range(3)])),
    # Chinese
    ("pic_fried_rice", "Fried Rice", lambda d: (plate(d, W // 2, 350, 120, 42), rice_mound(d, W // 2, 320, (240, 220, 160), (200, 60, 50)))),
    ("pic_chow_mein", "Chow Mein", lambda d: (plate(d, W // 2, 350, 120, 42), pasta_swirl(d, W // 2, 310))),
    ("pic_manchurian", "Manchurian", lambda d: bowl(d, W // 2, 340, 100, 55, (80, 50, 30))),
    ("pic_sweet_sour", "Sweet & Sour", lambda d: (plate(d, W // 2, 350, 115, 40), curry_pool(d, W // 2, 320, (220, 80, 60), 4))),
    ("pic_spring_rolls", "Spring Rolls", lambda d: (plate(d, W // 2, 360, 110, 38), *[d.rounded_rectangle((W//2-70+i*45, 300, W//2-30+i*45, 345), radius=6, fill=(220, 190, 100)) for i in range(3)])),
    # Continental
    ("pic_grilled_chicken", "Grilled Chicken", lambda d: (plate(d, W // 2, 360, 115, 40), d.ellipse((W//2-50, 295, W//2+50, 355), fill=(210, 170, 120)), grill_marks(d, W//2-40, 305, W//2+40, 345))),
    ("pic_pasta_alfredo", "Pasta Alfredo", lambda d: pasta_swirl(d, W // 2, 320)),
    ("pic_chicken_steak", "Chicken Steak", lambda d: (plate(d, W // 2, 360, 120, 42), d.rounded_rectangle((W//2-70, 300, W//2+70, 350), radius=8, fill=(160, 100, 60)))),
    ("pic_mashed_potato", "Mashed Potato", lambda d: bowl(d, W // 2, 340, 100, 55, (250, 240, 210))),
    # Salads & Soups
    ("pic_corn_soup", "Corn Soup", lambda d: bowl(d, W // 2, 340, 105, 58, (255, 230, 150))),
    ("pic_garden_salad", "Garden Salad", lambda d: salad_bowl(d, W // 2, 300)),
    ("pic_russian_salad", "Russian Salad", lambda d: (bowl(d, W // 2, 340, 100, 55, (240, 230, 220)), *[d.ellipse((W//2-30+i*30, 310, W//2-10+i*30, 330), fill=(200, 50+i*20, 50)) for i in range(3)])),
    ("pic_raita", "Raita", lambda d: bowl(d, W // 2, 340, 95, 52, (250, 250, 245))),
    # Breads
    ("pic_naan", "Naan", lambda d: naan_bread(d, W // 2, 320)),
    ("pic_garlic_naan", "Garlic Naan", lambda d: (naan_bread(d, W // 2, 320), [d.ellipse((W//2-30+i*20, 295, W//2-18+i*20, 307), fill=(240, 230, 200)) for i in range(4)])),
    ("pic_roghni_naan", "Roghni Naan", lambda d: (naan_bread(d, W // 2, 320, spots=False), d.ellipse((W//2-60, 290, W//2+60, 310), fill=(200, 160, 60)))),
    # Desserts
    ("pic_gulab_jamun", "Gulab Jamun", lambda d: (dessert_sphere(d, W//2-50, 320, (120, 60, 20), True), dessert_sphere(d, W//2+50, 310, (130, 70, 25), True))),
    ("pic_kheer", "Kheer", lambda d: bowl(d, W // 2, 340, 100, 55, (255, 250, 240))),
    ("pic_rasmalai", "Rasmalai", lambda d: (bowl(d, W // 2, 350, 110, 50, (255, 248, 240)), dessert_sphere(d, W//2-40, 310, (255, 250, 245)), dessert_sphere(d, W//2+40, 315, (255, 248, 238)))),
    ("pic_gajar_halwa", "Gajar Halwa", lambda d: bowl(d, W // 2, 340, 105, 55, (220, 100, 30))),
    ("pic_ice_cream", "Ice Cream", lambda d: (d.ellipse((W//2-30, 360, W//2+30, 390), fill=(220, 200, 180)), d.ellipse((W//2-45, 300, W//2+45, 370), fill=(255, 200, 220)), d.ellipse((W//2-20, 270, W//2+20, 310), fill=(200, 230, 255)))),
    # Beverages
    ("pic_mint_margarita", "Mint Margarita", lambda d: drink_glass(d, W // 2, 310, (80, 180, 100))),
    ("pic_kashmiri_chai", "Kashmiri Chai", lambda d: drink_glass(d, W // 2, 310, (200, 120, 140))),
    ("pic_fruit_juice", "Fruit Juice", lambda d: drink_glass(d, W // 2, 310, (255, 180, 60))),
    # Chef Specials
    ("pic_dum_biryani", "Dum Biryani", lambda d: (bowl(d, W//2, 350, 115, 60, (200, 80, 40)), rice_mound(d, W//2, 280, (230, 200, 130)), steam(d, W//2, 220))),
    ("pic_lq_karahi", "LQ Special Karahi", lambda d: (plate(d, W//2, 350, 125, 45), curry_pool(d, W//2, 320, (180, 50, 25), 7), d.text((W//2-30, 250), "SPECIAL", fill=ACCENT))),
    ("pic_shahi_tukda", "Shahi Tukda", lambda d: (plate(d, W//2, 360, 110, 40), d.rounded_rectangle((W//2-60, 300, W//2+60, 345), radius=6, fill=(220, 180, 100)), d.ellipse((W//2-20, 285, W//2+20, 305), fill=(255, 240, 200)))),
    ("pic_prawn_tempura", "Prawn Tempura", lambda d: (plate(d, W//2, 360, 115, 40), *[d.ellipse((W//2-60+i*40, 300, W//2-30+i*40, 340), fill=(255, 230, 180)) for i in range(3)])),
    ("pic_sizzling_brownie", "Sizzling Brownie", lambda d: (d.ellipse((W//2-80, 400, W//2+80, 430), fill=(255, 150, 50, 120)), d.rounded_rectangle((W//2-65, 310, W//2+65, 380), radius=8, fill=(100, 60, 30)), d.ellipse((W//2-30, 285, W//2+30, 320), fill=(255, 250, 240)))),
    ("pic_kunafa", "Kunafa", lambda d: (plate(d, W//2, 360, 115, 40), d.rounded_rectangle((W//2-70, 300, W//2+70, 350), radius=10, fill=(220, 180, 80)), d.ellipse((W//2-25, 285, W//2+25, 310), fill=(255, 240, 200)))),
]


def main():
    print("Generating Lal Qila Buffet illustrations...")
    save("pic_guide_cover", draw_cover, "Lal Qila Buffet Menu")
    save("pic_chapter_consent", draw_chapter_about, "About Lal Qila")
    save("pic_chapter_connection", draw_chapter_buffet, "Buffet Experience")
    save("pic_chapter_comfort", draw_chapter_stations, "Buffet Stations")
    save("pic_chapter_explore", draw_chapter_tips, "Dining Tips")
    save("pic_edu_face_contact", draw_edu_bbq, "Live BBQ Station")
    save("pic_edu_side_alignment", draw_edu_pakistani, "Pakistani Station")
    save("pic_edu_rear_safety", draw_edu_chinese, "Chinese Station")
    save("pic_edu_hip_pillow", draw_edu_dessert, "Dessert Station")
    save("pic_edu_body_map", draw_edu_salad, "Salad Bar")
    # Reuse chapter images for station guide chapters
    save("pic_edu_buffet_etiquette", draw_chapter_buffet, "Buffet Etiquette")
    save("pic_edu_spice_guide", draw_edu_pakistani, "Spice Guide")
    save("pic_edu_pairing", draw_chapter_tips, "Pairing Tips")
    save("pic_edu_dessert_pair", draw_edu_dessert, "Dessert Pairing")
    # Chef specials reuse dish art
    for name, title, drawer in DISHES:
        save(name, drawer, title)
    # Legacy names mapped for any remaining references
    aliases = {
        "pic_missionary": "pic_biryani", "pic_cowgirl": "pic_karahi",
        "pic_spooning": "pic_nihari", "pic_side_by_side": "pic_handi",
        "pic_doggy": "pic_seekh_kebab", "pic_lotus": "pic_chicken_tikka",
        "pic_standing": "pic_malai_boti", "pic_edge_bed": "pic_grilled_fish",
        "pic_reverse_cowgirl": "pic_bbq_wings", "pic_butterfly": "pic_fried_rice",
        "pic_scissors": "pic_chow_mein", "pic_lazy_dog": "pic_manchurian",
        "pic_imagine_breath": "pic_dum_biryani", "pic_imagine_candlelight": "pic_lq_karahi",
        "pic_imagine_embrace": "pic_shahi_tukda", "pic_imagine_ocean": "pic_prawn_tempura",
        "pic_imagine_starlight": "pic_sizzling_brownie", "pic_imagine_morning": "pic_kunafa",
    }
    for alias, source in aliases.items():
        src = os.path.join(OUT, f"{source}.png")
        dst = os.path.join(OUT, f"{alias}.png")
        if os.path.exists(src):
            Image.open(src).save(dst)
    print(f"Done — {len(os.listdir(OUT))} images in {OUT}")


if __name__ == "__main__":
    main()
