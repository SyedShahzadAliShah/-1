"""Build the BIEK Computer Science lecture PDFs."""

import re
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    BaseDocTemplate,
    CondPageBreak,
    Frame,
    HRFlowable,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Flowable,
)

from diagrams import Diagram, NAVY, TEAL, GOLD, INK, PALE, CREAM
from programs import PROGRAMS

PAGE_W, PAGE_H = A4
LEFT = 15 * mm
RIGHT = 15 * mm
CONTENT_W = PAGE_W - LEFT - RIGHT


class HeaderState:
    left = "BIEK Computer Science"
    right = ""


class SetHeader(Flowable):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def wrap(self, aw, ah):
        HeaderState.left = self.left
        HeaderState.right = self.right
        return 0, 0

    def draw(self):
        return


class Bookmark(Flowable):
    def __init__(self, key, title, level=0):
        super().__init__()
        self.key = key
        self.title = title
        self.level = level

    def wrap(self, aw, ah):
        return 0, 0

    def draw(self):
        self.canv.bookmarkPage(self.key)
        self.canv.addOutlineEntry(self.title, self.key, self.level, closed=0)


class CodeBlock(Flowable):
    def __init__(self, text):
        super().__init__()
        self.lines = text.strip("\n").splitlines() or [""]
        self.font = "Courier"
        self.size = 8
        self.leading = 10.5
        self.pad = 6

    def wrap(self, aw, ah):
        self.width = aw
        self.height = self.pad * 2 + self.leading * len(self.lines)
        return aw, self.height

    def split(self, aw, ah):
        n = int((ah - 2 * self.pad) // self.leading)
        if n >= len(self.lines):
            n = len(self.lines) - 1
        if n < 1:
            return []
        head = CodeBlock("\n".join(self.lines[:n]))
        tail = CodeBlock("\n".join(self.lines[n:]))
        return [head, tail]

    def draw(self):
        c = self.canv
        c.setFillColor(colors.HexColor("#F4F7F9"))
        c.setStrokeColor(colors.HexColor("#C5D0D8"))
        c.setLineWidth(0.6)
        c.roundRect(0, 0, self.width, self.height, 3, fill=1, stroke=1)
        c.setStrokeColor(TEAL)
        c.setLineWidth(2.5)
        c.line(1.2, 2, 1.2, self.height - 2)
        c.setFillColor(colors.HexColor("#1C2830"))
        c.setFont(self.font, self.size)
        y = self.height - self.pad - self.size
        for line in self.lines:
            c.drawString(self.pad + 2, y, line[:110])
            y -= self.leading


def markup(text):
    text = "" if text is None else str(text)
    pieces = []
    pos = 0
    for match in re.finditer(r"`([^`]+)`", text):
        pieces.append(("t", text[pos:match.start()]))
        pieces.append(("c", match.group(1)))
        pos = match.end()
    pieces.append(("t", text[pos:]))
    out = []
    for kind, value in pieces:
        value = (
            value.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )
        if kind == "c":
            out.append(f'<font face="Courier" size="9">{value}</font>')
        else:
            value = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", value)
            out.append(value)
    return "".join(out).replace("\n", "<br/>")


def styles():
    s = {}
    s["h1"] = ParagraphStyle(
        "h1", fontName="Helvetica-Bold", fontSize=18, leading=22,
        textColor=NAVY, alignment=TA_LEFT, spaceAfter=4,
    )
    s["kicker"] = ParagraphStyle(
        "kicker", fontName="Helvetica-Bold", fontSize=9, leading=12,
        textColor=GOLD, spaceAfter=2,
    )
    s["h2"] = ParagraphStyle(
        "h2", fontName="Helvetica-Bold", fontSize=13, leading=16,
        textColor=NAVY, spaceBefore=11, spaceAfter=4,
    )
    s["h3"] = ParagraphStyle(
        "h3", fontName="Helvetica-Bold", fontSize=11.5, leading=14,
        textColor=TEAL, spaceBefore=8, spaceAfter=3,
    )
    s["body"] = ParagraphStyle(
        "body", fontName="Helvetica", fontSize=10.5, leading=14.4,
        textColor=INK, alignment=TA_JUSTIFY, spaceAfter=6,
    )
    s["center"] = ParagraphStyle(
        "center", parent=s["body"], alignment=TA_CENTER, textColor=NAVY,
    )
    s["cover_title"] = ParagraphStyle(
        "cover_title", fontName="Helvetica-Bold", fontSize=26, leading=31,
        textColor=colors.white, alignment=TA_LEFT, spaceAfter=4,
    )
    s["cover_sub"] = ParagraphStyle(
        "cover_sub", fontName="Helvetica", fontSize=12, leading=16,
        textColor=colors.HexColor("#F4E4C4"), alignment=TA_LEFT, spaceAfter=3,
    )
    s["th"] = ParagraphStyle(
        "th", fontName="Helvetica-Bold", fontSize=8, leading=10.5,
        textColor=colors.white,
    )
    s["td"] = ParagraphStyle(
        "td", fontName="Helvetica", fontSize=8, leading=10.6, textColor=INK,
    )
    s["caption"] = ParagraphStyle(
        "caption", fontName="Helvetica-Oblique", fontSize=8.5, leading=11,
        textColor=TEAL, spaceBefore=2, spaceAfter=8,
    )
    s["tip"] = ParagraphStyle(
        "tip", fontName="Helvetica", fontSize=9.5, leading=12.8, textColor=INK,
    )
    s["q"] = ParagraphStyle(
        "q", fontName="Helvetica", fontSize=10.5, leading=14, textColor=INK,
        spaceAfter=2,
    )
    s["small"] = ParagraphStyle(
        "small", fontName="Helvetica", fontSize=9, leading=12, textColor=INK,
        alignment=TA_LEFT, spaceAfter=3,
    )
    return s


S = styles()


def P(text, style="body"):
    return Paragraph(markup(text), S[style])


def callout(title, text, tint, accent):
    body = Paragraph(f"<b>{markup(title)}</b><br/>{markup(text)}", S["tip"])
    bar = Table([[""]], colWidths=[3.2 * mm], rowHeights=[None])
    data = [[bar, body]]
    table = Table(data, colWidths=[3.2 * mm, CONTENT_W - 3.2 * mm])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), accent),
        ("BACKGROUND", (1, 0), (1, 0), tint),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("RIGHTPADDING", (0, 0), (0, 0), 0),
        ("LEFTPADDING", (1, 0), (1, 0), 8),
        ("RIGHTPADDING", (1, 0), (1, 0), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return table


def bullets(items, numbered=False):
    flow = []
    for item in items:
        flow.append(ListItem(Paragraph(markup(item), S["body"]), leftIndent=2))
    return ListFlowable(
        flow,
        bulletType="1" if numbered else "bullet",
        start="1" if numbered else "circle",
        leftIndent=16,
        bulletFontName="Helvetica",
        bulletFontSize=9,
        spaceBefore=1,
        spaceAfter=6,
    )


def make_table(headers, rows):
    head = [Paragraph(markup(h), S["th"]) for h in headers]
    data = [head]
    for row in rows:
        data.append([Paragraph(markup(str(cell)), S["td"]) for cell in row])
    table = Table(data, colWidths=[CONTENT_W / len(headers)] * len(headers), repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("BACKGROUND", (0, 1), (-1, -1), colors.white),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F4F8FB")]),
        ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#C5D0D8")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return table


def display_source(source):
    lines = []
    for line in source.strip().splitlines():
        if line.startswith("// CASE:") or line.startswith("// STDIN:") or line.startswith("// EXPECT:"):
            continue
        lines.append(line)
    while lines and lines[0].strip() == "":
        lines.pop(0)
    return "\n".join(lines).rstrip() + "\n"


def section_flowables(block):
    kind = block[0]
    if kind == "h":
        return [P(block[1], "h2")]
    if kind == "h3":
        return [P(block[1], "h3")]
    if kind == "p":
        return [P(block[1])]
    if kind == "ul":
        return [bullets(block[1])]
    if kind == "ol":
        return [bullets(block[1], numbered=True)]
    if kind == "table":
        caption, headers, rows = block[1], block[2], block[3]
        flows = []
        if caption:
            flows.append(P(caption, "h3"))
        flows.append(make_table(headers, rows))
        flows.append(Spacer(1, 6))
        return flows
    if kind == "code":
        caption, raw = block[1], block[2]
        source = PROGRAMS[raw] if raw in PROGRAMS else raw
        flows = []
        if caption:
            flows.append(P(caption, "h3"))
        code = CodeBlock(display_source(source))
        flows.append(CondPageBreak(min(code.wrap(CONTENT_W, 700)[1] + 8, 460)))
        flows.append(CodeBlock(display_source(source)))
        flows.append(Spacer(1, 6))
        return flows
    if kind == "tip":
        return [callout("Exam point", block[1], CREAM, GOLD), Spacer(1, 6)]
    if kind == "note":
        return [callout("In the lab", block[1], PALE, TEAL), Spacer(1, 6)]
    if kind == "def":
        return [P(f"**{block[1]}.** {block[2]}")]
    if kind == "diagram":
        kind_name, caption = block[1], block[2]
        height = block[3] if len(block) > 3 else 52 * mm
        return [Diagram(kind_name, height), P(caption, "caption")]
    raise ValueError(f"Unknown block {kind}")


def keep_heading(blocks, index):
    head = section_flowables(blocks[index])
    if index + 1 < len(blocks) and blocks[index + 1][0] in ("p", "def"):
        nxt = section_flowables(blocks[index + 1])
        return [KeepTogether(head + nxt)], index + 2
    return head, index + 1


def render_sections(blocks):
    flows = []
    i = 0
    while i < len(blocks):
        if blocks[i][0] in ("h", "h3"):
            chunk, i = keep_heading(blocks, i)
            flows.extend(chunk)
        else:
            flows.extend(section_flowables(blocks[i]))
            i += 1
    return flows


def render_lecture(lec):
    flows = []
    unit = lec.get("unit", "")
    flows.append(P(lec["kicker"], "kicker"))
    flows.append(P(lec["title"], "h1"))
    meta = []
    if lec.get("weight"):
        meta.append(f"Board weight about {lec['weight']}")
    if lec.get("periods"):
        meta.append(lec["periods"])
    if meta:
        flows.append(P(" | ".join(meta), "small"))
    flows.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=8))
    if lec.get("intro"):
        flows.append(P(lec["intro"]))
    if lec.get("slos"):
        flows.append(P("What you should be able to do", "h2"))
        flows.append(bullets(lec["slos"]))
    if lec.get("path"):
        flows.append(P("Path through the lecture", "h2"))
        flows.append(bullets(lec["path"], numbered=True))
    flows.extend(render_sections(lec.get("sections", [])))
    if lec.get("terms"):
        flows.append(P("Key terms", "h2"))
        flows.append(make_table(
            ["Term", "Meaning to write in an answer"],
            [[term, meaning] for term, meaning in lec["terms"]],
        ))
        flows.append(Spacer(1, 6))
    if lec.get("summary"):
        flows.append(P("Bring it together", "h2"))
        flows.append(bullets(lec["summary"]))
    if lec.get("labs"):
        flows.append(P("Do this in the practical", "h2"))
        flows.append(bullets(lec["labs"], numbered=True))
    if lec.get("mcqs"):
        flows.append(CondPageBreak(150))
        flows.append(P("Check yourself", "h2"))
        flows.append(P(
            "Attempt every item before you read the key. Section A of the Computer Science paper is a set of multiple-choice questions."
        ))
        for number, item in enumerate(lec["mcqs"], start=1):
            bits = [P(f"**{number}.** {item['q']}", "q")]
            letters = ["A", "B", "C", "D"]
            for letter, option in zip(letters, item["options"]):
                bits.append(P(f"{letter}. {option}", "small"))
            bits.append(Spacer(1, 4))
            flows.append(KeepTogether(bits))
        flows.append(P("Answer key", "h3"))
        key_rows = []
        for number, item in enumerate(lec["mcqs"], start=1):
            key_rows.append([str(number), item["a"], item["why"]])
        flows.append(make_table(["Q", "Answer", "Why this is the answer"], key_rows))
        flows.append(Spacer(1, 6))
    if lec.get("shorts"):
        flows.append(P("Short answers", "h2"))
        flows.append(P(
            "A 3-mark answer needs a definition and two clear points, or a three-row difference. Write in sentences."
        ))
        for number, item in enumerate(lec["shorts"], start=1):
            flows.append(KeepTogether([
                P(f"**Q{number}.** {item['q']}", "q"),
                callout("Model answer", item["a"], PALE, TEAL),
                Spacer(1, 5),
            ]))
    if lec.get("longs"):
        flows.append(P("Detailed answers", "h2"))
        flows.append(P(
            "Section C asks for a connected answer. Open with a definition, develop the points below, and close with one example."
        ))
        for number, item in enumerate(lec["longs"], start=1):
            flows.append(P(f"**Question {number}.** {item['q']}", "q"))
            flows.append(bullets(item["points"], numbered=True))
    return flows


def render_lab(lab):
    flows = [P(f"Practical {lab['code']}", "kicker"), P(lab["title"], "h1")]
    flows.append(HRFlowable(width="100%", thickness=1, color=GOLD, spaceAfter=8))
    flows.append(P(f"**Aim.** {lab['aim']}"))
    if lab.get("need"):
        flows.append(P("You need", "h3"))
        flows.append(bullets(lab["need"]))
    flows.append(P("Steps", "h3"))
    flows.append(bullets(lab["steps"], numbered=True))
    if lab.get("program"):
        flows.extend(section_flowables(("code", "Program", lab["program"])))
    if lab.get("output"):
        flows.append(callout("What you should observe", lab["output"], CREAM, GOLD))
        flows.append(Spacer(1, 6))
    if lab.get("viva"):
        flows.append(P("Viva questions", "h3"))
        flows.append(bullets(lab["viva"]))
    return flows


def draw_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, PAGE_H - 12 * mm, PAGE_W, 12 * mm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, PAGE_H - 13.4 * mm, PAGE_W, 1.4 * mm, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica", 8)
    canvas.drawString(LEFT, PAGE_H - 7.4 * mm, HeaderState.left[:70])
    canvas.setFont("Helvetica", 8)
    canvas.drawRightString(PAGE_W - RIGHT, PAGE_H - 7.4 * mm, HeaderState.right[:78])
    canvas.setFillColor(GOLD)
    canvas.rect(0, 11 * mm, PAGE_W, 1.3 * mm, fill=1, stroke=0)
    canvas.setFillColor(NAVY)
    canvas.setFont("Helvetica", 8)
    canvas.drawString(LEFT, 6 * mm, "Sindh Curriculum 2019  |  original study lectures for BIEK")
    canvas.drawRightString(PAGE_W - RIGHT, 6 * mm, str(doc.page))
    canvas.restoreState()


def build_pdf(path, story, title):
    doc = BaseDocTemplate(
        str(path),
        pagesize=A4,
        title=title,
        author="BIEK Computer Science lecture notes",
        subject="Computer Science Class XI and XII, aligned to the Sindh Curriculum 2019",
    )
    frame = Frame(
        LEFT,
        16 * mm,
        CONTENT_W,
        PAGE_H - 20 * mm - 16 * mm,
        id="body",
        showBoundary=0,
    )
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=draw_page)])
    doc.build(story)


def cover_story(kicker, title, subtitle, paragraphs):
    banner_text = [
        P(kicker, "cover_sub"),
        Paragraph(title, S["cover_title"]),
        P(subtitle, "cover_sub"),
    ]
    inner = banner_text
    data = [[item] for item in inner]
    banner = Table(data, colWidths=[CONTENT_W])
    banner.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (0, 0), 16),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 16),
        ("TOPPADDING", (0, 1), (-1, -2), 1),
        ("BOTTOMPADDING", (0, 0), (-1, -2), 1),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    flows = [Spacer(1, 8), banner, Spacer(1, 12)]
    for paragraph in paragraphs:
        flows.append(P(paragraph))
    return flows


def slug(text):
    keep = []
    for ch in text.lower():
        if ch.isalnum():
            keep.append(ch)
        elif ch in " -_":
            keep.append("-")
    out = "".join(keep)
    while "--" in out:
        out = out.replace("--", "-")
    return out.strip("-")[:60]
