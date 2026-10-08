from content.schema import lecture

LECTURE = lecture(
    id="xi-3",
    number=3,
    title="Programming Fundamentals in Python",
    kicker="CLASS XI  ·  UNIT 3",
    unit="Unit 3 — Programming Fundamentals",
    domain="C. Programming fundamentals",
    periods="about 40 periods",
    intro=(
        "A program takes input, processes it, and produces output, using the same processor and memory you described in computer systems. "
        "Python is the language of this unit because the programs are short, the errors are readable, and the same language continues in Class XII. "
        "You will write sequence, selection, and repetition; draw with the turtle; use a library without reading its source; store values in a list; and split a large job into functions you can test."
    ),
    outcomes=[
        "Explain what a program does with input, process, and output, and name the parts of an IDE.",
        "Write and run Python that uses variables, operators, decisions, and loops.",
        "Draw compound shapes with the turtle, including a pen-up move.",
        "Use a standard library and explain abstraction as the reason you can.",
        "Populate a list, walk through it, and find an item.",
        "Decompose a problem into functions with parameters and return values.",
        "Find a fault by a dry run and by a breakpoint or a printed check.",
    ],
    blocks=[
        ("h2", "Why programs exist"),
        (
            "p",
            "Hardware does nothing useful until software tells it which input to read, which calculation to repeat, and which output to show. Python is used for science, small web services, data work, and teaching, because the same ideas — variables, decisions, loops, functions — appear in larger systems. A real task for this year is modest: a fee receipt, a pass-fail list, a square drawn on screen. The habit that matters is that the program matches a specification you could have written in pseudocode first.",
        ),
        (
            "p",
            "An **IDE** (integrated development environment) is the workbench. You need an editor, a way to run the file, a console for input and output, a file list, and a debugger. Thonny, IDLE, and VS Code are offline. A site such as Replit is an online IDE when the lab has no install rights. The language is the same. Learn where the Run button is and where error messages appear: they name a line number, and that line is the first place you look, not the last.",
        ),
        ("h2", "Values, variables, and operators"),
        (
            "p",
            "A **variable** is a name bound to a value. `marks = 78` stores an integer. `fee = 2500.50` stores a float. `grade = \"B\"` stores a string. `passed = True` stores a Boolean. Python decides the type from the value. `input()` always returns a string, so a numeric answer must be converted with `int()` or `float()` before you do arithmetic.",
        ),
        (
            "code",
            {
                "lang": "Python",
                "text": (
                    "name = input(\"Name: \")\n"
                    "obtained = int(input(\"Marks obtained: \"))\n"
                    "total = int(input(\"Total marks: \"))\n"
                    "percent = obtained / total * 100\n"
                    "print(name, round(percent, 1))"
                ),
            },
        ),
        (
            "p",
            "Arithmetic operators are `+  -  *  /  //  %  **`. `//` is integer division. `%` is the remainder. `**` is power. Comparison operators are `==  !=  <  >  <=  >=`. They produce True or False. Logical operators are `and`, `or`, and `not`. Assignment is `=`. Comparison is `==`. Mixing them up is the most common first-month bug.",
        ),
        (
            "callout",
            {
                "kind": "warn",
                "title": "Common mistake",
                "text": "`if marks = 40` is a syntax error because `=` assigns. The test is `if marks == 40`. And `int(\"78.5\")` fails: a decimal string needs `float`, not `int`.",
            },
        ),
        ("h2", "Sequence, selection, and repetition"),
        (
            "p",
            "**Sequence** means the lines run from top to bottom. **Selection** chooses a branch with `if`, `elif`, and `else`. **Repetition** repeats a block with `while` or `for`. The body of each of these is the indented lines underneath. Four spaces is the usual indent. A missing indent is a syntax error. An extra indent attaches a line to the wrong block, which is worse, because the program runs and does the wrong thing.",
        ),
        (
            "code",
            {
                "lang": "Python",
                "text": (
                    "marks = int(input(\"Marks: \"))\n"
                    "if marks >= 80:\n"
                    "    result = \"Distinction\"\n"
                    "elif marks >= 40:\n"
                    "    result = \"Pass\"\n"
                    "else:\n"
                    "    result = \"Needs improvement\"\n"
                    "print(result)"
                ),
            },
        ),
        (
            "p",
            "A `while` loop needs a condition that eventually becomes false. A `for` loop is the better tool when you know how many times to repeat, or when you are walking through a list. `range(1, 6)` produces 1, 2, 3, 4, 5. The stop value is not included.",
        ),
        (
            "code",
            {
                "lang": "Python",
                "text": (
                    "total = 0\n"
                    "for subject in range(1, 6):\n"
                    "    score = int(input(\"Subject \" + str(subject) + \": \"))\n"
                    "    total = total + score\n"
                    "print(\"Total\", total, \"Average\", total / 5)"
                ),
            },
        ),
        ("h2", "Turtle graphics"),
        (
            "p",
            "The **turtle** is a pen that moves on a screen. You give it distances and angles. `forward` and `backward` move. `right` and `left` turn, in degrees. `penup` lifts the pen so a move does not draw. `pendown` puts it back. `circle` draws a circle. Colour and width are properties of the pen. A compound shape is several simple shapes, with the pen lifted between them so you do not draw a stray line.",
        ),
        (
            "code",
            {
                "lang": "Python (turtle)",
                "text": (
                    "import turtle\n"
                    "\n"
                    "pen = turtle.Turtle()\n"
                    "pen.color(\"navy\")\n"
                    "for _ in range(4):\n"
                    "    pen.forward(120)\n"
                    "    pen.right(90)\n"
                    "pen.penup()\n"
                    "pen.goto(30, 30)\n"
                    "pen.pendown()\n"
                    "pen.color(\"teal\")\n"
                    "pen.circle(30)\n"
                    "turtle.done()"
                ),
            },
        ),
        (
            "p",
            "The square uses repetition: four sides, each followed by a right angle. The circle is a second shape. `penup` before `goto` is what keeps the two shapes separate. `turtle.done()` keeps the window open until the user closes it. In a written paper, you may be asked to state the angle inside the loop. A regular pentagon turns `360 / 5 = 72` degrees, not 90.",
        ),
        ("h2", "Libraries and abstraction"),
        (
            "p",
            "A **library** is a collection of functions somebody else has tested. `import math` gives you `math.sqrt` and `math.pi`. You use them without reading how the square root is calculated. That is **abstraction** in programming: a name hides a complicated implementation behind a small, stable interface. A third-party library is installed separately and then imported the same way. You choose one because it solves a real sub-problem, not because it is famous.",
        ),
        (
            "code",
            {
                "lang": "Python",
                "text": (
                    "import math\n"
                    "\n"
                    "radius = float(input(\"Radius: \"))\n"
                    "area = math.pi * radius ** 2\n"
                    "print(round(area, 2))\n"
                    "print(math.sqrt(area))"
                ),
            },
        ),
        (
            "callout",
            {
                "kind": "note",
                "title": "Built-in and third-party",
                "text": "`math`, `random`, and `turtle` ship with Python. A library such as a charting package may need an install. In the examination you can assume `math` and `turtle` exist. Say `import` in the first lines of any program that uses them.",
            },
        ),
        ("h2", "Lists"),
        (
            "p",
            "A **list** stores an ordered series of values. Indexes start at 0. `marks[0]` is the first mark. `append` adds at the end. `len` gives the length. A loop can populate a list, and a second loop can search it. This is linear search from the previous lecture, now in Python.",
        ),
        (
            "code",
            {
                "lang": "Python",
                "text": (
                    "marks = []\n"
                    "for _ in range(4):\n"
                    "    marks.append(int(input(\"Mark: \")))\n"
                    "\n"
                    "target = int(input(\"Find: \"))\n"
                    "found_at = -1\n"
                    "for index in range(len(marks)):\n"
                    "    if marks[index] == target and found_at == -1:\n"
                    "        found_at = index\n"
                    "\n"
                    "if found_at == -1:\n"
                    "    print(\"Not found\")\n"
                    "else:\n"
                    "    print(\"Index\", found_at)"
                ),
            },
        ),
        (
            "p",
            "If the user enters 10, 20, 20, 30 and searches for 20, the index printed is 1, the first match. Index −1 is a sentinel meaning “not found”. Do not use 0 as the sentinel: 0 is a legal index.",
        ),
        ("h2", "Functions"),
        (
            "p",
            "A **function** is a named block with a job. You **define** it with `def` and you **call** it by name. **Parameters** are the names in the definition. **Arguments** are the values in the call. A **return** sends a value back. Code that is copied in three places should be moved into one function so a fix happens once. This is decomposition: the large problem calls smaller problems.",
        ),
        (
            "p",
            "A name created inside a function is **local**. It is not visible outside. A parameter is also local. This course passes numbers and strings **by value** in the everyday sense that changing the parameter does not change the caller’s variable, unless you return the new value and the caller stores it. (If you later pass a list and append to it, the list is shared. For the functions in this unit, return the result.)",
        ),
        (
            "code",
            {
                "lang": "Python",
                "text": (
                    "def celsius_to_fahrenheit(celsius):\n"
                    "    return celsius * 9 / 5 + 32\n"
                    "\n"
                    "def fee_total(items, rate):\n"
                    "    return items * rate\n"
                    "\n"
                    "print(celsius_to_fahrenheit(0))\n"
                    "print(celsius_to_fahrenheit(100))\n"
                    "print(fee_total(3, 250))"
                ),
            },
        ),
        (
            "p",
            "The calls print 32.0, 212.0, and 750. A function that prints but does not return is awkward to test, because the result is stuck on the screen. Prefer returning a value, and let the caller print it. Functions that call other functions, or that are called inside a loop, are normal: a loop of five temperatures can call the converter five times.",
        ),
        ("h2", "Debugging"),
        (
            "p",
            "A **syntax error** stops the program before it runs: a missing colon, a bad indent, a bracket left open. A **logic error** runs and gives the wrong answer. The second kind is why we test. Code inside a function is easier to test because you can call it with a known input and look at the returned value. A long script that only runs from `input()` makes you type the same data on every attempt.",
        ),
        (
            "p",
            "A **dry run** is a paper trace of the variables. A **breakpoint** is a mark in the debugger where execution pauses so you can see those variables in the middle of a run. Until you are fluent with the debugger, a temporary `print` of the index and the value is an honest tool. Remove those prints before you submit the practical, or label them clearly as checks.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — a fault in a loop",
                "text": (
                    "A student writes `for index in range(1, len(marks))` and never sees the first mark. "
                    "`range` starts at 1, but the first index is 0, so `marks[0]` is skipped. "
                    "The dry run of the list [40, 50] shows index 1 only. The fix is `range(len(marks))`. "
                    "The same trace would have caught an off-by-one in pseudocode last lecture."
                ),
            },
        ),
        (
            "callout",
            {
                "kind": "exam",
                "title": "Exam tip",
                "text": "In a program question, write the imports, then the functions, then the calls. Show one sample run underneath: the input you imagined and the output the code produces. Markers give method marks for a sensible structure even if a colon is missing, and output marks only when the sample is consistent with the code.",
            },
        ),
    ],
    terms=[
        ("IDE", "Editor, runner, console, file list, and debugger in one place."),
        ("Variable", "A name bound to a value."),
        ("Selection", "`if`, `elif`, and `else`."),
        ("Repetition", "`while` or `for`, with an indented body."),
        ("Turtle", "A drawing pen controlled by distances, turns, and pen-up."),
        ("Library", "Tested code you import and use through a small set of names."),
        ("List", "An ordered collection. The first index is 0."),
        ("Function", "A named, testable block. Parameters in, a return value out."),
        ("Scope", "Where a name is visible. A variable inside a function is local."),
        ("Breakpoint", "A pause in the debugger so you can inspect variables."),
    ],
    checks=[
        {
            "q": "What does `range(5)` produce?",
            "a": "0, 1, 2, 3, 4. Five numbers, starting at 0, stopping before 5.",
        },
        {
            "q": "Why must the result of `input()` be converted before you compare it with 40?",
            "a": "`input()` returns a string. Comparing the string \"40\" with the number 40 is not the numeric test you wanted, and subtracting from a string is an error.",
        },
        {
            "q": "What is the index of the value 8 in `[8, 3, 8]` if your loop returns the first match?",
            "a": "0. The later 8 is at index 2 and is not returned.",
        },
    ],
    mcqs=[
        {
            "q": "Which line correctly tests equality?",
            "options": ["if marks = 40:", "if marks == 40:", "if marks eq 40:", "if marks := 40"],
            "answer": "B",
            "why": "`==` compares. A single `=` assigns and is illegal in this `if`.",
        },
        {
            "q": "To move the turtle without drawing, you call",
            "options": ["penup()", "hide()", "color(\"white\")", "break"],
            "answer": "A",
            "why": "`penup` lifts the pen. Changing colour still draws.",
        },
        {
            "q": "A function returns a value with",
            "options": ["print", "return", "input", "import"],
            "answer": "B",
            "why": "`print` shows text. `return` hands a value back to the caller.",
        },
        {
            "q": "Using `math.sqrt` without studying its source is an example of",
            "options": ["decomposition only", "abstraction", "a syntax error", "white-box testing"],
            "answer": "B",
            "why": "The name hides the implementation behind an interface you can trust.",
        },
    ],
    shorts=[
        {
            "q": "Name four parts of an IDE and the job of each.",
            "a": "The editor holds the code. The runner executes the file. The console shows output and accepts input. The debugger pauses at a breakpoint so variables can be inspected. A file list is the fifth, useful part.",
        },
        {
            "q": "Write a function that takes a Celsius value and returns Fahrenheit. Show the call for 0.",
            "a": "def celsius_to_fahrenheit(celsius): return celsius * 9 / 5 + 32. The call celsius_to_fahrenheit(0) returns 32.0. The formula is the familiar multiply by 9/5 and add 32.",
        },
        {
            "q": "Explain one logic error that a dry run catches and a syntax checker does not.",
            "a": "Starting a list loop at 1 instead of 0 is valid Python, so the program runs. The dry run shows that the first item is never examined. The syntax checker has nothing to report.",
        },
    ],
    longs=[
        {
            "marks": 5,
            "q": "A stationer sells copies at a given rate and charges a flat packing fee. Write a Python program that defines a function for the bill, reads the number of copies, the rate, and the packing fee, and prints the total. Explain how you would test the function.",
            "a": (
                "def bill(copies, rate, packing):\n"
                "    return copies * rate + packing\n\n"
                "copies = int(input(\"Copies: \"))\n"
                "rate = float(input(\"Rate: \"))\n"
                "packing = float(input(\"Packing: \"))\n"
                "print(bill(copies, rate, packing))\n\n"
                "Test the function without input first. bill(2, 100, 20) must return 220. bill(0, 100, 20) must return 20. "
                "A wrong formula such as adding the packing inside the multiplication fails the second test. "
                "Because the function returns a number, the test does not depend on reading the screen."
            ),
        },
        {
            "marks": 5,
            "q": "Describe a turtle program that draws a square of side 100 and then a circle that does not sit on the square’s outline. State the role of the loop and of penup.",
            "a": (
                "Import turtle and create a turtle. Loop four times: forward 100, right 90. That repetition is the square; the angle is 90 because a square turns a full 360 degrees in four equal turns. "
                "Then penup, goto a point inside or clearly beside the square, pendown, and circle with a radius small enough not to cross the outline, for example 20. "
                "penup is required so the move between the shapes does not leave a line. pendown is required before the circle or the circle will not appear. "
                "A compound drawing is just sequence plus one loop, with the pen state managed between shapes."
            ),
        },
    ],
    labs=[
        {
            "title": "Lab 4 — Decisions, loops, and a function",
            "steps": [
                "Type the marks program with if, elif, and else. Run it for 80, 40, and 39.",
                "Write celsius_to_fahrenheit and print the results for 0 and 100 before you add input().",
                "Build a list of five integers using a loop and append. Search for a value that is present and a value that is absent.",
                "Dry-run the search on paper for the present value and compare it with the program’s index.",
            ],
            "success": "0 °C prints 32.0 and 100 °C prints 212.0. The search index matches your paper trace, and the missing value prints Not found.",
        },
        {
            "title": "Lab 5 — Turtle compound shape",
            "steps": [
                "Draw a square using a loop.",
                "Lift the pen, move, lower the pen, and draw a circle.",
                "Change the square into a regular hexagon by turning 60 degrees. Record the angle you chose and why.",
            ],
            "success": "The two shapes are separate, the hexagon closes, and your journal states that the exterior turn is 360 divided by the number of sides.",
        },
    ],
    summary=[
        "A program is input, process, and output. The IDE is where you edit, run, and debug.",
        "`input()` returns text. Convert it before arithmetic. `==` compares; `=` assigns.",
        "Indentation is the structure. `elif` is the second test. `range` stops before the end value.",
        "Turtle: forward, turn, penup, pendown, circle. A regular polygon turns 360 divided by the number of sides.",
        "Importing `math` is abstraction: you use a name and not the internal method.",
        "List indexes start at 0. Do not use 0 as a not-found flag.",
        "Functions take parameters and return results. Test the return value. Dry-run logic errors; the syntax checker will not see them.",
    ],
)
