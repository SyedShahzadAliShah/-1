"""BIEK Computer Science I (Class XI) lectures."""

from diagrams import computer_block, fetch_cycle, osi_layers, process_states, ram_rom, simplex_modes, topologies
from content.blocks import check, code, defn, exam, example, flow, h, h3, learn, lec, mcq, ol, p, table, tip, ul, urdu, warn, svg

LECTURES = []


def add(d):
    LECTURES.append(d)


add(lec(
    id="xi-00",
    grade="XI",
    unit="0",
    unit_title="How to use these lectures",
    title="BIEK Paper I pattern and how to study",
    time="Read once, then return before every test",
    slos=[
        "State the BIEK Computer Science I paper structure and marks",
        "Know which units carry weight in Sindh Curriculum 2019",
        "Write Section B answers in 6–8 lines with a definition + points + example",
        "Draw the diagrams that examiners expect in Section C",
    ],
    body=[
        h("Who this book is for"),
        p("You are a Class XI student of a Karachi college affiliated with the Board of Intermediate Education, Karachi (BIEK). Computer Science Paper I is the theory paper of HSC Part I (Science General or Humanities). These lectures follow the Sindh Curriculum for Computer Science Grades XI–XII (2019) and the official BIEK Model Paper 2026."),
        learn(
            "Paper I is 75 marks in 3 hours. It is NOT the programming paper. Programming in C or Visual Basic is Paper II in Class XII. Paper I tests hardware, software, memory, CPU, operating system, data communication and networks.",
        ),
        table(
            ["Section", "What you do", "Marks", "Time (typical)"],
            [
                ["A — MCQs", "15 questions, all compulsory, on OMR", "15", "20 min"],
                ["B — Short", "Short notes, differences, full forms", "30", "1 h 20 min"],
                ["C — Detailed", "Long answers with diagrams", "30", "1 h 20 min"],
            ],
        ),
        h("Sindh unit weightage (Grade XI)"),
        table(
            ["Unit", "Title", "Weight"],
            [
                ["1", "Overview of Computer System", "15%"],
                ["2", "Computer Memory", "10%"],
                ["3", "Inside System Unit", "15%"],
                ["4", "Operating System", "10%"],
                ["5", "Programming Concept Using C++", "20%"],
                ["6", "Arrays, String and Structure", "15%"],
                ["7", "Computer Communication & Networks", "15%"],
            ],
        ),
        exam(
            "BIEK Model Paper 2026 Paper I asked: IT uses/abuses, barcode reader, hardcopy vs softcopy, virus, plotter, fetch cycle, modulation, compiler vs interpreter, impact vs non-impact printers, analog vs digital, OSI model, OS functions, registers, secondary storage, network classification. Memorise those exact headings.",
        ),
        tip(
            "Section B method: (1) one-line definition, (2) 3–4 labelled points, (3) one example. Section C method: definition, labelled diagram, 5–7 explained points, comparison table if asked.",
            "Write full forms when an abbreviation appears: CPU, RAM, ROM, OSI, SMTP, BIOS.",
        ),
        urdu(
            "یہ کتاب بورڈ آف انٹرمیڈیٹ ایجوکیشن کراچی (BIEK) کے کمپیوٹر سائنس پیپر ون کے لیے لکچر نوٹس ہے۔ پیپر ون میں ہارڈویئر، سافٹ ویئر، میموری، آپریٹنگ سسٹم اور نیٹ ورک آتے ہیں۔ پروگرامنگ کلاس بارہویں کے پیپر ٹو میں ہے۔",
            "سیکشن بی میں تعریف، تین نکات اور ایک مثال لکھیں۔ سیکشن سی میں لیبل والا خاکہ لازمی بنائیں۔",
        ),
        warn(
            "Do not write Python answers in a BIEK Paper I / Paper II C paper. Karachi board still examines C (Option I) or Visual Basic (Option II) plus MS Access.",
        ),
        check(
            ("How many MCQs are in Paper I Section A?", "15 (one mark each)"),
            ("Which paper contains C programming?", "Paper II (Class XII), Option I"),
        ),
    ],
    mcqs=[
        mcq("BIEK Computer Science Paper I total marks are:", ["50", "60", "75", "100"], "c"),
        mcq("Programming using C is offered in:", ["Paper I only", "Paper II Option I", "Paper II Option II", "Practical only"], "b"),
    ],
    short=["Write the scheme of BIEK Computer Science Paper I.", "Why must Section C answers include a diagram?"],
    short_ans=[
        "75 marks, 3 hours: Section A 15 MCQs (15), Section B short (30), Section C detailed (30). All of Paper I is theory of computer systems, OS and networks.",
        "Detailed questions ask you to explain a model (OSI, fetch cycle, topologies). Marks are given for a labelled sketch plus explanation. A paragraph without a figure loses marks.",
    ],
))

add(lec(
    id="xi-01",
    grade="XI",
    unit="1",
    unit_title="Overview of Computer System",
    title="Computer, IT and the system block diagram",
    golden=True,
    slos=[
        "Define computer and Information Technology",
        "Draw the block diagram: input, CPU, memory, output",
        "List uses and abuses of IT",
        "State the four basic operations: input, process, output, storage",
    ],
    body=[
        defn("Computer", "An electronic data-processing machine that accepts data (input), processes it according to instructions, produces information (output) and stores results."),
        defn("Information Technology (IT)", "The use of computers, networking and software to collect, store, process, protect and transmit information."),
        svg(computer_block(), "IPO model: Input → Process (CPU + Memory) → Output. Storage sits under the CPU."),
        learn(
            "Every computer does four operations. Input brings data in. Processing is done by the CPU (ALU calculates, CU controls). Output shows results. Storage keeps data in memory or on disk.",
            "Hardware is the physical parts you can touch. Software is the set of programs that tell hardware what to do. Firmware (BIOS) is software stored in ROM.",
        ),
        h("Uses of IT"),
        ul(
            "Education: LMS, online classes, digital libraries.",
            "Business: billing, inventory, e-commerce, ATM / online banking.",
            "Health: MRI, patient records, telemedicine.",
            "Government: NADRA, tax, e-office, SECCAP admissions.",
            "Communication: email, video call, social media.",
        ),
        h("Abuses of IT"),
        ul(
            "Hacking and identity theft.",
            "Computer virus and ransomware.",
            "Cyber-bullying and fake news.",
            "Privacy loss and excessive screen time.",
            "Software piracy and plagiarism.",
        ),
        example(
            "Board short question: “What is Information Technology? Write any three uses or abuses of IT.”",
            "Answer: IT is the application of computers and telecommunication to handle information. Uses: online banking, hospital records, distance learning. Abuses: hacking, viruses, spread of false information.",
        ),
        exam(
            "BIEK 2026 Paper I Q2(i) is exactly this heading. Keep a 5-line ready answer plus 3 uses and 3 abuses.",
        ),
        tip("IPO memory trick: In-Process-Out, and Store underneath. Draw arrows; examiners look for arrows."),
        urdu(
            "کمپیوٹر ایک برقی مشین ہے جو ڈیٹا لیتی ہے، ہدایات کے مطابق اس پر عمل کرتی ہے، نتیجہ دیتی ہے اور محفوظ کرتی ہے۔",
            "انفارمیشن ٹیکنالوجی کمپیوٹر اور نیٹ ورک سے معلومات کو جمع، محفوظ، پراسیس اور منتقل کرنے کا نام ہے۔ فائدے تعلیم، صحت، بینکنگ میں ہیں؛ نقصان وائرس، ہیکنگ اور جعلی خبریں ہیں۔",
        ),
        check(
            ("Name the four basic operations of a computer.", "Input, process, output, storage"),
            ("Who performs processing?", "CPU (ALU + CU + registers)"),
        ),
    ],
    mcqs=[
        mcq("The primary function of the CPU is:", ["To input data", "To store data", "To process data", "To print data"], "c"),
        mcq("The brain of the computer is the:", ["RAM", "Hard disk", "CPU", "Keyboard"], "c"),
        mcq("IT stands for:", ["Internet Tool", "Information Technology", "Internal Transfer", "Input Terminal"], "b"),
    ],
    short=["Define computer. Draw its block diagram.", "Write three uses and three abuses of IT."],
    short_ans=[
        "A computer is an electronic device that inputs, processes, outputs and stores data. Diagram: Input devices → CPU (ALU, CU, registers) with Memory below → Output devices.",
        "Uses: education, e-banking, hospitals. Abuses: hacking, viruses, fake news / privacy loss.",
    ],
    long=["What is a computer system? Explain hardware, software, basic operations and memory with a labelled block diagram."],
))

add(lec(
    id="xi-02",
    grade="XI",
    unit="1",
    unit_title="Overview of Computer System",
    title="Hardware: input, output, storage and communication devices",
    golden=True,
    slos=[
        "Classify devices as input, output, storage, processing or communication",
        "Describe keyboard, mouse, scanner, barcode, OCR, MICR, OMR, joystick, microphone, webcam",
        "Describe monitors, printers, plotter, speakers, projector",
        "Differentiate hardcopy and softcopy; impact and non-impact printers",
    ],
    body=[
        defn("Hardware", "The physical, electronic and mechanical parts of a computer system."),
        table(
            ["Class", "Job", "Examples"],
            [
                ["Input", "Send data into the computer", "Keyboard, mouse, scanner, MICR, OMR, OCR, barcode, joystick, microphone, webcam, stylus, touch screen"],
                ["Output", "Send results to the user", "Monitor, printer, plotter, speaker, projector, headphones"],
                ["Storage", "Keep data permanently or temporarily", "HDD, SSD, USB, SD, CD/DVD/Blu-ray"],
                ["Processing", "Transform data", "CPU, GPU"],
                ["Communication", "Send data between devices / networks", "NIC, modem, switch, hub, router, gateway, fax"],
            ],
        ),
        h("Input devices the board loves"),
        ul(
            "Barcode reader: optical scanner that reads product bars in a superstore for price and stock.",
            "OCR (Optical Character Recognition): reads printed text into editable text.",
            "OMR (Optical Mark Recognition): reads filled bubbles on MCQ sheets.",
            "MICR (Magnetic Ink Character Recognition): reads cheque numbers in banks.",
            "Scanner / data tablet / joystick / voice recognition / touch screen / webcam / microphone.",
        ),
        h("Output: hardcopy vs softcopy"),
        table(
            ["", "Hardcopy", "Softcopy"],
            [
                ["Meaning", "Printed permanent copy", "Temporary display on screen"],
                ["Device", "Printer, plotter", "Monitor, speaker, projector"],
                ["Example", "Marksheet on paper", "Result on the college portal"],
            ],
        ),
        h("Printers"),
        table(
            ["Impact (hit the paper)", "Non-impact (no hit)"],
            [
                ["Dot matrix, daisy wheel, line printer", "Inkjet, laser, thermal"],
                ["Noisy, carbon copies possible", "Quiet, high quality"],
                ["Cheap per page for multipart forms", "Laser is fast for offices"],
            ],
        ),
        example(
            "Plotter: an output device that draws large maps, CAD drawings and banners with pens. Board 2026 asked: “What devices are useful to print huge drawing or maps?” Answer: plotter (drum or flatbed).",
        ),
        exam(
            "Ready differences: Hardcopy/Softcopy; Impact/Non-impact (four points); Barcode use in a superstore.",
        ),
        warn("A mouse is input, not output. A plotter is output, not a printer type you use for ordinary pages. Oracle is a DBMS, not an OS."),
        urdu(
            "ہارڈویئر چھونے والے حصے ہیں۔ ان پٹ کی بورڈ، ماؤس، بار کوڈ ریڈر؛ آؤٹ پٹ مانیٹر، پرنٹر، پلاٹر۔",
            "ہارڈ کاپی کاغذ پر چھپی کاپی ہے، سافٹ کاپی اسکرین پر۔ امپیکٹ پرنٹر کاغذ کو ٹکر مارتے ہیں، نان امپیکٹ (لیزر، انک جیٹ) نہیں مارتے۔",
        ),
        check(
            ("Is OMR an input or output device?", "Input — it reads marks from paper"),
            ("Which printer makes carbon copies?", "Impact / dot-matrix"),
        ),
    ],
    mcqs=[
        mcq("A scanning input device is:", ["Keyboard", "Mouse", "Track ball", "OMR"], "d"),
        mcq("Floppy disk and hard disk are types of:", ["Optical disk", "Magnetic tape", "Magnetic disk", "Flash memory"], "c"),
        mcq("A plotter is used to print:", ["Letters", "Huge drawings and maps", "Only photos", "Sound"], "b"),
    ],
    short=[
        "How can a barcode reader be useful in a superstore?",
        "Differentiate hardcopy and softcopy.",
        "Write any four differences between impact and non-impact printers.",
        "What devices print huge drawings or maps?",
    ],
    short_ans=[
        "It scans the bar code, fetches price and stock from the database, speeds billing and reduces typing errors.",
        "Hardcopy is printed paper (permanent); softcopy is on screen or speaker (temporary, easy to edit).",
        "Impact: strike paper, noisy, carbon copies, cheaper for forms. Non-impact: no strike, quiet, high quality, laser/inkjet.",
        "Plotters (and large-format printers).",
    ],
    long=["Classify computer hardware. Explain input and output devices with examples."],
))

add(lec(
    id="xi-03",
    grade="XI",
    unit="1",
    unit_title="Overview of Computer System",
    title="Software, translators, virus and cutting-edge technology",
    golden=True,
    slos=[
        "Distinguish system, application and utility software",
        "Explain compiler, interpreter, assembler and compare compiler with interpreter",
        "Define computer virus and name antiviruses",
        "Outline AI and cloud computing at Grade XI level",
    ],
    body=[
        defn("Software", "A set of programs, procedures and documentation that instruct the hardware."),
        table(
            ["Type", "Role", "Examples"],
            [
                ["System software", "Runs the computer; manages resources", "OS (Windows, Linux, macOS, Android), device drivers, BIOS"],
                ["Language translator", "Converts source code to machine code", "Compiler, interpreter, assembler"],
                ["Application software", "User jobs", "MS Word, Excel, Chrome, Turbo C IDE, Photoshop"],
                ["Utility", "Maintenance", "Antivirus, compression (WinRAR), disk cleanup, backup, data recovery"],
            ],
        ),
        h("Translators"),
        table(
            ["", "Compiler", "Interpreter"],
            [
                ["How", "Translates the whole program first, then runs the object code", "Translates and runs one statement at a time"],
                ["Speed", "Faster at run time", "Slower at run time"],
                ["Errors", "Shows a list of errors after compilation", "Stops at the first error"],
                ["Object file", "Creates .exe / .obj", "Usually no separate object file"],
                ["Example", "C, C++", "Python, BASIC (classic)"],
            ],
        ),
        p("Assembler translates assembly language (mnemonics) into machine code. Source code is the program you write; object code is the machine-language result."),
        h("Computer virus"),
        learn(
            "A computer virus is a malicious program that attaches itself to other files, replicates, and can damage data, steal information or slow the system. Worms spread on networks without a host file. Trojans pretend to be useful software. Ransomware locks files until a ransom is paid.",
            items=["Examples of viruses/malware: ILOVEYOU, WannaCry, Trojan horses, spyware, adware.",
                   "Antiviruses: Kaspersky, Avast, AVG, Norton, Bitdefender, Windows Defender, McAfee, Avira."],
        ),
        h("Cutting-edge technology (Unit 1.5)"),
        ul(
            "Artificial Intelligence (AI): making machines perform tasks that need human intelligence — speech, vision, expert advice. Applications: face unlock, chatbots, medical imaging, self-driving research.",
            "Cloud computing: using servers on the internet (Google Drive, Microsoft 365) so you need less local storage. Advantages: access anywhere, backup, pay-as-you-go, easy sharing.",
        ),
        exam("2026 Paper I: define virus with examples and name five antiviruses; compiler vs interpreter; HTML as the markup language for web pages."),
        warn("Windows is system software; MS Word is application software. A virus is software, not hardware. HTML is a markup language, not a full programming language like C, but BIEK MCQs still key it as the language of web pages."),
        urdu(
            "سافٹ ویئر پروگراموں کا مجموعہ ہے۔ سسٹم سافٹ ویئر کمپیوٹر چلاتا ہے، ایپلی کیشن صارف کا کام کرتی ہے، یوٹیلیٹی صفائی اور حفاظت کرتی ہے۔",
            "Compiler پورا پروگرام ایک ساتھ مشین کوڈ بناتا ہے، Interpreter لائن بہ لائن۔ وائرس نقصان دہ پروگرام ہے جو نقل کرتا ہے؛ اینٹی وائرس اس سے بچاتا ہے۔",
        ),
        check(
            ("Name three language translators.", "Compiler, interpreter, assembler"),
            ("Give two advantages of cloud computing.", "Access from anywhere; automatic backup / less local hardware"),
        ),
    ],
    mcqs=[
        mcq("A computer virus is a:", ["Signal", "Software", "Hardware", "Firmware"], "b"),
        mcq("Windows is an example of:", ["Application software", "System software", "Utility only", "Compiler"], "b"),
        mcq("The markup language used to produce web pages is:", ["XML", "HTML", "SGML", "WML"], "b"),
        mcq("C programs are converted into machine language by a:", ["Editor", "Assembler", "Compiler", "Debugger"], "c"),
    ],
    short=[
        "How is a compiler more efficient than an interpreter?",
        "Define computer virus with examples. Name any five antiviruses.",
        "Differentiate system software and application software.",
    ],
    short_ans=[
        "A compiler translates the whole program once into object code which then runs fast. An interpreter translates every line each time the program runs, so it is slower and stops at the first error.",
        "A virus is malicious replicating software (examples: worms, Trojans, ransomware). Antiviruses: Kaspersky, Avast, Norton, Bitdefender, Windows Defender.",
        "System software controls hardware (OS, drivers). Application software does user tasks (Word, browser, Turbo C).",
    ],
    long=["Explain types of software. Discuss language translators with a comparison of compiler and interpreter."],
))

add(lec(
    id="xi-04",
    grade="XI",
    unit="2",
    unit_title="Computer Memory",
    title="Memory units, RAM, ROM and measurement",
    golden=True,
    slos=[
        "State bit, nibble, byte and the binary prefixes KB–TB",
        "Differentiate volatile and non-volatile memory",
        "Explain RAM (SRAM, DRAM) and ROM (PROM, EPROM, EEPROM)",
        "Compare primary and secondary memory",
    ],
    body=[
        table(
            ["Unit", "Size"],
            [
                ["Bit", "0 or 1 — smallest unit of data"],
                ["Nibble", "4 bits"],
                ["Byte", "8 bits — stores one character"],
                ["KB (Kilobyte)", "1024 bytes"],
                ["MB (Megabyte)", "1024 KB"],
                ["GB (Gigabyte)", "1024 MB"],
                ["TB (Terabyte)", "1024 GB"],
            ],
            center=False,
        ),
        svg(ram_rom(), "Primary memory: RAM vs ROM."),
        learn(
            "Primary / main memory sits on the motherboard and is directly used by the CPU. RAM is volatile: its contents vanish when power is cut. ROM is non-volatile: it keeps BIOS even when the PC is off.",
        ),
        table(
            ["RAM", "ROM"],
            [
                ["Random Access Memory", "Read Only Memory"],
                ["Read and write", "Mostly read; writing needs special process"],
                ["Volatile", "Non-volatile"],
                ["Stores OS + running programs + data", "Stores firmware / BIOS"],
                ["Larger, cheaper per bit (DRAM)", "Smaller"],
            ],
        ),
        h("RAM types"),
        ul(
            "SRAM (Static): uses flip-flops, faster, used as cache, more expensive, no refresh.",
            "DRAM (Dynamic): uses capacitors, needs refresh, cheaper, used as main memory.",
            "SIMM = Single Inline Memory Module (board MCQ).",
        ),
        h("ROM types"),
        ul(
            "PROM: programmed once by the user.",
            "EPROM: erased with ultraviolet light, then reprogrammed.",
            "EEPROM: electrically erased and reprogrammed, used for modern BIOS.",
        ),
        exam("MCQ: 1 GB = 1024 MB. Never write 1000. Difference of primary vs secondary: speed, volatility, capacity, CPU distance, cost."),
        warn("1 GB is 1024 MB, not 1024 KB. Cache is high-speed SRAM inside or near the CPU, not the hard disk."),
        urdu(
            "سب سے چھوٹی اکائی بٹ ہے (0 یا 1)۔ آٹھ بٹ کا بائٹ ایک حرف رکھتا ہے۔ 1024 بائٹ = 1 KB۔",
            "RAM عارضی ہے، بجلی جانے پر خالی۔ ROM مستقل ہے، BIOS رکھتی ہے۔ SRAM تیز کیش ہے، DRAM مین میموری ہے۔",
        ),
        check(
            ("Convert: 2 KB = ? bytes", "2 × 1024 = 2048 bytes"),
            ("Which ROM is erased by UV light?", "EPROM"),
        ),
    ],
    mcqs=[
        mcq("1 Gigabyte is equivalent to:", ["1024 KB", "1024 Bytes", "1024 MB", "1024 TB"], "c"),
        mcq("SIMM is the abbreviation of:", ["Single interfacing Memory Module", "Simple Inline Memory Module", "Single Inline Memory Module", "Simple Inline Memory Mode"], "c"),
        mcq("Smallest unit of data is:", ["Bit", "Byte", "Megabyte", "Nibble"], "a"),
    ],
    short=["Differentiate RAM and ROM.", "Explain SRAM and DRAM.", "Write memory measurement units from bit to TB."],
    short_ans=[
        "RAM: volatile R/W working memory. ROM: non-volatile firmware memory. RAM loses data without power; ROM does not.",
        "SRAM is fast cache without refresh. DRAM is cheaper main memory that must be refreshed.",
        "Bit, nibble (4 bits), byte (8 bits), KB, MB, GB, TB — each step ×1024 except bit/nibble/byte.",
    ],
    long=["What is computer memory? Explain primary memory and its types with a comparison table."],
))

add(lec(
    id="xi-05",
    grade="XI",
    unit="2",
    unit_title="Computer Memory",
    title="Secondary storage and memory devices",
    golden=True,
    slos=[
        "Explain magnetic, optical and solid-state secondary storage",
        "Give examples: HDD, USB, SD, CD/DVD/Blu-ray, external drive",
        "Compare primary memory with secondary storage for a long answer",
    ],
    body=[
        defn("Secondary memory", "Non-volatile storage used to keep programs and data permanently, cheaper and larger than RAM but slower."),
        table(
            ["Family", "How it stores", "Examples"],
            [
                ["Magnetic", "Magnetised spots on spinning platters / tape", "Hard disk, floppy (old), magnetic tape"],
                ["Optical", "Laser pits on disc", "CD, DVD, Blu-ray"],
                ["Solid state / flash", "Electric charge in chips, no moving parts", "USB flash, SSD, SD / MicroSD"],
            ],
        ),
        ul(
            "Hard disk drive (HDD): large capacity, inside the system unit, moving heads — slower than SSD.",
            "SSD: flash chips, silent, fast boot, used in modern laptops.",
            "USB / pen drive / data traveler: portable flash memory.",
            "SD / MicroSD: phones and cameras.",
            "Combo drive: CD+DVD reader/writer in one bay.",
            "External HDD: backup connected by USB.",
        ),
        table(
            ["Primary memory", "Secondary memory"],
            [
                ["On motherboard, used by CPU directly", "On disk / USB, used via I/O"],
                ["Fast, expensive, smaller", "Slow, cheap, huge"],
                ["RAM is volatile", "Non-volatile"],
                ["Measured in GB today", "Measured in GB–TB"],
            ],
        ),
        exam("2026 Section C: “Explain secondary storage devices with examples.” Write magnetic, optical, solid-state with two examples each and one use."),
        urdu(
            "ثانوی میموری مستقل ذخیرہ ہے: ہارڈ ڈسک، یو ایس بی، سی ڈی/ڈی وی ڈی، ایس ڈی کارڈ۔ یہ RAM سے سست لیکن سستی اور بڑی ہے۔",
        ),
        check(
            ("Why is a USB called solid-state storage?", "No moving parts; data in flash chips"),
            ("Which is faster for Windows boot: HDD or SSD?", "SSD"),
        ),
    ],
    mcqs=[
        mcq("A USB flash drive is an example of:", ["Optical storage", "Magnetic tape", "Solid-state storage", "Cache"], "c"),
        mcq("Blu-ray is a type of:", ["Magnetic disk", "Optical disc", "SRAM", "Register"], "b"),
    ],
    short=["Explain secondary storage devices with examples.", "Differentiate primary and secondary memory."],
    short_ans=[
        "Secondary storage is permanent: HDD/SSD (magnetic/solid state), CD/DVD/Blu-ray (optical), USB and SD (flash). Used for files, OS install and backup.",
        "Primary is fast, CPU-close, costly, RAM volatile. Secondary is slow, cheap, large, non-volatile.",
    ],
    long=["Explain secondary storage devices with examples. Compare them with primary memory."],
))

add(lec(
    id="xi-06",
    grade="XI",
    unit="3",
    unit_title="Inside System Unit",
    title="System unit, motherboard, ports and expansion slots",
    slos=[
        "Describe the system unit / CPU casing and its main parts",
        "Label motherboard components: CPU socket, RAM slots, BIOS, CMOS battery, buses, ports, expansion slots",
        "List serial, parallel, USB and HDMI ports",
        "State PCI / expansion slot purpose",
    ],
    body=[
        defn("System unit", "The case that houses the motherboard, power supply, drives, cooling fans and ports — the “CPU box” of a desktop."),
        ul(
            "Power supply (SMPS): converts 220 V AC to DC for components.",
            "Motherboard / main board: printed circuit that connects everything.",
            "Hard drive / combo drive bays.",
            "Ports on the back/front panel.",
            "Cooling: heat sink + fan, sometimes liquid cooling.",
        ),
        h("Motherboard components"),
        table(
            ["Part", "Function"],
            [
                ["Microprocessor socket", "Holds the CPU"],
                ["RAM slots", "DIMM / SIMM modules of main memory"],
                ["BIOS chip (ROM)", "Starts the computer, POST, finds boot device"],
                ["CMOS battery", "Keeps date, time and BIOS settings when PC is off"],
                ["Chipset", "Northbridge/southbridge traffic between CPU, memory, I/O"],
                ["Jumpers", "Tiny connectors that set hardware options"],
                ["Expansion slots", "PCI / PCIe cards: graphics, Wi-Fi, sound"],
                ["System bus", "Electrical pathways for address, data, control"],
            ],
        ),
        h("Ports"),
        table(
            ["Port", "Use"],
            [
                ["Serial (RS-232, old)", "One bit at a time; mouse/modem in old PCs"],
                ["Parallel (LPT)", "Several bits at a time; old printers"],
                ["USB", "Universal, hot-pluggable: keyboard, disk, phone"],
                ["HDMI", "High-Definition Multimedia Interface — video+audio to TV/monitor"],
                ["VGA", "Analog video (older monitors)"],
            ],
        ),
        tip("CMOS battery dead ⇒ date/time reset every boot, sometimes “disk boot failure” until BIOS is set again."),
        exam("Short: components of the system unit. Long: motherboard with a sketch of CPU, RAM, slots, ports."),
        urdu(
            "سسٹم یونٹ ڈیسک ٹاپ کا باکس ہے۔ مدر بورڈ سب کو جوڑتی ہے۔ پاور سپلائی بجلی دیتی ہے، پورٹس کی بورڈ اور مانیٹر لگاتے ہیں، USB عام پورٹ ہے۔ CMOS بیٹری تاریخ/وقت رکھتی ہے۔",
        ),
        check(
            ("Which port carries video and audio together?", "HDMI"),
            ("What does BIOS do at startup?", "POST and locate a bootable disk / OS"),
        ),
    ],
    mcqs=[
        mcq("The electrical path that carries data from one device to another is called:", ["Bus", "CPU", "Circuit only", "Chip"], "a"),
        mcq("USB stands for:", ["Universal Serial Bus", "United System Board", "Ultra Speed Bit", "Uniform Serial Box"], "a"),
    ],
    short=["Write the main components of a system unit.", "What is CMOS battery used for?", "Differentiate serial and USB ports."],
    short_ans=[
        "Power supply, motherboard, CPU, RAM, storage drives, cooling, ports, expansion cards.",
        "It powers CMOS memory so BIOS settings, date and time survive when the PC is unplugged.",
        "Serial (old) sends one bit at a time; USB is a modern serial bus that is fast, hot-pluggable and powers devices.",
    ],
    long=["Describe the motherboard. Explain its components with a labelled diagram."],
))

add(lec(
    id="xi-07",
    grade="XI",
    unit="3",
    unit_title="Inside System Unit",
    title="CPU, registers, buses and the fetch cycle",
    golden=True,
    slos=[
        "Describe ALU, CU, registers and cache",
        "Explain types of registers used in board answers",
        "Differentiate address, data and control buses",
        "Draw and explain the fetch–decode–execute cycle",
    ],
    body=[
        defn("Microprocessor / CPU", "The integrated circuit that fetches instructions from memory, decodes them and executes them. It is the brain of the computer."),
        table(
            ["Part", "Role"],
            [
                ["ALU (Arithmetic and Logic Unit)", "Add, subtract, AND, OR, NOT, compare"],
                ["CU (Control Unit)", "Directs the flow of data; sends control signals"],
                ["Registers", "Very fast storage inside the CPU for one instruction/data word"],
                ["Cache", "Small SRAM holding recently used instructions/data"],
                ["Clock", "Pulses that time every step (GHz)"],
            ],
        ),
        h("Registers (board favourite)"),
        ul(
            "ACC (Accumulator): stores ALU results.",
            "PC (Program Counter): address of the next instruction.",
            "IR (Instruction Register): the instruction currently being decoded.",
            "MAR (Memory Address Register): address being accessed in RAM.",
            "MDR (Memory Data Register): data coming from or going to RAM.",
            "General purpose registers: AX, BX, CX, DX in old x86 teaching notes.",
            "Flag register: zero, carry, sign bits after ALU operations.",
        ),
        h("Buses"),
        table(
            ["Bus", "Carries", "Direction"],
            [
                ["Address bus", "Memory / I/O addresses", "Unidirectional (CPU → memory)"],
                ["Data bus", "Actual data and instructions", "Bidirectional"],
                ["Control bus", "Read, write, interrupt, clock", "Mostly CPU → others (some lines back)"],
            ],
        ),
        svg(fetch_cycle(), "Instruction cycle. Board wording: Fetch Cycle (often they mean the whole fetch-execute cycle)."),
        learn(
            "Fetch: PC gives address, instruction copied from memory into IR, PC incremented. Decode: CU interprets the opcode. Execute: ALU or memory operation happens. Store/write-back: result goes to a register or RAM. Then the cycle repeats.",
        ),
        exam("2026 Q2(iv): “What is fetch Cycle? Draw its diagram.” Draw four boxes Fetch→Decode→Execute→Store with a loop arrow. Q3 OR: Computer Register and its types."),
        tip("Clock speed, word size (32/64 bit), cache size and number of cores decide CPU power. Generation: 1st vacuum tubes … 3rd ICs … 4th microprocessors … 5th AI."),
        urdu(
            "CPU میں ALU حساب کرتی ہے، CU حکم دیتی ہے، رجسٹر بہت تیز چھوٹی میموری ہیں۔",
            "Fetch سائیکل: میموری سے ہدایت لاؤ، سمجھو، چلاؤ، نتیجہ رکھو۔ ایڈریس بس پتہ لے جاتی ہے، ڈیٹا بس ڈیٹا، کنٹرول بس اشارے۔",
        ),
        check(
            ("Which register holds the next instruction address?", "Program Counter (PC)"),
            ("Is the data bus uni- or bi-directional?", "Bidirectional"),
        ),
    ],
    mcqs=[
        mcq("The third generation of computers used:", ["Vacuum tubes", "Transistors", "Integrated circuits", "Microprocessors"], "c"),
        mcq("ALU is a part of the:", ["Printer", "CPU", "Monitor", "Keyboard"], "b"),
    ],
    short=["What is the fetch cycle? Draw its diagram.", "What is a computer register? Explain its types.", "Differentiate address bus and data bus."],
    short_ans=[
        "The CPU repeatedly fetches an instruction from memory, decodes it, executes it and stores the result. Diagram: Fetch → Decode → Execute → Store, looping.",
        "A register is a small high-speed memory cell in the CPU. Types: accumulator, PC, IR, MAR, MDR, flags, general purpose.",
        "Address bus sends locations one way from CPU; data bus carries the bits both ways.",
    ],
    long=["Explain the internal architecture of a microprocessor. Draw and describe the fetch-execute cycle."],
))

add(lec(
    id="xi-08",
    grade="XI",
    unit="4",
    unit_title="Operating System",
    title="Operating system: types, features and examples",
    golden=True,
    slos=[
        "Define OS and its objectives",
        "Name Windows, macOS, DOS, UNIX/Linux, Android",
        "Explain batch, multi-tasking, time-sharing, multi-processing, distributed, embedded",
        "State that a computer cannot boot without an OS",
    ],
    body=[
        defn("Operating System", "System software that manages hardware and software resources and provides an interface between the user and the computer. It is loaded at boot time. A PC cannot boot without an OS."),
        p("Common OS: Microsoft Windows, Apple macOS, DOS (old command-line), UNIX and Linux (open source), Android and iOS for mobiles."),
        table(
            ["Feature", "Meaning", "Example"],
            [
                ["Batch processing", "Jobs queued; no user interaction while running", "Old payroll runs, mainframes"],
                ["Multi-tasking", "Several programs appear to run at once", "Browser + Word + music"],
                ["Time sharing", "CPU time sliced among users/processes", "University server"],
                ["Multi-processing", "Two or more CPUs / cores share work", "Dual-core laptop"],
                ["Parallel processing", "One job split across processors", "Scientific calculation"],
                ["Distributed", "Many computers act as one system", "Google data centres"],
                ["Embedded", "OS baked into a device", "ATM, microwave, car ECU, Android phone"],
            ],
        ),
        table(
            ["CLI (Command Line)", "GUI (Graphical User Interface)"],
            [
                ["Type commands (DIR, CD)", "Windows, icons, mouse"],
                ["Fast for experts, low memory", "Easy for beginners"],
                ["DOS, UNIX shell", "Windows, GNOME, macOS"],
            ],
        ),
        exam("Long 2026: “What is an Operating System? Explain its Functions.” Functions are the next lecture — keep definition + types here and functions ready."),
        warn("Oracle is a database, not an OS. Chrome is a browser (application). Linux is an OS."),
        urdu(
            "آپریٹنگ سسٹم وہ سافٹ ویئر ہے جو کمپیوٹر کو بوٹ کرتا ہے، ہارڈویئر سنبھالتا ہے اور صارف کو انٹرفیس دیتا ہے۔ ونڈوز، لینکس، اینڈرائیڈ مشہور OS ہیں۔",
            "ملٹی ٹاسکنگ کئی پروگرام ایک ساتھ؛ ایمبیڈڈ OS فریج یا موبائل کے اندر ہوتا ہے۔",
        ),
        check(
            ("Can a computer boot without an OS?", "No"),
            ("Give one embedded OS example.", "Android in a phone / OS in an ATM"),
        ),
    ],
    mcqs=[
        mcq("A computer cannot boot if it does not have a:", ["Compiler", "Browser", "Operating System", "Loader only"], "c"),
        mcq("Which is NOT a type of operating system?", ["Windows", "Linux", "Mac OS", "Oracle"], "d"),
        mcq("Windows is:", ["Application software", "System software", "A compiler", "Firmware only"], "b"),
    ],
    short=["Define operating system. Name four operating systems.", "Differentiate multi-tasking and multi-processing.", "What is an embedded operating system?"],
    short_ans=[
        "OS is system software that manages resources and lets the user run programs. Windows, Linux, macOS, Android.",
        "Multi-tasking: many programs on one CPU by time-slicing. Multi-processing: more than one processor executing at the same time.",
        "An OS built into a dedicated device (router, car, TV, mobile) with a specific job.",
    ],
    long=["What is an operating system? Explain its types / features with examples."],
))

add(lec(
    id="xi-09",
    grade="XI",
    unit="4",
    unit_title="Operating System",
    title="Functions of OS, process management and GUI",
    golden=True,
    slos=[
        "List and explain the functions of an OS",
        "Define process and thread; draw process states",
        "Use files, folders, Control Panel, msconfig, dxdiag at a theory level",
        "Mention open-source OS and mobile OS",
    ],
    body=[
        h("Functions of an operating system"),
        table(
            ["Function", "What the OS does"],
            [
                ["Booting", "POST, load kernel, start system services"],
                ["Process management", "Create, schedule, suspend, terminate processes"],
                ["Memory management", "Allocate RAM, virtual memory / paging"],
                ["File management", "Create, copy, delete, rename files and folders; FAT/NTFS"],
                ["I/O management", "Talk to keyboard, disk, printer via drivers"],
                ["Secondary storage management", "Free space, disk scheduling"],
                ["Network management", "TCP/IP, sharing, firewall basics"],
                ["Protection / security", "Passwords, permissions, user accounts"],
                ["Command interpreter / shell", "cmd, PowerShell, Bash, or GUI Explorer"],
            ],
        ),
        defn("Process", "A program in execution. A thread is a lightweight unit of a process that shares the same memory space. Multi-threading: many threads in one process. Multi-tasking: many processes."),
        svg(process_states(), "Process states: New → Ready → Running → Waiting or Terminated."),
        ul(
            "New: being created.",
            "Ready: waiting for CPU.",
            "Running: on the CPU.",
            "Waiting / blocked: waiting for I/O or an event.",
            "Terminated: finished or killed.",
        ),
        h("Working with a GUI OS (Windows)"),
        p("Create / delete / copy / rename files; search; attributes (Read-only, Hidden, Archive, System); drives and paths (C:\\Users\\Ali\\Notes.txt); Control Panel / Settings for hardware; dxdiag to list display and sound; msconfig to change startup programs."),
        p("Open-source OS (Linux, Ubuntu) can be studied, copied and improved freely. Mobile OS: Android versions, iOS."),
        exam("Long answer: OS definition + at least 7 functions with one line each. Short: process vs thread; five process states."),
        urdu(
            "OS بوٹ کرتا ہے، پروسیس اور میموری بانٹتا ہے، فائلیں سنبھالتا ہے، پرنٹر چلاتا ہے اور پاس ورڈ سے حفاظت کرتا ہے۔",
            "پروسیس چلتا ہوا پروگرام ہے۔ حالتیں: نیا، تیار، چل رہا، انتظار، ختم۔",
        ),
        check(
            ("Name five OS functions.", "Booting, process, memory, file, I/O (any five)"),
            ("Ready vs running?", "Ready waits for CPU; running currently has the CPU"),
        ),
    ],
    mcqs=[
        mcq("A program in execution is called a:", ["File", "Process", "Folder", "Port"], "b"),
        mcq("File management is a function of the:", ["Compiler", "Operating system", "Browser", "ALU"], "b"),
    ],
    short=["Explain the functions of an operating system.", "Differentiate process and thread.", "Write the states of a process."],
    short_ans=[
        "Booting, process, memory, file, I/O, storage, network, protection, command interpreter — each in one sentence as in the table.",
        "Process: whole program in execution with its own memory. Thread: a path inside a process sharing memory; lighter to create.",
        "New, Ready, Running, Waiting/Blocked, Terminated.",
    ],
    long=["What is an Operating System? Explain its functions. Also describe process management."],
))

add(lec(
    id="xi-10",
    grade="XI",
    unit="7",
    unit_title="Computer Communication & Networks",
    title="Data communication: components, signals and modes",
    golden=True,
    slos=[
        "Define data communication and its five components",
        "Differentiate analog and digital signals",
        "Explain simplex, half duplex and full duplex",
        "Define modulation, demodulation, synchronous and asynchronous transmission",
    ],
    body=[
        defn("Data communication", "The exchange of data between two devices through a transmission medium according to a protocol."),
        p("Five components (board list): Sender, Receiver, Message, Medium, Protocol."),
        svg(simplex_modes(), "Direction of data flow."),
        table(
            ["Mode", "Direction", "Example"],
            [
                ["Simplex", "One way only", "Radio, keyboard → CPU, TV broadcast"],
                ["Half duplex", "Both ways, not at the same time", "Walkie-talkie"],
                ["Full duplex", "Both ways at the same time", "Telephone, mobile call"],
            ],
        ),
        h("Analog vs digital"),
        table(
            ["Analog signal", "Digital signal"],
            [
                ["Continuous wave, infinite values", "Discrete 0 and 1 pulses"],
                ["Human voice, old telephone line", "Computers, optical fibre (light pulses)"],
                ["Noise distorts easily", "More reliable, regenerable"],
            ],
        ),
        defn("Modulation", "Converting a digital signal into analog so it can travel on a telephone line (ASK/FSK/PSK). Performed by a modem on send."),
        defn("Demodulation", "Converting the analog signal back to digital at the receiving modem."),
        p("MODEM = MOdulator + DEModulator."),
        table(
            ["Asynchronous", "Synchronous"],
            [
                ["Start and stop bits around each character", "A timing clock; data sent in blocks/frames"],
                ["Cheaper, slower, keyboard typing", "Faster, used on networks"],
            ],
        ),
        p("Broadcast: one sender, many receivers (TV, radio). Point-to-point: one sender, one receiver (phone call)."),
        exam("2026 shorts: analog vs digital; modulation/demodulation; broadcast vs point-to-point; components of data communication; half duplex MCQ."),
        warn("Full duplex is both directions simultaneously. Half duplex is both directions but one at a time. Students mix these every year."),
        urdu(
            "ڈیٹا کمیونیکیشن میں بھیجنے والا، وصول کرنے والا، پیغام، میڈیم اور پروٹوکول ہوتے ہیں۔",
            "Simplex ایک طرف، Half duplex باری باری دونوں طرف، Full duplex ایک ساتھ دونوں طرف۔ Modulation ڈیجیٹل کو اینالاگ بناتا ہے، Demodulation الٹ۔",
        ),
        check(
            ("Telephone is which mode?", "Full duplex"),
            ("Modem expands to?", "Modulator Demodulator"),
        ),
    ],
    mcqs=[
        mcq("A mode that allows two directions but not simultaneously is:", ["Full duplex", "Half duplex", "Synchronous", "Simplex"], "b"),
        mcq("Converting analog to digital is called:", ["Modulation", "Telecommunicating", "Demodulation", "Switching"], "c"),
        mcq("Protocol means:", ["A topology", "A set of rules", "A router", "A modem"], "b"),
    ],
    short=[
        "Name the components of data communication.",
        "Differentiate analog and digital signals.",
        "What is modulation and demodulation?",
        "Differentiate broadcast and point-to-point.",
        "Differentiate synchronous and asynchronous transmission.",
    ],
    short_ans=[
        "Sender, receiver, message, medium, protocol.",
        "Analog is continuous; digital is 0/1. Digital resists noise better.",
        "Modulation: digital→analog for the line. Demodulation: analog→digital. Modem does both.",
        "Broadcast: one-to-many. Point-to-point: one-to-one.",
        "Async uses start/stop bits per character. Sync uses a clock and sends blocks — faster.",
    ],
    long=["Explain data communication. Describe communication modes and analog/digital signals with diagrams."],
))

add(lec(
    id="xi-11",
    grade="XI",
    unit="7",
    unit_title="Computer Communication & Networks",
    title="Transmission media and network devices",
    golden=True,
    slos=[
        "Classify guided and unguided media",
        "Describe twisted pair, coaxial and fibre optic",
        "Describe radio, microwave and infrared",
        "Explain NIC, modem, hub, switch, router, bridge, gateway",
    ],
    body=[
        h("Guided (wired) media"),
        table(
            ["Medium", "Construction", "Use / note"],
            [
                ["Twisted pair", "Pairs of copper wires twisted (UTP/STP)", "LAN cables Cat5/Cat6; cheap"],
                ["Coaxial", "Core, insulation, metal shield, jacket", "Old TV cable, some backbone"],
                ["Fibre optic", "Glass/plastic, light pulses", "Very fast, long distance, no EMI"],
            ],
        ),
        h("Unguided (wireless) media"),
        ul(
            "Radio waves: FM radio, Wi-Fi, Bluetooth, cellular.",
            "Microwaves: line-of-sight dishes, some mobile backhaul.",
            "Infrared: TV remote, old short laptop links; blocked by walls.",
        ),
        h("LAN / communication devices"),
        table(
            ["Device", "Job"],
            [
                ["NIC (Network Interface Card)", "Fits in PC; has MAC address"],
                ["Hub", "Repeats bits to all ports (old, collisions)"],
                ["Switch", "Forwards frames to the correct port using MAC"],
                ["Bridge", "Connects two similar LANs / segments"],
                ["Router", "Connects different networks using IP; path to the internet"],
                ["Gateway", "Connects two different networks/protocols (e.g. LAN to mainframe)"],
                ["Modem", "Analog↔digital for the phone/cable line"],
                ["Access point", "Wi-Fi radio for wireless clients"],
            ],
        ),
        exam("2026: coaxial and fibre are communication media; bridge connects two similar networks; router/gateway for different networks; SMTP is the common email protocol."),
        tip("Memory: Switch is smart hub. Router is smart switch that knows IP. Gateway is a protocol translator. Bridge = two similar LANs."),
        urdu(
            "گائیڈڈ میڈیم تار ہے: ٹوئسٹڈ پیئر، کواکسیئل، فائبر آپٹک۔ ان گائیڈڈ ریڈیو، مائیکرو ویو، انفراریڈ۔",
            "سوئچ LAN کے کمپیوٹر جوڑتا ہے، روٹر مختلف نیٹ ورک اور انٹرنیٹ، بریج دو ملتے جلتے LAN، گیٹ وے مختلف پروٹوکول۔",
        ),
        check(
            ("Which cable uses light?", "Fibre optic"),
            ("Which device uses IP addresses to connect networks?", "Router"),
        ),
    ],
    mcqs=[
        mcq("Coaxial cable and fibre optics are examples of:", ["Router", "Communication media", "Modem", "Switch"], "b"),
        mcq("The LAN component that connects two similar networks is:", ["Server", "Bridge", "Router", "Gateway"], "b"),
        mcq("The most common protocol used for e-mail is:", ["FTP", "TCP/IP", "SMTP", "IEEE"], "c"),
    ],
    short=[
        "Explain data communication channels / transmission media with examples.",
        "Define the LAN component which allows communication between two different networks.",
        "Differentiate hub and switch.",
    ],
    short_ans=[
        "Guided: twisted pair, coaxial, fibre. Unguided: radio, microwave, infrared. Fibre is fastest and immune to electrical noise.",
        "Router or gateway. A router forwards IP packets between networks; a gateway also converts protocols.",
        "Hub broadcasts to all ports; switch sends a frame only to the destination MAC port.",
    ],
    long=["Explain data communication channels with examples. Describe common networking devices."],
))

add(lec(
    id="xi-12",
    grade="XI",
    unit="7",
    unit_title="Computer Communication & Networks",
    title="Networks, topologies and architecture",
    golden=True,
    slos=[
        "Define network and its advantages",
        "Classify LAN, MAN, WAN",
        "Draw bus, star, ring, mesh, tree, hybrid topologies",
        "Name ISO, IEEE, ITU; introduce OSI and TCP/IP",
    ],
    body=[
        defn("Computer network", "Two or more computers connected to share resources (files, printers, internet) and communicate."),
        p("Advantages: resource sharing, cheaper software/hardware per user, easy communication, central backup. Disadvantages: security risk, server failure, cabling cost, viruses spread faster."),
        table(
            ["Type", "Span", "Example"],
            [
                ["LAN", "Room, lab, building", "College computer lab"],
                ["MAN", "City", "Cable TV / city Wi-Fi backbone"],
                ["WAN", "Country / world", "Internet, bank branches"],
            ],
        ),
        svg(topologies(), "Four topologies every Section C diagram should match."),
        table(
            ["Topology", "How linked", "Plus / minus"],
            [
                ["Bus", "One backbone cable", "Cheapest; cable break kills the LAN; BIEK MCQ: cheapest topology"],
                ["Star", "Each node to a hub/switch", "Easy to add PCs; centre fails ⇒ all fail"],
                ["Ring", "Circle, token passing (old)", "Equal access; one break can stop ring"],
                ["Mesh", "Many-to-many", "Very reliable; expensive"],
                ["Tree", "Stars of stars", "Scalable campus"],
                ["Hybrid", "Mix", "Real offices"],
            ],
        ),
        p("Standard bodies: ISO (OSI model), IEEE (802.3 Ethernet, 802.11 Wi-Fi), ITU (telecom), ASCII (character codes — often listed with them in the Sindh book)."),
        exam("Long 2026 OR: “What is meant by Computer Network? Classify by their scale and limitation.” Write LAN/MAN/WAN with distance and one limitation each, then topologies with diagrams."),
        urdu(
            "نیٹ ورک دو یا زیادہ کمپیوٹر جو وسائل بانٹتے ہیں۔ LAN عمارت، MAN شہر، WAN دنیا (انٹرنیٹ)۔",
            "بس سب سے سستی، اسٹار سوئچ پر، رنگ دائرہ، میش ہر ایک سے ہر ایک۔",
        ),
        check(
            ("Internet is which scale of network?", "WAN"),
            ("Cheapest topology?", "Bus"),
        ),
    ],
    mcqs=[
        mcq("The cheapest topology is:", ["Ring", "Bus", "Tree", "Star"], "b"),
        mcq("OSI model contains:", ["six layers", "five layers", "three layers", "seven layers"], "d"),
        mcq("Which is NOT a type of computer network?", ["LAN", "MAN", "WAN", "CPU"], "d"),
    ],
    short=["What is a computer network? Give advantages.", "Differentiate LAN and WAN.", "Write short notes on star and bus topology."],
    short_ans=[
        "Linked computers sharing resources. Advantages: sharing, communication, backup, cost.",
        "LAN is local and fast (lab). WAN covers large distance (internet) and is slower/more expensive.",
        "Star: nodes to central switch, easy management. Bus: shared cable, cheap, collision and break problems.",
    ],
    long=["What is meant by a computer network? Classify by scale and explain topologies with diagrams."],
))

add(lec(
    id="xi-13",
    grade="XI",
    unit="7",
    unit_title="Computer Communication & Networks",
    title="OSI reference model, TCP/IP and internet protocols",
    golden=True,
    slos=[
        "Draw seven OSI layers with one function and one protocol/device each",
        "Map TCP/IP four layers onto OSI",
        "Define protocol, TCP, IP, HTTP, FTP, SMTP, DNS, URL",
    ],
    body=[
        defn("Protocol", "A set of rules that sender and receiver follow so communication is understood (format, timing, error handling)."),
        svg(osi_layers(), "ISO OSI 7-layer model — learn bottom to top: Please Do Not Throw Sausage Pizza Away (Physical → Application)."),
        learn(
            "Physical: bits on wire. Data link: frames, MAC, switch. Network: packets, IP, router. Transport: segments, TCP (reliable) / UDP (fast). Session: connections. Presentation: encrypt/compress. Application: user programs.",
        ),
        table(
            ["TCP/IP layer", "OSI layers", "Examples"],
            [
                ["Application", "5+6+7", "HTTP, SMTP, FTP, DNS"],
                ["Transport", "4", "TCP, UDP"],
                ["Internet", "3", "IP, ICMP"],
                ["Network access / Link", "1+2", "Ethernet, Wi-Fi"],
            ],
        ),
        table(
            ["Protocol", "Use"],
            [
                ["TCP/IP", "Suite that runs the internet"],
                ["HTTP / HTTPS", "Web pages (S = encrypted)"],
                ["FTP", "File transfer"],
                ["SMTP", "Sending email"],
                ["POP3 / IMAP", "Receiving email"],
                ["DNS", "Name → IP (www.biek.edu.pk)"],
                ["URL", "Uniform Resource Locator — web address"],
            ],
        ),
        example(
            "URL example: https://www.biek.edu.pk/index.html — protocol https, host www.biek.edu.pk, path /index.html.",
        ),
        exam("2026 long: Draw and explain OSI. Also MCQ: seven layers; SMTP for email. Write one sentence per layer and a small stack diagram."),
        urdu(
            "OSI ماڈل سات تہوں میں نیٹ ورک سمجھاتا ہے: فزیکل سے ایپلی کیشن تک۔ TCP/IP انٹرنیٹ کا عملی ماڈل ہے (چار تہیں)۔",
            "پروٹوکول قواعد ہیں: SMTP ای میل بھیجنے، HTTP ویب، FTP فائل۔ URL ویب ایڈریس ہے۔",
        ),
        check(
            ("How many OSI layers?", "Seven"),
            ("Which protocol sends email?", "SMTP"),
        ),
    ],
    mcqs=[
        mcq("OSI model has:", ["4 layers", "5 layers", "6 layers", "7 layers"], "d"),
        mcq("URL stands for:", ["Universal Resource Locator", "Uniform Resource Locator", "Unique Resource Locator", "Ultimate Resource Locator"], "b"),
        mcq("HTTP works at the OSI:", ["Physical layer", "Network layer", "Application layer", "Data link layer"], "c"),
    ],
    short=["Write the seven layers of the OSI model.", "Differentiate TCP/IP and OSI.", "What is a protocol? Give three examples."],
    short_ans=[
        "Physical, Data Link, Network, Transport, Session, Presentation, Application — with one function each.",
        "OSI is a 7-layer ISO reference model. TCP/IP is the 4-layer practical internet model. TCP/IP application covers OSI 5–7.",
        "Rules of communication. TCP, IP, HTTP, SMTP, FTP.",
    ],
    long=["Draw and explain the OSI reference model. Give protocols at each layer."],
))

add(lec(
    id="xi-14",
    grade="XI",
    unit="1–4",
    unit_title="Paper I mixed theory",
    title="Number sense, generations, abbreviations and security recap",
    slos=[
        "Recall computer generations",
        "Expand the abbreviations that appear every year",
        "Restate virus / antivirus and basic security",
        "Keep a one-page formula sheet for Paper I",
    ],
    body=[
        table(
            ["Generation", "Technology", "Example / note"],
            [
                ["1st (1940s–50s)", "Vacuum tubes", "ENIAC, huge, hot"],
                ["2nd", "Transistors", "Smaller, more reliable"],
                ["3rd", "Integrated circuits (ICs)", "Board MCQ favourite"],
                ["4th", "Microprocessor", "IBM PC, personal computers"],
                ["5th", "AI, ULSI, natural language", "Modern research / assistants"],
            ],
        ),
        h("Full forms to memorise"),
        table(
            ["Abbrev.", "Full form"],
            [
                ["CPU", "Central Processing Unit"],
                ["ALU / CU", "Arithmetic and Logic Unit / Control Unit"],
                ["RAM / ROM / BIOS", "Random Access Memory / Read Only Memory / Basic Input Output System"],
                ["USB / HDMI / VGA", "Universal Serial Bus / High-Definition Multimedia Interface / Video Graphics Array"],
                ["OCR / OMR / MICR / CRT", "Optical Character / Mark / Magnetic Ink Character Recognition / Cathode Ray Tube"],
                ["GUI / CLI / OS", "Graphical User Interface / Command Line Interface / Operating System"],
                ["LAN / MAN / WAN / NIC", "Local / Metropolitan / Wide Area Network / Network Interface Card"],
                ["OSI / ISO / IEEE / SMTP / FTP / HTTP / DNS / URL / IP / TCP", "Open Systems Interconnection / International Organization for Standardization / Institute of Electrical and Electronics Engineers / Simple Mail Transfer Protocol / File Transfer Protocol / HyperText Transfer Protocol / Domain Name System / Uniform Resource Locator / Internet Protocol / Transmission Control Protocol"],
                ["SIMM / SRAM / DRAM / EEPROM", "Single Inline Memory Module / Static / Dynamic RAM / Electrically Erasable PROM"],
                ["AI / ICT / IT", "Artificial Intelligence / Information and Communication Technology / Information Technology"],
            ],
        ),
        tip("Every night before the paper, write this table from memory. Section B often says “write full form of any three”."),
        urdu(
            "جنریشن: ٹیوب، ٹرانزسٹر، IC، مائیکرو پروسیسر، AI۔ مخففات روزانہ لکھ کر یاد کریں — BIOS, SMTP, OCR, GUI۔",
        ),
        check(
            ("3rd generation technology?", "Integrated circuits"),
            ("BIOS full form?", "Basic Input Output System"),
        ),
    ],
    mcqs=[
        mcq("OCR stands for:", ["Optical Character Recognition", "Original Code Reader", "Output Card Reader", "Open Computer RAM"], "a"),
        mcq("GUI stands for:", ["General User Internet", "Graphical User Interface", "Global Unique ID", "General Utility Input"], "b"),
    ],
    short=["Write full forms of OCR, GUI, BIOS, SMTP, USB.", "Write a short note on computer generations."],
    short_ans=[
        "OCR Optical Character Recognition; GUI Graphical User Interface; BIOS Basic Input Output System; SMTP Simple Mail Transfer Protocol; USB Universal Serial Bus.",
        "Five generations from vacuum tubes to microprocessors and AI, each smaller, faster and cheaper.",
    ],
))

add(lec(
    id="xi-15",
    grade="XI",
    unit="5–6",
    unit_title="Programming bridge (Sindh XI C++)",
    title="Programming concepts that start in XI and are examined in XII",
    slos=[
        "Know that BIEK examines C in Paper II, while the Sindh 2019 book uses C++ in XI",
        "Recall algorithm, flowchart, source vs object code, IDE",
        "Preview data types, control structures, arrays and functions",
    ],
    body=[
        warn(
            "Karachi Board Paper I (XI) is theory. Full C programs are Paper II. Still, Sindh Unit 5–6 expect you to practise C++ in the lab in Year 1. This lecture is the bridge; Class XII lectures teach C in exam style.",
        ),
        defn("Algorithm", "A step-by-step finite method to solve a problem. Pseudocode is the algorithm in English-like lines. A flowchart uses standard symbols (terminal, process, input/output, decision)."),
        defn("IDE", "Integrated Development Environment — editor + compiler + debugger in one window (Turbo C++, Dev-C++, VS Code). Shortcuts in Turbo C: F2 save, F9 compile, Ctrl+F9 run, Alt+F5 user screen."),
        p("C/C++ program structure: preprocessor (#include), global declarations, main(), statements, return. Tokens: keywords, identifiers, constants, operators, separators. C is case-sensitive: int is a keyword, Int is not."),
        table(
            ["Idea", "C / C++ sketch"],
            [
                ["Input / output", 'scanf("%d", &n);  printf("%d", n);  or cin >> n; cout << n;'],
                ["Selection", "if, if-else, else-if, switch-case, nested if"],
                ["Loop", "for, while, do-while, nested loops; break, continue, goto"],
                ["Function", "return-type name(parameters) { body }"],
                ["Array", "int a[5] = {1,2,3,4,5};"],
                ["String", 'char s[20] = "BIEK"; strlen, strcpy, strcat, strcmp'],
                ["Structure", "struct Employee { char name[20]; float salary; };"],
            ],
        ),
        code(r'''
#include <stdio.h>
int main(void) {
    int m1 = 80, m2 = 70, m3 = 90;
    float avg = (m1 + m2 + m3) / 3.0f;
    if (avg >= 40) printf("Pass %.2f\n", avg);
    else printf("Fail\n");
    return 0;
}
'''),
        p("Lab list from the Sindh curriculum (XI): calculator, marksheet, prime test, digits of a number, factors, star pattern, larger of two via function, sort array, search, matrix add/multiply, reverse a name with strlen, employee structure."),
        urdu(
            "الخوارزم مسئلہ حل کرنے کے قدم ہیں۔ فلو چارٹ خاکہ ہے۔ IDE میں کوڈ لکھ کر چلاتے ہیں۔ BIEK کے پیپر ٹو میں C زبان آتی ہے — اگلی کتاب (XII) میں پوری مشق ہے۔",
        ),
        check(
            ("F9 in Turbo C?", "Compile"),
            ("Is C case-sensitive?", "Yes"),
        ),
    ],
    mcqs=[
        mcq("An IDE is used to:", ["Print books", "Write and run programs", "Scan photos only", "Connect fibre"], "b"),
        mcq("Which is a loop structure?", ["if", "switch", "for", "goto only"], "c"),
    ],
    short=["What is an IDE? Write a few shortcut keys.", "Differentiate source code and object code.", "Why is C called case-sensitive?"],
    short_ans=[
        "IDE combines editor, compiler and debugger. Turbo C: F2 save, F9 compile, Ctrl+F9 run, Alt+F5 output screen.",
        "Source code is human-written (file.c). Object/machine code is the compiler output that the CPU runs.",
        "Uppercase and lowercase letters are different: TOTAL and total are two identifiers; keywords must be lowercase (int, not INT).",
    ],
))

add(lec(
    id="xi-16",
    grade="XI",
    unit="R",
    unit_title="Revision",
    title="Paper I mock (BIEK 2026 style) with model answers",
    golden=True,
    slos=[
        "Attempt a full Paper I in one sitting",
        "Match answers to the marking style of Section B and C",
    ],
    body=[
        h("Section A — 15 MCQs (key at the end)"),
        p("1) 1 GB = ?  (a) 1024 KB (b) 1024 B (c) 1024 MB (d) 1024 TB"),
        p("2) Floppy and hard disk are (a) optical (b) magnetic tape (c) magnetic disk (d) flash"),
        p("3) SIMM means (c) Single Inline Memory Module"),
        p("4) OSI layers (d) seven"),
        p("5) Cheapest topology (b) Bus"),
        p("6) Virus is (b) software"),
        p("7) Scanning input (d) OMR"),
        p("8) Path for data between devices (a) Bus"),
        p("9) Two similar networks (b) Bridge"),
        p("10) Coaxial and fibre are (b) communication media"),
        p("11) Web markup (b) HTML"),
        p("12) Email send protocol (c) SMTP"),
        p("13) Analog→digital (c) demodulation"),
        p("14) Rules on the internet (b) protocol"),
        p("15) Two ways not together (b) half duplex"),
        h("Section B — write 6–8 lines each"),
        ol(
            "IT: definition + 3 uses + 3 abuses  OR  barcode in a superstore.",
            "Hardcopy vs softcopy  OR  sync vs async transmission.",
            "Virus + 5 antiviruses  OR  plotter.",
            "Fetch cycle + diagram  OR  five communication components.",
            "Modulation/demodulation  OR  compiler vs interpreter.",
            "Four differences: impact vs non-impact printers.",
            "Device that joins two different networks (router/gateway).",
            "Analog vs digital.",
            "Broadcast vs point-to-point.",
            "Full forms: OCR, GUI, SVGA, CRT, BIOS (any three).",
        ),
        h("Section C — diagrams compulsory"),
        ol(
            "OS and its functions  OR  registers and types.",
            "Communication channels with examples  OR  secondary storage.",
            "OSI model  OR  network classification by scale + topologies.",
        ),
        h("MCQ key"),
        p("1c 2c 3c 4d 5b 6b 7d 8a 9b 10b 11b 12c 13c 14b 15b"),
        example(
            "Model long: OSI — Draw seven labelled rectangles. Write: Physical bits; Data link frames/MAC; Network IP/routing; Transport TCP ports; Session dialogues; Presentation encryption; Application HTTP/SMTP. Mention ISO. 8–10 marks if diagram + all layers are named.",
        ),
        urdu(
            "ماک پیپر اسی انداز کا ہے جیسا 2026 ماڈل پیپر۔ پہلے MCQ، پھر مختصر، پھر خاکوں والے لمبے سوال۔ وقت تقسیم کریں: 20 منٹ MCQ، باقی دو حصے برابر۔",
        ),
        tip("On the real OMR: blue/black ballpoint only, no whitener. In the answer book, underline headings and box the final comparison table."),
    ],
    mcqs=[
        mcq("Paper I mock key starts with 1 GB = 1024 MB. That option is:", ["a", "b", "c", "d"], "c"),
    ],
    long=["Attempt Section C question 3 of this mock under timed conditions and compare with the OSI model lecture."],
))
