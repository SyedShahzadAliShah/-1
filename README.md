# BIEK Computer Science XI & XII Lectures (PDF)

Classroom lecture notes for **Board of Intermediate Education, Karachi (BIEK)**
Computer Science Class XI and Class XII. Content follows the Sindh Textbook Board
books (New Sindh Curriculum 2024, aligned with the National Curriculum of Pakistan
2022–23). Language is English with Urdu support.

These notes are original teaching material. They are **not** a scan or copy of the
STBB textbook.

## Download the lecture books

Use the `raw.githubusercontent.com` links (they save the PDF):

- **Class XI** — `releases/CS-XI-BIEK-Lectures.pdf`
- **Class XII** — `releases/CS-XII-BIEK-Lectures.pdf`
- **XI + XII complete** — `releases/CS-XI-and-XII-BIEK-Lectures.pdf`

Per-lecture and per-chapter PDFs live in `releases/lectures/` (see
`releases/lectures/README.md` after a rebuild). Zips:

- `releases/CS-XI-BIEK-Lectures.zip`
- `releases/CS-XII-BIEK-Lectures.zip`

## Syllabus map

**Class XI**

1. Computer Systems — digital logic, SDLC, OSI / TCP/IP
2. Computational Thinking & Algorithms
3. Programming Fundamentals (Python)
4. Data and Analysis (databases / MS Access)
5. Application and Impacts of Computing
6. Digital Literacy
7. Final revision and mock paper

**Class XII**

1. Computer Systems (Human–Computer Interaction)
2. Computational Thinking & Algorithms (correctness, efficiency, data structures)
3. Programming Fundamentals (Python collections, functions, files)
4. Data and Analysis (SQLite, Pandas, visualisation)
5. Application and Impacts of Computing (ML, security, collaboration)
6. Entrepreneurship in the Digital Age
7. Final revision and mock paper

## Rebuild

```bash
python3 -m pip install --user pymupdf
python3 booklets/build.py lectures
```

Requires Google Chrome (headless print) and Python 3.10+.
