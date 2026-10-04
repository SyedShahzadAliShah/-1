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
