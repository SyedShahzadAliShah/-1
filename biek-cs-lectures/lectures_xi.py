"""Original Class XI lectures for BIEK Computer Science Paper I."""

META = {
    "pdf_title": "BIEK Computer Science XI — Lecture Notes",
    "class_label": "Class XI",
    "running_header": "Computer Science  ·  Class XI  ·  Paper I",
    "cover_lines": ["Computer Science", "Class XI Lectures"],
    "cover_sub": "Paper I  ·  Science General Group  ·  Model Paper 2026",
    "cover_foot": "Theory paper  ·  75 marks  ·  Section A, B and C",
    "intro": (
        "These lectures prepare you for BIEK Computer Science Paper I, the theory paper. "
        "They follow the course set in the Board’s Model Paper 2026: information technology, "
        "hardware, the system unit, software, operating systems, data communication, networks "
        "and security. A newer Sindh curriculum also introduces C++ in Class XI. That is not "
        "the Paper I printed in the 2026 model papers, so it is not taught here. "
        "Read one lecture, attempt the checkpoint with the answers covered, then check your wording."
    ),
    "pattern_headers": ["Section", "What you do", "Marks", "Time"],
    "pattern_rows": [
        ["A  MCQs", "All 15 questions. One mark each. Fill the OMR with a blue or black ballpoint.", "15", "20 minutes"],
        ["B  Short", "All part questions. Many have an OR. About six or seven lines.", "30", "2 hours 40 minutes, shared with Section C"],
        ["C  Detailed", "All long questions. Each has an OR. About one page, with a heading and clear points.", "30", "Same sitting as Section B"],
    ],
    "pattern_widths": [90, 250, 70, 90],
    "pattern_note": (
        "When a part says OR, answer only one side. Pick the side you can explain with an example. "
        "A labelled diagram is worth marks in the fetch cycle, the OSI model and network types. "
        "Define the term in the first line, then give the points the question asked for."
    ),
}

LECTURES = [
    {
        "number": 1,
        "title": "Information Technology and the Computer",
        "meta": "Two periods  ·  Start of Paper I  ·  Uses and abuses of IT are a regular short question",
        "outcomes": [
            "Define computer, data, information, program and information technology.",
            "Draw the block diagram of a computer and name the four basic jobs.",
            "Write a short answer on uses or abuses of IT.",
            "Separate hardware from software with examples.",
        ],
        "blocks": [
            {"kind": "h2", "text": "What a computer is"},
            {
                "kind": "p",
                "text": "A computer is an electronic machine that accepts data, processes it according to a stored set of instructions, and produces a result. The raw facts and figures fed in are **data**. Data becomes **information** when processing gives it meaning. The set of instructions is a **program**, and programs together are **software**. The physical parts you can touch are **hardware**.",
            },
            {
                "kind": "p",
                "text": "**Information technology** is the use of computers, storage and communication equipment to create, store, protect, exchange and use information. A college attendance system, a bank ATM and a WhatsApp message are all IT at work. The computer is the processing tool. IT is the whole activity of handling information with that tool and with networks.",
            },
            {
                "kind": "define",
                "title": "Computer",
                "text": "An electronic device that takes data as input, processes it according to instructions, stores it when needed, and gives information as output.",
            },
            {"kind": "h2", "text": "Data, information and a program"},
            {
                "kind": "table",
                "headers": ["Term", "Meaning", "Example"],
                "rows": [
                    ["Data", "Raw facts, not yet useful by themselves", "75, 81, Ali, 12 May"],
                    ["Process", "Work done on data by a program", "Adding marks, sorting names"],
                    ["Information", "Processed data that has meaning", "Ali’s total is 156 and he passed"],
                    ["Program", "A set of instructions the computer follows", "The mark-sheet program"],
                ],
                "widths": [90, 210, 200],
            },
            {"kind": "h2", "text": "The block diagram"},
            {
                "kind": "p",
                "text": "Every computer, from a phone to a large server, does four jobs. Input brings data in. The processor works on it. Output presents the result. Storage keeps data and programs for later. Draw this whenever a question says “basic operations of a computer”.",
            },
            {
                "kind": "flow",
                "steps": [
                    "Input unit — keyboard, mouse, scanner or microphone sends data in",
                    "Memory — holds the data and the program while work is going on",
                    "CPU — control unit fetches instructions; ALU calculates and compares",
                    "Output unit — monitor, printer or speaker presents information",
                    "Secondary storage — hard disk or USB keeps data after power is off",
                ],
                "caption": "Figure 1.1  Block diagram of a computer system. Storage sits beside processing, not instead of it.",
            },
            {"kind": "h2", "text": "Why a computer is useful, and where it fails"},
            {
                "kind": "table",
                "headers": ["Strength", "What it means in an answer"],
                "rows": [
                    ["Speed", "Millions of operations in a second. A result that would take a person hours appears at once."],
                    ["Accuracy", "If the data and the program are correct, the result is correct. Errors come from bad input or a bad program. This is GIGO: garbage in, garbage out."],
                    ["Diligence", "A computer does not get tired or bored. The thousandth calculation is as careful as the first."],
                    ["Storage", "A disk holds a library of files and recalls any of them in a moment."],
                    ["Versatility", "The same machine can play a video, keep accounts, or run a lab program. The job changes when the program changes."],
                ],
                "widths": [100, 400],
            },
            {
                "kind": "p",
                "text": "A computer has no feelings, no common sense and no judgement of its own. It cannot decide that a result is kind, fair or sensible unless a person has written that test into the program. It also needs electricity, and it can be attacked by harmful software.",
            },
            {"kind": "h2", "text": "Uses and abuses of IT"},
            {
                "kind": "p",
                "text": "The short question is usually “What is information technology? Write any three uses or abuses.” Define IT in two lines, then give three uses **or** three abuses, each with a short example. Do not mix a long list of both unless the question asks for both.",
            },
            {
                "kind": "table",
                "headers": ["Uses you can quote", "Abuses you can quote"],
                "rows": [
                    ["Education: lectures, online classes, exam results", "Viruses and hacking that destroy or steal data"],
                    ["Banks: ATMs, transfers, statements", "Software piracy: copying programs without a licence"],
                    ["Hospitals: records, scans, monitoring", "Loss of privacy when personal data is shared or leaked"],
                    ["Business: stock, payroll, billing", "Cyber fraud, fake messages and scams"],
                    ["Communication: email, video calls", "Health strain from long hours at a screen, and wasted time"],
                    ["Government: NADRA, weather, defence systems", "Unemployment in jobs that machines now do, if people are not retrained"],
                ],
                "widths": [250, 250],
            },
            {
                "kind": "tip",
                "title": "Shape of a 3-mark answer",
                "text": "Line 1: definition of IT. Lines 2–4: three uses, each one clause plus an example. Stop. Five vague words such as “IT is used everywhere” do not score. Named examples do.",
            },
            {"kind": "h2", "text": "Hardware and software, first distinction"},
            {
                "kind": "p",
                "text": "Hardware is the physical equipment: keyboard, mouse, monitor, printer, system unit, cables. If the power is off, the hardware is still there. Software is the set of programs that tell the hardware what to do. A printer is hardware. The program that sends a page to the printer is software. You cannot run hardware usefully without software, and software cannot run without hardware.",
            },
            {
                "kind": "board",
                "title": "One sentence to memorise",
                "text": "Hardware is touched. Software is run. Data is entered. Information is the result.",
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "Processed data that has a meaning is called:",
                    "opts": ["A) Hardware", "B) A program", "C) Information", "D) A bus"],
                    "ans": "C",
                    "why": "Data is raw. Information is data after processing.",
                },
                {
                    "q": "GIGO means:",
                    "opts": ["A) The CPU is slow", "B) Wrong input produces wrong output", "C) A type of printer", "D) A network cable"],
                    "ans": "B",
                    "why": "Garbage in, garbage out. The machine follows the data it is given.",
                },
            ],
            "short": [
                {
                    "q": "What is information technology? Write any three uses of IT.",
                    "a": "Information technology is the use of computers and communication equipment to create, store, exchange and use information. Three uses are: banks use IT for ATMs and money transfers; hospitals use it for patient records and scans; colleges use it for results, timetables and online classes.",
                },
                {
                    "q": "Write any three abuses of information technology.",
                    "a": "IT can be abused when a virus damages files, when a person copies software without a licence (piracy), and when private data is stolen or published. Cyber fraud, in which a fake message tricks a person into sending money, is a fourth common abuse.",
                },
            ],
            "long": [
                {
                    "q": "Draw the block diagram of a computer and explain its basic operations.",
                    "a": "A computer performs input, processing, output and storage. The input unit (keyboard, mouse or scanner) accepts data and converts it into a form the computer can handle. Memory holds the program and the data during the work. The CPU has a control unit, which fetches and decodes instructions, and an ALU, which calculates and compares. The output unit (monitor or printer) presents information. Secondary storage, such as a hard disk, keeps programs and data after the power is switched off. Draw five labelled boxes: Input, Memory, CPU, Output and Storage, with arrows from Input to Memory and CPU, from CPU to Output, and both ways between CPU and Storage.",
                }
            ],
        },
    },
    {
        "number": 2,
        "title": "Input, Output and Storage Devices",
        "meta": "Two periods  ·  Printers, plotters, barcode readers, hard copy and soft copy",
        "outcomes": [
            "Classify a device as input, output, storage or communication.",
            "Explain a barcode reader in a superstore.",
            "Distinguish hard copy from soft copy, and impact printers from non-impact printers.",
            "Name magnetic, optical and flash storage with one example each.",
        ],
        "blocks": [
            {"kind": "h2", "text": "Sort every device by its job"},
            {
                "kind": "p",
                "text": "Do not memorise devices as a flat list. Place each one in a family. Input devices send data **into** the computer. Output devices present results **to** a person. Storage devices **keep** data. Communication devices **move** data between computers. The next lectures take communication and the CPU. This lecture is input, output and storage.",
            },
            {"kind": "h2", "text": "Input devices"},
            {
                "kind": "table",
                "headers": ["Device", "What it captures", "Where you meet it"],
                "rows": [
                    ["Keyboard", "Letters, numbers and commands", "Every desktop"],
                    ["Mouse", "Position and clicks", "Graphical screens"],
                    ["Joystick or game pad", "Direction and buttons", "Games and simulators"],
                    ["Scanner", "A picture of a page", "Offices"],
                    ["OCR", "Printed characters, turned into text", "Digitising a book page"],
                    ["OMR", "Marks on a printed sheet, such as bubbles", "MCQ answer sheets"],
                    ["MICR", "Special magnetic ink characters", "Cheque numbers at a bank"],
                    ["Barcode reader", "The code printed as bars", "Superstore billing"],
                    ["Microphone", "Sound", "Calls and recording"],
                    ["Webcam", "A live picture", "Online class"],
                    ["Touch screen", "A touch, used as both input and a display", "Phones and ATMs"],
                ],
                "widths": [110, 210, 180],
            },
            {
                "kind": "p",
                "text": "OMR, OCR and MICR are all readers, but they do not read the same thing. **OMR** detects the position of a mark. **OCR** recognises the shape of a character. **MICR** reads characters printed in magnetic ink, which is why a bank can still read a cheque that has been stamped or a little soiled. A question that says “it is a scanning input device” and offers keyboard, mouse, trackball and OMR is asking for **OMR**.",
            },
            {
                "kind": "board",
                "title": "Barcode reader in a superstore",
                "text": "The reader scans the bars on the packet. The code is sent to the computer. The program looks up the item name and price, adds the item to the bill, and subtracts one piece from stock. Billing is faster and the price is not typed by hand, so fewer mistakes are made.",
            },
            {"kind": "h2", "text": "Output devices, hard copy and soft copy"},
            {
                "kind": "define",
                "title": "Hard copy and soft copy",
                "text": "Hard copy is output on paper or another permanent physical medium, such as a printout. Soft copy is output on a screen. It disappears when the file is closed or the power goes off, unless you save it.",
            },
            {
                "kind": "table",
                "headers": ["Output device", "Copy", "Use"],
                "rows": [
                    ["Monitor (CRT, LCD, LED, plasma)", "Soft", "Shows text and graphics while you work"],
                    ["Printer", "Hard", "Puts the result on paper"],
                    ["Plotter", "Hard", "Draws large maps, plans and posters"],
                    ["Speaker or headphone", "Neither paper nor screen", "Sound"],
                    ["Multimedia projector", "Soft, on a wall or screen", "A class or a hall"],
                ],
                "widths": [190, 130, 180],
            },
            {
                "kind": "p",
                "text": "CRT monitors are the older, deep, glass screens. LCD and LED screens are flat and use less power. LED is an LCD panel lit by light-emitting diodes. Plasma was used for large flat screens. You only need the names and the fact that all of them give soft copy.",
            },
            {"kind": "h3", "text": "Impact and non-impact printers"},
            {
                "kind": "p",
                "text": "An **impact** printer strikes an inked ribbon against the paper. A dot-matrix printer does this with a column of pins. A daisy-wheel printer does it with raised characters. Impact printers are noisy and slower, but they can press through carbon paper to make several copies at once.",
            },
            {
                "kind": "p",
                "text": "A **non-impact** printer never strikes the paper. An inkjet sprays ink. A laser printer uses a powder (toner) and heat. A thermal printer heats special paper. These are quiet, and the print is finer. They do not make carbon copies. A plotter is the device to name when the question says “huge drawings or maps”.",
            },
            {
                "kind": "table",
                "headers": ["Point", "Impact", "Non-impact"],
                "rows": [
                    ["Contact with paper", "Pins or a hammer strike a ribbon", "No strike"],
                    ["Noise", "Noisy", "Quiet"],
                    ["Carbon copies", "Possible", "Not in the ordinary way"],
                    ["Examples", "Dot matrix, daisy wheel", "Inkjet, laser, thermal"],
                    ["Typical quality", "Lower, enough for bills and forms", "Higher, enough for letters and photos"],
                ],
                "widths": [120, 190, 190],
            },
            {"kind": "h2", "text": "Storage: where data lives"},
            {
                "kind": "p",
                "text": "Primary memory (RAM and ROM) sits on the motherboard and is covered in the next lecture. Secondary storage keeps data when the power is off. Group it by the way it records.",
            },
            {
                "kind": "table",
                "headers": ["Family", "How it records", "Examples", "Exam point"],
                "rows": [
                    ["Magnetic disk", "Magnetised spots on a spinning surface", "Hard disk, and the older floppy disk", "Floppy disk and hard disk are magnetic disks, not optical disks"],
                    ["Optical disc", "Pits read by a laser", "CD, DVD, Blu-ray", "Good for software, films and backups"],
                    ["Flash / solid state", "Electronic cells, no spinning parts", "USB pen drive, SD card, SSD", "Small, fast, shock-resistant"],
                    ["Magnetic tape", "A long strip, read in order", "Backup cartridges", "Cheap for archives, slow if you need one file in the middle"],
                ],
                "widths": [100, 140, 140, 120],
            },
            {
                "kind": "p",
                "text": "A **SIMM** is a Single Inline Memory Module: a small circuit board of RAM chips that plugs into the motherboard. It is a package for main memory, not a secondary-storage disk. The name is a favourite one-mark question. A later package, DIMM, means Dual Inline Memory Module.",
            },
            {
                "kind": "tip",
                "title": "Four contrasts that return every year",
                "text": "Hard copy / soft copy. Impact / non-impact. Magnetic disk / optical disc. OMR / OCR / MICR. Write the contrast in a two-column form even in a short answer. Markers look for the difference, not for a paragraph that describes only one side.",
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "Floppy disk and hard disk are types of:",
                    "opts": ["A) Optical disc", "B) Magnetic tape", "C) Magnetic disk", "D) Flash memory"],
                    "ans": "C",
                    "why": "Both record data as magnetic spots on a disk.",
                },
                {
                    "q": "SIMM stands for:",
                    "opts": ["A) Simple Inline Memory Mode", "B) Single Inline Memory Module", "C) Serial Interface Memory Module", "D) Single Internal Memory Map"],
                    "ans": "B",
                    "why": "It is a small board of RAM chips.",
                },
                {
                    "q": "Which of these is a scanning input device?",
                    "opts": ["A) Keyboard", "B) Mouse", "C) Trackball", "D) OMR"],
                    "ans": "D",
                    "why": "OMR scans marks. The others point or type.",
                },
            ],
            "short": [
                {
                    "q": "How is a barcode reader useful in a superstore?",
                    "a": "A barcode reader scans the bars printed on a product and sends that code to the computer. The program finds the item name and price, adds the item to the customer’s bill, and updates the stock. Billing is quicker and the cashier does not type the price, so errors are fewer.",
                },
                {
                    "q": "Write four differences between impact and non-impact printers.",
                    "a": "An impact printer strikes a ribbon (dot matrix); a non-impact printer does not (laser or inkjet). Impact printers are noisy; non-impact printers are quiet. Impact printers can make carbon copies; non-impact printers normally cannot. Non-impact printers give finer print and are preferred for letters and pictures.",
                },
                {
                    "q": "Differentiate hard copy and soft copy.",
                    "a": "Hard copy is output printed on paper, such as a mark sheet from a printer. It can be filed and read without a computer. Soft copy is output shown on a monitor. It is easy to change and needs no paper, but it is gone from the screen when the file is closed unless it has been saved.",
                },
            ],
            "long": [
                {
                    "q": "Explain secondary storage devices with examples.",
                    "a": "Secondary storage keeps data and programs when the power is off, and it holds much more than RAM. Magnetic disks, such as the hard disk and the older floppy disk, store data as magnetised spots; the hard disk is the usual permanent store inside a system unit. Optical discs, such as CD, DVD and Blu-ray, are read by a laser and are used for software, films and backups. Flash storage, such as a USB pen drive, an SD card or an SSD, stores data in electronic cells, has no spinning parts and is fast and portable. Magnetic tape stores data in order along a strip and is used for large backups, though reaching one file in the middle is slow. A plotter is not storage: it is an output device for large drawings.",
                }
            ],
        },
    },
    {
        "number": 3,
        "title": "The System Unit, Registers and the Fetch Cycle",
        "meta": "Two periods  ·  Long-question material: registers, buses, fetch cycle",
        "outcomes": [
            "Name the parts of the CPU and the job of ALU and CU.",
            "Define the main registers and draw the fetch cycle.",
            "Distinguish address bus, data bus and control bus.",
            "Name ports a student actually sees on a system unit.",
        ],
        "blocks": [
            {"kind": "h2", "text": "What is inside the system unit"},
            {
                "kind": "p",
                "text": "The system unit is the box that holds the working parts. Opening it is a practical period: you should be able to point at the power supply, the motherboard, the processor, the RAM modules, the hard drive, the optical drive if there is one, the cooling fan, and the ports on the back. The exam asks for the jobs, not for a repair guide.",
            },
            {
                "kind": "table",
                "headers": ["Part", "Job"],
                "rows": [
                    ["Power supply", "Converts mains electricity into the low voltages the boards need"],
                    ["Motherboard", "The main circuit board. Every other part plugs into it or is soldered on it"],
                    ["Microprocessor", "The CPU. Runs the program"],
                    ["RAM modules", "Main memory used while a program runs"],
                    ["Hard drive", "Secondary storage"],
                    ["Cooling fan and heat sink", "Carry heat away from the processor"],
                    ["Ports", "Sockets for keyboard, mouse, printer, display and USB devices"],
                ],
                "widths": [150, 350],
            },
            {"kind": "h2", "text": "The CPU"},
            {
                "kind": "define",
                "title": "Central processing unit",
                "text": "The CPU is the part that fetches instructions from memory, decodes them and carries them out. It has two main sections: the arithmetic and logic unit and the control unit, plus a small set of registers.",
            },
            {
                "kind": "p",
                "text": "The **ALU** adds, subtracts, multiplies, divides and compares. A comparison is a logical test, such as “is this mark at least 40?”. The **control unit** does not calculate. It directs. It fetches the next instruction, decodes it, and opens the right paths so that data moves among memory, ALU and input/output at the right moment. If the ALU is the calculator, the control unit is the person who reads the question and presses the right keys.",
            },
            {
                "kind": "p",
                "text": "Clock speed, measured in gigahertz, is the number of timing pulses the processor receives each second. A faster clock can start more steps per second. It is not, by itself, the whole story of speed: the number of cores, the cache and the memory also matter. You only need the definition unless a question asks for factors.",
            },
            {"kind": "h2", "text": "Registers"},
            {
                "kind": "p",
                "text": "A register is a small, very fast storage location inside the CPU. It holds one piece of data, one address or one instruction for the step that is happening now. A long question, “What is a computer register? Explain its types,” is answered from this table. Write the definition, then five registers with one line each.",
            },
            {
                "kind": "table",
                "headers": ["Register", "Holds", "Why it exists"],
                "rows": [
                    ["Program counter (PC)", "Address of the next instruction", "So the CPU knows where to fetch from"],
                    ["Instruction register (IR)", "The instruction just fetched", "The control unit decodes what is in the IR"],
                    ["Memory address register (MAR)", "The address of a memory location about to be used", "It is placed on the address bus"],
                    ["Memory buffer register (MBR or MDR)", "The data or instruction moving to or from memory", "It is the CPU’s side of a memory transfer"],
                    ["Accumulator (AC)", "The current arithmetic result", "The ALU works into the accumulator"],
                    ["General-purpose registers", "Temporary values for the running program", "They save trips to main memory"],
                ],
                "widths": [150, 170, 180],
            },
            {"kind": "h2", "text": "The fetch cycle"},
            {
                "kind": "p",
                "text": "An instruction cycle is fetch, then decode, then execute. The **fetch cycle** is only the first part: getting the next instruction into the instruction register. Questions that say “draw the fetch cycle” want the steps below, in order. Do not skip the program counter.",
            },
            {
                "kind": "flow",
                "steps": [
                    "The program counter holds the address of the next instruction",
                    "That address is copied into the MAR",
                    "The control unit reads memory. The instruction lands in the MBR",
                    "The instruction is copied from the MBR into the IR",
                    "The program counter is increased so it points at the following instruction",
                    "Decode begins: the control unit interprets the IR. Execute follows",
                ],
                "caption": "Figure 3.1  Fetch cycle. Decode and execute are the rest of the instruction cycle.",
            },
            {
                "kind": "tip",
                "title": "A diagram that scores",
                "text": "Five boxes are enough: PC, MAR, Memory, MBR, IR. Arrow from PC to MAR labelled “copy address”. Arrow from Memory to MBR labelled “read instruction”. Arrow from MBR to IR. A small note beside the PC: “then PC = PC + 1”. Label the figure. An unlabelled circle does not score.",
            },
            {"kind": "h2", "text": "Buses"},
            {
                "kind": "define",
                "title": "Bus",
                "text": "A bus is a shared electrical path that carries data, addresses or control signals from one part of the computer to another.",
            },
            {
                "kind": "table",
                "headers": ["Bus", "Carries", "Direction"],
                "rows": [
                    ["Address bus", "The address of a memory location or a port", "One way: from the CPU out to memory"],
                    ["Data bus", "The actual data or instruction", "Both ways: read from memory, or write back"],
                    ["Control bus", "Signals such as read, write and clock", "Both ways, depending on the signal"],
                ],
                "widths": [110, 230, 160],
            },
            {
                "kind": "p",
                "text": "A wider data bus moves more bits at once. A 64-bit data bus can carry 64 bits in one transfer. The address bus decides how much memory can be named. These two widths are the “bus width” a specification sheet talks about. Cache is a small fast memory beside the CPU that keeps copies of data the processor is likely to need again, so it does not wait for RAM every time.",
            },
            {"kind": "h2", "text": "The motherboard around the CPU"},
            {
                "kind": "p",
                "text": "You should recognise these parts if a practical or a short question names them. **BIOS** is the Basic Input Output System, a program in ROM that checks the machine at power-on and starts loading the operating system. The **CMOS battery** keeps the date, time and setup when the mains power is off. **RAM slots** hold the memory modules. **Expansion slots** (PCI and the older EISA) take extra cards such as a display card or a network card. **Jumpers** are small links that older boards used to select a setting. Ports face the outside of the case.",
            },
            {
                "kind": "table",
                "headers": ["Port", "Character", "Typical use"],
                "rows": [
                    ["Serial", "One bit at a time", "Older mice and some instruments"],
                    ["Parallel", "A group of bits together", "Older printers"],
                    ["USB", "A general serial bus, hot-pluggable", "Printers, phones, pen drives, keyboards"],
                    ["HDMI", "Picture and sound together", "Monitors and projectors"],
                    ["VGA", "Older analogue video", "Older projectors and CRT monitors"],
                ],
                "widths": [80, 180, 240],
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "The electrical path that carries signals from one computer part to another is a:",
                    "opts": ["A) Bus", "B) Port", "C) Plotter", "D) Virus"],
                    "ans": "A",
                    "why": "A bus is the shared path. A port is the socket on the outside.",
                },
                {
                    "q": "The register that holds the address of the next instruction is the:",
                    "opts": ["A) Accumulator", "B) Instruction register", "C) Program counter", "D) MBR"],
                    "ans": "C",
                    "why": "The IR holds the current instruction. The PC holds the address of the next one.",
                },
            ],
            "short": [
                {
                    "q": "What is the fetch cycle? Draw its diagram.",
                    "a": "The fetch cycle brings the next instruction from memory into the CPU. The program counter’s address is copied to the MAR. Memory is read and the instruction arrives in the MBR, then moves into the IR. The program counter is then increased. Draw PC to MAR to Memory to MBR to IR, and mark PC = PC + 1.",
                },
                {
                    "q": "Differentiate the address bus and the data bus.",
                    "a": "The address bus carries the address of the memory location the CPU wants to use, and it runs from the CPU towards memory. The data bus carries the data or instruction itself, and it runs in both directions: into the CPU on a read, and out of the CPU on a write.",
                },
            ],
            "long": [
                {
                    "q": "What is a computer register? Explain its types.",
                    "a": "A register is a small, fast storage location inside the CPU. It holds the address, instruction or value needed for the current step. The program counter holds the address of the next instruction. The instruction register holds the instruction that has just been fetched, so the control unit can decode it. The memory address register holds the address that will be placed on the address bus. The memory buffer register holds the data or instruction moving between the CPU and memory. The accumulator holds the result of the ALU. General-purpose registers hold temporary values for the program so that every value does not have to be written back to RAM at once. Registers are faster than RAM and much smaller.",
                }
            ],
        },
    },
    {
        "number": 4,
        "title": "Software and Language Translators",
        "meta": "One to two periods  ·  Compiler and interpreter is a standard OR question",
        "outcomes": [
            "Classify software as system software, application software or a utility.",
            "Place a language as machine, assembly or high-level.",
            "Explain why a compiler is more efficient at run time than an interpreter.",
            "Define source code and object code.",
        ],
        "blocks": [
            {"kind": "h2", "text": "Three families of software"},
            {
                "kind": "p",
                "text": "System software runs the machine and gives other programs a place to stand. Application software does a job the user came for. A utility is a house-keeping tool. If you sort a program into the wrong family, the rest of the answer drifts. Learn the families before the brand names.",
            },
            {
                "kind": "table",
                "headers": ["Family", "Purpose", "Examples"],
                "rows": [
                    ["System software", "Controls hardware and offers services to other programs", "Operating system, device drivers, language translators"],
                    ["Application software", "Does a user’s task", "A browser, a payroll program, a game, a word processor"],
                    ["Utility", "Maintains the system", "Antivirus, compression, disk checker, backup tool"],
                ],
                "widths": [120, 200, 180],
            },
            {
                "kind": "p",
                "text": "Application software is sometimes split into **general purpose** (a spreadsheet, used by many kinds of people) and **special purpose** (a program written for one organisation, such as a college’s own fee system). Device drivers are system software: they teach the operating system how to talk to one piece of hardware, such as a particular printer. Antivirus is a utility, and a virus itself is software, not hardware. That one-mark fact is easy to lose.",
            },
            {"kind": "h2", "text": "Generations of programming language"},
            {
                "kind": "p",
                "text": "A program is written in a language. The processor only understands machine language: numbers that mean operations and addresses. Everything else must be translated.",
            },
            {
                "kind": "table",
                "headers": ["Language", "Looks like", "Who translates it"],
                "rows": [
                    ["Machine language", "Binary instructions for one family of CPU", "Nothing. The CPU runs it"],
                    ["Assembly language", "Short symbols such as ADD and MOV, one per machine instruction", "An assembler"],
                    ["High-level language", "Statements nearer to English or algebra, such as C, Visual Basic or C++", "A compiler or an interpreter"],
                ],
                "widths": [120, 220, 160],
            },
            {
                "kind": "define",
                "title": "Source code and object code",
                "text": "Source code is the program as the programmer wrote it. Object code is the machine-language result after translation. A linker may join object code with library code to make the executable program.",
            },
            {"kind": "h2", "text": "Compiler and interpreter"},
            {
                "kind": "p",
                "text": "Both turn a high-level program into something the machine can run. They do it at different times, and that is the whole of the comparison the paper wants.",
            },
            {
                "kind": "table",
                "headers": ["Point", "Compiler", "Interpreter"],
                "rows": [
                    ["When it translates", "The whole program, before it runs", "One statement at a time, while it runs"],
                    ["What you keep", "Object code, which can be run again without translating", "Usually no separate saved object program"],
                    ["Errors", "A list of errors after compilation", "Stops at the first error it meets"],
                    ["Speed of the run", "Faster, because translation is already finished", "Slower, because translation happens on every run"],
                    ["Helpful for", "A finished program you will run many times", "Testing and learning, line by line"],
                ],
                "widths": [110, 195, 195],
            },
            {
                "kind": "board",
                "title": "Why a compiler is more efficient",
                "text": "A compiler translates the source program once and saves object code. Each later run executes that object code directly, so the user does not pay the translation cost again. An interpreter translates during every run, statement by statement, so the same program takes longer. That is why a compiler is more efficient at execution time.",
            },
            {
                "kind": "p",
                "text": "An **assembler** is the translator for assembly language, not for C or Visual Basic. Do not call a compiler an assembler. C in Paper II is a compiled language. Visual Basic in the college lab is usually run through a compiler as well, though the environment also lets you test as you type.",
            },
            {
                "kind": "tip",
                "title": "Do not swap the words",
                "text": "Machine language needs no translator. Assembly language needs an assembler. A high-level language needs a compiler or an interpreter. “Compiler” is not a general word for every translator.",
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "A computer virus is:",
                    "opts": ["A) Hardware", "B) Software", "C) A port", "D) A bus"],
                    "ans": "B",
                    "why": "A virus is a program. Harmful, but still software.",
                },
                {
                    "q": "Assembly language is translated by:",
                    "opts": ["A) A compiler", "B) An assembler", "C) A plotter", "D) A browser"],
                    "ans": "B",
                    "why": "Compiler and interpreter are for high-level languages.",
                },
            ],
            "short": [
                {
                    "q": "How is a compiler more efficient than an interpreter?",
                    "a": "A compiler translates the whole source program into object code before execution, and that object code can be run again without translating. An interpreter translates one statement at a time during every run. The compiled program therefore executes faster, so the compiler is more efficient at run time.",
                },
                {
                    "q": "Differentiate system software and application software, with one example of each.",
                    "a": "System software controls the hardware and provides services for other programs. The operating system is system software. Application software does a task the user wants, such as a word processor or a college fee program. The computer needs system software before an application can run.",
                },
            ],
            "long": [],
        },
    },
    {
        "number": 5,
        "title": "Operating Systems",
        "meta": "Two periods  ·  Section C question: define an OS and explain its functions",
        "outcomes": [
            "Define an operating system and state its objectives.",
            "Explain the main functions in enough detail for a 10-mark answer.",
            "Distinguish batch processing, multitasking and time sharing.",
            "Describe booting, and name DOS, Windows and UNIX.",
        ],
        "blocks": [
            {"kind": "h2", "text": "The program that runs the other programs"},
            {
                "kind": "define",
                "title": "Operating system",
                "text": "An operating system is system software that manages hardware and software resources and provides services so that application programs, and the user, can use the computer.",
            },
            {
                "kind": "p",
                "text": "Without an operating system you would have to tell the disk, the memory and the screen how to behave inside every program. The operating system does that work once. Its objectives are convenience for the user, efficient use of the hardware, and a safe place where programs do not casually destroy each other’s data.",
            },
            {
                "kind": "p",
                "text": "Names you should be able to place: **DOS** is an older single-user operating system with a command line. **Windows** is a graphical operating system used on most college PCs. **macOS** is Apple’s graphical system. **UNIX** is a powerful multi-user system; **Linux** is a UNIX-like system often used on servers. Android, used on phones, belongs with the mobile systems and is mentioned again with Paper I only as an example of an operating system that is not Windows.",
            },
            {"kind": "h2", "text": "Functions — the long answer"},
            {
                "kind": "p",
                "text": "Learn eight functions. In Section C, write the definition, then six or seven of these, two sentences each. That is a full answer. A list of bare headings without a verb is half an answer.",
            },
            {
                "kind": "table",
                "headers": ["Function", "What to write"],
                "rows": [
                    ["Booting", "Loads the operating system into RAM when the computer is switched on, after the BIOS has checked the hardware."],
                    ["Process management", "Starts programs, gives them the CPU in turn, and ends them. Keeps one program from locking the machine."],
                    ["Memory management", "Gives each program a share of RAM and takes it back when the program ends. Stops two programs writing the same bytes."],
                    ["File management", "Creates, names, copies, deletes and finds files. Keeps the folder structure on the disk."],
                    ["Device or I/O management", "Controls keyboard, mouse, printer and disk through drivers, so a program does not need the wiring details."],
                    ["Secondary storage management", "Keeps track of free space and decides where a new file is written."],
                    ["Protection", "Checks user accounts and permissions so that one user cannot read or erase another user’s files."],
                    ["Command interpreter", "Reads what the user typed, or the menu the user clicked, and starts the right service. This is the shell or the graphical desktop."],
                    ["Network management", "On a connected machine, handles the network connection and shared resources."],
                ],
                "widths": [140, 360],
            },
            {"kind": "h2", "text": "Ways of working"},
            {
                "kind": "table",
                "headers": ["Way of working", "Idea", "Picture to keep"],
                "rows": [
                    ["Batch processing", "Jobs are collected and run one after another without the user sitting there", "A bank processing a night of cheques"],
                    ["Multitasking", "One CPU switches among several programs so they all appear to move", "A browser, a player and a document open together"],
                    ["Time sharing", "Many users each get a thin slice of CPU time", "Several terminals on one host"],
                    ["Multiprocessing", "Two or more CPUs share the work inside one machine", "A dual-processor server"],
                    ["Real time", "A reply must arrive before a deadline", "A ticket booking seat, or a hospital monitor"],
                ],
                "widths": [110, 210, 180],
            },
            {
                "kind": "p",
                "text": "Multitasking is not the same as multiprocessing. Multitasking can happen on **one** CPU by switching. Multiprocessing needs **more than one** CPU. A thread is a smaller strand of work inside a process. You will not be asked to write thread code in Paper I. If a short question appears, say: a process is a running program; a thread is one line of activity inside that process; multitasking switches among programs; multithreading switches among threads inside one program.",
            },
            {"kind": "h2", "text": "The interface, and booting"},
            {
                "kind": "p",
                "text": "A **command-line interface** makes you type commands, as DOS and a UNIX shell do. You must know the words, but a skilled user can work quickly. A **graphical user interface** uses windows, icons, menus and a pointer. Windows and macOS are GUI systems. GUI stands for Graphical User Interface, not “general user interface”.",
            },
            {
                "kind": "flow",
                "steps": [
                    "Power on. The BIOS in ROM runs the power-on self test",
                    "BIOS finds a boot device: hard disk, USB or optical disc",
                    "A small loader program is read into RAM",
                    "The loader brings the rest of the operating system into RAM",
                    "The desktop or the login prompt appears. The machine is ready",
                ],
                "caption": "Figure 5.1  Cold boot. A warm boot is a restart while power was already on.",
            },
            {
                "kind": "p",
                "text": "In the Windows practical you should be able to create, rename, copy and delete a folder, recognise a drive letter and a path such as `D:\\College\\Notes`, search for a file, and see that a file can be read-only or hidden. Those are file-management skills, which is one function of the operating system made visible. The theory paper asks for the function, not for a list of mouse clicks.",
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "GUI stands for:",
                    "opts": ["A) General User Integration", "B) Graphical User Interface", "C) Guided Universal Input", "D) General Utility Interface"],
                    "ans": "B",
                    "why": "Windows, icons, menus and a pointer.",
                },
                {
                    "q": "Giving the CPU to several programs in turn on one processor is:",
                    "opts": ["A) Multiprocessing", "B) Multitasking", "C) Compiling", "D) Modulation"],
                    "ans": "B",
                    "why": "Multiprocessing needs more than one CPU.",
                },
            ],
            "short": [
                {
                    "q": "What is an operating system? Why is it necessary?",
                    "a": "An operating system is system software that manages hardware and programs and gives the user a way to command the computer. It is necessary because it manages memory, files and devices, starts and stops programs, and stops every application from having to control the hardware itself. DOS, Windows and UNIX are examples.",
                }
            ],
            "long": [
                {
                    "q": "What is an operating system? Explain its functions.",
                    "a": "An operating system is system software that controls computer resources and provides services to users and application programs. Its functions are as follows. Booting loads the system into RAM at start-up. Process management decides which program uses the CPU. Memory management allocates RAM and reclaims it. File management creates, names, saves and deletes files and folders. Device management controls input and output through drivers. Secondary-storage management tracks free disk space. Protection checks users and permissions. The command interpreter reads commands or clicks and starts the right action. On a networked PC it also manages the connection. Examples are Windows, Linux and UNIX. Without it, application programs could not share one machine safely.",
                }
            ],
        },
    },
    {
        "number": 6,
        "title": "Data Communication",
        "meta": "Two periods  ·  Signals, modes, modulation, media, synchronous transmission",
        "outcomes": [
            "Name the five components of a data-communication system.",
            "Distinguish analog and digital signals, and modulation and demodulation.",
            "Define simplex, half duplex and full duplex with an example each.",
            "Compare guided and unguided media, and synchronous and asynchronous transmission.",
        ],
        "blocks": [
            {"kind": "h2", "text": "A message has to travel"},
            {
                "kind": "define",
                "title": "Data communication",
                "text": "Data communication is the exchange of data between two devices through some medium. The exchange follows a set of rules called a protocol.",
            },
            {
                "kind": "p",
                "text": "Five components come up whenever the question says “components of data communication”. Miss one and the answer looks unfinished. They are sender, receiver, medium, message and protocol.",
            },
            {
                "kind": "table",
                "headers": ["Component", "Role", "Example"],
                "rows": [
                    ["Sender", "The device that starts the message", "Your computer"],
                    ["Receiver", "The device that is meant to get it", "A friend’s computer, or a server"],
                    ["Medium", "The path the signal uses", "A cable, or radio"],
                    ["Message", "The data being sent", "A file, a mail, a voice"],
                    ["Protocol", "The agreed rules of format, speed and order", "TCP/IP, HTTP, SMTP"],
                ],
                "widths": [100, 200, 200],
            },
            {"kind": "h2", "text": "Analog and digital signals"},
            {
                "kind": "p",
                "text": "An **analog** signal varies continuously, like a smooth wave. A spoken voice on an old telephone line is analog. A **digital** signal jumps between separate levels, usually written as 0 and 1. Data inside a computer is digital. A keyboard press becomes a digital code. Converting between the two is the modem’s whole job, and it is a separate pair of words from “synchronous”.",
            },
            {
                "kind": "board",
                "title": "Modulation and demodulation",
                "text": "Modulation puts a digital signal onto an analog carrier so it can travel on a line made for analog waves. Demodulation takes the analog signal and recovers the digital data. A modem modulates when it sends and demodulates when it receives. The name is modulator–demodulator. The one-mark statement “converting an analog signal to a digital signal” is demodulation.",
            },
            {"kind": "h2", "text": "Direction of data: three modes"},
            {
                "kind": "table",
                "headers": ["Mode", "Direction", "Everyday example"],
                "rows": [
                    ["Simplex", "One direction only. The other end cannot reply on that channel", "A keyboard sending to the CPU, a television broadcast, a loudspeaker"],
                    ["Half duplex", "Both directions, but only one direction at a time", "A walkie-talkie: you talk, then you listen"],
                    ["Full duplex", "Both directions at the same time", "A telephone call"],
                ],
                "widths": [90, 230, 180],
            },
            {
                "kind": "tip",
                "title": "The half-duplex wording",
                "text": "The paper’s phrase is almost fixed: a mode that allows information to travel in two directions, but not at the same time, is half duplex. If the question says “at the same time”, the answer is full duplex. If it says “one direction only”, the answer is simplex.",
            },
            {"kind": "h2", "text": "Synchronous and asynchronous transmission"},
            {
                "kind": "p",
                "text": "This contrast is about **timing**, not about analog and digital. Do not mix the two tables in one answer.",
            },
            {
                "kind": "table",
                "headers": ["Point", "Synchronous", "Asynchronous"],
                "rows": [
                    ["Clock", "Sender and receiver share a timing signal", "No shared clock"],
                    ["How bytes are framed", "Data moves as a block", "Each character has a start bit and a stop bit"],
                    ["Speed", "Faster, less extra framing", "Slower, because of start and stop bits"],
                    ["Where you meet it", "High-speed links", "Keyboards and older serial ports"],
                ],
                "widths": [120, 190, 190],
            },
            {"kind": "h2", "text": "Channels and media"},
            {
                "kind": "p",
                "text": "A Section C question, “explain data communication channels with examples”, is answered as transmission media. Split the page into guided and unguided. Guided means a physical wire or fibre. Unguided means a wave through air or space.",
            },
            {
                "kind": "table",
                "headers": ["Medium", "Guided?", "One fact worth a mark"],
                "rows": [
                    ["Twisted pair", "Yes", "Two copper wires twisted to reduce noise. Cheap. Used in telephone and LAN cables."],
                    ["Coaxial cable", "Yes", "A copper core, insulation, and a metal shield. Better against noise than twisted pair. Used in cable TV and older LANs."],
                    ["Fibre optic", "Yes", "Light in a glass thread. Very fast, long distance, no electrical noise. More costly to join."],
                    ["Radio waves", "No", "Broadcast through the air. Need no cable. Can be interfered with."],
                    ["Microwave", "No", "Straight-line towers, a few tens of kilometres apart. Used for long links."],
                    ["Satellite", "No", "A microwave repeater in orbit. Reaches remote areas. There is a delay."],
                    ["Infrared", "No", "Short range, line of sight. A remote control."],
                ],
                "widths": [100, 70, 330],
            },
            {
                "kind": "p",
                "text": "**Point-to-point** communication joins one sender to one receiver, like a private phone call or a cable between two computers. **Broadcast** communication sends one message to many receivers at once, like radio, or a hub flooding a frame onto a bus. The paper asks for this difference in Section B. Two lines and one example on each side are enough.",
            },
            {
                "kind": "p",
                "text": "Signals weaken and get dirty on the way. **Attenuation** is the loss of strength with distance, cured by a repeater or amplifier. **Noise** is an unwanted signal added on the way. You can mention both if a question says “impairments”, but they are not required in every media answer.",
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "Converting an analog signal into a digital signal is:",
                    "opts": ["A) Modulation", "B) Demodulation", "C) Compilation", "D) Encryption"],
                    "ans": "B",
                    "why": "Modulation is the opposite direction: digital onto an analog carrier.",
                },
                {
                    "q": "Two directions, but not at the same time, describes:",
                    "opts": ["A) Simplex", "B) Half duplex", "C) Full duplex", "D) Broadcast only"],
                    "ans": "B",
                    "why": "A walkie-talkie. A telephone call is full duplex.",
                },
                {
                    "q": "Coaxial cable and fibre optic are examples of:",
                    "opts": ["A) A router", "B) Communication media", "C) A modem", "D) System software"],
                    "ans": "B",
                    "why": "They are paths for the signal, not devices that choose a route.",
                },
            ],
            "short": [
                {
                    "q": "Name the components of data communication.",
                    "a": "The five components are the sender, which starts the message; the receiver, which is meant to get it; the medium, which is the path; the message, which is the data; and the protocol, which is the set of rules both sides follow. A protocol example is HTTP or SMTP.",
                },
                {
                    "q": "Differentiate analog signals and digital signals.",
                    "a": "An analog signal varies continuously, like a voice wave on a telephone line. A digital signal has separate levels, usually 0 and 1, like data inside a computer. A modem converts between them: modulation sends digital data as an analog signal, and demodulation recovers the digital data.",
                },
                {
                    "q": "Differentiate synchronous and asynchronous transmission.",
                    "a": "In synchronous transmission the sender and receiver share a clock and data moves as a block, which is fast. In asynchronous transmission there is no shared clock; each character is framed by a start bit and a stop bit, which is slower. Keyboards use the asynchronous method.",
                },
            ],
            "long": [
                {
                    "q": "Explain data communication channels with examples.",
                    "a": "A communication channel is the medium that carries the signal. Guided media use a physical path. Twisted-pair cable is two copper wires twisted together; it is cheap and common in LANs and telephone lines. Coaxial cable has a shielded copper core and resists noise better; cable television uses it. Fibre-optic cable carries light in glass and gives high speed over long distances. Unguided media use waves. Radio waves broadcast through the air. Microwaves travel in a straight line between towers. A satellite repeats a microwave signal and can reach remote places, with a small delay. Infrared is short-range and needs line of sight, as in a remote control. The choice depends on distance, speed, cost and whether a cable can be laid.",
                }
            ],
        },
    },
    {
        "number": 7,
        "title": "Networks, Devices and the OSI Model",
        "meta": "Two periods  ·  The highest-scoring diagram paper: OSI, LAN/WAN, topologies",
        "outcomes": [
            "Classify a network as LAN, MAN or WAN and state a limit of each.",
            "Compare bus, star and ring topologies.",
            "Place hub, switch, bridge, router and gateway in the right job.",
            "Draw the seven OSI layers in order and give one job of each.",
        ],
        "blocks": [
            {"kind": "h2", "text": "Why networks exist"},
            {
                "kind": "define",
                "title": "Computer network",
                "text": "A computer network is two or more computers, and other devices, linked so that they can share data, software and hardware such as a printer.",
            },
            {
                "kind": "p",
                "text": "The gains are shared files, shared printers, a shared Internet connection, mail inside an office, and central backup. The costs are cabling or wireless equipment, a person to look after the network, and the new risk that a virus or an intruder can reach more than one machine.",
            },
            {"kind": "h2", "text": "Scale: LAN, MAN and WAN"},
            {
                "kind": "p",
                "text": "The Section C wording is “classify networks by their scale and limitation”. Scale means how far the network reaches. Limitation means what it cannot do, or what it costs you.",
            },
            {
                "kind": "table",
                "headers": ["Network", "Scale", "Owned by", "Limitation"],
                "rows": [
                    ["LAN, local area network", "A room, a lab, a building, sometimes a campus", "Usually one organisation", "Does not cover a city or a country by itself"],
                    ["MAN, metropolitan area network", "A city, or several offices of one organisation across a city", "Organisation or a city provider", "More costly than a LAN; not worldwide"],
                    ["WAN, wide area network", "A country or the world. The Internet is the largest WAN", "Often uses lines rented from telecom companies", "Slower and less private than a LAN unless extra protection is added; monthly cost"],
                ],
                "widths": [130, 140, 110, 120],
            },
            {"kind": "h2", "text": "Topologies"},
            {
                "kind": "p",
                "text": "A topology is the shape of the connections, not the brand of the cable. Three shapes are enough for the paper if you can also name mesh, tree and hybrid in one line each.",
            },
            {"kind": "topologies"},
            {
                "kind": "table",
                "headers": ["Topology", "Shape", "Advantage", "Weak point"],
                "rows": [
                    ["Bus", "One backbone cable. Devices tap onto it", "Cheapest. Least cable. Easy to set up a small lab", "A break in the backbone stops the network. More collisions as you add machines"],
                    ["Star", "Each device has its own cable to a central hub or switch", "A broken spoke affects only one device. Easy to find the fault", "If the centre fails, everything stops. More cable"],
                    ["Ring", "Each device joins the next in a loop. A token or frames pass around", "Orderly access. No central hub in a pure ring", "A break in the ring can stop traffic. Slower to extend"],
                    ["Mesh", "Many devices connected to many others", "More than one path, so one break is survivable", "Expensive. A full mesh needs a huge number of links"],
                    ["Tree", "Stars joined under a root, like a hierarchy", "Matches a building with floors and departments", "The root is a single weak point"],
                    ["Hybrid", "A mixture, such as star of buses", "Fits a real campus", "Harder to design"],
                ],
                "widths": [70, 130, 160, 140],
            },
            {
                "kind": "tip",
                "title": "Cheapest topology",
                "text": "The bus is the cheapest of the common topologies because one cable is shared and no central switch is required. The star is easier to maintain and is what modern switched LANs actually look like. If the question says cheapest, write bus. If it says most fault tolerant, write mesh.",
            },
            {"kind": "h2", "text": "Devices, and the similar / different trick"},
            {
                "kind": "p",
                "text": "BIEK pairs two ideas. A device that joins **two similar networks** is a **bridge**. A device that allows communication between **two different networks** is a **gateway**. Learn that pair for the wording of the paper, and then learn the fuller list so a long answer is not only two names.",
            },
            {
                "kind": "table",
                "headers": ["Device", "What it does", "Where it sits"],
                "rows": [
                    ["NIC", "Connects one computer to the cable or the wireless network. Has a hardware address", "Inside or plugged into each computer"],
                    ["Repeater", "Rebuilds a weak signal so the cable can be longer", "Physical"],
                    ["Hub", "A multiport repeater. Sends an incoming frame out of every other port", "Physical. A shared bus in a box"],
                    ["Switch", "Sends a frame only to the port that leads to the destination address", "Data link. The centre of a modern star"],
                    ["Bridge", "Joins two similar network segments and filters traffic by hardware address", "Data link. The paper’s “similar networks” device"],
                    ["Router", "Forwards packets from one network to another using IP addresses and a routing table", "Network layer"],
                    ["Gateway", "Connects networks that use different rules or protocols and translates between them", "The paper’s “different networks” device"],
                    ["Modem", "Modulates and demodulates so digital data can use an analog line", "At the end of a telephone or broadband link"],
                ],
                "widths": [70, 270, 160],
            },
            {
                "kind": "p",
                "text": "In a fuller answer you may say that a router joins different IP networks, while a gateway is the device the paper names when the networks differ in protocol. Do not call a bridge a router. A bridge does not choose a path across the Internet. An NIC is not a topology.",
            },
            {"kind": "h2", "text": "Standards and the OSI model"},
            {
                "kind": "p",
                "text": "Standards exist so that equipment from different makers can work together. **ISO** is the International Organization for Standardization. **IEEE** sets many LAN standards, including the Ethernet family. **ITU** works on telecommunication standards. You need the names more than their history.",
            },
            {
                "kind": "p",
                "text": "The **OSI model** has **seven** layers. It is a reference model: a way to teach and to design, not a single piece of software. Learn the order from the bottom, because cables are at the bottom and the user is at the top. A sentence you can chant: **Please Do Not Throw Sausage Pizza Away** — Physical, Data link, Network, Transport, Session, Presentation, Application.",
            },
            {
                "kind": "table",
                "headers": ["Layer", "Job in one sentence", "Example to quote"],
                "rows": [
                    ["7 Application", "The service the user actually touches", "HTTP, FTP, SMTP, a browser"],
                    ["6 Presentation", "Format, encryption and compression so the two sides agree on the look of the data", "ASCII, encryption"],
                    ["5 Session", "Opens, manages and closes a conversation", "Login session, checkpoints"],
                    ["4 Transport", "End-to-end delivery, and splitting a message into segments", "TCP, UDP"],
                    ["3 Network", "Logical addressing and choosing a path", "IP address, router"],
                    ["2 Data link", "Frames, hardware addresses, and the hop to the next device", "MAC address, switch, bridge"],
                    ["1 Physical", "The bits on the wire or the radio: voltages, light, connectors", "Cable, hub, NIC pins"],
                ],
                "widths": [90, 230, 180],
                "caption": "Figure 7.1  OSI layers from the user down to the cable. Draw them as a stack, layer 7 on top.",
            },
            {
                "kind": "p",
                "text": "TCP/IP is the family the Internet actually runs. It is often drawn in four layers: application, transport, internet, and network access. You do not need to map every OSI layer onto TCP/IP unless a question asks. You do need to say that **TCP/IP** is the protocol suite of the Internet, and that a **protocol** is a set of rules.",
            },
            {
                "kind": "tip",
                "title": "How to draw OSI for 10 marks",
                "text": "Draw seven stacked boxes, Application at the top, Physical at the bottom, numbered. Under the drawing, write one job for each layer. Add one example on Application (HTTP), Transport (TCP), Network (IP) and Data link (switch). Stop. A novel about the history of ISO does not add marks.",
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "The OSI model contains:",
                    "opts": ["A) 5 layers", "B) 6 layers", "C) 7 layers", "D) 4 layers"],
                    "ans": "C",
                    "why": "Physical through Application. TCP/IP is the one often drawn with four.",
                },
                {
                    "q": "The cheapest common topology is:",
                    "opts": ["A) Mesh", "B) Star", "C) Bus", "D) Fully connected"],
                    "ans": "C",
                    "why": "One shared cable and no central switch.",
                },
                {
                    "q": "The device that connects two similar networks is a:",
                    "opts": ["A) Gateway", "B) Bridge", "C) Plotter", "D) Compiler"],
                    "ans": "B",
                    "why": "Gateway is the paper’s answer for different networks.",
                },
            ],
            "short": [
                {
                    "q": "Define the LAN device used to allow communication between two different networks.",
                    "a": "A gateway connects networks that are different, often because they use different protocols, and translates between them so data can pass. In the same family of questions, a bridge joins two similar networks, and a router forwards packets between networks by using addresses and a routing table.",
                },
                {
                    "q": "Differentiate broadcast and point-to-point communication.",
                    "a": "Point-to-point communication links one sender with one receiver, as in a dedicated cable between two computers or a telephone call. Broadcast communication sends one transmission to many receivers at the same time, as in radio or a hub repeating a frame to every port.",
                },
            ],
            "long": [
                {
                    "q": "Draw and explain the OSI reference model.",
                    "a": "OSI is a seven-layer reference model for network communication, with the user at the top and the cable at the bottom. Application provides services such as HTTP, FTP and SMTP. Presentation handles format, compression and encryption. Session opens and closes the dialogue. Transport gives end-to-end delivery and splits data into segments; TCP works here. Network provides logical addressing and routing; IP and routers work here. Data link makes frames, uses hardware addresses, and includes switches and bridges. Physical transmits bits as voltages or light over cable or radio. Draw the seven names in a stack, Application on top. Data passes down the sender’s stack and up the receiver’s stack.",
                },
                {
                    "q": "What is a computer network? Classify networks by scale and state a limitation of each.",
                    "a": "A computer network is a set of computers and other devices linked to share data and resources. By scale: a LAN covers a room, building or campus, is usually private, and cannot by itself span a city. A MAN covers a city, for example several branches of one college, and costs more than a LAN while still not covering a country. A WAN covers a large geographical area. The Internet is the largest WAN. A WAN often rents public lines, so it costs a monthly fee and is generally slower and more exposed than a LAN unless it is protected. Advantages common to all three are sharing of files, printers and data.",
                },
            ],
        },
    },
    {
        "number": 8,
        "title": "The Internet, Security and Viruses",
        "meta": "One to two periods  ·  Protocols, full forms, viruses and antivirus names",
        "outcomes": [
            "Define Internet, intranet, protocol, URL and browser.",
            "Name the protocol used for the web, for email and for file transfer.",
            "Define a virus, distinguish it from a worm and a Trojan, and name five antivirus products.",
            "Expand the short forms that appear in Section B.",
        ],
        "blocks": [
            {"kind": "h2", "text": "The Internet is a network of networks"},
            {
                "kind": "p",
                "text": "The **Internet** is a worldwide public network of networks that uses the TCP/IP family of rules. An **intranet** is a private network inside one organisation that uses the same kinds of tools (pages, browsers) but is not open to the public. A college notice site that only works on the campus LAN is an intranet. The public web is part of the Internet.",
            },
            {
                "kind": "define",
                "title": "Protocol",
                "text": "A protocol is a set of rules that decides the format, timing and error handling of communication, so that two different computers can understand each other.",
            },
            {
                "kind": "table",
                "headers": ["Name", "Full form", "The one fact to write"],
                "rows": [
                    ["HTTP", "Hypertext Transfer Protocol", "Fetches web pages"],
                    ["HTTPS", "HTTP Secure", "The same, with encryption"],
                    ["HTML", "Hypertext Markup Language", "The markup language used to write web pages. It is not a protocol"],
                    ["SMTP", "Simple Mail Transfer Protocol", "The common protocol for sending email"],
                    ["FTP", "File Transfer Protocol", "Copies files between computers"],
                    ["TCP/IP", "Transmission Control Protocol / Internet Protocol", "The pair of rules the Internet runs on"],
                ],
                "widths": [70, 180, 250],
            },
            {
                "kind": "p",
                "text": "The question “the most common protocol used for email” is **SMTP**. The question “markup language used to produce web pages” is **HTML**. HTML describes the page. HTTP carries the page. They are not substitutes.",
            },
            {
                "kind": "p",
                "text": "A **browser** is application software that requests pages and displays them. A **URL** is the address of a resource, such as `https://www.biek.edu.pk`. An **ISP** is an Internet service provider, the organisation that connects you. You do not need the internal life of a search engine.",
            },
            {"kind": "h2", "text": "Viruses and the programs that stop them"},
            {
                "kind": "define",
                "title": "Computer virus",
                "text": "A computer virus is a program that attaches itself to another program or file, spreads when that host is copied or run, and may damage data, waste resources or open a door for misuse.",
            },
            {
                "kind": "p",
                "text": "A virus is **software**. It is not a hardware fault and not a bacterium. Names you can safely quote as examples are Melissa, ILOVEYOU and WannaCry. If you remember an older textbook name such as Chernobyl, that is also acceptable. Give the definition first, then two examples.",
            },
            {
                "kind": "table",
                "headers": ["Malware", "How it differs"],
                "rows": [
                    ["Virus", "Needs a host file. Spreads when the host runs or is shared."],
                    ["Worm", "A standalone program that spreads across a network by itself, without a host file."],
                    ["Trojan horse", "Disguised as useful software. It does not have to copy itself. The user is tricked into running it."],
                ],
                "widths": [110, 390],
            },
            {
                "kind": "p",
                "text": "An **antivirus** is a utility that detects, blocks and removes known malware, usually by comparing files with a list of signatures and by watching suspicious behaviour. Five names are enough for the short question: Windows Defender, Avast, AVG, Kaspersky and Bitdefender. Norton and McAfee are equally acceptable. The product must be kept updated, because a list from last year does not know this month’s virus. Antivirus does not replace careful habits: do not open an unexpected attachment, and do not install cracked software.",
            },
            {"kind": "h2", "text": "Full forms for the “any three” question"},
            {
                "kind": "p",
                "text": "Section B often says “write the full form of any three”. Write the full words, not a second abbreviation. These are the ones that actually appear.",
            },
            {
                "kind": "table",
                "headers": ["Short form", "Full form"],
                "rows": [
                    ["OCR", "Optical Character Recognition"],
                    ["OMR", "Optical Mark Recognition (or Optical Mark Reader)"],
                    ["GUI", "Graphical User Interface"],
                    ["SVGA", "Super Video Graphics Array"],
                    ["CRT", "Cathode Ray Tube"],
                    ["BIOS", "Basic Input Output System"],
                    ["HTML", "Hypertext Markup Language"],
                    ["SMTP", "Simple Mail Transfer Protocol"],
                    ["HTTP", "Hypertext Transfer Protocol"],
                    ["FTP", "File Transfer Protocol"],
                    ["URL", "Uniform Resource Locator"],
                    ["USB", "Universal Serial Bus"],
                    ["LAN / MAN / WAN", "Local / Metropolitan / Wide Area Network"],
                    ["OSI", "Open Systems Interconnection"],
                    ["ISO", "International Organization for Standardization"],
                    ["CPU / ALU / CU", "Central Processing Unit / Arithmetic and Logic Unit / Control Unit"],
                    ["RAM / ROM", "Random Access Memory / Read Only Memory"],
                    ["NIC", "Network Interface Card"],
                    ["MODEM", "Modulator–Demodulator"],
                    ["IT", "Information Technology"],
                ],
                "widths": [140, 360],
            },
            {
                "kind": "p",
                "text": "Copyright, in one paragraph if it is asked: software is owned by its author. A licence is the permission to use it. Copying a program and giving it out without that permission is piracy, and it is illegal. Data that identifies a person should not be collected or published without a proper reason. That is the privacy side of the same short question.",
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "The markup language used to produce web pages is:",
                    "opts": ["A) SMTP", "B) HTML", "C) FTP", "D) TCP"],
                    "ans": "B",
                    "why": "SMTP carries email. HTML describes the page.",
                },
                {
                    "q": "The most common protocol for sending email is:",
                    "opts": ["A) FTP", "B) HTML", "C) SMTP", "D) OCR"],
                    "ans": "C",
                    "why": "Simple Mail Transfer Protocol.",
                },
                {
                    "q": "A set of rules for communication is a:",
                    "opts": ["A) Topology", "B) Protocol", "C) Plotter", "D) Register"],
                    "ans": "B",
                    "why": "Both sides must follow the same rules.",
                },
            ],
            "short": [
                {
                    "q": "Define a computer virus and name any five antivirus programs.",
                    "a": "A computer virus is a program that attaches to a host file, spreads when that host is shared or run, and may damage data or waste resources. Five antivirus programs are Windows Defender, Avast, AVG, Kaspersky and Bitdefender. An antivirus must be updated so that it recognises new viruses.",
                },
                {
                    "q": "Write the full form of any three: OCR, GUI, SVGA, CRT, BIOS.",
                    "a": "OCR is Optical Character Recognition. GUI is Graphical User Interface. SVGA is Super Video Graphics Array. CRT is Cathode Ray Tube. BIOS is Basic Input Output System. Any three of these full forms satisfy the question.",
                },
            ],
            "long": [],
        },
    },
    {
        "number": 9,
        "title": "Memory Units and a Paper I Drill",
        "meta": "One period of units, then a full mixed drill in the shape of the paper",
        "outcomes": [
            "Convert among bit, byte, kilobyte, megabyte, gigabyte and terabyte using 1024.",
            "Separate RAM from ROM, and volatile from non-volatile.",
            "Attempt a mixed Paper I drill under the real section rules.",
        ],
        "blocks": [
            {"kind": "h2", "text": "How memory is measured"},
            {
                "kind": "p",
                "text": "Inside the machine the smallest unit is a **bit**, which is either 0 or 1. A **nibble** is 4 bits. A **byte** is 8 bits, enough for one character in the usual coding. After the byte, the exam uses steps of **1024**, not 1000.",
            },
            {
                "kind": "table",
                "headers": ["Unit", "Equals", "A way to picture it"],
                "rows": [
                    ["1 nibble", "4 bits", "Half a byte"],
                    ["1 byte", "8 bits", "One character"],
                    ["1 kilobyte (KB)", "1024 bytes", "About half a page of plain text"],
                    ["1 megabyte (MB)", "1024 KB", "A short piece of music, or a thick book of text"],
                    ["1 gigabyte (GB)", "1024 MB", "A film, or a few thousand photographs"],
                    ["1 terabyte (TB)", "1024 GB", "A large hard disk"],
                ],
                "widths": [130, 110, 260],
            },
            {
                "kind": "board",
                "title": "The one-mark conversion",
                "text": "1 GB = 1024 MB. It is not 1024 KB and it is not 1024 TB. To go up one named step, divide by 1024. To go down one step, multiply by 1024. Example: 4 GB = 4 × 1024 = 4096 MB.",
            },
            {"kind": "h2", "text": "RAM and ROM"},
            {
                "kind": "p",
                "text": "Primary memory is on the motherboard and is directly used by the CPU. **RAM** is Random Access Memory. The CPU can read it and write it. It is **volatile**: the contents are lost when power goes off. It holds the operating system, the open program and the data you are working on. More RAM usually means more programs can stay open without the machine slowing down.",
            },
            {
                "kind": "p",
                "text": "**ROM** is Read Only Memory. It is **non-volatile**. The ordinary user does not write over it. It holds the startup program, the BIOS. Variants you may meet by name: PROM can be programmed once; EPROM can be erased with ultraviolet light and rewritten; EEPROM can be erased electrically. You only need those names if the question lists them. The essential contrast is RAM volatile and writable, ROM non-volatile and used for permanent startup instructions.",
            },
            {
                "kind": "p",
                "text": "Static RAM is faster and more expensive and is used for cache. Dynamic RAM is cheaper and is the usual main memory; it has to be refreshed. Secondary storage (Lecture 2) is non-volatile and larger, but slower to reach than RAM. Do not call a hard disk RAM.",
            },
            {"kind": "h2", "text": "A mixed drill"},
            {
                "kind": "p",
                "text": "Do this on paper in one sitting. Section A: all fifteen, about twelve minutes. Section B: all parts, one side of each OR only. Section C: both questions, one side of each OR. Then open the model answers and mark strictly. If a point is missing, go back to that lecture rather than re-reading the answer three times.",
            },
            {"kind": "h3", "text": "Section A"},
            {
                "kind": "p",
                "text": "1  One gigabyte equals: A) 1024 KB  B) 1024 bytes  C) 1024 MB  D) 1024 TB.",
            },
            {
                "kind": "p",
                "text": "2  Which topology uses the least cable for a small lab? A) Mesh  B) Bus  C) Full star with a spare hub  D) A separate cable between every pair.",
            },
            {
                "kind": "p",
                "text": "3  SMTP is used for: A) Printing maps  B) Sending email  C) Describing a web page  D) Scanning a cheque.",
            },
            {
                "kind": "p",
                "text": "4  Demodulation converts: A) Digital to analog  B) Analog to digital  C) Source code to object code  D) A file into a folder.",
            },
            {
                "kind": "p",
                "text": "5  The register holding the instruction currently being decoded is the: A) PC  B) MAR  C) IR  D) Address bus.",
            },
            {
                "kind": "p",
                "text": "6  A virus is: A) Hardware  B) Software  C) A protocol  D) A topology.",
            },
            {
                "kind": "p",
                "text": "7  Two similar LAN segments are joined by a: A) Bridge  B) Plotter  C) Compiler  D) Daisy wheel.",
            },
            {
                "kind": "p",
                "text": "8  OSI has: A) 4 layers  B) 5 layers  C) 7 layers  D) 8 layers.",
            },
            {
                "kind": "p",
                "text": "9  Half duplex means: A) One direction only  B) Both directions, not together  C) Both directions together  D) No transmission.",
            },
            {
                "kind": "p",
                "text": "10  Which is a magnetic disk? A) DVD  B) Fibre  C) Hard disk  D) RAM.",
            },
            {
                "kind": "p",
                "text": "11  HTML is a: A) Mail protocol  B) Markup language for web pages  C) Type of ROM  D) Bus.",
            },
            {
                "kind": "p",
                "text": "12  Which memory loses its contents when power fails? A) ROM  B) Hard disk  C) RAM  D) DVD.",
            },
            {
                "kind": "p",
                "text": "13  A large engineering drawing is produced on a: A) Plotter  B) Microphone  C) Bridge  D) Bus.",
            },
            {
                "kind": "p",
                "text": "14  The translator for a whole high-level program, producing object code, is a: A) Plotter  B) Compiler  C) Repeater  D) Hub.",
            },
            {
                "kind": "p",
                "text": "15  BIOS stands for: A) Basic Input Output System  B) Binary Internal Operating Software  C) Bus Interface Of Storage  D) Basic Internet Output Signal.",
            },
            {"kind": "h3", "text": "Section B — answer every part, one side of each OR"},
            {
                "kind": "p",
                "text": "i) Define information technology and give three abuses. **OR** Explain the use of a barcode reader at a checkout.",
            },
            {
                "kind": "p",
                "text": "ii) Differentiate hard copy and soft copy. **OR** Differentiate synchronous and asynchronous transmission.",
            },
            {
                "kind": "p",
                "text": "iii) Define a computer virus and name five antivirus programs. **OR** Which device prints a large map? Explain briefly.",
            },
            {
                "kind": "p",
                "text": "iv) What is the fetch cycle? **OR** Name the five components of data communication.",
            },
            {
                "kind": "p",
                "text": "v) Why is a compiler more efficient at run time than an interpreter? **OR** What is modulation?",
            },
            {
                "kind": "p",
                "text": "vi) Give four differences between impact and non-impact printers.",
            },
            {
                "kind": "p",
                "text": "vii) Which device lets two different networks communicate? Define it.",
            },
            {
                "kind": "p",
                "text": "viii) Differentiate analog and digital signals.",
            },
            {
                "kind": "p",
                "text": "ix) Differentiate broadcast and point-to-point transmission.",
            },
            {
                "kind": "p",
                "text": "x) Write the full form of any three: OCR, GUI, CRT, BIOS, SMTP.",
            },
            {"kind": "h3", "text": "Section C — answer both, one side of each OR"},
            {
                "kind": "p",
                "text": "1  Explain the functions of an operating system. **OR** Explain the types of CPU register.",
            },
            {
                "kind": "p",
                "text": "2  Explain communication media with examples. **OR** Draw the OSI model and state the job of each layer.",
            },
            {"kind": "h2", "text": "Answer key for the drill"},
            {
                "kind": "p",
                "text": "Section A: 1 C, 2 B, 3 B, 4 B, 5 C, 6 B, 7 A, 8 C, 9 B, 10 C, 11 B, 12 C, 13 A, 14 B, 15 A.",
            },
            {
                "kind": "p",
                "text": "Section B and Section C are answered in Lectures 1 to 8. Mark your paper against those model answers. A short answer needs the definition plus the examples the question asked for. A long answer needs a heading, a definition, and a point for every item in the lecture table, written as sentences.",
            },
            {
                "kind": "tip",
                "title": "How to mark yourself",
                "text": "Give the mark only if the point is on the page. A correct idea written as one vague line scores the definition mark, not the explanation marks. If you missed the fetch-cycle order, redraw it tonight from Lecture 3. If you swapped bridge and gateway, rewrite that pair from Lecture 7 before you sleep.",
            },
        ],
        "checkpoint": {},
    },
]
