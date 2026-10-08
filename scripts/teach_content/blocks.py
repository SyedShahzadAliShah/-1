"""Small constructors for Urdish lecture blocks."""


def p(say, html=None):
    return {"type": "p", "say": say, "html": say if html is None else html}


def math(tex, say, display=True):
    return {"type": "math", "tex": tex, "say": say, "display": display}


def svg(name, say, caption="", **opts):
    block = {"type": "svg", "name": name, "say": say, "caption": caption}
    block.update(opts)
    return block


def table(headers, rows, say):
    return {"type": "table", "headers": headers, "rows": rows, "say": say}


def steps(title, items, say):
    return {"type": "steps", "title": title, "items": items, "say": say}


def code(text, say, lang="text"):
    return {"type": "code", "lang": lang, "text": text, "say": say}


def tip(say):
    return {"type": "tip", "say": say}


def check(q, a):
    return {"type": "check", "q": q, "a": a, "say": q + " Jawab. " + a}


def lecture(lid, code, title, minutes, blocks, golden=False):
    return {
        "id": lid,
        "code": code,
        "title": title,
        "minutes": minutes,
        "golden": golden,
        "blocks": list(blocks),
    }
