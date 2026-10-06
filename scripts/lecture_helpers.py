"""Shared builders for original whiteboard lecture scripts."""


def title(text):
    return {"k": "title", "t": text}


def h2(text):
    return {"k": "h2", "t": text}


def bullet(text):
    return {"k": "bullet", "t": text}


def note(text, tone="gold"):
    return {"k": "note", "t": text, "tone": tone}


def formula(text):
    return {"k": "formula", "t": text}


def code(*lines):
    return {"k": "code", "items": list(lines)}


def gates(*names):
    return {"k": "gates", "items": list(names)}


def table(headers, rows):
    return {"k": "table", "headers": list(headers), "rows": [list(row) for row in rows]}


def flow(*nodes):
    return {"k": "flow", "items": list(nodes)}


def layers(*items):
    return {"k": "layers", "items": list(items)}


def cols(left_title, left, right_title, right):
    return {
        "k": "cols",
        "t": left_title,
        "items": list(left),
        "t2": right_title,
        "items2": list(right),
    }


def array(items, hi=None, caption=""):
    return {"k": "array", "t": caption, "items": [str(x) for x in items], "hi": list(hi or [])}


def steps(*items):
    return {"k": "steps", "items": list(items)}


def kmap(cells, hi=None, caption="A \\ B"):
    return {"k": "kmap", "t": caption, "items": [str(c) for c in cells], "hi": list(hi or [])}


def chips(*items):
    return {"k": "chips", "items": list(items)}


def board(narration, *marks):
    text = " ".join(narration.split())
    return {"narration": text, "marks": list(marks)}


def lecture(lecture_id, lecture_title, golden, boards):
    return {
        "id": lecture_id,
        "title": lecture_title,
        "golden": golden,
        "boards": boards,
    }


def chapter(chapter_id, number, chapter_title, lectures):
    return {
        "id": chapter_id,
        "number": number,
        "title": chapter_title,
        "lectures": lectures,
    }
