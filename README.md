# Intimacy Guide

Bilingual (English & Urdu) couples sex-education app — **100% SheKnows article photos**, no stick figures.

## Download

**Latest (v4.2.0)** — all screens use SheKnows illustrations:

https://github.com/SyedShahzadAliShah/-1/raw/cursor/sheknows-embed-urdu-en-e45b/releases/IntimacyHandbook-v4.2.0-debug.apk

## v4.2.0

- **Zero stick figures** — removed all generated figure diagrams
- **69 position photos** from SheKnows article
- **13 category header images** from SheKnows sections
- **Edu cards, guide chapters, imagination exercises** — mapped to relevant SheKnows photos
- **Guide cover** — SheKnows bucket-list hero image
- Image layouts use `fitCenter` so full illustrations are visible

## Build

```bash
pip install Pillow beautifulsoup4
python3 scripts/download_sheknows_images.py
python3 scripts/generate_sheknows_content.py
./gradlew assembleDebug
```

## Version 4.2.0
