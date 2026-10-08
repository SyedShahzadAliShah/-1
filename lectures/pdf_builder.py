"""Build BIEK Computer Science lecture booklets as PDF."""

from __future__ import annotations

import html
import re
import textwrap
from pathlib import Path

from reportlab.lib.colors import Color, white
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    CondPageBreak,
    Flowable,
    Frame,
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
)
from reportlab.platypus.tableofcontents import TableOfContents

from lectures.diagrams import Diagram, make_diagram

FONT_DIR = Path("/usr/share/fonts/truetype")
pdfmetrics.registerFont(TTFont("Sans", str(FONT_DIR / "liberation/LiberationSans-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Sans-Bold", str(FONT_DIR / "liberation/LiberationSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Sans-Italic", str(FONT_DIR / "liberation/LiberationSans-Italic.ttf")))
pdfmetrics.registerFont(TTFont("Sans-BoldItalic", str(FONT_DIR / "liberation/LiberationSans-BoldItalic.ttf")))
pdfmetrics.registerFont(TTFont("Serif", str(FONT_DIR / "liberation/LiberationSerif-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Serif-Bold", str(FONT_DIR / "liberation/LiberationSerif-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Serif-Italic", str(FONT_DIR / "liberation/LiberationSerif-Italic.ttf")))
pdfmetrics.registerFont(TTFont("Serif-BoldItalic", str(FONT_DIR / "liberation/LiberationSerif-BoldItalic.ttf")))
pdfmetrics.registerFont(TTFont("Mono", str(FONT_DIR / "jetbrains-mono/JetBrainsMono-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Mono-Bold", str(FONT_DIR / "jetbrains-mono/JetBrainsMono-Bold.ttf")))
pdfmetrics.registerFontFamily(
    "Sans",
    normal="Sans",
    bold="Sans-Bold",
    italic="Sans-Italic",
    boldItalic="Sans-BoldItalic",
)
pdfmetrics.registerFontFamily(
    "Serif",
    normal="Serif",
    bold="Serif-Bold",
    italic="Serif-Italic",
    boldItalic="Serif-BoldItalic",
)
pdfmetrics.registerFontFamily("Mono", normal="Mono", bold="Mono-Bold")

NAVY = Color(0.067, 0.165, 0.310)
TEAL = Color(0.055, 0.380, 0.455)
GOLD = Color(0.722, 0.580, 0.275)
INK = Color(0.110, 0.145, 0.180)
MUTED = Color(0.33, 0.38, 0.44)
RULE = Color(0.82, 0.85, 0.88)
CREAM = Color(0.973, 0.965, 0.945)
PALE = Color(0.925, 0.953, 0.957)
PALE_GOLD = Color(0.976, 0.953, 0.894)
CODE_BG = Color(0.965, 0.969, 0.973)
ANSWER_BG = Color(0.945, 0.953, 0.933)
RED_SOFT = Color(0.55, 0.16, 0.16)

PAGE_W, PAGE_H = A4


def _esc(text: str) -> str:
    return html.escape(text, quote=False)


def markup(text: str) -> str:
    """Turn a small markdown subset into reportlab XML.

    Code spans are lifted out first so that ``**`` and ``*`` inside code
    are not read as bold or italic markers.
    """
    text = _esc(text)
    codes: list[str] = []

    def hold_code(match: re.Match) -> str:
        codes.append(match.group(1))
        return f"\x00C{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", hold_code, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*(.+?)\*(?!\*)", r"<i>\1</i>", text)

    def restore(match: re.Match) -> str:
        return f"<font face='Mono' size='8.5'>{codes[int(match.group(1))]}</font>"

    text = re.sub(r"\x00C(\d+)\x00", restore, text)
    return text.replace("\n", "<br/>")


class HeaderMark(Flowable):
    """Set the running header for the following page."""

    def __init__(self, text: str):
        super().__init__()
        self.text = text

    def wrap(self, aw, ah):
        return (0, 0)

    def draw(self):
        return


class TocHeading(Paragraph):
    def __init__(self, text: str, style: ParagraphStyle, level: int, key: str):
        super().__init__(markup(text) if level else text, style)
        self._toc_level = level
        self._toc_text = text
        self._toc_key = key


def styles() -> dict[str, ParagraphStyle]:
    s = {
        "h_unit": ParagraphStyle(
            "UnitHead",
            fontName="Sans-Bold",
            fontSize=16,
            leading=20,
            textColor=NAVY,
            spaceBefore=0,
            spaceAfter=4,
        ),
        "unit_blurb": ParagraphStyle(
            "UnitBlurb",
            fontName="Serif",
            fontSize=10.5,
            leading=15,
            textColor=INK,
            alignment=TA_JUSTIFY,
            spaceAfter=8,
        ),
        "lecture": ParagraphStyle(
            "LectureTitle",
            fontName="Sans-Bold",
            fontSize=13.5,
            leading=17,
            textColor=NAVY,
            spaceBefore=2,
            spaceAfter=4,
        ),
        "h2": ParagraphStyle(
            "H2",
            fontName="Sans-Bold",
            fontSize=11.5,
            leading=14.5,
            textColor=TEAL,
            spaceBefore=9,
            spaceAfter=3,
        ),
        "h3": ParagraphStyle(
            "H3",
            fontName="Sans-Bold",
            fontSize=10.5,
            leading=13.5,
            textColor=NAVY,
            spaceBefore=7,
            spaceAfter=2,
        ),
        "body": ParagraphStyle(
            "Body",
            fontName="Serif",
            fontSize=10.5,
            leading=14.6,
            textColor=INK,
            alignment=TA_JUSTIFY,
            spaceAfter=6,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            fontName="Serif",
            fontSize=10.5,
            leading=14.2,
            textColor=INK,
            leftIndent=4,
        ),
        "caption": ParagraphStyle(
            "Caption",
            fontName="Sans-Italic",
            fontSize=8.5,
            leading=11,
            textColor=MUTED,
            alignment=TA_CENTER,
            spaceBefore=1,
            spaceAfter=8,
        ),
        "box_title": ParagraphStyle(
            "BoxTitle",
            fontName="Sans-Bold",
            fontSize=9,
            leading=12,
            textColor=NAVY,
            spaceAfter=2,
        ),
        "box_body": ParagraphStyle(
            "BoxBody",
            fontName="Serif",
            fontSize=10,
            leading=13.6,
            textColor=INK,
            alignment=TA_LEFT,
        ),
        "th": ParagraphStyle(
            "TH",
            fontName="Sans-Bold",
            fontSize=8.5,
            leading=11,
            textColor=white,
            alignment=TA_LEFT,
        ),
        "td": ParagraphStyle(
            "TD",
            fontName="Serif",
            fontSize=9,
            leading=12,
            textColor=INK,
        ),
        "td_center": ParagraphStyle(
            "TDCenter",
            fontName="Mono",
            fontSize=8.5,
            leading=11,
            textColor=INK,
            alignment=TA_CENTER,
        ),
        "q": ParagraphStyle(
            "Question",
            fontName="Serif",
            fontSize=10.5,
            leading=14.2,
            textColor=INK,
            spaceBefore=3,
            spaceAfter=2,
        ),
        "answer": ParagraphStyle(
            "Answer",
            fontName="Serif",
            fontSize=10,
            leading=13.4,
            textColor=INK,
        ),
        "toc_title": ParagraphStyle(
            "TOCTitle",
            fontName="Sans-Bold",
            fontSize=18,
            leading=22,
            textColor=NAVY,
            spaceAfter=8,
        ),
        "front": ParagraphStyle(
            "Front",
            fontName="Serif",
            fontSize=10.5,
            leading=15,
            textColor=INK,
            alignment=TA_JUSTIFY,
            spaceAfter=8,
        ),
        "front_h": ParagraphStyle(
            "FrontH",
            fontName="Sans-Bold",
            fontSize=13,
            leading=16,
            textColor=NAVY,
            spaceBefore=8,
            spaceAfter=4,
        ),
        "footer": ParagraphStyle(
            "Footer",
            fontName="Sans",
            fontSize=8,
            textColor=MUTED,
        ),
    }
    s["toc0"] = ParagraphStyle(
        "TOC0",
        fontName="Sans-Bold",
        fontSize=11,
        leading=16,
        textColor=NAVY,
        leftIndent=0,
        spaceBefore=6,
    )
    s["toc1"] = ParagraphStyle(
        "TOC1",
        fontName="Serif",
        fontSize=10.5,
        leading=15,
        textColor=INK,
        leftIndent=12,
    )
    return s


S = styles()


def _shade_table(flowables, bg, border, pad=7):
    data = [[flowables]] if not isinstance(flowables, list) else [[flowables]]
    # flowables may already be a list of flowables to stack
    inner = flowables if isinstance(flowables, list) else [flowables]
    table = Table([[inner]], colWidths=["*"])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), bg),
                ("BOX", (0, 0), (-1, -1), 0.6, border),
                ("LEFTPADDING", (0, 0), (-1, -1), pad),
                ("RIGHTPADDING", (0, 0), (-1, -1), pad),
                ("TOPPADDING", (0, 0), (-1, -1), pad),
                ("BOTTOMPADDING", (0, 0), (-1, -1), pad),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return table


def paragraph(text: str, style: str = "body") -> Paragraph:
    return Paragraph(markup(text), S[style])


def bullets(items: list[str]) -> ListFlowable:
    flow = []
    for item in items:
        flow.append(ListItem(Paragraph(markup(item), S["bullet"]), leftIndent=14))
    return ListFlowable(
        flow,
        bulletType="bullet",
        start="bulletchar",
        leftIndent=16,
        bulletFontName="Sans",
        bulletFontSize=9,
        bulletColor=TEAL,
        spaceBefore=1,
        spaceAfter=6,
    )


def numbered(items: list[str]) -> ListFlowable:
    flow = [
        ListItem(Paragraph(markup(item), S["bullet"]), leftIndent=14) for item in items
    ]
    return ListFlowable(
        flow,
        bulletType="1",
        leftIndent=16,
        bulletFontName="Sans-Bold",
        bulletFontSize=9,
        bulletColor=TEAL,
        spaceBefore=1,
        spaceAfter=6,
    )


def data_table(headers: list[str], rows: list[list[str]], col_widths=None, center=False) -> Table:
    head = [Paragraph(markup(h), S["th"]) for h in headers]
    body_style = S["td_center"] if center else S["td"]
    data = [head]
    for row in rows:
        data.append([Paragraph(markup(str(cell)), body_style) for cell in row])
    table = Table(data, colWidths=col_widths, repeatRows=1, hAlign="CENTER")
    style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("FONTNAME", (0, 0), (-1, 0), "Sans-Bold"),
        ("BACKGROUND", (0, 1), (-1, -1), white),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, CREAM]),
        ("GRID", (0, 0), (-1, -1), 0.3, RULE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
    table.setStyle(TableStyle(style_cmds))
    return table


def _wrap_code_line(line: str, width: int = 88) -> list[str]:
    if len(line) <= width:
        return [line]
    indent = len(line) - len(line.lstrip(" "))
    parts = textwrap.wrap(
        line[indent:],
        width=max(20, width - indent),
        break_long_words=False,
        break_on_hyphens=False,
    ) or [line[indent:]]
    return [(" " * (indent + (2 if i else 0))) + part for i, part in enumerate(parts)]


def code_block(source: str, output: str | None = None) -> list:
    source = textwrap.dedent(source).strip("\n")
    wrapped: list[str] = []
    for line in source.splitlines():
        wrapped.extend(_wrap_code_line(line))
    pre = Preformatted(
        "\n".join(wrapped) + "\n",
        ParagraphStyle(
            "Code",
            fontName="Mono",
            fontSize=8,
            leading=10.6,
            textColor=INK,
        ),
    )
    block = _shade_table([pre], CODE_BG, Color(0.75, 0.80, 0.84), pad=6)
    items = [Spacer(1, 3), block]
    if output is not None:
        out = Preformatted(
            output.rstrip() + "\n",
            ParagraphStyle(
                "Out",
                fontName="Mono",
                fontSize=8,
                leading=10.6,
                textColor=Color(0.12, 0.32, 0.22),
            ),
        )
        label = Paragraph("Output", S["box_title"])
        items.append(Spacer(1, 3))
        items.append(_shade_table([label, out], ANSWER_BG, Color(0.62, 0.72, 0.58), pad=6))
    items.append(Spacer(1, 6))
    return items


def callout(kind: str, body: str) -> Table:
    colors = {
        "Remember": (PALE_GOLD, GOLD),
        "Outcomes": (PALE, TEAL),
        "Definition": (PALE, TEAL),
        "Example": (CREAM, NAVY),
        "Exam tip": (Color(0.97, 0.93, 0.93), RED_SOFT),
    }
    bg, border = colors.get(kind, (PALE, TEAL))
    title = Paragraph(kind.upper(), S["box_title"])
    text = Paragraph(markup(body), S["box_body"])
    return _shade_table([title, text], bg, border)


def question_block(questions: list[dict]) -> list:
    items = [Paragraph("Checkpoint", S["h2"])]
    items.append(
        paragraph(
            "Answer these before you look at the key. The short questions are written in the style used in HSSC Section B."
        )
    )
    for i, q in enumerate(questions, 1):
        if q["type"] == "mcq":
            lines = [f"**{i}.** {q['stem']}"]
            for label, choice in zip("ABCD", q["choices"]):
                lines.append(f"&nbsp;&nbsp;{label}. {choice}")
            # markup() escapes ampersands, so put the entities in after it.
            rendered = "<br/>".join(markup(line) for line in lines).replace("&amp;nbsp;", "&nbsp;")
            items.append(Paragraph(rendered, S["q"]))
        else:
            items.append(Paragraph(markup(f"**{i}.** {q['stem']}"), S["q"]))
    answers = [Paragraph("ANSWERS", S["box_title"])]
    for i, q in enumerate(questions, 1):
        if q["type"] == "mcq":
            answers.append(
                Paragraph(markup(f"**{i}.** {q['answer']}. {q['why']}"), S["answer"])
            )
        else:
            answers.append(Paragraph(markup(f"**{i}.** {q['answer']}"), S["answer"]))
    items.append(Spacer(1, 4))
    items.append(_shade_table(answers, ANSWER_BG, Color(0.55, 0.66, 0.48)))
    items.append(Spacer(1, 8))
    return items


class LectureDoc(BaseDocTemplate):
    def __init__(self, path: str, meta: dict):
        super().__init__(
            path,
            pagesize=A4,
            title=meta["title"],
            author="BIEK Computer Science lecture notes",
            subject=meta["subject"],
        )
        self.meta = meta
        self.header_title = meta["grade_label"]
        frame = Frame(
            16 * mm,
            14 * mm,
            PAGE_W - 32 * mm,
            PAGE_H - 32 * mm,
            id="body",
            showBoundary=0,
        )
        cover_frame = Frame(16 * mm, 14 * mm, PAGE_W - 32 * mm, PAGE_H - 28 * mm, id="cover")
        self.addPageTemplates(
            [
                PageTemplate(id="cover", frames=[cover_frame], onPage=self.draw_cover),
                PageTemplate(
                    id="body",
                    frames=[frame],
                    onPage=self.draw_margin,
                    onPageEnd=self.draw_header,
                ),
            ]
        )

    def beforeDocument(self):
        BaseDocTemplate.beforeDocument(self)
        self.header_title = "How to use these lectures"
        self._header_for_this_page = self.header_title
        self._header_locked = False

    def handle_pageBegin(self):
        BaseDocTemplate.handle_pageBegin(self)
        self._header_for_this_page = self.header_title
        self._header_locked = False

    def afterFlowable(self, flowable):
        if isinstance(flowable, (HeaderMark, TocHeading)):
            text = flowable.text if isinstance(flowable, HeaderMark) else flowable._toc_text
            if not self._header_locked:
                self._header_for_this_page = text
            self.header_title = text
            self._header_locked = True
        elif isinstance(flowable, (Paragraph, Table, Preformatted, ListFlowable, Diagram)):
            self._header_locked = True
        if isinstance(flowable, TocHeading):
            self.canv.bookmarkPage(flowable._toc_key)
            self.notify(
                "TOCEntry",
                (flowable._toc_level, flowable._toc_text, self.page, flowable._toc_key),
            )
            try:
                self.canv.addOutlineEntry(
                    flowable._toc_text, flowable._toc_key, level=flowable._toc_level, closed=0
                )
            except Exception:
                pass

    def draw_cover(self, canv, doc):
        canv.saveState()
        canv.setFillColor(NAVY)
        canv.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
        canv.setFillColor(TEAL)
        canv.rect(0, 0, 12 * mm, PAGE_H, fill=1, stroke=0)
        canv.setFillColor(GOLD)
        canv.rect(12 * mm, 0, 2.2 * mm, PAGE_H, fill=1, stroke=0)
        canv.setFillColor(GOLD)
        canv.rect(28 * mm, PAGE_H - 48 * mm, 70 * mm, 1.4, fill=1, stroke=0)
        canv.setFillColor(white)
        canv.setFont("Sans", 11)
        canv.drawString(28 * mm, PAGE_H - 42 * mm, "BOARD OF INTERMEDIATE EDUCATION KARACHI")
        canv.setFont("Sans", 12)
        canv.setFillColor(GOLD)
        canv.drawString(28 * mm, PAGE_H - 62 * mm, "HIGHER SECONDARY  ·  COMPUTER SCIENCE")
        canv.setFillColor(white)
        canv.setFont("Sans-Bold", 28)
        canv.drawString(28 * mm, PAGE_H - 82 * mm, self.meta["grade_label"])
        canv.setFont("Sans-Bold", 22)
        y = PAGE_H - 98 * mm
        for line in self.meta["cover_lines"]:
            canv.drawString(28 * mm, y, line)
            y -= 10 * mm
        canv.setStrokeColor(GOLD)
        canv.setLineWidth(1)
        canv.line(28 * mm, 78 * mm, PAGE_W - 22 * mm, 78 * mm)
        canv.setFillColor(Color(0.85, 0.90, 0.93))
        canv.setFont("Sans", 10)
        canv.drawString(28 * mm, 66 * mm, self.meta["alignment"])
        canv.drawString(28 * mm, 54 * mm, "Original lecture notes for classroom and self-study")
        canv.setFont("Sans", 9)
        canv.drawString(28 * mm, 38 * mm, "Session 2026–27")
        canv.restoreState()

    def draw_margin(self, canv, doc):
        canv.saveState()
        canv.setFillColor(NAVY)
        canv.rect(0, PAGE_H - 8 * mm, PAGE_W, 8 * mm, fill=1, stroke=0)
        canv.setFillColor(GOLD)
        canv.rect(0, PAGE_H - 9.2 * mm, PAGE_W, 1.2 * mm, fill=1, stroke=0)
        canv.setFillColor(NAVY)
        canv.rect(0, 0, PAGE_W, 8 * mm, fill=1, stroke=0)
        canv.setFillColor(white)
        canv.setFont("Sans", 8)
        canv.drawString(16 * mm, 3.1 * mm, self.meta["footer"])
        canv.drawRightString(PAGE_W - 16 * mm, 3.1 * mm, str(doc.page))
        canv.restoreState()

    def draw_header(self, canv, doc):
        canv.saveState()
        canv.setFillColor(white)
        canv.setFont("Sans", 8)
        title = getattr(self, "_header_for_this_page", "") or ""
        if len(title) > 78:
            title = title[:75] + "..."
        canv.drawString(16 * mm, PAGE_H - 5.6 * mm, title)
        canv.drawRightString(PAGE_W - 16 * mm, PAGE_H - 5.6 * mm, "Computer Science")
        canv.restoreState()


def front_matter(meta: dict) -> list:
    story = []
    story.append(Paragraph("How to use these lectures", S["front_h"]))
    story.append(
        Paragraph(
            markup(meta["preface"]),
            S["front"],
        )
    )
    story.append(Paragraph("What each lecture contains", S["front_h"]))
    story.append(
        bullets(
            [
                "**Learning outcomes** match the student learning outcomes of the National Curriculum of Pakistan 2022–23 for this grade.",
                "**Explanations and worked examples** are written so that a student can revise a period without a second textbook open.",
                "**Python programs** that are complete scripts include the output produced by running them.",
                "**Checkpoint** questions follow the HSSC pattern: one-mark choices and three-mark short answers, with a key underneath.",
            ]
        )
    )
    story.append(Paragraph("A note on the source of the course", S["front_h"]))
    story.append(
        paragraph(
            "Karachi intermediate colleges teach the Sindh Textbook Board books. For 2026–27 those books follow the Sindh Curriculum of Computer Science 2024, which is aligned with the National Curriculum of Pakistan 2022–23. Class XI and Class XII are organised by the same domains: Computer Systems, Computational Thinking and Algorithms, Programming Fundamentals, Data and Analysis, Applications and Impacts of Computing, Digital Literacy, and Entrepreneurship in the Digital Age. Programming in this course is Python, not the older C++ syllabus."
        )
    )
    story.append(
        callout(
            "Remember",
            "These notes are an original teaching set. They are not an official BIEK paper, not a past paper, and not a copy of the Sindh Textbook Board book. Use the textbook alongside them for exercises set by your teacher.",
        )
    )
    story.append(Spacer(1, 8))
    story.append(Paragraph("Units in this booklet", S["front_h"]))
    rows = []
    for unit in meta["units"]:
        rows.append([unit["code"], unit["title"], unit["weight"]])
    story.append(
        data_table(
            ["Unit", "Title", "Emphasis in the course"],
            rows,
        )
    )
    story.append(Spacer(1, 8))
    return story


def render_blocks(blocks: list, width: float) -> list:
    flow = []
    for block in blocks:
        kind = block[0]
        if kind == "h2":
            flow.append(Paragraph(markup(block[1]), S["h2"]))
        elif kind == "h3":
            flow.append(Paragraph(markup(block[1]), S["h3"]))
        elif kind == "p":
            flow.append(paragraph(block[1]))
        elif kind == "ul":
            flow.append(bullets(block[1]))
        elif kind == "ol":
            flow.append(numbered(block[1]))
        elif kind == "note":
            flow.append(Spacer(1, 2))
            flow.append(callout(block[1], block[2]))
            flow.append(Spacer(1, 6))
        elif kind == "table":
            headers, rows = block[1], block[2]
            center = block[3] if len(block) > 3 else False
            flow.append(Spacer(1, 2))
            flow.append(data_table(headers, rows, center=center))
            if len(block) > 4 and block[4]:
                flow.append(Paragraph(block[4], S["caption"]))
            else:
                flow.append(Spacer(1, 6))
        elif kind == "code":
            source = block[1]
            output = block[2] if len(block) > 2 else None
            flow.extend(code_block(source, output))
        elif kind == "diagram":
            diagram, caption = make_diagram(block[1], width)
            flow.append(Spacer(1, 3))
            flow.append(diagram)
            if caption:
                flow.append(Paragraph(caption, S["caption"]))
            else:
                flow.append(Spacer(1, 6))
        else:
            raise ValueError(f"Unknown block {kind}")
    return flow


def build_story(meta: dict, units: list[dict]) -> list:
    story = [NextPageTemplate("body"), PageBreak()]
    story.extend(front_matter(meta))
    story.append(HeaderMark("Contents"))
    story.append(PageBreak())
    toc = TableOfContents()
    toc.levelStyles = [S["toc0"], S["toc1"]]
    toc.dotsMinLevel = 0
    story.append(TocHeading("Contents", S["toc_title"], 0, "contents"))
    # The contents heading itself should not be a TOC entry at level 0 mixed with units.
    # Use a plain paragraph instead.
    story.pop()
    story.append(Paragraph("Contents", S["toc_title"]))
    story.append(toc)
    story.append(PageBreak())

    for unit in units:
        key = "unit-" + unit["code"].replace(" ", "-")
        story.append(CondPageBreak(160))
        story.append(TocHeading(f"{unit['code']}  {unit['title']}", S["h_unit"], 0, key))
        story.append(paragraph(unit["intro"]))
        if unit.get("outcomes"):
            story.append(
                callout("Outcomes", "By the end of this unit you should be able to: " + " ".join(unit["outcomes"]))
            )
            story.append(Spacer(1, 6))
        for lecture in unit["lectures"]:
            story.append(CondPageBreak(180))
            lkey = "lec-" + lecture["code"].replace(".", "-")
            opening = [
                TocHeading(
                    f"Lecture {lecture['code']}   {lecture['title']}",
                    S["lecture"],
                    1,
                    lkey,
                ),
                callout("Outcomes", " ".join(lecture["outcomes"])),
                Spacer(1, 6),
            ]
            story.append(KeepTogether(opening))
            story.extend(render_blocks(lecture["blocks"], PAGE_W - 32 * mm))
            story.extend(question_block(lecture["questions"]))
        if unit.get("lab"):
            story.append(Paragraph("Practical work", S["h2"]))
            story.append(paragraph(unit["lab_intro"]))
            story.append(numbered(unit["lab"]))
    return story


def build_pdf(path: Path, meta: dict, units: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = LectureDoc(str(path), meta)
    doc.multiBuild(build_story(meta, units))
