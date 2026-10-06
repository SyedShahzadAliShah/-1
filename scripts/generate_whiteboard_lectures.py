#!/usr/bin/env python3
"""Build bilingual whiteboard lecture JSON from the CS XI / XII teach-yourself booklets."""

from __future__ import annotations

import json
import re
from pathlib import Path

XI_PAGES = {
    1: range(6, 48),
    2: range(48, 87),
    3: range(87, 140),
    4: range(140, 160),
    5: range(160, 189),
    6: range(189, 224),
}
XII_PAGES = {
    1: range(6, 40),
    2: range(40, 91),
    3: range(91, 140),
    4: range(140, 155),
    5: range(155, 193),
    6: range(193, 233),
}

XI_CHAPTERS = [
    (1, "Computer Systems", "کمپیوٹر سسٹمز"),
    (2, "Computational Thinking & Algorithms", "کمپیوٹیشنل سوچ اور الگورتھم"),
    (3, "Programming Fundamentals", "پروگرامنگ کی بنیادی باتیں"),
    (4, "Data and Analysis", "ڈیٹا اور تجزیہ"),
    (5, "Application and Impacts of Computing", "کمپیوٹنگ کے اثرات"),
    (6, "Digital Literacy", "ڈیجیٹل خواندگی"),
]
XII_CHAPTERS = [
    (1, "Computer Systems (HCI)", "کمپیوٹر سسٹمز — انسانی تعامل"),
    (2, "Computational Thinking & Algorithms", "کمپیوٹیشنل سوچ اور الگورتھم"),
    (3, "Programming Fundamentals", "پروگرامنگ کی بنیادی باتیں"),
    (4, "Data and Analysis", "ڈیٹا اور تجزیہ"),
    (5, "Application and Impacts of Computing", "کمپیوٹنگ کے اثرات"),
    (6, "Entrepreneurship in the Digital Age", "ڈیجیٹل دور میں کاروبار"),
]

URDU_TITLES = {
    "Discrete and Continuous Quantities": "الگ اور مسلسل مقداریں",
    "Introduction to Digital Systems": "ڈیجیٹل نظام کا تعارف",
    "Analog and Digital Signals": "اینالاگ اور ڈیجیٹل سگنل",
    "Boolean Algebra": "بولین الجبرا",
    "Boolean Operations": "بولین عمل",
    "Truth Tables": "سچائی جدولی",
    "Logic Gates": "لاجک گیٹس",
    "Universal Logic Gates": "یونیورسل لاجک گیٹس",
    "Advanced Logic Gates": "ایڈوانسڈ لاجک گیٹس",
    "Karnaugh Maps": "کارنو نقشے",
    "Software Development Life Cycle": "سافٹ ویئر ڈیولپمنٹ لائف سائیکل",
    "Waterfall": "واٹر فال ماڈل",
    "Agile": "ایجائل ماڈل",
    "OSI": "او ایس آئی ماڈل",
    "TCP/IP": "ٹی سی پی / آئی پی ماڈل",
}

DIAGRAM_RULES = [
    (r"analog|digital signal|sine wave|square wave", "analog_digital"),
    (r"\bNAND\b", "nand_gate"),
    (r"\bNOR\b", "nor_gate"),
    (r"\bXOR\b|XNOR|exclusive", "xor_gate"),
    (r"\bAND gate\b|\bAND operation\b", "and_gate"),
    (r"\bOR gate\b|\bOR operation\b", "or_gate"),
    (r"\bNOT gate\b|\bNOT operation\b", "not_gate"),
    (r"truth table", "truth_table"),
    (r"k-map|karnaugh", "kmap"),
    (r"sdlc|software development life", "sdlc"),
    (r"waterfall", "waterfall"),
    (r"\bagile\b|sprint", "agile"),
    (r"\bosi\b", "osi"),
    (r"tcp/ip|tcp ip", "tcpip"),
    (r"bubble sort", "bubble_sort"),
    (r"selection sort", "selection_sort"),
    (r"binary search", "binary_search"),
    (r"linear search", "linear_search"),
    (r"decomposition|computational thinking", "ct_pillars"),
    (r"if-else|selection statement", "if_else"),
    (r"for loop|while loop|repetition", "loop"),
    (r"er-model|entity relationship|entities", "er_diagram"),
    (r"primary key|foreign key|dbms|database", "db_table"),
    (r"iot|internet of things", "iot"),
    (r"artificial intelligence|\bAI\b|machine learning|neural", "ai_net"),
    (r"stack\b", "stack"),
    (r"queue\b", "queue"),
    (r"linked list", "linked_list"),
    (r"\btree\b|graph", "tree"),
    (r"\bmvp\b|prototype", "mvp"),
    (r"hci|sensory|interaction", "hci"),
    (r"big o|efficiency", "big_o"),
]


def clean(text: str) -> str:
    text = (
        text.replace("", ":")
        .replace("", "(")
        .replace("", ")")
        .replace("", "+")
        .replace("", "=")
        .replace("", "—")
        .replace("", "-")
        .replace("", "→")
        .replace("", "×")
        .replace("", "1. ")
        .replace("", "2. ")
        .replace("", "3. ")
        .replace("", "4. ")
        .replace("", "5. ")
        .replace("", "")
        .replace("\u00a0", " ")
    )
    text = re.sub(r"[\ue000-\uf8ff]", " ", text)
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text)
    text = text.replace("★ Golden", "★").replace("★Golden", "★")
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def mostly_english(line: str) -> bool:
    letters = re.findall(r"[A-Za-z\u0600-\u06FF]", line)
    if not letters:
        return False
    latin = sum(1 for ch in letters if ("A" <= ch <= "Z") or ("a" <= ch <= "z"))
    return latin / len(letters) >= 0.55


def english_lines(block: str) -> list[str]:
    out = []
    for raw in block.splitlines():
        line = clean(raw)
        if not line:
            continue
        if line.startswith("===== PAGE"):
            continue
        if line.isdigit() and len(line) <= 3:
            continue
        if not mostly_english(line):
            continue
        if line in {"LEARN IT", "WORKED EXAMPLE", "REMEMBER IT", "COMMON MISTAKE", "EXAM TIP", "CHECK YOURSELF"}:
            continue
        out.append(line)
    return out


def join_lines(lines: list[str]) -> str:
    text = " ".join(lines)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+([,.;:)])", r"\1", text)
    return text.strip(" -")


def split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"“])", text)
    sentences = []
    for part in parts:
        part = part.strip()
        if len(part) < 18:
            if sentences:
                sentences[-1] = (sentences[-1] + " " + part).strip()
            continue
        if len(part) > 220:
            chunks = re.split(r";\s+", part)
            sentences.extend(c.strip() for c in chunks if len(c.strip()) > 12)
        else:
            sentences.append(part)
    return sentences[:8]


def pick_diagram(*texts: str) -> str | None:
    blob = " ".join(texts).lower()
    for pattern, name in DIAGRAM_RULES:
        if re.search(pattern, blob):
            return name
    return None


def urdu_title(english: str) -> str:
    for key, ur in URDU_TITLES.items():
        if key.lower() in english.lower():
            return ur
    return english


def urdu_speech(title: str, points: list[str], remember: str, mistake: str) -> str:
    bits = [
        f"السلام علیکم۔ آج کا موضوع {urdu_title(title)} ہے۔",
        "میں وائٹ بورڈ پر سبق لکھ رہا ہوں۔ غور سے سنیں، رک کر نوٹس بنائیں، اور مثال کاغذ پر خود حل کریں۔",
    ]
    if points:
        bits.append("اہم بات بورڈ پر لکھی جا رہی ہے۔ تعریف، وضاحت اور مثال یاد رکھیں۔")
    if remember:
        bits.append("سنہری نکتہ یاد رکھیں — امتحان میں یہی بات اکثر پوچھی جاتی ہے۔")
    if mistake:
        bits.append("عام غلطی سے بچیں جو طلبہ بورڈ پیپر میں کرتے ہیں۔")
    bits.append("سبق کے آخر میں خود کو پرکھیں۔")
    return " ".join(bits)


def section_map(block: str) -> dict[str, list[str]]:
    markers = [
        "WORKED EXAMPLE",
        "REMEMBER IT",
        "COMMON MISTAKE",
        "EXAM TIP",
        "CHECK YOURSELF",
        "GOLDEN TOPIC",
    ]
    idxs = []
    for m in markers:
        pos = block.find(m)
        if pos >= 0:
            idxs.append((pos, m))
    idxs.sort()
    learn_end = idxs[0][0] if idxs else len(block)
    sections = {"LEARN IT": english_lines(block[:learn_end])}
    for i, (pos, name) in enumerate(idxs):
        end = idxs[i + 1][0] if i + 1 < len(idxs) else len(block)
        sections[name] = english_lines(block[pos:end])
    return sections


def bullets_from(text: str, limit: int = 5) -> list[str]:
    sents = split_sentences(text)
    out = []
    for s in sents:
        s = s.strip(" -")
        if len(s) < 20:
            continue
        if s.lower().startswith("the main explanation"):
            continue
        out.append(s[:180])
        if len(out) >= limit:
            break
    return out


def page_of(block_prefix: str) -> int:
    pages = [int(p) for p in re.findall(r"===== PAGE (\d+) =====", block_prefix)]
    return pages[-1] if pages else 1


def chapter_for(page: int, table: dict[int, range]) -> int:
    for num, rng in table.items():
        if page in rng:
            return num
    return 1


def heading_from(prev: str) -> str:
    lines = [clean(ln) for ln in prev.splitlines() if clean(ln)]
    for line in reversed(lines):
        if line.startswith("===== PAGE") or line.isdigit():
            continue
        if not mostly_english(line):
            continue
        if line in {"Contents", "LEARN IT"}:
            continue
        if len(line) < 8 or len(line) > 110:
            continue
        return line
    return "Lecture topic"


def make_lecture(class_id: str, code: str, title: str, golden: bool, sections: dict[str, list[str]]) -> dict:
    learn = join_lines(sections.get("LEARN IT", []))
    worked = join_lines(sections.get("WORKED EXAMPLE", []))
    remember = join_lines(sections.get("REMEMBER IT", []))
    mistake = join_lines(sections.get("COMMON MISTAKE", []))
    exam = join_lines(sections.get("EXAM TIP", []))
    check = join_lines(sections.get("CHECK YOURSELF", []))

    learn_bullets = bullets_from(learn, 6)
    if not learn_bullets:
        return {}

    diagram = pick_diagram(title, learn, worked)
    segments = []

    intro_actions = [
        {"type": "heading", "text": title[:70]},
        {"type": "note", "text": "Animated whiteboard · listen and watch the marker"},
    ]
    if golden:
        intro_actions.append({"type": "callout", "kind": "exam", "text": "★ Golden topic — high-yield for Sindh board exams."})
    if diagram:
        intro_actions.append({"type": "diagram", "name": diagram})
    segments.append(
        {
            "speakEn": f"Let's open the whiteboard for {title}. Watch the marker and listen carefully.",
            "speakUr": urdu_speech(title, learn_bullets[:1], "", ""),
            "clear": True,
            "actions": intro_actions,
        }
    )

    first_chunk = learn_bullets[:3]
    second_chunk = learn_bullets[3:]
    segments.append(
        {
            "speakEn": " ".join(first_chunk),
            "speakUr": urdu_speech(title, first_chunk, "", ""),
            "clear": False,
            "actions": [{"type": "subheading", "text": "Learn it"}]
            + [{"type": "bullet", "text": b} for b in first_chunk],
        }
    )
    if second_chunk:
        segments.append(
            {
                "speakEn": " ".join(second_chunk),
                "speakUr": urdu_speech(title, second_chunk, "", ""),
                "clear": False,
                "actions": [{"type": "bullet", "text": b} for b in second_chunk],
            }
        )

    if worked:
        w_sents = bullets_from(worked, 4)
        if w_sents:
            actions = [{"type": "subheading", "text": "Worked example"}] + [
                {"type": "bullet", "text": s} for s in w_sents
            ]
            if any(k in worked.lower() for k in ["print", "def ", "for ", "import ", "select "]):
                code_lines = [ln[:60] for ln in re.findall(r"(print\([^)]+\)|def [^\n]+|for [^\n]+|import [^\n]+)", worked)][:4]
                if code_lines:
                    actions.append({"type": "code", "lines": code_lines})
            segments.append(
                {
                    "speakEn": "Here is a worked example. Pause the lecture and try it on paper before you continue. "
                    + " ".join(w_sents[:2]),
                    "speakUr": "اب ایک حل شدہ مثال۔ وقفہ کر کے کاغذ پر خود کوشش کریں۔",
                    "clear": False,
                    "actions": actions,
                }
            )

    closing_actions = []
    speak_bits = []
    if remember:
        r = bullets_from(remember, 2) or [remember[:180]]
        closing_actions.append({"type": "callout", "kind": "remember", "text": r[0]})
        speak_bits.append("Memory trick: " + r[0])
    if mistake:
        m = bullets_from(mistake, 2) or [mistake[:180]]
        closing_actions.append({"type": "callout", "kind": "mistake", "text": m[0]})
        speak_bits.append("Common mistake: " + m[0])
    if exam:
        e = bullets_from(exam, 2) or [exam[:180]]
        closing_actions.append({"type": "callout", "kind": "exam", "text": e[0]})
        speak_bits.append("Exam tip: " + e[0])
    if check:
        q = bullets_from(check, 3)
        if q:
            closing_actions.append({"type": "subheading", "text": "Check yourself"})
            closing_actions.extend({"type": "bullet", "text": item} for item in q[:3])
            speak_bits.append("Pause and answer the check-yourself questions on the board.")
    if closing_actions:
        segments.append(
            {
                "speakEn": " ".join(speak_bits) or "Review the board, then try the next lecture.",
                "speakUr": urdu_speech(title, [], remember[:120], mistake[:120]),
                "clear": False,
                "actions": closing_actions,
            }
        )

    words = sum(len(s["speakEn"].split()) for s in segments)
    return {
        "id": f"{class_id}-{code}",
        "code": code,
        "titleEn": title[:80],
        "titleUr": urdu_title(title)[:80],
        "golden": golden,
        "durationHintSec": max(55, min(160, int(words / 2.2) + 20)),
        "segments": segments,
    }


def parse_book(path: Path, class_id: str, chapter_meta: list[tuple[int, str, str]], page_table: dict[int, range]) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    parts = re.split(r"LEARN IT\n", text)
    chapters: dict[int, dict] = {
        n: {"id": f"{class_id}-ch{n}", "number": n, "titleEn": en, "titleUr": ur, "lectures": []}
        for n, en, ur in chapter_meta
    }
    for i, block in enumerate(parts[1:], 1):
        prefix = parts[i - 1]
        heading = heading_from(prefix)
        if heading.lower().startswith("the main explanation") or "coloured boxes" in heading.lower():
            continue
        if heading.lower() in {"contents", "how to use this booklet"}:
            continue
        learn_preview = join_lines(english_lines(block[:400]))
        if learn_preview.lower().startswith("the main explanation"):
            continue
        page = page_of(prefix + "\n" + block[:200])
        ch = chapter_for(page, page_table)
        sections = section_map(block)
        golden = "★" in heading or "golden" in heading.lower() or "★ Golden" in prefix[-200:]
        code = f"{ch}.{len(chapters[ch]['lectures']) + 1:02d}"
        m = re.search(r"(\d+\.\d+(?:\.\d+)?)", heading)
        if m:
            code = m.group(1)
        lecture = make_lecture(class_id, code, heading, golden, sections)
        if lecture:
            chapters[ch]["lectures"].append(lecture)

    out = []
    for n, _en, _ur in chapter_meta:
        ch = chapters[n]
        if ch["lectures"]:
            out.append(ch)
    return out


def welcome(class_id: str, title_en: str, title_ur: str, year: str) -> dict:
    return {
        "id": f"{class_id}-welcome",
        "number": 0,
        "titleEn": "How to learn on this whiteboard",
        "titleUr": "اس وائٹ بورڈ پر کیسے سیکھیں",
        "lectures": [
            {
                "id": f"{class_id}-welcome-1",
                "code": "0.1",
                "titleEn": "Welcome to the self-taught whiteboard",
                "titleUr": "خوش آمدید — خود سیکھیں وائٹ بورڈ",
                "golden": True,
                "durationHintSec": 70,
                "segments": [
                    {
                        "speakEn": f"Assalamu alaikum. This is your animated whiteboard for {title_en}, based on the Ultimate Teach Yourself booklet and the new Sindh curriculum {year}. I will write as I speak.",
                        "speakUr": f"السلام علیکم۔ یہ {title_ur} کا متحرک وائٹ بورڈ لیکچر ہے۔ میں بولتے ہوئے بورڈ پر لکھوں گا۔ سندھ کے نئے نصاب {year} پر مبنی۔",
                        "clear": True,
                        "actions": [
                            {"type": "heading", "text": title_en},
                            {"type": "bullet", "text": "English + Urdu voice · marker writes with you"},
                            {"type": "bullet", "text": "★ Golden topics are high-yield exam questions"},
                            {"type": "bullet", "text": "Pause, copy the board, then tap Next"},
                            {"type": "diagram", "name": "ct_pillars"},
                        ],
                    },
                    {
                        "speakEn": "Study method: preview the title, watch one lecture, copy the worked example on paper, then answer check-yourself from memory. Spaced review after one day, three days, and seven days.",
                        "speakUr": "طریقہ: عنوان دیکھیں، لیکچر سنیں، مثال کاغذ پر لکھیں، سوالات یاد سے حل کریں۔ ایک، تین اور سات دن بعد دہرائیں۔",
                        "clear": False,
                        "actions": [
                            {"type": "subheading", "text": "Board-exam method"},
                            {"type": "bullet", "text": "Define + explain + example for short questions"},
                            {"type": "bullet", "text": "Tables for differentiate questions"},
                            {"type": "bullet", "text": "Draw and label gates, diagrams, charts"},
                            {"type": "callout", "kind": "exam", "text": "Marks are given for working, not only the final answer."},
                        ],
                    },
                ],
            }
        ],
    }


def main() -> None:
    uploads = Path("/home/ubuntu/.cursor/projects/workspace/uploads")
    xi_src = uploads / "CS-XI-Ultimate-Teach-Yourself-Booklet-compressed_b94a.pdf"
    # Use pre-extracted text (generated beside the PDFs in /tmp)
    xi_txt = Path("/tmp/xi_extract.txt")
    xii_txt = Path("/tmp/xii_extract.txt")
    if not xi_txt.exists() or not xii_txt.exists():
        raise SystemExit("Missing /tmp/xi_extract.txt or /tmp/xii_extract.txt")

    xi_chapters = [welcome("xi", "Computer Science XI", "کمپیوٹر سائنس یازدہم", "2026")]
    xi_chapters.extend(parse_book(xi_txt, "xi", XI_CHAPTERS, XI_PAGES))
    xii_chapters = [welcome("xii", "Computer Science XII", "کمپیوٹر سائنس بارہویں", "2025-27")]
    xii_chapters.extend(parse_book(xii_txt, "xii", XII_CHAPTERS, XII_PAGES))

    data = {
        "version": "1.0.0",
        "classes": [
            {
                "id": "xi",
                "titleEn": "Computer Science XI",
                "titleUr": "کمپیوٹر سائنس یازدہم",
                "subtitleEn": "Sindh Curriculum 2026 · Teach Yourself",
                "subtitleUr": "سندھ نصاب 2026 · خود سیکھیں",
                "chapters": xi_chapters,
            },
            {
                "id": "xii",
                "titleEn": "Computer Science XII",
                "titleUr": "کمپیوٹر سائنس بارہویں",
                "subtitleEn": "Sindh Curriculum 2025–27 · Teach Yourself",
                "subtitleUr": "سندھ نصاب 2025–27 · خود سیکھیں",
                "chapters": xii_chapters,
            },
        ],
    }

    out = Path("/workspace/app/src/main/assets/lectures/curriculum.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    n_lec = sum(len(ch["lectures"]) for c in data["classes"] for ch in c["chapters"])
    n_seg = sum(
        len(lec["segments"])
        for c in data["classes"]
        for ch in c["chapters"]
        for lec in ch["lectures"]
    )
    print(f"Wrote {out} lectures={n_lec} segments={n_seg} bytes={out.stat().st_size}")


if __name__ == "__main__":
    main()
