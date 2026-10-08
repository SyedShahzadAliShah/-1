#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WWW = ROOT / "app/src/main/assets/www"
data = json.loads((WWW / "data/curriculum.json").read_text(encoding="utf-8"))

assert data["voice"] == "urdish"
assert data["layout"] == "flexbox"
assert data["math"].startswith("mathjax")
ids = [t["id"] for t in data["tracks"]]
assert ids == ["studio", "xi", "xii"], ids

studio = data["tracks"][0]["chapters"][0]
assert studio["file"] == "studio/sketchnotes.html"
assert (WWW / studio["file"]).is_file()
assert any("Flexbox" in t["titleEn"] for t in studio["topics"])

for track in data["tracks"][1:]:
    assert len(track["chapters"]) >= 6
    for ch in track["chapters"]:
        assert (WWW / ch["file"]).is_file(), ch["file"]
        assert ch["topics"], ch["id"]
        assert ch["file"].endswith(".html")

xi1 = next(ch for ch in data["tracks"][1]["chapters"] if ch["id"].endswith("ch1"))
assert xi1["svgCount"] >= 8
assert xi1["goldenCount"] >= 5
assert any("Boolean" in t["titleEn"] for t in xi1["topics"])
assert any("Karnaugh" in t["titleEn"] for t in xi1["topics"])

xii1 = next(ch for ch in data["tracks"][2]["chapters"] if ch["id"].endswith("ch1"))
assert any("HCI" in t["titleEn"] or "Human" in t["titleEn"] for t in xii1["topics"])

beats = sum(len(ch["topics"]) for t in data["tracks"] for ch in t["chapters"])
assert beats > 150, beats
print(f"curriculum ok: {beats} beats, tracks={ids}")
