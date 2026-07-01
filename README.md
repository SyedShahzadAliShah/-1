# Intimacy Guide

Bilingual (English & Urdu) couples sex-education app with **23 embedded posture photos** from the enclosed PDF guide, imagination exercises, voice narration, and PDF export.

## Download

**Latest (v3.6.0)** — all 23 fun positions with PDF photos embedded (censorship removed):

https://github.com/SyedShahzadAliShah/-1/raw/cursor/embed-pdf-posture-photos-466b/releases/IntimacyHandbook-v3.6.0-debug.apk

> **Important:** Uninstall any older version first, then install v3.6.0. On the home screen you should see **"Version 3.6.0 — 23 PDF posture photos embedded"** below the subtitle.

## v3.6.0

- **23 PDF posture photos embedded** — illustrations extracted from the enclosed *Guide to 23 Fun Positions* PDF
- **Censorship removed** — white boxes, black bars, and scribble overlays inpainted with surrounding skin tones
- **Full posture library** — Bicycle, Face to Face, Cowgirl, Spooning, Wheelbarrow, and all 23 positions from the guide
- Man/woman role guidance for every posture (English & Urdu)

## Build

```bash
pip install pymupdf pillow opencv-python-headless
python3 scripts/embed_pdf_postures.py
python3 scripts/generate_posture_pictures.py
export ANDROID_HOME=/path/to/android-sdk
./gradlew assembleDebug
```

Place the source PDF at `uploads/guide-to-23-fun-positions_compress_bc58.pdf` or set `PDF_PATH` when running the embed script.

## Version 3.6.0
