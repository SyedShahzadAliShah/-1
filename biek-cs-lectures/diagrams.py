"""Canvas diagrams for BIEK CS lectures."""

from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import Flowable

NAVY = colors.HexColor("#0B2545")
TEAL = colors.HexColor("#0D7377")
GOLD = colors.HexColor("#C9A227")
SOFT = colors.HexColor("#E8F1F2")
CREAM = colors.HexColor("#F7F3E9")
WHITE = colors.white
BOX = colors.HexColor("#1A1A1A")


class Diagram(Flowable):
    def __init__(self, kind, height=62 * mm):
        super().__init__()
        self.kind = kind
        self._h = height

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        self.height = self._h
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(SOFT)
        c.setStrokeColor(TEAL)
        c.roundRect(0, 0, self.width, self.height, 5, fill=1, stroke=1)
        fn = DIAGRAMS.get(self.kind)
        if fn:
            fn(c, self.width, self.height)


def _box(c, x, y, w, h, text, fill=TEAL, fg=WHITE, size=8):
    c.setFillColor(fill)
    c.setStrokeColor(NAVY)
    c.roundRect(x, y, w, h, 3, fill=1, stroke=1)
    c.setFillColor(fg)
    c.setFont("Head-Bold", size)
    lines = text.split("\n")
    total = len(lines) * (size + 2)
    ty = y + h / 2 + total / 2 - size
    for line in lines:
        c.drawCentredString(x + w / 2, ty, line)
        ty -= size + 2


def _arrow(c, x1, y1, x2, y2):
    c.setStrokeColor(NAVY)
    c.setFillColor(NAVY)
    c.setLineWidth(1.4)
    c.line(x1, y1, x2, y2)
    c.drawCentredString((x1 + x2) / 2, (y1 + y2) / 2 + 3, "")
    # simple arrow head
    c.circle(x2, y2, 2, fill=1, stroke=0)


def _label(c, x, y, text, size=7.5, color=NAVY):
    c.setFillColor(color)
    c.setFont("Head", size)
    c.drawCentredString(x, y, text)


def d_block(c, w, h):
    cx = w / 2
    _box(c, cx - 28 * mm, h - 18 * mm, 56 * mm, 12 * mm, "INPUT DEVICES")
    _arrow(c, cx, h - 18 * mm, cx, h - 22 * mm)
    _box(c, cx - 32 * mm, h / 2 - 8 * mm, 64 * mm, 16 * mm, "CPU  (ALU + CU + REGISTERS)", fill=NAVY)
    _arrow(c, cx, h / 2 - 8 * mm, cx, 22 * mm)
    _box(c, cx - 28 * mm, 8 * mm, 56 * mm, 12 * mm, "OUTPUT DEVICES", fill=GOLD, fg=NAVY)
    _box(c, 10 * mm, h / 2 - 8 * mm, 28 * mm, 16 * mm, "MEMORY\n(RAM / ROM)", fill=colors.HexColor("#3D5A80"))
    _arrow(c, 38 * mm, h / 2, cx - 32 * mm, h / 2)
    _box(c, w - 38 * mm, h / 2 - 8 * mm, 28 * mm, 16 * mm, "STORAGE\nHDD / SSD", fill=colors.HexColor("#3D5A80"))
    _arrow(c, cx + 32 * mm, h / 2, w - 38 * mm, h / 2)


def d_fetch(c, w, h):
    steps = ["FETCH\nInstruction", "DECODE\nInstruction", "EXECUTE\nInstruction", "STORE\nResult"]
    n = len(steps)
    box_w = 32 * mm
    gap = (w - n * box_w) / (n + 1)
    y = h / 2 - 8 * mm
    for i, s in enumerate(steps):
        x = gap + i * (box_w + gap)
        _box(c, x, y, box_w, 18 * mm, s, fill=NAVY if i % 2 == 0 else TEAL)
        if i < n - 1:
            _arrow(c, x + box_w, y + 9 * mm, x + box_w + gap, y + 9 * mm)
    _label(c, w / 2, 10 * mm, "Instruction Cycle (Fetch – Decode – Execute – Store)", 8)


def d_cpu(c, w, h):
    _box(c, 8 * mm, 8 * mm, w - 16 * mm, h - 16 * mm, "", fill=CREAM, fg=NAVY)
    _label(c, w / 2, h - 14 * mm, "MICROPROCESSOR (CPU)", 9)
    _box(c, 16 * mm, h / 2 + 2 * mm, 50 * mm, 16 * mm, "CONTROL UNIT (CU)")
    _box(c, w / 2 + 4 * mm, h / 2 + 2 * mm, 50 * mm, 16 * mm, "ALU")
    _box(c, 16 * mm, 14 * mm, w - 32 * mm, 14 * mm, "REGISTERS  (AC, PC, IR, MAR, MDR, SP)", fill=NAVY)
    _label(c, w / 2, h / 2 - 4 * mm, "System Bus: Address  |  Data  |  Control", 8)


def d_modes(c, w, h):
    thirds = w / 3
    titles = ["SIMPLEX", "HALF DUPLEX", "FULL DUPLEX"]
    notes = ["One way only\nKeyboard → CPU", "Both ways,\nnot together\nWalkie-talkie", "Both ways\nat the same time\nTelephone"]
    for i in range(3):
        x = 6 * mm + i * thirds
        _box(c, x, 28 * mm, thirds - 12 * mm, 26 * mm, titles[i], fill=NAVY if i != 2 else TEAL)
        _label(c, x + (thirds - 12 * mm) / 2, 12 * mm, notes[i].split("\n")[0], 7.5)
        _label(c, x + (thirds - 12 * mm) / 2, 4 * mm, notes[i].split("\n")[-1], 7)


def d_osi(c, w, h):
    layers = [
        ("7 Application", "HTTP, SMTP, FTP, DNS"),
        ("6 Presentation", "Encryption, compression"),
        ("5 Session", "Start / manage / end session"),
        ("4 Transport", "TCP, UDP  —  ports"),
        ("3 Network", "IP, routing"),
        ("2 Data Link", "MAC, frames, NIC, switch"),
        ("1 Physical", "Cables, hubs, bits"),
    ]
    bh = (h - 10 * mm) / 7
    for i, (name, desc) in enumerate(layers):
        y = h - 6 * mm - (i + 1) * bh
        fill = NAVY if i % 2 == 0 else TEAL
        c.setFillColor(fill)
        c.roundRect(10 * mm, y, w - 20 * mm, bh - 1.5 * mm, 2, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Head-Bold", 8)
        c.drawString(14 * mm, y + bh / 2 - 3, name)
        c.setFont("Head", 7.5)
        c.drawRightString(w - 14 * mm, y + bh / 2 - 3, desc)


def d_star(c, w, h):
    cx, cy = w / 2, h / 2
    _box(c, cx - 18 * mm, cy - 8 * mm, 36 * mm, 16 * mm, "HUB / SWITCH", fill=NAVY, size=7)
    pts = [
        (cx - 58 * mm, cy + 18 * mm),
        (cx + 34 * mm, cy + 18 * mm),
        (cx - 58 * mm, cy - 24 * mm),
        (cx + 34 * mm, cy - 24 * mm),
    ]
    for i, (x, y) in enumerate(pts):
        _box(c, x, y, 24 * mm, 10 * mm, f"PC {i+1}", fill=TEAL)
        hx = cx - 18 * mm if x < cx else cx + 18 * mm
        hy = cy + 8 * mm if y > cy else cy - 8 * mm
        _arrow(c, x + 12 * mm, y + 5 * mm, hx, hy)


def d_bus(c, w, h):
    c.setStrokeColor(NAVY)
    c.setLineWidth(3)
    c.line(12 * mm, h / 2, w - 12 * mm, h / 2)
    _label(c, w / 2, h / 2 + 4 * mm, "SHARED BACKBONE CABLE", 8)
    for i, x in enumerate([20 * mm, 50 * mm, 90 * mm, 130 * mm]):
        c.setLineWidth(1.2)
        c.line(x, h / 2, x, h / 2 + 16 * mm)
        _box(c, x - 10 * mm, h / 2 + 16 * mm, 20 * mm, 9 * mm, f"PC{i+1}", fill=TEAL)
    _box(c, 12 * mm, h / 2 - 4 * mm, 8 * mm, 8 * mm, "T", fill=GOLD, fg=NAVY, size=7)
    _box(c, w - 20 * mm, h / 2 - 4 * mm, 8 * mm, 8 * mm, "T", fill=GOLD, fg=NAVY, size=7)
    _label(c, w / 2, 8 * mm, "Terminators (T) absorb the signal at both ends", 7.5)


def d_ring(c, w, h):
    import math

    cx, cy, r = w / 2, h / 2, 16 * mm
    c.setStrokeColor(NAVY)
    c.setFillColor(NAVY)
    c.setLineWidth(1.6)
    c.circle(cx, cy, r, fill=0, stroke=1)
    for i in range(4):
        ang = (i * 90 + 45) * math.pi / 180
        px = cx + (r + 14 * mm) * math.cos(ang)
        py = cy + (r + 14 * mm) * math.sin(ang)
        _box(c, px - 11 * mm, py - 5 * mm, 22 * mm, 10 * mm, f"PC {i+1}", fill=TEAL, size=7)
        ix = cx + r * math.cos(ang)
        iy = cy + r * math.sin(ang)
        c.setStrokeColor(NAVY)
        c.setLineWidth(1.1)
        c.line(ix, iy, px, py)


def d_mesh(c, w, h):
    pts = [(30 * mm, h - 18 * mm), (w - 40 * mm, h - 18 * mm), (30 * mm, 16 * mm), (w - 40 * mm, 16 * mm), (w / 2 - 10 * mm, h / 2)]
    c.setStrokeColor(NAVY)
    c.setLineWidth(0.8)
    for i, (x1, y1) in enumerate(pts):
        for j, (x2, y2) in enumerate(pts):
            if i < j:
                c.line(x1 + 10 * mm, y1 + 5 * mm, x2 + 10 * mm, y2 + 5 * mm)
    for i, (x, y) in enumerate(pts):
        _box(c, x, y, 20 * mm, 10 * mm, f"N{i+1}", fill=NAVY, size=7)


def d_gate(name):
    def draw(c, w, h):
        c.setFillColor(NAVY)
        c.setFont("Head-Bold", 12)
        c.drawCentredString(w / 2, h - 14 * mm, name + " GATE")
        c.setFont("Head", 8)
        if name == "NOT":
            _box(c, 18 * mm, h / 2 - 6 * mm, 24 * mm, 12 * mm, "A", fill=TEAL)
            _arrow(c, 42 * mm, h / 2, 70 * mm, h / 2)
            _box(c, 70 * mm, h / 2 - 10 * mm, 36 * mm, 20 * mm, "NOT", fill=NAVY)
            _arrow(c, 106 * mm, h / 2, 132 * mm, h / 2)
            _box(c, 132 * mm, h / 2 - 6 * mm, 28 * mm, 12 * mm, "A'", fill=GOLD, fg=NAVY)
        else:
            _box(c, 12 * mm, h / 2 + 8 * mm, 22 * mm, 10 * mm, "A", fill=TEAL)
            _box(c, 12 * mm, h / 2 - 18 * mm, 22 * mm, 10 * mm, "B", fill=TEAL)
            _arrow(c, 34 * mm, h / 2 + 13 * mm, 58 * mm, h / 2 + 4 * mm)
            _arrow(c, 34 * mm, h / 2 - 13 * mm, 58 * mm, h / 2 - 4 * mm)
            _box(c, 58 * mm, h / 2 - 12 * mm, 40 * mm, 24 * mm, name, fill=NAVY)
            _arrow(c, 98 * mm, h / 2, 126 * mm, h / 2)
            _box(c, 126 * mm, h / 2 - 6 * mm, 32 * mm, 12 * mm, "Y", fill=GOLD, fg=NAVY)
        _label(c, w / 2, 8 * mm, "Draw this symbol AND the truth table in Section C answers.", 7.5)

    return draw


def d_modem(c, w, h):
    _box(c, 10 * mm, h / 2 - 10 * mm, 40 * mm, 20 * mm, "DIGITAL\nComputer", fill=NAVY)
    _arrow(c, 50 * mm, h / 2, 68 * mm, h / 2)
    _box(c, 68 * mm, h / 2 - 10 * mm, 36 * mm, 20 * mm, "MODEM", fill=GOLD, fg=NAVY)
    _arrow(c, 104 * mm, h / 2, 122 * mm, h / 2)
    _box(c, 122 * mm, h / 2 - 10 * mm, 44 * mm, 20 * mm, "ANALOG\nTelephone line", fill=TEAL)
    _label(c, w / 2, 12 * mm, "Modulation: digital → analog     Demodulation: analog → digital", 8)


def d_dbms(c, w, h):
    levels = [
        ("External / View level", "What each user sees"),
        ("Logical / Conceptual level", "Whole database design"),
        ("Physical / Internal level", "How data is stored on disk"),
    ]
    for i, (n, d) in enumerate(levels):
        y = h - 18 * mm - i * 16 * mm
        _box(c, 18 * mm, y, w - 36 * mm, 14 * mm, f"{n}   —   {d}", fill=NAVY if i != 1 else TEAL)


def d_keys(c, w, h):
    _box(c, 12 * mm, h / 2 + 4 * mm, 70 * mm, 22 * mm, "STUDENT\nRollNo (PK), Name, Class", fill=NAVY)
    _box(c, w - 82 * mm, h / 2 + 4 * mm, 70 * mm, 22 * mm, "RESULT\nRollNo (FK), Marks, Grade", fill=TEAL)
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.6)
    c.line(82 * mm, h / 2 + 15 * mm, w - 82 * mm, h / 2 + 15 * mm)
    _label(c, w / 2, 14 * mm, "Primary Key uniquely identifies a row. Foreign Key links two tables.", 8)


def d_c_struct(c, w, h):
    parts = [
        "#include <stdio.h>     /* preprocessor */",
        "int main() {           /* starting point */",
        "    statements;        /* body */",
        "    return 0;          /* exit status */",
        "}",
    ]
    c.setFillColor(NAVY)
    c.roundRect(12 * mm, 8 * mm, w - 24 * mm, h - 16 * mm, 4, fill=1, stroke=0)
    c.setFillColor(GOLD)
    c.setFont("Head-Bold", 8)
    c.drawString(18 * mm, h - 16 * mm, "BASIC STRUCTURE OF A C PROGRAM")
    c.setFillColor(WHITE)
    c.setFont("Mono", 8)
    y = h - 26 * mm
    for p in parts:
        c.drawString(20 * mm, y, p)
        y -= 8 * mm


def d_if(c, w, h):
    _box(c, w / 2 - 22 * mm, h - 16 * mm, 44 * mm, 10 * mm, "START", fill=NAVY, size=7)
    _arrow(c, w / 2, h - 16 * mm, w / 2, h - 22 * mm)
    # diamond-ish
    _box(c, w / 2 - 28 * mm, h / 2 + 2 * mm, 56 * mm, 14 * mm, "Condition?", fill=GOLD, fg=NAVY, size=8)
    _box(c, 10 * mm, 14 * mm, 50 * mm, 12 * mm, "TRUE  →  if body", fill=TEAL, size=7)
    _box(c, w - 60 * mm, 14 * mm, 50 * mm, 12 * mm, "FALSE  →  else body", fill=NAVY, size=7)
    _arrow(c, w / 2 - 28 * mm, h / 2 + 9 * mm, 35 * mm, 26 * mm)
    _arrow(c, w / 2 + 28 * mm, h / 2 + 9 * mm, w - 35 * mm, 26 * mm)


def d_for(c, w, h):
    _box(c, 12 * mm, h / 2 - 10 * mm, 38 * mm, 20 * mm, "INIT\ni = 1", fill=NAVY)
    _arrow(c, 50 * mm, h / 2, 62 * mm, h / 2)
    _box(c, 62 * mm, h / 2 - 10 * mm, 42 * mm, 20 * mm, "TEST\ni <= n ?", fill=GOLD, fg=NAVY)
    _arrow(c, 104 * mm, h / 2, 116 * mm, h / 2)
    _box(c, 116 * mm, h / 2 - 10 * mm, 42 * mm, 20 * mm, "BODY\nprintf", fill=TEAL)
    _label(c, w / 2, 10 * mm, "After body: increment i++  then go back to TEST", 8)


def d_hier(c, w, h):
    _box(c, w / 2 - 16 * mm, h - 18 * mm, 32 * mm, 10 * mm, "ROOT", fill=NAVY, size=7)
    _box(c, 20 * mm, h / 2, 32 * mm, 10 * mm, "CHILD A", fill=TEAL, size=7)
    _box(c, w / 2 - 16 * mm, h / 2, 32 * mm, 10 * mm, "CHILD B", fill=TEAL, size=7)
    _box(c, w - 52 * mm, h / 2, 32 * mm, 10 * mm, "CHILD C", fill=TEAL, size=7)
    _box(c, 14 * mm, 10 * mm, 28 * mm, 9 * mm, "LEAF", fill=GOLD, fg=NAVY, size=7)
    _box(c, 48 * mm, 10 * mm, 28 * mm, 9 * mm, "LEAF", fill=GOLD, fg=NAVY, size=7)
    c.setStrokeColor(NAVY)
    c.setLineWidth(1)
    c.line(w / 2, h - 18 * mm, 36 * mm, h / 2 + 10 * mm)
    c.line(w / 2, h - 18 * mm, w / 2, h / 2 + 10 * mm)
    c.line(w / 2, h - 18 * mm, w - 36 * mm, h / 2 + 10 * mm)
    c.line(36 * mm, h / 2, 28 * mm, 19 * mm)
    c.line(36 * mm, h / 2, 62 * mm, 19 * mm)


def d_cover_badge(c, w, h):
    pass


DIAGRAMS = {
    "block": d_block,
    "fetch": d_fetch,
    "cpu": d_cpu,
    "modes": d_modes,
    "osi": d_osi,
    "star": d_star,
    "bus": d_bus,
    "ring": d_ring,
    "mesh": d_mesh,
    "and": d_gate("AND"),
    "or": d_gate("OR"),
    "not": d_gate("NOT"),
    "nand": d_gate("NAND"),
    "nor": d_gate("NOR"),
    "xor": d_gate("XOR"),
    "modem": d_modem,
    "dbms": d_dbms,
    "keys": d_keys,
    "c_struct": d_c_struct,
    "if": d_if,
    "for": d_for,
    "hier": d_hier,
}


class CoverPage(Flowable):
    def __init__(self, kicker, title, subtitle, bullets, edition):
        super().__init__()
        self.kicker = kicker
        self.title = title
        self.subtitle = subtitle
        self.bullets = bullets
        self.edition = edition

    def wrap(self, availWidth, availHeight):
        from reportlab.lib.pagesizes import A4

        self.width, self.height = A4
        return self.width, self.height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        # already painted by template; draw text
        c.setFillColor(GOLD)
        c.setFont("Head-Bold", 11)
        c.drawCentredString(w / 2, h - 42 * mm, self.kicker.upper())
        c.setFillColor(WHITE)
        c.setFont("Head-Bold", 26)
        # wrap title
        from reportlab.pdfbase.pdfmetrics import stringWidth

        words = self.title.split()
        lines, cur = [], ""
        for word in words:
            trial = (cur + " " + word).strip()
            if stringWidth(trial, "Head-Bold", 26) < w - 50 * mm:
                cur = trial
            else:
                lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
        y = h - 58 * mm
        for line in lines:
            c.drawCentredString(w / 2, y, line)
            y -= 12 * mm
        c.setFont("Body", 13)
        c.setFillColor(CREAM)
        y -= 4 * mm
        for part in self.subtitle.split("\n"):
            c.drawCentredString(w / 2, y, part)
            y -= 7 * mm
        # gold rule
        c.setStrokeColor(GOLD)
        c.setLineWidth(1.4)
        c.line(40 * mm, y - 2 * mm, w - 40 * mm, y - 2 * mm)
        y -= 16 * mm
        from reportlab.pdfbase.pdfmetrics import stringWidth as sw
        c.setFont("Head", 11)
        max_w = max(sw(b, "Head", 11) for b in self.bullets)
        left = w / 2 - max_w / 2
        for b in self.bullets:
            c.setFillColor(GOLD)
            c.circle(left - 5 * mm, y + 3, 2.4, fill=1, stroke=0)
            c.setFillColor(WHITE)
            c.drawString(left, y, b)
            y -= 8 * mm
        c.setFillColor(GOLD)
        c.setFont("Head-Bold", 10)
        c.drawCentredString(w / 2, 36 * mm, self.edition)
