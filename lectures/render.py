"""Turn lecture dicts into print-ready HTML."""

from __future__ import annotations

import html as htmlmod
from pathlib import Path

CSS = (Path(__file__).parent / "assets" / "lecture.css").read_text(encoding="utf-8")


def e(text: str) -> str:
    return htmlmod.escape(str(text), quote=True)


def _p(text: str) -> str:
    return f"<p>{e(text)}</p>"


def render_block(block: dict | str) -> str:
    if isinstance(block, str):
        return _p(block)
    kind = block["type"]
    if kind == "h":
        return f"<h2>{e(block['text'])}</h2>"
    if kind == "h3":
        return f"<h3>{e(block['text'])}</h3>"
    if kind == "p":
        return _p(block["text"])
    if kind == "html":
        return block["html"]
    if kind == "ul":
        items = "".join(f"<li>{e(x)}</li>" for x in block["items"])
        return f"<ul>{items}</ul>"
    if kind == "ol":
        items = "".join(f"<li>{e(x)}</li>" for x in block["items"])
        return f"<ol>{items}</ol>"
    if kind in {"learn", "example", "tip", "warn", "exam", "urdu"}:
        inner = block.get("html") or "".join(_p(p) for p in block.get("paras", [block.get("text", "")]))
        extra = ""
        if "items" in block:
            extra = "<ul>" + "".join(f"<li>{e(x)}</li>" for x in block["items"]) + "</ul>"
        ur_cls = " urdu" if kind == "urdu" else ""
        ur_p = ' class="ur"' if kind == "urdu" else ""
        if kind == "urdu" and not block.get("html"):
            inner = "".join(f"<p class='ur'>{e(p)}</p>" for p in block.get("paras", [block.get("text", "")]))
            return f'<div class="box urdu">{inner}{extra}</div>'
        return f'<div class="box {kind}{ur_cls}">{inner}{extra}</div>'
    if kind == "defn":
        return f'<div class="defn"><b>{e(block["term"])}.</b> {e(block["text"])}</div>'
    if kind == "table":
        cls = ' class="center"' if block.get("center") else ""
        head = "".join(f"<th>{e(h)}</th>" for h in block["headers"])
        rows = []
        for row in block["rows"]:
            tds = []
            for cell in row:
                if isinstance(cell, dict) and cell.get("hl"):
                    tds.append(f'<td class="hl">{e(cell["text"])}</td>')
                else:
                    tds.append(f"<td>{e(cell)}</td>")
            rows.append("<tr>" + "".join(tds) + "</tr>")
        cap = f'<p class="small">{e(block["caption"])}</p>' if block.get("caption") else ""
        return f"{cap}<table{cls}><tr>{head}</tr>{''.join(rows)}</table>"
    if kind == "code":
        cls = "code output" if block.get("output") else "code"
        return f'<pre class="{cls}">{e(block["text"])}</pre>'
    if kind == "svg":
        cap = f"<figcaption>{e(block['caption'])}</figcaption>" if block.get("caption") else ""
        return f'<figure class="diagram">{block["svg"]}{cap}</figure>'
    if kind == "flow":
        bits = []
        for i, step in enumerate(block["steps"]):
            if i:
                bits.append("<i>→</i>")
            bits.append(f"<span>{e(step)}</span>")
        return f'<div class="flow">{"".join(bits)}</div>'
    if kind == "check":
        qs = "".join(f"<p><b>{i}.</b> {e(q)}</p>" for i, (q, _) in enumerate(block["pairs"], 1))
        ans = " · ".join(f"{i}. {e(a)}" for i, (_, a) in enumerate(block["pairs"], 1))
        return f'<div class="box check">{qs}<div class="ans">Answers: {ans}</div></div>'
    if kind == "two":
        left = "".join(render_block(b) for b in block["left"])
        right = "".join(render_block(b) for b in block["right"])
        return f'<div class="two-col"><div>{left}</div><div>{right}</div></div>'
    raise ValueError(kind)


def render_lecture(lec: dict, index: int) -> str:
    golden = ' <span class="star">★&nbsp;Golden</span>' if lec.get("golden") else ""
    kicker = f"Class {lec['grade']}  ·  Unit {lec.get('unit', '—')}  ·  Lecture {index:02d}"
    if lec.get("option"):
        kicker += f"  ·  {lec['option']}"
    slos = "".join(f"<li>{e(s)}</li>" for s in lec.get("slos", []))
    body = "".join(render_block(b) for b in lec["body"])
    practice = ""
    if lec.get("mcqs"):
        items = []
        for q in lec["mcqs"]:
            opts = "".join(f"<li>{e(o)}</li>" for o in q["opts"])
            items.append(f'<li>{e(q["q"])}<ol class="opts">{opts}</ol></li>')
        key = ", ".join(f"{i+1}={m['ans']}" for i, m in enumerate(lec["mcqs"]))
        practice += f"<h3>MCQs</h3><ol class='mcq'>{''.join(items)}</ol><p class='ans'>Key: {e(key)}</p>"
    if lec.get("short"):
        items = "".join(f"<li>{e(x)}</li>" for x in lec["short"])
        practice += f"<h3>Short questions (3 marks each)</h3><ol class='short'>{items}</ol>"
    if lec.get("short_ans"):
        items = "".join(f"<li>{e(x)}</li>" for x in lec["short_ans"])
        practice += f"<div class='answers'><h3>Model short answers</h3><ol>{items}</ol></div>"
    if lec.get("long"):
        items = "".join(f"<li>{e(x)}</li>" for x in lec["long"])
        practice += f"<h3>Long questions (board Section C)</h3><ol class='long'>{items}</ol>"
    return f'''
<section class="lecture" id="{e(lec['id'])}">
  <div class="lec-head">
    <div class="kicker">{e(kicker)}</div>
    <h1>{e(lec['title'])}{golden}</h1>
    <div class="meta">{e(lec.get("time", "One college period · 40–45 minutes"))} · {e(lec.get("unit_title", ""))}</div>
  </div>
  <h3>What you will learn</h3>
  <ul class="objectives">{slos}</ul>
  {body}
  {practice}
</section>
'''


def cover_page(grade: str, extra: str) -> str:
    title = {
        "XI": "Computer Science I",
        "XII": "Computer Science II",
        "XI+XII": "Computer Science I &amp; II",
    }[grade]
    return f'''
<section class="cover">
  <div>
    <div class="hero">
      <div class="brand">Board of Intermediate Education Karachi · BIEK</div>
      <h1>{title}<br>Lecture Notes</h1>
      <p class="sub">Class {grade} · Science General &amp; Humanities · Printed lectures for college and self-study</p>
      <div class="badge-row">
        <span class="badge">Sindh Curriculum 2019</span>
        <span class="badge">BIEK Model Paper 2026</span>
        <span class="badge">English + Urdu</span>
        <span class="badge">C / VB / MS Access</span>
      </div>
    </div>
  </div>
  <div class="panel">
    <h2>What is in this book</h2>
    {extra}
    <p class="small" style="margin-top:10px">Unofficial teaching notes for students of BIEK-affiliated colleges. Definitions, programs and diagrams follow the Sindh HSC Computer Science curriculum and the official BIEK paper pattern (Section A MCQs, Section B short, Section C detailed). Turbo C / void main() style is shown because that is what Karachi board answer books still expect.</p>
  </div>
</section>
'''


def toc_page(lectures: list[dict]) -> str:
    parts = ['<section class="toc"><h1>Lecture index</h1>']
    last_unit = None
    open_list = False
    n = 0
    for lec in lectures:
        u = f"{lec.get('unit')} {lec.get('unit_title')}"
        if u != last_unit:
            if open_list:
                parts.append("</ol>")
            parts.append(
                f'<h3>Unit {e(str(lec.get("unit", "")))}: {e(lec.get("unit_title", ""))}</h3><ol start="{n+1}">'
            )
            open_list = True
            last_unit = u
        n += 1
        star = " ★" if lec.get("golden") else ""
        parts.append(f"<li>{e(lec['title'])}{star}</li>")
    if open_list:
        parts.append("</ol>")
    parts.append("</section>")
    return "".join(parts)


def document(title: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>{e(title)}</title>
<style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>
"""
