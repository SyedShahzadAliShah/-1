# BIEK lecture-wise Computer Science Study Guides

Printable **lecture-wise Study Guide PDFs** for Board of Intermediate Education Karachi (BIEK) Computer Science **XI** and **XII** (New Sindh Curriculum). Each PDF follows the textbook lecture list.

- **MathJax** for formulae (Boolean algebra, Big O, mean/variance)
- **SVG diagrams** (gates, OSI, stacks/queues, charts)
- **Flexbox** layout (two-column compare cards, extra-practice MCQ cards)
- **Extra MCQs, short and long questions** after the book content
- **Career-only extras** that were not in the book lecture list are removed

## Rebuild

```bash
python3 booklets/build.py              # XI + XII lecture PDFs
python3 booklets/build.py lectures xi  # Grade XI only
```

Needs Google Chrome and the Inter + Noto Naskh Arabic fonts.

## Source

Chapter HTML lives in `booklets/src/xi` and `booklets/src/xii`. Lecture grouping (book TOC) is `booklets/biek_map.py`. Extra board practice is `booklets/extra_practice.py`.
