# Intimacy Guide

An educational bilingual Android app (English & Urdu) that helps couples learn intimate postures with **embedded picture diagrams**, voice narration, and PDF export.

## Features

- **Bilingual** — Full English and Urdu (اردو) support with in-app language switching
- **Picture diagrams** — 17 embedded PNG illustrations for all postures, chapters, and cover
- **12 illustrated postures** across 5 categories
- **4 guide chapters** — Communication, Connection, Comfort, Exploration
- **Voice narration** — Text-to-speech reads guide content aloud (English or Urdu)
- **PDF export** — Export the full guide or individual postures with images
- **Gentle motion** — Subtle breathing animation on all pictures

## Regenerate pictures

```bash
python3 scripts/generate_posture_pictures.py
```

Output: `app/src/main/res/drawable-nodpi/pic_*.png`

## Build the APK

```bash
export ANDROID_HOME=/path/to/android-sdk
./gradlew assembleDebug
```

## Download

https://github.com/SyedShahzadAliShah/-1/raw/cursor/couples-posture-guide-de33/releases/IntimacyGuide-v2.2-debug.apk

## App Info

- **Package:** `com.couplesguide.postures`
- **Version:** 2.2.0
- **Min SDK:** 24 (Android 7.0)
