#!/usr/bin/env python3
"""Build BIEK CS XI / XII lecture PDFs with headless Chrome."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from render import cover_page, document, render_lecture, toc_page

OUT_REL = ROOT.parent / "releases"
OUT_LEC = OUT_REL / "lectures"
BUILD = ROOT / ".build"


def chrome() -> str:
    for c in ("google-chrome", "google-chrome-stable", "chromium"):
        p = shutil.which(c)
        if p:
            return p
    raise SystemExit("Google Chrome is required to print PDFs")


def html_to_pdf(html_path: Path, pdf_path: Path) -> None:
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    if pdf_path.exists():
        pdf_path.unlink()
    udir = Path(tempfile.mkdtemp(prefix="chrome-pdf-"))
    cmd = [
        chrome(),
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--no-first-run",
        "--disable-extensions",
        "--disable-dev-shm-usage",
        "--disable-background-networking",
        "--disable-sync",
        "--disable-default-apps",
        "--no-default-browser-check",
        "--no-pdf-header-footer",
        "--allow-file-access-from-files",
        "--virtual-time-budget=8000",
        f"--user-data-dir={udir}",
        f"--crash-dumps-dir={udir / 'crashes'}",
        f"--print-to-pdf={pdf_path}",
        html_path.resolve().as_uri(),
    ]
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )
    deadline = time.time() + 40
    last_size = -1
    stable = 0
    try:
        while time.time() < deadline:
            if pdf_path.exists():
                size = pdf_path.stat().st_size
                if size > 1500 and size == last_size:
                    stable += 1
                    if stable >= 4:
                        break
                else:
                    stable = 0
                last_size = size
            elif proc.poll() is not None:
                break
            time.sleep(0.2)
    finally:
        if proc.poll() is None:
            try:
                os.killpg(proc.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
            try:
                proc.wait(timeout=4)
            except subprocess.TimeoutExpired:
                try:
                    os.killpg(proc.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                proc.wait()
        shutil.rmtree(udir, ignore_errors=True)
    if not pdf_path.exists() or pdf_path.stat().st_size < 1000:
        raise SystemExit(f"PDF not written: {pdf_path}")


def slug(text: str) -> str:
    s = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-")
    return s[:70]


def write_book(grade: str, lectures: list[dict], pdf_name: str, cover_extra: str) -> Path:
    parts = [cover_page(grade, cover_extra), toc_page(lectures)]
    for i, lec in enumerate(lectures, 1):
        parts.append(render_lecture(lec, i))
    html = document(f"BIEK CS {grade} Lectures", "".join(parts))
    BUILD.mkdir(parents=True, exist_ok=True)
    html_path = BUILD / f"CS-{grade.replace('+','-')}-lectures.html"
    html_path.write_text(html, encoding="utf-8")
    pdf_path = OUT_REL / pdf_name
    html_to_pdf(html_path, pdf_path)
    return pdf_path


def write_splits(grade: str, lectures: list[dict], folder: Path) -> list[Path]:
    folder.mkdir(parents=True, exist_ok=True)
    paths = []
    for i, lec in enumerate(lectures, 1):
        html = document(
            lec["title"],
            render_lecture(lec, i),
        )
        html_path = BUILD / f"{grade}-{i:02d}.html"
        html_path.write_text(html, encoding="utf-8")
        pdf = folder / f"CS-{grade}-Lecture-{i:02d}-{slug(lec['title'])}.pdf"
        html_to_pdf(html_path, pdf)
        paths.append(pdf)
    return paths


def merge_pdfs(inputs: list[Path], output: Path) -> None:
    try:
        from pypdf import PdfWriter
    except ImportError:
        subprocess.check_call(["pip", "install", "-q", "pypdf"])
        from pypdf import PdfWriter
    w = PdfWriter()
    for p in inputs:
        w.append(str(p))
    output.parent.mkdir(parents=True, exist_ok=True)
    w.write(str(output))
    w.close()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("what", nargs="?", default="all", choices=["all", "xi", "xii", "merge"])
    args = ap.parse_args()

    from content.xi import LECTURES as XI
    from content.xii import LECTURES as XII

    xi_extra = """<table>
    <tr><td>Paper</td><td>Computer Science Paper I · 75 marks · 3 hours</td></tr>
    <tr><td>Section A</td><td>15 MCQs · 15 marks · OMR</td></tr>
    <tr><td>Section B</td><td>Short answers · 30 marks</td></tr>
    <tr><td>Section C</td><td>Detailed answers · 30 marks · diagrams required</td></tr>
    <tr><td>Units</td><td>Computer system, memory, system unit, OS, networks &amp; data communication, plus Sindh programming bridge</td></tr>
    </table>"""
    xii_extra = """<table>
    <tr><td>Paper</td><td>Computer Science Paper II · 75 marks · choose ONE option</td></tr>
    <tr><td>Option I</td><td>Programming using C + Database / MS Access</td></tr>
    <tr><td>Option II</td><td>Programming using Visual Basic + Database / MS Access</td></tr>
    <tr><td>Also covered</td><td>Pointers, OOP (C++), file handling, SDLC, multimedia, wireless — Sindh Grade XII units</td></tr>
    </table>"""

    made = []
    if args.what in {"all", "xi"}:
        p = write_book("XI", XI, "CS-XI-BIEK-Lectures.pdf", xi_extra)
        write_splits("XI", XI, OUT_LEC / "xi")
        made.append(p)
    if args.what in {"all", "xii"}:
        p = write_book("XII", XII, "CS-XII-BIEK-Lectures.pdf", xii_extra)
        write_splits("XII", XII, OUT_LEC / "xii")
        made.append(p)
    if args.what in {"all", "merge"}:
        xi_pdf = OUT_REL / "CS-XI-BIEK-Lectures.pdf"
        xii_pdf = OUT_REL / "CS-XII-BIEK-Lectures.pdf"
        both_extra = xi_extra + xii_extra
        combo = write_book("XI+XII", XI + XII, "CS-XI-and-XII-BIEK-Lectures.pdf", both_extra)
        made.append(combo)
        # keep merge helper available if combo HTML is huge
        if not combo.exists() and xi_pdf.exists() and xii_pdf.exists():
            merge_pdfs([xi_pdf, xii_pdf], OUT_REL / "CS-XI-and-XII-BIEK-Lectures.pdf")

    print("Wrote:")
    for p in made:
        print(" ", p, p.stat().st_size if p.exists() else "missing")


if __name__ == "__main__":
    main()
