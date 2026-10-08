"""SVG figures for the lecture notes. Kept simple so they stay vector drawings in the PDF."""

from __future__ import annotations


def _doc(width: int, height: int, body: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">'
        f'<rect width="{width}" height="{height}" fill="#F4F7FB" stroke="#D5DEE8"/>'
        f"{body}</svg>"
    )


def _text(x, y, label, size=13, fill="#1C2430", anchor="start"):
    safe = (
        str(label)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    return (
        f'<text x="{x}" y="{y}" font-family="Noto Sans" font-size="{size}" '
        f'fill="{fill}" text-anchor="{anchor}">{safe}</text>'
    )


def _and(x, y):
    return (
        f'<path d="M {x} {y+8} L {x} {y+52} A 22 22 0 0 0 {x} {y+8}" '
        f'fill="#ffffff" stroke="#0B3A5B" stroke-width="2"/>'
    )


def _or(x, y):
    return (
        f'<path d="M {x} {y+8} Q {x+18} {y+30} {x} {y+52} '
        f'Q {x+36} {y+52} {x+48} {y+30} Q {x+36} {y+8} {x} {y+8}" '
        f'fill="#ffffff" stroke="#0B3A5B" stroke-width="2"/>'
    )


def _not(x, y):
    return (
        f'<polygon points="{x},{y+10} {x},{y+50} {x+34},{y+30}" '
        f'fill="#ffffff" stroke="#0B3A5B" stroke-width="2"/>'
        f'<circle cx="{x+42}" cy="{y+30}" r="6" fill="#ffffff" stroke="#0B3A5B" stroke-width="2"/>'
    )


def _bubble_after_and(x, y):
    return (
        f'<path d="M {x} {y+8} L {x} {y+52} A 22 22 0 0 0 {x} {y+8}" '
        f'fill="#ffffff" stroke="#0B3A5B" stroke-width="2"/>'
        f'<circle cx="{x+28}" cy="{y+30}" r="6" fill="#ffffff" stroke="#0B3A5B" stroke-width="2"/>'
    )


def _xor(x, y):
    return (
        f'<path d="M {x-6} {y+8} Q {x+12} {y+30} {x-6} {y+52}" '
        f'fill="none" stroke="#0B3A5B" stroke-width="2"/>'
        + _or(x, y)
    )


def logic_gates() -> str:
    gates = [
        ("AND", _and(36, 36)),
        ("OR", _or(168, 36)),
        ("NOT", _not(300, 36)),
        ("NAND", _bubble_after_and(420, 36)),
        ("XOR", _xor(560, 36)),
    ]
    parts = [_text(16, 24, "Distinctive gate shapes", 14, "#0B3A5B")]
    labels_x = [48, 186, 312, 436, 576]
    for (name, shape), lx in zip(gates, labels_x):
        parts.append(shape)
        parts.append(_text(lx, 112, name, 13, "#0F6E6E", "middle"))
    return _doc(680, 130, "".join(parts))


def sample_circuit() -> str:
    # F = (A AND B) OR (NOT C)
    parts = [
        _text(16, 24, "F = (A AND B) OR (NOT C)", 14, "#0B3A5B"),
        _text(28, 58, "A"),
        _text(28, 92, "B"),
        _text(28, 150, "C"),
        '<line x1="48" y1="54" x2="110" y2="54" stroke="#1C2430" stroke-width="1.6"/>',
        '<line x1="48" y1="88" x2="110" y2="88" stroke="#1C2430" stroke-width="1.6"/>',
        '<line x1="48" y1="146" x2="120" y2="146" stroke="#1C2430" stroke-width="1.6"/>',
        _and(110, 42),
        _not(120, 124),
        '<line x1="154" y1="72" x2="250" y2="72" stroke="#1C2430" stroke-width="1.6"/>',
        '<line x1="250" y1="72" x2="250" y2="96" stroke="#1C2430" stroke-width="1.6"/>',
        '<line x1="168" y1="154" x2="250" y2="154" stroke="#1C2430" stroke-width="1.6"/>',
        '<line x1="250" y1="154" x2="250" y2="128" stroke="#1C2430" stroke-width="1.6"/>',
        _or(250, 78),
        '<line x1="298" y1="108" x2="360" y2="108" stroke="#1C2430" stroke-width="1.6"/>',
        _text(368, 112, "F", 16, "#0B3A5B"),
        _text(118, 128, "AND", 11, "#0F6E6E"),
        _text(118, 196, "NOT", 11, "#0F6E6E"),
        _text(262, 168, "OR", 11, "#0F6E6E"),
    ]
    return _doc(420, 214, "".join(parts))


def osi_tcp() -> str:
    osi = [
        ("7  Application", "#0B3A5B"),
        ("6  Presentation", "#1D4E89"),
        ("5  Session", "#0F6E6E"),
        ("4  Transport", "#C4A35A"),
        ("3  Network", "#8A5A00"),
        ("2  Data link", "#334155"),
        ("1  Physical", "#1C2430"),
    ]
    tcp = [
        ("Application", 0, 3, "#0B3A5B"),
        ("Transport", 3, 4, "#C4A35A"),
        ("Internet", 4, 5, "#8A5A00"),
        ("Link", 5, 7, "#334155"),
    ]
    parts = [
        _text(16, 24, "OSI", 14, "#0B3A5B"),
        _text(360, 24, "TCP/IP", 14, "#0B3A5B"),
    ]
    y = 40
    for label, color in osi:
        parts.append(
            f'<rect x="16" y="{y}" width="250" height="28" fill="{color}"/>'
        )
        parts.append(_text(28, y + 19, label, 13, "#ffffff"))
        y += 32
    for label, start, end, color in tcp:
        top = 40 + start * 32
        height = (end - start) * 32 - 4
        parts.append(
            f'<rect x="340" y="{top}" width="220" height="{height}" fill="{color}"/>'
        )
        parts.append(_text(450, top + height / 2 + 5, label, 13, "#ffffff", "middle"))
    return _doc(580, 280, "".join(parts))


def topologies() -> str:
    def panel(x, title):
        return (
            f'<rect x="{x}" y="36" width="150" height="150" fill="#ffffff" stroke="#D5DEE8"/>'
            + _text(x + 75, 58, title, 13, "#0B3A5B", "middle")
        )

    def node(cx, cy):
        return f'<circle cx="{cx}" cy="{cy}" r="8" fill="#0F6E6E"/>'

    def link(x1, y1, x2, y2):
        return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#0B3A5B" stroke-width="1.5"/>'

    parts = [_text(16, 24, "Four topologies", 14, "#0B3A5B"), panel(16, "Bus"), panel(182, "Star"), panel(348, "Ring"), panel(514, "Mesh")]
    # bus
    parts.append(link(36, 130, 146, 130))
    for x in (48, 78, 108, 136):
        parts.append(link(x, 110, x, 130))
        parts.append(node(x, 102))
    # star
    cx, cy = 257, 120
    parts.append(node(cx, cy))
    for dx, dy in ((-40, -28), (40, -28), (-40, 36), (40, 36)):
        parts.append(link(cx, cy, cx + dx, cy + dy))
        parts.append(node(cx + dx, cy + dy))
    # ring
    ring = [(423, 90), (470, 120), (450, 160), (396, 160), (376, 120)]
    for i, (x, y) in enumerate(ring):
        nx, ny = ring[(i + 1) % len(ring)]
        parts.append(link(x, y, nx, ny))
        parts.append(node(x, y))
    # mesh
    mesh = [(560, 100), (620, 90), (640, 140), (580, 160)]
    for i, (x, y) in enumerate(mesh):
        for x2, y2 in mesh[i + 1 :]:
            parts.append(link(x, y, x2, y2))
    for x, y in mesh:
        parts.append(node(x, y))
    return _doc(680, 204, "".join(parts))


def grade_flowchart() -> str:
    def box(x, y, w, h, label):
        return (
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#ffffff" stroke="#0B3A5B" stroke-width="1.6"/>'
            + _text(x + w / 2, y + h / 2 + 4, label, 12, "#1C2430", "middle")
        )

    def oval(x, y, w, h, label):
        return (
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="#E7F4F4" stroke="#0F6E6E" stroke-width="1.6"/>'
            + _text(x + w / 2, y + h / 2 + 4, label, 12, "#0B3A5B", "middle")
        )

    def diamond(cx, cy, label):
        return (
            f'<polygon points="{cx},{cy-28} {cx+70},{cy} {cx},{cy+28} {cx-70},{cy}" '
            f'fill="#FFF6E0" stroke="#8A5A00" stroke-width="1.6"/>'
            + _text(cx, cy + 4, label, 12, "#1C2430", "middle")
        )

    def arrow(x1, y1, x2, y2):
        return (
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#1C2430" stroke-width="1.4"/>'
            f'<polygon points="{x2},{y2} {x2-4},{y2-8} {x2+4},{y2-8}" fill="#1C2430"/>'
        )

    parts = [
        _text(16, 22, "Pass mark, the decision in the pseudocode", 14, "#0B3A5B"),
        oval(250, 36, 120, 32, "Start"),
        arrow(310, 68, 310, 86),
        box(230, 86, 160, 32, "Input mark"),
        arrow(310, 118, 310, 140),
        diamond(310, 168, "mark ≥ 40?"),
        _text(400, 158, "yes", 11, "#0F6E6E"),
        _text(188, 150, "no", 11, "#8C2F2F"),
        arrow(380, 168, 470, 168),
        box(470, 152, 120, 32, "Pass"),
        arrow(240, 168, 150, 168),
        box(30, 152, 120, 32, "Below 40"),
    ]
    return _doc(620, 220, "".join(parts))


def binary_search() -> str:
    values = [2, 5, 8, 12, 16, 23, 38]
    parts = [_text(16, 24, "Binary search for 16 in a sorted list", 14, "#0B3A5B")]
    steps = [
        (0, 6, 3, "Middle is 12. 16 is larger, so discard the left half."),
        (4, 6, 5, "Middle is 23. 16 is smaller, so discard the right half."),
        (4, 4, 4, "Middle is 16. Found."),
    ]
    y = 44
    for low, high, mid, note in steps:
        x = 24
        for index, value in enumerate(values):
            if low <= index <= high:
                fill = "#C4A35A" if index == mid else "#ffffff"
            else:
                fill = "#E7EEF6"
            parts.append(
                f'<rect x="{x}" y="{y}" width="36" height="28" fill="{fill}" stroke="#0B3A5B"/>'
            )
            parts.append(_text(x + 18, y + 19, str(value), 12, "#1C2430", "middle"))
            x += 40
        parts.append(_text(320, y + 19, note, 12, "#334155"))
        y += 40
    parts.append(_text(24, y + 8, "Grey cells are discarded. Gold is the middle compared on that step.", 12, "#5C6B7A"))
    return _doc(700, 196, "".join(parts))


def library_er() -> str:
    def entity(x, y, w, h, title, lines):
        body = (
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#ffffff" stroke="#0B3A5B" stroke-width="1.8"/>'
            + _text(x + 12, y + 22, title, 14, "#0B3A5B")
        )
        yy = y + 42
        for line in lines:
            body += _text(x + 12, yy, line, 12)
            yy += 16
        return body

    parts = [
        _text(16, 24, "Library schema: one-to-many on both sides of Loan", 14, "#0B3A5B"),
        entity(24, 48, 170, 88, "Student", ["RollNo  PK", "Name"]),
        entity(250, 70, 180, 100, "Loan", ["LoanId  PK", "RollNo  FK", "BookId  FK"]),
        entity(490, 48, 160, 88, "Book", ["BookId  PK", "Title"]),
        '<line x1="194" y1="92" x2="250" y2="110" stroke="#0F6E6E" stroke-width="2"/>',
        '<line x1="430" y1="110" x2="490" y2="92" stroke="#0F6E6E" stroke-width="2"/>',
        _text(200, 84, "1", 13, "#0F6E6E"),
        _text(228, 124, "M", 13, "#0F6E6E"),
        _text(436, 124, "M", 13, "#0F6E6E"),
        _text(468, 84, "1", 13, "#0F6E6E"),
    ]
    return _doc(674, 196, "".join(parts))


def comm_model() -> str:
    labels = ["Sender", "Encoder", "Medium", "Decoder", "Receiver"]
    parts = [_text(16, 24, "A message crossing a noisy medium", 14, "#0B3A5B")]
    x = 20
    for index, label in enumerate(labels):
        fill = "#FFF6E0" if label == "Medium" else "#ffffff"
        parts.append(
            f'<rect x="{x}" y="56" width="100" height="40" rx="4" fill="{fill}" stroke="#0B3A5B"/>'
        )
        parts.append(_text(x + 50, 80, label, 12, "#1C2430", "middle"))
        if index < len(labels) - 1:
            parts.append(
                f'<line x1="{x+100}" y1="76" x2="{x+128}" y2="76" stroke="#0F6E6E" stroke-width="1.6"/>'
                f'<polygon points="{x+128},76 {x+120},72 {x+120},80" fill="#0F6E6E"/>'
            )
        x += 128
    parts.append(_text(300, 130, "Noise can change the signal on the medium", 12, "#8A5A00", "middle"))
    return _doc(670, 152, "".join(parts))


def kmap_b() -> str:
    # F = 1 wherever B = 0, which is the two left columns in Gray-code BC.
    headers = ["BC 00", "01", "11", "10"]
    rows = [("A=0", ["1", "1", "0", "0"]), ("A=1", ["1", "1", "0", "0"])]
    parts = [_text(16, 24, "K-map for F = B′. The four 1s in B = 0 form one group.", 14, "#0B3A5B")]
    x0, y0 = 70, 48
    parts.append(_text(x0 + 90, y0 - 6, "BC", 12, "#0F6E6E", "middle"))
    for col, header in enumerate(headers):
        parts.append(_text(x0 + 36 + col * 52, y0 + 16, header.replace("BC ", ""), 11, "#5C6B7A", "middle"))
    for r, (label, cells) in enumerate(rows):
        parts.append(_text(x0 - 8, y0 + 48 + r * 36, label, 12, "#0B3A5B", "end"))
        for c, value in enumerate(cells):
            grouped = c in (0, 1)
            fill = "#E7F4F4" if grouped else "#ffffff"
            parts.append(
                f'<rect x="{x0 + c * 52}" y="{y0 + 28 + r * 36}" width="48" height="32" fill="{fill}" stroke="#0B3A5B"/>'
            )
            parts.append(_text(x0 + 24 + c * 52, y0 + 49 + r * 36, value, 14, "#1C2430", "middle"))
    parts.append(
        '<rect x="68" y="74" width="108" height="76" fill="none" stroke="#C4A35A" stroke-width="3"/>'
    )
    parts.append(_text(300, 120, "Group drops A and C.", 13))
    parts.append(_text(300, 142, "B is 0 throughout, so F = B′.", 13))
    return _doc(620, 180, "".join(parts))


def _tree(root, width, height, title):
    parts = [_text(16, 24, title, 14, "#0B3A5B")]

    def walk(node, depth, left, right):
        if node is None:
            return
        label, child_left, child_right = node
        x = (left + right) / 2
        y = 48 + depth * 52
        if child_left:
            cx = (left + x) / 2
            cy = 48 + (depth + 1) * 52
            parts.append(f'<line x1="{x}" y1="{y}" x2="{cx}" y2="{cy}" stroke="#0B3A5B" stroke-width="1.5"/>')
            walk(child_left, depth + 1, left, x)
        if child_right:
            cx = (x + right) / 2
            cy = 48 + (depth + 1) * 52
            parts.append(f'<line x1="{x}" y1="{y}" x2="{cx}" y2="{cy}" stroke="#0B3A5B" stroke-width="1.5"/>')
            walk(child_right, depth + 1, x, right)
        parts.append(f'<circle cx="{x}" cy="{y}" r="16" fill="#ffffff" stroke="#0F6E6E" stroke-width="2"/>')
        parts.append(_text(x, y + 4, label, 12, "#0B3A5B", "middle"))

    walk(root, 0, 30, width - 30)
    return _doc(width, height, "".join(parts))


def bst() -> str:
    tree = (
        "50",
        ("30", ("20", None, None), ("40", None, None)),
        ("70", ("60", None, None), ("80", None, None)),
    )
    return _tree(tree, 420, 210, "Binary search tree. Inorder reads 20, 30, 40, 50, 60, 70, 80.")


def org_chart() -> str:
    tree = (
        "CEO",
        ("HR", ("Staff", None, None), None),
        ("IT", ("Dev", None, None), ("Accounts", None, None)),
    )
    return _tree(tree, 420, 210, "Organisation tree used for the BFS and DFS traces.")


def stack_queue() -> str:
    parts = [
        _text(16, 24, "Stack: last in, first out", 14, "#0B3A5B"),
        _text(250, 24, "Queue: first in, first out", 14, "#0B3A5B"),
    ]
    for i, label in enumerate(["top: call 3", "call 2", "call 1"]):
        y = 44 + i * 32
        parts.append(f'<rect x="36" y="{y}" width="140" height="28" fill="#ffffff" stroke="#0B3A5B"/>')
        parts.append(_text(106, y + 19, label, 12, "#1C2430", "middle"))
    parts.append(_text(106, 156, "pop removes call 3", 12, "#0F6E6E", "middle"))
    jobs = ["job 1", "job 2", "job 3"]
    for i, label in enumerate(jobs):
        x = 250 + i * 78
        parts.append(f'<rect x="{x}" y="70" width="70" height="32" fill="#ffffff" stroke="#0B3A5B"/>')
        parts.append(_text(x + 35, 90, label, 12, "#1C2430", "middle"))
    parts.append(_text(268, 64, "front", 11, "#0F6E6E"))
    parts.append(_text(430, 64, "back", 11, "#8A5A00"))
    parts.append(_text(360, 130, "dequeue removes job 1", 12, "#0F6E6E", "middle"))
    return _doc(520, 176, "".join(parts))


def train_test() -> str:
    parts = [
        _text(16, 24, "Train on most rows. Measure on rows the model has not seen.", 14, "#0B3A5B"),
        '<rect x="24" y="56" width="520" height="36" fill="#0B3A5B"/>',
        '<rect x="440" y="56" width="104" height="36" fill="#C4A35A"/>',
        _text(180, 78, "training rows", 13, "#ffffff", "middle"),
        _text(492, 78, "test", 13, "#1C2430", "middle"),
        _text(24, 120, "A score on the training rows can be memorisation. The test rows are the check.", 12, "#334155"),
    ]
    return _doc(568, 144, "".join(parts))


FIGURES = {
    "logic-gates": logic_gates,
    "sample-circuit": sample_circuit,
    "osi-tcp": osi_tcp,
    "topologies": topologies,
    "grade-flowchart": grade_flowchart,
    "binary-search": binary_search,
    "library-er": library_er,
    "comm-model": comm_model,
    "kmap-b": kmap_b,
    "bst": bst,
    "org-chart": org_chart,
    "stack-queue": stack_queue,
    "train-test": train_test,
}


def svg_for(figure_id: str) -> str:
    try:
        return FIGURES[figure_id]()
    except KeyError as exc:
        raise KeyError(f"Unknown figure {figure_id}") from exc
