# BIEK Computer Science XI & XII lectures (PDF)

Original classroom lecture notes for **Board of Intermediate Education, Karachi** Computer Science (HSC Part-I and Part-II).

| File | Who it is for |
| --- | --- |
| `BIEK_CS_XI_Lectures.pdf` | Class XI / CS Paper-I |
| `BIEK_CS_XII_Lectures.pdf` | Class XII / CS Paper-II (C, Visual Basic, and 2019 units) |

## What is covered

**XI** follows Sindh Curriculum 2019 Grade XI (computer system, memory, system unit, OS, C++, arrays/strings/structures, networks) and the extra Paper-I topics BIEK still asks: number systems, Boolean algebra, data security.

**XII** includes:

- Option I — Programming using C (current BIEK Paper-II option)
- Option II — Visual Basic
- 2019 Grade XII units — SDLC, pointers, OOP, file handling, database/SQL, multimedia, wireless

Each volume has definitions, comparison tables, programs, board-style MCQs, short questions, long questions, and the official lab activity lists.

These notes are **not** a scan or reconstruction of any commercial textbook.

## Rebuild

```bash
python3 -m pip install reportlab
python3 biek-cs-lectures/generate.py
```
