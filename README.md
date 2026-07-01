# Intimacy Guide

Bilingual (English & Urdu) couples sex-education app rebuilt from the [SheKnows 69 Sex Positions](https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/) slideshow — **real SheKnows article images**, embedded reference, voice narration, and PDF export.

## Download

**Latest (v4.1.0)** — SheKnows article photos · Urdu/English · Voice · PDF:

https://github.com/SyedShahzadAliShah/-1/raw/cursor/sheknows-embed-urdu-en-e45b/releases/IntimacyHandbook-v4.1.0-debug.apk

## v4.1.0

- **Real SheKnows images** — all 69 position illustrations downloaded from the article (replaces generated figure diagrams)
- **Article cover** — home screen uses the SheKnows bucket-list hero image

## v4.0.0

- **Full SheKnows rebuild** — all 69 positions with bilingual tutorials
- **Embedded SheKnows article** — WebView on home screen
- **Voice narration** and **PDF export**

## Build

```bash
pip install Pillow beautifulsoup4
python3 scripts/download_sheknows_images.py   # fetch article photos
python3 scripts/generate_sheknows_content.py  # Kotlin data + edu assets
./gradlew assembleDebug
```

## Version 4.1.0
