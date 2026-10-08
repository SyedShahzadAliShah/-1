#!/usr/bin/env python3
"""Pack each cinematic lecture as a built-in FLV (English board for the Urdish APK)."""
from __future__ import annotations

import html as html_lib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import export_lecture_catalog as catalog  # noqa: E402

import importlib.util

spec = importlib.util.spec_from_file_location("booklets_build", ROOT / "booklets" / "build.py")
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)

JSON_PATH = ROOT / "lectures" / "src" / "main" / "assets" / "lectures.json"
WB = Path(os.environ.get("WHITEBOARD_OUT", ROOT / "lectures" / "src" / "main" / "assets" / "whiteboards"))
FLV_OUT = Path(os.environ.get("FLV_OUT", ROOT / "lectures" / "src" / "main" / "assets" / "flv"))
CSS = (WB / "whiteboard.css").as_uri()
MJAX = (WB / "mathjax" / "tex-svg.js").as_uri()
FFMPEG = shutil.which("ffmpeg") or "ffmpeg"
FFPROBE = shutil.which("ffprobe") or "ffprobe"
FORCE = os.environ.get("FORCE_FLV") == "1"
SKIP_PRINT = os.environ.get("SKIP_PRINT") == "1"
REPRINT = os.environ.get("REPRINT_FLV") == "1"


def article_from(html_path: Path) -> str:
    text = html_path.read_text(encoding="utf-8")
    m = re.search(r"<article class=\"board\">(.*?)</article>", text, flags=re.S)
    inner = m.group(1) if m else text
    return f'<article class="board">{inner}</article>'


def print_document(grade_id: str, topics: list[dict]) -> str:
    parts = []
    for t in topics:
        html_file = ROOT / "lectures" / "src" / "main" / "assets" / t["board"]
        if not html_file.exists():
            html_file = WB / t["board"].replace("whiteboards/", "")
        if not html_file.exists():
            continue
        mark = html_lib.escape(t["id"])
        parts.append(
            f'<div class="flv-pack" data-id="{mark}">'
            f'<p class="flv-mark">FLV|{mark}|</p>'
            f"{article_from(html_file)}</div>"
        )
    body = "\n".join(parts)
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>{html_lib.escape(grade_id)} lecture FLV pack</title>
<link rel="stylesheet" href="{CSS}">
<style>
@page {{ size: A4; margin: 9mm; }}
.flv-pack {{ break-before: page; page-break-before: always; }}
article.board {{ break-before: auto; page-break-before: auto; min-height: 0; }}
.flv-mark {{ font: 11pt/1.3 ui-monospace, monospace; color: #111827; margin: 0 0 8px; }}
.cinema {{ display: none; }}
</style>
<script>
window.MathJax = {{
  tex: {{
    inlineMath: [['\\\\(', '\\\\)']],
    displayMath: [['\\\\[', '\\\\]']],
    processEscapes: true,
    processEnvironments: true
  }},
  svg: {{ fontCache: 'global', displayAlign: 'left', scale: 0.92 }},
  options: {{ skipHtmlTags: ['script','noscript','style','textarea','pre','code','svg'] }},
  startup: {{ typeset: true }}
}};
</script>
<script src="{MJAX}"></script>
</head>
<body class="print-flv">
{body}
</body></html>
"""


def speech_seconds(text: str) -> float:
    return max(24.0, float(catalog.spoken_seconds(text or "")))


def page_holds(total: float, weights: list[int]) -> list[float]:
    if not weights:
        return [total]
    safe = [max(8, w) for w in weights]
    s = float(sum(safe))
    return [round(total * w / s, 2) for w in safe]


def flv_duration(path: Path) -> float:
    if not path.exists():
        return 0.0
    proc = subprocess.run(
        [FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        capture_output=True,
        text=True,
    )
    try:
        return float((proc.stdout or "0").strip() or 0)
    except ValueError:
        return 0.0


def needs_encode(dest: Path, spoken: str) -> bool:
    if FORCE or not dest.exists() or dest.stat().st_size < 4000:
        return True
    want = speech_seconds(spoken)
    have = flv_duration(dest)
    return have < want * 0.72 or have > want * 1.35


def encode_flv(pngs: list[Path], dest: Path, holds: list[float]) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if len(holds) != len(pngs):
        holds = page_holds(sum(holds) if holds else speech_seconds(""), [1] * len(pngs))
    vf = "scale=720:-2:flags=lanczos,scale=720:trunc(ih/2)*2,format=yuv420p"
    with tempfile.TemporaryDirectory(prefix="flv-enc-") as tmp:
        tmp_path = Path(tmp)
        inputs: list[str] = []
        for i, png in enumerate(pngs):
            hold = max(4.0, holds[i])
            clip = tmp_path / f"c{i:02d}.flv"
            subprocess.run(
                [
                    FFMPEG, "-y",
                    "-loop", "1", "-framerate", "1", "-t", f"{hold:.2f}", "-i", str(png),
                    "-vf", vf,
                    "-an",
                    "-c:v", "libx264", "-tune", "stillimage", "-preset", "veryfast", "-crf", "32",
                    "-g", "250", "-bf", "0", "-pix_fmt", "yuv420p",
                    "-max_interleave_delta", "0", "-f", "flv", str(clip),
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
            )
            inputs.append(str(clip))
        if len(inputs) == 1:
            shutil.copy2(inputs[0], dest)
            return
        lst = tmp_path / "list.txt"
        lst.write_text("".join(f"file '{p}'\n" for p in inputs), encoding="utf-8")
        subprocess.run(
            [
                FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
                "-c", "copy", "-f", "flv", str(dest),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )


def pages_for_topics(pdf_path: Path, topic_ids: list[str]) -> dict[str, list[int]]:
    import pymupdf

    doc = pymupdf.open(pdf_path)
    found: dict[str, list[int]] = {tid: [] for tid in topic_ids}
    current = None
    for i, page in enumerate(doc):
        text = page.get_text()
        hit = None
        for tid in sorted(topic_ids, key=len, reverse=True):
            if f"FLV|{tid}|" in text:
                hit = tid
                break
        if hit:
            current = hit
            body = text.replace(f"FLV|{hit}|", "").strip()
            if not body:
                continue
        if current:
            found[current].append(i)
    doc.close()
    return found


def render_pages(pdf_path: Path, indexes: list[int], dest_dir: Path, topic_id: str) -> tuple[list[Path], list[int]]:
    import pymupdf

    dest_dir.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(pdf_path)
    zoom = pymupdf.Matrix(1.45, 1.45)
    pngs: list[Path] = []
    weights: list[int] = []
    mark = f"FLV|{topic_id}|"
    for n, idx in enumerate(indexes, 1):
        if idx < 0 or idx >= doc.page_count:
            continue
        png = dest_dir / f"{n:02d}.png"
        page = doc[idx]
        page.get_pixmap(matrix=zoom, alpha=False).save(png)
        body = page.get_text().replace(mark, "")
        pngs.append(png)
        weights.append(max(8, len(body.split())))
    doc.close()
    return pngs, weights


def topics_of(catalog: dict, grade_id: str) -> list[dict]:
    for g in catalog["grades"]:
        if g["id"] == grade_id:
            rows = []
            for ch in g["chapters"]:
                rows.extend(ch["topics"])
            return rows
    return []


def flv_path(topic: dict) -> Path:
    rel = topic.get("flv") or ""
    return ROOT / "lectures" / "src" / "main" / "assets" / rel


def pack_chapter(grade_id: str, ch_num: int, topics: list[dict]) -> int:
    needed = [t for t in topics if needs_encode(flv_path(t), t.get("spokenUrdu") or "")]
    if not needed:
        return 0
    work = ROOT / "booklets" / "output"
    work.mkdir(parents=True, exist_ok=True)
    html_path = work / f"{grade_id}-ch{ch_num:02d}-flv-pack.html"
    pdf_path = work / f"{grade_id}-ch{ch_num:02d}-flv-pack.pdf"
    if REPRINT or not pdf_path.exists():
        html = print_document(f"{grade_id}-ch{ch_num}", topics)
        print(f"{grade_id} ch{ch_num}: printing {len(topics)} boards for FLV…")
        b.print_job(html, html_path, pdf_path, min_bytes=20_000, budget_ms=120000)
    else:
        print(f"{grade_id} ch{ch_num}: re-timing {len(needed)} FLV from printed boards")
    mapping = pages_for_topics(pdf_path, [t["id"] for t in topics])
    built = 0
    with tempfile.TemporaryDirectory(prefix="flv-pages-") as tmp:
        tmp_path = Path(tmp)
        for t in needed:
            pages = mapping.get(t["id"] or "", [])
            if not pages:
                print(f"  skip {t['id']} (no printed pages)")
                continue
            pngs, weights = render_pages(pdf_path, pages, tmp_path / t["id"], t["id"])
            if not pngs:
                continue
            dest = flv_path(t)
            total = speech_seconds(t.get("spokenUrdu") or t.get("readSeconds") and str(t.get("readSeconds")) or "")
            if t.get("readSeconds"):
                total = max(total, float(t["readSeconds"]))
            holds = page_holds(total, weights)
            encode_flv(pngs, dest, holds)
            built += 1
            print(
                f"  {t['id']} -> {dest.name} ({dest.stat().st_size} bytes, "
                f"{len(pngs)} page(s), {sum(holds):.0f}s TTS)"
            )
    return built


def pack_grade(grade: dict) -> int:
    built = 0
    total = 0
    for ch in grade["chapters"]:
        topics = ch["topics"]
        total += len(topics)
        built += pack_chapter(grade["id"], ch["num"], topics)
    if built == 0:
        have = sum(1 for ch in grade["chapters"] for t in ch["topics"] if flv_path(t).exists())
        print(f"{grade['id']}: packed {have}/{total} FLV on disk")
    return built


def main() -> int:
    if not JSON_PATH.exists() or not (WB / "whiteboard.css").exists():
        catalog.main()
    catalog_data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    FLV_OUT.mkdir(parents=True, exist_ok=True)
    built = 0
    for g in catalog_data["grades"]:
        built += pack_grade(g)
    n = sum(1 for g in catalog_data["grades"] for t in topics_of(catalog_data, g["id"]) if flv_path(t).exists())
    print(f"packed {built} new FLV · {n} on disk -> {FLV_OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
