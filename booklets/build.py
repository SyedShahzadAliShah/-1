#!/usr/bin/env python3
"""Assemble the Teach Yourself booklets from HTML fragments and print them to PDF.

Usage: python3 booklets/build.py [xi|xii ...]
"""
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
OUT = ROOT / "output"
CSS = (ROOT / "assets" / "booklet.css").as_uri()
CHROME = "google-chrome"

BOOKS = {
    "xi": {
        "grade": "XI",
        "title": "Computer Science XI",
        "urdu": "کمپیوٹر سائنس — گیارہویں جماعت: خود سیکھیں، خود پرکھیں",
        "curriculum": "New Sindh Curriculum 2026",
        "file": "CS-XI-Ultimate-Teach-Yourself-Booklet.pdf",
    },
    "xii": {
        "grade": "XII",
        "title": "Computer Science XII",
        "urdu": "کمپیوٹر سائنس — بارہویں جماعت: خود سیکھیں، خود پرکھیں",
        "curriculum": "New Sindh Curriculum 2025-27",
        "file": "CS-XII-Ultimate-Teach-Yourself-Booklet.pdf",
    },
}


def chapter_meta(fragment: str):
    num = re.search(r'data-num="(\d+)"', fragment)
    title = re.search(r'data-title="([^"]+)"', fragment)
    topics = re.findall(r'<h2[^>]*>(.*?)</h2>', fragment, flags=re.S)
    clean = []
    for t in topics:
        t = re.sub(r"<[^>]+>", "", t)
        t = html.unescape(t).replace("★ Golden", "").replace("★", "").strip()
        low = t.lower()
        skip = (
            low.startswith(("chapter review", "key terms", "practice", "answer",
                            "self-assessment", "chapter summary"))
            or re.match(r"chapter \d+ review", low)
        )
        if t and not skip:
            clean.append(t)
    return int(num.group(1)), html.unescape(title.group(1)), clean


def cover(book, chapters):
    units = "".join(
        f"<div><b>{n:02d}</b>{html.escape(t)}</div>" for n, t, _ in chapters
    )
    return f"""
<section class="cover">
  <div class="grade">{book['grade']}</div>
  <span class="tag">ULTIMATE TEACH YOURSELF BOOKLET</span>
  <h1>{book['title']}</h1>
  <p class="sub">Learn every chapter on your own &mdash; explanations, worked examples,
  memory tricks, practice questions and full answer keys.</p>
  <p class="sub">Bilingual support: English + اردو</p>
  <div class="ur">{book['urdu']}</div>
  <div class="units">{units}</div>
  <div class="foot">Based on the Bilingual Teacher's Edition lecture notes &middot; {book['curriculum']} &middot;
  ★ marks Golden (high-yield) exam topics.</div>
</section>"""


def contents(chapters, has_final):
    items = []
    for n, t, topics in chapters:
        sub = "".join(f"<li>{html.escape(x)}</li>" for x in topics)
        items.append(f'<li><b>Chapter {n}:</b> {html.escape(t)}<ul>{sub}</ul></li>')
    if has_final:
        items.append("<li><b>Final Revision:</b> one-page summaries, mock paper and answers</li>")
    return f"""
<section class="front">
  <h1>Contents</h1>
  <ol class="toc">{''.join(items)}</ol>
</section>"""


def build(key):
    book = BOOKS[key]
    folder = SRC / key
    frags = sorted(folder.glob("ch*.html"), key=lambda p: int(re.search(r"\d+", p.stem).group()))
    chapters_html, chapters = [], []
    for f in frags:
        text = f.read_text(encoding="utf-8")
        chapters.append(chapter_meta(text))
        chapters_html.append(text)
    intro = (SRC / "how-to-use.html").read_text(encoding="utf-8")
    final_path = folder / "final.html"
    final = final_path.read_text(encoding="utf-8") if final_path.exists() else ""

    doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>{book['title']} &mdash; Ultimate Teach Yourself Booklet</title>
<link rel="stylesheet" href="{CSS}">
</head><body>
{cover(book, chapters)}
{contents(chapters, bool(final))}
{intro}
{''.join(chapters_html)}
{final}
</body></html>"""
    OUT.mkdir(exist_ok=True)
    html_path = OUT / f"{key}.html"
    html_path.write_text(doc, encoding="utf-8")
    pdf_path = OUT / book["file"]
    with tempfile.TemporaryDirectory() as profile:
        print_pdf(html_path, pdf_path, profile)
    print(f"{key}: {len(frags)} chapters -> {pdf_path}")


def print_pdf(html_path, pdf_path, profile):
    subprocess.run(
        [
            CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
            f"--user-data-dir={profile}", "--no-first-run", "--disable-extensions",
            "--no-pdf-header-footer",
            "--run-all-compositor-stages-before-draw",
            "--virtual-time-budget=60000",
            f"--print-to-pdf={pdf_path}", html_path.as_uri(),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        timeout=600,
    )


if __name__ == "__main__":
    for k in sys.argv[1:] or list(BOOKS):
        build(k)
