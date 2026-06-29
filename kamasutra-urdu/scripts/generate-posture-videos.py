import math
import os
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw

W, H = 640, 360
FPS = 24
DURATION = 5
FRAMES = FPS * DURATION
OUT_DIR = Path(__file__).resolve().parent.parent / "public" / "videos"
TMP_DIR = Path("/tmp/posture-frames")

BG = (250, 246, 241)
FIGURE = (107, 45, 60)
FIGURE2 = (139, 69, 88)
BED = (232, 213, 196)


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def ease(t: float) -> float:
    return 0.5 - 0.5 * math.cos(t * math.pi * 2)


def base_frame() -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw.ellipse([W // 2 - 200, H - 40, W // 2 + 200, H - 20], fill=BED)
    return img, draw


def draw_head(draw, x, y, r=14):
    draw.ellipse([x - r, y - r, x + r, y + r], outline=FIGURE, width=3)


def draw_limb(draw, x1, y1, x2, y2, color=FIGURE):
    draw.line([x1, y1, x2, y2], fill=color, width=4)


def draw_body(draw, points, color=FIGURE):
    if len(points) >= 2:
        draw.line(points, fill=color, width=5, joint="curve")


def frame_missionary(t: float) -> Image.Image:
    img, draw = base_frame()
    rock = math.sin(t * math.pi * 2) * 4
    # bottom partner
    draw.rounded_rectangle([180, 220, 460, 250], radius=20, outline=FIGURE, width=3)
    draw_head(draw, 220, 205)
    draw_limb(draw, 250, 230, 300, 240)
    draw_limb(draw, 400, 230, 430, 245)
    # top partner
    ty = 175 + rock
    draw_head(draw, 300, ty - 25)
    draw.rounded_rectangle([260, ty, 360, ty + 55], radius=15, outline=FIGURE2, width=3)
    draw_limb(draw, 280, ty + 20, 240, 235)
    draw_limb(draw, 340, ty + 20, 380, 235)
    return img


def frame_spooning(t: float) -> Image.Image:
    img, draw = base_frame()
    sway = math.sin(t * math.pi * 2) * 3
    # front
    draw.rounded_rectangle([200, 225, 420, 255], radius=18, outline=FIGURE, width=3)
    draw_head(draw, 180 + sway, 215)
    # behind
    draw.rounded_rectangle([210, 210, 430, 240], radius=18, outline=FIGURE2, width=3)
    draw_head(draw, 420 + sway, 200)
    draw_limb(draw, 400, 220, 370, 210)
    return img


def frame_lotus(t: float) -> Image.Image:
    img, draw = base_frame()
    bob = math.sin(t * math.pi * 2) * 3
    cx, cy = W // 2, 200 + bob
    draw_head(draw, cx - 35, cy - 50)
    draw_head(draw, cx + 35, cy - 50)
    draw.line([cx - 35, cy - 35, cx - 35, cy + 40], fill=FIGURE, width=4)
    draw.line([cx + 35, cy - 35, cx + 35, cy + 40], fill=FIGURE2, width=4)
    draw.arc([cx - 80, cy + 10, cx - 10, cy + 70], 0, 180, fill=FIGURE, width=3)
    draw.arc([cx + 10, cy + 10, cx + 80, cy + 70], 0, 180, fill=FIGURE2, width=3)
    draw.line([cx - 60, cy + 55, cx + 60, cy + 55], fill=FIGURE, width=3)
    return img


def frame_cowgirl(t: float) -> Image.Image:
    img, draw = base_frame()
    bounce = abs(math.sin(t * math.pi * 2)) * 12
    draw.rounded_rectangle([200, 235, 440, 255], radius=15, outline=FIGURE, width=3)
    draw_head(draw, 230, 220)
    ty = 150 - bounce
    draw_head(draw, 320, ty)
    draw.rounded_rectangle([290, ty + 10, 350, ty + 70], radius=12, outline=FIGURE2, width=3)
    draw_limb(draw, 300, ty + 50, 280, 240)
    draw_limb(draw, 340, ty + 50, 360, 240)
    return img


def frame_side(t: float) -> Image.Image:
    img, draw = base_frame()
    sway = math.sin(t * math.pi * 2) * 2
    draw_head(draw, 250 + sway, 200)
    draw_head(draw, 390 - sway, 200)
    draw.rounded_rectangle([230, 220, 310, 255], radius=12, outline=FIGURE, width=3)
    draw.rounded_rectangle([330, 220, 410, 255], radius=12, outline=FIGURE2, width=3)
    draw.line([300, 235, 340, 235], fill=FIGURE, width=3)
    return img


def frame_standing(t: float) -> Image.Image:
    img, draw = base_frame()
    draw.rectangle([500, 80, 515, 280], fill=(212, 196, 176))
    sway = math.sin(t * math.pi * 2) * 2
    draw_head(draw, 300, 90 + sway)
    draw.line([300, 105, 300, 200], fill=FIGURE, width=4)
    draw.line([300, 130, 260, 170], fill=FIGURE, width=3)
    draw.line([300, 200, 280, 270], fill=FIGURE, width=3)
    draw.line([300, 200, 320, 270], fill=FIGURE, width=3)
    draw_head(draw, 360, 100 - sway)
    draw.line([360, 115, 355, 210], fill=FIGURE2, width=4)
    draw.line([355, 210, 340, 275], fill=FIGURE2, width=3)
    return img


def frame_doggy(t: float) -> Image.Image:
    img, draw = base_frame()
    rock = math.sin(t * math.pi * 2) * 3
    draw.line([120, 250, 350, 230 + rock], fill=FIGURE, width=5)
    draw_head(draw, 100, 235 + rock)
    draw.line([200, 235 + rock, 200, 260], fill=FIGURE, width=3)
    draw.line([300, 232 + rock, 300, 258], fill=FIGURE, width=3)
    draw_head(draw, 420, 220)
    draw.line([400, 235, 370, 240 + rock], fill=FIGURE2, width=4)
    draw.line([420, 235, 420, 270], fill=FIGURE2, width=3)
    return img


def frame_reverse(t: float) -> Image.Image:
    img, draw = base_frame()
    bounce = abs(math.sin(t * math.pi * 2)) * 10
    draw.rounded_rectangle([200, 235, 440, 255], radius=15, outline=FIGURE, width=3)
    draw_head(draw, 230, 220)
    ty = 155 - bounce
    draw.rounded_rectangle([290, ty + 10, 350, ty + 65], radius=12, outline=FIGURE2, width=3)
    draw_head(draw, 320, ty - 5)
    return img


def frame_butterfly(t: float) -> Image.Image:
    img, draw = base_frame()
    pulse = math.sin(t * math.pi * 2) * 5
    draw.rounded_rectangle([200, 240, 440, 258], radius=10, outline=FIGURE, width=3)
    draw_head(draw, 230, 225)
    draw.line([380, 200 - pulse, 360, 240], fill=FIGURE2, width=3)
    draw.line([420, 200 - pulse, 440, 240], fill=FIGURE2, width=3)
    draw_head(draw, 400, 175 - pulse)
    draw.line([390, 190 - pulse, 390, 240], fill=FIGURE2, width=4)
    return img


def frame_yabyum(t: float) -> Image.Image:
    img, draw = base_frame()
    bob = math.sin(t * math.pi * 2) * 2
    cy = 230 + bob
    draw_head(draw, 320, cy - 70)
    draw.line([320, cy - 55, 320, cy], fill=FIGURE, width=4)
    draw.line([300, cy, 340, cy], fill=FIGURE, width=3)
    draw_head(draw, 320, cy - 25)
    draw.line([320, cy - 10, 320, cy + 35], fill=FIGURE2, width=4)
    draw.arc([280, cy + 20, 360, cy + 55], 0, 180, fill=FIGURE2, width=3)
    return img


def frame_scissors(t: float) -> Image.Image:
    img, draw = base_frame()
    sway = math.sin(t * math.pi * 2) * 2
    draw_head(draw, 260 + sway, 195)
    draw_head(draw, 380 - sway, 195)
    draw.rounded_rectangle([240, 220, 310, 255], radius=12, outline=FIGURE, width=3)
    draw.rounded_rectangle([330, 220, 400, 255], radius=12, outline=FIGURE2, width=3)
    draw.line([290, 250, 370, 230], fill=FIGURE, width=4)
    draw.line([310, 230, 350, 250], fill=FIGURE2, width=4)
    return img


def frame_bridge(t: float) -> Image.Image:
    img, draw = base_frame()
    lift = 15 + math.sin(t * math.pi * 2) * 8
    draw.rounded_rectangle([200, 245, 440, 258], radius=8, outline=FIGURE, width=3)
    draw_head(draw, 230, 230)
    # bridge arch
    draw.arc([220, 200 - lift, 420, 260], 180, 360, fill=FIGURE2, width=4)
    draw_head(draw, 320, 175 - lift)
    draw.line([300, 190 - lift, 280, 245], fill=FIGURE2, width=3)
    draw.line([340, 190 - lift, 360, 245], fill=FIGURE2, width=3)
    return img


RENDERERS = {
    "missionary": frame_missionary,
    "spooning": frame_spooning,
    "lotus": frame_lotus,
    "cowgirl": frame_cowgirl,
    "side": frame_side,
    "standing": frame_standing,
    "doggy": frame_doggy,
    "reverse": frame_reverse,
    "butterfly": frame_butterfly,
    "yabyum": frame_yabyum,
    "scissors": frame_scissors,
    "bridge": frame_bridge,
}

POSTURE_IDS = [
    "missionary", "spooning", "lotus", "cowgirl", "side-by-side", "standing",
    "doggy", "reverse-cowgirl", "butterfly", "yab-yum", "scissors", "bridge",
]

ILLUSTRATION_MAP = {
    "side-by-side": "side",
    "reverse-cowgirl": "reverse",
    "yab-yum": "yabyum",
}


def generate_video(posture_id: str, renderer_key: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    frame_dir = TMP_DIR / posture_id
    frame_dir.mkdir(parents=True, exist_ok=True)

    renderer = RENDERERS[renderer_key]
    for i in range(FRAMES):
        t = i / FRAMES
        frame = renderer(t)
        frame.save(frame_dir / f"frame_{i:04d}.png")

    out_path = OUT_DIR / f"{posture_id}.mp4"
    subprocess.run(
        [
            "ffmpeg", "-y", "-framerate", str(FPS),
            "-i", str(frame_dir / "frame_%04d.png"),
            "-c:v", "libx264", "-pix_fmt", "yuv420p",
            "-movflags", "+faststart",
            str(out_path),
        ],
        check=True,
        capture_output=True,
    )
    print(f"Generated {out_path} ({out_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    for pid in POSTURE_IDS:
        key = ILLUSTRATION_MAP.get(pid, pid)
        if key in RENDERERS:
            generate_video(pid, key)
