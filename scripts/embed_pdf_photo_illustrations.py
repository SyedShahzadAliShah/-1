#!/usr/bin/env python3
"""Extract photo illustrations from the uploaded PDF and embed them in the app frame."""
from __future__ import annotations

import io
import os
from typing import Dict, Optional, Tuple

import fitz
from PIL import Image, ImageDraw, ImageFilter

PDF_PATH = os.environ.get(
    "PDF_SOURCE",
    "/home/ubuntu/.cursor/projects/workspace/uploads/"
    "spectacular-sex-moves-she-ll-never-forget-ingenious-positions-and-techniques-that-will-blow-her-mind__1___2__6385.pdf",
)
OUT = "/workspace/app/src/main/res/drawable-nodpi"
W, H = 1280, 800

BG = (252, 246, 238)
BG2 = (238, 226, 212)
PRIMARY = (78, 52, 42)
SECONDARY = (138, 100, 80)
LABEL_BG = (255, 252, 248)

# page number -> drawable name; pages chosen to best match each posture/topic
PAGE_MAP: Dict[str, int] = {
    "pic_missionary": 11,
    "pic_cowgirl": 33,
    "pic_spooning": 29,
    "pic_side_by_side": 87,
    "pic_doggy": 41,
    "pic_lotus": 15,
    "pic_standing": 50,
    "pic_edge_bed": 105,
    "pic_reverse_cowgirl": 68,
    "pic_butterfly": 94,
    "pic_scissors": 90,
    "pic_lazy_dog": 70,
    "pic_guide_cover": 1,
    "pic_chapter_consent": 113,
    "pic_chapter_connection": 7,
    "pic_chapter_comfort": 15,
    "pic_chapter_explore": 19,
    "pic_edu_face_contact": 11,
    "pic_edu_side_alignment": 87,
    "pic_edu_rear_safety": 41,
    "pic_edu_hip_pillow": 94,
    "pic_edu_body_map": 68,
    "pic_edu_consent_talk": 113,
    "pic_imagine_breath": 7,
    "pic_imagine_candlelight": 15,
    "pic_imagine_embrace": 81,
    "pic_imagine_ocean": 87,
    "pic_imagine_starlight": 29,
    "pic_imagine_morning": 5,
}

TITLES: Dict[str, str] = {
    "pic_missionary": "Missionary",
    "pic_cowgirl": "Cowgirl",
    "pic_spooning": "Spooning",
    "pic_side_by_side": "Side by Side",
    "pic_doggy": "Rear Entry",
    "pic_lotus": "Lotus",
    "pic_standing": "Standing",
    "pic_edge_bed": "Edge of Bed",
    "pic_reverse_cowgirl": "Reverse Cowgirl",
    "pic_butterfly": "Butterfly",
    "pic_scissors": "Scissors",
    "pic_lazy_dog": "Lazy Dog",
    "pic_guide_cover": "Intimacy Handbook",
    "pic_chapter_consent": "Consent & Communication",
    "pic_chapter_connection": "Connection",
    "pic_chapter_comfort": "Comfort",
    "pic_chapter_explore": "Explore Together",
    "pic_edu_face_contact": "Face Contact",
    "pic_edu_side_alignment": "Side Alignment",
    "pic_edu_rear_safety": "Rear Safety",
    "pic_edu_hip_pillow": "Hip Support",
    "pic_edu_body_map": "Body Awareness",
    "pic_edu_consent_talk": "Consent Talk",
    "pic_imagine_breath": "Shared Breath",
    "pic_imagine_candlelight": "Candlelight",
    "pic_imagine_embrace": "Warm Embrace",
    "pic_imagine_ocean": "Open Air",
    "pic_imagine_starlight": "Soft Light",
    "pic_imagine_morning": "Morning Light",
}

# Multi-panel pages: use left half of photo region
MULTI_PANEL_PAGES = {18, 25, 35, 44, 90}


def extract_page_image(doc: fitz.Document, page_num: int) -> Image.Image:
    page = doc[page_num - 1]
    imgs = page.get_images()
    if not imgs:
        raise ValueError(f"No image on page {page_num}")
    xref = imgs[0][0]
    pix = fitz.Pixmap(doc, xref)
    if pix.n - pix.alpha > 3:
        pix = fitz.Pixmap(fitz.csRGB, pix)
    return Image.open(io.BytesIO(pix.tobytes("png")))


def crop_photo_region(img: Image.Image, page_num: int) -> Image.Image:
    w, h = img.size
    top = int(h * 0.045)
    bottom = int(h * 0.54) if page_num != 1 else int(h * 0.62)
    photo = img.crop((0, top, w, bottom))

    if page_num in MULTI_PANEL_PAGES:
        pw, ph = photo.size
        photo = photo.crop((0, 0, pw // 2, ph))
    elif page_num == 1:
        # Cover: use top photo portion only
        pw, ph = photo.size
        photo = photo.crop((0, 0, pw, int(ph * 0.72)))
    return photo


def embed_photo(photo: Image.Image, title: str) -> Image.Image:
    canvas = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(canvas, "RGBA")

    for row in range(H):
        t = row / H
        r = int(BG[0] * (1 - t) + BG2[0] * t)
        g = int(BG[1] * (1 - t) + BG2[1] * t)
        b = int(BG[2] * (1 - t) + BG2[2] * t)
        draw.line([(0, row), (W, row)], fill=(r, g, b))

    draw.rounded_rectangle((12, 12, W - 12, H - 12), radius=14, outline=SECONDARY, width=2)
    draw.rounded_rectangle((18, 18, W - 18, 56), radius=8, fill=(*LABEL_BG, 230), outline=SECONDARY, width=1)
    draw.text((30, 28), title, fill=SECONDARY)
    draw.text((30, 46), "Educational photo illustration", fill=PRIMARY)

    frame_x, frame_y = 40, 72
    frame_w, frame_h = W - 80, H - 112
    draw.rounded_rectangle(
        (frame_x - 2, frame_y - 2, frame_x + frame_w + 2, frame_y + frame_h + 2),
        radius=10,
        fill=(220, 210, 200),
        outline=SECONDARY,
        width=1,
    )

    photo = photo.convert("RGB")
    pw, ph = photo.size
    scale = min(frame_w / pw, frame_h / ph)
    nw, nh = int(pw * scale), int(ph * scale)
    photo = photo.resize((nw, nh), Image.LANCZOS)
    photo = photo.filter(ImageFilter.UnsharpMask(radius=1.2, percent=80, threshold=2))

    px = frame_x + (frame_w - nw) // 2
    py = frame_y + (frame_h - nh) // 2
    canvas.paste(photo, (px, py))
    return canvas


def generate(name: str, page_num: int, doc: fitz.Document) -> None:
    raw = extract_page_image(doc, page_num)
    photo = crop_photo_region(raw, page_num)
    title = TITLES.get(name, name.replace("pic_", "").replace("_", " ").title())
    result = embed_photo(photo, title)
    path = os.path.join(OUT, f"{name}.png")
    result.save(path, optimize=True)
    print(f"  {name}.png  <- page {page_num}  ({result.size[0]}x{result.size[1]})")


def main() -> None:
    if not os.path.isfile(PDF_PATH):
        raise SystemExit(f"PDF not found: {PDF_PATH}")
    os.makedirs(OUT, exist_ok=True)
    doc = fitz.open(PDF_PATH)
    print(f"Embedding {len(PAGE_MAP)} photo illustrations from {doc.page_count}-page PDF...")
    for name, page_num in PAGE_MAP.items():
        generate(name, page_num, doc)
    doc.close()
    print("done")


if __name__ == "__main__":
    main()
