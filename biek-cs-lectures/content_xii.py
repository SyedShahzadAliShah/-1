"""Class XII / Computer Science Paper-II lectures (BIEK 2026: C or VB + DBMS)."""

from content_xi import add_cover
from diagrams import Diagram
from reportlab.lib.units import mm


def build_xii(b):
    add_cover(
        b,
        "Board of Intermediate Education, Karachi",
        "Computer Science XII Lectures  Paper – II",
        "H.S.C. Part II  ·  Science General & Humanities Groups\n"
        "Option I: Programming Using C    ·    Option II: Programming Using Visual Basic\n"
        "Both options include DBMS / MS-Access",
        [
            "C language from structure to functions, arrays and pointers",
            "DBMS, data models, keys, MS-Access objects and data types",
            "Visual Basic Option II: controls, events, loops, arrays",
            "Board programs + solved Model Paper 2026",
        ],
        "Original exam-oriented lecture notes  ·  2026 edition",
    )
    _intro(b)
    _c01(b)
    _c02(b)
    _c03(b)
    _c04(b)
    _c05(b)
    _c06(b)
    _c07(b)
    _db01(b)
    _db02(b)
    _vb01(b)
    _programs(b)
    _xii_bank(b)
    _model(b)


def _intro(b):
    b.h1("How Paper–II is set (BIEK 2026)")
    b.p(
        "Paper–II has <b>two independent options</b>. Attempt the option you studied. "
        "Mixing C and Visual Basic in the same script is not allowed."
    )
    b.table(
        ["Option", "Programming", "Also asked every year"],
        [
            ["I", "Programming Using C (stdio.h, printf, scanf)", "DBMS + MS-Access"],
            ["II", "Programming Using Visual Basic", "DBMS + MS-Access"],
        ],
    )
    b.table(
        ["Section", "Time", "Marks", "2026 instruction"],
        [
            ["A MCQs", "20 min", "15", "All 15 — C MCQs or VB MCQs according to option"],
            ["B Short", "in 2 h 40 min", "30", "Attempt any TEN parts (3 marks each)"],
            ["C Detailed", "in 2 h 40 min", "30", "Attempt any THREE questions"],
            ["Practical", "lab", "25", "Write, compile, run programs; Access tables; viva"],
        ],
    )
    b.exam_tip(
        "In C answers, always write <b>complete programs</b> with #include, main(), scanf/printf "
        "and return 0. Examiners cut marks for missing semicolons, mismatched braces and wrong "
        "format specifiers. Indent the body. For DBMS questions, draw tables and mark PK/FK.",
    )
    b.h1("Contents — Class XII / Paper–II")
    b.table(
        ["Lecture", "Title", "Option"],
        [
            ["1", "Introduction to C, IDE, program structure", "I"],
            ["2", "Tokens, data types, operators, printf/scanf", "I"],
            ["3", "if and switch", "I"],
            ["4", "Loops, break/continue, board patterns", "I"],
            ["5", "Functions", "I"],
            ["6", "Arrays, strings, structures", "I"],
            ["7", "Pointers and files", "I"],
            ["8", "Database fundamentals and data models", "I and II"],
            ["9", "MS-Access objects and data types", "I and II"],
            ["10", "Visual Basic controls, events, loops", "II"],
            ["11", "Practical C program bank", "I (lab)"],
            ["12", "MCQ one-liners", "Both"],
            ["13", "Solved Model Paper 2026", "Both"],
        ],
    )
    b.page_break()


def _c01(b):
    b.chapter_banner("01", "Introduction to Programming and the C Language", "Paper–II Option I", "Structure of C")
    b.definition(
        "Program",
        "A program is a set of instructions written in a programming language that tells the "
        "computer how to solve a problem.",
    )
    b.definition(
        "Programming language",
        "A programming language is a formal language with syntax and semantics used to write programs. "
        "Examples: C, C++, Java, Python, Visual Basic.",
    )
    b.h2("1.1 Types of errors")
    b.table(
        ["Error", "When it appears", "Example"],
        [
            ["Syntax", "At compile time", "Missing semicolon, undeclared variable"],
            ["Logical", "Program runs but result is wrong", "Using + instead of * in a formula"],
            ["Run-time", "During execution", "Divide by zero, missing file"],
            ["Linker", "After compile, at linking", "Forgot to include a library"],
        ],
    )
    b.h2("1.2 History of C (MCQ)")
    b.bullets(
        [
            "Developed by <b>Dennis Ritchie</b> at Bell Labs in 1972, based on B (Ken Thompson).",
            "Used to write the UNIX operating system.",
            "ANSI C / C89 standardised the language; C99 and later added features.",
            "C is a middle-level, structured, compiled, case-sensitive language.",
        ]
    )
    b.h2("1.3 IDE")
    b.definition(
        "IDE",
        "An Integrated Development Environment is software that combines an editor, compiler, "
        "linker and debugger in one place. Examples: Turbo C, Dev-C++, Code::Blocks, Visual Studio.",
    )
    b.p("Typical Turbo C keys (older papers): <b>Alt+F9</b> compile, <b>Ctrl+F9</b> run, <b>Alt+F5</b> user screen.")
    b.h2("1.4 Basic structure of a C program (2026 Q.2 i)")
    b.add(Diagram("c_struct", 58 * mm))
    b.caption("Figure 1.1  Skeleton every C answer should follow.")
    b.code(
        """#include <stdio.h>   /* header for printf / scanf */

int main(void)
{
    /* declarations */
    int a;

    /* input, process, output */
    a = 5;
    printf("%d", a);

    return 0;        /* success */
}
""",
        "Minimum complete C program.",
    )
    b.h3("Parts of the structure")
    b.numbered(
        [
            "<b>Preprocessor directives</b> — lines starting with #, handled before compilation.",
            "<b>#include &lt;stdio.h&gt;</b> — inserts standard input/output declarations.",
            "<b>#define PI 3.14</b> — symbolic constant (macro).",
            "<b>Global declarations</b> — optional; known to every function.",
            "<b>main()</b> — the function every C program must contain (2026 MCQ).",
            "<b>Body</b> — statements between { } ending with semicolons.",
            "<b>Comments</b> — /* multi-line */ and // single line (C99). Ignored by compiler.",
        ]
    )
    b.h2("1.5 #include and #define (2026 Q.2 ii)")
    b.code(
        """#include <stdio.h>     /* standard library header */
#include <math.h>      /* sqrt, pow, abs related */
#define PI 3.14159
#define SQUARE(x) ((x)*(x))
""",
        "Two #include examples and two #define examples.",
    )
    b.p(
        "<b>Header files</b> contain function prototypes. Angle brackets &lt;stdio.h&gt; search the "
        "system include path; quotes \"my.h\" search the project folder first."
    )
    b.page_break()


def _c02(b):
    b.chapter_banner("02", "Tokens, Data Types, Operators and I/O", "Paper–II Option I", "MCQ + short programs")
    b.h2("2.1 Tokens")
    b.p("A token is the smallest unit of a C program: keywords, identifiers, constants, strings, operators, separators.")
    b.definition(
        "Keyword / reserved word",
        "A reserved word is a word that already has a meaning in C and cannot be used as a "
        "variable name. Examples: int, float, char, if, else, for, while, do, switch, case, "
        "break, continue, return, void, sizeof. (2026: name any three.)",
    )
    b.definition(
        "Identifier",
        "A name given to a variable, constant or function. Rules: start with a letter or underscore; "
        "then letters, digits, underscore; no spaces; case-sensitive; not a keyword. "
        "Valid: Number, NUMBER5, Number_5. Invalid: 5number (starts with digit).",
    )
    b.h2("2.2 Data types")
    b.table(
        ["Type", "Typical size", "Format", "Range (16/32-bit typical in papers)"],
        [
            ["char", "1 byte", "%c", "-128 to 127 (signed)"],
            ["int", "2 or 4 bytes", "%d", "-32768 to 32767 (2-byte)"],
            ["float", "4 bytes", "%f", "~10^-38 to 10^38, 6 digits"],
            ["double", "8 bytes", "%lf", "more precision than float"],
            ["void", "none", "—", "no value (functions)"],
        ],
    )
    b.exam_tip("% operator (modulus) works only with <b>integers</b>, not float/double. 2026 MCQ.")
    b.h2("2.3 Variables and constants")
    b.code(
        """int age = 17;          /* declaration + initialisation */
const float PI = 3.14; /* constant — cannot change */
char grade = 'A';      /* character constant in single quotes */
char name[] = "Ali";   /* string constant in double quotes */
""",
        "Defining, declaring and initialising.",
    )
    b.h2("2.4 Operators")
    b.table(
        ["Group", "Operators", "Notes"],
        [
            ["Arithmetic", "+  -  *  /  %", "% only on int; / on int truncates"],
            ["Assignment", "=  +=  -=  *=  /=  %=", "a += 2 means a = a + 2"],
            ["Increment", "++k (pre), k++ (post)", "pre changes then uses; post uses then changes"],
            ["Decrement", "--k, k--", "same idea"],
            ["Relational", "&lt;  &lt;=  &gt;  &gt;=  ==  !=", "== tests equality; = assigns"],
            ["Logical", "&amp;&amp;  ||  !", "AND, OR, NOT"],
            ["Conditional", "? :", "ternary"],
            ["Address", "&amp;", "gives the address of a variable (2026 Q)"],
            ["Indirection", "*", "value at a pointer"],
        ],
    )
    b.h3("Precedence (high → low) — 2026 MCQ: highest among + - / %")
    b.p(
        "Parentheses ( )  →  ++ -- unary !  →  * / %  →  + -  →  relational  →  == !=  →  "
        "&amp;&amp;  →  ||  →  ?:  →  assignment. Among * / % the same level, left-to-right. "
        "So between + - / %, <b>/</b> and <b>%</b> are higher than + and -."
    )
    b.h3("Worked expressions (style of 2026 Q.2 x)")
    b.p("If a = 2, b = 5, c = 10:")
    b.table(
        ["Expression", "Working", "Result"],
        [
            ["200*((a*10)+c)", "200*((2*10)+10)=200*(20+10)=200*30", "6000"],
            ["a*b*10/c+a+c", "2*5*10/10+2+10 → 100/10+2+10 → 10+2+10", "22"],
            ["a-(c/b)/2+100", "2-(10/5)/2+100 → 2-2/2+100 → 2-1+100", "101"],
        ],
    )
    b.p("Integer division: 10/5 = 2, 2/2 = 1. Always show steps.")
    b.h2("2.5 printf, scanf, getchar")
    b.table(
        ["Function", "Header", "Use"],
        [
            ["printf(format, …)", "stdio.h", "Output to screen"],
            ["scanf(format, &amp;vars)", "stdio.h", "Formatted input; needs address operator &amp;"],
            ["getchar()", "stdio.h", "Reads one character (including space)"],
            ["putchar(ch)", "stdio.h", "Writes one character"],
            ["gets / puts", "stdio.h", "Old string I/O — gets is unsafe; papers still mention it"],
            ["getch()", "conio.h", "Reads a key without Enter and without echo (Turbo C)"],
        ],
    )
    b.p(
        "<b>scanf vs getchar (2026):</b> scanf can read numbers and strings with format specifiers "
        "and skips leading whitespace for %d/%f. getchar reads exactly one character, does not need "
        "a format, and can read a space or newline. scanf needs &amp;; getchar does not."
    )
    b.h3("Format specifiers and escape sequences")
    b.table(
        ["Specifier", "Meaning", "Escape", "Meaning"],
        [
            ["%d", "int", "\\n", "new line"],
            ["%f", "float", "\\t", "tab"],
            ["%c", "char", "\\a", "alert / beep"],
            ["%s", "string", "\\\\", "backslash"],
            ["%lf", "double", "\\\"", "quote"],
            ["%u / %ld", "unsigned / long", "\\0", "string terminator (null)"],
        ],
    )
    b.h2("2.6 Convert formulae to C (2026 Q.2 xiii)")
    b.table(
        ["Mathematics", "C statement"],
        [
            ["A = ½ × base × height", "A = 0.5 * base * height;"],
            ["x = 3ab³ + 3a²b", "x = 3*a*b*b*b + 3*a*a*b;"],
            ["d = |b² − 4ac|", "d = fabs(b*b - 4*a*c);   /* need math.h */"],
            ["A = πr²", "A = 3.1416 * r * r;"],
        ],
    )
    b.page_break()


def _c03(b):
    b.chapter_banner("03", "Decision Making — if and switch", "Paper–II Option I", "Section C: switch")
    b.add(Diagram("if", 58 * mm))
    b.caption("Figure 3.1  Selection structure.")
    b.h2("3.1 if, if-else, nested if, else-if ladder")
    b.code(
        """#include <stdio.h>
int main(void) {
    int a, b, max;
    printf("Enter two integers: ");
    scanf("%d %d", &a, &b);
    if (a > b)
        max = a;
    else
        max = b;
    printf("Greater = %d", max);
    return 0;
}
""",
        "Greater of two numbers — also required as a function in 2026 Q.2 xii.",
    )
    b.code(
        """if (marks >= 80)
    printf("A+");
else if (marks >= 70)
    printf("A");
else if (marks >= 60)
    printf("B");
else
    printf("Fail");
""",
        "else-if ladder for a mark sheet.",
    )
    b.h2("3.2 switch statement (2026 Section C Q.3)")
    b.definition(
        "switch",
        "switch is a multi-way selection statement that compares an integer (or char) expression "
        "with several case labels and jumps to the matching block. A break prevents fall-through. "
        "default runs when no case matches.",
    )
    b.code(
        """switch (choice) {
    case 1:
        printf("Red colour");
        break;
    case 2:
        printf("Black colour");
        break;
    case 3:
        printf("White colour");
        break;
    default:
        printf("No colour");
}
""",
        "This is the classic conversion from a nested if-else (past papers).",
    )
    b.h3("Rules of switch")
    b.numbered(
        [
            "The switch expression must be int or char (not float).",
            "case labels must be constant (not variables).",
            "Write break after each case unless you want fall-through.",
            "default is optional but recommended.",
            "No two cases can have the same label.",
        ]
    )
    b.p("In Section C, draw a flowchart: diamond 'choice?' with arrows to case 1, 2, 3 and default.")
    b.page_break()


def _c04(b):
    b.chapter_banner("04", "Loops — for, while, do-while, nested", "Paper–II Option I", "Programs every year")
    b.definition(
        "Loop / iteration",
        "A loop is a control structure that repeats a block of statements while a condition remains true.",
    )
    b.add(Diagram("for", 48 * mm))
    b.caption("Figure 4.1  for-loop: init → test → body → increment → test …")
    b.h2("4.1 Three loops")
    b.code(
        """/* for: used when count is known */
int i;
for (i = 1; i <= 10; i++)
    printf("%d ", i);

/* while: test first — may run zero times */
int n = 1;
while (n <= 10) {
    printf("%d ", n);
    n++;
}

/* do-while: body first — runs at least once */
int m = 1;
do {
    printf("%d ", m);
    m++;
} while (m <= 10);
""",
        "Print 1 to 10 with each loop.",
    )
    b.table(
        ["for", "while", "do-while"],
        [
            ["All three parts in the header", "Only condition in header", "Condition at the bottom"],
            ["Best when count is known", "Best when count is unknown", "Menu / 'try again'"],
            ["May run 0 times", "May run 0 times", "Always at least once"],
        ],
    )
    b.h2("4.2 break and continue (2026 Q.2 iv)")
    b.table(
        ["break", "continue"],
        [
            ["Leaves the loop (or switch) immediately", "Skips the rest of this iteration"],
            ["Control goes to the statement after the loop", "Control goes to the next test / increment"],
            ["Used to exit early", "Used to skip unwanted cases"],
        ],
    )
    b.exam_tip(
        "2026 MCQ: 'skip the rest of a loop and carry on from the top' = <b>continue</b>, not break.",
    )
    b.h2("4.3 Board programs")
    b.h3("Multiplication table of an inputted number (2026 Q.2 iii)")
    b.code(
        """#include <stdio.h>
int main(void) {
    int n, i;
    printf("Enter a number: ");
    scanf("%d", &n);
    for (i = 1; i <= 10; i++)
        printf("%d x %d = %d\\n", n, i, n * i);
    return 0;
}
"""
    )
    b.h3("Factorial (2026 Q.2 vii)  hint 4! = 24")
    b.code(
        """#include <stdio.h>
int main(void) {
    int n, i;
    long fact = 1;
    printf("Enter n: ");
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
        fact = fact * i;
    printf("Factorial = %ld", fact);
    return 0;
}
"""
    )
    b.h3("Nested loops — two classic patterns (2026 Q.2 xiv)")
    b.code(
        """/* Pattern A:  1
               12
               123
               1234
               12345          */
int i, j;
for (i = 1; i <= 5; i++) {
    for (j = 1; j <= i; j++)
        printf("%d", j);
    printf("\\n");
}

/* Pattern B: number and square
   1  1
   2  4
   3  9
   4  16
   5  25                       */
for (i = 1; i <= 5; i++)
    printf("%d\\t%d\\n", i, i * i);
"""
    )
    b.h3("Even numbers 0–50")
    b.code(
        """int i;
for (i = 0; i <= 50; i += 2)
    printf("%d ", i);
"""
    )
    b.h3("Prime or composite")
    b.code(
        """int n, i, flag = 0;
scanf("%d", &n);
if (n <= 1) flag = 1;
for (i = 2; i <= n / 2; i++) {
    if (n % i == 0) { flag = 1; break; }
}
if (flag == 0) printf("Prime");
else printf("Composite / not prime");
"""
    )
    b.page_break()


def _c05(b):
    b.chapter_banner("05", "Functions", "Paper–II Option I", "Section C + 2026 greater-number program")
    b.definition(
        "Function",
        "A function is a named, independent block of code that performs a specific task and "
        "can be called from other parts of the program. main() is also a function.",
    )
    b.h2("5.1 Why functions? (characteristics — 2026 Q.5)")
    b.numbered(
        [
            "<b>Modularity</b> — split a large program into small jobs.",
            "<b>Reusability</b> — write once, call many times.",
            "<b>Easy debugging</b> — test one block at a time.",
            "<b>Team work</b> — different programmers write different functions.",
            "<b>Readability</b> — names describe actions (e.g. factorial).",
            "<b>Returns a value</b> (or void) to the caller through return.",
        ]
    )
    b.h2("5.2 Prototype, definition, call")
    b.code(
        """#include <stdio.h>

int greater(int x, int y);     /* prototype / declaration */

int main(void) {
    int a, b, g;
    printf("Enter two integers: ");
    scanf("%d %d", &a, &b);
    g = greater(a, b);         /* call — a,b are actual parameters */
    printf("Greater = %d", g);
    return 0;
}

int greater(int x, int y) {    /* definition — x,y are formal parameters */
    if (x > y)
        return x;
    else
        return y;
}
""",
        "2026 Q.2 xii complete program.",
    )
    b.table(
        ["Actual parameters", "Formal parameters"],
        [
            ["Values passed at the call", "Variables in the function header"],
            ["a, b in greater(a,b)", "x, y in int greater(int x, int y)"],
        ],
    )
    b.h2("5.3 Local vs global (2026 Q in older papers; still useful)")
    b.table(
        ["Local (automatic)", "Global (external)"],
        [
            ["Declared inside a function", "Declared outside all functions"],
            ["Known only in that function", "Known to every function"],
            ["Created on entry, destroyed on exit", "Lives for the whole program"],
            ["Prefer these", "Use sparingly"],
        ],
    )
    b.h2("5.4 Passing arguments")
    b.bullets(
        [
            "<b>Pass by value</b> — a copy is sent; changes inside the function do not affect the original.",
            "<b>Pass by reference / address</b> — the address is sent (&amp;x); the function can change the original through a pointer.",
        ]
    )
    b.page_break()


def _c06(b):
    b.chapter_banner("06", "Arrays, Strings and Structures", "Paper–II Option I", "Practical + nested programs")
    b.definition(
        "Array",
        "An array is a collection of elements of the <b>same data type</b> stored in contiguous "
        "memory, sharing one name and distinguished by an index. The first index is 0.",
    )
    b.code(
        """int marks[5];                 /* declaration, size 5 */
int a[5] = {10, 20, 30, 40, 50};  /* initialisation */
marks[0] = 80;                /* access element */
int i, sum = 0;
for (i = 0; i < 5; i++)
    sum = sum + a[i];
printf("Average = %d", sum / 5);
"""
    )
    b.h3("Sort ten numbers ascending (classic Section C)")
    b.code(
        """int a[10], i, j, t;
for (i = 0; i < 10; i++)
    scanf("%d", &a[i]);
for (i = 0; i < 9; i++)
    for (j = i + 1; j < 10; j++)
        if (a[i] > a[j]) {
            t = a[i]; a[i] = a[j]; a[j] = t;
        }
for (i = 0; i < 10; i++)
    printf("%d ", a[i]);
"""
    )
    b.h2("6.1 Two-dimensional arrays")
    b.code(
        """int m[3][3], i, j;
for (i = 0; i < 3; i++)
    for (j = 0; j < 3; j++)
        scanf("%d", &m[i][j]);
"""
    )
    b.h2("6.2 Strings")
    b.p(
        "A string is a char array ended by the null terminator <b>'\\0'</b>. "
        "char name[20] = \"Karachi\";"
    )
    b.table(
        ["Function", "Header", "Job"],
        [
            ["strlen(s)", "string.h", "Length without '\\0'"],
            ["strcpy(d,s)", "string.h", "Copy s into d"],
            ["strcat(d,s)", "string.h", "Join s onto the end of d"],
            ["strcmp(a,b)", "string.h", "0 if equal; &lt;0 if a&lt;b; &gt;0 if a&gt;b"],
        ],
    )
    b.h3("Reverse a name using strlen")
    b.code(
        """char s[50];
int i, n;
gets(s);               /* or scanf("%s", s) for one word */
n = strlen(s);
for (i = n - 1; i >= 0; i--)
    putchar(s[i]);
"""
    )
    b.h2("6.3 Structures (short)")
    b.code(
        """struct employee {
    char name[30];
    char desig[20];
    float salary;
};
struct employee e;
printf("Name: "); scanf("%s", e.name);
printf("Pay: ");  scanf("%f", &e.salary);
printf("%s  %.2f", e.name, e.salary);
"""
    )
    b.page_break()


def _c07(b):
    b.chapter_banner("07", "Pointers (address operator) and a note on files", "Paper–II Option I", "2026 asks &amp;")
    b.definition(
        "Pointer",
        "A pointer is a variable that stores the <b>memory address</b> of another variable. "
        "The address operator <b>&amp;</b> gives an address; the dereference operator <b>*</b> "
        "gives the value at that address.",
    )
    b.code(
        """int x = 10;
int *p;        /* p is a pointer to int */
p = &x;        /* p holds the address of x */
printf("Address = %p\\n", (void*)p);
printf("Value   = %d\\n", *p);   /* 10 */
*p = 25;       /* x becomes 25 */
"""
    )
    b.p(
        "scanf(\"%d\", &amp;n) uses the address operator because scanf must write into n. "
        "printf(\"%d\", n) does not need &amp; because it only reads the value."
    )
    b.h3("Double two numbers using pointers (practical list)")
    b.code(
        """void double_them(int *a, int *b) {
    *a = *a * 2;
    *b = *b * 2;
}
int main(void) {
    int x = 3, y = 4;
    double_them(&x, &y);
    printf("%d %d", x, y);   /* 6 8 */
    return 0;
}
"""
    )
    b.h2("7.1 File handling (short — useful extra)")
    b.p("Text files store characters; binary files store raw bytes. Modes: \"r\" read, \"w\" write, \"a\" append.")
    b.code(
        """FILE *fp = fopen("notes.txt", "w");
if (fp != NULL) {
    fprintf(fp, "BIEK Computer Science\\n");
    fclose(fp);
}
"""
    )
    b.page_break()


def _db01(b):
    b.chapter_banner("08", "Database Fundamentals and DBMS", "Paper–II both options", "2026 Section B + C")
    b.definition(
        "Database",
        "A database is an organised collection of related data stored so that it can be retrieved "
        "and updated efficiently. Example: student records, library books, bank accounts.",
    )
    b.definition(
        "DBMS",
        "A Database Management System is software that creates, maintains and controls access "
        "to a database. Examples: MS-Access, MySQL, Oracle, SQL Server.",
    )
    b.h2("8.1 File system vs DBMS")
    b.table(
        ["Flat / file system", "DBMS"],
        [
            ["Data in separate files for each program", "Central shared database"],
            ["High redundancy (same name stored many times)", "Controlled redundancy"],
            ["Inconsistency risk", "Integrity constraints keep data consistent"],
            ["Data depends on the program", "Data independence"],
            ["Weak security", "Users, passwords, privileges"],
            ["Hard to query ad-hoc", "SQL / QBE"],
        ],
    )
    b.h2("8.2 Advantages of DBMS (Option II 2026 Q.2 i)")
    b.numbered(
        [
            "Less data redundancy.",
            "Data consistency and integrity.",
            "Data can be shared by many programs / users.",
            "Security and backup.",
            "Easy queries, forms and reports.",
            "Data independence — change storage without rewriting all programs.",
        ]
    )
    b.h2("8.3 Components of DBMS (2026 Q.2 xi Option I)")
    b.table(
        ["Component", "Role"],
        [
            ["Hardware", "Servers, disks, network"],
            ["Software", "The DBMS itself plus OS"],
            ["Data", "Actual stored facts"],
            ["Procedures", "Rules for backup, recovery, use"],
            ["People / users", "DBA, designers, programmers, end users"],
            ["Data access language", "SQL"],
        ],
    )
    b.h2("8.4 Database users")
    b.bullets(
        [
            "<b>DBA (Database Administrator)</b> — installs DBMS, creates users, backup, performance, security. "
            "Responsibilities (2026 VB Q): user accounts, recovery, tuning, enforcing standards.",
            "<b>Application programmer</b> — writes programs / forms that use the database.",
            "<b>End user</b> — enters and reads data through forms (clerk, teacher, cashier).",
        ]
    )
    b.h2("8.5 Three levels of data abstraction")
    b.add(Diagram("dbms", 58 * mm))
    b.caption("Figure 8.1  External, logical and physical levels.")
    b.h2("8.6 Data models (2026 Section C Q.6 both options)")
    b.definition(
        "Data model",
        "A data model is a set of concepts used to describe the structure of a database — "
        "how data is organised and how items relate to each other.",
    )
    b.add(Diagram("hier", 62 * mm))
    b.caption("Figure 8.2  Hierarchical model — tree of parent/child records (IMS).")
    b.table(
        ["Model", "Structure", "Plus / minus"],
        [
            ["Hierarchical", "Tree; one parent, many children", "Fast for 1:M; hard for M:M"],
            ["Network", "Graph; a child may have many parents (CODASYL)", "Flexible; complex pointers"],
            ["Relational", "Tables (relations) with rows and columns; SQL", "Simple, used in Access/MySQL"],
            ["E-R model", "Entities, attributes, relationships (design drawing)", "Used at design time"],
            ["Object / OR", "Objects with methods + tables", "Fits OOP applications"],
        ],
    )
    b.p("2026 MCQ (VB): the model that organises data into a <b>tree</b> is Hierarchical. The model that allows SQL is <b>Relational</b>.")
    b.h2("8.7 Relational terms")
    b.table(
        ["Term", "Also called", "Meaning"],
        [
            ["Table", "Relation", "A named 2-D grid of data"],
            ["Row", "Tuple / record", "One complete object (one student)"],
            ["Column", "Attribute / field", "One property (Name, Marks)"],
            ["Domain", "Data type of a column", "Allowed values"],
            ["Schema", "Design of the database", "Table names + fields + keys"],
        ],
    )
    b.h2("8.8 Keys")
    b.add(Diagram("keys", 48 * mm))
    b.caption("Figure 8.3  Primary key and foreign key.")
    b.table(
        ["Key", "Definition"],
        [
            ["Primary key", "One or more fields that uniquely identify each record; not null, not duplicate"],
            ["Foreign key", "A field whose values match the primary key of another table — the link"],
            ["Candidate key", "Any field(s) that could be chosen as primary key"],
            ["Composite key", "A primary key made of two or more fields"],
            ["Super key", "Any set of fields that uniquely identifies a row (may have extras)"],
        ],
    )
    b.exam_tip("2026 C-option short Q: differentiate Primary key and Foreign key. Write: unique vs linking; in parent vs in child table.")
    b.h2("8.9 Relationships")
    b.table(
        ["Type", "Example"],
        [
            ["One to one (1:1)", "One citizen ↔ one CNIC record"],
            ["One to many (1:M)", "One class ↔ many students  (most common)"],
            ["Many to many (M:M)", "Students ↔ courses — needs a third (junction) table"],
        ],
    )
    b.h2("8.10 Integrity and a taste of normalisation")
    b.bullets(
        [
            "<b>Entity integrity</b> — primary key cannot be NULL.",
            "<b>Referential integrity</b> — foreign key must match an existing PK or be NULL.",
            "<b>Domain integrity</b> — values match the data type / validation rule.",
            "<b>1NF</b> — atomic values, no repeating groups.",
            "<b>2NF</b> — 1NF + no partial dependence on part of a composite PK.",
            "<b>3NF</b> — 2NF + no transitive dependence on non-key fields.",
        ]
    )
    b.h2("8.11 SQL snapshot")
    b.code(
        """CREATE TABLE Student (
    RollNo  INT PRIMARY KEY,
    SName   VARCHAR(40),
    Class   VARCHAR(10)
);
INSERT INTO Student VALUES (1, 'Ahmed', 'XII');
SELECT SName, Class FROM Student WHERE RollNo = 1;
UPDATE Student SET Class = 'XI' WHERE RollNo = 1;
DELETE FROM Student WHERE RollNo = 1;
"""
    )
    b.p("<b>Selection</b> chooses rows (WHERE). <b>Projection</b> chooses columns (the SELECT list).")
    b.page_break()


def _db02(b):
    b.chapter_banner("09", "MS-Access — Objects and Data Types", "Paper–II both options", "2026 Q.7 data types")
    b.h2("9.1 Objects of MS-Access (2026: define any four / primary object)")
    b.table(
        ["Object", "Job"],
        [
            ["Table", "Stores data — the <b>primary object</b> (2026 C-option MCQ)"],
            ["Query", "Questions the data; select, update, make-table; SQL behind the scenes"],
            ["Form", "Screen for entering and displaying one record at a time"],
            ["Report", "Printed / PDF output for display (2026 VB MCQ)"],
            ["Macro", "Saved actions (open form, print report)"],
            ["Module", "VBA code"],
        ],
    )
    b.h2("9.2 Data types in MS-Access (write ALL in Section C)")
    b.table(
        ["Data type", "Stores"],
        [
            ["Text / Short Text", "Names, up to 255 characters"],
            ["Memo / Long Text", "Long remarks"],
            ["Number", "Integers and real numbers (Byte, Integer, Long, Single, Double)"],
            ["Date/Time", "Dates and times"],
            ["Currency", "Money, 4 decimal places, no round-off"],
            ["AutoNumber", "Automatic unique integer — often used as PK"],
            ["Yes/No", "Boolean True/False"],
            ["OLE Object", "Pictures, Word files (older)"],
            ["Hyperlink", "URL or email"],
            ["Attachment", "Files attached to a record (newer Access)"],
            ["Lookup Wizard", "Drop-down from another table or list"],
            ["Calculated", "Value computed from other fields"],
        ],
    )
    b.h2("9.3 Field properties (practical)")
    b.bullets(
        [
            "Field Size, Format, Input Mask, Caption.",
            "Default Value, Validation Rule / Text.",
            "Required, Indexed, Primary Key button.",
        ]
    )
    b.h2("9.4 Planning a small database (library example)")
    b.numbered(
        [
            "Purpose: issue books to students.",
            "Tables: STUDENT (RollNo PK, Name, Class), BOOK (ISBN PK, Title, Author), ISSUE (IssueID PK, RollNo FK, ISBN FK, Date).",
            "1:M from STUDENT to ISSUE and BOOK to ISSUE.",
            "Normalise to 3NF: do not store student name inside ISSUE — look it up.",
            "Build tables, relationships (Enforce Referential Integrity), then a query and a report.",
        ]
    )
    b.page_break()


def _vb01(b):
    b.chapter_banner("10", "Visual Basic — Option II", "Paper–II Option II", "Skip this lecture if you offered C")
    b.definition(
        "Visual Basic",
        "Visual Basic (VB) is an event-driven, object-based programming language from Microsoft "
        "used to build Windows GUI applications. Code runs in response to events such as Click.",
    )
    b.h2("10.1 IDE and the form")
    b.bullets(
        [
            "Form is the window; its Name, Caption, BackColor, BorderStyle are properties.",
            "Code window holds event procedures: Private Sub Command1_Click() … End Sub.",
            "Toolbox holds ActiveX / intrinsic controls.",
        ]
    )
    b.h2("10.2 Basic ActiveX / intrinsic controls (2026 Q)")
    b.table(
        ["Control", "Use", "Important properties"],
        [
            ["Form", "Container window", "Caption, Name; Cancel button property is of a <b>Button</b> (2026 MCQ)"],
            ["Label", "Display text the user does not type", "Caption, Font"],
            ["Text Box", "User types data", "Text, MaxLength, PasswordChar, Multiline, Locked"],
            ["Command Button", "Click to run code", "Caption, Enabled, Default, Cancel"],
            ["Check Box", "On/off options (many at once)", "Value 0/1/2"],
            ["Option Button", "Choose exactly one from a group", "Value True/False"],
            ["Combo Box", "Drop-down list + optional typing", "Text, List, ListIndex, Style"],
            ["List Box", "List of items", "List, ListCount, MultiSelect"],
            ["Image / Picture Box", "Pictures", "Picture, Stretch"],
            ["Timer", "Events by interval", "Interval (ms), Enabled"],
        ],
    )
    b.h3("Combo Box (2026 Q.2 ii)")
    b.p(
        "A Combo Box combines a text box and a list. Properties: Name, Text, List, ListIndex, "
        "Sorted, Style (0 DropDown Combo, 1 Simple, 2 DropDown List). Methods: AddItem, RemoveItem, Clear."
    )
    b.h3("Text Box properties (2026 Q.2 x)")
    b.p("Text, Font, ForeColor, MaxLength, PasswordChar, Multiline, ScrollBars, Alignment, Locked, Enabled, TabIndex, ToolTipText.")
    b.h2("10.3 Variables in VB")
    b.code(
        """Dim n As Integer          ' explicit type
Dim x As Variant         ' default if type omitted; also: Dim x
Dim name As String
Const PI As Double = 3.1416
"""
    )
    b.p(
        "<b>DIM</b> declares a variable (2026 MCQ). Variant can hold any type and is the default. "
        "Passing a copy is <b>ByVal</b>; passing the original is <b>ByRef</b> (default in older VB)."
    )
    b.h2("10.4 Select Case (2026 Q.2 vi)")
    b.code(
        """Select Case choice
    Case 1
        Label1.Caption = "Red"
    Case 2
        Label1.Caption = "Black"
    Case 3
        Label1.Caption = "White"
    Case Else
        Label1.Caption = "No colour"
End Select
"""
    )
    b.h2("10.5 Loops in VB (2026 Section C Q.4)")
    b.code(
        """Dim i As Integer
For i = 0 To 50 Step 2        ' even numbers 0-50  (2026 Q.2 xiii)
    Print i
Next i

Dim sum As Double, k As Integer, n As Double
sum = 0
For k = 1 To 10               ' sum and average of 10 inputs (Q.2 xiv)
    n = Val(InputBox("Number " & k))
    sum = sum + n
Next k
MsgBox "Sum=" & sum & "  Avg=" & sum / 10

Do While i < 10
    i = i + 1
Loop
"""
    )
    b.p("Default Step of For…Next is <b>1</b> (2026 MCQ).")
    b.h2("10.6 Arrays in VB (2026 Section C Q.3)")
    b.code(
        """Dim a(1 To 10) As Integer          ' static / fixed array
Dim b() As Integer                 ' dynamic
ReDim b(1 To n)
' Control array: several Command buttons sharing one name, Index 0,1,2…
"""
    )
    b.p("Types: one-dimensional, two-dimensional, dynamic (ReDim), control arrays.")
    b.h2("10.7 Built-in functions (2026 Q.5)")
    b.table(
        ["Function", "Job"],
        [
            ["Val(s)", "Text to number"],
            ["Str(n) / CStr", "Number to text"],
            ["Len(s), Left, Right, Mid", "String length and slices"],
            ["UCase / LCase", "Case conversion"],
            ["Int / Fix / Round", "Whole numbers"],
            ["Sqr, Abs, Sin", "Math (need no extra include)"],
            ["Date, Time, Now", "System clock"],
            ["InputBox / MsgBox", "Simple I/O dialogs"],
            ["IsNumeric", "Validation"],
        ],
    )
    b.code(
        """Private Sub Command1_Click()
    Dim r As Double, area As Double
    r = Val(Text1.Text)
    area = 3.1416 * r * r
    Label1.Caption = "Area = " & Format(area, "0.00")
End Sub
""",
        "Built-in Val + arithmetic on a Click event.",
    )
    b.h2("10.8 VB equivalent of formulae (2026 Q.2 xi)")
    b.table(
        ["Math", "VB"],
        [
            ["X = (ab)² / c³", "X = (a * b) ^ 2 / c ^ 3"],
            ["Y = (4/3) π r³", "Y = (4 / 3) * 3.1416 * r ^ 3"],
            ["Y = (a + b)² / n³", "Y = (a + b) ^ 2 / n ^ 3"],
            ["A = ½ × base × height", "A = 0.5 * base * height"],
        ],
    )
    b.h2("10.9 Errors in VB (2026 Q.2 xii)")
    b.table(
        ["Type", "Example"],
        [
            ["Syntax", "Missing End If, misspelt keyword"],
            ["Logic", "Wrong formula, off-by-one in a loop"],
            ["Run-time", "Divide by zero, type mismatch, file not found"],
        ],
    )
    b.h2("10.10 Full forms (2026 Q.2 ix)")
    b.table(
        ["Abbrev.", "Full form"],
        [
            ["ADO", "ActiveX Data Objects"],
            ["MDI", "Multiple Document Interface"],
            ["SQL", "Structured Query Language"],
            ["DBA", "Database Administrator"],
            ["OLE", "Object Linking and Embedding"],
        ],
    )
    b.page_break()


def _programs(b):
    b.chapter_banner("11", "Practical program bank (C Option I)", "Paper–II", "Write these in the journal")
    b.h3("P1. Simple calculator")
    b.code(
        """#include <stdio.h>
int main(void) {
    char op; float a, b;
    printf("Enter a op b: ");
    scanf("%f %c %f", &a, &op, &b);
    switch (op) {
        case '+': printf("%.2f", a + b); break;
        case '-': printf("%.2f", a - b); break;
        case '*': printf("%.2f", a * b); break;
        case '/':
            if (b != 0) printf("%.2f", a / b);
            else printf("Division by zero");
            break;
        default: printf("Unknown operator");
    }
    return 0;
}
"""
    )
    b.h3("P2. Four-digit number — print each digit on a new line")
    b.code(
        """int n, d1, d2, d3, d4;
scanf("%d", &n);          /* e.g. 2584 */
d1 = n / 1000;
d2 = (n / 100) % 10;
d3 = (n / 10) % 10;
d4 = n % 10;
printf("%d\\n%d\\n%d\\n%d", d1, d2, d3, d4);
"""
    )
    b.h3("P3. Factors of n")
    b.code(
        """int n, i;
scanf("%d", &n);
for (i = 1; i <= n; i++)
    if (n % i == 0) printf("%d ", i);
"""
    )
    b.h3("P4. Search a number in a list")
    b.code(
        """int a[10], key, i, found = 0;
for (i = 0; i < 10; i++) scanf("%d", &a[i]);
scanf("%d", &key);
for (i = 0; i < 10; i++)
    if (a[i] == key) { found = 1; break; }
if (found) printf("Found at index %d", i);
else printf("Not found");
"""
    )
    b.h3("P5. Add two 3×3 matrices")
    b.code(
        """int a[3][3], b[3][3], c[3][3], i, j;
for (i = 0; i < 3; i++)
    for (j = 0; j < 3; j++) scanf("%d", &a[i][j]);
for (i = 0; i < 3; i++)
    for (j = 0; j < 3; j++) scanf("%d", &b[i][j]);
for (i = 0; i < 3; i++) {
    for (j = 0; j < 3; j++) {
        c[i][j] = a[i][j] + b[i][j];
        printf("%d ", c[i][j]);
    }
    printf("\\n");
}
"""
    )
    b.page_break()


def _xii_bank(b):
    b.chapter_banner("12", "MCQ one-liners (C + DBMS + VB)", "Paper–II", "Last-night revision")
    b.numbered(
        [
            "Every C program must contain main(). Dennis Ritchie founded C.",
            "A person who writes application programs is a Programmer.",
            "C programs become machine language with a Compiler (not assembler).",
            "5number is an invalid identifier. % works only with int.",
            "k++ is post increment. Highest of + − / % is / and % (same level, above + −).",
            "continue skips the rest of this iteration. break leaves the loop.",
            "Names of variables are identifiers.",
            "for is an iteration (loop) structure.",
            "Primary key uniquely identifies a row. Table is the primary Access object.",
            "DBMS advantage: data is integrated and shared. Report displays/prints data.",
            "Columns = attributes. Rows = records/tuples.",
            "Hierarchical model is a tree. Relational model uses SQL.",
            "Option Button selects one choice; Check Box is independent Yes/No.",
            "DIM declares a variable. Default For Step is 1. Cancel button property belongs to Button.",
            "A sub program that returns a value is a Function. ByVal = pass a copy.",
        ]
    )
    b.page_break()


def _model(b):
    b.chapter_banner("13", "Solved Model Paper 2026 — Paper–II", "Paper–II", "Option I and Option II")
    b.h2("Option I — Programming Using C")
    b.h3("Section A (MCQs)")
    b.table(
        ["#", "Answer"],
        [
            ["i", "main()"],
            ["ii", "C  (Dennis Ritchie)"],
            ["iii", "Programmer"],
            ["iv", "Compiler"],
            ["v", "5number  (invalid identifier)"],
            ["vi", "int"],
            ["vii", "k++"],
            ["viii", "/  and  %  (higher than + −; if only one bubble, pick / or % as printed)"],
            ["ix", "Primary key"],
            ["x", "continue"],
            ["xi", "data is integrated and can be accessed by multiple programs"],
            ["xii", "Table"],
            ["xiii", "identifiers"],
            ["xiv", "Iteration structure"],
            ["xv", "Follow the remaining printed option on the OMR — typically a DBMS/C mix"],
        ],
    )
    b.p(
        "The official PDF extract of Q.xiv ends at 'Top d…' (top-down). for() is used when we need "
        "an <b>iteration structure</b>."
    )
    b.h3("Section B — model points (attempt any ten)")
    b.qa("i Basic structure of C", "See Lecture 1 code: include, main, declarations, statements, return 0.")
    b.qa("ii #include or #define", "#include &lt;stdio.h&gt;; #include &lt;math.h&gt;; #define PI 3.14; #define MAX 100.")
    b.qa("iii Multiplication table", "Lecture 4 complete for-loop program.")
    b.qa("iv break vs continue", "Lecture 4 table.")
    b.qa("v Reserved words", "int, float, return (any three). Cannot be identifiers.")
    b.qa("vi Address operator", "&amp;x is the address of x; used in scanf(\"%d\", &amp;x) and pointers.")
    b.qa("vii Factorial", "Lecture 4 program; 4! = 24.")
    b.qa("viii scanf vs getchar", "Lecture 2 paragraph.")
    b.qa("ix Primary vs Foreign key", "Lecture 8 table.")
    b.qa("x Expressions a=2,b=5,c=10", "6000 ; 22 ; 101  (Lecture 2 working).")
    b.qa("xi Major components of DBMS", "Hardware, software, data, procedures, users, SQL.")
    b.qa("xii Greater number using a function", "Lecture 5 complete program.")
    b.qa("xiii Three formulae in C", "Lecture 2 conversion table.")
    b.qa("xiv Nested pattern A or B", "Lecture 4 nested-loop code.")
    b.qa("xv Table, Query, Report", "Lecture 9 one-line each.")
    b.h3("Section C — pick any three")
    b.qa("3 switch with logical diagram", "Definition, syntax, rules, colour example, flowchart of cases.")
    b.qa("4 Types of operators in C", "Arithmetic, assignment, increment, relational, logical, conditional, bitwise (mention), address. One example each.")
    b.qa("5 Characteristics of a function with example", "Lecture 5 six points + greater() program.")
    b.qa("6 Data models in DBMS", "Hierarchical, network, relational, ER, object — definition + diagram of at least two.")
    b.qa("7 Data types in MS-Access", "Write the full table in Lecture 9 with one example value each.")

    b.h2("Option II — Visual Basic")
    b.h3("Section A")
    b.table(
        ["#", "Answer"],
        [
            ["i", "Button  (Cancel property)"],
            ["ii", "1  (default Step)"],
            ["iii", "Record"],
            ["iv", "Report"],
            ["v", "Primary Key"],
            ["vi", "Check Box  (Yes/No) — if the stem is 0/1; Option Button if 'only one from a group'"],
            ["vii", "Relational  (comparison operators)"],
            ["viii", "Pass by value"],
            ["ix", "Return"],
            ["x", "Attributes"],
            ["xi", "Hierarchical model"],
            ["xii", "Option Button"],
            ["xiii", "Function"],
            ["xiv", "Variable  (DIM)"],
            ["xv", "Relational"],
        ],
    )
    b.h3("Section B / C")
    b.p(
        "Use Lectures 8–10: four DBMS advantages; Combo Box properties; Dim x As Variant; "
        "1:M relationship diagram; four Access objects; Select Case structure; DBA duties; "
        "ActiveX controls; ADO/MDI/SQL/DBA/OLE; Text Box properties; formula conversions; "
        "error types; even 0–50 loop; sum and average of ten numbers; PK vs FK. "
        "Long: arrays with types; two loops with examples; built-in function program; "
        "all data models with diagrams; all Access data types."
    )
    b.h2("Practical checklist — Class XII")
    b.numbered(
        [
            "C: calculator, mark sheet, prime, factorial, table, sort array, reverse string, structure of employee.",
            "C: class STUDENT with age and percentage; constructor-style initialisation if your lab uses C++.",
            "Pointers: print address and value; double two numbers via pointers.",
            "Files: write and read a text file.",
            "Access: create table, set PK, change field size, insert/update/delete, SELECT with WHERE.",
            "VB (if offered): form with TextBox + Button + Label; even-number loop; area of circle.",
        ]
    )
    b.spacer(6)
    b.p(
        "<i>End of Class XII / Paper–II lectures. Revise Paper–I theory from the XI book. "
        "On exam day, read OR options, write complete C programs, and draw OSI / topology / data-model diagrams in pencil with labels.</i>",
        "center",
    )
