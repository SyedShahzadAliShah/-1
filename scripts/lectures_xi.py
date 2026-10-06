from lecture_helpers import (
    array,
    board,
    bullet,
    chapter,
    chips,
    code,
    cols,
    flow,
    formula,
    gates,
    h2,
    kmap,
    layers,
    lecture,
    note,
    steps,
    table,
    title,
)


def chapters():
    return [
        chapter("xi-ch1", 1, "Computer Systems", [
            lecture("xi-digital", "Discrete, analog, and digital", True, [
                board(
                    """
                    A quantity is discrete when you can count it in separate steps, like how many
                    students are sitting in this room. A quantity is continuous when it may fall
                    anywhere between two values, like the temperature of the room. Computers are
                    built for the discrete side. They store symbols, not a smooth curve.
                    """,
                    title("Discrete and continuous"),
                    cols(
                        "Discrete",
                        ["Counted in steps", "Students in a class", "A switch: on or off"],
                        "Continuous",
                        ["Any value in between", "Temperature", "The loudness of a voice"],
                    ),
                    note("If you can list the allowed values, the quantity is discrete."),
                ),
                board(
                    """
                    An analog signal follows the continuous quantity. It can rise and fall smoothly,
                    like a microphone voltage that copies a voice. A digital signal jumps between
                    fixed levels. In this course those levels are 0 and 1. A digital system is any
                    device that stores and processes those discrete values.
                    """,
                    title("Analog signal and digital signal"),
                    cols(
                        "Analog",
                        ["Smooth change", "Many possible levels", "A dimmer, not a switch"],
                        "Digital",
                        ["Sudden jumps", "Usually 0 and 1", "A light that is on or off"],
                    ),
                    note("Noise can bend an analog wave. A digital 0 or 1 can be restored.", "green"),
                ),
                board(
                    """
                    Why do computers prefer bits? A bit is one binary digit, either 0 or 1. With
                    eight bits you can already make 256 different patterns. Pictures, letters, and
                    sound are all turned into patterns of bits before the processor works on them.
                    The processor then uses logic, not a sliding needle.
                    """,
                    title("A digital system uses bits"),
                    chips("Bit: 0 or 1", "Byte: 8 bits", "Patterns stand for data"),
                    steps(
                        "Sense the real world",
                        "Convert the measurement to bits",
                        "Process the bits with logic",
                        "Convert the result back if a person must see it",
                    ),
                ),
            ]),
            lecture("xi-boolean", "Boolean algebra", True, [
                board(
                    """
                    Boolean algebra is the arithmetic of 0 and 1. There is no digit 2. The three
                    basic operations are AND, OR, and NOT. AND gives 1 only when every input is 1.
                    OR gives 1 when at least one input is 1. NOT flips a single bit.
                    """,
                    title("Boolean operations"),
                    formula("AND   OR   NOT"),
                    gates("AND", "OR", "NOT"),
                    note("Say AND as both, OR as either, and NOT as the opposite."),
                ),
                board(
                    """
                    Let us test a door alarm. Let D mean the door is open, and N mean it is night.
                    The alarm should ring only when the door is open and it is night. That sentence
                    is D AND N. If the door is shut, D is 0, so the AND is 0 even at night.
                    """,
                    title("Worked example: night alarm"),
                    table(
                        ["D", "N", "D AND N"],
                        [["0", "0", "0"], ["0", "1", "0"], ["1", "0", "0"], ["1", "1", "1"]],
                    ),
                    note("Change the rule to door open or window open and you need OR, not AND.", "blue"),
                ),
                board(
                    """
                    A few laws let you rewrite an expression without changing its meaning.
                    Order does not matter for AND or OR, so A AND B equals B AND A. De Morgan's
                    laws are the ones exams love. NOT of A AND B equals NOT A OR NOT B. NOT of
                    A OR B equals NOT A AND NOT B. You break the bar and you swap AND with OR.
                    """,
                    title("Laws you will reuse"),
                    formula("NOT (A AND B) = NOT A OR NOT B"),
                    bullet("NOT (A OR B) = NOT A AND NOT B"),
                    note("Break the bar, then swap AND and OR.", "green"),
                ),
            ]),
            lecture("xi-truth", "Truth tables and basic gates", True, [
                board(
                    """
                    A truth table lists every possible input and the matching output. Two inputs
                    give four rows, because each input can be 0 or 1. Three inputs give eight rows.
                    You fill the output column from the rule, one row at a time. Never skip a row.
                    """,
                    title("How to build a truth table"),
                    steps(
                        "Count the inputs",
                        "Make 2 to the power of that count rows",
                        "List inputs in binary counting order",
                        "Compute the output for each row",
                    ),
                    note("2 inputs: 4 rows. 3 inputs: 8 rows. 4 inputs: 16 rows."),
                ),
                board(
                    """
                    Here are the three basic gates side by side. AND is 1 only on the last row.
                    OR is 0 only on the first row. NOT has one input, so it has two rows, and the
                    output is the opposite of the input. Learn these three tables by heart before
                    you meet the other gates.
                    """,
                    title("AND, OR, and NOT"),
                    table(
                        ["A", "B", "AND", "OR"],
                        [["0", "0", "0", "0"], ["0", "1", "0", "1"], ["1", "0", "0", "1"], ["1", "1", "1", "1"]],
                    ),
                    gates("AND", "OR", "NOT"),
                ),
                board(
                    """
                    A common mistake is to treat OR as exclusive, as if both inputs cannot be 1.
                    In Boolean algebra, OR is still 1 when both inputs are 1. The gate that is 1
                    only when the inputs differ has another name, XOR, and we will draw it next.
                    Also remember that NOT applies to one value, not to a pair.
                    """,
                    title("Mistakes that cost marks"),
                    note("OR allows both inputs to be 1. It is not the either-but-not-both gate.", "red"),
                    note("Write every row. A missing row is a missing mark in the exam.", "green"),
                ),
            ]),
            lecture("xi-more-gates", "NAND, NOR, XOR, and XNOR", True, [
                board(
                    """
                    NAND is AND followed by NOT. NOR is OR followed by NOT. You can spot them on
                    a diagram by the little bubble on the output. NAND is 0 only when both inputs
                    are 1. NOR is 1 only when both inputs are 0. The bubble means invert the result.
                    """,
                    title("Universal gates"),
                    gates("NAND", "NOR"),
                    table(
                        ["A", "B", "NAND", "NOR"],
                        [["0", "0", "1", "1"], ["0", "1", "1", "0"], ["1", "0", "1", "0"], ["1", "1", "0", "0"]],
                    ),
                ),
                board(
                    """
                    NAND is called universal because you can build AND, OR, and NOT from NAND
                    gates alone. The same is true of NOR. A NOT is a NAND with both inputs tied
                    to the same wire. Designers like a universal gate because the factory can
                    stock one part and still make any Boolean function.
                    """,
                    title("Why universal matters"),
                    steps(
                        "Tie both NAND inputs together to make NOT",
                        "NAND the inputs, then NOT that result, to make AND",
                        "NOT each input, then NAND those results, to make OR",
                    ),
                    note("If a question says use only NAND, do not sneak in an AND gate.", "red"),
                ),
                board(
                    """
                    XOR is 1 when the inputs are different. XNOR is 1 when the inputs are the same.
                    XNOR is XOR with a bubble. Use XOR when you mean one or the other, but not both.
                    A simple example is a stair light with two switches: the lamp toggles when
                    either switch changes, which is exactly XOR.
                    """,
                    title("XOR and XNOR"),
                    gates("XOR", "XNOR"),
                    table(
                        ["A", "B", "XOR", "XNOR"],
                        [["0", "0", "0", "1"], ["0", "1", "1", "0"], ["1", "0", "1", "0"], ["1", "1", "0", "1"]],
                    ),
                    note("Different bits: XOR is 1. Matching bits: XNOR is 1."),
                ),
            ]),
            lecture("xi-expressions", "Expressions, minterms, and diagrams", True, [
                board(
                    """
                    A logic expression is a written form of a circuit. A AND B OR C needs care,
                    because AND is usually done before OR, just as multiplication comes before
                    addition. When you are unsure, add parentheses. The expression and the diagram
                    must describe the same truth table.
                    """,
                    title("From words to an expression"),
                    formula("(A AND B) OR C"),
                    bullet("AND binds more tightly than OR"),
                    bullet("Parentheses remove doubt"),
                    note("Build the truth table if two students disagree about an expression.", "blue"),
                ),
                board(
                    """
                    A minterm is a product, an AND, that is 1 for exactly one input row. For two
                    variables the minterm of row 1 0 is A AND NOT B. A maxterm is a sum, an OR,
                    that is 0 for exactly one row. Sum of minterms lists the rows where the
                    function is 1. Product of maxterms lists the rows where it is 0.
                    """,
                    title("Minterms and maxterms"),
                    table(
                        ["A", "B", "Minterm", "F"],
                        [["0", "0", "NOT A AND NOT B", "0"], ["0", "1", "NOT A AND B", "1"], ["1", "0", "A AND NOT B", "0"], ["1", "1", "A AND B", "1"]],
                    ),
                    note("F is 1 on rows 0 1 and 1 1, so F = (NOT A AND B) OR (A AND B), which simplifies to B."),
                ),
                board(
                    """
                    A logic diagram draws the gates and the wires. Read it from inputs on the left
                    to the output on the right. Each bubble is a NOT. To check a diagram, pick one
                    input row, push the bits through each gate, and see if the output matches the
                    table. That trace is the same skill you will use later on algorithms.
                    """,
                    title("Reading a logic diagram"),
                    flow("Inputs A and B|io", "AND gate|process", "NOT bubble|process", "Output|term"),
                    note("A bubble on the output of AND makes that gate a NAND.", "green"),
                ),
            ]),
            lecture("xi-kmap", "Karnaugh maps", True, [
                board(
                    """
                    A Karnaugh map, or K-map, is a truth table drawn so that neighbors differ by
                    only one bit. That layout lets you circle groups of 1s. Each group must hold
                    1, 2, 4, or 8 cells, a power of two, and the group must be a rectangle. The
                    circled group becomes one simpler term.
                    """,
                    title("Why a K-map helps"),
                    steps(
                        "Draw the map in Gray-code order",
                        "Fill 1 where the function is 1",
                        "Circle the largest legal groups",
                        "Write one term for each circle",
                    ),
                    note("Groups of 3 are illegal. 3 is not a power of 2.", "red"),
                ),
                board(
                    """
                    Fill this map for F equals A OR B. The cell A 0 B 0 is 0. Every other cell is 1.
                    The right column, where B is 1, is a group of two. That column depends only on B.
                    The bottom row, where A is 1, is another group of two. That row depends only on A.
                    So the simplified expression is A OR B, which matches the story we started with.
                    """,
                    title("Simplify A OR B"),
                    kmap(["0", "1", "1", "1"], hi=[1, 3], caption="A \\ B"),
                    formula("F = A OR B"),
                    note("Overlapping groups are allowed. A cell may sit in two circles."),
                ),
                board(
                    """
                    Read a group by asking which variable does not change inside it. If B is 1 in
                    every cell of the circle, write B. If A is 0 in every cell, write NOT A. Drop
                    any variable that is 0 in some cells of the group and 1 in others. Then OR the
                    terms from each circle together.
                    """,
                    title("Reading a circle"),
                    chips("Same variable stays", "Changing variable is dropped", "OR the circles"),
                    note("Check the answer by expanding it back into a truth table.", "green"),
                ),
            ]),
            lecture("xi-logisim", "A first circuit in Logisim", False, [
                board(
                    """
                    Logisim Evolution is a program where you place gates and watch them work.
                    You do not need a soldering iron. The canvas is your breadboard. Input pins
                    are switches. An output pin or an LED shows the result. Wiring is just a line
                    you drag from one port to another.
                    """,
                    title("What the simulator is for"),
                    chips("Input pin", "Gate", "Wire", "Output or LED"),
                    note("Save the circuit before you poke the switches, so a mistake is easy to undo.", "blue"),
                ),
                board(
                    """
                    Build the night alarm. Place an AND gate. Add two input pins and name them
                    Door and Night. Add one output pin named Alarm. Draw a wire from each input
                    to the AND gate, and from the AND gate to the output. Then choose the poke
                    tool and click the inputs. The alarm must light only when both pins are 1.
                    """,
                    title("Build D AND N"),
                    flow("Door pin|io", "AND gate|process", "Alarm output|term"),
                    steps("Place the AND gate", "Add two inputs and one output", "Wire the ports", "Poke both inputs on"),
                ),
                board(
                    """
                    If the LED stays dark, check three things. Is the wire actually touching the
                    port, or is it only nearby? Is the poke tool selected, or are you still in
                    the select tool? Did you tie the wrong gate, an OR instead of an AND? Change
                    one thing, poke again, and compare with the truth table on paper.
                    """,
                    title("When the circuit misbehaves"),
                    note("A floating input is not a reliable 0. Connect every input pin.", "red"),
                    note("The simulator agrees with the truth table, or the wiring is wrong.", "green"),
                ),
            ]),
            lecture("xi-sdlc", "Waterfall, Agile, and the life cycle", True, [
                board(
                    """
                    The software development life cycle is the path from a need to a program people
                    can use, and then to keeping that program healthy. The usual stops are
                    requirements, design, building, testing, release, and maintenance. Requirements
                    say what the program must do. Design says how the parts fit. Testing asks
                    whether it really does what was promised.
                    """,
                    title("The life cycle"),
                    steps(
                        "Requirements: what problem?",
                        "Design: how will it be built?",
                        "Implementation: write it",
                        "Testing: try to break it",
                        "Deployment: people start using it",
                        "Maintenance: fix and improve",
                    ),
                ),
                board(
                    """
                    Waterfall walks those stops once, in order. You finish requirements before
                    design, and design before coding. It is easy to explain and easy to grade,
                    but a mistake found at the end is expensive, because you rarely walk back.
                    Agile repeats a short loop. A team builds a small working slice, shows it to
                    the user, and changes the next slice. Change is expected, not a failure.
                    """,
                    title("Waterfall and Agile"),
                    cols(
                        "Waterfall",
                        ["One pass down the list", "Stable requirements", "Late working software"],
                        "Agile",
                        ["Short repeated cycles", "Requirements may change", "Working software early"],
                    ),
                ),
                board(
                    """
                    Choose waterfall when the rules are fixed and well known, such as a program
                    that must follow a published exam-result formula. Choose Agile when the school
                    is still discovering what the attendance app should do. A case study answer
                    should name the model and give the reason. The name alone is not enough.
                    """,
                    title("Which model fits?"),
                    note("Fixed rules and a heavy cost of change: waterfall.", "blue"),
                    note("Unclear needs and a user you can talk to every week: Agile.", "green"),
                ),
            ]),
            lecture("xi-osi", "OSI and TCP/IP", True, [
                board(
                    """
                    The OSI model splits network communication into seven layers so each layer has
                    one job. From the top they are Application, Presentation, Session, Transport,
                    Network, Data Link, and Physical. A memory line is: All People Seem To Need
                    Data Processing. The physical layer moves bits on a wire or through the air.
                    The application layer is the program you actually touch, such as a browser.
                    """,
                    title("Seven OSI layers"),
                    layers(
                        "7 Application: the program the user sees",
                        "6 Presentation: format and encryption",
                        "5 Session: start and end a conversation",
                        "4 Transport: delivery between programs",
                        "3 Network: addressing and routing",
                        "2 Data link: hop to the next device",
                        "1 Physical: bits on the medium",
                    ),
                ),
                board(
                    """
                    TCP/IP is the model the internet actually grew up with. It has four layers.
                    Application covers the top three OSI layers. Transport still moves data between
                    programs. Internet matches the OSI network layer and finds a path using IP
                    addresses. Network access covers the data link and the physical medium. You
                    should be able to place a job in both models.
                    """,
                    title("TCP/IP beside OSI"),
                    cols(
                        "TCP/IP",
                        ["Application", "Transport", "Internet", "Network access"],
                        "Matches OSI",
                        ["Layers 5 to 7", "Layer 4", "Layer 3", "Layers 1 and 2"],
                    ),
                    note("A router works at the network, or internet, layer. A switch works at the data link layer.", "green"),
                ),
                board(
                    """
                    Suppose you send a photo to a classmate. The application prepares the file.
                    Transport chops it into segments and numbers them. The internet layer adds
                    addresses and chooses a route. The link and physical layers carry frames and
                    bits to the next device. On the far side the layers unwrap the photo in reverse.
                    """,
                    title("One photo, many layers"),
                    flow("Photo in the app|io", "Numbered segments|process", "IP addresses|process", "Bits on the wire|term"),
                    note("Higher layers depend on lower layers. They do not replace them.", "red"),
                ),
            ]),
        ]),
        chapter("xi-ch2", 2, "Computational Thinking and Algorithms", [
            lecture("xi-thinking", "Decomposition, patterns, abstraction", True, [
                board(
                    """
                    Computational thinking is how you prepare a problem before you write steps.
                    Decomposition breaks a big problem into smaller problems you can solve one at
                    a time. Pattern recognition notices what repeats. Abstraction hides details
                    that do not change the decision. Together they stop you from coding the whole
                    world on the first line.
                    """,
                    title("Three thinking tools"),
                    chips("Decomposition", "Pattern recognition", "Abstraction"),
                    note("An algorithm comes after these tools, not instead of them."),
                ),
                board(
                    """
                    Take a school morning. Decomposition gives: wake, dress, breakfast, travel,
                    attend class. Pattern recognition notices that Monday to Friday share the same
                    travel, while Sunday does not. Abstraction for a late-slip program keeps the
                    arrival time and the bell time, and throws away the color of the bag. The bag
                    color never decides whether you are late.
                    """,
                    title("A morning, pulled apart"),
                    steps("List the small tasks", "Mark what repeats", "Cross out details that do not affect the result"),
                    note("If a detail cannot change the output, leave it out of the model.", "green"),
                ),
                board(
                    """
                    A useful check is to explain the problem in one sentence that names the inputs
                    and the output. Late slip: inputs are bell time and arrival time, output is
                    late or on time. If your sentence still mentions breakfast, you have not
                    abstracted yet. Decomposition without abstraction leaves you with a pile of
                    facts and no decision.
                    """,
                    title("Input and output in one sentence"),
                    formula("Inputs -> decision -> output"),
                    note("Write that sentence before you draw a flowchart.", "blue"),
                ),
            ]),
            lecture("xi-algorithm", "Algorithms and pseudocode", True, [
                board(
                    """
                    An algorithm is a finite list of clear steps that always finishes and produces
                    a result. A recipe can be an algorithm if the amounts and the order are exact.
                    Pseudocode writes those steps in plain language that looks a little like code,
                    but it is not tied to Python spelling. Its job is to show the idea.
                    """,
                    title("Algorithm versus pseudocode"),
                    cols(
                        "Algorithm",
                        ["The method itself", "Must finish", "Must be precise"],
                        "Pseudocode",
                        ["One way to write it", "Plain words are allowed", "Not run by Python"],
                    ),
                ),
                board(
                    """
                    Here is pseudocode for the larger of two marks. Read A. Read B. If A is greater
                    than or equal to B, output A, otherwise output B. Stop. Every path reaches stop.
                    There is no step that says do the usual thing. Words like usual are not allowed,
                    because two readers would guess different actions.
                    """,
                    title("Larger of two marks"),
                    flow("Start|term", "Read A and B|io", "A >= B ?|decision", "Output the larger|process", "Stop|term"),
                    note("One input row, one path. Ambiguous verbs fail the clarity test.", "red"),
                ),
                board(
                    """
                    You can translate good pseudocode into Python later, almost line for line.
                    You should not start in Python if you do not yet know the steps. First make
                    the algorithm correct on paper with a tiny example, such as marks 70 and 85.
                    The output must be 85. Then code it.
                    """,
                    title("Paper first, then Python"),
                    steps("Write the steps", "Trace a tiny example by hand", "Fix the steps", "Then open the editor"),
                ),
            ]),
            lecture("xi-sort", "Bubble sort and selection sort", True, [
                board(
                    """
                    A sorting algorithm puts items in order. Bubble sort walks along the list and
                    swaps any pair of neighbors that is out of order. Large values bubble toward
                    the end. Selection sort is different. It finds the smallest unsorted item and
                    swaps it into the next front position. One pass of selection places one item
                    forever. One pass of bubble guarantees the end item.
                    """,
                    title("Two sorts, two ideas"),
                    cols(
                        "Bubble sort",
                        ["Compare neighbors", "Swap if out of order", "Largest settles at the end"],
                        "Selection sort",
                        ["Search for the minimum", "Swap it to the front", "Front grows sorted"],
                    ),
                ),
                board(
                    """
                    Watch bubble sort on 5, 1, 4, 2. Compare 5 and 1, swap, now 1, 5, 4, 2.
                    Compare 5 and 4, swap, now 1, 4, 5, 2. Compare 5 and 2, swap, now 1, 4, 2, 5.
                    The 5 has bubbled to the end and will not move again. The next pass only looks
                    at the first three items.
                    """,
                    title("Bubble sort, first pass"),
                    array(["5", "1", "4", "2"], hi=[0, 1], caption="Start: compare the highlighted pair"),
                    array(["1", "4", "2", "5"], caption="After the first pass, 5 is home"),
                ),
                board(
                    """
                    Now selection sort on the same list 5, 1, 4, 2. The minimum of the whole list
                    is 1, already almost at the front. Swap index 0 with index 1 to get 1, 5, 4, 2.
                    The sorted front is just the 1. Next, the minimum of the rest is 2. Swap it
                    toward the front. Selection does fewer swaps than bubble, but it still looks
                    through the unsorted part on every pass.
                    """,
                    title("Selection sort on the same list"),
                    array(["1", "5", "4", "2"], hi=[0], caption="1 is fixed in front"),
                    note("Do not say the list is sorted after one pass. Only one item is guaranteed.", "red"),
                ),
            ]),
            lecture("xi-search", "Linear search and binary search", True, [
                board(
                    """
                    Linear search checks the first item, then the next, until it finds the target
                    or runs out of items. The list does not need to be sorted. In the worst case
                    you look at every item. Binary search only works on a sorted list. It looks at
                    the middle. If the target is smaller, it throws away the right half. If the
                    target is larger, it throws away the left half.
                    """,
                    title("Two ways to search"),
                    cols(
                        "Linear",
                        ["Any order", "Check one by one", "Worst case: every item"],
                        "Binary",
                        ["Must be sorted", "Check the middle", "Throw away half each time"],
                    ),
                ),
                board(
                    """
                    Search for 19 in this sorted list. Indexes run from 0 to 6. The middle index
                    is 3, and the value there is 12. 19 is larger than 12, so the new low index
                    is 4. The middle of the right side is index 5, value 23. 19 is smaller, so
                    the high index becomes 4. Index 4 holds 19. Found.
                    """,
                    title("Binary search for 19"),
                    array(["2", "5", "8", "12", "19", "23", "30"], hi=[3], caption="First middle is 12, too small"),
                    array(["2", "5", "8", "12", "19", "23", "30"], hi=[4], caption="Next look lands on 19"),
                    note("If you forget the list must be sorted, binary search can skip the answer.", "red"),
                ),
                board(
                    """
                    Use linear search for a short unsorted list, such as ten names on a register
                    you will not reuse. Use binary search when the data is already sorted and the
                    list is long, such as a roll of thousands of student numbers. Sorting just to
                    answer one question may cost more than one linear pass. Say that tradeoff in
                    the exam if the question asks you to choose.
                    """,
                    title("Which search do you pick?"),
                    note("Sorted plus many searches: binary. Unsorted plus one search: linear.", "green"),
                ),
            ]),
            lecture("xi-evaluate", "Judging and choosing an algorithm", True, [
                board(
                    """
                    An algorithm can be correct and still be a poor choice. Judge it on four
                    questions. Does it give the right answer on every legal input? Are the steps
                    clear enough for another student to follow? How many steps does it take as the
                    list grows? How much extra memory does it need? A beautiful idea that never
                    finishes is not an algorithm.
                    """,
                    title("Four questions"),
                    chips("Correct", "Clear", "Fast enough", "Fits in memory"),
                    note("Test more than the happy example. Include an empty list and a one-item list.", "blue"),
                ),
                board(
                    """
                    Bubble sort does about n times n comparisons on n items, so the work grows
                    much faster than the list. Binary search cuts the problem in half, so adding
                    many more sorted items adds only a few extra looks. When you choose, match the
                    shape of the data. Sorted, unsorted, tiny, huge, searched once, or searched
                    every minute: those facts decide.
                    """,
                    title("Growth decides the winner"),
                    cols(
                        "Grows quickly",
                        ["Bubble sort", "Checking every pair"],
                        "Grows gently",
                        ["Binary search on sorted data", "One pass to find a total"],
                    ),
                ),
                board(
                    """
                    A practical rule for this class: if you understand a simple algorithm and the
                    data is small, use the simple one. Clarity matters in a school project. If the
                    data will grow, or the same search runs all day, pay for a method whose work
                    grows more slowly. Write the reason next to the choice. The reason is the mark.
                    """,
                    title("Decide in one sentence"),
                    note("Name the algorithm and the property of the data that makes it fit.", "green"),
                ),
            ]),
        ]),
        chapter("xi-ch3", 3, "Programming Fundamentals", [
            lecture("xi-languages", "Languages, careers, and an IDE", False, [
                board(
                    """
                    A programming language is a set of rules for writing instructions a computer
                    can carry out. Machine language is numeric and painful to read. Assembly uses
                    short codes for one machine. High-level languages, such as Python, look closer
                    to English and run on many machines after a translator turns them into machine
                    instructions. This course writes Python.
                    """,
                    title("Kinds of languages"),
                    layers(
                        "High-level: Python, easier for people",
                        "Assembly: short codes for one processor",
                        "Machine code: bits the processor executes",
                    ),
                ),
                board(
                    """
                    Python shows up in data work, simple web tools, and automation. You do not
                    need to pick a forever career in class 11. You do need to be able to read an
                    error, write a small program, and explain it. An IDE, an integrated development
                    environment, is the workshop: editor, runner, and debugger together. Visual
                    Studio Code is one IDE you can use for Python files.
                    """,
                    title("Python and the workshop"),
                    steps("Write a .py file", "Save it", "Run it", "Read the error if it stops"),
                    note("The IDE does not think for you. It only makes the cycle faster.", "gold"),
                ),
                board(
                    """
                    Keep projects in a folder with a clear name. Run the file you think you edited,
                    not an old copy on the desktop. When a program fails, the message names a line
                    number. Go to that line first. Careers that use this skill include software
                    development, data analysis, and teaching computing. The shared foundation is
                    the same: precise steps.
                    """,
                    title("Habits that matter more than the logo"),
                    note("Line numbers in errors are gifts. Read them.", "green"),
                ),
            ]),
            lecture("xi-variables", "Variables, types, input, and output", True, [
                board(
                    """
                    A variable is a name for a value the program can change. In Python you create
                    it by assigning, for example marks = 78. You do not declare the type in a
                    separate line. The type belongs to the value. 78 is an int, 78.5 is a float,
                    the word pass inside quotes is a str, and True or False is a bool. Capital T
                    in True matters.
                    """,
                    title("Names and types"),
                    code("marks = 78", "average = 78.5", "grade = \"pass\"", "late = False"),
                    chips("int", "float", "str", "bool"),
                ),
                board(
                    """
                    input always gives you text, even if the user types digits. If you want a
                    number, wrap the call: marks = int(input("Marks: ")). print sends text to the
                    screen. You can print several items separated by commas. If you forget int,
                    then marks + 5 tries to add text and a number, and Python stops.
                    """,
                    title("Input is text until you convert it"),
                    code("name = input(\"Name: \")", "marks = int(input(\"Marks: \"))", "print(name, marks)"),
                    note("int around input when you will do arithmetic. Quotes when the data is a name.", "red"),
                ),
                board(
                    """
                    Choose names that say what the value is. m is weaker than marks. Do not use
                    spaces in a name, and do not start with a digit. A good short program reads
                    one mark, adds a bonus of 2, and prints the new mark. Trace it with the input
                    40. The printed result must be 42. If you cannot trace it, do not add more lines.
                    """,
                    title("Trace a three-line program"),
                    code("marks = int(input())", "marks = marks + 2", "print(marks)"),
                    note("Input 40. After line 2, marks holds 42.", "blue"),
                ),
            ]),
            lecture("xi-operators", "Arithmetic, logic, and bits", True, [
                board(
                    """
                    Arithmetic operators calculate. Plus, minus, star, and slash are add, subtract,
                    multiply, and divide. Two slashes divide and drop the fraction, so 7 divided
                    with two slashes by 2 is 3. Percent is the remainder, so 7 percent 2 is 1.
                    Two stars mean power, so 2 star star 3 is 8. A single equals assigns. A double
                    equals asks a question.
                    """,
                    title("Arithmetic and assignment"),
                    table(
                        ["Expression", "Result"],
                        [["7 / 2", "3.5"], ["7 // 2", "3"], ["7 % 2", "1"], ["2 ** 3", "8"]],
                    ),
                    note("= stores a value. == compares two values.", "red"),
                ),
                board(
                    """
                    Relational operators compare and give True or False: less than, greater than,
                    and the equal and not-equal forms. Logical and is True only when both sides
                    are True. Logical or is True when at least one side is True. not flips a
                    Boolean. Membership uses the word in, as in 3 in [1, 3, 5], which is True.
                    """,
                    title("Questions Python can ask"),
                    code("passed = marks >= 50 and absent == False", "print(3 in [1, 3, 5])"),
                    cols("and", ["Both sides True"], "or", ["At least one side True"]),
                ),
                board(
                    """
                    Bitwise operators look at the bits inside integers. 5 is binary 0101 and 3 is
                    binary 0011. Bitwise AND keeps a bit only where both numbers have 1, so the
                    result is 0001, which is 1. Bitwise OR gives 0111, which is 7. You will not
                    need these every day, but you should be able to compute a tiny example and
                    tell them apart from logical and and or.
                    """,
                    title("A tiny bitwise example"),
                    table(
                        ["", "bits"],
                        [["5", "0 1 0 1"], ["3", "0 0 1 1"], ["5 AND 3", "0 0 0 1"], ["5 OR 3", "0 1 1 1"]],
                    ),
                    note("Logical and works on True and False. Bitwise AND works on bits.", "green"),
                ),
            ]),
            lecture("xi-selection", "if, elif, and nested decisions", True, [
                board(
                    """
                    Sequence means the lines run from top to bottom. Selection means some lines
                    run only when a condition is true. if marks greater than or equal to 50, print
                    pass. An else branch runs when the condition is false. Exactly one of those
                    two branches runs. Indent the branch. In Python the indent is the structure,
                    not decoration.
                    """,
                    title("if and else"),
                    code("if marks >= 50:", "    print(\"Pass\")", "else:", "    print(\"Retake\")"),
                    note("The colon and the indent are part of the syntax.", "red"),
                ),
                board(
                    """
                    elif adds another question after the first failed. Use it for bands: 80 and
                    above is distinction, 50 and above is pass, otherwise retake. Python asks the
                    questions from top to bottom and stops at the first true one. If you test
                    marks greater than or equal to 50 before the distinction test, a mark of 90
                    prints pass and never reaches distinction.
                    """,
                    title("Order the tests"),
                    code("if marks >= 80:", "    print(\"Distinction\")", "elif marks >= 50:", "    print(\"Pass\")", "else:", "    print(\"Retake\")"),
                    note("Put the stricter test first.", "green"),
                ),
                board(
                    """
                    Nested if means a decision inside a decision. A student is eligible for the
                    trip if fees are paid, and then if permission is signed, print going, else
                    print slip missing. Draw it as a flowchart before you indent it twice. Every
                    if that needs an opposite path should have its own else, or you should be
                    sure the missing path is allowed to do nothing.
                    """,
                    title("A decision inside a decision"),
                    flow("Fees paid?|decision", "Slip signed?|decision", "Print going|process", "Stop|term"),
                    note("Trace marks 90, 60, and 40. You should see three different messages.", "blue"),
                ),
            ]),
            lecture("xi-loops", "for, while, break, and continue", True, [
                board(
                    """
                    A loop repeats. for walks through a sequence. range of 4 gives 0, 1, 2, 3.
                    It stops before the number you wrote. while repeats as long as a condition
                    stays true. A while loop needs a line that changes the condition, or it never
                    ends. for is the better choice when you know how many times, or you are walking
                    a list. while fits when you wait for a user to type stop.
                    """,
                    title("for and while"),
                    code("for i in range(4):", "    print(i)", "n = 3", "while n > 0:", "    n = n - 1"),
                    note("range(4) does not include 4.", "red"),
                ),
                board(
                    """
                    break leaves the loop immediately. continue skips the rest of this round and
                    starts the next one. In a list of marks, continue can skip a negative typo,
                    and break can stop when a sentinel value such as minus 1 appears. Do not use
                    break to hide a confused condition. If the loop's job is clear, the while line
                    can usually say it.
                    """,
                    title("break and continue"),
                    cols("break", ["Leave the loop now"], "continue", ["Skip to the next round"]),
                    note("A sentinel is a special value that means stop, not a real mark.", "gold"),
                ),
                board(
                    """
                    A nested loop is a loop inside a loop. To print a 3 by 3 grid of stars you let
                    the outer loop pick the row and the inner loop print three stars. The inner
                    loop finishes completely for each single step of the outer loop. If your table
                    has the wrong number of rows, look at the outer range. If each row is the wrong
                    length, look at the inner range.
                    """,
                    title("Nested loops"),
                    code("for row in range(3):", "    for col in range(3):", "        print(\"*\", end=\"\")", "    print()"),
                    note("Inner loop restarts every time the outer loop takes one step.", "green"),
                ),
            ]),
            lecture("xi-debug", "Libraries, debugging, and a bill", False, [
                board(
                    """
                    A library is a collection of ready-made functions. Python ships with libraries
                    such as math and random. import math lets you call math.sqrt of 16. A third-party
                    library is one you add to your computer, often with the pip tool, because it is
                    not in the standard set. Use a library when the task is common. Write your own
                    code when the rule is specific to your problem.
                    """,
                    title("Built in and third party"),
                    code("import math", "print(math.sqrt(16))", "import random", "print(random.randint(1, 6))"),
                    note("sqrt of 16 is 4. randint of 1 and 6 simulates one die.", "blue"),
                ),
                board(
                    """
                    Debugging means finding why the program does not match your intention. Read the
                    error type and the line number. NameError means you used a name you never
                    assigned. IndentationError means the spaces are inconsistent. If there is no
                    error but the answer is wrong, print the important variables just before the
                    bad result. Fix one cause, run again, and remove the extra prints when it works.
                    """,
                    title("A calm debugging order"),
                    steps("Read the line number", "Name the error type", "Print the values just above it", "Change one thing and run again"),
                    note("Changing five lines at once makes a new bug and hides the old one.", "red"),
                ),
                board(
                    """
                    A shopping bill adds prices. Start total at 0. For each price in the list, add
                    it to total. Then print total. With prices 120, 45, and 80, the total is 245.
                    If you reset total inside the loop, you throw away the earlier prices. That is
                    the bug to watch. The same pattern later becomes a database total.
                    """,
                    title("Shopping bill"),
                    code("prices = [120, 45, 80]", "total = 0", "for price in prices:", "    total = total + price", "print(total)"),
                    note("245. If your program prints 80, total was reset inside the loop.", "green"),
                ),
            ]),
        ]),
        chapter("xi-ch4", 4, "Data and Analysis", [
            lecture("xi-dbms", "Data, information, and tables", True, [
                board(
                    """
                    Data is a raw recorded fact, such as the characters 4 2. Information is data
                    plus meaning, such as 42 marks in Computer Science for student 15. A database
                    is an organized collection of related data. A database management system, a
                    DBMS, is the software that stores it, guards the rules, and answers questions.
                    The file on disk is not the DBMS. The DBMS is the program that manages it.
                    """,
                    title("Data, information, database, DBMS"),
                    flow("Raw data|io", "Meaning added|process", "Information|term"),
                    note("42 alone is data. 42 marks for Ayesha is information."),
                ),
                board(
                    """
                    A table holds one kind of thing. A row, also called a record, is one example,
                    such as one student. A column, also called a field, is one property, such as
                    the class name. A cell is the crossing of one row and one column. If you put
                    students and their books in one wide messy table, later questions become hard.
                    Separate tables are the start of a relational design.
                    """,
                    title("Table, record, field"),
                    table(
                        ["student_id", "name", "class"],
                        [["15", "Ayesha", "XI"], ["16", "Bilal", "XI"]],
                    ),
                    note("One row is one student. Do not put two students in one row.", "red"),
                ),
                board(
                    """
                    The DBMS does jobs a loose spreadsheet does poorly: many people can use the
                    data, rules can be enforced, and you can ask questions without rewriting the
                    tables. Microsoft Access is the desktop DBMS this class practices. The ideas
                    you learn, tables and keys and queries, also live in larger systems. Learn the
                    ideas, not only the button names.
                    """,
                    title("What the DBMS is for"),
                    chips("Store", "Enforce rules", "Query", "Report"),
                ),
            ]),
            lecture("xi-keys", "Keys, integrity, and ER diagrams", True, [
                board(
                    """
                    A primary key is a field, or a combination of fields, that identifies one row
                    and never repeats and is never empty. student_id can be a primary key. A name
                    cannot, because two students can share a name. A foreign key is a field in one
                    table that points at a primary key in another table. It is how rows in different
                    tables stay related.
                    """,
                    title("Primary key and foreign key"),
                    table(
                        ["loan_id", "student_id", "book_id"],
                        [["1", "15", "88"], ["2", "16", "88"]],
                    ),
                    note("student_id inside the loan table is a foreign key. It must match a real student.", "green"),
                ),
                board(
                    """
                    Entity integrity says every primary key is unique and not null. Referential
                    integrity says a foreign key either matches an existing primary key or is empty
                    when the design allows that. If loan 3 names student 99 and there is no student
                    99, the database is lying. A relational DBMS can reject that insert. That rejection
                    is a feature, not a crash.
                    """,
                    title("Two integrity rules"),
                    cols(
                        "Entity integrity",
                        ["Primary key unique", "Primary key not empty"],
                        "Referential integrity",
                        ["Foreign key must exist", "Or be allowed to be empty"],
                    ),
                ),
                board(
                    """
                    An entity-relationship diagram sketches the design before you build tables.
                    Draw an entity as a rectangle, an attribute as an oval, and a relationship as
                    a diamond. Student borrows Book. Cardinality says how many: one student can
                    borrow many books, and one copy is borrowed by one student at a time. The
                    diagram is a conversation with the rules. It is not decoration.
                    """,
                    title("ER sketch"),
                    flow("Student|process", "Borrows|decision", "Book|process"),
                    note("Rectangle: entity. Oval: attribute. Diamond: relationship.", "gold"),
                ),
            ]),
            lecture("xi-schema", "A lab-loan schema", True, [
                board(
                    """
                    A relational schema names each table and its fields, and it underlines the
                    primary key. Here is a computer-lab loan system, the same kind of problem as a
                    library desk. Student has student_id, name, and class. Device has device_id,
                    kind, and status. Loan has loan_id, student_id, device_id, and due date.
                    The repeated ids are the foreign keys that tie a loan to one student and one device.
                    """,
                    title("Three related tables"),
                    code(
                        "Student(student_id, name, class_name)",
                        "Device(device_id, kind, status)",
                        "Loan(loan_id, student_id, device_id, due)",
                    ),
                    note("Underline student_id, device_id, and loan_id as primary keys on paper."),
                ),
                board(
                    """
                    Why not store the student name inside every loan row? If Ayesha fixes the
                    spelling of her name, you would have to hunt every loan. Stored once in Student,
                    the name stays consistent. The loan keeps only student_id. This is the point of
                    a relational schema: each fact lives in one home, and keys point to that home.
                    """,
                    title("Each fact lives once"),
                    cols(
                        "Stored once",
                        ["Name in Student", "Device kind in Device"],
                        "Pointed to",
                        ["student_id in Loan", "device_id in Loan"],
                    ),
                    note("If a name changes in two places and only one is edited, the data has split.", "red"),
                ),
                board(
                    """
                    Walk a question across the schema. Which devices are out, and who has them?
                    Start at Loan, keep rows with no return yet, then follow student_id to Student
                    for the name, and device_id to Device for the kind. You did not need a new
                    table. If a question cannot be answered by following keys, the schema is missing
                    a field or a relationship.
                    """,
                    title("Follow the keys to answer"),
                    steps("Start at Loan", "Match student_id to Student", "Match device_id to Device", "Read the names and the due date"),
                ),
            ]),
            lecture("xi-access", "Access objects, queries, and charts", False, [
                board(
                    """
                    In Microsoft Access a table stores the rows. A form is a screen for entering
                    or editing one record without scrolling a huge grid. A query asks a question
                    and returns a set of rows. A report lays those rows out for printing. Build
                    the tables and keys first. A pretty form on a bad table only helps you type
                    wrong data faster.
                    """,
                    title("Table, form, query, report"),
                    chips("Table stores", "Form edits", "Query asks", "Report presents"),
                    note("Objects are views and tools. The table still holds the data.", "gold"),
                ),
                board(
                    """
                    A query can filter, for example status equals Issued. It can sort by due date.
                    It can calculate a count of loans per class. Criteria belong in the criteria
                    row, not glued into the field name. If you want devices issued and overdue,
                    put both conditions in the query and test it on a table where you already know
                    the answer by hand. Three known rows are enough for a test.
                    """,
                    title("A query is a precise question"),
                    steps("Choose the tables", "Add the fields you want to see", "Put criteria in the criteria row", "Run and compare with a hand count"),
                    note("If the hand count is 2 and the query shows 5, a relationship is probably wrong.", "red"),
                ),
                board(
                    """
                    Summaries become charts. A count of loans by device kind can be a column chart.
                    A share of issued versus available devices can be a pie chart. Label the axes
                    and give the chart a title that states the question, not Chart 1. The chart is
                    only as honest as the query under it. Fix the query before you recolor the bars.
                    """,
                    title("From summary to chart"),
                    cols("Column chart", ["Compare counts"], "Pie chart", ["Show parts of a whole"]),
                    note("Title the chart with the question it answers.", "green"),
                ),
            ]),
        ]),
        chapter("xi-ch5", 5, "Applications and Impacts of Computing", [
            lecture("xi-ai-iot", "AI, IoT, and data analytics", True, [
                board(
                    """
                    Artificial intelligence, in this course, means computing that performs a task
                    we usually associate with human judgment, such as recognizing a face in a photo
                    or suggesting a next word. It is not a person, and it is not magic. It follows
                    a model built from examples and rules. If the examples were narrow, the results
                    will be narrow too.
                    """,
                    title("Artificial intelligence"),
                    bullet("Learns or follows a model"),
                    bullet("Needs examples or rules"),
                    bullet("Can be wrong with confidence"),
                    note("Ask what data the system saw before you trust the answer.", "red"),
                ),
                board(
                    """
                    The Internet of Things is ordinary objects that sense, send, and sometimes act.
                    A soil sensor, a link to the network, a small processor, and a pump that turns
                    on form one IoT loop. Data analytics is the work of turning collected records
                    into a decision: clean them, calculate, and present. AI may sit on top of that
                    data. IoT may be the thing that gathered it. They are partners, not synonyms.
                    """,
                    title("IoT and analytics"),
                    cols(
                        "IoT parts",
                        ["Sensor", "Connection", "Processor", "Actuator"],
                        "Analytics parts",
                        ["Collect", "Clean", "Calculate", "Present"],
                    ),
                ),
                board(
                    """
                    Compare them on one line each. IoT collects from the physical world. AI makes
                    or suggests a judgment. Data analytics explains what the numbers say. A smart
                    irrigation project can use all three: sensors collect moisture, analytics show
                    the week, and a model decides when to open the valve. In an exam, define the
                    one the question names. Do not swap the definitions.
                    """,
                    title("Do not mix the three"),
                    chips("IoT senses", "Analytics explains", "AI judges or predicts"),
                    note("A chart of attendance is analytics. It is not automatically AI.", "green"),
                ),
            ]),
            lecture("xi-impact", "Uses, sources, and effects", False, [
                board(
                    """
                    IoT shows up where a measurement should trigger an action: a clinic fridge that
                    warns if the temperature rises, a bus that shares its location, a meter that
                    reports electricity use. AI in Pakistani classrooms might mean reading practice
                    that adapts, or a tool that helps a teacher sort open responses. The useful
                    question is always the same: what decision gets better, and who checks it?
                    """,
                    title("Where these tools show up"),
                    steps("Name the place", "Name the data", "Name the decision", "Name the human who can override it"),
                ),
                board(
                    """
                    Information sources have levels. A primary source is the original record, such
                    as your own survey or a sensor log. A secondary source interprets that record,
                    such as a news article about the survey. A tertiary source collects secondary
                    work, such as an encyclopedia entry. Cite the closest source you actually used.
                    A blog that quotes a report is not the report.
                    """,
                    title("Primary, secondary, tertiary"),
                    layers(
                        "Primary: the original measurement or document",
                        "Secondary: an explanation of that original",
                        "Tertiary: a summary of explanations",
                    ),
                ),
                board(
                    """
                    Computing changes health, education, business, and the environment. A patient
                    file that follows the patient can prevent a repeated test. The same file can
                    harm the patient if it leaks. An online class reaches a village and also fails
                    when the power fails. Impact answers should name both the benefit and the new
                    risk. One-sided praise is incomplete.
                    """,
                    title("Impact has two sides"),
                    cols("Benefit", ["Faster access", "Fewer repeated tasks"], "Risk", ["Privacy", "Depends on power and skill"]),
                    note("For full marks, state one benefit and one risk.", "green"),
                ),
            ]),
            lecture("xi-assistive", "Assistive technology", False, [
                board(
                    """
                    Assistive technology is a tool that lets someone do a task their body or senses
                    make hard. A screen reader speaks what is on the screen. Captions turn speech
                    into text. A switch lets a student select with one reliable movement. These are
                    not extras for a few people. A caption also helps a student in a noisy corridor.
                    """,
                    title("Tools that open a task"),
                    chips("Screen reader", "Captions", "Switch", "Large text"),
                    note("If a task can only be done with a mouse, some students are locked out.", "red"),
                ),
                board(
                    """
                    The importance is participation. A student who cannot hear the video can still
                    learn the science if captions exist. A student who cannot use a keyboard can
                    still answer if the software accepts a switch. Designers who ignore this build
                    a smaller world. Careers include accessibility specialist, speech technology,
                    and ordinary software work done with these needs in mind.
                    """,
                    title("Why it belongs in this course"),
                    bullet("Same lesson, more students can finish it"),
                    bullet("The skill is part of computing, not a separate kindness"),
                    note("Describe the barrier, then the tool that removes it.", "green"),
                ),
                board(
                    """
                    Work one example in a sentence a marker can write. Barrier: a deaf student cannot
                    use a video that has only music and speech. Tool: captions plus a short transcript
                    under the video. Check: the student can answer the same two questions as the class
                    without asking a neighbor to repeat the audio. If the check fails, the tool was not
                    actually available, even if a menu claimed captions were on.
                    """,
                    title("Barrier, tool, check"),
                    steps("Name the barrier", "Name the tool", "Ask the same question the class got", "Fix the tool if the answer is impossible"),
                    note("A setting that exists but is turned off does not count as access.", "blue"),
                ),
            ]),
        ]),
        chapter("xi-ch6", 6, "Digital Literacy", [
            lecture("xi-literacy", "Digital literacy and kinds of data", False, [
                board(
                    """
                    Digital literacy is the ability to find, judge, use, and share information with
                    digital tools, and to do it safely. Searching is only the first step. You also
                    decide whether a page is trustworthy, whether you may reuse its picture, and
                    whether a message is trying to rush you. In the information age the scarce skill
                    is judgment, not access to more tabs.
                    """,
                    title("More than clicking search"),
                    steps("Find", "Judge", "Use with permission", "Share carefully"),
                    note("A top search result is not automatically a true result.", "red"),
                ),
                board(
                    """
                    Data can be quantitative or qualitative. Quantitative data is numbers you can
                    calculate with, such as ages or marks. Qualitative data is descriptions, such
                    as a student's reason for choosing a subject. You can count how many students
                    said facilities, and then the count is quantitative, but the original words
                    were qualitative. Say which form you are analyzing.
                    """,
                    title("Numbers and descriptions"),
                    cols("Quantitative", ["Marks", "Ages", "Counts"], "Qualitative", ["Reasons", "Interview quotes", "Observations"]),
                ),
                board(
                    """
                    A literate researcher writes down where each number came from and the date.
                    A screenshot without a source becomes a rumor with a border. Before you build
                    a chart, ask if the data is the kind that can support the claim. You cannot
                    average a list of favorite colors. You can count them.
                    """,
                    title("Match the data to the claim"),
                    note("Count categories. Average only true numbers.", "green"),
                ),
            ]),
            lecture("xi-collect", "Collecting primary and secondary data", True, [
                board(
                    """
                    Interviews ask a few people deeper questions. Surveys ask many people the same
                    short questions. Observation watches what people do, not only what they say.
                    A prototype test watches someone try a design. A simulation copies a situation
                    when the real one is too costly or risky, such as a fire drill model. Pick the
                    method that matches the question, not the method that feels easiest.
                    """,
                    title("Ways to collect"),
                    chips("Interview", "Survey", "Observation", "Prototype test", "Simulation"),
                ),
                board(
                    """
                    Primary data is data you collect for this question. Secondary data is data
                    someone else already collected. Your class survey about canteen time is primary.
                    A government education table you download is secondary. Secondary data is faster
                    and may be larger, but it was gathered for someone else's purpose. Read how it
                    was collected before you trust it for yours.
                    """,
                    title("Primary and secondary"),
                    cols("Primary", ["You design it", "Fits your question", "Takes time"], "Secondary", ["Already exists", "May not fit", "Check the method"]),
                    note("Name the source and the year for every secondary figure.", "green"),
                ),
                board(
                    """
                    Design the approach on paper first. Write the question, the people, the tool,
                    and what you will not collect. If you do not need phone numbers, do not ask for
                    them. A short survey of twenty classmates about lunch queues can be enough for
                    a class project. A national claim would need a wider sample you probably cannot
                    gather, so do not pretend the class is the country.
                    """,
                    title("Design the approach"),
                    steps("Write the question", "Choose who is asked", "Choose the tool", "Limit what you collect"),
                    note("Do not generalize a single class to the whole district.", "red"),
                ),
            ]),
            lecture("xi-present", "Sheets, stories, and a small inquiry", False, [
                board(
                    """
                    A spreadsheet stores rows and calculates. Use it to sort survey answers, count
                    categories, and compute an average of numeric columns. A presentation tells the
                    story in a few slides: question, method, chart, conclusion. An infographic is
                    one picture that carries a single comparison. A report is the long form with
                    the method written so someone else could repeat it.
                    """,
                    title("Pick the container"),
                    cols("Spreadsheet", ["Rows", "Formulas", "The working data"], "Slides or report", ["The claim", "One chart", "The limit of the study"]),
                ),
                board(
                    """
                    A digital inquiry can follow a short path. Search with precise words and note
                    the source. Choose a method. Collect a small primary set, such as a five-question
                    survey. Add one secondary figure for context. Clean the sheet. Chart one comparison.
                    Write a conclusion that does not outrun the data, and one recommendation a school
                    could actually try. That bundle is your digital artefact.
                    """,
                    title("A full inquiry, compressed"),
                    steps(
                        "Search and record sources",
                        "Survey a real group",
                        "Add one secondary number",
                        "Chart a comparison",
                        "Conclude only what the data shows",
                    ),
                ),
                board(
                    """
                    The final artefact should let a new reader see the question without asking you.
                    Label units. Say how many people answered. If only eighteen students answered,
                    write that. Careers that use this skill include research assistance, journalism,
                    data work, and any job that must explain a number to a person who was not in the room.
                    """,
                    title("Leave a trail"),
                    note("Question, sample size, chart, limit, recommendation.", "green"),
                ),
            ]),
            lecture("xi-revision", "Class XI revision boards", True, [
                board(
                    """
                    Revision pass for systems and logic. Discrete means countable steps. Digital
                    signals jump, usually between 0 and 1. AND is 1 only when all inputs are 1.
                    OR is 1 when any input is 1. NOT flips. NAND and NOR are universal. XOR is 1
                    when the bits differ. A K-map group must be a power of two.
                    """,
                    title("Logic, fast"),
                    gates("AND", "OR", "NOT", "XOR"),
                    note("De Morgan: break the bar and swap AND with OR.", "gold"),
                ),
                board(
                    """
                    Revision pass for process and networks. Waterfall is one downhill pass and fits
                    fixed rules. Agile repeats short cycles and fits changing needs. OSI has seven
                    layers, from application down to physical. TCP/IP folds those into four:
                    application, transport, internet, and network access. A router routes. A switch
                    forwards on the local link.
                    """,
                    title("Life cycle and layers"),
                    layers("Application", "Transport", "Internet", "Network access"),
                ),
                board(
                    """
                    Revision pass for algorithms and Python. Decompose, notice patterns, then hide
                    irrelevant detail. Bubble sort swaps neighbors. Selection sort parks the minimum
                    at the front. Binary search needs sorted data and checks the middle. input
                    returns text. == compares, = assigns. Test the stricter if before the looser one.
                    range stops before the end number.
                    """,
                    title("Algorithms and Python"),
                    chips("Bubble: neighbors", "Selection: minimum", "Binary: sorted middle", "input is text"),
                ),
                board(
                    """
                    Revision pass for data and impact. A primary key is unique and not empty. A
                    foreign key points at a primary key. Referential integrity means that pointer
                    is valid. IoT senses and may act. Analytics explains numbers. AI makes a
                    judgment from a model. Primary data is yours. Secondary data needs a source
                    and a date. State one benefit and one risk when you discuss impact.
                    """,
                    title("Data and impact"),
                    note("Benefit plus risk. Source plus date. Key plus match.", "green"),
                ),
            ]),
        ]),
    ]
