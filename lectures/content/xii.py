"""BIEK Computer Science II (Class XII) lectures — C, VB, Access, Sindh units."""

from diagrams import class_object, er_library
from content.blocks import check, code, defn, exam, example, flow, h, h3, learn, lec, mcq, ol, p, table, tip, ul, urdu, warn, svg

LECTURES = []


def add(d):
    LECTURES.append(d)


add(lec(
    id="xii-00",
    grade="XII",
    unit="0",
    unit_title="Paper II map",
    title="BIEK Paper II: Option I (C) or Option II (Visual Basic)",
    option="Paper pattern",
    slos=[
        "Choose the option you studied in college — you cannot mix C and VB in one paper",
        "State that Database / MS Access is common to both options",
        "Know Section A 15 MCQs, Section B 10 of 15 shorts, Section C 3 of 5 longs (2026 model)",
    ],
    body=[
        learn(
            "Paper II is 75 marks. The front page says: attempt ONE option — Programming using C OR Programming using Visual Basic. Database questions (keys, MS Access objects, data models, SQL) appear in BOTH options.",
        ),
        table(
            ["", "Option I — C", "Option II — Visual Basic"],
            [
                ["Language", "Turbo C / ANSI C in answer book", "VB 6 style forms + code"],
                ["Typical programs", "factorial, table, greater of two, patterns, functions", "even numbers, sum/average, tax slabs, calculator form"],
                ["Theory", "tokens, operators, loops, arrays, functions, pointers", "controls, DIM, loops, arrays, built-in functions, errors"],
                ["Shared", "DBMS, tables, keys, ER, Access data types, SQL", "same"],
            ],
        ),
        p("Sindh Curriculum 2019 Grade XII also includes SDLC, pointers, OOP with C++, file handling, multimedia and wireless. Colleges that follow the new book still need C or VB for the BIEK paper, so this pack teaches both the board options and the extra Sindh units."),
        exam("2026 Option I shorts: structure of C, #include/#define, multiplication table, break vs continue, reserved words, address operator, factorial, scanf vs getchar, primary vs foreign key, expression values, DBMS components, function to print greater number, maths→C, nested-loop patterns, table/query/report."),
        warn("void is a reserved word, so it is an invalid identifier. Identifiers cannot start with a digit or contain a space: 1st number is invalid; std_marks is valid."),
        urdu(
            "بارہویں کا پیپر ٹو دو آپشن میں ہے: C زبان یا Visual Basic۔ دونوں میں MS Access / ڈیٹا بیس آتا ہے۔ جو آپشن کالج میں پڑھا ہے وہی حل کریں۔",
        ),
        check(
            ("Can you answer a C long question in the VB option?", "No — pick one option for the whole paper"),
            ("Is MS Access only in Option II?", "No — database is in both options"),
        ),
    ],
    mcqs=[
        mcq("Every C program must contain:", ["start()", "getch()", "main()", "printf()"], "c"),
        mcq("Dennis Ritchie founded:", ["C", "BASIC", "JAVA", "PASCAL"], "a"),
        mcq("In MS Access a row is also called a:", ["Field", "Column", "Record", "Query"], "c"),
    ],
))

add(lec(
    id="xii-01",
    grade="XII",
    unit="C1",
    unit_title="Programming using C",
    title="C language, structure of a program and Turbo C IDE",
    option="Option I",
    golden=True,
    slos=[
        "Write the basic structure of a C program",
        "Explain #include and #define with examples",
        "Use Turbo C shortcuts and know compiler vs editor vs debugger",
        "List reserved words and rules of identifiers",
    ],
    body=[
        p("C was designed by Dennis Ritchie at Bell Labs (1972) to write UNIX. It is a middle-level, compiled, case-sensitive language. BIEK still expects Turbo C style in many colleges: #include <stdio.h>, #include <conio.h>, void main(), clrscr(), getch()."),
        code(r'''
#include <stdio.h>
#include <conio.h>
#define PI 3.14
void main()
{
    clrscr();
    printf("Board of Intermediate Education Karachi\n");
    getch();
}
'''),
        table(
            ["Part", "Job"],
            [
                ["#include <stdio.h>", "Preprocessor: copies standard I/O functions (printf, scanf)"],
                ["#include <conio.h>", "Turbo C console: clrscr, getch"],
                ["#define PI 3.14", "Manifest constant — name replaced before compile"],
                ["void main()", "Execution starts here (ISO C prefers int main(void))"],
                ["Declarations", "Variables before use in C89 / Turbo C"],
                ["Statements", "End with semicolon"],
                ["getch()", "Wait for a key so the output screen stays"],
            ],
        ),
        h("Identifiers and keywords"),
        ul(
            "Letters, digits, underscore; cannot start with a digit; no spaces or special symbols; cannot be a keyword.",
            "Valid: std_marks, NUMBER5, Number_5. Invalid: 5number, 1st number, void, int, float.",
            "Keywords (reserved): auto, break, case, char, const, continue, default, do, double, else, enum, extern, float, for, goto, if, int, long, register, return, short, signed, sizeof, static, struct, switch, typedef, union, unsigned, void, volatile, while.",
        ),
        defn("Escape sequence", r"A backslash code inside a string: \n new line, \t tab, \\ backslash, \a beep, \" quote, \0 string terminator."),
        exam("2025/26 shorts: structure of C; #include or #define; reserved words; valid/invalid identifiers; why C is case sensitive; IDE shortcuts."),
        urdu(
            "C پروگرام #include سے شروع ہوتا ہے، main() سے چلتا ہے۔ #define نام کو قدر سے بدل دیتا ہے۔ Reserved words (int, void, for) نام نہیں بن سکتے۔",
        ),
        check(
            ("Who developed C?", "Dennis Ritchie"),
            (r"What does \n do?", "Moves the cursor to a new line"),
        ),
    ],
    mcqs=[
        mcq("C programs are converted to machine language by a:", ["Editor", "Assembler", "Compiler", "Debugger"], "c"),
        mcq("This is not a valid identifier:", ["Number", "5number", "NUMBER5", "Number_5"], "b"),
        mcq("Comments in C are enclosed in:", ["/* … */", "/* … /*", "*/ … /*", "** **"], "a"),
        mcq("Names of variables and functions are called:", ["header files", "identifiers", "loops", "structures"], "b"),
    ],
    short=[
        "Write the basic structure of a C program.",
        "Define #include or #define with two examples.",
        "What is an IDE? Write a few shortcut keys.",
        "Identify valid/invalid: void, std_marks, 1st number.",
        "Why is C called case-sensitive? Define three reserved words.",
    ],
    short_ans=[
        "Preprocessor directives, global declarations, main(), local declarations, statements, closing brace. Show a 8-line skeleton as above.",
        "#include <stdio.h> brings printf. #include <math.h> brings sqrt. #define PI 3.14 and #define MAX 100 create constants.",
        "IDE = editor+compiler+debugger. Turbo C: F2 save, F9 compile, Ctrl+F9 run, Alt+F5 user screen, F8 step.",
        "void invalid (keyword). std_marks valid. 1st number invalid (digit start + space).",
        "TOTAL and total are different. Keywords: int, return, while.",
    ],
    long=["Explain the structure of a C program with a labelled example. Discuss tokens: keywords, identifiers, constants, operators."],
))

add(lec(
    id="xii-02",
    grade="XII",
    unit="C2",
    unit_title="Programming using C",
    title="Data types, variables, constants and input/output",
    option="Option I",
    golden=True,
    slos=[
        "List C data types and format specifiers",
        "Use printf, scanf, getchar, getch, puts, gets (exam style)",
        "Convert algebraic expressions into C",
    ],
    body=[
        table(
            ["Type", "Typical size (Turbo C 16-bit)", "Specifier", "Example"],
            [
                ["char", "1 byte", "%c", "grade = 'A'"],
                ["int", "2 bytes", "%d", "n = 25"],
                ["float", "4 bytes", "%f", "avg = 72.5"],
                ["double", "8 bytes", "%lf", "pi = 3.14159"],
                ["long", "4 bytes", "%ld", "pop = 16000000L"],
            ],
        ),
        p("Constants: 25 integer, 3.14 float, 'A' character, \"BIEK\" string. Variables must be declared before use: int roll; float marks;"),
        code(r'''
int a, b, sum;
printf("Enter two numbers: ");
scanf("%d%d", &a, &b);   /* & is the address operator */
sum = a + b;
printf("Sum = %d\n", sum);
'''),
        table(
            ["Function", "Use"],
            [
                ["printf", "Formatted output to screen"],
                ["scanf", "Formatted input; needs & for scalars"],
                ["getchar", "Read one character (waits for Enter)"],
                ["getch", "Read one character without echo (conio.h)"],
                ["gets / puts", "String line I/O (unsafe in modern C, still in old papers)"],
            ],
        ),
        h("Algebra → C (every year)"),
        table(
            ["Mathematics", "C expression"],
            [
                ["A = ½ × base × height", "A = 0.5 * base * height;"],
                ["x = 3ab³ + 3a²b", "x = 3*a*b*b*b + 3*a*a*b;"],
                ["d = |b² − 4ac|", "d = fabs(b*b - 4*a*c);  /* math.h */"],
                ["A = πr²", "A = 3.14 * r * r;"],
                ["(a+b)² / ab", "((a+b)*(a+b))/(a*b)"],
                ["y = (a+b)^n", "y = pow(a+b, n);"],
            ],
        ),
        example(
            "If a=2, b=5, c=10:",
            "200*((a*10)+c) wait — follow the paper’s parentheses exactly.",
            "a*b*10/c+a+c = 2*5*10/10+2+10 = 100/10+2+10 = 10+2+10 = 22  (integer division if all int).",
            "a-(c/b)/2+100 = 2-(10/5)/2+100 = 2-2/2+100 = 2-1+100 = 101 with int division of 10/5 first.",
        ),
        warn("scanf(\"%d\", &n) — forgetting & is the #1 runtime bug. % with float is undefined; % is for integers only."),
        urdu(
            "int عدد صحیح، float اعشاری، char ایک حرف، %d %f %c فارمیٹ۔ scanf میں & پتہ دیتا ہے۔",
            "ریاضی کو C میں * / اور pow() سے لکھیں۔ ½ کو 0.5* بنائیں۔",
        ),
        check(
            ("Format specifier for int?", "%d"),
            ("Why & in scanf?", "Pass the address so the value can be stored in the variable"),
        ),
    ],
    mcqs=[
        mcq("% operator is only used with:", ["float", "int", "double", "string"], "b"),
        mcq("The address operator is:", ["*", "&", "%", "#"], "b"),
    ],
    short=[
        "How does scanf() differ from getchar()?",
        "What is the address operator? Explain with example.",
        "Convert A = ½ base·height and A = πr² into C.",
        "Define increment and decrement operators.",
    ],
    short_ans=[
        "scanf reads formatted data (numbers, strings) using specifiers; getchar reads a single character from the keyboard buffer.",
        "& gives the memory address. int x=5; printf(\"%u\", &x); prints the address of x. scanf(\"%d\", &x) stores input at that address.",
        "A=0.5*base*height;  A=3.14*r*r; (or PI*r*r).",
        "++ adds 1, -- subtracts 1. Pre (++k) changes then uses; post (k++) uses then changes.",
    ],
    long=["What are different types of operators in C? Explain with examples. Also discuss printf and scanf."],
))

add(lec(
    id="xii-03",
    grade="XII",
    unit="C3",
    unit_title="Programming using C",
    title="Operators, precedence and expressions",
    option="Option I",
    golden=True,
    slos=[
        "Classify arithmetic, relational, logical, assignment, increment, conditional, bitwise operators",
        "Apply precedence: () then ++/-- then * / % then + - ",
        "Trace small programs with x++ vs ++x",
    ],
    body=[
        table(
            ["Class", "Operators", "Result"],
            [
                ["Arithmetic", "+ - * / %", "% remainder, integers only"],
                ["Relational", "> < >= <= == !=", "1 (true) or 0 (false)"],
                ["Logical", "&& || !", "compound conditions"],
                ["Assignment", "= += -= *= /= %=", "x += 2 means x = x+2"],
                ["Increment", "++ --", "pre or post"],
                ["Conditional", "? :", "x = (a>b)? a : b;"],
                ["Bitwise", "& | ^ ~ << >>", "bit level (rare in Paper II but listed in books)"],
            ],
        ),
        learn(
            "Precedence (high → low): ()  ++ --  * / %  + -  relational  logical  assignment. Same-level * / % go left to right.",
            "Integer division: 5/2 is 2, not 2.5. Use 5/2.0 or a float variable.",
        ),
        example(
            "If x = 1:",
            r'printf("x=%d\n", x);     → x=1',
            r'printf("x=%d\n", x + x); → x=2',
            r'printf("x=%d\n", x);     → x=1   (x was never assigned a new value)',
            "Post-increment example: k++ is post; ++k is pre. MCQ: k++ is post increment.",
        ),
        code(r'''
int a = 5, b = 2, c;
c = a / b;          /* 2 */
c = a % b;          /* 1 */
c = (a > b) && (b > 0);  /* 1 */
c = (a > b) ? a : b;     /* 5 */
'''),
        exam("Long 2026 Q4: types of operators in C. Make a table with one example each. Trace questions: never change a variable unless you see =, ++ or --."),
        urdu(
            "آپریٹر حساب (+ - * / %)، موازنہ (== != >)، منطق (&& || !) اور ++/-- ہیں۔ فیصد % صرف int پر۔ 5/2 کا جواب 2 ہے۔",
        ),
        check(
            ("Value of 17 % 5?", "2"),
            ("Is k++ pre or post increment?", "Post"),
        ),
    ],
    mcqs=[
        mcq("An example of post increment is:", ["k++", "++k", "k+=", "k=+"], "a"),
        mcq("Highest precedence among + - / % is:", ["+", "-", "/", "% — actually / and % are equal and higher than + -"], "c"),
        mcq("== is a:", ["assignment", "relational operator", "loop", "header"], "b"),
    ],
    short=["Define increment and decrement with examples.", "If x=1, output of three printf lines using x, x+x, x.", "Write C expressions for (x²−y²)(x+y)/(a+b)."],
    short_ans=[
        "++k pre-increment, k++ post. -- same for decrement. int k=5; printf(\"%d\", k++); prints 5 then k becomes 6.",
        "1 then 2 then 1.",
        "((x*x - y*y)*(x+y))/(a+b)",
    ],
    long=["What are different types of operators used in a C program? Explain with examples and precedence."],
))

add(lec(
    id="xii-04",
    grade="XII",
    unit="C4",
    unit_title="Programming using C",
    title="Selection: if, if-else, nested if and switch",
    option="Option I",
    golden=True,
    slos=[
        "Write if, if-else, else-if ladder and nested if",
        "Write switch-case with break and default",
        "Draw the switch logical diagram",
        "Program: greater of two, pass/fail, leap year",
    ],
    body=[
        code(r'''
if (marks >= 40)
    printf("Pass");
else
    printf("Fail");
'''),
        code(r'''
if (n > 0) printf("Positive");
else if (n < 0) printf("Negative");
else printf("Zero");
'''),
        h("switch (board long question)"),
        code(r'''
int ch;
printf("1.Add  2.Sub  3.Mul\n");
scanf("%d", &ch);
switch (ch) {
    case 1: printf("Add"); break;
    case 2: printf("Sub"); break;
    case 3: printf("Mul"); break;
    default: printf("Invalid");
}
'''),
        learn(
            "switch works on int or char (not float). Each case should end with break, otherwise execution falls through. default is optional but expected in board answers.",
        ),
        flow("Evaluate expression", "Match case", "Execute statements", "break → leave switch"),
        example(
            "Greater of two using a function (2026 Q2 xii):",
        ),
        code(r'''
int greater(int x, int y) {
    if (x > y) return x;
    else return y;
}
void main() {
    int a, b;
    scanf("%d%d", &a, &b);
    printf("Greater = %d", greater(a, b));
}
'''),
        exam("2026 Section C Q3: Define switch with logical diagram. Draw a diamond or a multi-way box: expression, case 1, case 2, default."),
        urdu(
            "if شرط سچی ہو تو بلاک چلتا ہے۔ switch ایک متغیر کی کئی قیمتوں پر چلتا ہے، ہر case کے بعد break لکھیں۔",
        ),
        check(
            ("Can switch test a float?", "No"),
            ("What if you omit break?", "Fall-through: the next case also runs"),
        ),
    ],
    mcqs=[
        mcq("switch is a:", ["loop", "selection / decision structure", "function", "header"], "b"),
        mcq("default in switch runs when:", ["always", "no case matches", "every case", "at compile time"], "b"),
    ],
    short=["Define switch with a small example.", "Write a program that prints the greater of two integers using a function.", "Differentiate if-else and switch."],
    short_ans=[
        "switch(expression) { case c1: … break; default: … } selects one case by matching integers/chars.",
        "Full greater() program as in the lecture.",
        "if-else handles ranges and floats; switch is multi-way on discrete int/char values and is cleaner for menus.",
    ],
    long=["Define switch statement with a logical diagram and a complete C program (menu or grade)."],
))

add(lec(
    id="xii-05",
    grade="XII",
    unit="C5",
    unit_title="Programming using C",
    title="Loops: for, while, do-while, break, continue, patterns",
    option="Option I",
    golden=True,
    slos=[
        "Write for, while and do-while and compare them",
        "Use break and continue",
        "Print multiplication tables, factorial, nested-loop patterns",
    ],
    body=[
        table(
            ["", "for", "while", "do-while"],
            [
                ["Test", "At the top", "At the top", "At the bottom — runs at least once"],
                ["Best when", "Count known", "Condition, count unknown", "Menus, “repeat until”"],
                ["Header", "for(s;c;u)", "while(c)", "do { } while(c);"],
            ],
        ),
        code(r'''
/* table of n */
int n, i;
scanf("%d", &n);
for (i = 1; i <= 10; i++)
    printf("%d x %d = %d\n", n, i, n * i);
'''),
        code(r'''
/* factorial : 4! = 24 */
int n, i; long f = 1;
scanf("%d", &n);
for (i = 1; i <= n; i++)
    f = f * i;
printf("%ld", f);
'''),
        h("break vs continue"),
        ul(
            "break: leave the loop immediately.",
            "continue: skip the rest of this iteration and go to the next test / increment.",
        ),
        code(r'''
int i;
for (i = 1; i <= 5; i++) {
    if (i == 3) continue;
    printf("%d ", i);   /* 1 2 4 5 */
}
'''),
        h("Nested loops — 2026 pattern"),
        code(r'''
int i, j;
for (i = 1; i <= 5; i++) {
    for (j = 1; j <= i; j++)
        printf("%d", j);
    printf("\n");
}
/* 1
   12
   123
   1234
   12345 */
'''),
        p("Number / Square: for(i=1;i<=5;i++) printf(\"%d %d\\n\", i, i*i);"),
        exam("Programs to memorise: table, factorial, even 0–50, sum of n numbers, reverse digits, prime check, Fibonacci, patterns."),
        warn("do-while ends with a semicolon after while(condition); forgetting it is a syntax error. Infinite loop: for(;;;) or while(1)."),
        urdu(
            "for گنتی معلوم ہو تو، while شرط پر، do-while کم از کم ایک بار۔ break لوپ توڑتا ہے، continue اس چکر کو چھوڑتا ہے۔",
            "ٹیبل، فیکٹوریل اور پیٹرن ہر سال آتے ہیں — زبانی لکھ کر یاد کریں۔",
        ),
        check(
            ("4! = ?", "24"),
            ("Does do-while always run once?", "Yes"),
        ),
    ],
    mcqs=[
        mcq("for() is used when we need:", ["Sequential structure", "Selection structure", "Iteration structure", "Top down structure"], "c"),
        mcq("This statement skips the rest of the loop body and continues from the top:", ["break", "resume", "continue", "skip"], "c"),
    ],
    short=[
        "Write a program that prints the multiplication table of an inputted number.",
        "Write a program that prints factorial of n (hint 4!=24).",
        "Differentiate while and do-while.",
        "Define break and continue with an example.",
        "Write a nested-loop program for the triangle 1 / 12 / 123 / …",
    ],
    short_ans=[
        "for i=1 to 10 print n x i = n*i.",
        "f=1; for i=1..n f*=i; print f.",
        "while tests first (may run 0 times). do-while tests after the body (at least once).",
        "break exits; continue jumps to next iteration. Show a 4-line for-loop example.",
        "Outer i=1..5, inner j=1..i print j, then newline.",
    ],
    long=["What is a loop? Explain for, while and do-while with programs. Discuss nested loops."],
))

add(lec(
    id="xii-06",
    grade="XII",
    unit="C6",
    unit_title="Programming using C",
    title="Arrays and strings",
    option="Option I",
    golden=True,
    slos=[
        "Declare, initialise and traverse 1-D and 2-D arrays",
        "Explain string terminator '\\0' and strlen, strcpy, strcat, strcmp",
        "Predict output of num[3] style MCQs",
    ],
    body=[
        defn("Array", "A collection of elements of the same data type stored in contiguous memory, accessed by index starting at 0."),
        code(r'''
int num[] = {3, 5, 7, 10, 20};
printf("%d", num[3]);   /* 10  — index 3 is the fourth element */
'''),
        code(r'''
int a[5], i, sum = 0;
for (i = 0; i < 5; i++) {
    scanf("%d", &a[i]);
    sum += a[i];
}
printf("Average = %.2f", sum / 5.0);
'''),
        h("Two-dimensional array"),
        code(r'''
int m[3][3], i, j;
for (i = 0; i < 3; i++)
    for (j = 0; j < 3; j++)
        scanf("%d", &m[i][j]);
'''),
        h("Strings"),
        p("A string is a char array ending with '\\0'. char name[20] = \"Ali\";  /* 'A','l','i','\\0' */"),
        table(
            ["Function", "Header", "Use"],
            [
                ["strlen(s)", "string.h", "length without '\\0'"],
                ["strcpy(d,s)", "string.h", "copy s into d"],
                ["strcat(d,s)", "string.h", "join s onto d"],
                ["strcmp(a,b)", "string.h", "0 if equal, <0 or >0 if not"],
            ],
        ),
        code(r'''
char s[30];
int i, n;
gets(s);               /* exam style */
n = strlen(s);
for (i = n - 1; i >= 0; i--)
    printf("%c", s[i]);  /* reverse name */
'''),
        exam("2025: What is an array? Declare and initialise. Output of num[3] with {3,5,7,10,20} is 10 — not 7. Students forget index 0."),
        warn("scanf(\"%s\", name) — no & for arrays because the name is already an address. Overrunning the array size crashes the program."),
        urdu(
            "Array ایک ہی قسم کی کئی قیمتیں، انڈیکس 0 سے۔ num[3] چوتھا عنصر ہے۔",
            "سٹرنگ حروف کی صف ہے جو \\0 پر ختم ہوتی ہے۔ strlen لمبائی، strcpy نقل، strcat جوڑ، strcmp موازنہ۔",
        ),
        check(
            ("Index of the first element?", "0"),
            ("num[]={3,5,7,10,20}; num[3]?", "10"),
        ),
    ],
    mcqs=[
        mcq("Array index in C starts from:", ["1", "0", "-1", "2"], "b"),
        mcq("A string in C ends with:", ["\\n", "\\0", "\\t", "NULL pointer only"], "b"),
    ],
    short=[
        "What is an array? Declare and initialise an integer array.",
        "int num[]={3,5,7,10,20}; what does printf(\"%d\", num[3]) print?",
        "Write a program to reverse an inputted name using strlen().",
        "Name four string functions.",
    ],
    short_ans=[
        "Same-type contiguous list. int a[5]={1,2,3,4,5}; or int a[]={10,20};",
        "10.",
        "Read string, loop from strlen-1 down to 0 printing characters.",
        "strlen, strcpy, strcat, strcmp (plus strncpy etc. if space).",
    ],
    long=["Explain array and its types with examples. Write a program to add two 3×3 matrices."],
))

add(lec(
    id="xii-07",
    grade="XII",
    unit="C7",
    unit_title="Programming using C",
    title="Functions: prototype, call, return, types",
    option="Option I",
    golden=True,
    slos=[
        "State advantages and characteristics of functions",
        "Differentiate built-in and user-defined; call by value vs reference",
        "Write programs that use functions (greater, factorial, area)",
    ],
    body=[
        defn("Function", "A named, reusable block that performs a task. main() is itself a function. Advantages: modularity, reuse, easier testing, team work."),
        flow("Prototype (declaration)", "Definition (body)", "Call (use)"),
        code(r'''
int square(int n);          /* prototype */
void main() {
    printf("%d", square(5));  /* call — actual parameter 5 */
}
int square(int n) {           /* definition — n is formal parameter */
    return n * n;
}
'''),
        table(
            ["Idea", "Meaning"],
            [
                ["Built-in", "printf, scanf, sqrt, strlen — already in libraries"],
                ["User-defined", "You write them"],
                ["Return type", "void if nothing is returned"],
                ["Formal parameters", "In the definition header"],
                ["Actual parameters", "In the call"],
                ["Call by value", "A copy is passed; original safe"],
                ["Call by reference", "Address (&) / pointer; function can change the original"],
                ["Local vs global", "Local inside block; global outside functions"],
                ["Recursion", "Function calls itself (factorial, Fibonacci)"],
            ],
        ),
        exam("2026 long Q5: main characteristics of a function with example. List: name, return type, parameters, independent compilation, reuse, call by value/reference."),
        urdu(
            "فنکشن نام والا بلاک ہے جو بار بار کام کرتا ہے۔ Prototype اعلان، تعریف جسم، کال استعمال۔ return قدر بھیجتا ہے۔",
        ),
        check(
            ("Does main have to exist?", "Yes — it is the entry point"),
            ("sqrt comes from which header?", "math.h"),
        ),
    ],
    mcqs=[
        mcq("A subprogram that returns a value is a:", ["function", "report", "macro only", "file"], "a"),
        mcq("Passing a copy of a variable is:", ["pass by value", "pass by address", "pass by reference", "pass by pointer"], "a"),
    ],
    short=["Write any one program using a function to print the greater of two numbers.", "Differentiate formal and actual parameters.", "What are built-in functions? Give three."],
    short_ans=[
        "int greater(int x,int y){ return (x>y)?x:y; } call from main after scanf.",
        "Formal: names in the definition. Actual: values in the call. They correspond in order and type.",
        "Library functions: printf, scanf, getchar, strlen, sqrt.",
    ],
    long=["What are the main characteristics of a function? Describe with an example program."],
))

add(lec(
    id="xii-08",
    grade="XII",
    unit="2",
    unit_title="Pointers (Sindh XII + C paper)",
    title="Pointers and the address operator",
    option="Option I / Sindh Unit 2",
    golden=True,
    slos=[
        "Explain & and * ",
        "Declare and initialise a pointer",
        "Write a program that prints address and value",
        "Pass addresses to a function to double two numbers",
    ],
    body=[
        defn("Pointer", "A variable that stores the memory address of another variable. Declared with * . The address operator & gives an address; the dereference operator * accesses the value at that address."),
        code(r'''
int x = 10;
int *p;      /* p is a pointer to int */
p = &x;      /* p holds the address of x */
printf("Value = %d\n", *p);   /* 10 */
printf("Address = %u\n", p);
'''),
        code(r'''
void double_them(int *a, int *b) {
    *a = *a * 2;
    *b = *b * 2;
}
void main() {
    int x = 4, y = 5;
    double_them(&x, &y);
    printf("%d %d", x, y);   /* 8 10 */
}
'''),
        exam("2025 Paper II: What is a pointer in C? How is it initialised? What is the address operator?"),
        warn("*p = &x is wrong for the first assignment if p is int*. Use p = &x; then read *p. Mixing them loses marks."),
        urdu(
            "پوائنٹر وہ متغیر ہے جو دوسرے متغیر کا پتہ رکھتا ہے۔ & پتہ دیتا ہے، * اس پتے پر موجود قدر دیتا ہے۔",
        ),
        check(
            ("If int x=5; int *p=&x; what is *p?", "5"),
            ("Symbol for address operator?", "&"),
        ),
    ],
    mcqs=[
        mcq("A pointer stores a:", ["value only", "memory address", "file name", "keyword"], "b"),
        mcq("&x means:", ["value of x", "address of x", "pointer declaration", "multiply x"], "b"),
    ],
    short=["What is a pointer in C? How is it initialised?", "Explain the address operator with an example.", "Write a program to display address and value of a variable using a pointer."],
    short_ans=[
        "A variable that holds an address. int *p; p = &x; or int *p = &x;",
        "&x is the address of x. scanf uses it; pointers store it.",
        "Declare x and p=&x; printf value *p and address p.",
    ],
    long=["Explain pointers with a diagram of x and p. Write a function that receives two addresses and doubles both values."],
))

add(lec(
    id="xii-09",
    grade="XII",
    unit="3–4",
    unit_title="OOP using C++ and file handling",
    title="OOP in C++: class, object, constructor, inheritance, polymorphism",
    option="Sindh Units 3–4",
    golden=True,
    slos=[
        "State encapsulation, inheritance, polymorphism",
        "Write a simple class Student with constructor",
        "Explain public, private, protected",
        "Open text/binary files for read, write, append",
    ],
    body=[
        svg(class_object(), "A class is a blueprint; objects are instances with their own data."),
        ul(
            "Encapsulation: wrap data + functions; hide data with private.",
            "Inheritance: derived class reuses base class (reusability).",
            "Polymorphism: one name, many forms — overload (same name, different parameters) and override (same signature in derived class).",
        ),
        code(r'''
#include <iostream>
using namespace std;
class Student {
    int age; float percentage;          // private by default
public:
    Student() { age = 0; percentage = 0; }           // default constructor
    Student(int a, float p) { age = a; percentage = p; }  // overloaded
    void show() { cout << age << " " << percentage; }
    ~Student() { }   // destructor
};
int main() {
    Student s1(17, 82.5);
    s1.show();
}
'''),
        p("Access specifiers: private (only inside class), public (everywhere), protected (class + derived). Constructor has the class name, no return type, called automatically. Destructor ~ClassName() at end of life."),
        h3("Inheritance sketch"),
        code(r'''
class Base { public: int x; };
class Drive : public Base { public: int y; };
// Drive object can use x and y
'''),
        h("File handling"),
        p("Text files store characters; binary files store raw bytes (objects). Modes: ios::in read, ios::out write (truncate), ios::app append. BOF beginning, EOF end. Streams: get/put (char), getline (string), read/write (binary)."),
        code(r'''
#include <fstream>
ofstream out("data.txt");
out << "Ali 80\n";
out.close();
ifstream in("data.txt");
string line; getline(in, line);
'''),
        exam("Sindh lab: class STUDENT with AGE and PERCENTAGE; TIME class with constructors; inherit DRIVE from BASE; write/read text file; write/read student object as binary."),
        urdu(
            "کلاس خاکہ ہے، آبجیکٹ اس کی کاپی۔ Encapsulation ڈیٹا چھپاتا ہے، Inheritance وراثت، Polymorphism ایک نام کئی کام۔ Constructor آبجیکٹ بنتے وقت چلتا ہے۔",
            "فائل ہینڈلنگ: ٹیکسٹ اور بائنری، read/write/append۔",
        ),
        check(
            ("Does a constructor return a value?", "No — not even void"),
            ("ios::app means?", "Append to the file without erasing old data"),
        ),
    ],
    mcqs=[
        mcq("Wrapping data and functions together is:", ["inheritance", "encapsulation", "compilation", "paging"], "b"),
        mcq("A constructor has:", ["the class name and no return type", "any name", "return type int", "a destructor symbol"], "a"),
    ],
    short=["Explain class and object.", "Differentiate constructor and destructor.", "Differentiate text and binary files."],
    short_ans=[
        "Class: user-defined type with data members and member functions. Object: variable of that type.",
        "Constructor initialises (same name, auto-called). Destructor cleans up (~Name), no arguments.",
        "Text: human-readable characters. Binary: exact memory image, efficient for objects.",
    ],
    long=["Explain OOP principles with a C++ class that uses a constructor. Discuss inheritance and polymorphism briefly."],
))

add(lec(
    id="xii-10",
    grade="XII",
    unit="VB1",
    unit_title="Programming using Visual Basic",
    title="Visual Basic IDE, forms and ActiveX controls",
    option="Option II",
    golden=True,
    slos=[
        "Describe the VB IDE and a form",
        "List basic ActiveX controls and important properties",
        "Set Cancel button, use labels, text boxes, command buttons, combo, option, check",
    ],
    body=[
        defn("Visual Basic", "An event-driven programming language and IDE from Microsoft. You draw controls on a Form; code runs when events occur (Click, Load, Change)."),
        table(
            ["Control", "Use", "Key properties"],
            [
                ["Form", "Window", "Caption, BackColor, BorderStyle"],
                ["Label", "Display text the user does not type", "Caption, Font, AutoSize"],
                ["TextBox", "Input / output of text", "Text, MaxLength, PasswordChar, MultiLine"],
                ["CommandButton", "Click to run code", "Caption, Enabled, Cancel, Default"],
                ["CheckBox", "Yes/No independent", "Value 0/1/2"],
                ["OptionButton", "One choice from a group", "Value True/False"],
                ["ComboBox / ListBox", "Pick from a list", "List, Text, AddItem"],
                ["Image / PictureBox", "Pictures", "Picture, Stretch"],
            ],
        ),
        p("Cancel button property belongs to CommandButton (MCQ). Default step in For…Next is 1. DIM declares a variable. Variant can hold any type: Dim x As Variant or Dim x  (undeclared = Variant if no Option Explicit — board still asks “how can a variable be defined as variant”)."),
        code(r'''
Private Sub cmdAdd_Click()
    lblSum.Caption = Val(txtA.Text) + Val(txtB.Text)
End Sub
'''),
        exam("2026 shorts: ComboBox properties; TextBox properties; basic ActiveX controls; Cancel button object; DIM; Option Button vs CheckBox."),
        urdu(
            "Visual Basic میں فارم پر بٹن، ٹیکسٹ باکس، لیبل رکھتے ہیں۔ کلک ایونٹ پر کوڈ چلتا ہے۔ Option Button ایک انتخاب، CheckBox ہاں/نہیں۔",
        ),
        check(
            ("Default For step?", "1"),
            ("Which control is for a single choice in a group?", "Option Button (radio)"),
        ),
    ],
    mcqs=[
        mcq("The Cancel button property belongs to:", ["Form", "Label", "Button", "Textbox"], "c"),
        mcq("Default Step in For…Next is:", ["2", "0", "-1", "1"], "d"),
        mcq("DIM declares a:", ["variable", "constant only", "keyword", "function only"], "a"),
        mcq("A control that selects a single choice from a group:", ["Check Box", "Option Button", "Caption Box", "List Box"], "b"),
    ],
    short=["What is a ComboBox? List properties.", "Write properties of a TextBox.", "What are basic ActiveX controls in VB?", "How can a variable be defined as Variant?"],
    short_ans=[
        "Drop-down list combining text box + list. Properties: List, ListIndex, Text, Style, AddItem, Sorted.",
        "Text, Font, MaxLength, PasswordChar, MultiLine, Locked, Alignment.",
        "Label, TextBox, CommandButton, CheckBox, OptionButton, ComboBox, ListBox, Frame, Timer, Image.",
        "Dim x As Variant  or  Dim x  (Variant is the default type).",
    ],
    long=["Explain commonly used VB controls with properties. Write a form program that adds two numbers."],
))

add(lec(
    id="xii-11",
    grade="XII",
    unit="VB2",
    unit_title="Programming using Visual Basic",
    title="VB language: operators, if, Select Case, loops, arrays, functions",
    option="Option II",
    golden=True,
    slos=[
        "Write If…Then and Select Case",
        "Write For…Next, Do While, Do Until",
        "Declare arrays and small functions",
        "Translate formulae into VB",
    ],
    body=[
        code(r'''
If marks >= 40 Then
    lblR.Caption = "Pass"
Else
    lblR.Caption = "Fail"
End If
'''),
        code(r'''
Select Case ch
    Case 1: lbl.Caption = "Add"
    Case 2: lbl.Caption = "Sub"
    Case Else: lbl.Caption = "Invalid"
End Select
'''),
        code(r'''
Dim i As Integer, s As Integer
s = 0
For i = 0 To 50 Step 2
    s = s + i          ' even numbers 0-50
Next i
'''),
        code(r'''
' sum and average of 10 inputted numbers
Dim i As Integer, n As Double, t As Double
t = 0
For i = 1 To 10
    n = Val(InputBox("Number " & i))
    t = t + n
Next i
MsgBox "Sum=" & t & "  Avg=" & t / 10
'''),
        table(
            ["Maths", "VB"],
            [
                ["x = 3ab² / c", "x = 3 * a * b ^ 2 / c"],
                ["Y = (4/3)πr³", "Y = (4 / 3) * 3.14 * r ^ 3"],
                ["Y = (a+b)^n", "Y = (a + b) ^ n"],
                ["a = ½ base·height", "a = 0.5 * base * height"],
            ],
        ),
        p("Built-in functions: Val, Str, Left, Right, Mid, Len, UCase, LCase, Int, Rnd, Date, Sqr, Abs, Format. User-defined: Function Area(r As Double) As Double : Area = 3.14 * r * r : End Function. Errors: syntax, run-time, logical. On Error GoTo handler."),
        exam("2026 programs: even 0–50; sum and average of ten numbers. Long: arrays; loops; built-in function with a program."),
        urdu(
            "VB میں If...Then، Select Case، For...Next اور Do While لوپ ہیں۔ ^ طاقت ہے۔ Val ٹیکسٹ کو عدد بناتا ہے۔",
        ),
        check(
            ("Even numbers 0–50: Step?", "2, start 0"),
            ("Val(\"12a\") in VB6?", "12  (stops at first non-numeric, classic VB)"),
        ),
    ],
    mcqs=[
        mcq("Comparison operators are also called:", ["Comparators", "Comparables", "Relations", "Relational"], "d"),
        mcq("The last statement in a Function is often:", ["Footer", "Header", "End Function / Return value assignment", "Call"], "c"),
        mcq("A function returns a:", ["form", "value", "only a MsgBox", "table"], "b"),
    ],
    short=[
        "Write the structure of Select Case.",
        "Write a VB program to generate even numbers 0–50.",
        "Write a VB program to calculate sum and average of ten numbers.",
        "Convert Y = (4/3)πr³ to VB.",
        "What is an error? Define its types.",
    ],
    short_ans=[
        "Select Case expr : Case v1: … : Case Else: … : End Select",
        "For i = 0 To 50 Step 2 : Print i : Next",
        "Loop 10 InputBox, add to total, divide by 10.",
        "Y = (4 / 3) * 3.14 * r ^ 3",
        "Mistake in a program. Syntax (grammar), run-time (divide by zero), logical (wrong formula, runs but answer wrong).",
    ],
    long=["Explain arrays in VB with types and an example. OR Explain loops with two types and programs. OR Built-in functions with a program."],
))

add(lec(
    id="xii-12",
    grade="XII",
    unit="5",
    unit_title="Database fundamentals",
    title="DBMS, models, ER diagrams, keys and normalisation",
    option="Both options",
    golden=True,
    slos=[
        "Differentiate file system and DBMS",
        "Draw hierarchical, network, relational, object models",
        "Define PK, FK, candidate, super key; 1NF 2NF 3NF",
        "Draw a simple ER diagram (library / student-book)",
    ],
    body=[
        defn("Database", "An organised collection of related data. DBMS is software that creates, manages and controls access to the database (MS Access, Oracle, MySQL)."),
        p("Advantages vs flat files: less redundancy, data integrity, sharing, security, backup, query language. Components: hardware, software, data, procedures, people, DML/DDL (data access language). Users: DBA, application programmer, end user."),
        table(
            ["Model", "Picture"],
            [
                ["Hierarchical", "Tree — one parent, many children (IMS)"],
                ["Network", "Graph — many-to-many with pointers (CODASYL)"],
                ["Relational", "Tables (relations) linked by keys — SQL works here"],
                ["Object / object-relational", "Objects with methods; ORDBMS"],
            ],
        ),
        svg(er_library(), "Entity Relationship: rectangles = entities, diamond = relationship, ovals = attributes (in full ER)."),
        table(
            ["Term", "Meaning"],
            [
                ["Table / relation", "A grid of rows and columns"],
                ["Record / tuple", "A row"],
                ["Field / attribute", "A column"],
                ["Primary key", "Unique identifier, not null"],
                ["Foreign key", "A field that matches the PK of another table"],
                ["Candidate key", "Any field(s) that could be PK"],
                ["Super key", "Any set that uniquely identifies, may have extras"],
                ["1NF", "Atomic cells, no repeating groups"],
                ["2NF", "1NF + non-key fields depend on whole PK"],
                ["3NF", "2NF + no transitive dependence on non-keys"],
            ],
        ),
        p("Relationships: 1:1, 1:M, M:M, M:1. Integrity: NOT NULL, PRIMARY KEY, FOREIGN KEY (referential). Three ANSI levels: internal/physical, conceptual/logical, external/view."),
        exam("Both options 2026: PK vs FK; table, query, report; DBMS components; data models long question; Access data types long question."),
        urdu(
            "ڈیٹا بیس منظم متعلقہ ڈیٹا ہے۔ DBMS سافٹ ویئر (Access) اسے سنبھالتا ہے۔ Primary Key یکتا، Foreign Key دوسری ٹیبل کا لنک۔",
            "Relational ماڈل ٹیبلز اور SQL۔ 1NF 2NF 3NF ڈیٹا دہرانے سے بچاتے ہیں۔",
        ),
        check(
            ("Row is also called?", "Record / tuple"),
            ("SQL works on which model?", "Relational"),
        ),
    ],
    mcqs=[
        mcq("A unique key in a table is the:", ["Primary key", "Foreign key", "Super key only", "Candidate only — PK is the chosen candidate"], "a"),
        mcq("The primary object in a database is the:", ["Table", "Query", "Report", "Form"], "a"),
        mcq("Tree-like database model:", ["Relational", "Hierarchical", "Network", "Object"], "b"),
        mcq("Columns in a database are:", ["Tuples", "Attributes", "Keys only", "Tables"], "b"),
        mcq("The model that allows SQL is:", ["Network", "Hierarchical", "Relational", "Flat"], "c"),
        mcq("DBMS advantage:", ["data depends on programs", "redundancy increases", "data is integrated and shared", "integrity decreases"], "c"),
    ],
    short=[
        "Differentiate primary key and foreign key.",
        "Define table, query, report.",
        "Name the major components of DBMS.",
        "Who is a DBA? Three responsibilities.",
        "Define one-to-many relationship.",
        "Write any four advantages of DBMS.",
        "Name four objects in MS Access.",
    ],
    short_ans=[
        "PK uniquely identifies a row in its own table. FK is a field pointing to a PK in another table to link records.",
        "Table stores data. Query asks questions / filters. Report is a printable layout of data.",
        "Hardware, software, data, procedures, users, query language.",
        "Database Administrator: security, backup, performance, user accounts, recovery.",
        "One parent row links to many child rows (one class, many students). Draw 1 — M.",
        "Less redundancy, integrity, sharing, security, standard SQL, backup.",
        "Tables, Queries, Forms, Reports (Macros, Modules).",
    ],
    long=["What is a data model? Explain types with diagrams. OR Explain ER modelling and normalisation up to 3NF with a library example."],
))

add(lec(
    id="xii-13",
    grade="XII",
    unit="5",
    unit_title="Database fundamentals",
    title="MS Access objects, data types and SQL",
    option="Both options",
    golden=True,
    slos=[
        "List Access objects and data types for a long answer",
        "Write CREATE, INSERT, UPDATE, DELETE, SELECT",
        "Plan a Library Management schema",
    ],
    body=[
        table(
            ["Object", "Purpose"],
            [
                ["Table", "Store data in fields/records; set PK"],
                ["Query", "Select, update, calculate, join tables"],
                ["Form", "On-screen data entry (like a VB form)"],
                ["Report", "Print marksheets, lists"],
                ["Macro / Module", "Automate / VBA"],
            ],
        ),
        h("MS Access data types (learn for Section C)"),
        table(
            ["Type", "Stores"],
            [
                ["Text / Short Text", "Names, up to 255 chars"],
                ["Memo / Long Text", "Remarks, long notes"],
                ["Number", "Byte, Integer, Long, Single, Double"],
                ["Date/Time", "Dates and clocks"],
                ["Currency", "Money, 4 decimal"],
                ["AutoNumber", "Automatic PK"],
                ["Yes/No", "Boolean"],
                ["OLE Object", "Pictures, files"],
                ["Hyperlink", "URLs"],
                ["Attachment / Lookup", "Newer Access extras"],
            ],
        ),
        code(r'''
CREATE TABLE Book (
  ISBN TEXT PRIMARY KEY,
  Title TEXT,
  Author TEXT,
  Price CURRENCY
);
INSERT INTO Book VALUES ('978-1', 'CS XI', 'STBB', 450);
SELECT Title, Author FROM Book WHERE Price > 400;
UPDATE Book SET Price = 500 WHERE ISBN = '978-1';
DELETE FROM Book WHERE ISBN = '978-1';
'''),
        p("SELECT is projection (columns) + WHERE is selection (rows). JOIN combines tables on keys. Equijoin: WHERE Book.AuthorID = Author.ID. Operators: AND OR NOT, = <> > < LIKE BETWEEN."),
        h("Planning a library database"),
        ol(
            "Purpose: issue and return books.",
            "Tables: STUDENT(Roll PK, Name, Class), BOOK(ISBN PK, Title, Author), ISSUE(IssueID PK, Roll FK, ISBN FK, IssueDate, ReturnDate).",
            "Unique fields: Roll, ISBN, IssueID.",
            "Relationships: Student 1—M Issue M—1 Book, all up to 3NF (no repeating books inside student).",
            "Refine: add Fine, status Issued/Returned.",
        ),
        exam("Practical 2026 Access: create Library_Management, PK, 5 records, query currently issued books. Theory: explain all Access data types."),
        urdu(
            "Access میں Table ڈیٹا، Query سوال، Form انٹری، Report پرنٹ۔ SQL: SELECT چننا، INSERT داخل، UPDATE بدل، DELETE مٹانا۔",
        ),
        check(
            ("Which object is for printing?", "Report"),
            ("AutoNumber is typically used as?", "Primary key"),
        ),
    ],
    mcqs=[
        mcq("MS Access object used to display and print data:", ["Report", "Table", "Form", "Macro"], "a"),
        mcq("This key uniquely identifies a record:", ["Super Key", "Foreign Key", "Conditional Key", "Primary Key"], "d"),
    ],
    short=["Write SELECT syntax with WHERE.", "Differentiate form and report.", "Write steps to design a library database."],
    short_ans=[
        "SELECT field1, field2 FROM table WHERE condition; example SELECT Title FROM Book WHERE Price>400;",
        "Form is interactive on screen; report is formatted for paper/PDF.",
        "Purpose, tables, fields, unique keys, relationships to 3NF, refine.",
    ],
    long=["Explain all the data types used in MS-Access. OR Explain SQL DML statements with examples."],
))

add(lec(
    id="xii-14",
    grade="XII",
    unit="1",
    unit_title="System Development Life Cycle",
    title="SDLC, stakeholders and phases",
    option="Sindh Unit 1",
    golden=True,
    slos=[
        "Define system and SDLC",
        "Name stakeholder roles",
        "Describe planning, analysis, design, coding, testing, deployment, maintenance",
    ],
    body=[
        defn("System", "A set of related components that work together toward a goal. SDLC is the planned process of building information software from idea to retirement."),
        table(
            ["Stakeholder", "Role"],
            [
                ["Project manager", "Plan, cost, schedule"],
                ["Business analyst", "Gather requirements"],
                ["System architect", "Overall design"],
                ["Developer", "Write code"],
                ["Tester", "Find bugs"],
                ["Operations", "Deploy on servers"],
                ["Production support", "Maintenance after go-live"],
            ],
        ),
        flow("Planning", "Requirement analysis", "Design", "Coding", "Testing", "Deployment", "Maintenance"),
        ul(
            "Planning: problem, feasibility (technical, economic, operational), schedule.",
            "Requirement engineering: functional (what it must do) vs non-functional (speed, security). SRS document.",
            "Design: architecture, algorithms, flowcharts, database schema, UI.",
            "Implementation: coding in C / VB / other.",
            "Testing: find bugs and errors; unit, integration, system, acceptance.",
            "Deployment & SLA: install, train, service-level agreement.",
            "Maintenance: fix, adapt, improve.",
        ),
        p("Models you may mention: Waterfall (linear, old board favourite) vs Agile (iterative sprints)."),
        urdu(
            "SDLC سافٹ ویئر بنانے کا منصوبہ بند چکر ہے: منصوبہ، ضرورت، ڈیزائن، کوڈ، ٹیسٹ، تنصیب، دیکھ بھال۔",
        ),
        check(
            ("SRS means?", "Software Requirements Specification"),
            ("Who gathers requirements?", "Business analyst"),
        ),
    ],
    mcqs=[
        mcq("SDLC is mainly about:", ["repairing printers", "developing software in stages", "only testing viruses", "drawing cables"], "b"),
        mcq("Converting design into programs is:", ["testing", "coding / implementation", "feasibility", "retirement"], "b"),
    ],
    short=["Define SDLC and list its phases.", "Differentiate functional and non-functional requirements.", "Who are the stakeholders of SDLC?"],
    short_ans=[
        "Life cycle of software: plan, analyse, design, code, test, deploy, maintain.",
        "Functional: features (print marksheet). Non-functional: quality (response in 2 seconds, password security).",
        "PM, analyst, architect, developers, testers, operations, support, plus the client/users.",
    ],
    long=["Explain the System Development Life Cycle with a diagram and the role of each stakeholder."],
))

add(lec(
    id="xii-15",
    grade="XII",
    unit="6–7",
    unit_title="Multimedia and wireless",
    title="Multimedia systems; wireless and mobile communication",
    option="Sindh Units 6–7",
    slos=[
        "Define multimedia components and file types",
        "Use layers, keyframes, export/share a short video (theory + lab idea)",
        "Compare Wi-Fi, Bluetooth, infrared, WiMAX, microwave",
        "Outline cellular network, 2G–5G, GEO/MEO/LEO, ad hoc / MANET",
    ],
    body=[
        defn("Multimedia", "The combination of text, graphics, animation, audio and video used to communicate. Advantages: richer teaching, advertising, games, training."),
        table(
            ["Component", "Typical files"],
            [
                ["Text", ".txt .doc .pdf"],
                ["Graphics", ".jpg .png .gif .bmp .svg"],
                ["Animation", ".gif .mp4"],
                ["Audio", ".mp3 .wav .aac"],
                ["Video", ".mp4 .avi .mkv"],
            ],
        ),
        p("Packages: web apps vs desktop (ProShow Gold, JetAudio, Shotcut, Canva, PowerPoint). Scene/canvas = work area; layers stack pictures/text; keyframes mark motion in animation. Lab: 2-minute video, export MP4, upload/share."),
        h("Wireless"),
        ul(
            "Wireless: no physical cable; uses electromagnetic waves. Mobile: communication while moving.",
            "Terms: frequency spectrum, radio signal, transceiver, access point, line of sight.",
        ),
        table(
            ["Short range", "Typical use"],
            [
                ["Wi-Fi", "LAN internet in college / home"],
                ["Bluetooth", "earbuds, file share, few metres"],
                ["Infrared", "TV remote, line of sight"],
                ["Microwave", "dishes, backhaul"],
                ["WiMAX", "city-wide wireless (MAN-like)"],
            ],
        ),
        p("Satellites: GEO ~36000 km (TV), MEO (GPS), LEO (phones, Starlink-style). Cellular: cell, BTS, BSC, MSC, frequency reuse. Generations: 2G GSM voice, 3G GPRS/data, 4G LTE fast data, 5G low latency. Ad hoc: no fixed AP; MANET is a mobile ad hoc network."),
        urdu(
            "ملٹی میڈیا متن، تصویر، آواز، ویڈیو، اینیمیشن کا ملاپ ہے۔ وائرلیس تار کے بغیر ریڈیو لہریں: وائی فائی، بلوٹوتھ، سیلولر 2G سے 5G۔",
        ),
        check(
            ("Bluetooth vs Wi-Fi range?", "Bluetooth shorter; Wi-Fi room/building"),
            ("4G technology name often asked?", "LTE"),
        ),
    ],
    mcqs=[
        mcq("MP3 is mainly a file of:", ["video", "audio", "database", "source code"], "b"),
        mcq("Wi-Fi is a:", ["wired LAN cable", "short-range wireless technology", "printer type", "CPU register"], "b"),
        mcq("GSM is associated with:", ["2G", "5G only", "fibre optics", "OSI layer 7 only"], "a"),
    ],
    short=["Define multimedia and its components.", "Differentiate Wi-Fi and Bluetooth.", "What is a cellular network? Name 2G to 5G.", "GEO vs LEO satellites."],
    short_ans=[
        "Combination of text, graphics, animation, audio, video. Used in education and ads.",
        "Wi-Fi: higher speed/range for internet. Bluetooth: very short range for accessories.",
        "Geographic area split into cells with BTS. 2G GSM, 3G, 4G LTE, 5G.",
        "GEO high and stationary over earth (TV). LEO low and fast (phones, imaging).",
    ],
    long=["Explain multimedia components and how you would make a 2-minute educational video. OR Explain wireless technologies and cellular generations."],
))

add(lec(
    id="xii-16",
    grade="XII",
    unit="R",
    unit_title="Revision",
    title="Paper II Option I mock (C + Access) with answers",
    option="Option I",
    golden=True,
    slos=["Sit a full Option I paper and check against keys"],
    body=[
        h("Section A key (15)"),
        p("1 main()  2 C (Ritchie)  3 Programmer  4 Compiler  5 5number invalid  6 % with int  7 k++ post  8 / and % highest among listed arithmetic  9 Primary key  10 continue  11 data integrated  12 Table  13 identifiers  14 Iteration  15 /* */"),
        h("Section B — practise these 10"),
        ol(
            "Skeleton of a C program.",
            "#include and #define examples.",
            "Program: table of n.",
            "break vs continue.",
            "Three reserved words.",
            "Address operator example.",
            "Factorial program.",
            "scanf vs getchar.",
            "PK vs FK.",
            "Evaluate integer expressions.",
            "DBMS components.",
            "greater() function program.",
            "Three maths→C conversions.",
            "Nested pattern 1 / 12 / 123… and number-square table.",
            "Table, query, report.",
        ),
        h("Section C — pick 3"),
        ol(
            "switch with diagram.",
            "Operators in C.",
            "Characteristics of functions + program.",
            "Data models in DBMS.",
            "MS Access data types.",
        ),
        example(
            "Scoring a C program on the board: correct headers (1), main (1), declarations (1), logic/loop (3), output (1), indentation/comments (1). Always write clrscr/getch if your college uses Turbo C, and box the output.",
        ),
        urdu(
            "آپشن I: C کے پروگرام کاغذ پر صحیح semicolon اور & کے ساتھ لکھیں۔ Access کے ڈیٹا ٹائپ زبانی یاد کریں۔",
        ),
    ],
    mcqs=[mcq("Option I mock: the required function in every C program is:", ["main()", "start()", "loop()", "file()"], "a")],
    long=["Write the factorial program and the switch-menu program from memory in 25 minutes."],
))

add(lec(
    id="xii-17",
    grade="XII",
    unit="R",
    unit_title="Revision",
    title="Paper II Option II mock (VB + Access) with answers",
    option="Option II",
    golden=True,
    slos=["Sit a full Option II paper and check against keys"],
    body=[
        h("Section A key (15)"),
        p("1 Command Button (Cancel)  2 Step default 1  3 Record  4 Report  5 Primary Key  6 Check Box is 0/1 (paper wording) / Option for exclusive — learn both  7 Relational operators  8 Pass by value  9 Return/End Function  10 Attributes  11 Hierarchical  12 Option Button  13 Function  14 Variable  15 Relational model"),
        h("Section B list from 2026"),
        ol(
            "Four advantages of DBMS.",
            "ComboBox + properties.",
            "Variant type.",
            "One-to-many + diagram.",
            "Four Access objects.",
            "Select Case structure.",
            "DBA responsibilities.",
            "Basic ActiveX controls.",
            "ADO MDI SQL DBA OLE full forms (any three).",
            "TextBox properties.",
            "Three VB formulae.",
            "Types of errors.",
            "Even numbers 0–50 program.",
            "Sum and average of ten numbers.",
            "PK vs FK.",
        ),
        h("Section C"),
        ol(
            "Arrays and types with examples.",
            "Loop — any two types with examples.",
            "Built-in function + program.",
            "All database models with diagrams.",
            "All MS Access data types.",
        ),
        example(
            "ADO = ActiveX Data Objects. MDI = Multiple Document Interface. SQL = Structured Query Language. DBA = Database Administrator. OLE = Object Linking and Embedding.",
        ),
        urdu(
            "آپشن II: فارم کے نام cmd، txt، lbl رکھیں۔ Val() سے جمع کریں۔ Access کے سوال C والے کاغذ جیسے ہی ہیں۔",
        ),
    ],
    mcqs=[mcq("ADO stands for:", ["ActiveX Data Objects", "Access Data Only", "All Data Output", "Array Data Object"], "a")],
    long=["Design on paper a VB form with two text boxes, four command buttons (+ − × ÷) and a label for the result. Write the four Click events."],
))
