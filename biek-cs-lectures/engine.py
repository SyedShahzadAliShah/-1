#!/usr/bin/env python3
"""Shared ReportLab engine for BIEK Computer Science lecture PDFs."""

from __future__ import annotations

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    CondPageBreak,
    Flowable,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

NAVY = colors.HexColor("#0B3D91")
NAVY_DARK = colors.HexColor("#072A64")
TEAL = colors.HexColor("#0E7490")
GOLD = colors.HexColor("#B45309")
CREAM = colors.HexColor("#FFF7ED")
SOFT = colors.HexColor("#EFF6FF")
MINT = colors.HexColor("#ECFDF5")
ROSE = colors.HexColor("#FFF1F2")
SLATE = colors.HexColor("#334155")
LINE = colors.HexColor("#CBD5E1")
CODE_BG = colors.HexColor("#0F172A")
CODE_FG = colors.HexColor("#E2E8F0")
WHITE = colors.white

FONT_REG = "DejaVu"
FONT_BOLD = "DejaVu-Bold"
FONT_ITALIC = "DejaVu-Italic"
FONT_MONO = "DejaVuMono"

pdfmetrics.registerFont(TTFont(FONT_REG, "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont(FONT_BOLD, "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont(FONT_ITALIC, "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"))
pdfmetrics.registerFont(TTFont(FONT_MONO, "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"))
pdfmetrics.registerFont(
    TTFont("DejaVuMono-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf")
)


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", "<br/>")
    )


def styles():
    ss = getSampleStyleSheet()
    ss.add(
        ParagraphStyle(
            "CoverKicker",
            fontName=FONT_BOLD,
            fontSize=11,
            textColor=GOLD,
            alignment=TA_CENTER,
            spaceAfter=6,
            tracking=1.2,
        )
    )
    ss.add(
        ParagraphStyle(
            "CoverTitle",
            fontName=FONT_BOLD,
            fontSize=28,
            leading=34,
            textColor=WHITE,
            alignment=TA_CENTER,
            spaceAfter=8,
        )
    )
    ss.add(
        ParagraphStyle(
            "CoverSub",
            fontName=FONT_REG,
            fontSize=13,
            leading=18,
            textColor=colors.HexColor("#DBEAFE"),
            alignment=TA_CENTER,
            spaceAfter=4,
        )
    )
    ss.add(
        ParagraphStyle(
            "H1",
            fontName=FONT_BOLD,
            fontSize=16,
            leading=21,
            textColor=NAVY,
            spaceBefore=14,
            spaceAfter=8,
            borderPadding=3,
        )
    )
    ss.add(
        ParagraphStyle(
            "H2",
            fontName=FONT_BOLD,
            fontSize=12.5,
            leading=17,
            textColor=TEAL,
            spaceBefore=10,
            spaceAfter=5,
        )
    )
    ss.add(
        ParagraphStyle(
            "H3",
            fontName=FONT_BOLD,
            fontSize=11,
            leading=15,
            textColor=NAVY_DARK,
            spaceBefore=8,
            spaceAfter=4,
        )
    )
    ss.add(
        ParagraphStyle(
            "Body",
            fontName=FONT_REG,
            fontSize=9.6,
            leading=13.4,
            textColor=SLATE,
            alignment=TA_JUSTIFY,
            spaceAfter=6,
        )
    )
    ss.add(
        ParagraphStyle(
            "BodyLeft",
            fontName=FONT_REG,
            fontSize=9.6,
            leading=13.4,
            textColor=SLATE,
            alignment=TA_LEFT,
            spaceAfter=4,
        )
    )
    ss.add(
        ParagraphStyle(
            "BulletBody",
            fontName=FONT_REG,
            fontSize=9.5,
            leading=13,
            textColor=SLATE,
            leftIndent=12,
            spaceAfter=2,
        )
    )
    ss.add(
        ParagraphStyle(
            "Caption",
            fontName=FONT_ITALIC,
            fontSize=8.5,
            leading=11,
            textColor=colors.HexColor("#64748B"),
            alignment=TA_CENTER,
            spaceBefore=2,
            spaceAfter=8,
        )
    )
    ss.add(
        ParagraphStyle(
            "BoxTitle",
            fontName=FONT_BOLD,
            fontSize=9,
            leading=12,
            textColor=NAVY,
            spaceAfter=3,
        )
    )
    ss.add(
        ParagraphStyle(
            "BoxBody",
            fontName=FONT_REG,
            fontSize=9,
            leading=12.4,
            textColor=SLATE,
            alignment=TA_LEFT,
        )
    )
    ss.add(
        ParagraphStyle(
            "CodeBlockStyle",
            fontName=FONT_MONO,
            fontSize=8.2,
            leading=11.2,
            textColor=CODE_FG,
            backColor=CODE_BG,
        )
    )
    ss.add(
        ParagraphStyle(
            "Small",
            fontName=FONT_REG,
            fontSize=8.4,
            leading=11.4,
            textColor=SLATE,
        )
    )
    ss.add(
        ParagraphStyle(
            "Footer",
            fontName=FONT_REG,
            fontSize=7.5,
            textColor=colors.HexColor("#64748B"),
        )
    )
    ss.add(
        ParagraphStyle(
            "TOCEntry",
            fontName=FONT_REG,
            fontSize=10,
            leading=16,
            textColor=SLATE,
        )
    )
    ss.add(
        ParagraphStyle(
            "Q",
            fontName=FONT_BOLD,
            fontSize=9.4,
            leading=13,
            textColor=NAVY_DARK,
            spaceBefore=4,
            spaceAfter=2,
        )
    )
    ss.add(
        ParagraphStyle(
            "A",
            fontName=FONT_REG,
            fontSize=9.3,
            leading=12.8,
            textColor=SLATE,
            leftIndent=8,
            spaceAfter=6,
        )
    )
    ss.add(
        ParagraphStyle(
            "TableCell",
            fontName=FONT_REG,
            fontSize=8.3,
            leading=11.2,
            textColor=SLATE,
        )
    )
    ss.add(
        ParagraphStyle(
            "TableHead",
            fontName=FONT_BOLD,
            fontSize=8.3,
            leading=11.2,
            textColor=WHITE,
        )
    )
    ss.add(
        ParagraphStyle(
            "CenterWhite",
            fontName=FONT_BOLD,
            fontSize=10,
            textColor=WHITE,
            alignment=TA_CENTER,
        )
    )
    return ss


class ColoredBox(Flowable):
    def __init__(self, title: str, body: str, bg, border, width: float, S):
        super().__init__()
        self.title = title
        self.body = body
        self.bg = bg
        self.border = border
        self.box_width = width
        self.S = S
        self._inner = None

    def wrap(self, availWidth, availHeight):
        w = min(self.box_width, availWidth)
        inner_w = w - 12
        story = []
        if self.title:
            story.append(Paragraph(esc(self.title), self.S["BoxTitle"]))
        for para in self.body.split("\n\n"):
            story.append(Paragraph(esc(para).replace("\n", "<br/>"), self.S["BoxBody"]))
        data = [[story]]
        t = Table(data, colWidths=[inner_w])
        t.setStyle(
            TableStyle(
                [
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                    ("TOPPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ]
            )
        )
        iw, ih = t.wrap(inner_w, availHeight)
        self._inner = t
        self.width = w
        self.height = ih + 12
        return self.width, self.height

    def draw(self):
        self.canv.setFillColor(self.bg)
        self.canv.setStrokeColor(self.border)
        self.canv.setLineWidth(1.2)
        self.canv.roundRect(0, 0, self.width, self.height, 4, fill=1, stroke=1)
        self.canv.setFillColor(self.border)
        self.canv.rect(0, 0, 3.2, self.height, fill=1, stroke=0)
        self._inner.drawOn(self.canv, 8, 6)


class CodeBlock(Flowable):
    def __init__(self, code: str, width: float, caption: str | None = None):
        super().__init__()
        self.code = code.rstrip() + "\n"
        self.box_width = width
        self.caption = caption
        self._pre = None

    def wrap(self, availWidth, availHeight):
        w = min(self.box_width, availWidth)
        style = ParagraphStyle(
            "CodeInner",
            fontName=FONT_MONO,
            fontSize=8.0,
            leading=10.8,
            textColor=CODE_FG,
        )
        pre = Preformatted(self.code, style)
        iw, ih = pre.wrap(w - 16, availHeight)
        self._pre = pre
        self._cap_h = 11 if self.caption else 0
        self.width = w
        self.height = ih + 16 + self._cap_h
        return self.width, self.height

    def draw(self):
        box_h = self.height - self._cap_h
        self.canv.setFillColor(CODE_BG)
        self.canv.roundRect(0, self._cap_h, self.width, box_h, 4, fill=1, stroke=0)
        cy = self._cap_h + box_h - 8
        self.canv.setFillColor(colors.HexColor("#F59E0B"))
        self.canv.circle(10, cy, 2.2, fill=1, stroke=0)
        self.canv.setFillColor(colors.HexColor("#22C55E"))
        self.canv.circle(18, cy, 2.2, fill=1, stroke=0)
        self.canv.setFillColor(colors.HexColor("#3B82F6"))
        self.canv.circle(26, cy, 2.2, fill=1, stroke=0)
        self._pre.drawOn(self.canv, 8, self._cap_h + 4)
        if self.caption:
            self.canv.setFillColor(colors.HexColor("#64748B"))
            self.canv.setFont(FONT_ITALIC, 7.5)
            self.canv.drawString(2, 2, self.caption)


class Heading(Flowable):
    """Heading that notifies the TOC."""

    def __init__(self, text: str, level: int, style, outline_text: str | None = None):
        super().__init__()
        self.text = text
        self.level = level
        self.style = style
        self.outline_text = outline_text or text
        self._p = Paragraph(esc(text), style)

    def wrap(self, availWidth, availHeight):
        w, h = self._p.wrap(availWidth, availHeight)
        self.width, self.height = w, h
        return w, h

    def draw(self):
        self._p.drawOn(self.canv, 0, 0)

    def notify(self, doc):
        pass


class LectureDoc(SimpleDocTemplate):
    def __init__(
        self,
        path: str,
        header_left: str,
        header_right: str,
        cover: dict | None = None,
        **kwargs,
    ):
        kwargs.setdefault("pagesize", A4)
        kwargs.setdefault("leftMargin", 16 * mm)
        kwargs.setdefault("rightMargin", 16 * mm)
        kwargs.setdefault("topMargin", 18 * mm)
        kwargs.setdefault("bottomMargin", 16 * mm)
        super().__init__(path, **kwargs)
        self.header_left = header_left
        self.header_right = header_right
        self.cover = cover or {}
        self._toc_notify = []

    def afterFlowable(self, flowable):
        if isinstance(flowable, Heading):
            text = flowable.outline_text
            if flowable.level == 0:
                self.notify("TOCEntry", (0, text, self.page))
            key = "h%d-%s" % (self.page, "".join(ch if ch.isalnum() else "-" for ch in text[:48]))
            try:
                self.canv.bookmarkPage(key)
                self.canv.addOutlineEntry(text[:80], key, level=min(flowable.level, 2), closed=(flowable.level > 0))
            except Exception:
                pass


def header_footer(canvas, doc: LectureDoc):
    canvas.saveState()
    w, h = A4
    if doc.page == 1:
        canvas.restoreState()
        return
    canvas.setFillColor(NAVY)
    canvas.rect(0, h - 12 * mm, w, 12 * mm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, h - 12.8 * mm, w, 1.6, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont(FONT_BOLD, 8)
    canvas.drawString(16 * mm, h - 7.6 * mm, doc.header_left)
    canvas.setFont(FONT_REG, 8)
    canvas.drawRightString(w - 16 * mm, h - 7.6 * mm, doc.header_right)
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, w, 10 * mm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, 10 * mm, w, 1.4, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont(FONT_REG, 8)
    canvas.drawString(16 * mm, 4 * mm, "Original lecture notes  ·  Not a photocopy of any textbook")
    canvas.setFont(FONT_BOLD, 8)
    canvas.drawRightString(w - 16 * mm, 4 * mm, f"Page {doc.page}")
    canvas.restoreState()


def wrap_canvas_text(canvas, text, x, y, max_width, font, size, leading, fill=WHITE, align="left"):
    canvas.setFont(font, size)
    canvas.setFillColor(fill)
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if canvas.stringWidth(trial, font, size) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    for i, line in enumerate(lines):
        yy = y - i * leading
        if align == "center":
            canvas.drawCentredString(x, yy, line)
        else:
            canvas.drawString(x, yy, line)
    return len(lines) * leading


def draw_cover(canvas, doc):
    w, h = A4
    c = doc.cover
    canvas.setFillColor(NAVY_DARK)
    canvas.rect(0, 0, w, h, fill=1, stroke=0)
    canvas.setFillColor(NAVY)
    canvas.rect(0, h - 46 * mm, w, 46 * mm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, h - 47.4 * mm, w, 3.4, fill=1, stroke=0)
    canvas.setFillColor(TEAL)
    path = canvas.beginPath()
    path.moveTo(0, 0)
    path.lineTo(w, 0)
    path.lineTo(w, 42 * mm)
    path.lineTo(0, 24 * mm)
    path.close()
    canvas.drawPath(path, fill=1, stroke=0)

    canvas.setFillColor(GOLD)
    canvas.circle(28 * mm, h - 24 * mm, 10 * mm, fill=1, stroke=0)
    canvas.setFillColor(NAVY_DARK)
    canvas.setFont(FONT_BOLD, 12)
    canvas.drawCentredString(28 * mm, h - 22.2 * mm, "BIEK")
    canvas.setFillColor(WHITE)
    canvas.setFont(FONT_BOLD, 10)
    canvas.drawString(44 * mm, h - 19 * mm, "BOARD OF INTERMEDIATE EDUCATION, KARACHI")
    canvas.setFont(FONT_REG, 8.5)
    canvas.drawString(44 * mm, h - 25 * mm, "HSC Computer Science  ·  Science General & Humanities")
    canvas.drawString(44 * mm, h - 30 * mm, "Theory 75 marks  +  Practical 25 marks  =  100 per part")

    canvas.setFillColor(GOLD)
    canvas.setFont(FONT_BOLD, 11)
    canvas.drawCentredString(w / 2, h - 62 * mm, c.get("kicker", "COMPLETE LECTURE NOTES"))

    canvas.setFillColor(WHITE)
    canvas.setFont(FONT_BOLD, 24)
    canvas.drawCentredString(w / 2, h - 78 * mm, c.get("title", "Computer Science"))
    canvas.setFont(FONT_REG, 13)
    canvas.setFillColor(colors.HexColor("#BFDBFE"))
    canvas.drawCentredString(w / 2, h - 90 * mm, c.get("subtitle", ""))

    y = h - 112 * mm
    canvas.setFillColor(colors.HexColor("#1E3A8A"))
    canvas.roundRect(22 * mm, y - 82 * mm, w - 44 * mm, 82 * mm, 6, fill=1, stroke=0)
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(1)
    canvas.roundRect(22 * mm, y - 82 * mm, w - 44 * mm, 82 * mm, 6, fill=0, stroke=1)
    canvas.setFillColor(GOLD)
    canvas.setFont(FONT_BOLD, 9)
    canvas.drawString(28 * mm, y - 8 * mm, "WHAT THESE NOTES COVER")
    canvas.setFillColor(WHITE)
    canvas.setFont(FONT_REG, 9.2)
    yy = y - 16 * mm
    for line in c.get("bullets", []):
        canvas.drawString(32 * mm, yy, "▸  " + line)
        yy -= 6.2 * mm

    wrap_canvas_text(
        canvas,
        c.get("footer", ""),
        w / 2,
        16 * mm,
        w - 40 * mm,
        FONT_REG,
        8.2,
        11,
        fill=WHITE,
        align="center",
    )


def on_first_page(canvas, doc):
    canvas.saveState()
    draw_cover(canvas, doc)
    canvas.restoreState()


def later_pages(canvas, doc):
    header_footer(canvas, doc)


class LectureBuilder:
    def __init__(self, content_width: float):
        self.S = styles()
        self.W = content_width
        self.story = []

    def h1(self, text: str):
        self.story.append(CondPageBreak(42 * mm))
        self.story.append(Heading(text, 0, self.S["H1"]))
        line = Table([[""]], colWidths=[self.W], rowHeights=[2])
        line.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), GOLD)]))
        self.story.append(line)
        self.story.append(Spacer(1, 4))

    def h2(self, text: str):
        self.story.append(Heading(text, 1, self.S["H2"]))

    def h3(self, text: str):
        self.story.append(Heading(text, 2, self.S["H3"]))

    def p(self, text: str):
        self.story.append(Paragraph(esc(text), self.S["Body"]))

    def rich(self, html: str):
        self.story.append(Paragraph(html, self.S["Body"]))

    def bullets(self, items: list[str], numbered: bool = False):
        flow_items = []
        for it in items:
            flow_items.append(ListItem(Paragraph(esc(it), self.S["BulletBody"]), leftIndent=8))
        kwargs = dict(
            leftIndent=16,
            bulletFontName=FONT_REG,
            bulletFontSize=9,
            spaceAfter=6,
        )
        if numbered:
            kwargs.update(bulletType="1", start="1")
        else:
            kwargs.update(bulletType="bullet")
        self.story.append(ListFlowable(flow_items, **kwargs))

    def defn(self, term: str, meaning: str):
        self.story.append(
            ColoredBox(f"Definition — {term}", meaning, SOFT, NAVY, self.W, self.S)
        )
        self.story.append(Spacer(1, 5))

    def tip(self, text: str):
        self.story.append(ColoredBox("Board exam tip", text, CREAM, GOLD, self.W, self.S))
        self.story.append(Spacer(1, 5))

    def note(self, text: str):
        self.story.append(ColoredBox("Remember", text, MINT, TEAL, self.W, self.S))
        self.story.append(Spacer(1, 5))

    def warn(self, text: str):
        self.story.append(ColoredBox("Common mistake", text, ROSE, colors.HexColor("#BE123C"), self.W, self.S))
        self.story.append(Spacer(1, 5))

    def code(self, src: str, caption: str | None = None):
        self.story.append(CodeBlock(src, self.W, None))
        if caption:
            self.story.append(Paragraph(esc(caption), self.S["Caption"]))
        else:
            self.story.append(Spacer(1, 6))

    def caption(self, text: str):
        self.story.append(Paragraph(esc(text), self.S["Caption"]))

    def table(self, headers: list[str], rows: list[list[str]], col_widths: list[float] | None = None):
        head = [Paragraph(esc(h), self.S["TableHead"]) for h in headers]
        body = [[Paragraph(esc(c), self.S["TableCell"]) for c in r] for r in rows]
        data = [head] + body
        if col_widths is None:
            n = len(headers)
            col_widths = [self.W / n] * n
        else:
            total = float(sum(col_widths)) or 1.0
            col_widths = [self.W * (w / total) for w in col_widths]
        t = Table(data, colWidths=col_widths, repeatRows=1)
        cmds = [
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
            ("FONTNAME", (0, 0), (-1, 0), FONT_BOLD),
            ("BACKGROUND", (0, 1), (-1, -1), WHITE),
            ("GRID", (0, 0), (-1, -1), 0.4, LINE),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ]
        for i in range(1, len(data)):
            if i % 2 == 0:
                cmds.append(("BACKGROUND", (0, i), (-1, i), colors.HexColor("#F8FAFC")))
        t.setStyle(TableStyle(cmds))
        self.story.append(t)
        self.story.append(Spacer(1, 7))

    def qa(self, q: str, a: str):
        self.story.append(Paragraph(esc("Q. " + q), self.S["Q"]))
        self.story.append(Paragraph(esc("A. " + a), self.S["A"]))

    def mcqs(self, items: list[tuple[str, list[str], str]]):
        letters = "ABCD"
        for i, (q, opts, ans) in enumerate(items, 1):
            self.story.append(Paragraph(esc(f"{i}. {q}"), self.S["BodyLeft"]))
            for j, opt in enumerate(opts):
                mark = "  ✓" if letters[j] == ans else ""
                self.story.append(
                    Paragraph(esc(f"    ({letters[j]}) {opt}{mark}"), self.S["Small"])
                )
            self.story.append(Spacer(1, 3))

    def page_break(self):
        self.story.append(PageBreak())

    def spacer(self, h=4):
        self.story.append(Spacer(1, h))

    def toc(self):
        toc = TableOfContents()
        toc.levelStyles = [
            ParagraphStyle(
                name="TOC0",
                fontName=FONT_BOLD,
                fontSize=11,
                leading=16,
                textColor=NAVY,
                leftIndent=0,
                firstLineIndent=0,
                spaceBefore=6,
            ),
            ParagraphStyle(
                name="TOC1",
                fontName=FONT_REG,
                fontSize=9.5,
                leading=13,
                textColor=SLATE,
                leftIndent=12,
                firstLineIndent=0,
            ),
            ParagraphStyle(
                name="TOC2",
                fontName=FONT_REG,
                fontSize=9,
                leading=12,
                textColor=colors.HexColor("#64748B"),
                leftIndent=24,
            ),
        ]
        self.story.append(Paragraph("Contents", self.S["H1"]))
        self.story.append(toc)
        self.story.append(PageBreak())
        return toc


def build_pdf(path: str, header_left: str, header_right: str, fill, cover: dict):
    doc = LectureDoc(
        path,
        header_left,
        header_right,
        cover=cover,
        title=cover.get("title", "BIEK Computer Science"),
        author="Original BIEK Computer Science lectures",
        subject=cover.get("subtitle", "HSC Computer Science"),
    )
    b = LectureBuilder(doc.width)
    b.story.append(PageBreak())  # page 1 is the canvas cover
    fill(b)
    doc.multiBuild(b.story, onFirstPage=on_first_page, onLaterPages=later_pages)
    return path
