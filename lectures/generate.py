"""Generate the Class XI and Class XII lecture PDFs."""

from pathlib import Path

from lectures.pdf_builder import build_pdf
from lectures.xi_content import UNITS as XI_UNITS
from lectures.xii_content import UNITS as XII_UNITS

OUT = Path(__file__).resolve().parent / "pdf"

PREFACE = (
    "These lectures are written for Higher Secondary students taking Computer Science "
    "with the Board of Intermediate Education Karachi. They follow the Sindh Curriculum "
    "of Computer Science 2024, which is aligned with the National Curriculum of Pakistan "
    "2022–23 and with the Sindh Textbook Board books for the 2026–27 session. "
    "Each lecture is one teaching block: the idea, a worked example, and a short checkpoint "
    "in the style of the HSSC paper. Python programs that are complete scripts show the "
    "output produced by running them on Python 3."
)


def meta_for(grade: str, units: list[dict]) -> dict:
    label = f"Class {grade}"
    return {
        "title": f"BIEK Computer Science {label} Lectures",
        "subject": f"Computer Science {label} lecture notes",
        "grade_label": label,
        "cover_lines": ["Lecture notes", "Computer Science"],
        "alignment": "Sindh Curriculum 2024  ·  National Curriculum of Pakistan 2022–23",
        "footer": f"BIEK Computer Science  ·  {label}  ·  Lecture notes",
        "preface": PREFACE,
        "units": [
            {"code": unit["code"], "title": unit["title"], "weight": unit["weight"]}
            for unit in units
        ],
    }


def main() -> None:
    xi = OUT / "BIEK-Computer-Science-XI-Lectures.pdf"
    xii = OUT / "BIEK-Computer-Science-XII-Lectures.pdf"
    build_pdf(xi, meta_for("XI", XI_UNITS), XI_UNITS)
    build_pdf(xii, meta_for("XII", XII_UNITS), XII_UNITS)
    print(xi)
    print(xii)


if __name__ == "__main__":
    main()
