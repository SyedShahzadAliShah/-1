# شاندار حرکتیں — Urdu App

Android app based on **Spectacular Sex Moves She'll Never Forget** (Sonia Borg PDF attachment).

## Features (v4.0.0)

- **Urdu only** — concise descriptions for all 30 moves
- **Voice narration** — Urdu TTS (install Urdu voice in system TTS settings)
- **PDF export** — full book or single move, with embedded Urdu font
- **9 categories** — He's on Top, She's on Top, Rear Entry, Sitting & Kneeling, Standing, Side by Side, Oral, Hand Jobs, Moregasms

## Download

Debug APK: `releases/SpectacularMoves-v4.0.0-urdu-debug.apk`

## Build

```bash
python3 scripts/generate_posture_pictures.py
# Set sdk.dir in local.properties, e.g. sdk.dir=/path/to/android-sdk
./gradlew assembleDebug
```

## Version 4.0.0

- Rebuilt from attached PDF book — 30 moves with concise Urdu text
- Removed English UI; RTL layout
- Urdu PDF export with Noto Naskh Arabic font
- Urdu voice narration (no English fallback)
