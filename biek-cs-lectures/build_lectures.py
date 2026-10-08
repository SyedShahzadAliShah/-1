"""Build the Class XI and Class XII lecture PDFs."""

from pathlib import Path

from content import XI_LECTURES, XII_LECTURES
from content.front import XI_CLOSING, XI_FRONT, XII_CLOSING, XII_FRONT
from mathjax_svg import render_formulas
from render_pdf import build_pdf, collect_formulas, install_math

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "pdf"


def book(part, title_lines, header_right, lectures, front, closing, closing_title):
    return {
        "pdf_title": f"BIEK Computer Science {part} lecture notes",
        "pdf_subject": "HSC Computer Science lectures aligned with the Sindh Textbook Board 2024 curriculum",
        "header_left": "BIEK  ·  Computer Science",
        "header_right": header_right,
        "cover": {
            "part": part,
            "title_lines": title_lines,
            "subtitle": "Worked examples, board-style practice, and practicals",
            "session": "Session 2026–27",
            "foot_lines": [
                "Sindh Textbook Board chapter scheme",
                "New Sindh Curriculum of Computer Science 2024",
                "Aligned with the National Curriculum of Pakistan 2022–23",
                "Theory 75 marks   ·   Practical 25 marks",
            ],
        },
        "front": front,
        "lectures": lectures,
        "closing": closing,
        "closing_title": closing_title,
    }


def main():
    xi = book(
        "HSC PART I   ·   CLASS XI",
        ["Computer Science", "Lecture Notes"],
        "Class XI",
        XI_LECTURES,
        XI_FRONT,
        XI_CLOSING,
        "Revision and the practical journal",
    )
    xii = book(
        "HSC PART II   ·   CLASS XII",
        ["Computer Science", "Lecture Notes"],
        "Class XII",
        XII_LECTURES,
        XII_FRONT,
        XII_CLOSING,
        "Revision and the practical journal",
    )
    xi_path = OUT / "BIEK-CS-XI-Lectures.pdf"
    xii_path = OUT / "BIEK-CS-XII-Lectures.pdf"
    formulas = collect_formulas(xi) | collect_formulas(xii)
    install_math(render_formulas(sorted(formulas)))
    build_pdf(xi, xi_path, math_ready=True)
    build_pdf(xii, xii_path, math_ready=True)
    print(xi_path)
    print(xii_path)


if __name__ == "__main__":
    main()
