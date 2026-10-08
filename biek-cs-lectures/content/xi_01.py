from content.schema import lecture

LECTURE = lecture(
    id="xi-1",
    number=1,
    title="Computer Systems",
    kicker="CLASS XI  ·  UNIT 1",
    unit="Unit 1 — Computer Systems",
    domain="A. Computer systems",
    periods="about 30 periods",
    intro=(
        "A computer system is not only the box on the desk. It is hardware, software, "
        "data, and the rules that move that data safely from one place to another. "
        "This lecture follows the Class XI textbook unit: how analog and digital signals "
        "differ, how Boolean logic becomes a circuit, how a software project moves from "
        "an idea to a tested product, and how networks are organised so they can grow "
        "and keep working."
    ),
    outcomes=[
        "Distinguish analog and digital signals and build truth tables for up to three inputs.",
        "Write Boolean expressions, apply the basic identities and duality, and draw the matching logic diagram.",
        "Relate the stages of the software development life cycle to a small case, and compare Waterfall with Agile.",
        "Explain black-box and white-box testing.",
        "Describe the basic communication model, the OSI layers, and the TCP/IP model.",
        "Compare network topologies for scalability and reliability.",
        "Explain why cybersecurity matters and contrast encryption with hashing, at the level of purpose and use.",
    ],
    blocks=[
        ("h2", "Analog and digital representation"),
        (
            "p",
            "An **analog** signal changes smoothly. A microphone turns a voice into a voltage that rises and falls with the sound. A **digital** signal uses a fixed set of values. Inside a computer those values are two voltage bands that we call 0 and 1. A **bit** is one such value. Eight bits make a **byte**.",
        ),
        (
            "p",
            "Digital representation is the reason a file can be copied without slowly becoming blurry. Each bit is restored to a clean 0 or 1 at every step. The cost is that a smooth real-world signal must be **sampled** (measured at moments in time) and **quantised** (rounded to the nearest allowed level). A higher sampling rate and more bits per sample keep more detail, and they also make a larger file.",
        ),
        (
            "callout",
            {
                "kind": "define",
                "title": "Digital logic",
                "text": "Digital logic is the set of rules that combine bits. Those rules are written as Boolean expressions and built in hardware as logic gates. Every later topic in this lecture — circuits, programs, and even encryption — rests on bits being cleanly 0 or 1.",
            },
        ),
        ("h2", "Boolean expressions, functions, and identities"),
        (
            "p",
            "A **Boolean variable** is a name that stands for 0 or 1. We write 0 for false and 1 for true. A **Boolean expression** combines variables with operators. A **Boolean function** is the rule that maps each possible input combination to one output. The truth table is the full listing of that function.",
        ),
        (
            "p",
            "In this course the operators are written in words so the paper stays readable: **AND** (also written as a dot), **OR** (also written as +), and **NOT** (a bar or a prime, so the NOT of A is A'). AND gives 1 only when every input is 1. OR gives 1 when at least one input is 1. NOT flips its single input.",
        ),
        (
            "table",
            {
                "caption": "Table 1. Boolean identities used in Class XI. A and B are inputs. A' is NOT A.",
                "headers": ["Name", "OR form", "AND form"],
                "rows": [
                    ["Identity", "A + 0 = A", "A · 1 = A"],
                    ["Null (dominance)", "A + 1 = 1", "A · 0 = 0"],
                    ["Idempotent", "A + A = A", "A · A = A"],
                    ["Complement", "A + A' = 1", "A · A' = 0"],
                    ["Double negation", "(A')' = A", "(A')' = A"],
                    ["Commutative", "A + B = B + A", "A · B = B · A"],
                    ["Associative", "(A + B) + C = A + (B + C)", "(A · B) · C = A · (B · C)"],
                    ["Distributive", "A + (B · C) = (A + B) · (A + C)", "A · (B + C) = (A · B) + (A · C)"],
                    ["Absorption", "A + (A · B) = A", "A · (A + B) = A"],
                    ["De Morgan", "(A + B)' = A' · B'", "(A · B)' = A' + B'"],
                ],
                "widths": [0.24, 0.40, 0.36],
            },
        ),
        (
            "math",
            r"\begin{aligned}"
            r"A+0 &= A & A\cdot 1 &= A \\"
            r"A+1 &= 1 & A\cdot 0 &= 0 \\"
            r"A+\overline{A} &= 1 & A\cdot\overline{A} &= 0 \\"
            r"\overline{A+B} &= \overline{A}\cdot\overline{B} & \overline{A\cdot B} &= \overline{A}+\overline{B} \\"
            r"A\oplus B &= \overline{A}B + A\overline{B}"
            r"\end{aligned}",
        ),
        (
            "p",
            "**Duality** swaps the operators and the constants: every OR becomes AND, every AND becomes OR, every 0 becomes 1, and every 1 becomes 0. Variables are left as they are. The dual of a true identity is another true identity. The dual of `A + 0 = A` is `A · 1 = A`. The dual of `A + A' = 1` is `A · A' = 0`. Duality does not mean the dual expression has the same output as the original. It means the dual *law* is also a law.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — simplify and check",
                "text": (
                    "Simplify F = A · (A + B).\n\n"
                    "By the absorption law, A · (A + B) = A. So the circuit ignores B.\n\n"
                    "Check one row. If A = 1 and B = 0, then A + B = 1, and A · 1 = 1, which equals A. "
                    "If A = 0 and B = 1, then A + B = 1, and 0 · 1 = 0, which equals A. The identity holds."
                ),
            },
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — De Morgan",
                "text": (
                    "Show that (A + B)' and A' · B' match for A = 0, B = 1.\n\n"
                    "A + B = 0 + 1 = 1, so (A + B)' = 0.\n\n"
                    "A' = 1 and B' = 0, so A' · B' = 0. Both sides agree. "
                    "A full proof is the four-row truth table; one matching row is only a check, not a proof."
                ),
            },
        ),
        ("h2", "Logic gates and truth tables"),
        ("figure", "logic-gates", "Figure 1. The gate shapes used when a question asks for a logic diagram."),
        (
            "p",
            "A **logic gate** is the hardware for one operator. A **switch** is an older picture of the same idea: two switches in series act as AND (both must be closed), and two switches in parallel act as OR (either one is enough). You may be asked to recognise a gate from its shape or from its table. Learn both the two-input table and the name of the gate that inverts it.",
        ),
        (
            "table",
            {
                "caption": "Table 2. Two-input gates. NAND is NOT of AND. NOR is NOT of OR. XOR is 1 when the inputs differ. XNOR is 1 when they match.",
                "headers": ["A", "B", "AND", "OR", "NAND", "NOR", "XOR", "XNOR"],
                "rows": [
                    ["0", "0", "0", "0", "1", "1", "0", "1"],
                    ["0", "1", "0", "1", "1", "0", "1", "0"],
                    ["1", "0", "0", "1", "1", "0", "1", "0"],
                    ["1", "1", "1", "1", "0", "0", "0", "1"],
                ],
                "center": True,
                "widths": [0.1, 0.1, 0.13, 0.12, 0.14, 0.13, 0.13, 0.15],
            },
        ),
        (
            "p",
            "NOT has one input: 0 becomes 1, and 1 becomes 0. **NAND** and **NOR** are called universal gates because any other gate can be built from NAND alone, or from NOR alone. **XOR** is the odd-one-out detector: `A XOR B = A'·B + A·B'`.",
        ),
        (
            "p",
            "For three inputs, list the rows in binary counting order from 000 to 111 so you never skip a row. There are 2³ = 8 rows. Compute the expression in small pieces, column by column, instead of doing it in your head.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — three-input truth table",
                "text": (
                    "Build the truth table for F = A·B + C'.\n\n"
                    "Order the rows as ABC from 000 to 111. First column: A·B is 1 only on the last two rows "
                    "(110 and 111). Second column: C' is 1 whenever C is 0, that is on rows 000, 010, 100, and 110. "
                    "F is 1 where either column is 1, so F = 1 on 000, 010, 100, 110, and 111. "
                    "F = 0 on 001, 011, and 101."
                ),
            },
        ),
        (
            "p",
            "To **draw a logic diagram** from an expression, start inside the brackets. For `F = (A AND B) OR (NOT C)` draw an AND gate for A and B, a NOT gate for C, and feed both results into an OR gate. To **read an expression from a diagram**, label the wire after every gate and combine those labels at the next gate. The final wire is F.",
        ),
        ("figure", "sample-circuit", r"Figure 2. One AND, one NOT, and one OR for \(F = (A \cdot B) + \overline{C}\)."),
        ("h3", "A first look at Karnaugh maps"),
        (
            "p",
            "A **Karnaugh map** (K-map) is a truth table redrawn so that neighbouring cells differ by only one variable. Grouping neighbouring 1s lets you drop the variable that changes inside the group. Groups must be rectangles of 1, 2, 4, or 8 cells. This course expects you to recognise the map and simplify a small one, not to handle five variables.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — a map that collapses to one variable",
                "text": (
                    "Let the minterms where F = 1 be the four cases in which B = 0: ABC = 000, 001, 100, and 101. "
                    "Those four cells form one group. Inside the group, A takes both values and C takes both values, "
                    "so A and C are not needed. B is 0 throughout, which is written B'. So F = B'.\n\n"
                    "Check: when B is 0, F is 1 no matter what A and C are. When B is 1, F is 0. That is exactly B'."
                ),
            },
        ),
        ("figure", "kmap-b", r"Figure 3. The gold outline is the group of four. It simplifies to \(F = \overline{B}\)."),
        ("h2", "The software development life cycle"),
        (
            "p",
            "The **software development life cycle (SDLC)** is the planned path from a need to a working system that somebody can maintain. A **bug** is a fault that makes the system do the wrong thing. **Debugging** is the work of finding and removing that fault. The engineering point of the SDLC is that quality and risk are managed on purpose, not left until the night before submission.",
        ),
        (
            "table",
            {
                "caption": "Table 3. Stages you should be able to name and illustrate.",
                "headers": ["Stage", "What the team does", "A college-portal example"],
                "rows": [
                    ["Analysis", "Write down who the users are and what the system must do.", "Students must see the date sheet. Clerks must upload it."],
                    ["Design", "Decide screens, data, and structure before heavy coding.", "A timetable table, a login screen, and an upload screen."],
                    ["Coding", "Build the design in a programming language.", "Write the pages and the database queries."],
                    ["Testing", "Compare behaviour with the requirements.", "Try a wrong password. Try a missing file."],
                    ["Deployment", "Put the system where real users reach it.", "Publish it on the college server."],
                    ["Maintenance", "Fix faults and adapt to change.", "Next year's class names are added."],
                ],
                "widths": [0.18, 0.42, 0.40],
            },
        ),
        (
            "p",
            "Two process models organise those stages differently. **Waterfall** completes each stage before the next begins. It is understandable and easy to document, and it fits when the requirements are stable, such as a payroll rule that is fixed by policy. It is painful when the first analysis was wrong, because the team discovers that late. **Agile** builds in short cycles called sprints. Each sprint delivers a small working piece, the user comments, and the next sprint adjusts. Agile fits a college app whose teachers keep changing what they want. It needs a customer who will actually look at each piece. Agile is not an excuse to skip testing.",
        ),
        (
            "p",
            "You may see two further names on a key-term list. **UML** is a family of diagrams for design, such as a picture of users and their actions. A **design pattern** is a known shape for a recurring design problem. You are not required to draw a full UML model in this unit; you should know why a diagram exists before the code.",
        ),
        ("h3", "Black-box and white-box testing"),
        (
            "p",
            "**Black-box testing** looks only at inputs and outputs. The tester does not read the code. If the requirement says “a mark below 0 is rejected”, the tester enters −1 and checks the message. **White-box testing** looks inside. The tester chooses inputs that travel through each branch, including the branch that almost never runs. Black-box testing asks “did we build the right behaviour?” White-box testing asks “did we exercise the code we wrote?” A serious project uses both. Testing reduces risk. It does not prove that no bug remains.",
        ),
        (
            "callout",
            {
                "kind": "exam",
                "title": "Exam tip",
                "text": "A five-mark SDLC question wants the stage names in order, one activity for each, and a single running example. Do not define Agile in a question that asked for the stages, and do not list the stages in a question that asked for the difference between Waterfall and Agile.",
            },
        ),
        ("h2", "Communication model, OSI, and TCP/IP"),
        (
            "p",
            "A basic **communication model** has a sender, an encoder that turns the message into a signal, a medium, a decoder, and a receiver. **Noise** is anything that damages the signal on the way: electrical interference, a damaged cable, or too many devices talking at once. A **protocol** is a shared rulebook: the order of messages, the addresses, and what to do when a piece is lost. Without a protocol, the bits arrive and neither side knows what they mean.",
        ),
        ("figure", "comm-model", "Figure 4. Encoder and decoder sit on either side of the medium, which is where noise acts."),
        (
            "p",
            "The **OSI model** of ISO splits the work into seven layers so that a change in the cable does not force a change in the email program. Learn the order from the wire upward, and one job plus one example for each layer.",
        ),
        (
            "table",
            {
                "caption": "Table 4. OSI layers. PDU means the name of the chunk at that layer.",
                "headers": ["Layer", "Job", "Examples"],
                "rows": [
                    ["7 Application", "The service the user actually wants.", "HTTP, SMTP, FTP, DNS"],
                    ["6 Presentation", "Format, compression, and encryption of the data.", "Character encoding, TLS formatting"],
                    ["5 Session", "Open, manage, and close a dialogue.", "Keeping a login session in order"],
                    ["4 Transport", "End-to-end delivery and ports.", "TCP, UDP"],
                    ["3 Network", "Addresses and routes across networks.", "IP addresses, routers"],
                    ["2 Data link", "Frames on one link, and MAC addresses.", "Ethernet, a switch"],
                    ["1 Physical", "The bits on the medium.", "Cable, radio, hub, voltages"],
                ],
                "widths": [0.24, 0.40, 0.36],
            },
        ),
        (
            "p",
            "The **TCP/IP model** used on the real Internet folds those seven layers into four: Link (OSI 1–2), Internet (OSI 3), Transport (OSI 4), and Application (OSI 5–7). **IP** moves packets using IP addresses. **TCP** adds reliability: numbering, acknowledgements, and retransmission. **UDP** sends datagrams without that handshake, which is why it is used when a late packet is useless, such as a live voice call. A **port** number tells the receiving computer which program should get the segment.",
        ),
        ("figure", "osi-tcp", "Figure 5. The TCP/IP application layer covers OSI layers 5, 6, and 7. The link layer covers OSI layers 1 and 2."),
        (
            "callout",
            {
                "kind": "warn",
                "title": "Common mistake",
                "text": "Switches and MAC addresses belong with the data-link layer. Routers and IP addresses belong with the network layer. HTTP is an application protocol that usually travels over TCP. Do not call HTTP a physical-layer protocol because you use it on a cable.",
            },
        ),
        ("h2", "Topologies, scalability, and reliability"),
        (
            "p",
            "A **network topology** is the shape of the connections. The shape decides how easily the network grows (**scalability**) and how well it survives a fault (**reliability**). **Availability** is the share of time the service is actually usable: uptime divided by uptime plus downtime. A design can be fast and still unreliable if one small part stops everything.",
        ),
        ("math", r"\mathrm{Availability}=\frac{\mathrm{uptime}}{\mathrm{uptime}+\mathrm{downtime}}"),
        ("figure", "topologies", "Figure 6. Bus, star, ring, and mesh. A tree is a hierarchy of stars, and a hybrid mixes these shapes."),
        (
            "table",
            {
                "caption": "Table 5. Topologies to compare in a long question.",
                "headers": ["Topology", "Shape", "Strength", "Weakness"],
                "rows": [
                    ["Bus", "One shared backbone", "Little cable", "A break in the backbone affects every device; collisions grow as devices are added"],
                    ["Star", "Each device to a central switch", "Easy to add a device; one cable fault is local", "The central switch is a single point of failure"],
                    ["Ring", "Each device to the next, in a loop", "Orderly access, often by a token", "One break can stop the ring unless a second ring exists"],
                    ["Mesh", "Many paths between devices", "A failed link can be routed around", "Many links, so high cost"],
                    ["Tree", "Stars joined in a hierarchy", "Matches a campus or an organisation", "A failed link high in the tree isolates a whole branch"],
                    ["Hybrid", "A mix of the above", "Each part uses a suitable shape", "Harder to document and to repair"],
                ],
                "widths": [0.14, 0.24, 0.32, 0.30],
            },
        ),
        (
            "p",
            "On a bus, devices often share the cable using **CSMA**: listen before sending, and cope with a collision if two speak together. On a classic ring, a **token** is a permission that travels around the ring; only the device holding the token may send. In a **star**, a **client** uses a service and a **server** provides it. Those words also describe roles, not only topology: a lab PC can be a client of the college file server.",
        ),
        (
            "p",
            "Cloud computing helps scale because more storage or processing can be rented when the load grows, and released when it falls. Reliability still has to be designed: two copies in two places, a spare path, and a test that actually adds load and removes a part to see what breaks. A test of scale is not the same thing as an attack. It is a measurement the owner runs on a system they are allowed to test.",
        ),
        ("h2", "Cybersecurity and encryption"),
        (
            "p",
            "A system is attacked because the data or the service is valuable. **Cybersecurity** is the work of keeping three properties: **confidentiality** (the wrong people cannot read it), **integrity** (nobody changes it unnoticed), and **availability** (the people who should reach it still can). A security plan ranks the risks and spends effort on the serious ones first. A written **privacy policy** says what data is collected and why. A policy does not protect anyone if the system ignores it.",
        ),
        (
            "table",
            {
                "caption": "Table 6. Threats named in the curriculum, described by impact. The defence column is what a student and a college should do.",
                "headers": ["Name", "Impact", "Defence to remember"],
                "rows": [
                    ["Malware", "Software that harms the device or the data", "Install software from known sources; keep updates on"],
                    ["Phishing", "A fake message that tries to collect a password or a payment", "Check the real address; do not use a link from an unexpected message"],
                    ["DDoS", "A service is flooded until genuine users cannot use it", "The service owner filters traffic and adds capacity; users cannot stop this from a browser"],
                    ["XSS", "A website runs a script a visitor did not intend, which can take over that visitor's session", "The site must treat typed-in text as text, not as code"],
                    ["Unauthorised access", "Someone uses an account or a system they do not own", "Authentication, authorisation, and least privilege"],
                ],
                "widths": [0.18, 0.42, 0.40],
            },
        ),
        (
            "p",
            "**Authentication** checks who you are. **Authorisation** checks what that identity is allowed to do. A login proves identity; a clerk's account that cannot edit the date sheet is authorisation. **2FA** (two-factor authentication) asks for a second proof, such as a code on a phone, so a stolen password is not enough. A **firewall** allows or blocks traffic by rule. **Hashing** turns data into a short fingerprint. A good hash is one-way: you cannot rebuild the password from the fingerprint. That is why systems store hashes of passwords rather than the passwords themselves.",
        ),
        (
            "p",
            "**Encryption** turns **plaintext** into **ciphertext** with a key, so that someone who sees the message still cannot read it. **Decryption** reverses the step with the proper key. **Symmetric** encryption uses the same secret key to lock and unlock. It is fast, and the hard part is delivering that secret key safely. **Asymmetric** encryption uses a key pair: a public key anyone may know, and a private key that stays secret. It is slower and is often used to agree a symmetric key, or to sign a message so the receiver can check who sent it. Hashing is not encryption. A hash is not meant to be decrypted.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — a teaching cipher, not a real defence",
                "text": (
                    "The Caesar cipher shifts each letter by a fixed number. Shift BOARD by 3: B→E, O→R, A→D, R→U, D→G, so the ciphertext is ERDUG. "
                    "Shifting back by 3 restores BOARD. This shows plaintext, ciphertext, and a key (the number 3). "
                    "It is a classroom illustration only. A shift cipher is easy to undo by trying all 25 shifts, so it does not protect a password, a result, or a message."
                ),
            },
        ),
        (
            "callout",
            {
                "kind": "note",
                "title": "What this lecture will not teach you to do",
                "text": "You should be able to name an attack, say what harm it causes, and say which control reduces that harm. Building a phishing page, flooding a network, or writing an exploit is not part of the practical and is not a skill this course awards marks for.",
            },
        ),
    ],
    terms=[
        ("Bit / byte", "A bit is a 0 or a 1. A byte is eight bits."),
        ("Boolean function", "A rule that gives one output bit for each combination of input bits."),
        ("Duality", "Swap AND with OR and 0 with 1 in a law. The dual law is also true."),
        ("Logic gate", "A circuit element that performs AND, OR, NOT, NAND, NOR, XOR, or XNOR."),
        ("Karnaugh map", "A truth table arranged so groups of 1s can be simplified."),
        ("SDLC", "The staged process of analysis, design, coding, testing, deployment, and maintenance."),
        ("Waterfall / Agile", "One-pass stages, versus short cycles with user feedback."),
        ("Black-box / white-box", "Testing from the outside by inputs and outputs, versus testing internal paths."),
        ("Protocol", "An agreed set of rules for communication."),
        ("OSI model", "Seven layers from physical up to application."),
        ("TCP/IP", "The four-layer model of the Internet: link, internet, transport, application."),
        ("Topology", "The shape of a network: bus, star, ring, mesh, tree, or hybrid."),
        ("Scalability", "The ability to grow in users or data without collapsing."),
        ("Reliability", "The ability to keep working when a part fails."),
        ("Encryption", "Reversible transformation of plaintext into ciphertext using a key."),
        ("Hashing", "A one-way fingerprint, used to detect change and to store password checks."),
        ("Authentication", "Checking identity. Authorisation then checks permission."),
    ],
    checks=[
        {
            "q": "Why is a digital copy cleaner than a long chain of analog copies?",
            "a": "Each digital stage restores the signal to a definite 0 or 1, so small noise is thrown away. An analog copy copies the noise as well, so quality falls at every step.",
        },
        {
            "q": "State the dual of A + 1 = 1.",
            "a": "Swap + with · and 1 with 0. The dual is A · 0 = 0.",
        },
        {
            "q": "A gate outputs 0 only when both inputs are 1, and outputs 1 otherwise. Name it.",
            "a": "NAND. It is the NOT of AND, and AND is 1 only when both inputs are 1.",
        },
        {
            "q": "Give one activity of the design stage and one activity of the testing stage.",
            "a": "Design decides the structure, for example the tables and the screens. Testing checks the running system against the requirements, for example by entering a bad password and reading the result.",
        },
        {
            "q": "Which OSI layer uses IP addresses, and which uses MAC addresses?",
            "a": "The network layer uses IP addresses and routers. The data-link layer uses MAC addresses and switches.",
        },
    ],
    mcqs=[
        {
            "q": "Which identity is the dual of A · 1 = A?",
            "options": ["A + 0 = A", "A + 1 = 1", "A · 0 = 0", "A · A = A"],
            "answer": "A",
            "why": "Duality swaps · with + and 1 with 0, so A · 1 = A becomes A + 0 = A.",
        },
        {
            "q": "The output of XOR is 1 when",
            "options": [
                "both inputs are 1",
                "both inputs are 0",
                "the inputs are different",
                "either input is 1, including both",
            ],
            "answer": "C",
            "why": "XOR is 1 only on rows 01 and 10. Row 11 is 0, so option D is ordinary OR.",
        },
        {
            "q": "Black-box testing mainly checks",
            "options": [
                "the names of the variables",
                "inputs against expected outputs",
                "the brand of the keyboard",
                "how many comments are in the code",
            ],
            "answer": "B",
            "why": "The tester does not need the source. The requirement and the observed output are enough.",
        },
        {
            "q": "In the TCP/IP model, TCP belongs to the",
            "options": ["link layer", "internet layer", "transport layer", "physical cable"],
            "answer": "C",
            "why": "TCP provides end-to-end reliable delivery, which is the transport job.",
        },
        {
            "q": "A star topology is easy to extend, but",
            "options": [
                "it has no central device",
                "the central switch is a single point of failure",
                "it cannot use a switch",
                "it is always more reliable than a mesh",
            ],
            "answer": "B",
            "why": "Every device depends on the centre. A mesh has extra paths and is usually more reliable, at a higher cost.",
        },
        {
            "q": "Hashing a password is preferred to storing the password because",
            "options": [
                "a hash is designed to be reversed with the public key",
                "a hash is a one-way fingerprint",
                "a hash makes the network faster",
                "a hash replaces the need for authentication",
            ],
            "answer": "B",
            "why": "The system can check a login by hashing the typed password and comparing fingerprints. It need not keep the password itself.",
        },
    ],
    shorts=[
        {
            "q": "Differentiate analog and digital signals with one example of each.",
            "a": "An analog signal varies smoothly, such as the voltage from a microphone. A digital signal uses discrete values, such as the bits stored in a computer. A digital system samples and quantises an analog source before it can store it.",
        },
        {
            "q": "Draw the truth table of NAND and state why NAND is called universal. (A description is enough if the paper does not provide a drawing box.)",
            "a": "Rows 00, 01, 10, 11 give outputs 1, 1, 1, 0. NAND is universal because NOT, AND, and OR can all be constructed from NAND gates alone, so any Boolean function can be built from NAND.",
        },
        {
            "q": "Give two differences between Waterfall and Agile.",
            "a": "Waterfall finishes a stage before the next starts; Agile repeats short cycles. Waterfall suits fixed requirements; Agile expects the requirements to be refined after each working increment. Both still need testing.",
        },
        {
            "q": "What is the difference between symmetric and asymmetric encryption?",
            "a": "Symmetric encryption uses one shared secret key to encrypt and decrypt, and it is fast, but the key must be delivered safely. Asymmetric encryption uses a public key and a private key. It is slower and is used to exchange a secret or to check a signature.",
        },
    ],
    longs=[
        {
            "marks": 5,
            "q": "A college wants a result portal. Relate the SDLC stages to this project, and say whether you would start with Waterfall or Agile. Justify the choice.",
            "a": (
                "Analysis lists the users and the rules: students view their own result, teachers enter marks, and the controller publishes them. "
                "Design chooses the data (student, subject, mark) and the screens. Coding builds those screens and the checks, such as rejecting a mark above 100. "
                "Testing tries correct marks, out-of-range marks, and a student opening another student's roll number. Deployment places the portal on the college server. "
                "Maintenance covers a changed grade scale next year.\n\n"
                "Agile is the better start if teachers are still deciding the screens, because a first sprint can publish a read-only result and the next sprint can add mark entry. "
                "Waterfall would fit better only if the board's rules and the screens were already frozen. Name the risk either way: a wrong roll-number check is a privacy fault, so that test belongs in the plan before launch."
            ),
        },
        {
            "marks": 5,
            "q": "Compare star and mesh topologies for a computer laboratory of 40 PCs that must stay usable during a practical examination.",
            "a": (
                "A star joins each PC to one switch. Adding a PC is one cable, a broken PC cable does not stop the others, and fault finding is simple. "
                "The weakness is the switch: if it fails, the whole lab stops, which is unacceptable in an examination. "
                "A full mesh would give each PC many paths, so one failed link would not isolate the lab, but 40 PCs cannot sensibly be fully meshed; the cable count is enormous.\n\n"
                "A practical design is a star, or a tree of stars, with a second switch ready, or two switches so that the server remains reachable. "
                "Reliability here means an examination can continue after one failure. Scalability means next year's larger class can be added without replacing the whole lab. "
                "The pure mesh wins on paper for reliability and loses on cost. The examined answer should say that trade-off in one sentence."
            ),
        },
    ],
    labs=[
        {
            "title": "Lab 1 — Truth table and logic diagram",
            "steps": [
                "On paper, draw F = (A AND B) OR (NOT C). Label every wire.",
                "Complete the eight-row truth table in binary order.",
                "If Logisim (or Logisim-evolution) is installed, build the same circuit, toggle the inputs, and tick each row your table got right.",
                "Change the expression to F = (A NAND B). Record the new table and name the gate.",
            ],
            "success": "Your paper table matches the simulator on all eight rows, or, if you have no simulator, a classmate can recompute two rows you chose at random and get your answers.",
        },
        {
            "title": "Lab 2 — SDLC on one page",
            "steps": [
                "Pick a small system used in college: attendance, library issue, or the result portal.",
                "Write six headings for the SDLC and two bullets under each, specific to that system.",
                "Write three black-box tests and one white-box idea (a branch that must be tried, such as an empty name).",
                "State one risk and how the test plan catches it.",
            ],
            "success": "A reader who was not in the room can tell what will be built and how you will know it failed.",
        },
    ],
    summary=[
        "Digital signals use discrete bits; analog signals vary smoothly and pick up noise when copied.",
        "Learn the identities, De Morgan's laws, and duality. Duality swaps operators and constants; it does not claim the dual expression has the same value.",
        "NAND outputs 0 only when all inputs are 1. XOR outputs 1 when the inputs differ.",
        "Three-input tables have eight rows. Work in columns.",
        "SDLC: analyse, design, code, test, deploy, maintain. Waterfall is one pass. Agile is short cycles. Test from the outside and from the inside.",
        "OSI has seven layers. TCP/IP has four. IP addresses routes; TCP adds reliability; a switch is not a router.",
        "Star is easy and centrally fragile. Mesh is resilient and costly. Scalability and reliability are different compliments.",
        "Encryption is reversible with a key. Hashing is a one-way fingerprint. Authentication is not the same word as authorisation.",
    ],
)
