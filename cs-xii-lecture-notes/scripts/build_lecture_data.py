#!/usr/bin/env python3
"""Build processed lecture scenes from chapters_raw.json (PDF extract)."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "chapters_raw.json"
OUT = ROOT / "data" / "chapters.json"

URDU_RE = re.compile(r"[\u0600-\u06FF]")
SKIP_HEADINGS = re.compile(
    r"^(COMPUTER SCIENCE|TABLE OF CONTENTS|\d+\.\s+(Enhance|Promotes|Drives|End Users|Stakeholders))",
    re.I,
)
GOLDEN_MARK = re.compile(r"★|GOLDEN TOPIC", re.I)
MATH_PATTERNS = [
    (re.compile(r"\bO\s*\(\s*1\s*\)"), r"\\(O(1)\\)"),
    (re.compile(r"\bO\s*\(\s*log\s*n\s*\)", re.I), r"\\(O(\\log n)\\)"),
    (re.compile(r"\bO\s*\(\s*n\s*\^?\s*2\s*\)", re.I), r"\\(O(n^2)\\)"),
    (re.compile(r"\bO\s*\(\s*n\s*\)"), r"\\(O(n)\\)"),
    (re.compile(r"\bO\s*\(\s*n\s+log\s*n\s*\)", re.I), r"\\(O(n \\log n)\\)"),
    (re.compile(r"\bLIFO\b"), r"LIFO (Last-In, First-Out)"),
    (re.compile(r"\bFIFO\b"), r"FIFO (First-In, First-Out)"),
]

DIAGRAM_MAP = [
    (re.compile(r"sensory channel|fundamentals of human", re.I), "sensoryChannels"),
    (re.compile(r"traditional interaction|natural interaction", re.I), "tradVsNatural"),
    (re.compile(r"applications of hci", re.I), "hciApplications"),
    (re.compile(r"components of hci|types of user interaction", re.I), "hciComponents"),
    (re.compile(r"importance of hci", re.I), "hciImportance"),
    (re.compile(r"accessibility", re.I), "accessibility"),
    (re.compile(r"interaction problems|improving hci", re.I), "hciProblems"),
    (re.compile(r"user interface design|ui vs ux|wirefram", re.I), "uiUx"),
    (re.compile(r"figma|prototype", re.I), "figmaProto"),
    (re.compile(r"testing methods|a/b testing|evaluate hci", re.I), "testing"),
    (re.compile(r"trace table", re.I), "traceTable"),
    (re.compile(r"big o", re.I), "bigO"),
    (re.compile(r"data structure|stack|queue|linked list", re.I), "dataStructures"),
    (re.compile(r"lists\b|tuples|dictionaries|sets", re.I), "pythonCollections"),
    (re.compile(r"dataframe|pandas|sqlite", re.I), "dataAnalysis"),
    (re.compile(r"neural network|deep learning|machine learning", re.I), "mlNn"),
    (re.compile(r"entrepreneur|prototype development", re.I), "entrepreneurship"),
]


def split_bilingual(body: str) -> tuple[str, str]:
    eng_lines: list[str] = []
    urdu_lines: list[str] = []
    for line in body.splitlines():
        line = line.strip()
        if not line or line.startswith("👨"):
            continue
        if URDU_RE.search(line):
            urdu_lines.append(line)
        elif re.match(r"^[A-Za-z0-9#`\[\].,\"'():;/\\\-–—+=%$@!?&]", line) or line.startswith("Step "):
            eng_lines.append(line)
        elif len(line) > 2:
            eng_lines.append(line)
    english = "\n".join(eng_lines)
    urdu = "\n".join(urdu_lines)
    return english, urdu


def enhance_math(text: str) -> str:
    for pat, repl in MATH_PATTERNS:
        text = pat.sub(repl, text)
    return text


def pick_diagram(title: str, body: str) -> str | None:
    blob = f"{title}\n{body[:400]}"
    for pat, key in DIAGRAM_MAP:
        if pat.search(blob):
            return key
    return None


def scene_title(heading: str, body: str) -> str:
    first = body.split("\n", 1)[0].strip()
    if len(first) > len(heading) and len(first) < 100:
        return first
    return heading.strip()[:100]


def main() -> None:
    raw = json.loads(RAW.read_text(encoding="utf-8"))
    chapters_out = []

    for ch in raw:
        scenes = []
        for sec in ch["sections"]:
            heading = sec["heading"]
            body = sec["body"]
            if SKIP_HEADINGS.match(heading) and len(body) < 200:
                continue
            if heading == "COMPUTER SCIENCE" and "TABLE OF CONTENTS" in body:
                scenes.append(
                    {
                        "id": f"ch{ch['id']}-overview",
                        "title": "Course map & golden topics",
                        "golden": True,
                        "diagram": "courseMap",
                        "english": enhance_math(
                            "Welcome to the Ultimate Self-Taught Cinema Edition for CS XII (Sindh 2024–27). "
                            "Topics marked ★ are exam-critical. Start with golden scenes if motivation is low—"
                            "one small win builds momentum.\n\n"
                            + re.sub(r"👨.*", "", body.split("These notes")[0])
                        ),
                        "urdu": "CS XII کے لیے سینمائی لیکچر نوٹس — ★ والی topics امتحان کے لیے نہایت اہم ہیں۔",
                        "ttsEnglish": (
                            "Welcome. This is your self-taught cinema edition for Computer Science twelve. "
                            "If you feel reluctant, start with golden topics only. One small win today is enough."
                        ),
                        "ttsUrdu": (
                            "خوش آمدید۔ یہ CS XII کا س elf taught سینمائی edition ہے۔ "
                            "اگر دل نہیں لگ رہا تو صرف golden topics سے شروع کریں۔ آج ایک چھوٹی کامیابی کافی ہے۔"
                        ),
                    }
                )
                continue
            if len(body.strip()) < 60:
                continue

            english, urdu = split_bilingual(body)
            if len(english) < 40 and not sec.get("golden"):
                continue

            title = scene_title(heading, body)
            golden = sec.get("golden") or bool(GOLDEN_MARK.search(body[:300]))
            scene = {
                "id": f"ch{ch['id']}-{len(scenes)+1}",
                "title": title,
                "golden": golden,
                "diagram": pick_diagram(title, body),
                "english": enhance_math(english),
                "urdu": urdu,
                "ttsEnglish": re.sub(r"\s+", " ", english)[:1200],
                "ttsUrdu": urdu[:1200] if urdu else "",
            }
            scenes.append(scene)

        chapters_out.append(
            {
                "id": ch["id"],
                "title": ch["title"].replace(" BILINGUAL TEACHER'S EDITION", "").strip(),
                "scenes": scenes,
            }
        )

    OUT.write_text(json.dumps(chapters_out, ensure_ascii=False, indent=2), encoding="utf-8")
    total = sum(len(c["scenes"]) for c in chapters_out)
    golden = sum(1 for c in chapters_out for s in c["scenes"] if s["golden"])
    print(f"Wrote {OUT} — {len(chapters_out)} chapters, {total} scenes, {golden} golden")


if __name__ == "__main__":
    main()
