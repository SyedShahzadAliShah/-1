# BIEK Computer Science XI & XII Lectures (PDF)

Original exam-oriented lecture notes for the Board of Intermediate Education, Karachi.

These PDFs are **not** an official BIEK publication and are **not** a copy of any Sindh Textbook Board book. They follow the topics and paper pattern of **Computer Science Paper–I and Paper–II (Model Paper 2026)**.

## Files

| PDF | What it covers |
| --- | --- |
| `output/BIEK_CS_XI_Lectures.pdf` | Class XI / Paper–I theory: IT, hardware, memory, CPU & registers, software, OS, data communication, networks & OSI, security, Boolean revision, solved 2026 paper |
| `output/BIEK_CS_XII_Lectures.pdf` | Class XII / Paper–II: Option I (C), DBMS & MS-Access, Option II (Visual Basic), practical programs, solved 2026 paper |

Paper–II still has two independent options: **Programming Using C** or **Programming Using Visual Basic**. Both options also ask DBMS / MS-Access.

## Rebuild

```bash
python3 -m pip install -r requirements.txt
python3 generate_lectures.py
```

PDFs are written to `output/`.
