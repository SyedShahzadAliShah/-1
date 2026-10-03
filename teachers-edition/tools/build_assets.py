#!/usr/bin/env python3
"""Turn authored content/pNNN.json into the app assets.

  * synthesises Urdu narration for every block / table row with a neural Urdu voice (edge-tts)
  * encodes it to Opus/Ogg (small, natively supported by Android)
  * writes app/src/main/assets/content/pNNN.json (content + audio asset paths) and index.json

Usage: build_assets.py [--voice ur-PK-UzmaNeural] [--rate -5%] [--no-audio] [--pages 1 2 3]
Synthesised clips are cached in work/audio_cache keyed by (voice, rate, text).
"""
import argparse
import asyncio
import glob
import hashlib
import json
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
ASSETS = os.path.join(ROOT, "app", "src", "main", "assets")
CACHE = os.path.join(ROOT, "work", "audio_cache")

CHAPTERS = [
    (1, "Computer Systems", 1, 26),
    (2, "Computational Thinking & Algorithm", 27, 43),
    (3, "Programming Fundamentals", 44, 69),
    (4, "Data and Analysis", 70, 95),
    (5, "Application and Impacts of Computing", 96, 110),
    (6, "Digital Literacy", 111, 127),
]


def clean_for_tts(text):
    text = text.replace("\u200b", "").replace("\u200e", "").replace("\u200f", "")
    text = re.sub(r"[\"“”'‘’*_#`|\\\[\]{}<>]", " ", text)
    text = text.replace("(", "، ").replace(")", "، ").replace("/", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def units(page, block_idx, block):
    """Yield (key, text, container, field) for each audio unit in a block."""
    if block["t"] == "table":
        for r, row in enumerate(block["rows"]):
            yield f"p{page:03d}_{block_idx:02d}_{r:02d}", row["ur"], row
    else:
        yield f"p{page:03d}_{block_idx:02d}", block["ur"], block


async def synth(jobs, voice, rate, concurrency=6):
    import edge_tts

    sem = asyncio.Semaphore(concurrency)
    done = 0

    async def one(path, text):
        nonlocal done
        async with sem:
            for attempt in range(6):
                try:
                    await edge_tts.Communicate(text, voice, rate=rate).save(path + ".part")
                    os.replace(path + ".part", path)
                    break
                except Exception as e:  # noqa: BLE001
                    if attempt == 5:
                        raise
                    await asyncio.sleep(2 * (attempt + 1))
            done += 1
            if done % 50 == 0:
                print(f"  synthesised {done}/{len(jobs)}", flush=True)

    await asyncio.gather(*(one(p, t) for p, t in jobs))


def encode(src, dst):
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-ac", "1", "-c:a", "libopus",
         "-b:a", "20k", "-application", "voip", "-vbr", "on", dst],
        check=True,
    )


def page_label(page):
    ext = open(os.path.join(ROOT, "work", "extract", f"p{page:03d}.txt")).read()
    m = re.search(r"\]\s*Page (\d+)\s*$", ext, re.M)
    return int(m.group(1)) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--voice", default="ur-PK-UzmaNeural")
    ap.add_argument("--rate", default="-5%")
    ap.add_argument("--no-audio", action="store_true")
    ap.add_argument("--pages", type=int, nargs="*")
    args = ap.parse_args()

    os.makedirs(CACHE, exist_ok=True)
    out_content = os.path.join(ASSETS, "content")
    out_audio = os.path.join(ASSETS, "audio")
    os.makedirs(out_content, exist_ok=True)
    os.makedirs(out_audio, exist_ok=True)

    files = sorted(glob.glob(os.path.join(ROOT, "content", "p*.json")))
    if args.pages:
        files = [f for f in files if int(os.path.basename(f)[1:4]) in args.pages]

    pages, jobs, plan = [], {}, []
    for f in files:
        data = json.load(open(f, encoding="utf-8"))
        page = data["page"]
        for bi, block in enumerate(data["blocks"]):
            for key, ur, container in units(page, bi, block):
                text = clean_for_tts(ur)
                digest = hashlib.sha1(f"{args.voice}|{args.rate}|{text}".encode()).hexdigest()
                mp3 = os.path.join(CACHE, digest + ".mp3")
                if not os.path.exists(mp3):
                    jobs[mp3] = text
                plan.append((key, mp3))
                container["a"] = f"audio/{key}.ogg"
        pages.append(data)

    print(f"{len(plan)} audio units, {len(jobs)} to synthesise")
    if not args.no_audio:
        if jobs:
            asyncio.run(synth(list(jobs.items()), args.voice, args.rate))
        for key, mp3 in plan:
            dst = os.path.join(out_audio, key + ".ogg")
            if not os.path.exists(dst) or os.path.getmtime(dst) < os.path.getmtime(mp3):
                encode(mp3, dst)

    index_pages = []
    for data in pages:
        page = data["page"]
        with open(os.path.join(out_content, f"p{page:03d}.json"), "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, separators=(",", ":"))
        heads = [b["en"] for b in data["blocks"] if b["t"] in ("title", "h1")]
        subs = [b["en"] for b in data["blocks"] if b["t"] == "h2"]
        golden = any(b["t"] == "badge" for b in data["blocks"])
        chapter = next(c[0] for c in CHAPTERS if c[2] <= page <= c[3])
        index_pages.append(
            {"page": page, "label": page_label(page), "chapter": chapter, "heads": heads,
             "subs": subs, "golden": golden}
        )
    index = {
        "title": "Computer Science XI",
        "subtitle": "Bilingual Teacher's Edition",
        "chapters": [{"n": n, "title": t, "first": a, "last": b} for n, t, a, b in CHAPTERS],
        "pages": index_pages,
        "voice": args.voice,
    }
    with open(os.path.join(ASSETS, "index.json"), "w", encoding="utf-8") as fh:
        json.dump(index, fh, ensure_ascii=False, separators=(",", ":"))
    print("wrote", len(index_pages), "pages")


if __name__ == "__main__":
    sys.exit(main())
