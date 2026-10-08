"""Extra MCQs and Q&A that are not in the textbook lecture notes."""

from __future__ import annotations

import html
import re


def _mcq_card(n: int, q: str, opts: list[str]) -> str:
    letters = "abcd"
    items = "".join(
        f"<li><b>{letters[i]}.</b> {opt}</li>" for i, opt in enumerate(opts)
    )
    return (
        f'<article class="extra-card mcq-card"><p><b>MCQ {n}.</b> {q}</p>'
        f'<ol class="opts">{items}</ol></article>'
    )


def _block(
    title: str,
    mcq: list[tuple[str, list[str], str]],
    short: list[tuple[str, str]],
    long: list[tuple[str, str]],
) -> str:
    cards = "".join(_mcq_card(i, q, opts) for i, (q, opts, _a) in enumerate(mcq, 1))
    shorts = "".join(f"<li>{q}</li>" for q, _a in short)
    longs = "".join(f"<li>{q}</li>" for q, _a in long)
    keys_mcq = " ".join(
        f"<b>{i}.</b> {a.upper()}" for i, (_q, _o, a) in enumerate(mcq, 1)
    )
    keys_short = "".join(
        f"<li>{html.escape(a) if False else a}</li>" for _q, a in short
    )
    keys_long = "".join(f"<li>{a}</li>" for _q, a in long)
    return f"""
<section class="extra-practice">
  <h3>Extra board practice</h3>
  <p class="muted">These MCQs and questions are extra to the textbook. Close the notes, attempt them, then open the key.</p>
  <div class="extra-grid">{cards}</div>
  <h4>Extra short questions</h4>
  <ol class="short extra-short">{shorts}</ol>
  <h4>Extra long question</h4>
  <ol class="long extra-long">{longs}</ol>
  <div class="answers extra-key">
    <h3>Extra answer key</h3>
    <p><b>MCQs:</b> {keys_mcq}</p>
    <h4>Short</h4>
    <ol>{keys_short}</ol>
    <h4>Long</h4>
    <ol>{keys_long}</ol>
  </div>
</section>
"""


def _bank(title: str, golden: bool) -> tuple[list, list, list]:
    t = title.lower()
    rules = [
        ("discrete", _discrete),
        ("analog", _analog),
        ("boolean", _boolean),
        ("truth table", _boolean),
        ("basic logic", _gates),
        ("and, or, not", _gates),
        ("universal", _universal),
        ("nand", _universal),
        ("minterm", _minterms),
        ("logic expression", _minterms),
        ("karnaugh", _kmap),
        ("k-map", _kmap),
        ("logisim", _logisim),
        ("sdlc", _sdlc),
        ("waterfall", _agile),
        ("agile", _agile),
        ("osi", _osi),
        ("tcp/ip", _tcp),
        ("computational thinking", _ct),
        ("introduction to ct", _ct),
        ("pseudocode", _pseudo),
        ("decomposition", _decomp),
        ("pattern recognition", _pattern),
        ("abstraction", _abs),
        ("bubble", _bubble),
        ("selection sort", _selection),
        ("linear search", _linear),
        ("binary search", _binary),
        ("evaluation criteria", _eval_algo),
        ("which algorithm", _choose_algo),
        ("programming & language", _lang),
        ("career growth with python", _py_career),
        ("ide", _ide),
        ("fundamentals of python", _py_fund),
        ("variables and data", _vars),
        ("input output", _io),
        ("operators", _ops),
        ("control structures", _control),
        ("3.5.1 sequence", _seq),
        ("selection statement", _ifstmt),
        ("repetition", _loops),
        ("libraries in python", _libs),
        ("debugging", _debug),
        ("data, information and database", _data_info),
        ("dbms", _dbms),
        ("database components", _db_comp),
        ("keys and integrity", _keys),
        ("rdbms", _rdbms),
        ("entity relationship", _er),
        ("referential integrity", _refint),
        ("relational schema", _schema),
        ("library management", _library_cs),
        ("database objects", _db_obj),
        ("tables in microsoft", _access_tbl),
        ("designing forms", _forms),
        ("creating queries", _queries),
        ("summarization", _summarize),
        ("visualization in ms access", _access_chart),
        ("computing impacts", _impacts_intro),
        ("artificial intelligence", _ai),
        ("internet of things", _iot),
        ("data analytics", _analytics),
        ("iot vs ai", _compare_tech),
        ("uses of iot", _iot_uses),
        ("ai in education", _ai_edu),
        ("information sources", _sources),
        ("impacts of computing in various", _impacts),
        ("assistive", _assist),
        ("digital literacy", _dl),
        ("types of data", _data_types),
        ("data-collection", _collect),
        ("interviews and surveys", _survey),
        ("prototypes, observation", _proto_obs),
        ("primary and secondary", _primary),
        ("data-collection approach", _approach),
        ("presenting data", _present),
        ("spreadsheets", _present),
        ("digital inquiry", _inquiry),
        ("advanced search", _inquiry),
        ("survey prep", _inquiry),
        ("spreadsheet organization", _inquiry),
        ("conclusion & artefact", _inquiry),
        ("human computer interaction", _hci),
        ("traditional vs natural", _hci_types),
        ("applications of hci", _hci_app),
        ("components of hci", _hci_comp),
        ("types of user interaction", _hci_ui),
        ("interface types", _hci_fb),
        ("importance of hci", _hci_imp),
        ("accessibility", _a11y),
        ("need analysis", _need),
        ("interaction problems", _hci_prob),
        ("improving hci", _hci_fix),
        ("ui vs ux", _uiux),
        ("wireframing", _wire),
        ("evaluate hci", _eval_hci),
        ("testing methods", _test_hci),
        ("correctness", _correct),
        ("trace table", _trace),
        ("clarity of an algorithm", _clarity),
        ("modularity", _modular),
        ("algorithm efficiency", _eff),
        ("big o", _bigo),
        ("number of conditions", _conds),
        ("number of repetitions", _reps),
        ("efficiency evaluation", _eff_fw),
        ("refinements", _refine),
        ("concept of data structure", _ds),
        ("linear data structures", _linear_ds),
        ("non-linear", _nonlinear),
        ("operations on data", _ds_ops),
        ("problem scenarios", _ds_scene),
        ("trace data retrieval", _ds_trace),
        ("data structures in python", _py_ds),
        ("lists (", _lists),
        ("tuples", _tuples),
        ("sets (", _sets),
        ("dictionaries", _dicts),
        ("built-in functions", _builtins),
        ("attendance", _attendance),
        ("word frequency", _wordfreq),
        ("functions in python", _fn),
        ("types of functions", _fn_types),
        ("return values", _fn_ret),
        ("arithmetic calculator", _calc),
        ("scope of local", _scope),
        ("file handling", _files),
        ("with statement", _withstmt),
        ("errors and exceptions", _except),
        ("grade tracker", _grades),
        ("concept of data analysis", _analysis),
        ("data sources and", _connect),
        ("sqlite", _sqlite),
        ("pandas", _pandas),
        ("missing values", _nan),
        ("data organization", _org),
        ("visualization", _charts),
        ("descriptive statistics", _stats),
        ("machine learning, neural", _ml_intro),
        ("machine learning (ml)", _ml),
        ("neural networks (nn)", _nn),
        ("deep learning (dl)", _dl_topic),
        ("components of neural", _nn_parts),
        ("components of deep", _dl_parts),
        ("applications of neural", _nn_app),
        ("secure collaboration", _secure),
        ("data protection", _protect),
        ("security threats", _threats),
        ("identify security", _id_threat),
        ("mitigation", _mitigate),
        ("equity", _equity),
        ("functions of equity", _equity),
        ("collaboration tools", _collab),
        ("entrepreneur and", _ent),
        ("digital age", _digital_ent),
        ("local examples", _local_ent),
        ("problem to business", _idea),
        ("6.4 prototype", _proto),
        ("types of prototypes", _proto_types),
        ("prototype development cycle", _proto_cycle),
        ("class activity: create", _proto_act),
        ("minimum viable", _mvp),
        ("prototype and mvp", _proto_mvp),
        ("riskiest assumption", _risk),
        ("developing an mvp", _mvp_dev),
        ("canteen", _canteen),
        ("testing an mvp", _mvp_test),
        ("beachhead", _beach),
        ("student project", _project),
    ]
    for needle, fn in rules:
        if needle in t:
            return fn(title, golden)
    return _generic(title, golden)


def extra_html(title: str, golden: bool = False) -> str:
    mcq, short, long = _bank(title, golden)
    return _block(title, mcq, short, long)


def chapter_extra_html(grade: str, ch: int, title: str) -> str:
    """Ten extra MCQs appended to the chapter review."""
    sample_title = f"{grade.upper()} chapter {ch} {title}"
    mcq, short, long = _bank(sample_title, True)
    # pad from generic if a chapter title matches poorly
    if len(mcq) < 6:
        g_mcq, g_short, g_long = _generic(title, True)
        mcq = (mcq + g_mcq)[:6]
        short = (short + g_short)[:4]
        long = (long + g_long)[:1]
    return _block(f"Chapter {ch} extra", mcq, short, long)


# ----- topic banks -----

def _generic(title: str, golden: bool):
    mcq = [
        (f"This lecture is mainly about:", [title[:40], "Printer hardware only", "Cooking recipes", "Sports scores"], "a"),
        ("A board answer should usually include:", ["A definition, explanation and example", "Only a yes/no", "A joke", "The teacher’s name"], "a"),
        ("★ Golden topics are:", ["High-yield exam topics", "Optional hobbies", "Printer errors", "Sports"], "a"),
        ("The safest exam habit is:", ["Define · explain · example · diagram", "Memorise one word", "Skip Urdu", "Guess without reading"], "a"),
        ("If two options look similar you should:", ["Pick the one that matches the definition exactly", "Always pick (d)", "Skip the paper", "Change the syllabus"], "a"),
        ("Urdu boxes in this guide are for:", ["The same idea in اردو", "A different syllabus", "Games", "Passwords"], "a"),
    ]
    short = [
        (f"Define the title of this lecture in one sentence: {html.escape(title)}.",
         "Write a one-line textbook definition of the heading, then add one example from class or daily life."),
        ("Give one exam mistake students make on this topic.",
         "Leaving out the example, mixing two nearby terms, or drawing an unlabelled diagram."),
        ("State one real-life example that fits this lecture.",
         "Pick a Karachi/Sindh classroom, shop, hospital or phone example that matches the definition."),
        ("Write the Urdu name of the main term.",
         "Use the Urdu box in the lecture; keep the English technical word in brackets."),
    ]
    long = [
        (f"Write a 10-mark answer on: {html.escape(title)}. Include definition, three points, one example and a diagram or table.",
         "Opening definition (2). Three explained points (6). Example + labelled diagram/table (2). Finish with one exam warning."),
    ]
    return mcq, short, long


def _discrete(title, golden):
    return (
        [
            ("A discrete quantity is:", ["Counted in separate steps", "Any value on a smooth range", "Always analog", "A sine wave"], "a"),
            ("Temperature of tea is:", ["Continuous", "Discrete", "Only Boolean", "A gate"], "a"),
            ("Number of students in a class is:", ["Discrete", "Continuous", "Analog voltage", "A ramp"], "a"),
            ("The stairs vs ramp analogy: stairs are:", ["Discrete", "Continuous", "TCP", "Agile"], "a"),
            ("Digital systems use:", ["0 and 1", "Every real number", "Only sine waves", "Paper only"], "a"),
            ("A bit is:", ["A binary digit, 0 or 1", "Eight bytes", "A logic gate", "A database"], "a"),
        ],
        [
            ("Differentiate discrete and continuous with one example each.",
             "Discrete: countable steps (cars in a park). Continuous: any value in a range (speed of a car)."),
            ("Why do computers prefer digital values?",
             "Bits 0/1 can be restored after noise; analog waves are bent by interference."),
            ("What is a digital system?",
             "An electronic system that stores and processes only two values, 0 and 1."),
            ("Give two advantages of digital systems.",
             "Reliable (noise resistant), accurate copies, easy to design (two states), programmable."),
        ],
        [
            ("With a labelled stairs/ramp sketch, explain discrete vs continuous and link both to analog vs digital signals.",
             "Stairs = discrete/digital (fixed levels). Ramp = continuous/analog (smooth). Computers convert analog measurements into bits, process bits, then convert back if a human must see the result."),
        ],
    )


def _analog(title, golden):
    return (
        [
            ("An analog signal:", ["Changes smoothly, like a sine wave", "Jumps only 0/1", "Is a truth table", "Is TCP"], "a"),
            ("A digital signal looks like:", ["A square wave of HIGH and LOW", "A smooth sine", "A pie chart", "A stack"], "a"),
            ("Noise harms analog more because:", ["Many in-between levels can be bent", "Bits cannot exist", "OSI has 7 layers", "Python is analog"], "a"),
            ("Human voice on a microphone is first:", ["Analog", "A Boolean 1 only", "A K-map", "SQL"], "a"),
            ("HIGH in digital means:", ["1 / ON / TRUE", "0 / OFF", "A continuous ramp", "Gray code"], "a"),
            ("Copying analog tape many times:", ["Loses quality", "Stays perfect", "Creates bits", "Builds NAND"], "a"),
        ],
        [
            ("Define analog signal and digital signal.",
             "Analog: continuous, smooth change. Digital: only two levels, HIGH(1) and LOW(0), a square wave."),
            ("Give one example of each.",
             "Analog: traditional thermometer / voice. Digital: computer data / logic pulse."),
            ("Why is digital more reliable?",
             "A bent 0 or 1 can be restored to a clean 0 or 1; analog distortion stays in the wave."),
            ("What does a computer do with analog sound?",
             "Sample and quantise it into bits, process the bits, then convert back to analog for a speaker."),
        ],
        [
            ("Draw analogue (sine) and digital (square) waves. Tabulate nature and reliability. This is a ★ Golden 10-mark.",
             "Sine labelled V against t; square labelled HIGH/LOW. Table: analog = continuous, low reliability; digital = discrete bits, high reliability. Close with the noise argument."),
        ],
    )


def _boolean(title, golden):
    return (
        [
            ("Boolean algebra uses:", ["TRUE(1) and FALSE(0) only", "All real numbers", "ASCII letters", "IPv4"], "a"),
            ("AND is 1 only when:", ["Every input is 1", "Any input is 1", "Inputs differ", "There is no input"], "a"),
            ("OR is 1 when:", ["Any input is 1", "All inputs are 0", "Inputs are equal", "NOT is applied twice"], "a"),
            ("NOT of 1 is:", ["0", "1", "2", "A"], "a"),
            ("Rows in an n-input truth table:", [r"\(2^n\)", "n", "n²", "n+1"], "a"),
            ("Two-input truth table has:", ["4 rows", "2 rows", "8 rows", "16 rows"], "a"),
        ],
        [
            ("Who developed Boolean algebra and what two values does it use?",
             "George Boole. TRUE(1) and FALSE(0)."),
            ("Write Y = A · B and Y = A + B in words.",
             "AND: output 1 only if all inputs are 1. OR: output 1 if any input is 1."),
            ("Why is NOT called unary?",
             "It has only one operand: it inverts a single input."),
            ("List the four steps to build a truth table.",
             "Count inputs n; rows = 2ⁿ; list combinations in binary order; compute each output."),
        ],
        [
            ("Write complete truth tables for 2-input AND, OR and 1-input NOT. Add one real-life lock/door/switch example each.",
             "AND 0001 on AB=11 (two locks). OR 0111 (two doors). NOT 10 / 01 (light switch). Show all four/two rows."),
        ],
    )


def _gates(title, golden):
    return (
        [
            ("Logic gates implement:", ["Boolean operations in hardware", "SQL joins", "HTTP only", "Pie charts"], "a"),
            ("AND output is 1 for inputs 1,1:", ["1", "0", "Z", "X"], "a"),
            ("OR of 1 and 0 is:", ["1", "0", "NAND", "XOR"], "a"),
            ("The inverter is the:", ["NOT gate", "AND gate", "Bus", "Router"], "a"),
            ("Building blocks of digital systems are:", ["Logic gates", "Spreadsheets", "MVPs", "Fonts"], "a"),
            ("Y = A · B is the:", ["AND expression", "OR expression", "XOR", "NOR"], "a"),
        ],
        [
            ("Define a logic gate.",
             "An electronic circuit that performs a Boolean operation; the building block of digital systems."),
            ("State the AND, OR, NOT expressions.",
             "Y = A·B ; Y = A+B ; Y = A' (or Ā)."),
            ("Draw the truth table of 2-input AND from memory.",
             "00→0, 01→0, 10→0, 11→1."),
            ("Why is NOT drawn with a bubble?",
             "The bubble marks inversion of the input."),
        ],
        [
            ("For AND, OR and NOT: symbol, expression, full truth table, and one daily-life model. ★ Golden.",
             "Standard IEC/US symbols. AND two locks, OR two doors, NOT a switch. Tables must have every row."),
        ],
    )


def _universal(title, golden):
    return (
        [
            ("NAND and NOR are universal because:", ["Any circuit can be built from only that gate", "They are analog", "They store files", "They sort arrays"], "a"),
            ("NAND is:", ["NOT of AND", "AND of NOT", "OR of XOR", "Only OR"], "a"),
            ("NAND of 1,1 is:", ["0", "1", "Z", "2"], "a"),
            ("NOR of 0,0 is:", ["1", "0", "A", "B"], "a"),
            ("XOR is 1 when inputs are:", ["Different", "Both 1 only", "Both 0 only", "Always 1"], "a"),
            ("XNOR is 1 when inputs are:", ["The same", "Different", "Only 1,0", "Floating"], "a"),
        ],
        [
            ("Why are NAND and NOR called universal gates?",
             "Any Boolean function (AND, OR, NOT, XOR…) can be built using only NAND, or only NOR."),
            ("Write NAND and NOR expressions.",
             "Y = (A·B)' and Y = (A+B)'."),
            ("Memory trick for XOR vs XNOR.",
             "XOR: eXclusively different → 1. XNOR: same → 1 (equivalence)."),
            ("Truth table of XOR.",
             "00→0, 01→1, 10→1, 11→0."),
        ],
        [
            ("Show how a NOT, AND and OR can each be built from NAND only. Include truth-table checks.",
             "NOT: NAND with inputs tied. AND: NAND then NAND-NOT. OR: invert inputs with NAND-NOTs then NAND (De Morgan). Tables must match the target gate."),
        ],
    )


def _minterms(title, golden):
    return (
        [
            ("Precedence (highest first) is:", ["( ) then NOT then AND then OR", "OR then AND then NOT", "AND then ( ) then OR", "XOR first always"], "a"),
            ("A minterm is used when Y is:", ["1 (SOP)", "0 (POS)", "Always 0", "A stack"], "a"),
            ("For AB=01 if Y=1 the minterm is:", ["A'B", "AB", "A+B", "A'B'"], "a"),
            ("A maxterm is a:", ["Sum (OR) for a 0 output", "Product for a 1", "K-map only", "Gate delay"], "a"),
            ("SOP means:", ["Sum of products", "Sum of people", "Stack of pointers", "Set of pies"], "a"),
            ("In a logic diagram you draw first the operation with:", ["Highest precedence", "Lowest precedence", "Most inputs", "Green ink"], "a"),
        ],
        [
            ("State operator precedence in Boolean algebra.",
             "Parentheses, NOT, AND, OR."),
            ("Define minterm and maxterm.",
             "Minterm: AND of all variables (complemented if 0) for rows where Y=1. Maxterm: OR of all variables (complemented if 1) for rows where Y=0."),
            ("From Y rows 01 and 11 = 1, write SOP.",
             "Y = A'B + AB."),
            ("For Y = A·B + C, which gate is drawn first?",
             "AND (A·B), then OR with C, because AND beats OR."),
        ],
        [
            ("Given a 2-input truth table with Y = 0,1,0,1, write minterms, SOP, maxterms that apply, and draw the logic diagram.",
             "Y=1 on 01 and 11 → A'B + AB which simplifies to B. Diagram: if unsimplified, two ANDs into an OR; simplified, Y=B (wire). Show both and say examiners accept the simplified form if working is shown."),
        ],
    )


def _kmap(title, golden):
    return (
        [
            ("Adjacent K-map cells differ by:", ["One bit (Gray code)", "Two bits", "The output only", "ASCII"], "a"),
            ("Group sizes must be:", ["Powers of 2 (1,2,4,8…)", "Only 3", "Only 5", "Prime numbers"], "a"),
            ("A 3-variable K-map has:", ["8 cells", "4 cells", "3 cells", "16 cells"], "a"),
            ("Wrapping left to right is:", ["Allowed", "Forbidden", "Only for XOR", "Only analog"], "a"),
            ("Inside a group, variables that change are:", ["Eliminated", "Doubled", "ANDed twice", "Sent to OR first"], "a"),
            ("We group:", ["1s (for SOP)", "Only 0s always", "Gray cells empty", "Page numbers"], "a"),
        ],
        [
            ("What is a K-map?",
             "A grid for simplifying Boolean expressions. Adjacent cells differ by one bit (Gray code)."),
            ("State the grouping rules.",
             "Groups of 1,2,4,8…; as large as possible; overlap allowed; wrap around edges; drop variables that change inside the group."),
            ("Gray code order for two bits.",
             "00, 01, 11, 10."),
            ("Why not group three 1s as a triple?",
             "3 is not a power of 2, so it is not a valid grouping."),
        ],
        [
            ("Simplify Y(A,B,C) = Σm(0,2,4,6) with a 3-variable K-map. Show cells, groups and the final expression.",
             "Cells m0,m2,m4,m6 are 1 (even minterms). They form a quad: C is 0 in all, A and B change → Y = C'. Label Gray columns 00 01 11 10. Draw the wrap/quad clearly."),
        ],
    )


def _logisim(*_):
    return (
        [
            ("LogiSim Evolution is used to:", ["Draw and simulate logic circuits", "Edit videos", "Send email", "Compile Java only"], "a"),
            ("The canvas is where you:", ["Place and wire gates", "Install Python", "Write SQL", "Draw pie charts"], "a"),
            ("Poke tool is for:", ["Toggling inputs while simulating", "Deleting the OS", "Printing Urdu", "Sorting"], "a"),
            ("Attribute table sets:", ["Inputs, facing, labels", "Big O", "IP addresses", "Passwords"], "a"),
            ("To build Y=A·B you need:", ["AND gate plus two inputs and an output", "Only XOR", "A stack", "Pandas"], "a"),
            ("Simulation lets you check:", ["The truth table live", "HTTP status", "File modes", "HCI wireframes only"], "a"),
        ],
        [
            ("Name four areas of the LogiSim window.",
             "Menu bar, toolbar, explorer (libraries), attribute table, drawing canvas."),
            ("Steps to build Y=A·B.",
             "Place AND; add two input pins; add output pin; wire; label; simulate with Poke."),
            ("Where do you change the number of inputs on a gate?",
             "Attribute table (bottom left)."),
            ("Why simulate at all if the truth table is already on paper?",
             "Catches wiring mistakes and shows students the table “come alive”."),
        ],
        [
            ("Describe, with a canvas sketch, how you would build and test Y = A·B + C in LogiSim.",
             "AND for A,B; OR with C; three inputs, one output; wiring; poke all 8 combinations; tick the truth table. Mention facing and labels."),
        ],
    )


def _sdlc(*_):
    return (
        [
            ("SDLC is:", ["A structured process from idea to retired software", "A logic gate", "A search algorithm", "A chart type"], "a"),
            ("The first SDLC phase is usually:", ["Requirement analysis", "Maintenance", "Coding only", "Retirement"], "a"),
            ("A deliverable is:", ["The document or product of a phase", "A Boolean 1", "A pie slice", "An IP port"], "a"),
            ("Testing comes:", ["After implementation, before deployment", "Before requirements", "Instead of design", "Never"], "a"),
            ("Maintenance is:", ["Fixing and updating after release", "The first interview", "NAND", "Big O"], "a"),
            ("SDLC exists to:", ["Control quality, cost and time", "Replace Boolean algebra", "Draw K-maps", "Sort arrays"], "a"),
        ],
        [
            ("Define SDLC.",
             "Software Development Life Cycle: a structured process that guides software from beginning to end."),
            ("List the six phases in order.",
             "Requirements, design, implementation/coding, testing, deployment, maintenance."),
            ("Name one deliverable of requirements and of design.",
             "SRS / requirements document; design diagrams or architecture document."),
            ("Why not jump straight to coding?",
             "Wrong requirements become expensive bugs; SDLC catches them on paper first."),
        ],
        [
            ("Tabulate the six SDLC phases with activities and one deliverable each. ★ Golden 10-mark.",
             "Phase | activities | deliverable. Stress that testing uses the requirements as the oracle, and maintenance is the longest phase in real life."),
        ],
    )


def _agile(*_):
    return (
        [
            ("Waterfall is:", ["Linear — finish a phase before the next", "2-week sprints", "Random order", "A gate"], "a"),
            ("Agile builds software in:", ["Short sprints with feedback", "One giant leap only", "Hardware NAND", "OSI layer 1"], "a"),
            ("You cannot easily go back in:", ["Waterfall", "Agile", "Both equally", "Neither"], "a"),
            ("Customer sees a working slice first in:", ["Agile", "Pure waterfall", "K-maps", "Binary search"], "a"),
            ("A hospital records system with frozen law rules fits:", ["Waterfall", "Only Agile memes", "No SDLC", "HCI pie charts"], "a"),
            ("Changing shop-app features weekly fits:", ["Agile", "Waterfall only", "TCP", "Selection sort"], "a"),
        ],
        [
            ("Define Waterfall and Agile in one line each.",
             "Waterfall: sequential phases, no going back. Agile: iterative sprints (about 2–4 weeks) with customer feedback."),
            ("Give one advantage of each.",
             "Waterfall: clear documents and deadlines. Agile: change is cheap and the user sees value early."),
            ("Give one disadvantage of each.",
             "Waterfall: late change is painful. Agile: needs an available customer and can look undocumented."),
            ("When would you pick Waterfall?",
             "Stable, legally frozen requirements (e.g. a regulated records system)."),
        ],
        [
            ("Compare Waterfall vs Agile on five dimensions and attach one Sindh-college case to each model.",
             "Dimensions: order, change, customer, documentation, risk. Case Waterfall: board exam-result system with fixed rules. Case Agile: college app whose features keep changing after student feedback."),
        ],
    )


def _osi(*_):
    return (
        [
            ("OSI has:", ["7 layers", "4 layers", "2 layers", "12 layers"], "a"),
            ("Layer 7 is:", ["Application", "Physical", "Network", "Data link"], "a"),
            ("IP addressing lives at:", ["Network (layer 3)", "Application", "Physical", "Session"], "a"),
            ("Cables and bits are:", ["Physical", "Presentation", "Session", "Application"], "a"),
            ("End-to-end ports (TCP/UDP) are:", ["Transport", "Network", "Physical", "Data link"], "a"),
            ("The model that explains “how data travels” is a:", ["Communication model", "Sort algorithm", "K-map", "MVP"], "a"),
        ],
        [
            ("Write the 7 OSI layers from top to bottom.",
             "Application, Presentation, Session, Transport, Network, Data Link, Physical."),
            ("One job of Transport and of Network.",
             "Transport: reliability/ports (TCP/UDP). Network: routing and logical addressing (IP)."),
            ("Why layer models?",
             "Each layer has a small job; vendors can change one layer without rewriting the rest."),
            ("Mnemonic you will actually write in the exam.",
             "Please Do Not Throw Sausage Pizza Away (bottom-up) or All People Seem To Need Data Processing (top-down)."),
        ],
        [
            ("Name all 7 OSI layers with one job and one protocol/hardware example each. ★ Golden.",
             "7 App HTTP/DNS; 6 Pres encryption/JPEG; 5 Sess dialogs; 4 Trans TCP/UDP; 3 Net IP/routers; 2 DL frames/MAC/switches; 1 Phy cables/bits/hubs. Draw the stack."),
        ],
    )


def _tcp(*_):
    return (
        [
            ("TCP/IP has:", ["4 layers", "7 layers", "2 layers", "9 layers"], "a"),
            ("TCP/IP Application equivalent OSI layers are:", ["5,6,7", "Only 1", "Only 3", "2 and 3"], "a"),
            ("Internet layer ≈ OSI:", ["Network", "Physical", "Application", "Session"], "a"),
            ("Host-to-network ≈ OSI:", ["Physical + Data Link", "Only Application", "Only Transport", "Session + Presentation"], "a"),
            ("The real Internet uses:", ["TCP/IP", "Only the 7-layer hardware", "K-maps", "Waterfall"], "a"),
            ("HTTP sits in TCP/IP at:", ["Application", "Internet", "Network Interface", "Physical only"], "a"),
        ],
        [
            ("Name the four TCP/IP layers.",
             "Application, Transport, Internet, Network Access (Host-to-Network)."),
            ("Map them onto OSI.",
             "App = OSI 5–7; Transport = 4; Internet = 3; Network Access = 1–2."),
            ("Why do we still teach OSI?",
             "OSI is the teaching/reference model; TCP/IP is what packets actually follow."),
            ("Where does a router work in each model?",
             "OSI Network; TCP/IP Internet layer."),
        ],
        [
            ("Draw OSI (7) beside TCP/IP (4), draw mapping bands, and explain two differences plus one similarity.",
             "Similarity: both are layered communication models. Differences: 7 vs 4; OSI is reference, TCP/IP is implemented. HTTP/TCP/IP/Ethernet example walking down the stack."),
        ],
    )


def _ct(*_):
    return (
        [
            ("Computational thinking is:", ["A systematic way to solve problems", "Only typing Python", "Only drawing gates", "A database key"], "a"),
            ("An algorithm is:", ["A step-by-step finite method to solve a problem", "A random guess", "A picture of a PC", "An IP address"], "a"),
            ("CT pillars include:", ["Decomposition, pattern, abstraction, algorithm", "Only encryption", "Only HTML", "Only Agile sprints"], "a"),
            ("Algorithms must halt:", ["After finitely many steps", "Never", "Only on Fridays", "After OSI layer 1"], "a"),
            ("Cooking a recipe is like:", ["An algorithm", "A K-map group of 3", "A XOR of pies", "Big O of clouds"], "a"),
            ("CT is useful even:", ["Without a computer", "Only inside NAND", "Only in Figma", "Only in SQLite"], "a"),
        ],
        [
            ("Define computational thinking.",
             "Solving problems by breaking them down, spotting patterns, hiding detail (abstraction) and writing algorithms."),
            ("Define algorithm with two properties.",
             "Ordered, finite, unambiguous steps that produce a result. Precision + finiteness."),
            ("Give a non-computer algorithm.",
             "Making tea / finding a roll number in a sorted list."),
            ("How is CT different from “just coding”?",
             "CT is the thinking; coding is one way to write the algorithm down."),
        ],
        [
            ("Take “assign 200 students to exam rooms”. Apply the four CT pillars and then write a 6-step algorithm.",
             "Decompose: rooms, students, constraints. Pattern: groups of 30. Abstract: ignore bag colours. Algorithm: numbered steps with a stop condition. Mention input/output."),
        ],
    )


def _pseudo(*_):
    return (
        [
            ("Pseudocode is:", ["English-like steps for an algorithm, not a real language", "Runnable C++", "A logic gate", "A pie chart"], "a"),
            ("An algorithm vs pseudocode: algorithm is:", ["The idea/method", "Always Python", "Always a table", "Always OSI"], "a"),
            ("Pseudocode should be:", ["Clear enough to code from", "Encrypted", "Drawn as NAND only", "A CSV file"], "a"),
            ("Keywords like IF, WHILE in pseudocode are:", ["Control, written in capitals by convention", "Python-only", "SQL-only", "Illegal"], "a"),
            ("You write pseudocode:", ["Before coding", "After the program crashes only", "Instead of requirements", "On OSI layer 1"], "a"),
            ("A flowchart is:", ["A diagram of the algorithm", "A database index", "A stack pop", "A sprint"], "a"),
        ],
        [
            ("Differentiate algorithm and pseudocode.",
             "Algorithm: the method. Pseudocode: a structured English write-up of that method that a programmer can translate."),
            ("Give two pseudocode conventions.",
             "Capital keywords (IF, WHILE); one step per line; indent blocks; START/END."),
            ("Why not write Python immediately?",
             "Pseudocode is language-independent and easier to correct on paper."),
            ("Write 5 lines of pseudocode to add two numbers.",
             "START; READ a,b; SET s ← a+b; PRINT s; END."),
        ],
        [
            ("Write an algorithm AND pseudocode to find the largest of three numbers. ★ Golden.",
             "Algorithm numbered 1…n. Pseudocode with IF/ELSE. Same logic. Show a dry-run with 4, 9, 7 → 9."),
        ],
    )


def _decomp(*_):
    return (
        [
            ("Decomposition means:", ["Breaking a big problem into smaller parts", "Hiding detail", "Finding repeats", "Sorting"], "a"),
            ("A college admission system split into forms, tests, lists is:", ["Decomposition", "Binary search", "Encryption", "A pie"], "a"),
            ("Smaller parts should be:", ["Solvable on their own, then combined", "Random", "Always analog", "Always O(n!)"], "a"),
            ("Without decomposition, teams:", ["Block each other on one giant task", "Finish faster always", "Need no tests", "Use only XOR"], "a"),
            ("Decomposition is a CT:", ["Strategy / pillar", "Gate", "File mode", "Chart"], "a"),
            ("Which is NOT decomposition?", ["Writing one 400-line main() with everything mixed", "Split into input/process/output modules", "Separate UI and marks logic", "One function per report"], "a"),
        ],
        [
            ("Define decomposition with an example.",
             "Split a complex task. Example: library system → members, books, issue, fine."),
            ("How does it help testing?",
             "Each small part can be tested before integration."),
            ("Link decomposition to later functions in Python.",
             "Each piece becomes a function or module."),
            ("What is the opposite mistake?",
             "A monoblock of mixed logic that nobody can reuse."),
        ],
        [
            ("Decompose “online canteen pre-order for a college”. List 6 sub-problems and the interface between two of them.",
             "Menu, account, cart, payment, kitchen queue, pickup. Cart posts item-id+qty to kitchen. Draw a simple block diagram."),
        ],
    )


def _pattern(*_):
    return (
        [
            ("Pattern recognition is:", ["Spotting repeats and rules in data", "Hiding details", "Breaking into parts", "A TCP flag"], "a"),
            ("If every student card has name+photo+id, that is a:", ["Pattern", "Virus", "K-map wrap", "Sprint"], "a"),
            ("Patterns let you:", ["Reuse a solution", "Delete the algorithm", "Avoid abstraction", "Skip testing"], "a"),
            ("Spam filters look for:", ["Patterns in text", "OSI layer 1 copper", "NAND only", "Beachhead markets"], "a"),
            ("No pattern means:", ["Treat the case as unique", "Always bubble sort", "Always pie charts", "Always Agile"], "a"),
            ("CT pillar closest to “I’ve seen this shape of problem” is:", ["Pattern recognition", "Physical layer", "Variance", "Figma"], "a"),
        ],
        [
            ("Define pattern recognition.",
             "Finding regularities, repetitions or rules so you can reuse a method."),
            ("Give a school example.",
             "Every paper has roll, name, marks — same record shape, same processing loop."),
            ("How do patterns shrink an algorithm?",
             "One loop or one function handles every similar case."),
            ("What if you force a pattern that is not there?",
             "Wrong reuse — the solution fails on the odd case."),
        ],
        [
            ("Show pattern recognition on: (a) attendance lists, (b) weather by month, (c) login screens. For each, name the repeating structure and the algorithm you reuse.",
             "(a) row per student → linear scan/count. (b) month+value → line graph / average. (c) username+password+submit → same validation function."),
        ],
    )


def _abs(*_):
    return (
        [
            ("Abstraction means:", ["Hiding extra detail, keeping what matters", "Adding every detail", "Sorting slowly", "Drawing 7 OSI layers always"], "a"),
            ("A metro map that is not to scale is:", ["Abstraction", "A truth table", "A histogram", "A key"], "a"),
            ("In coding, a function header without inner code is:", ["Abstraction of how", "Decomposition only", "A race condition", "NAND"], "a"),
            ("Too little abstraction:", ["Overwhelms you with noise", "Always speeds Big O", "Creates XOR", "Fixes phishing"], "a"),
            ("Too much abstraction:", ["Hides a detail you actually need", "Prints SQL", "Draws K-maps", "Creates sprints"], "a"),
            ("A data type (list, stack) is an abstraction of:", ["How items are stored/accessed", "TCP ports", "Screen DPI", "Figma frames"], "a"),
        ],
        [
            ("Define abstraction.",
             "Hide unnecessary features; keep the essential ones needed to solve the problem."),
            ("Give a transport example.",
             "Bus timetable shows stops and times, not engine temperature."),
            ("Give a programming example.",
             "You call sort(list) without writing the swap loop."),
            ("How is abstraction different from decomposition?",
             "Decomposition splits; abstraction hides. You often do both."),
        ],
        [
            ("For a college library app, list five details to keep and five to hide. Justify each as abstraction.",
             "Keep: ISBN, availability, due date, member id, fine. Hide: shelf paint colour, server fan speed, librarian’s tea break, exact disk blocks, CSS pixels. Link to a simple interface of search/issue/return."),
        ],
    )


def _bubble(*_):
    return (
        [
            ("Bubble sort repeatedly:", ["Swaps adjacent out-of-order pairs", "Picks the global min into place", "Halves a sorted list", "Hashes keys"], "a"),
            ("After pass 1 of bubble, the largest item is:", ["At the end", "At the start always", "Deleted", "In a stack"], "a"),
            ("Best-case bubble (already sorted, with flag) is:", [r"\(O(n)\)", r"\(O(n^2)\) always", r"\(O(1)\)", r"\(O(n!)\)"], "a"),
            ("Typical/worst bubble is:", [r"\(O(n^2)\)", r"\(O(\log n)\)", r"\(O(n)\)", r"\(O(n^3)\)"], "a"),
            ("On 8,4 the first swap gives:", ["4,8", "8,4", "0,0", "4,4"], "a"),
            ("Bubble is easy but:", ["Slow on large n", "Faster than binary search on sorted data", "A graph algorithm", "O(1) memory sort of magic"], "a"),
        ],
        [
            ("Define bubble sort.",
             "Repeatedly compare adjacent items and swap if they are in the wrong order so large values “bubble” to the end."),
            ("Dry-run one pass on 8,4,1.",
             "8>4 swap → 4,8,1; 8>1 swap → 4,1,8. Largest 8 is at the end."),
            ("Space complexity?",
             "O(1) extra — in-place."),
            ("When is bubble acceptable?",
             "Tiny lists or teaching; not for thousands of records."),
        ],
        [
            ("Trace bubble sort on 8,4,1,9,3 until sorted. Show each pass. State comparisons in the worst case for n=5.",
             "Passes: after p1 …3,8,4,1,9 wait — actually 8,4,1,9,3 → 4,1,8,3,9 → 1,4,3,8,9 → 1,3,4,8,9 → 1,3,4,8,9. Worst comparisons n(n-1)/2 = 10."),
        ],
    )


def _selection(*_):
    return (
        [
            ("Selection sort each pass:", ["Selects the minimum from the unsorted part and swaps it into place", "Swaps only adjacent", "Needs a sorted list first", "Uses a stack"], "a"),
            ("After k passes, the first k items are:", ["The k smallest in order", "Random", "The k largest", "Deleted"], "a"),
            ("Comparisons are about:", [r"\(O(n^2)\) even if nearly sorted", r"\(O(n)\)", r"\(O(1)\)", r"\(O(\log n)\)"], "a"),
            ("Swaps per pass: at most:", ["One", "n", "n²", "Zero always"], "a"),
            ("Selection vs bubble: selection usually has:", ["Fewer swaps", "Fewer comparisons", "Better Big O", "A hash table"], "a"),
            ("On 8,4,1 min of whole list is:", ["1, swapped to front", "8", "4", "9"], "a"),
        ],
        [
            ("Define selection sort.",
             "Repeatedly select the smallest remaining item and swap it into the next position."),
            ("One pass on 8,4,1,9,3.",
             "Min=1, swap with 8 → 1,4,8,9,3."),
            ("Why still O(n²) if data is sorted?",
             "You still scan the unsorted suffix every pass; there is no early exit like flagged bubble."),
            ("Stable?",
             "Classic selection is not stable (equal keys can swap order)."),
        ],
        [
            ("Full trace of selection sort on 8,4,1,9,3. Count swaps. Compare swap count with bubble on the same list.",
             "Passes put 1, then 3, then 4, then 8,9. Swaps: 8↔1, 4↔3, 8↔4, maybe 8↔8 skip, 9 in place. Bubble does more adjacent swaps. Both O(n²) comparisons."),
        ],
    )


def _linear(*_):
    return (
        [
            ("Linear search checks:", ["Each item in order until found or the list ends", "Only the middle", "Only the last", "A binary tree"], "a"),
            ("It works on:", ["Sorted or unsorted lists", "Sorted lists only", "Graphs only", "Empty files only"], "a"),
            ("Worst comparisons for n items:", ["n", "log n", "1", "n²"], "a"),
            ("Best case is:", ["Target is first: 1 comparison", "Always n", "Always log n", "0"], "a"),
            ("If the item is absent:", ["You scan the whole list", "You halt at mid", "You pop a stack", "You draw a pie"], "a"),
            ("Linear search is also called:", ["Sequential search", "Binary search", "Hash search", "Interpolation always"], "a"),
        ],
        [
            ("Define linear search.",
             "Examine each element from the start until the target is found or the list ends."),
            ("Advantage vs binary.",
             "No need to sort first; works on any list."),
            ("Disadvantage.",
             "O(n) — slow for huge lists."),
            ("Trace search for 7 in 8,3,6,1,7.",
             "8≠,3≠,6≠,1≠,7= found at index 4 (0-based) / position 5."),
        ],
        [
            ("Write pseudocode for linear search that returns the index or −1. Dry-run a hit and a miss.",
             "FOR i ← 0 TO n-1: IF a[i]=t RETURN i; RETURN −1. Hit example and miss example with counts."),
        ],
    )


def _binary(*_):
    return (
        [
            ("Binary search requires:", ["A sorted list", "An unsorted list", "A graph", "A pie chart"], "a"),
            ("Each step discards:", ["About half the remaining items", "One item only", "The whole list", "Only even numbers"], "a"),
            ("Complexity is:", [r"\(O(\log n)\)", r"\(O(n)\)", r"\(O(n^2)\)", r"\(O(1)\) always"], "a"),
            ("If mid value is too big you go:", ["Left half", "Right half", "To a stack", "To OSI layer 7"], "a"),
            ("On sorted [1..8] searching 3, first mid is:", ["4 (value 4), then go left", "1", "8", "7"], "a"),
            ("Binary search on unsorted data is:", ["Wrong / may miss", "Always faster", "A sort", "A gate"], "a"),
        ],
        [
            ("Define binary search and its precondition.",
             "Repeatedly test the middle of a sorted list; go left or right. List must already be sorted."),
            ("Why O(log n)?",
             "n → n/2 → n/4 … until 1. About log₂ n steps."),
            ("What if the list is unsorted?",
             "Sort first (extra cost) or use linear search."),
            ("Trace 3 in [1,2,3,4,5,6,7,8].",
             "mid 4; 3<4 left [1,2,3,4]; mid 2; 3>2 right [3,4]; mid 3 found."),
        ],
        [
            ("Write binary-search pseudocode with low, high, mid. Trace two targets (present and absent) on an 8-item sorted list. ★ Golden.",
             "WHILE low≤high: mid=(low+high)//2; equal return; less → high=mid-1; greater → low=mid+1. Absent: low>high → not found. Show the shrinking intervals."),
        ],
    )


def _eval_algo(*_):
    return (
        [
            ("Correctness means:", ["Output matches the spec, including edges", "The code is short", "It uses XOR", "It prints Urdu"], "a"),
            ("Time efficiency is:", ["How fast it grows with n", "Font size", "Cable length", "Number of comments"], "a"),
            ("Space efficiency is:", ["Extra memory used", "Screen brightness", "TCP window only", "Pie slices"], "a"),
            ("An edge case for divide is:", ["Divisor 0", "n=100 always", "Color of GUI", "Sprint length"], "a"),
            ("Readability is part of:", ["Quality / clarity, not Big O itself", "Physical layer", "NAND grouping", "Variance"], "a"),
            ("You evaluate an algorithm before coding so you can:", ["Pick a good one", "Skip tests", "Avoid variables", "Draw Figma only"], "a"),
        ],
        [
            ("List four evaluation criteria.",
             "Correctness, time, space, clarity/simplicity (and sometimes completeness)."),
            ("What is an edge case?",
             "An extreme input: empty list, n=1, already sorted, not found, 0."),
            ("Correct but slow — is it acceptable?",
             "For tiny n yes; for huge n you need a better Big O."),
            ("How do you show correctness in XI/XII?",
             "Trace table or stepwise reasoning plus test cases."),
        ],
        [
            ("Compare linear vs binary search using correctness, time, space, preconditions and a 10,000-name example.",
             "Both can be correct. Linear O(n) any order; binary O(log n) needs sort. Space O(1). 10k names: ~10k vs ~14 comparisons. Mention the cost of keeping the list sorted."),
        ],
    )


def _choose_algo(*_):
    return (
        [
            ("If the list is unsorted and n is small, search with:", ["Linear search", "Binary search immediately", "Dijkstra", "Quicksort only"], "a"),
            ("If the list is sorted and n is huge, search with:", ["Binary search", "Linear only", "Bubble", "OSI"], "a"),
            ("If you must sort a class of 20 names by hand:", ["Simple O(n²) is fine", "You must use O(n log n) hardware", "K-maps", "HCI"], "a"),
            ("Memory is tiny: prefer:", ["In-place algorithms", "Huge extra arrays", "Storing every trace forever", "Videos"], "a"),
            ("Need a stable sort of equal keys:", ["Do not pick unstable selection without care", "Always XOR", "Always pie", "Always Agile"], "a"),
            ("The first questions are:", ["n? sorted? time vs memory?", "Font? Colour? OSI?", "NAND count only", "Figma frames"], "a"),
        ],
        [
            ("List four questions before choosing an algorithm.",
             "Input size? Sorted? Need speed or memory? Stable? Worst vs average?"),
            ("When is O(n²) OK?",
             "Small n, or the inner work is tiny, or you run it rarely."),
            ("When must you use binary search?",
             "Large sorted collection, many queries."),
            ("Give a wrong choice and why.",
             "Binary search on unsorted roll numbers — may miss the target."),
        ],
        [
            ("A college has 30 students (daily) and 50,000 archived papers (yearly search). Recommend sort/search for each situation with reasons.",
             "Daily: selection/bubble or even by-hand; linear search. Archive: keep sorted, binary search (or a database index). State Big O and a precondition."),
        ],
    )


def _lang(*_):
    return (
        [
            ("A program is:", ["A set of instructions", "A mouse", "A cable", "A pie"], "a"),
            ("High-level languages are:", ["Closer to English (Python, C++)", "Only 0 and 1", "Only analog", "Only SQL"], "a"),
            ("Machine language is:", ["Binary codes for the CPU", "Python", "Urdu", "HTML always"], "a"),
            ("C++ is typically:", ["High-level, closer to hardware than Python", "A DBMS", "A chart", "An OSI layer"], "a"),
            ("Python is popular in XI because:", ["Simple syntax, huge libraries", "It is binary only", "It cannot print", "It is analog"], "a"),
            ("The translator of Python is a:", ["Interpreter (also compiles to bytecode)", "Router", "Switch", "K-map"], "a"),
        ],
        [
            ("Define program and programming language.",
             "Program: instructions for a computer. Language: the notation used to write them."),
            ("Differentiate high-level and low-level.",
             "High-level: English-like, portable. Low-level: close to hardware, faster but harder."),
            ("Name three high-level languages and one use each.",
             "Python data/scripts; C++ systems/games; Java apps — (accept similar)."),
            ("Why are computers “dumb” without programs?",
             "They only follow instructions; they do not understand the problem."),
        ],
        [
            ("Compare machine, assembly and high-level languages in a table (readability, speed, portability, example). Link why this course uses Python.",
             "Machine 0/1 fastest least portable; assembly mnemonics; high-level portable. Python: readable, batteries included, matches the Sindh practicals."),
        ],
    )


def _py_career(*_):
    return (
        [
            ("Python careers include:", ["Data analyst, web, automation, AI", "Only plumber", "Only analog technician", "Only OS kernel in 1950"], "a"),
            ("Python is used in AI because:", ["Libraries like TensorFlow/Pandas exist", "It is binary only", "It cannot loop", "It has no syntax"], "a"),
            ("A scripting job often means:", ["Automating repetitive tasks with Python", "Soldering NAND", "Drawing OSI only", "Figma only"], "a"),
            ("Learning Python in XI helps later with:", ["XII data analysis and file handling", "Cooking only", "Cabling only", "Waterfall contracts only"], "a"),
            ("Syntax of Python is:", ["Clear and beginner-friendly", "Harder than machine code", "Only umlauts", "Mandatory semicolons always"], "a"),
            ("Open-source means:", ["The language/tools are free to use and inspect", "You must pay per loop", "Closed NAND", "Secret OSI"], "a"),
        ],
        [
            ("Give four career paths that use Python.",
             "Developer, data analyst, automation/scripting, AI/ML, teaching, testing."),
            ("Why do employers like Python?",
             "Fast to write, huge ecosystem, readable by teams."),
            ("What should an XI student build as proof?",
             "Small projects: bill calculator, file grader, attendance list."),
            ("Is Python the only language you will ever need?",
             "No — but it is a strong first language and used in this syllabus."),
        ],
        [
            ("Write a 10-mark “career connection” answer: three jobs, the Python skill each needs from this chapter, and one ethical warning.",
             "Analyst: data types+libraries. Developer: control structures. Automation: files later in XII. Ethics: do not scrape private student data without permission."),
        ],
    )


def _ide(*_):
    return (
        [
            ("An IDE is:", ["One app to write, run and debug code", "A printer", "A sort", "A cable"], "a"),
            ("VS Code is:", ["A popular editor/IDE", "A DBMS", "An OSI layer", "A gate"], "a"),
            ("The terminal/run button is for:", ["Executing the program", "Drawing pie charts only", "Sending TCP SYN only", "K-maps"], "a"),
            ("Syntax highlighting helps you:", ["See keywords and mistakes", "Sort faster", "Encrypt disks", "Route packets"], "a"),
            ("A file explorer in VS Code shows:", ["Project files", "OSI layer 1", "NAND groups", "Beachhead users"], "a"),
            ("Debugging in an IDE uses:", ["Breakpoints and variable watch", "Only bubble sort", "Only pie charts", "Only Agile stickers"], "a"),
        ],
        [
            ("Define IDE.",
             "Integrated Development Environment: editor + run + debug + files in one place."),
            ("Name four VS Code areas.",
             "Activity bar/sidebar (files), editor, terminal, status bar (and extensions)."),
            ("Why not use Notepad only?",
             "No easy run, no highlighting, no debugger."),
            ("What is an extension?",
             "An add-on (Python plugin) that teaches VS Code a language."),
        ],
        [
            ("Describe how you would create, run and debug a first Python file in VS Code. Include two interface elements from the notes.",
             "New file .py, type print, Run Python, read terminal. Mention top menu, explorer, terminal panel. Breakpoint on a wrong variable."),
        ],
    )


def _py_fund(*_):
    return (
        [
            ("Python runs statements:", ["From top to bottom (unless control changes that)", "Randomly", "Only backwards", "Only on even lines"], "a"),
            ("A statement is:", ["One instruction", "A mouse", "A layer", "A sprint"], "a"),
            ("Comments start with:", ["#", "// always only", "<!--", "REM"], "a"),
            ("Indentation in Python is:", ["Syntax (blocks)", "Optional decoration", "Only for Urdu", "A compiler flag in C"], "a"),
            ("print is:", ["An output function", "A sort", "A gate", "A key"], "a"),
            ("Python files use extension:", [".py", ".docx", ".mp4", ".exe only"], "a"),
        ],
        [
            ("What is the basic structure of a Python program?",
             "Statements in order: comments, imports, variables, processing, output."),
            ("Why does indentation matter?",
             "It defines which lines belong to if/for/def. Wrong indent = error or wrong logic."),
            ("Write a 3-line program that stores 5 in x and prints it.",
             "x = 5; print(x) plus optional comment."),
            ("What does the interpreter do?",
             "Reads each line and executes it (via bytecode)."),
        ],
        [
            ("Write a tiny program that asks for a name and prints a greeting. Label sequence, input, output and a comment.",
             "name = input(...); print(\"Hello\", name). Arrow of sequence. Comment with #. Mention string type."),
        ],
    )


def _vars(*_):
    return (
        [
            ("A variable is:", ["A named memory space", "A printer", "An OSI hub", "A sprint"], "a"),
            ("Python types include:", ["int, float, str, bool", "Only NAND", "Only charts", "Only files"], "a"),
            ("You need to declare types first in Python?", ["No — assignment creates the variable", "Yes, like old C always", "Only for print", "Only in SQL"], "a"),
            ("True and False are:", ["bool", "str", "float only", "lists"], "a"),
            ("\"17\" is a:", ["str, not int", "int", "bool", "dict"], "a"),
            ("A legal name is:", ["total_marks", "2nd", "class", "total-marks"], "a"),
        ],
        [
            ("Define variable and give the assignment syntax.",
             "Named storage. name = value."),
            ("List four data types with one example each.",
             "int 5; float 5.0; str \"Ali\"; bool True."),
            ("Why is \"17\" + \"1\" = \"171\"?",
             "Strings concatenate; convert with int() for arithmetic."),
            ("Give two identifier rules.",
             "Start with letter/underscore; no spaces; no keywords; case-sensitive."),
        ],
        [
            ("A program reads two marks as input() and should print the average. Show types, conversions, and a common bug if you forget int().",
             "a=int(input()); b=int(input()); print((a+b)/2). Without int, + concatenates strings. Average is float."),
        ],
    )


def _io(*_):
    return (
        [
            ("print() is for:", ["Output to the screen", "Reading files only", "Sorting", "OSI routing"], "a"),
            ("input() always returns a:", ["str", "int", "bool", "list"], "a"),
            ("To read an integer you write:", ["int(input(...))", "print(input)", "float only", "open('r')"], "a"),
            ("sep in print controls:", ["The string between items", "File mode", "Big O", "Color of NAND"], "a"),
            ("end in print controls:", ["What is printed after the items (default newline)", "SQL commit", "TCP port", "K-map wrap"], "a"),
            ("Prompt text goes:", ["Inside input(\"...\")", "Inside NAND", "In OSI layer 1", "In a pie"], "a"),
        ],
        [
            ("Write a print that shows Ali and 85 separated by a colon.",
             "print(\"Ali\", 85, sep=\":\") → Ali:85 (space rules depend on sep)."),
            ("Why convert input?",
             "input is str; arithmetic needs int/float."),
            ("What does end=\"\" do?",
             "Stops print from moving to the next line."),
            ("Show a safe pattern to read a float.",
             "x = float(input(\"Marks: \"))."),
        ],
        [
            ("Write a program that asks for item and price, prints a labelled bill line, and explain each I/O call. Mention a type-conversion bug.",
             "item=input(); price=float(input()); print(item, price). If price stays str you cannot multiply quantity. Show output."),
        ],
    )


def _ops(*_):
    return (
        [
            ("% is:", ["Remainder (modulo)", "Power", "AND gate", "Floor always in Python 3 /"], "a"),
            ("** is:", ["Exponent", "XOR", "Comment", "Input"], "a"),
            ("== tests:", ["Equality (Boolean)", "Assignment", "Bitwise AND", "File open"], "a"),
            ("and/or/not are:", ["Logical operators", "Bitwise only", "SQL only", "HTML"], "a"),
            ("5 & 3 (bitwise AND) is:", ["1", "8", "15", "0"], "a"),
            ("= vs == : = is:", ["Assignment", "Comparison", "Power", "Comment"], "a"),
        ],
        [
            ("Define operator and operand.",
             "Operator: the symbol. Operand: the value it works on. In 3+4, + is operator, 3 and 4 operands."),
            ("List arithmetic operators.",
             "+ - * / // % **"),
            ("Relational operators return what type?",
             "bool True/False."),
            ("Compute 11 % 3 and 2**3.",
             "2 and 8."),
        ],
        [
            ("For A=6 (110), B=3 (011) show AND OR XOR bitwise, then show 6>3 and 6==3. Explain assignment vs comparison.",
             "AND 010=2; OR 111=7; XOR 101=5. 6>3 True; 6==3 False. = stores, == asks."),
        ],
    )


def _control(*_):
    return (
        [
            ("The three basic control structures are:", ["Sequence, selection, repetition", "AND, OR, NOT", "OSI 1,2,3", "Mean, median, mode"], "a"),
            ("Sequence means:", ["One after another", "Skip around", "Loop forever", "Sort first"], "a"),
            ("Selection uses:", ["if / elif / else", "only for", "only def", "only import"], "a"),
            ("Repetition uses:", ["for / while", "print only", "class only", "try only"], "a"),
            ("Almost every useful program mixes:", ["All three", "Only comments", "Only gates", "Only charts"], "a"),
            ("A flowchart diamond is:", ["A decision (selection)", "A process always", "A file", "A stack"], "a"),
        ],
        [
            ("Define the three control structures.",
             "Sequence: order. Selection: choose a path. Repetition: repeat a block."),
            ("Give a school example of each.",
             "Seq: enter marks then print. Sel: if fail, reprint. Rep: for each student."),
            ("What happens if you only have sequence?",
             "The program cannot react or repeat — it is a straight recipe."),
            ("How do you show them in a flowchart?",
             "Rectangles process, diamonds decisions, arrows loops back."),
        ],
        [
            ("The shopping-bill program uses all three structures. Identify one line of each and explain why the bill would be wrong if that structure vanished.",
             "Seq: print header then loop. Sel: if qty invalid. Rep: while more items. Without loop only one item; without if bad qty; without sequence output is unordered."),
        ],
    )


def _seq(*_):
    return (
        [
            ("In sequence, line 2 runs:", ["After line 1 finishes", "Before line 1", "In parallel always", "Never"], "a"),
            ("x=2; x=x+1; print(x) prints:", ["3", "2", "1", "x"], "a"),
            ("Sequence bugs are often:", ["Wrong order of statements", "Missing NAND", "OSI layer skip", "Pie explode"], "a"),
            ("You cannot print a variable:", ["Before you assign it", "After you assign it", "Using print", "In comments"], "a"),
            ("Sequence is the default in:", ["Python", "Only Prolog", "Only SQL joins", "Only CSS"], "a"),
            ("Swap two variables needs:", ["A temp (or Python a,b=b,a) in the right order", "A K-map", "A router", "A sprint"], "a"),
        ],
        [
            ("Define sequence.",
             "Statements executed in the order they are written."),
            ("Show a 4-step sequence to compute area of a rectangle.",
             "Read L; read W; area=L*W; print area."),
            ("What is a NameError from order?",
             "Printing x before x = ..."),
            ("Can sequence include comments?",
             "Yes; comments are not executed but sit in order in the file."),
        ],
        [
            ("Write two versions of a “read marks, total, average” program — one with statements in a sensible sequence and one in a broken order. Explain the error.",
             "Broken: print average before computing it, or total before reading marks. NameError or wrong value. Correct numbered steps."),
        ],
    )


def _ifstmt(*_):
    return (
        [
            ("if runs its block when the condition is:", ["True", "False", "A string always", "A list"], "a"),
            ("else runs when:", ["The if condition is False", "Always", "Never", "Only on Sundays"], "a"),
            ("elif is for:", ["More conditions, first True wins", "Loops", "Files", "Imports"], "a"),
            ("Nested if means:", ["An if inside another if", "Two prints", "A stack pop", "A pie"], "a"),
            ("marks>=40 is a:", ["Boolean condition", "Assignment", "Comment", "Gate delay"], "a"),
            ("if x=5: is:", ["Syntax error (use ==)", "Correct assignment if", "A loop", "A class"], "a"),
        ],
        [
            ("Write if-else to print Pass if marks≥40.",
             "if marks>=40: print(\"Pass\") else: print(\"Fail\")."),
            ("When do you need elif vs nested if?",
             "elif: mutually exclusive bands (A/B/C). Nested: a second question that only matters if the first is True."),
            ("What is a dead elif?",
             "A later condition that can never run because an earlier one already caught those values."),
            ("Trace marks=75 through A≥80, B≥65, C≥50, else.",
             "Not A, B True → B. Later elifs skipped."),
        ],
        [
            ("Write a nested-if program: if present, then if marks≥40 Pass else Fail; if absent print Absent. Show traces for three students.",
             "Outer: present yes/no. Inner: pass/fail. Traces: Absent; Present 30 Fail; Present 55 Pass. Indentation must be correct."),
        ],
    )


def _loops(*_):
    return (
        [
            ("for i in range(3) runs:", ["i=0,1,2", "i=1,2,3", "i=3,2,1", "forever"], "a"),
            ("while repeats while the condition is:", ["True", "False", "A file", "None always"], "a"),
            ("break:", ["Exits the loop immediately", "Skips one line only", "Closes Python", "Commits SQL"], "a"),
            ("continue:", ["Skips the rest of this iteration", "Ends the program", "Defines a function", "Opens a file"], "a"),
            ("A nested loop: inner runs:", ["Fully for each outer step", "Once in total", "Never", "Only if NAND"], "a"),
            ("range(2, 6) yields:", ["2,3,4,5", "2,3,4,5,6", "1,2,3,4,5,6", "6,5,4"], "a"),
        ],
        [
            ("When for vs while?",
             "for: known count / iterate a sequence. while: unknown count, stop on a condition."),
            ("What is an infinite loop?",
             "while True without break, or a condition that never becomes False."),
            ("Trace s=0; for i in range(1,4): s+=i.",
             "i=1 s=1; i=2 s=3; i=3 s=6."),
            ("Shopping bill uses which loop typically?",
             "while more items (unknown count) or for a known list of items."),
        ],
        [
            ("Write nested loops to print a 3×3 table of i,j. Then rewrite the shopping-bill outline with a while, a running total, and an if on quantity.",
             "for i in range(3): for j in range(3): print(i,j). Bill: total=0; while True: read item/qty; if qty<=0: continue; if item==\"end\": break; total+=...; print total."),
        ],
    )


def _libs(*_):
    return (
        [
            ("A library is:", ["Pre-written functions you import", "A logic gate", "A cable", "A sprint"], "a"),
            ("math is:", ["Built-in / standard library", "Third-party only", "A DBMS", "An OSI layer"], "a"),
            ("pandas is:", ["Third-party (pip install)", "Built into every tiny Python", "A sort algorithm", "A gate"], "a"),
            ("import math then square root is:", ["math.sqrt(x)", "sqrt x", "x** without import always for sqrt", "print.sqrt"], "a"),
            ("random.randint(1,6) is for:", ["A dice integer 1–6", "Sorting", "Files", "TCP"], "a"),
            ("pip installs:", ["Third-party packages", "The CPU", "OSI layer 1", "Urdu fonts only"], "a"),
        ],
        [
            ("Differentiate built-in and third-party libraries.",
             "Built-in ship with Python (math, random, sqlite3). Third-party need pip (pandas, matplotlib)."),
            ("How do you call a library function?",
             "import lib; lib.func(...) or from lib import func."),
            ("Give two built-in and two third-party examples from this course.",
             "Built-in: math, random (or sqlite3 in XII). Third: pandas, matplotlib."),
            ("Why libraries?",
             "Do not reinvent sqrt, CSV readers, or plots."),
        ],
        [
            ("Write a tiny program using math and random, then explain how you would add pandas (install + import). Mention a mistake: importing before installing.",
             "import math, random; print(math.pi, random.randint(1,6)). Terminal: pip install pandas. Then import pandas as pd. ImportError if pip was skipped."),
        ],
    )


def _debug(*_):
    return (
        [
            ("A syntax error is:", ["Broken grammar; the program will not run", "Wrong answer but it runs", "A crash while running", "A slow Big O"], "a"),
            ("A runtime error is:", ["A crash while running (e.g. /0, missing file)", "A missing colon only", "A wrong formula that still prints", "A comment"], "a"),
            ("A logic error is:", ["Runs but the answer is wrong", "Always a crash", "Always SyntaxError", "A font"], "a"),
            ("A traceback tells you:", ["File, line, error type, message", "OSI layer only", "The teacher’s marks", "Big O"], "a"),
            ("int(\"hi\") raises:", ["ValueError (runtime)", "A logic silent bug", "SyntaxError always", "Success"], "a"),
            ("Using = instead of == in if is usually:", ["SyntaxError", "A correct if", "A sort", "A pie"], "a"),
        ],
        [
            ("Name the three error types with one example each.",
             "Syntax: if x==1 print (missing :). Runtime: 1/0. Logic: average = a+b without /2."),
            ("How do you read a traceback from the bottom?",
             "Last line is the error; above it the call stack; look at your file’s line number."),
            ("How do you hunt a logic error?",
             "Print/trace variables, test edge cases, compare with a worked example."),
            ("Does a logic error show a traceback?",
             "No — that is why they are dangerous."),
        ],
        [
            ("Classify five bugs: missing colon; int(input) on \"A\"; average without divide; wrong indent of else; open missing file. For each give type + fix.",
             "Syntax; runtime ValueError; logic; syntax/logic indent; runtime FileNotFoundError. Fixes: add colon; validate input; /n; match indent; check path/try-except."),
        ],
    )


def _data_info(*_):
    return (
        [
            ("Data is:", ["Raw unprocessed facts", "Always information", "Always a graph", "A program"], "a"),
            ("Information is:", ["Processed, meaningful data", "Noise only", "A cable", "A gate"], "a"),
            ("A database is:", ["An organised collection of related data", "A single unsorted scrap", "A CPU fan", "A pie chart"], "a"),
            ("Marks 45, 67, 12 are:", ["Data", "Information already", "A query", "A report"], "a"),
            ("\"Ali failed\" after processing marks is:", ["Information", "Raw data only", "A primary key", "A form"], "a"),
            ("Storing related tables together is the job of a:", ["Database", "Compiler", "Router", "K-map"], "a"),
        ],
        [
            ("Differentiate data and information with a school example.",
             "Data: 45, 67. Information: class average is 56 so we need extra classes."),
            ("Define database.",
             "Organised related data stored so it can be retrieved quickly."),
            ("Give two problems of storing data only in paper lists.",
             "Slow search, duplication, hard updates, errors."),
            ("Is a phone contacts app a database?",
             "Yes — organised related records (name, number)."),
        ],
        [
            ("A college keeps loose pages of marks. Argue, with definitions, why they should move to a database, and what information a principal could then get.",
             "Define data/information/database. Benefits: search, consistency, reports (fail list, subject averages). One risk: need backup/access control."),
        ],
    )


def _dbms(*_):
    return (
        [
            ("A DBMS is software that:", ["Creates and manages databases", "Draws only pie charts", "Routes IP", "Sorts using bubble only"], "a"),
            ("Examples of DBMS:", ["MS Access, MySQL, SQLite, Oracle", "Python only", "Figma only", "Chrome only"], "a"),
            ("DBMS handles:", ["Storage, retrieval, security, multi-user access", "Only fonts", "Only OSI layer 1", "Only NAND"], "a"),
            ("Without a DBMS, programs would:", ["Each invent their own file format", "Run faster always", "Need no keys", "Need no SQL"], "a"),
            ("Access is used in XI because:", ["It is a GUI DBMS for tables/forms/queries/reports", "It is a programming language", "It is Agile", "It is analog"], "a"),
            ("SQLite in XII is a:", ["Lightweight DBMS/library", "Chart", "Gate", "Sprint"], "a"),
        ],
        [
            ("Define DBMS.",
             "Database Management System: software to define, store, query, protect and share a database."),
            ("Four DBMS functions.",
             "Create tables, insert/update/delete, query, enforce keys/security, backup."),
            ("DBMS vs database.",
             "Database is the data; DBMS is the software that manages it."),
            ("Name two desktop and two server DBMS.",
             "Desktop: Access, SQLite. Server: MySQL, Oracle, PostgreSQL."),
        ],
        [
            ("Compare managing 500 students in Excel vs a DBMS (Access). Use data integrity, search, multi-user and reports.",
             "Excel: easy but duplicates, weak keys, clash when two people edit. DBMS: primary keys, queries, forms, reports, controlled access."),
        ],
    )


def _db_comp(*_):
    return (
        [
            ("A table is:", ["Rows and columns of one entity type", "A Python for-loop", "A cable", "A sprint"], "a"),
            ("A record is:", ["One row", "One column", "The DBMS name", "A query"], "a"),
            ("A field/attribute is:", ["One column", "The whole database", "A report", "A form"], "a"),
            ("A value in one cell is:", ["A data item", "A relationship", "A schema", "A view"], "a"),
            ("Students table columns might be:", ["id, name, class", "AND, OR, NOT", "HTTP, TCP", "Mean, π"], "a"),
            ("Many records share the same:", ["Fields (structure)", "Primary key value", "OSI layer", "Random NAND"], "a"),
        ],
        [
            ("Define table, record, field.",
             "Table: entity set. Record: one instance. Field: one property."),
            ("Give a 3-field student record example.",
             "101 | Ali | 85"),
            ("What is a data type of a field?",
             "The kind of value: Number, Text, Date, Yes/No."),
            ("Why not put two entities in one messy table?",
             "Duplication and update anomalies — later ER/normalisation."),
        ],
        [
            ("Design a Marks table: fields, types, one sample record, and which field will likely become the primary key.",
             "roll (Number, PK), name (Text), subject (Text), marks (Number). Sample 12, Ali, CS, 85. Justify uniqueness of roll or roll+subject."),
        ],
    )


def _keys(*_):
    return (
        [
            ("A primary key:", ["Uniquely identifies each record", "May freely repeat", "Is always a name", "Is a chart"], "a"),
            ("A candidate key is:", ["Any field set that could be the PK", "A foreign key", "A report", "A form"], "a"),
            ("An alternate key is:", ["A candidate not chosen as PK", "A duplicate PK", "A null PK", "A pie"], "a"),
            ("A foreign key:", ["Refers to a PK in another table", "Is always unique in its table", "Sorts the table", "Encrypts the DB"], "a"),
            ("NULL in a primary key is:", ["Not allowed", "Required", "A default", "A relationship type"], "a"),
            ("Integrity constraints exist to:", ["Stop invalid data", "Draw graphs", "Route packets", "Compile Python"], "a"),
        ],
        [
            ("Define PK, FK, candidate, alternate.",
             "PK: chosen unique identifier. Candidate: any unique identifier. Alternate: unused candidate. FK: copy of another table’s PK."),
            ("Give a two-table example with an FK.",
             "Students(roll PK); Marks(roll FK, subject, score)."),
            ("Entity integrity rule.",
             "PK unique and not NULL."),
            ("Why not use student name as PK?",
             "Names duplicate and change."),
        ],
        [
            ("For Members and Borrow in a library, choose keys and write two integrity rules. Show one invalid insert the DBMS should reject. ★ Golden.",
             "MemberID PK; Borrow(BorrowID PK, MemberID FK). Reject Borrow with unknown MemberID or NULL MemberID. Mention cascade later."),
        ],
    )


def _rdbms(*_):
    return (
        [
            ("RDBMS stores data in:", ["Related tables (relations)", "Only XML trees", "Only graphs", "Only analog tapes"], "a"),
            ("A relation is a:", ["Table with unique rows", "Python list", "OSI hub", "Sprint"], "a"),
            ("SQL is:", ["The language to query relational data", "A gate", "A sort", "A font"], "a"),
            ("Access and MySQL are:", ["RDBMS products", "Compilers", "Browsers", "Cables"], "a"),
            ("Relationships use:", ["Foreign keys", "Pie charts", "Sine waves", "Sprints"], "a"),
            ("“Relational” refers to:", ["Tables linked by keys", "Family relations of staff", "TCP relation", "Agile rituals"], "a"),
        ],
        [
            ("Define RDBMS.",
             "Relational DBMS: data in tables with keys and SQL."),
            ("Two advantages over a single flat file.",
             "Less duplication; relationships; queries; integrity."),
            ("What is a tuple in theory class language?",
             "A row/record."),
            ("Name two RDBMS used in this syllabus.",
             "MS Access (XI), SQLite (XII)."),
        ],
        [
            ("Explain with a 2-table sketch how an RDBMS models Students and Courses (many-to-many via Enrolment). Identify each key.",
             "Students(sid PK), Courses(cid PK), Enrolment(sid FK, cid FK, year) composite uniqueness. This is the relational way to store M:N."),
        ],
    )


def _er(*_):
    return (
        [
            ("An ER model is drawn:", ["Before building tables", "After deleting the DB", "Only in Python", "Only in OSI"], "a"),
            ("An entity is:", ["A real-world thing we store", "A Python keyword", "A cable", "A sprint"], "a"),
            ("A relationship 1:M means:", ["One A, many B", "Many A, many B only", "One to one only", "No link"], "a"),
            ("M:N in an RDBMS needs:", ["A bridge/associative table", "A pie chart", "A stack", "A NAND"], "a"),
            ("A diamond in ER often shows:", ["A relationship", "An attribute oval only", "A PK square", "A report"], "a"),
            ("Cardinality is:", ["1:1, 1:M, M:N", "Big O", "TCP window", "Variance"], "a"),
        ],
        [
            ("Define ER model.",
             "Entity-Relationship: conceptual design of entities, attributes, relationships."),
            ("Three relationship types with examples.",
             "1:1 person–NIC; 1:M mother–children / member–borrows; M:N students–courses."),
            ("How do you convert 1:M to tables?",
             "PK of the 1 side copied as FK on the M side."),
            ("Why ER first?",
             "Cheaper to fix a diagram than a populated database."),
        ],
        [
            ("Draw ER for Library: Member, Book, Borrow. Mark keys, cardinality, and how you resolve M:N. ★ Golden.",
             "Member 1—M Borrow M—1 Book (Borrow as relationship-entity with date). If Book–Member M:N, Borrow is the bridge with composite/surrogate key."),
        ],
    )


def _refint(*_):
    return (
        [
            ("Referential integrity means:", ["Every FK matches an existing PK (or is NULL if allowed)", "Names are unique", "Files are encrypted", "Charts are labelled"], "a"),
            ("Cascade update:", ["Changes child FKs when the parent PK changes", "Deletes the DBMS", "Sorts tables", "Draws ER"], "a"),
            ("Cascade delete:", ["Deletes child rows when the parent is deleted", "Inserts a parent", "Creates a view", "Opens a form"], "a"),
            ("Inserting an FK that does not exist should:", ["Be rejected", "Be auto-sorted", "Draw a pie", "Start Agile"], "a"),
            ("Orphan records are:", ["Child rows whose parent is gone", "Primary keys", "Reports", "Queries"], "a"),
            ("Referential integrity is enforced by the:", ["DBMS", "Monitor", "Mouse", "Compiler of Python only"], "a"),
        ],
        [
            ("Define referential integrity.",
             "FK values must exist in the parent PK (unless NULL is allowed)."),
            ("What does cascade update solve?",
             "If roll number 12 becomes 112, all Marks.roll 12 become 112 automatically."),
            ("When is cascade delete dangerous?",
             "Deleting a member could wipe years of borrow history — sometimes restrict instead."),
            ("Give an invalid operation.",
             "INSERT borrow for MemberID 999 when no such member."),
        ],
        [
            ("In Members–Borrow, specify restrict vs cascade for UPDATE and DELETE with a Sindh-college story. ★ Golden.",
             "UPDATE MemberID: cascade so old cards still match. DELETE member who still has books: restrict (cannot delete). DELETE member with no books: allow. Show one rejected SQL/Access action."),
        ],
    )


def _schema(*_):
    return (
        [
            ("A relational schema is:", ["The blueprint of tables, keys, types", "A running query result", "A pie chart", "A Python list"], "a"),
            ("Student(roll PK, name, class) is a:", ["Schema notation", "Python call", "OSI frame", "MVP"], "a"),
            ("Schema is designed:", ["Before stuffing thousands of rows", "After losing the backup", "Instead of ER", "By the compiler"], "a"),
            ("Data types in schema stop:", ["Wrong values (text in marks)", "TCP errors", "NAND delay", "Figma overflow"], "a"),
            ("Foreign keys in schema implement:", ["Relationships", "Sorts", "Charts", "Sprints"], "a"),
            ("Changing schema later is:", ["Painful once data exists", "Free always", "Impossible in Access", "A gate"], "a"),
        ],
        [
            ("Define relational schema.",
             "Formal structure: relation names, attributes, types, keys."),
            ("Write schema for Book.",
             "Book(ISBN PK, title, author, copies: Number)."),
            ("How does schema differ from ER?",
             "ER is conceptual diagram; schema is the relational implementation."),
            ("Name two things schema documents besides columns.",
             "PKs, FKs, unique, not null, relationships."),
        ],
        [
            ("Turn your library ER into a schema listing: three tables, keys, two constraints. Justify one data type.",
             "Member(MemberID PK, name Text, phone Text unique). Book(ISBN PK, title Text, copies Number). Borrow(BorrowID PK, MemberID FK, ISBN FK, date Date). Copies is Number because you count them."),
        ],
    )


def _library_cs(*_):
    return (
        [
            ("The library case study starts from:", ["Requirements", "Random tables", "Pie charts", "Sprints only"], "a"),
            ("Member to Borrow is typically:", ["1:M", "Always 1:1", "No relation", "M:1 the other way only if reversed"], "a"),
            ("Book to Borrow is typically:", ["1:M (one book title/copy can be borrowed many times)", "Always M:N without a bridge", "1:1 mandatory", "A stack"], "a"),
            ("M:N Member–Book is resolved by:", ["Borrow record table", "A pie", "A NAND", "OSI"], "a"),
            ("A good case-study answer shows:", ["ER then schema then sample rows", "Only careers", "Only Python turtle", "Only Figma"], "a"),
            ("Fine calculation would be stored in:", ["Borrow (or computed in a query)", "The OSI header", "A K-map", "A histogram bin"], "a"),
        ],
        [
            ("List four requirements of a college library system.",
             "Register members; catalogue books; issue/return; calculate fines; search."),
            ("Name the entities.",
             "Member, Book, Borrow (and maybe Copy if multiple copies)."),
            ("Why a Borrow entity?",
             "The issue event has its own date/fine — and it breaks M:N."),
            ("One report the librarian wants.",
             "Overdue list: member, book, days late."),
        ],
        [
            ("Walk the seven case-study steps from the notes: requirements → entities → attributes → relationships → keys → resolve M:N → final ER. Draw the final diagram.",
             "Follow the textbook library walk-through. Final: Member 1–M Borrow M–1 Book. Keys labelled. One sentence on cascade."),
        ],
    )


def _db_obj(*_):
    return (
        [
            ("The four Access objects are:", ["Tables, forms, queries, reports", "Lists, tuples, sets, dicts", "AND OR NOT XOR", "HTTP TCP IP ETH"], "a"),
            ("Tables store:", ["The actual data", "Only print layout", "Only VBA", "Only charts"], "a"),
            ("Forms are for:", ["Friendly data entry", "Physical cabling", "Big O proofs", "Sorting theories"], "a"),
            ("Queries:", ["Ask questions / filter / calculate without changing stored rows (select)", "Always delete tables", "Draw OSI", "Compile C"], "a"),
            ("Reports are for:", ["Printable summaries", "Capturing packets", "NAND grouping", "Figma prototypes"], "a"),
            ("You should enter daily data in a:", ["Form (not raw datasheet if avoidable)", "Report", "Macro only", "Relationship window only"], "a"),
        ],
        [
            ("Role of each object in one line.",
             "Table: store. Form: enter. Query: ask. Report: print/share."),
            ("Why not type into reports?",
             "Reports are output; they do not store new rows."),
            ("A select query does not:",
             "By itself permanently delete table data (unless you run a delete-query)."),
            ("Give one example object for a library.",
             "Query: books overdue; Report: overdue letters; Form: issue desk."),
        ],
        [
            ("Design the four objects for an attendance database. Say what each contains and how a teacher uses them in one period.",
             "Table Students+Attendance. Form mark present. Query absentees today. Report monthly letter. Flow: form → table → query → report."),
        ],
    )


def _access_tbl(*_):
    return (
        [
            ("Design View is best when you:", ["Need full control of names, types, keys before data", "Want a random spreadsheet", "Draw Figma", "Ping a router"], "a"),
            ("Datasheet View is for:", ["Typing rows after the structure exists", "Defining PK only", "Writing Python", "OSI captures"], "a"),
            ("A Number field should not store:", ["Phone numbers that need leading zeros (use Text)", "Marks", "Counts", "IDs that are truly numeric"], "a"),
            ("Primary key is set in:", ["Design View (key icon)", "A report footer", "A pie", "Agile sticky"], "a"),
            ("Yes/No fields store:", ["Boolean-like presence", "Paragraphs", "Images only", "OSI layers"], "a"),
            ("Creating tables is step one because:", ["Everything else hangs on the structure", "Reports can store data", "Queries invent columns from nothing always", "Forms replace keys"], "a"),
        ],
        [
            ("Steps to create a table in Design View.",
             "Create → Table Design; field name; data type; PK; save name."),
            ("When Datasheet create is OK?",
             "Quick throwaway; still go back to Design to set PK/types."),
            ("Why set field size/validation?",
             "Stop 999 marks out of 100; stop 40-character roll numbers."),
            ("Name three data types you used in class.",
             "Short Text, Number, Date/Time, Yes/No, Currency, AutoNumber."),
        ],
        [
            ("Create (on paper) Design View for Students: four fields, PK, one validation rule, and say what error Access shows if the rule fails.",
             "Roll AutoNumber/Number PK; Name Short Text required; Marks Number 0–100 validation; Passed Yes/No. Invalid marks: validation text “0 to 100”."),
        ],
    )


def _forms(*_):
    return (
        [
            ("A form is:", ["A screen for entering/editing records", "A printed summary only", "A TCP socket", "A sort"], "a"),
            ("Bound controls show:", ["Fields from a table/query", "Random clipart only", "OSI headers", "NAND"], "a"),
            ("Validation on a form:", ["Stops bad keystrokes before they hit the table", "Sorts binary search", "Encrypts OSI", "Draws histograms"], "a"),
            ("A combo box is for:", ["Picking from a list (e.g. class names)", "Drawing ER", "Pinging", "Compiling"], "a"),
            ("Why forms vs datasheet?",
             ["Fewer mistakes, one-record focus, hidden dangerous fields", "Forms store more rows than tables", "Datasheets cannot show data", "Forms replace primary keys"], "a"),
            ("Navigation buttons on a form:", ["Move among records", "Create queries", "Set PK", "Start sprints"], "a"),
        ],
        [
            ("Define form.",
             "Interface to enter, edit, view records, with validation."),
            ("Two controls and their use.",
             "Text box: name. Combo: class list. Button: save/new."),
            ("How does a form enforce a rule visually?",
             "Required star, dropdown instead of free text, cannot tab off an empty PK."),
            ("Wizard vs Design View?",
             "Wizard fast; Design for layout and extra controls."),
        ],
        [
            ("Design an Issue-Book form: record source, four controls, one validation, and how it prevents an orphan borrow.",
             "Source Borrow+combo of MemberID and ISBN from parent tables (combo bound to FK). Date default today. Validation: due>issue. Combo prevents typing a non-existent member."),
        ],
    )


def _queries(*_):
    return (
        [
            ("A query is:", ["A request to retrieve/filter/calculate data", "A printed letter", "A cable", "A gate"], "a"),
            ("Criteria in a query:", ["Filter rows (e.g. Marks>=40)", "Change field types", "Draw ER", "Set the OS"], "a"),
            ("A parameter query asks:", ["The user for a value at run time", "The CPU voltage", "TCP window", "Figma frames"], "a"),
            ("Select queries by default:", ["Do not delete stored rows", "Always wipe the table", "Always cascade", "Always print"], "a"),
            ("Sorting in a query:", ["Orders the result (Asc/Desc)", "Changes PK", "Encrypts", "Creates a form"], "a"),
            ("This topic is ★ because board papers love:", ["Writing criteria and showing results", "Cabling", "NAND only", "Sprints"], "a"),
        ],
        [
            ("Define query.",
             "A saved question that selects, filters, sorts, calculates from tables."),
            ("Write criteria: CS students with marks < 40.",
             "Class = \"CS\" AND Marks < 40 (field names as in the table)."),
            ("Difference between filter on a datasheet and a query.",
             "Query is reusable, can join tables, calculate, feed reports."),
            ("What is a calculated field in a query?",
             "Total:[Math]+[Eng] — not stored, computed."),
        ],
        [
            ("Design a query: join Students and Marks, show Fail list (marks<40) sorted by name, with a calculated column 40-Marks as Needed. Write QBE grid/SQL-like criteria. ★ Golden.",
             "Tables joined on roll. Fields Name, Subject, Marks, Needed: 40-[Marks]. Criteria Marks<40. Sort Name. Result sample two rows."),
        ],
    )


def _summarize(*_):
    return (
        [
            ("Grouping in a query:", ["Collapses rows that share a value (e.g. by class)", "Deletes the table", "Draws OSI", "Opens Figma"], "a"),
            ("Count(*) with group by class gives:", ["How many students per class", "The PK", "A pie automatically", "A stack"], "a"),
            ("Avg(Marks) is:", ["An aggregate", "A primary key", "A form control always", "A foreign key"], "a"),
            ("Sum is for:", ["Totals (fees, marks)", "Sorting names alphabetically", "Encryption", "Routing"], "a"),
            ("Min/Max in a totals query:", ["Smallest/largest in the group", "The table name", "The form wizard", "TCP ports"], "a"),
            ("You summarise when:", ["n is large and you need a picture of each group", "You have one row", "You draw NAND", "You write sprints"], "a"),
        ],
        [
            ("Name four aggregate functions.",
             "Count, Sum, Avg, Min, Max."),
            ("What must you set in Access Totals query?",
             "Group By on the category; Count/Avg on the measure."),
            ("Example: average marks per subject.",
             "Group by Subject; Avg(Marks)."),
            ("Why not list 2000 rows to the principal?",
             "A 5-row summary is decidable; a dump is not."),
        ],
        [
            ("From a Marks table, design two totals queries: (1) count of fails per class (2) average marks per subject. Show the Group By row.",
             "(1) Class Group By; Marks Count with criteria <40 or a Fail Yes/No Count. (2) Subject Group By; Marks Avg. Sample output."),
        ],
    )


def _access_chart(*_):
    return (
        [
            ("A column chart in Access is for:", ["Comparing categories", "Parts of a whole only", "Time only", "OSI only"], "a"),
            ("A pie chart shows:", ["Share of a total", "A trend of 60 months well", "Binary search", "Foreign keys"], "a"),
            ("A line chart shows:", ["Change over time", "Unrelated categories best", "ER diamonds", "NAND"], "a"),
            ("Charts should be based on:", ["A summarised query, not 10,000 raw rows if possible", "The relationship window", "Python turtle", "Figma"], "a"),
            ("Unlabelled axes in an exam chart score:", ["Near zero", "Full marks", "Bonus NAND", "An extra sprint"], "a"),
            ("Choose the chart that matches the question, same rule as:", ["Matplotlib in XII", "Bubble sort", "TCP handshake", "K-maps"], "a"),
        ],
        [
            ("When pie vs column?",
             "Pie: composition of one whole (few slices). Column: compare separate categories."),
            ("When line?",
             "Enrolment 2019–2026 — time."),
            ("Why chart a totals query not the raw table?",
             "The chart needs one number per category, not every student."),
            ("Three labels every chart needs.",
             "Title, axis titles / legend, units."),
        ],
        [
            ("For library data pick a chart: (a) books per genre (b) issues per month (c) share of lost vs on-shelf vs borrowed. Justify and sketch.",
             "(a) column (b) line (c) pie. Each sketch labelled. One sentence why the others are worse."),
        ],
    )


def _impacts_intro(*_):
    return (
        [
            ("Computing is now part of:", ["Daily life — phones, banks, schools", "Only museums", "Only NAND labs", "Only OSI textbooks"], "a"),
            ("An impact can be:", ["Positive or negative", "Only positive", "Only hardware heat", "Only Big O"], "a"),
            ("This unit’s three big technologies are:", ["AI, IoT, Data analytics", "Only bubble sort", "Only Access forms", "Only Figma"], "a"),
            ("A smart meter is closest to:", ["IoT", "A primary key", "A K-map", "A sprint"], "a"),
            ("Predicting fail risk from marks is:", ["Data analytics / AI", "Physical cabling", "A pie only", "Waterfall always"], "a"),
            ("Students must also learn:", ["Limits and ethics, not only hype", "That computers never fail", "That data is always true", "That IoT needs no internet"], "a"),
        ],
        [
            ("Give two daily computing uses in Pakistan.",
             "JazzCash/Easypaisa; NADRA records; online boards; WhatsApp classrooms — any two."),
            ("Why study impacts, not only coding?",
             "Technology changes jobs, privacy, inequality — exams ask both sides."),
            ("Name the three tools this chapter compares.",
             "AI, IoT, data analytics."),
            ("One negative impact.",
             "Job displacement, addiction, surveillance, e-waste."),
        ],
        [
            ("Write a balanced 10-mark intro: three benefits of computing in a Sindh college and three harms, with one mitigation each.",
             "Benefits: attendance systems, online notes, analytics of results. Harms: distraction, data leaks, unfair access. Mitigations: phone policy, passwords/backups, lab hours for students without devices."),
        ],
    )


def _ai(*_):
    return (
        [
            ("AI is:", ["Machines performing tasks that need human intelligence", "Any Excel sheet", "A copper cable", "A primary key"], "a"),
            ("Machine learning is AI that:", ["Learns patterns from data", "Only follows a fixed 5-line script forever", "Is analog only", "Is a pie chart"], "a"),
            ("A chatbot is an:", ["AI application", "OSI hub", "AND gate", "MVP canvas"], "a"),
            ("AI needs:", ["Data + model + compute", "Only a mouse", "Only paper", "Only Agile stickers"], "a"),
            ("An exam risk of AI answers is:", ["Hallucination / wrong confident text", "Too much NAND", "Too much OSI", "Too much bubble sort"], "a"),
            ("This is a ★ topic because papers ask:", ["Definition + examples + one issue", "Only cabling colours", "Only Access wizards", "Only Big O proofs"], "a"),
        ],
        [
            ("Define AI with two examples.",
             "Intelligence in machines. Face unlock; Google Translate; board-result chatbots."),
            ("AI vs ordinary software.",
             "Ordinary: fixed rules. AI: improves from data / handles messy input."),
            ("One benefit and one risk in exams/education.",
             "Benefit: tutoring. Risk: cheating / wrong answers."),
            ("Name two Pakistani/education uses.",
             "Urdu OCR; adaptive quizzes; NADRA biometrics (accept reasonable)."),
        ],
        [
            ("Explain AI to a Class XI student: definition, two components, two applications, two ethical issues. ★ Golden.",
             "Def. Data+algorithms(+sensors). Apps: health imaging, spam filter. Ethics: bias, privacy, job loss. One sentence on human remaining responsible."),
        ],
    )


def _iot(*_):
    return (
        [
            ("IoT is:", ["Physical devices on the internet sharing data", "Only desktop Word", "Only K-maps", "Only sprints"], "a"),
            ("A typical IoT chain is:", ["Sensor → connectivity → data → action", "Query → form → report only", "SYN → ACK only", "Bubble → selection"], "a"),
            ("Connectivity might be:", ["Wi-Fi, 4G, Bluetooth", "A primary key", "A pie chart", "A NAND-only bus"], "a"),
            ("An actuator:", ["Does something in the real world (motor, relay)", "Only stores SQL", "Only sorts", "Only prints Urdu"], "a"),
            ("Without connectivity, sensors:", ["Cannot send readings", "Become RDBMS", "Become AI models", "Become OSI layer 7"], "a"),
            ("A smart irrigation valve is IoT because:", ["It senses, sends, and acts remotely", "It is made of paper", "It runs bubble sort", "It is a form wizard"], "a"),
        ],
        [
            ("Define IoT.",
             "Internet of Things: physical objects with sensors/software that connect and exchange data."),
            ("List four components.",
             "Devices/sensors, connectivity, data processing, user interface / actuators."),
            ("Give a farm example.",
             "Soil moisture sensor → mobile network → app → pump on/off."),
            ("One security worry.",
             "Unpatched cameras on the internet; weak default passwords."),
        ],
        [
            ("Draw the IoT component diagram for a smart classroom (lights, attendance, AC). Label each component and one risk. ★ Golden.",
             "Sensors (PIR, RFID), Wi-Fi, college server/analytics, dashboard, relays for lights. Risk: student location privacy. Mitigation: local processing, access control."),
        ],
    )


def _analytics(*_):
    return (
        [
            ("Data analytics is:", ["Collect, clean, study, present data for decisions", "Only drawing NAND", "Only cabling", "Only Figma"], "a"),
            ("Cleaning data means:", ["Fixing missing/wrong values", "Washing the PC", "Defrag only", "Sorting OSI layers"], "a"),
            ("A dashboard is:", ["A visual summary of analytics", "A primary key", "A sprint log only", "A K-map"], "a"),
            ("Analytics without a question is:", ["Just a pile of charts", "Always AI", "Always IoT", "Always SQL keys"], "a"),
            ("Finding that “second shift fails more in CS” is:", ["Insight from analysis", "A foreign key", "A gate delay", "A beachhead"], "a"),
            ("Python’s later tool for this in XII is:", ["Pandas + charts", "LogiSim", "Figma only", "Access macros only"], "a"),
        ],
        [
            ("Define data analytics and list its steps.",
             "Collect → organise/clean → analyse → present → decide."),
            ("Why clean first?",
             "Garbage in, garbage out — mean of marks with blanks is wrong."),
            ("Give a college decision driven by analytics.",
             "Extra classes for a subject whose fail rate jumped."),
            ("How is analytics different from IoT?",
             "IoT gathers live device data; analytics is the studying/presenting (often of that data)."),
        ],
        [
            ("A principal has 3 years of BIEK results. Outline an analytics project: source, clean, one chart, one decision.",
             "Source: gazette CSVs. Clean: missing roll numbers. Chart: line of pass% by year. Decision: change lab hours if practical marks drag theory. Mention ethics (no public shaming of named students)."),
        ],
    )


def _compare_tech(*_):
    return (
        [
            ("IoT’s centre is:", ["Connected devices/sensors", "Learning models", "Statistics only", "Paper forms"], "a"),
            ("AI’s centre is:", ["Intelligent decisions from data", "Cables", "Tables of keys", "Sine waves"], "a"),
            ("Analytics’ centre is:", ["Finding patterns for humans to decide", "Motors", "TCP only", "NAND"], "a"),
            ("A camera + model that flags cheating is:", ["IoT (camera) + AI (model)", "Only a primary key", "Only waterfall", "Only a pie without data"], "a"),
            ("They often work:", ["Together in one system", "As enemies", "Only in 1990", "Only offline on paper"], "a"),
            ("Exam trick: define each in one line then:", ["One difference and one example that uses two of them", "Draw 7 OSI layers", "Write bubble sort", "List Access objects"], "a"),
        ],
        [
            ("One-line IoT vs AI vs analytics.",
             "IoT: things on the net. AI: machine intelligence. Analytics: study data to decide."),
            ("Shared need of all three.",
             "Data — without data none of them work well."),
            ("An example that uses all three.",
             "Smart hospital: IoT monitors, analytics dashboards, AI alerts for crisis."),
            ("A table heading you should memorise.",
             "Basis | IoT | AI | Analytics."),
        ],
        [
            ("Tabulate IoT vs AI vs analytics on: definition, core component, example, limitation. Then describe a Karachi traffic system using all three.",
             "IoT cameras/loops; analytics congestion charts; AI signal timing. Limitation: IoT privacy, AI bias, analytics bad data. 10-mark table + paragraph."),
        ],
    )


def _iot_uses(*_):
    return (
        [
            ("Smart cities use IoT for:", ["Traffic, waste, lighting", "Only K-maps", "Only sprints", "Only Access reports"], "a"),
            ("Health IoT example:", ["Remote heart-rate monitor", "Bubble sort", "Primary keys", "Figma frames"], "a"),
            ("Farms use IoT to:", ["Water when soil is dry", "Compile C", "Draw ER", "Write OSI"], "a"),
            ("Homes: a smart lock is IoT if:", ["It is on the network and reports/acts", "It is a mechanical padlock only", "It is a Python tuple", "It is a pie"], "a"),
            ("Education IoT:", ["RFID attendance, smart boards", "Only textbooks", "Only NAND labs", "Only waterfalls"], "a"),
            ("A risk in all these areas:", ["Privacy / hacked devices", "Too much paper", "Too few charts", "Too much Big O"], "a"),
        ],
        [
            ("Four application areas of IoT from the book.",
             "Cities, health, farms, homes, industry, education — any four."),
            ("One benefit in health.",
             "Doctors see vitals without the patient travelling."),
            ("One farm sensor + actuator pair.",
             "Moisture sensor + water pump."),
            ("Why security matters more as IoT grows.",
             "More doors into private spaces (cameras, locks)."),
        ],
        [
            ("Pick city, hospital, farm. For each: one device, one data item, one action, one risk.",
             "City: traffic cam / count / signal / surveillance. Hospital: SpO2 / alert nurse / false alarm. Farm: moisture / pump / overwater if sensor fails."),
        ],
    )


def _ai_edu(*_):
    return (
        [
            ("AI in Pakistani classrooms can:", ["Personalise practice, mark MCQs, translate", "Replace all teachers tomorrow by law", "Lay fibre", "Set primary keys"], "a"),
            ("A risk of AI homework tools is:", ["Students submit work they cannot explain", "Faster bubble sort", "Better NAND", "Longer OSI"], "a"),
            ("Adaptive learning means:", ["Difficulty changes with the student", "Everyone gets the same paper always", "No data is used", "Only analog TV"], "a"),
            ("Teachers still needed because:", ["Care, judgment, fairness, lab skill", "AI cannot use electricity", "Books are illegal", "BIEK forbids computers"], "a"),
            ("Data used by education AI must be:", ["Protected (student privacy)", "Posted publicly with names", "Sold always", "Ignored"], "a"),
            ("A realistic near-term use is:", ["Urdu/English support and drill quizzes", "Fully autonomous colleges", "Replacing SDLC", "Replacing ER diagrams"], "a"),
        ],
        [
            ("Two uses of AI in education in Pakistan.",
             "Language practice; auto-marking MCQs; plagiarism hints; accessibility readers."),
            ("Two limits.",
             "Bias, hallucinations, connectivity gaps, cheating."),
            ("What should a student still be able to do unaided?",
             "Explain the answer in the board paper without the chatbot."),
            ("One policy idea for a college.",
             "AI allowed for practice, banned in the exam hall; teach citation."),
        ],
        [
            ("Write a balanced note: opportunities of AI for BIEK CS students vs three rules a college should set.",
             "Opp: extra drills, Urdu help, code explainers. Rules: no AI in exams, no pasting private data into public bots, teacher reviews flagged work. Link to digital literacy."),
        ],
    )


def _sources(*_):
    return (
        [
            ("A primary source is:", ["Original, first-hand", "A summary of summaries", "Always Wikipedia", "A pie chart of rumours"], "a"),
            ("A secondary source is:", ["Someone else’s analysis of primary material", "Raw sensor logs only", "Always false", "A NAND gate"], "a"),
            ("A tertiary source is:", ["Highly summarised (encyclopaedia, textbook index)", "A lab notebook", "A witness interview", "A packet capture"], "a"),
            ("Your own class survey is:", ["Primary", "Tertiary", "Always secondary", "Not a source"], "a"),
            ("A newspaper report of that survey is:", ["Secondary", "Primary always", "Tertiary always", "IoT"], "a"),
            ("Board papers want you to:", ["Judge reliability, not just copy Google", "Use any blog", "Ignore dates", "Prefer unsigned forwards"], "a"),
        ],
        [
            ("Define the three source types with one example each.",
             "Primary: experiment, interview, sensor. Secondary: review article, textbook chapter discussing others. Tertiary: encyclopaedia, library catalogue."),
            ("Which is a BIEK past paper for you as a student?",
             "Primary evidence of the exam; or secondary if you only read a guide about it — say so."),
            ("One reliability test.",
             "Author, date, purpose, evidence, bias."),
            ("Why tertiary is still useful.",
             "Fast overview and pointers to better sources — not the final citation for a claim."),
        ],
        [
            ("For a project “screen time vs grades”, list two primary, two secondary, one tertiary source and how you would check each. ★ Golden.",
             "Primary: your survey, school lab logs. Secondary: a journalistic feature, a review paper. Tertiary: textbook definition of survey. Checks: sample size, date, conflict of interest."),
        ],
    )


def _impacts(*_):
    return (
        [
            ("Computing in health:", ["Records, imaging, telemedicine", "Only games", "Only NAND", "Only sprints"], "a"),
            ("Computing in education:", ["LMS, simulations, analytics", "Only chalk forever", "Only OSI layer 1", "Only keys"], "a"),
            ("A social harm is:", ["Addiction / fake news / job loss", "Faster search in a library", "Safer banks always only", "Shorter SDLC only"], "a"),
            ("E-waste is:", ["Discarded electronics", "A Python error", "A foreign key", "A histogram bin"], "a"),
            ("The exam pattern is:", ["One field + one good + one bad + one control", "Only definitions", "Only code", "Only careers"], "a"),
            ("Banks use computing for:", ["Accounts, ATMs, fraud analytics", "Growing wheat", "Drawing K-maps", "Sorting hats"], "a"),
        ],
        [
            ("Two fields and one impact each.",
             "Health: telemedicine. Transport: ride apps / signals. Banking: mobile wallets."),
            ("One environmental issue.",
             "E-waste, energy of data centres."),
            ("One social issue.",
             "Digital divide — students without smartphones."),
            ("One control/mitigation.",
             "Laws, privacy settings, recycling, lab access at college."),
        ],
        [
            ("“Computing has only benefits.” Refute with three fields, each with a benefit, a harm, and a mitigation. 10 marks.",
             "Health, education, media. Structure a table. Close: technology is a tool; policy and literacy decide the outcome."),
        ],
    )


def _assist(*_):
    return (
        [
            ("Assistive technology helps:", ["People with disabilities use systems", "Only hackers", "Only DBMS keys", "Only Agile coaches"], "a"),
            ("A screen reader is for:", ["Blind / low-vision users", "Faster bubble sort", "Wi-Fi", "Primary keys"], "a"),
            ("Captions help:", ["Deaf / hard-of-hearing users (and many others)", "Routers", "NAND gates", "Pie charts only"], "a"),
            ("Importance: they support:", ["Equal access to education and work", "Faster CPUs only", "Cheaper RAM only", "OSI layer 1 only"], "a"),
            ("A career path is:", ["Accessibility specialist / AT developer", "Only analog radio", "Only waterfalls", "Only K-maps"], "a"),
            ("Good HCI + AT means:", ["Design for a wide range of users from the start", "A separate broken version forever", "No keyboard needed ever", "No contrast ever"], "a"),
        ],
        [
            ("Define assistive technology with two examples.",
             "Devices/software that help functional limits: screen readers, switches, captions, magnification."),
            ("Why it matters in a Pakistani college.",
             "A blind student can still take CS if materials are readable by NVDA and papers have electronic copies."),
            ("Link to HCI accessibility principles.",
             "Perceivable, operable, understandable, robust — AT relies on those."),
            ("One career connection from the book.",
             "AT designer, accessibility tester, special-education technologist."),
        ],
        [
            ("Propose AT + ordinary design changes so a student with low vision and a student with limited hands can use the college portal. 10 marks. ★ if tagged Golden.",
             "Low vision: contrast, zoom, screen reader labels. Limited hands: large targets, keyboard/switch, extra time. Test with real users. Do not ship a mouse-only form."),
        ],
    )


def _dl(*_):
    return (
        [
            ("Digital literacy is:", ["Using digital tools safely and smartly", "Owning a phone only", "Typing 10 words", "Watching any video"], "a"),
            ("It includes:", ["Search, evaluate, create, behave ethically", "Only cabling", "Only NAND", "Only sprints"], "a"),
            ("A digitally literate student can:", ["Tell a reliable source from a forward", "Believe every screenshot", "Post passwords", "Skip citations"], "a"),
            ("Information age means:", ["Value of data/knowledge is huge", "Stone tools", "No networks", "No computers"], "a"),
            ("Safety in DL includes:", ["Passwords, privacy, respectful posts", "Sharing OTPs", "Unknown USBs always", "Public exam photos of others without consent"], "a"),
            ("This chapter later asks you to:", ["Collect and present data yourself", "Build CPUs", "Lay fibre", "Write OSI sniffers"], "a"),
        ],
        [
            ("Define digital literacy.",
             "Ability to find, evaluate, use, create and share digital information safely."),
            ("Three skills besides “knowing Word”.",
             "Search operators, source judging, privacy, creating a chart, citing."),
            ("One unsafe practice.",
             "Using the same password for email and JazzCash."),
            ("Why it is in a CS course, not only Islamiyat/civics.",
             "You produce and analyse data — you are responsible for it."),
        ],
        [
            ("A cousin forwards a “BIEK result leaked” screenshot. Using digital literacy, write the steps you take before sharing, and how you would present your finding.",
             "Check official site/date/URL, reverse-image, look for primary source. Do not share. Present as a short report: claim, checks, conclusion. Link to later inquiry project."),
        ],
    )


def _data_types(*_):
    return (
        [
            ("Qualitative data is:", ["Categories / words (favourite subject)", "Heights in cm only", "Always continuous numbers", "Always bits"], "a"),
            ("Quantitative data is:", ["Numeric measurements or counts", "Colours of bags only", "Always opinions", "Always URLs"], "a"),
            ("Favourite colour is:", ["Qualitative", "Quantitative continuous", "A primary key always", "A gate"], "a"),
            ("Height is:", ["Quantitative continuous", "Qualitative", "Boolean only", "Tertiary"], "a"),
            ("Number of siblings is:", ["Quantitative discrete", "Qualitative", "Analog voltage", "A query"], "a"),
            ("Why the type matters:", ["It decides the chart and statistic", "It decides OSI layer", "It decides NAND grouping", "It decides Agile sprint length"], "a"),
        ],
        [
            ("Define qualitative vs quantitative with examples.",
             "Qual: labels (blood group). Quant: numbers (marks)."),
            ("Discrete vs continuous quantitative.",
             "Discrete: counts (students). Continuous: measurements (time, temperature)."),
            ("Which chart for qualitative shares?",
             "Bar or pie (few categories)."),
            ("Which average for qualitative?",
             "Mode — mean of “red/blue” is meaningless."),
        ],
        [
            ("A survey has: gender, hours of study, favourite app, test marks. Classify each, pick a chart, and say mean/median/mode which is legal.",
             "Gender qual → pie/bar, mode. Hours quant cont → hist, mean/median. App qual → bar, mode. Marks quant → hist/box, mean/median. Table."),
        ],
    )


def _collect(*_):
    return (
        [
            ("Data-collection strategies include:", ["Interview, survey, prototype, observation, simulation", "Only NAND", "Only OSI ping", "Only K-maps"], "a"),
            ("You collect data when:", ["Existing sources are not enough", "You already have the full census always", "The question is undefined", "You only need a meme"], "a"),
            ("A strategy must match:", ["The question and the people", "The teacher’s favourite chart only", "Agile always", "TCP window"], "a"),
            ("Bias in collection:", ["Systematically distorts answers", "Improves SD always", "Is required in exams", "Is a primary key"], "a"),
            ("Ethics: people should:", ["Know and consent", "Be filmed secretly always", "Hand over passwords", "Be named in viral posts"], "a"),
            ("This is ★ because papers ask:", ["Name + when to use + one limit of a method", "Only Python turtles", "Only ER", "Only Big O"], "a"),
        ],
        [
            ("List five strategies from the book.",
             "Interview, survey, prototype, observation, simulation (and others in 6.4)."),
            ("One advantage of planning methods first.",
             "You do not collect the wrong type of data for your chart later."),
            ("One ethical rule.",
             "Informed consent; anonymise students."),
            ("What is a biased question?",
             "“Don’t you agree our canteen is terrible?” — pushes the answer."),
        ],
        [
            ("Choose methods for: (a) why students skip practicals (b) how a new ID-card prototype feels (c) traffic at the gate. Justify. ★ Golden.",
             "(a) interview+survey (b) prototype test (c) observation/count or simulation. Limits of each. Ethics sentence."),
        ],
    )


def _survey(*_):
    return (
        [
            ("An interview is:", ["A spoken Q&A, often fewer people, deeper", "A 500-person tick sheet always", "A NAND", "A pie"], "a"),
            ("A survey is:", ["The same questions to many people", "Always one celebrity chat", "A sort", "A cable"], "a"),
            ("Closed questions are easier to:", ["Count and chart", "Explore feelings", "Build CPUs", "Route IP"], "a"),
            ("Open questions are better for:", ["Reasons and quotes", "Instant averages", "Primary keys", "Gray codes"], "a"),
            ("A leading question is:", ["Biased", "Required", "A foreign key", "A sprint"], "a"),
            ("Sampling matters because:", ["Only asking prefects is not the whole college", "n always equals 1", "Charts ignore n", "Ethics forbid samples"], "a"),
        ],
        [
            ("Differentiate interview and survey.",
             "Interview: deep, slow, few. Survey: standardised, many, shallower."),
            ("Two question-writing rules.",
             "One idea per item; avoid leading; simple Urdu/English; pilot test."),
            ("When mix both?",
             "Survey for numbers, then interview to explain a surprising number."),
            ("What is a pilot?",
             "Try the form on 5 classmates and fix confusing items."),
        ],
        [
            ("Write 4 survey questions (2 closed, 2 open) on screen time, plus 3 interview prompts. Mark any bias you avoided.",
             "Closed: hours bands; devices. Open: why night use; effect on sleep. Interview: walk me through yesterday evening. No “don’t you think phones are evil”."),
        ],
    )


def _proto_obs(*_):
    return (
        [
            ("A prototype here is:", ["An early model to test an idea", "The final app store release", "A primary key", "A histogram"], "a"),
            ("Observation means:", ["Watching what people actually do", "Only asking them", "Only simulating", "Only Googling"], "a"),
            ("Simulation is:", ["A model of a system you can run", "A real flood in the campus", "A NAND chip", "A foreign key"], "a"),
            ("People say they wait 2 minutes but observation shows 10: trust:", ["Observation of that behaviour", "The boast", "Neither ever", "OSI"], "a"),
            ("Paper screens of an app are a:", ["Low-fidelity prototype", "MVP already selling", "Database schema", "Pie chart"], "a"),
            ("Simulations are useful when:", ["Real experiments are costly or unsafe", "You already have all answers", "n=1 always", "Ethics forbid models"], "a"),
        ],
        [
            ("Define prototype, observation, simulation in one line each.",
             "Prototype: early model. Observation: watch. Simulation: run a model."),
            ("One limit of observation.",
             "Hawthorne effect — people act differently when watched."),
            ("One limit of simulation.",
             "Wrong assumptions → pretty but false results."),
            ("When is a prototype better than a survey?",
             "When you need to see if a design is usable, not just popular in words."),
        ],
        [
            ("A team wants a quieter library. Combine prototype, observation and simulation in a plan with ethics.",
             "Observe noise sources; prototype signage/zones; simulate seating. Consent to watch; no filming faces for TikTok. What would change your mind (data)."),
        ],
    )


def _primary(*_):
    return (
        [
            ("Primary data is:", ["Collected by you for this question", "Copied from a textbook table always", "Always tertiary", "A NAND output"], "a"),
            ("Secondary data is:", ["Collected by others, reused", "Your interview today", "Always fake", "A pie only"], "a"),
            ("You control quality more with:", ["Primary", "Secondary always", "Tertiary always", "None"], "a"),
            ("Secondary is often:", ["Faster and cheaper", "Always more accurate", "Always ethical-free", "Always qualitative"], "a"),
            ("Census tables you download are:", ["Secondary for you", "Primary for you", "Not data", "A query object"], "a"),
            ("A common exam pair is:", ["Define both + one difference + one example each", "Only Big O", "Only ER", "Only Agile"], "a"),
        ],
        [
            ("Table: primary vs secondary on source, control, cost, example.",
             "You vs others; high vs low control; high vs low cost; survey vs PBS stats."),
            ("One risk of secondary.",
             "Out of date, different definitions, hidden bias."),
            ("One risk of primary.",
             "Small sample, poor questions, time."),
            ("Can a project use both?",
             "Yes — and the book’s inquiry project does."),
        ],
        [
            ("For “canteen waiting time”, list primary and secondary data you would gather, and how each could lie. ★ Golden.",
             "Primary: observe queues, survey. Secondary: last year’s complaint log, news on food inflation. Lies: observed only at 8am; old log incomplete. Triangulate."),
        ],
    )


def _approach(*_):
    return (
        [
            ("A data-collection approach is:", ["The planned mix of methods, sample, ethics, timeline", "A random Google", "A NAND", "A sprint demo only"], "a"),
            ("You start from:", ["The question / decision", "The prettiest chart", "The favourite library", "TCP"], "a"),
            ("Sample defines:", ["Who/what you measure", "The CPU model", "OSI layer 1", "Figma colours"], "a"),
            ("A timeline stops:", ["Endless collection with no analysis", "Ethics", "Backups", "Citations"], "a"),
            ("Ethics belong in the plan:", ["Before you collect", "After viral posting", "Never", "Only in XII entrepreneurship"], "a"),
            ("The output of the approach is:", ["A method you could hand to another student", "A secret", "A pie without numbers", "A career list"], "a"),
        ],
        [
            ("List the parts of a collection approach.",
             "Question, data type, methods, sample, tools, ethics, time, how you will present."),
            ("Why write it down?",
             "So the project is repeatable and examinable."),
            ("What if methods disagree?",
             "Say so — that is a result (triangulation)."),
            ("Link to 6.7 presenting.",
             "The approach must produce data the chosen charts can show."),
        ],
        [
            ("Write a one-page approach for “Does the second shift have worse CS practical marks?” Include sample, two methods, ethics, and a fallback if the office refuses data.",
             "Question; sample both shifts; primary: anonymised marks if allowed + survey on lab access; secondary: timetable. Ethics: no names on graphs. Fallback: observation of lab crowding + self-reported marks with bias warning."),
        ],
    )


def _present(*_):
    return (
        [
            ("Spreadsheets are good for:", ["Tables, calculations, simple charts", "3D games", "NAND simulation", "OSI sniffing"], "a"),
            ("A presentation (slides) is for:", ["Talking an audience through findings", "Storing the only copy of raw data", "Primary keys", "Kernel drivers"], "a"),
            ("An infographic is:", ["A visual one-pager of facts", "A 40-page appendix", "A binary search", "A foreign key"], "a"),
            ("A report is:", ["Structured writing with method, results, limits", "Only memes", "Only code", "Only ER"], "a"),
            ("Choose the tool by:", ["Audience and purpose", "Whatever is newest", "Always infographic", "Always 80 slides"], "a"),
            ("Raw 2000-row sheets in a 5-minute talk are:", ["A bad present", "Ideal", "Required by BIEK", "A sort algorithm"], "a"),
        ],
        [
            ("Four digital presentation tools in the book.",
             "Spreadsheets, slides, infographics, reports."),
            ("When spreadsheet > slides.",
             "When the audience must check the numbers or filter."),
            ("When infographic > report.",
             "Awareness poster / social post — not a methods thesis."),
            ("One rule for all four.",
             "Cite sources; label axes; do not crop axes to lie."),
        ],
        [
            ("Same finding (70% of surveyed students want longer labs). Design: a spreadsheet cell, a slide headline, an infographic hook, and a report paragraph.",
             "Sheet: table+bar. Slide: one number, one chart, one ask. Infographic: 7 of 10 icon row. Report: sample n, question wording, 70%, limit (one college)."),
        ],
    )


def _inquiry(*_):
    return (
        [
            ("The digital inquiry project applies:", ["All of chapter 6 in order", "Only careers", "Only NAND", "Only OSI"], "a"),
            ("Advanced search helps you:", ["Narrow secondary sources (quotes, site, date)", "Hack Wi-Fi", "Draw K-maps", "Sort in O(1)"], "a"),
            ("Primary collection in the project is often:", ["A class survey", "A CPU design", "A TCP stack", "A waterfall contract"], "a"),
            ("You organise results in a:", ["Spreadsheet + charts", "Random WhatsApp dump only", "NAND netlist", "Figma only"], "a"),
            ("The artefact is:", ["The final digital product that answers the question", "The first brainstorm sticky", "The career list", "The teacher’s attendance"], "a"),
            ("A conclusion should:", ["Answer the question and admit limits", "Ignore the data", "Name and shame students", "Invent n=1 million"], "a"),
        ],
        [
            ("List the project steps in order (grouped as in the book).",
             "Search/method; survey/primary; secondary+sheet; analyse/conclude; artefact."),
            ("What is a digital artefact here?",
             "Slides, infographic, short video, site — that answers the inquiry question."),
            ("Why include secondary if you surveyed?",
             "To compare your small sample with a published claim."),
            ("One sentence of a good limitation.",
             "n=40 in one college, so we cannot speak for all Sindh."),
        ],
        [
            ("Outline a 12-step inquiry: “Does extra screen time lower concentration in our class?” Name tools and the artefact. ★ Golden.",
             "Steps 1–3 search; 4–6 survey; 7–9 PBS/article + sheet; 10–12 charts, conclusion, artefact (infographic+spreadsheet). Ethics. One expected chart: hours vs self-reported focus."),
        ],
    )


def _hci(*_):
    return (
        [
            ("HCI studies:", ["How people and computers work together", "Only CPU clocks", "Only NAND", "Only SQL keys"], "a"),
            ("Another name mentioned is:", ["CHI / MMI", "MVP", "SDLC only", "K-map"], "a"),
            ("Sensory channels include:", ["Sight, touch, hearing, voice, spatial", "Only smell in this course", "Only taste", "Only OSI layer 7"], "a"),
            ("Good HCI makes systems:", ["Usable, efficient, fitting human needs", "Harder on purpose", "Mouse-only always", "Text in 4pt always"], "a"),
            ("Haptics are:", ["Touch feedback (vibration)", "Pie charts", "Foreign keys", "Sprints"], "a"),
            ("VR tracking is a:", ["Spatial channel", "Primary key", "Bubble sort", "Histogram"], "a"),
        ],
        [
            ("Define HCI.",
             "Human-Computer Interaction: design of technology around people."),
            ("Five sensory channels from the notes.",
             "Sight, touch, hearing, voice, spatial."),
            ("Give a computer response for touch and for voice.",
             "Touch: click/haptic. Voice: speech recognition and spoken reply."),
            ("Why HCI is not “just drawing a pretty screen”.",
             "It includes users, tasks, environment, feedback, accessibility."),
        ],
        [
            ("Tabulate the five channels with a human action and a computer response. Then explain one device that uses three channels at once.",
             "Smartphone: sight (GUI), touch (tap/haptic), hearing (ringtone), optional voice assistant. Closing: if one channel fails, another should still work (accessibility)."),
        ],
    )


def _hci_types(*_):
    return (
        [
            ("Traditional interaction uses:", ["Standard controls — keys, mouse, menus", "Gaze and gesture as the default 1980 PC", "Smell", "Telepathy"], "a"),
            ("Natural interaction tries to:", ["Use human skills (speech, gesture, touch) with less training", "Force people to learn command codes only", "Remove all feedback", "Use only punch cards"], "a"),
            ("A command-line is more:", ["Traditional / learned", "Natural baby-talk", "IoT soil", "A pie"], "a"),
            ("Pinch-to-zoom on a phone is more:", ["Natural (gesture)", "A foreign key", "A K-map", "Waterfall"], "a"),
            ("Both still need:", ["Feedback so the user knows the system heard them", "No UI", "No errors ever", "No accessibility"], "a"),
            ("Alexa-style speech is:", ["Natural-ish voice interaction", "A datasheet", "A histogram", "A stack pop"], "a"),
        ],
        [
            ("Define traditional vs natural interaction.",
             "Traditional: trained widgets (keyboard/mouse). Natural: speech, gesture, touch that feel like the real world."),
            ("One example each in a college.",
             "Traditional: SIS forms. Natural: fingerprint attendance, touch kiosk."),
            ("A drawback of “natural”.",
             "False gesture recognition; privacy of voice; not natural for every disability."),
            ("Can a product mix both?",
             "Yes — a phone has icons (traditional GUI) and gestures/voice."),
        ],
        [
            ("Design a library search: one traditional UI and one natural UI. Compare learnability, errors, and accessibility.",
             "Traditional: typed query + filters. Natural: speak the title / point at a shelf QR. Learnability vs noisy halls. Accessibility: keyboard vs voice. Recommend both."),
        ],
    )


def _hci_app(*_):
    return (
        [
            ("HCI applies to:", ["Desktops, web, mobile, kiosks, embedded, VR", "Only mainframes in 1970", "Only NAND trainers", "Only paper"], "a"),
            ("A hospital infusion pump UI is HCI in:", ["Health / safety-critical life", "Sports memes only", "Fashion only", "OSI cabling only"], "a"),
            ("Education HCI example:", ["LMS that students can actually submit homework on", "A random 4pt PDF", "An unlabelled form", "A hidden button"], "a"),
            ("Bad HCI in a bank app can:", ["Make people send money to the wrong account", "Speed bubble sort", "Fix NAND", "Change Big O of Python"], "a"),
            ("Domains of life in the book include:", ["Work, health, education, home, public services", "Only gaming", "Only compilers", "Only ER"], "a"),
            ("This is ★ because you must:", ["Name domains with a concrete interface each", "Draw K-maps", "Write SQL only", "List sprints"], "a"),
        ],
        [
            ("Five domains of HCI application.",
             "Work software, health devices, education, home/consumer, government/public kiosks, transport…"),
            ("Why HCI in medical devices is life-critical.",
             "A confusing unit (mg vs ml) can dose wrongly."),
            ("A public-service example in Pakistan.",
             "NADRA/passport kiosks, metro ticket machines."),
            ("What “application of HCI” means in a 3-mark.",
             "Not the definition — a place + the interface + why users matter."),
        ],
        [
            ("Pick four domains. For each: one system, one user, one HCI requirement. ★ Golden 10-mark.",
             "Clinic: nurse, glanceable alarms. College portal: student, language + mobile. ATM: elderly, privacy hood + large text. Car dash: driver, eyes-up. Table."),
        ],
    )


def _hci_comp(*_):
    return (
        [
            ("The user in HCI is:", ["The human with goals, limits, skills", "The CPU", "The database", "The sprint log"], "a"),
            ("The task is:", ["What the user is trying to get done", "The Wi-Fi password", "The NAND count", "The pie flavour"], "a"),
            ("The context/environment is:", ["Where/when/noise/light/stress", "Only RGB of the logo", "Only Big O", "Only SQL"], "a"),
            ("Missing any component in design causes:", ["HCI problems", "Faster CPUs", "Better keys", "Shorter OSI"], "a"),
            ("A tired nurse at night is part of:", ["User + environment", "Only the algorithm", "Only the DBMS", "Only Figma auto-layout"], "a"),
            ("Components work:", ["Together", "In isolation always", "Only in waterfall phase 6", "Only after MVPs ship"], "a"),
        ],
        [
            ("List the primary HCI components from the notes.",
             "User, task, interface, environment/context, feedback (and system)."),
            ("Give a college-lab example of each.",
             "User: XI student. Task: submit practical. UI: LMS upload. Env: noisy lab, short period. Feedback: “uploaded” tick."),
            ("What if you design only for an expert user?",
             "Beginners fail — a typical HCI problem."),
            ("Why environment?",
             "A UI that needs silence fails in a crowded canteen kiosk."),
        ],
        [
            ("Analyse JazzCash (or a similar app) using HCI components. Where might it fail for a first-time Urdu user in bright sunlight?",
             "User literacy/language; task send-money; UI contrast; outdoor glare; feedback of “success”. Recommend larger type, Urdu toggle, confirmation screen."),
        ],
    )


def _hci_ui(*_):
    return (
        [
            ("GUI means:", ["Graphical User Interface", "Great Universal Internet", "Gate Unary Inverter", "Grouped Unique Index"], "a"),
            ("CLI is:", ["Command-line (typed commands)", "Only touch", "Only VR", "Only pie menus of 1990 Mac always"], "a"),
            ("Voice UI example:", ["Siri / Alexa / Google Assistant", "A datasheet", "A K-map", "A foreign key"], "a"),
            ("Gesture UI example:", ["Swipe, pinch, Wii/Kinect-style move", "SQL SELECT", "Bubble swap", "HTTP GET only"], "a"),
            ("The best interaction type depends on:", ["User, task, environment", "Whatever is newest", "Always voice", "Always CLI"], "a"),
            ("A surgeon in a sterile field may prefer:", ["Voice/gesture over touch", "A dusty mouse", "Tiny 4pt CLI", "Captcha on the pump"], "a"),
        ],
        [
            ("Name four interaction types with examples.",
             "GUI desktop; CLI terminal; touch; voice; gesture; AR/VR — any four."),
            ("One strength of CLI.",
             "Fast and scriptable for experts."),
            ("One weakness of voice.",
             "Noise, privacy, accents, no visual scan of options."),
            ("Can one app offer two types?",
             "Yes — VS Code GUI + terminal; phones GUI + voice."),
        ],
        [
            ("Recommend an interaction type for: (a) programmer (b) ATM (c) car while driving (d) museum kiosk. Justify with user+environment.",
             "(a) GUI+CLI (b) GUI+keys, privacy (c) voice/steering-wheel, eyes up (d) large touch, language choice. Table."),
        ],
    )


def _hci_fb(*_):
    return (
        [
            ("Feedback is:", ["The system telling the user what happened", "A student evaluation form only", "A foreign key", "A sprint retrospective only"], "a"),
            ("A spinner/progress bar is:", ["Feedback that work is ongoing", "A primary key", "A sort", "A NAND"], "a"),
            ("No feedback after Save causes:", ["Double clicks / lost trust", "Faster CPUs", "Better Big O", "Shorter OSI"], "a"),
            ("The environment includes:", ["Noise, light, device, social setting", "Only CSS colours", "Only RAM", "Only Agile"], "a"),
            ("A GUI button should look:", ["Clickable (affordance) and then respond", "Like body text", "Invisible", "Like a pie"], "a"),
            ("Error messages should:", ["Say what went wrong and what to do", "Say ERROR 0xUnknown only", "Be in 4pt grey", "Vanish in 0.1s"], "a"),
        ],
        [
            ("Define interface and feedback.",
             "UI: the medium of interaction. Feedback: system response the user can sense."),
            ("Three feedback channels.",
             "Visual (message), audio (beep), haptic (vibrate)."),
            ("Example of poor environment–UI fit.",
             "Voice-only help in a noisy canteen; tiny text on a sunny ticket machine."),
            ("What is an affordance?",
             "The look that suggests how to use a control (a button looks pressable)."),
        ],
        [
            ("Audit the college portal login: environment, UI type, three feedback events (success, fail, loading). Rewrite one bad message.",
             "Lab noise/shared PCs. GUI form. Success: “Welcome Ali”. Fail: “Wrong password — try again or reset”. Loading: spinner. Bad: “Error 500” → “Server busy, wait 1 min or see the lab attendant”."),
        ],
    )


def _hci_imp(*_):
    return (
        [
            ("HCI matters because:", ["It turns complex machines into usable tools", "It makes CPUs clock faster by magic", "It replaces maths", "It deletes ethics"], "a"),
            ("Usability includes:", ["Effectiveness, efficiency, satisfaction", "Only colour", "Only NAND count", "Only price"], "a"),
            ("Poor HCI costs:", ["Errors, time, accidents, abandoned products", "Nothing", "Only printer ink", "Only font licences"], "a"),
            ("Good HCI can:", ["Widen who can use the system (accessibility)", "Reduce RAM physically", "Change OSI to 2 layers", "Remove the need for passwords always"], "a"),
            ("This is ★: expect a question:", ["Why HCI is important — 3–5 points with examples", "Trace a K-map", "Write bubble sort", "Normalise to 5NF"], "a"),
            ("A usable result portal:", ["Students find the mark without a tutorial", "Hides the mark in 12 menus", "Uses 4pt text", "Needs a CS degree"], "a"),
        ],
        [
            ("Three reasons HCI is important.",
             "Fewer errors; faster tasks; more users included; safer devices; product success."),
            ("Link to a Pakistani e-service.",
             "If the tax/passport site is confusing, people pay agents — HCI failure with social cost."),
            ("HCI vs pretty graphics.",
             "A pretty unusable app still fails; a plain clear form can succeed."),
            ("One safety example.",
             "Car dashboards / medical pumps — confusion harms people."),
        ],
        [
            ("Write a 10-mark essay: importance of HCI with five points, each with a local example. ★ Golden.",
             "Learnability (first-year portal); efficiency (JazzCash); safety (clinic software); accessibility (screen reader); business (app store ratings). Short intro/conclusion."),
        ],
    )


def _a11y(*_):
    return (
        [
            ("Accessibility means:", ["People with diverse abilities can use the system", "Only experts can use it", "Colourful GIFs always", "Mouse-only"], "a"),
            ("A principle is providing:", ["Multiple ways to see/operate (text, caption, keyboard)", "Captcha of 12 steps", "4pt grey on grey", "Auto-playing sound only"], "a"),
            ("Keyboard access helps:", ["Motor impairment and power users", "Nobody", "Only AI models", "Only IoT soil"], "a"),
            ("Contrast helps:", ["Low vision", "Faster bubble sort", "TCP window", "Primary keys"], "a"),
            ("Captions help:", ["Deaf users and noisy labs", "Routers", "NAND", "K-maps"], "a"),
            ("Accessibility is part of:", ["HCI quality, not an optional sticker", "Only marketing", "Only XII entrepreneurship", "Only physical cabling"], "a"),
        ],
        [
            ("Define accessibility in HCI.",
             "Design so people with disabilities (and many others) can perceive, operate and understand the UI."),
            ("Four practical techniques.",
             "Alt text, captions, keyboard, contrast, resizable text, Urdu/English toggle."),
            ("Who else benefits besides disabled users?",
             "Broken arm, noisy room, bright sun, second-language users."),
            ("Link to assistive tech in XI.",
             "Screen readers need labelled buttons — that is an HCI job."),
        ],
        [
            ("Audit a video lecture page against accessibility: list 6 fixes. Include one for vision, hearing, motor, language.",
             "Transcript+captions; contrast; pause; keyboard; alt on diagrams; Urdu summary. Do not autoplay. Test with Tab and a screen reader."),
        ],
    )


def _need(*_):
    return (
        [
            ("Need analysis finds:", ["The gap between now and the desired UI outcome", "The CPU benchmark", "The NAND delay", "The sprint velocity only"], "a"),
            ("You study:", ["Users, tasks, pain points, constraints", "Only colours you like", "Only competitors’ logos", "Only Big O"], "a"),
            ("A persona is:", ["A realistic portrait of a user type", "A primary key", "A pie chart", "A gate"], "a"),
            ("Skipping need analysis causes:", ["Pretty UIs that solve the wrong problem", "Correct Big O automatically", "Free RAM", "Shorter OSI"], "a"),
            ("Constraints include:", ["Time, devices, literacy, connectivity", "Only Figma seats", "Only NAND trainers", "Only exam memes"], "a"),
            ("Output of need analysis is:", ["Requirements for the interface", "A compiled kernel", "A K-map", "A histogram of NAND"], "a"),
        ],
        [
            ("Define need analysis in HCI.",
             "Identify the gap between the current situation and what users need the interface to do."),
            ("Three techniques.",
             "Interview, observe, survey, task analysis, look at old system logs."),
            ("Give a college example.",
             "Students miss fee deadlines → need SMS reminders + a 3-step mobile payment UI."),
            ("What is a constraint here?",
             "Many students on low-end Androids and 2G — no huge animations."),
        ],
        [
            ("Do a mini need analysis for a hostel complaint app: users, top 3 tasks, environment, constraints, 5 requirements.",
             "Users: residents, warden. Tasks: report, track, urgent leak. Env: phone on the stairs. Constraints: Urdu, photos, weak wifi. Req: offline draft, photo, status, privacy, large buttons."),
        ],
    )


def _hci_prob(*_):
    return (
        [
            ("HCI problems are:", ["Obstacles that stop smooth use", "CPU overheating only", "SQL deadlocks only", "Cable cuts only"], "a"),
            ("Inconsistency is:", ["The same action looking different in two screens", "A good pattern", "A primary key", "A sprint"], "a"),
            ("Poor feedback is:", ["The system stays silent after an action", "A progress bar", "A confirmation", "A beep plus message"], "a"),
            ("Contextual neglect is:", ["Ignoring where/who the user is", "Studying the environment well", "Need analysis", "Accessibility"], "a"),
            ("Overload is:", ["Too many options/messages at once", "A simple 3-button kiosk", "A labelled form", "A caption"], "a"),
            ("This is ★: answers should:", ["Name the problem, example, and a fix", "Only define HCI", "Only draw OSI", "Only write Python"], "a"),
        ],
        [
            ("Name four HCI problems from the notes.",
             "Inconsistency, poor feedback, overload, jargon, hidden features, contextual neglect, accessibility failure — any four."),
            ("Example of jargon.",
             "“Abort transaction / errno 2” on a student fee screen."),
            ("Example of inconsistency.",
             "Save is a disk icon on one page and a text “Commit” on the next."),
            ("A fix pattern.",
             "Name the problem, show the user impact, give a redesign."),
        ],
        [
            ("A college app has tiny grey errors, different logout buttons, and 40 items on the home grid. Identify three HCI problems and redesign the home in a wireframe description. ★ Golden.",
             "Feedback, inconsistency, overload. Home: 4–6 tasks (attendance, LMS, fees, results). Errors in Urdu/English, high contrast. One logout top-right always."),
        ],
    )


def _hci_fix(*_):
    return (
        [
            ("Improving HCI often starts with:", ["Watching real users (usability test)", "Adding more clipart", "Reducing contrast", "Hiding labels"], "a"),
            ("Consistency means:", ["Same words/icons/positions for the same action", "A new metaphor every page", "Random colours", "Surprise menus"], "a"),
            ("Simple IA (information architecture) means:", ["Fewer, clearer paths to tasks", "Deeper 12-level menus", "All links in a PDF dump", "No search"], "a"),
            ("Prototypes help you:", ["Fix HCI cheaply before code", "Skip users", "Skip accessibility", "Skip feedback"], "a"),
            ("Training is a fix when:", ["The task is rare/complex — but do not use it to excuse a bad UI", "The button is invisible", "Contrast is 1:1", "Errors are in hex only"], "a"),
            ("Iterative improvement is:", ["Test → change → test again", "Ship once never look", "Waterfall with no users", "Only career slides"], "a"),
        ],
        [
            ("Five methods to improve HCI.",
             "Simplify, consistent patterns, better feedback, accessibility, user tests, prototypes, reduce steps."),
            ("Why test with real students not only the developer?",
             "Developers know the map; users get lost."),
            ("A quick win for a form.",
             "Show required fields, inline errors, remember the class dropdown."),
            ("What is a heuristic evaluation?",
             "An expert checks the UI against rules (consistency, feedback…) before/besides user tests."),
        ],
        [
            ("Take a 7-step fee-payment UI. Cut it to 3 steps, list the HCI problems you removed, and how you would re-test.",
             "Steps: amount → confirm → OTP. Removed: extra account-type screens, jargon, no progress. Re-test: 5 students timed, errors counted, one interview."),
        ],
    )


def _uiux(*_):
    return (
        [
            ("UI is:", ["The look and interactive controls", "The whole research journey only", "The database schema", "The sprint velocity"], "a"),
            ("UX is:", ["The overall experience (useful, usable, satisfying)", "Only the colour palette", "Only the logo", "Only the NAND count"], "a"),
            ("You can have pretty UI and bad UX when:", ["The task still takes 20 confusing steps", "Buttons are clear and short", "Feedback is excellent", "Accessibility is strong"], "a"),
            ("UX research includes:", ["Interviews, tests, personas", "Only picking hex colours", "Only SQL", "Only OSI"], "a"),
            ("This is ★: define both, then:", ["Give a product example of each going wrong", "Draw a K-map", "Write a sort", "List Access objects"], "a"),
            ("A progress tracker in a 3-step form is mainly:", ["UX (and a bit of UI)", "A foreign key", "A histogram", "A gate"], "a"),
        ],
        [
            ("Define UI vs UX.",
             "UI: visual/interactive layer. UX: how the whole journey feels and whether the goal is achieved easily."),
            ("Who typically does each job.",
             "UI designer: screens/components. UX: research, flows, prototypes, testing. They overlap."),
            ("Example: ATM.",
             "UI: button layout. UX: whether you felt safe and finished withdrawal quickly."),
            ("Why both matter in exams.",
             "Papers ask the difference plus one example — do not mix the letters."),
        ],
        [
            ("A food-delivery app is gorgeous but checkout fails twice. Analyse UI vs UX, then list 4 UX fixes that may not need new colours. ★ Golden.",
             "UI may be fine. UX: errors, extra steps, unclear fees. Fixes: guest checkout, saved address, fee shown early, retry without losing the cart, better messages."),
        ],
    )


def _wire(*_):
    return (
        [
            ("A wireframe is:", ["A low-detail blueprint of screens", "The final branded mock", "A running MVP", "A database dump"], "a"),
            ("Figma is:", ["A collaborative UI/prototype tool in the browser", "A DBMS", "An OSI sniffer", "A sort"], "a"),
            ("A prototype here is:", ["A clickable model of the UI", "The production server", "A primary key", "A pie"], "a"),
            ("You wireframe:", ["Before polishing pixels", "After launch only", "Instead of need analysis", "Instead of testing ever"], "a"),
            ("Low fidelity means:", ["Boxes and labels, not final art", "Photoreal 3D", "Compiled ARM", "Encrypted SQL"], "a"),
            ("Figma is taught because the book uses it to:", ["Design and share UI without installing heavy tools", "Replace Python", "Replace ER", "Replace SDLC"], "a"),
        ],
        [
            ("Define wireframe and prototype.",
             "Wireframe: structure/layout. Prototype: interactive simulation of the UI."),
            ("Why Figma (from the notes)?",
             "Free, web-based, collaborative, good for class."),
            ("Order: need analysis → wireframe → prototype → test.",
             "Do not skip to colour before structure."),
            ("What belongs on a wireframe?",
             "Boxes, headings, buttons, notes — not lorem-pretty photos."),
        ],
        [
            ("Describe three Figma wireframe frames for college attendance: login, mark, confirm. List what you would test with five students.",
             "Frame contents; tap targets; Urdu. Test: time to mark, errors, could they undo. Change the prototype, not the database first."),
        ],
    )


def _eval_hci(*_):
    return (
        [
            ("Testing asks:", ["Does it work / any bugs?", "Is the logo pretty only", "What is Big O", "What is a FK"], "a"),
            ("Evaluation asks:", ["Does it meet user needs / usability goals?", "Only CPU temp", "Only compile errors", "Only SQL syntax"], "a"),
            ("You need both because:", ["A bug-free UI can still be unusable", "Bugs never matter", "Users never matter", "HCI is only art"], "a"),
            ("A usability goal example:", ["First-time student pays fees in < 3 minutes", "More colours", "More menus", "More jargon"], "a"),
            ("Evaluation can be:", ["With users or with experts/heuristics", "Only with the CEO’s nephew", "Only after 5 years", "Only in assembly"], "a"),
            ("Do this:", ["After a prototype, not only after full code", "Never", "Only on paper NAND", "Only on OSI diagrams"], "a"),
        ],
        [
            ("Differentiate testing and evaluation in HCI.",
             "Testing: system behaviour/bugs. Evaluation: human fit/usability/need."),
            ("Give a metric for each.",
             "Test: crash rate. Eval: task success, time, SUS satisfaction, error types."),
            ("When is expert review useful?",
             "Early, cheap, catches obvious heuristic breaks before booking users."),
            ("Why include real students?",
             "They hold the real tasks and language."),
        ],
        [
            ("Plan an evaluation of the LMS assignment-upload: 2 test cases (bugs) and 2 evaluation questions (usability) with measures.",
             "Test: 20MB PDF; no network. Eval: can a new student succeed unaided; time; satisfaction 1–5. n=8. What you would change if time > 5 min."),
        ],
    )


def _test_hci(*_):
    return (
        [
            ("Usability testing is:", ["Watching people do real tasks", "Only pinging servers", "Only unit tests of Python", "Only load tests of CPUs"], "a"),
            ("A/B testing compares:", ["Two versions on similar users", "NAND vs NOR only", "Mean vs mode only", "TCP vs UDP only"], "a"),
            ("Automated UI tests are good for:", ["Regressions of known flows", "Discovering new user feelings", "Replacing all interviews", "Measuring joy perfectly"], "a"),
            ("Think-aloud means:", ["Users speak while they try the task", "The computer reads NAND", "SQL dumps", "Sprinters shout"], "a"),
            ("A/B needs:", ["A clear metric (clicks, success)", "Random colours with no goal", "n=1", "No ethics"], "a"),
            ("This is ★: name the method, when to use it, one limit.",
             ["Yes — that is the 5-mark recipe", "No — only definitions", "No — write code", "No — draw OSI"], "a"),
        ],
        [
            ("Define usability testing, A/B, automated testing.",
             "Usability: observe tasks. A/B: two live variants. Automated: scripts click through."),
            ("One limit of each.",
             "Usability: small n, lab effect. A/B: needs traffic, can harm half the users. Auto: misses confusion that does not throw errors."),
            ("When A/B is overkill in XI/XII class.",
             "Five classmates on a Figma prototype is enough — no live traffic."),
            ("What do you record in a usability test?",
             "Task, success, time, errors, quotes, where they hesitated."),
        ],
        [
            ("Design a usability test + a tiny A/B for a “download slip” button (blue text vs big labelled button). Tasks, n, metric, ethics. ★ Golden.",
             "Task: get the slip. n=10 (5+5). Metric: success and time. Ethics: consent, no marks attached. Predict big button wins. Also one automated check that the link still works."),
        ],
    )


def _correct(*_):
    return (
        [
            ("An algorithm is correct if:", ["Outputs match the spec for the intended inputs (incl. edges)", "It is short", "It uses XOR", "It prints Hello"], "a"),
            ("A failed edge case means:", ["Not fully correct", "Still correct enough always", "Faster Big O", "Better UX"], "a"),
            ("You demonstrate correctness in this chapter with:", ["Trace tables / stepwise reasoning / tests", "Only careers", "Only Figma", "Only pie charts"], "a"),
            ("A spec is:", ["The expected behaviour", "The CPU model", "The font", "The sprint name"], "a"),
            ("Partial correctness often means:", ["IF it halts, the answer is right — you still need termination", "It never needs to halt", "It is Agile", "It is a GUI"], "a"),
            ("Off-by-one in a loop is a:", ["Correctness bug", "OSI issue", "NAND issue", "Career issue"], "a"),
        ],
        [
            ("Define correctness.",
             "For every specified input, the algorithm produces the specified output and finishes."),
            ("Two ways it can fail.",
             "Wrong answer; infinite loop (does not finish)."),
            ("Why test edges.",
             "Empty, one element, already sorted, not found, max int."),
            ("Link to later trace tables.",
             "A dry run is a manual proof for a small case."),
        ],
        [
            ("Give a “find maximum” algorithm, two traces (normal and n=1), and an incorrect version that fails on negatives. Explain.",
             "Init max to first element not 0. Trace [3,-1,5] and [−4]. Bug: init 0 fails all-negative lists. That is correctness, not Big O."),
        ],
    )


def _trace(*_):
    return (
        [
            ("A trace table is:", ["A dry-run grid of variables vs steps", "A database table", "A pie", "A Figma frame"], "a"),
            ("Stepwise reasoning checks:", ["The state at logical sections, not every micro-step", "Only Big O", "Only colours", "Only SQL"], "a"),
            ("Use a trace table when:", ["Few variables, you must not miss an assignment", "The algorithm is a huge system diagram only", "You need UX quotes", "You need a histogram"], "a"),
            ("Use stepwise when:", ["The logic is chunky (phases) rather than many tiny vars", "n=2 and 8 columns of i", "You sort visually", "You draw OSI"], "a"),
            ("Both methods aim at:", ["Correctness", "Careers", "Fonts", "TCP windows"], "a"),
            ("A soldier-eligibility trace would track:", ["Each input and the count so far", "CSS padding", "NAND groups", "Sprint points"], "a"),
        ],
        [
            ("Define trace table vs stepwise reasoning.",
             "Trace: column per variable, row per step. Stepwise: argue each phase’s post-condition."),
            ("When each is better (book comparison).",
             "Trace: loops with a few vars. Stepwise: long algorithms with clear sections."),
            ("What must every trace column include?",
             "Changing variables and the output/decision."),
            ("A common student error.",
             "Updating i in the table but forgetting the accumulator."),
        ],
        [
            ("Build a full trace table for: count how many of 3 heights are ≥ 5.5. Then write three stepwise sentences. ★ Golden.",
             "Columns: i, height, count. Rows for each soldier. Stepwise: init 0; for each, if tall count++; after loop count is the answer. Compare the two explanations."),
        ],
    )


def _clarity(*_):
    return (
        [
            ("Clarity means the algorithm is:", ["Easy to read, understand, change", "As short as possible even if cryptic", "Written in one letter variables only", "Uncommented hex"], "a"),
            ("Modularity helps clarity because:", ["Named pieces have one job", "Everything is in main", "There are no names", "Gotos everywhere"], "a"),
            ("Readability includes:", ["Names, structure, comments, consistent style", "Removing all spaces", "1-letter names always", "No line breaks"], "a"),
            ("A 200-line monoblock is:", ["Low modularity", "High modularity", "A primary key", "A pie"], "a"),
            ("Clarity can matter more than a tiny speed gain when:", ["Humans must maintain the code", "n=10^12 always", "It is a one-off NAND", "It is OSI layer 1"], "a"),
            ("Poor names are a:", ["Readability problem", "TCP problem", "Power problem", "RAM manufacturing problem"], "a"),
        ],
        [
            ("Define clarity of an algorithm.",
             "A person can see the purpose and logic without running it."),
            ("Two ways to improve it.",
             "Decompose into modules; meaningful names; comments on why; consistent structure."),
            ("Can a correct algorithm be unclear?",
             "Yes — and then it will be modified wrongly."),
            ("Link to functions in Ch 3.",
             "Functions are modularity in Python."),
        ],
        [
            ("Rewrite a messy “average of array” monoblock as three modules (input, compute, output). Explain the clarity gain.",
             "Show before/after pseudocode. Each module tested. Names: sum_list, mean. Comments why n=0 is rejected."),
        ],
    )


def _modular(*_):
    return (
        [
            ("Modularity is:", ["Splitting into independent pieces with clear interfaces", "One file of 2000 mixed lines", "Random copy-paste", "A chart type"], "a"),
            ("A module should have:", ["One job", "Every job", "No name", "No inputs"], "a"),
            ("Readability is:", ["How easily another person understands the algorithm", "Font size of the PDF only", "RAM size", "Cable length"], "a"),
            ("Reusing a module is easier if:", ["It does not depend on hidden globals", "It prints inside and uses global n", "It is unnamed", "It mixes I/O and maths"], "a"),
            ("Comments should explain:", ["Why, not every obvious i=i+1", "Nothing", "Only your WhatsApp", "Only Big O symbols"], "a"),
            ("Poor readability increases:", ["Bugs when changing code", "CPU GHz", "OSI layers", "Pie slices"], "a"),
        ],
        [
            ("Define modularity and readability.",
             "Modularity: parts. Readability: understandable text/structure."),
            ("One benefit of each.",
             "Modularity: test/reuse. Readability: fewer maintenance bugs."),
            ("A readable name vs a bad one.",
             "total_marks vs x1."),
            ("How they interact.",
             "Small named modules are easier to read."),
        ],
        [
            ("Take a messy attendance script (globals, 1-letter names). Produce a modular readable version and a 5-point rubric a teacher could mark.",
             "Modules: load, mark, save, report. Rubric: names, functions, no magic numbers, comments why, handles empty file."),
        ],
    )


def _eff(*_):
    return (
        [
            ("Efficiency is mainly:", ["Time and extra memory vs n", "How pretty the UI is", "How many comments", "Font choice"], "a"),
            ("As n grows, we care about:", ["Growth class (Big O), not a 2 ms blip", "Only the constant 2 ms", "Only variable names", "Only colours"], "a"),
            ("Space efficiency is:", ["Extra RAM/disk beyond the input", "Screen size", "PDF margins", "Cable thickness"], "a"),
            ("An algorithm can be:", ["Correct but inefficient", "Efficient but never correct and still useful always", "A pie", "A sprint"], "a"),
            ("This chapter’s framework later uses:", ["Steps, conditions, repetitions", "Only UX", "Only ER", "Only Figma"], "a"),
            ("Why efficiency is ★:", ["Board likes compare-two-algorithms questions", "It replaces correctness", "It replaces HCI", "It replaces Python"], "a"),
        ],
        [
            ("Define time and space efficiency.",
             "Time: how running time grows with input. Space: extra memory."),
            ("Why not measure only one run on your PC?",
             "Machines differ; we need growth vs n."),
            ("Example of wasting space.",
             "Copying a huge list on every recursive call."),
            ("Example of wasting time.",
             "Linear search 1 million times on a static sorted list instead of binary/index."),
        ],
        [
            ("Compare linear vs binary search on n=2, n=1 000 000 for time and space. State preconditions. 10-mark table.",
             "Time ~n vs ~log n. Space O(1) both (iterative). Binary needs sorted. For n=1e6, ~1e6 vs ~20 comparisons. Correctness not sacrificed."),
        ],
    )


def _bigo(*_):
    return (
        [
            (r"\(O(1)\) means:", ["Constant time, independent of n", "Linear in n", "Quadratic", "Factorial"], "a"),
            (r"\(O(n)\) example:", ["Linear search", "Binary search", "Nested n×n always", "Hash O(1) best always guaranteed"], "a"),
            (r"\(O(\log n)\) example:", ["Binary search", "Bubble sort", "Reading all n items once", "Nested loops n²"], "a"),
            (r"\(O(n^2)\) example:", ["Bubble / selection sort", "Binary search", "Closed formula sum", "Array index"], "a"),
            ("We drop constants and small terms because:", ["Growth class dominates for large n", "They are always 0", "Big O is UX", "Boards forbid numbers"], "a"),
            ("log n grows:", ["Slowly", "Faster than n²", "Faster than n!", "As a straight 45° line always"], "a"),
        ],
        [
            ("Define Big O in one student sentence.",
             "An upper-class of how time (or space) grows as n gets large."),
            ("Order these from fast to slow: n², 1, log n, n.",
             "O(1), O(log n), O(n), O(n²)."),
            ("Why is 3n+5 still O(n)?",
             "Constants ignored; linear term dominates."),
            ("What does O(log n) look like on a phone contacts list?",
             "Each step halves the remaining names."),
        ],
        [
            ("For each: array index, binary search, linear search, bubble sort — state Big O and a 1-line why. Then pick one for n=50 vs n=5 million. ★ Golden.",
             "O(1), O(log n), O(n), O(n²). n=50 anything fine; n=5e6 avoid n², prefer log/linear as appropriate. Mention sort cost if you need binary."),
        ],
    )


def _conds(*_):
    return (
        [
            ("Number of conditions affects:", ["How many decisions (and often branches) you pay for", "Only the font", "Only RAM manufacturing", "Only UX colour"], "a"),
            ("A nested if inside a loop can make work:", ["Depend on data (sometimes skip inner work)", "Always n²", "Always O(1)", "Always crash"], "a"),
            ("Short-circuit and/or can:", ["Skip later tests", "Sort the array", "Open a file", "Draw a pie"], "a"),
            ("Too many rare special cases:", ["Hurt clarity and can hurt time if mis-ordered", "Always reduce Big O class", "Always increase RAM", "Always fix UX"], "a"),
            ("Binary search’s conditions:", ["Few, but they cut n in half — very efficient", "n²", "Are UX heuristics", "Are SQL joins"], "a"),
            ("Counting conditions is part of the:", ["Efficiency evaluation framework", "HCI Nielsen list only", "ER cardinality only", "MVP canvas only"], "a"),
        ],
        [
            ("What is a “condition” in this chapter’s sense?",
             "A true/false test the algorithm performs (if, loop test, while)."),
            ("How can conditions save time?",
             "Early exit: if found, break; if x<0, skip expensive work."),
            ("How can they waste time?",
             "Re-testing the same expensive predicate; poorly ordered or/and."),
            ("Link to readability.",
             "A tower of nested ifs is slow to understand even if O(n)."),
        ],
        [
            ("Two versions of search: (A) no break (B) break when found. Compare conditions, time, traces on a hit at position 2 of 10.",
             "A always 10 tests. B 2 tests. Same Big O class worst-case still O(n), but average better. Show trace tables."),
        ],
    )


def _reps(*_):
    return (
        [
            ("Repetitions (loops) usually dominate:", ["Running time", "Font size", "Cable length", "Pie colours"], "a"),
            ("One loop over n is typically:", [r"\(O(n)\)", r"\(O(1)\)", r"\(O(n^2)\) always", r"\(O(n!)\)"], "a"),
            ("Nested loops i,j = 1..n are typically:", [r"\(O(n^2)\)", r"\(O(n)\)", r"\(O(\log n)\)", r"\(O(1)\)"], "a"),
            ("A loop that halves n each time is:", [r"\(O(\log n)\)", r"\(O(n^2)\)", r"\(O(n!)\)", r"\(O(n^3)\)"], "a"),
            ("Infinite loop is:", ["A correctness + time failure", "O(1)", "Good UX", "A foreign key"], "a"),
            ("To improve efficiency, first look at:", ["The innermost loop", "The comments", "The logo", "The folder name"], "a"),
        ],
        [
            ("Why loops matter most for efficiency.",
             "Work inside is multiplied by how often it runs."),
            ("How to count nested for i in n, for j in n.",
             "n×n = n² iterations."),
            ("An inner loop to n/2 still:",
             "Θ(n²) if outer is n (constants drop)."),
            ("Give a loop you can remove.",
             "Computing the same sum of a static list inside another loop — precompute."),
        ],
        [
            ("Rewrite a naive pair of nested loops that re-sum a prefix each time into an O(n) running total. Show both counts for n=4.",
             "Naive ~ n²/2 additions. Running total n additions. Tiny table of prefix sums. State both Big O."),
        ],
    )


def _eff_fw(*_):
    return (
        [
            ("The framework looks at:", ["Steps, conditions, repetitions (then Big O)", "Only logos", "Only careers", "Only Figma"], "a"),
            ("“Number of steps” is:", ["Basic operations in one pass / closed form", "The page count of the PDF", "OSI layers", "Sprint days"], "a"),
            ("You combine the three to:", ["Justify a Big O class", "Pick a colour", "Pick a font", "Pick a career"], "a"),
            ("A 5-mark compare question wants:", ["The framework on both algorithms + a verdict", "Only names", "Only Python libraries", "Only UX"], "a"),
            ("Constants matter at tiny n but the framework emphasises:", ["Growth", "Hex colours", "Teacher names", "PDF margins"], "a"),
            ("If repetitions are nested n×n, Big O is likely:", ["n² regardless of a few extra ifs", "log n", "1", "n!"], "a"),
        ],
        [
            ("State the efficiency evaluation framework.",
             "Count significant steps, conditions, repetitions; combine into time/space class; compare to requirements."),
            ("Apply in one line to binary search.",
             "Few steps per shot, one/two conditions, log n repetitions → O(log n) time, O(1) space."),
            ("Apply to bubble sort.",
             "Compare+swap steps, a condition, nested repetitions → O(n²)."),
            ("When would you still pick the slower class?",
             "Tiny n, need stability/simplicity, or the fast one needs a costly precondition (sort first)."),
        ],
        [
            ("Using the framework, compare selection sort vs binary search as if a student mixed them up. Then say why they are not alternatives.",
             "Different problems (order vs find). Framework still: both have loops; sort n² vs search log n. Verdict: sort then many binary queries if the list is reused."),
        ],
    )


def _refine(*_):
    return (
        [
            ("A clarity refinement is:", ["Rename, split, comment, simplify logic", "Add more nested loops for fun", "Shorten names to a,b,c", "Remove all spaces"], "a"),
            ("An efficiency refinement is:", ["Cut extra work (e.g. already-sorted inner of bubble)", "Add random sleeps", "Copy the list 12 times", "Print inside the inner loop 1e6 times"], "a"),
            ("Flagged bubble sort’s early exit is:", ["Efficiency refinement", "A new UX colour", "A foreign key", "A pie"], "a"),
            ("Extracting a function is:", ["Clarity (and sometimes reuse) refinement", "Always worse Big O", "OSI layering", "A histogram"], "a"),
            ("Do not “optimise” first if:", ["The algorithm is still incorrect or unreadable", "n=10^12 already proven", "Tests all pass and profiler points here", "It is O(n!) on huge n and you must ship"], "a"),
            ("Redundant work means:", ["Computing the same thing twice", "A needed loop", "A primary key", "A caption"], "a"),
        ],
        [
            ("Two clarity refinements.",
             "Better names; extract module; remove duplicate logic; add pre/post comments."),
            ("Two efficiency refinements from the book.",
             "Stop inner bubble as the suffix grows sorted; avoid extra copies; fewer conditions in the inner loop."),
            ("A refinement that hurts clarity for 1% speed is:",
             "Usually a bad deal in XI/XII and in teams."),
            ("How do you know a refinement worked?",
             "Same tests (correctness) + fewer operations or clearer reading."),
        ],
        [
            ("Show bubble sort before/after: (1) meaningful names (2) last-i unsorted bound (3) swapped flag. State what each changed (clarity vs efficiency).",
             "Code/pseudocode both versions. (1) clarity (2) fewer comparisons n²/2 still O(n²) (3) best case O(n). Tests unchanged."),
        ],
    )


def _ds(*_):
    return (
        [
            ("A data structure is:", ["An organised way to store and access data", "A random pile", "A font", "A sprint"], "a"),
            ("We pick a structure for:", ["The operations we need (fast insert? fast search?)", "The logo", "The teacher’s birthday", "The PDF theme"], "a"),
            ("Linear vs non-linear is about:", ["Whether elements form a sequence vs branches/links", "Colour", "File format .py vs .txt", "Agile vs waterfall"], "a"),
            ("An array gives fast:", ["Index access O(1)", "Insert at front O(1) always", "Arbitrary graph neighbours", "Sorted insert O(1) always"], "a"),
            ("This is ★ because papers ask:", ["Define + why we need DS + one example", "Only careers", "Only Figma", "Only OSI"], "a"),
            ("A queue of print jobs is a DS chosen because:", ["Order of arrival matters (FIFO)", "LIFO undo", "Hierarchy of boss-staff", "Random friends links"], "a"),
        ],
        [
            ("Define data structure.",
             "A systematic way to organise data for efficient access and modification."),
            ("Why not always use one big list?",
             "Some problems need LIFO, FIFO, hierarchy, or many-to-many links."),
            ("Give one linear and one non-linear example.",
             "Linear: array/stack/queue. Non-linear: tree/graph."),
            ("What is an operation on a DS?",
             "Insert, delete, search, traverse, peek…"),
        ],
        [
            ("“If you pick the wrong structure, the algorithm looks harder.” Explain with college examples of array, stack, queue, tree. ★ Golden.",
             "Roll list: array. Undo typing: stack. Printer/canteen line: queue. Org chart/folders: tree. Wrong pick: using a stack for a fair queue angers people."),
        ],
    )


def _linear_ds(*_):
    return (
        [
            ("An array stores items:", ["In contiguous indexed slots of one type", "With arbitrary node links only", "As a hierarchy always", "As a pie"], "a"),
            ("A linked list stores items:", ["In nodes with pointers to the next", "In one block of equal indexes only", "As a tree of bosses", "As a hash of pies"], "a"),
            ("A stack is:", ["LIFO", "FIFO", "A graph", "A GUI"], "a"),
            ("A queue is:", ["FIFO", "LIFO", "A binary tree", "A K-map"], "a"),
            ("Undo in an editor uses a:", ["Stack", "Queue", "Pie", "OSI layer"], "a"),
            ("A printer line is a:", ["Queue", "Stack", "AVL tree always", "NAND"], "a"),
        ],
        [
            ("Define array, linked list, stack, queue in one line each.",
             "Array: indexed block. List: nodes+links. Stack: LIFO. Queue: FIFO."),
            ("One op each: push/pop, enqueue/dequeue.",
             "Stack push/pop top. Queue enqueue rear, dequeue front."),
            ("Array vs list for insert at front.",
             "Array shifts O(n); list pointer change O(1) if you have the head."),
            ("Peek means:",
             "Read the top/front without removing."),
        ],
        [
            ("Draw stack and queue after the sequence: insert A,B,C then remove one. Show remaining order and a real example of each. ★ Golden for stack/queue.",
             "Stack remaining B,A (C popped). Queue remaining B,C (A served). Examples: back button vs ticket counter. Diagrams with top/front labelled."),
        ],
    )


def _nonlinear(*_):
    return (
        [
            ("A tree has:", ["A root and branches, no cycles in the usual CS tree", "A single line only", "A LIFO rule only", "A pie"], "a"),
            ("A graph models:", ["Nodes and edges, possibly with cycles", "Only a list", "Only a stack", "Only a table of two columns always"], "a"),
            ("A college org chart is a:", ["Tree", "Queue", "Stack", "Pie"], "a"),
            ("A road map of Karachi is a:", ["Graph", "Stack", "Array of 2 cells", "Queue of 1"], "a"),
            ("Hierarchy of folders is a:", ["Tree", "FIFO queue", "LIFO only", "OSI physical only"], "a"),
            ("Friends on a social network: better a:", ["Graph", "Strict tree of one boss", "Stack of likes only", "Queue of photos only"], "a"),
        ],
        [
            ("Define tree and graph.",
             "Tree: hierarchical, one parent (except root), no cycles. Graph: vertices+edges, cycles allowed."),
            ("Give a school tree and a school graph.",
             "Tree: principal→HOD→teachers. Graph: bus routes between campuses."),
            ("What is a child / leaf?",
             "Child: node under a parent. Leaf: no children."),
            ("Why not force a graph into a tree?",
             "You would drop extra links that are real (two roads, two friends)."),
        ],
        [
            ("For (a) course prerequisites (b) WhatsApp groups (c) folder system: choose tree or graph and justify with a tiny sketch.",
             "(a) graph (or DAG) — cycles should not exist but multiple parents can. (b) graph. (c) tree. Sketches labelled. One sentence if a cycle would mean a bug."),
        ],
    )


def _ds_ops(*_):
    return (
        [
            ("Common DS operations include:", ["Insert, delete, search, traverse", "Only compile", "Only ping", "Only print the logo"], "a"),
            ("Traverse means:", ["Visit elements in some order", "Delete all", "Encrypt all", "Sort the OS"], "a"),
            ("Search cost depends on:", ["The structure (array vs sorted vs hash vs tree)", "The PDF theme", "The teacher name", "The sprint"], "a"),
            ("Insert in a full array may:", ["Fail or require resizing", "Always O(1) no matter what", "Create a graph edge automatically", "Pop a stack"], "a"),
            ("Delete from a queue happens at the:", ["Front", "Rear only always", "Random index", "Root of a tree"], "a"),
            ("You choose a DS by the:", ["Operations you will do most", "First letter of the course", "Colour", "NAND count"], "a"),
        ],
        [
            ("List five operations.",
             "Create, insert, delete, search, traverse, update, sort (as applicable)."),
            ("Give costs qualitatively: array index vs list search.",
             "Array index O(1); unsorted list search O(n)."),
            ("What does traverse a tree mean?",
             "Visit every node (pre/in/post or level order)."),
            ("Why “update” might be search+insert.",
             "You must find the item first."),
        ],
        [
            ("For array, stack, queue, tree: name the natural insert/delete ends and one costly operation. Table.",
             "Array: insert middle costly. Stack: top only cheap. Queue: rear in front out. Tree: search/insert depend on balance. 8-row table."),
        ],
    )


def _ds_scene(*_):
    return (
        [
            ("Matching a DS to a scenario is:", ["Looking at order, hierarchy, and operations", "Picking at random", "Always a stack", "Always a pie"], "a"),
            ("Browser back button:", ["Stack", "Queue", "Tree of the whole internet always", "Array of 1"], "a"),
            ("Print spooler:", ["Queue", "Stack", "Graph of fonts", "K-map"], "a"),
            ("Family tree / org chart:", ["Tree", "Queue", "Stack", "FIFO only"], "a"),
            ("Maps / networks:", ["Graph", "Stack", "Queue", "Single array of 2 ints"], "a"),
            ("Marks of 40 students in one test:", ["Array (or list)", "Graph of roads", "Call stack", "Binary tree of buses"], "a"),
        ],
        [
            ("Give the decision questions from the notes.",
             "Is there a first/last? Hierarchy? Many links? Need fast index?"),
            ("Two linear scenarios.",
             "Array of marks; queue at the photocopier."),
            ("Two non-linear.",
             "Folders; city roads."),
            ("A wrong match.",
             "Using a stack for a fair ticket line — last person is served first."),
        ],
        [
            ("Six scenarios → DS + one reason each: undo, call waiting, class list, website links, company staff, circular metro line.",
             "Stack; queue; array/list; graph; tree; graph (cycle). Table. One sentence on operations you need."),
        ],
    )


def _ds_trace(*_):
    return (
        [
            ("Tracing retrieval means:", ["Following how an algorithm finds/returns an item", "Deleting the DS", "Drawing Figma", "Running pip"], "a"),
            ("Array retrieval by index is:", ["Direct: a[i]", "Walk from head always", "Pop until empty always", "BFS always"], "a"),
            ("Linked-list retrieval of the k-th is:", ["Walk k links", "O(1) index", "A binary cut", "A hash"], "a"),
            ("Queue retrieval of the next client is:", ["Dequeue front (FIFO)", "Pop top (LIFO)", "Random node", "Tree root"], "a"),
            ("You cannot take the middle of a queue without:", ["Breaking FIFO (or using another DS)", "It is the definition of queue", "A pie", "A sprint"], "a"),
            ("A trace should show:", ["Pointers/indexes before and after", "Only the career names", "Only colours", "Only OSI"], "a"),
        ],
        [
            ("Trace getting a[2] from array [10,20,30,40].",
             "Index 2 → 30 in one step."),
            ("Trace finding 30 in a list 10→20→30.",
             "Start 10 ≠, next 20 ≠, next 30 =. Three visits."),
            ("Trace queue  A-B-C  serve one.",
             "Dequeue A; front is B. Remaining B-C."),
            ("Why tracing retrieval is in the syllabus.",
             "So you can justify the DS with actual steps, not slogans."),
        ],
        [
            ("Same three names stored in array, list, queue. Trace “get the second person” in each. Who is not allowed in a pure queue?",
             "Array a[1]; list two hops; queue: you may only legally take the front — getting the second requires dequeue then the new front, which also removes the first. That is the point."),
        ],
    )


def _py_ds(*_):
    return (
        [
            ("Python built-in structures in this chapter include:", ["list, tuple, set, dict", "only arrays of C", "only trees", "only graphs"], "a"),
            ("You choose among them by:", ["Order? Duplicates? Mutability? Key lookup?", "The logo", "The font", "The sprint"], "a"),
            ("Mutable means:", ["You can change it in place", "Frozen forever", "Always sorted", "Always unique"], "a"),
            ("A dict maps:", ["Keys to values", "Only numbers to NAND", "Only OSI layers", "Only files"], "a"),
            ("A set is best for:", ["Unique items / membership tests", "Ordered ranking with duplicates", "LIFO", "FIFO"], "a"),
            ("This lecture is the map; later lectures:", ["Zoom into each type", "Delete Python", "Draw only ER", "Draw only Figma"], "a"),
        ],
        [
            ("One-line each: list, tuple, set, dict.",
             "List: ordered mutable sequence. Tuple: ordered immutable. Set: unique unordered. Dict: key→value."),
            ("Which for student names that may repeat seats? ",
             "List (order). If unique roll numbers: set or dict."),
            ("Which for a record of roll→marks?",
             "Dict."),
            ("Which as a function return of (x,y) that must not change?",
             "Tuple."),
        ],
        [
            ("Four college needs → choose the Python DS and justify with one operation each.",
             "Attendance ordered: list. RGB colour constant: tuple. Club unique IDs: set. Phonebook: dict. Show one line of code each."),
        ],
    )


def _lists(*_):
    return (
        [
            ("A list is:", ["Ordered and mutable", "Immutable", "Unordered unique only", "A dict of keys"], "a"),
            ("Negative index -1 is:", ["The last item", "The first", "An error always", "A key"], "a"),
            ("append adds:", ["At the end", "At the front always", "A new dict key", "A file"], "a"),
            ("slicing a[1:3] on [10,20,30,40] is:", ["[20,30]", "[10,20,30]", "[30]", "[20,30,40]"], "a"),
            ("Lists can hold:", ["Mixed types (but usually don’t for sanity)", "Only ints", "Only strings", "Only dicts"], "a"),
            ("remove(x) raises if:", ["x is not in the list", "x is last", "The list is long", "You used print"], "a"),
        ],
        [
            ("Three list methods with effect.",
             "append, insert, pop, remove, sort, reverse — any three with one line each."),
            ("How do you walk a list?",
             "for x in lst:  or for i in range(len(lst))."),
            ("What does mutable mean here?",
             "lst[0]=5 is legal; the object changes."),
            ("Show a search snippet.",
             "if target in lst / for loop with break."),
        ],
        [
            ("Write a small program: read 5 marks into a list, print max, min, and those above average. Show a sample run.",
             "Use list, loop, sum/len, if. Output exact for a chosen sample. Mention IndexError if you go past 4."),
        ],
    )


def _tuples(*_):
    return (
        [
            ("A tuple is:", ["Ordered and immutable", "Mutable like a list", "A set of unique keys", "A file mode"], "a"),
            ("t[0]=5 on a tuple:", ["TypeError", "Works", "Deletes t", "Converts to list silently always"], "a"),
            ("Why immutability?",
             ["Safe as dict keys; safer returns; can be hashed", "It makes tuples faster than CPUs", "It allows append()", "It stores files"], "a"),
            ("A 1-item tuple is written:", ["(5,)", "(5)", "[5]", "{5}"], "a"),
            ("Unpacking a,b = (1,2) sets:", ["a=1, b=2", "a=(1,2)", "Syntax error", "a=2"], "a"),
            ("tuple methods include:", ["count, index", "append, sort", "add, discard", "keys, items"], "a"),
        ],
        [
            ("Define tuple and one use.",
             "Immutable ordered sequence. RGB colour; returning two values."),
            ("How to “change” a tuple?",
             "Build a new one, or convert to list, change, convert back."),
            ("Why (5,) not (5)?",
             "(5) is just int 5; comma makes a tuple."),
            ("Can a tuple contain a list?",
             "Yes — the tuple’s slots cannot be rebound, but the inner list can still mutate (a subtle exam point)."),
        ],
        [
            ("Write code that stores student (name, roll) tuples in a list, prints each, and explain two errors: mutate the tuple; forget the comma in a 1-tuple.",
             "records.append((\"Ali\", 12)). for n,r in records. t[0]=… TypeError. (5) vs (5,). 10-mark with output."),
        ],
    )


def _sets(*_):
    return (
        [
            ("A set holds:", ["Unique unordered items", "Ordered duplicates", "Key-value pairs", "File handles only"], "a"),
            ("{1,2,2,3} becomes:", ["{1,2,3}", "{1,2,2,3}", "[1,2,2,3]", "(1,2,2,3)"], "a"),
            ("s.add is for:", ["Insert (no-op if present)", "Append at index 0", "Sort", "Open a file"], "a"),
            ("Union of {1,2} and {2,3} is:", ["{1,2,3}", "{2}", "{1}", "{}"], "a"),
            ("You cannot:", ["Index s[0] on a set", "Iterate a set", "Test x in s", "Compute intersection"], "a"),
            ("Sets are great for:", ["Membership and unique collections", "FIFO queues", "LIFO undo", "Stable sorted ranks with duplicates"], "a"),
        ],
        [
            ("Define set and two operations.",
             "Unordered unique. union |  intersection &  difference - ."),
            ("Why no index?",
             "No order — use a loop, not s[0]."),
            ("How to make unique names from a list?",
             "set(names) — order lost."),
            ("Empty set syntax?",
             "set() not {} (that is a dict)."),
        ],
        [
            ("Two clubs A and B as sets. Write Python for members in both, only A, either. Show a sample.",
             "A&B, A-B, A|B. Sample Ali/Sara. Mention add/discard. One exam warning: {} is dict."),
        ],
    )


def _dicts(*_):
    return (
        [
            ("A dict stores:", ["key: value pairs", "Only a list of values", "Only unique numbers without keys", "Only files"], "a"),
            ("Keys in a dict must be:", ["Hashable (immutable) and unique", "Lists", "Sets", "Other dicts as keys commonly"], "a"),
            ("d.get(\"x\") if missing:", ["Returns None (or default) instead of crashing", "Always KeyError", "Deletes d", "Sorts d"], "a"),
            ("d[\"x\"] if missing:", ["KeyError", "None always", "0 always", "Inserts NAND"], "a"),
            ("d.keys() is:", ["A view of keys", "A tuple of values", "A file", "A stack"], "a"),
            ("Updating d[\"a\"]=2 if a exists:", ["Overwrites", "Creates a second a", "Errors always", "Appends a list"], "a"),
        ],
        [
            ("Define dictionary with a 2-pair example.",
             "{\"Ali\": 85, \"Sara\": 90}"),
            ("Safe read vs direct read.",
             "get vs [ ]."),
            ("How to loop keys and values.",
             "for k,v in d.items():"),
            ("Why lists cannot be keys.",
             "Mutable, unhashable."),
        ],
        [
            ("Write a marks dict program: add a student, update, print using items(), handle a missing name with get. Sample I/O.",
             "CRUD-ish four operations. KeyError demo vs get. 10-mark complete code."),
        ],
    )


def _builtins(*_):
    return (
        [
            ("len(x) works on:", ["Sequences and many collections", "Only ints", "Only files", "Only NAND"], "a"),
            ("min([3,1,2]) is:", ["1", "3", "2", "6"], "a"),
            ("sum((1,2,3)) is:", ["6", "123", "Error always", "(1,2,3)"], "a"),
            ("max on a dict without a key function uses:", ["Keys (careful!)", "Values always", "Lengths always", "Random"], "a"),
            ("These functions expect:", ["Non-empty for min/max", "Always empty", "Only sets", "Only files"], "a"),
            ("len(\"CS\") is:", ["2", "1", "0", "3"], "a"),
        ],
        [
            ("Four built-ins and a type they work on.",
             "len list; min tuple; max set; sum list of numbers."),
            ("What happens min([]))",
             "ValueError."),
            ("sum of a list of strings?",
             "TypeError — sum starts at 0."),
            ("len vs count in a list.",
             "len whole length; count(x) occurrences of x."),
        ],
        [
            ("Given marks = [70, 80, 90] write expressions for n, total, mean, best, worst using built-ins. Show values. Warn about empty lists.",
             "n=len=3; sum=240; mean=80; max=90; min=70. Empty: don’t divide; min/max error. Link to Ch 4 statistics."),
        ],
    )


def _attendance(*_):
    return (
        [
            ("A sensible structure for present/absent flags by name is:", ["dict name→status or two lists/sets", "A pie without data", "A NAND net", "An OSI capture"], "a"),
            ("You should still:", ["Validate input (yes/no)", "Trust any string", "Use eval", "Open the OS"], "a"),
            ("Printing a report uses:", ["A loop over the collection", "A single print of the object id", "TCP", "Figma"], "a"),
            ("This activity combines:", ["DS + input + selection + repetition", "Only HCI colours", "Only ER", "Only Big O proofs"], "a"),
            ("A set of absentees is useful to:", ["Unique names, fast membership", "Keep duplicate absences as a stack", "FIFO print jobs", "Store key-value marks"], "a"),
            ("Never store:", ["Passwords in the same toy script unprotected", "Names", "P/A flags", "Dates"], "a"),
        ],
        [
            ("Outline the attendance program’s data and loop.",
             "For each student: ask status; store; then print counts."),
            ("Two Python DS options.",
             "dict[str,str] or present_set/absent_set."),
            ("How do you count presents?",
             "Counter in the loop or list.count / sum(1 for …)."),
            ("One improvement for XII files.",
             "Save to a text file with with-open."),
        ],
        [
            ("Write a complete small attendance program for 3 names using a dict, print a tidy table, and a sample run.",
             "Working code, output, and one validation (only P/A). Mention a logic error if you forget to store."),
        ],
    )


def _wordfreq(*_):
    return (
        [
            ("Word frequency uses a dict as:", ["word → count", "count → word only", "A stack of letters", "A queue of files"], "a"),
            ("A standard pattern is:", ["d[w] = d.get(w,0)+1", "sort first always O(n²)", "binary search the sentence", "draw OSI"], "a"),
            ("You usually:", ["split() and maybe lower()", "Keep punctuation attached always", "Use a set so counts die", "Use a tuple of counts you cannot update"], "a"),
            ("split(\"a a b\") has length:", ["3", "2", "1", "0"], "a"),
            ("This activity shows:", ["Dicts + loops + strings", "Only Access reports", "Only NAND", "Only HCI"], "a"),
            ("Most frequent word is:", ["The key with max count", "Always the first word", "Always the last", "A foreign key"], "a"),
        ],
        [
            ("Write the counting pattern.",
             "for w in text.lower().split(): d[w]=d.get(w,0)+1"),
            ("How to print nicely.",
             "for k,v in d.items(): print(k,v)  or sorted by count."),
            ("A limitation of naive split.",
             "Punctuation (“hello,”) is a different word."),
            ("Why a dict not a list of pairs?",
             "O(1) average update by word."),
        ],
        [
            ("Count words in “to be or not to be”. Show the dict, then the mode word(s). Full code.",
             "to:2 be:2 or:1 not:1. Bimodal to/be. Code with get. Mention lower()."),
        ],
    )


def _fn(*_):
    return (
        [
            ("A function is:", ["A named reusable block", "A random line in main only", "A pie", "A cable"], "a"),
            ("You define with:", ["def name(params):", "function name {}", "fun name", "lambda only always"], "a"),
            ("A call is:", ["name(arguments)", "def again", "import name always", "print the source only"], "a"),
            ("Duplicate code is bad because:", ["Fixes must be repeated; more bugs", "Python forbids functions", "It is faster always", "It is required by BIEK"], "a"),
            ("This is ★: expect:", ["Write a small function + call + output", "Only define HCI", "Only OSI", "Only ER"], "a"),
            ("Parameters are:", ["Placeholders in the definition", "The values at the call (arguments)", "Always globals", "Always files"], "a"),
        ],
        [
            ("Define function, parameter, argument.",
             "Reusable block; names in def; values you pass."),
            ("Why functions (three reasons).",
             "Reuse, clarity, testing, less duplication."),
            ("Show a 3-line add function.",
             "def add(a,b): return a+b"),
            ("What happens if you def but never call?",
             "Nothing runs — no output."),
        ],
        [
            ("Write functions to compute area of rectangle and circle, call both from main, show output. Explain def vs call. ★ Golden.",
             "Two defs, two calls, printed numbers. Mention return vs print inside. π=3.14 or math.pi."),
        ],
    )


def _fn_types(*_):
    return (
        [
            ("Built-in functions include:", ["len, print, min (provided by Python)", "Only ones you def", "Only pip packages", "Only SQL"], "a"),
            ("User-defined functions are:", ["Ones you write with def", "print and len", "CPU instructions", "OSI layers"], "a"),
            ("You still:", ["Call both with name()", "Cannot call built-ins", "Must recompile C", "Must draw Figma"], "a"),
            ("A module function like math.sqrt is:", ["Library/built-in-standard, not your def", "A user def in your file", "A dict", "A stack"], "a"),
            ("Why write your own if print exists?",
             ["Your problem’s chunks (bill tax, grade band) are not built in", "Python forbids print", "Built-ins cannot be called", "def is illegal"], "a"),
            ("Help(len) documents a:", ["Built-in", "Your secret function always", "A table", "A query"], "a"),
        ],
        [
            ("Differentiate built-in vs user-defined with examples.",
             "Built-in: print, len. User: def grade(m): …"),
            ("Can user-defined call built-in?",
             "Yes — that is normal."),
            ("Where do library functions sit?",
             "Neither in your file nor mysterious — imported modules."),
            ("One exam trap.",
             "Calling a function you never defined and is not built-in → NameError."),
        ],
        [
            ("In one program use a built-in, a standard-library function, and a user-defined function. Label each and show output.",
             "print/len; math.sqrt; def mean. Three labels in comments. Exact numeric output."),
        ],
    )


def _fn_ret(*_):
    return (
        [
            ("return sends a value:", ["Back to the caller", "To the printer always", "To a file always", "To OSI layer 1"], "a"),
            ("A function with only print:", ["Shows something but gives None to the caller", "Returns the text automatically", "Returns 0", "Cannot run"], "a"),
            ("x = f() if f has no return:", ["x is None", "x is 0", "Error always", "x is f"], "a"),
            ("return also:", ["Exits the function immediately", "Loops forever", "Defines a class", "Opens a socket"], "a"),
            ("You can return:", ["Any object (number, str, tuple, list, dict)", "Only ints", "Only True", "Only files"], "a"),
            ("print(f()) prints the:", ["Returned value (or None)", "Source code", "The name f", "A pie"], "a"),
        ],
        [
            ("Why return rather than print inside?",
             "The caller can store, test, or reuse the value."),
            ("Show both styles for doubling 5.",
             "print inside vs return 10 and print in main."),
            ("Returning two values.",
             "return a,b  → a tuple, unpack."),
            ("What is None?",
             "The default return if you fall off the end."),
        ],
        [
            ("Write mean(a,b,c) that returns a float. Show a test print and a logic error version that prints but returns None. Explain the bug in a unit-test style.",
             "Correct return (a+b+c)/3. Buggy print only → assert mean(1,2,3)==2 fails with None. Teaching point of return."),
        ],
    )


def _calc(*_):
    return (
        [
            ("A calculator activity should use:", ["A function per operation", "One 200-line print spaghetti only", "No functions", "Only globals named a,b,c,d,e"], "a"),
            ("Division must consider:", ["Zero divisor", "NAND grouping", "OSI layer", "Figma frames"], "a"),
            ("Menu + functions is:", ["Selection + modularity", "A stack hardware", "A pie", "A foreign key"], "a"),
            ("return lets you:", ["Print nicely in one place", "Hide errors", "Skip tests", "Avoid operators"], "a"),
            ("float(input) may raise:", ["ValueError", "A pie", "A K-map", "A sprint"], "a"),
            ("This activity prepares:", ["Reusable functions + later try/except", "Only Access", "Only HCI colours", "Only ER"], "a"),
        ],
        [
            ("Outline four functions for + − × ÷.",
             "add, sub, mul, div with two params, return."),
            ("How do you stop divide by zero?",
             "if b==0: return a message / raise / skip."),
            ("Where does the menu live?",
             "In main: while True: choice…"),
            ("Why not copy the formula 12 times?",
             "One fix in one function."),
        ],
        [
            ("Write a mini calculator with four functions, a loop menu, and a safe divide. Sample session of 3 operations then quit.",
             "Working structure, sample I/O, ZeroDivision handled. Mention return vs print."),
        ],
    )


def _scope(*_):
    return (
        [
            ("A local variable lives:", ["Inside the function", "In the whole file always", "On the disk", "In OSI"], "a"),
            ("A global variable lives:", ["At module level (the file)", "Only in one for-loop", "Only in a dict key", "Only in RAM of another PC"], "a"),
            ("Reading a global from a function:", ["Works", "Always error", "Deletes it", "Makes it local"], "a"),
            ("Assigning to a name in a function without global:", ["Creates a local (does not change the outer)", "Always updates global", "Syntax error", "Opens a file"], "a"),
            ("global x is needed to:", ["Rebind a global from inside a function", "Import math", "Draw a pie", "Sort a list"], "a"),
            ("Prefer:", ["Parameters and return, not lots of globals", "All globals", "No names", "eval"], "a"),
        ],
        [
            ("Define local vs global.",
             "Local: created in function, dies when it ends. Global: file-level."),
            ("A classic bug.",
             "x=1; def f(): x=x+1  without global → UnboundLocalError."),
            ("How to share results instead of globals?",
             "return values / pass them as arguments."),
            ("Can two functions have locals named total?",
             "Yes — they are different variables."),
        ],
        [
            ("Show a 10-line program where a global count is incremented with global, then rewrite it with return so you do not need global. Explain which is clearer.",
             "Both outputs match. Prefer return. UnboundLocalError snippet as a warning."),
        ],
    )


def _files(*_):
    return (
        [
            ("open(path, \"r\") is for:", ["Reading", "Wiping the file", "Appending only", "Creating a DB"], "a"),
            ("Mode \"w\":", ["Write (truncates existing)", "Read only", "Append", "Binary XOR"], "a"),
            ("Mode \"a\":", ["Append at the end", "Overwrite from start", "Read", "Delete the file"], "a"),
            ("You should:", ["close() (or use with)", "Leave files locked", "Never flush", "Always use w for logs"], "a"),
            ("read() returns:", ["The whole content as str (text mode)", "A dict always", "A pandas DataFrame", "A stack"], "a"),
            ("This is ★ because practicals ask you to:", ["Write a small file program", "Draw only ER", "Only HCI", "Only OSI"], "a"),
        ],
        [
            ("The three text modes and a danger of w.",
             "r read, w write/overwrite, a append. w erases previous content."),
            ("write vs writelines.",
             "write a string; writelines a sequence of strings."),
            ("Why close?",
             "Flush + unlock. Crash before close can lose data."),
            ("A FileNotFoundError happens when:",
             "r on a path that does not exist."),
        ],
        [
            ("Write a program that appends a line to marks.txt and then reads all lines. Show the file after two runs. ★ Golden.",
             "open a; write; close; open r; print. Second run has two lines. Warn that w would have kept only the last."),
        ],
    )


def _withstmt(*_):
    return (
        [
            ("with open(...) as f:", ["Closes the file automatically, even after errors", "Never closes", "Deletes the path", "Converts to pandas"], "a"),
            ("The with-block is a:", ["Context manager", "Thread", "Socket always", "K-map"], "a"),
            ("If an exception happens inside with:", ["The file still closes", "The file stays locked forever", "Python uninstalls", "The disk formats"], "a"),
            ("You still choose the mode:", ["r/w/a as before", "with replaces modes", "Modes are only for SQL", "Modes are HCI"], "a"),
            ("This is ★ because it is the:", ["Safe modern pattern for files", "Old optional style", "Only for pandas", "Only for Figma"], "a"),
            ("f is only valid:", ["Inside the with block", "After the block always", "Before open", "In another file automatically"], "a"),
        ],
        [
            ("Write the canonical read pattern.",
             "with open(\"a.txt\") as f: data=f.read()"),
            ("Why it beats try/finally for beginners.",
             "Less boilerplate; close is guaranteed."),
            ("Can you nest with for two files?",
             "Yes — with open(a) as f, open(b) as g:"),
            ("What if the path is wrong in with-open r?",
             "Still FileNotFoundError — with does not create the file in r."),
        ],
        [
            ("Rewrite a grade-tracker snippet from open/close to with, and show what happens if int() fails on a line. Why is with safer? ★ Golden.",
             "Exception in parse still closes. Compare to forgotten close on the error path. Sample file 3 lines, one bad."),
        ],
    )


def _except(*_):
    return (
        [
            ("try/except is for:", ["Handling runtime errors without crashing the whole program", "Fixing syntax errors (missing colons)", "Faster Big O", "Drawing pie charts"], "a"),
            ("FileNotFoundError is raised when:", ["open r on a missing path", "1/0", "int(\"a\")", "A logic bug that prints 3 instead of 4"], "a"),
            ("except ValueError catches:", ["int(\"hi\")", "Missing files", "SyntaxError of a colon", "Logic silent bugs"], "a"),
            ("except Exception is:", ["Broad — use with care", "The way to hide all bugs always", "A sort", "A key"], "a"),
            ("else on try runs when:", ["No exception occurred", "Always", "Only on errors", "On syntax errors"], "a"),
            ("finally runs:", ["Always (cleanup)", "Only on success", "Only on error", "Never with with"], "a"),
        ],
        [
            ("Why exceptions in file programs?",
             "Missing files and bad lines are expected; crash is a poor UX."),
            ("Show a try around int(input).",
             "try: n=int(input()) except ValueError: print(\"Enter a number\")."),
            ("Does try fix logic errors?",
             "No — wrong formula still wrong."),
            ("Order of except clauses.",
             "Specific first, broader later."),
        ],
        [
            ("Write a reader that tries to open marks.txt, handles missing file, skips bad lines with ValueError, and prints a count of good rows.",
             "Full code. Sample: file missing message; file with 80, x, 90 → 2 good. Mention not using bare except."),
        ],
    )


def _grades(*_):
    return (
        [
            ("A grade tracker typically:", ["Writes scores, then reads to average", "Only draws Figma", "Only sorts NAND", "Only pings OSI"], "a"),
            ("Use mode a when:", ["Adding a new score without wiping history", "You want an empty file each run", "You only read", "You drop tables"], "a"),
            ("Average needs:", ["Sum and count of valid numbers", "Min only", "A pie only", "A stack"], "a"),
            ("with + try together give:", ["Safe close + safe parse", "Faster CPUs", "UI colours", "Foreign keys"], "a"),
            ("A good report prints:", ["Each line and the mean", "Only the file path", "Only None", "Only errors"], "a"),
            ("This mini project pulls together:", ["Functions, files, exceptions, arithmetic", "Only HCI wireframes", "Only ER", "Only Agile"], "a"),
        ],
        [
            ("List the features of the mini project.",
             "Create/append records, read, compute average, handle missing/bad data."),
            ("File format you would choose.",
             "One number per line, or name,marks CSV."),
            ("How to compute mean safely.",
             "Count valid rows; if count==0 do not divide."),
            ("One extension.",
             "Also print min/max; skip blank lines."),
        ],
        [
            ("Write the full grade-tracker: append two marks, reopen, print average. Show both the code and the file contents. Handle empty file.",
             "Working program, sample file, output 85.0 for 80 and 90. Empty → “no marks yet”. with-open throughout."),
        ],
    )


def _analysis(*_):
    return (
        [
            ("Data analysis is:", ["Examining data to extract useful information", "Only collecting rumours", "Only drawing logos", "Only cabling"], "a"),
            ("Python is used because:", ["Files, databases, stats, plots in one language", "It is analog", "It cannot loop", "It cannot import"], "a"),
            ("Raw marks vs “class average 62”:", ["Data vs information", "Information vs data", "Both keys", "Both NAND"], "a"),
            ("A decision is the:", ["Point of analysis", "First NAND", "Last OSI layer always", "Sprint name"], "a"),
            ("Without a question, analysis is:", ["Aimless charting", "Always AI", "Always IoT", "Always HCI"], "a"),
            ("XII tools for analysis include:", ["sqlite3, pandas, matplotlib, statistics", "Only LogiSim", "Only Figma", "Only Access macros"], "a"),
        ],
        [
            ("Define data analysis with a college example.",
             "Process marks to decide who needs extra class."),
            ("Four Python superpowers listed in the notes.",
             "Read files, talk to DB, statistics, charts (and readable syntax)."),
            ("What is not analysis?",
             "Dumping 400 rows on a slide with no summary."),
            ("Link to XI digital literacy.",
             "Same collect–present loop, now with code."),
        ],
        [
            ("A Hyderabad college has 400 CS marks. Write four analysis questions and which Python tool answers each.",
             "Average: pandas mean. Fail count: filter. Shift compare: groupby. Trend: matplotlib line if by year. Mention cleaning NaNs first."),
        ],
    )


def _connect(*_):
    return (
        [
            ("The five connection parts in order start with:", ["Database then driver", "Cursor then database", "SQL then mouse", "Chart then file"], "a"),
            ("The cursor:", ["Executes SQL and fetches rows", "Is the .db file", "Is matplotlib", "Is Figma"], "a"),
            ("The connection object is the:", ["Pipeline", "SQL text", "Driver brand only", "Pie"], "a"),
            ("sqlite3 is the:", ["Built-in driver (+ DB engine in-process)", "A web browser", "An OSI layer", "A sort"], "a"),
            ("SQL examples:", ["SELECT, INSERT, CREATE", "def, for, if", "AND, OR, NOT gates", "HTTP GET only"], "a"),
            ("Swapping cursor and connection in an answer is a:", ["Classic 0-mark mix-up", "Required trick", "Big O class", "UX heuristic"], "a"),
        ],
        [
            ("Name the five components in order.",
             "Database, driver, connection, cursor, SQL."),
            ("Why a driver?",
             "Translates Python calls to the DBMS protocol/API."),
            ("SQLite vs MySQL in one line.",
             "SQLite: file, no server. MySQL: server for many users."),
            ("Draw the flow.",
             "Python → driver → connection → cursor → SQL → DB."),
        ],
        [
            ("Label a 9-line sqlite snippet with the five components. Explain commit vs close. ★ Golden.",
             "import=driver; connect=connection; cursor=cursor; execute=SQL; school.db=database. commit saves; close unlocks. Missing commit → empty next run."),
        ],
    )


def _sqlite(*_):
    return (
        [
            ("sqlite3.connect(\"school.db\") will:", ["Open or create the file", "Always error if missing", "Start MySQL server", "Draw a pie"], "a"),
            ("After INSERT you must:", ["commit()", "only close", "drop the table", "pip install sqlite"], "a"),
            ("fetchall() returns:", ["A list of tuples (rows)", "A DataFrame always", "A dict of dicts always", "A string of SQL"], "a"),
            ("CREATE TABLE IF NOT EXISTS avoids:", ["Error on re-run", "The need for types", "The need for keys", "commit"], "a"),
            ("close() is needed to:", ["Unlock the file", "Create pandas", "Sort rows", "Encrypt OSI"], "a"),
            ("SELECT * means:", ["All columns", "All tables in the folder", "A pie of all apps", "Drop everything"], "a"),
        ],
        [
            ("Nine-step sequence from the notes.",
             "import, connect, cursor, create, insert, commit, select, fetch, close."),
            ("What does * mean?",
             "Every column."),
            ("Two classic bugs.",
             "No commit; forgotten close; SQL string quotes mixed up."),
            ("How do you see the data next run?",
             "It is in school.db — connect again and SELECT."),
        ],
        [
            ("Write a complete program: table students(id, name, marks), insert Ali 85 and Sara 90, print rows. Number the five connection components in comments.",
             "Full working code and output two tuples. Comments: driver/connection/cursor/SQL/database."),
        ],
    )


def _pandas(*_):
    return (
        [
            ("pandas is installed with:", ["pip install pandas", "import pandas (that does not install)", "sqlite3.connect", "plt.show"], "a"),
            ("A DataFrame is:", ["A 2-D labelled table", "A 1-D NAND", "A file mode", "An OSI layer"], "a"),
            ("pd is:", ["The conventional alias", "A primary key", "A stack", "A sprint"], "a"),
            ("read_csv loads:", ["A comma-separated file into a DataFrame", "A PNG", "A .db without SQL", "A Figma file"], "a"),
            ("df.head() shows:", ["First 5 rows", "Last 5 always", "Only dtypes", "Only NaNs"], "a"),
            ("df[\"Total\"]=df.A+df.B is:", ["A vectorised new column", "A Python for-loop of rows you wrote", "A SQL DELETE", "A pie"], "a"),
        ],
        [
            ("Define DataFrame.",
             "2-D table of rows and columns with labels, like Excel/SQL."),
            ("How to build one from a dict (Ali/Sara/Ahmed example).",
             "pd.DataFrame({...}) as in the notes."),
            ("Why head()?",
             "A million rows would flood the screen."),
            ("read_excel extra argument.",
             "sheet_name=\"Sheet1\"."),
        ],
        [
            ("From the Ali/Sara/Ahmed dict, add Total and Average columns and write the exact output table. ★ Golden.",
             "Totals 165,178,148 Averages 82.5,89.0,74.0. Code + output. Mention pip if import fails."),
        ],
    )


def _nan(*_):
    return (
        [
            ("NaN means:", ["Not a Number — missing", "A huge number", "Zero always", "A pie slice"], "a"),
            ("isnull().sum() gives:", ["Count of missing per column", "The mean", "The PK", "The chart type"], "a"),
            ("fillna(mean) :", ["Replaces gaps with the average", "Deletes the column names", "Sorts", "Commits SQL"], "a"),
            ("dropna() by default:", ["Drops rows that contain any NaN", "Drops the whole DataFrame always", "Fills with 0", "Draws a box plot"], "a"),
            ("You should clean NaNs:", ["Before analysing", "After publishing", "Never", "Only in Figma"], "a"),
            ("Filling salary with the mean can:", ["Hide poverty if a CEO is in the data", "Fix ethics", "Create keys", "Route packets"], "a"),
        ],
        [
            ("Three tools: find, fill, drop.",
             "isnull/sum; fillna; dropna."),
            ("Mean of 85, None, 78, 92 for filling.",
             "Known 85+78+92=255/3=85.0."),
            ("When drop is better than fill.",
             "If inventing a value would lie (unknown category, huge outlier)."),
            ("isnull() returns what type of frame?",
             "Booleans True where missing."),
        ],
        [
            ("Given Marks [85, None, 78, 92] and Grade [A,A,None,A]: show isnull sum, fill marks with mean and grade with “Not Assigned”, print the frame. ★ Golden.",
             "Counts 1 and 1. Sara marks 85.0, Ahmed grade Not Assigned. Code + table. Warn about dropna deleting two rows if used first."),
        ],
    )


def _org(*_):
    return (
        [
            ("Tabular form is for:", ["Exact values in rows/columns", "Only a pretty poster", "Only NAND", "Only sprints"], "a"),
            ("A frequency table shows:", ["How many in each bin/range", "The ER diagram", "The OSI stack", "The Figma layers"], "a"),
            ("Most students in the notes’ table scored:", ["70–79", "90–100", "0–10", "Exactly 100"], "a"),
            ("Graphical representation is for:", ["Seeing patterns fast", "Storing PKs", "Compiling C", "Routing"], "a"),
            ("Matplotlib import line:", ["import matplotlib.pyplot as plt", "import pie", "import osi", "import nand"], "a"),
            ("plt.show() :", ["Renders the figure", "Commits SQL", "Closes sqlite", "Starts Figma"], "a"),
        ],
        [
            ("Three organisation methods in the notes.",
             "Table, frequency distribution, graph."),
            ("From the frequency table, how many scored 80+?",
             "4+2=6."),
            ("Steps of a matplotlib figure.",
             "import, figure, plot, labels, title, show."),
            ("Why frequencies for large n?",
             "A list of 2000 marks is unreadable; bins are not."),
        ],
        [
            ("Build a frequency table for 12 marks you invent, then say which graph you would draw and why. Include axis titles.",
             "Bins of 10. Most-filled bin noted. Histogram (numeric distribution) or column if you treat bands as categories — say which and why bars touch or not."),
        ],
    )


def _charts(*_):
    return (
        [
            ("Bar/column charts compare:", ["Discrete categories", "Parts of one whole only", "A single time point of one var as a distribution", "A 5-number summary"], "a"),
            ("Line graphs are for:", ["Trends over time", "Unrelated categories with gaps", "Shares of a budget", "Outliers in five numbers"], "a"),
            ("Pie charts need:", ["Parts of one whole; few slices", "60 slices of 1%", "Time on x", "Two numeric axes of correlation"], "a"),
            ("Histogram bars:", ["Touch (continuous bins)", "Must have large gaps", "Are always time", "Replace the mean"], "a"),
            ("Scatter plots show:", ["Two numeric variables (correlation)", "One category vs colour", "FIFO order", "OSI layers"], "a"),
            ("A box plot shows:", ["Min, Q1, median, Q3, max (+ outliers)", "Only the mean", "Only mode", "Only n"], "a"),
        ],
        [
            ("One-line job of each of the six charts.",
             "Bar categories; line time; pie share; hist distribution; scatter relationship; box spread/outliers."),
            ("Why histogram ≠ bar.",
             "Numeric bins, touching bars vs separate categories."),
            ("When pie fails.",
             "Too many / nearly equal slices."),
            ("Rainfall vs yield?",
             "Scatter; look for positive correlation."),
        ],
        [
            ("Six school questions → pick the chart and a matplotlib function (bar, plot, pie, hist, scatter, boxplot). Justify in one sentence each. ★ Golden.",
             "Enrolment by faculty: bar. Hits by month: plot. Club shares: pie. Heights: hist. Hours vs marks: scatter. Two classes’ spread: boxplot. Unlabelled charts score 0."),
        ],
    )


def _stats(*_):
    return (
        [
            ("Mean of 70,80,90 is:", ["80", "70", "90", "240"], "a"),
            ("Median of 10,15,35,70,95 is:", ["35", "10", "70", "45"], "a"),
            ("Mode of 20,25,20,30,20,25,20 is:", ["20", "25", "30", "7"], "a"),
            ("Range of 120,150,180 is:", ["60", "30", "150", "180"], "a"),
            ("pandas .std() uses:", ["n−1 (sample)", "n always", "2n", "zero"], "a"),
            ("SD is the square root of:", ["Variance", "Mean", "Median", "n"], "a"),
        ],
        [
            ("When mean vs median vs mode.",
             "Mean typical no outliers; median with outliers; mode popular category/value."),
            ("Population variance formula idea.",
             "Mean of squared deviations; ÷n. Sample ÷(n−1)."),
            ("Why square root for SD?",
             "Back to original units."),
            ("Outlier trap with 9×10 and one 1000.",
             "Mean 109 vs median 10."),
        ],
        [
            ("For 4,8,6,10,2 compute mean, median, range, population variance and SD. Then say what pandas std reports. Show every step. ★ Golden.",
             "Sorted 2,4,6,8,10. Mean 6, median 6, range 8. Devs −4,−2,0,2,4 sq 16,4,0,4,16 sum 40. σ²=8, σ=√8≈2.828. pandas 40/4=10, √10≈3.162."),
        ],
    )


def _ml_intro(*_):
    return (
        [
            ("ML, NN and DL are parts of:", ["AI", "OSI layer 1 only", "Access wizards only", "Waterfall only"], "a"),
            ("They all need:", ["Data to learn from", "Only copper cable", "Only primary keys", "Only Figma"], "a"),
            ("The course order is:", ["ML as the idea, NN as a model, DL as deep NNs", "DL then stone tools", "SQL then NAND", "HCI then K-maps"], "a"),
            ("Pakistan’s AI policy is mentioned as:", ["A future/local context", "A Python library", "A chart type", "A file mode"], "a"),
            ("A student mistake is:", ["Treating the three terms as identical", "Giving one example", "Mentioning data", "Mentioning layers"], "a"),
            ("This lecture is the map; later ones:", ["Define each term properly", "Delete the chapter", "Only careers", "Only MVPs"], "a"),
        ],
        [
            ("Place ML, NN, DL in one nested sentence.",
             "DL is a kind of NN which is a way to do ML which is a kind of AI."),
            ("What do they share?",
             "Learn patterns from data instead of only hand-written rules."),
            ("What should an XI/XII answer still include?",
             "A human-responsible, data-quality, bias warning."),
            ("One Pakistani hope from the notes.",
             "Agriculture, health, Urdu NLP, public service — any from the book."),
        ],
        [
            ("Draw a nested diagram AI ⊃ ML ⊃ NN ⊃ DL and write one example at each ring.",
             "AI: chess rules engine. ML: spam filter. NN: digit recognition. DL: speech-to-Urdu. One limit at the DL ring (needs lots of data/compute)."),
        ],
    )


def _ml(*_):
    return (
        [
            ("Machine learning lets a model:", ["Improve from examples, not only hard-coded rules", "Run without data", "Replace all maths", "Ignore errors always"], "a"),
            ("Training data is:", ["Examples used to fit the model", "The final user password", "OSI headers", "Figma frames"], "a"),
            ("A model that memorizes noise is:", ["Overfitting", "Perfect science", "A stack", "A pie"], "a"),
            ("Supervised learning uses:", ["Labels (the right answers)", "No data", "Only unsupervised always", "Only cables"], "a"),
            ("ML in this book is the “trained brain” metaphor for:", ["Mapping inputs to outputs after seeing examples", "A DBMS trigger", "A foreign key", "A sprint"], "a"),
            ("Garbage data yields:", ["Garbage predictions", "Perfect fairness", "O(1) time always", "Free RAM"], "a"),
        ],
        [
            ("Define ML in the book’s words/your own accurate line.",
             "A model that learns from data to produce outputs without being explicitly programmed for every case."),
            ("Give two applications.",
             "Spam; recommendations; marks prediction; vision."),
            ("What is a label?",
             "The known answer attached to a training example."),
            ("One ethical issue.",
             "Bias in the training data is copied into decisions."),
        ],
        [
            ("Explain ML to a principal who wants to predict drop-outs: data, train, test, a risk, a human check.",
             "Past attendance+marks → model → test on held-out year. Risk: punishing poverty correlated with absence. Human counsellor decides, model only flags."),
        ],
    )


def _nn(*_):
    return (
        [
            ("A neural network is inspired by:", ["The brain’s networks of neurons (loosely)", "OSI cables", "Access forms", "Bubble sort"], "a"),
            ("It learns:", ["Weights that turn inputs into outputs", "SQL indexes", "TCP windows", "Figma auto-layout"], "a"),
            ("Simple NNs have:", ["Input, hidden, output layers", "Only a pie", "Only one Excel cell", "No numbers"], "a"),
            ("This is ★: define, then:", ["One diagram + two uses", "Only careers", "Only MVPs", "Only keys"], "a"),
            ("NN vs linear formula:", ["NN can stack non-linear layers for complex patterns", "NN cannot use data", "NN is a queue", "NN is HCI only"], "a"),
            ("Digits on paper are a classic:", ["NN / vision example", "Primary key example", "Waterfall example", "K-map example"], "a"),
        ],
        [
            ("Define neural network.",
             "A computer model of connected units that learns patterns from data, loosely like neurons."),
            ("Three layer types.",
             "Input, hidden, output."),
            ("Two applications.",
             "Image recognition; speech; translation."),
            ("Need for data.",
             "Without enough varied examples the net does not generalise."),
        ],
        [
            ("Draw a 3-layer net for pass/fail from 3 marks. Label input, hidden, output. Explain one training idea in words (weights change). ★ Golden.",
             "3 input nodes, few hidden, 1 output. Training: compare prediction to label, adjust weights. Limit: not a biological brain."),
        ],
    )


def _dl_topic(*_):
    return (
        [
            ("Deep learning uses:", ["Many-layer neural nets", "One if-statement", "Only Access macros", "Only OSI"], "a"),
            ("“Deep” refers to:", ["Many hidden layers", "Deep sea cables only", "Deep stacks in Python only", "Deep queues"], "a"),
            ("DL shines at:", ["Images, speech, complex patterns", "Two-row Excel averages", "Primary keys", "K-maps of 2 vars"], "a"),
            ("A cost of DL is:", ["Lots of data and compute", "No data needed", "No energy use", "Perfect fairness always"], "a"),
            ("DL is a subset of:", ["NN / ML / AI", "HCI only", "SQL only", "SDLC only"], "a"),
            ("Medical imaging in the book is a:", ["DL application", "A foreign key", "A pie of NAND", "A sprint"], "a"),
        ],
        [
            ("Define deep learning.",
             "ML using multi-layer neural networks to learn complex patterns."),
            ("How is it different from a shallow net?",
             "More layers can build higher-level features (edges → shapes → faces)."),
            ("Two applications.",
             "X-ray analysis; voice assistants; translation."),
            ("One Pakistani constraint.",
             "GPUs/data/labels are expensive; start with smaller models."),
        ],
        [
            ("Compare ML vs NN vs DL in a 6-row table (definition, depth, data need, example, limit). 10 marks.",
             "Clear nesting. Example row: spam vs digit net vs speech net. Limits: data, bias, black box, energy."),
        ],
    )


def _nn_parts(*_):
    return (
        [
            ("Input layer:", ["Receives the features", "Always outputs the class", "Stores SQL", "Draws Figma"], "a"),
            ("Hidden layers:", ["Transform features (learned)", "Are optional pie charts", "Are OSI hubs", "Are primary keys"], "a"),
            ("Output layer:", ["Produces the prediction", "Reads the keyboard", "Commits sqlite", "Opens VS Code"], "a"),
            ("Weights are:", ["Strengths of connections, learned from data", "Font weights only", "TCP weights", "Agile story points"], "a"),
            ("Activation functions:", ["Add non-linearity so layers can do more than a straight line", "Sort the array", "Encrypt the disk", "Draw ER"], "a"),
            ("This is ★: a 5-mark wants:", ["Named parts + one sentence each + tiny diagram", "Only the word “brain”", "Only careers", "Only MVPs"], "a"),
        ],
        [
            ("List components of a NN from the notes.",
             "Layers (in/hidden/out), neurons/nodes, weights, activations, (bias)."),
            ("What does a neuron do conceptually?",
             "Weighted sum of inputs, then activation."),
            ("Why more than one hidden layer can help.",
             "Features of features (deep)."),
            ("What is not a component?",
             "A pie chart; a primary key; a sprint."),
        ],
        [
            ("Draw and label input, 2 hidden, output. Annotate weights on two edges. Explain in 4 sentences how a pass/fail signal moves left to right. ★ Golden.",
             "Diagram. Forward pass description. Training mentioned as changing weights, not needed in full backprop maths. One misuse: calling it an exact brain."),
        ],
    )


def _dl_parts(*_):
    return (
        [
            ("DL components include:", ["Deep stacks of layers, lots of data, lots of compute, specialised architectures", "A single if", "A single Access form", "A single NAND"], "a"),
            ("CNNs are often for:", ["Images", "Undo stacks", "Printer queues", "Primary keys"], "a"),
            ("RNNs/transformers often for:", ["Sequences (text/speech)", "Pie charts", "ER diamonds", "K-map groups"], "a"),
            ("GPUs help because:", ["Many multiply-adds in parallel", "They store FKs", "They draw OSI", "They boil water"], "a"),
            ("Pretrained models let you:", ["Reuse features (transfer) when you have less data", "Skip ethics", "Skip labels forever", "Skip HCI"], "a"),
            ("A practical school limit is:", ["Not enough labelled images/GPU", "Too many GPUs always", "Too few ethics issues", "Too much labelled data always"], "a"),
        ],
        [
            ("Name DL-specific components vs a tiny NN.",
             "Depth, specialised layers (conv), big datasets, accelerators, regularisation."),
            ("Why not train ImageNet in a college lab from scratch?",
             "Compute and labelled data; use a pretrained net if anything."),
            ("One architecture name at definition level.",
             "CNN for images / transformer for language — no need for full maths."),
            ("Ethics still apply.",
             "Medical DL that is biased still harms patients."),
        ],
        [
            ("A team wants DL for Urdu speech marks entry. List DL components they need and three reasons to start smaller (ML or rules).",
             "Need: audio data, labels, model, GPU, evaluation. Start smaller: n small, accents, privacy of children’s voices, electricity/cost. Human checks the marks."),
        ],
    )


def _nn_app(*_):
    return (
        [
            ("Vision applications include:", ["Face unlock, medical images, number-plate reads", "Primary keys", "Bubble sort", "OSI ping"], "a"),
            ("Language applications include:", ["Translation, speech-to-text, chatbots", "NAND grouping", "Foreign keys", "Pie charts of cables"], "a"),
            ("Healthcare DL must still:", ["Be checked by clinicians", "Replace doctors unsupervised always", "Ignore bias", "Train on one patient"], "a"),
            ("A local example could be:", ["Urdu voice assistants / crop images", "K-maps of farms", "Access reports of OSI", "Figma of NAND"], "a"),
            ("Recommendation systems are:", ["ML/NN apps (what to watch/buy)", "Queues in printers only", "Stacks of plates only", "ER only"], "a"),
            ("The exam wants:", ["Named field + how NN/DL helps + one risk", "Only the word Pakistan", "Only careers list", "Only math of backprop"], "a"),
        ],
        [
            ("Four application areas from the book.",
             "Vision, speech, health, transport, security, education — any four with a concrete system."),
            ("One risk in health.",
             "False negative on an X-ray; bias against a skin tone."),
            ("One risk in security/surveillance.",
             "Misidentification; privacy."),
            ("Why “application” questions still need a definition line.",
             "1 mark for the term, rest for use+limit."),
        ],
        [
            ("Pick vision, health, language. For each: system, data it needs, a benefit, a harm. 10-mark table.",
             "Face gate / images / fast entry / racism in scores. X-ray / labelled scans / earlier catch / missed cases. Urdu STT / audio / inclusion / leaking class recordings."),
        ],
    )


def _secure(*_):
    return (
        [
            ("Authentication is:", ["Proving who you are", "What you are allowed to do", "Encrypting a disk", "A pie chart"], "a"),
            ("MFA means:", ["More than one factor (password + OTP/phone)", "Many files always", "Many Figma frames", "Many OSI layers"], "a"),
            ("Access control is:", ["What an authenticated user may do", "The login spelling", "A histogram", "A stack"], "a"),
            ("Accountability needs:", ["Actions tied to accounts (logs)", "Shared “class” password", "No names", "Disabled logs"], "a"),
            ("A shared Google-doc with “anyone can edit” fails:", ["Access control / accountability", "Big O", "NAND", "Median"], "a"),
            ("This is ★: define collaboration risk, then:", ["Auth, MFA, access control, tracking", "Only careers", "Only MVPs", "Only charts"], "a"),
        ],
        [
            ("Define authentication vs access control.",
             "Auth: who. Access: what they can do."),
            ("Two MFA factors.",
             "Something you know (password) + have (phone OTP) / are (fingerprint)."),
            ("Why logs?",
             "After a leak you can see who opened the file."),
            ("A class example of bad practice.",
             "One Facebook password on the projector."),
        ],
        [
            ("Design login for a college LMS: password rules, MFA, roles (student/teacher/admin), and what an audit log stores. ★ Golden.",
             "Roles table. Students cannot edit marks. Teachers cannot drop the DB. MFA for admin. Logs: user, time, action, IP. No shared accounts."),
        ],
    )


def _protect(*_):
    return (
        [
            ("Encryption makes data:", ["Unreadable without a key", "Faster to sort", "A primary key", "A pie"], "a"),
            ("A strong password is:", ["Long, unique, not a word+123", "Ali123 for every site", "Written on the monitor", "OTP posted in the group"], "a"),
            ("Backup is:", ["A second copy you can restore", "A stronger GPU", "A prettier UI", "A faster sort"], "a"),
            ("A firewall:", ["Filters traffic in/out", "Encrypts Excel cells one-by-one always", "Sorts arrays", "Draws ER"], "a"),
            ("Ransomware defence includes:", ["Offline/offline-ish backups", "Paying and hoping always", "No updates", "Shared admin"], "a"),
            ("Data protection is about:", ["Confidentiality, integrity, availability (CIA idea)", "Only colours", "Only NAND", "Only sprints"], "a"),
        ],
        [
            ("Four protection techniques from the notes.",
             "Encryption, strong passwords, backup, firewall (and updates, least privilege)."),
            ("Why unique passwords?",
             "One leaked site should not open email+JazzCash."),
            ("3-2-1 backup idea (simple).",
             "More than one copy, not only on the same laptop."),
            ("Firewall vs antivirus in one line.",
             "Firewall: traffic gate. AV: looks for malware on the host (both useful)."),
        ],
        [
            ("A college lab is hit by ransomware. Using encryption, passwords, backup, firewall: what should already have been in place, and what do you do now (without paying if possible)?",
             "Before: backups offline, least admin, updates, firewall. Now: isolate PCs, restore from backup, change passwords, report. Paying is not a syllabus requirement to endorse."),
        ],
    )


def _threats(*_):
    return (
        [
            ("Malware is:", ["Malicious software (virus, worm, trojan, ransomware…)", "A friendly backup", "A primary key", "A caption"], "a"),
            ("Phishing is:", ["Tricking you into giving secrets (fake mail/site)", "A fishing sport in the syllabus", "A sort", "A chart"], "a"),
            ("DoS aims to:", ["Make a service unavailable by flooding it", "Encrypt with your key", "Fix UX", "Normalise tables"], "a"),
            ("A threat is:", ["Anything that can harm system or data", "Only earthquakes", "Only NAND delay", "Only slow Wi-Fi in exams"], "a"),
            ("This is ★: name, one example, one mitigation.",
             ["The 3-mark recipe", "Only the name", "Only Python", "Only Figma"], "a"),
            ("A fake BIEK result link is likely:", ["Phishing", "A K-map", "A stack", "A median"], "a"),
        ],
        [
            ("Define malware, phishing, DoS.",
             "Malware: bad software. Phishing: social trick. DoS: flood to outage."),
            ("One extra threat from the notes (theft/identity).",
             "Data/identity theft — using someone’s CNIC/account."),
            ("A student-level mitigation for phishing.",
             "Check URL, don’t tap unknown SMS, official portal only."),
            ("Why USB etiquette?",
             "Worms travel on sticks."),
        ],
        [
            ("Table of four threats: what it is, a Sindh-college example, a sign, a mitigation. ★ Golden.",
             "Malware, phishing, DoS, theft. Signs: slowness, fake from-addresses, site down, unknown logins. Mitigations: updates/AV, URL check, backups+capacity, MFA."),
        ],
    )


def _id_threat(*_):
    return (
        [
            ("Identifying threats early means:", ["Noticing signs before huge damage", "Waiting for the newspaper", "Formatting C: first", "Posting passwords"], "a"),
            ("A sign of phishing:", ["Urgent ask + odd URL + attachments", "A signed letter from a known office on letterhead you verify", "A slow bubble sort", "A pie"], "a"),
            ("A sign of malware:", ["Sudden slowness, pop-ups, unknown processes", "A labelled histogram", "A foreign key", "A sprint"], "a"),
            ("Unknown login alerts are:", ["Identity/account threat signs", "HCI wireframes", "K-map wraps", "MVP tests"], "a"),
            ("You should:", ["Report to the lab admin, not forward the bait", "Click to check", "Reply with CNIC “to verify”", "Disable logs"], "a"),
            ("False alarms happen; still:", ["Prefer caution on money/password requests", "Always ignore", "Always wipe the DB", "Always pay"], "a"),
        ],
        [
            ("Three signs of phishing.",
             "Urgency, mismatched sender, shortened/odd links, grammar, asks for OTP."),
            ("Three signs of malware.",
             "Slowness, new toolbars, disabled AV, encrypted files + ransom note."),
            ("What is threat identification vs mitigation?",
             "See it vs stop/reduce it (next lecture)."),
            ("A classroom protocol.",
             "Don’t open; screenshot; tell teacher; change password on a clean PC."),
        ],
        [
            ("A student gets SMS “BIEK withhold — click to pay 500”. Walk through identification questions and the safe actions. 8–10 marks.",
             "Who sent? Official channel? URL? Payment on SMS? No. Open biek.edu.pk typed manually. Report. Don’t sideload APK. Inform classmates not to click."),
        ],
    )


def _mitigate(*_):
    return (
        [
            ("Mitigation means:", ["Prevent or reduce harm from threats", "Ignore them", "Rename the threat", "Draw them in Figma"], "a"),
            ("Updates/patches:", ["Close known holes", "Always break Python", "Replace HCI", "Replace ER"], "a"),
            ("Least privilege means:", ["Only the rights you need", "Everyone is admin", "No passwords", "No backups"], "a"),
            ("User education fights:", ["Phishing / bad USB / weak passwords", "Cosmic rays only", "NAND delay", "Median bias only"], "a"),
            ("Incident plan includes:", ["Isolate, preserve, restore, report", "Panic format twice", "Pay first always", "Post OTPs"], "a"),
            ("Technical + human controls together are:", ["Stronger than either alone", "Illegal", "Useless", "Only for banks"], "a"),
        ],
        [
            ("Five mitigation techniques from the book.",
             "Updates, AV, firewall, backup, MFA, training, least privilege, encryption — any five."),
            ("Map one technique to phishing, one to ransomware, one to DoS.",
             "Phishing: training+MFA. Ransomware: backup. DoS: filtering/capacity (high level)."),
            ("What not to do?",
             "Share the malware “to warn friends” as an attachment."),
            ("Why backups must be tested?",
             "A backup you cannot restore is theatre."),
        ],
        [
            ("Write a one-page lab policy: 8 rules that mitigate the threats in 5.4.1. Tag each rule with the threat.",
             "No shared admin (malware/theft); USB scan; official links (phishing); weekly backup (ransomware); firewall; MFA email; report SMS; no pirated cracks. Table."),
        ],
    )


def _equity(*_):
    return (
        [
            ("Equity in digital collaboration means:", ["Fair access to tools and participation, not only “same link for all”", "Giving everyone the identical laptop always without support", "Banning assistive tech", "English-only 4pt PDFs"], "a"),
            ("Equal access includes:", ["Devices, connectivity, language, disability support", "Only the top 10 students", "Only computer labs at midnight", "Only paid apps"], "a"),
            ("A student on 2G with no laptop needs:", ["Low-data options / lab time", "A 4K video lecture only", "A VR headset", "A GPU DL assignment first"], "a"),
            ("Collaboration tools fail equity when:", ["They require an expensive phone feature", "They have captions and Urdu", "They work on a lab PC", "They allow keyboard only"], "a"),
            ("This is ★ for 5.5.1: functions of equity are:", ["Inclusion, fairness of voice, accessible tools, support", "Faster CPUs", "Shorter OSI", "Nicer NAND"], "a"),
            ("A fair group project:", ["Roles + shared docs + offline option", "One member who owns the only laptop does all", "Voice chat only at 2am", "Uncaptioned 1-hour video mandatory"], "a"),
        ],
        [
            ("Define equity vs “everyone got the WhatsApp”.",
             "Same message is not the same opportunity if some have no data bundle or cannot hear."),
            ("Functions of equity (book).",
             "Access, participation, support, accessible design, respect."),
            ("Two practical college moves.",
             "Lab hours; printed alternative; captions; Urdu UI; extra time."),
            ("Link to XI assistive tech.",
             "Screen readers + accessible docs are equity, not charity."),
        ],
        [
            ("A group of 5: one blind, one with no smartphone, one in a village on weekends. Design the collaboration so all can submit. 10 marks ★.",
             "Shared doc that works in lab PCs; keyboard/screen reader; tasks that don’t need 2am Zoom; recorded captions; warden-lab timetable. Assessment not based on who has 4G."),
        ],
    )


def _collab(*_):
    return (
        [
            ("Collaboration tools include:", ["Docs, chat, video, boards, LMS", "Only NAND trainers", "Only K-maps", "Only copper"], "a"),
            ("A good tool match: editing a report together →", ["Shared document", "Only SMS", "Only a pie chart", "Only a stack"], "a"),
            ("Video class needs:", ["Captions + low-bandwidth option", "4K only", "No mute", "Forced camera in hostels always"], "a"),
            ("Permissions on a shared folder are:", ["Access control (Ch 5.3)", "A histogram", "A median", "A sprint"], "a"),
            ("Chat is poor for:", ["Final marks sheets (no audit, easy leak)", "Quick questions", "Memes the teacher banned", "Reminders"], "a"),
            ("Choose tools after:", ["The task and the weakest connection in the group", "The trendiest brand", "The teacher’s cousin’s startup", "The GPU"], "a"),
        ],
        [
            ("Four tool types and a school use.",
             "Docs: assignment. Chat: quick. Video: guest lecture. LMS: submit. Board: brainstorm."),
            ("One security setting per tool.",
             "Docs: restricted link. Video: waiting room. Chat: no OTP sharing."),
            ("One equity setting.",
             "Captions; allow phone upload not only desktop app."),
            ("When not to use public WhatsApp.",
             "CNIC photos, marks, minors’ data."),
        ],
        [
            ("Plan a 1-week group CS project using three tools. For each: purpose, permission, equity tweak, security tweak.",
             "LMS submit; Google Doc restricted; recorded Meet with captions. No personal numbers in the file. Lab slot for the student without data. Table."),
        ],
    )


def _ent(*_):
    return (
        [
            ("An entrepreneur:", ["Turns a problem into a product/service and takes the risk", "Only works in a bank job", "Only draws NAND", "Only writes OSI"], "a"),
            ("Entrepreneurship is the:", ["Process of doing that (test and improve until useful)", "Logo", "First tweet", "Compiler"], "a"),
            ("A student can be entrepreneurial by:", ["A small local solution (notes, tutoring, canteen queue)", "Waiting for a billion-dollar app", "Avoiding all users", "Skipping tests"], "a"),
            ("Risk in the book’s sense includes:", ["It might not work / no one pays", "NAND delay", "Median of 1", "OSI layer 2"], "a"),
            ("Not every shopkeeper in the bazaar is automatically:", ["A digital entrepreneur (needs the digital-age piece)", "A failure", "A programmer", "A UX designer"], "a"),
            ("Ethics still apply:", ["Don’t scam, don’t leak user data", "Scams are clever entrepreneurship", "Spy on classmates", "Copy a bank app’s OTP"], "a"),
        ],
        [
            ("Define entrepreneur and entrepreneurship.",
             "Person vs process: problem → solution → offer to users, with risk."),
            ("A local non-app example.",
             "A photocopy stall that also sells past papers at the gate — still entrepreneurship; digital comes next lecture."),
            ("Why “risk” is in the definition.",
             "You may waste time/money; users may not come."),
            ("One quality of an entrepreneur from class discussion.",
             "Observes problems, tests, iterates — not just dreams."),
        ],
        [
            ("Is a class fellow who sells printed notes an entrepreneur? Use the book definitions, then say what would make it “digital age”.",
             "Yes if they identified a problem and run a small offer. Digital: WhatsApp catalogue, JazzCash, PDF store. Ethics: copyright of the textbook."),
        ],
    )


def _digital_ent(*_):
    return (
        [
            ("Digital-age entrepreneurship uses:", ["Digital tools to start, test, improve, grow", "Only a physical shop with no phone", "Only NAND labs", "Only paper ledgers forever"], "a"),
            ("A WhatsApp business catalogue is:", ["A digital channel", "OSI layer 1 hardware", "A primary key", "A K-map"], "a"),
            ("Low cost of testing online means:", ["You can try an MVP cheaply", "You skip users", "You skip ethics", "You skip problems"], "a"),
            ("This is ★: define + two local examples + one risk.",
             ["The recipe", "Only Silicon Valley names", "Only Python lists", "Only ER"], "a"),
            ("Payment via JazzCash is:", ["Digital infrastructure an entrepreneur can use", "A sort algorithm", "A pie of NAND", "A Figma auto-layout"], "a"),
            ("Copying an app without a real user problem is:", ["Not the book’s method", "Guaranteed success", "A stack", "A median"], "a"),
        ],
        [
            ("Define entrepreneurship in the digital age.",
             "Using digital tools to start/test/improve/grow a business."),
            ("Two tools a student actually has.",
             "Phone camera, WhatsApp, Google Form, Canva, GitHub pages — any two."),
            ("A risk unique to digital.",
             "Cyber fraud, copycats, platform bans, data leak."),
            ("Why local problems beat fake “Uber for X”.",
             "You can talk to users this week (canteen, hostels, tuition)."),
        ],
        [
            ("Take a photocopier stall. List 5 digital upgrades that fit Chapter 6 (not a full app). For each, the problem it tests. ★ Golden.",
             "WhatsApp queue, prepay JazzCash, Google Form for notes list, simple status stories, PDF sample. Each tests demand. Ethics: no pirated books."),
        ],
    )


def _local_ent(*_):
    return (
        [
            ("Table 6.1 is there to show:", ["Ordinary local problems can start digital businesses", "Only US startups count", "Only AI labs count", "Only OSI consultants count"], "a"),
            ("A good exam use of the table is:", ["One example, the problem, the digital twist", "Copying 20 rows unread", "Ignoring Pakistan", "Only listing apps"], "a"),
            ("“Local” means:", ["Your college/bazaar/city, not only Silicon Valley", "Only Karachi DHA", "Only English users", "Only GPUs"], "a"),
            ("If you invent an example it must still:", ["Be realistic and ethical", "Promise billions", "Need NASA", "Need a compiler in C"], "a"),
            ("The table sits after 6.2 because:", ["It illustrates digital-age entrepreneurship", "It replaces prototypes", "It is HCI only", "It is SQL only"], "a"),
            ("A rickshaw app idea should still start from:", ["A real pain (wait, fare fights)", "A random blockchain", "A random NFT", "A random pie"], "a"),
        ],
        [
            ("From memory, give two local digital entrepreneurship examples (book or equivalent).",
             "Food delivery, online tuition, used-books WhatsApp, ride apps, handicraft Instagram — mapped to a problem."),
            ("For one example: problem → digital twist.",
             "Long canteen line → pre-order form."),
            ("Why the board likes local examples.",
             "Shows you understood 6.2, not just American brand names."),
            ("One unethical “business”.",
             "Selling leaked papers; fake job ads."),
        ],
        [
            ("Add three rows in Table 6.1 style for your college: problem, idea, digital tool, first test.",
             "Queue, lost keys, hostel laundry. Tools: form, group, JazzCash. First test: 10 users this week. Ethics column."),
        ],
    )


def _idea(*_):
    return (
        [
            ("A business idea should start from:", ["An observed problem", "A random trendy word", "A stolen brand", "A NAND leftover"], "a"),
            ("The path in the notes is roughly:", ["See problem → idea → test", "Code first, ask never", "Logo first", "GPU first"], "a"),
            ("Talking to five users is:", ["Part of shaping the idea", "A waste", "Only for XII stats", "Only HCI wireframes, never business"], "a"),
            ("A problem with no one who feels it is:", ["Not a business yet", "A unicorn", "A foreign key", "A pie"], "a"),
            ("College is a good lab because:", ["Users are next to you", "Users are on Mars", "There are no problems", "Ethics never apply"], "a"),
            ("Table 6.2-style answers should:", ["Show steps from problem to idea", "Skip to valuation", "Skip to ads", "Skip to hiring 200 people"], "a"),
        ],
        [
            ("List the problem-to-idea steps from the book.",
             "Observe, write the pain, who feels it, current workaround, your twist, first test."),
            ("What is a workaround?",
             "What people already do (e.g. send a younger brother to the canteen)."),
            ("Why write the user in one sentence?",
             "“XI students who miss breakfast because of 8am class” is testable."),
            ("A bad idea statement.",
             "“An AI blockchain metaverse for everything.”"),
        ],
        [
            ("Walk one college problem through the book’s table: problem, who, workaround, idea, first experiment this week.",
             "Full row. Experiment must be doable without an app store (form, poster, WhatsApp). Success metric: n of people who try."),
        ],
    )


def _proto(*_):
    return (
        [
            ("A prototype is:", ["An early model of how it may look/work — not the final product", "The finished mass-produced item", "A database backup", "A pie of revenue"], "a"),
            ("You build it to:", ["Learn, not to impress investors first", "Win a logo contest only", "Replace users", "Skip tests"], "a"),
            ("This is ★: define, purpose, what it is NOT.",
             ["The 5-mark", "Only draw Figma pretty", "Only Python", "Only OSI"], "a"),
            ("A paper phone screen is still a:", ["Prototype (low fidelity)", "MVP already charged", "Compiler", "Firewall"], "a"),
            ("Prototype before code when:", ["The question is “do people understand the idea?”", "You already have 1 million users", "The law froze the spec like waterfall NASA", "You are only drawing NAND"], "a"),
            ("Throwing a prototype away can be:", ["Success (you learned cheaply)", "Shame", "A SQL error", "A median"], "a"),
        ],
        [
            ("Define prototype from the book.",
             "Early model of a product/service/app that shows how it may look or work. Not the final thing."),
            ("Three purposes.",
             "Communicate idea, test with users, find problems early."),
            ("What it is not.",
             "Not the finished product; not necessarily coded; not an MVP (next topics)."),
            ("A non-app prototype.",
             "A cardboard token for a queue system."),
        ],
        [
            ("Design a paper prototype of a “lost-and-found” college app: 3 screens, 3 things you would watch in a test. ★ Golden.",
             "Home, report item, search. Watch: do they find report in 30s, do they understand photos, do they trust privacy. Don’t code yet."),
        ],
    )


def _proto_types(*_):
    return (
        [
            ("Fidelity means:", ["How close the prototype is to the real thing", "How loud it is", "How expensive the CEO is", "How many NAND gates"], "a"),
            ("Low-fidelity is:", ["Paper/sketches, fast, ugly on purpose", "Pixel-perfect branded app", "The production database", "A compiled APK"], "a"),
            ("High-fidelity is:", ["Looks/works closer to final", "A napkin sketch", "A stack of sticky notes only", "A spoken idea only"], "a"),
            ("Students should usually start:", ["Low-fi", "High-fi week 1", "MVP with payments week 1", "TV ads week 1"], "a"),
            ("Mid-fidelity might be:", ["Clickable Figma grey boxes", "The factory mould", "A legal company", "A GPU cluster"], "a"),
            ("A common mistake is:", ["Building high-fi too soon", "Talking to users", "Sketching", "Throwing paper away"], "a"),
        ],
        [
            ("Define the three fidelities.",
             "Low: paper. Mid: simple digital. High: close to real visuals/interactions."),
            ("Cost vs learning.",
             "Low-fi: cheap learning. High-fi: slower, good for look & feel later."),
            ("When high-fi is worth it.",
             "After the flow is right; testing visual trust (a bank app)."),
            ("Which fidelity is a Figma click-through?",
             "Usually mid (or high if fully branded)."),
        ],
        [
            ("For a canteen app, what you test at low, mid, high fidelity. One trap of jumping to high.",
             "Low: flow (order→pay→pickup). Mid: taps. High: colours/photos of food. Trap: arguing hex codes before anyone wants the product."),
        ],
    )


def _proto_cycle(*_):
    return (
        [
            ("The cycle is:", ["Design → build → test → iterate (repeat)", "Build once, never look", "Test on no one", "Advertise first"], "a"),
            ("Iterate means:", ["Change the prototype from what you learned", "Print more logos", "Hire 50 people", "Write OSI parsers"], "a"),
            ("This is ★ because:", ["Entrepreneurship is not one-shot in the book", "Waterfall never iterates even in software", "Users are optional", "Ethics are optional"], "a"),
            ("If tests fail, you:", ["Return to design", "Ship anyway always", "Delete the users", "Change the syllabus"], "a"),
            ("A cycle can be:", ["Hours (paper) not months", "Only yearly", "Only after IPO", "Only in Silicon Valley"], "a"),
            ("Skipping test in the cycle turns it into:", ["Just building in the dark", "HCI gold", "SQL gold", "Big O gold"], "a"),
        ],
        [
            ("Name the four stages.",
             "Design, build, test, iterate."),
            ("What do you carry from test to design?",
             "Notes: where people stuck, what they asked for, what they ignored."),
            ("How many cycles is “enough” for class?",
             "At least two documented rounds."),
            ("Link to Agile from XI.",
             "Same spirit: small loops with feedback. Don’t over-claim they are identical."),
        ],
        [
            ("Document two cycles of a homework-reminder prototype. Each cycle: what you built, who tested, what changed. ★ Golden.",
             "Cycle1 paper: people wanted SMS not email. Cycle2 Figma with SMS mock. Metric: 4/5 could complete. Table."),
        ],
    )


def _proto_act(*_):
    return (
        [
            ("The class activity exists to:", ["Make you build and test a prototype, not only define it", "Replace the exam", "Teach NAND", "Teach OSI"], "a"),
            ("Forgotten deadlines is a:", ["Problem you can prototype", "GPU problem", "Primary key problem", "K-map problem"], "a"),
            ("Five classmates as testers are:", ["Enough for a class test if you watch silently", "A statistically perfect census", "Useless", "A DoS attack"], "a"),
            ("The observer should:", ["Watch, not rescue immediately", "Click for them", "Shout answers", "Grade their fashion"], "a"),
            ("You record:", ["Where they hesitate and what they say", "Only a selfie", "Only the logo poll", "Only Big O"], "a"),
            ("After the activity you still:", ["Iterate", "Ship to Play Store same hour", "Skip ethics", "Skip the write-up"], "a"),
        ],
        [
            ("Summarise the book’s activity scenario.",
             "Students forget homework/tests/items; team prototypes a reminder."),
            ("Three paper screens you would draw.",
             "Today’s tasks; add task; alarm confirm."),
            ("How to test without coding.",
             "Ask a classmate to “use” paper as if it were a phone; you swap sheets."),
            ("One ethical rule in class tests.",
             "Don’t mock testers; don’t collect their personal timetable into a public group."),
        ],
        [
            ("Write a lab report of the activity: idea, 3 screens, 5-user results, 3 changes. Use the cycle words.",
             "Results: 2/5 missed Add. Changes: bigger button, Urdu, confirm. Iterate. Marks-style headings."),
        ],
    )


def _mvp(*_):
    return (
        [
            ("An MVP is:", ["The simplest working version that can test the riskiest assumption", "A paper sketch only", "The full app with every feature", "A logo"], "a"),
            ("Working means:", ["Real users can get the core value (even if ugly/manual)", "It compiles Hello World", "It has 40 screens", "It has AI always"], "a"),
            ("This is ★: contrast with prototype in the next lecture, but here emphasise:", ["Learning from a real offer", "Colours", "NAND", "OSI"], "a"),
            ("A WhatsApp group that actually takes canteen orders is:", ["Closer to MVP than a Figma only", "Not digital", "A stack", "A pie"], "a"),
            ("Building extra features first is:", ["The usual MVP failure", "Required", "Agile gold always", "HCI gold always"], "a"),
            ("The goal is to learn:", ["Whether people use/pay, cheaply", "Whether the CEO likes purple", "Whether Big O is n²", "Whether ER is 3NF"], "a"),
        ],
        [
            ("Define MVP from the book.",
             "Minimum Viable Product: simplest working version with only essential features, used to learn from real users."),
            ("What “viable” means.",
             "Someone can complete the core job (order food, book notes)."),
            ("What “minimum” means.",
             "Strip extras (reviews, AI, dark mode) until the core is tested."),
            ("One example.",
             "Google Form + JazzCash + pickup window, before an app."),
        ],
        [
            ("Design an MVP for “notes exchange” that you could run next week without an app store. List in/out features and the learning question. ★ Golden.",
             "In: list of notes, request, pickup. Out: chat, ratings, payments maybe later. Question: will 20 students actually exchange? How you measure."),
        ],
    )


def _proto_mvp(*_):
    return (
        [
            ("A prototype mainly:", ["Shows/tests the design", "Takes real payments at scale always", "Replaces the company", "Is the beachhead"], "a"),
            ("An MVP mainly:", ["Delivers the core working offer to real users to learn", "Is always paper", "Is always high-fi Figma only", "Has every feature"], "a"),
            ("You can have a prototype that is:", ["Not working software", "Already the full product", "A DBMS", "An OSI stack"], "a"),
            ("You should not call a clickable mock the:", ["MVP (if nobody can actually complete the job)", "Prototype", "Wireframe", "Test"], "a"),
            ("Order often is:", ["Need → prototype → MVP → later product", "MVP → ignore users → prototype", "IPO → problem", "GPU → problem"], "a"),
            ("Exam 5-mark: table of:", ["Purpose, working?, users, fidelity, example", "Only definitions swapped", "Only careers", "Only Python"], "a"),
        ],
        [
            ("Four differences prototype vs MVP.",
             "Purpose design vs learning from a real offer; may not work vs must work; testers vs customers; cheap fake vs minimum real."),
            ("Can an MVP look ugly?",
             "Yes — viability ≠ beauty."),
            ("Can a prototype be digital?",
             "Yes (Figma) — still not MVP if it doesn’t deliver the job."),
            ("One sentence you should memorise.",
             "Prototype answers “do they understand it?”; MVP answers “do they use it?”."),
        ],
        [
            ("Table + one paragraph: for the canteen idea, what is the prototype and what is the MVP. Do not mix them.",
             "Prototype: paper/Figma order flow. MVP: form that cooks actually receive and food is collected. Learning: % of orders picked up."),
        ],
    )


def _risk(*_):
    return (
        [
            ("An assumption is:", ["Something you believe but have not tested", "A proven law", "A primary key", "A NAND identity"], "a"),
            ("The riskiest assumption is:", ["The one that, if false, kills the idea", "The logo colour", "The font", "The folder name"], "a"),
            ("For a canteen pre-order, a typical risky one is:", ["Students will order ahead / kitchen will honour it", "The app icon gradient", "The CEO title", "The NAND count"], "a"),
            ("You test it with:", ["The smallest experiment (often the MVP)", "A 2-year build", "A press conference", "A GPU cluster"], "a"),
            ("If the risky assumption fails you:", ["Pivot or stop cheaply", "Add more features", "Raise a huge team first", "Print brochures"], "a"),
            ("Not every assumption is equal:", ["UI colour is rarely the killer", "Colour is always the killer", "Fonts kill more than demand", "OSI layers kill demand"], "a"),
        ],
        [
            ("Define assumption vs riskiest assumption.",
             "Belief untested; the one that must be true or the business dies."),
            ("How to find it.",
             "Ask: if this is false, is there still a business? Demand, payment, delivery are usual."),
            ("A cheap test of “will they pay”.",
             "Take 10 JazzCash orders before building an app."),
            ("A cheap test of “kitchen can cope”.",
             "One item, one hour, one stall."),
        ],
        [
            ("List 5 assumptions of a hostel laundry service. Star the riskiest and write a 3-day test with a success number.",
             "Assumptions: students hate queues; will bag clothes; will pay 50 Rs; dhobi agrees; no theft. Riskiest: pay or dhobi capacity. Test: 10 bags, 50 Rs, 70% return. If <3 bags, stop."),
        ],
    )


def _mvp_dev(*_):
    return (
        [
            ("Developing an MVP means:", ["Choosing only essential features and a way to deliver them", "Hiring 40 engineers first", "Designing 12 themes", "Writing the TOS of a unicorn"], "a"),
            ("A feature is essential if:", ["The core job fails without it", "A competitor has it", "It is AI", "It is animated"], "a"),
            ("Manual-behind-the-scenes is allowed if:", ["The user still gets the job done (concierge MVP)", "You lie that it is fully automatic forever", "You skip users", "You skip ethics"], "a"),
            ("Time-box the build to:", ["Days/weeks, not years", "A decade", "Until perfect", "Until the logo shines"], "a"),
            ("You still need:", ["A way to measure the learning", "No metric", "Only likes", "Only press"], "a"),
            ("Extra features before the core works are:", ["Waste", "Professionalism", "Required by BIEK", "HCI law"], "a"),
        ],
        [
            ("Steps to develop an MVP from the notes.",
             "Core job, essential features, drop extras, pick tools, build, measure."),
            ("Concierge MVP meaning.",
             "You perform the service by hand (WhatsApp) while pretending the “product” exists — to test demand."),
            ("Tools a student can use.",
             "Forms, sheets, WhatsApp, JazzCash, a landing page."),
            ("One ethics line.",
             "If you take money, deliver or refund; don’t ghost testers."),
        ],
        [
            ("Turn the notes-exchange idea into an MVP plan: features in/out, tools, 7-day schedule, metric, kill-criteria.",
             "In: list+request. Out: chat/AI. Tools: sheet+group. Metric: 10 completed exchanges. Kill if <2. Schedule table."),
        ],
    )


def _canteen(*_):
    return (
        [
            ("The canteen case is there to:", ["Show a full MVP story on a local problem", "Teach NAND", "Teach OSI", "Teach ER only"], "a"),
            ("The problem is:", ["Queues / food running out", "GPUs", "Primary keys", "Figma auto-layout"], "a"),
            ("A sensible MVP is:", ["Pre-order a few items for pickup, not a full restaurant OS", "Drone delivery in week 1", "AI chefs", "Blockchain loyalty"], "a"),
            ("The kitchen is a:", ["User/constraint you must test", "A pie", "A stack", "An OSI hub"], "a"),
            ("If nobody pre-orders, the idea:", ["Failed the risky assumption — good you learned cheap", "Needs more gradients", "Needs a CEO", "Needs C++"], "a"),
            ("Write the case as:", ["Problem, users, assumption, MVP, test, result, next", "Only the logo", "Only careers", "Only Python lists"], "a"),
        ],
        [
            ("Retell the case in 5 bullets.",
             "Queue; students+staff+cooks; assume pre-order helps; form/WhatsApp MVP; measure wait/orders; iterate."),
            ("Two user groups with different needs.",
             "Students (speed); kitchen (simple tickets, not 40 modifiers)."),
            ("A metric.",
             "Orders completed; average wait; food wasted."),
            ("A next step if it works.",
             "Add payment; then maybe an app."),
        ],
        [
            ("Write the canteen case as a 10-mark structured answer with a tiny flow diagram (order → kitchen → pickup).",
             "Headings as above. Diagram three boxes. One risk: kitchen overwhelmed at 10:55. Mitigation: cap orders. Ethics: allergies."),
        ],
    )


def _mvp_test(*_):
    return (
        [
            ("Testing an MVP means:", ["Real users, real core task, collect numbers and comments", "Only your friends saying “cool logo”", "Only the teacher’s mark", "Only a unit test of Python"], "a"),
            ("Vanity metrics are:", ["Likes with no usage", "Completed jobs", "Repeat orders", "Time to complete"], "a"),
            ("You want both:", ["Numbers and quotes", "Only numbers", "Only vibes", "Only press"], "a"),
            ("A failed test is useful when:", ["You write what you will change or stop", "You hide it", "You add features at random", "You buy ads"], "a"),
            ("Sample of 5–20 users is:", ["OK for class MVPs if honest", "A national census", "Useless always", "A DoS"], "a"),
            ("Don’t help the user in the test if you are measuring:", ["Whether the offer is understandable/usable", "Kindness in general life", "SQL skill", "NAND skill"], "a"),
        ],
        [
            ("What to measure (book + good practice).",
             "Did they finish? Time? Would they repeat? Pay? Quotes of confusion."),
            ("How to collect.",
             "Tally sheet + 3 interview questions after."),
            ("Bias: testing only your friends.",
             "They are too nice — include one stranger in the line."),
            ("Then what?",
             "Iterate the MVP (or the assumption)."),
        ],
        [
            ("Write a test plan for the canteen MVP: n, tasks, 3 metrics, 3 questions, pass/fail thresholds, ethics (food safety).",
             "n=15 lunch buyers. Task: order and collect. Metrics: % complete, wait, errors. Questions: would you do this tomorrow? Thresholds: 70% complete. Don’t poison anyone; allergens."),
        ],
    )


def _beach(*_):
    return (
        [
            ("A beachhead market is:", ["A small focused first group of users", "The whole country on day 1", "Random Twitter", "Every age/city/income at once"], "a"),
            ("You pick them because:", ["They feel the pain strongly and you can reach them", "They are richest always", "They are abroad always", "They hate the product"], "a"),
            ("This is ★: define, why small, one example.",
             ["The recipe", "Only the D-Day story without CS", "Only Python", "Only ER"], "a"),
            ("XI CS students in one college as first users of a notes app is a:", ["Beachhead", "Global TAM", "OSI layer", "NAND net"], "a"),
            ("After the beachhead works you:", ["Expand to the next similar group", "Immediately advertise on TV nationwide", "Quit", "Rewrite in assembly"], "a"),
            ("A beachhead that is too broad is:", ["Hard to test and to talk to", "Ideal", "Required", "A median"], "a"),
        ],
        [
            ("Define beachhead market.",
             "Small, focused first users with a clear need, likely to try."),
            ("Why not “all Pakistan” first?",
             "You cannot learn; message becomes vague; cost explodes."),
            ("Example from college.",
             "Hostel Block B, not all Karachi youth."),
            ("How it links to MVP.",
             "The MVP is aimed at that beachhead, not every imaginary user."),
        ],
        [
            ("For a canteen pre-order, choose a beachhead (who, where, when), why they are best, and who you refuse at first. ★ Golden.",
             "XI 10:00 break, one stall. They queue worst. Refuse staff catering and evening shift until the kitchen process works. Success: 20 repeating students."),
        ],
    )


def _project(*_):
    return (
        [
            ("The student project should be:", ["Small, local, possible in class time", "A full bank app", "A new OS", "A satellite"], "a"),
            ("It should include:", ["Problem, idea, prototype/MVP, test, ethics", "Only a logo", "Only careers", "Only a Python hello"], "a"),
            ("Ethical use of digital tools means:", ["Consent, no harassment, no leaked data, honest claims", "Scrape classmates’ photos", "Fake testimonials", "Spam the college group"], "a"),
            ("The rubric rewards:", ["A real test, not a fantasy pitch deck", "Unicorn valuation", "English poetry only", "NAND counts"], "a"),
            ("Safe tools:", ["Forms/docs you have a right to use; no piracy", "Cracked Adobe", "Stolen question papers", "Phishing kits"], "a"),
            ("6.15 and 6.16 together remind you:", ["Build something small and don’t harm people", "Skip users", "Skip tests", "Skip the write-up"], "a"),
        ],
        [
            ("List the project pieces the book wants.",
             "Team, local problem, idea, prototype, MVP or test, beachhead, results, ethics, reflection."),
            ("Two ethical rules for digital tools.",
             "Permission for photos; no copyright theft; no unsafe personal data in public sheets."),
            ("What “possible” means.",
             "You can test this week with people you can walk to."),
            ("A fail on ethics even if the idea is clever.",
             "Secretly recording students in the canteen."),
        ],
        [
            ("Write a one-page project proposal that would score well: 8 headings including ethics and a 7-day test. Invent a local idea that is not the canteen copy-paste.",
             "e.g. lab-equipment booking. Headings match rubric. Ethics: no shame list of late students on a public wall. Metric: 10 bookings honoured."),
        ],
    )
