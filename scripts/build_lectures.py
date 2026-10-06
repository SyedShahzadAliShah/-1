#!/usr/bin/env python3
"""Write app/src/main/assets/lectures/catalog.json from the original scripts."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lectures_xi import chapters as xi_chapters
from lectures_xii import chapters as xii_chapters


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "app" / "src" / "main" / "assets" / "lectures" / "catalog.json"


def validate(catalog):
    seen = set()
    lectures = 0
    boards = 0
    for grade in catalog["grades"]:
        assert grade["chapters"], grade["id"]
        for chapter in grade["chapters"]:
            assert chapter["lectures"], chapter["id"]
            for lec in chapter["lectures"]:
                assert lec["id"] not in seen, lec["id"]
                seen.add(lec["id"])
                lectures += 1
                assert len(lec["boards"]) >= 3, lec["id"]
                for index, board in enumerate(lec["boards"]):
                    boards += 1
                    words = board["narration"].split()
                    assert len(words) >= 28, (lec["id"], index, len(words), board["narration"][:120])
                    assert board["marks"], lec["id"]
                    assert board["marks"][0]["k"] == "title", (lec["id"], index)
                    for mark in board["marks"]:
                        assert mark["k"]
    print(f"lectures={lectures} boards={boards}")


def main():
    catalog = {
        "grades": [
            {
                "id": "xi",
                "label": "Class XI",
                "title": "Computer Science XI",
                "subtitle": "Sindh curriculum, animated lectures",
                "chapters": xi_chapters(),
            },
            {
                "id": "xii",
                "label": "Class XII",
                "title": "Computer Science XII",
                "subtitle": "Sindh curriculum, animated lectures",
                "chapters": xii_chapters(),
            },
        ]
    }
    validate(catalog)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(catalog, ensure_ascii=True, indent=2), encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
