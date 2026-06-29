# قربت کی تعلیم — Intimacy Education APK

An **18+ Android educational app** for couples, inspired by Kamasutra posture traditions. Content is in **Urdu** with **Text-to-Speech (TTS)** narration and **PDF export** for offline study.

## Features

- **18+ age verification** gate on first launch
- **12 practical intimacy postures** with Urdu descriptions, benefits, and tips
- **Educational SVG illustrations** for each posture (diagram-style, tasteful)
- **Embedded video clips** — animated posture demonstrations for every position (bundled MP4, plays offline)
- **Urdu TTS** — listen to full posture guides or individual sections (uses device Urdu voice on Android)
- **PDF export** — single posture or complete guidebook download
- **RTL Urdu UI** with Noto Nastaliq Urdu typography
- **Category filters**: بنیادی، متوازن، گہری قربت، آرام دہ

## APK Download

Pre-built debug APK:

```
releases/qurbat-ki-taleem-debug.apk
```

Install on Android 7.0+ (API 24+). Enable "Install from unknown sources" if sideloading.

## Build from Source

### Prerequisites

- Node.js 18+
- Java JDK 17+
- Android SDK (API 36, build-tools 35+)

### Web + Sync

```bash
cd kamasutra-urdu
npm install
npm run videos:generate   # optional: regenerate posture demo clips
npm run build
npx cap sync android
```

### Android APK

```bash
# Set SDK path in android/local.properties:
# sdk.dir=/path/to/android-sdk

cd android
./gradlew assembleDebug
```

APK output: `android/app/build/outputs/apk/debug/app-debug.apk`

Release build:

```bash
./gradlew assembleRelease
```

## Project Structure

```
kamasutra-urdu/
├── src/
│   ├── components/     # AgeGate, PostureCard, PostureDetail, Illustrations
│   ├── data/           # Urdu posture content + SVG strings
│   └── services/       # TTS and PDF export
├── android/            # Capacitor Android native project
└── releases/           # Pre-built APK (at repo root)
```

## Tech Stack

- **React + TypeScript + Vite** — UI
- **Capacitor 8** — native Android wrapper
- **@capacitor-community/text-to-speech** — Urdu TTS on device
- **jsPDF** — PDF generation with embedded illustrations

## Educational Disclaimer

This app provides **sex education material for consenting adult couples only**. All content emphasizes mutual respect, consent, safety, and communication. It is not medical advice — consult a healthcare provider for specific concerns.

## License

Educational use. Content illustrations are original SVG diagrams, not reproductions of historical artwork.
