# Cinematic Self-Taught Bootcamp

Android bootcamp for **Sindh Curriculum Computer Science Class XI & XII**, built from the bilingual teacher's edition lecture-notes PDFs (high-yield ★ golden topics). Learn on your own with cinematic lectures, embedded TTS, and bilingual chapter study.

## Features

- **Class XI & XII** — six chapters each, aligned to the bundled teacher PDFs
- **Cinematic lecture mode** — Ken Burns animation over rendered PDF pages with auto-play and TTS narration
- **Self-paced bootcamp** — chapter notes in English and Urdu, golden ★ key points
- **Full PDF embedded** — XI (127 pp) and XII (147 pp) teacher notes in `assets/lecture_notes/`
- **Embed TTS** — English or Urdu male-voice narration per page or full PDF
- **PDF export** — printable chapter summary study guide

## Build assets (after updating source PDFs in uploads)

Place `XI-compressed_*.pdf` and `XII-compressed_*.pdf` in the agent uploads folder, then:

```bash
python3 scripts/build_cs_study_assets.py
```

## Download

**Latest (v1.1.0)** — Cinematic Self-Taught Bootcamp:

https://github.com/SyedShahzadAliShah/-1/raw/cursor/cinematic-self-taught-bootcamp-9c6c/releases/Self-Taught-Bootcamp-v1.1.0-debug.apk

> Install on Android 7+ (minSdk 24). Uninstall older CS Lecture Notes builds if you had them — this app uses package `com.sindhcs.selftaughtbootcamp`. Allow “Install unknown apps” for your browser or file manager if prompted.

## Build APK

```bash
export ANDROID_HOME=/opt/android-sdk
./gradlew assembleDebug
cp app/build/outputs/apk/debug/app-debug.apk releases/Self-Taught-Bootcamp-v1.1.0-debug.apk
```

## Version 1.1.0

- Rebranded as **Cinematic Self-Taught Bootcamp** (from CS Lecture Notes study guide)
- Same cinematic + embed TTS + bilingual content for XI & XII
