# Intimacy Guide

Bilingual (English & Urdu) couples sex-education app with embedded photo illustrations, imagination postures, voice narration, and PDF export.

## Download

**Latest (v4.0.0)** — embedded photo illustrations from the uploaded guide:

https://github.com/SyedShahzadAliShah/-1/raw/cursor/embed-photo-illustrations-5144/releases/IntimacyHandbook-v4.0.0-debug.apk

> **Important:** Uninstall any older version first, then install v4.0.0. On the home screen you should see **"Version 4.0.0 — Embedded photo illustrations + Man/Woman roles"** below the subtitle.

## v4.0.0

- **Embedded photo illustrations** — all 12 postures, chapters, education cards, and imagination exercises use real photo illustrations extracted from the uploaded guide PDF
- **1280×800 framed assets** — each photo is cropped and placed in an educational frame with posture title
- **Regeneration script** — `scripts/embed_pdf_photo_illustrations.py` rebuilds all drawable assets from the source PDF

## v3.2.1

- **Fix:** Sex Education and chapter lists now display correctly inside the scroll view
- **Fix:** Version badge on home screen so you can confirm the correct build is installed

## v3.2.0

- **Man & woman roles** — each posture defines the man's and woman's position and guidance
- **Sex education for him** — 4 chapters on arousal, pleasuring partner, stamina, confidence
- **Sex education for her** — 4 chapters on arousal, pleasure, comfort, confidence
- Diagram labels updated to Man/Woman

## Build

```bash
pip install pymupdf pillow
python3 scripts/embed_pdf_photo_illustrations.py
export ANDROID_HOME=/path/to/android-sdk
./gradlew assembleDebug
```

To regenerate diagram-style illustrations instead:

```bash
python3 scripts/generate_posture_pictures.py
```

## Version 4.0.0
