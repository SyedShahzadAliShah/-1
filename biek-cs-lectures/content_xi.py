"""Class XI / Computer Science Paper-I lectures (BIEK 2026 pattern)."""

from diagrams import CoverPage, Diagram
from reportlab.platypus import NextPageTemplate, PageBreak, Spacer
from reportlab.lib.units import mm


def add_cover(b, kicker, title, subtitle, bullets, edition):
    b.story.append(CoverPage(kicker, title, subtitle, bullets, edition))
    b.story.append(NextPageTemplate("body"))
    b.story.append(PageBreak())


def build_xi(b):
    add_cover(
        b,
        "Board of Intermediate Education, Karachi",
        "Computer Science XI Lectures  Paper – I",
        "H.S.C. Part I  ·  Science General & Humanities Groups\nTheory 75  +  Practical 25  =  200 (with Paper-II)",
        [
            "Aligned to BIEK Model Paper 2026",
            "Definitions, comparison tables, diagrams",
            "3-mark and detailed answers in board style",
            "Solved 2026 model paper at the end",
        ],
        "Original exam-oriented lecture notes  ·  2026 edition",
    )
    _how_to_use(b)
    _paper_map(b)
    _lec01(b)
    _lec02(b)
    _lec03(b)
    _lec04(b)
    _lec05(b)
    _lec06(b)
    _lec07(b)
    _lec08(b)
    _lec09(b)
    _lec10(b)
    _bank(b)
    _model_2026(b)


def _how_to_use(b):
    b.h1("How to use these lectures")
    b.p(
        "These notes are original teaching material written for students of the Board of "
        "Intermediate Education, Karachi (BIEK). They follow the topics actually asked in "
        "Computer Science Paper–I, including the official Model Paper 2026. They are "
        "<b>not</b> a photocopy of any Sindh Textbook Board book and are <b>not</b> an official BIEK paper."
    )
    b.p("Paper–I is a <b>theory</b> paper. Programming in C / Visual Basic is Paper–II (Class XII).")
    b.h2("Marks you must remember")
    b.table(
        ["Part", "Time", "Marks", "What to do"],
        [
            ["Section A — MCQs", "20 minutes", "15", "OMR sheet. All 15 compulsory."],
            ["Section B — Short", "within 2 h 40 min", "30", "2026 pattern: attempt ALL short parts."],
            ["Section C — Detailed", "within 2 h 40 min", "30", "2026 pattern: attempt ALL long questions (each has OR)."],
            ["Practical", "lab exam", "25", "Assembling, OS, cables, viva, journal."],
        ],
    )
    b.exam_tip(
        "In Model Paper 2026, Section B says <b>answer all parts</b> and Section C says "
        "<b>answer all questions</b>. Older papers allowed choice (attempt 5 of 15, 2 of 3). "
        "Follow the instructions printed on <i>your</i> question paper on exam day."
    )
    b.h2("How examiners award marks")
    b.numbered(
        [
            "Start every answer with a <b>one-line definition</b>.",
            "Then give <b>numbered points</b> (not a long paragraph).",
            "Draw a <b>neat labelled diagram</b> wherever the wording is draw / show / classify.",
            "Comparison questions need a <b>table</b> with at least four differences.",
            "Write full forms when an abbreviation is used (LAN, OSI, BIOS, SMTP).",
        ]
    )
    b.page_break()
    b.h1("Contents — Class XI / Paper–I")
    b.table(
        ["Lecture", "Title", "Use it for"],
        [
            ["1", "IT and introduction to computers", "IT, barcode, types, generations"],
            ["2", "Hardware and I/O devices", "Printers, plotter, hardcopy"],
            ["3", "Memory and storage", "RAM/ROM, GB, secondary storage"],
            ["4", "CPU, registers, buses, fetch cycle", "Section C registers / fetch"],
            ["5", "Software and translators", "Compiler vs interpreter"],
            ["6", "Operating system", "Section C OS functions"],
            ["7", "Data communication", "Channels, modem, signals"],
            ["8", "Networks, topologies, OSI", "OSI diagram, LAN/WAN, devices"],
            ["9", "Internet and data security", "Virus, HTML, SMTP, BIOS"],
            ["10", "Boolean algebra (past papers)", "Gates and DeMorgan"],
            ["11", "MCQ and 3-mark bank", "Last-night drill"],
            ["12", "Solved Model Paper 2026", "Timed mock"],
        ],
    )
    b.page_break()


def _paper_map(b):
    b.h1("Syllabus map for Paper–I")
    b.p(
        "BIEK Paper–I tests computer fundamentals, architecture, software, operating systems, "
        "data communication, networks and security. The 2026 model paper did <b>not</b> ask "
        "Boolean algebra, but many past papers did — Lecture 10 is a short revision of gates."
    )
    b.table(
        ["Lecture", "Topic", "2026 model paper links"],
        [
            ["1", "IT and introduction to computers", "IT uses/abuses; barcode"],
            ["2", "Hardware and I/O devices", "Hardcopy/softcopy; plotter; printers; OMR/OCR"],
            ["3", "Memory and storage", "GB = 1024 MB; magnetic disk; secondary storage (C)"],
            ["4", "CPU, registers, buses, fetch cycle", "Fetch cycle; registers (C); SIMM; bus"],
            ["5", "Software and language translators", "Compiler vs interpreter; GUI"],
            ["6", "Operating system", "OS functions (C)"],
            ["7", "Data communication", "Components; analog/digital; modulation; channels (C)"],
            ["8", "Networks, topologies, OSI", "LAN devices; OSI (C); network types (C)"],
            ["9", "Internet and data security", "Virus; HTML; SMTP; BIOS/CRT/SVGA"],
            ["10", "Boolean algebra (past papers)", "DeMorgan, gates — keep ready"],
        ],
    )
    b.page_break()


def _lec01(b):
    b.chapter_banner("01", "Information Technology and Introduction to Computers", "Paper–I", "Foundation unit")
    b.definition(
        "Computer",
        "A computer is an electronic machine that accepts data (input), processes it according "
        "to instructions, stores the result and produces output. It works on the IPO cycle: "
        "<b>Input → Process → Output</b> (plus storage).",
    )
    b.definition(
        "Information Technology (IT)",
        "Information Technology is the use of computers, networking, software and telecommunication "
        "to collect, process, store, protect and share information.",
    )
    b.add(Diagram("block", 70 * mm))
    b.caption("Figure 1.1  Block diagram of a computer system — draw this in long answers.")

    b.h2("1.1 Characteristics of a computer")
    b.table(
        ["Feature", "Meaning for the exam"],
        [
            ["Speed", "Performs millions of instructions per second."],
            ["Accuracy", "Gives error-free results if the input and program are correct (GIGO)."],
            ["Diligence", "Does not get tired; the 1st and the millionth job are equally accurate."],
            ["Storage", "Stores huge data on primary and secondary memory."],
            ["Versatility", "Same machine can do accounts, design, games, research."],
            ["Automation", "Once programmed, it runs without continuous human help."],
            ["No feelings", "No emotion, no intelligence of its own (unless AI software is used)."],
        ],
    )
    b.h2("1.2 Advantages of computer education")
    b.numbered(
        [
            "Builds career skills for banking, medicine, engineering, media and e-commerce.",
            "Makes office work faster: typing, spreadsheets, presentations, email.",
            "Supports online learning, research and digital libraries.",
            "Helps in data analysis, graphics, CAD and scientific calculation.",
            "Enables communication through internet, video call and social media.",
        ]
    )
    b.h2("1.3 Uses and abuses of IT")
    b.table(
        ["Uses of IT", "Abuses of IT"],
        [
            ["Education: e-learning, LMS, online exams", "Cyberbullying and fake news"],
            ["Health: MRI, patient records, telemedicine", "Theft of medical / personal data"],
            ["Banking: ATM, online transfer, NADRA records", "Hacking, phishing, credit-card fraud"],
            ["Business: inventory, e-commerce, accounts", "Software piracy and copyright theft"],
            ["Government: NADRA, FBR, e-governance", "Surveillance without consent; identity theft"],
        ],
    )
    b.h2("1.4 Types of computers")
    b.h3("According to size")
    b.table(
        ["Type", "Point for 3-mark answer"],
        [
            ["Supercomputer", "Fastest; weather, nuclear research, space (e.g. Cray)."],
            ["Mainframe", "Huge storage; banks, airlines, census; many terminals."],
            ["Minicomputer", "Mid-range; departments and medium organisations."],
            ["Microcomputer / PC", "Single-user: desktop, laptop, tablet, smartphone."],
        ],
    )
    b.h3("According to working principle")
    b.table(
        ["Type", "Data", "Example"],
        [
            ["Analog", "Continuous physical quantities", "Speedometer, analog thermometer"],
            ["Digital", "Discrete 0 and 1", "PC, calculator, digital watch"],
            ["Hybrid", "Mix of analog and digital", "Hospital monitoring, petrol pump"],
        ],
    )
    b.h2("1.5 Generations of computers (quick revision)")
    b.table(
        ["Gen", "Years (approx.)", "Technology", "Language / remark"],
        [
            ["1st", "1940–56", "Vacuum tubes", "Machine language; huge, hot, ENIAC"],
            ["2nd", "1956–63", "Transistors", "Assembly; smaller, more reliable"],
            ["3rd", "1964–71", "ICs", "High-level languages; minicomputers"],
            ["4th", "1971–present", "Microprocessor / VLSI", "PCs, GUI, internet"],
            ["5th", "Present +", "AI, ULSI, NLP", "Robots, expert systems, ML"],
        ],
    )
    b.h2("1.6 Bar code reader")
    b.p(
        "A <b>bar code</b> is a pattern of parallel black and white bars that stores a product "
        "number (usually UPC / EAN). A <b>bar code reader</b> is an optical scanner that reads "
        "this pattern with a laser or camera and converts it into a digital code for the computer."
    )
    b.h3("Use in a superstore")
    b.numbered(
        [
            "Cashier scans the item; price and name appear at once from the database.",
            "Stock quantity is reduced automatically (inventory control).",
            "Billing becomes fast and error-free; no manual price typing.",
            "Sales reports and reorder levels can be generated daily.",
        ]
    )
    b.board_q(
        "What is Information Technology? Write any three uses or abuses of IT. (3 marks)",
        "IT is the use of computers, software and networks to process and share information. "
        "<b>Uses:</b> (i) online banking (ii) e-learning (iii) hospital records. "
        "<b>Abuses:</b> (i) hacking (ii) fake news (iii) software piracy. Write three of either, or a mix, as asked.",
    )
    b.page_break()


def _lec02(b):
    b.chapter_banner("02", "Computer Hardware and Input / Output Devices", "Paper–I", "High-frequency unit")
    b.definition(
        "Hardware",
        "Hardware is the physical, touchable parts of a computer system — keyboard, mouse, "
        "monitor, printer, CPU box, cables and chips.",
    )
    b.definition(
        "Peripheral",
        "A peripheral is any hardware device connected to the CPU to perform input, output "
        "or storage, for example keyboard, printer and USB drive.",
    )
    b.h2("2.1 Classification of hardware")
    b.table(
        ["Class", "Job", "Examples"],
        [
            ["Input", "Enter data / commands", "Keyboard, mouse, scanner, MIC, joystick, OCR, OMR, barcode, webcam, stylus"],
            ["Output", "Show results", "Monitor, printer, plotter, speaker, projector, SGD"],
            ["Processing", "Calculate and control", "CPU (ALU + CU + registers)"],
            ["Storage", "Hold data", "HDD, SSD, USB, SD, CD/DVD, Blu-ray"],
            ["Communication", "Link computers", "NIC, modem, router, switch, hub, gateway"],
        ],
    )
    b.h2("2.2 Input devices you must be able to describe")
    b.table(
        ["Device", "Exam line"],
        [
            ["Keyboard", "Standard QWERTY; alphanumeric, function, numeric and control keys."],
            ["Mouse", "Pointing device; left/right click, scroll; optical or wireless."],
            ["Joystick / joy pad", "Gaming and simulation; stick reports X–Y position."],
            ["Scanner", "Converts paper image into a digital picture (flatbed / handheld)."],
            ["OCR", "Optical Character Recognition — reads printed text into editable type."],
            ["OMR", "Optical Mark Recognition — reads pencil marks on MCQ sheets."],
            ["MICR", "Magnetic Ink Character Recognition — bank cheques."],
            ["Barcode / QR", "Reads product or ticket codes at speed."],
            ["Microphone", "Voice input; used with speech-recognition software."],
            ["Webcam", "Live video for calls and recording."],
            ["Touch screen", "Input + output on the same surface (phones, kiosks)."],
            ["Digitizer / stylus", "Drawing tablets for CAD and graphic design."],
        ],
    )
    b.h2("2.3 Output devices")
    b.h3("Monitors")
    b.table(
        ["Type", "Working idea", "Note"],
        [
            ["CRT", "Electron beam on phosphor screen", "Bulky, old, SVGA common in MCQs"],
            ["LCD", "Liquid crystals + backlight", "Thin, low power"],
            ["LED", "LCD with LED backlight", "Brighter, today's standard"],
            ["Plasma", "Ionised gas cells", "Large TVs, high contrast"],
        ],
    )
    b.p(
        "<b>Softcopy</b> is temporary output on screen or speaker. "
        "<b>Hardcopy</b> is permanent printed output on paper."
    )
    b.h3("Printers")
    b.table(
        ["Impact printers", "Non-impact printers"],
        [
            ["Head hits ribbon / paper", "No striking; spray, heat or laser"],
            ["Noisy", "Quiet"],
            ["Can print carbon copies", "No carbon copies"],
            ["Slower, cheaper (dot matrix, daisy wheel, drum, line)", "Faster (inkjet, laser, thermal)"],
            ["Low print quality (dpi)", "High dpi, graphics and colour"],
        ],
    )
    b.p(
        "Print quality is measured in <b>DPI (dots per inch)</b>. Speed is measured in "
        "<b>CPS, LPM or PPM</b> (characters / lines / pages per minute)."
    )
    b.h3("Plotter")
    b.p(
        "A <b>plotter</b> is an output device that draws high-quality line graphics using pens. "
        "It is used for huge drawings and maps: engineering CAD, architecture, GIS maps, "
        "and banners. Types: <b>drum plotter</b> and <b>flatbed plotter</b>."
    )
    b.h3("Other output")
    b.bullets(
        [
            "<b>Speakers / headphones</b> — sound output.",
            "<b>Multimedia projector</b> — large-screen display for class and meetings.",
            "<b>SGD (Speech Generating Device)</b> — voice output for users who cannot speak.",
        ]
    )
    b.board_q(
        "What are the differences between Hardcopy and Softcopy? (3 marks)",
        "Hardcopy is printed permanent output (paper); softcopy is temporary electronic output (monitor). "
        "Hardcopy needs a printer and can be touched; softcopy needs power and can be edited easily. "
        "Hardcopy is slower to produce; softcopy is instant. Give 3–4 points in a mini-table.",
    )
    b.page_break()


def _lec03(b):
    b.chapter_banner("03", "Computer Memory and Storage", "Paper–I", "MCQ favourite")
    b.definition(
        "Memory",
        "Memory is the computer's storage area that holds data, instructions and results. "
        "It is divided into <b>primary (main)</b> memory inside the system unit and "
        "<b>secondary</b> memory for long-term storage.",
    )
    b.h2("3.1 Memory measurement units")
    b.table(
        ["Unit", "Equals", "Board line"],
        [
            ["Bit", "0 or 1", "Smallest unit of data"],
            ["Nibble", "4 bits", "Half a byte"],
            ["Byte", "8 bits", "Stores one character"],
            ["KB", "1024 bytes", "Kilobyte"],
            ["MB", "1024 KB", "Megabyte"],
            ["GB", "1024 MB", "Gigabyte — 2026 MCQ answer"],
            ["TB", "1024 GB", "Terabyte"],
            ["PB", "1024 TB", "Petabyte"],
        ],
    )
    b.exam_tip(
        "BIEK always uses binary multiples: 1 KB = <b>1024</b> bytes, not 1000. "
        "2026 MCQ: 1 GB = 1024 MB (option C).",
    )
    b.h2("3.2 Primary / main memory")
    b.p(
        "<b>Volatile</b> memory loses contents when power is off. "
        "<b>Non-volatile</b> memory keeps contents without power."
    )
    b.table(
        ["RAM", "ROM"],
        [
            ["Random Access Memory", "Read Only Memory"],
            ["Volatile", "Non-volatile"],
            ["Read and write", "Usually read only (programmed once or rarely)"],
            ["Holds running programs and data", "Holds firmware / BIOS"],
            ["Faster access; measured in GB today", "Smaller; measured in MB"],
            ["Types: SRAM, DRAM", "Types: PROM, EPROM, EEPROM, Flash"],
        ],
    )
    b.h3("RAM types")
    b.bullets(
        [
            "<b>SRAM (Static RAM)</b> — uses flip-flops; faster; no refresh; used as cache; expensive.",
            "<b>DRAM (Dynamic RAM)</b> — uses capacitors; needs refresh; cheaper; used as main memory.",
            "<b>SIMM</b> — Single Inline Memory Module (32-bit). <b>DIMM</b> — Dual Inline Memory Module (64-bit).",
        ]
    )
    b.h3("ROM types")
    b.table(
        ["Type", "Can be erased?", "How"],
        [
            ["ROM (mask)", "No", "Written at factory"],
            ["PROM", "No (once only)", "Programmed by user with a PROM burner"],
            ["EPROM", "Yes", "Ultraviolet light through a quartz window"],
            ["EEPROM", "Yes", "Electrically, byte-wise"],
            ["Flash", "Yes", "Electrically, in blocks — USB, BIOS, SSD"],
        ],
    )
    b.h2("3.3 Cache memory")
    b.p(
        "Cache is a small, very fast SRAM between the CPU and RAM. It stores the data and "
        "instructions the CPU is most likely to need next. Levels: <b>L1</b> (inside core, smallest, fastest), "
        "<b>L2</b>, <b>L3</b> (shared). Cache increases processing speed."
    )
    b.h2("3.4 Secondary storage")
    b.table(
        ["Device", "Technology", "Exam points"],
        [
            ["Hard disk (HDD)", "Magnetic disk", "Platters, tracks, sectors, heads; random access; large GB/TB"],
            ["Floppy disk", "Magnetic disk", "Obsolete 1.44 MB; still appears in MCQs"],
            ["Magnetic tape", "Magnetic sequential", "Backup; cheap; slow sequential access"],
            ["CD", "Optical", "700 MB; CD-ROM / CD-R / CD-RW"],
            ["DVD", "Optical", "4.7 GB+; movies and software"],
            ["Blu-ray", "Optical (blue laser)", "25 GB+ per layer"],
            ["USB / flash / pen drive", "Flash EEPROM", "Portable, non-volatile, hot-pluggable"],
            ["SD / microSD", "Flash", "Cameras, phones"],
            ["SSD / external HDD", "Flash / magnetic", "Fast boot (SSD); backup (external)"],
        ],
    )
    b.p(
        "Access methods: <b>Sequential</b> (tape — start from the beginning) and "
        "<b>Direct / random</b> (disk, USB — jump to any address)."
    )
    b.board_q(
        "Explain secondary storage devices with examples. (detailed)",
        "Define secondary storage as non-volatile, large, cheaper memory used when the computer is off. "
        "Then describe at least four devices with one example each: HDD, optical discs, flash/USB, magnetic tape. "
        "Add a comparison: slower than RAM, larger capacity, used for backup and files.",
    )
    b.page_break()


def _lec04(b):
    b.chapter_banner("04", "Inside the System Unit — CPU, Registers, Buses, Fetch Cycle", "Paper–I", "Section C favourite")
    b.definition(
        "System unit",
        "The system unit (CPU cabinet / chassis) is the box that houses the motherboard, "
        "power supply, processor, RAM, storage drives, cooling fans and ports.",
    )
    b.h2("4.1 Parts of the system unit")
    b.bullets(
        [
            "<b>Power supply (SMPS)</b> — converts 220 V AC to 12 V / 5 V / 3.3 V DC.",
            "<b>Motherboard</b> — main printed circuit board; everything plugs into it.",
            "<b>Microprocessor</b> — the CPU chip in the socket.",
            "<b>RAM slots</b> — SIMM / DIMM modules.",
            "<b>BIOS ROM</b> — firmware that tests hardware and starts the OS (POST).",
            "<b>CMOS battery</b> — keeps date, time and BIOS settings.",
            "<b>Expansion slots</b> — PCI, PCIe (older papers also mention EISA).",
            "<b>Ports</b> — USB, HDMI, VGA, audio, Ethernet, serial, parallel.",
            "<b>Cooling</b> — heat sink and fan; laptop heat pipes.",
            "<b>Drives</b> — HDD / SSD / optical combo drive.",
        ]
    )
    b.add(Diagram("cpu", 58 * mm))
    b.caption("Figure 4.1  Internal view of the microprocessor.")
    b.h2("4.2 CPU = ALU + CU + Registers")
    b.p(
        "The <b>Central Processing Unit</b> is the brain of the computer. "
        "It fetches instructions from memory, decodes them and executes them."
    )
    b.table(
        ["Part", "Function"],
        [
            ["ALU", "Arithmetic (+ − × ÷) and logic (AND OR NOT compare) operations."],
            ["CU", "Controls and coordinates all parts; generates timing and control signals."],
            ["Registers", "Very fast storage cells inside the CPU for data, addresses and instructions."],
            ["Clock", "Crystal oscillator; speed in GHz; one cycle = one basic tick."],
            ["Cache", "On-chip fast memory for hot data."],
        ],
    )
    b.h2("4.3 Computer registers (draw and explain)")
    b.definition(
        "Register",
        "A register is a small, high-speed storage location inside the CPU that holds data, "
        "an instruction or an address during processing. Registers are faster than cache and RAM.",
    )
    b.table(
        ["Register", "Full form / role"],
        [
            ["AC / Accumulator", "Holds the result of ALU operations."],
            ["PC / Program Counter", "Holds the address of the <b>next</b> instruction."],
            ["IR / Instruction Register", "Holds the instruction currently being executed."],
            ["MAR / Memory Address Register", "Holds the address of the memory cell to be accessed."],
            ["MDR / MBR", "Memory Data / Buffer Register — data going to or from memory."],
            ["SP / Stack Pointer", "Address of the top of the stack."],
            ["Flag / Status", "Bits that show zero, carry, sign, overflow after ALU work."],
            ["Index / General purpose", "AX, BX, CX, DX in Intel-style papers — temporary data."],
        ],
    )
    b.h2("4.4 Fetch cycle (instruction cycle)")
    b.add(Diagram("fetch", 52 * mm))
    b.caption("Figure 4.2  Instruction cycle — 2026 short question: 'What is fetch Cycle? Draw its diagram.'")
    b.numbered(
        [
            "<b>Fetch:</b> PC gives address to MAR. Instruction is copied from memory to MDR, then to IR. PC is incremented.",
            "<b>Decode:</b> CU reads IR and decides which operation and which operands.",
            "<b>Execute:</b> ALU or CU carries out the operation (add, move, jump, I/O).",
            "<b>Store / Write-back:</b> Result is written to a register or memory if needed.",
        ]
    )
    b.h2("4.5 Buses")
    b.definition(
        "Bus",
        "A bus is a shared electrical pathway that carries data, addresses and control signals "
        "between the CPU, memory and I/O devices.",
    )
    b.table(
        ["Bus", "Carries", "Direction"],
        [
            ["Data bus", "Actual data and instructions", "Bi-directional"],
            ["Address bus", "Memory / I/O addresses", "Uni-directional (CPU → memory)"],
            ["Control bus", "Read, write, interrupt, clock, reset", "Mostly uni-directional from CU"],
        ],
    )
    b.p("Bus <b>width</b> (8, 16, 32, 64 bit) decides how many bits travel together. Wider bus = faster transfer.")
    b.h2("4.6 Ports")
    b.table(
        ["Port", "Use"],
        [
            ["Serial", "One bit at a time; old mouse/modem (RS-232)."],
            ["Parallel", "Byte at a time; old printers (Centronics)."],
            ["USB", "Universal Serial Bus — hot plug, keyboards, disks, 2.0/3.x/C."],
            ["HDMI", "High-Definition Multimedia Interface — digital video + audio."],
            ["VGA", "Analog video to CRT/old monitors (appears as SVGA in MCQs)."],
        ],
    )
    b.board_q(
        "What is Computer Register? Explain its types. (detailed)",
        "Define register. Explain at least five: AC, PC, IR, MAR, MDR with one line each. "
        "Add: registers are inside CPU, faster than RAM, measured in bits (16/32/64). Draw a small CPU diagram showing registers.",
    )
    b.page_break()


def _lec05(b):
    b.chapter_banner("05", "Computer Software and Language Translators", "Paper–I", "Definitions + compiler/interpreter")
    b.definition(
        "Software",
        "Software is a set of programs, procedures and documentation that tells the hardware "
        "what to do. It is intangible — you cannot touch it.",
    )
    b.h2("5.1 Types of software")
    b.table(
        ["Type", "Job", "Examples"],
        [
            ["System software", "Controls hardware and provides a platform", "OS, device drivers, BIOS, translators"],
            ["Application software", "Solves user tasks", "Word, Excel, Chrome, Photoshop, games"],
            ["Utility software", "Housekeeping / maintenance", "Antivirus, zip, backup, disk defrag, recovery"],
        ],
    )
    b.h3("Application software")
    b.bullets(
        [
            "<b>General purpose</b> — used in many fields: word processor, spreadsheet, DBMS, browser, presentation.",
            "<b>Special purpose</b> — written for one job: airline reservation, hospital LIS, NADRA software, ATM software.",
        ]
    )
    b.h2("5.2 Language translators")
    b.definition(
        "Language translator",
        "A translator is system software that converts a program written in a programming "
        "language into machine language (0s and 1s) that the CPU can execute.",
    )
    b.table(
        ["Translator", "Converts", "How it works"],
        [
            ["Assembler", "Assembly → machine", "One-to-one mnemonic translation"],
            ["Compiler", "High-level → machine (object code)", "Translates the <b>whole program</b> first, then runs"],
            ["Interpreter", "High-level → machine", "Translates and executes <b>line by line</b>"],
        ]
    )
    b.h3("Compiler is more efficient than interpreter — 2026 question")
    b.numbered(
        [
            "Compiler translates the program once; later runs are at full machine speed. Interpreter re-translates every run.",
            "Compiled object code can be saved and distributed without source. Interpreted programs need the interpreter present.",
            "Compilers perform global optimisation; interpreters generally do not.",
            "After compilation, execution does not stop at each line, so run-time is faster.",
            "Note: interpreters are easier for beginners (immediate error on the current line). Mention this as a contrast.",
        ]
    )
    b.h2("5.3 Programming language levels")
    b.table(
        ["Level", "Example", "Point"],
        [
            ["Machine", "01001101", "CPU native; difficult for humans"],
            ["Assembly", "MOV AX, 5", "Mnemonics; needs assembler"],
            ["High-level", "C, Java, Python, VB", "English-like; needs compiler/interpreter"],
            ["4GL / query", "SQL", "What to do, not how"],
        ],
    )
    b.h2("5.4 Device drivers and firmware")
    b.bullets(
        [
            "<b>Device driver</b> — small program that lets the OS talk to a specific hardware device (printer, GPU, NIC).",
            "<b>Firmware / BIOS</b> — software stored in ROM/flash on the board; runs POST and locates the boot device.",
            "<b>Anti-malware</b> — antivirus, anti-Trojan; scans and quarantines malicious programs.",
        ]
    )
    b.page_break()


def _lec06(b):
    b.chapter_banner("06", "Operating System", "Paper–I", "Almost every year in Section C")
    b.definition(
        "Operating system",
        "An operating system is system software that manages computer hardware and software "
        "resources and provides a platform on which application programs run. It is the "
        "interface between the user and the hardware.",
    )
    b.p("Common OS: <b>Windows, macOS, Linux/UNIX, DOS, Android, iOS</b>.")
    b.h2("6.1 Objectives of an OS")
    b.numbered(
        [
            "Make the computer convenient to use (GUI / commands).",
            "Use CPU, memory and devices efficiently.",
            "Provide security and access control.",
            "Hide hardware details from the user (abstraction).",
            "Allow many programs / users to share the machine fairly.",
        ]
    )
    b.h2("6.2 Functions of an OS (write these in the long question)")
    b.table(
        ["Function", "What the OS does"],
        [
            ["Booting", "Loads itself from disk into RAM after BIOS POST (cold / warm boot)."],
            ["Process management", "Creates, schedules, suspends and terminates processes; CPU scheduling."],
            ["Memory management", "Allocates and frees RAM; virtual memory / paging."],
            ["File management", "Creates folders, keeps FAT/NTFS directories, access rights."],
            ["I/O / device management", "Talks to devices through drivers; spooling for printer."],
            ["Secondary storage management", "Disk space, partitions, defragmentation."],
            ["Network management", "TCP/IP stack, sharing, user login on LAN."],
            ["Security / protection", "Passwords, permissions, firewall hooks."],
            ["Command interpreter / GUI", "CMD, PowerShell, bash, or icons and windows."],
            ["Error detection", "Reports disk fail, no paper, invalid instruction."],
        ],
    )
    b.h2("6.3 Types / features of OS")
    b.table(
        ["Type", "Idea", "Example"],
        [
            ["Batch", "Jobs collected, run without user sitting there", "Old payroll jobs"],
            ["Multi-tasking", "Several programs in memory; CPU switches fast", "Windows, Linux"],
            ["Time-sharing", "CPU time slices among many users", "UNIX lab servers"],
            ["Multi-processing", "Two or more CPUs / cores share jobs", "Modern PCs"],
            ["Parallel", "Many processors on one task", "Scientific clusters"],
            ["Distributed", "Many computers appear as one system", "Google data centres"],
            ["Embedded / real-time", "Inside a device; strict time limits", "ATM, car ABS, Android TV"],
            ["Single-user", "One person", "MS-DOS, home Windows"],
            ["Multi-user", "Many logins", "Linux server, mainframe"],
        ],
    )
    b.h2("6.4 Process and its states")
    b.definition(
        "Process",
        "A process is a program in execution. It includes the code, data, stack and the current register values (PCB).",
    )
    b.bullets(
        [
            "<b>New</b> — being created.",
            "<b>Ready</b> — waiting for CPU.",
            "<b>Running</b> — using the CPU.",
            "<b>Waiting / blocked</b> — waiting for I/O or an event.",
            "<b>Terminated</b> — finished or killed.",
        ]
    )
    b.p(
        "<b>Thread</b> is a lightweight sub-process that shares the same memory space. "
        "<b>Multi-threading</b> = many threads in one process. "
        "<b>Multi-tasking</b> = many processes on one OS."
    )
    b.h2("6.5 GUI vs CLI")
    b.table(
        ["GUI (Graphical User Interface)", "CLI (Command Line Interface)"],
        [
            ["Icons, windows, menus, pointer", "Typed commands"],
            ["Easy for beginners", "Faster for experts / scripts"],
            ["Windows, macOS, GNOME", "DOS, bash, PowerShell"],
        ],
    )
    b.p(
        "Useful Windows tools that appear in practicals: "
        "<b>Control Panel</b>, file attributes (R/H/S/A), search, "
        "<b>msconfig</b> (startup), <b>dxdiag</b> (DirectX / hardware report)."
    )
    b.board_q(
        "What is an Operating System? Explain its functions. (detailed — 2026 Q.3)",
        "Write the definition, name 2–3 examples, then explain 8 functions from the table with one sentence each. "
        "A small labelled diagram 'User → OS → Hardware' scores extra. This is the safest Section C choice.",
    )
    b.page_break()


def _lec07(b):
    b.chapter_banner("07", "Data Communication", "Paper–I", "Heavy in 2026 model paper")
    b.definition(
        "Data communication",
        "Data communication is the exchange of digital or analog data between two or more "
        "devices through a transmission medium and following a set of rules called a protocol.",
    )
    b.h2("7.1 Components of data communication (2026 short question)")
    b.table(
        ["Component", "Role"],
        [
            ["Sender / source", "Device that sends the message (computer, phone)."],
            ["Receiver / destination", "Device that accepts the message."],
            ["Message", "The information: text, number, picture, audio, video."],
            ["Medium / channel", "Path: wire, fibre, radio, microwave, satellite."],
            ["Protocol", "Agreed rules of communication (TCP/IP, HTTP, SMTP)."],
        ]
    )
    b.h2("7.2 Analog vs digital signals")
    b.table(
        ["Analog", "Digital"],
        [
            ["Continuous wave; infinite values", "Discrete; only 0 and 1"],
            ["Sine wave", "Square wave"],
            ["Human voice on telephone line", "Computer data"],
            ["Easily affected by noise", "More noise-resistant; can be regenerated"],
            ["Measured in frequency (Hz)", "Measured in bit rate (bps)"],
        ],
    )
    b.h2("7.3 Communication modes (data flow direction)")
    b.add(Diagram("modes", 55 * mm))
    b.caption("Figure 7.1  Simplex, half duplex and full duplex.")
    b.table(
        ["Mode", "Direction", "Example"],
        [
            ["Simplex", "One way only", "Keyboard → CPU, radio broadcast, monitor"],
            ["Half duplex", "Both ways, not at the same time", "Walkie-talkie, old hub Ethernet"],
            ["Full duplex", "Both ways at the same time", "Telephone, modern switched Ethernet"],
        ],
    )
    b.exam_tip(
        "2026 MCQ: 'two directions but not simultaneously' = <b>Half duplex</b>. "
        "Do not confuse with full duplex.",
    )
    b.h2("7.4 Serial vs parallel; sync vs async")
    b.table(
        ["Serial", "Parallel"],
        [
            ["Bits travel one after another on one wire", "A group of bits travel together on many wires"],
            ["USB, SATA, Ethernet", "Old printer port, internal CPU buses"],
            ["Good for long distance", "Good for short distance, high speed internally"],
        ],
    )
    b.table(
        ["Synchronous", "Asynchronous"],
        [
            ["Sender and receiver share a clock", "No shared clock; each byte has start/stop bits"],
            ["Data sent as a continuous block / frames", "Data sent character by character"],
            ["Higher speed; used in networks", "Lower speed; old serial terminals, some keyboards"],
            ["Idle time is filled with idle sync bits", "Gap between characters is allowed"],
        ],
    )
    b.h2("7.5 Transmission media / channels (2026 Section C)")
    b.h3("Guided (wired)")
    b.table(
        ["Medium", "Construction", "Use / limit"],
        [
            ["Twisted pair (UTP/STP)", "Copper pairs twisted to cut noise; Cat5e/Cat6", "LAN, telephone; ~100 m; cheapest"],
            ["Coaxial", "Core, insulation, metal shield, jacket", "Cable TV, older LAN; better shield"],
            ["Fibre optic", "Glass/plastic core; light pulses", "Backbone, sea cables; fastest, no EMI, costly"],
        ],
    )
    b.h3("Unguided (wireless)")
    b.table(
        ["Medium", "Point"],
        [
            ["Radio waves", "Omnidirectional; AM/FM, Wi-Fi, Bluetooth, cellular"],
            ["Microwave", "Line of sight; dishes on towers; 1–30 GHz"],
            ["Infrared", "Short range, cannot cross walls; TV remote, old IrDA"],
            ["Satellite", "GEO/MEO/LEO; TV, GPS, remote areas"],
        ],
    )
    b.h2("7.6 Modulation, demodulation and modem")
    b.add(Diagram("modem", 48 * mm))
    b.caption("Figure 7.2  Role of a modem.")
    b.definition(
        "Modulation",
        "Modulation is converting a digital signal into an analog signal so that it can travel "
        "on an analog telephone line or radio wave. Methods: AM, FM, PM (amplitude, frequency, phase).",
    )
    b.definition(
        "Demodulation",
        "Demodulation is converting the received analog signal back into digital form for the computer.",
    )
    b.p(
        "<b>Modem</b> = <b>Mo</b>dulator + <b>Dem</b>odulator. "
        "It sits between a digital computer and an analog line."
    )
    b.exam_tip(
        "Standard theory: digital→analog = modulation; analog→digital = demodulation. "
        "Some old MCQs wrongly label analog→digital as modulation. On the paper, pick the option "
        "that matches <b>your textbook wording</b> if two options fight; otherwise use the standard definition. "
        "The 2026 MCQ wording 'analog signal to digital signal' is demodulation / ADC — not modulation.",
    )
    b.h2("7.7 Broadcast vs point-to-point")
    b.table(
        ["Broadcast", "Point-to-point"],
        [
            ["One sender, many receivers on a shared medium", "Dedicated link between two nodes"],
            ["Radio, TV, bus network, Wi-Fi beacon", "Telephone call, PPP, most router links"],
            ["Address may be 'all stations'", "Only the two ends see the data"],
        ],
    )
    b.h2("7.8 Coding schemes (short notes)")
    b.bullets(
        [
            "<b>ASCII</b> — American Standard Code for Information Interchange; 7-bit (128 characters), extended 8-bit.",
            "<b>EBCDIC</b> — Extended Binary Coded Decimal Interchange Code; 8-bit; IBM mainframes.",
            "<b>BCD</b> — Binary Coded Decimal; each decimal digit stored in 4 bits.",
            "<b>Unicode / UTF-8</b> — world languages including Urdu (not always in old papers).",
        ]
    )
    b.page_break()


def _lec08(b):
    b.chapter_banner("08", "Computer Networks, Devices, Topologies and OSI", "Paper–I", "Highest Section C weight")
    b.definition(
        "Computer network",
        "A computer network is a collection of two or more computers and devices connected "
        "by a medium so that they can share data, hardware and software, following protocols.",
    )
    b.h2("8.1 Advantages of networking")
    b.numbered(
        [
            "Resource sharing — printers, files, internet.",
            "Communication — email, chat, video.",
            "Central backup and security control.",
            "Cheaper than giving every user a full set of peripherals.",
            "Distributed processing and remote work.",
        ]
    )
    b.h2("8.2 Types of networks by scale (2026 Section C)")
    b.table(
        ["Type", "Span", "Limitation / note"],
        [
            ["PAN", "A few metres (Bluetooth, USB)", "Personal devices only"],
            ["LAN", "Room, building, campus", "Privately owned; high speed; limited distance"],
            ["MAN", "A city (cable TV, campus city-wide)", "Costly infrastructure; municipal scale"],
            ["WAN", "Country / world (internet)", "Lower speed than LAN; uses telecom / satellite; public or leased"],
            ["Internet", "Network of networks", "Needs ISP, TCP/IP, global addressing"],
            ["Intranet", "Private TCP/IP network of an organisation", "Staff only; may use internet technology internally"],
            ["Extranet", "Intranet opened to partners", "Suppliers / customers with login"],
        ],
    )
    b.h2("8.3 Network topologies")
    b.add(Diagram("bus", 48 * mm))
    b.caption("Figure 8.1  Bus topology — cheapest; one backbone; terminators required. 2026 MCQ.")
    b.add(Diagram("star", 58 * mm))
    b.caption("Figure 8.2  Star topology — each node to a hub/switch; easy fault finding.")
    b.add(Diagram("ring", 55 * mm))
    b.caption("Figure 8.3  Ring topology — token passing; a break can stop the ring (unless dual ring).")
    b.add(Diagram("mesh", 55 * mm))
    b.caption("Figure 8.4  Mesh — every node linked to many others; most reliable, most cables.")
    b.table(
        ["Topology", "Plus", "Minus"],
        [
            ["Bus", "Cheap, short cable", "Collision; backbone break kills all; hard to find fault"],
            ["Star", "Easy add/remove; one cable fault affects one PC", "Central hub/switch failure kills all; more cable"],
            ["Ring", "Fair access (token)", "A cut can stop network; harder to reconfigure"],
            ["Mesh", "No single point of failure", "Expensive; complex"],
            ["Tree / hybrid", "Fits buildings with many floors", "Depends on the mix"],
        ],
    )
    b.h2("8.4 Network devices (LAN components)")
    b.table(
        ["Device", "Layer (OSI)", "Job in one line"],
        [
            ["NIC", "1–2", "Card that gives a computer a MAC address and connects to the medium"],
            ["Repeater", "1", "Regenerates weak analog/digital signals over long cable"],
            ["Hub", "1", "Broadcasts bits to all ports (old, collisions)"],
            ["Switch", "2", "Forwards frames using MAC table — today's LAN centre"],
            ["Bridge", "2", "Connects two <b>similar</b> LANs / segments (2026 MCQ)"],
            ["Router", "3", "Connects different networks using IP; chooses path"],
            ["Gateway", "4–7", "Connects two <b>different</b> networks / protocols (2026 short Q)"],
            ["Modem", "1", "Digital ↔ analog for telephone / cable line"],
            ["Access point", "1–2", "Wi-Fi radio that joins wireless clients to a LAN"],
        ],
    )
    b.exam_tip(
        "Memorise this pair: <b>Bridge = two similar networks</b>. "
        "<b>Gateway = two different networks / protocols</b>. "
        "Router connects different IP networks. Switch is inside one LAN.",
    )
    b.h2("8.5 OSI reference model (2026 Section C — draw and explain)")
    b.definition(
        "OSI",
        "OSI (Open Systems Interconnection) is a seven-layer reference model published by ISO "
        "that describes how data travels from one application to another across a network.",
    )
    b.add(Diagram("osi", 85 * mm))
    b.caption("Figure 8.5  ISO-OSI seven layers. Always draw this stack in the long answer.")
    b.p("Memory sentence: <b>Please Do Not Throw Sausage Pizza Away</b> (Physical → Application) or the reverse <b>All People Seem To Need Data Processing</b>.")
    b.h3("What each layer does (write 2 lines each in Section C)")
    b.numbered(
        [
            "<b>Physical:</b> bits on wire/radio; voltage, fibre, connectors, hubs, repeaters.",
            "<b>Data link:</b> frames, MAC addresses, error detection, switches, NIC.",
            "<b>Network:</b> logical IP addressing and routing; routers; best path.",
            "<b>Transport:</b> end-to-end reliability (TCP) or fast datagrams (UDP); port numbers.",
            "<b>Session:</b> start, manage and close a dialogue between applications.",
            "<b>Presentation:</b> format, encryption, compression (SSL/TLS often discussed here).",
            "<b>Application:</b> services the user sees — HTTP, SMTP, FTP, DNS, Telnet.",
        ]
    )
    b.h2("8.6 TCP/IP model (short)")
    b.table(
        ["TCP/IP layer", "Close OSI layers", "Examples"],
        [
            ["Application", "5, 6, 7", "HTTP, SMTP, FTP, DNS"],
            ["Transport", "4", "TCP, UDP"],
            ["Internet", "3", "IP, ICMP, ARP"],
            ["Network access / link", "1, 2", "Ethernet, Wi-Fi"],
        ],
    )
    b.p("<b>TCP/IP</b> is the protocol suite of the internet. <b>IP</b> delivers packets; <b>TCP</b> makes the stream reliable.")
    b.h2("8.7 Standards bodies")
    b.bullets(
        [
            "<b>ISO</b> — International Organization for Standardization (OSI model).",
            "<b>IEEE</b> — Institute of Electrical and Electronics Engineers (802.3 Ethernet, 802.11 Wi-Fi).",
            "<b>ITU</b> — International Telecommunication Union (phone and radio standards).",
            "<b>IANA / ICANN</b> — IP addresses and domain names (extra).",
        ]
    )
    b.page_break()


def _lec09(b):
    b.chapter_banner("09", "Internet, Email and Data Security", "Paper–I", "Virus, HTML, SMTP, BIOS")
    b.definition(
        "Internet",
        "The internet is a worldwide public network of networks that uses the TCP/IP protocol "
        "suite to share information and services.",
    )
    b.definition(
        "Intranet",
        "An intranet is a private network that uses internet technologies (browsers, HTTP, email) "
        "but is available only inside an organisation.",
    )
    b.h2("9.1 Important internet terms")
    b.table(
        ["Term", "Full form / meaning"],
        [
            ["WWW", "World Wide Web — linked hypertext documents viewed in a browser"],
            ["URL", "Uniform Resource Locator — address of a web resource"],
            ["HTML", "HyperText Markup Language — language of web pages (2026 MCQ)"],
            ["HTTP / HTTPS", "HyperText Transfer Protocol (Secure)"],
            ["ISP", "Internet Service Provider"],
            ["DNS", "Domain Name System — name to IP"],
            ["FTP", "File Transfer Protocol"],
            ["SMTP", "Simple Mail Transfer Protocol — sending email (2026 MCQ)"],
            ["POP3 / IMAP", "Receiving email from a mailbox"],
            ["IP address", "Logical 32-bit (IPv4) or 128-bit (IPv6) host identity"],
            ["MAC address", "48-bit burned-in NIC identity"],
        ],
    )
    b.h2("9.2 Email")
    b.p(
        "Electronic mail sends messages to a mailbox over a data network. "
        "A message has From, To, Subject, body and optional attachment. "
        "Sending uses <b>SMTP</b>; receiving uses <b>POP3 or IMAP</b>."
    )
    b.h2("9.3 Computer virus and other malware")
    b.definition(
        "Computer virus",
        "A computer virus is a malicious program that attaches itself to other programs or documents, "
        "replicates, and can damage files, slow the system or steal data. It is <b>software</b>, not hardware "
        "(2026 MCQ).",
    )
    b.table(
        ["Malware", "Behaviour"],
        [
            ["Virus", "Needs a host file; spreads when the host is copied / run"],
            ["Worm", "Spreads by itself over a network"],
            ["Trojan horse", "Looks useful, hides a harmful payload; does not self-replicate"],
            ["Spyware / keylogger", "Steals passwords and activity"],
            ["Ransomware", "Encrypts files and demands money"],
            ["Time bomb / logic bomb", "Triggers on a date or condition"],
        ],
    )
    b.h3("Antivirus examples (write any five)")
    b.p(
        "Norton, McAfee, Kaspersky, Avast, AVG, Bitdefender, Windows Defender, Avira, ESET NOD32, "
        "Quick Heal. Use keeps definitions <b>updated</b>."
    )
    b.h2("9.4 Protection methods")
    b.numbered(
        [
            "Install and update antivirus / anti-malware.",
            "Use a <b>firewall</b> — hardware or software that filters packets between a trusted LAN and the internet.",
            "Strong passwords and two-factor authentication.",
            "Do not open unknown attachments; beware phishing.",
            "Keep OS and browsers patched; take backups.",
            "A <b>proxy</b> server can hide internal IPs and filter web content.",
        ]
    )
    b.h2("9.5 Full forms drill (2026 Q.2 x)")
    b.table(
        ["Abbrev.", "Full form"],
        [
            ["OCR", "Optical Character Recognition"],
            ["OMR", "Optical Mark Recognition"],
            ["MICR", "Magnetic Ink Character Recognition"],
            ["GUI", "Graphical User Interface"],
            ["CLI", "Command Line Interface"],
            ["CRT", "Cathode Ray Tube"],
            ["LCD / LED", "Liquid Crystal Display / Light Emitting Diode"],
            ["SVGA", "Super Video Graphics Array"],
            ["BIOS", "Basic Input Output System"],
            ["POST", "Power On Self Test"],
            ["USB", "Universal Serial Bus"],
            ["HDMI", "High-Definition Multimedia Interface"],
            ["SIMM", "Single Inline Memory Module"],
        ],
    )
    b.page_break()


def _lec10(b):
    b.chapter_banner("10", "Boolean Algebra and Logic Gates (past-paper revision)", "Paper–I", "Not in 2026 model; common earlier")
    b.p(
        "Model Paper 2026 did not include Boolean algebra. Many older BIEK papers did. "
        "Revise this lecture if your college still teaches Chapter 4 of the old book."
    )
    b.definition(
        "Boolean algebra",
        "Boolean algebra is the algebra of logic, developed by George Boole, in which variables "
        "take only two values: TRUE/1 and FALSE/0. It is the basis of digital circuits.",
    )
    b.h2("10.1 Basic operations")
    b.table(
        ["Operation", "Symbol", "Meaning", "Gate"],
        [
            ["AND (product)", "A · B  or  AB", "1 only if all inputs are 1", "AND"],
            ["OR (sum)", "A + B", "1 if any input is 1", "OR"],
            ["NOT (complement)", "A'  or  Ā", "Inverts 0↔1", "NOT"],
            ["NAND", "(AB)'", "AND then NOT", "NAND (universal)"],
            ["NOR", "(A+B)'", "OR then NOT", "NOR (universal)"],
            ["XOR", "A ⊕ B", "1 if inputs differ", "XOR"],
            ["XNOR", "(A ⊕ B)'", "1 if inputs are same", "XNOR"],
        ],
    )
    b.add(Diagram("and", 50 * mm))
    b.add(Diagram("or", 50 * mm))
    b.add(Diagram("not", 48 * mm))
    b.h2("10.2 Truth tables (memorise)")
    b.table(
        ["A", "B", "AND", "OR", "NAND", "NOR", "XOR"],
        [
            ["0", "0", "0", "0", "1", "1", "0"],
            ["0", "1", "0", "1", "1", "0", "1"],
            ["1", "0", "0", "1", "1", "0", "1"],
            ["1", "1", "1", "1", "0", "0", "0"],
        ],
    )
    b.h2("10.3 Important laws")
    b.table(
        ["Law", "OR form", "AND form"],
        [
            ["Identity", "A + 0 = A", "A · 1 = A"],
            ["Null", "A + 1 = 1", "A · 0 = 0"],
            ["Idempotent", "A + A = A", "A · A = A"],
            ["Complement", "A + A' = 1", "A · A' = 0"],
            ["Commutative", "A + B = B + A", "AB = BA"],
            ["Associative", "(A+B)+C = A+(B+C)", "(AB)C = A(BC)"],
            ["Distributive", "A+BC = (A+B)(A+C)", "A(B+C) = AB+AC"],
            ["Absorption", "A + AB = A", "A(A+B) = A"],
            ["Double complement", "(A')' = A", "—"],
        ],
    )
    b.h3("DeMorgan's theorems (very common)")
    b.numbered(
        [
            "(A + B)' = A' · B'   —  NOT of OR is AND of NOTs.",
            "(A · B)' = A' + B'   —  NOT of AND is OR of NOTs.",
        ]
    )
    b.p("Always show <b>both truth tables</b> and a logic diagram when asked.")
    b.page_break()


def _bank(b):
    b.chapter_banner("11", "MCQ drill and 3-mark bank", "Paper–I", "Practice")
    b.h2("11.1 One-line MCQ facts")
    b.numbered(
        [
            "1 GB = 1024 MB. 1 Byte = 8 bits. 1 Nibble = 4 bits.",
            "Floppy and HDD are magnetic disks (not optical).",
            "SIMM = Single Inline Memory Module.",
            "OSI has seven layers. Cheapest topology is bus.",
            "Virus is software. OMR is a scanning input device.",
            "Bus is the electrical path among devices.",
            "Bridge connects two similar networks; gateway connects different networks.",
            "Coaxial and fibre are communication media.",
            "HTML produces web pages. SMTP is the common email-sending protocol.",
            "Analog → digital for a modem is demodulation. Half duplex = both ways, not together.",
            "ALU = Arithmetic and Logic Unit. BIOS = Basic Input Output System.",
            "Compiler translates the whole program; interpreter line by line.",
            "Laser and inkjet are non-impact; dot matrix is impact.",
            "Plotter prints huge drawings and maps.",
            "TCP/IP is the internet protocol suite. Fast Ethernet is 100 Base-T.",
        ]
    )
    b.h2("11.2 Short questions — write 5–7 lines each")
    shorts = [
        ("Define volatile and non-volatile memory.",
         "Volatile loses data without power (RAM). Non-volatile keeps data (ROM, HDD, flash)."),
        ("What is a protocol?",
         "A protocol is a set of rules for communication (format, timing, error handling). Example: TCP/IP, HTTP, SMTP."),
        ("Differentiate compiler and interpreter.",
         "Compiler: whole program, object file, faster run. Interpreter: line by line, slower run, easier debug."),
        ("What is a gateway?",
         "A gateway connects two networks that use different protocols; it can convert packet formats. It works at higher OSI layers."),
        ("Define LAN and WAN.",
         "LAN covers a building, high speed, private. WAN covers cities/countries, uses telecom, the internet is the largest WAN."),
        ("What is BIOS?",
         "BIOS is firmware in ROM that runs POST, initialises hardware and loads the boot loader / OS."),
        ("Impact vs non-impact printer (four differences).",
         "Use the table in Lecture 2. Always write four rows."),
        ("What is modulation?",
         "Changing digital data into analog form for analog media. Modem performs modulation and demodulation."),
        ("Name five antiviruses.",
         "Norton, Kaspersky, Avast, McAfee, Windows Defender."),
        ("What is cache memory?",
         "Small fast SRAM between CPU and RAM that stores likely-next instructions/data to reduce wait."),
    ]
    for q, a in shorts:
        b.qa(q, a)
    b.page_break()


def _model_2026(b):
    b.chapter_banner("12", "Solved BIEK Model Paper 2026 — Computer Science Paper–I", "Paper–I", "Use as a timed mock")
    b.p(
        "The wording below follows the official Model Paper 2026 (Science General Group). "
        "Answers are original model answers, not copied from any guidebook."
    )
    b.h2("Section A — MCQs (15 × 1 = 15)")
    b.table(
        ["#", "Answer", "Why"],
        [
            ["1", "C) 1024 MB", "1 GB = 1024 MB"],
            ["2", "C) Magnetic Disk", "Floppy and HDD"],
            ["3", "C) Single Inline Memory Module", "SIMM"],
            ["4", "D) seven layers", "OSI"],
            ["5", "B) Bus", "Cheapest topology"],
            ["6", "B) Software", "Virus is a program"],
            ["7", "D) OMR", "Scanning input"],
            ["8", "A) Bus", "Electrical path"],
            ["9", "B) Bridge", "Two similar networks"],
            ["10", "B) Communication Media", "Coax and fibre"],
            ["11", "B) HTML", "Web pages"],
            ["12", "C) SMTP", "Sending email"],
            ["13", "C) Demodulation", "Analog → digital at the modem (see Lecture 7 tip)"],
            ["14", "B) Protocol", "Rules on the internet"],
            ["15", "B) Half duplex", "Both ways, not simultaneous"],
        ],
    )
    b.h2("Section B — Short answers (all parts)")
    b.qa(
        "2(i) What is Information Technology? Write any three uses or abuses of IT.  OR  How can a Bar Code Reader be useful in a superstore?",
        "IT: use of computers and networks to process information. Uses: e-learning, e-banking, telemedicine. "
        "OR Barcode: instant price, automatic stock update, fast error-free billing, sales reports.",
    )
    b.qa(
        "2(ii) Hardcopy vs Softcopy  OR  Synchronous vs Asynchronous transmission",
        "Hardcopy = printed paper; softcopy = screen.  OR  Sync shares a clock and sends blocks; async uses start/stop bits per character.",
    )
    b.qa(
        "2(iii) Define computer virus with examples. Name any five antiviruses.  OR  Devices to print huge drawings or maps.",
        "Virus = malicious self-replicating software (ILOVEYOU, Melissa). Antiviruses: Norton, Kaspersky, Avast, McAfee, Defender. "
        "OR Plotters (drum and flatbed); large-format inkjet for maps.",
    )
    b.qa(
        "2(iv) What is fetch Cycle? Draw its diagram.  OR  Name the components of data communication.",
        "Fetch-decode-execute-(store) as in Figure 4.2.  OR  Sender, receiver, message, medium, protocol.",
    )
    b.qa(
        "2(v) Modulation and Demodulation  OR  How is a Compiler more efficient than Interpreter?",
        "Modulation digital→analog; demodulation analog→digital; modem does both. "
        "OR Compiler translates once to object code so execution is faster; interpreter re-translates every line every run.",
    )
    b.qa(
        "2(vi) Four differences: Impact vs Non-Impact printers.",
        "Strike vs no strike; noisy vs quiet; carbon copies vs none; slower/cheaper vs faster/high dpi. Examples: dot matrix vs laser.",
    )
    b.qa(
        "2(vii) LAN component that allows communication between two different networks.",
        "Gateway (also acceptable in some marking: router if they want IP networks). Best answer: Gateway.",
    )
    b.qa(
        "2(viii) Analog signals vs Digital signals.",
        "Continuous vs discrete; sine vs square; noise-sensitive vs regenerable; voice vs computer data.",
    )
    b.qa(
        "2(ix) Broadcast vs Point-to-Point.",
        "One-to-many shared medium vs dedicated two-end link. Radio vs telephone call.",
    )
    b.qa(
        "2(x) Full form of any three: OCR, GUI, SVGA, CRT, BIOS.",
        "OCR Optical Character Recognition; GUI Graphical User Interface; SVGA Super Video Graphics Array; "
        "CRT Cathode Ray Tube; BIOS Basic Input Output System.",
    )
    b.h2("Section C — Detailed answers")
    b.qa(
        "3. Operating System and its functions  OR  Computer Register and its types",
        "See Lectures 6 and 4. Write definition + 8 functions, or definition + AC, PC, IR, MAR, MDR, flags + diagram.",
    )
    b.qa(
        "4. Data communication channels with examples  OR  Secondary storage devices with examples",
        "See Lectures 7 and 3. Guided (twisted pair, coax, fibre) and unguided (radio, microwave, satellite, infrared) "
        "with one use each.  OR  HDD, optical, flash, tape with properties.",
    )
    b.qa(
        "5. Draw and explain OSI  OR  Computer Network classified by scale and limitation",
        "Draw seven boxes, two lines per layer.  OR  PAN, LAN, MAN, WAN with distance, ownership and speed/cost limits.",
    )
    b.h2("Practical journal — Paper–I related")
    b.numbered(
        [
            "Identify motherboard parts: RAM, CPU fan, SATA, 24-pin power, CMOS battery, PCI slots.",
            "Show BIOS boot order and POST.",
            "Windows: create / copy / rename / delete folders; set Hidden and Read-only attributes.",
            "Control Panel: date/time, mouse, uninstall a program.",
            "Make a straight-through UTP cable (T568B both ends) and a cross-over cable; test with a LAN tester.",
            "Set a static IP, subnet mask and gateway; ping another PC.",
            "Share a folder on LAN.",
        ]
    )
    b.spacer(6)
    b.p(
        "<i>End of Class XI / Paper–I lectures. Continue with the Class XII book for Programming in C "
        "(Option I), Visual Basic (Option II) and DBMS / MS-Access, which BIEK examines in Paper–II.</i>",
        "center",
    )
