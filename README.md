# CS XI Teach Yourself Edition (Urdish)

Self-study Android app for **Computer Science XI** (Sindh Curriculum 2026). Lectures are **Urdish only** (Urdu with English CS terms), with offline **MathJax SVG**, **inline SVG** diagrams, **Flexbox** RTL layout, and **Urdu TTS**.

## Download

**Latest (v5.0.0-tye)** — خود سیکھو لیکچرز · چھ ابواب · سنہری موضوعات · خود آزمائی:

https://github.com/SyedShahzadAliShah/-1/raw/cursor/cs-xi-teach-yourself-urdish-05c8/releases/CSXI-TeachYourself-Urdish-v5.0.0-tye-debug.apk

Uninstall any older CS XI / handbook APK first. The launcher title is **CS XI خود سیکھو**.

```bash
python3 scripts/generate_ty_curriculum.py
python3 scripts/validate_teach_yourself.py
export ANDROID_HOME=/path/to/android-sdk
./gradlew assembleDebug
```

Web preview: `python3 -m http.server 8765 --directory teach-yourself`

See [teach-yourself/README.md](teach-yourself/README.md).

## Intimacy Guide (previous)

Bilingual (English & Urdu) couples sex-education app with embedded diagram pictures, imagination postures, voice narration, and PDF export.

## Download (handbook archive)

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
