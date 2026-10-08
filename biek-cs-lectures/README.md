# BIEK Computer Science XI and XII lectures

Original classroom lectures for the Board of Intermediate Education Karachi, written to the **Model Paper 2026**.

They are not an official BIEK publication and they do not reproduce a textbook.

## What the 2026 paper actually examines

Paper I (Class XI) is theory: information technology, hardware, the system unit, software, operating systems, data communication, networks and security.

Paper II (Class XII) is one sitting with two options. Choose the option your college taught and do not mix them.

- Option I: Programming Using C
- Option II: Programming Using Visual Basic 6
- Database questions (DBMS, keys, data models, MS Access, SQL) are inside both options

A later Sindh curriculum introduces C++. That is not the paper printed in the 2026 model papers, so these notes do not teach it.

## PDFs

| File | Contents |
| --- | --- |
| `pdf/BIEK-CS-XI-Lectures.pdf` | Class XI, 9 lectures |
| `pdf/BIEK-CS-XII-Lectures.pdf` | Class XII, 15 lectures |
| `pdf/XI/` | One PDF per Class XI lecture |
| `pdf/XII/` | One PDF per Class XII lecture |

Each lecture has outcomes, worked explanations, exam tips, a checkpoint in the style of Sections A–C, and model answers.

## Rebuild

```bash
python3 -m pip install -r requirements.txt
python3 build_lectures.py
```

Needs Liberation Sans and DejaVu Sans Mono, which are the fonts used in the PDFs.
