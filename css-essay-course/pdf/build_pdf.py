#!/usr/bin/env python3
"""Build the CSS Essay Grammar Course as a single A4 PDF."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import markdown
from weasyprint import CSS, HTML

ROOT = Path(__file__).resolve().parent.parent
PDF_DIR = Path(__file__).resolve().parent
DEFAULT_OUT = ROOT / "CSS-Essay-Grammar-Course.pdf"

SOURCES: list[tuple[str, Path]] = [
    ("Syllabus", ROOT / "00-SYLLABUS.md"),
    ("Teacher handbook", ROOT / "TEACHER-HANDBOOK.md"),
    ("Formula sheet", ROOT / "FORMULA-SHEET.md"),
    ("How to photocopy", ROOT / "STUDENT-PRINT-PACK.md"),
    ("Session 1 — The CSS sentence", ROOT / "sessions/01-the-css-sentence.md"),
    ("Session 2 — Nouns, pronouns, articles", ROOT / "sessions/02-nouns-pronouns-articles.md"),
    ("Session 3 — Verbs, auxiliaries, modals", ROOT / "sessions/03-verbs-auxiliaries-modals.md"),
    ("Session 4 — Adjectives, adverbs, determiners", ROOT / "sessions/04-adjectives-adverbs-determiners.md"),
    ("Session 5 — Prepositions, conjunctions, connectors", ROOT / "sessions/05-prepositions-conjunctions-connectors.md"),
    ("Session 6 — Present tenses", ROOT / "sessions/06-present-tenses.md"),
    ("Session 7 — Past tenses", ROOT / "sessions/07-past-tenses.md"),
    ("Session 8 — Future and sequence of tenses", ROOT / "sessions/08-future-sequence-of-tenses.md"),
    ("Session 9 — Agreement and sentence architecture", ROOT / "sessions/09-agreement-sentence-architecture.md"),
    ("Session 10 — Active and passive voice", ROOT / "sessions/10-active-passive-voice.md"),
    ("Session 11 — Narration", ROOT / "sessions/11-narration-direct-indirect.md"),
    ("Session 12 — Conditionals", ROOT / "sessions/12-conditionals-hypotheticals.md"),
    ("Session 13 — Punctuation", ROOT / "sessions/13-punctuation-sentence-polish.md"),
    ("Session 14 — Removing errors I", ROOT / "sessions/14-removing-errors-I.md"),
    ("Session 15 — Removing errors II", ROOT / "sessions/15-removing-errors-II.md"),
    ("Session 16 — From grammar to paragraph", ROOT / "sessions/16-from-grammar-to-paragraph.md"),
    ("Session 17 — Capstone mini-essay", ROOT / "sessions/17-capstone-timed-mini-essay.md"),
    ("Diagnostic test", ROOT / "assessments/01-diagnostic.md"),
    ("Mid-course test", ROOT / "assessments/02-mid-course-test.md"),
    ("Final mini-essay rubric", ROOT / "assessments/03-final-mini-essay.md"),
    ("Error log template", ROOT / "assessments/04-error-log-template.md"),
    ("Answer keys", ROOT / "answer-keys/SESSIONS-01-TO-17-KEYS.md"),
]

MD = markdown.Markdown(
    extensions=["tables", "fenced_code", "sane_lists", "smarty", "toc"],
    extension_configs={"toc": {"permalink": False, "toc_depth": "1-3"}},
)


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text).strip("-")
    return text or "section"


def strip_relative_md_links(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        label, href = match.group(1), match.group(2)
        if href.startswith(("http://", "https://", "mailto:")):
            return match.group(0)
        return label

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, text)


def load_markdown(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    text = strip_relative_md_links(text)
    # Avoid accidental setext H1 from underline-only tables/rules colliding with WeasyPrint.
    return text.strip() + "\n"


COVER = """
<div class="cover">
  <p class="cover-kicker">Federal Public Service Commission · CSS Compulsory English</p>
  <h1>Essay Writing for CSS Aspirants</h1>
  <p class="subtitle">A 17-session grammar foundation: from the sentence to a timed mini-essay. Notes for the classroom teacher and the candidate.</p>
  <div class="cover-rule"></div>
  <p class="cover-meta">
    <strong>British English</strong> · 17 × 90-minute sessions<br>
    Parts of speech · Tenses · Voice · Narration · Error removal · Paragraph and essay transfer
  </p>
  <div class="cover-grid">
    <div class="cover-cell"><span class="n">01–05</span><div class="l">The sentence &amp; parts of speech</div></div>
    <div class="cover-cell"><span class="n">06–11</span><div class="l">Tense, agreement, voice, narration</div></div>
    <div class="cover-cell"><span class="n">12–17</span><div class="l">Errors, style, timed writing</div></div>
  </div>
  <div class="cover-foot">
    Teacher + student edition · Print on A4 · Answer keys at the back (release after each attempt)
  </div>
</div>
"""

PARTS = [
    (
        "part-design",
        "Part A — Course design",
        "Syllabus, method, formula sheet, and how to photocopy the pack.",
        0,
        4,
    ),
    (
        "part-sessions",
        "Part B — Seventeen sessions",
        "Teach from the plan; study from the notes. Each class ends in writing.",
        4,
        21,
    ),
    (
        "part-assess",
        "Part C — Tests and keys",
        "Diagnostic, mid-course test, final rubric, error log, then teacher answer keys.",
        21,
        26,
    ),
]


def part_banner(anchor: str, title: str, blurb: str) -> str:
    return (
        f'<section class="part-banner" id="{anchor}">'
        f"<h1>{title}</h1><p>{blurb}</p></section>\n"
    )


def build_html() -> str:
    toc_items: list[str] = []
    body_chunks: list[str] = []
    used_ids: dict[str, int] = {}

    def unique_id(title: str) -> str:
        base = slugify(title)
        n = used_ids.get(base, 0) + 1
        used_ids[base] = n
        return base if n == 1 else f"{base}-{n}"

    for index, (toc_title, path) in enumerate(SOURCES):
        for start_at, banner in [
            (0, PARTS[0]),
            (4, PARTS[1]),
            (21, PARTS[2]),
        ]:
            if index == start_at:
                anchor, title, blurb, *_ = banner
                toc_items.append(
                    f'<li class="l1"><a href="#{anchor}">{title}</a></li>'
                )
                body_chunks.append(part_banner(anchor, title, blurb))

        if not path.is_file():
            raise FileNotFoundError(path)

        md_text = load_markdown(path)
        html = MD.reset().convert(md_text)
        chapter_id = unique_id(toc_title)
        extra_class = " teacher-keys" if path.name == "SESSIONS-01-TO-17-KEYS.md" else ""
        # Make the first h1 keep its page-break; wrap for targeting.
        body_chunks.append(
            f'<section class="chapter{extra_class}" id="{chapter_id}">\n{html}\n</section>\n'
        )
        toc_items.append(f'<li class="l1"><a href="#{chapter_id}">{toc_title}</a></li>')

    toc = (
        '<nav id="toc"><h1>Contents</h1><ul>\n'
        + "\n".join(toc_items)
        + "\n</ul></nav>\n"
    )

    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <title>CSS Essay Grammar Course — 17 Sessions</title>
</head>
<body>
{COVER}
{toc}
{''.join(body_chunks)}
</body>
</html>
"""


def main() -> int:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT
    out.parent.mkdir(parents=True, exist_ok=True)
    html = build_html()
    html_path = PDF_DIR / "_build.html"
    html_path.write_text(html, encoding="utf-8")
    print(f"Wrote HTML {html_path} ({html_path.stat().st_size} bytes)", flush=True)

    HTML(filename=str(html_path), base_url=str(PDF_DIR)).write_pdf(
        str(out),
        stylesheets=[CSS(filename=str(PDF_DIR / "print.css"))],
        presentational_hints=True,
    )
    size_mb = out.stat().st_size / (1024 * 1024)
    print(f"Wrote PDF  {out} ({size_mb:.2f} MB)", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
