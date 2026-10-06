#!/usr/bin/env python3
"""Turn the teach-yourself chapter HTML into short cinematic narration cards."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "booklets" / "src"
OUT = Path(__file__).resolve().parents[1] / "src" / "main" / "assets" / "scenes.json"
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
GRADES = (
    ("xi", "Computer Science XI", "Grade XI"),
    ("xii", "Computer Science XII", "Grade XII"),
)


def clean_title(text: str) -> str:
    text = text.replace("★", " ")
    text = re.sub(r"\bGolden\b", "", text)
    text = re.sub(r"\s+", " ", text).strip(" -–—")
    return text.strip()


def speakable(text: str) -> str:
    text = re.sub(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+", " ", text)
    text = (
        text.replace("—", ", ")
        .replace("–", " ")
        .replace("→", " to ")
        .replace("×", " times ")
        .replace("÷", " divided by ")
        .replace("≤", " is at most ")
        .replace("≥", " is at least ")
    )
    text = re.sub(r"[^A-Za-z0-9.,;:!?()'\"/+%\-\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def split_beats(text: str, limit: int = 520, max_beats: int = 3):
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return []
    sentences = re.split(r"(?<=[.!?])\s+", text)
    beats = []
    buf = ""
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        if buf and len(buf) + 1 + len(sentence) > limit:
            beats.append(buf.strip())
            buf = sentence
            if len(beats) >= max_beats:
                break
        else:
            buf = f"{buf} {sentence}".strip()
    if buf and len(beats) < max_beats:
        beats.append(buf.strip())
    return beats


class ChapterParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.skip_depth = 0
        self.in_urdu = 0
        self.in_opener = 0
        self.chapters = []
        self.current = None
        self.topic = None
        self.opener = []

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            return
        attr = dict(attrs)
        classes = set((attr.get("class") or "").split())
        self.stack.append((tag, classes, self.skip_depth, self.in_urdu, self.in_opener))
        if tag == "section" and "chapter" in classes:
            self.current = {
                "num": attr.get("data-num") or "",
                "title": clean_title(attr.get("data-title") or "Chapter"),
                "scenes": [],
            }
            self.chapters.append(self.current)
            self.opener = []
        if "ch-opener" in classes:
            self.in_opener += 1
        if tag == "div" and "topic" in classes and self.skip_depth == 0 and self.current is not None:
            self.topic = {"title": "", "parts": [], "urdu": []}
        if tag in {"pre", "svg", "script", "style", "table"} or "review" in classes:
            self.skip_depth += 1
        if "ur" in classes or attr.get("lang") == "ur":
            self.in_urdu += 1

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        while self.stack:
            start, classes, skip_before, urdu_before, opener_before = self.stack.pop()
            if start != tag:
                continue
            self.skip_depth = skip_before
            self.in_urdu = urdu_before
            self.in_opener = opener_before
            if "ch-opener" in classes and self.current is not None and not self.current["scenes"]:
                opener = clean_title(" ".join(self.opener))
                beats = split_beats(opener, limit=460, max_beats=1)
                if beats:
                    self.current["scenes"].append({
                        "title": self.current["title"],
                        "body": beats[0],
                        "urdu": "",
                        "speak": speakable(beats[0]),
                    })
                self.opener = []
            if tag == "div" and "topic" in classes and self.topic is not None and self.current is not None:
                self._close_topic()
            break

    def handle_data(self, data):
        text = re.sub(r"\s+", " ", data).strip()
        if not text or self.skip_depth or self.current is None:
            return
        if self.topic is not None:
            if any(frame[0] == "h2" for frame in self.stack):
                self.topic["title"] = clean_title(f"{self.topic['title']} {text}")
            elif self.in_urdu:
                self.topic["urdu"].append(text)
            else:
                self.topic["parts"].append(text)
        elif self.in_opener and not self.in_urdu and not any(frame[0] in {"h1", "h2"} for frame in self.stack):
            self.opener.append(text)

    def _close_topic(self):
        title = self.topic["title"] or self.current["title"]
        body = " ".join(self.topic["parts"])
        urdu = " ".join(self.topic["urdu"])
        urdu = re.sub(r"\s+", " ", urdu).strip()
        if len(urdu) > 280:
            urdu = urdu[:277].rsplit(" ", 1)[0] + "…"
        for index, beat in enumerate(split_beats(body)):
            spoken = speakable(beat)
            if len(spoken) < 12:
                continue
            self.current["scenes"].append({
                "title": title if index == 0 else f"{title} · {index + 1}",
                "body": beat,
                "urdu": urdu if index == 0 else "",
                "speak": spoken,
            })
        self.topic = None


def load_grade(folder: Path):
    files = sorted(folder.glob("ch*.html"), key=lambda p: int(re.search(r"\d+", p.stem).group()))
    final = folder / "final.html"
    if final.exists():
        files.append(final)
    chapters = []
    for path in files:
        parser = ChapterParser()
        parser.feed(path.read_text(encoding="utf-8"))
        parser.close()
        chapters.extend(ch for ch in parser.chapters if ch["scenes"])
    return chapters


def main():
    grades = []
    for key, title, label in GRADES:
        chapters = load_grade(SRC / key)
        grades.append({"id": key, "title": title, "label": label, "chapters": chapters})
        scenes = sum(len(ch["scenes"]) for ch in chapters)
        print(f"{key}: {len(chapters)} chapters, {scenes} scenes")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"grades": grades}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
