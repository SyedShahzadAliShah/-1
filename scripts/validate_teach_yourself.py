#!/usr/bin/env python3
"""Validate Teach Yourself curriculum, diagrams, and MathJax embedding."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TY = ROOT / "teach-yourself"


def extract_export_object(js: str, name: str) -> dict | list:
    m = re.search(rf"(?:export const |const ){name} = ", js)
    if not m:
        raise SystemExit(f"missing export {name}")
    start = js.find("{", m.end()) if "{" in js[m.end():m.end() + 20] else js.find("[", m.end())
    depth = 0
    in_str = None
    esc = False
    for i, ch in enumerate(js[start:], start):
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == in_str:
                in_str = None
            continue
        if ch in "\"'":
            in_str = ch
            continue
        if ch in "{[":
            depth += 1
        elif ch in "}]":
            depth -= 1
            if depth == 0:
                return json.loads(js[start : i + 1])
    raise SystemExit(f"could not parse {name}")


def diagram_ids_from_js(js: str) -> set[str]:
    keys = set(re.findall(r"\n  ([A-Za-z0-9_]+): \{", js))
    return keys


def main() -> int:
    errors: list[str] = []
    index = (TY / "index.html").read_text(encoding="utf-8")
    css = (TY / "css" / "app.css").read_text(encoding="utf-8")
    mathjax = TY / "vendor" / "mathjax" / "tex-svg-full.js"
    if "vendor/mathjax/tex-svg-full.js" not in index:
        errors.append("index.html must embed local MathJax SVG")
    if "cdn.jsdelivr" in index or "cdnjs" in index:
        errors.append("index.html must not load CDN MathJax")
    if "svg: { fontCache" not in index:
        errors.append("MathJax must use SVG output")
    if "display: flex" not in css:
        errors.append("app.css must use Flexbox")
    if 'dir="rtl"' not in index or 'lang="ur"' not in index:
        errors.append("HTML must be Urdu RTL")
    if not mathjax.is_file() or mathjax.stat().st_size < 500_000:
        errors.append("tex-svg-full.js missing or too small")

    cur_js = (TY / "js" / "curriculum.js").read_text(encoding="utf-8")
    diag_js = (TY / "js" / "diagrams.js").read_text(encoding="utf-8")
    curriculum = extract_export_object(cur_js, "CURRICULUM")
    diagram_ids = diagram_ids_from_js(diag_js)

    modules = 0
    slides = 0
    quizzes = 0
    math_slides = 0
    used_diagrams: set[str] = set()
    for ch in curriculum["chapters"]:
        for mod in ch["modules"]:
            modules += 1
            if not re.search(r"[\u0600-\u06FF]", mod["title"]):
                errors.append(f"module title not Urdu: {mod['id']}")
            for slide in mod["slides"]:
                slides += 1
                body = slide.get("body") or ""
                narr = slide.get("narrator") or ""
                if not re.search(r"[\u0600-\u06FF]", body + slide.get("headline", "")):
                    errors.append(f"non-Urdish slide {mod['id']} {slide.get('headline')}")
                if "\\(" in body or "\\[" in body:
                    math_slides += 1
                if slide.get("quiz"):
                    quizzes += 1
                did = slide.get("diagram")
                if did:
                    used_diagrams.add(did)
                    if did not in diagram_ids:
                        errors.append(f"unknown diagram '{did}' in {mod['id']}")
                if "Teacher's Tip" in body or "اساتذہ" in (slide.get("headline") or ""):
                    errors.append(f"teacher-edition leftover in {mod['id']}")
                if narr and not re.search(r"[\u0600-\u06FF]", narr):
                    errors.append(f"English-only narrator in {mod['id']}")

    tts = (TY / "js" / "tts.js").read_text(encoding="utf-8")
    if "ur-PK" not in tts:
        errors.append("TTS must target Urdu")
    if "en-US" in tts and "ALLOWED" in tts:
        errors.append("TTS must not keep bilingual EN mode")

    print(f"chapters={len(curriculum['chapters'])} modules={modules} slides={slides} quizzes={quizzes} math_slides={math_slides} diagrams={len(used_diagrams)}")
    if modules < 40:
        errors.append(f"expected 40+ lecture modules, got {modules}")
    if math_slides < 6:
        errors.append("too few MathJax slides")
    if quizzes < 20:
        errors.append("too few self-check quizzes")
    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
