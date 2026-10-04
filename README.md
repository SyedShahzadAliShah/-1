# Intimacy Guide + MT-331 Lecture Notes

## MT-331 (v4.0.0) — Cinematic bilingual lecture notes

NED UET **Probability & Statistics (MT-331)** teacher sketchnotes as swipeable **lecture beats** with **Text-to-Speech** in:

- English only
- Urdu only
- **Bilingual** (English then Urdu, auto-advance optional)

The app launcher opens **MT-331 Lecture Notes**. The original intimacy handbook remains available from the overflow menu (MT-331) or **Open intimacy handbook** (handbook → MT-331 lecture notes).

Teacher PDF booklet is bundled at `app/src/main/assets/mt331_teachers_cheatsheet.pdf`.

Browser preview (same beat/TTS idea): open `tools/mt331-lecture-preview.html` in Chrome.

---

Bilingual (English & Urdu) couples sex-education app with embedded diagram pictures, imagination postures, voice narration, and PDF export.

## Download

**Latest (v3.2.1)** — man/woman posture roles + sex education for him & her:

https://github.com/SyedShahzadAliShah/-1/raw/main/releases/IntimacyHandbook-v3.2.1-debug.apk

Branch copy: https://github.com/SyedShahzadAliShah/-1/raw/cursor/couples-posture-guide-ed65/releases/IntimacyHandbook-v3.2.1-debug.apk

> **Important:** Uninstall any older version first, then install v3.2.1. On the home screen you should see **"Version 3.2.1 — Man/Woman roles + Sex Ed for Him & Her"** below the subtitle.

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
