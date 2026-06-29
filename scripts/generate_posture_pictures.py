#!/usr/bin/env python3
"""Generate educational intimacy/sex-education diagram PNGs for the Intimacy Guide app."""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = "/workspace/app/src/main/res/drawable-nodpi"
W, H = 960, 600

BG = (255, 248, 245)
BG2 = (238, 228, 238)
PRIMARY = (123, 75, 106)
SECONDARY = (196, 154, 108)
SKIN_A = (225, 185, 155)
SKIN_B = (195, 155, 125)
SKIN_OUTLINE = (140, 100, 85)
BED = (220, 200, 192)
PILLOW = (248, 240, 235)
ACCENT = (90, 140, 180)
LABEL_BG = (255, 255, 255)


def new_canvas():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    for row in range(H):
        t = row / H
        r = int(BG[0] * (1 - t) + BG2[0] * t)
        g = int(BG[1] * (1 - t) + BG2[1] * t)
        b = int(BG[2] * (1 - t) + BG2[2] * t)
        draw.line([(0, row), (W, row)], fill=(r, g, b))
    frame(draw)
    return img, draw


def frame(draw):
    draw.rounded_rectangle((12, 12, W - 12, H - 12), radius=16, outline=PRIMARY, width=3)
    draw.text((28, 20), "Educational Diagram", fill=PRIMARY)


def oval(draw, xy, fill, outline=SKIN_OUTLINE, width=2):
    draw.ellipse(xy, fill=fill, outline=outline, width=width)


def limb(draw, xy, fill, outline=SKIN_OUTLINE):
    draw.rounded_rectangle(xy, radius=10, fill=fill, outline=outline, width=2)


def bed(draw, y=420):
    draw.ellipse((W // 2 - 200, y + 55, W // 2 + 200, y + 85), fill=(180, 160, 155))
    draw.rounded_rectangle((60, y, W - 60, y + 70), radius=20, fill=BED, outline=(190, 170, 160), width=2)
    draw.rounded_rectangle((80, y - 25, W - 80, y + 5), radius=14, fill=PILLOW, outline=(210, 195, 185), width=2)


def tag(draw, x, y, text, color=PRIMARY):
    tw = len(text) * 9 + 24
    draw.rounded_rectangle((x, y, x + tw, y + 30), radius=8, fill=LABEL_BG, outline=color, width=2)
    draw.text((x + 12, y + 7), text, fill=color)


def arrow(draw, x1, y1, x2, y2, color=ACCENT):
    draw.line([(x1, y1), (x2, y2)], fill=color, width=3)
    draw.polygon([(x2, y2), (x2 - 10, y2 - 6), (x2 - 10, y2 + 6)], fill=color)


def head(draw, cx, cy, r, color):
    oval(draw, (cx - r, cy - r, cx + r, cy + r), color)


def torso(draw, cx, cy, w, h, color):
    limb(draw, (cx - w // 2, cy, cx + w // 2, cy + h), color)


def partner_labels(draw, a_pos, b_pos):
    tag(draw, a_pos[0], a_pos[1], "Partner A", SECONDARY)
    tag(draw, b_pos[0], b_pos[1], "Partner B", PRIMARY)


def title_label(draw, text):
    draw.rounded_rectangle((W // 2 - len(text) * 7 - 20, H - 52, W // 2 + len(text) * 7 + 20, H - 14),
                           radius=12, fill=LABEL_BG, outline=PRIMARY, width=2)
    draw.text((W // 2 - len(text) * 6, H - 44), text, fill=PRIMARY)


def save(name, img):
    path = os.path.join(OUT, f"{name}.png")
    img.save(path, "PNG", optimize=True)
    print("saved", path, os.path.getsize(path))


# --- Physical postures ---

def gen_missionary():
    img, draw = new_canvas()
    bed(draw, 400)
    torso(draw, 420, 360, 90, 55, SKIN_A)
    head(draw, 420, 320, 28, SKIN_A)
    limb(draw, (360, 400, 410, 470), SKIN_A)
    limb(draw, (430, 400, 480, 465), SKIN_A)
    torso(draw, 420, 310, 80, 50, SKIN_B)
    head(draw, 420, 275, 26, SKIN_B)
    limb(draw, (370, 300, 400, 350), SKIN_B)
    limb(draw, (440, 300, 470, 350), SKIN_B)
    arrow(draw, 520, 340, 560, 340)
    tag(draw, 565, 325, "Face to face")
    partner_labels(draw, (80, 80), (80, 120))
    title_label(draw, "Missionary Position")
    save("pic_missionary", img)


def gen_cowgirl():
    img, draw = new_canvas()
    bed(draw, 405)
    torso(draw, 430, 385, 95, 50, SKIN_A)
    head(draw, 430, 345, 28, SKIN_A)
    head(draw, 430, 255, 26, SKIN_B)
    torso(draw, 430, 275, 70, 55, SKIN_B)
    limb(draw, (380, 310, 410, 400), SKIN_B)
    limb(draw, (450, 310, 480, 400), SKIN_B)
    arrow(draw, 560, 290, 600, 260)
    tag(draw, 605, 245, "Partner B on top")
    partner_labels(draw, (80, 80), (80, 120))
    title_label(draw, "Cowgirl / Woman on Top")
    save("pic_cowgirl", img)


def gen_spooning():
    img, draw = new_canvas()
    bed(draw, 405)
    torso(draw, 500, 370, 110, 45, SKIN_B)
    head(draw, 560, 345, 26, SKIN_B)
    torso(draw, 420, 375, 100, 42, SKIN_A)
    head(draw, 370, 350, 26, SKIN_A)
    limb(draw, (390, 405, 430, 470), SKIN_A)
    tag(draw, 600, 300, "Same direction")
    partner_labels(draw, (80, 80), (80, 120))
    title_label(draw, "Spooning Position")
    save("pic_spooning", img)


def gen_side_by_side():
    img, draw = new_canvas()
    bed(draw, 405)
    torso(draw, 360, 370, 80, 42, SKIN_A)
    head(draw, 330, 345, 24, SKIN_A)
    torso(draw, 520, 370, 80, 42, SKIN_B)
    head(draw, 550, 345, 24, SKIN_B)
    limb(draw, (400, 400, 480, 430), SKIN_A)
    arrow(draw, 400, 320, 520, 320)
    tag(draw, 420, 290, "Facing each other")
    partner_labels(draw, (80, 80), (80, 120))
    title_label(draw, "Side by Side (Facing)")
    save("pic_side_by_side", img)


def gen_doggy():
    img, draw = new_canvas()
    bed(draw, 415)
    torso(draw, 400, 365, 100, 38, SKIN_A)
    head(draw, 350, 350, 24, SKIN_A)
    limb(draw, (360, 390, 385, 460), SKIN_A)
    limb(draw, (420, 390, 445, 460), SKIN_A)
    torso(draw, 520, 330, 75, 55, SKIN_B)
    head(draw, 555, 305, 24, SKIN_B)
    arrow(draw, 470, 350, 510, 340)
    tag(draw, 515, 325, "Rear entry")
    partner_labels(draw, (80, 80), (80, 120))
    title_label(draw, "Rear Entry Position")
    save("pic_doggy", img)


def gen_lotus():
    img, draw = new_canvas()
    draw.rounded_rectangle((120, 430, W - 120, 490), radius=16, fill=BED, outline=(190, 170, 160), width=2)
    torso(draw, 420, 390, 90, 45, SKIN_A)
    head(draw, 420, 355, 26, SKIN_A)
    torso(draw, 420, 310, 70, 50, SKIN_B)
    head(draw, 420, 275, 24, SKIN_B)
    limb(draw, (380, 340, 410, 420), SKIN_B)
    limb(draw, (430, 340, 460, 420), SKIN_B)
    tag(draw, 560, 300, "Seated embrace")
    partner_labels(draw, (80, 80), (80, 120))
    title_label(draw, "Lotus Position")
    save("pic_lotus", img)


def gen_standing():
    img, draw = new_canvas()
    draw.rounded_rectangle((700, 120, 740, 480), radius=8, fill=(210, 200, 195))
    torso(draw, 500, 280, 70, 100, SKIN_B)
    head(draw, 500, 240, 26, SKIN_B)
    limb(draw, (470, 370, 495, 470), SKIN_B)
    limb(draw, (505, 370, 530, 470), SKIN_B)
    torso(draw, 420, 320, 60, 70, SKIN_A)
    head(draw, 400, 290, 22, SKIN_A)
    limb(draw, (430, 360, 470, 420), SKIN_A)
    tag(draw, 560, 200, "Wall support")
    partner_labels(draw, (80, 80), (80, 120))
    title_label(draw, "Standing Position")
    save("pic_standing", img)


def gen_edge_bed():
    img, draw = new_canvas()
    bed(draw, 400)
    torso(draw, 350, 365, 95, 48, SKIN_A)
    head(draw, 310, 340, 26, SKIN_A)
    limb(draw, (300, 400, 340, 470), SKIN_A)
    limb(draw, (360, 400, 400, 470), SKIN_A)
    torso(draw, 520, 300, 65, 95, SKIN_B)
    head(draw, 520, 265, 24, SKIN_B)
    arrow(draw, 450, 380, 490, 350)
    tag(draw, 495, 335, "At bed edge")
    partner_labels(draw, (80, 80), (80, 120))
    title_label(draw, "Edge of Bed")
    save("pic_edge_bed", img)


def gen_reverse_cowgirl():
    img, draw = new_canvas()
    bed(draw, 405)
    torso(draw, 430, 385, 95, 50, SKIN_A)
    head(draw, 430, 345, 28, SKIN_A)
    head(draw, 430, 265, 24, SKIN_B)
    torso(draw, 430, 285, 70, 50, SKIN_B)
    limb(draw, (380, 310, 405, 400), SKIN_B)
    limb(draw, (455, 310, 480, 400), SKIN_B)
    tag(draw, 560, 250, "Facing away")
    partner_labels(draw, (80, 80), (80, 120))
    title_label(draw, "Reverse Cowgirl")
    save("pic_reverse_cowgirl", img)


def gen_butterfly():
    img, draw = new_canvas()
    bed(draw, 400)
    draw.rounded_rectangle((360, 375, 500, 395), radius=6, fill=PILLOW, outline=SECONDARY, width=2)
    torso(draw, 400, 355, 90, 45, SKIN_A)
    head(draw, 360, 335, 24, SKIN_A)
    limb(draw, (330, 370, 370, 420), SKIN_A)
    limb(draw, (430, 370, 470, 420), SKIN_A)
    torso(draw, 540, 300, 65, 90, SKIN_B)
    head(draw, 540, 268, 24, SKIN_B)
    tag(draw, 560, 240, "Hips elevated")
    partner_labels(draw, (80, 80), (80, 120))
    title_label(draw, "Butterfly Position")
    save("pic_butterfly", img)


def gen_scissors():
    img, draw = new_canvas()
    bed(draw, 405)
    torso(draw, 360, 370, 80, 40, SKIN_A)
    head(draw, 330, 345, 24, SKIN_A)
    limb(draw, (400, 390, 480, 420), SKIN_A)
    torso(draw, 520, 375, 80, 40, SKIN_B)
    head(draw, 550, 350, 24, SKIN_B)
    limb(draw, (400, 400, 480, 430), SKIN_B)
    tag(draw, 600, 330, "Legs intertwined")
    partner_labels(draw, (80, 80), (80, 120))
    title_label(draw, "Scissors Position")
    save("pic_scissors", img)


def gen_lazy_dog():
    img, draw = new_canvas()
    bed(draw, 415)
    draw.rounded_rectangle((350, 380, 490, 400), radius=6, fill=PILLOW, outline=SECONDARY, width=2)
    torso(draw, 400, 375, 110, 35, SKIN_A)
    head(draw, 340, 360, 24, SKIN_A)
    torso(draw, 420, 350, 90, 30, SKIN_B)
    head(draw, 460, 335, 22, SKIN_B)
    tag(draw, 560, 310, "Flat & relaxed")
    partner_labels(draw, (80, 80), (80, 120))
    title_label(draw, "Lazy Dog Position")
    save("pic_lazy_dog", img)


# --- Chapters ---

def gen_chapter_consent():
    img, draw = new_canvas()
    head(draw, 320, 250, 40, SKIN_A)
    head(draw, 640, 250, 40, SKIN_B)
    draw.rounded_rectangle((340, 320, 620, 390), radius=16, fill=LABEL_BG, outline=PRIMARY, width=2)
    draw.text((400, 345), "Is this okay?", fill=PRIMARY)
    tag(draw, 260, 180, "Communication")
    title_label(draw, "Consent & Communication")
    save("pic_chapter_consent", img)


def gen_chapter_connection():
    img, draw = new_canvas()
    head(draw, 300, 260, 36, SKIN_A)
    head(draw, 660, 260, 36, SKIN_B)
    draw.line([(340, 280), (620, 280)], fill=SECONDARY, width=4)
    for x in range(420, 540, 30):
        draw.ellipse((x, 200, x + 18, 218), fill=PRIMARY)
    title_label(draw, "Building Connection")
    save("pic_chapter_connection", img)


def gen_chapter_comfort():
    img, draw = new_canvas()
    bed(draw, 400)
    torso(draw, 430, 365, 90, 48, SKIN_A)
    head(draw, 430, 325, 28, SKIN_A)
    draw.rounded_rectangle((370, 380, 490, 400), radius=6, fill=PILLOW, outline=SECONDARY, width=2)
    tag(draw, 560, 300, "Pillow support")
    title_label(draw, "Comfort & Safety")
    save("pic_chapter_comfort", img)


def gen_chapter_explore():
    img, draw = new_canvas()
    for i, x in enumerate([220, 430, 640]):
        c = SKIN_A if i % 2 == 0 else SKIN_B
        head(draw, x, 260, 28, c)
        torso(draw, x, 300, 55, 40, c)
        draw.ellipse((x - 50, 360, x + 50, 400), outline=PRIMARY, width=2)
    title_label(draw, "Explore Together")
    save("pic_chapter_explore", img)


def gen_guide_cover():
    img, draw = new_canvas()
    bed(draw, 400)
    torso(draw, 380, 370, 80, 42, SKIN_A)
    head(draw, 350, 345, 26, SKIN_A)
    torso(draw, 520, 370, 80, 42, SKIN_B)
    head(draw, 550, 345, 26, SKIN_B)
    draw.text((W // 2 - 160, 120), "Ultimate Intimacy Guide", fill=PRIMARY)
    draw.text((W // 2 - 100, 155), "English  |  Urdu", fill=SECONDARY)
    title_label(draw, "Couples Sex Education")
    save("pic_guide_cover", img)


# --- Imagination postures ---

def gen_imagine_breath():
    img, draw = new_canvas()
    head(draw, 360, 260, 32, SKIN_A)
    head(draw, 600, 260, 32, SKIN_B)
    for x in range(380, 580, 50):
        draw.arc((x, 180, x + 60, 240), 200, 340, fill=SECONDARY, width=3)
    tag(draw, 400, 340, "Breathe together")
    title_label(draw, "Breath Together")
    save("pic_imagine_breath", img)


def gen_imagine_candlelight():
    img, draw = new_canvas()
    draw.rounded_rectangle((60, 60, W - 60, H - 80), radius=20, fill=(35, 25, 45))
    draw.rectangle((460, 240, 500, 380), fill=(255, 220, 150))
    draw.polygon([(480, 210), (455, 245), (505, 245)], fill=(255, 200, 80))
    head(draw, 340, 300, 30, SKIN_A)
    head(draw, 620, 300, 30, SKIN_B)
    title_label(draw, "Candlelight Gaze")
    save("pic_imagine_candlelight", img)


def gen_imagine_embrace():
    img, draw = new_canvas()
    bed(draw, 400)
    draw.rounded_rectangle((350, 280, 610, 400), radius=24, fill=SKIN_B, outline=SKIN_OUTLINE, width=2)
    head(draw, 400, 250, 28, SKIN_A)
    head(draw, 560, 250, 28, SKIN_B)
    title_label(draw, "Slow Embrace")
    save("pic_imagine_embrace", img)


def gen_imagine_ocean():
    img, draw = new_canvas()
    for row in range(300, 500, 35):
        draw.arc((80, row, W - 80, row + 50), 0, 180, fill=ACCENT, width=3)
    torso(draw, 380, 370, 80, 40, SKIN_A)
    head(draw, 350, 345, 24, SKIN_A)
    torso(draw, 520, 370, 80, 40, SKIN_B)
    head(draw, 550, 345, 24, SKIN_B)
    title_label(draw, "Ocean Waves")
    save("pic_imagine_ocean", img)


def gen_imagine_starlight():
    img, draw = new_canvas()
    draw.rectangle((0, 0, W, 220), fill=(30, 25, 55))
    for i in range(20):
        x, y = 50 + i * 45, 40 + (i % 5) * 25
        draw.ellipse((x, y, x + 5, y + 5), fill=(255, 255, 200))
    bed(draw, 400)
    torso(draw, 380, 370, 80, 40, SKIN_A)
    torso(draw, 520, 370, 80, 40, SKIN_B)
    title_label(draw, "Starlit Embrace")
    save("pic_imagine_starlight", img)


def gen_imagine_morning():
    img, draw = new_canvas()
    draw.rectangle((0, 0, W, 200), fill=(255, 235, 200))
    draw.ellipse((760, 40, 880, 160), fill=(255, 220, 100))
    bed(draw, 400)
    torso(draw, 400, 365, 90, 45, SKIN_A)
    head(draw, 370, 335, 26, SKIN_A)
    torso(draw, 500, 360, 75, 42, SKIN_B)
    head(draw, 530, 332, 24, SKIN_B)
    title_label(draw, "Morning Light")
    save("pic_imagine_morning", img)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    gen_missionary()
    gen_cowgirl()
    gen_spooning()
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
    gen_guide_cover()
    gen_imagine_breath()
    gen_imagine_candlelight()
    gen_imagine_embrace()
    gen_imagine_ocean()
    gen_imagine_starlight()
    gen_imagine_morning()
    print("done")
