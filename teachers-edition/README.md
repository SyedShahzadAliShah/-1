# Computer Science XI – Bilingual Teacher's Edition (Android)

Android app built from `source/XI_8518.pdf` (Computer Science XI, 6 chapters, 127 pages).

* **Text on screen: English** – every page is re-flowed into readable cards (headings, paragraphs, bullets, call-outs, table rows, code, diagrams).
* **Vocals in Urdu** – every block and table row has a pre-recorded neural Urdu narration (about 3 hours in total, stored offline in the APK). Tap any card to start narration from there, or use the play button to read a whole page; narration can auto-advance to the next page and plays at 0.75x - 1.5x.
* **Page layout view** – the original page rendering with the Urdu text removed (English only) for diagrams, gate symbols, K-maps, etc.; pinch to zoom.
* Chapter/page browser with search, "★ Golden topic" marks, and "continue where you left off".

## Install

Download `releases/CS-XI-Teachers-Edition-v1.0.apk` and open it on an Android 7.0+ phone/tablet (allow "install unknown apps" for your file manager/browser).

## How it is built

```
source/XI_8518.pdf
  tools/extract_pdf.py      English text lines + Urdu-free page renders (assets/pages/*.webp)
  content/pNNN.json         authored per-page content: English text + Urdu narration script (see tools/AUTHORING.md)
  tools/validate_content.py checks English against the PDF and Urdu script
  tools/build_assets.py     neural Urdu TTS (edge-tts, ur-PK-UzmaNeural) -> Opus/Ogg + index.json
app/                        Kotlin app (View-based, minSdk 24)
```

Rebuild:

```bash
pip install pymupdf pillow edge-tts          # ffmpeg with libopus is also required
python3 tools/extract_pdf.py                 # (needs work/extract + page images)
python3 tools/validate_content.py
python3 tools/build_assets.py                # synthesises missing audio, writes app assets
export ANDROID_HOME=/path/to/android-sdk
./gradlew assembleRelease                    # release signing uses keystore/release.jks if present
```
