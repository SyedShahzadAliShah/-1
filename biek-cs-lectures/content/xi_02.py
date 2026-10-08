from content.schema import lecture

LECTURE = lecture(
    id="xi-2",
    number=2,
    title="Computational Thinking and Algorithms",
    kicker="CLASS XI  ·  UNIT 2",
    unit="Unit 2 — Computational Thinking and Algorithms",
    domain="B. Computational thinking and algorithms",
    periods="about 20 periods",
    intro=(
        "Computational thinking is the habit of turning a messy problem into steps a computer can follow. "
        "This lecture covers the four habits — decomposition, pattern recognition, abstraction, and algorithms — "
        "then the two families of algorithms the paper actually asks you to trace: searching and sorting."
    ),
    outcomes=[
        "Analyse a problem using decomposition, pattern recognition, and abstraction.",
        "State the properties of a proper algorithm and write clear pseudocode.",
        "Trace a flowchart or a pseudocode listing and judge correctness, clarity, and efficiency in plain language.",
        "Apply linear search, binary search, bubble sort, and insertion sort to a small list and show the steps.",
    ],
    blocks=[
        ("h2", "Four habits of computational thinking"),
        (
            "p",
            "**Decomposition** breaks one problem into smaller problems that can be solved separately. A result portal decomposes into login, mark entry, calculation, and display. **Pattern recognition** notices that two of those pieces are the same kind of check: both reject an empty box, both reject a value out of range. **Abstraction** keeps the detail that matters and hides the rest. For a search, the list items matter and the colour of the screen does not. An **algorithm** is the finite sequence of precise steps that uses those habits.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — counting a real problem",
                "text": (
                    "Problem: how many students in this class scored 80 or above?\n\n"
                    "Decomposition: get the list, look at one mark, decide, count, move on, stop at the end. "
                    "Pattern: every mark is handled the same way, so a loop is honest. "
                    "Abstraction: the algorithm needs the marks, not the students' addresses. "
                    "A vague instruction such as “look at the good ones” is not an algorithm, because two people would not do the same thing."
                ),
            },
        ),
        ("h2", "What makes an algorithm acceptable"),
        (
            "p",
            "A classroom algorithm should have five properties. It has **input**. It has **output**. Each step is **definite** (no guesswork). It is **finite** (it ends). Each step is **effective** (a person, or a computer, can actually carry it out). “Try every possible password in the world until something happens” fails finiteness in any useful sense and is not a task this course sets.",
        ),
        (
            "p",
            "**Pseudocode** is structured English, not a programming language. For board work, use line numbers, a consistent indent for the body of a loop or a decision, uppercase words for the commands, and a short comment only where the step is not obvious. Declare the data in one line before you use it. The usual commands in this course are INPUT, SET, IF, ELSE, WHILE, FOR, and OUTPUT.",
        ),
        (
            "code",
            {
                "lang": "Pseudocode",
                "text": (
                    "1  INPUT mark\n"
                    "2  IF mark >= 80 THEN\n"
                    "3      OUTPUT \"Distinction\"\n"
                    "4  ELSE\n"
                    "5      IF mark >= 40 THEN\n"
                    "6          OUTPUT \"Pass\"\n"
                    "7      ELSE\n"
                    "8          OUTPUT \"Needs improvement\"\n"
                    "9      ENDIF\n"
                    "10 ENDIF"
                ),
            },
        ),
        (
            "p",
            "A **flowchart** is the same algorithm in symbols. An oval starts and stops. A parallelogram is input or output. A rectangle is a process. A diamond is a decision, and every diamond needs two labelled exits. Arrows must not vanish. Tracing means writing the value of each variable after every step, on a fresh row, until you reach the end. A trace that skips the false branch has not tested the algorithm.",
        ),
        ("h2", "Correctness, clarity, and efficiency"),
        (
            "p",
            "An algorithm is **correct** if, for every allowed input, the output matches the specification. One lucky example does not prove correctness; a single counter-example disproves it. It is **clear** if another student can trace it without asking you what a line means. Names such as `count` and `position` are clearer than `x` and `y` once a problem has two different numbers. It is **efficient**, at this level, if it does not repeat work for no reason. You do not need formal big-O notation to say that looking at every item once is kinder than looking at every pair of items, when a single pass is enough.",
        ),
        (
            "callout",
            {
                "kind": "warn",
                "title": "Common mistake",
                "text": "A flowchart diamond with only one arrow is unfinished. An IF in pseudocode without an ENDIF, or an indent that does not match the ENDIF, will be marked as unclear even when your idea was right.",
            },
        ),
        ("h2", "Linear search"),
        (
            "p",
            "**Linear search** starts at the first item and compares until it finds the target or runs out of items. The list need not be sorted. If the target is absent, the honest result is “not found”, not the last item.",
        ),
        (
            "code",
            {
                "lang": "Pseudocode",
                "text": (
                    "1  INPUT list, n, target\n"
                    "2  SET position TO 0\n"
                    "3  SET index TO 1\n"
                    "4  WHILE index <= n AND position = 0\n"
                    "5      IF list[index] = target THEN\n"
                    "6          SET position TO index\n"
                    "7      ELSE\n"
                    "8          SET index TO index + 1\n"
                    "9      ENDIF\n"
                    "10 ENDWHILE\n"
                    "11 IF position = 0 THEN\n"
                    "12     OUTPUT \"Not found\"\n"
                    "13 ELSE\n"
                    "14     OUTPUT position\n"
                    "15 ENDIF"
                ),
            },
        ),
        (
            "p",
            "Positions in that listing start at 1, which is the usual board convention. Python later in the course starts at 0. Say which convention you are using. Trace of target 4 in the list 5, 1, 4, 2: index 1 compares 5, index 2 compares 1, index 3 compares 4 and sets position to 3. Three comparisons. If the target were 9, the loop would examine all four items and output “Not found”.",
        ),
        ("h2", "Binary search"),
        (
            "p",
            "**Binary search** requires a **sorted** list. It compares the target with the middle item. If the target is smaller, the right half is discarded. If it is larger, the left half is discarded. Each comparison removes about half of the remaining items, which is why it beats linear search on a long sorted list. On an unsorted list it is simply wrong, not “a bit slower”.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — binary search for 16",
                "text": (
                    "Sorted list, positions 1 to 7: 2, 5, 8, 12, 16, 23, 38. Target 16.\n\n"
                    "Low = 1, high = 7. Middle position = (1+7)÷2 = 4, value 12. 16 is greater, so low becomes 5.\n\n"
                    "Low = 5, high = 7. Middle = (5+7)÷2 = 6, value 23. 16 is smaller, so high becomes 5.\n\n"
                    "Low = 5, high = 5. Middle = 5, value 16. Found at position 5.\n\n"
                    "Use integer division, discarding the fraction. Write low, high, and middle on every row of the trace."
                ),
            },
        ),
        (
            "p",
            "If the item is absent, low eventually passes high and you stop. Searching for 10 in the same list ends with the middle values 12, then 8, then 12’s neighbour is exhausted, and the result is not found. Show that stopping condition in a trace if the question asks for a missing item.",
        ),
        ("h2", "Bubble sort"),
        (
            "p",
            "**Bubble sort** repeatedly walks the list and swaps any neighbouring pair that is out of order. After the first pass the largest item has bubbled to the end. After the second pass the next largest is in place. You may stop early if a pass makes no swaps.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — bubble sort of 5, 1, 4, 2",
                "text": (
                    "Pass 1: compare 5 and 1, swap to 1, 5, 4, 2. Compare 5 and 4, swap to 1, 4, 5, 2. Compare 5 and 2, swap to 1, 4, 2, 5.\n\n"
                    "Pass 2: compare 1 and 4, keep. Compare 4 and 2, swap to 1, 2, 4, 5. Compare 4 and 5, keep.\n\n"
                    "Pass 3: 1 and 2 are in order, 2 and 4 are in order. No swap, so the list is sorted: 1, 2, 4, 5.\n\n"
                    "The end of each pass is the line the examiner wants to see. Do not jump to the final list."
                ),
            },
        ),
        ("h2", "Insertion sort"),
        (
            "p",
            "**Insertion sort** keeps a sorted portion on the left and inserts the next item into its proper place, shifting larger items right to make a gap. It is the way many people sort a hand of cards.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — insertion sort of 5, 1, 4, 2",
                "text": (
                    "Start with the first card: [5] | 1, 4, 2.\n\n"
                    "Insert 1 in front of 5: [1, 5] | 4, 2.\n\n"
                    "Insert 4 between 1 and 5: [1, 4, 5] | 2.\n\n"
                    "Insert 2 between 1 and 4: [1, 2, 4, 5].\n\n"
                    "Each line shows the sorted portion in brackets. That is the trace."
                ),
            },
        ),
        (
            "p",
            "Choose the algorithm to match the data. An unsorted list of 12 names on a worksheet is a linear search or an insertion sort; binary search would be a mistake until you sort. A sorted attendance roll of several hundred names is a binary search. Bubble sort is easy to trace in an examination and wasteful on a huge list, which is a fair comment if a question asks you to evaluate it. Clarity is why we still teach the trace.",
        ),
        (
            "callout",
            {
                "kind": "exam",
                "title": "Exam tip",
                "text": "If the question says “show each pass”, a final sorted list with no passes scores almost nothing. If it says “which algorithm”, the first sentence must name it and the second must give the reason, usually “the list is not sorted” or “the list is already sorted and long”.",
            },
        ),
    ],
    terms=[
        ("Decomposition", "Splitting a problem into smaller problems."),
        ("Pattern recognition", "Noticing that the same step repeats or that two problems share a shape."),
        ("Abstraction", "Keeping the necessary detail and ignoring the rest."),
        ("Algorithm", "A finite, precise sequence of steps from input to output."),
        ("Pseudocode", "Structured English for an algorithm, with indent and line numbers."),
        ("Trace", "A table of variable values after each step."),
        ("Linear search", "Check items one by one. The list may be unsorted."),
        ("Binary search", "Halve a sorted list at each comparison."),
        ("Bubble sort", "Swap neighbouring items that are out of order, pass after pass."),
        ("Insertion sort", "Insert each next item into an already sorted left-hand portion."),
    ],
    checks=[
        {
            "q": "Why is “sort the names nicely” not an algorithm?",
            "a": "It is not definite. Two people can interpret “nicely” differently, so the steps are not precise and the result is not determined.",
        },
        {
            "q": "Can binary search be used on 9, 1, 4, 7 to find 4?",
            "a": "No. The list is not sorted. Sort it first, or use linear search. Binary search on unsorted data can report “not found” when the item is present.",
        },
        {
            "q": "After the first full pass of bubble sort on 5, 1, 4, 2, what is the list?",
            "a": "1, 4, 2, 5. The largest value, 5, has moved to the end.",
        },
    ],
    mcqs=[
        {
            "q": "Which property fails if an algorithm can run forever on a valid input?",
            "options": ["Input", "Output", "Finiteness", "Abstraction"],
            "answer": "C",
            "why": "Finiteness means the steps end. A loop with no progress toward a stopping condition fails it.",
        },
        {
            "q": "Binary search is appropriate when the data is",
            "options": [
                "unsorted and small",
                "sorted",
                "a single number",
                "stored only on paper and must not be ordered",
            ],
            "answer": "B",
            "why": "Each step throws away half of the list, which is valid only if every item on one side is smaller and every item on the other side is larger.",
        },
        {
            "q": "In insertion sort, the left-hand portion after each insertion is",
            "options": [
                "the unsorted remainder",
                "sorted",
                "reversed",
                "always a single item",
            ],
            "answer": "B",
            "why": "That is the idea of the algorithm: grow a sorted portion one item at a time.",
        },
        {
            "q": "Abstraction, in the counting-marks problem, means",
            "options": [
                "collecting home addresses as well as marks",
                "ignoring details that the steps do not use",
                "writing the program in Python immediately",
                "sorting before you count",
            ],
            "answer": "B",
            "why": "The count depends on the marks. Addresses are irrelevant detail.",
        },
    ],
    shorts=[
        {
            "q": "List the four computational-thinking habits and one sentence for each.",
            "a": "Decomposition splits the problem. Pattern recognition finds repeated structure. Abstraction drops detail that does not affect the result. An algorithm writes the remaining work as finite precise steps.",
        },
        {
            "q": "Trace linear search for 8 in the list 3, 8, 8, 1. Positions start at 1. Which 8 do you report, and why?",
            "a": "Compare position 1 (3), then position 2 (8). Stop and report position 2. The second 8 is never examined. The algorithm as written returns the first match, so say so.",
        },
        {
            "q": "Give one reason bubble sort is taught, and one reason it is a poor choice for a very large list.",
            "a": "It is taught because each pass is easy to trace by hand and the idea of a swap is visible. It is a poor choice at large scale because it repeatedly compares neighbours and moves values only one place at a time, so the number of comparisons grows much faster than the length of the list.",
        },
    ],
    longs=[
        {
            "marks": 5,
            "q": "The sorted list is 4, 9, 15, 21, 28, 33, 40. Trace binary search for 21. Then explain, without a formula, why this method beats linear search as the list grows, and when it must not be used.",
            "a": (
                "Positions 1 to 7. Low 1, high 7, middle 4, value 21. The middle value is the target, so the search stops at position 4. "
                "If a marker scheme expects you to show the halving anyway, state that the first comparison already succeeded, so there is no second row. Do not invent extra steps.\n\n"
                "Linear search may have to look at every item. Binary search throws away half of the remaining items after each comparison, so a list that is twice as long needs only one extra comparison, not twice the work. "
                "It must not be used when the list is unsorted, because the decision to discard a half depends on every item on that side being too small or too large."
            ),
        },
        {
            "marks": 5,
            "q": "Sort 7, 3, 7, 1 by insertion sort, showing the sorted portion after each insertion. Then say how your trace would differ if the question had asked for bubble sort.",
            "a": (
                "Insertion: [7] | 3, 7, 1. Insert 3 to get [3, 7] | 7, 1. Insert 7, which stays after the existing 7, to get [3, 7, 7] | 1. Insert 1 at the front to get [1, 3, 7, 7]. "
                "Equal values keep their relative order in this left-to-right insertion.\n\n"
                "Bubble sort would instead show full passes of neighbour swaps. Pass 1 ends as 3, 7, 1, 7. Pass 2 ends as 3, 1, 7, 7. Pass 3 ends as 1, 3, 7, 7. "
                "The final list matches, but the intermediate lines do not, so a bubble-sort trace written as insertion steps would lose the method marks."
            ),
        },
    ],
    labs=[
        {
            "title": "Lab 3 — Trace before you code",
            "steps": [
                "Write pseudocode for binary search with positions starting at 1.",
                "Trace it for the list 2, 5, 8, 12, 16, 23, 38 and the target 23. Keep a three-column table: low, high, middle value.",
                "Trace the same algorithm for the target 7 and show the step where low passes high.",
                "Ask a partner to follow only your pseudocode, not your explanation. Correct any line they cannot execute.",
            ],
            "success": "The partner’s trace matches yours, including the not-found stop, without extra oral help.",
        }
    ],
    summary=[
        "Decomposition, patterns, and abstraction come before code.",
        "An algorithm has input, output, definite steps, an end, and steps that can be carried out.",
        "Pseudocode needs indent, end markers, and line numbers. A decision symbol needs two exits.",
        "One counter-example destroys a claim of correctness. Clarity is part of the mark.",
        "Linear search walks from the start and works on unsorted data. It returns the first match.",
        "Binary search halves a sorted list. Integer middle, and stop when low passes high.",
        "Bubble sort swaps neighbours. Show every pass. Insertion sort grows a sorted left portion.",
    ],
)
