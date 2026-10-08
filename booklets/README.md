# BIEK Computer Science Lectures

Classroom lecture PDFs for **BIEK Computer Science XI and XII**, aligned to the
Sindh Textbook Board books (New Sindh Curriculum 2024 / National Curriculum 2022–23).

## What you get

- One PDF **per textbook lecture**
- One packed PDF **per chapter** (all lectures in that unit)
- Merged **XI**, **XII**, and **XI+XII** lecture books
- Extra **MCQs / short / long questions** after the book notes
- English explanations with Urdu support, MathJax, and SVG diagrams

## Rebuild

```bash
python3 booklets/build.py                 # default: lecture PDFs + merged books
python3 booklets/build.py lectures xi
python3 booklets/build.py merge           # stitch existing chapter packs only
```

Output: `releases/lectures/xi/`, `releases/lectures/xii/`, and merged files in `releases/`.

Authoring rules for chapter HTML: `AUTHORING.md`.
