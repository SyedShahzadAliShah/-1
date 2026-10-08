#!/usr/bin/env python3
"""Generate BIEK CS XI and XII lecture PDFs."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from content_xi import fill_xi
from content_xii import fill_xii
from engine import build_pdf

HERE = Path(__file__).resolve().parent
OUT_XI = HERE / "BIEK_CS_XI_Lectures.pdf"
OUT_XII = HERE / "BIEK_CS_XII_Lectures.pdf"


def main() -> None:
    print("Building Class XI …")
    build_pdf(
        str(OUT_XI),
        "BIEK  ·  Computer Science XI",
        "HSC Part-I lectures",
        fill_xi,
        cover={
            "kicker": "COMPLETE CLASSROOM LECTURES  ·  HSC PART-I",
            "title": "Computer Science XI",
            "subtitle": "Original notes for Karachi Board (BIEK)",
            "bullets": [
                "Sindh Curriculum 2019 Grade XI units 1–7 with board weightages",
                "Extra Paper-I topics: number systems, Boolean algebra, data security",
                "C++ programming, arrays, strings, structures, and lab journal list",
                "Paper pattern (75 theory + 25 practical) and a full model paper",
                "Definitions, comparison tables, programs, MCQs, short and long questions",
            ],
            "footer": "Independently written teaching notes aligned to the public Sindh Curriculum 2019 and BIEK’s published paper scheme. Not a photocopy of any textbook.",
        },
    )
    print("  wrote", OUT_XI, "bytes", OUT_XI.stat().st_size)

    print("Building Class XII …")
    build_pdf(
        str(OUT_XII),
        "BIEK  ·  Computer Science XII",
        "HSC Part-II lectures",
        fill_xii,
        cover={
            "kicker": "COMPLETE CLASSROOM LECTURES  ·  HSC PART-II",
            "title": "Computer Science XII",
            "subtitle": "Option I (C)  ·  Option II (VB)  ·  2019 units",
            "bullets": [
                "Part A — Programming using C (BIEK Option I, Turbo C++ style)",
                "Part B — Visual Basic (BIEK Option II, event-driven board topics)",
                "Part C — SDLC, pointers, OOP, files, database/SQL, multimedia, wireless",
                "Practical journal list from the Sindh Curriculum 2019",
                "Model MCQs, short questions and 8-mark long questions",
            ],
            "footer": "Independently written teaching notes aligned to BIEK Option I/II papers and the public Sindh Curriculum 2019. Not a photocopy of any textbook.",
        },
    )
    print("  wrote", OUT_XII, "bytes", OUT_XII.stat().st_size)


if __name__ == "__main__":
    main()
