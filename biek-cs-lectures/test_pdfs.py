#!/usr/bin/env python3
"""Smoke test: generated lecture PDFs exist, have content, and match the 2026 paper."""

from pathlib import Path

from pypdf import PdfReader

OUT = Path(__file__).resolve().parent / "output"

CHECKS = [
    (
        "BIEK_CS_XI_Lectures.pdf",
        30,
        [
            "Operating System",
            "OSI",
            "Fetch",
            "Hardcopy",
            "Gateway",
            "1024 MB",
            "Model Paper 2026",
        ],
    ),
    (
        "BIEK_CS_XII_Lectures.pdf",
        30,
        [
            "Dennis Ritchie",
            "scanf",
            "Primary key",
            "MS-Access",
            "Visual Basic",
            "factorial",
            "Model Paper 2026",
        ],
    ),
]


def main():
    failures = []
    for name, min_pages, needles in CHECKS:
        path = OUT / name
        if not path.exists():
            failures.append(f"missing {name}")
            continue
        reader = PdfReader(str(path))
        pages = len(reader.pages)
        if pages < min_pages:
            failures.append(f"{name} has {pages} pages, expected >= {min_pages}")
        text = "\n".join((p.extract_text() or "") for p in reader.pages)
        for n in needles:
            if n not in text:
                failures.append(f"{name} missing phrase: {n}")
        print(f"OK {name}: {pages} pages, {path.stat().st_size // 1024} KB")
    if failures:
        raise SystemExit("FAIL:\n" + "\n".join(failures))
    print("All smoke checks passed.")


if __name__ == "__main__":
    main()
