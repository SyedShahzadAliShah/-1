"""Inline SVG diagrams for BIEK CS lectures."""


def _svg(w, h, body, vb=None):
    view = vb or f"0 0 {w} {h}"
    return f'''<svg viewBox="{view}" width="{w}" xmlns="http://www.w3.org/2000/svg" font-family="Inter, Liberation Sans, sans-serif">
{body}
</svg>'''


def computer_block():
    return _svg(640, 220, '''
  <rect x="8" y="8" width="624" height="204" rx="10" fill="#eef5f9" stroke="#0b3d5c" stroke-width="2"/>
  <rect x="40" y="70" width="120" height="70" rx="6" fill="#14557a" />
  <text x="100" y="110" fill="#fff" text-anchor="middle" font-size="13" font-weight="700">INPUT</text>
  <rect x="260" y="40" width="140" height="130" rx="6" fill="#0b3d5c" />
  <text x="330" y="85" fill="#fff" text-anchor="middle" font-size="14" font-weight="700">CPU</text>
  <text x="330" y="108" fill="#d9e8f2" text-anchor="middle" font-size="11">ALU + CU</text>
  <text x="330" y="128" fill="#c9a227" text-anchor="middle" font-size="11">Registers</text>
  <rect x="480" y="70" width="120" height="70" rx="6" fill="#2e7d4f" />
  <text x="540" y="110" fill="#fff" text-anchor="middle" font-size="13" font-weight="700">OUTPUT</text>
  <rect x="260" y="180" width="140" height="22" rx="4" fill="#c9a227" />
  <text x="330" y="196" fill="#1a1404" text-anchor="middle" font-size="11" font-weight="700">MEMORY</text>
  <path d="M160 105 H260" stroke="#0b3d5c" stroke-width="3"/>
  <path d="M400 105 H480" stroke="#0b3d5c" stroke-width="3"/>
  <text x="330" y="28" font-size="12" fill="#0b3d5c" font-weight="700" text-anchor="middle">Block diagram of a computer system</text>
''')


def fetch_cycle():
    boxes = [
        (20, "Fetch"),
        (160, "Decode"),
        (300, "Execute"),
        (440, "Store"),
    ]
    parts = []
    for i, (x, label) in enumerate(boxes):
        parts.append(f'<rect x="{x}" y="50" width="120" height="56" rx="8" fill="#0b3d5c"/>')
        parts.append(f'<text x="{x+60}" y="84" fill="#fff" text-anchor="middle" font-size="14" font-weight="700">{label}</text>')
        if i < 3:
            parts.append(f'<text x="{x+128}" y="84" font-size="18" fill="#c9a227">→</text>')
    parts.append('<path d="M500 106 C 500 150, 80 150, 80 106" fill="none" stroke="#c9a227" stroke-width="2"/>')
    parts.append('<text x="290" y="168" text-anchor="middle" font-size="12" fill="#0b3d5c">repeats for the next instruction</text>')
    return _svg(640, 190, "\n".join(parts))


def osi_layers():
    names = [
        ("7 Application", "#0b3d5c", "HTTP, SMTP, FTP, DNS"),
        ("6 Presentation", "#14557a", "encryption, compression, translation"),
        ("5 Session", "#1c6a92", "start, manage, end sessions"),
        ("4 Transport", "#2b5ea7", "TCP, UDP  —  ports, reliability"),
        ("3 Network", "#2e7d4f", "IP addressing, routing"),
        ("2 Data Link", "#6b3fa0", "frames, MAC, switches"),
        ("1 Physical", "#8a5a2a", "cables, bits, hubs, NICs"),
    ]
    parts = []
    for i, (name, color, note) in enumerate(names):
        y = 12 + i * 36
        parts.append(f'<rect x="40" y="{y}" width="560" height="32" rx="5" fill="{color}"/>')
        parts.append(f'<text x="56" y="{y+21}" fill="#fff" font-size="13" font-weight="700">{name}</text>')
        parts.append(f'<text x="580" y="{y+21}" fill="#f3f7fb" font-size="11" text-anchor="end">{note}</text>')
    return _svg(640, 275, "\n".join(parts))


def topologies():
    return _svg(640, 210, '''
  <text x="80" y="22" text-anchor="middle" font-size="12" font-weight="700" fill="#0b3d5c">Bus</text>
  <line x1="20" y1="90" x2="150" y2="90" stroke="#0b3d5c" stroke-width="4"/>
  <circle cx="45" cy="60" r="8" fill="#c9a227"/><line x1="45" y1="68" x2="45" y2="90" stroke="#0b3d5c"/>
  <circle cx="85" cy="120" r="8" fill="#c9a227"/><line x1="85" y1="112" x2="85" y2="90" stroke="#0b3d5c"/>
  <circle cx="125" cy="60" r="8" fill="#c9a227"/><line x1="125" y1="68" x2="125" y2="90" stroke="#0b3d5c"/>

  <text x="250" y="22" text-anchor="middle" font-size="12" font-weight="700" fill="#0b3d5c">Star</text>
  <circle cx="250" cy="95" r="12" fill="#0b3d5c"/>
  <circle cx="250" cy="45" r="8" fill="#c9a227"/><line x1="250" y1="53" x2="250" y2="83" stroke="#0b3d5c"/>
  <circle cx="300" cy="95" r="8" fill="#c9a227"/><line x1="292" y1="95" x2="262" y2="95" stroke="#0b3d5c"/>
  <circle cx="200" cy="95" r="8" fill="#c9a227"/><line x1="208" y1="95" x2="238" y2="95" stroke="#0b3d5c"/>
  <circle cx="250" cy="145" r="8" fill="#c9a227"/><line x1="250" y1="137" x2="250" y2="107" stroke="#0b3d5c"/>

  <text x="430" y="22" text-anchor="middle" font-size="12" font-weight="700" fill="#0b3d5c">Ring</text>
  <circle cx="430" cy="100" r="48" fill="none" stroke="#0b3d5c" stroke-width="3"/>
  <circle cx="430" cy="52" r="8" fill="#c9a227"/>
  <circle cx="478" cy="100" r="8" fill="#c9a227"/>
  <circle cx="430" cy="148" r="8" fill="#c9a227"/>
  <circle cx="382" cy="100" r="8" fill="#c9a227"/>

  <text x="575" y="22" text-anchor="middle" font-size="12" font-weight="700" fill="#0b3d5c">Mesh</text>
  <circle cx="545" cy="60" r="8" fill="#c9a227"/>
  <circle cx="605" cy="60" r="8" fill="#c9a227"/>
  <circle cx="545" cy="140" r="8" fill="#c9a227"/>
  <circle cx="605" cy="140" r="8" fill="#c9a227"/>
  <line x1="545" y1="60" x2="605" y2="60" stroke="#0b3d5c"/>
  <line x1="545" y1="140" x2="605" y2="140" stroke="#0b3d5c"/>
  <line x1="545" y1="60" x2="545" y2="140" stroke="#0b3d5c"/>
  <line x1="605" y1="60" x2="605" y2="140" stroke="#0b3d5c"/>
  <line x1="545" y1="60" x2="605" y2="140" stroke="#0b3d5c"/>
  <line x1="605" y1="60" x2="545" y2="140" stroke="#0b3d5c"/>
''')


def ram_rom():
    return _svg(640, 150, '''
  <rect x="20" y="20" width="280" height="110" rx="8" fill="#e8f4ec" stroke="#2e7d4f" stroke-width="2"/>
  <text x="160" y="48" text-anchor="middle" font-size="16" font-weight="700" fill="#2e7d4f">RAM</text>
  <text x="160" y="72" text-anchor="middle" font-size="12">volatile · read/write</text>
  <text x="160" y="92" text-anchor="middle" font-size="12">holds running programs</text>
  <text x="160" y="112" text-anchor="middle" font-size="12">SRAM / DRAM</text>
  <rect x="340" y="20" width="280" height="110" rx="8" fill="#eef3fb" stroke="#2b5ea7" stroke-width="2"/>
  <text x="480" y="48" text-anchor="middle" font-size="16" font-weight="700" fill="#2b5ea7">ROM</text>
  <text x="480" y="72" text-anchor="middle" font-size="12">non-volatile · mostly read</text>
  <text x="480" y="92" text-anchor="middle" font-size="12">holds BIOS / firmware</text>
  <text x="480" y="112" text-anchor="middle" font-size="12">PROM / EPROM / EEPROM</text>
''')


def process_states():
    return _svg(640, 170, '''
  <circle cx="70" cy="85" r="36" fill="#14557a"/><text x="70" y="90" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">New</text>
  <circle cx="200" cy="85" r="36" fill="#c9a227"/><text x="200" y="90" text-anchor="middle" fill="#1a1404" font-size="12" font-weight="700">Ready</text>
  <circle cx="340" cy="85" r="36" fill="#2e7d4f"/><text x="340" y="90" text-anchor="middle" fill="#fff" font-size="12" font-weight="700">Running</text>
  <circle cx="480" cy="40" r="36" fill="#6b3fa0"/><text x="480" y="45" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">Waiting</text>
  <circle cx="580" cy="120" r="36" fill="#8a5a2a"/><text x="580" y="125" text-anchor="middle" fill="#fff" font-size="11" font-weight="700">Terminated</text>
  <path d="M106 85 H164" stroke="#0b3d5c" stroke-width="2"/>
  <path d="M236 85 H304" stroke="#0b3d5c" stroke-width="2"/>
  <path d="M368 60 Q 410 40 444 40" fill="none" stroke="#0b3d5c" stroke-width="2"/>
  <path d="M460 76 Q 400 130 360 118" fill="none" stroke="#0b3d5c" stroke-width="2"/>
  <path d="M372 100 Q 470 160 548 130" fill="none" stroke="#0b3d5c" stroke-width="2"/>
''')


def simplex_modes():
    return _svg(640, 150, '''
  <text x="80" y="24" font-size="12" font-weight="700" fill="#0b3d5c">Simplex</text>
  <text x="20" y="70" font-size="11">TV broadcast →</text>
  <line x1="130" y1="66" x2="200" y2="66" stroke="#0b3d5c" stroke-width="3"/>
  <text x="80" y="110" font-size="11" fill="#4a5564">one direction only</text>

  <text x="320" y="24" font-size="12" font-weight="700" fill="#0b3d5c">Half duplex</text>
  <text x="250" y="60" font-size="11">Walkie-talkie</text>
  <line x1="250" y1="80" x2="390" y2="80" stroke="#0b3d5c" stroke-width="3"/>
  <text x="250" y="110" font-size="11" fill="#4a5564">both ways, not together</text>

  <text x="530" y="24" font-size="12" font-weight="700" fill="#0b3d5c">Full duplex</text>
  <text x="470" y="60" font-size="11">Telephone</text>
  <line x1="470" y1="72" x2="610" y2="72" stroke="#0b3d5c" stroke-width="3"/>
  <line x1="470" y1="88" x2="610" y2="88" stroke="#c9a227" stroke-width="3"/>
  <text x="470" y="120" font-size="11" fill="#4a5564">both ways at once</text>
''')


def er_library():
    return _svg(640, 180, '''
  <rect x="40" y="50" width="150" height="80" rx="6" fill="#eef3fb" stroke="#2b5ea7" stroke-width="2"/>
  <text x="115" y="78" text-anchor="middle" font-weight="700" fill="#0b3d5c">STUDENT</text>
  <text x="115" y="100" text-anchor="middle" font-size="11">RollNo (PK)</text>
  <text x="115" y="116" text-anchor="middle" font-size="11">Name, Class</text>
  <polygon points="250,90 280,70 310,90 280,110" fill="#fff6d9" stroke="#b8860b" stroke-width="2"/>
  <text x="280" y="94" text-anchor="middle" font-size="10">issues</text>
  <rect x="360" y="50" width="150" height="80" rx="6" fill="#eef3fb" stroke="#2b5ea7" stroke-width="2"/>
  <text x="435" y="78" text-anchor="middle" font-weight="700" fill="#0b3d5c">BOOK</text>
  <text x="435" y="100" text-anchor="middle" font-size="11">ISBN (PK)</text>
  <text x="435" y="116" text-anchor="middle" font-size="11">Title, Author</text>
  <text x="220" y="40" font-size="11">1</text>
  <text x="318" y="40" font-size="11">M</text>
  <line x1="190" y1="90" x2="250" y2="90" stroke="#0b3d5c"/>
  <line x1="310" y1="90" x2="360" y2="90" stroke="#0b3d5c"/>
''')


def class_object():
    return _svg(640, 170, '''
  <rect x="50" y="20" width="200" height="130" rx="8" fill="#0b3d5c"/>
  <text x="150" y="48" text-anchor="middle" fill="#c9a227" font-size="14" font-weight="700">class Student</text>
  <line x1="70" y1="58" x2="230" y2="58" stroke="#c9a227"/>
  <text x="70" y="82" fill="#fff" font-size="12">roll, name, marks</text>
  <text x="70" y="104" fill="#d9e8f2" font-size="12">(data members)</text>
  <text x="70" y="130" fill="#fff" font-size="12">input(), show()</text>
  <text x="280" y="90" font-size="28" fill="#c9a227">⇒</text>
  <rect x="340" y="30" width="120" height="100" rx="8" fill="#e8f4ec" stroke="#2e7d4f" stroke-width="2"/>
  <text x="400" y="58" text-anchor="middle" font-weight="700">obj s1</text>
  <text x="400" y="82" text-anchor="middle" font-size="11">101 Ali 85</text>
  <rect x="480" y="30" width="120" height="100" rx="8" fill="#e8f4ec" stroke="#2e7d4f" stroke-width="2"/>
  <text x="540" y="58" text-anchor="middle" font-weight="700">obj s2</text>
  <text x="540" y="82" text-anchor="middle" font-size="11">102 Sana 91</text>
''')
