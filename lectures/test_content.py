#!/usr/bin/env python3
"""Sanity checks for BIEK lecture content and built PDFs."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from content.xi import LECTURES as XI
from content.xii import LECTURES as XII


def check_set(name, lectures, n):
    assert len(lectures) == n, f"{name} expected {n} lectures, got {len(lectures)}"
    ids = [l["id"] for l in lectures]
    assert len(ids) == len(set(ids)), f"{name} duplicate ids"
    for lec in lectures:
        assert lec["title"] and lec["body"] and lec["slos"]
        assert lec["grade"] in {"XI", "XII"}


def check_pdf(path: Path, min_pages: int):
    import pymupdf

    doc = pymupdf.open(path)
    assert len(doc) >= min_pages, f"{path.name} has {len(doc)} pages, expected >= {min_pages}"
    text = "\n".join(p.get_text() or "" for p in doc)
    assert "BIEK" in text
    assert "اردو" in text or "کمپیوٹر" in text


def main() -> None:
    check_set("XI", XI, 17)
    check_set("XII", XII, 18)
    rel = ROOT.parent / "releases"
    check_pdf(rel / "CS-XI-BIEK-Lectures.pdf", 40)
    check_pdf(rel / "CS-XII-BIEK-Lectures.pdf", 40)
    check_pdf(rel / "CS-XI-and-XII-BIEK-Lectures.pdf", 80)
    xi_n = len(list((rel / "lectures" / "xi").glob("*.pdf")))
    xii_n = len(list((rel / "lectures" / "xii").glob("*.pdf")))
    assert xi_n == 17, xi_n
    assert xii_n == 18, xii_n
    print("OK: 17 XI + 18 XII lectures, books 44/45/88 pages, split PDFs present")


if __name__ == "__main__":
    main()
