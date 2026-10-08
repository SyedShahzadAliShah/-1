#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate Urdish lectures and write the asset consumed by the APK."""

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from urdish_lectures import CHAPTERS, LECTURES  # noqa: E402
from urdish_lectures_more import MORE  # noqa: E402

ARABIC = re.compile(r"[\u0600-\u06FF]")
DIAGRAMS = set(re.findall(r"^\s+(\w+):\s*\(\)\s*=>", (ROOT / "teach/src/main/assets/www/diagrams.js").read_text(encoding="utf-8"), re.M))


class Balancer(HTMLParser):
    VOID = {"br", "img", "input", "hr", "meta", "link"}

    def __init__(self):
        super().__init__()
        self.stack = []
        self.paragraphs = []
        self._capture = None
        self._buf = []

    def handle_starttag(self, tag, attrs):
        if tag not in self.VOID:
            self.stack.append(tag)
        if tag == "p":
            self._capture = dict(attrs).get("class", "")
            self._buf = []

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        if not self.stack or self.stack[-1] != tag:
            raise SystemExit(f"unbalanced </{tag}> near {self.stack[-3:]}")
        self.stack.pop()
        if tag == "p" and self._capture is not None:
            self.paragraphs.append((self._capture, "".join(self._buf)))
            self._capture = None

    def handle_data(self, data):
        if self._capture is not None:
            self._buf.append(data)


def main():
    lectures = LECTURES + MORE
    ids = [item["id"] for item in lectures]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate lecture id")
    chapters = {item["id"] for item in CHAPTERS}
    errors = []
    for lec in lectures:
        if lec["chapter"] not in chapters:
            errors.append(f"{lec['id']} bad chapter")
        if lec["diagram"] not in DIAGRAMS:
            errors.append(f"{lec['id']} missing diagram {lec['diagram']}")
        if not ARABIC.search(lec["title"] + lec["html"] + lec["caption"]):
            errors.append(f"{lec['id']} has no Urdu")
        if lec["html"].count(r"\(") != lec["html"].count(r"\)"):
            errors.append(f"{lec['id']} inline math")
        if lec["html"].count(r"\[") != lec["html"].count(r"\]"):
            errors.append(f"{lec['id']} display math")
        if "<pre" in lec["html"] and "data-speak" not in lec["html"]:
            errors.append(f"{lec['id']} code without speech label")
        parser = Balancer()
        parser.feed(lec["html"])
        if parser.stack:
            errors.append(f"{lec['id']} unclosed {parser.stack}")
        for klass, text in parser.paragraphs:
            letters = [ch for ch in text if ch.isalpha() or ARABIC.match(ch)]
            if len(letters) < 12:
                continue
            arabic = sum(1 for ch in letters if ARABIC.match(ch))
            if arabic == 0 and "code" not in klass:
                errors.append(f"{lec['id']} English-only paragraph: {text[:80]}")
        if len(lec["checks"]) < 2:
            errors.append(f"{lec['id']} needs two checks")
        for check in lec["checks"]:
            if not 0 <= check["answer"] < len(check["options"]):
                errors.append(f"{lec['id']} bad answer")
            if not ARABIC.search(check["q"] + check["why"]):
                errors.append(f"{lec['id']} check not Urdish")
    for chapter in CHAPTERS:
        if not any(item["chapter"] == chapter["id"] for item in lectures):
            errors.append(f"empty chapter {chapter['id']}")
    if errors:
        raise SystemExit("\n".join(errors))

    payload = {"chapters": CHAPTERS, "lectures": lectures}
    out = ROOT / "teach/src/main/assets/www/lectures.js"
    text = "window.LECTURES = " + json.dumps(payload, ensure_ascii=False, indent=2) + ";\n"
    out.write_text(text, encoding="utf-8")
    math = sum(item["html"].count(r"\[") + item["html"].count(r"\(") for item in lectures)
    print(f"lectures {len(lectures)} formulas {math} bytes {out.stat().st_size}")


if __name__ == "__main__":
    main()
