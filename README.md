# Intimacy Guide

An educational bilingual Android app (English & Urdu) with embedded picture diagrams, **imagination postures**, fixed voice narration, and PDF export.

## Features

- **Bilingual** — English and Urdu (اردو) with in-app language switching
- **Imagination Postures** — 6 educational visualization exercises (breath, candlelight, embrace, ocean, starlight, morning)
- **12 physical postures** with embedded PNG pictures
- **4 guide chapters** — consent, connection, comfort, exploration
- **Voice narration** — chunked TTS with Urdu/English locale fallbacks
- **PDF export** — full guide including imagination and physical sections

## Download

https://github.com/SyedShahzadAliShah/-1/raw/cursor/couples-posture-guide-de33/releases/IntimacyGuide-v2.3-debug.apk

## Build

```bash
python3 scripts/generate_posture_pictures.py
export ANDROID_HOME=/path/to/android-sdk
./gradlew assembleDebug
```

## Version 2.3.0
