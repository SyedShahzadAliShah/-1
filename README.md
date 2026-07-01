# Intimacy Guide

Bilingual (English & Urdu) couples sex-education app rebuilt from the [SheKnows 69 Sex Positions](https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/) slideshow — embedded reference, educational diagrams, voice narration, and PDF export.

## Download

**Latest (v4.0.0)** — 69 SheKnows positions · Urdu/English · Voice · PDF:

https://github.com/SyedShahzadAliShah/-1/raw/cursor/sheknows-embed-urdu-en-e45b/releases/IntimacyHandbook-v4.0.0-debug.apk

## v4.0.0

- **Full SheKnows rebuild** — all 69 positions from the slideshow with bilingual tutorials
- **Embedded SheKnows article** — WebView on home screen + per-posture source reference
- **Educational diagrams** — auto-generated for every position
- **Voice narration** — English & Urdu text-to-speech on home and detail screens
- **PDF export** — single posture or full handbook with Urdu font support
- **13 categories** — Classic, Non-Penetrative, Elevated, Shower, Bondage, Car, Solo, Flat, Blindfold, Anal, Beach, Orgasm, Creative + Imagination

## Build

```bash
pip install Pillow
python3 scripts/generate_sheknows_content.py
./gradlew assembleDebug
```

## Version 4.0.0
