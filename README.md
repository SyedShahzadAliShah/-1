# Intimacy Handbook — Married Couples Posture Guide (Urdu)

Bilingual intimate sexual postures guide for married couples, based on the [Canva design](https://canva.link/rocr1ea9qir5hez). Opens in **Urdu** by default with **voice narration** and **PDF export**.

## Download

**Latest (v3.2.3)** — Urdu-first married couples posture guide with voice & PDF:

https://github.com/SyedShahzadAliShah/-1/raw/cursor/urdu-married-couples-guide-f316/releases/IntimacyHandbook-v3.2.3-debug.apk

> **Important:** Uninstall any older version first, then install v3.2.3. On the home screen you should see **"Version 3.2.3 — Urdu + Voice + PDF Export"** below the subtitle.

## Features

- **Urdu by default** — app opens in اردو; switch to English from the menu
- **Voice narration (آواز)** — tap **سنیں** on any screen to hear content read aloud in Urdu
- **PDF export** — tap **مکمل ہینڈ بک برآمد** to export the full handbook with embedded Urdu fonts
- **12 intimate postures** with 960×600 educational positioning diagrams (Man/Woman labeled)
- **Man & woman role guidance** for each posture
- **4 foundation chapters** — Communication & Consent, Connection, Comfort & Safety, Exploration
- **Sex education for him & her** — 4 chapters each
- **6 imagination exercises** — visualization to build connection

## Postures Included

| Category | Positions |
|----------|-----------|
| Face to Face | Missionary, Cowgirl |
| Side by Side | Spooning, Side by Side (Facing), Scissors |
| Rear Entry | Rear Entry, Lazy Dog |
| Standing & Seated | Lotus, Standing |
| Variations | Edge of Bed, Reverse Cowgirl, Butterfly |

## Build

```bash
python3 scripts/generate_posture_pictures.py
export ANDROID_HOME=/path/to/android-sdk
./gradlew assembleDebug
cp app/build/outputs/apk/debug/app-debug.apk releases/IntimacyHandbook-v3.2.3-debug.apk
```

## Version 3.2.3

- **Urdu default language** on first launch
- Married couples posture guide branding from Canva design
- Voice narration and PDF export prominently featured
