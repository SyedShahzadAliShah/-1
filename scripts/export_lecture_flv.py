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
FORCE = os.environ.get("FORCE_FLV") == "1"


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
            f'<div class="flv-mark">FLV:{mark}</div>'
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
.flv-mark {{ font: 9px/1.2 ui-monospace, monospace; color: #64748b; margin: 0 0 6px; }}
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


def hold_seconds(n_pages: int) -> float:
    if n_pages <= 1:
        return 6.0
    return max(2.2, min(3.4, 14.0 / n_pages))


def encode_flv(pngs: list[Path], dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    hold = hold_seconds(len(pngs))
    vf = "scale=720:-2:flags=lanczos,scale=720:trunc(ih/2)*2,fps=12,format=yuv420p"
    with tempfile.TemporaryDirectory(prefix="flv-enc-") as tmp:
        tmp_path = Path(tmp)
        inputs: list[str] = []
        for i, png in enumerate(pngs):
            clip = tmp_path / f"c{i:02d}.flv"
            subprocess.run(
                [
                    FFMPEG, "-y", "-loop", "1", "-t", f"{hold:.2f}", "-i", str(png),
                    "-f", "lavfi", "-t", f"{hold:.2f}", "-i", "anullsrc=r=44100:cl=mono",
                    "-vf", vf, "-c:v", "libx264", "-preset", "veryfast", "-crf", "29",
                    "-c:a", "aac", "-b:a", "32k", "-shortest", "-pix_fmt", "yuv420p",
                    "-f", "flv", str(clip),
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
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
        for tid in topic_ids:
            if f"FLV:{tid}" in text:
                hit = tid
                break
        if hit:
            current = hit
        if current:
            found[current].append(i)
    doc.close()
    return found


def render_pages(pdf_path: Path, indexes: list[int], dest_dir: Path) -> list[Path]:
    import pymupdf

    dest_dir.mkdir(parents=True, exist_ok=True)
    doc = pymupdf.open(pdf_path)
    zoom = pymupdf.Matrix(1.45, 1.45)
    pngs = []
    for n, idx in enumerate(indexes, 1):
        if idx < 0 or idx >= doc.page_count:
            continue
        png = dest_dir / f"{n:02d}.png"
        doc[idx].get_pixmap(matrix=zoom, alpha=False).save(png)
        pngs.append(png)
    doc.close()
    return pngs


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
    needed = []
    for t in topics:
        dest = flv_path(t)
        if dest.exists() and dest.stat().st_size > 4000 and not FORCE:
            continue
        needed.append(t)
    if not needed:
        return 0
    html = print_document(f"{grade_id}-ch{ch_num}", topics)
    work = ROOT / "booklets" / "output"
    work.mkdir(parents=True, exist_ok=True)
    html_path = work / f"{grade_id}-ch{ch_num:02d}-flv-pack.html"
    pdf_path = work / f"{grade_id}-ch{ch_num:02d}-flv-pack.pdf"
    print(f"{grade_id} ch{ch_num}: printing {len(topics)} boards for FLV…")
    b.print_job(html, html_path, pdf_path, min_bytes=20_000, budget_ms=120000)
    mapping = pages_for_topics(pdf_path, [t["id"] for t in topics])
    built = 0
    with tempfile.TemporaryDirectory(prefix="flv-pages-") as tmp:
        tmp_path = Path(tmp)
        for t in needed:
            pages = mapping.get(t["id"] or "", [])
            if not pages:
                print(f"  skip {t['id']} (no printed pages)")
                continue
            pngs = render_pages(pdf_path, pages, tmp_path / t["id"])
            if not pngs:
                continue
            dest = flv_path(t)
            encode_flv(pngs, dest)
            built += 1
            print(f"  {t['id']} -> {dest.name} ({dest.stat().st_size} bytes, {len(pngs)} page(s))")
    return built


def pack_grade(grade: dict) -> int:
    built = 0
    total = 0
    for ch in grade["chapters"]:
        topics = ch["topics"]
        total += len(topics)
        built += pack_chapter(grade["id"], ch["num"], topics)
    if built == 0:
        print(f"{grade['id']}: {total} FLV already packed")
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
