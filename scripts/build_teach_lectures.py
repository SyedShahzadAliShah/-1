#!/usr/bin/env python3
"""Write the embedded Urdish lecture script consumed by the APK WebView."""

import json
from pathlib import Path

from teach_content import CHAPTERS

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "teachyourself" / "src" / "main" / "assets" / "www" / "data" / "lectures.js"

SVG_NAMES = {
    "stairs",
    "waves",
    "gate",
    "circuit",
    "kmap2",
    "kmap3",
    "logisim",
    "waterfall",
    "agile",
    "osi",
    "tcpip",
    "bubble",
    "selection",
    "binary",
    "languages",
    "flow",
    "keys",
    "er",
    "library",
    "integrity",
    "iot",
    "bars",
    "pie",
    "sources",
    "inquiry",
}


def validate(course):
    errors = []
    seen = set()
    if len(course["chapters"]) != 6:
        errors.append("expected 6 chapters")
    for chapter in course["chapters"]:
        if not chapter["lectures"]:
            errors.append(f"{chapter['id']} has no lectures")
        for lecture in chapter["lectures"]:
            if lecture["id"] in seen:
                errors.append(f"duplicate id {lecture['id']}")
            seen.add(lecture["id"])
            says = [block.get("say", "").strip() for block in lecture["blocks"]]
            if not any(says):
                errors.append(f"{lecture['id']} has nothing to speak")
            for block in lecture["blocks"]:
                if block["type"] == "svg" and block["name"] not in SVG_NAMES:
                    errors.append(f"{lecture['id']} unknown svg {block['name']}")
                if block["type"] == "math" and not block.get("tex"):
                    errors.append(f"{lecture['id']} empty tex")
                if block["type"] == "check" and (not block.get("q") or not block.get("a")):
                    errors.append(f"{lecture['id']} empty check")
    return errors


def main():
    course = {
        "edition": "Teach Yourself Edition",
        "language": "Urdish",
        "title": "Computer Science XI",
        "curriculum": "Sindh Curriculum 2026",
        "chapters": CHAPTERS,
    }
    errors = validate(course)
    if errors:
        raise SystemExit("\n".join(errors))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(course, ensure_ascii=False, indent=2)
    OUT.write_text("window.COURSE = " + payload + ";\n", encoding="utf-8")
    lectures = sum(len(chapter["lectures"]) for chapter in CHAPTERS)
    print(f"wrote {OUT} ({lectures} lectures, {OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
