# Cinematic Self-Taught Bootcamp

Android bootcamp for **Sindh Curriculum Computer Science Class XI & XII**, built from the bilingual teacher's edition lecture-notes PDFs (high-yield ★ golden topics). Learn on your own with cinematic lectures, embedded TTS, and bilingual chapter study.

## Features

- **Class XI & XII** — six chapters each, aligned to the bundled teacher PDFs
- **Cinematic lecture mode** — Ken Burns animation over rendered PDF pages with auto-play and TTS narration
- **Self-paced bootcamp** — chapter notes in English and Urdu, golden ★ key points
- **Full PDF embedded** — XI (127 pp) and XII (147 pp) teacher notes in `assets/lecture_notes/`
- **Embed TTS** — English or Urdu male-voice narration per page or full PDF
- **Embedded AI Tutor** — offline Q&amp;A grounded in lecture notes; quiz &amp; ★ golden topics; optional Gemini API key
- **PDF export** — printable chapter summary study guide

## Build assets (after updating source PDFs in uploads)

Place `XI-compressed_*.pdf` and `XII-compressed_*.pdf` in the agent uploads folder, then:

```bash
python3 scripts/build_cs_study_assets.py
```

## Download

**Download (recommended)** — **v1.2.3** stable (same narration as v1.2.2):

https://github.com/SyedShahzadAliShah/-1/raw/cursor/cinematic-self-taught-bootcamp-9c6c/releases/Self-Taught-Bootcamp-v1.2.3-debug.apk

Also: [v1.2.2](https://github.com/SyedShahzadAliShah/-1/raw/cursor/cinematic-self-taught-bootcamp-9c6c/releases/Self-Taught-Bootcamp-v1.2.2-debug.apk). Avoid v1.3.0 if you preferred 1.2.2 — see [DOWNLOAD.md](DOWNLOAD.md).

> Install on Android 7+ (minSdk 24). Uninstall older CS Lecture Notes builds if you had them — this app uses package `com.sindhcs.selftaughtbootcamp`. Allow “Install unknown apps” for your browser or file manager if prompted.

## Build APK

```bash
export ANDROID_HOME=/opt/android-sdk
./gradlew assembleDebug
cp app/build/outputs/apk/debug/app-debug.apk releases/Self-Taught-Bootcamp-v1.1.0-debug.apk
```

## Version 1.3.0

- Skips blank/title PDF pages during embed TTS; live **cinematic captions**; voice status on home screen
- AI Tutor **read reply aloud**; stronger lecture text cleanup; Google TTS fallback engine

## Version 1.2.2

- **TTS fix** — Google engine init corrected; SSML no longer split mid-tag; offline voices preferred; auto-fallback to plain text if SSML fails

## Version 1.2.1

- **Natural-language TTS** — lecture text cleanup, Google neural voice preference, SSML pauses, Urdu punctuation & term expansion
- Install **Google Text-to-speech** + high-quality English & Urdu (Pakistan) voices for best results

## Version 1.2.0

- **Embedded AI Tutor** chat (offline retrieval from XI/XII notes + PDF page index)
- Optional Gemini boost via API key in tutor settings

## Version 1.1.0

- Rebranded as **Cinematic Self-Taught Bootcamp** (from CS Lecture Notes study guide)
- Same cinematic + embed TTS + bilingual content for XI & XII
