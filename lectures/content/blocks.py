"""Short constructors for lecture body blocks."""


def h(text):
    return {"type": "h", "text": text}


def h3(text):
    return {"type": "h3", "text": text}


def p(text):
    return {"type": "p", "text": text}


def ul(*items):
    return {"type": "ul", "items": list(items)}


def ol(*items):
    return {"type": "ol", "items": list(items)}


def learn(*paras, items=None):
    d = {"type": "learn", "paras": list(paras)}
    if items:
        d["items"] = list(items)
    return d


def example(*paras, items=None):
    d = {"type": "example", "paras": list(paras)}
    if items:
        d["items"] = list(items)
    return d


def tip(*paras, items=None):
    d = {"type": "tip", "paras": list(paras)}
    if items:
        d["items"] = list(items)
    return d


def warn(*paras, items=None):
    d = {"type": "warn", "paras": list(paras)}
    if items:
        d["items"] = list(items)
    return d


def exam(*paras, items=None):
    d = {"type": "exam", "paras": list(paras)}
    if items:
        d["items"] = list(items)
    return d


def urdu(*paras):
    return {"type": "urdu", "paras": list(paras)}


def defn(term, text):
    return {"type": "defn", "term": term, "text": text}


def table(headers, rows, center=False, caption=None):
    d = {"type": "table", "headers": headers, "rows": rows, "center": center}
    if caption:
        d["caption"] = caption
    return d


def code(text, output=False):
    return {"type": "code", "text": text.strip("\n"), "output": output}


def svg(svg, caption=None):
    d = {"type": "svg", "svg": svg}
    if caption:
        d["caption"] = caption
    return d


def flow(*steps):
    return {"type": "flow", "steps": list(steps)}


def check(*pairs):
    return {"type": "check", "pairs": list(pairs)}


def mcq(q, opts, ans):
    return {"q": q, "opts": opts, "ans": ans}


def lec(**kwargs):
    return kwargs
