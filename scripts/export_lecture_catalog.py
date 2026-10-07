#!/usr/bin/env python3
"""Build lectures.json: English notes + Urdu spoken lecture scripts."""
from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "booklets" / "build.py"
OUT = ROOT / "lectures" / "src" / "main" / "assets" / "lectures.json"

spec = importlib.util.spec_from_file_location("booklets_build", BUILD)
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)


def plain(text: str) -> str:
    text = b.unescape(b.strip_tags(text))
    text = text.replace("★ Golden", "").replace("★", "")
    return re.sub(r"\s+", " ", text).strip()


def bold_terms(html: str) -> list[str]:
    found = [plain(x) for x in re.findall(r"<b>(.*?)</b>", html, flags=re.S)]
    out, seen = [], set()
    for term in found:
        if 2 < len(term) < 48:
            key = term.lower()
            if key not in seen:
                seen.add(key)
                out.append(term)
        if len(out) >= 8:
            break
    return out


def spoken_urdu(title: str, chapter: str, golden: bool, urdu: str, terms: list[str], exam: str) -> str:
    bits = [
        "طلبہ، السلام علیکم۔",
        "آج ہم کالج کے طالب علموں کو انگریزی لیکچر نوٹس اردو میں سمجھا رہے ہیں۔",
        f"سبق کا عنوان ہے: {title}۔",
        f"یہ باب {chapter} سے ہے۔",
    ]
    if golden:
        bits.append("یہ گولڈن موضوع ہے۔ بورڈ امتحان میں زیادہ نمبر اسی سے آتے ہیں۔ پوری توجہ سے سنو۔")
    if urdu:
        bits.append("اب سبق کی وضاحت سنو۔")
        bits.append(urdu.rstrip("۔") + "۔")
    if terms:
        bits.append("انگریزی نوٹ میں یہ اصطلاحات یاد رکھو: " + "، ".join(terms) + "۔")
    if exam:
        bits.append("بورڈ میں یہ یوں پوچھا جاتا ہے: " + exam.rstrip("۔") + "۔")
    bits.append("جواب میں تعریف، وضاحت، مثال، خاکہ اور ورکنگ لکھنا۔ اللہ حافظ۔")
    return " ".join(bits)


def topics_from(fragment: str, grade: str, ch_num: int, ch_title: str) -> list[dict]:
    rows = []
    for i, block in enumerate(b.extract_class_divs(fragment, "topic"), 1):
        raw = b.topic_title(block)
        title = re.sub(r"\s*★.*", "", raw).strip()
        golden = b.topic_is_golden(raw, block)
        learn_html = b.extract_box_html(block, "learn") or ""
        learn = plain(learn_html)[:1800]
        urdu = b.topic_urdu(block)
        exam = b.clip_text(b.extract_box_text(block, "exam"), 220)
        terms = bold_terms(learn_html)
        rows.append({
            "id": f"{grade}-{ch_num}-{i}",
            "title": title,
            "golden": golden,
            "learn": learn,
            "urdu": urdu,
            "spokenUrdu": spoken_urdu(title, ch_title, golden, urdu, terms, exam),
            "terms": terms,
        })
    return rows


def main() -> int:
    grades = []
    for key, book in b.BOOKS.items():
        folder = b.SRC / key
        chapters = []
        for f in sorted(folder.glob("ch*.html"), key=lambda p: int(re.search(r"\d+", p.stem).group())):
            text = f.read_text(encoding="utf-8")
            num, title, _ = b.chapter_meta(text)
            chapters.append({
                "num": num,
                "title": title,
                "topics": topics_from(text, key, num, title),
            })
        grades.append({
            "id": key,
            "title": book["title"],
            "urdu": book["urdu"],
            "curriculum": book["curriculum"],
            "chapters": chapters,
        })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {"grades": grades}
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    n = sum(len(t) for g in grades for c in g["chapters"] for t in [c["topics"]])
    print(f"wrote {OUT} ({n} topics)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
