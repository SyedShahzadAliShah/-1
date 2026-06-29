#!/usr/bin/env python3
"""Generate sex-education diagrams with articulated human figures for the Intimacy Guide app."""
from __future__ import annotations

import math
import os
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Tuple

from PIL import Image, ImageDraw

OUT = "/workspace/app/src/main/res/drawable-nodpi"
W, H = 960, 600

# Anime sex-education palette
BG = (255, 240, 248)
BG2 = (230, 220, 255)
PRIMARY = (140, 80, 120)
SECONDARY = (210, 140, 170)
SKIN_A = (255, 224, 196)
SKIN_A_SHADE = (235, 190, 165)
SKIN_B = (255, 210, 185)
SKIN_B_SHADE = (225, 175, 150)
SKIN_OUTLINE = (50, 40, 60)
HAIR_A = (95, 60, 45)
HAIR_B = (50, 55, 95)
EYE_A = (110, 170, 220)
EYE_B = (170, 110, 200)
BED = (235, 215, 235)
PILLOW = (255, 250, 255)
ACCENT = (255, 150, 190)
JOINT = (200, 150, 170)
LABEL_BG = (255, 255, 255)
PELVIS = (255, 180, 200, 80)
BLUSH = (255, 160, 180, 110)


Point = Tuple[float, float]


@dataclass
class FigurePose:
    head: Point
    neck: Point
    shoulder_l: Point
    shoulder_r: Point
    elbow_l: Point
    elbow_r: Point
    wrist_l: Point
    wrist_r: Point
    hip_l: Point
    hip_r: Point
    knee_l: Point
    knee_r: Point
    ankle_l: Point
    ankle_r: Point


def new_canvas(title: str = "Anime Sex Education"):
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for row in range(H):
        t = row / H
        r = int(BG[0] * (1 - t) + BG2[0] * t)
        g = int(BG[1] * (1 - t) + BG2[1] * t)
        b = int(BG[2] * (1 - t) + BG2[2] * t)
        draw.line([(0, row), (W, row)], fill=(r, g, b))
    # Soft anime sparkles
    for sx, sy in [(120, 90), (820, 110), (750, 480), (180, 420), (500, 80)]:
        draw.ellipse((sx, sy, sx + 6, sy + 6), fill=(255, 255, 255, 180))
        draw.ellipse((sx + 10, sy + 8, sx + 14, sy + 12), fill=(255, 220, 240, 140))
    draw.rounded_rectangle((12, 12, W - 12, H - 12), radius=20, outline=PRIMARY, width=4)
    draw.rounded_rectangle((18, 18, W - 18, 52), radius=12, fill=(255, 255, 255, 200), outline=SECONDARY, width=2)
    draw.text((32, 26), title, fill=PRIMARY)
    return img, draw


def bed(draw: ImageDraw.ImageDraw, y: int = 420):
    draw.ellipse((W // 2 - 210, y + 58, W // 2 + 210, y + 92), fill=(180, 160, 155))
    draw.rounded_rectangle((60, y, W - 60, y + 72), radius=20, fill=BED, outline=(190, 170, 160), width=2)
    draw.rounded_rectangle((80, y - 26, W - 80, y + 6), radius=14, fill=PILLOW, outline=(210, 195, 185), width=2)


def pillow(draw: ImageDraw.ImageDraw, xy: Tuple[int, int, int, int]):
    draw.rounded_rectangle(xy, radius=8, fill=PILLOW, outline=SECONDARY, width=2)


def tag(draw: ImageDraw.ImageDraw, x: int, y: int, text: str, color=PRIMARY):
    tw = len(text) * 9 + 24
    draw.rounded_rectangle((x, y, x + tw, y + 30), radius=8, fill=LABEL_BG, outline=color, width=2)
    draw.text((x + 12, y + 7), text, fill=color)


def arrow(draw: ImageDraw.ImageDraw, x1: float, y1: float, x2: float, y2: float, color=ACCENT):
    draw.line([(x1, y1), (x2, y2)], fill=color, width=3)
    angle = math.atan2(y2 - y1, x2 - x1)
    size = 10
    draw.polygon(
        [
            (x2, y2),
            (x2 - size * math.cos(angle - 0.45), y2 - size * math.sin(angle - 0.45)),
            (x2 - size * math.cos(angle + 0.45), y2 - size * math.sin(angle + 0.45)),
        ],
        fill=color,
    )


def title_label(draw: ImageDraw.ImageDraw, text: str):
    tw = len(text) * 7
    draw.rounded_rectangle(
        (W // 2 - tw - 20, H - 52, W // 2 + tw + 20, H - 14),
        radius=12,
        fill=LABEL_BG,
        outline=PRIMARY,
        width=2,
    )
    draw.text((W // 2 - tw + 6, H - 44), text, fill=PRIMARY)


def partner_labels(draw: ImageDraw.ImageDraw):
    tag(draw, 80, 70, "Partner A", SECONDARY)
    tag(draw, 80, 110, "Partner B", PRIMARY)
    tag(draw, 80, 150, "Anime Guide", ACCENT)


def anime_limb(draw: ImageDraw.ImageDraw, a: Point, b: Point, color, shade, width: int = 12):
    draw.line([a, b], fill=SKIN_OUTLINE, width=width + 5)
    draw.line([a, b], fill=color, width=width)
    mx = (a[0] + b[0]) / 2 + 2
    my = (a[1] + b[1]) / 2
    draw.line([(mx, my), b], fill=shade, width=max(4, width - 4))


def anime_hair(draw: ImageDraw.ImageDraw, hx: float, hy: float, head_r: int, hair_color, side: str = "center"):
    offset = head_r * 0.3 if side == "right" else -head_r * 0.3 if side == "left" else 0
    draw.ellipse(
        (hx - head_r - 4 + offset, hy - head_r - 8, hx + head_r + 6 + offset, hy + head_r * 0.3),
        fill=hair_color,
        outline=SKIN_OUTLINE,
        width=2,
    )
    # Anime bangs
    draw.polygon(
        [
            (hx - head_r + offset, hy - head_r),
            (hx + offset, hy - head_r - 6),
            (hx + head_r + offset, hy - head_r),
            (hx + head_r * 0.6 + offset, hy - head_r * 0.2),
            (hx - head_r * 0.6 + offset, hy - head_r * 0.2),
        ],
        fill=hair_color,
        outline=SKIN_OUTLINE,
    )


def anime_face(draw: ImageDraw.ImageDraw, hx: float, hy: float, head_r: int, skin, shade, hair, eye_color, facing: float = 1.0):
    anime_hair(draw, hx, hy, head_r, hair, "left" if facing < 0 else "right" if facing > 0 else "center")
    draw.ellipse(
        (hx - head_r, hy - head_r, hx + head_r, hy + head_r),
        fill=skin,
        outline=SKIN_OUTLINE,
        width=3,
    )
    # Cel-shade on cheek
    draw.ellipse(
        (hx + head_r * 0.15 * facing, hy - head_r * 0.1, hx + head_r * 0.85, hy + head_r * 0.75),
        fill=shade,
    )
    draw.ellipse(
        (hx - head_r, hy - head_r, hx + head_r, hy + head_r),
        fill=skin,
        outline=SKIN_OUTLINE,
        width=3,
    )
    # Blush
    draw.ellipse((hx - head_r * 0.55, hy + head_r * 0.05, hx - head_r * 0.2, hy + head_r * 0.35), fill=BLUSH)
    draw.ellipse((hx + head_r * 0.2, hy + head_r * 0.05, hx + head_r * 0.55, hy + head_r * 0.35), fill=BLUSH)
    # Large anime eyes
    for ex in (hx - head_r * 0.38, hx + head_r * 0.12):
        draw.ellipse((ex, hy - head_r * 0.15, ex + head_r * 0.42, hy + head_r * 0.38), fill=(255, 255, 255), outline=SKIN_OUTLINE, width=2)
        draw.ellipse((ex + 4, hy - head_r * 0.05, ex + head_r * 0.3, hy + head_r * 0.28), fill=eye_color, outline=SKIN_OUTLINE, width=1)
        draw.ellipse((ex + 8, hy - head_r * 0.02, ex + 14, hy + 6), fill=(255, 255, 255))
    # Small anime mouth
    draw.arc((hx - head_r * 0.2, hy + head_r * 0.2, hx + head_r * 0.2, hy + head_r * 0.55), 15, 165, fill=SKIN_OUTLINE, width=2)


def draw_figure(
    draw: ImageDraw.ImageDraw,
    pose: FigurePose,
    color: Tuple[int, int, int],
    shade: Tuple[int, int, int],
    hair: Tuple[int, int, int],
    eye_color: Tuple[int, int, int],
    head_r: int = 30,
    show_joints: bool = False,
    show_pelvis: bool = True,
    facing: float = 1.0,
):
    pelvis_cx = (pose.hip_l[0] + pose.hip_r[0]) / 2
    pelvis_cy = (pose.hip_l[1] + pose.hip_r[1]) / 2
    shoulder_cx = (pose.shoulder_l[0] + pose.shoulder_r[0]) / 2
    shoulder_cy = (pose.shoulder_l[1] + pose.shoulder_r[1]) / 2

    if show_pelvis:
        draw.ellipse(
            (pelvis_cx - 30, pelvis_cy - 18, pelvis_cx + 30, pelvis_cy + 18),
            fill=PELVIS,
            outline=(255, 140, 170, 160),
            width=2,
        )

    torso_poly = [pose.shoulder_l, pose.shoulder_r, pose.hip_r, pose.hip_l]
    shade_poly = [pose.shoulder_r, pose.hip_r, (pelvis_cx + 12, pelvis_cy + 8), (shoulder_cx + 10, shoulder_cy + 6)]
    draw.polygon(torso_poly, fill=color, outline=SKIN_OUTLINE)
    draw.polygon(shade_poly, fill=shade)
    draw.line([pose.shoulder_l, pose.shoulder_r, pose.hip_r, pose.hip_l, pose.shoulder_l], fill=SKIN_OUTLINE, width=3)

    anime_limb(draw, pose.neck, pose.shoulder_l, color, shade, 11)
    anime_limb(draw, pose.shoulder_l, pose.elbow_l, color, shade, 10)
    anime_limb(draw, pose.elbow_l, pose.wrist_l, color, shade, 9)
    anime_limb(draw, pose.neck, pose.shoulder_r, color, shade, 11)
    anime_limb(draw, pose.shoulder_r, pose.elbow_r, color, shade, 10)
    anime_limb(draw, pose.elbow_r, pose.wrist_r, color, shade, 9)
    anime_limb(draw, pose.hip_l, pose.knee_l, color, shade, 11)
    anime_limb(draw, pose.knee_l, pose.ankle_l, color, shade, 10)
    anime_limb(draw, pose.hip_r, pose.knee_r, color, shade, 11)
    anime_limb(draw, pose.knee_r, pose.ankle_r, color, shade, 10)

    hx, hy = pose.head
    anime_face(draw, hx, hy, head_r, color, shade, hair, eye_color, facing)
    anime_limb(draw, pose.head, pose.neck, color, shade, 9)

    if show_joints:
        for p in (
            pose.neck, pose.shoulder_l, pose.shoulder_r, pose.elbow_l, pose.elbow_r,
            pose.wrist_l, pose.wrist_r, pose.hip_l, pose.hip_r, pose.knee_l,
            pose.knee_r, pose.ankle_l, pose.ankle_r,
        ):
            joint_dot(draw, p)


def joint_dot(draw: ImageDraw.ImageDraw, p: Point, r: int = 5):
    x, y = p
    draw.ellipse((x - r, y - r, x + r, y + r), fill=JOINT, outline=SKIN_OUTLINE, width=1)


def draw_figure_simple(
    draw: ImageDraw.ImageDraw,
    pose: FigurePose,
    color: Tuple[int, int, int],
    head_r: int = 30,
    show_joints: bool = False,
    show_pelvis: bool = True,
    facing: float = 1.0,
):
    kw = dict(head_r=head_r, show_joints=show_joints, show_pelvis=show_pelvis, facing=facing)
    if color == SKIN_A:
        draw_figure(draw, pose, SKIN_A, SKIN_A_SHADE, HAIR_A, EYE_A, **kw)
    else:
        draw_figure(draw, pose, SKIN_B, SKIN_B_SHADE, HAIR_B, EYE_B, **kw)


def save(name: str, img: Image.Image):
    path = os.path.join(OUT, f"{name}.png")
    img.save(path, "PNG", optimize=True)
    print("saved", path, os.path.getsize(path))


def pose(**kwargs) -> FigurePose:
    defaults = dict(
        head=(0, 0),
        neck=(0, 0),
        shoulder_l=(0, 0),
        shoulder_r=(0, 0),
        elbow_l=(0, 0),
        elbow_r=(0, 0),
        wrist_l=(0, 0),
        wrist_r=(0, 0),
        hip_l=(0, 0),
        hip_r=(0, 0),
        knee_l=(0, 0),
        knee_r=(0, 0),
        ankle_l=(0, 0),
        ankle_r=(0, 0),
    )
    defaults.update(kwargs)
    return FigurePose(**defaults)


def lying_back(cx: int, cy: int, scale: float = 1.0) -> FigurePose:
    s = scale
    return pose(
        head=(cx, cy - 55 * s),
        neck=(cx, cy - 30 * s),
        shoulder_l=(cx - 35 * s, cy - 20 * s),
        shoulder_r=(cx + 35 * s, cy - 20 * s),
        elbow_l=(cx - 55 * s, cy + 5 * s),
        elbow_r=(cx + 55 * s, cy + 5 * s),
        wrist_l=(cx - 70 * s, cy + 25 * s),
        wrist_r=(cx + 70 * s, cy + 25 * s),
        hip_l=(cx - 28 * s, cy + 35 * s),
        hip_r=(cx + 28 * s, cy + 35 * s),
        knee_l=(cx - 35 * s, cy + 75 * s),
        knee_r=(cx + 35 * s, cy + 75 * s),
        ankle_l=(cx - 38 * s, cy + 110 * s),
        ankle_r=(cx + 38 * s, cy + 110 * s),
    )


def lying_prone(cx: int, cy: int, scale: float = 1.0) -> FigurePose:
    p = lying_back(cx, cy, scale)
    return pose(**{k: (v[0], v[1] - 8 * scale) for k, v in p.__dict__.items()})


def on_top(cx: int, cy: int, scale: float = 1.0) -> FigurePose:
    s = scale
    return pose(
        head=(cx, cy - 45 * s),
        neck=(cx, cy - 22 * s),
        shoulder_l=(cx - 30 * s, cy - 12 * s),
        shoulder_r=(cx + 30 * s, cy - 12 * s),
        elbow_l=(cx - 45 * s, cy + 10 * s),
        elbow_r=(cx + 45 * s, cy + 10 * s),
        wrist_l=(cx - 55 * s, cy + 30 * s),
        wrist_r=(cx + 55 * s, cy + 30 * s),
        hip_l=(cx - 24 * s, cy + 28 * s),
        hip_r=(cx + 24 * s, cy + 28 * s),
        knee_l=(cx - 20 * s, cy + 55 * s),
        knee_r=(cx + 20 * s, cy + 55 * s),
        ankle_l=(cx - 18 * s, cy + 80 * s),
        ankle_r=(cx + 18 * s, cy + 80 * s),
    )


def straddle(cx: int, cy: int, scale: float = 1.0) -> FigurePose:
    s = scale
    return pose(
        head=(cx, cy - 50 * s),
        neck=(cx, cy - 26 * s),
        shoulder_l=(cx - 28 * s, cy - 16 * s),
        shoulder_r=(cx + 28 * s, cy - 16 * s),
        elbow_l=(cx - 40 * s, cy + 5 * s),
        elbow_r=(cx + 40 * s, cy + 5 * s),
        wrist_l=(cx - 48 * s, cy + 28 * s),
        wrist_r=(cx + 48 * s, cy + 28 * s),
        hip_l=(cx - 34 * s, cy + 30 * s),
        hip_r=(cx + 34 * s, cy + 30 * s),
        knee_l=(cx - 55 * s, cy + 55 * s),
        knee_r=(cx + 55 * s, cy + 55 * s),
        ankle_l=(cx - 60 * s, cy + 85 * s),
        ankle_r=(cx + 60 * s, cy + 85 * s),
    )


def side_lying(cx: int, cy: int, facing: str = "right", scale: float = 1.0) -> FigurePose:
    s = scale
    flip = -1 if facing == "left" else 1
    return pose(
        head=(cx + 30 * flip * s, cy - 20 * s),
        neck=(cx + 10 * flip * s, cy - 5 * s),
        shoulder_l=(cx - 10 * flip * s, cy),
        shoulder_r=(cx + 25 * flip * s, cy - 5 * s),
        elbow_l=(cx - 30 * flip * s, cy + 20 * s),
        elbow_r=(cx + 45 * flip * s, cy + 10 * s),
        wrist_l=(cx - 35 * flip * s, cy + 40 * s),
        wrist_r=(cx + 60 * flip * s, cy + 25 * s),
        hip_l=(cx - 5 * flip * s, cy + 35 * s),
        hip_r=(cx + 20 * flip * s, cy + 30 * s),
        knee_l=(cx + 5 * flip * s, cy + 65 * s),
        knee_r=(cx + 35 * flip * s, cy + 60 * s),
        ankle_l=(cx + 10 * flip * s, cy + 95 * s),
        ankle_r=(cx + 45 * flip * s, cy + 90 * s),
    )


def hands_knees(cx: int, cy: int, scale: float = 1.0) -> FigurePose:
    s = scale
    return pose(
        head=(cx - 45 * s, cy - 10 * s),
        neck=(cx - 30 * s, cy + 5 * s),
        shoulder_l=(cx - 15 * s, cy + 10 * s),
        shoulder_r=(cx + 5 * s, cy + 8 * s),
        elbow_l=(cx - 50 * s, cy + 25 * s),
        elbow_r=(cx - 20 * s, cy + 22 * s),
        wrist_l=(cx - 65 * s, cy + 40 * s),
        wrist_r=(cx - 35 * s, cy + 38 * s),
        hip_l=(cx + 15 * s, cy + 35 * s),
        hip_r=(cx + 35 * s, cy + 32 * s),
        knee_l=(cx + 10 * s, cy + 65 * s),
        knee_r=(cx + 40 * s, cy + 62 * s),
        ankle_l=(cx + 8 * s, cy + 95 * s),
        ankle_r=(cx + 42 * s, cy + 92 * s),
    )


def kneeling_behind(cx: int, cy: int, scale: float = 1.0) -> FigurePose:
    s = scale
    return pose(
        head=(cx + 20 * s, cy - 35 * s),
        neck=(cx + 15 * s, cy - 15 * s),
        shoulder_l=(cx, cy - 8 * s),
        shoulder_r=(cx + 30 * s, cy - 10 * s),
        elbow_l=(cx - 10 * s, cy + 15 * s),
        elbow_r=(cx + 40 * s, cy + 12 * s),
        wrist_l=(cx - 15 * s, cy + 35 * s),
        wrist_r=(cx + 45 * s, cy + 32 * s),
        hip_l=(cx + 5 * s, cy + 40 * s),
        hip_r=(cx + 30 * s, cy + 38 * s),
        knee_l=(cx, cy + 75 * s),
        knee_r=(cx + 35 * s, cy + 72 * s),
        ankle_l=(cx - 5 * s, cy + 95 * s),
        ankle_r=(cx + 40 * s, cy + 92 * s),
    )


def seated(cx: int, cy: int, scale: float = 1.0) -> FigurePose:
    s = scale
    return pose(
        head=(cx, cy - 48 * s),
        neck=(cx, cy - 24 * s),
        shoulder_l=(cx - 26 * s, cy - 14 * s),
        shoulder_r=(cx + 26 * s, cy - 14 * s),
        elbow_l=(cx - 38 * s, cy + 8 * s),
        elbow_r=(cx + 38 * s, cy + 8 * s),
        wrist_l=(cx - 45 * s, cy + 30 * s),
        wrist_r=(cx + 45 * s, cy + 30 * s),
        hip_l=(cx - 30 * s, cy + 35 * s),
        hip_r=(cx + 30 * s, cy + 35 * s),
        knee_l=(cx - 50 * s, cy + 55 * s),
        knee_r=(cx + 50 * s, cy + 55 * s),
        ankle_l=(cx - 55 * s, cy + 78 * s),
        ankle_r=(cx + 55 * s, cy + 78 * s),
    )


def standing(cx: int, cy: int, scale: float = 1.0) -> FigurePose:
    s = scale
    return pose(
        head=(cx, cy - 70 * s),
        neck=(cx, cy - 48 * s),
        shoulder_l=(cx - 24 * s, cy - 42 * s),
        shoulder_r=(cx + 24 * s, cy - 42 * s),
        elbow_l=(cx - 32 * s, cy - 10 * s),
        elbow_r=(cx + 32 * s, cy - 10 * s),
        wrist_l=(cx - 36 * s, cy + 18 * s),
        wrist_r=(cx + 36 * s, cy + 18 * s),
        hip_l=(cx - 20 * s, cy + 10 * s),
        hip_r=(cx + 20 * s, cy + 10 * s),
        knee_l=(cx - 18 * s, cy + 55 * s),
        knee_r=(cx + 18 * s, cy + 55 * s),
        ankle_l=(cx - 20 * s, cy + 100 * s),
        ankle_r=(cx + 20 * s, cy + 100 * s),
    )


def lifted_legs(cx: int, cy: int, scale: float = 1.0) -> FigurePose:
    s = scale
    return pose(
        head=(cx, cy - 40 * s),
        neck=(cx, cy - 18 * s),
        shoulder_l=(cx - 22 * s, cy - 10 * s),
        shoulder_r=(cx + 22 * s, cy - 10 * s),
        elbow_l=(cx - 30 * s, cy + 12 * s),
        elbow_r=(cx + 30 * s, cy + 12 * s),
        wrist_l=(cx - 35 * s, cy + 32 * s),
        wrist_r=(cx + 35 * s, cy + 32 * s),
        hip_l=(cx - 20 * s, cy + 28 * s),
        hip_r=(cx + 20 * s, cy + 28 * s),
        knee_l=(cx - 30 * s, cy + 5 * s),
        knee_r=(cx + 30 * s, cy + 5 * s),
        ankle_l=(cx - 35 * s, cy - 20 * s),
        ankle_r=(cx + 35 * s, cy - 20 * s),
    )


# --- Physical postures ---

def gen_missionary():
    img, draw = new_canvas()
    bed(draw, 400)
    draw_figure_simple(draw, lying_back(430, 390, 1.0), SKIN_A)
    draw_figure_simple(draw, on_top(430, 330, 0.95), SKIN_B)
    arrow(draw, 560, 360, 610, 360)
    tag(draw, 615, 345, "Face to face")
    partner_labels(draw)
    title_label(draw, "Missionary Position")
    save("pic_missionary", img)


def gen_cowgirl():
    img, draw = new_canvas()
    bed(draw, 405)
    draw_figure_simple(draw, lying_back(430, 400, 0.95), SKIN_A)
    draw_figure_simple(draw, straddle(430, 290, 0.9), SKIN_B)
    arrow(draw, 560, 280, 610, 250)
    tag(draw, 615, 235, "Partner B on top")
    partner_labels(draw)
    title_label(draw, "Cowgirl / Woman on Top")
    save("pic_cowgirl", img)


def gen_spooning():
    img, draw = new_canvas()
    bed(draw, 405)
    draw_figure_simple(draw, side_lying(500, 380, "left", 1.05), SKIN_B)
    draw_figure_simple(draw, side_lying(420, 385, "left", 1.0), SKIN_A)
    tag(draw, 600, 300, "Same direction")
    partner_labels(draw)
    title_label(draw, "Spooning Position")
    save("pic_spooning", img)


def gen_side_by_side():
    img, draw = new_canvas()
    bed(draw, 405)
    draw_figure_simple(draw, side_lying(360, 380, "right", 1.0), SKIN_A)
    draw_figure_simple(draw, side_lying(540, 380, "left", 1.0), SKIN_B)
    arrow(draw, 400, 310, 500, 310)
    tag(draw, 420, 280, "Facing each other")
    partner_labels(draw)
    title_label(draw, "Side by Side (Facing)")
    save("pic_side_by_side", img)


def gen_doggy():
    img, draw = new_canvas()
    bed(draw, 415)
    draw_figure_simple(draw, hands_knees(400, 360, 1.0), SKIN_A)
    draw_figure_simple(draw, kneeling_behind(520, 330, 0.95), SKIN_B)
    arrow(draw, 470, 350, 510, 340)
    tag(draw, 515, 320, "Rear entry")
    partner_labels(draw)
    title_label(draw, "Rear Entry Position")
    save("pic_doggy", img)


def gen_lotus():
    img, draw = new_canvas()
    draw.rounded_rectangle((120, 430, W - 120, 500), radius=16, fill=BED, outline=(190, 170, 160), width=2)
    draw_figure_simple(draw, seated(430, 400, 1.0), SKIN_A)
    p_b = straddle(430, 320, 0.85)
    draw_figure_simple(draw, p_b, SKIN_B)
    tag(draw, 560, 300, "Seated embrace")
    partner_labels(draw)
    title_label(draw, "Lotus Position")
    save("pic_lotus", img)


def gen_standing():
    img, draw = new_canvas()
    draw.rounded_rectangle((700, 120, 740, 480), radius=8, fill=(210, 200, 195))
    draw_figure_simple(draw, standing(500, 280, 1.0), SKIN_B)
    draw_figure_simple(draw, lifted_legs(420, 310, 0.85), SKIN_A)
    tag(draw, 560, 200, "Wall support")
    partner_labels(draw)
    title_label(draw, "Standing Position")
    save("pic_standing", img)


def gen_edge_bed():
    img, draw = new_canvas()
    bed(draw, 400)
    draw_figure_simple(draw, lying_back(350, 385, 0.95), SKIN_A)
    p = standing(540, 290, 0.9)
    draw_figure_simple(draw, p, SKIN_B)
    arrow(draw, 450, 380, 490, 350)
    tag(draw, 495, 335, "At bed edge")
    partner_labels(draw)
    title_label(draw, "Edge of Bed")
    save("pic_edge_bed", img)


def gen_reverse_cowgirl():
    img, draw = new_canvas()
    bed(draw, 405)
    draw_figure_simple(draw, lying_back(430, 400, 0.95), SKIN_A)
    p = straddle(430, 295, 0.9)
    p = pose(**{**p.__dict__, "head": (p.head[0], p.head[1] + 8)})
    draw_figure_simple(draw, p, SKIN_B, show_pelvis=False)
    tag(draw, 560, 250, "Facing away")
    partner_labels(draw)
    title_label(draw, "Reverse Cowgirl")
    save("pic_reverse_cowgirl", img)


def gen_butterfly():
    img, draw = new_canvas()
    bed(draw, 400)
    pillow(draw, (360, 375, 500, 395))
    p = lying_back(400, 360, 0.95)
    p = pose(**{**p.__dict__, "knee_l": (p.knee_l[0] - 15, p.knee_l[1] - 25), "knee_r": (p.knee_r[0] + 15, p.knee_r[1] - 25)})
    draw_figure_simple(draw, p, SKIN_A)
    draw_figure_simple(draw, standing(540, 290, 0.85), SKIN_B)
    tag(draw, 560, 240, "Hips elevated")
    partner_labels(draw)
    title_label(draw, "Butterfly Position")
    save("pic_butterfly", img)


def gen_scissors():
    img, draw = new_canvas()
    bed(draw, 405)
    draw_figure_simple(draw, side_lying(360, 380, "right", 1.0), SKIN_A)
    draw_figure_simple(draw, side_lying(520, 385, "left", 1.0), SKIN_B)
    draw.line([(400, 410), (480, 410)], fill=ACCENT, width=3)
    tag(draw, 600, 330, "Legs intertwined")
    partner_labels(draw)
    title_label(draw, "Scissors Position")
    save("pic_scissors", img)


def gen_lazy_dog():
    img, draw = new_canvas()
    bed(draw, 415)
    pillow(draw, (350, 380, 490, 400))
    p_a = hands_knees(400, 390, 0.9)
    p_a = pose(**{**p_a.__dict__, "head": (p_a.head[0] + 20, p_a.head[1] + 30)})
    draw_figure_simple(draw, p_a, SKIN_A)
    draw_figure_simple(draw, on_top(420, 350, 0.85), SKIN_B)
    tag(draw, 560, 310, "Flat & relaxed")
    partner_labels(draw)
    title_label(draw, "Lazy Dog Position")
    save("pic_lazy_dog", img)


# --- Educational inserts ---

def gen_edu_body_map():
    img, draw = new_canvas("Body Awareness")
    draw_figure_simple(draw, standing(480, 260, 1.35), SKIN_A, show_joints=True, show_pelvis=True)
    labels = [
        (560, 150, "Head & neck"),
        (620, 220, "Chest"),
        (620, 300, "Abdomen"),
        (620, 370, "Pelvis / hips"),
        (620, 450, "Thighs"),
        (620, 520, "Knees & ankles"),
    ]
    for x, y, text in labels:
        arrow(draw, x - 40, y + 5, x - 80, y + 5)
        tag(draw, x, y - 10, text, ACCENT)
    title_label(draw, "Know Your Body Zones")
    save("pic_edu_body_map", img)


def gen_edu_face_contact():
    img, draw = new_canvas("Face-to-Face Education")
    bed(draw, 405)
    draw_figure_simple(draw, lying_back(400, 390, 0.9), SKIN_A)
    draw_figure_simple(draw, on_top(400, 335, 0.85), SKIN_B)
    tag(draw, 560, 300, "Eye contact")
    tag(draw, 560, 340, "Kissing")
    tag(draw, 560, 380, "Verbal check-ins")
    draw.rounded_rectangle((300, 250, 500, 290), radius=12, fill=LABEL_BG, outline=PRIMARY, width=2)
    draw.text((330, 262), "Ask: Is this comfortable?", fill=PRIMARY)
    title_label(draw, "Face-to-Face Connection")
    save("pic_edu_face_contact", img)


def gen_edu_hip_pillow():
    img, draw = new_canvas("Hip Support")
    bed(draw, 405)
    pillow(draw, (370, 388, 510, 408))
    draw_figure_simple(draw, lying_back(430, 385, 0.95), SKIN_A)
    arrow(draw, 560, 395, 520, 395)
    tag(draw, 565, 380, "Pillow under hips")
    tag(draw, 565, 420, "Better angle & comfort")
    title_label(draw, "Hip Elevation Guide")
    save("pic_edu_hip_pillow", img)


def gen_edu_consent_talk():
    img, draw = new_canvas("Consent Education")
    draw_figure_simple(draw, standing(340, 280, 1.1), SKIN_A)
    draw_figure_simple(draw, standing(620, 280, 1.1), SKIN_B)
    draw.rounded_rectangle((380, 180, 580, 230), radius=14, fill=LABEL_BG, outline=PRIMARY, width=2)
    draw.text((410, 198), "Is this okay for you?", fill=PRIMARY)
    draw.rounded_rectangle((400, 420, 560, 470), radius=14, fill=LABEL_BG, outline=SECONDARY, width=2)
    draw.text((430, 438), "We can pause anytime", fill=SECONDARY)
    title_label(draw, "Ongoing Consent")
    save("pic_edu_consent_talk", img)


def gen_edu_side_alignment():
    img, draw = new_canvas("Side Position Guide")
    bed(draw, 405)
    draw_figure_simple(draw, side_lying(400, 380, "right", 1.05), SKIN_A)
    draw_figure_simple(draw, side_lying(520, 380, "left", 1.05), SKIN_B)
    pillow(draw, (430, 430, 490, 450))
    tag(draw, 600, 430, "Knee pillow")
    tag(draw, 600, 340, "Hip alignment")
    title_label(draw, "Side-by-Side Alignment")
    save("pic_edu_side_alignment", img)


def gen_edu_rear_safety():
    img, draw = new_canvas("Rear Entry Safety")
    bed(draw, 415)
    pillow(draw, (360, 382, 470, 402))
    draw_figure_simple(draw, hands_knees(390, 360, 0.95), SKIN_A)
    draw_figure_simple(draw, kneeling_behind(510, 330, 0.9), SKIN_B)
    tag(draw, 560, 390, "Hip pillow")
    tag(draw, 560, 330, "Slow pace")
    tag(draw, 560, 290, "Check in often")
    title_label(draw, "Rear Entry Comfort")
    save("pic_edu_rear_safety", img)


# --- Chapters ---

def gen_chapter_consent():
    img, draw = new_canvas("Consent Chapter")
    draw_figure_simple(draw, standing(320, 280, 1.05), SKIN_A)
    draw_figure_simple(draw, standing(640, 280, 1.05), SKIN_B)
    draw.rounded_rectangle((340, 320, 620, 390), radius=16, fill=LABEL_BG, outline=PRIMARY, width=2)
    draw.text((400, 345), "Is this okay?", fill=PRIMARY)
    tag(draw, 260, 180, "Communication")
    title_label(draw, "Consent & Communication")
    save("pic_chapter_consent", img)


def gen_chapter_connection():
    img, draw = new_canvas("Connection Chapter")
    draw_figure_simple(draw, standing(300, 280, 1.0), SKIN_A)
    draw_figure_simple(draw, standing(660, 280, 1.0), SKIN_B)
    draw.line([(340, 280), (620, 280)], fill=SECONDARY, width=4)
    for x in range(420, 540, 30):
        draw.ellipse((x, 200, x + 18, 218), fill=PRIMARY)
    title_label(draw, "Building Connection")
    save("pic_chapter_connection", img)


def gen_chapter_comfort():
    img, draw = new_canvas("Comfort Chapter")
    bed(draw, 400)
    pillow(draw, (370, 388, 490, 408))
    draw_figure_simple(draw, lying_back(430, 385, 0.95), SKIN_A)
    tag(draw, 560, 300, "Pillow support")
    title_label(draw, "Comfort & Safety")
    save("pic_chapter_comfort", img)


def gen_chapter_explore():
    img, draw = new_canvas("Explore Chapter")
    for i, x in enumerate([220, 430, 640]):
        draw_figure_simple(draw, standing(x, 300, 0.75), SKIN_A if i % 2 == 0 else SKIN_B, show_pelvis=False)
        draw.ellipse((x - 50, 360, x + 50, 400), outline=PRIMARY, width=2)
    title_label(draw, "Explore Together")
    save("pic_chapter_explore", img)


def gen_guide_cover():
    img, draw = new_canvas("Ultimate Intimacy Handbook")
    bed(draw, 400)
    draw_figure_simple(draw, lying_back(380, 385, 0.85), SKIN_A)
    draw_figure_simple(draw, lying_back(520, 385, 0.85), SKIN_B)
    draw.text((W // 2 - 200, 115), "Ultimate Intimacy Handbook", fill=PRIMARY)
    draw.text((W // 2 - 130, 150), "Anime Sex Education for Couples", fill=SECONDARY)
    draw.text((W // 2 - 100, 175), "English  |  Urdu", fill=ACCENT)
    title_label(draw, "Couples Intercourse Postures")
    save("pic_guide_cover", img)


# --- Imagination postures ---

def gen_imagine_breath():
    img, draw = new_canvas("Breath Exercise")
    draw_figure_simple(draw, seated(360, 320, 0.9), SKIN_A, show_pelvis=False)
    draw_figure_simple(draw, seated(600, 320, 0.9), SKIN_B, show_pelvis=False)
    for x in range(380, 580, 50):
        draw.arc((x, 180, x + 60, 240), 200, 340, fill=SECONDARY, width=3)
    tag(draw, 400, 340, "Breathe together")
    title_label(draw, "Breath Together")
    save("pic_imagine_breath", img)


def gen_imagine_candlelight():
    img, draw = new_canvas("Candlelight Exercise")
    draw.rectangle((60, 60, W - 60, H - 80), fill=(35, 25, 45))
    draw.rectangle((460, 240, 500, 380), fill=(255, 220, 150))
    draw.polygon([(480, 210), (455, 245), (505, 245)], fill=(255, 200, 80))
    draw_figure_simple(draw, seated(340, 330, 0.85), SKIN_A, show_pelvis=False)
    draw_figure_simple(draw, seated(620, 330, 0.85), SKIN_B, show_pelvis=False)
    title_label(draw, "Candlelight Gaze")
    save("pic_imagine_candlelight", img)


def gen_imagine_embrace():
    img, draw = new_canvas("Embrace Exercise")
    bed(draw, 400)
    draw_figure_simple(draw, side_lying(400, 370, "right", 0.95), SKIN_A)
    draw_figure_simple(draw, side_lying(480, 370, "left", 0.95), SKIN_B)
    title_label(draw, "Slow Embrace")
    save("pic_imagine_embrace", img)


def gen_imagine_ocean():
    img, draw = new_canvas("Ocean Visualization")
    for row in range(300, 500, 35):
        draw.arc((80, row, W - 80, row + 50), 0, 180, fill=ACCENT, width=3)
    draw_figure_simple(draw, side_lying(380, 380, "right", 0.95), SKIN_A)
    draw_figure_simple(draw, side_lying(520, 380, "left", 0.95), SKIN_B)
    title_label(draw, "Ocean Waves")
    save("pic_imagine_ocean", img)


def gen_imagine_starlight():
    img, draw = new_canvas("Starlight Exercise")
    draw.rectangle((0, 0, W, 220), fill=(30, 25, 55))
    for i in range(20):
        x, y = 50 + i * 45, 40 + (i % 5) * 25
        draw.ellipse((x, y, x + 5, y + 5), fill=(255, 255, 200))
    bed(draw, 400)
    draw_figure_simple(draw, side_lying(380, 380, "right", 0.9), SKIN_A)
    draw_figure_simple(draw, side_lying(520, 380, "left", 0.9), SKIN_B)
    title_label(draw, "Starlit Embrace")
    save("pic_imagine_starlight", img)


def gen_imagine_morning():
    img, draw = new_canvas("Morning Light")
    draw.rectangle((0, 0, W, 200), fill=(255, 235, 200))
    draw.ellipse((760, 40, 880, 160), fill=(255, 220, 100))
    bed(draw, 400)
    draw_figure_simple(draw, side_lying(400, 375, "right", 0.95), SKIN_A)
    draw_figure_simple(draw, side_lying(500, 375, "left", 0.95), SKIN_B)
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
    gen_edu_body_map()
    gen_edu_face_contact()
    gen_edu_hip_pillow()
    gen_edu_consent_talk()
    gen_edu_side_alignment()
    gen_edu_rear_safety()
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
