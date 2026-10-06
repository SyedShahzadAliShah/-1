#!/usr/bin/env python3
"""Sanity-check generated whiteboard lecture curriculum."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ALLOWED = {
    "heading",
    "subheading",
    "note",
    "bullet",
    "callout",
    "code",
    "diagram",
    "formula",
    "clear",
}

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = ROOT / "app/src/main/assets/lectures/curriculum.json"


def main() -> int:
    data = json.loads(CURRICULUM.read_text(encoding="utf-8"))
    errors: list[str] = []
    lectures = 0
    golden = 0
    segments = 0
    for pack in data.get("classes", []):
        if pack["id"] not in {"xi", "xii"}:
            errors.append(f"unexpected class {pack['id']}")
        for chapter in pack.get("chapters", []):
            for lecture in chapter.get("lectures", []):
                lectures += 1
                if lecture.get("golden"):
                    golden += 1
                segs = lecture.get("segments") or []
                if not segs:
                    errors.append(f"{lecture.get('id')} has no segments")
                for seg in segs:
                    segments += 1
                    if not seg.get("speakEn"):
                        errors.append(f"{lecture.get('id')} empty English vocals")
                    if not seg.get("speakUr"):
                        errors.append(f"{lecture.get('id')} empty Urdu vocals")
                    if not seg.get("actions"):
                        errors.append(f"{lecture.get('id')} segment has no board actions")
                    for action in seg.get("actions", []):
                        if action.get("type") not in ALLOWED:
                            errors.append(f"{lecture.get('id')} bad action {action.get('type')}")
    print(f"classes={len(data.get('classes', []))} lectures={lectures} golden={golden} segments={segments}")
    if lectures < 200:
        errors.append(f"expected at least 200 lectures, got {lectures}")
    if errors:
        print("FAILED")
        for err in errors[:20]:
            print(" ", err)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
