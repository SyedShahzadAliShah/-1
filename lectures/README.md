# BIEK Computer Science XI & XII — Lecture PDFs

Printed lecture notes for **Board of Intermediate Education, Karachi** Computer Science, aligned to:

- Sindh Curriculum for Computer Science Grades XI–XII (2019)
- BIEK Model Paper 2026 (Paper I theory; Paper II Option I **C** or Option II **Visual Basic**, plus MS Access)

## Download

| Book | File |
| --- | --- |
| Class XI (Paper I) | [`releases/CS-XI-BIEK-Lectures.pdf`](../releases/CS-XI-BIEK-Lectures.pdf) |
| Class XII (Paper II) | [`releases/CS-XII-BIEK-Lectures.pdf`](../releases/CS-XII-BIEK-Lectures.pdf) |
| Combined XI + XII | [`releases/CS-XI-and-XII-BIEK-Lectures.pdf`](../releases/CS-XI-and-XII-BIEK-Lectures.pdf) |

Per-lecture PDFs: `releases/lectures/xi/` and `releases/lectures/xii/`.

## Rebuild

```bash
python3 lectures/build.py          # XI, XII, combined, and per-lecture PDFs
python3 lectures/build.py xi
python3 lectures/build.py xii
```

Requires Google Chrome (headless print). Optional: `pip install pypdf` for PDF merging.

## What is covered

**XI / Paper I:** computer system, IT, hardware, software, virus, memory, motherboard, CPU, registers, fetch cycle, operating system, data communication, media, devices, topologies, OSI/TCP-IP, abbreviations, plus a C++ programming bridge.

**XII / Paper II:** C language (structure through arrays, functions, pointers), OOP/file handling from the Sindh book, Visual Basic (forms, controls, loops, programs), DBMS, ER, normalisation, MS Access + SQL, SDLC, multimedia, wireless/mobile, and two mock papers.
