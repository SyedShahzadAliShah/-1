#!/usr/bin/env python3
"""Turn the teach-yourself chapter HTML into cinematic cards with math and diagrams."""
import json
import re
from html import unescape
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
FIGURE_RE = re.compile(r'<figure\s+class="diagram">.*?</figure>', re.S)
SUP_SUB_RE = re.compile(r"([A-Za-z0-9]*)<(sup|sub)>(.*?)</\2>", re.S | re.I)
UNICODE_SUP_RE = re.compile(r"([A-Za-z0-9]+)([⁰¹²³⁴⁵⁶⁷⁸⁹]+)")
CAPTION_RE = re.compile(r"<figcaption>(.*?)</figcaption>", re.S)
MATH_RE = re.compile(r"\\\((.+?)\\\)")
SUP_DIGITS = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")


def clean_title(text: str) -> str:
    text = text.replace("★", " ")
    text = re.sub(r"\bGolden\b", "", text)
    text = re.sub(r"\s+", " ", text).strip(" -–—")
    return text.strip()


def tex_fragment(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = unescape(text)
    text = text.replace("−", "-").replace("–", "-").replace("—", "-")
    text = text.replace("\\", r"\textbackslash ")
    for char, escaped in (
        ("{", r"\{"),
        ("}", r"\}"),
        ("#", r"\#"),
        ("%", r"\%"),
        ("&", r"\&"),
        ("_", r"\_"),
        ("^", r"\^{}"),
        ("~", r"\~{}"),
    ):
        text = text.replace(char, escaped)
    return re.sub(r"\s+", " ", text).strip()


def convert_math(html: str) -> str:
    def script(match: re.Match) -> str:
        base, kind, inner = match.group(1), match.group(2).lower(), tex_fragment(match.group(3))
        if not inner:
            return base
        piece = f"^{{{inner}}}" if kind == "sup" else f"_{{{inner}}}"
        if base:
            return f"\\({base}{piece}\\)"
        return f"\\({piece}\\)"

    def power(match: re.Match) -> str:
        base, digits = match.group(1), match.group(2).translate(SUP_DIGITS)
        return f"\\({base}^{{{digits}}}\\)"

    html = SUP_SUB_RE.sub(script, html)
    return UNICODE_SUP_RE.sub(power, html)


def prepare_html(html: str):
    figures = []

    def take_figure(match: re.Match) -> str:
        raw = CAPTION_RE.sub(
            lambda cap: "<figcaption>" + convert_math(cap.group(1)) + "</figcaption>",
            match.group(0),
            count=1,
        )
        figures.append(raw)
        return f"<!--FIG{len(figures) - 1}-->"

    html = FIGURE_RE.sub(take_figure, html)
    return convert_math(html), figures


def caption_text(figure: str) -> str:
    match = CAPTION_RE.search(figure)
    if not match:
        return ""
    text = re.sub(r"<[^>]+>", " ", match.group(1))
    return re.sub(r"\s+", " ", unescape(text)).strip()


def verbalize(text: str) -> str:
    def say(match: re.Match) -> str:
        expr = match.group(1).strip()
        sup = re.match(r"^([A-Za-z0-9]+)\^\{([^{}]+)\}$", expr)
        sub = re.match(r"^([A-Za-z0-9]+)_\{([^{}]+)\}$", expr)
        if sup:
            base, exp = sup.group(1), verbal_exp(sup.group(2))
            if exp == "2":
                return f"{base} squared"
            if exp == "3":
                return f"{base} cubed"
            return f"{base} to the power {exp}"
        if sub:
            base, exp = sub.group(1), verbal_exp(sub.group(2))
            if base.lower() == "log":
                return f"log base {exp}"
            return f"{base} sub {exp}"
        return expr

    return MATH_RE.sub(say, text)


def verbal_exp(exp: str) -> str:
    exp = exp.replace("-", " minus ").replace("+", " plus ")
    return re.sub(r"\s+", " ", exp).strip()


def speakable(text: str) -> str:
    text = verbalize(text)
    text = re.sub(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]+", " ", text)
    text = (
        text.replace("—", ", ")
        .replace("–", " ")
        .replace("→", " to ")
        .replace("×", " times ")
        .replace("÷", " divided by ")
        .replace("≤", " is at most ")
        .replace("≥", " is at least ")
        .replace("≈", " about ")
        .replace("=", " equals ")
        .replace("²", " squared")
        .replace("³", " cubed")
    )
    text = re.sub(r"[^A-Za-z0-9.,;:!?()'\"/+%\-\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def join_parts(parts):
    text = ""
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if not text:
            text = part
        elif part[0] in ".,;:!?)]}":
            text += part
        else:
            text += " " + part
    return re.sub(r"\s+", " ", text).strip()


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
    def __init__(self, figures):
        super().__init__(convert_charrefs=True)
        self.figure_bank = figures
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
            self.topic = {"title": "", "parts": [], "urdu": [], "figures": [], "captions": []}
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
                opener = clean_title(join_parts(self.opener))
                beats = split_beats(opener, limit=460, max_beats=1)
                if beats:
                    self.current["scenes"].append({
                        "title": self.current["title"],
                        "body": beats[0],
                        "urdu": "",
                        "speak": speakable(beats[0]),
                        "figures": [],
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

    def handle_comment(self, data):
        match = re.match(r"FIG(\d+)$", data.strip())
        if not match or self.skip_depth or self.topic is None:
            return
        figure = self.figure_bank[int(match.group(1))]
        self.topic["figures"].append(figure)
        caption = caption_text(figure)
        if caption:
            self.topic["captions"].append(caption)

    def _close_topic(self):
        title = self.topic["title"] or self.current["title"]
        body = join_parts(self.topic["parts"])
        urdu = join_parts(self.topic["urdu"])
        urdu = re.sub(r"\s+", " ", urdu).strip()
        if len(urdu) > 280:
            urdu = urdu[:277].rsplit(" ", 1)[0] + "…"
        figures = self.topic["figures"]
        caption_speech = speakable(" ".join(self.topic["captions"]))
        for index, beat in enumerate(split_beats(body)):
            spoken = speakable(beat)
            if index == 0 and caption_speech:
                spoken = f"{spoken} {caption_speech}".strip()
            if len(spoken) < 12:
                continue
            self.current["scenes"].append({
                "title": title if index == 0 else f"{title} · {index + 1}",
                "body": beat,
                "urdu": urdu if index == 0 else "",
                "speak": spoken,
                "figures": figures if index == 0 else [],
            })
        self.topic = None


def load_grade(folder: Path):
    files = sorted(folder.glob("ch*.html"), key=lambda p: int(re.search(r"\d+", p.stem).group()))
    final = folder / "final.html"
    if final.exists():
        files.append(final)
    chapters = []
    for path in files:
        html, figures = prepare_html(path.read_text(encoding="utf-8"))
        parser = ChapterParser(figures)
        parser.feed(html)
        parser.close()
        chapters.extend(ch for ch in parser.chapters if ch["scenes"])
    return chapters


def audit(grades):
    math_scenes = 0
    diagram_scenes = 0
    for grade in grades:
        for chapter in grade["chapters"]:
            for scene in chapter["scenes"]:
                if "\\(" in scene["body"]:
                    math_scenes += 1
                if any("<svg" in figure for figure in scene["figures"]):
                    diagram_scenes += 1
                if "\\(" in scene["speak"] or "<svg" in scene["speak"] or "<sup>" in scene["speak"]:
                    raise SystemExit(f"narration leaked markup: {scene['speak'][:120]}")
    print(f"math scenes: {math_scenes}, diagram scenes: {diagram_scenes}")
    if math_scenes == 0 or diagram_scenes == 0:
        raise SystemExit("expected both MathJax and SVG scenes")
    return math_scenes, diagram_scenes


def main():
    grades = []
    for key, title, label in GRADES:
        chapters = load_grade(SRC / key)
        grades.append({"id": key, "title": title, "label": label, "chapters": chapters})
        scenes = sum(len(ch["scenes"]) for ch in chapters)
        print(f"{key}: {len(chapters)} chapters, {scenes} scenes")
    audit(grades)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"grades": grades}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
