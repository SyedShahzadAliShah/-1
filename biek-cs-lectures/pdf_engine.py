"""Academic PDF engine for BIEK CS lecture notes."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    FrameBreak,
    KeepTogether,
    ListFlowable,
    ListItem,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
    Flowable,
)

NAVY = colors.HexColor("#0B2545")
TEAL = colors.HexColor("#0D7377")
GOLD = colors.HexColor("#C9A227")
CREAM = colors.HexColor("#F7F3E9")
SOFT = colors.HexColor("#E8F1F2")
DEF_BG = colors.HexColor("#EAF4FF")
TIP_BG = colors.HexColor("#FFF6DC")
EXAM_BG = colors.HexColor("#F3E8FF")
CODE_BG = colors.HexColor("#1B2430")
CODE_FG = colors.HexColor("#E8F0E8")
MUTED = colors.HexColor("#5A6570")
RULE = colors.HexColor("#D5D8DC")
WHITE = colors.white
BLACK = colors.HexColor("#1A1A1A")

FONT_DIR = Path("/usr/share/fonts/truetype")
LIB = FONT_DIR / "liberation"
DEJ = FONT_DIR / "dejavu"

pdfmetrics.registerFont(TTFont("Body", str(LIB / "LiberationSerif-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Body-Bold", str(LIB / "LiberationSerif-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Body-Italic", str(LIB / "LiberationSerif-Italic.ttf")))
pdfmetrics.registerFont(TTFont("Body-BoldItalic", str(LIB / "LiberationSerif-BoldItalic.ttf")))
pdfmetrics.registerFont(TTFont("Head", str(LIB / "LiberationSans-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Head-Bold", str(LIB / "LiberationSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Head-Italic", str(LIB / "LiberationSans-Italic.ttf")))
pdfmetrics.registerFont(TTFont("Mono", str(DEJ / "DejaVuSansMono.ttf")))
pdfmetrics.registerFont(TTFont("Mono-Bold", str(DEJ / "DejaVuSansMono-Bold.ttf")))
pdfmetrics.registerFontFamily(
    "Body",
    normal="Body",
    bold="Body-Bold",
    italic="Body-Italic",
    boldItalic="Body-BoldItalic",
)
pdfmetrics.registerFontFamily(
    "Head",
    normal="Head",
    bold="Head-Bold",
    italic="Head-Italic",
    boldItalic="Head-Bold",
)


def make_styles():
    base = getSampleStyleSheet()
    styles = {
        "cover_kicker": ParagraphStyle(
            "cover_kicker",
            fontName="Head-Bold",
            fontSize=11,
            textColor=GOLD,
            alignment=TA_CENTER,
            tracking=1.4,
            spaceAfter=6,
        ),
        "cover_title": ParagraphStyle(
            "cover_title",
            fontName="Head-Bold",
            fontSize=26,
            leading=32,
            textColor=WHITE,
            alignment=TA_CENTER,
            spaceAfter=8,
        ),
        "cover_sub": ParagraphStyle(
            "cover_sub",
            fontName="Body",
            fontSize=13,
            leading=18,
            textColor=CREAM,
            alignment=TA_CENTER,
            spaceAfter=6,
        ),
        "h1": ParagraphStyle(
            "h1",
            fontName="Head-Bold",
            fontSize=18,
            leading=22,
            textColor=NAVY,
            spaceBefore=4,
            spaceAfter=8,
        ),
        "h2": ParagraphStyle(
            "h2",
            fontName="Head-Bold",
            fontSize=13.5,
            leading=17,
            textColor=TEAL,
            spaceBefore=10,
            spaceAfter=5,
        ),
        "h3": ParagraphStyle(
            "h3",
            fontName="Head-Bold",
            fontSize=11.5,
            leading=15,
            textColor=NAVY,
            spaceBefore=8,
            spaceAfter=3,
        ),
        "body": ParagraphStyle(
            "body",
            fontName="Body",
            fontSize=10.5,
            leading=14.5,
            textColor=BLACK,
            alignment=TA_JUSTIFY,
            spaceAfter=6,
        ),
        "center": ParagraphStyle(
            "center",
            fontName="Body-Italic",
            fontSize=9,
            leading=12,
            textColor=MUTED,
            alignment=TA_CENTER,
            spaceBefore=2,
            spaceAfter=8,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            fontName="Body",
            fontSize=10.5,
            leading=14.2,
            textColor=BLACK,
            leftIndent=12,
            spaceAfter=2,
        ),
        "caption": ParagraphStyle(
            "caption",
            fontName="Head-Italic",
            fontSize=8.5,
            leading=11,
            textColor=MUTED,
            alignment=TA_CENTER,
            spaceBefore=2,
            spaceAfter=8,
        ),
        "box_title": ParagraphStyle(
            "box_title",
            fontName="Head-Bold",
            fontSize=9,
            leading=12,
            textColor=NAVY,
            spaceAfter=2,
        ),
        "box_body": ParagraphStyle(
            "box_body",
            fontName="Body",
            fontSize=10,
            leading=13.4,
            textColor=BLACK,
        ),
        "code": ParagraphStyle(
            "code",
            fontName="Mono",
            fontSize=8.2,
            leading=11.2,
            textColor=CODE_FG,
        ),
        "toc_chap": ParagraphStyle(
            "toc_chap",
            fontName="Head-Bold",
            fontSize=11,
            leading=16,
            textColor=NAVY,
            spaceBefore=4,
        ),
        "toc_item": ParagraphStyle(
            "toc_item",
            fontName="Body",
            fontSize=10.5,
            leading=15,
            textColor=BLACK,
        ),
        "footer": ParagraphStyle(
            "footer",
            fontName="Head",
            fontSize=8,
            textColor=MUTED,
        ),
        "small": ParagraphStyle(
            "small",
            fontName="Body",
            fontSize=9,
            leading=12,
            textColor=BLACK,
        ),
        "th": ParagraphStyle(
            "th",
            fontName="Head-Bold",
            fontSize=8.6,
            leading=11.5,
            textColor=WHITE,
        ),
        "td": ParagraphStyle(
            "td",
            fontName="Body",
            fontSize=8.8,
            leading=11.8,
            textColor=BLACK,
        ),
        "td_b": ParagraphStyle(
            "td_b",
            fontName="Body-Bold",
            fontSize=8.8,
            leading=11.8,
            textColor=NAVY,
        ),
        "q": ParagraphStyle(
            "q",
            fontName="Body-Bold",
            fontSize=10.5,
            leading=14,
            textColor=NAVY,
            spaceBefore=4,
            spaceAfter=2,
        ),
        "a": ParagraphStyle(
            "a",
            fontName="Body",
            fontSize=10.5,
            leading=14.2,
            textColor=BLACK,
            alignment=TA_JUSTIFY,
            spaceAfter=6,
        ),
    }
    return styles


class ColoredBox(Flowable):
    def __init__(self, title, body_flowables, bg, accent, width=None):
        super().__init__()
        self.title = title
        self.body = body_flowables
        self.bg = bg
        self.accent = accent
        self.box_width = width
        self._inner = None

    def wrap(self, availWidth, availHeight):
        self.box_width = availWidth
        inner_w = availWidth - 16
        from reportlab.platypus.doctemplate import Frame
        # measure by wrapping each
        h = 10
        self._sizes = []
        for f in self.body:
            w, fh = f.wrap(inner_w, availHeight)
            self._sizes.append((w, fh))
            h += fh + 2
        self.height = h + 10
        self.width = availWidth
        return availWidth, self.height

    def draw(self):
        self.canv.setFillColor(self.bg)
        self.canv.setStrokeColor(self.accent)
        self.canv.setLineWidth(1.2)
        self.canv.roundRect(0, 0, self.width, self.height, 4, fill=1, stroke=1)
        self.canv.setFillColor(self.accent)
        self.canv.rect(0, 0, 5, self.height, fill=1, stroke=0)
        y = self.height - 8
        inner_w = self.width - 16
        for f, (w, h) in zip(self.body, self._sizes):
            y -= h
            f.drawOn(self.canv, 12, y)
            y -= 2


class HLine(Flowable):
    def __init__(self, color=GOLD, thickness=1.5, space=6):
        super().__init__()
        self.color = color
        self.thickness = thickness
        self.space = space

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        self.height = self.space * 2 + self.thickness
        return self.width, self.height

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        y = self.space
        self.canv.line(0, y, self.width, y)


class CoverBand(Flowable):
    def __init__(self, height=40 * mm):
        super().__init__()
        self._h = height

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        self.height = self._h
        return self.width, self.height

    def draw(self):
        pass


class LectureDoc(BaseDocTemplate):
    def __init__(self, path, book_label, class_label):
        self.book_label = book_label
        self.class_label = class_label
        super().__init__(
            str(path),
            pagesize=A4,
            leftMargin=16 * mm,
            rightMargin=16 * mm,
            topMargin=18 * mm,
            bottomMargin=16 * mm,
            title=book_label,
            author="Original exam-oriented lecture notes",
            subject=f"BIEK Computer Science {class_label}",
        )
        page_w, page_h = A4
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            page_w - self.leftMargin - self.rightMargin,
            page_h - self.topMargin - self.bottomMargin,
            id="normal",
        )
        cover_frame = Frame(
            0,
            0,
            page_w,
            page_h,
            id="cover",
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
        )
        self.addPageTemplates(
            [
                PageTemplate(id="cover", frames=[cover_frame], onPage=self._cover_page),
                PageTemplate(id="body", frames=[frame], onPage=self._body_page),
            ]
        )

    def _cover_page(self, canv, doc):
        canv.saveState()
        w, h = A4
        canv.setFillColor(NAVY)
        canv.rect(0, 0, w, h, fill=1, stroke=0)
        canv.setFillColor(TEAL)
        canv.rect(0, 0, 14 * mm, h, fill=1, stroke=0)
        canv.setFillColor(GOLD)
        canv.rect(14 * mm, 0, 3 * mm, h, fill=1, stroke=0)
        canv.setFillColor(colors.HexColor("#12315A"))
        canv.rect(0, h - 28 * mm, w, 28 * mm, fill=1, stroke=0)
        canv.setFillColor(GOLD)
        canv.rect(0, h - 30 * mm, w, 2.2 * mm, fill=1, stroke=0)
        canv.setFillColor(GOLD)
        canv.rect(0, 22 * mm, w, 2.2 * mm, fill=1, stroke=0)
        canv.setFillColor(colors.HexColor("#12315A"))
        canv.rect(0, 0, w, 22 * mm, fill=1, stroke=0)
        canv.setFillColor(CREAM)
        canv.setFont("Head", 8)
        canv.drawCentredString(
            w / 2,
            10 * mm,
            "Original teaching notes  |  Not an official BIEK publication  |  Aligned to Model Paper 2026",
        )
        canv.restoreState()

    def _body_page(self, canv, doc):
        canv.saveState()
        w, h = A4
        canv.setFillColor(NAVY)
        canv.rect(0, h - 12 * mm, w, 12 * mm, fill=1, stroke=0)
        canv.setFillColor(GOLD)
        canv.rect(0, h - 13.2 * mm, w, 1.2 * mm, fill=1, stroke=0)
        canv.setFillColor(WHITE)
        canv.setFont("Head", 8)
        canv.drawString(16 * mm, h - 8 * mm, self.book_label)
        canv.drawRightString(w - 16 * mm, h - 8 * mm, self.class_label)
        canv.setFillColor(NAVY)
        canv.rect(0, 0, w, 12 * mm, fill=1, stroke=0)
        canv.setFillColor(GOLD)
        canv.rect(0, 12 * mm, w, 1.1 * mm, fill=1, stroke=0)
        canv.setFillColor(WHITE)
        canv.setFont("Head", 8)
        canv.drawString(16 * mm, 5 * mm, "Exam-oriented lectures  ·  Original notes")
        canv.drawRightString(w - 16 * mm, 5 * mm, f"Page {doc.page}")
        canv.restoreState()


class LectureBuilder:
    def __init__(self, book_label, class_label):
        self.book_label = book_label
        self.class_label = class_label
        self.styles = make_styles()
        self.story = []
        self.toc = []

    def p(self, text, style="body"):
        self.story.append(Paragraph(text, self.styles[style]))

    def h1(self, text):
        self.story.append(Paragraph(text, self.styles["h1"]))
        self.story.append(HLine())

    def h2(self, text):
        self.story.append(Paragraph(text, self.styles["h2"]))

    def h3(self, text):
        self.story.append(Paragraph(text, self.styles["h3"]))

    def spacer(self, mm_h=3):
        self.story.append(Spacer(1, mm_h * mm))

    def bullets(self, items):
        for it in items:
            self.story.append(Paragraph(f"• {it}", self.styles["bullet"]))
        self.spacer(2)

    def numbered(self, items):
        for i, it in enumerate(items, 1):
            self.story.append(Paragraph(f"<b>{i}.</b> {it}", self.styles["bullet"]))
        self.spacer(2)

    def caption(self, text):
        self.story.append(Paragraph(text, self.styles["caption"]))

    def page_break(self):
        self.story.append(PageBreak())

    def box(self, kind, title, paragraphs):
        bg = {"def": DEF_BG, "tip": TIP_BG, "exam": EXAM_BG, "note": SOFT}.get(kind, SOFT)
        accent = {"def": TEAL, "tip": GOLD, "exam": colors.HexColor("#6B3FA0"), "note": NAVY}.get(
            kind, TEAL
        )
        body = [Paragraph(title, self.styles["box_title"])]
        if isinstance(paragraphs, str):
            paragraphs = [paragraphs]
        for para in paragraphs:
            body.append(Paragraph(para, self.styles["box_body"]))
        self.story.append(ColoredBox(title, body, bg, accent))
        self.spacer(3)

    def definition(self, term, meaning):
        self.box("def", f"BOARD DEFINITION — {term}", [meaning])

    def exam_tip(self, text):
        self.box("tip", "EXAM TIP", [text])

    def board_q(self, q, a):
        self.box("exam", "LIKELY BOARD QUESTION", [f"<b>Q.</b> {q}", f"<b>Model answer.</b> {a}"])

    def table(self, headers, rows, col_widths=None):
        s = self.styles
        head = [Paragraph(h, s["th"]) for h in headers]
        data = [head]
        for r in rows:
            line = []
            for i, cell in enumerate(r):
                st = s["td_b"] if i == 0 else s["td"]
                line.append(Paragraph(str(cell), st))
            data.append(line)
        t = Table(data, colWidths=col_widths, repeatRows=1)
        t.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                    ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
                    ("BACKGROUND", (0, 1), (-1, -1), CREAM),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CREAM, WHITE]),
                    ("GRID", (0, 0), (-1, -1), 0.4, RULE),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 5),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ]
            )
        )
        self.story.append(t)
        self.spacer(4)

    def code(self, source, caption=None):
        lines = source.strip("\n").split("\n")
        body = [Paragraph(title_safe := "PROGRAM / CODE", self.styles["box_title"])]
        # Use Preformatted inside a table for dark background
        pre = Preformatted(source.strip("\n"), self.styles["code"])
        inner = Table([[pre]], colWidths=[None])
        inner.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
                    ("LEFTPADDING", (0, 0), (-1, -1), 8),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                    ("TOPPADDING", (0, 0), (-1, -1), 6),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ]
            )
        )
        wrap = Table([[Paragraph("PROGRAM / CODE", self.styles["box_title"])], [inner]])
        wrap.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
                    ("BOX", (0, 0), (-1, -1), 1, NAVY),
                    ("LEFTPADDING", (0, 0), (-1, 0), 8),
                    ("TOPPADDING", (0, 0), (-1, 0), 6),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 2),
                ]
            )
        )
        # Title in cream on navy bar
        header = Paragraph('<font color="#F7F3E9"><b>PROGRAM / CODE</b></font>', self.styles["box_title"])
        block = Table([[header], [inner]])
        block.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                    ("BACKGROUND", (0, 1), (-1, 1), CODE_BG),
                    ("BOX", (0, 0), (-1, -1), 0.8, NAVY),
                    ("LEFTPADDING", (0, 0), (-1, -1), 8),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                    ("TOPPADDING", (0, 0), (-1, 0), 5),
                    ("BOTTOMPADDING", (0, 0), (-1, 0), 5),
                    ("TOPPADDING", (0, 1), (-1, 1), 0),
                    ("BOTTOMPADDING", (0, 1), (-1, 1), 0),
                ]
            )
        )
        self.story.append(block)
        if caption:
            self.caption(caption)
        else:
            self.spacer(3)

    def qa(self, q, a):
        self.p(f"Q. {q}", "q")
        self.p(a, "a")

    def add(self, flowable):
        self.story.append(flowable)

    def chapter_banner(self, number, title, paper, weight):
        s = self.styles
        data = [
            [
                Paragraph(
                    f'<font color="#C9A227">LECTURE {number}</font><br/>'
                    f'<font color="#FFFFFF" size="16"><b>{title}</b></font><br/>'
                    f'<font color="#E8F1F2" size="9">{paper}  ·  {weight}</font>',
                    ParagraphStyle("ban", fontName="Head", fontSize=11, leading=16),
                )
            ]
        ]
        t = Table(data, colWidths=[178 * mm])
        t.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), NAVY),
                    ("LEFTPADDING", (0, 0), (-1, -1), 12),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                    ("TOPPADDING", (0, 0), (-1, -1), 12),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
                    ("BOX", (0, 0), (-1, -1), 2, GOLD),
                ]
            )
        )
        self.story.append(t)
        self.spacer(5)
        self.toc.append((number, title))

    def build(self, path):
        doc = LectureDoc(path, self.book_label, self.class_label)
        doc.build(self.story)
        return path
