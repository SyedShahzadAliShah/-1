#!/usr/bin/env python3
"""Generate tasteful educational posture diagram PNGs for the Intimacy Guide app."""
from PIL import Image, ImageDraw, ImageFilter
import math
import os

OUT = "/workspace/app/src/main/res/drawable-nodpi"
W, H = 640, 400

BG = (255, 248, 245)
BG2 = (240, 230, 239)
PRIMARY = (123, 75, 106)
SECONDARY = (196, 154, 108)
SKIN_A = (210, 170, 140)
SKIN_B = (180, 140, 115)
BED = (224, 208, 200)
PILLOW = (245, 235, 228)
SHADOW = (80, 50, 70, 60)


def new_canvas():
    img = Image.new("RGBA", (W, H), BG + (255,))
    draw = ImageDraw.Draw(img)
  # soft gradient background
    for y in range(H):
        t = y / H
        r = int(BG[0] * (1 - t) + BG2[0] * t)
        g = int(BG[1] * (1 - t) + BG2[1] * t)
        b = int(BG[2] * (1 - t) + BG2[2] * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))
    return img, ImageDraw.Draw(img)


def oval(draw, xy, fill, outline=None, width=2):
    draw.ellipse(xy, fill=fill, outline=outline or PRIMARY, width=width)


def shadow(draw, cx, cy, w=80, h=16):
    draw.ellipse((cx - w, cy - h // 2, cx + w, cy + h // 2), fill=(100, 70, 90, 35))


def rounded_rect(draw, xy, fill, radius=12, outline=None):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline or PRIMARY, width=2)


def bed_base(draw, y=280):
    shadow(draw, W // 2, y + 75, 220, 20)
    rounded_rect(draw, (40, y, W - 40, y + 70), BED, 18, (200, 180, 170))
    rounded_rect(draw, (50, y - 18, W - 50, y + 8), PILLOW, 14, (220, 200, 190))


def person_lying_back(draw, cx, cy, color=SKIN_A, scale=1.0):
    s = scale
    oval(draw, (cx - 22*s, cy - 55*s, cx + 22*s, cy - 15*s), color)  # head
    rounded_rect(draw, (cx - 35*s, cy - 15*s, cx + 35*s, cy + 45*s), color, 10)  # torso
    rounded_rect(draw, (cx - 55*s, cy + 20*s, cx - 15*s, cy + 70*s), color, 8)  # legs
    rounded_rect(draw, (cx + 15*s, cy + 20*s, cx + 55*s, cy + 65*s), color, 8)


def person_on_top(draw, cx, cy, color=SKIN_B, scale=1.0):
    s = scale
    oval(draw, (cx - 20*s, cy - 70*s, cx + 20*s, cy - 30*s), color)
    rounded_rect(draw, (cx - 30*s, cy - 30*s, cx + 30*s, cy + 25*s), color, 10)
    rounded_rect(draw, (cx - 45*s, cy + 5*s, cx - 10*s, cy + 55*s), color, 8)
    rounded_rect(draw, (cx + 10*s, cy + 5*s, cx + 45*s, cy + 55*s), color, 8)


def person_side(draw, cx, cy, facing_right=True, color=SKIN_A, scale=1.0):
    s = scale
    d = 1 if facing_right else -1
    oval(draw, (cx + d*30*s - 18*s, cy - 40*s, cx + d*30*s + 18*s, cy - 5*s), color)
    rounded_rect(draw, (cx - 40*s, cy - 5*s, cx + 40*s, cy + 35*s), color, 10)
    rounded_rect(draw, (cx + d*20*s - 12*s, cy + 25*s, cx + d*20*s + 35*s, cy + 65*s), color, 8)


def label(draw, text):
    rounded_rect(draw, (20, 16, 20 + len(text) * 11 + 24, 52), (255, 255, 255, 230), 10, PRIMARY)
    draw.text((32, 24), text, fill=PRIMARY)


def save(name, img):
    path = os.path.join(OUT, f"{name}.png")
    img.convert("RGB").save(path, "PNG", optimize=True)
    print("saved", path, os.path.getsize(path))


def gen_missionary():
    img, draw = new_canvas()
    bed_base(draw)
    person_lying_back(draw, 300, 250, SKIN_A, 1.1)
    person_on_top(draw, 300, 220, SKIN_B, 0.95)
    label(draw, "Missionary")
    save("pic_missionary", img)


def gen_cowgirl():
    img, draw = new_canvas()
    bed_base(draw)
    person_lying_back(draw, 310, 255, SKIN_A, 1.0)
    # sitting figure
    cx, cy = 310, 195
    oval(draw, (cx - 20, cy - 55, cx + 20, cy - 15), SKIN_B)
    rounded_rect(draw, (cx - 28, cy - 15, cx + 28, cy + 35), SKIN_B, 10)
    rounded_rect(draw, (cx - 50, cy + 10, cx - 18, cy + 70), SKIN_B, 8)
    rounded_rect(draw, (cx + 18, cy + 10, cx + 50, cy + 70), SKIN_B, 8)
    label(draw, "Cowgirl")
    save("pic_cowgirl", img)


def gen_side_by_side():
    img, draw = new_canvas()
    bed_base(draw, 290)
    person_side(draw, 260, 250, True, SKIN_A, 1.0)
    person_side(draw, 380, 250, False, SKIN_B, 1.0)
    label(draw, "Side by Side")
    save("pic_side_by_side", img)


def gen_doggy():
    img, draw = new_canvas()
    bed_base(draw, 295)
    # front on hands knees
    cx, cy = 270, 240
    oval(draw, (cx - 16, cy - 50, cx + 16, cy - 18), SKIN_A)
    rounded_rect(draw, (cx - 30, cy - 18, cx + 30, cy + 20), SKIN_A, 10)
    rounded_rect(draw, (cx - 35, cy + 5, cx - 5, cy + 55), SKIN_A, 8)
    rounded_rect(draw, (cx + 5, cy + 5, cx + 35, cy + 55), SKIN_A, 8)
    # behind kneeling
    cx2 = 360
    oval(draw, (cx2 - 18, cy - 65, cx2 + 18, cy - 25), SKIN_B)
    rounded_rect(draw, (cx2 - 28, cy - 25, cx2 + 28, cy + 30), SKIN_B, 10)
    label(draw, "Rear Entry")
    save("pic_doggy", img)


def gen_lotus():
    img, draw = new_canvas()
    rounded_rect(draw, (80, 300, W - 80, 360), BED, 16, (200, 180, 170))
    # seated base
    cx, cy = 300, 250
    oval(draw, (cx - 55, cy - 10, cx + 55, cy + 50), SKIN_A)
    oval(draw, (cx - 22, cy - 70, cx + 22, cy - 30), SKIN_A)
    rounded_rect(draw, (cx - 30, cy - 30, cx + 30, cy + 20), SKIN_A, 10)
    # on lap
    cx2, cy2 = 300, 200
    oval(draw, (cx2 - 20, cy2 - 60, cx2 + 20, cy2 - 20), SKIN_B)
    rounded_rect(draw, (cx2 - 25, cy2 - 20, cx2 + 25, cy2 + 30), SKIN_B, 10)
    rounded_rect(draw, (cx2 - 40, cy2 + 5, cx2 - 10, cy2 + 55), SKIN_B, 8)
    rounded_rect(draw, (cx2 + 10, cy2 + 5, cx2 + 40, cy2 + 55), SKIN_B, 8)
    label(draw, "Lotus")
    save("pic_lotus", img)


def gen_standing():
    img, draw = new_canvas()
    # wall
    rounded_rect(draw, (420, 60, 460, 340), (220, 210, 205), 8)
    # standing support
    cx = 340
    oval(draw, (cx - 20, 80, cx + 20, 120), SKIN_B)
    rounded_rect(draw, (cx - 28, 120, cx + 28, 240), SKIN_B, 10)
    rounded_rect(draw, (cx - 24, 240, cx - 6, 330), SKIN_B, 6)
    rounded_rect(draw, (cx + 6, 240, cx + 24, 330), SKIN_B, 6)
    # lifted partner
    cx2 = 370
    oval(draw, (cx2 - 18, 110, cx2 + 18, 150), SKIN_A)
    rounded_rect(draw, (cx2 - 22, 150, cx2 + 22, 210), SKIN_A, 10)
    rounded_rect(draw, (cx2 - 8, 210, cx2 + 30, 260), SKIN_A, 8)
    label(draw, "Standing")
    save("pic_standing", img)


def gen_edge_bed():
    img, draw = new_canvas()
    rounded_rect(draw, (200, 250, W - 60, 340), BED, 16, (200, 180, 170))
    person_lying_back(draw, 280, 230, SKIN_A, 0.9)
    # standing between legs
    cx = 420
    oval(draw, (cx - 18, 120, cx + 18, 160), SKIN_B)
    rounded_rect(draw, (cx - 24, 160, cx + 24, 270), SKIN_B, 10)
    rounded_rect(draw, (cx - 20, 270, cx - 4, 340), SKIN_B, 6)
    rounded_rect(draw, (cx + 4, 270, cx + 20, 340), SKIN_B, 6)
    label(draw, "Edge of Bed")
    save("pic_edge_bed", img)


def gen_reverse_cowgirl():
    img, draw = new_canvas()
    bed_base(draw)
    person_lying_back(draw, 310, 255, SKIN_A, 1.0)
    cx, cy = 310, 195
    oval(draw, (cx - 20, cy - 50, cx + 20, cy - 10), SKIN_B)
    rounded_rect(draw, (cx - 28, cy - 10, cx + 28, cy + 40), SKIN_B, 10)
    rounded_rect(draw, (cx - 48, cy + 15, cx - 15, cy + 75), SKIN_B, 8)
    rounded_rect(draw, (cx + 15, cy + 15, cx + 48, cy + 75), SKIN_B, 8)
    draw.text((295, 170), "↻", fill=PRIMARY)
    label(draw, "Reverse Cowgirl")
    save("pic_reverse_cowgirl", img)


def gen_butterfly():
    img, draw = new_canvas()
    rounded_rect(draw, (180, 270, W - 100, 350), BED, 16)
    rounded_rect(draw, (250, 255, 390, 275), PILLOW, 8)  # hip pillow
    cx, cy = 310, 220
    oval(draw, (cx - 20, cy - 45, cx + 20, cy - 5), SKIN_A)
    rounded_rect(draw, (cx - 30, cy - 5, cx + 30, cy + 35), SKIN_A, 10)
    rounded_rect(draw, (cx - 70, cy - 15, cx - 25, cy + 25), SKIN_A, 8)
    rounded_rect(draw, (cx + 25, cy - 15, cx + 70, cy + 25), SKIN_A, 8)
    cx2 = 430
    oval(draw, (cx2 - 18, 140, cx2 + 18, 180), SKIN_B)
    rounded_rect(draw, (cx2 - 22, 180, cx2 + 22, 280), SKIN_B, 10)
    label(draw, "Butterfly")
    save("pic_butterfly", img)


def gen_scissors():
    img, draw = new_canvas()
    bed_base(draw, 295)
    person_side(draw, 250, 255, True, SKIN_A, 0.95)
    person_side(draw, 390, 255, False, SKIN_B, 0.95)
    # intertwined legs hint
    draw.line([(290, 300), (350, 290)], fill=PRIMARY, width=3)
    label(draw, "Scissors")
    save("pic_scissors", img)


def gen_lazy_dog():
    img, draw = new_canvas()
    bed_base(draw, 295)
    rounded_rect(draw, (220, 265, 400, 285), PILLOW, 6)
    # flat on stomach
    cx, cy = 310, 255
    oval(draw, (cx - 50, cy - 15, cx - 10, cy + 15), SKIN_A)  # head turned
    rounded_rect(draw, (cx - 60, cy + 10, cx + 60, cy + 45), SKIN_A, 10)
    rounded_rect(draw, (cx - 55, cy + 35, cx - 15, cy + 70), SKIN_A, 8)
    rounded_rect(draw, (cx + 15, cy + 35, cx + 55, cy + 70), SKIN_A, 8)
    # partner behind lying on top lightly
    rounded_rect(draw, (cx - 50, cy - 5, cx + 50, cy + 30), (SKIN_B[0], SKIN_B[1], SKIN_B[2]), 10)
    label(draw, "Lazy Dog")
    save("pic_lazy_dog", img)


def gen_chapter_consent():
    img, draw = new_canvas()
    oval(draw, (200, 140, 280, 220), SKIN_A)
    oval(draw, (360, 140, 440, 220), SKIN_B)
    rounded_rect(draw, (230, 220, 410, 280), (255, 255, 255), 20, PRIMARY)
    draw.text((255, 240), "Is this okay?", fill=PRIMARY)
    # speech bubbles
    for i, x in enumerate([170, 390]):
        draw.ellipse((x, 90, x + 50, 130), fill=(255, 255, 255), outline=PRIMARY, width=2)
    label(draw, "Consent")
    save("pic_chapter_consent", img)


def gen_chapter_connection():
    img, draw = new_canvas()
    oval(draw, (180, 150, 260, 230), SKIN_A)
    oval(draw, (380, 150, 460, 230), SKIN_B)
    rounded_rect(draw, (220, 230, 420, 300), BED, 16)
    draw.line([(260, 190), (380, 190)], fill=SECONDARY, width=4)
    # hearts
    for x in [290, 310, 330]:
        draw.ellipse((x, 110, x + 20, 130), fill=PRIMARY)
    label(draw, "Connection")
    save("pic_chapter_connection", img)


def gen_chapter_comfort():
    img, draw = new_canvas()
    bed_base(draw, 270)
    rounded_rect(draw, (260, 245, 380, 265), PILLOW, 8)
    person_lying_back(draw, 310, 240, SKIN_A, 0.9)
    # blanket
    rounded_rect(draw, (240, 260, 400, 310), (230, 210, 200), 12)
    label(draw, "Comfort")
    save("pic_chapter_comfort", img)


def gen_chapter_explore():
    img, draw = new_canvas()
    positions = [(150, 200), (310, 160), (470, 200)]
    for i, (x, y) in enumerate(positions):
        c = SKIN_A if i % 2 == 0 else SKIN_B
        oval(draw, (x - 15, y - 30, x + 15, y), c)
        rounded_rect(draw, (x - 22, y, x + 22, y + 40), c, 8)
    for x1, y1 in positions:
        draw.ellipse((x1 - 40, y1 + 50, x1 + 40, y1 + 90), outline=PRIMARY, width=2)
    label(draw, "Explore")
    save("pic_chapter_explore", img)


def gen_spooning():
    img, draw = new_canvas()
    bed_base(draw, 295)
    # back partner
    cx, cy = 350, 255
    oval(draw, (cx + 20, cy - 35, cx + 56, cy + 5), SKIN_B)
    rounded_rect(draw, (cx - 20, cy + 0, cx + 80, cy + 40), SKIN_B, 12)
    rounded_rect(draw, (cx + 30, cy + 30, cx + 70, cy + 75), SKIN_B, 8)
    # front partner
    cx2, cy2 = 300, 260
    oval(draw, (cx2 - 50, cy2 - 30, cx2 - 10, cy2 + 10), SKIN_A)
    rounded_rect(draw, (cx2 - 70, cy2 + 5, cx2 + 30, cy2 + 45), SKIN_A, 12)
    rounded_rect(draw, (cx2 - 30, cy2 + 35, cx2 + 10, cy2 + 75), SKIN_A, 8)
    label(draw, "Spooning")
    save("pic_spooning", img)


def gen_guide_cover():
    img, draw = new_canvas()
    # decorative heart arc
    for i in range(5):
        x = 120 + i * 100
        draw.ellipse((x, 100, x + 40, 140), fill=(PRIMARY[0], PRIMARY[1], PRIMARY[2], 40), outline=PRIMARY)
    bed_base(draw, 270)
    person_side(draw, 260, 240, True, SKIN_A, 1.1)
    person_side(draw, 380, 240, False, SKIN_B, 1.1)
    draw.text((200, 50), "Ultimate Intimacy Guide", fill=PRIMARY)
    draw.text((210, 78), "English  •  Urdu", fill=SECONDARY)
    save("pic_guide_cover", img)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    gen_missionary()
    gen_cowgirl()
    gen_side_by_side()
    gen_doggy()
    gen_lotus()
    gen_standing()
    gen_edge_bed()
    gen_reverse_cowgirl()
    gen_butterfly()
    gen_scissors()
    gen_lazy_dog()
    gen_chapter_consent()
    gen_chapter_connection()
    gen_chapter_comfort()
    gen_chapter_explore()
    gen_spooning()
    gen_guide_cover()
    print("done")
