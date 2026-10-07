# BIEK lecture-wise Study Guides

Computer Science XI and XII study-guide PDFs aligned to the BIEK / Sindh textbook lecture lists.

## What changed versus older extra editions

- One PDF **per textbook lecture**, plus a packed PDF **per chapter**
- Extra **MCQs / short / long questions** after the book notes
- Extra computer pages that were **not in the book TOC** (standalone career lectures) are **dropped**
- MathJax, SVG diagrams, Flexbox cards

## Rebuild

```bash
python3 booklets/build.py                 # default: lecture study guides
python3 booklets/build.py lectures xi
python3 booklets/build.py lectures xii
```

Output: `releases/lectures/xi/` and `releases/lectures/xii/`.

Authoring rules for chapter HTML: `AUTHORING.md`.
