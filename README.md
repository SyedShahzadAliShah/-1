# Intimacy Handbook — Married Couples Posture Guide

Bilingual (English & Urdu) intimate sexual postures guide for married couples, with illustrated positioning photos, man/woman role guidance, sex education chapters, voice narration, and PDF export.

## Download

**Latest (v3.2.2)** — Married couples posture guide with illustrated positioning photos:

https://github.com/SyedShahzadAliShah/-1/raw/main/releases/IntimacyHandbook-v3.2.2-debug.apk

> **Important:** Uninstall any older version first, then install v3.2.2. On the home screen you should see **"Version 3.2.2 — Married Couples Posture Guide with Photos"** below the subtitle.

## Features

- **12 intimate postures** with 960×600 educational positioning diagrams (Man/Woman labeled)
- **Man & woman role guidance** for each posture — position and tips for each partner
- **4 foundation chapters** — Communication & Consent, Connection, Comfort & Safety, Exploration
- **Sex education for him** — 4 chapters on arousal, pleasuring partner, stamina, confidence
- **Sex education for her** — 4 chapters on arousal, pleasure, comfort, confidence
- **6 imagination exercises** — visualization to build connection before physical intimacy
- **Bilingual** — full English and Urdu support
- **Voice narration** — listen to posture and chapter content
- **PDF export** — export individual postures or the full handbook

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
cp app/build/outputs/apk/debug/app-debug.apk releases/IntimacyHandbook-v3.2.2-debug.apk
```

## Version 3.2.2

- Updated branding and copy for married couples focus
- Regenerated all posture positioning diagram photos
