"""Simple lecture diagrams drawn with reportlab."""

import math

from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import Flowable

NAVY = colors.HexColor("#0C3C60")
TEAL = colors.HexColor("#1F6F8B")
GOLD = colors.HexColor("#A67C2D")
INK = colors.HexColor("#1C2830")
PALE = colors.HexColor("#E7F1F6")
CREAM = colors.HexColor("#FBF6EA")
GREEN = colors.HexColor("#1B7A4E")


def _box(c, x, y, w, h, text, fill=PALE, size=8):
    c.setStrokeColor(NAVY)
    c.setFillColor(fill)
    c.setLineWidth(1)
    c.roundRect(x, y, w, h, 3, fill=1, stroke=1)
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", size)
    lines = text.split("\n")
    total = (len(lines) - 1) * (size + 1)
    base = y + h / 2 - size / 3 + total / 2
    for i, line in enumerate(lines):
        c.drawCentredString(x + w / 2, base - i * (size + 1), line)


def _arrow(c, x1, y1, x2, y2):
    c.setStrokeColor(TEAL)
    c.setFillColor(TEAL)
    c.setLineWidth(1.2)
    c.line(x1, y1, x2, y2)
    angle = math.atan2(y2 - y1, x2 - x1)
    size = 6
    p1 = (x2 - size * math.cos(angle - 0.4), y2 - size * math.sin(angle - 0.4))
    p2 = (x2 - size * math.cos(angle + 0.4), y2 - size * math.sin(angle + 0.4))
    path = c.beginPath()
    path.moveTo(x2, y2)
    path.lineTo(*p1)
    path.lineTo(*p2)
    path.close()
    c.drawPath(path, fill=1, stroke=0)


def _label(c, x, y, text, size=7):
    c.setFillColor(INK)
    c.setFont("Helvetica", size)
    c.drawCentredString(x, y, text)


class Diagram(Flowable):
    def __init__(self, kind, height=52 * mm):
        super().__init__()
        self.kind = kind
        self._height = height

    def wrap(self, aw, ah):
        self.width = aw
        self.height = self._height
        return aw, self.height

    def draw(self):
        getattr(self, f"draw_{self.kind}")()

    def draw_computer(self):
        c = self.canv
        w = self.width
        h = self.height
        _box(c, 8, h * 0.38, w * 0.16, h * 0.28, "Input\nunit")
        _box(c, w * 0.28, h * 0.22, w * 0.28, h * 0.62, "")
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(w * 0.42, h * 0.72, "CPU")
        _box(c, w * 0.31, h * 0.48, w * 0.10, h * 0.16, "ALU", CREAM, 7)
        _box(c, w * 0.43, h * 0.48, w * 0.10, h * 0.16, "CU", CREAM, 7)
        _box(c, w * 0.34, h * 0.28, w * 0.16, h * 0.14, "Registers", PALE, 7)
        _box(c, w * 0.62, h * 0.38, w * 0.16, h * 0.28, "Memory")
        _box(c, w * 0.82, h * 0.38, w * 0.16, h * 0.28, "Output\nunit")
        _arrow(c, w * 0.16 + 8, h * 0.52, w * 0.28, h * 0.52)
        _arrow(c, w * 0.56, h * 0.58, w * 0.62, h * 0.58)
        _arrow(c, w * 0.62, h * 0.46, w * 0.56, h * 0.46)
        _arrow(c, w * 0.78, h * 0.52, w * 0.82, h * 0.52)
        _label(c, w * 0.50, 8, "Data moves in. The CPU processes it with memory. Results go out.")

    def draw_memory(self):
        c = self.canv
        w = self.width
        h = self.height
        rows = [
            "Registers",
            "Cache",
            "Main memory",
            "Secondary storage",
        ]
        top = h - 8
        row_h = 22
        gap = 6
        for i, text in enumerate(rows):
            inset = (3 - i) * w * 0.08
            y = top - (i + 1) * row_h - i * gap
            _box(c, inset, y, w - 2 * inset - 4, row_h, text, PALE if i % 2 == 0 else CREAM, 8)

    def draw_states(self):
        c = self.canv
        w = self.width
        h = self.height
        boxes = [
            (w * 0.05, h * 0.55, "New"),
            (w * 0.28, h * 0.55, "Ready"),
            (w * 0.52, h * 0.55, "Running"),
            (w * 0.74, h * 0.55, "Terminated"),
            (w * 0.52, h * 0.16, "Waiting"),
        ]
        for x, y, name in boxes:
            _box(c, x, y, w * 0.16, h * 0.22, name)
        _arrow(c, w * 0.21, h * 0.66, w * 0.28, h * 0.66)
        _arrow(c, w * 0.44, h * 0.66, w * 0.52, h * 0.66)
        _arrow(c, w * 0.68, h * 0.66, w * 0.74, h * 0.66)
        _arrow(c, w * 0.60, h * 0.55, w * 0.60, h * 0.38)
        _arrow(c, w * 0.52, h * 0.27, w * 0.36, h * 0.55)
        _label(c, w * 0.24, h * 0.80, "admit")
        _label(c, w * 0.48, h * 0.80, "dispatch")
        _label(c, w * 0.71, h * 0.80, "exit")
        _label(c, w * 0.70, h * 0.42, "wait")
        _label(c, w * 0.40, h * 0.36, "I/O done, back to Ready")

    def draw_osi(self):
        c = self.canv
        w = self.width
        h = self.height
        osi = [
            "7  Application",
            "6  Presentation",
            "5  Session",
            "4  Transport",
            "3  Network",
            "2  Data link",
            "1  Physical",
        ]
        tcp = [
            "Application",
            "Application",
            "Application",
            "Transport",
            "Internet",
            "Network access",
            "Network access",
        ]
        row_h = (h - 28) / 7
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(8, h - 12, "OSI model")
        c.drawString(w * 0.55, h - 12, "TCP/IP model")
        for i, (left, right) in enumerate(zip(osi, tcp)):
            y = h - 22 - (i + 1) * row_h
            fill = PALE if i % 2 == 0 else colors.white
            _box(c, 8, y, w * 0.42, row_h - 2, left, fill, 7)
            _box(c, w * 0.55, y, w * 0.40, row_h - 2, right, CREAM if i in (0, 3, 4) else fill, 7)

    def draw_topologies(self):
        c = self.canv
        w = self.width
        h = self.height
        # Bus
        c.setStrokeColor(NAVY)
        c.setLineWidth(2)
        c.line(16, h * 0.28, w * 0.28, h * 0.28)
        for i, x in enumerate((28, w * 0.12, w * 0.20)):
            c.line(x, h * 0.28, x, h * 0.48)
            _box(c, x - 16, h * 0.48, 32, 16, f"N{i+1}", PALE, 7)
        _label(c, w * 0.15, 10, "Bus")
        # Star
        cx, cy = w * 0.50, h * 0.42
        _box(c, cx - 18, cy - 10, 36, 18, "Switch", CREAM, 7)
        for angle in (30, 90, 150, 210, 270, 330):
            rad = math.radians(angle)
            x = cx + 48 * math.cos(rad)
            y = cy + 28 * math.sin(rad)
            c.setStrokeColor(TEAL)
            c.setLineWidth(1)
            c.line(cx, cy, x, y)
            c.setFillColor(NAVY)
            c.circle(x, y, 4, fill=1, stroke=0)
        _label(c, w * 0.50, 10, "Star")
        # Ring
        rcx, rcy, r = w * 0.82, h * 0.46, 26
        c.setStrokeColor(TEAL)
        c.circle(rcx, rcy, r, fill=0, stroke=1)
        for i in range(4):
            rad = math.radians(i * 90 - 90)
            x = rcx + r * math.cos(rad)
            y = rcy + r * math.sin(rad)
            c.setFillColor(NAVY)
            c.circle(x, y, 5, fill=1, stroke=0)
        _label(c, w * 0.82, 10, "Ring")

    def draw_sdlc(self):
        c = self.canv
        w = self.width
        h = self.height
        steps = [
            "1 Plan and\nrequirements",
            "2 Design",
            "3 Build",
            "4 Test",
            "5 Deploy and\nmaintain",
        ]
        box_w = w * 0.16
        gap = (w - 5 * box_w) / 6
        for i, step in enumerate(steps):
            x = gap + i * (box_w + gap)
            _box(c, x, h * 0.32, box_w, h * 0.40, step, PALE if i % 2 == 0 else CREAM, 7)
            if i < 4:
                _arrow(c, x + box_w, h * 0.52, x + box_w + gap - 2, h * 0.52)
        _label(c, w / 2, 8, "Maintenance feeds new requirements back into planning.")

    def draw_pointer(self):
        c = self.canv
        w = self.width
        h = self.height
        _box(c, w * 0.08, h * 0.28, w * 0.28, h * 0.40, "p\nholds an address", CREAM, 8)
        _box(c, w * 0.58, h * 0.28, w * 0.28, h * 0.40, "marks\nvalue 25", PALE, 8)
        _arrow(c, w * 0.36, h * 0.48, w * 0.58, h * 0.48)
        _label(c, w / 2, h * 0.78, "p = &marks     and     *p  reaches 25")
        _label(c, w / 2, 8, "The pointer stores where the variable lives, not a second copy of the value.")

    def draw_levels(self):
        c = self.canv
        w = self.width
        h = self.height
        rows = [
            ("External level", "What one user or program is allowed to see"),
            ("Conceptual level", "The whole database: tables, keys, relationships"),
            ("Physical level", "Files, indexes and storage on disk"),
        ]
        for i, (title, detail) in enumerate(rows):
            y = h - 18 - i * (h * 0.28)
            _box(c, 8, y - h * 0.18, w - 16, h * 0.20, f"{title}\n{detail}", PALE if i != 1 else CREAM, 8)

    def draw_cellular(self):
        c = self.canv
        w = self.width
        h = self.height
        centres = [(w * 0.22, h * 0.48), (w * 0.50, h * 0.48), (w * 0.78, h * 0.48)]
        c.setStrokeColor(TEAL)
        c.setLineWidth(1)
        for x, y in centres:
            c.setFillColor(colors.Color(0.12, 0.44, 0.55, alpha=0.12))
            c.circle(x, y, 38, fill=1, stroke=1)
            _box(c, x - 22, y - 8, 44, 16, "BTS", CREAM, 7)
        _box(c, w / 2 - 50, 12, 100, 18, "Mobile switching centre", PALE, 7)
        _arrow(c, w * 0.50, h * 0.48 - 38, w * 0.50, 30)
        _label(c, w * 0.22, h * 0.82, "Cell")
        _label(c, w * 0.50, h * 0.82, "Cell")
        _label(c, w * 0.78, h * 0.82, "Cell")
