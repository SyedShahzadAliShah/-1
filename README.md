# Teach Yourself Sketchnotes

Ultimate teaching APK for **Computer Science XI & XII** (Sindh curriculum). Every lesson is a sketchnote: Flexbox cards, SVG diagrams, MathJax formulas, and **Urdish TTS** (English technical terms inside Urdu explanation, with the voice switching at each script change).

## What’s inside

- **Sketchnote Studio** — visual vocabulary, Flexbox layout engine, Urdish voice, MathJax, SVG, board-exam method
- **CS XI** — Computer Systems, Computational Thinking, Python, Data & Analysis, Impacts of Computing, Digital Literacy + recap/mock
- **CS XII** — HCI, Algorithms & Data Structures, Python structures/files, Data Analysis, AI/Security, Digital Entrepreneurship + recap/mock
- Offline **MathJax 3** (`tex-svg`) and vector **SVG** diagrams
- Progress ticks stored on-device

## Build

```bash
python3 tools/build_content.py
bash tools/fetch_mathjax.sh
export ANDROID_HOME=/path/to/android-sdk
./gradlew assembleDebug
```

The debug APK is copied to `releases/TeachYourselfSketchnotes-v1.0.0-debug.apk`.

## Tests

```bash
python3 tools/build_content.py
python3 tests/test_curriculum.py
node tests/js/urdish.test.js
```

Open `app/src/main/assets/www/index.html` in a browser (or serve the `www` folder) to walk the sketchnotes with the Web Speech API when Android TTS is not present.
