# شاندار حرکتیں — Spectacular Sex Moves (Urdu)

Urdu tutorial app from the attached PDF **"Spectacular Sex Moves She'll Never Forget"** with:

- **Embedded PDF photos** — original move images extracted from the attachment
- **In-depth Urdu tutorials** — concept (تصور), step-by-step method, and why-it-works tips per move
- **Voice narration** — Urdu TTS (listen on home screen or per move)
- **PDF export** — full handbook or single-move PDF with embedded images and Urdu text

## Download

**v4.1.0** — PDF photos embedded + concept-wise Urdu tutorials:

https://github.com/SyedShahzadAliShah/-1/raw/cursor/spectacular-urdu-tutorial-bd0b/releases/SpectacularMoves-v4.1.0-urdu-debug.apk

## v4.1.0

- 30 moves from the attached PDF with **original embedded photos** (`pic_move_01` … `pic_move_30`)
- **Concept-wise Urdu** descriptions: تصور، طریقہ، کیوں مؤثر ہے
- Urdu voice narration + full/single-move PDF export
- 9 categories: وہ اوپر، پیچھے سے، زبانی لطف، انزال تک، وغیرہ

## Build

```bash
# Extract photos from PDF (default path: uploaded attachment)
python3 scripts/embed_spectacular_pdf.py

export ANDROID_HOME=/path/to/android-sdk
./gradlew assembleDebug
```

## Version 4.1.0
