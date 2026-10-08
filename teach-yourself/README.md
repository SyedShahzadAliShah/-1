# CS XI Teach Yourself Edition (Urdish)

Self-study lectures for **Computer Science XI** (Sindh Curriculum 2026), rewritten from the bilingual teacher's notes into a student **خود سیکھو** course.

- Lectures in **Urdish only** (Urdu prose with English CS terms: AND, OSI, SDLC, K-map)
- **MathJax SVG** bundled offline (`vendor/mathjax/tex-svg-full.js`)
- **Inline SVG** diagrams
- **Flexbox** RTL layout
- **TTS** Urdu via Android `TextToSpeech` (Web Speech fallback in Chrome)

## Preview

```bash
python3 scripts/generate_ty_curriculum.py
python3 -m http.server 8765 --directory teach-yourself
```

Open `http://127.0.0.1:8765/`.

## Validate

```bash
python3 scripts/validate_teach_yourself.py
```
