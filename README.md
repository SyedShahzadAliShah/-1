# CS Lecture Notes — Bilingual Teacher's Study Guide

Android study guide for **Sindh Curriculum Computer Science Class XI & XII**, built from the bilingual teacher's edition lecture-notes PDFs (high-yield ★ golden topics).

## Features

- **Class XI & XII** — six chapters each, aligned to the attached lecture PDFs
- **Bilingual teacher layout** — English and Urdu lecture sections on every chapter screen
- **Cinematic lecture mode** — Ken Burns animation over rendered PDF pages with auto-play and TTS narration
- **Full PDF embedded** — original XI (127 pp) and XII (147 pp) teacher notes in `assets/lecture_notes/`
- **Voice narration** — English or Urdu TTS for overview and per-page lecture text
- **PDF export** — printable chapter summary study guide

## Build assets (after updating source PDFs)

```bash
python3 scripts/build_cs_study_assets.py
```

## Download

**Latest (v1.1.2)** — Embed TTS: **English + Urdu** (both per page), or either language alone. Built-in India Voice 1:

https://github.com/SyedShahzadAliShah/-1/raw/cursor/cs-lecture-notes-studyguide-7efe/releases/CS-Lecture-Notes-StudyGuide-v1.1.2-debug.apk

> Install on Android 7+ (minSdk 24). Allow “Install unknown apps” for your browser or file manager if prompted.

## Build APK

```bash
export ANDROID_HOME=/path/to/android-sdk
./gradlew assembleDebug
```

APK: `app/build/outputs/apk/debug/app-debug.apk` (same as `releases/CS-Lecture-Notes-StudyGuide-v1.0.0-debug.apk`)

## Version 1.0.0

- Initial CS Lecture Notes Study Guide (cinematic + bilingual)
