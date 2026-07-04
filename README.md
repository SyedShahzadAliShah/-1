# Intimacy Guide

Bilingual (English & Urdu) couples sex-education app with embedded diagram pictures, imagination postures, voice narration, PDF export, and a 49-page illustrated book with Urdu narration.

## Download

**Latest (v4.0.0)** — 49-page illustrated sex-ed book with Urdu voice narration:

https://github.com/SyedShahzadAliShah/-1/raw/main/releases/IntimacyHandbook-v4.0.0-debug.apk

> **Important:** Uninstall any older version first, then install v4.0.0. On the home screen you should see **"Version 4.0.0 — Illustrated Book + Urdu Narration"** below the subtitle. Tap the purple **"Illustrated Sex Ed Book"** card to open the 49-page book viewer with swipe navigation and Urdu voice narration per page.

## v4.0.0

- **New:** 49-page illustrated sex-education book viewer (full PDF images from attachment)
- **New:** Swipe / Prev/Next navigation between all 49 pages
- **New:** Per-page Urdu narration — tap **سنیں** (Listen) to hear the page read aloud in Urdu
- **New:** Each page shows Urdu title, English title, full Urdu narration text, and English narration text
- **New:** Prominent entry-card on the home screen for quick access to the book

## v3.2.1

- **Fix:** Sex Education and chapter lists now display correctly inside the scroll view
- **Fix:** Version badge on home screen so you can confirm the correct build is installed

## v3.2.0

- **Man & woman roles** — each posture defines the man's and woman's position and guidance
- **Sex education for him** — 4 chapters on arousal, pleasuring partner, stamina, confidence
- **Sex education for her** — 4 chapters on arousal, pleasure, comfort, confidence
- Diagram labels updated to Man/Woman

## v2.4 fixes

- **PDF export fixed** — proper image loading, multi-page pagination, Urdu font embedding, reliable sharing
- **Upgraded pictures** — 960×600 educational diagrams with Partner A/B labels and position annotations

## Build

```bash
python3 scripts/generate_posture_pictures.py
export ANDROID_HOME=/path/to/android-sdk
./gradlew assembleDebug
```

## Version 3.2.1
