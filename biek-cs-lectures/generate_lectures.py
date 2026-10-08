#!/usr/bin/env python3
"""Build BIEK CS XI and XII lecture PDFs."""

from pathlib import Path

from content_xi import build_xi
from content_xii import build_xii
from pdf_engine import LectureBuilder

OUT = Path(__file__).resolve().parent / "output"


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    xi = LectureBuilder(
        "BIEK Computer Science  ·  Class XI Lectures",
        "Paper–I  ·  Theory",
    )
    build_xi(xi)
    xi_path = OUT / "BIEK_CS_XI_Lectures.pdf"
    xi.build(xi_path)

    xii = LectureBuilder(
        "BIEK Computer Science  ·  Class XII Lectures",
        "Paper–II  ·  C / VB / DBMS",
    )
    build_xii(xii)
    xii_path = OUT / "BIEK_CS_XII_Lectures.pdf"
    xii.build(xii_path)

    print(f"Wrote {xi_path} ({xi_path.stat().st_size // 1024} KB)")
    print(f"Wrote {xii_path} ({xii_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
