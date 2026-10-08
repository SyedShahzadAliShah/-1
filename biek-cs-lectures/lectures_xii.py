"""Original Class XII lectures for BIEK Computer Science Paper II."""

META = {
    "pdf_title": "BIEK Computer Science XII — Lecture Notes",
    "class_label": "Class XII",
    "running_header": "Computer Science  ·  Class XII  ·  Paper II",
    "cover_lines": ["Computer Science", "Class XII Lectures"],
    "cover_sub": "Paper II  ·  Option I (C) or Option II (Visual Basic)  ·  Model Paper 2026",
    "cover_foot": "75 marks  ·  Choose one programming option and stay with it",
    "intro": (
        "Paper II is one sitting with two independent options. Option I is Programming Using C. "
        "Option II is Programming Using Visual Basic. Choose the option your college taught, and "
        "do not mix them in one answer script. Database questions are set inside both options, "
        "so Lectures 12 to 14 are for every candidate. Lectures 1 to 7 are Option I. Lectures 8 to 11 "
        "are Option II. Lecture 15 is a drill for both. These notes follow the BIEK Model Paper 2026. "
        "They use C and Visual Basic 6, which is the style of that paper, not C++ and not VB.NET."
    ),
    "pattern_headers": ["Section", "What you do", "Marks"],
    "pattern_rows": [
        ["A  MCQs", "All 15 questions of the option you chose. One mark each.", "15"],
        ["B  Short", "Any ten part questions. Programs, differences and definitions. About six or seven lines, or a short program.", "30"],
        ["C  Detailed", "Any three questions. A program explanation, operators, functions, arrays, data models or Access data types.", "30"],
    ],
    "pattern_widths": [90, 340, 70],
    "pattern_note": (
        "A program answer needs the include line or the event procedure, the declarations, the input, the processing and the output. "
        "Write one comment only if it helps. Trace a loop for a small input when the question gives a hint, such as 4! = 24. "
        "Database answers need the term, then an example from a table you invent and stick to."
    ),
}

LECTURES = [
    {
        "number": 1,
        "title": "The Shape of a C Program",
        "meta": "Option I  ·  Two periods  ·  Structure, #include, #define, reserved words",
        "outcomes": [
            "Write the skeleton of a C program that prints one line.",
            "Explain #include and #define with an example of each.",
            "State the rules of an identifier and name reserved words.",
            "Distinguish scanf from getchar.",
        ],
        "blocks": [
            {"kind": "h2", "text": "What you are being asked to write"},
            {
                "kind": "p",
                "text": "C is a high-level language designed by Dennis Ritchie. A compiler translates your source program into object code the processor can run. Every complete program in this option has a function called **main**. The machine starts there. A program with no main does not have a starting point, which is why the multiple-choice line “the only function all C programs must contain” is **main**.",
            },
            {
                "kind": "code",
                "caption": "Program 1.1  The smallest honest program. It prints one line and ends cleanly.",
                "text": r"""#include <stdio.h>

int main(void) {
    printf("Computer Science\n");
    return 0;
}""",
            },
            {
                "kind": "p",
                "text": "Read it from the top. `#include <stdio.h>` asks the preprocessor to bring in the standard input/output header, which declares `printf` and `scanf`. The line `int main(void)` starts the main function and promises that it returns an integer and takes no arguments. `printf` sends text to the screen. `\\n` inside the quotes moves to the next line. `return 0` tells the operating system that the program finished normally. Comments, which the compiler ignores, sit between `/*` and `*/`.",
            },
            {
                "kind": "tip",
                "title": "Turbo C in the college lab",
                "text": "Some labs still use Turbo C and write void main, clrscr and getch from conio.h. The board marks the logic. Prefer the form above when you are writing on the answer script: stdio.h, int main, and return 0. If your teacher has drilled the Turbo C form, either is accepted when the program is otherwise correct. Do not mix clrscr into a program and then forget stdio.h.",
            },
            {"kind": "h2", "text": "#include and #define"},
            {
                "kind": "p",
                "text": "Both lines are **preprocessor directives**. They are handled before compilation. They have no semicolon.",
            },
            {
                "kind": "table",
                "headers": ["Directive", "Job", "Example"],
                "rows": [
                    ["#include", "Inserts a header so you can call its functions", "#include <stdio.h>"],
                    ["#define", "Gives a name to a constant or a short macro. The name is replaced by the value before compile time", "#define PI 3.1416"],
                ],
                "widths": [90, 250, 160],
            },
            {
                "kind": "code",
                "caption": "Program 1.2  #define used for a constant. There is no equals sign and no semicolon on the define line.",
                "text": r"""#include <stdio.h>
#define PI 3.1416

int main(void) {
    float r = 7;
    printf("Area = %f\n", PI * r * r);
    return 0;
}""",
            },
            {
                "kind": "board",
                "title": "Two examples, as the question asks",
                "text": "#include <stdio.h> brings in printf and scanf. #include <math.h> brings in fabs and sqrt. #define MAX 100 replaces every MAX with 100. #define PI 3.1416 replaces PI with the value. That is four legal examples. Two are enough.",
            },
            {"kind": "h2", "text": "Names, reserved words and comments"},
            {
                "kind": "p",
                "text": "An **identifier** is a name you invent for a variable, a constant or a function. It may contain letters, digits and underscores. It must start with a letter or an underscore. It must not be a reserved word. `Number`, `NUMBER5` and `Number_5` are legal. `5number` is not, because it starts with a digit. C treats `Marks` and `marks` as different names.",
            },
            {
                "kind": "p",
                "text": "A **reserved word** already has a meaning in the language, so you cannot use it as a variable name. Learn a working list: `int`, `float`, `char`, `double`, `void`, `if`, `else`, `for`, `while`, `do`, `switch`, `case`, `break`, `continue`, `return`, `struct`. The question “name any three” is that list. Do not invent words such as `print` or `loop` and call them reserved.",
            },
            {
                "kind": "define",
                "title": "scanf and getchar",
                "text": "scanf reads formatted input. You give a format and the address of the variable: scanf(\"%d\", &n) reads an integer into n. getchar reads exactly one character and returns it. scanf can skip spaces and read a whole number. getchar does not format the input; the next character, which might be a newline left behind, is what you get.",
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "Every complete C program must contain:",
                    "opts": ["A) start()", "B) getch()", "C) main()", "D) clrscr()"],
                    "ans": "C",
                    "why": "Execution begins at main.",
                },
                {
                    "q": "Which identifier is illegal?",
                    "opts": ["A) Number", "B) 5number", "C) NUMBER5", "D) Number_5"],
                    "ans": "B",
                    "why": "An identifier cannot start with a digit.",
                },
                {
                    "q": "C was designed by:",
                    "opts": ["A) Dennis Ritchie", "B) Charles Babbage", "C) Tim Berners-Lee", "D) Bill Gates"],
                    "ans": "A",
                    "why": "Ritchie designed C. Babbage belongs with early mechanical computing.",
                },
            ],
            "short": [
                {
                    "q": "Write the basic structure of a C program.",
                    "a": "A C program includes the headers it needs, then defines main. Execution starts at main. A minimal program is: #include <stdio.h> then int main(void) { printf(\"Hello\\n\"); return 0; }. The include line has no semicolon. return 0 ends main successfully.",
                },
                {
                    "q": "Define #include and #define. Give one example of each.",
                    "a": "#include is a preprocessor directive that inserts a header file. Example: #include <stdio.h> provides printf and scanf. #define gives a name to a value that is substituted before compilation. Example: #define PI 3.1416. Neither directive ends with a semicolon.",
                },
            ],
            "long": [],
        },
    },
    {
        "number": 2,
        "title": "Data Types, Operators and Expressions",
        "meta": "Option I  ·  Two periods  ·  A Section C question is “types of operators”",
        "outcomes": [
            "Choose int, float, double or char and the matching printf or scanf code.",
            "List the operator families with one example each.",
            "Evaluate an integer expression left to right, showing the working.",
            "Rewrite an algebraic formula as a legal C expression.",
        ],
        "blocks": [
            {"kind": "h2", "text": "The types you actually use"},
            {
                "kind": "table",
                "headers": ["Type", "Holds", "Format for printf / scanf"],
                "rows": [
                    ["int", "Whole numbers", "%d"],
                    ["float", "Numbers with a fractional part, single precision", "%f"],
                    ["double", "Fractional numbers with more precision", "%lf in scanf, %f in printf"],
                    ["char", "One character", "%c"],
                    ["void", "No value. Used for a function that returns nothing", "none"],
                ],
                "widths": [80, 230, 190],
            },
            {
                "kind": "p",
                "text": "Declare a variable before you use it: `int marks;` or `float average;`. You can initialise as you declare: `int n = 0;`. A constant that must not change can be written with `#define` or with `const int PASS = 40;`. The `%` operator, remainder, is only for integers. `10 % 3` is 1. You do not write `%` on a float.",
            },
            {"kind": "h2", "text": "Families of operators"},
            {
                "kind": "p",
                "text": "A Section C answer is this table turned into sentences, plus one line of code for each family. Arithmetic operators do the calculation. Relational operators compare and give 1 or 0. Logical operators join comparisons. Assignment stores a value. Increment and decrement change a variable by one.",
            },
            {
                "kind": "table",
                "headers": ["Family", "Operators", "Example and result"],
                "rows": [
                    ["Arithmetic", "+  −  *  /  %", "If a is 7, a % 2 is 1. Integer 7 / 2 is 3, not 3.5"],
                    ["Relational", "<  >  <=  >=  ==  !=", "marks >= 40 is 1 when the student has passed"],
                    ["Logical", "&&  ||  !", "age >= 16 && age <= 19 is true only when both tests are true"],
                    ["Assignment", "=  +=  −=", "n += 2 means n = n + 2"],
                    ["Increment", "++  −−", "n++ uses n, then adds 1. ++n adds 1, then uses n"],
                ],
                "widths": [90, 120, 290],
            },
            {
                "kind": "p",
                "text": "Among `+`, `−`, `/` and `%`, the higher precedence belongs to `/` and `%`, equally. They are done before addition and subtraction, and from left to right when they sit together. `*` has that same high level. So `a + b * c` multiplies first. Use brackets whenever you are not certain. Brackets also make an exam expression readable, and readable working scores.",
            },
            {
                "kind": "board",
                "title": "Post-increment",
                "text": "k++ is post-increment: the current value of k is used, then k becomes k + 1. ++k is pre-increment: k increases first, then the new value is used. The multiple-choice phrase “an example of a post-increment operator” is k++.",
            },
            {"kind": "h2", "text": "Integer expressions, worked the way the paper sets them"},
            {
                "kind": "p",
                "text": "Let `a = 2`, `b = 5` and `c = 10`, all integers. Show every step. Integer division throws away the fraction.",
            },
            {
                "kind": "table",
                "headers": ["Expression", "Working", "Result"],
                "rows": [
                    ["200 * ((a * 10) + c)", "a * 10 = 20; 20 + 10 = 30; 200 * 30 = 6000", "6000"],
                    ["a * b * 10 / c + a + c", "2 * 5 = 10; 10 * 10 = 100; 100 / 10 = 10; 10 + 2 = 12; 12 + 10 = 22", "22"],
                    ["a - (c / b) / 2 + 100", "10 / 5 = 2; 2 / 2 = 1; 2 − 1 + 100 = 101", "101"],
                ],
                "widths": [150, 280, 70],
            },
            {"kind": "h2", "text": "Algebra into C"},
            {
                "kind": "p",
                "text": "C has no superscripts and no implied multiplication. `3ab` must become `3 * a * b`. A fraction needs a slash. A square is a name multiplied by itself. The absolute value needs `fabs` from `math.h`.",
            },
            {
                "kind": "table",
                "headers": ["Mathematics", "Legal C"],
                "rows": [
                    ["A = (1/2) × base × height", "A = 0.5 * base * height;"],
                    ["x = 3ab³ + 3a²b", "x = 3 * a * b * b * b + 3 * a * a * b;"],
                    ["d = |b² − 4ac|", "d = fabs(b * b - 4 * a * c);"],
                    ["area = πr²", "area = 3.1416 * r * r;"],
                ],
                "widths": [220, 280],
            },
            {
                "kind": "tip",
                "title": "The half that becomes zero",
                "text": "If base and height are integers, writing (1/2) * base * height gives 0, because 1/2 in integer arithmetic is 0. Write 0.5, or divide by 2.0. This is the mistake that turns a correct formula into a wrong program.",
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "The % operator is used with:",
                    "opts": ["A) float only", "B) int", "C) a string", "D) char only"],
                    "ans": "B",
                    "why": "Remainder is defined for integers.",
                },
                {
                    "q": "Which is a post-increment?",
                    "opts": ["A) ++k", "B) k++", "C) k += 1 written as a comparison", "D) k == 1"],
                    "ans": "B",
                    "why": "The plus signs come after the variable.",
                },
            ],
            "short": [
                {
                    "q": "If a = 2, b = 5 and c = 10, all int, find the value of a * b * 10 / c + a + c. Show the working.",
                    "a": "Work left to right for * and /. 2 * 5 = 10. 10 * 10 = 100. 100 / 10 = 10. Then 10 + a + c = 10 + 2 + 10 = 22. The result is 22.",
                },
                {
                    "q": "Convert these into C: A = (1/2) × base × height, and d = |b² − 4ac|.",
                    "a": "A = 0.5 * base * height; and, after #include <math.h>, d = fabs(b * b - 4 * a * c);. Do not write 1/2 as an integer division if you need a half, because 1/2 is 0 in integer arithmetic.",
                },
            ],
            "long": [
                {
                    "q": "What are the different types of operators used in a C program? Explain with examples.",
                    "a": "An operator is a symbol that asks C to do something to its operands. Arithmetic operators are + − * / and %. If n is 7, n % 2 is 1, and integer 7/2 is 3. Relational operators are < > <= >= == and !=. They compare two values and give 1 or 0, as in marks >= 40. Logical operators are &&, || and !. They join conditions: age >= 16 && age <= 19. Assignment operators store a result: n = 5 and n += 2. Increment and decrement are ++ and −−. k++ is post-increment. / and % are done before + and −. Brackets force the order you want. The % operator is only for integers.",
                }
            ],
        },
    },
    {
        "number": 3,
        "title": "Decisions and the switch Statement",
        "meta": "Option I  ·  Two periods  ·  Section C asks for switch with a logical diagram",
        "outcomes": [
            "Write if, if-else and else-if for a mark sheet or a larger-of-two test.",
            "Draw switch as a choice among cases, each closed by break.",
            "Explain what happens when break is omitted.",
        ],
        "blocks": [
            {"kind": "h2", "text": "if, else, and a chain of tests"},
            {
                "kind": "p",
                "text": "A decision runs one block and skips another. The condition in brackets is tested. If it is true (not zero), the first block runs. `else` is the path when the test fails. A chain of `else if` is used when there are several bands, such as grades. The first true test wins, and the rest are skipped.",
            },
            {
                "kind": "code",
                "caption": "Program 3.1  Pass and fail. One test, two paths.",
                "text": r"""#include <stdio.h>

int main(void) {
    int marks;
    printf("Enter marks: ");
    scanf("%d", &marks);
    if (marks >= 40)
        printf("Pass\n");
    else
        printf("Fail\n");
    return 0;
}""",
            },
            {
                "kind": "code",
                "caption": "Program 3.2  Three grades. The tests are in order, highest band first.",
                "text": r"""#include <stdio.h>

int main(void) {
    int marks;
    printf("Enter marks: ");
    scanf("%d", &marks);
    if (marks >= 80)
        printf("Grade A\n");
    else if (marks >= 60)
        printf("Grade B\n");
    else if (marks >= 40)
        printf("Grade C\n");
    else
        printf("Fail\n");
    return 0;
}""",
            },
            {
                "kind": "tip",
                "title": "Use == when you compare",
                "text": "A single = stores a value. A double == compares. if (choice = 1) assigns 1 and is always true. if (choice == 1) asks the question you meant. This is the most common logic error in a decision.",
            },
            {"kind": "h2", "text": "switch"},
            {
                "kind": "p",
                "text": "`switch` chooses among constant values of one integer or character expression. Each `case` labels one value. `break` leaves the switch. `default` runs when no case matches. It is the right tool when you are matching a menu number or a day number, not when you are testing ranges such as “80 and above”.",
            },
            {
                "kind": "flow",
                "steps": [
                    "Evaluate the switch expression once",
                    "Compare it with case 1. If it matches, run that block, then break",
                    "Otherwise compare it with case 2, and so on",
                    "If nothing matches, run default",
                    "Continue with the statement after the switch",
                ],
                "caption": "Figure 3.1  Logical diagram of switch. Each case ends in break so control does not fall into the next case.",
            },
            {
                "kind": "code",
                "caption": "Program 3.3  A menu. break stops a match from falling into the next printf.",
                "text": r"""#include <stdio.h>

int main(void) {
    int choice;
    printf("1 Add  2 Subtract: ");
    scanf("%d", &choice);
    switch (choice) {
        case 1:
            printf("You chose add\n");
            break;
        case 2:
            printf("You chose subtract\n");
            break;
        default:
            printf("No such option\n");
    }
    return 0;
}""",
            },
            {
                "kind": "p",
                "text": "If you delete the `break` after case 1, a choice of 1 prints both lines. C does not leave the switch at the end of a case by itself. That fall-through is the fact a long answer must mention. `default` does not need a break if it is the last label, but writing one does no harm.",
            },
            {
                "kind": "board",
                "title": "10-mark shape for switch",
                "text": "Define switch in two lines. Draw the diagram: expression, then arrows to case 1, case 2 and default, each case arrow continuing out only after break. Then write Program 3.3. End with one sentence: without break, execution falls into the next case.",
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "Which operator compares two values for equality?",
                    "opts": ["A) =", "B) ==", "C) !=", "D) +="],
                    "ans": "B",
                    "why": "A single equals sign assigns. Two equals signs compare.",
                }
            ],
            "short": [
                {
                    "q": "Why is break written at the end of a case?",
                    "a": "break leaves the switch as soon as that case has run. Without it, C continues into the next case and runs that code as well. This is called fall-through. default handles every value that matched no case.",
                }
            ],
            "long": [
                {
                    "q": "Define the switch statement and draw its logical diagram.",
                    "a": "switch selects one path according to the value of an integer or character expression. The expression is evaluated once and compared with each case label. The matching case runs until break, which leaves the switch. If no case matches, default runs. Diagram: a box for the expression, arrows to case 1, case 2 and default, and from each case an arrow labelled break that joins the statement after the switch. Example: switch(choice) { case 1: printf(\"Add\"); break; case 2: printf(\"Subtract\"); break; default: printf(\"Error\"); }. Omitting break makes case 1 fall into case 2.",
                }
            ],
        },
    },
    {
        "number": 4,
        "title": "Loops, break and continue",
        "meta": "Option I  ·  Two periods  ·  Tables, factorials and number patterns",
        "outcomes": [
            "Choose for, while or do-while and say why.",
            "Write a multiplication table and a factorial loop.",
            "Distinguish break from continue.",
            "Print a number triangle with a nested loop.",
        ],
        "blocks": [
            {"kind": "h2", "text": "Three loops, one idea"},
            {
                "kind": "p",
                "text": "A loop repeats a block. `for` is the one to reach for when you know how many times, or when you are counting. `while` tests the condition before the body, so the body may never run. `do-while` runs the body once and then tests, so the body always runs at least once. A `for` loop is an iteration statement, not a selection statement. Selection is `if` and `switch`.",
            },
            {
                "kind": "table",
                "headers": ["Loop", "Test", "Use it for"],
                "rows": [
                    ["for", "Before each pass, after an initialisation", "A table from 1 to 10, a pattern of 5 rows"],
                    ["while", "Before the body", "Reading numbers until the user types a sentinel, when the count is unknown"],
                    ["do-while", "After the body", "A menu that must be shown at least once"],
                ],
                "widths": [80, 200, 220],
            },
            {
                "kind": "code",
                "caption": "Program 4.1  Multiplication table. Change only the limit if the question asks for 1 to 10.",
                "text": r"""#include <stdio.h>

int main(void) {
    int n, i;
    printf("Enter a number: ");
    scanf("%d", &n);
    for (i = 1; i <= 10; i++)
        printf("%d x %d = %d\n", n, i, n * i);
    return 0;
}""",
            },
            {
                "kind": "code",
                "caption": "Program 4.2  Factorial. For input 4 the trace is 1, 2, 6, 24.",
                "text": r"""#include <stdio.h>

int main(void) {
    int n, i;
    long fact = 1;
    printf("Enter a number: ");
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
        fact = fact * i;
    printf("Factorial = %ld\n", fact);
    return 0;
}""",
            },
            {
                "kind": "p",
                "text": "Trace for 4, which the hint 4! = 24 is asking you to understand. Start with fact = 1. i = 1 gives 1. i = 2 gives 2. i = 3 gives 6. i = 4 gives 24. Then i becomes 5 and the loop stops. `long` is used because factorials grow quickly. The program as written is for a non-negative n. Say that in one line if you have room.",
            },
            {"kind": "h2", "text": "break and continue"},
            {
                "kind": "define",
                "title": "break and continue",
                "text": "break leaves the loop at once and continues after it. continue skips the rest of this pass and goes to the next test of the loop. break is an exit. continue is a skip.",
            },
            {
                "kind": "code",
                "caption": "Program 4.3  continue skips 3. The loop still finishes. break would have stopped it.",
                "text": r"""#include <stdio.h>

int main(void) {
    int i;
    for (i = 1; i <= 5; i++) {
        if (i == 3)
            continue;
        printf("%d\n", i);
    }
    return 0;
}""",
            },
            {
                "kind": "p",
                "text": "The output is 1, 2, 4, 5. The number 3 is skipped, not used as a reason to abandon the loop. The multiple-choice line “skip the rest of a loop and carry on from the top” is **continue**. `break` would print 1 and 2 only.",
            },
            {"kind": "h2", "text": "Nested loops and the two patterns"},
            {
                "kind": "p",
                "text": "An inner loop finishes all of its passes for one pass of the outer loop. For a triangle, the outer loop is the row and the inner loop is how many numbers are printed on that row.",
            },
            {
                "kind": "code",
                "caption": "Program 4.4  Prints 1 / 12 / 123 / 1234 / 12345.",
                "text": r"""#include <stdio.h>

int main(void) {
    int row, col;
    for (row = 1; row <= 5; row++) {
        for (col = 1; col <= row; col++)
            printf("%d", col);
        printf("\n");
    }
    return 0;
}""",
            },
            {
                "kind": "code",
                "caption": "Program 4.5  Number and its square. A single loop is the honest tool. Nesting is not required for this pattern.",
                "text": r"""#include <stdio.h>

int main(void) {
    int n;
    printf("Number  Square\n");
    for (n = 1; n <= 5; n++)
        printf("%d       %d\n", n, n * n);
    return 0;
}""",
            },
            {
                "kind": "p",
                "text": "The square of 1 is 1, of 2 is 4, of 3 is 9, of 4 is 16, of 5 is 25. If a question insists on nested loops for this second pattern, you can still use Program 4.4’s shape and print `row` and `row * row` from the outer loop only. Do not invent an inner loop that does nothing useful.",
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "A for loop is used for:",
                    "opts": ["A) Selection", "B) Iteration", "C) Compilation", "D) Linking only"],
                    "ans": "B",
                    "why": "Iteration means repetition. if and switch select.",
                },
                {
                    "q": "Which statement starts the next pass of a loop immediately?",
                    "opts": ["A) break", "B) continue", "C) return from the operating system", "D) #define"],
                    "ans": "B",
                    "why": "break leaves the loop. continue skips to the next pass.",
                },
            ],
            "short": [
                {
                    "q": "Differentiate break and continue.",
                    "a": "break ends the loop at once. The statement after the loop runs next. continue skips the rest of the current pass and starts the next pass of the same loop. In a loop from 1 to 5, continue when i is 3 prints 1 2 4 5. break when i is 3 prints 1 2.",
                },
                {
                    "q": "Write a program that prints the factorial of an inputted number.",
                    "a": "Use the program in this lecture: read n, set fact to 1, multiply fact by i for i from 1 to n, and print fact. For n = 4 the running product is 1, 2, 6, 24. Use long so the result has room to grow.",
                },
            ],
            "long": [],
        },
    },
    {
        "number": 5,
        "title": "Functions",
        "meta": "Option I  ·  Two periods  ·  Section C: characteristics of a function, with an example",
        "outcomes": [
            "Name the parts of a function: return type, name, parameters and body.",
            "Write a function that returns the greater of two integers.",
            "Distinguish the definition, the call and a prototype.",
            "Say what return does.",
        ],
        "blocks": [
            {"kind": "h2", "text": "Why a function exists"},
            {
                "kind": "p",
                "text": "A function is a named block of statements that does one job and can be used again. `main` is a function. `printf` is a function someone else wrote. A user-defined function is one you write, such as `greater`. Using functions keeps `main` readable, lets you test one job at a time, and avoids copying the same loop into five places.",
            },
            {
                "kind": "define",
                "title": "The four parts",
                "text": "A function has a return type (what it sends back, or void), a name, a parameter list in brackets (the values it receives), and a body in braces (the statements that do the work). Together, the first three are the heading. The body is the definition of what it does.",
            },
            {
                "kind": "code",
                "caption": "Program 5.1  greater returns the larger of two integers. main only reads, calls and prints.",
                "text": r"""#include <stdio.h>

int greater(int x, int y) {
    if (x > y)
        return x;
    else
        return y;
}

int main(void) {
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    printf("Greater = %d\n", greater(a, b));
    return 0;
}""",
            },
            {
                "kind": "p",
                "text": "Walk through 8 and 3. `main` reads them into `a` and `b`. The call `greater(a, b)` copies 8 into `x` and 3 into `y`. These are different variables. Changing `x` would not change `a`, because C passes arguments **by value**. The `return` sends 8 back, and `printf` prints it. If the numbers are equal, the `else` path returns `y`, which is correct because neither is larger.",
            },
            {"kind": "h2", "text": "Prototype, definition and call"},
            {
                "kind": "table",
                "headers": ["Piece", "What it is", "Where it sits"],
                "rows": [
                    ["Prototype", "A declaration of the heading, ending in a semicolon, with no body", "Above main, if the function is written below main"],
                    ["Definition", "The heading plus the body", "Program 5.1 defines greater above main, so no separate prototype is required"],
                    ["Call", "The use of the function, passing actual values", "greater(a, b) inside main"],
                ],
                "widths": [90, 230, 180],
            },
            {
                "kind": "p",
                "text": "`return` does two things: it sends a value back to the caller, and it ends the function immediately. A `void` function may use `return;` with no value just to stop early. The last statement of a function that promised an `int` should be a `return` of an `int`.",
            },
            {
                "kind": "board",
                "title": "Characteristics, for the long question",
                "text": "A function has a name, a return type, parameters and a body. It is called by name. It can return one value. It can be called many times. Arguments are passed by value unless you later learn pointers. It makes the program modular. Then write Program 5.1 and trace 8 and 3.",
            },
            {
                "kind": "p",
                "text": "The person who writes programs in a language such as C is a **programmer**. The tool that turns the C source into machine code is a **compiler**, not an assembler and not an editor. The editor only types the text. Those two one-mark answers sit next to this lecture because this is where you meet the finished program.",
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "A C program is translated into machine code by a:",
                    "opts": ["A) Compiler", "B) Scanner", "C) Browser", "D) Hub"],
                    "ans": "A",
                    "why": "The editor types the source. The compiler translates it.",
                },
                {
                    "q": "Comments in C are written between:",
                    "opts": ["A) /* and */", "B) // only, with no other form", "C) < and >", "D) # and ;"],
                    "ans": "A",
                    "why": "/* comment */ is the form every C compiler accepts. // is also allowed in modern C, but the paper’s symbols are /* and */.",
                },
            ],
            "short": [
                {
                    "q": "Write a function that prints the greater of two inputted numbers.",
                    "a": "Define int greater(int x, int y) which returns x if x > y and otherwise returns y. In main, read a and b with scanf, then printf the value returned by greater(a, b). Arguments are passed by value.",
                }
            ],
            "long": [
                {
                    "q": "What are the main characteristics of a function? Describe them with an example.",
                    "a": "A function is a named block that performs one job. Its characteristics are: it has a return type, a name and a parameter list; it has a body; it is executed only when it is called; it returns at most one value with return; and the same function can be called many times, which keeps the program shorter and easier to test. In C, the values sent in are copied (pass by value). Example: int greater(int x, int y) returns x when x is larger and y otherwise. main reads two integers and prints greater(a, b). For 8 and 3 the returned value is 8. printf and scanf are library functions; greater is user-defined.",
                }
            ],
        },
    },
    {
        "number": 6,
        "title": "Arrays",
        "meta": "Option I  ·  One to two periods  ·  Needed for lists, totals and for questions that cross over from the programming syllabus",
        "outcomes": [
            "Declare, initialise and index a one-dimensional array.",
            "Find the total and the average with a loop.",
            "State that the first index is 0 and the last is size minus one.",
        ],
        "blocks": [
            {"kind": "h2", "text": "One name, many values of the same type"},
            {
                "kind": "define",
                "title": "Array",
                "text": "An array is a collection of values of the same type, stored one after another under one name. Each value is an element. An element is reached by an index.",
            },
            {
                "kind": "p",
                "text": "`int marks[5];` creates five integers: `marks[0]` through `marks[4]`. There is no `marks[5]`. Using that index steps off the end of the array. This is the error to mention even if you are not asked, because it shows you understand the size. You may initialise in the declaration: `int marks[5] = {70, 81, 64, 90, 55};`.",
            },
            {
                "kind": "code",
                "caption": "Program 6.1  Total and average of five marks. The loop index is the array index.",
                "text": r"""#include <stdio.h>

int main(void) {
    int marks[5];
    int i, sum = 0;
    for (i = 0; i < 5; i++) {
        printf("Enter marks: ");
        scanf("%d", &marks[i]);
        sum = sum + marks[i];
    }
    printf("Total = %d\n", sum);
    printf("Average = %f\n", sum / 5.0);
    return 0;
}""",
            },
            {
                "kind": "p",
                "text": "The address operator is on `marks[i]`, not on the whole array name, because `scanf` needs the address of the element being read. Dividing by `5.0` forces a fractional average. Dividing by the integer 5 would chop the fraction.",
            },
            {
                "kind": "p",
                "text": "A two-dimensional array is a table: `int grid[3][3];` has three rows and three columns, indexed from 0. You need two nested loops, the outer for the row and the inner for the column. Paper II’s C option rarely asks for a matrix. Know the declaration and the idea that it is a table of one type. Do not start using C++ `string` or `cin` here. A short text is a character array, `char name[20];`, read with a width-limited `scanf`.",
            },
            {
                "kind": "tip",
                "title": "Say the type of array in the first line",
                "text": "If a question says “explain an array and its types”, write: one-dimensional (a list) and two-dimensional (a table). Give one declaration of each. Then one loop for the list. Stop.",
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "In int a[5], the last legal index is:",
                    "opts": ["A) 5", "B) 4", "C) 6", "D) 1"],
                    "ans": "B",
                    "why": "Indexes run from 0 to size − 1.",
                }
            ],
            "short": [
                {
                    "q": "Declare an array of 5 integers and write a loop that reads values into it.",
                    "a": "int marks[5]; then for (i = 0; i < 5; i++) scanf(\"%d\", &marks[i]);. The first element is marks[0] and the last is marks[4]. The & is required because scanf needs the address of each element.",
                }
            ],
            "long": [],
        },
    },
    {
        "number": 7,
        "title": "C Programs for the Examination",
        "meta": "Option I  ·  A practical lecture  ·  Type every program, then write it from memory",
        "outcomes": [
            "Write, from a blank page, the table, factorial, greater-of-two and triangle programs.",
            "Trace the three integer expressions set with a = 2, b = 5, c = 10.",
            "Convert the standard algebraic formulas into C.",
        ],
        "blocks": [
            {"kind": "h2", "text": "How to practise a program question"},
            {
                "kind": "p",
                "text": "Close the notes. Write the program. Then type it, or trace it by hand if you are not at a machine. A program that you have only read will lose its braces under exam pressure. The four programs below are the set the paper keeps returning to. Database questions are in Lectures 12 to 14 and will sit in the same Section B.",
            },
            {"kind": "h3", "text": "1. Multiplication table"},
            {
                "kind": "p",
                "text": "Read n. Loop i from 1 to 10. Print n, i and n times i on each line. That is Program 4.1. If the question says “inputted number”, the scanf is compulsory. A table of a fixed 5, with no input, does not answer it.",
            },
            {"kind": "h3", "text": "2. Factorial"},
            {
                "kind": "p",
                "text": "Program 4.2. Under the program, write the trace for 4: fact becomes 1, 2, 6, 24. The hint in the question is there so that a correct trace confirms your loop. Starting fact at 0 ruins the answer, because every product stays 0.",
            },
            {"kind": "h3", "text": "3. Greater of two numbers, using a function"},
            {
                "kind": "p",
                "text": "Program 5.1. The question says “using function”. A program that compares inside main and never defines a second function misses the point. The function must return the value. Printing inside the function can be accepted, but returning is the cleaner match to “a function that returns”.",
            },
            {"kind": "h3", "text": "4. The two patterns"},
            {
                "kind": "p",
                "text": "Program 4.4 prints the triangle of numbers. Program 4.5 prints the number and its square. Write the output beside the program for one mark of confidence: the triangle’s third line is 123, and the square of 4 is 16.",
            },
            {"kind": "h3", "text": "5. Expressions and formulas"},
            {
                "kind": "p",
                "text": "From Lecture 2, with a = 2, b = 5, c = 10: the three results are 6000, 22 and 101. Show the working. Formula conversions: use 0.5 for a half, stars between every factor, `fabs` for an absolute value, and `r * r` for a square. Include `math.h` when you call `fabs`.",
            },
            {
                "kind": "tip",
                "title": "What a marker looks for",
                "text": "The header. The types. The & in scanf. The loop limits. The place where the answer is printed. A missing brace is serious. A missing comment is not. Do not spend ten minutes decorating the program.",
            },
        ],
        "checkpoint": {
            "mcq": [],
            "short": [
                {
                    "q": "Write a program that reads a number and prints its multiplication table.",
                    "a": "See Program 4.1. Include stdio.h, read n with scanf(\"%d\", &n), and for i from 1 to 10 print n, i and n * i. End main with return 0.",
                },
                {
                    "q": "Write a nested loop that prints 1, then 12, then 123, then 1234, then 12345.",
                    "a": "See Program 4.4. Outer loop row from 1 to 5. Inner loop col from 1 to row, printing col with no newline. After the inner loop, print a newline.",
                },
            ],
            "long": [],
        },
    },
    {
        "number": 8,
        "title": "Visual Basic: Forms and Controls",
        "meta": "Option II  ·  Two periods  ·  Text box, combo box, option button, check box",
        "outcomes": [
            "Name the parts of the VB design screen you use in every program.",
            "List the properties of a text box and of a combo box that the paper asks for.",
            "Choose a check box or an option button for the right kind of choice.",
            "Expand ADO, MDI, OLE, SQL and DBA.",
        ],
        "blocks": [
            {"kind": "h2", "text": "The screen you design on"},
            {
                "kind": "p",
                "text": "This option is Visual Basic 6, the form-based language in the BIEK paper, not VB.NET. You draw a **form**. On it you place **controls**. You set their **properties**. You write **code** in an event, usually the Click of a command button. The toolbox holds the controls. The properties window edits the selected control. The code window holds the procedures. A project is saved as a form file plus a project file. That is the environment. You do not need the menu history.",
            },
            {
                "kind": "table",
                "headers": ["Control", "What the user sees", "Typical job"],
                "rows": [
                    ["Label", "Text the user cannot edit", "A caption such as “Marks”"],
                    ["TextBox", "A box the user can type in", "Input, or a result you place in the Text property"],
                    ["CommandButton", "A button", "Runs the code in its Click event"],
                    ["OptionButton", "A round choice", "Exactly one from a group: male or female, or a payment method"],
                    ["CheckBox", "A square yes/no", "An independent choice. Several can be ticked. The value is checked or not, often thought of as 1 or 0"],
                    ["ListBox", "A list that stays open", "Pick one item from a visible list"],
                    ["ComboBox", "A text box with a drop-down list", "Pick an item, or type one, depending on Style"],
                ],
                "widths": [110, 160, 230],
            },
            {
                "kind": "p",
                "text": "Read the question’s verb. “One choice from a group” is an **option button**. “A yes or no that stands alone” is a **check box**. The paper sometimes phrases a check box as choosing yes (1) or no (0). That wording is the check box, because each box stores its own yes or no. It is not an option button, and it is not a command button.",
            },
            {"kind": "h2", "text": "Properties to memorise"},
            {
                "kind": "table",
                "headers": ["Control", "Properties worth writing"],
                "rows": [
                    ["TextBox", "Name, Text, Font, Enabled, Visible, MaxLength, MultiLine, PasswordChar, Locked"],
                    ["ComboBox", "Name, Text, List, Style, Sorted, Enabled, Visible"],
                    ["CommandButton", "Name, Caption, Enabled, Visible, Default, Cancel"],
                    ["Label", "Name, Caption, Font, AutoSize"],
                    ["Form", "Name, Caption, BackColor"],
                ],
                "widths": [110, 390],
            },
            {
                "kind": "p",
                "text": "`Name` is how the code talks to the control: `Text1.Text`. `Caption` is the words on a button or a label. A text box has **Text**, not Caption. `Enabled = False` shows the control but refuses clicks. `Visible = False` hides it. PasswordChar set to an asterisk hides a password as stars. `MaxLength` limits the characters. `MultiLine = True` allows more than one line. On a combo box, **List** is the set of items, **Text** is the current value, **Style** decides whether the user may type or only pick, and **Sorted** keeps the list in order.",
            },
            {
                "kind": "p",
                "text": "**ActiveX** controls are extra controls you add to the toolbox, beyond the ones that are there at the start. You need the name and that sentence. You do not need to install one in the exam.",
            },
            {"kind": "h2", "text": "Full forms that belong to this option"},
            {
                "kind": "table",
                "headers": ["Short form", "Full form", "One fact"],
                "rows": [
                    ["ADO", "ActiveX Data Objects", "A library VB uses to open a database and read records"],
                    ["MDI", "Multiple Document Interface", "A parent window that holds several child windows"],
                    ["OLE", "Object Linking and Embedding", "Placing an object from another program, such as a sheet or a picture, into yours"],
                    ["SQL", "Structured Query Language", "The language of relational database questions"],
                    ["DBA", "Database Administrator", "The person responsible for the database"],
                ],
                "widths": [80, 180, 240],
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "The default Step in For…Next is:",
                    "opts": ["A) 0", "B) 2", "C) 1", "D) −1"],
                    "ans": "C",
                    "why": "If you omit Step, the loop counts upward by 1. The loop itself is in the next lecture; the fact is a one-mark answer.",
                },
                {
                    "q": "A control used to pick exactly one option from a group is the:",
                    "opts": ["A) Check box, when several may be on", "B) Option button", "C) Label", "D) Timer"],
                    "ans": "B",
                    "why": "Option buttons in one group are mutually exclusive.",
                },
            ],
            "short": [
                {
                    "q": "List four properties of a text box.",
                    "a": "Name (the name in code), Text (the contents), MaxLength (the maximum number of characters), and PasswordChar (the character shown instead of the real text). Enabled, Visible, MultiLine and Font are equally acceptable.",
                },
                {
                    "q": "What is a combo box? List three properties.",
                    "a": "A combo box is a control that combines a text box with a drop-down list, so the user can pick an item or, depending on Style, type one. Three properties are Text, List and Style. Sorted is a fourth.",
                },
                {
                    "q": "Write the full form of ADO, MDI and SQL.",
                    "a": "ADO is ActiveX Data Objects. MDI is Multiple Document Interface. SQL is Structured Query Language. OLE is Object Linking and Embedding and DBA is Database Administrator, if the question offers those instead.",
                },
            ],
            "long": [],
        },
    },
    {
        "number": 9,
        "title": "Visual Basic: Variables, Decisions and Loops",
        "meta": "Option II  ·  Two periods  ·  Dim, Variant, Select Case, For…Next",
        "outcomes": [
            "Declare a variable with Dim and explain Variant.",
            "Write Select Case.",
            "Write a For loop, including one that steps by 2.",
            "Convert a simple formula into VB.",
        ],
        "blocks": [
            {"kind": "h2", "text": "Dim and Variant"},
            {
                "kind": "p",
                "text": "`Dim` declares a variable. `Dim marks As Integer` creates an integer named marks. Other types you should name are `Single` and `Double` for fractional numbers, `String` for text, `Boolean` for True or False, `Long` for a large whole number, and `Currency` for money. A constant is declared with `Const PASS As Integer = 40`.",
            },
            {
                "kind": "define",
                "title": "Variant",
                "text": "A Variant is a variable that can hold almost any kind of value: a number, a string or a date. Dim x As Variant, or simply Dim x, makes x a Variant. It is flexible and slower, and it hides mistakes. Use a specific type unless the question asks for Variant.",
            },
            {
                "kind": "p",
                "text": "`Val` turns text into a number. A text box always gives you a string. `Val(Text1.Text)` is how you do arithmetic on what the user typed. Without `Val`, the `+` operator may join strings instead of adding. The `&` operator joins strings on purpose, as in a label that reads Total followed by the number.",
            },
            {"kind": "h2", "text": "If and Select Case"},
            {
                "kind": "p",
                "text": "`If marks >= 40 Then` … `Else` … `End If`. For several exact values, `Select Case` is clearer than a long chain of If. The paper asks for its structure.",
            },
            {
                "kind": "code",
                "caption": "Program 9.1  Select Case on a grade letter typed into Text1.",
                "text": r"""Private Sub Command1_Click()
    Dim grade As String
    grade = Text1.Text
    Select Case grade
        Case "A"
            Label1.Caption = "Excellent"
        Case "B"
            Label1.Caption = "Good"
        Case Else
            Label1.Caption = "Keep working"
    End Select
End Sub""",
            },
            {
                "kind": "p",
                "text": "The structure is: `Select Case expression`, then one or more `Case` lines, an optional `Case Else`, and `End Select`. `Case Is >= 80` is legal when you are testing a range. There is no `break`. Visual Basic does not fall through into the next case the way C does. Say that if you are a student who has also seen C, and do not write `break` inside Select Case.",
            },
            {"kind": "h2", "text": "For…Next"},
            {
                "kind": "p",
                "text": "The counter starts at the first value and stops after the last. If `Step` is omitted, the counter increases by **1**. `Step 2` counts even numbers if you start at 0. `Step -1` counts downwards. A `Do While … Loop` repeats while a condition stays true. For a known count, use For.",
            },
            {
                "kind": "code",
                "caption": "Program 9.2  Even numbers from 0 to 50. Step 2 is the whole point of the program.",
                "text": r"""Private Sub Command1_Click()
    Dim i As Integer
    For i = 0 To 50 Step 2
        Print i
    Next i
End Sub""",
            },
            {
                "kind": "code",
                "caption": "Program 9.3  Sum and average of ten numbers. Val is required because InputBox returns text.",
                "text": r"""Private Sub Command1_Click()
    Dim i As Integer
    Dim n As Double
    Dim total As Double
    total = 0
    For i = 1 To 10
        n = Val(InputBox("Enter number " & i))
        total = total + n
    Next i
    Print "Sum = "; total
    Print "Average = "; total / 10
End Sub""",
            },
            {"kind": "h2", "text": "Formulas"},
            {
                "kind": "p",
                "text": "The same translation rules as C apply, with VB’s words. A square is `r * r` or `r ^ 2`. A half is `0.5 * base * height`. Absolute value is `Abs(b * b - 4 * a * c)`. Pi can be written `3.1416`. Integer division uses `\\`. Ordinary division uses `/`. You will usually want `/`.",
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "Dim is used to:",
                    "opts": ["A) Declare a variable", "B) Close a form", "C) Draw a circle", "D) Send email"],
                    "ans": "A",
                    "why": "Dim marks As Integer declares marks.",
                },
                {
                    "q": "If Step is omitted in For…Next, the counter changes by:",
                    "opts": ["A) 0", "B) 1", "C) 10", "D) −1"],
                    "ans": "B",
                    "why": "The default step is 1.",
                },
            ],
            "short": [
                {
                    "q": "How is a variable declared as Variant? Why might you avoid it?",
                    "a": "Dim x As Variant, or Dim x with no type, makes x a Variant. It can store a number, a string or a date. It is convenient and it is slow, and a mistaken text value will not be caught as a type error. A specific type such as Integer or Double is safer.",
                },
                {
                    "q": "Write the structure of Select Case.",
                    "a": "Select Case expression, then Case value, then the statements for that value, further Case lines as needed, an optional Case Else, and End Select. Example: Select Case grade / Case \"A\" / Label1.Caption = \"Excellent\" / Case Else / Label1.Caption = \"Other\" / End Select. VB does not fall through to the next case.",
                },
            ],
            "long": [],
        },
    },
    {
        "number": 10,
        "title": "Functions, Arrays and Errors in Visual Basic",
        "meta": "Option II  ·  Two periods  ·  Section C asks for arrays, loops and built-in functions",
        "outcomes": [
            "Distinguish a Function, which returns a value, from a Sub, which does not.",
            "Declare a one-dimensional and a two-dimensional array.",
            "Name syntax, run-time and logical errors with an example each.",
            "Use one built-in function in a small program.",
        ],
        "blocks": [
            {"kind": "h2", "text": "Function and Sub"},
            {
                "kind": "p",
                "text": "A **Sub** does a job and does not return a value: `Sub ShowTotal()`. A **Function** returns a value: `Function Greater(x As Integer, y As Integer) As Integer`. The multiple-choice line “a subprogram which returns a value” is a function. You call a function inside an expression. You call a Sub as a statement.",
            },
            {
                "kind": "code",
                "caption": "Program 10.1  A function returns the larger integer. The result is assigned, not printed inside the function.",
                "text": r"""Function Greater(x As Integer, y As Integer) As Integer
    If x > y Then
        Greater = x
    Else
        Greater = y
    End If
End Function

Private Sub Command1_Click()
    Dim a As Integer, b As Integer
    a = Val(Text1.Text)
    b = Val(Text2.Text)
    Label1.Caption = Greater(a, b)
End Sub""",
            },
            {
                "kind": "p",
                "text": "In VB the function’s name is assigned the value to return: `Greater = x`. There is no `return x` of the C kind. Passing **by value** (`ByVal`) sends a copy, so the procedure cannot change the caller’s variable. Passing **by reference** (`ByRef`, the older default) sends the variable itself, so a change inside is visible outside. The one-mark phrase “passing a copy of the variable” is pass by value.",
            },
            {"kind": "h2", "text": "Arrays"},
            {
                "kind": "define",
                "title": "Array",
                "text": "An array is a set of values of one type under one name, reached by an index. A one-dimensional array is a list. A two-dimensional array is a table, with a row index and a column index.",
            },
            {
                "kind": "code",
                "caption": "Program 10.2  A list of five marks. The index runs from 1 to 5 because the declaration says so.",
                "text": r"""Private Sub Command1_Click()
    Dim marks(1 To 5) As Integer
    Dim i As Integer
    Dim total As Integer
    total = 0
    For i = 1 To 5
        marks(i) = Val(InputBox("Enter marks"))
        total = total + marks(i)
    Next i
    Print "Total = "; total
End Sub""",
            },
            {
                "kind": "p",
                "text": "`Dim grid(1 To 3, 1 To 3) As Integer` is a three-by-three table. You need two nested For loops to visit every cell. If you write `Dim marks(5)`, VB creates indexes from 0 to 5 unless Option Base has been set, which is a trap. Writing `(1 To 5)` says exactly what you mean. Do that in the exam.",
            },
            {"kind": "h2", "text": "Built-in functions"},
            {
                "kind": "p",
                "text": "A built-in function comes with the language. You call it. You do not write its body. Useful ones: `Val` (text to number), `Abs` (absolute value), `Sqr` (square root), `Len` (length of a string), `Left`, `Right`, `Mid`, `UCase`, `Int`. A long answer is: define built-in function, name three, then one program.",
            },
            {
                "kind": "code",
                "caption": "Program 10.3  Val and a built-in arithmetic function. Sqr needs a non-negative value.",
                "text": r"""Private Sub Command1_Click()
    Dim n As Double
    n = Val(Text1.Text)
    Label1.Caption = Sqr(n)
End Sub""",
            },
            {"kind": "h2", "text": "Errors"},
            {
                "kind": "table",
                "headers": ["Error", "When you meet it", "Example"],
                "rows": [
                    ["Syntax", "Before the program runs. The editor or compiler rejects the line", "End Select missing, or a misspelt keyword"],
                    ["Run-time", "While the program is running. It stops", "Division by zero, or Val of a situation that then divides badly; a missing file"],
                    ["Logical", "The program runs and gives a wrong answer", "Average divided by 9 when ten numbers were read; using = instead of a comparison in a language that allows it"],
                ],
                "widths": [80, 200, 220],
            },
            {
                "kind": "p",
                "text": "A syntax error is the cheapest to find. A logical error is the most expensive, because nothing crashes. When a question says “define an error and its types”, use this table and one example each. Three types are enough.",
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "A subprogram that returns a value is a:",
                    "opts": ["A) Report", "B) Function", "C) Table", "D) Label"],
                    "ans": "B",
                    "why": "A Sub does not return a value. A Function does.",
                },
                {
                    "q": "Passing a copy of a variable is:",
                    "opts": ["A) Pass by value", "B) Pass by reference", "C) A syntax error", "D) A query"],
                    "ans": "A",
                    "why": "ByVal copies. ByRef shares the original variable.",
                },
            ],
            "short": [
                {
                    "q": "Define an error and its three types.",
                    "a": "An error is a fault that stops a program or makes it give a wrong result. A syntax error breaks the grammar of the language and is caught before a successful run. A run-time error appears during the run, such as division by zero. A logical error lets the program finish with the wrong answer, such as dividing a total by the wrong count.",
                }
            ],
            "long": [
                {
                    "q": "Explain an array and its types, with examples in Visual Basic.",
                    "a": "An array stores many values of one type under one name. Each value is an element, reached by an index. A one-dimensional array is a list: Dim marks(1 To 5) As Integer creates five integers, marks(1) to marks(5). A loop For i = 1 To 5 reads them and can total them. A two-dimensional array is a table: Dim grid(1 To 3, 1 To 3) As Integer has rows and columns, visited by two nested loops. All elements have the same type. The index must stay inside the declared bounds. Arrays suit marks, names and any series where separate variables (m1, m2, m3) would be clumsy.",
                },
                {
                    "q": "What is a built-in function? Explain with a program.",
                    "a": "A built-in function is supplied by Visual Basic. The programmer calls it and does not write its body. Examples are Val, which converts text to a number, Abs, Sqr, Len and UCase. Program: in Command1_Click, read n = Val(Text1.Text) and set Label1.Caption = Sqr(n). Val is required because a text box holds text. Sqr returns the square root. The function has a name, receives a value, and returns a result.",
                },
            ],
        },
    },
    {
        "number": 11,
        "title": "Visual Basic Programs for the Examination",
        "meta": "Option II  ·  A practical lecture  ·  Write each program from a blank page",
        "outcomes": [
            "Write the even-number loop and the ten-number average from memory.",
            "Write Select Case and a Function that returns a value.",
            "Name the lines a marker expects in each.",
        ],
        "blocks": [
            {"kind": "h2", "text": "The set to be able to reproduce"},
            {
                "kind": "p",
                "text": "Four pieces cover most programming questions in Option II. Database questions in the same paper are prepared in Lectures 12 to 14.",
            },
            {
                "kind": "p",
                "text": "**Even numbers from 0 to 50.** Program 9.2. The mark is `Step 2`. A loop `For i = 0 To 50` without Step prints the odd numbers as well and does not answer the question. Starting at 1 with Step 2 prints the odds.",
            },
            {
                "kind": "p",
                "text": "**Sum and average of ten numbers.** Program 9.3. `total` must start at 0. The average is `total / 10`, not `total / i` after the loop, because after `Next` the counter has moved on. `Val` around `InputBox` is part of the marks.",
            },
            {
                "kind": "p",
                "text": "**Select Case.** Program 9.1. Include `Case Else` and `End Select`. Do not import `break` from C.",
            },
            {
                "kind": "p",
                "text": "**A function.** Program 10.1. Assign the result to the function’s name. The Click procedure only collects input and displays what the function returns.",
            },
            {
                "kind": "tip",
                "title": "A program layout that is easy to mark",
                "text": "First line: Private Sub Command1_Click() or Function …. Then Dim. Then input. Then the loop or the Select. Then the output. Then End Sub or End Function. Indent the inside of the loop by two spaces. The marker is reading fifty scripts.",
            },
        ],
        "checkpoint": {
            "mcq": [],
            "short": [
                {
                    "q": "Write a VB program to print all even numbers from 0 to 50.",
                    "a": "In Command1_Click, Dim i As Integer, then For i = 0 To 50 Step 2, Print i, Next i, End Sub. Step 2 is required. The default step of 1 would also print the odd numbers.",
                },
                {
                    "q": "Write a VB program for the sum and average of ten inputted numbers.",
                    "a": "Dim i As Integer, n As Double, total As Double. Set total = 0. For i = 1 To 10, add Val(InputBox(...)) to total. After Next, Print the total and total / 10.",
                },
            ],
            "long": [],
        },
    },
    {
        "number": 12,
        "title": "Database Fundamentals",
        "meta": "Both options  ·  Two periods  ·  Asked inside Paper II whichever language you chose",
        "outcomes": [
            "Distinguish a flat file from a database.",
            "Define a table, a record and a field, and give the other names the paper uses.",
            "List the components of a DBMS and three duties of a DBA.",
            "State advantages that match the multiple-choice wording.",
        ],
        "blocks": [
            {"kind": "h2", "text": "From a pile of files to a database"},
            {
                "kind": "p",
                "text": "A **flat file** is one file of records, often repeated in another file. A college might keep a class list in one sheet and a fee list in another, with each student’s name typed twice. Change a name in one place and the other place is wrong. A **database** stores the data once, in related tables, and many programs can use it. A **database management system** (DBMS) is the software that creates, protects and queries that database. Microsoft Access is the DBMS this paper expects you to know. The person who writes application programs is a programmer. The person who looks after the database is the DBA. The person who only uses the finished screens is an end user.",
            },
            {
                "kind": "define",
                "title": "Table, record, field",
                "text": "A table is the basic object: rows and columns about one kind of thing, such as Student. A row is a record (also called a tuple). A column is a field (also called an attribute). Roll number, name and class are fields. Ali’s whole line is one record.",
            },
            {
                "kind": "table",
                "headers": ["Word in one book", "Word in another", "In a sentence"],
                "rows": [
                    ["Row", "Record or tuple", "One student’s data"],
                    ["Column", "Field or attribute", "The Name column"],
                    ["Table", "Relation", "The Student table"],
                    ["Table structure", "Schema", "The field names and types, not the rows of data"],
                ],
                "widths": [130, 140, 230],
            },
            {"kind": "h2", "text": "Components of a DBMS"},
            {
                "kind": "p",
                "text": "Five components answer “name the major components of a DBMS”. Write them as a list with a few words each.",
            },
            {
                "kind": "table",
                "headers": ["Component", "What it is"],
                "rows": [
                    ["Hardware", "The computer, disks and network the database runs on"],
                    ["Software", "The DBMS itself, such as MS Access, plus the operating system"],
                    ["Data", "The facts stored in the tables. This is the reason the system exists"],
                    ["Procedures", "The rules: who may enter marks, how often a backup is taken"],
                    ["Users and the data language", "DBA, programmers and end users. SQL is the language they use to ask questions"],
                ],
                "widths": [150, 350],
            },
            {"kind": "h2", "text": "Why a database is worth the trouble"},
            {
                "kind": "p",
                "text": "Learn five advantages in verbs. **Redundancy is reduced** because a fact is stored once. **Consistency** follows: there is one name to update. **Sharing** means several programs, and several users, can use the same data. **Integrity** means the data obeys rules, such as “marks are between 0 and 100”. **Security** means accounts and passwords decide who may see or change a table. Backup and recovery are a sixth, and a good one. The multiple-choice advantage that matches this list is: data is integrated and can be accessed by multiple programs. “Redundancy increases” and “integrity decreases” are the wrong way round.",
            },
            {
                "kind": "board",
                "title": "Three duties of a DBA",
                "text": "The database administrator designs the tables, controls who may use them, and takes backups so the data can be restored. Monitoring performance and keeping the data consistent are fair extra duties. Do not say the DBA’s job is to type every student’s marks. That is a data-entry user.",
            },
            {
                "kind": "p",
                "text": "Applications you can quote: a college admission system, a bank’s account records, a hospital’s patients, a library’s loans, a shop’s stock. One example beside the definition is enough in Section B.",
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "The primary object in a database is the:",
                    "opts": ["A) Report", "B) Query", "C) Table", "D) Form"],
                    "ans": "C",
                    "why": "Reports and queries are built on tables. The data lives in the table.",
                },
                {
                    "q": "A row in a table is a:",
                    "opts": ["A) Field", "B) Record", "C) Query", "D) Form"],
                    "ans": "B",
                    "why": "A column is a field. A row is a record.",
                },
                {
                    "q": "An advantage of the database approach is that:",
                    "opts": ["A) Data redundancy increases", "B) Data is integrated and can be shared by programs", "C) Integrity must decrease", "D) Each program keeps its own copy on purpose"],
                    "ans": "B",
                    "why": "The point of a DBMS is one integrated store used by many programs.",
                },
            ],
            "short": [
                {
                    "q": "Name the major components of a DBMS.",
                    "a": "Hardware (the machine and disks), software (the DBMS, such as MS Access), data (the contents of the tables), procedures (backup and access rules), and people together with a data language such as SQL. Users include the DBA, programmers and end users.",
                },
                {
                    "q": "Who is a DBA? Write three responsibilities.",
                    "a": "A database administrator is the person responsible for the database. Three duties are: designing the tables and relationships, controlling security so only the right people can change data, and taking backups and restoring them when needed.",
                },
                {
                    "q": "Define table, query and report.",
                    "a": "A table stores the data in rows and columns. A query asks a question of the tables, for example which students scored 80 or more, and can also change data. A report lays the data out for printing. A form, if you have a fourth line, is the screen used to enter and view records.",
                },
            ],
            "long": [],
        },
    },
    {
        "number": 13,
        "title": "Data Models, Keys and Relationships",
        "meta": "Both options  ·  Two periods  ·  Section C: data models. Section B: primary and foreign key",
        "outcomes": [
            "Explain hierarchical, network and relational models.",
            "Define primary key and foreign key with one table example.",
            "Draw a one-to-many relationship.",
            "State 1NF, 2NF and 3NF in one sentence each.",
        ],
        "blocks": [
            {"kind": "h2", "text": "A data model is the shape of the data"},
            {
                "kind": "define",
                "title": "Data model",
                "text": "A data model is a way of organising data and of showing how one piece is related to another. The model comes before the software. Access implements the relational model.",
            },
            {
                "kind": "table",
                "headers": ["Model", "Shape", "What to say about it"],
                "rows": [
                    ["Hierarchical", "A tree. One parent, many children", "Like folders, or a college containing classes containing students. Simple. Awkward when a child needs two parents, because the tree does not allow it"],
                    ["Network", "Records linked as a graph. A child may have more than one parent", "More flexible than a tree. Harder to design and to change. Not the model Access uses"],
                    ["Relational", "Data in tables. A row is a record. A column is a field. Tables are linked by keys", "The model in the paper and in MS Access. Questions are asked in SQL. This is the one to give the longest paragraph"],
                    ["Object-oriented", "Data and the operations on it live together as objects", "Mention it as a fourth model if the question says “all”. One sentence is enough"],
                ],
                "widths": [100, 160, 240],
            },
            {
                "kind": "tip",
                "title": "The tree question",
                "text": "“The model that organises data in a tree” is hierarchical. “The model that allows queries through SQL” is relational. Those two multiple-choice answers are a pair. Do not swap them.",
            },
            {"kind": "h2", "text": "Keys"},
            {
                "kind": "p",
                "text": "A **primary key** is a field, or a group of fields, that uniquely identifies each row. It cannot be empty, and no two rows may share it. Roll number in a Student table is a primary key. Name is a bad primary key because two students can share a name.",
            },
            {
                "kind": "p",
                "text": "A **foreign key** is a field in one table that refers to the primary key of another table. It is how a relationship is stored. It may repeat, because many children can point at one parent. It should not point at a parent that does not exist.",
            },
            {
                "kind": "table",
                "headers": ["DeptCode", "DeptName"],
                "rows": [
                    ["CS", "Computer Science"],
                    ["PE", "Pre-Engineering"],
                ],
                "caption": "Table DEPARTMENT. DeptCode is the primary key.",
                "widths": [120, 200],
            },
            {
                "kind": "table",
                "headers": ["RollNo", "Name", "DeptCode"],
                "rows": [
                    ["1101", "Ali", "CS"],
                    ["1102", "Sara", "CS"],
                    ["1103", "Hina", "PE"],
                ],
                "caption": "Table STUDENT. RollNo is the primary key. DeptCode is a foreign key pointing at DEPARTMENT.",
                "widths": [100, 140, 120],
            },
            {
                "kind": "p",
                "text": "This relationship is **one-to-many**: one department has many students. One student here belongs to one department. A **one-to-one** relationship is rarer: one person, one national identity record. A **many-to-many** relationship, such as students and subjects, is not stored as a single foreign key. It is broken into two one-to-many links through a third table, for example ENROLMENT(RollNo, SubjectCode).",
            },
            {
                "kind": "board",
                "title": "Primary key and foreign key, six lines",
                "text": "A primary key uniquely identifies a row and cannot be null. Example: RollNo in STUDENT. A foreign key is a column that matches the primary key of another table. Example: DeptCode in STUDENT, which refers to DeptCode in DEPARTMENT. The primary key does not repeat. The foreign key may repeat. That repetition is the “many” side.",
            },
            {"kind": "h2", "text": "Normal forms, in case the question goes one step further"},
            {
                "kind": "p",
                "text": "Normalisation is arranging tables so that facts are not repeated and updates stay sane. Three levels are enough.",
            },
            {
                "kind": "table",
                "headers": ["Form", "Rule in one sentence"],
                "rows": [
                    ["1NF", "Each cell holds a single value. There is no list inside a cell, and no repeating group of columns such as Subject1, Subject2, Subject3."],
                    ["2NF", "The table is in 1NF, and every field that is not part of the key depends on the whole key, not on only one part of a two-field key."],
                    ["3NF", "The table is in 2NF, and no non-key field depends on another non-key field. If Course determines Teacher, Teacher belongs in a Course table, not copied onto every student row."],
                ],
                "widths": [60, 440],
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "The model that organises data as a tree is:",
                    "opts": ["A) Relational", "B) Hierarchical", "C) Flat file only", "D) Spreadsheet"],
                    "ans": "B",
                    "why": "One parent, many children, no second parent.",
                },
                {
                    "q": "A key that uniquely identifies a record is the:",
                    "opts": ["A) Foreign key", "B) Primary key", "C) Caption", "D) Report"],
                    "ans": "B",
                    "why": "The foreign key is allowed to repeat. It points at a primary key.",
                },
            ],
            "short": [
                {
                    "q": "Differentiate primary key and foreign key.",
                    "a": "A primary key uniquely identifies each row and cannot be null. RollNo in a Student table is a primary key. A foreign key is a field in one table that refers to the primary key of another table, such as DeptCode in Student referring to DeptCode in Department. A primary key does not repeat. A foreign key may repeat, which is how one department can have many students.",
                },
                {
                    "q": "Define a one-to-many relationship and give an example.",
                    "a": "In a one-to-many relationship, one row of the first table matches many rows of the second, and each row of the second matches only one row of the first. One department has many students. DeptCode is the primary key in Department and a foreign key in Student.",
                },
            ],
            "long": [
                {
                    "q": "What is a data model? Explain its types.",
                    "a": "A data model describes how data is organised and related. The hierarchical model is a tree: each child has one parent, for example a college containing classes containing students. It is simple and it cannot easily show a child with two parents. The network model allows a record to have more than one parent, which is more flexible and harder to maintain. The relational model stores data in tables made of rows and columns and links tables by keys. It is the model used by MS Access, and questions are asked with SQL. A primary key identifies a row; a foreign key refers to a primary key in another table. The object-oriented model keeps data and its operations together as objects. For this paper the relational model is the one used in practical work.",
                }
            ],
        },
    },
    {
        "number": 14,
        "title": "Microsoft Access and SQL",
        "meta": "Both options  ·  Two periods  ·  Section C: data types in MS Access. Objects, queries, one SELECT",
        "outcomes": [
            "Name the Access objects and the job of each.",
            "List the field data types with one example each.",
            "Write a SELECT statement with a WHERE clause.",
            "Distinguish selecting rows from projecting columns.",
        ],
        "blocks": [
            {"kind": "h2", "text": "The objects on the Access window"},
            {
                "kind": "table",
                "headers": ["Object", "Job", "You use it when"],
                "rows": [
                    ["Table", "Stores the data", "You design Student with RollNo, Name and Marks"],
                    ["Query", "Asks a question or changes rows", "You want only the students who passed"],
                    ["Form", "A screen for viewing and typing", "A clerk enters a new admission"],
                    ["Report", "A layout for paper", "You print a class list"],
                    ["Macro", "A saved sequence of actions", "A button opens a form"],
                    ["Module", "Visual Basic code inside Access", "A calculation the macro cannot express"],
                ],
                "widths": [70, 160, 270],
            },
            {
                "kind": "p",
                "text": "The object used to display and print data, in the paper’s wording, is the **report**. The object that stores the data is the **table**. A query does not store the data permanently; it shows a view of it. Do not answer “query” when the question says “print”.",
            },
            {"kind": "h2", "text": "Data types"},
            {
                "kind": "p",
                "text": "A data type is the kind of value a field may hold. Choosing it badly wastes space or rejects legal values. This list is the Section C answer. Newer Access renames Text to Short Text and Memo to Long Text. If you have learned the new names, write the old name and the new name together. Markers taught on either screen can follow you.",
            },
            {
                "kind": "table",
                "headers": ["Data type", "Holds", "Example field"],
                "rows": [
                    ["Text (Short Text)", "Words and short codes, up to 255 characters. Digits that are not quantities, such as a phone number", "Name, RollNo stored as text"],
                    ["Memo (Long Text)", "A long note", "Remarks"],
                    ["Number", "A quantity you will add or compare", "Marks, Age"],
                    ["Date/Time", "A date, a time, or both", "AdmissionDate"],
                    ["Currency", "Money, without binary rounding surprises", "Fee"],
                    ["AutoNumber", "A number Access fills in, different for every new row", "A receipt id"],
                    ["Yes/No", "A true or false", "FeePaid"],
                    ["OLE Object", "A file embedded from elsewhere, such as a picture", "Photo"],
                    ["Hyperlink", "A link or a web address", "Portfolio URL"],
                ],
                "widths": [130, 250, 120],
            },
            {
                "kind": "p",
                "text": "Use Text for a roll number if you will not add the roll numbers up. Use Number for marks because you will. Use Date/Time for a date rather than Text, so that “after March” is a real comparison. AutoNumber is not typed by the user. Yes/No is not the place for a student’s name.",
            },
            {"kind": "h2", "text": "SQL that you can write by hand"},
            {
                "kind": "p",
                "text": "SQL is the language of the relational model. In this paper you need to read and write a basic `SELECT`. You should also recognise `INSERT`, `UPDATE` and `DELETE` as the statements that add, change and remove rows.",
            },
            {
                "kind": "code",
                "caption": "Query 14.1  Names and marks of students who passed. The asterisk form SELECT * would return every column.",
                "text": """SELECT Name, Marks
FROM Student
WHERE Marks >= 40;""",
            },
            {
                "kind": "p",
                "text": "**Projection** chooses columns: the `Name, Marks` list. **Selection** chooses rows: the `WHERE` clause. A question that says “differentiate selection and projection” is this pair. Selection is horizontal (which records). Projection is vertical (which fields).",
            },
            {
                "kind": "code",
                "caption": "Query 14.2  A new table and one inserted row. Types are written so the example matches the lecture.",
                "text": """CREATE TABLE Student (
    RollNo TEXT(10),
    Name TEXT(40),
    Marks NUMBER
);

INSERT INTO Student (RollNo, Name, Marks)
VALUES ('1101', 'Ali', 81);""",
            },
            {
                "kind": "p",
                "text": "In the Access design grid you can do the same query without typing SQL: choose the table, tick the columns, and put `>= 40` in the Criteria row under Marks. Knowing both the grid and the `SELECT` is the practical. The written paper wants the words and the statement.",
            },
            {
                "kind": "p",
                "text": "A **join** brings columns from two tables together. An equi-join keeps the rows where the keys are equal, for example Student.DeptCode equal to Department.DeptCode, so each student appears with the department name. You can describe that in a sentence if a short question says “join”. A full syntax of every join type is beyond what this paper usually demands.",
            },
            {
                "kind": "tip",
                "title": "The long answer on data types",
                "text": "Open with one sentence: a data type decides what a field may store and what operations are sensible. Then eight types, each with a field name from a Student or Fee table. Close with the roll-number point: text if you will not calculate, number if you will. That is a complete 10-mark answer.",
            },
        ],
        "checkpoint": {
            "mcq": [
                {
                    "q": "In MS Access, the object used to print data is the:",
                    "opts": ["A) Table", "B) Report", "C) Module", "D) Macro"],
                    "ans": "B",
                    "why": "A table stores. A report is laid out for paper.",
                },
                {
                    "q": "A column in a table is also called:",
                    "opts": ["A) A tuple", "B) An attribute or field", "C) A form", "D) A macro"],
                    "ans": "B",
                    "why": "A tuple is a row. An attribute is a column.",
                },
            ],
            "short": [
                {
                    "q": "Differentiate selection and projection.",
                    "a": "Selection picks rows. In SQL it is the WHERE clause, for example WHERE Marks >= 40. Projection picks columns. It is the list after SELECT, for example SELECT Name, Marks. Selection is which records. Projection is which fields.",
                },
                {
                    "q": "Write a query to show Name and Marks of students who scored 80 or more.",
                    "a": "SELECT Name, Marks FROM Student WHERE Marks >= 80; Name and Marks are the projection. The WHERE clause is the selection.",
                },
            ],
            "long": [
                {
                    "q": "Explain the data types used in MS Access.",
                    "a": "A data type specifies the kind of value a field can store. Text (Short Text) stores names and codes up to 255 characters; use it for a name or a roll number you will not add up. Memo (Long Text) stores a long remark. Number stores quantities such as marks or age. Date/Time stores a date or a time, such as the day of admission. Currency stores money, such as a fee. AutoNumber gives each new row a unique number automatically. Yes/No stores a true or false, such as whether the fee is paid. OLE Object stores an embedded file such as a photograph. Hyperlink stores a web address. Choosing Number for marks allows a total. Choosing Text for a phone number stops Access from dropping a leading zero.",
                }
            ],
        },
    },
    {
        "number": 15,
        "title": "Paper II Drill",
        "meta": "Both options  ·  One sitting each  ·  Do only the option you will enter in the examination",
        "outcomes": [
            "Sit a 15-mark multiple-choice paper for your option.",
            "Pick ten short questions and three long questions under the real rules.",
            "Mark the paper from the lectures, not from memory of the question.",
        ],
        "blocks": [
            {"kind": "h2", "text": "Rules for this drill"},
            {
                "kind": "p",
                "text": "Give yourself 20 minutes for Section A and two and a half hours for the rest, or a shorter class test of Section A plus five short questions. Option I candidates ignore the Visual Basic block. Option II candidates ignore the C block. Everyone does the database questions. These questions are original practice in the shape of the 2026 paper. They are not a past paper to memorise.",
            },
            {"kind": "h2", "text": "Option I — Section A"},
            {"kind": "p", "text": "1  All C programs contain: A) clrscr  B) main  C) getch  D) start."},
            {"kind": "p", "text": "2  An illegal name is: A) fee  B) fee_2  C) 2fee  D) Fee."},
            {"kind": "p", "text": "3  % may be applied to: A) int  B) a sentence  C) a form  D) a report."},
            {"kind": "p", "text": "4  k++ is: A) pre-increment  B) post-increment  C) a comment  D) a header."},
            {"kind": "p", "text": "5  Comments use: A) /* */  B) < >  C) # ;  D) { }."},
            {"kind": "p", "text": "6  continue: A) ends the program  B) skips to the next pass of the loop  C) declares a variable  D) opens a file."},
            {"kind": "p", "text": "7  A for loop is: A) selection  B) iteration  C) a data type  D) a key."},
            {"kind": "p", "text": "8  The translator of a C program is a: A) compiler  B) plotter  C) bridge  D) hub."},
            {"kind": "p", "text": "9  A primary key: A) may repeat  B) uniquely identifies a row  C) is a form  D) is always a date."},
            {"kind": "p", "text": "10  A row is a: A) field  B) record  C) query  D) macro."},
            {"kind": "p", "text": "11  Data stored once and used by many programs shows: A) more unwanted duplication  B) integration  C) that a DBMS is useless  D) a syntax error."},
            {"kind": "p", "text": "12  The object that stores the data is the: A) report  B) table  C) printer  D) label."},
            {"kind": "p", "text": "13  C was designed by: A) Dennis Ritchie  B) Blaise Pascal, as the author of C  C) the inventor of the mouse only  D) a standards body for HDMI."},
            {"kind": "p", "text": "14  In int a[4] the first index is: A) 1  B) 0  C) 4  D) 5."},
            {"kind": "p", "text": "15  scanf needs: A) the address of the variable  B) a plotter  C) a foreign key  D) a form."},
            {"kind": "h2", "text": "Option I — short questions, answer any ten on the real paper"},
            {"kind": "p", "text": "i) Write the structure of a C program. ii) Explain #define with two examples. iii) Write a program for the multiplication table of an inputted number. iv) Differentiate break and continue. v) Name five reserved words. vi) What does & do in scanf? vii) Write a factorial program and show 4! = 24. viii) Differentiate scanf and getchar. ix) Differentiate primary key and foreign key. x) If a = 2, b = 5 and c = 10, evaluate 200 * ((a * 10) + c). xi) Name five components of a DBMS. xii) Write a function that returns the greater of two integers. xiii) Convert A = (1/2) × base × height into C. xiv) Write a nested loop for the triangle 1 / 12 / 123 / 1234 / 12345. xv) Define table, query and report."},
            {"kind": "h2", "text": "Option I — long questions, answer any three"},
            {"kind": "p", "text": "1  Explain switch with a diagram and a program. 2  Explain the types of operators in C. 3  Explain the characteristics of a function, with a program. 4  What is a data model? Explain the types. 5  Explain the data types in MS Access."},
            {"kind": "h2", "text": "Option II — Section A"},
            {"kind": "p", "text": "1  The default Step of For…Next is: A) 0  B) 1  C) 2  D) 10."},
            {"kind": "p", "text": "2  A row is a: A) field  B) record  C) query  D) module."},
            {"kind": "p", "text": "3  Printing is the job of a: A) report  B) primary key only  C) modem  D) comment."},
            {"kind": "p", "text": "4  A unique key is the: A) primary key  B) caption  C) label  D) step."},
            {"kind": "p", "text": "5  Dim declares a: A) variable  B) cable  C) topology  D) virus."},
            {"kind": "p", "text": "6  A function: A) cannot return a value  B) returns a value  C) is a printer  D) is a topology."},
            {"kind": "p", "text": "7  Passing a copy is: A) ByVal  B) a foreign key  C) a report  D) OLE only."},
            {"kind": "p", "text": "8  The tree-shaped data model is: A) hierarchical  B) relational  C) a text box  D) SMTP."},
            {"kind": "p", "text": "9  SQL belongs to the: A) hierarchical model only  B) relational model  C) plotter  D) fetch cycle."},
            {"kind": "p", "text": "10  One choice from a group uses: A) an option button  B) a label  C) a timer  D) a bus."},
            {"kind": "p", "text": "11  ADO stands for: A) ActiveX Data Objects  B) Analog Data Output  C) All Disk Operations  D) Automatic Default Option."},
            {"kind": "p", "text": "12  A column is: A) an attribute  B) a tuple  C) a form  D) a macro."},
            {"kind": "p", "text": "13  Case Else in Select Case resembles: A) default  B) a primary key  C) a hub  D) RAM."},
            {"kind": "p", "text": "14  Val is used to: A) convert text to a number  B) draw a circle  C) shut down Windows  D) define a protocol."},
            {"kind": "p", "text": "15  The object that stores records is the: A) table  B) report  C) label  D) cable."},
            {"kind": "h2", "text": "Option II — short and long"},
            {"kind": "p", "text": "Short, any ten: four advantages of a DBMS; three properties of a combo box; declare a Variant; one-to-many with a diagram in words; four Access objects; the structure of Select Case; three duties of a DBA; what an ActiveX control is; full forms of ADO, SQL and DBA; four properties of a text box; a program of even numbers from 0 to 50; sum and average of ten numbers; primary key versus foreign key; three types of error."},
            {"kind": "p", "text": "Long, any three: arrays and their types; two kinds of loop with examples; a built-in function with a program; data models; data types in MS Access."},
            {"kind": "h2", "text": "Answer key — Section A only"},
            {
                "kind": "p",
                "text": "Option I: 1 B, 2 C, 3 A, 4 B, 5 A, 6 B, 7 B, 8 A, 9 B, 10 B, 11 B, 12 B, 13 A, 14 B, 15 A.",
            },
            {
                "kind": "p",
                "text": "Option II: 1 B, 2 B, 3 A, 4 A, 5 A, 6 B, 7 A, 8 A, 9 B, 10 A, 11 A, 12 A, 13 A, 14 A, 15 A.",
            },
            {
                "kind": "p",
                "text": "Mark a short or long answer from the model answer in the lecture named by the topic. A program with the right loop and a missing Dim, or a missing ampersand in scanf, is not a full-mark program. A database answer with no example is not a full-mark answer.",
            },
        ],
        "checkpoint": {},
    },
]
