# Intimacy Guide

An educational bilingual Android app (English & Urdu) that helps couples learn intimate postures with illustrated guides, voice narration, and PDF export.

## Features

- **Bilingual** — Full English and Urdu (اردو) support with in-app language switching
- **12 illustrated postures** across 5 categories
- **4 guide chapters** — Communication, Connection, Comfort, Exploration
- **Voice narration** — Text-to-speech reads guide content aloud (English or Urdu)
- **PDF export** — Export the full guide or individual postures with images
- **Step-by-step instructions** with difficulty ratings and comfort tips

## Build the APK

Requirements: Android SDK (API 34), JDK 17+

```bash
export ANDROID_HOME=/path/to/android-sdk
./gradlew assembleDebug
```

APK output: `app/build/outputs/apk/debug/app-debug.apk`

## Install on Device

```bash
adb install app/build/outputs/apk/debug/app-debug.apk
```

## Usage

| Action | How |
|--------|-----|
| Switch language | Toolbar menu → Language → English or اردو |
| Listen | Tap the play icon to hear narration |
| Export PDF | Tap the save icon to create and share a PDF |

## App Info

- **Package:** `com.couplesguide.postures`
- **Version:** 2.0.0
- **Min SDK:** 24 (Android 7.0)
- **Target SDK:** 34

**Note:** Urdu voice narration requires Urdu TTS data installed on the device (Settings → Language → Text-to-speech).
