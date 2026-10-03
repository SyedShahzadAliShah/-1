#!/usr/bin/env python3
"""Validate authored page content (content/pNNN.json) against the extracted PDF English text.

Usage: validate_content.py [page ...]    (no args = all pages)
Exit status is non-zero if any page fails.
"""
import collections
import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
AR = re.compile("[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]")
LETTER = re.compile(r"[A-Za-z\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]")
TOKEN = re.compile(r"[A-Za-z0-9]+")
TYPES = {"title", "h1", "h2", "h3", "badge", "p", "li", "note", "table", "code", "figure"}
TOTAL_PAGES = 127


def block_texts(b):
    """All English strings contributed by a block."""
    out = [b.get("en", ""), b.get("label", "")]
    out += b.get("cols", [])
    for r in b.get("rows", []):
        out += r.get("cells", [])
    return out


def block_urdu(b):
    """(label, urdu) pairs that must carry narration."""
    if b["t"] == "table":
        return [(f"row {i}", r.get("ur", "")) for i, r in enumerate(b.get("rows", []))]
    return [("block", b.get("ur", ""))]


def extracted_text(page):
    path = os.path.join(ROOT, "work", "extract", f"p{page:03d}.txt")
    out = []
    for line in open(path).read().splitlines()[1:]:
        text = re.sub(r"^\[[^\]]*\]\s*", "", line)
        if not re.fullmatch(r"Page \d+", text.strip()):
            out.append(text)
    return " ".join(out)


def extracted_tokens(page):
    path = os.path.join(ROOT, "work", "extract", f"p{page:03d}.txt")
    toks = collections.Counter()
    for line in open(path).read().splitlines()[1:]:
        text = re.sub(r"^\[[^\]]*\]\s*", "", line)
        if re.fullmatch(r"Page \d+", text.strip()):
            continue
        toks.update(TOKEN.findall(text.lower()))
    return toks


def validate(page):
    errs = []
    path = os.path.join(ROOT, "content", f"p{page:03d}.json")
    if not os.path.exists(path):
        return [f"missing {path}"]
    try:
        data = json.load(open(path, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return [f"invalid JSON: {e}"]
    if data.get("page") != page:
        errs.append(f"page field is {data.get('page')}, expected {page}")
    blocks = data.get("blocks")
    if not isinstance(blocks, list) or not blocks:
        return errs + ["no blocks"]

    got = collections.Counter()
    for i, b in enumerate(blocks):
        t = b.get("t")
        if t not in TYPES:
            errs.append(f"block {i}: bad type {t!r}")
            continue
        if t == "table":
            if not b.get("cols") or not b.get("rows"):
                errs.append(f"block {i}: table needs cols and rows")
            for r in b.get("rows", []):
                if len(r.get("cells", [])) != len(b.get("cols", [])):
                    errs.append(f"block {i}: row/col count mismatch {r.get('cells')}")
        elif not b.get("en", "").strip():
            errs.append(f"block {i}: empty en")
        for text in block_texts(b):
            got.update(TOKEN.findall(text.lower()))
        for label, ur in block_urdu(b):
            letters = LETTER.findall(ur)
            arabic = AR.findall(ur)
            if not ur.strip():
                errs.append(f"block {i} ({t}) {label}: missing ur")
            elif len(arabic) < 0.8 * max(1, len(letters)):
                errs.append(f"block {i} ({t}) {label}: ur is not mostly Urdu script: {ur[:60]!r}")
            if len(ur) > 900:
                errs.append(f"block {i} ({t}) {label}: ur too long ({len(ur)} chars), split the block")

    ext = extracted_tokens(page)
    missing = ext - got
    extra = got - ext
    n = sum(ext.values())
    miss_n, extra_n = sum(missing.values()), sum(extra.values())
    token_ok = miss_n <= max(2, 0.03 * n) and extra_n <= max(4, 0.06 * n)
    if token_ok:
        return errs
    # Code lines lose their spaces in the PDF text layer, so fall back to comparing alphanumerics.
    chars = lambda s: collections.Counter(re.findall(r"[a-z0-9]", s.lower()))  # noqa: E731
    ext_c = chars(extracted_text(page))
    got_c = chars(" ".join(t for b in blocks for t in block_texts(b)))
    c_missing, c_extra = sum((ext_c - got_c).values()), sum((got_c - ext_c).values())
    total = sum(ext_c.values())
    if c_missing > max(6, 0.03 * total) or c_extra > max(12, 0.06 * total):
        if miss_n > max(2, 0.03 * n):
            errs.append(f"{miss_n}/{n} extracted English tokens missing: {dict(list(missing.items())[:25])}")
        if extra_n > max(4, 0.06 * n):
            errs.append(f"{extra_n} English tokens not in source: {dict(list(extra.items())[:25])}")
        errs.append(f"character check also failed: {c_missing} missing, {c_extra} extra of {total}")
    return errs


def main():
    pages = [int(a) for a in sys.argv[1:]] or list(range(1, TOTAL_PAGES + 1))
    bad = 0
    for p in pages:
        errs = validate(p)
        if errs:
            bad += 1
            print(f"PAGE {p}: FAIL")
            for e in errs:
                print("   -", e)
    print(f"{len(pages) - bad}/{len(pages)} pages OK")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
