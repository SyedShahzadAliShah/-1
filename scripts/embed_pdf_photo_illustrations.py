#!/usr/bin/env python3
"""Extract photo illustrations from the uploaded PDF and embed them in the app frame."""
from __future__ import annotations

import io
import os
import urllib.request
from typing import Dict, List, Tuple

import cv2
import fitz
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

PDF_PATH = os.environ.get(
    "PDF_SOURCE",
    "/home/ubuntu/.cursor/projects/workspace/uploads/"
    "spectacular-sex-moves-she-ll-never-forget-ingenious-positions-and-techniques-that-will-blow-her-mind__1___2__6385.pdf",
)
OUT = "/workspace/app/src/main/res/drawable-nodpi"
FACE_MODEL = os.environ.get(
    "FACE_MODEL_PATH",
    os.path.join(os.path.dirname(__file__), "face_detection_yunet_2023mar.onnx"),
)
FACE_MODEL_URL = (
    "https://github.com/opencv/opencv_zoo/raw/main/models/"
    "face_detection_yunet/face_detection_yunet_2023mar.onnx"
)
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

_face_detector: cv2.FaceDetectorYN | None = None


def ensure_face_model() -> str:
    if os.path.isfile(FACE_MODEL):
        return FACE_MODEL
    os.makedirs(os.path.dirname(FACE_MODEL), exist_ok=True)
    print(f"Downloading face model to {FACE_MODEL}...")
    urllib.request.urlretrieve(FACE_MODEL_URL, FACE_MODEL)
    return FACE_MODEL


def _detect_faces(rgb: np.ndarray, scale: float, score_threshold: float) -> List[Tuple[int, int, int, int, float]]:
    h, w = rgb.shape[:2]
    up_w, up_h = int(w * scale), int(h * scale)
    upscaled = cv2.resize(rgb, (up_w, up_h), interpolation=cv2.INTER_CUBIC)

    global _face_detector
    if _face_detector is None:
        ensure_face_model()
        _face_detector = cv2.FaceDetectorYN.create(FACE_MODEL, "", (up_w, up_h))

    _face_detector.setInputSize((up_w, up_h))
    _face_detector.setScoreThreshold(score_threshold)
    _face_detector.setNMSThreshold(0.3)
    _, faces = _face_detector.detect(upscaled)
    if faces is None:
        return []

    found: List[Tuple[int, int, int, int, float]] = []
    for face in faces:
        x = int(face[0] / scale)
        y = int(face[1] / scale)
        fw = int(face[2] / scale)
        fh = int(face[3] / scale)
        score = float(face[14])
        if fw < 12 or fh < 12:
            continue
        if fw > w * 0.55 or fh > h * 0.55:
            continue
        found.append((x, y, fw, fh, score))
    return found


def _merge_face_boxes(
    boxes: List[Tuple[int, int, int, int, float]],
) -> List[Tuple[int, int, int, int]]:
    if not boxes:
        return []

    merged: List[Tuple[int, int, int, int, float]] = []
    for box in sorted(boxes, key=lambda b: b[4] * b[2] * b[3], reverse=True):
        x, y, fw, fh, _ = box
        if x < 0 or y < 0:
            continue
        cx, cy = x + fw / 2, y + fh / 2
        duplicate = False
        for mx, my, mfw, mfh, _ in merged:
            mcx, mcy = mx + mfw / 2, my + mfh / 2
            dist = ((cx - mcx) ** 2 + (cy - mcy) ** 2) ** 0.5
            if dist < min(fw, fh) * 0.6:
                duplicate = True
                break
        if not duplicate:
            merged.append(box)

    return [(x, y, fw, fh) for x, y, fw, fh, _ in merged[:3]]


def find_faces(rgb: np.ndarray) -> List[Tuple[int, int, int, int]]:
    h, w = rgb.shape[:2]
    img_area = h * w
    short_side = min(h, w)
    candidates: List[Tuple[int, int, int, int, float]] = []

    if short_side < 420:
        scales = (2.5, 3.0, 3.5)
        thresholds = (0.28, 0.22, 0.16, 0.10)
    else:
        scales = (1.0, 1.25, 1.5)
        thresholds = (0.35, 0.25, 0.18, 0.12, 0.08)

    for scale in scales:
        for threshold in thresholds:
            candidates.extend(_detect_faces(rgb, scale, threshold))

    # Drop boxes that cover too much of the frame (false positives).
    filtered: List[Tuple[int, int, int, int, float]] = []
    for x, y, fw, fh, score in candidates:
        if x < -fw * 0.1 or y < -fh * 0.1:
            continue
        if fw * fh > img_area * 0.22:
            continue
        filtered.append((max(0, x), max(0, y), fw, fh, score))

    merged = _merge_face_boxes(filtered)
    if len(merged) >= 2:
        return merged[:3]

    # Keep well-separated lower-confidence detections for the second person.
    if merged:
        primary = merged[0]
        pcx = primary[0] + primary[2] / 2
        for x, y, fw, fh, score in sorted(filtered, key=lambda b: b[4], reverse=True):
            cx = x + fw / 2
            if abs(cx - pcx) > w * 0.18 and score >= 0.08:
                merged.append((max(0, x), max(0, y), fw, fh))
                if len(merged) >= 3:
                    break

    return merged[:3]


def _blur_ellipse(img: np.ndarray, x: int, y: int, fw: int, fh: int) -> None:
    h, w = img.shape[:2]
    pad_x = int(fw * 0.55)
    pad_y = int(fh * 0.65)
    x1 = max(0, x - pad_x)
    y1 = max(0, y - pad_y)
    x2 = min(w, x + fw + pad_x)
    y2 = min(h, y + fh + pad_y)
    if x2 <= x1 or y2 <= y1:
        return

    region = img[y1:y2, x1:x2].copy()
    rh, rw = region.shape[:2]
    # Pixelate then blur for strong anonymization.
    tiny_w = max(4, rw // 10)
    tiny_h = max(4, rh // 10)
    pixelated = cv2.resize(
        cv2.resize(region, (tiny_w, tiny_h), interpolation=cv2.INTER_LINEAR),
        (rw, rh),
        interpolation=cv2.INTER_NEAREST,
    )
    k = max(rw, rh)
    k = k if k % 2 == 1 else k + 1
    k = min(max(k, 41), 121)
    blurred = cv2.GaussianBlur(pixelated, (k, k), 0)

    mask = np.zeros((rh, rw), dtype=np.uint8)
    cv2.ellipse(
        mask,
        (rw // 2, rh // 2),
        (max(1, rw // 2 - 2), max(1, rh // 2 - 2)),
        0,
        0,
        360,
        255,
        -1,
    )
    mask = cv2.GaussianBlur(mask, (21, 21), 0)
    alpha = (mask.astype(np.float32) / 255.0)[..., None]
    img[y1:y2, x1:x2] = (
        blurred.astype(np.float32) * alpha + region.astype(np.float32) * (1.0 - alpha)
    ).astype(np.uint8)


def mask_faces(photo: Image.Image) -> Tuple[Image.Image, int]:
    rgb = np.array(photo.convert("RGB"))
    faces = find_faces(rgb)
    for x, y, fw, fh in faces:
        _blur_ellipse(rgb, x, y, fw, fh)

    if len(faces) >= 2:
        ux = min(x for x, _, _, _ in faces)
        uy = min(y for _, y, _, _ in faces)
        ux2 = max(x + fw for x, _, fw, _ in faces)
        uy2 = max(y + fh for _, y, _, fh in faces)
        _blur_ellipse(rgb, ux, uy, ux2 - ux, uy2 - uy)

    return Image.fromarray(rgb), len(faces)


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


def embed_photo(photo: Image.Image, title: str) -> Tuple[Image.Image, int]:
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
    photo, face_count = mask_faces(photo)
    photo = photo.filter(ImageFilter.UnsharpMask(radius=1.2, percent=80, threshold=2))

    px = frame_x + (frame_w - nw) // 2
    py = frame_y + (frame_h - nh) // 2
    canvas.paste(photo, (px, py))
    return canvas, face_count


def generate(name: str, page_num: int, doc: fitz.Document) -> None:
    raw = extract_page_image(doc, page_num)
    photo = crop_photo_region(raw, page_num)
    title = TITLES.get(name, name.replace("pic_", "").replace("_", " ").title())
    result, face_count = embed_photo(photo, title)
    path = os.path.join(OUT, f"{name}.png")
    result.save(path, optimize=True)
    print(f"  {name}.png  <- page {page_num}  ({result.size[0]}x{result.size[1]}, {face_count} faces masked)")


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
