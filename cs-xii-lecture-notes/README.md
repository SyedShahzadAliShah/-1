# CS XII — Cinematic Self-Taught Lecture Notes (Ultimate Edition)

Interactive **bilingual** lecture notes for Sindh **Computer Science XII** (all 6 chapters from the uploaded teacher’s PDF), designed for students who are reluctant or overwhelmed.

## Features

- **Cinematic UI** — scene-based scrolling “lecture cinema” with golden-topic badges
- **TTS (English & Urdu only)** — Web Speech API; no other languages exposed
- **Embedded SVG diagrams** — HCI, algorithms, Python, data, ML, entrepreneurship
- **MathJax** — renders `\(O(n)\)`, `\(O(n^2)\)`, etc. in scene text
- **Reluctant-learner path** — filter **★ Golden only**, auto-lecture, **Mark win ✓** progress (localStorage)

## Run locally

```bash
cd cs-xii-lecture-notes
python3 -m http.server 8765
```

Open `http://localhost:8765/` (ES modules require a local server).

## Rebuild content from PDF

Place the teacher PDF at `../uploads/` or edit the path in `scripts/build_lecture_data.py`, then:

```bash
# Extract once (requires pymupdf) — chapters_raw.json is committed after first extract
python3 scripts/build_lecture_data.py
```

## Structure

- `data/chapters.json` — processed scenes (227 scenes, 35 golden)
- `js/diagrams.js` — inline SVG library
- `js/tts.js` — English/Urdu narration
- `js/app.js` — UI, progress, MathJax typeset

## Android APK

Module **`cs-xii-app`** wraps the web lecture notes in a WebView (offline scenes + diagrams; **MathJax** loads from CDN when online).

**Download (debug build):** `releases/CS-XII-Lecture-Cinema-v1.0.2-debug.apk`

Direct link (use this if GitHub shows “Page not found”):

https://raw.githubusercontent.com/SyedShahzadAliShah/-1/cursor/cs-xii-lecture-notes-1978/releases/CS-XII-Lecture-Cinema-v1.0.2-debug.apk

**Important:** Uninstall any older CS XII Lecture Cinema APK, then install **v1.0.2** (fixes WebView “Page not found”).

```bash
export ANDROID_HOME=$HOME/android-sdk   # or your SDK path
./gradlew :cs-xii-app:assembleDebug
```

Install on device: enable “Install unknown apps”, open the APK. Use **English / Urdu** TTS buttons inside the app (device TTS engines).
