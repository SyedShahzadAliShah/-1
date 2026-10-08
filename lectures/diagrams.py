"""Small teaching diagrams drawn with reportlab."""

from reportlab.lib.colors import Color, white
from reportlab.platypus import Flowable

NAVY = Color(0.067, 0.165, 0.310)
TEAL = Color(0.055, 0.380, 0.455)
GOLD = Color(0.722, 0.580, 0.275)
INK = Color(0.110, 0.145, 0.180)
PALE = Color(0.925, 0.953, 0.957)
LINE = Color(0.35, 0.42, 0.48)


class Diagram(Flowable):
    def __init__(self, width, height, painter, caption=""):
        super().__init__()
        self.diagram_width = width
        self.diagram_height = height
        self.painter = painter
        self.caption = caption

    def wrap(self, aw, ah):
        self.diagram_width = min(self.diagram_width, aw)
        return self.diagram_width, self.diagram_height

    def draw(self):
        self.canv.saveState()
        self.painter(self.canv, self.diagram_width, self.diagram_height)
        self.canv.restoreState()


def _box(c, x, y, w, h, text, fill=PALE, lines=None):
    c.setStrokeColor(NAVY)
    c.setFillColor(fill)
    c.setLineWidth(1)
    c.roundRect(x, y, w, h, 4, fill=1, stroke=1)
    c.setFillColor(INK)
    c.setFont("Sans", 8)
    parts = lines if lines is not None else text.split("\n")
    total = len(parts) * 10
    ty = y + h / 2 + total / 2 - 8
    for part in parts:
        c.drawCentredString(x + w / 2, ty, part)
        ty -= 10


def _arrow(c, x1, y1, x2, y2):
    c.setStrokeColor(TEAL)
    c.setFillColor(TEAL)
    c.setLineWidth(1.2)
    c.line(x1, y1, x2, y2)
    import math

    ang = math.atan2(y2 - y1, x2 - x1)
    size = 6
    c.saveState()
    c.translate(x2, y2)
    c.rotate(ang * 180 / math.pi)
    p = c.beginPath()
    p.moveTo(0, 0)
    p.lineTo(-size, 3)
    p.lineTo(-size, -3)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.restoreState()


def paint_gates(c, w, h):
    labels = ["NOT", "AND", "OR", "NAND", "XOR"]
    gap = w / 5
    for i, name in enumerate(labels):
        cx = gap * i + gap / 2
        cy = h / 2 + 6
        c.setStrokeColor(NAVY)
        c.setFillColor(white)
        c.setLineWidth(1.3)
        if name == "NOT":
            p = c.beginPath()
            p.moveTo(cx - 22, cy - 16)
            p.lineTo(cx - 22, cy + 16)
            p.lineTo(cx + 10, cy)
            p.close()
            c.drawPath(p, fill=1, stroke=1)
            c.circle(cx + 15, cy, 4, fill=0, stroke=1)
            c.line(cx - 36, cy, cx - 22, cy)
            c.line(cx + 19, cy, cx + 34, cy)
        elif name in ("AND", "NAND"):
            c.line(cx - 24, cy - 16, cx - 24, cy + 16)
            c.line(cx - 24, cy + 16, cx, cy + 16)
            c.line(cx - 24, cy - 16, cx, cy - 16)
            c.arc(cx - 16, cy - 16, cx + 16, cy + 16, -90, 180)
            c.line(cx - 40, cy + 8, cx - 24, cy + 8)
            c.line(cx - 40, cy - 8, cx - 24, cy - 8)
            if name == "NAND":
                c.circle(cx + 20, cy, 4, fill=0, stroke=1)
                c.line(cx + 24, cy, cx + 38, cy)
            else:
                c.line(cx + 16, cy, cx + 34, cy)
        else:
            # OR / XOR curved inputs, simplified as a pointed shield
            p = c.beginPath()
            p.moveTo(cx - 26, cy - 16)
            p.curveTo(cx - 8, cy - 16, cx + 8, cy - 8, cx + 18, cy)
            p.curveTo(cx + 8, cy + 8, cx - 8, cy + 16, cx - 26, cy + 16)
            p.curveTo(cx - 14, cy + 8, cx - 14, cy - 8, cx - 26, cy - 16)
            c.drawPath(p, fill=1, stroke=1)
            if name == "XOR":
                p2 = c.beginPath()
                p2.moveTo(cx - 32, cy - 16)
                p2.curveTo(cx - 20, cy - 6, cx - 20, cy + 6, cx - 32, cy + 16)
                c.drawPath(p2, fill=0, stroke=1)
            c.line(cx - 46, cy + 8, cx - 28, cy + 8)
            c.line(cx - 46, cy - 8, cx - 28, cy - 8)
            c.line(cx + 18, cy, cx + 34, cy)
        c.setFillColor(NAVY)
        c.setFont("Sans-Bold", 8)
        c.drawCentredString(cx, 12, name)
    c.setFillColor(INK)
    c.setFont("Sans", 8)
    c.drawString(8, h - 14, "Each symbol reads inputs on the left and writes one output on the right.")


def paint_circuit(c, w, h):
    """F = A·B' + C'"""
    c.setFont("Sans", 8)
    c.setFillColor(INK)
    c.drawString(8, h - 14, "Logic circuit for  F = A·B' + C'")
    # inputs
    ys = {"A": h * 0.72, "B": h * 0.48, "C": h * 0.24}
    for name, y in ys.items():
        c.setFillColor(NAVY)
        c.circle(28, y, 8, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Sans-Bold", 8)
        c.drawCentredString(28, y - 3, name)
    # NOT on B
    c.setStrokeColor(NAVY)
    c.setFillColor(white)
    c.setLineWidth(1.2)
    p = c.beginPath()
    p.moveTo(70, ys["B"] - 12)
    p.lineTo(70, ys["B"] + 12)
    p.lineTo(96, ys["B"])
    p.close()
    c.setFillColor(PALE)
    c.drawPath(p, fill=1, stroke=1)
    c.circle(102, ys["B"], 3.5, fill=0, stroke=1)
    c.line(36, ys["B"], 70, ys["B"])
    # NOT on C
    p = c.beginPath()
    p.moveTo(70, ys["C"] - 12)
    p.lineTo(70, ys["C"] + 12)
    p.lineTo(96, ys["C"])
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    c.circle(102, ys["C"], 3.5, fill=0, stroke=1)
    c.line(36, ys["C"], 70, ys["C"])
    # AND gate
    and_y = (ys["A"] + ys["B"]) / 2
    c.line(150, and_y - 22, 150, and_y + 22)
    c.line(150, and_y + 22, 172, and_y + 22)
    c.line(150, and_y - 22, 172, and_y - 22)
    c.arc(156, and_y - 22, 188, and_y + 22, -90, 180)
    c.line(36, ys["A"], 150, ys["A"])
    c.line(106, ys["B"], 150, ys["B"])
    # wires need to meet AND inputs - draw short verticals if needed
    # OR gate
    or_x = 280
    or_y = (and_y + ys["C"]) / 2
    p = c.beginPath()
    p.moveTo(or_x, or_y - 20)
    p.curveTo(or_x + 16, or_y - 20, or_x + 30, or_y - 8, or_x + 42, or_y)
    p.curveTo(or_x + 30, or_y + 8, or_x + 16, or_y + 20, or_x, or_y + 20)
    p.curveTo(or_x + 12, or_y + 8, or_x + 12, or_y - 8, or_x, or_y - 20)
    c.drawPath(p, fill=1, stroke=1)
    c.line(188, and_y, or_x + 8, and_y)
    c.line(or_x + 8, and_y, or_x + 8, or_y + 8)
    c.line(or_x + 8, or_y + 8, or_x + 14, or_y + 8)
    c.line(106, ys["C"], or_x + 8, ys["C"])
    c.line(or_x + 8, ys["C"], or_x + 8, or_y - 8)
    c.line(or_x + 8, or_y - 8, or_x + 14, or_y - 8)
    c.line(or_x + 42, or_y, w - 36, or_y)
    c.setFillColor(TEAL)
    c.roundRect(w - 34, or_y - 10, 26, 20, 3, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Sans-Bold", 9)
    c.drawCentredString(w - 21, or_y - 3, "F")


def paint_kmap(c, w, h):
    entries = [["1", "0", "0", "1"], ["1", "1", "0", "1"]]
    cell = 32
    left = 72
    # top is the top edge of the first cell row. Keep headings below the title.
    top = h - 36 - cell
    c.setFillColor(INK)
    c.setFont("Sans", 8)
    c.drawString(8, h - 14, "K-map for F = m(0, 2, 4, 5, 6). Column order of BC is 00, 01, 11, 10.")
    headers = ["00", "01", "11", "10"]
    c.setFont("Sans-Bold", 8)
    c.drawCentredString(left - 14, top + cell + 8, "A")
    for i, lab in enumerate(headers):
        c.drawCentredString(left + i * cell + cell / 2, top + cell + 8, lab)
    for r, row_lab in enumerate(["0", "1"]):
        c.setFillColor(INK)
        c.setFont("Sans-Bold", 8)
        c.drawCentredString(left - 14, top - r * cell + cell / 2 - 3, row_lab)
        for col, val in enumerate(entries[r]):
            x = left + col * cell
            y = top - r * cell
            c.setStrokeColor(NAVY)
            c.setFillColor(Color(0.86, 0.93, 0.86) if val == "1" else white)
            c.rect(x, y, cell, cell, fill=1, stroke=1)
            c.setFillColor(INK)
            c.setFont("Sans-Bold", 11)
            c.drawCentredString(x + cell / 2, y + cell / 2 - 4, val)
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.6)
    c.rect(left + 1.5, top - cell + 1.5, cell * 2 - 3, cell - 3, fill=0, stroke=1)
    c.setFillColor(INK)
    c.setFont("Sans", 8)
    note_x = left + 4 * cell + 16
    c.drawString(note_x, top + 18, "Gold pair = AB'")
    c.drawString(note_x, top + 4, "Cells with C = 0")
    c.drawString(note_x, top - 10, "are one group: C'")
    c.setFont("Sans-Bold", 10)
    c.drawString(note_x, top - 32, "F = C' + AB'")


def paint_topologies(c, w, h):
    def node(x, y):
        c.setFillColor(TEAL)
        c.circle(x, y, 5, fill=1, stroke=0)

    def label(text, x, y):
        c.setFillColor(NAVY)
        c.setFont("Sans-Bold", 8)
        c.drawCentredString(x, y, text)

    # Bus
    x0 = 20
    c.setStrokeColor(NAVY)
    c.setLineWidth(2)
    c.line(x0 + 10, 28, x0 + 100, 28)
    c.setLineWidth(1)
    for i, px in enumerate((30, 55, 80, 105)):
        c.line(x0 + px, 28, x0 + px, 48)
        node(x0 + px, 54)
    label("Bus", x0 + 60, 74)
    # Star
    x0 = 160
    cx, cy = x0 + 50, 46
    for ang in (30, 90, 150, 210, 270, 330):
        import math

        px = cx + 28 * math.cos(math.radians(ang))
        py = cy + 22 * math.sin(math.radians(ang))
        c.setStrokeColor(NAVY)
        c.line(cx, cy, px, py)
        node(px, py)
    c.setFillColor(GOLD)
    c.circle(cx, cy, 6, fill=1, stroke=0)
    label("Star", x0 + 50, 78)
    # Ring
    x0 = 300
    import math

    pts = []
    for i in range(6):
        ang = math.radians(-90 + i * 60)
        pts.append((x0 + 48 + 26 * math.cos(ang), 46 + 22 * math.sin(ang)))
    c.setStrokeColor(NAVY)
    for i in range(6):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % 6]
        c.line(x1, y1, x2, y2)
    for x, y in pts:
        node(x, y)
    label("Ring", x0 + 48, 78)
    # Mesh (4 nodes)
    x0 = 410
    pts = [(x0 + 20, 30), (x0 + 70, 30), (x0 + 20, 62), (x0 + 70, 62)]
    c.setStrokeColor(NAVY)
    for i in range(4):
        for j in range(i + 1, 4):
            c.line(pts[i][0], pts[i][1], pts[j][0], pts[j][1])
    for x, y in pts:
        node(x, y)
    label("Mesh", x0 + 45, 78)


def paint_osi(c, w, h):
    layers = [
        ("7  Application", "HTTP, DNS, SMTP"),
        ("6  Presentation", "Formatting, encryption"),
        ("5  Session", "Dialog control"),
        ("4  Transport", "TCP, UDP"),
        ("3  Network", "IP, routing"),
        ("2  Data link", "Frames, MAC"),
        ("1  Physical", "Bits on the medium"),
    ]
    box_h = (h - 28) / 7
    for i, (name, job) in enumerate(layers):
        y = 10 + (6 - i) * box_h
        c.setFillColor(TEAL if i % 2 == 0 else NAVY)
        c.roundRect(16, y, w * 0.46, box_h - 3, 3, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Sans-Bold", 8.5)
        c.drawString(26, y + box_h / 2 - 3, name)
        c.setFillColor(INK)
        c.setFont("Sans", 8.5)
        c.drawString(w * 0.52, y + box_h / 2 - 3, job)
    c.setFont("Sans", 8)
    c.setFillColor(MUTED if False else INK)


def paint_sdlc(c, w, h):
    steps = ["Plan", "Analyse", "Design", "Code", "Test", "Deploy", "Maintain"]
    bw = (w - 30) / len(steps)
    for i, name in enumerate(steps):
        x = 12 + i * bw
        c.setFillColor(NAVY if i % 2 == 0 else TEAL)
        c.roundRect(x, 36, bw - 8, 28, 4, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Sans-Bold", 7.5)
        c.drawCentredString(x + (bw - 8) / 2, 46, name)
        if i < len(steps) - 1:
            _arrow(c, x + bw - 8, 50, x + bw - 1, 50)
    c.setStrokeColor(GOLD)
    c.setLineWidth(1)
    c.line(w - 28, 36, 24, 22)
    c.setFillColor(INK)
    c.setFont("Sans", 8)
    c.drawString(28, 10, "Waterfall moves one way. Agile repeats design, code, and test in short cycles.")


def paint_bst(c, w, h):
    import math

    nodes = {
        "50": (w / 2, h - 28),
        "30": (w / 2 - 110, h - 78),
        "70": (w / 2 + 110, h - 78),
        "20": (w / 2 - 165, h - 128),
        "40": (w / 2 - 55, h - 128),
        "60": (w / 2 + 55, h - 128),
        "80": (w / 2 + 165, h - 128),
    }
    edges = [("50", "30"), ("50", "70"), ("30", "20"), ("30", "40"), ("70", "60"), ("70", "80")]
    c.setStrokeColor(NAVY)
    c.setLineWidth(1.2)
    for a, b in edges:
        c.line(nodes[a][0], nodes[a][1], nodes[b][0], nodes[b][1])
    for name, (x, y) in nodes.items():
        c.setFillColor(TEAL if name == "50" else PALE)
        c.circle(x, y, 14, fill=1, stroke=1)
        c.setFillColor(white if name == "50" else INK)
        c.setFont("Sans-Bold", 9)
        c.drawCentredString(x, y - 3, name)
    c.setFillColor(INK)
    c.setFont("Sans", 8)
    c.drawString(10, 16, "Left child is smaller. Right child is larger. In-order visit: 20, 30, 40, 50, 60, 70, 80.")


def paint_search(c, w, h):
    values = ["2", "5", "8", "12", "16", "23", "38"]
    cell = 42
    left = (w - cell * 7) / 2
    c.setFillColor(INK)
    c.setFont("Sans", 8)
    c.drawString(10, h - 14, "Binary search for 16. Low, mid, and high move until mid holds the target.")
    rounds = [
        (0, 3, 6, "mid = 12, too small, search the right half"),
        (4, 5, 6, "mid = 23, too large, search the left half"),
        (4, 4, 4, "mid = 16, found"),
    ]
    for r, (lo, mid, hi, note) in enumerate(rounds):
        y = h - 48 - r * 32
        for i, val in enumerate(values):
            x = left + i * cell
            if i == mid:
                fill = TEAL
                color = white
            elif lo <= i <= hi:
                fill = PALE
                color = INK
            else:
                fill = Color(0.93, 0.93, 0.93)
                color = Color(0.6, 0.6, 0.6)
            c.setFillColor(fill)
            c.setStrokeColor(NAVY)
            c.rect(x, y, cell - 4, 20, fill=1, stroke=1)
            c.setFillColor(color)
            c.setFont("Sans-Bold", 8)
            c.drawCentredString(x + (cell - 4) / 2, y + 6, val)
        c.setFillColor(INK)
        c.setFont("Sans", 7.5)
        c.drawString(left, y - 11, note)


def paint_bubble(c, w, h):
    passes = [
        ["5", "1", "4", "2"],
        ["1", "4", "2", "5"],
        ["1", "2", "4", "5"],
        ["1", "2", "4", "5"],
    ]
    labels = ["Start", "After pass 1", "After pass 2", "After pass 3"]
    cell = 36
    c.setFillColor(INK)
    c.setFont("Sans", 8)
    c.drawString(8, h - 14, "Bubble sort on [5, 1, 4, 2]. Each pass walks left to right and swaps any pair that is out of order.")
    for r, row in enumerate(passes):
        y = h - 46 - r * 28
        c.setFont("Sans", 8)
        c.setFillColor(NAVY)
        c.drawString(10, y + 4, labels[r])
        for i, val in enumerate(row):
            x = 120 + i * cell
            c.setFillColor(TEAL if r == 3 else PALE)
            c.setStrokeColor(NAVY)
            c.roundRect(x, y, 30, 20, 3, fill=1, stroke=1)
            c.setFillColor(white if r == 3 else INK)
            c.setFont("Sans-Bold", 9)
            c.drawCentredString(x + 15, y + 5, val)


def paint_er(c, w, h):
    _box(c, 30, h / 2 - 22, 90, 44, "STUDENT", fill=PALE)
    _box(c, w - 130, h / 2 - 22, 90, 44, "BOOK", fill=PALE)
    c.setStrokeColor(NAVY)
    c.setFillColor(GOLD)
    c.saveState()
    c.translate(w / 2, h / 2)
    c.rotate(45)
    c.rect(-16, -16, 32, 32, fill=1, stroke=1)
    c.restoreState()
    c.setFillColor(INK)
    c.setFont("Sans-Bold", 7)
    c.drawCentredString(w / 2, h / 2 - 3, "borrows")
    c.setStrokeColor(NAVY)
    c.setLineWidth(1.2)
    c.line(120, h / 2, w / 2 - 24, h / 2)
    c.line(w / 2 + 24, h / 2, w - 130, h / 2)
    c.setFont("Sans", 8)
    c.drawCentredString(w / 2, h / 2 + 28, "M : N")
    c.setFillColor(INK)
    c.drawString(36, 18, "Rectangles are entities. The diamond is the relationship.")
    c.drawString(36, 6, "A many-to-many borrow relationship needs its own table in the relational model.")


def paint_cloud(c, w, h):
    tiers = [
        ("SaaS", "Ready-made software in the browser", "Google Docs, an online LMS"),
        ("PaaS", "A platform on which you deploy an app", "A host that runs your Python site"),
        ("IaaS", "Virtual machines, storage, networks", "A rented server you configure"),
    ]
    for i, (name, meaning, example) in enumerate(tiers):
        y = h - 36 - i * 36
        c.setFillColor(NAVY if i == 0 else TEAL if i == 1 else Color(0.18, 0.32, 0.42))
        c.roundRect(12, y, 70, 28, 4, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Sans-Bold", 10)
        c.drawCentredString(47, y + 8, name)
        c.setFillColor(INK)
        c.setFont("Sans", 8.5)
        c.drawString(96, y + 12, meaning)
        c.setFillColor(MUTED := Color(0.33, 0.38, 0.44))
        c.setFont("Sans", 8)
        c.drawString(96, y + 1, example)


def paint_normal(c, w, h):
    c.setFillColor(INK)
    c.setFont("Sans", 8)
    c.drawString(8, h - 14, "A registration table that breaks the rules, and the same facts in third normal form.")
    _box(
        c,
        10,
        28,
        200,
        78,
        "",
        fill=Color(0.98, 0.93, 0.93),
        lines=["Enrolment (unnormalised)", "StudentID, Name,", "CourseID, Course,", "Grade"],
    )
    _arrow(c, 214, 66, 246, 66)
    _box(c, 250, 78, 230, 36, "", fill=PALE, lines=["Student (StudentID, Name)"])
    _box(c, 250, 40, 230, 32, "", fill=PALE, lines=["Course (CourseID, Course)"])
    _box(c, 250, 4, 230, 32, "", fill=Color(0.90, 0.95, 0.90), lines=["Result (StudentID, CourseID, Grade)"])


def paint_confusion(c, w, h):
    c.setFillColor(INK)
    c.setFont("Sans", 8)
    c.drawString(8, h - 16, "A confusion matrix. Precision uses the predicted-positive column: 90 / (90 + 30) = 0.75.")
    headers_x = [180, 300]
    c.setFont("Sans-Bold", 8)
    c.drawCentredString(230, h - 36, "Predicted positive")
    c.drawCentredString(360, h - 36, "Predicted negative")
    labels = ["Actual positive", "Actual negative"]
    vals = [["90", "10"], ["30", "70"]]
    for r in range(2):
        c.setFont("Sans", 8)
        c.setFillColor(INK)
        c.drawRightString(150, h - 68 - r * 36, labels[r])
        for col in range(2):
            x = 170 + col * 120
            y = h - 80 - r * 36
            c.setFillColor(TEAL if (r, col) == (0, 0) else PALE)
            c.setStrokeColor(NAVY)
            c.roundRect(x, y, 90, 28, 3, fill=1, stroke=1)
            c.setFillColor(white if (r, col) == (0, 0) else INK)
            c.setFont("Sans-Bold", 12)
            c.drawCentredString(x + 45, y + 8, vals[r][col])


def make_diagram(spec: str, width: float):
    painters = {
        "gates": (paint_gates, 78, "The five gates used most often in this course."),
        "circuit": (paint_circuit, 150, "Worked circuit: invert B and C, AND A with B', then OR that result with C'."),
        "kmap": (paint_kmap, 148, "Adjacent 1s are grouped in sizes 1, 2, 4, or 8. Opposite edges of a K-map are adjacent."),
        "topologies": (paint_topologies, 100, "Four topologies. The gold dot in the star is the switch or hub."),
        "osi": (paint_osi, 168, "OSI is a reference model. TCP/IP is the stack the Internet actually runs."),
        "sdlc": (paint_sdlc, 78, "The seven names used for the life cycle in this course."),
        "bst": (paint_bst, 160, "Binary search tree used in the Class XII traversal examples."),
        "search": (paint_search, 130, "Grey cells are outside the current search window. The teal cell is the middle."),
        "bubble": (paint_bubble, 130, "The largest unsorted value settles at the right after each pass."),
        "er": (paint_er, 110, "Entity-relationship sketch for a college library."),
        "cloud": (paint_cloud, 130, "Three cloud service models, from the most managed to the least."),
        "normal": (paint_normal, 130, "Names and course titles are stored once. The grade stays in the link table."),
        "confusion": (paint_confusion, 120, "True positives sit on the top left of this layout."),
    }
    if spec not in painters:
        raise KeyError(spec)
    painter, height, caption = painters[spec]
    return Diagram(width, height, painter), caption
