"""BIEK Computer Science XI — original lecture content."""

from engine import LectureBuilder


def fill_xi(b: LectureBuilder) -> None:
    b.toc()
    b.h1("How to use these lectures")
    b.p(
        "These notes are original classroom lectures written for students appearing in "
        "HSC Part-I Computer Science from the Board of Intermediate Education, Karachi (BIEK). "
        "They follow the public Sindh Curriculum for Computer Science, Grades XI–XII (2019), "
        "and also include the theory topics that still appear in BIEK Computer Science Paper-I: "
        "Boolean algebra, number systems, data security, and computer architecture."
    )
    b.bullets(
        [
            "Read one unit, then attempt that unit’s short questions without looking at the answers.",
            "Copy every C++ program into Turbo C++ / Dev-C++ / VS Code and run it.",
            "Memorise definitions in the blue boxes; board short questions are often one definition plus two examples.",
            "Use the end-of-book model paper under timed conditions (Section A 30 min, B 90 min, C 60 min).",
        ]
    )
    b.note(
        "These notes are not a photocopy or reconstruction of any commercial textbook. "
        "They are independently written teaching notes aligned to the public curriculum and BIEK paper pattern."
    )

    b.h1("BIEK paper pattern (Computer Science I)")
    b.p(
        "Each HSC part carries 100 marks: 75 theory + 25 practical. The theory paper is three hours. "
        "BIEK’s published scheme for Science General and Humanities (Regular) is:"
    )
    b.table(
        ["Section", "Type", "Time", "Marks", "What you must do"],
        [
            ["A", "MCQs (complete syllabus)", "30 min", "29", "Attempt all 29; 1 mark each"],
            ["B", "Short answers", "90 min", "30", "15 questions given; attempt 10 (3 marks each)"],
            ["C", "Detailed answers", "60 min", "16", "3 questions given; attempt 2 (8 marks each)"],
        ],
        [28, 42, 24, 22, 62],
    )
    b.tip(
        "Section C has no part-questions. Write a full 8-mark answer: definition, classification or diagram, "
        "and at least three explained points. Leave 5 minutes to underline key terms."
    )

    b.h1("Syllabus map")
    b.p(
        "Sindh Curriculum 2019 unit weightages for Grade XI, plus extra BIEK Paper-I topics still asked in Karachi board exams."
    )
    b.table(
        ["Unit", "Title", "Weight", "Why it matters in BIEK"],
        [
            ["1", "Overview of Computer System", "15%", "Definitions, hardware, software, AI/cloud"],
            ["2", "Computer Memory", "10%", "Bit–TB, RAM/ROM families, secondary storage"],
            ["3", "Inside the System Unit", "15%", "Motherboard, CPU, buses, ports, slots"],
            ["4", "Operating System", "10%", "Types, functions, process states, GUI"],
            ["5", "Programming using C++", "20%", "Data types, control, functions, overloading"],
            ["6", "Arrays, Strings, Structures", "15%", "1-D/2-D arrays, string.h, struct"],
            ["7", "Communication & Networks", "15%", "Media, topologies, OSI, TCP/IP"],
            ["A", "Number systems & codes", "extra", "Binary/hex, ASCII, BCD, EBCDIC"],
            ["B", "Boolean algebra & gates", "extra", "Laws, truth tables, De Morgan, K-map idea"],
            ["C", "Data security", "extra", "Virus, firewall, proxy, email safety"],
        ],
        [16, 58, 22, 82],
    )

    _unit1(b)
    _unit2(b)
    _unit3(b)
    _unit4(b)
    _unitA(b)
    _unitB(b)
    _unitC(b)
    _unit5(b)
    _unit6(b)
    _unit7(b)
    _unitD(b)
    _practicals(b)
    _model_paper(b)
    _glossary(b)


def _unit1(b: LectureBuilder) -> None:
    b.h1("Unit 1 — Overview of the Computer System")
    b.p("Curriculum weight 15%. This unit builds the vocabulary used in every later chapter.")

    b.h2("1.1 What is a computer system?")
    b.defn(
        "Computer",
        "An electronic device that accepts data (input), processes it according to stored instructions, "
        "stores results, and produces information (output) with high speed and accuracy.",
    )
    b.defn(
        "Computer system",
        "The complete working combination of hardware, software, data, users (people), and procedures. "
        "A CPU chip alone is not a system; Windows alone is not a system.",
    )
    b.p(
        "IPO model: Input → Process → Output, with Storage feeding the process and holding results. "
        "The stored-program idea (von Neumann) means both data and instructions live in memory."
    )
    b.h3("Block diagram (IPO)")
    b.code(
        """
                    +-----------+      +------------------+      +-----------+
     DATA ------->  |   INPUT   | ---> |     PROCESS      | ---> |  OUTPUT   | ---> INFORMATION
                    |  devices  |      |  (CPU + Memory)  |      |  devices  |
                    +-----------+      +--------+---------+      +-----------+
                                               ^
                                               |  STORAGE (primary + secondary)
""".strip(
            "\n"
        ),
        "Fig. 1.1  Block diagram of a computer system",
    )

    b.h2("1.2 Characteristics")
    b.table(
        ["Feature", "Meaning", "Board example"],
        [
            ["Speed", "Millions of instructions per second", "Payroll of 5,000 employees in seconds"],
            ["Accuracy", "Errors come from humans, not the CPU logic", "Wrong formula in a spreadsheet"],
            ["Diligence", "No tiredness or boredom", "ATM works 24 hours"],
            ["Storage", "Huge data in tiny space", "A 1 TB disk holds a library"],
            ["Versatility", "Same machine, many jobs", "Accounts, games, design"],
            ["Automation", "Runs a stored program without step-by-step human control", "Batch billing"],
        ],
        [32, 72, 74],
    )
    b.p(
        "Limitations you should mention in a long answer: no IQ or common sense, depends on a program, "
        "no feelings, and garbage-in/garbage-out (GIGO)."
    )

    b.h2("1.3 Generations of computers")
    b.table(
        ["Gen.", "Period (approx.)", "Main technology", "Example / note"],
        [
            ["1st", "1940s–1950s", "Vacuum tubes", "ENIAC, UNIVAC; huge, hot, slow"],
            ["2nd", "1950s–1960s", "Transistors", "Smaller, more reliable"],
            ["3rd", "1960s–1970s", "Integrated circuits (IC)", "Minicomputers appear"],
            ["4th", "1970s–present", "Microprocessor (VLSI)", "IBM PC, laptops, smartphones"],
            ["5th", "Present–future", "AI, parallel processing, ULSI", "Expert systems, NLP, robots"],
        ],
        [22, 36, 52, 68],
    )

    b.h2("1.4 Types of computers")
    b.h3("By size / capacity")
    b.bullets(
        [
            "Supercomputer — fastest; weather, nuclear research, climate models (examples: Cray-class machines).",
            "Mainframe — many simultaneous users; banks, airlines, tax systems.",
            "Minicomputer / midrange — department-level servers.",
            "Microcomputer / PC — desktop, laptop, tablet, smartphone.",
            "Workstation — high-end microcomputer for CAD, video, engineering.",
        ]
    )
    b.h3("By purpose / function")
    b.bullets(
        [
            "General purpose — can run many kinds of programs (school PC, office laptop).",
            "Special purpose / dedicated — built for one job (ATM controller, washing-machine MCU, ABS in a car).",
            "Analog — continuous physical quantities (old laboratory instruments).",
            "Digital — discrete 0/1 data (almost all modern computers).",
            "Hybrid — analog plus digital (some hospital monitoring systems).",
        ]
    )

    b.h2("1.5 Hardware classification")
    b.p("Hardware is the physical part you can touch. Classify devices by the job they do.")
    b.table(
        ["Class", "Job", "Examples you must name in exams"],
        [
            ["Input", "Send data into the system", "Keyboard, mouse, scanner, mic, joystick, stylus, webcam, barcode reader, touch screen"],
            ["Output", "Present results", "Monitor (CRT, LCD, LED, plasma), printer, plotter, speaker, projector, SGD"],
            ["Processing", "Transform data", "CPU / microprocessor"],
            ["Storage", "Hold data", "HDD, SSD, USB flash, SD/microSD, CD/DVD/Blu-ray"],
            ["Communication", "Move data between machines", "NIC, modem, router, switch/hub, gateway, fax"],
        ],
        [32, 40, 106],
    )
    b.h3("Printers (favourite short question)")
    b.table(
        ["Type", "How it prints", "Quality / use"],
        [
            ["Dot-matrix (impact)", "Pins strike an ink ribbon", "Carbon copies, noisy, cheap running cost"],
            ["Inkjet (non-impact)", "Sprays liquid ink", "Home photos, colour, clogging risk"],
            ["Laser (non-impact)", "Toner fused by heat", "Offices, high speed, sharp text"],
            ["Plotter", "Pens or inkjet on large paper", "Maps, CAD drawings"],
            ["3D printer", "Adds layers of plastic/resin", "Prototypes (mention as modern extra)"],
        ],
        [40, 52, 86],
    )
    b.defn(
        "Hard copy / Soft copy",
        "Hard copy is printed on paper. Soft copy is displayed on a screen or stored as a file. "
        "A PDF on a USB is still a soft copy until it is printed.",
    )

    b.h2("1.6 Software at a glance")
    b.p(
        "Software is the set of programs and associated data that tell hardware what to do. "
        "Unit 1 only needs the map; later units go deeper."
    )
    b.bullets(
        [
            "System software — OS, device drivers, language translators, anti-malware.",
            "Application software — general purpose (Word, Excel, Chrome) and special purpose (hospital MIS, payroll).",
            "Utility software — compression, backup, disk manager, data recovery.",
        ]
    )

    b.h2("1.7 Cutting-edge topics required by the 2019 curriculum")
    b.defn(
        "Artificial Intelligence (AI)",
        "The branch of computer science that tries to make machines perform tasks that normally need human intelligence: "
        "learning, reasoning, perception, and language.",
    )
    b.p(
        "Applications to quote: medical diagnosis support, face unlock, chatbots, self-driving research, "
        "fraud detection in banks, and recommendation systems. Mention ethics: bias, privacy, job change."
    )
    b.defn(
        "Cloud computing",
        "Delivery of computing resources (servers, storage, databases, software) over the Internet on a pay-as-you-go model, "
        "instead of owning a local data centre.",
    )
    b.bullets(
        [
            "Advantages: lower capital cost, easy scaling, access from anywhere, professional backups.",
            "Examples: Google Drive, Microsoft 365, AWS, college email on Gmail.",
            "Caution: needs a reliable link; sensitive data needs a clear privacy policy.",
        ]
    )

    b.h2("Unit 1 — board practice")
    b.h3("Short questions (3 marks)")
    b.qa(
        "Differentiate hardware and software with two examples each.",
        "Hardware is physical (keyboard, RAM). Software is a set of instructions (Windows, MS Word). "
        "Hardware is visible and wears out; software is intangible and can be copied.",
    )
    b.qa(
        "Why is a computer called a versatile machine?",
        "The same hardware can run many programs — accounts today, video editing tomorrow — because the program, not the wiring, defines the job.",
    )
    b.h3("Long question (8 marks)")
    b.qa(
        "Draw the block diagram of a computer system and explain input, process, output and storage.",
        "Draw Fig. 1.1. Define each box with two device examples. End with IPO + stored program. That structure scores full marks.",
    )
    b.h3("MCQs")
    b.mcqs(
        [
            ("Which generation introduced the microprocessor?", ["1st", "2nd", "3rd", "4th"], "D"),
            ("A plotter is mainly an", ["input device", "output device", "storage device", "OS"], "B"),
            ("GIGO means", ["Good Input Good Output", "Garbage In Garbage Out", "Gate In Gate Out", "None"], "B"),
        ]
    )


def _unit2(b: LectureBuilder) -> None:
    b.h1("Unit 2 — Computer Memory")
    b.p("Curriculum weight 10%. Almost every Paper-I contains one memory MCQ and one short question.")

    b.h2("2.1 Measurement units")
    b.table(
        ["Unit", "Equals", "Board memory aid"],
        [
            ["Bit", "0 or 1", "Smallest unit"],
            ["Nibble", "4 bits", "Half a byte; one hex digit"],
            ["Byte", "8 bits", "One ASCII character"],
            ["KB", "1024 bytes", "About one short email"],
            ["MB", "1024 KB", "A photo or MP3"],
            ["GB", "1024 MB", "A film or a game"],
            ["TB", "1024 GB", "A disk pack / backup drive"],
        ],
        [28, 36, 114],
    )
    b.warn(
        "In board answers always write 1 KB = 1024 bytes, not 1000. Hard-disk marketers use 1000, which is SI, not the exam convention."
    )

    b.h2("2.2 Primary / main memory")
    b.defn(
        "Primary memory",
        "Semiconductor memory the CPU can address directly. It is fast and limited in size. Two families: RAM and ROM.",
    )
    b.table(
        ["Point", "RAM", "ROM"],
        [
            ["Full form", "Random Access Memory", "Read Only Memory"],
            ["Volatility", "Volatile — contents vanish on power-off", "Non-volatile"],
            ["Read/write", "Read and write", "Normally read only"],
            ["Use", "Running programs and data", "Firmware / BIOS"],
            ["Speed", "Very fast", "Fast, but not a working area"],
        ],
        [32, 73, 73],
    )
    b.h3("RAM types")
    b.bullets(
        [
            "SRAM (Static RAM) — flip-flops; no refresh; used as cache; expensive, small.",
            "DRAM (Dynamic RAM) — capacitors; needs refresh; cheap, large; used as main memory.",
        ]
    )
    b.h3("ROM types")
    b.table(
        ["Type", "Can you write after manufacture?", "How to erase"],
        [
            ["Mask ROM", "No", "Cannot"],
            ["PROM", "Once (by programmer)", "Cannot"],
            ["EPROM", "Yes, after erase", "Ultraviolet light through a window"],
            ["EEPROM", "Yes, electrically, byte-wise", "Electric signal"],
            ["Flash", "Yes, in blocks", "Electric; used in BIOS and USB"],
        ],
        [36, 72, 70],
    )

    b.h2("2.3 Cache and registers")
    b.p(
        "Cache is a small, very fast SRAM sitting between CPU and RAM. L1 is on the core, L2/L3 are larger and slightly slower. "
        "Registers (accumulator, PC, IR, MAR, MDR, FLAGS) are the fastest storage of all — a handful of bytes inside the CPU."
    )
    b.note("Hierarchy from fastest/smallest to slowest/largest: registers → cache → RAM → SSD/HDD → optical/tape.")

    b.h2("2.4 Secondary memory")
    b.bullets(
        [
            "Hard disk drive (HDD) — magnetic platters; cheap capacity; moving parts.",
            "Solid state drive (SSD) — flash chips; faster, no spinning platter.",
            "USB flash / data traveller — portable EEPROM/flash.",
            "External HDD — backup and extra space.",
            "SD / microSD — phones, cameras.",
            "CD / DVD / Blu-ray / combo drive — optical; CD ≈ 700 MB, DVD ≈ 4.7 GB, Blu-ray 25 GB+ per layer.",
        ]
    )
    b.qa(
        "Differentiate volatile and non-volatile memory.",
        "Volatile memory (RAM) loses data when power is removed. Non-volatile memory (ROM, HDD, flash) keeps data without power. "
        "A running document lives in RAM; Save writes it to secondary non-volatile storage.",
    )


def _unit3(b: LectureBuilder) -> None:
    b.h1("Unit 3 — Inside the System Unit (Computer Architecture)")
    b.p("Curriculum weight 15%. Overlaps BIEK’s old ‘Computer Architecture’ chapter — fetch-decode-execute is a classic 8-mark question.")

    b.h2("3.1 The system unit")
    b.p(
        "The system unit (CPU cabinet / chassis) houses the power supply, motherboard, storage drives, cooling, and ports. "
        "Form factors: desktop tower, SFF, all-in-one, laptop clamshell. Cooling uses heatsink + fan, and on some chips, liquid loops."
    )
    b.bullets(
        [
            "Power supply (SMPS) converts 220 V AC to 12 V / 5 V / 3.3 V DC.",
            "Motherboard is the main printed circuit board.",
            "Hard drive / SSD and optical combo drive mount in bays or M.2 slots.",
            "Ports on the back/front panel connect peripherals.",
        ]
    )

    b.h2("3.2 Motherboard components")
    b.table(
        ["Part", "Function"],
        [
            ["Microprocessor socket", "Holds the CPU"],
            ["Chipset (north/south or modern PCH)", "Traffic manager between CPU, RAM, and I/O"],
            ["RAM slots (DIMM)", "Main memory modules"],
            ["BIOS / UEFI chip", "Firmware that starts the machine"],
            ["CMOS battery", "Keeps clock and some setup values when unplugged"],
            ["Jumpers", "Tiny switches for old configuration options"],
            ["Expansion slots", "PCI / PCIe cards: graphics, Wi-Fi, capture"],
            ["System bus", "Shared pathways for address, data, control"],
            ["Ports", "USB, HDMI, audio, LAN, legacy serial/parallel"],
        ],
        [70, 108],
    )

    b.h2("3.3 Microprocessor")
    b.defn(
        "Microprocessor",
        "An IC that contains the ALU, control unit, and registers of a CPU on a single chip. It fetches instructions from memory and executes them.",
    )
    b.h3("Internal architecture")
    b.bullets(
        [
            "ALU — arithmetic (+ − × ÷) and logic (AND OR NOT XOR, compare).",
            "Control Unit — fetches instructions, decodes opcodes, issues control signals, manages timing.",
            "Registers — scratch storage; Program Counter holds the next instruction address; Instruction Register holds the current instruction.",
            "Clock — crystal pulses; 3.2 GHz means 3.2 billion ticks per second (not the same as 3.2 billion instructions, because of multi-cycle ops and IPC).",
            "Cache — on-chip SRAM.",
        ]
    )
    b.h3("External pins (idea)")
    b.p(
        "Address pins send the memory address, data pins carry the bits, control pins carry READ/WRITE/MEM/IO, "
        "interrupt pins let devices request service, power pins supply Vcc/GND."
    )
    b.p(
        "Specifications to quote: process technology (nm), generation/family, clock speed, word size (32/64-bit), "
        "bus width, cache size, number of cores, TDP."
    )

    b.h2("3.4 Buses")
    b.table(
        ["Bus", "Carries", "Direction"],
        [
            ["Address bus", "Location numbers", "Unidirectional (CPU → memory/IO)"],
            ["Data bus", "Actual data and instructions", "Bidirectional"],
            ["Control bus", "Read, write, interrupt, clock", "Mostly CPU → others, some status back"],
        ],
        [36, 62, 80],
    )
    b.tip(
        "Width of the address bus decides how much memory can be addressed: n address lines → 2^n locations. "
        "A 32-bit address bus theoretically maps 4 GB."
    )

    b.h2("3.5 Ports and expansion slots")
    b.table(
        ["Port / slot", "Typical use"],
        [
            ["Serial (legacy RS-232)", "Old mouse, industrial devices; bit by bit"],
            ["Parallel (legacy)", "Old printers; several bits at once"],
            ["USB 2/3/C", "Almost every peripheral; hot-pluggable"],
            ["HDMI", "Digital video + audio to monitor/TV"],
            ["VGA", "Older analog video"],
            ["PCI", "Older expansion cards"],
            ["PCIe (modern; curriculum also lists EISA/VISA as historical)", "Graphics and fast I/O"],
        ],
        [70, 108],
    )

    b.h2("3.6 Fetch–Decode–Execute cycle")
    b.p("This is the heartbeat of the von Neumann machine. Write it as three (sometimes four) labelled steps.")
    b.code(
        """
  PC  -->  MAR  -->  Memory  -->  MDR  -->  IR
                                              |
                                         CU decodes
                                              |
                              ALU / registers execute, then PC := PC+1
""".strip(
            "\n"
        ),
        "Fig. 3.1  Instruction cycle (simplified)",
    )
    b.bullets(
        [
            "Fetch: CU places PC on the address bus, issues READ, copies the instruction into IR, increments PC.",
            "Decode: CU interprets the opcode and turns on the correct control lines.",
            "Execute: ALU or a data movement happens; result may go to a register or memory.",
            "Store / write-back (sometimes listed separately): result is written back if needed.",
        ]
    )
    b.qa(
        "What is the role of the CPU? Name its two main parts.",
        "The CPU processes instructions. Its two main parts are the ALU (arithmetic/logic) and the Control Unit (sequencing). Registers and cache support both.",
    )


def _unit4(b: LectureBuilder) -> None:
    b.h1("Unit 4 — Operating System")
    b.p("Curriculum weight 10%. ‘What is an OS and why is it necessary?’ is a standard 3-mark or 8-mark question.")

    b.h2("4.1 Definition and objectives")
    b.defn(
        "Operating system",
        "System software that manages hardware resources and provides a platform on which application programs run. "
        "It is the first program the user effectively meets after firmware/BIOS.",
    )
    b.p("Objectives: convenience for the user, efficient use of CPU/memory/devices, security, and a stable environment.")
    b.p("Common desktop/server families: Microsoft Windows, Apple macOS, UNIX/Linux, and historically MS-DOS. Mobile: Android, iOS.")

    b.h2("4.2 Features / types")
    b.table(
        ["Type", "Idea", "Example"],
        [
            ["Batch", "Jobs queued; no interaction while running", "Old payroll runs"],
            ["Multi-tasking", "Several programs appear to run at once (time slices)", "Browser + Word"],
            ["Time-sharing", "Many users, short CPU bursts each", "University server"],
            ["Multi-processing", "More than one CPU/core sharing work", "Quad-core PC"],
            ["Parallel", "Problem split across processors at once", "Scientific jobs"],
            ["Distributed", "Many machines act as one resource pool", "Cluster"],
            ["Embedded", "OS inside a device, limited UI", "Car ECU, router"],
            ["Real-time", "Deadlines must be met", "Airbag controller"],
        ],
        [40, 78, 60],
    )

    b.h2("4.3 Functions of an OS")
    b.bullets(
        [
            "Booting — loading the kernel from disk into RAM after POST.",
            "Process management — create, schedule, suspend, terminate processes.",
            "Memory management — allocate/free RAM, virtual memory / paging.",
            "File management — names, folders, permissions, FAT/NTFS/ext4.",
            "I/O and device management — drivers, buffers, spooling for printers.",
            "Secondary storage management — free space, disk scheduling.",
            "Network management — protocol stack, sharing.",
            "Protection and security — passwords, access control, user accounts.",
            "Command interpreter / shell — CMD, PowerShell, bash, or a GUI.",
        ]
    )

    b.h2("4.4 Process management")
    b.defn(
        "Process",
        "A program in execution. A program on disk is passive; a process has a program counter, registers, and an address space.",
    )
    b.table(
        ["State", "Meaning"],
        [
            ["New", "Process is being created"],
            ["Ready", "Waiting for CPU; all other resources available"],
            ["Running", "Instructions are executing on a CPU"],
            ["Waiting / blocked", "Waiting for I/O or an event"],
            ["Terminated", "Finished or killed; PCB will be freed"],
        ],
        [40, 138],
    )
    b.p(
        "Thread: a lightweight path of execution inside a process. Multi-threading = many threads in one process "
        "(a browser with one tab hanging). Multi-tasking = many processes (browser + Word)."
    )

    b.h2("4.5 Working with a GUI OS (Windows skills)")
    b.bullets(
        [
            "Files and folders: create, delete, copy, rename, drag-and-drop.",
            "Path: C:\\Users\\Ali\\Documents\\notes.pdf — drive, folders, file.",
            "Search by name, date, or type; wildcards * and ?.",
            "Attributes: read-only, hidden, system, archive.",
            "Control Panel / Settings: printers, accounts, date/time, programs.",
            "dxdiag — DirectX diagnostic of display/sound/CPU.",
            "msconfig — startup and boot options (use carefully).",
        ]
    )

    b.h2("4.6 Open source and mobile OS")
    b.p(
        "Open-source OS (Linux distributions) publish source code; users may study, change, and share under a licence. "
        "Advantages: low cost, community patches, control, good servers. Android is a mobile OS based on a Linux kernel, "
        "versioned as API levels (mention any current name you know, e.g. recent Android releases)."
    )
    b.qa(
        "Why is an operating system necessary?",
        "Without an OS, every program would have to talk to hardware itself. The OS hides hardware details, shares the CPU fairly, "
        "keeps files organised, and stops one program from destroying another’s memory.",
    )


def _unitA(b: LectureBuilder) -> None:
    b.h1("Extra A — Number systems and codes")
    b.p(
        "Not a separate 2019 unit, but BIEK Paper-I still examines conversions and character codes "
        "(ASCII, BCD, EBCDIC). Learn the methods; examiners love a conversion with working."
    )

    b.h2("A.1 Four number systems")
    b.table(
        ["System", "Base", "Digits", "Board use"],
        [
            ["Decimal", "10", "0–9", "Human counting"],
            ["Binary", "2", "0, 1", "Machine states"],
            ["Octal", "8", "0–7", "Compact binary (groups of 3)"],
            ["Hexadecimal", "16", "0–9, A–F", "Compact binary (groups of 4); colours, addresses"],
        ],
        [36, 22, 40, 80],
    )

    b.h2("A.2 Conversion methods")
    b.bullets(
        [
            "Decimal → binary: divide by 2, remainder is the next low-order bit; read remainders bottom-up.",
            "Binary → decimal: expand weights 1, 2, 4, 8, 16, … from the right.",
            "Binary ↔ octal: groups of 3 bits. Binary ↔ hex: groups of 4 bits. Pad with leading zeros.",
            "Decimal → hex: divide by 16; remainders 10–15 become A–F.",
        ]
    )
    b.h3("Worked example")
    b.p("Convert 45 to binary: 45/2=22 r1, 22/2=11 r0, 11/2=5 r1, 5/2=2 r1, 2/2=1 r0, 1/2=0 r1. Read up: 101101₂.")
    b.p("Check: 32+8+4+1=45. Hex: 101101 → 0010 1101 = 2D₁₆.")

    b.h2("A.3 Character codes")
    b.table(
        ["Code", "Bits / character", "Note"],
        [
            ["BCD", "4 bits per decimal digit", "8421 weights; 45 → 0100 0101"],
            ["EBCDIC", "8 bits", "IBM mainframes"],
            ["ASCII", "7-bit original, 8-bit extended", "A = 65, a = 97, 0 = 48, space = 32"],
            ["Unicode / UTF-8", "variable", "All world scripts; mention as modern extra"],
        ],
        [32, 40, 106],
    )
    b.tip("If an MCQ says ‘standard code for microcomputers’, the answer is almost always ASCII.")


def _unitB(b: LectureBuilder) -> None:
    b.h1("Extra B — Boolean algebra and logic gates")
    b.p("A high-frequency BIEK Paper-I topic. Practise truth tables until you can draw them in under a minute.")

    b.h2("B.1 Why Boolean algebra?")
    b.defn(
        "Boolean algebra",
        "Algebra of two values, TRUE/FALSE or 1/0, using AND, OR and NOT. It is the mathematics of digital circuits and of conditions in programs.",
    )
    b.p("AND (·) is 1 only if every input is 1. OR (+) is 1 if any input is 1. NOT (′) inverts a single input.")

    b.h2("B.2 Basic gates")
    b.table(
        ["Gate", "Expression", "Output 1 when", "Unique identity"],
        [
            ["AND", "Y = A·B", "all inputs 1", ""],
            ["OR", "Y = A+B", "at least one input 1", ""],
            ["NOT", "Y = A′", "input is 0", "one input only"],
            ["NAND", "Y = (A·B)′", "not (all 1)", "universal gate"],
            ["NOR", "Y = (A+B)′", "all inputs 0", "universal gate"],
            ["XOR", "Y = A⊕B", "inputs differ", "odd number of 1s"],
            ["XNOR", "Y = (A⊕B)′", "inputs same", "equality detector"],
        ],
        [28, 36, 48, 66],
    )
    b.note(
        "NAND and NOR are universal: any Boolean function can be built from only NAND gates, or only NOR gates. "
        "That fact is a popular MCQ."
    )

    b.h2("B.3 Truth tables of AND, OR, NOT, NAND")
    b.table(
        ["A", "B", "AND", "OR", "NAND", "NOR", "XOR"],
        [
            ["0", "0", "0", "0", "1", "1", "0"],
            ["0", "1", "0", "1", "1", "0", "1"],
            ["1", "0", "0", "1", "1", "0", "1"],
            ["1", "1", "1", "1", "0", "0", "0"],
        ],
        [22, 22, 24, 22, 26, 24, 24],
    )

    b.h2("B.4 Laws (learn names + one identity each)")
    b.table(
        ["Law", "AND form", "OR form"],
        [
            ["Identity", "A·1 = A", "A+0 = A"],
            ["Null / Annulment", "A·0 = 0", "A+1 = 1"],
            ["Idempotent", "A·A = A", "A+A = A"],
            ["Complement", "A·A′ = 0", "A+A′ = 1"],
            ["Commutative", "A·B = B·A", "A+B = B+A"],
            ["Associative", "A·(B·C)=(A·B)·C", "A+(B+C)=(A+B)+C"],
            ["Distributive", "A·(B+C)=A·B+A·C", "A+(B·C)=(A+B)·(A+C)"],
            ["Absorption", "A·(A+B)=A", "A+(A·B)=A"],
            ["Involution", "(A′)′ = A", "(A′)′ = A"],
            ["De Morgan", "(A·B)′ = A′+B′", "(A+B)′ = A′·B′"],
        ],
        [40, 70, 68],
    )
    b.p("Principle of duality: swap · with + and 0 with 1; the dual identity is also true.")

    b.h2("B.5 De Morgan — the 8-mark favourite")
    b.p("Law 1: (A·B)′ = A′ + B′. Law 2: (A+B)′ = A′ · B′. Prove each with a truth table AND a gate diagram.")
    b.table(
        ["A", "B", "A·B", "(A·B)′", "A′", "B′", "A′+B′"],
        [
            ["0", "0", "0", "1", "1", "1", "1"],
            ["0", "1", "0", "1", "1", "0", "1"],
            ["1", "0", "0", "1", "0", "1", "1"],
            ["1", "1", "1", "0", "0", "0", "0"],
        ],
        [20, 20, 24, 28, 20, 20, 28],
    )
    b.p("Columns (A·B)′ and A′+B′ match, so Law 1 is proved. Repeat the pattern for Law 2 in the exam.")

    b.h2("B.6 SOP, POS, and Karnaugh map (idea)")
    b.p(
        "From a truth table, a 1-row becomes a minterm (AND of literals). Sum of those minterms is SOP. "
        "A 0-row becomes a maxterm (OR of literals); product of maxterms is POS. "
        "A K-map groups 1s in power-of-two blocks (1, 2, 4, 8) to cancel variables. BIEK usually stays at 2 or 3 variables; "
        "FBISE-style 4-variable maps are extra credit."
    )
    b.p("Example: Y = AB + BC reduces with Boolean algebra; Y = CD + EF needs two AND gates and one OR gate.")


def _unitC(b: LectureBuilder) -> None:
    b.h1("Extra C — Data security")
    b.defn(
        "Malware",
        "Software written to damage, steal, or hijack a system. A virus attaches to files and spreads when they run; "
        "a worm self-replicates over networks; a Trojan looks useful but hides a payload; ransomware encrypts files for money.",
    )
    b.bullets(
        [
            "Antivirus / anti-malware scans signatures and behaviour; update definitions daily.",
            "Firewall filters packets by rule (port, IP, application); can be hardware or software.",
            "Proxy server sits between clients and the Internet: cache, filter, hide internal IPs.",
            "Email threats: phishing, fake invoices, attachments with macros. Never send passwords by email.",
            "Good habits: strong unique passwords, backups, licensed software, least privilege accounts.",
        ]
    )
    b.qa(
        "Why do we use antivirus software? Name two products.",
        "To detect, quarantine, and remove malware before it damages files or steals data. Examples: Windows Defender, "
        "Kaspersky, Avast, Bitdefender (any two named correctly).",
    )


def _unit5(b: LectureBuilder) -> None:
    b.h1("Unit 5 — Programming concepts using C++")
    b.p(
        "Curriculum weight 20% — the largest XI theory unit. BIEK Paper-II Option I still uses C (printf/scanf). "
        "The 2019 XI book uses C++ streams. Learn both syntaxes; the ideas (types, if, loops, functions) are the same."
    )

    b.h2("5.1 What is a program?")
    b.defn(
        "Program",
        "A finite set of instructions written in a programming language to solve a problem.",
    )
    b.p(
        "Language levels: machine (binary), assembly (mnemonics + assembler), high-level (C, C++, Java, Python). "
        "Translators: compiler (whole program → object code), interpreter (line by line), assembler (assembly → machine). "
        "A linker combines object files; an IDE (Turbo C++, Dev-C++, Code::Blocks, VS Code) edits, compiles, and runs."
    )
    b.table(
        ["Error type", "When it is found", "Example"],
        [
            ["Syntax", "Compile time", "Missing semicolon"],
            ["Semantic / type", "Compile or link time", "Assigning a string to int wrongly"],
            ["Runtime", "While running", "Divide by zero, missing file"],
            ["Logical", "Wrong answer, program ‘works’", "Using = instead of == in a condition"],
        ],
        [36, 50, 92],
    )

    b.h2("5.2 Structure of a C++ program")
    b.code(
        """#include <iostream>
using namespace std;

int main() {
    int a, b, sum;
    cout << "Enter two integers: ";
    cin >> a >> b;          // cascading input
    sum = a + b;
    cout << "Sum = " << sum << endl;
    return 0;
}""",
        "Program 5.1  IPO with cascading streams",
    )
    b.p(
        "Turbo C style of the same idea uses #include <stdio.h>, printf/scanf, and often void main() plus getch(). "
        "BIEK Option I papers still show that style in Class XII."
    )

    b.h2("5.3 Tokens, data types, operators")
    b.bullets(
        [
            "Tokens: keywords (int, if, return), identifiers (marks1 — must start with letter or _), constants, operators, punctuators, strings.",
            "Basic types: int, short, long, float, double, char, bool (C++), void.",
            "Arithmetic: + − * / %   Relational: < <= > >= == !=   Logical: && || !   Assignment: = += -= *= /= %=",
            "Increment: ++x (pre) vs x++ (post).  Conditional: c ? t : f.  sizeof operator.",
        ]
    )
    b.tip(
        "Precedence: postfix ++, then unary, then * / %, then + −, then relational, then ==, then &&, then ||, then assignment. "
        "When in doubt, use parentheses.  y = 5+3-6*2/3  does * and / first: 6*2=12, 12/3=4, then 5+3-4=4."
    )
    b.warn("a=+1 is NOT increment. Valid increment forms: a = a+1; a += 1; a++; ++a.")

    b.h2("5.4 Selection")
    b.code(
        """if (marks >= 40)
    cout << "Pass";
else
    cout << "Fail";

// nested / else-if ladder
if (n > 0) cout << "positive";
else if (n < 0) cout << "negative";
else cout << "zero";

switch (colour) {
    case 1: cout << "Red"; break;
    case 2: cout << "Black"; break;
    case 3: cout << "White"; break;
    default: cout << "No colour";
}""",
        "if, else-if, and switch",
    )
    b.note("switch can test int or char, not float. Always write break unless you want fall-through.")

    b.h2("5.5 Iteration")
    b.table(
        ["Loop", "Test", "Guaranteed to run once?"],
        [
            ["for (init; test; update)", "before body", "No (if test is false at start)"],
            ["while (test)", "before body", "No"],
            ["do { body } while (test);", "after body", "Yes"],
        ],
        [70, 40, 68],
    )
    b.code(
        """// print 1 to 5
for (int i = 1; i <= 5; i++)
    cout << i << " ";

int i = 1;
while (i <= 5) { cout << i << " "; i++; }

i = 1;
do { cout << i << " "; i++; } while (i <= 5);""",
        "Three loops, same output",
    )
    b.p("Nested loops build tables and patterns. break leaves the loop; continue skips to the next iteration; goto is legal but poor style.")

    b.h2("5.6 Functions")
    b.p(
        "A function is a named block. Advantages: reuse, shorter main, easier testing. "
        "Predefined: sqrt, pow (cmath), strlen (cstring). User-defined: you write them."
    )
    b.bullets(
        [
            "Signature = name + parameter types + return type.",
            "Prototype (declaration) tells the compiler before main; definition has the body; call uses the name.",
            "Formal parameters are in the definition; actual parameters are in the call.",
            "Pass by value copies; pass by reference (int &x) can change the caller’s variable.",
            "Default arguments: void greet(string n = \"Student\");",
            "local vs global vs static: local dies when the function ends; global lives for the program; static local remembers its value between calls.",
            "inline suggests the compiler paste the body at the call site (small functions).",
            "exit(0) (cstdlib) ends the whole program.",
        ]
    )
    b.code(
        """#include <iostream>
using namespace std;

int larger(int x, int y);          // prototype

int main() {
    cout << larger(12, 7);
    return 0;
}

int larger(int x, int y) {         // definition; x,y formal
    return (x > y) ? x : y;
}""",
        "Prototype, call, definition",
    )

    b.h2("5.7 Function overloading")
    b.p(
        "Same function name, different parameter lists (count or types). Return type alone is not enough to overload. "
        "The compiler picks the best match at compile time (static polymorphism)."
    )
    b.code(
        """int add(int a, int b) { return a + b; }
double add(double a, double b) { return a + b; }
int add(int a, int b, int c) { return a + b + c; }"""
    )


def _unit6(b: LectureBuilder) -> None:
    b.h1("Unit 6 — Arrays, strings and structures")
    b.p("Curriculum weight 15%. Sorting, searching, and string reverse appear in both theory and practicals.")

    b.h2("6.1 One-dimensional arrays")
    b.defn(
        "Array",
        "A named sequence of elements of the same type stored in consecutive memory locations, accessed by an integer index starting at 0.",
    )
    b.code(
        """int marks[5] = {70, 80, 90, 60, 75};
cout << marks[0];          // 70
int n = sizeof(marks) / sizeof(marks[0]);   // 5

int sum = 0;
for (int i = 0; i < 5; i++)
    sum += marks[i];
cout << "Average = " << sum / 5.0;""",
        "Declaration, index, traversal, sizeof",
    )
    b.warn("marks[5] on an array of size 5 is out of range (valid indices 0–4). Board MCQs love this trap.")

    b.h2("6.2 Two-dimensional arrays")
    b.p("Think of a matrix: rows then columns. int a[3][3];  Access a[r][c]. Nested loops required.")
    b.code(
        """int a[2][2] = {{1, 2}, {3, 4}};
int b[2][2] = {{5, 6}, {7, 8}};
int c[2][2];
for (int i = 0; i < 2; i++)
    for (int j = 0; j < 2; j++)
        c[i][j] = a[i][j] + b[i][j];""",
        "Matrix addition (same pattern for 3×3)",
    )

    b.h2("6.3 Strings")
    b.p(
        "A C-string is a char array ending with '\\0'. char name[20] = \"Ali\"; occupies A,l,i,\\0. "
        "Never forget the terminator when counting storage."
    )
    b.table(
        ["Function", "Header", "Job"],
        [
            ["strlen(s)", "<cstring>", "Count characters before \\0"],
            ["strcpy(d,s)", "<cstring>", "Copy s into d"],
            ["strcat(d,s)", "<cstring>", "Append s onto d"],
            ["strcmp(a,b)", "<cstring>", "0 if equal, <0 if a<b, >0 if a>b"],
            ["substr (C++ string)", "<string>", "s.substr(pos, len)"],
        ],
        [40, 32, 106],
    )
    b.code(
        """#include <iostream>
#include <cstring>
using namespace std;
int main() {
    char name[30];
    cin.getline(name, 30);
    for (int i = strlen(name) - 1; i >= 0; i--)
        cout << name[i];
    return 0;
}""",
        "Print a name in reverse using strlen",
    )

    b.h2("6.4 Structures")
    b.defn(
        "Structure",
        "A user-defined type that groups variables of possibly different types under one name. Unlike an array, members can mix char, int, float.",
    )
    b.code(
        """struct Employee {
    char name[30];
    char designation[20];
    float salary;
};

int main() {
    Employee e = {"Sara", "Clerk", 45000};
    cout << e.name << "  " << e.designation << "  " << e.salary;
}""",
        "Curriculum practical: display employee data",
    )
    b.p("Dot operator e.name accesses a member. An array of struct Employee staff[50]; is how simple databases start — a bridge to Class XII.")


def _unit7(b: LectureBuilder) -> None:
    b.h1("Unit 7 — Computer communication and networks")
    b.p("Curriculum weight 15%. Topologies with diagrams are a classic Section C question.")

    b.h2("7.1 Network and components")
    b.defn(
        "Computer network",
        "Two or more computers connected to share resources (files, printers, Internet) and to communicate.",
    )
    b.table(
        ["Component", "Role"],
        [
            ["Sender", "Device that originates the message"],
            ["Receiver", "Device that accepts the message"],
            ["Message", "Data actually sent (file, voice, video)"],
            ["Medium", "Path: cable or wireless"],
            ["Protocol", "Agreed rules (HTTP, TCP, IP, SMTP)"],
        ],
        [36, 142],
    )
    b.p("Advantages: sharing, communication, cheaper peripherals, central backup. Disadvantages: security risk, cabling cost, dependence on the server in a star.")

    b.h2("7.2 Communication modes (data flow)")
    b.table(
        ["Mode", "Direction", "Example"],
        [
            ["Simplex", "One way only", "Keyboard → CPU, radio broadcast"],
            ["Half duplex", "Both ways, not at the same time", "Walkie-talkie"],
            ["Full duplex", "Both ways at once", "Telephone, modern Ethernet"],
        ],
        [36, 58, 84],
    )

    b.h2("7.3 Transmission media")
    b.table(
        ["Kind", "Examples", "Notes"],
        [
            ["Guided (wired)", "Twisted pair, coaxial, fibre optic", "Fibre: light, longest distance, immune to EMI"],
            ["Unguided (wireless)", "Radio, microwave, infrared", "Microwave often needs line of sight"],
        ],
        [40, 58, 80],
    )
    b.p(
        "Twisted pair: cheap LAN cable (Cat5e/Cat6). Coaxial: older TV and some backbone. "
        "Straight-through cable: PC to switch. Crossover: PC to PC (older NICs). Practicals ask you to crimp RJ-45."
    )

    b.h2("7.4 Network types")
    b.table(
        ["Type", "Span", "Example"],
        [
            ["LAN", "Room, floor, campus", "College computer lab"],
            ["MAN", "A city", "City-wide cable network"],
            ["WAN", "Country / planet", "The Internet"],
            ["PAN (extra)", "A few metres", "Phone + earbuds (Bluetooth)"],
        ],
        [28, 44, 106],
    )
    b.defn(
        "Internet / Intranet",
        "Internet is the global public network of networks using TCP/IP. Intranet is a private TCP/IP network of one organisation, "
        "often using web technology but not open to the world.",
    )

    b.h2("7.5 Topologies")
    b.table(
        ["Topology", "Shape", "Strength", "Weakness"],
        [
            ["Bus", "One backbone", "Cheap cable", "Backbone break kills all"],
            ["Star", "All nodes to a hub/switch", "Easy to add PCs; one cable fault is local", "Central device is a single point of failure"],
            ["Ring", "Closed loop", "Fair access (token)", "A break can stop the ring (unless dual ring)"],
            ["Mesh", "Many-to-many links", "Very fault tolerant", "Expensive cabling"],
            ["Tree", "Hierarchy of stars", "Scales a campus", "Root failure"],
            ["Hybrid", "Mix of the above", "Fits real buildings", "Complex to manage"],
        ],
        [28, 40, 58, 52],
    )
    b.code(
        """
  STAR:           RING:            BUS:
      [H]          A---B            A--B--C--D
     / | \\         |   |               |
    A  B  C        D---C             backbone
""".strip(
            "\n"
        ),
        "Sketch these three in Section C; label hub/switch on star",
    )

    b.h2("7.6 Standards and architectures")
    b.table(
        ["Body", "What it standardises"],
        [
            ["ISO", "OSI 7-layer model; many quality standards"],
            ["IEEE", "LAN standards, e.g. 802.3 Ethernet, 802.11 Wi-Fi"],
            ["ITU", "Telecom (radio, telephone, some wireless)"],
            ["ASCII (as a code standard)", "Character encoding — often listed beside these bodies in the curriculum"],
        ],
        [40, 138],
    )
    b.h3("ISO OSI seven layers (learn in order)")
    b.table(
        ["#", "Layer", "Job in one line"],
        [
            ["7", "Application", "User programs: HTTP, SMTP, FTP, DNS"],
            ["6", "Presentation", "Encryption, compression, format (JPEG, ASCII)"],
            ["5", "Session", "Start, manage, end conversations"],
            ["4", "Transport", "End-to-end: TCP (reliable), UDP (fast)"],
            ["3", "Network", "Routing and IP addressing"],
            ["2", "Data link", "Frames, MAC addresses, switches"],
            ["1", "Physical", "Bits on wire/radio, cables, hubs"],
        ],
        [12, 36, 130],
    )
    b.p(
        "TCP/IP model (Internet model) is the one the Internet actually uses: Application, Transport, Internet, Network Access (Link). "
        "Mnemonic for OSI: All People Seem To Need Data Processing."
    )
    b.qa(
        "What is topology? Describe star, bus and ring with diagrams.",
        "Topology is the geometric arrangement of links and nodes. Draw the three sketches, then write one advantage and one disadvantage for each (use the table above).",
    )


def _unitD(b: LectureBuilder) -> None:
    b.h1("Extra D — Signals, modem and software types")
    b.p(
        "Old BIEK Paper-I still asks analog versus digital signals, the job of a modem, and a full software classification. "
        "Keep this extra lecture next to Unit 7."
    )
    b.h2("D.1 Analog and digital signals")
    b.table(
        ["Point", "Analog", "Digital"],
        [
            ["Form", "Continuous wave, infinite values in a range", "Discrete levels, usually two (0 and 1)"],
            ["Example", "Human voice on a copper telephone line, mercury thermometer", "CD audio after sampling, a USB transfer"],
            ["Noise", "Hard to separate from the signal", "Easier to regenerate; computers are digital"],
            ["Use in PCs", "Sound card input before conversion", "CPU, RAM, storage, Ethernet"],
        ],
        [28, 76, 74],
    )
    b.defn(
        "Modem",
        "Modulator–demodulator. It converts a computer’s digital bits into analog waves for a telephone or cable line (modulation) "
        "and converts incoming analog waves back into bits (demodulation). ADSL/fibre boxes at home still play this role on the last hop.",
    )
    b.h2("D.2 Full software map (8-mark structure)")
    b.defn(
        "Software",
        "A set of programs, procedures and related documentation that tell hardware what to do. Without software a computer is a dead box.",
    )
    b.table(
        ["Branch", "Sub-type", "Examples"],
        [
            ["System software", "Operating system", "Windows, Linux, Android, macOS"],
            ["System software", "Device driver", "Printer driver, graphics driver"],
            ["System software", "Language translator", "Compiler (gcc), interpreter (Python), assembler"],
            ["System software", "Anti-malware", "Windows Defender, Kaspersky"],
            ["Application — general", "Office, browser, media", "Word, Excel, Chrome, VLC"],
            ["Application — special", "One organisation / job", "Hospital MIS, bank CBS, college payroll"],
            ["Utility", "Housekeeping", "Zip, backup, Disk Cleanup, Recuva"],
        ],
        [44, 50, 84],
    )
    b.p(
        "Translators in more detail: a compiler reads the whole source and builds an object/exe (fast later runs, all syntax errors at once). "
        "An interpreter executes line by line (easier to try, slower, stops at the first runtime error). "
        "An assembler translates mnemonic assembly into machine code, one instruction roughly to one opcode."
    )
    b.qa(
        "Define software. Explain system software and application software.",
        "Start with the definition box. Draw the classification table. Give two examples in each box. Close with: system software manages the machine; application software does the user’s actual job (letter, accounts, game).",
    )


def _practicals(b: LectureBuilder) -> None:
    b.h1("Grade XI practical journal (Sindh list)")
    b.p("25 marks. Keep a dated journal. The official activity list includes hardware, Windows, C++, and networking.")
    b.h2("Hardware and OS")
    b.bullets(
        [
            "Identify CPU, RAM, HDD/SSD, PSU, ports on a motherboard.",
            "Assemble/disassemble RAM, drive, and SATA/power cables (under teacher supervision).",
            "BIOS/UEFI: boot order, date/time, hardware monitor.",
            "Desktop, Explorer, create/copy/move/delete/rename, search, attributes.",
            "Control Panel resource management; dxdiag; msconfig (view only if school policy says so).",
        ]
    )
    b.h2("Programming (write these in your journal with output)")
    b.bullets(
        [
            "Calculator using arithmetic operators.",
            "Mark sheet with if / else-if (grade A/B/C/F).",
            "Prime or composite test.",
            "Split a 4-digit number onto four lines.",
            "Factors of n; stars pattern function; larger-of-two function.",
            "Sort an array; linear search; average of array; 3×3 add/multiply.",
            "Reverse a name with strlen; employee structure display.",
        ],
        numbered=True,
    )
    b.h2("Networking practicals")
    b.bullets(
        [
            "Identify CAT cable, crimp straight-through and crossover, test with a tester.",
            "Name switch, router, NIC, modem in the lab.",
            "Set a static IP, subnet, gateway, DNS; ping the gateway.",
            "Share a folder on a LAN; explain client vs centralised vs workgroup.",
        ]
    )


def _model_paper(b: LectureBuilder) -> None:
    b.h1("Model practice paper — Computer Science I")
    b.p("Time 3 hours. Marks 75. Attempt this on paper, then mark from the keys below.")

    b.h2("Section A — MCQs (attempt all)")
    b.mcqs(
        [
            ("The brain of the computer is the", ["ALU only", "CPU", "Monitor", "USB"], "B"),
            ("1 MB equals", ["1000 KB", "1024 KB", "1024 bytes", "1024 GB"], "B"),
            ("Which memory is volatile?", ["ROM", "Flash", "RAM", "HDD"], "C"),
            ("EEPROM is erased by", ["UV light", "A hammer", "Electric signal", "BIOS password"], "C"),
            ("The address bus is normally", ["Bidirectional", "Unidirectional", "Optical", "Analog"], "B"),
            ("Which is a function of an OS?", ["Compiling C++", "Process management", "Crimping cable", "None"], "B"),
            ("A process waiting for a printer is in", ["Running", "Ready", "Waiting/blocked", "New"], "C"),
            ("ASCII code of ‘A’ is", ["48", "65", "97", "32"], "B"),
            ("(A·B)′ equals", ["A′·B′", "A′+B′", "A+B", "A·B"], "B"),
            ("A universal gate is", ["AND", "XOR", "NAND", "Buffer"], "C"),
            ("HTTP works at OSI layer", ["Transport", "Network", "Application", "Physical"], "C"),
            ("College lab network is typically a", ["WAN", "LAN", "MAN", "GAN"], "B"),
            ("Optical fibre carries", ["Sound", "Light", "Water", "Steam"], "B"),
            ("Compiler translates", ["Line by line", "The whole program", "Only comments", "Only HTML"], "B"),
            ("Index of the first array element is", ["1", "0", "-1", "n"], "B"),
            ("Which loop always runs at least once?", ["for", "while", "do-while", "goto"], "C"),
            ("strcmp returns 0 when strings are", ["Unequal", "Equal", "Empty", "Numeric"], "B"),
            ("A firewall is used for", ["Cooling CPU", "Filtering network traffic", "Printing", "Compiling"], "B"),
            ("Cloud computing mainly provides resources", ["Only offline", "Over the Internet", "Inside ROM", "Via plotter"], "B"),
            ("HDMI is a", ["Storage device", "Port", "Topology", "Virus"], "B"),
            ("Cache memory is usually", ["DRAM", "SRAM", "Magnetic", "Optical"], "B"),
            ("Star topology’s centre is often a", ["Repeater only", "Hub or switch", "Plotter", "Scanner"], "B"),
            ("void as a return type means", ["Returns int", "Returns nothing", "Returns float", "Error"], "B"),
            ("Which is application software?", ["Linux kernel", "MS Word", "Device driver", "BIOS"], "B"),
            ("Full duplex example", ["Radio", "Keyboard", "Telephone", "Loudspeaker"], "C"),
            ("Program Counter holds", ["Current instruction", "Next instruction address", "Result of ALU", "Stack size"], "B"),
            ("1 nibble is", ["2 bits", "4 bits", "8 bits", "16 bits"], "B"),
            ("Phishing is usually delivered by", ["Heatsink", "Email or fake websites", "ALU", "HDMI"], "B"),
            ("sizeof(int array of 10) / sizeof(int) gives", ["10", "40", "0", "2"], "A"),
        ]
    )

    b.h2("Section B — sample short questions (attempt 10 of 15)")
    b.bullets(
        [
            "Define computer system. List four characteristics.",
            "Hard copy versus soft copy.",
            "Volatile versus non-volatile memory with examples.",
            "Differentiate compiler and interpreter.",
            "Draw De Morgan’s first law with a truth table.",
            "LAN versus WAN.",
            "Internet versus intranet.",
            "Any three input devices and one use each.",
            "Two types of printers.",
            "What is a process? Name four states.",
            "Define protocol and give two examples.",
            "What is an array? Show a declaration.",
            "Local versus global variables.",
            "Purpose of BIOS and CMOS battery.",
            "Two advantages of fibre optic cable.",
        ],
        numbered=True,
    )

    b.h2("Section C — sample detailed questions (attempt 2 of 3)")
    b.bullets(
        [
            "Define software. Explain system software and application software with examples.",
            "What is topology? Explain star, bus and ring with diagrams, advantages and disadvantages.",
            "Explain the fetch–decode–execute cycle with a labelled sketch of CPU components.",
        ],
        numbered=True,
    )


def _glossary(b: LectureBuilder) -> None:
    b.h1("Quick glossary (XI)")
    b.table(
        ["Term", "One-line meaning"],
        [
            ["ALU", "Part of CPU that calculates and compares"],
            ["BIOS/UEFI", "Firmware that starts hardware before the OS"],
            ["Bit", "Binary digit 0 or 1"],
            ["Bus", "Shared communication pathway"],
            ["Cache", "Small fast memory close to the CPU"],
            ["Compiler", "Translator of a whole high-level program"],
            ["GUI", "Graphical user interface (windows, icons, mouse)"],
            ["IDE", "Program that edits, compiles and runs code"],
            ["IPO", "Input–Process–Output model"],
            ["LAN", "Local area network"],
            ["OSI", "ISO’s seven-layer network model"],
            ["Protocol", "Rules of communication"],
            ["RAM", "Volatile main memory"],
            ["ROM", "Non-volatile firmware memory"],
            ["SDLC", "Covered in XII — lifecycle of software"],
            ["USB", "Universal Serial Bus port/protocol"],
        ],
        [36, 142],
    )
    b.p(
        "End of Class XI lectures. Continue with the Class XII volume for C / Visual Basic options "
        "and the remaining 2019 units (SDLC, pointers, OOP, files, database, multimedia, wireless)."
    )
