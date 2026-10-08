"""Build BIEK Computer Science XI and XII lecture PDFs.

The notes are original classroom lectures aligned to the Board of
Intermediate Education Karachi Model Paper 2026. They are not an official
board publication and they do not reproduce any textbook.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib.colors import Color, HexColor, white
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    ListFlowable,
    ListItem,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Flowable,
)

ROOT = Path(__file__).resolve().parent
PDF_DIR = ROOT / "pdf"
SANS = Path("/usr/share/fonts/truetype/liberation")
MONO = Path("/usr/share/fonts/truetype/dejavu")

pdfmetrics.registerFont(TTFont("Body", str(SANS / "LiberationSans-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Body-Bold", str(SANS / "LiberationSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Body-Italic", str(SANS / "LiberationSans-Italic.ttf")))
pdfmetrics.registerFont(TTFont("Body-BoldItalic", str(SANS / "LiberationSans-BoldItalic.ttf")))
pdfmetrics.registerFont(TTFont("Mono", str(MONO / "DejaVuSansMono.ttf")))
pdfmetrics.registerFontFamily(
    "Body",
    normal="Body",
    bold="Body-Bold",
    italic="Body-Italic",
    boldItalic="Body-BoldItalic",
)

NAVY = HexColor("#16324F")
TEAL = HexColor("#0F6E6E")
TEAL_DARK = HexColor("#0B5555")
GOLD = HexColor("#A6843D")
CREAM = HexColor("#FBF8F1")
INK = HexColor("#1C2430")
MUTED = HexColor("#5C6770")
LINE = HexColor("#D5DDE3")
BOX = HexColor("#F4F8F7")
TIP_BG = HexColor("#F8F3E6")
ANS_BG = HexColor("#F7F4EE")
CODE_BG = HexColor("#F6F4EF")
ROW_ALT = HexColor("#F3F8F8")
PALE = HexColor("#E7F0F0")

PAGE_W, PAGE_H = A4
MARGIN_L = 42
MARGIN_R = 42
MARGIN_T = 58
MARGIN_B = 48
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def markup(text: str) -> str:
    """Allow **bold** and `code` in paragraph text.

    Code spans are taken out first so characters such as * and < inside
    them are not treated as markup.
    """
    spans: list[str] = []

    def hold(match: re.Match) -> str:
        spans.append(match.group(1))
        return f"\x00CODE{len(spans) - 1}\x00"

    text = re.sub(r"`([^`]+)`", hold, text)
    text = esc(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)

    def restore(match: re.Match) -> str:
        inner = esc(spans[int(match.group(1))])
        return f"<font face='Mono' size='9' color='#0B5555'>{inner}</font>"

    return re.sub(r"\x00CODE(\d+)\x00", restore, text)


def styles() -> dict[str, ParagraphStyle]:
    s = {}
    s["h1"] = ParagraphStyle(
        "h1",
        fontName="Body-Bold",
        fontSize=18,
        leading=22,
        textColor=NAVY,
        spaceAfter=8,
    )
    s["h2"] = ParagraphStyle(
        "h2",
        fontName="Body-Bold",
        fontSize=13,
        leading=16,
        textColor=TEAL_DARK,
        spaceBefore=12,
        spaceAfter=4,
        keepWithNext=True,
    )
    s["h3"] = ParagraphStyle(
        "h3",
        fontName="Body-Bold",
        fontSize=11,
        leading=14,
        textColor=NAVY,
        spaceBefore=8,
        spaceAfter=2,
        keepWithNext=True,
    )
    s["body"] = ParagraphStyle(
        "body",
        fontName="Body",
        fontSize=10.5,
        leading=14.5,
        textColor=INK,
        alignment=TA_LEFT,
        spaceAfter=6,
    )
    s["bullet"] = ParagraphStyle(
        "bullet",
        parent=s["body"],
        alignment=TA_LEFT,
        leftIndent=0,
        spaceAfter=1,
    )
    s["th"] = ParagraphStyle(
        "th",
        fontName="Body-Bold",
        fontSize=8.5,
        leading=11,
        textColor=white,
    )
    s["td"] = ParagraphStyle(
        "td",
        fontName="Body",
        fontSize=8.5,
        leading=11,
        textColor=INK,
    )
    s["kicker"] = ParagraphStyle(
        "kicker",
        fontName="Body-Bold",
        fontSize=8,
        leading=10,
        textColor=GOLD,
        spaceAfter=2,
    )
    s["cover_body"] = ParagraphStyle(
        "cover_body",
        fontName="Body",
        fontSize=10.5,
        leading=15,
        textColor=INK,
        alignment=TA_LEFT,
        spaceAfter=8,
    )
    s["small"] = ParagraphStyle(
        "small",
        fontName="Body",
        fontSize=8.5,
        leading=11.5,
        textColor=INK,
        alignment=TA_LEFT,
    )
    s["answer"] = ParagraphStyle(
        "answer",
        fontName="Body",
        fontSize=9,
        leading=12.5,
        textColor=INK,
        alignment=TA_LEFT,
        spaceAfter=4,
    )
    s["code"] = ParagraphStyle(
        "code",
        fontName="Mono",
        fontSize=8,
        leading=10.5,
        textColor=HexColor("#1A2330"),
        alignment=TA_LEFT,
    )
    s["caption"] = ParagraphStyle(
        "caption",
        fontName="Body-Italic",
        fontSize=8,
        leading=10,
        textColor=MUTED,
        spaceBefore=1,
        spaceAfter=8,
    )
    s["footer"] = ParagraphStyle(
        "footer",
        fontName="Body",
        fontSize=8,
        leading=10,
        textColor=MUTED,
    )
    s["toc"] = ParagraphStyle(
        "toc",
        fontName="Body",
        fontSize=10.5,
        leading=15,
        textColor=INK,
    )
    return s


S = styles()


class LectureMark(Flowable):
    def __init__(self, title: str, outline: str, key: str):
        super().__init__()
        self.title = title
        self.outline = outline
        self.key = key
        self.width = 0
        self.height = 0

    def draw(self):
        self.canv._lecture_title = self.title
        self.canv.bookmarkPage(self.key)
        self.canv.addOutlineEntry(self.outline, self.key, level=0, closed=False)


class FlowChart(Flowable):
    """Stacked rounded boxes joined by downward arrows."""

    def __init__(self, steps: list[str], width: float | None = None):
        super().__init__()
        self.steps = steps
        self.box_w = width or CONTENT_W
        self.width = self.box_w
        self._lines = [self._wrap(step) for step in steps]
        self._heights = [max(22, 8 + len(lines) * 11) for lines in self._lines]
        gaps = 16 * (len(steps) - 1)
        self.height = sum(self._heights) + gaps + 4

    def _wrap(self, text: str) -> list[str]:
        words = text.split()
        lines: list[str] = []
        current = ""
        max_w = self.box_w - 16
        for word in words:
            trial = word if not current else current + " " + word
            if pdfmetrics.stringWidth(trial, "Body", 8.5) <= max_w:
                current = trial
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
        return lines or [""]

    def draw(self):
        c = self.canv
        y = self.height - 2
        for i, lines in enumerate(self._lines):
            h = self._heights[i]
            y -= h
            c.setFillColor(CREAM)
            c.setStrokeColor(TEAL)
            c.setLineWidth(1)
            c.roundRect(0, y, self.box_w, h, 4, fill=1, stroke=1)
            c.setFillColor(INK)
            c.setFont("Body", 8.5)
            text_h = len(lines) * 11
            ty = y + (h - text_h) / 2 + (len(lines) - 1) * 11 + 1
            for line in lines:
                c.drawCentredString(self.box_w / 2, ty, line)
                ty -= 11
            if i < len(self._lines) - 1:
                ax = self.box_w / 2
                c.setStrokeColor(NAVY)
                c.setFillColor(NAVY)
                c.setLineWidth(1)
                c.line(ax, y, ax, y - 12)
                path = c.beginPath()
                path.moveTo(ax, y - 16)
                path.lineTo(ax - 4, y - 10)
                path.lineTo(ax + 4, y - 10)
                path.close()
                c.drawPath(path, fill=1, stroke=0)
                y -= 16


class Topology(Flowable):
    def __init__(self, kind: str, caption: str, width: float = 160, height: float = 128):
        super().__init__()
        self.kind = kind
        self.caption = caption
        self.width = width
        self.height = height

    def draw(self):
        c = self.canv
        c.setStrokeColor(LINE)
        c.setFillColor(HexColor("#F8FBFA"))
        c.roundRect(0, 16, self.width, self.height - 18, 4, fill=1, stroke=1)
        c.setStrokeColor(TEAL)
        c.setFillColor(TEAL)
        c.setLineWidth(1.2)
        if self.kind == "bus":
            self._bus(c)
        elif self.kind == "star":
            self._star(c)
        elif self.kind == "ring":
            self._ring(c)
        c.setFillColor(MUTED)
        c.setFont("Body", 8)
        c.drawCentredString(self.width / 2, 4, self.caption)

    def _node(self, c, x, y, r=7):
        c.setFillColor(NAVY)
        c.circle(x, y, r, fill=1, stroke=0)

    def _bus(self, c):
        y = 48
        c.setStrokeColor(GOLD)
        c.setLineWidth(2.5)
        c.line(18, y, self.width - 18, y)
        xs = [32, 68, 104, 140]
        for x in xs:
            c.setStrokeColor(TEAL)
            c.setLineWidth(1)
            c.line(x, y, x, y + 28)
            self._node(c, x, y + 36)

    def _star(self, c):
        cx, cy = self.width / 2, 78
        points = [(cx, 112), (self.width - 24, 92), (self.width - 36, 48), (36, 48), (24, 92)]
        c.setStrokeColor(TEAL)
        c.setLineWidth(1)
        for x, y in points:
            c.line(cx, cy, x, y)
        for x, y in points:
            self._node(c, x, y)
        c.setFillColor(GOLD)
        c.circle(cx, cy, 8, fill=1, stroke=0)

    def _ring(self,
              c):
        import math

        cx, cy, r = self.width / 2, 74, 32
        pts = []
        for i in range(5):
            ang = math.radians(-90 + i * 72)
            pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
        c.setStrokeColor(TEAL)
        c.setLineWidth(1.2)
        for i, (x, y) in enumerate(pts):
            nx, ny = pts[(i + 1) % len(pts)]
            c.line(x, y, nx, ny)
        for x, y in pts:
            self._node(c, x, y)


def _shade_table(data, bg: Color, bar: Color, width: float | None = None) -> Table:
    t = Table(data, colWidths=[width or CONTENT_W])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), bg),
                ("LINEBEFORE", (0, 0), (0, -1), 3.5, bar),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return t


def callout(title: str, text: str, kind: str = "define") -> Table:
    if kind == "tip":
        bg, bar = TIP_BG, GOLD
        label = "EXAM TIP"
    elif kind == "board":
        bg, bar = PALE, NAVY
        label = "ON THE BOARD"
    elif kind == "answer":
        bg, bar = ANS_BG, GOLD
        label = "MODEL ANSWER"
    else:
        bg, bar = BOX, TEAL
        label = "DEFINITION"
    heading = title if title else label
    body = Paragraph(
        f"<font face='Body-Bold' size='8' color='#8C6A28'>{esc(label)}</font>"
        f"<font face='Body-Bold' size='10' color='#16324F'>   {markup(heading)}</font><br/>"
        f"<font size='9.5'>{markup(text)}</font>",
        S["small"],
    )
    return _shade_table([[body]], bg, bar)


def code_block(source: str, caption: str | None = None) -> list:
    folded = _fold_code(source.rstrip("\n"))
    safe = "<br/>".join(
        esc(line).replace(" ", "&nbsp;") if line else "&nbsp;" for line in folded.split("\n")
    )
    para = Paragraph(safe, S["code"])
    table = Table([[para]], colWidths=[CONTENT_W])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
                ("LINEBEFORE", (0, 0), (0, -1), 3, TEAL_DARK),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    flow = [Spacer(1, 3), table]
    if caption:
        flow.append(Paragraph(markup(caption), S["caption"]))
    else:
        flow.append(Spacer(1, 6))
    return flow


def _fold_code(text: str, width: int = 86) -> str:
    out = []
    for line in text.split("\n"):
        if len(line) <= width:
            out.append(line)
            continue
        while len(line) > width:
            out.append(line[:width])
            line = "  " + line[width:]
        out.append(line)
    return "\n".join(out)


def make_table(headers: list[str], rows: list[list[str]], widths: list[float] | None = None) -> Table:
    if widths is None:
        widths = [CONTENT_W / len(headers)] * len(headers)
    # Scale if the caller used a 500-pt design width.
    scale = CONTENT_W / sum(widths)
    widths = [w * scale for w in widths]
    head = [Paragraph(markup(h), S["th"]) for h in headers]
    data = [head]
    for row in rows:
        data.append([Paragraph(markup(str(cell)), S["td"]) for cell in row])
    table = Table(data, colWidths=widths, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), TEAL),
                ("TEXTCOLOR", (0, 0), (-1, 0), white),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, ROW_ALT]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("GRID", (0, 0), (-1, -1), 0.3, HexColor("#C5D4D4")),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    return table


def bullets(items: list[str]) -> ListFlowable:
    flow_items = []
    for item in items:
        flow_items.append(
            ListItem(Paragraph(markup(item), S["bullet"]), leftIndent=12, bulletColor=TEAL)
        )
    return ListFlowable(
        flow_items,
        bulletType="bullet",
        start="•",
        leftIndent=14,
        bulletFontName="Body",
        bulletFontSize=9,
        spaceBefore=1,
        spaceAfter=6,
    )


def banner(kicker: str, title: str, meta: str) -> Table:
    text = (
        f"<font face='Body-Bold' size='8' color='#E2C27A'>{esc(kicker.upper())}</font><br/>"
        f"<font face='Body-Bold' size='13' color='white'>{markup(title)}</font><br/>"
        f"<font face='Body' size='8' color='#D5E3E3'>{markup(meta)}</font>"
    )
    para = Paragraph(text, S["small"])
    table = Table([[para]], colWidths=[CONTENT_W])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), NAVY),
                ("LINEBEFORE", (0, 0), (0, -1), 5, GOLD),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    return table


def render_blocks(blocks: list[dict]) -> list:
    flow = []
    for block in blocks:
        kind = block["kind"]
        if kind == "h2":
            flow.append(Paragraph(markup(block["text"]), S["h2"]))
        elif kind == "h3":
            flow.append(Paragraph(markup(block["text"]), S["h3"]))
        elif kind == "p":
            flow.append(Paragraph(markup(block["text"]), S["body"]))
        elif kind == "bullets":
            flow.append(bullets(block["items"]))
        elif kind == "define":
            flow.append(Spacer(1, 2))
            flow.append(callout(block.get("title", ""), block["text"], "define"))
            flow.append(Spacer(1, 6))
        elif kind == "tip":
            flow.append(Spacer(1, 2))
            flow.append(callout(block.get("title", "How to score"), block["text"], "tip"))
            flow.append(Spacer(1, 6))
        elif kind == "board":
            flow.append(Spacer(1, 2))
            flow.append(callout(block.get("title", "Copy this"), block["text"], "board"))
            flow.append(Spacer(1, 6))
        elif kind == "table":
            flow.append(Spacer(1, 3))
            flow.append(make_table(block["headers"], block["rows"], block.get("widths")))
            if block.get("caption"):
                flow.append(Paragraph(markup(block["caption"]), S["caption"]))
            else:
                flow.append(Spacer(1, 6))
        elif kind == "code":
            flow.extend(code_block(block["text"], block.get("caption")))
        elif kind == "flow":
            flow.append(Spacer(1, 3))
            flow.append(FlowChart(block["steps"]))
            if block.get("caption"):
                flow.append(Paragraph(markup(block["caption"]), S["caption"]))
            else:
                flow.append(Spacer(1, 6))
        elif kind == "topologies":
            flow.append(Spacer(1, 3))
            cells = [Topology("bus", "Bus"), Topology("star", "Star"), Topology("ring", "Ring")]
            wrap = Table([cells], colWidths=[CONTENT_W / 3.0] * 3)
            wrap.setStyle(
                TableStyle(
                    [
                        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 2),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
                    ]
                )
            )
            flow.append(wrap)
            flow.append(Spacer(1, 6))
        elif kind == "rule":
            flow.append(Spacer(1, 2))
            flow.append(HRFlowable(width="100%", thickness=0.4, color=LINE, spaceAfter=4))
        else:
            raise ValueError(f"Unknown block kind: {kind}")
    return flow


def render_checkpoint(lecture: dict) -> list:
    cp = lecture.get("checkpoint") or {}
    if not (cp.get("mcq") or cp.get("short") or cp.get("long")):
        return []
    flow: list = [
        Spacer(1, 6),
        Paragraph("Checkpoint", S["h2"]),
        Paragraph(
            "Try the questions before you read the model answers. Section B answers on the real paper should stay within about six or seven lines.",
            S["body"],
        ),
    ]
    mcqs = cp.get("mcq") or []
    if mcqs:
        flow.append(Paragraph("Multiple choice", S["h3"]))
        for i, item in enumerate(mcqs, 1):
            lines = [f"**{i}.** {item['q']}"]
            flow.append(Paragraph(markup(lines[0]), S["body"]))
            flow.append(bullets(item["opts"]))
    shorts = cp.get("short") or []
    if shorts:
        flow.append(Paragraph("Short answers", S["h3"]))
        for i, item in enumerate(shorts, 1):
            flow.append(Paragraph(markup(f"**S{i}.** {item['q']}"), S["body"]))
    longs = cp.get("long") or []
    if longs:
        flow.append(Paragraph("Detailed answer", S["h3"]))
        for i, item in enumerate(longs, 1):
            flow.append(Paragraph(markup(f"**L{i}.** {item['q']}"), S["body"]))

    flow.append(Paragraph("Model answers", S["h2"]))
    flow.append(
        Paragraph(
            "Cover this section while you attempt the checkpoint. The wording is a full-mark style answer, not the only acceptable wording.",
            S["body"],
        )
    )
    bits = []
    for i, item in enumerate(mcqs, 1):
        why = item.get("why", "")
        bits.append(
            Paragraph(
                markup(f"**MCQ {i}.** {item['ans']}. {why}"),
                S["answer"],
            )
        )
    for i, item in enumerate(shorts, 1):
        bits.append(Paragraph(markup(f"**S{i}.** {item['a']}"), S["answer"]))
    for i, item in enumerate(longs, 1):
        bits.append(Paragraph(markup(f"**L{i}.** {item['a']}"), S["answer"]))
    if bits:
        flow.append(_shade_table([[b] for b in bits], ANS_BG, GOLD))
    flow.append(Spacer(1, 8))
    return flow


def lecture_flow(lecture: dict, class_label: str) -> list:
    meta = lecture.get("meta") or ""
    number = lecture["number"]
    flow = [
        LectureMark(
            f"L{number}  {lecture['title']}",
            f"{class_label}  ·  Lecture {number}  ·  {lecture['title']}",
            f"{class_label}-L{number}",
        ),
        banner(
            f"{class_label}   ·   Lecture {number}",
            lecture["title"],
            meta,
        ),
        Spacer(1, 8),
    ]
    if lecture.get("outcomes"):
        flow.append(Paragraph("By the end of this lecture you can", S["h3"]))
        flow.append(bullets(lecture["outcomes"]))
    flow.extend(render_blocks(lecture["blocks"]))
    flow.extend(render_checkpoint(lecture))
    return flow


class LectureDoc(BaseDocTemplate):
    def __init__(self, filename: str, meta: dict, cover: bool = True):
        super().__init__(
            filename,
            pagesize=A4,
            title=meta["pdf_title"],
            author="Original lecture notes for BIEK Computer Science",
            subject=meta["pdf_title"],
        )
        self.meta = meta
        self.lecture_title = ""
        body = Frame(
            MARGIN_L,
            MARGIN_B,
            CONTENT_W,
            PAGE_H - MARGIN_T - MARGIN_B,
            id="body",
            showBoundary=0,
        )
        cover_frame = Frame(
            MARGIN_L,
            72,
            CONTENT_W,
            PAGE_H - 168 - 72,
            id="cover",
            showBoundary=0,
        )
        templates = []
        if cover:
            templates.append(
                PageTemplate(id="cover", frames=[cover_frame], onPage=self._cover_chrome, onPageEnd=self._noop)
            )
        templates.append(
            PageTemplate(id="body", frames=[body], onPage=self._noop, onPageEnd=self._body_chrome)
        )
        self.addPageTemplates(templates)

    def afterFlowable(self, flowable):
        if isinstance(flowable, LectureMark):
            self.lecture_title = flowable.title

    @staticmethod
    def _noop(canvas, doc):
        return

    def _cover_chrome(self, canvas, doc):
        c = canvas
        c.saveState()
        c.setFillColor(NAVY)
        c.rect(0, PAGE_H - 158, PAGE_W, 158, fill=1, stroke=0)
        c.setFillColor(GOLD)
        c.rect(0, PAGE_H - 166, PAGE_W, 8, fill=1, stroke=0)
        c.setFillColor(HexColor("#E2C27A"))
        c.setFont("Body", 9)
        c.drawString(MARGIN_L, PAGE_H - 46, "BOARD OF INTERMEDIATE EDUCATION, KARACHI")
        c.setFillColor(white)
        c.setFont("Body-Bold", 22)
        y = PAGE_H - 82
        for line in doc.meta["cover_lines"]:
            c.drawString(MARGIN_L, y, line)
            y -= 26
        c.setFillColor(HexColor("#D5E4E4"))
        c.setFont("Body", 10)
        c.drawString(MARGIN_L, PAGE_H - 142, doc.meta["cover_sub"])
        c.setFillColor(NAVY)
        c.rect(0, 0, PAGE_W, 52, fill=1, stroke=0)
        c.setFillColor(HexColor("#E2C27A"))
        c.setFont("Body", 8)
        c.drawString(MARGIN_L, 28, doc.meta["cover_foot"])
        c.setFillColor(HexColor("#D5E4E4"))
        c.setFont("Body", 8)
        c.drawString(MARGIN_L, 14, "Original classroom notes  ·  Not an official BIEK publication")
        c.restoreState()

    def _body_chrome(self, canvas, doc):
        c = canvas
        c.saveState()
        c.setFillColor(NAVY)
        c.rect(0, PAGE_H - 32, PAGE_W, 32, fill=1, stroke=0)
        c.setFillColor(GOLD)
        c.rect(0, PAGE_H - 35, PAGE_W, 3, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Body", 8)
        header_left = doc.meta["running_header"]
        c.drawString(MARGIN_L, PAGE_H - 20, header_left)
        title = getattr(doc, "lecture_title", "") or ""
        c.setFont("Body", 8)
        max_w = CONTENT_W - pdfmetrics.stringWidth(header_left, "Body", 8) - 70
        shown = title
        while shown and pdfmetrics.stringWidth(shown, "Body", 8) > max_w:
            shown = shown[:-2]
        if shown != title and shown:
            shown = shown[:-1] + "…"
        c.drawRightString(PAGE_W - MARGIN_R, PAGE_H - 20, shown)
        c.setStrokeColor(LINE)
        c.setLineWidth(0.4)
        c.line(MARGIN_L, 36, PAGE_W - MARGIN_R, 36)
        c.setFillColor(MUTED)
        c.setFont("Body", 8)
        c.drawString(MARGIN_L, 22, "BIEK Computer Science lectures  ·  Model Paper 2026")
        c.drawRightString(PAGE_W - MARGIN_R, 22, f"{doc.page}")
        c.restoreState()


def cover_story(meta: dict, lectures: list[dict]) -> list:
    flow = [
        NextPageTemplate("body"),
        Paragraph("How to use these lectures", S["h1"]),
        Paragraph(meta["intro"], S["cover_body"]),
        Paragraph("Paper pattern these notes follow", S["h2"]),
    ]
    flow.append(make_table(meta["pattern_headers"], meta["pattern_rows"], meta.get("pattern_widths")))
    flow.append(Spacer(1, 8))
    flow.append(Paragraph(meta["pattern_note"], S["body"]))
    flow.append(Paragraph("Lectures in this booklet", S["h2"]))
    items = []
    for lec in lectures:
        items.append(f"**Lecture {lec['number']}.** {lec['title']}")
    flow.append(bullets(items))
    flow.append(
        Paragraph(
            "Each lecture ends with a checkpoint in the style of the board paper, then model answers. Use the PDF bookmarks to jump to a lecture.",
            S["body"],
        )
    )
    flow.append(PageBreak())
    return flow


def build_volume(path: Path, meta: dict, lectures: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = LectureDoc(str(path), meta)
    story = cover_story(meta, lectures)
    for index, lecture in enumerate(lectures):
        if index:
            story.append(PageBreak())
        story.extend(lecture_flow(lecture, meta["class_label"]))
    doc.build(story)


def build_single(path: Path, meta: dict, lecture: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    single_meta = dict(meta)
    single_meta["pdf_title"] = f"{meta['class_label']} Lecture {lecture['number']}: {lecture['title']}"
    doc = LectureDoc(str(path), single_meta, cover=False)
    doc.build(lecture_flow(lecture, meta["class_label"]))


def slug(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-")
    return text[:60]


def main() -> None:
    from lectures_xi import LECTURES as XI
    from lectures_xi import META as XI_META
    from lectures_xii import LECTURES as XII
    from lectures_xii import META as XII_META

    xi_path = PDF_DIR / "BIEK-CS-XI-Lectures.pdf"
    xii_path = PDF_DIR / "BIEK-CS-XII-Lectures.pdf"
    build_volume(xi_path, XI_META, XI)
    build_volume(xii_path, XII_META, XII)
    for lec in XI:
        name = f"Lecture-{lec['number']:02d}-{slug(lec['title'])}.pdf"
        build_single(PDF_DIR / "XI" / name, XI_META, lec)
    for lec in XII:
        name = f"Lecture-{lec['number']:02d}-{slug(lec['title'])}.pdf"
        build_single(PDF_DIR / "XII" / name, XII_META, lec)
    print(f"Wrote {xi_path}")
    print(f"Wrote {xii_path}")


if __name__ == "__main__":
    main()
