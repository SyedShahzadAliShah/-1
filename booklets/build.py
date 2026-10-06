#!/usr/bin/env python3
"""Assemble Teach Yourself booklets and standalone lecture PDFs.

Usage:
  python3 booklets/build.py              # full booklets (xi + xii)
  python3 booklets/build.py xi           # Grade XI booklet
  python3 booklets/build.py lectures     # chapter + topic lecture PDFs
  python3 booklets/build.py lectures xi  # Grade XI lectures only
  python3 booklets/build.py editions     # Student's Edition + Teacher's Edition
  python3 booklets/build.py all          # booklets + lectures + editions
"""
from __future__ import annotations

import html
import re
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
OUT = ROOT / "output"
RELEASES = ROOT.parent / "releases" / "lectures"
CSS = (ROOT / "assets" / "booklet.css").as_uri()
FIT = (ROOT / "assets" / "fit-pages.js").as_uri()
CHROME = "google-chrome"
BRANCH = "cursor/teach-yourself-lectures-pdf-339e"
RAW = f"https://github.com/SyedShahzadAliShah/-1/raw/{BRANCH}/releases/lectures"
ZIP_RAW = f"https://github.com/SyedShahzadAliShah/-1/raw/{BRANCH}/releases"

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

DIV_OPEN = re.compile(r"<div\b", re.I)
DIV_CLOSE = re.compile(r"</div>", re.I)
SECTION_OPEN = re.compile(r"<section\b", re.I)
SECTION_CLOSE = re.compile(r"</section>", re.I)


def unescape(text: str) -> str:
    return html.unescape(text)


def strip_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text)


def chapter_meta(fragment: str):
    num = re.search(r'data-num="(\d+)"', fragment)
    title = re.search(r'data-title="([^"]+)"', fragment)
    topics = re.findall(r"<h2[^>]*>(.*?)</h2>", fragment, flags=re.S)
    clean = []
    for t in topics:
        t = unescape(strip_tags(t)).replace("★ Golden", "").replace("★", "").strip()
        low = t.lower()
        skip = (
            low.startswith(("chapter review", "key terms", "practice", "answer",
                            "self-assessment", "chapter summary"))
            or re.match(r"chapter \d+ review", low)
        )
        if t and not skip:
            clean.append(t)
    return int(num.group(1)), unescape(title.group(1)), clean


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


def wrap_html(title: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="{CSS}">
</head><body>
{body}
<script src="{FIT}"></script>
</body></html>"""


def extract_balanced(html_text: str, start: int, open_re: re.Pattern, close_re: re.Pattern) -> str:
    first = open_re.search(html_text, start)
    if not first:
        return ""
    pos = first.end()
    depth = 1
    while pos < len(html_text) and depth:
        nxt_open = open_re.search(html_text, pos)
        nxt_close = close_re.search(html_text, pos)
        if not nxt_close:
            return html_text[start:]
        if nxt_open and nxt_open.start() < nxt_close.start():
            depth += 1
            pos = nxt_open.end()
        else:
            depth -= 1
            pos = nxt_close.end()
    return html_text[start:pos]


def extract_class_divs(html_text: str, class_name: str) -> list[str]:
    blocks = []
    for m in re.finditer(rf'<div\s+class="{re.escape(class_name)}">', html_text):
        blocks.append(extract_balanced(html_text, m.start(), DIV_OPEN, DIV_CLOSE))
    return blocks


def extract_review(fragment: str) -> str:
    m = re.search(r'<section\s+class="review">', fragment)
    if not m:
        return ""
    return extract_balanced(fragment, m.start(), SECTION_OPEN, SECTION_CLOSE)


def extract_opener(fragment: str) -> str:
    first_topic = fragment.find('<div class="topic">')
    review = fragment.find('<section class="review">')
    end = first_topic if first_topic != -1 else (review if review != -1 else len(fragment))
    head = fragment[:end]
    # Drop the outer <section ...> opening tag; keep opener + objectives.
    head = re.sub(r"^<section[^>]*>", "", head, count=1).strip()
    return head


def topic_title(block: str) -> str:
    m = re.search(r"<h2[^>]*>(.*?)</h2>", block, flags=re.S)
    raw = unescape(strip_tags(m.group(1))) if m else "Untitled"
    return re.sub(r"\s+", " ", raw).strip()


def topic_is_golden(title: str, block: str) -> bool:
    return "★" in title or 'class="star"' in block[:800]


def topic_urdu(block: str) -> str:
    m = re.search(r'<p class="ur">(.*?)</p>', block, flags=re.S)
    if not m:
        return ""
    return unescape(strip_tags(m.group(1))).strip()


def slugify(title: str) -> str:
    t = unescape(title).replace("★ Golden", "").replace("★", "")
    t = t.replace("–", "-").replace("—", "-")
    t = re.sub(r"[^\w\s.\-]+", "", t, flags=re.UNICODE)
    t = re.sub(r"\s+", "-", t.strip())
    t = re.sub(r"-{2,}", "-", t)
    return t[:72].strip("-._") or "lecture"


def print_pdf(html_path: Path, pdf_path: Path, profile: Path, min_bytes: int = 12_000, budget_ms: int = 45000):
    pdf_path = Path(pdf_path)
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    if pdf_path.exists():
        pdf_path.unlink()
    proc = subprocess.Popen(
        [
            CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
            f"--user-data-dir={profile}", "--no-first-run", "--disable-extensions",
            "--no-pdf-header-footer",
            "--run-all-compositor-stages-before-draw",
            f"--virtual-time-budget={budget_ms}",
            f"--print-to-pdf={pdf_path}", html_path.as_uri(),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    last_size, stable = -1, 0
    tries = max(40, budget_ms // 1000 + 15)
    for _ in range(tries):
        time.sleep(1.2)
        if not pdf_path.exists():
            if proc.poll() is not None:
                raise RuntimeError(f"Chrome exited {proc.returncode} without writing {pdf_path}")
            continue
        size = pdf_path.stat().st_size
        if size > min_bytes and size == last_size:
            stable += 1
            if stable >= 2:
                break
        else:
            stable = 0
            last_size = size
    else:
        proc.terminate()
        try:
            proc.wait(timeout=8)
        except subprocess.TimeoutExpired:
            proc.kill()
        raise RuntimeError(f"Timed out waiting for {pdf_path}")
    if proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=12)
        except subprocess.TimeoutExpired:
            proc.kill()
    if pdf_path.stat().st_size < min_bytes:
        raise RuntimeError(f"PDF too small: {pdf_path.stat().st_size} bytes ({pdf_path})")


def print_job(html_text: str, html_path: Path, pdf_path: Path, min_bytes: int, budget_ms: int):
    html_path.parent.mkdir(parents=True, exist_ok=True)
    html_path.write_text(html_text, encoding="utf-8")
    last_err = None
    for attempt in range(2):
        with tempfile.TemporaryDirectory(prefix="chrome-pdf-", ignore_cleanup_errors=True) as profile:
            try:
                print_pdf(html_path, pdf_path, Path(profile), min_bytes=min_bytes, budget_ms=budget_ms)
                return pdf_path
            except Exception as exc:
                last_err = exc
                time.sleep(1.5)
    raise last_err


def build_booklet(key: str):
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

    doc = wrap_html(
        f"{book['title']} — Ultimate Teach Yourself Booklet",
        cover(book, chapters) + contents(chapters, bool(final)) + intro + "".join(chapters_html) + final,
    )
    OUT.mkdir(exist_ok=True)
    html_path = OUT / f"{key}.html"
    pdf_path = OUT / book["file"]
    print_job(doc, html_path, pdf_path, min_bytes=50_000, budget_ms=120000)
    dest = ROOT.parent / "releases" / book["file"]
    dest.parent.mkdir(exist_ok=True)
    shutil.copy2(pdf_path, dest)
    all_in_one = ROOT.parent / "releases" / f"CS-{book['grade']}-Teach-Yourself-All-in-One.pdf"
    shutil.copy2(pdf_path, all_in_one)
    print(f"{key} booklet: {len(frags)} chapters -> {pdf_path}")
    print(f"{key} all-in-one -> {all_in_one}")


def merge_complete(keys: list[str]):
    """Stitch grade all-in-one PDFs into one XI+XII complete file when pymupdf is available."""
    try:
        import pymupdf
    except ImportError:
        print("skip XI+XII complete merge (pymupdf not installed)")
        return
    releases = ROOT.parent / "releases"
    srcs = [releases / f"CS-{BOOKS[k]['grade']}-Teach-Yourself-All-in-One.pdf" for k in keys]
    srcs = [p for p in srcs if p.exists()]
    if len(srcs) < 2:
        return
    dest = releases / "CS-XI-and-XII-Teach-Yourself-Complete.pdf"
    out = pymupdf.open()
    for p in srcs:
        out.insert_file(p)
    dest.parent.mkdir(exist_ok=True)
    out.save(dest, deflate=True, garbage=3)
    pages = out.page_count
    out.close()
    print(f"complete XI+XII -> {dest} ({pages} pages)")


def section_open_tag(fragment: str) -> str:
    m = re.search(r"<section[^>]*>", fragment)
    return m.group(0) if m else '<section class="chapter">'


def first_sentence(text: str) -> str:
    text = re.sub(r"\s+", " ", unescape(strip_tags(text))).strip()
    if not text:
        return ""
    parts = re.split(r"(?<=[.!?۔])\s+", text)
    return (parts[0] if parts else text).strip()


def box_inner(block: str, kind: str) -> str:
    m = re.search(rf'<div class="box {re.escape(kind)}">(.*?)</div>', block, flags=re.S)
    return m.group(1) if m else ""


def check_prompts(block: str) -> list[str]:
    m = re.search(r'<div class="box check">(.*?)<div class="ans">', block, flags=re.S)
    if not m:
        return []
    found = re.findall(r"<p><b>\d+\.</b>\s*(.*?)</p>", m.group(1), flags=re.S)
    return [unescape(strip_tags(q)).strip() for q in found if strip_tags(q).strip()]


def studentize_fragment(fragment: str) -> str:
    opener = extract_opener(fragment)
    topics = extract_class_divs(fragment, "topic")
    review = extract_review(fragment)
    open_tag = section_open_tag(fragment)
    items = []
    new_topics = []
    for block in topics:
        title = re.sub(r"\s*★.*", "", topic_title(block)).strip()
        ans_m = re.search(r'<div class="ans">(.*?)</div>', block, flags=re.S)
        if ans_m:
            items.append(f"<li><b>{html.escape(title)}.</b> {ans_m.group(1).strip()}</li>")
            block = (
                block[: ans_m.start()]
                + '<div class="ans write-here">Write your answers in your notebook. '
                "Check the Answer key at the end of this chapter.</div>"
                + block[ans_m.end() :]
            )
        new_topics.append(block)
    check_key = ""
    if items:
        check_key = f'<h3>Check yourself — answers</h3><ol class="check-key">{"".join(items)}</ol>'
    seal = (
        '<div class="answers-seal"><p><b>Answer key.</b> Finish the practice first, then mark your work. '
        "Do not peek while you are still answering.</p>"
        '<p class="ur">پہلے سوالات حل کریں، پھر اس کلید سے نمبر لگائیں۔</p></div>'
    )
    sealed = False
    if review:
        if '<div class="answers">' in review:
            review = review.replace(
                '<div class="answers">',
                seal + '<div class="answers">' + check_key,
                1,
            )
            sealed = True
        else:
            review = seal + check_key + review
            sealed = True
    elif check_key:
        review = f'<section class="review">{seal}<div class="answers">{check_key}</div></section>'
        sealed = True
    body = opener + "".join(new_topics) + review
    if not sealed and '<div class="answers">' in body:
        body = body.replace('<div class="answers">', seal + '<div class="answers">', 1)
    return f"{open_tag}\n{body}\n</section>"


def teacher_notes_box(block: str) -> str:
    raw_title = topic_title(block)
    title = re.sub(r"\s*★.*", "", raw_title).strip()
    golden = topic_is_golden(raw_title, block)
    mins = 25 if golden else 15
    star = ' <span class="star">★ Golden</span>' if golden else ""
    qs = check_prompts(block)
    ask = ""
    if qs:
        ask = "<p><b>Ask the class:</b> " + " ".join(
            f"{i}. {html.escape(q)}" for i, q in enumerate(qs, 1)
        ) + "</p>"
    board = first_sentence(box_inner(block, "learn"))
    warn = first_sentence(box_inner(block, "warn"))
    urdu = first_sentence(box_inner(block, "urdu"))
    board_p = f"<p><b>On the board:</b> {html.escape(board)}</p>" if board else ""
    warn_p = f"<p><b>Stop and correct:</b> {html.escape(warn)}</p>" if warn else ""
    ur_p = f'<p class="ur"><b>اردو میں کہیں:</b> {html.escape(urdu)}</p>' if urdu else ""
    return f"""
    <div class="box teach">
      <p><b>{html.escape(title)}</b>{star} · <b>{mins} minutes</b>
      ({'one full period if you include practice' if golden else 'half to three-quarters of a period'}).</p>
      {board_p}
      {ask}
      {warn_p}
      {ur_p}
      <p>End by asking Check yourself orally. Answers are printed in the purple box for you.</p>
    </div>"""


def teacherize_fragment(fragment: str) -> str:
    opener = extract_opener(fragment)
    topics = extract_class_divs(fragment, "topic")
    review = extract_review(fragment)
    open_tag = section_open_tag(fragment)
    golden = sum(1 for b in topics if topic_is_golden(topic_title(b), b))
    n = len(topics)
    mins = sum(25 if topic_is_golden(topic_title(b), b) else 15 for b in topics) or 40
    periods = max(1, round(mins / 40))
    plan = ""
    if n:
        plan = f"""
    <div class="box teach">
      <p><b>Chapter plan:</b> {n} topics · {golden} Golden · about <b>{mins} minutes</b>
      ({periods} period{'s' if periods != 1 else ''} of 40 minutes).</p>
      <p>Teach every ★ Golden topic in full. If time is short, set non-Golden Check yourself as homework.
      Use the chapter practice paper as a period test or weekend homework, then mark with the answer key.</p>
      <p class="ur">گولڈن موضوعات پوری تفصیل سے پڑھائیں۔ وقت کم ہو تو باقی سوالات گھر کے کام دیں۔ باب کے مشقی سوالات ٹیسٹ یا ہوم ورک بنائیں۔</p>
    </div>"""
    new_topics = []
    for block in topics:
        notes = teacher_notes_box(block)
        block = re.sub(r"(<h2[^>]*>.*?</h2>)", r"\1" + notes, block, count=1, flags=re.S)
        new_topics.append(block)
    if not topics:
        plan = """
    <div class="box teach">
      <p><b>Final week:</b> students read one recap aloud, then sit the mock paper in 2 hours 30 minutes with no notes.
      Mark with the key in this edition and re-teach any Golden topic they missed.</p>
      <p class="ur">آخری ہفتے خلاصے زبانی سنیں، پھر ماک پیپر بغیر نوٹس کے کرائیں۔ غلط گولڈن موضوعات دوبارہ پڑھائیں۔</p>
    </div>"""
    body = opener + plan + "".join(new_topics) + review
    return f"{open_tag}\n{body}\n</section>"


def edition_cover(book, chapters, edition: str):
    units = "".join(
        f"<div><b>{n:02d}</b>{html.escape(t)}</div>" for n, t, _ in chapters
    )
    if edition == "teacher":
        tag = "TEACHER'S EDITION"
        cover_cls = "cover teacher-cover"
        sub = ("For teachers &mdash; lesson timing, board questions, Urdu classroom cues "
               "and full answers on the same page.")
        urdu = "اساتذہ کے لیے — سبق کی منصوبہ بندی، بورڈ سوالات، اردو وضاحت اور مکمل جوابات"
        foot = (f"Bilingual Teacher's Edition &middot; {book['curriculum']} &middot; "
                "★ marks Golden (high-yield) exam topics. Not a student workbook.")
    else:
        tag = "STUDENT'S EDITION"
        cover_cls = "cover student-cover"
        sub = ("For students &mdash; learn every chapter on your own. Practice first; "
               "the answer key is at the end of each chapter.")
        urdu = "طلبہ کے لیے — خود سیکھیں، سوالات پہلے حل کریں، جوابات باب کے آخر میں ہیں"
        foot = (f"Student's Edition &middot; {book['curriculum']} &middot; "
                "★ marks Golden (high-yield) exam topics.")
    return f"""
<section class="{cover_cls}">
  <div class="grade">{book['grade']}</div>
  <span class="tag">{tag}</span>
  <h1>{book['title']}</h1>
  <p class="sub">{sub}</p>
  <p class="sub">Bilingual support: English + اردو</p>
  <div class="ur">{urdu}</div>
  <div class="units">{units}</div>
  <div class="foot">{foot}</div>
</section>"""


def build_edition(key: str, edition: str):
    book = BOOKS[key]
    folder = SRC / key
    how_name = "how-to-use-teacher.html" if edition == "teacher" else "how-to-use-student.html"
    intro = (SRC / how_name).read_text(encoding="utf-8")
    transform = teacherize_fragment if edition == "teacher" else studentize_fragment
    frags = sorted(folder.glob("ch*.html"), key=lambda p: int(re.search(r"\d+", p.stem).group()))
    chapters_html, chapters = [], []
    for f in frags:
        text = f.read_text(encoding="utf-8")
        chapters.append(chapter_meta(text))
        chapters_html.append(transform(text))
    final_path = folder / "final.html"
    final = transform(final_path.read_text(encoding="utf-8")) if final_path.exists() else ""
    label = "Teacher's Edition" if edition == "teacher" else "Student's Edition"
    file_name = f"CS-{book['grade']}-{'Teachers' if edition == 'teacher' else 'Students'}-Edition.pdf"
    doc = wrap_html(
        f"{book['title']} — {label}",
        edition_cover(book, chapters, edition)
        + contents(chapters, bool(final))
        + intro
        + "".join(chapters_html)
        + final,
    )
    OUT.mkdir(exist_ok=True)
    html_path = OUT / f"{key}-{edition}.html"
    pdf_path = ROOT.parent / "releases" / file_name
    print_job(doc, html_path, pdf_path, min_bytes=50_000, budget_ms=120000)
    print(f"{key} {edition} edition -> {pdf_path}")
    return pdf_path


def merge_edition_pair(edition: str, paths: list[Path]):
    paths = [p for p in paths if p and p.exists()]
    if len(paths) < 2:
        return
    try:
        import pymupdf
    except ImportError:
        print("skip edition complete merge (pymupdf not installed)")
        return
    name = ("CS-XI-and-XII-Teachers-Edition-Complete.pdf" if edition == "teacher"
            else "CS-XI-and-XII-Students-Edition-Complete.pdf")
    dest = ROOT.parent / "releases" / name
    out = pymupdf.open()
    for p in paths:
        out.insert_file(p)
    out.save(dest, deflate=True, garbage=3)
    pages = out.page_count
    out.close()
    print(f"{edition} complete -> {dest} ({pages} pages)")


def build_editions(keys: list[str]):
    for edition in ("student", "teacher"):
        paths = [build_edition(k, edition) for k in keys]
        merge_edition_pair(edition, paths)


def short_urdu(text: str, limit: int = 110) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return ""
    for sep in ("۔", "؟", "!"):
        if sep in text:
            piece = text.split(sep)[0].strip() + sep
            if 12 <= len(piece) <= limit + 20:
                return piece
    if len(text) <= limit:
        return text
    return text[:limit].rstrip(" ،,") + "…"


def lecture_banner(book, ch_num, ch_title, index, total, title, golden, urdu):
    star = '<span class="chip golden">★ Golden</span>' if golden else ""
    ur = f'<p class="ur">{html.escape(short_urdu(urdu))}</p>' if urdu else ""
    return f"""
<header class="lecture-banner">
  <div class="kicker">Teach Yourself Lecture</div>
  <h1>{html.escape(title.replace("★ Golden", "").replace("★", "").strip())}</h1>
  {ur}
  <div class="chips">
    <span class="chip">CS {book['grade']}</span>
    <span class="chip">Chapter {ch_num}: {html.escape(ch_title)}</span>
    <span class="chip">Lecture {index:02d} of {total}</span>
    {star}
  </div>
</header>"""


def chapter_cover(book, ch_num, ch_title, topics, kind="Chapter lecture"):
    n = len(topics)
    units = (
        f"<div><b>{n:02d}</b>teach-yourself lectures in this pack</div>"
        f"<div><b>★</b>Golden topics, Urdu notes, review and answer key</div>"
    )
    return f"""
<section class="cover lecture-cover">
  <div class="grade">{book['grade']}</div>
  <span class="tag">TEACH YOURSELF LECTURE</span>
  <h1>Lecture {ch_num:02d}<br>{html.escape(ch_title)}</h1>
  <p class="sub">{html.escape(kind)} &mdash; {n} topics with explanations, worked examples,
  Urdu notes, practice questions and a full answer key.</p>
  <p class="sub">{book['title']} · Bilingual support: English + اردو</p>
  <div class="ur">{book['urdu']}</div>
  <div class="units">{units}</div>
  <div class="foot">{book['curriculum']} · Based on the Bilingual Teacher's Edition lecture notes ·
  ★ marks Golden (high-yield) exam topics.</div>
</section>"""


def chapter_contents(ch_num, ch_title, topics):
    items = "".join(
        f"<li><b>L{i:02d}.</b> {html.escape(t)}</li>" for i, t in enumerate(topics, 1)
    )
    return f"""
  <h2>Lectures in this pack</h2>
  <p>Chapter {ch_num}: {html.escape(ch_title)}. Study one lecture at a time, then use the chapter
  review and answer key at the end of this PDF.</p>
  <ol class="toc lecture-index">{items}</ol>
"""


def parse_book_lectures(key: str):
    book = BOOKS[key]
    folder = SRC / key
    how = (SRC / "how-to-use-lecture.html").read_text(encoding="utf-8")
    items = []
    ch_files = sorted(folder.glob("ch*.html"), key=lambda p: int(re.search(r"\d+", p.stem).group()))
    for path in ch_files:
        fragment = path.read_text(encoding="utf-8")
        ch_num, ch_title, _ = chapter_meta(fragment)
        topics = extract_class_divs(fragment, "topic")
        titles = [re.sub(r"\s*★.*", "", topic_title(b)).strip() for b in topics]
        opener = extract_opener(fragment)
        review = extract_review(fragment)
        packed_how = how.replace("</section>", chapter_contents(ch_num, ch_title, titles) + "</section>", 1)
        items.append({
            "kind": "chapter",
            "key": key,
            "ch_num": ch_num,
            "ch_title": ch_title,
            "topics": titles,
            "html_name": f"{key}-ch{ch_num:02d}.html",
            "pdf_name": f"CS-{book['grade']}-Lecture-{ch_num:02d}-{slugify(ch_title)}.pdf",
            "rel_dir": key,
            "body": (
                chapter_cover(book, ch_num, ch_title, titles)
                + packed_how
                + f'<section class="chapter" id="{key}-ch{ch_num}">'
                + opener
                + "".join(topics)
                + review
                + "</section>"
            ),
            "title": f"{book['title']} · Lecture {ch_num:02d}: {ch_title}",
            "golden": False,
            "index": ch_num,
            "total": len(ch_files),
            "budget": 90000,
            "min_bytes": 30_000,
        })
        total = len(topics)
        for i, block in enumerate(topics, 1):
            raw_title = topic_title(block)
            title = re.sub(r"\s*★.*", "", raw_title).strip()
            golden = topic_is_golden(raw_title, block)
            urdu = topic_urdu(block)
            nxt = titles[i] if i < total else "Chapter review (in the chapter lecture PDF)"
            body = (
                lecture_banner(book, ch_num, ch_title, i, total, raw_title, golden, urdu)
                + f'<section class="chapter">{block}</section>'
            )
            if nxt:
                body += f'<p class="lecture-next">Next lecture: {html.escape(nxt)}</p>'
            items.append({
                "kind": "topic",
                "key": key,
                "ch_num": ch_num,
                "ch_title": ch_title,
                "html_name": f"{key}-ch{ch_num:02d}-l{i:02d}.html",
                "pdf_name": f"CS-{book['grade']}-Ch{ch_num:02d}-L{i:02d}-{slugify(title)}.pdf",
                "rel_dir": f"{key}/ch{ch_num:02d}",
                "body": body,
                "title": title,
                "golden": golden,
                "index": i,
                "total": total,
                "budget": 45000,
                "min_bytes": 12_000,
                "topics": [title],
            })
    final_path = folder / "final.html"
    if final_path.exists():
        fragment = final_path.read_text(encoding="utf-8")
        _n, final_title, _ = chapter_meta(fragment)
        items.append({
            "kind": "final",
            "key": key,
            "ch_num": 7,
            "ch_title": final_title,
            "topics": [final_title],
            "html_name": f"{key}-final.html",
            "pdf_name": f"CS-{book['grade']}-Lecture-07-{slugify(final_title)}.pdf",
            "rel_dir": key,
            "body": chapter_cover(book, 7, final_title, [final_title], kind="Final revision lecture")
            + how
            + fragment,
            "title": f"{book['title']} · {final_title}",
            "golden": False,
            "index": 7,
            "total": 7,
            "budget": 60000,
            "min_bytes": 20_000,
        })
    return items


def catalog_html(key: str, items: list[dict]) -> str:
    book = BOOKS[key]
    rows = []
    for it in items:
        mark = "★" if it.get("golden") else ""
        if it["kind"] == "topic":
            code = f"Ch{it['ch_num']:02d}-L{it['index']:02d}"
            label = it["title"]
        elif it["kind"] == "final":
            code = "Lecture 07"
            label = it["ch_title"]
        else:
            code = f"Lecture {it['ch_num']:02d}"
            label = it["ch_title"]
        rows.append(
            f"<tr><td>{html.escape(code)}</td><td>{html.escape(it['pdf_name'])}</td>"
            f"<td>{html.escape(label)} {mark}</td></tr>"
        )
    body = f"""
<section class="cover lecture-cover">
  <div class="grade">{book['grade']}</div>
  <span class="tag">TEACH YOURSELF LECTURES</span>
  <h1>{book['title']}</h1>
  <p class="sub">One PDF per lecture &mdash; plus a full chapter pack for each unit.</p>
  <p class="sub">Bilingual support: English + اردو</p>
  <div class="ur">{book['urdu']}</div>
  <div class="foot">{book['curriculum']} · {len(items)} lecture PDFs</div>
</section>
<section class="front catalog">
  <h1>Lecture index</h1>
  <p>Chapter packs are named <b>Lecture 01–06</b>. Individual topics are <b>ChNN-LNN</b>.
  ★ marks Golden (high-yield) exam topics.</p>
  <table>
    <tr><th>Code</th><th>File</th><th>Title</th></tr>
    {''.join(rows)}
  </table>
</section>"""
    return wrap_html(f"{book['title']} — Teach Yourself Lectures", body)


def write_index_md(all_items: dict[str, list[dict]]):
    RELEASES.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Teach Yourself Lectures (PDF)",
        "",
        "Standalone **Teach Yourself** lecture PDFs for Computer Science XI and XII "
        "(Sindh curriculum). Each topic is one printable lecture; each chapter also has "
        "a packed lecture PDF with the review and answer key.",
        "",
        "## Chapter lecture packs",
        "",
    ]
    for key, items in all_items.items():
        book = BOOKS[key]
        lines.append(f"### {book['title']}")
        lines.append("")
        for it in items:
            if it["kind"] not in ("chapter", "final"):
                continue
            url = f"{RAW}/{it['rel_dir']}/{it['pdf_name']}"
            lines.append(f"- [Lecture {it['ch_num']:02d}: {it['ch_title']}]({url})")
        lines.append("")
        lines.append(f"- [Lecture index PDF]({RAW}/{key}/CS-{book['grade']}-Lecture-Index.pdf)")
        lines.append(f"- [All {book['grade']} lectures (zip)]({ZIP_RAW}/CS-{book['grade']}-Teach-Yourself-Lectures.zip)")
        lines.append("")
        lines.append("<details><summary>Individual topic lectures</summary>")
        lines.append("")
        current = None
        for it in items:
            if it["kind"] != "topic":
                continue
            if it["ch_num"] != current:
                current = it["ch_num"]
                lines.append(f"**Chapter {current}: {it['ch_title']}**")
                lines.append("")
            star = " ★" if it["golden"] else ""
            url = f"{RAW}/{it['rel_dir']}/{it['pdf_name']}"
            lines.append(f"- [L{it['index']:02d} {it['title']}]({url}){star}")
        lines.append("")
        lines.append("</details>")
        lines.append("")
    (RELEASES / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def zip_grade(key: str, pdf_paths: list[Path]):
    book = BOOKS[key]
    zip_path = RELEASES.parent / f"CS-{book['grade']}-Teach-Yourself-Lectures.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for p in pdf_paths:
            zf.write(p, arcname=f"{book['grade']}/{p.relative_to(RELEASES)}")
    print(f"zip -> {zip_path} ({zip_path.stat().st_size} bytes)")


def build_lectures(keys: list[str], workers: int = 3):
    how_exists = (SRC / "how-to-use-lecture.html").exists()
    if not how_exists:
        raise SystemExit("missing booklets/src/how-to-use-lecture.html")
    OUT.mkdir(exist_ok=True)
    html_root = OUT / "lectures"
    html_root.mkdir(exist_ok=True)
    RELEASES.mkdir(parents=True, exist_ok=True)

    parsed = {key: parse_book_lectures(key) for key in keys}
    jobs = []
    copied: dict[str, list[Path]] = {k: [] for k in keys}

    for key, items in parsed.items():
        catalog_name = f"CS-{BOOKS[key]['grade']}-Lecture-Index.pdf"
        cat_html = html_root / f"{key}-index.html"
        cat_pdf = RELEASES / key / catalog_name
        jobs.append({
            "html": catalog_html(key, items),
            "html_path": cat_html,
            "pdf_path": cat_pdf,
            "min_bytes": 20_000,
            "budget": 60000,
            "label": f"{key} index",
            "key": key,
        })
        copied[key].append(cat_pdf)
        for it in items:
            jobs.append({
                "html": wrap_html(it["title"], it["body"]),
                "html_path": html_root / it["html_name"],
                "pdf_path": RELEASES / it["rel_dir"] / it["pdf_name"],
                "min_bytes": it["min_bytes"],
                "budget": it["budget"],
                "label": it["pdf_name"],
                "key": key,
            })
            copied[key].append(RELEASES / it["rel_dir"] / it["pdf_name"])

    print(f"Printing {len(jobs)} lecture PDFs with {workers} Chrome workers…")
    failed = []

    def run(job):
        print_job(job["html"], job["html_path"], job["pdf_path"], job["min_bytes"], job["budget"])
        return job["label"], job["pdf_path"].stat().st_size

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futs = {pool.submit(run, job): job for job in jobs}
        done = 0
        for fut in as_completed(futs):
            job = futs[fut]
            done += 1
            try:
                label, size = fut.result()
                print(f"  [{done}/{len(jobs)}] {label} ({size} bytes)")
            except Exception as exc:
                failed.append((job["label"], str(exc)))
                print(f"  [{done}/{len(jobs)}] FAIL {job['label']}: {exc}")

    if failed:
        print(f"Retrying {len(failed)} failed jobs serially…")
        still = []
        lookup = {j["label"]: j for j in jobs}
        for label, _ in failed:
            job = lookup[label]
            try:
                print_job(job["html"], job["html_path"], job["pdf_path"], job["min_bytes"], job["budget"])
                print(f"  recovered {label}")
            except Exception as exc:
                still.append((label, str(exc)))
        if still:
            raise SystemExit("Failed PDFs:\n" + "\n".join(f"- {a}: {b}" for a, b in still))

    write_index_md(parsed)
    for key in keys:
        existing = [p for p in copied[key] if p.exists()]
        zip_grade(key, existing)
    print("Lecture PDFs ready in", RELEASES)


def main(argv: list[str]):
    args = argv[1:]
    mode = "booklets"
    keys = []
    if args and args[0] in ("lectures", "booklets", "editions", "all"):
        mode = args[0]
        args = args[1:]
    keys = [a for a in args if a in BOOKS] or list(BOOKS)
    if mode in ("booklets", "all"):
        for k in keys:
            build_booklet(k)
        merge_complete(keys)
    if mode in ("lectures", "all"):
        build_lectures(keys)
    if mode in ("editions", "all"):
        build_editions(keys)


if __name__ == "__main__":
    main(sys.argv)
