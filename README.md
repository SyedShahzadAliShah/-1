# CS XII خود پڑھو — Teach Yourself Edition

Urdish-only self-study lectures for Sindh Computer Science XII, chapters 1–6 (HCI, algorithms, Python, data analysis, computing impacts, digital entrepreneurship). The teacher’s bilingual notes are not copied; each lecture is written for a student, with English technical terms inside Urdu sentences.

The debug APK embeds, and does not download:

- MathJax 3 `tex-svg` (formulas become SVG inside the app)
- SVG figures for stacks, trees, Big O, neurons, and the prototype cycle
- Flexbox layout for the reader
- Text-to-speech that alternates an Urdu voice and an English voice

There is no internet permission. If the phone has no Urdu voice, the player links to the system TTS settings.

**APK:** [releases/CSXII-TeachYourself-v1.0.0-debug.apk](releases/CSXII-TeachYourself-v1.0.0-debug.apk)

```bash
python3 scripts/build_urdish_lectures.py
export ANDROID_HOME=$HOME/android-sdk
./gradlew :teach:assembleDebug
```

# Intimacy Guide

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
