"""Render BIEK Computer Science lecture notes to print-ready A4 PDFs."""

from __future__ import annotations

import hashlib
import re
import tempfile
from pathlib import Path

import cairosvg
from reportlab.graphics import renderPDF
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import ImageReader
from svglib.svglib import svg2rlg
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
    HRFlowable,
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

NAVY = HexColor("#0B3A5B")
NAVY_DEEP = HexColor("#07263C")
TEAL = HexColor("#0F6E6E")
GOLD = HexColor("#C4A35A")
INK = HexColor("#1C2430")
MUTED = HexColor("#5C6B7A")
RULE = HexColor("#D5DEE8")
ROW = HexColor("#F4F7FB")
CODE_BG = HexColor("#F6F3EC")
CODE_INK = HexColor("#1E2430")

PAGE_W, PAGE_H = A4
LEFT = 16 * mm
RIGHT = 16 * mm
CONTENT_W = PAGE_W - LEFT - RIGHT
MATH_RE = re.compile(r"\\\((.+?)\\\)", re.S)
MATH = {"svg": {}, "png": {}, "dir": None}

CALLOUT = {
    "define": (NAVY, HexColor("#E7EEF6"), "Definition"),
    "exam": (HexColor("#8A5A00"), HexColor("#FFF6E0"), "Exam tip"),
    "lab": (HexColor("#0F6E56"), HexColor("#E5F6F1"), "In the lab"),
    "example": (TEAL, HexColor("#E7F4F4"), "Worked example"),
    "warn": (HexColor("#8C2F2F"), HexColor("#FDECEC"), "Common mistake"),
    "answer": (HexColor("#1F4D3A"), HexColor("#F3FAF6"), "Model answer"),
    "note": (HexColor("#334155"), HexColor("#F1F5F9"), "Note"),
}


def register_fonts() -> None:
    pairs = {
        "NotoSerif": "/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf",
        "NotoSerif-Bold": "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf",
        "NotoSerif-Italic": "/usr/share/fonts/truetype/noto/NotoSerif-Italic.ttf",
        "NotoSerif-BoldItalic": "/usr/share/fonts/truetype/noto/NotoSerif-BoldItalic.ttf",
        "NotoSans": "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
        "NotoSans-Bold": "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
        "NotoSans-Italic": "/usr/share/fonts/truetype/noto/NotoSans-Italic.ttf",
        "NotoSans-BoldItalic": "/usr/share/fonts/truetype/noto/NotoSans-BoldItalic.ttf",
        "JetBrainsMono": "/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-Regular.ttf",
        "JetBrainsMono-Bold": "/usr/share/fonts/truetype/jetbrains-mono/JetBrainsMono-Bold.ttf",
    }
    for name, path in pairs.items():
        pdfmetrics.registerFont(TTFont(name, path))
    pdfmetrics.registerFontFamily(
        "NotoSerif",
        normal="NotoSerif",
        bold="NotoSerif-Bold",
        italic="NotoSerif-Italic",
        boldItalic="NotoSerif-BoldItalic",
    )
    pdfmetrics.registerFontFamily(
        "NotoSans",
        normal="NotoSans",
        bold="NotoSans-Bold",
        italic="NotoSans-Italic",
        boldItalic="NotoSans-BoldItalic",
    )
    pdfmetrics.registerFontFamily(
        "JetBrainsMono",
        normal="JetBrainsMono",
        bold="JetBrainsMono-Bold",
        italic="JetBrainsMono",
        boldItalic="JetBrainsMono-Bold",
    )


def make_styles() -> dict[str, ParagraphStyle]:
    styles = {
        "h1": ParagraphStyle(
            "h1",
            fontName="NotoSans-Bold",
            fontSize=18,
            leading=22,
            textColor=NAVY,
            spaceBefore=0,
            spaceAfter=2,
        ),
        "kicker": ParagraphStyle(
            "kicker",
            fontName="NotoSans-Bold",
            fontSize=8.5,
            leading=11,
            textColor=TEAL,
            spaceAfter=1,
        ),
        "h2": ParagraphStyle(
            "h2",
            fontName="NotoSans-Bold",
            fontSize=13,
            leading=16,
            textColor=NAVY,
            spaceBefore=8,
            spaceAfter=2,
        ),
        "h3": ParagraphStyle(
            "h3",
            fontName="NotoSans-Bold",
            fontSize=11.5,
            leading=14,
            textColor=TEAL,
            spaceBefore=7,
            spaceAfter=2,
        ),
        "body": ParagraphStyle(
            "body",
            fontName="NotoSerif",
            fontSize=10.5,
            leading=14.4,
            textColor=INK,
            alignment=TA_JUSTIFY,
            spaceAfter=6,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            fontName="NotoSerif",
            fontSize=10.5,
            leading=14.2,
            textColor=INK,
            alignment=TA_LEFT,
        ),
        "caption": ParagraphStyle(
            "caption",
            fontName="NotoSans-Italic",
            fontSize=8.5,
            leading=11,
            textColor=MUTED,
            alignment=TA_LEFT,
            spaceBefore=1,
            spaceAfter=8,
        ),
        "th": ParagraphStyle(
            "th",
            fontName="NotoSans-Bold",
            fontSize=8.5,
            leading=11,
            textColor=white,
            alignment=TA_LEFT,
        ),
        "td": ParagraphStyle(
            "td",
            fontName="NotoSans",
            fontSize=8.5,
            leading=11,
            textColor=INK,
            alignment=TA_LEFT,
        ),
        "td_center": ParagraphStyle(
            "td_center",
            fontName="NotoSans",
            fontSize=8.5,
            leading=11,
            textColor=INK,
            alignment=TA_CENTER,
        ),
        "code": ParagraphStyle(
            "code",
            fontName="JetBrainsMono",
            fontSize=8,
            leading=10.6,
            textColor=CODE_INK,
            alignment=TA_LEFT,
        ),
        "code_label": ParagraphStyle(
            "code_label",
            fontName="NotoSans-Bold",
            fontSize=7.5,
            leading=9,
            textColor=MUTED,
            spaceAfter=2,
        ),
        "callout_title": ParagraphStyle(
            "callout_title",
            fontName="NotoSans-Bold",
            fontSize=8.5,
            leading=11,
            textColor=NAVY,
            spaceAfter=2,
        ),
        "callout_body": ParagraphStyle(
            "callout_body",
            fontName="NotoSerif",
            fontSize=10,
            leading=13.4,
            textColor=INK,
            alignment=TA_LEFT,
            spaceAfter=3,
        ),
        "toc_title": ParagraphStyle(
            "toc_title",
            fontName="NotoSans-Bold",
            fontSize=18,
            leading=22,
            textColor=NAVY,
            spaceAfter=8,
        ),
        "front_h": ParagraphStyle(
            "front_h",
            fontName="NotoSans-Bold",
            fontSize=14,
            leading=18,
            textColor=NAVY,
            spaceBefore=8,
            spaceAfter=4,
        ),
        "footer": ParagraphStyle(
            "footer",
            fontName="NotoSans",
            fontSize=8,
            leading=10,
            textColor=white,
        ),
        "small": ParagraphStyle(
            "small",
            fontName="NotoSans",
            fontSize=9,
            leading=12,
            textColor=INK,
            spaceAfter=4,
        ),
        "center_small": ParagraphStyle(
            "center_small",
            fontName="NotoSans",
            fontSize=9,
            leading=12,
            textColor=MUTED,
            alignment=TA_CENTER,
        ),
        "qa_q": ParagraphStyle(
            "qa_q",
            fontName="NotoSans-Bold",
            fontSize=10.5,
            leading=13.6,
            textColor=NAVY,
            spaceBefore=4,
            spaceAfter=2,
        ),
    }
    styles["toc0"] = ParagraphStyle(
        "toc0",
        fontName="NotoSans-Bold",
        fontSize=11,
        leading=16,
        textColor=NAVY,
        leftIndent=0,
    )
    styles["toc1"] = ParagraphStyle(
        "toc1",
        fontName="NotoSans",
        fontSize=9,
        leading=12,
        textColor=INK,
        leftIndent=12,
    )
    return styles


def escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def markup(text: str) -> str:
    chunk = escape(text)
    chunk = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", chunk)
    chunk = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", chunk)
    return chunk


def math_image(latex: str) -> str:
    key = latex.strip()
    path, width, height, valign = MATH["png"][key]
    return (
        f'<img src="{path}" width="{width:.2f}" height="{height:.2f}" '
        f'valign="{valign:.2f}"/>'
    )


def inline(text: str) -> str:
    parts = re.split(r"(`[^`]+`)", text)
    out: list[str] = []
    for part in parts:
        if len(part) >= 2 and part.startswith("`") and part.endswith("`"):
            out.append(f'<font name="JetBrainsMono" size="8.5">{escape(part[1:-1])}</font>')
            continue
        cursor = 0
        for match in MATH_RE.finditer(part):
            out.append(markup(part[cursor:match.start()]))
            out.append(math_image(match.group(1)))
            cursor = match.end()
        out.append(markup(part[cursor:]))
    return "".join(out)


def collect_formulas(book: dict) -> set[str]:
    found: set[str] = set()

    def walk(value):
        if isinstance(value, str):
            for match in MATH_RE.finditer(value):
                found.add(match.group(1).strip())
            return
        if isinstance(value, tuple) and value and value[0] == "code":
            return
        if isinstance(value, tuple) and len(value) >= 2 and value[0] == "math":
            found.add(value[1].strip())
            return
        if isinstance(value, dict):
            for item in value.values():
                walk(item)
            return
        if isinstance(value, (list, tuple)):
            for item in value:
                walk(item)

    walk(book)
    return found


def install_math(rendered: dict[str, str]) -> None:
    directory = Path(tempfile.mkdtemp(prefix="biek-math-"))
    MATH["svg"] = rendered
    MATH["dir"] = directory
    pngs = {}
    for formula, svg in rendered.items():
        digest = hashlib.sha1(formula.encode()).hexdigest()[:12]
        png_path = directory / f"{digest}.png"
        cairosvg.svg2png(bytestring=svg.encode(), write_to=str(png_path), scale=4)
        pixels_w, pixels_h = ImageReader(str(png_path)).getSize()
        width = pixels_w / 4 * 0.75
        height = pixels_h / 4 * 0.75
        if height > 22:
            width *= 22 / height
            height = 22
        pngs[formula] = (str(png_path), width, height, -height * 0.22)
    MATH["png"] = pngs


class ScaledDrawing(Flowable):
    def __init__(self, drawing, max_width: float):
        super().__init__()
        scale = 1.0
        if drawing.width > max_width:
            scale = max_width / drawing.width
        elif drawing.width < max_width * 0.42:
            scale = min(1.25, max_width * 0.62 / drawing.width)
        self.drawing = drawing
        self.scale = scale
        self.width = drawing.width * scale
        self.height = drawing.height * scale

    def draw(self):
        self.canv.saveState()
        self.canv.scale(self.scale, self.scale)
        renderPDF.draw(self.drawing, self.canv, 0, 0)
        self.canv.restoreState()


def drawing_from_svg(svg: str) -> object:
    path = MATH["dir"] / f"fig-{hashlib.sha1(svg.encode()).hexdigest()[:12]}.svg"
    path.write_text(svg, encoding="utf-8")
    drawing = svg2rlg(str(path))
    if drawing is None:
        raise RuntimeError("Could not draw an SVG figure.")
    return drawing


def centered(flowable) -> Table:
    table = Table([[flowable]], colWidths=[CONTENT_W])
    table.setStyle(
        TableStyle(
            [
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    return table


class TocMark(Spacer):
    """Zero-height story mark that feeds the table of contents."""

    def __init__(self, level: int, text: str, key: str):
        super().__init__(0, 0)
        self.level = level
        self.toc_text = text
        self.key = key

    def draw(self):
        self.canv.bookmarkPage(self.key)
        self.canv.addOutlineEntry(self.toc_text, self.key, self.level, 0)


class LectureDoc(BaseDocTemplate):
    def __init__(self, filename: str, header_left: str, header_right: str, **kwargs):
        super().__init__(filename, **kwargs)
        self.header_left = header_left
        self.header_right = header_right

    def afterFlowable(self, flowable):
        if isinstance(flowable, TocMark):
            self.notify(
                "TOCEntry",
                (flowable.level, flowable.toc_text, self.page, flowable.key),
            )


def draw_header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, PAGE_H - 11 * mm, PAGE_W, 11 * mm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, PAGE_H - 12.2 * mm, PAGE_W, 1.2 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("NotoSans", 8)
    canvas.drawString(LEFT, PAGE_H - 7 * mm, doc.header_left)
    canvas.drawRightString(PAGE_W - RIGHT, PAGE_H - 7 * mm, doc.header_right)
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, 9 * mm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, 9 * mm, PAGE_W, 1.1 * mm, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("NotoSans", 8)
    canvas.drawString(LEFT, 3.4 * mm, "Classroom lecture notes  ·  not an official BIEK publication")
    canvas.setFont("NotoSans-Bold", 8)
    canvas.drawRightString(PAGE_W - RIGHT, 3.4 * mm, str(doc.page))
    canvas.restoreState()


def draw_cover(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY_DEEP)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, PAGE_H - 7 * mm, PAGE_W, 7 * mm, fill=1, stroke=0)
    canvas.rect(0, 0, PAGE_W, 7 * mm, fill=1, stroke=0)
    canvas.setFillColor(TEAL)
    canvas.rect(0, 32 * mm, PAGE_W, 56 * mm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(18 * mm, PAGE_H - 58 * mm, 28 * mm, 1.4 * mm, fill=1, stroke=0)

    canvas.setFillColor(GOLD)
    canvas.setFont("NotoSans-Bold", 11)
    canvas.drawString(18 * mm, PAGE_H - 48 * mm, "BOARD OF INTERMEDIATE EDUCATION KARACHI")
    canvas.setFillColor(white)
    canvas.setFont("NotoSans", 12)
    canvas.drawString(18 * mm, PAGE_H - 78 * mm, doc.cover["part"])
    canvas.setFont("NotoSans-Bold", 28)
    y = PAGE_H - 96 * mm
    for line in doc.cover["title_lines"]:
        canvas.drawString(18 * mm, y, line)
        y -= 12 * mm
    canvas.setFillColor(HexColor("#D6E4F0"))
    canvas.setFont("NotoSans", 12)
    canvas.drawString(18 * mm, y - 2 * mm, doc.cover["subtitle"])

    canvas.setFillColor(white)
    canvas.setFont("NotoSans-Bold", 13)
    canvas.drawString(18 * mm, 74 * mm, doc.cover["session"])
    canvas.setFont("NotoSans", 9.5)
    canvas.setFillColor(HexColor("#E5EEF6"))
    for i, line in enumerate(doc.cover["foot_lines"]):
        canvas.drawString(18 * mm, 64 * mm - i * 5.4 * mm, line)
    canvas.restoreState()


def paragraphs(text: str, style: ParagraphStyle) -> list:
    chunks = [c.strip() for c in text.strip().split("\n\n") if c.strip()]
    return [Paragraph(inline(c.replace("\n", " ")), style) for c in chunks]


def bullet_list(items: list[str], styles, numbered: bool = False) -> ListFlowable:
    flowables = [
        ListItem(Paragraph(inline(item), styles["bullet"]), leftIndent=8)
        for item in items
    ]
    return ListFlowable(
        flowables,
        bulletType="1" if numbered else "bullet",
        start="1" if numbered else "•",
        leftIndent=14,
        bulletFontName="NotoSans-Bold",
        bulletFontSize=9,
        bulletColor=TEAL if not numbered else NAVY,
        spaceBefore=1,
        spaceAfter=6,
    )


def make_table(spec: dict, styles) -> list:
    headers = spec["headers"]
    rows = spec["rows"]
    center = spec.get("center", False)
    cell_style = styles["td_center"] if center else styles["td"]
    head = [Paragraph(inline(str(h)), styles["th"]) for h in headers]
    body = [[Paragraph(inline(str(c)), cell_style) for c in row] for row in rows]
    fractions = spec.get("widths")
    if fractions:
        widths = [CONTENT_W * f for f in fractions]
    else:
        widths = [CONTENT_W / len(headers)] * len(headers)
    table = Table([head, *body], colWidths=widths, repeatRows=1)
    commands = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, ROW]),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
        ("ALIGN", (0, 0), (-1, 0), "LEFT"),
    ]
    table.setStyle(TableStyle(commands))
    flow = [table]
    if spec.get("caption"):
        flow.append(Paragraph(inline(spec["caption"]), styles["caption"]))
    else:
        flow.append(Spacer(1, 6))
    return flow


def make_code(spec: dict, styles) -> Table:
    text = spec["text"].rstrip() + "\n"
    bits = []
    if spec.get("lang"):
        bits.append(Paragraph(escape(spec["lang"]), styles["code_label"]))
    bits.append(Preformatted(text, styles["code"]))
    table = Table([[bits]], colWidths=[CONTENT_W])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), CODE_BG),
                ("BOX", (0, 0), (-1, -1), 0.6, HexColor("#E2D8C4")),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return table


def make_callout(kind: str, title: str | None, text: str, styles) -> Table:
    border, bg, default_title = CALLOUT[kind]
    heading = title or default_title
    inner = [Paragraph(escape(heading).upper(), styles["callout_title"])]
    inner.extend(paragraphs(text, styles["callout_body"]))
    table = Table([[inner]], colWidths=[CONTENT_W])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), bg),
                ("BOX", (0, 0), (-1, -1), 0.4, border),
                ("LINEBEFORE", (0, 0), (0, -1), 3.5, border),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return table


def blocks_to_flowables(blocks: list, styles, key_prefix: str) -> list:
    flow: list = []
    h2_count = 0
    for block in blocks:
        kind = block[0]
        if kind == "h2":
            h2_count += 1
            text = block[1]
            key = f"{key_prefix}-s{h2_count}"
            flow.append(CondPageBreak(28 * mm))
            flow.append(TocMark(1, text, key))
            flow.append(Paragraph(inline(text), styles["h2"]))
            flow.append(
                HRFlowable(width="100%", thickness=0.6, color=GOLD, spaceBefore=0, spaceAfter=4)
            )
        elif kind == "h3":
            flow.append(Paragraph(inline(block[1]), styles["h3"]))
        elif kind == "p":
            flow.extend(paragraphs(block[1], styles["body"]))
        elif kind == "bullets":
            flow.append(bullet_list(block[1], styles, numbered=False))
        elif kind == "numbers":
            flow.append(bullet_list(block[1], styles, numbered=True))
        elif kind == "table":
            flow.extend(make_table(block[1], styles))
        elif kind == "code":
            flow.append(Spacer(1, 2))
            flow.append(make_code(block[1], styles))
            flow.append(Spacer(1, 6))
        elif kind == "callout":
            spec = block[1]
            flow.append(Spacer(1, 2))
            flow.append(make_callout(spec["kind"], spec.get("title"), spec["text"], styles))
            flow.append(Spacer(1, 6))
        elif kind == "math":
            svg = MATH["svg"][block[1].strip()]
            flow.append(Spacer(1, 3))
            flow.append(centered(ScaledDrawing(drawing_from_svg(svg), CONTENT_W)))
            flow.append(Spacer(1, 4))
        elif kind == "figure":
            from diagrams import svg_for

            svg = svg_for(block[1])
            flow.append(Spacer(1, 3))
            flow.append(centered(ScaledDrawing(drawing_from_svg(svg), CONTENT_W)))
            if len(block) > 2 and block[2]:
                flow.append(Paragraph(inline(block[2]), styles["caption"]))
            else:
                flow.append(Spacer(1, 6))
        else:
            raise ValueError(f"Unknown block {kind}")
    return flow


def lecture_story(lecture: dict, styles) -> list:
    key = lecture["id"]
    story: list = [PageBreak(), TocMark(0, f"Lecture {lecture['number']}.  {lecture['title']}", key)]
    story.append(Paragraph(escape(lecture["kicker"]), styles["kicker"]))
    story.append(Paragraph(escape(f"Lecture {lecture['number']}"), styles["kicker"]))
    story.append(Paragraph(escape(lecture["title"]), styles["h1"]))
    story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceBefore=1, spaceAfter=6))
    story.append(Paragraph(f"<b>Textbook unit.</b> {escape(lecture['unit'])}", styles["small"]))
    story.append(Paragraph(f"<b>Curriculum domain.</b> {escape(lecture['domain'])}", styles["small"]))
    story.append(Paragraph(f"<b>Class time.</b> {escape(lecture['periods'])}", styles["small"]))
    story.extend(paragraphs(lecture["intro"], styles["body"]))
    story.append(Paragraph("Learning outcomes", styles["h3"]))
    story.append(bullet_list(lecture["outcomes"], styles))
    story.extend(blocks_to_flowables(lecture["blocks"], styles, key))

    story.append(CondPageBreak(40 * mm))
    story.append(TocMark(1, f"{lecture['title']}: key terms", f"{key}-terms"))
    story.append(Paragraph("Key terms", styles["h2"]))
    story.append(HRFlowable(width="100%", thickness=0.6, color=GOLD, spaceBefore=0, spaceAfter=4))
    term_rows = [[term, meaning] for term, meaning in lecture["terms"]]
    story.extend(
        make_table(
            {
                "headers": ["Term", "Meaning in this lecture"],
                "rows": term_rows,
                "widths": [0.28, 0.72],
            },
            styles,
        )
    )

    story.append(Paragraph("Check your understanding", styles["h2"]))
    story.append(HRFlowable(width="100%", thickness=0.6, color=GOLD, spaceBefore=0, spaceAfter=4))
    story.append(
        paragraphs(
            "Attempt each question before you read the model answer. In the examination, a short question usually earns marks for a definition plus one precise point or a tiny example.",
            styles["body"],
        )[0]
    )
    for item in lecture["checks"]:
        story.append(Paragraph(inline(item["q"]), styles["qa_q"]))
        story.append(make_callout("answer", "Model answer", item["a"], styles))
        story.append(Spacer(1, 4))

    story.append(CondPageBreak(50 * mm))
    story.append(Paragraph("Board-style practice", styles["h2"]))
    story.append(HRFlowable(width="100%", thickness=0.6, color=GOLD, spaceBefore=0, spaceAfter=4))
    story.append(Paragraph("Multiple choice", styles["h3"]))
    story.append(
        paragraphs(
            "Each item is worth one mark. Cross out two options that cannot be right before you choose.",
            styles["body"],
        )[0]
    )
    letters = "ABCD"
    for i, mcq in enumerate(lecture["mcqs"], start=1):
        story.append(Paragraph(inline(f"**{i}.** {mcq['q']}"), styles["body"]))
        opts = [f"{letters[n]}. {opt}" for n, opt in enumerate(mcq["options"])]
        story.append(bullet_list(opts, styles))
    story.append(Paragraph("Answer key with reasons", styles["h3"]))
    key_rows = []
    for i, mcq in enumerate(lecture["mcqs"], start=1):
        key_rows.append([str(i), mcq["answer"], mcq["why"]])
    story.extend(
        make_table(
            {"headers": ["Q", "Answer", "Why"], "rows": key_rows, "widths": [0.08, 0.12, 0.80]},
            styles,
        )
    )

    story.append(Paragraph("Short questions", styles["h3"]))
    for i, item in enumerate(lecture["shorts"], start=1):
        story.append(Paragraph(inline(f"**S{i}.** {item['q']}"), styles["qa_q"]))
        story.append(make_callout("answer", "Model answer", item["a"], styles))
        story.append(Spacer(1, 3))

    story.append(Paragraph("Long questions", styles["h3"]))
    for i, item in enumerate(lecture["longs"], start=1):
        story.append(Paragraph(inline(f"**L{i}.** ({item['marks']} marks) {item['q']}"), styles["qa_q"]))
        story.append(make_callout("answer", "Model answer", item["a"], styles))
        story.append(Spacer(1, 3))

    story.append(CondPageBreak(45 * mm))
    story.append(Paragraph("Practical work", styles["h2"]))
    story.append(HRFlowable(width="100%", thickness=0.6, color=GOLD, spaceBefore=0, spaceAfter=4))
    story.append(
        paragraphs(
            "The practical paper is 25 marks. Keep a journal: aim, steps, the program or diagram, the output, and one sentence on what went wrong the first time.",
            styles["body"],
        )[0]
    )
    for lab in lecture["labs"]:
        story.append(Paragraph(inline(lab["title"]), styles["h3"]))
        story.append(bullet_list(lab["steps"], styles, numbered=True))
        if lab.get("success"):
            story.append(make_callout("lab", "What success looks like", lab["success"], styles))
            story.append(Spacer(1, 4))

    story.append(Paragraph("Copy this summary", styles["h2"]))
    story.append(HRFlowable(width="100%", thickness=0.6, color=GOLD, spaceBefore=0, spaceAfter=4))
    story.append(bullet_list(lecture["summary"], styles))
    return story


def build_pdf(book: dict, destination: Path, math_ready: bool = False) -> None:
    if not math_ready:
        from mathjax_svg import render_formulas

        install_math(render_formulas(sorted(collect_formulas(book))))
    if MATH["dir"] is None:
        MATH["dir"] = Path(tempfile.mkdtemp(prefix="biek-figures-"))
    register_fonts()
    styles = make_styles()
    destination.parent.mkdir(parents=True, exist_ok=True)
    doc = LectureDoc(
        str(destination),
        header_left=book["header_left"],
        header_right=book["header_right"],
        pagesize=A4,
        title=book["pdf_title"],
        author="BIEK Computer Science lecture notes",
        subject=book["pdf_subject"],
    )
    doc.cover = book["cover"]
    frame = Frame(
        LEFT,
        14 * mm,
        CONTENT_W,
        PAGE_H - 14 * mm - 16 * mm,
        id="body",
        showBoundary=0,
    )
    cover_frame = Frame(LEFT, 14 * mm, CONTENT_W, PAGE_H - 30 * mm, id="cover", showBoundary=0)
    doc.addPageTemplates(
        [
            PageTemplate(id="cover", frames=[cover_frame], onPage=draw_cover),
            PageTemplate(id="body", frames=[frame], onPage=draw_header_footer),
        ]
    )
    toc = TableOfContents()
    toc.levelStyles = [styles["toc0"], styles["toc1"]]
    toc.dotsMinLevel = 0
    story = [NextPageTemplate("body"), PageBreak()]
    story.append(Paragraph("Contents", styles["toc_title"]))
    story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceBefore=0, spaceAfter=8))
    story.append(toc)
    story.append(PageBreak())
    story.append(TocMark(0, "How to use these lectures", "front-how"))
    story.append(Paragraph("How to use these lectures", styles["h1"]))
    story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceBefore=1, spaceAfter=6))
    story.extend(blocks_to_flowables(book["front"], styles, "front"))
    for lecture in book["lectures"]:
        story.extend(lecture_story(lecture, styles))
    if book.get("closing"):
        story.append(PageBreak())
        story.append(TocMark(0, book["closing_title"], "closing"))
        story.append(Paragraph(book["closing_title"], styles["h1"]))
        story.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceBefore=1, spaceAfter=6))
        story.extend(blocks_to_flowables(book["closing"], styles, "close"))
    doc.multiBuild(story)


if __name__ == "__main__":
    raise SystemExit("Use build_lectures.py")
