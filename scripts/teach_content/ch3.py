from .blocks import check, code, lecture, math, p, steps, svg, table, tip

CHAPTER = {
    "id": "ch3",
    "num": "03",
    "title": "Programming Fundamentals",
    "blurb": "Python, variables, operators, if else, loops, libraries, aur bugs.",
    "lectures": [
        lecture(
            "languages",
            "3.1",
            "Programming aur language ki qismen",
            8,
            [
                p("Computer khud se nahi sochta. Bina instructions ke woh kuch nahi karta. Instructions ke set ko program kehte hain, aur un instructions ki zaban programming language hai."),
                svg("languages", "Low level binary hai, mid level assembly mnemonics, high level angrezi jaise lafz.", "Three language levels."),
                table(
                    ["Level", "Matlab", "Misal"],
                    [
                        ["Low", "Machine ki apni zaban, zero one, insaan ke liye mushkil", "Binary machine language"],
                        ["Mid", "Hardware ke qareeb, lekin words se, mnemonics", "Assembly, MOV AX, BX"],
                        ["High", "Insaan ke liye asaan, angrezi jaise", "C++, Java, Python"],
                    ],
                    "Teen levels: low binary, mid assembly, high C++ Java Python.",
                ),
                p("C++ hardware ke qareeb hai, operating system aur games mein. Java ka naara write once run anywhere hai, enterprise aur Android mein. Python ka syntax seedha hai, data science, AI, web, aur beginners ke liye."),
                check(
                    "Assembly language low hai, mid, ya high?",
                    "Mid level. Mnemonics use karti hai, jaise MOV AX, BX.",
                ),
            ],
        ),
        lecture(
            "python-careers",
            "3.2",
            "Python se career",
            6,
            [
                p("Python is liye seekhte hain ke dimagh logic pe lage, syntax yaad karne pe nahi. Sindh curriculum bhi Python ko shuruat ki zaban banata hai."),
                steps(
                    "Python kahan kaam aati hai",
                    [
                        "Desktop aur web applications.",
                        "Data science: reports aur predictions.",
                        "AI aur machine learning, chatbots, recommendations.",
                        "Django aur Flask se websites.",
                        "Office ke repetitive kaam automate karna.",
                        "Security tools aur network data.",
                    ],
                    "Software, data, AI, web, automation, aur cybersecurity.",
                ),
                check(
                    "Python beginner ko syntax se zyada kis cheez pe focus karne deti hai?",
                    "Problem solving aur logic pe.",
                ),
            ],
        ),
        lecture(
            "ide",
            "3.3",
            "IDE aur VS Code",
            7,
            [
                p("IDE woh jagah hai jahan aap code likhte, chalate, aur sambhalte hain. Ek hi workspace."),
                steps(
                    "IDE ke hisse",
                    [
                        "Code editor, jahan likhte hain.",
                        "Syntax highlighting, rang se parhna asaan.",
                        "Auto completion, likhte waqt suggestion.",
                        "Run button.",
                        "Debugger, galti dhoondhne ke liye.",
                    ],
                    "Editor, colors, suggestions, run, aur debugger.",
                ),
                p("VS Code muft aur halka editor hai. Default mein poora IDE nahi, lekin extensions se ban jata hai. Microsoft ka Python extension laga lein, tab highlighting aur run dono aa jate hain."),
                table(
                    ["Hissa", "Kaam"],
                    [
                        ["Explorer", "Files aur folders"],
                        ["Search", "Project mein lafz dhoondhna"],
                        ["Source Control", "Git se changes"],
                        ["Run and Debug", "Code chalana, line pe rukna, variables dekhna"],
                        ["Extensions", "Python extension jaisi extra cheezein"],
                    ],
                    "Side bar: explorer, search, git, debug, extensions.",
                ),
                check(
                    "VS Code ko Python IDE banane ke liye kya chahiye?",
                    "Python extension, aam tor pe Microsoft wali.",
                ),
            ],
        ),
        lecture(
            "python-basics",
            "3.4",
            "Python program ki bunyad",
            7,
            [
                p("Python program upar se neeche chalta hai. Comments insaan ke liye note hain. Hash se shuru hote hain. Interpreter unhein ignore kar deta hai."),
                p("C++ aur Java curly brackets se block banate hain. Python indentation se. Andar wali line shuru mein spaces leti hai. Standard char spaces hain. Indentation optional nahi, zaroori hai."),
                code(
                    "# yeh comment hai, interpreter ignore karega\nprint(\"Hello, World!\")\nif 5 > 2:\n    print(\"Five is greater than two!\")",
                    "Hash comment hai. If ke neeche print indented hai, warna program nahi chalta.",
                    lang="python",
                ),
                tip("IndentationError aaye to spaces check karein. Tabs aur spaces mila kar program toot jata hai."),
                check(
                    "Python block curly brackets se banta hai ya indentation se?",
                    "Indentation se. Standard char spaces.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "variables",
            "3.4.1",
            "Variables aur data types",
            10,
            [
                p("Variable memory ka naam wala container hai. Python mein type alag se declare nahi karte. Value dekh kar Python khud type laga leta hai. Golden topic hai."),
                steps(
                    "Naam ke rules",
                    [
                        "Letters, numbers, aur underscore chalenge.",
                        "Shuru letter ya underscore se ho, number se nahi. 1name galat hai.",
                        "age aur Age alag variables hain. Case sensitive.",
                        "if, for, while jaise keywords naam nahi ban sakte.",
                        "Beech mein space nahi. my height galat, my_height theek.",
                    ],
                    "Letter se shuru, space nahi, keyword nahi, case alag.",
                ),
                table(
                    ["Type", "Misal"],
                    [
                        ["int", "age = 16"],
                        ["float", "height = 5.7"],
                        ["str", 'name = "Sammy"'],
                        ["bool", "is_student = True"],
                        ["list", "marks = [85, 90, 75]"],
                        ["tuple", "coords = (10, 20). Badal nahi sakte"],
                        ["dict", 'student = {"name": "Ahmed", "age": 16}'],
                        ["set", "vowels = {'a', 'e', 'i'}. Unique cheezein"],
                    ],
                    "Int whole number, float decimal, str text, bool True False, list badal sakti hai, tuple nahi, dict key value, set unique.",
                ),
                tip("Boolean mein True aur False ka pehla letter capital hai. true chhota likhoge to naam ban jayega, Boolean value nahi."),
                check(
                    "List aur tuple mein farq kya hai?",
                    "List badal sakti hai, square brackets. Tuple badal nahi sakta, round brackets.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "io",
            "3.4.2",
            "Input aur output",
            7,
            [
                p("print screen pe dikhata hai. Comma se text aur variable dono ek line mein aa jate hain. f-string sab se parhne layak tareeqa hai."),
                code(
                    'name = "Ali"\nage = 16\nprint("Welcome,", name)\nprint(f"My name is {name} and I am {age} years old.")',
                    "f se pehle string, aur curly brackets ke andar variable.",
                    lang="python",
                ),
                p("input program ko rok deta hai jab tak user kuch likhe. Jo bhi aata hai, woh hamesha string hota hai, chahe user ne number hi kyun na likha ho. Number chahiye to int ya float se type cast karein."),
                code(
                    'user_name = input("Enter your name: ")\nage = int(input("Enter your age: "))\nheight = float(input("Enter your height: "))',
                    "input string deta hai. int aur float us string ko number bana dete hain.",
                    lang="python",
                ),
                check(
                    "input() number return karta hai ya string?",
                    "Hamesha string. Number chahiye to int ya float lagayein.",
                ),
            ],
        ),
        lecture(
            "operators",
            "3.4.3",
            "Operators aur operands",
            12,
            [
                p("Operand value hai, operator nishaan hai. 10 operand, plus operator, 20 operand. Golden topic hai."),
                math(r"9 / 2 = 4.5 \qquad 9 // 2 = 4 \qquad 9 \% 2 = 1 \qquad 2^{3} = 8", "Nau taqseem do float 4.5 hai. Double slash floor 4 hai. Percent remainder 1 hai. Do star star teen, yaani do ki power teen, barabar 8."),
                table(
                    ["Operator", "Kaam", "Misal"],
                    [
                        ["+", "Jama", "5 + 3 = 8"],
                        ["-", "Tafreeq", "10 - 4 = 6"],
                        ["*", "Zarb", "4 * 2 = 8"],
                        ["/", "Taqseem, hamesha float", "9 / 2 = 4.5"],
                        ["//", "Floor, decimal girao", "9 // 2 = 4"],
                        ["%", "Baqi", "9 % 2 = 1"],
                        ["**", "Power", "2 ** 3 = 8"],
                    ],
                    "Division slash float deta hai. Double slash decimal gira deta hai.",
                ),
                p("Assignment: x = 5. x += 2 ka matlab x = x + 2. Relational operators True ya False dete hain. == barabar, != na barabar. Ek equals assign karta hai, do equals compare karte hain."),
                p("and tab True jab dono conditions true hon. or tab True jab ek bhi true ho. not ulta kar deta hai. in check karta hai ke value andar hai ya nahi."),
                code(
                    'name = "Python"\nprint("P" in name)       # True\nprint("z" not in name)   # True\nprint(10 & 6)            # 2\nprint(10 | 6)            # 14\nprint(5 << 1)            # 10\nprint(20 >> 1)           # 10',
                    "Membership in aur not in. Bitwise AND 10 aur 6 ka result 2 hai, OR ka 14. Left shift zarb do, right shift floor taqseem do.",
                    lang="python",
                ),
                table(
                    ["Bits", "AND", "OR", "XOR"],
                    [
                        ["0 0", "0", "0", "0"],
                        ["0 1", "0", "1", "1"],
                        ["1 0", "0", "1", "1"],
                        ["1 1", "1", "1", "0"],
                    ],
                    "Bitwise AND dono one tab one. OR koi ek one. XOR jab bits alag hon.",
                ),
                p("10 binary 1010 hai, 6 binary 0110. AND 0010 deta hai jo decimal 2 hai. OR 1110 deta hai jo 14 hai. NOT of 10, tilde 10, result negative 11 hai. Left shift ek bit se 5 ko 10 bana deta hai."),
                tip("Slash aur double slash ka farq exam ka favourite hai. 9 slash 2 barabar 4.5. 9 double slash 2 barabar 4."),
                check(
                    "10 AND 6 bitwise ka decimal result?",
                    "2. Binary 1010 aur 0110 ka AND 0010 hai.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "sequence",
            "3.5 – 3.5.1",
            "Control structures aur sequence",
            6,
            [
                p("Control structure yeh faisla karti hai ke statements kis order mein chalenge. Teen bunyadi structures hain: sequence, selection, aur repetition."),
                svg("flow", "Sequence seedhi line hai. Start, statement, statement, end. Koi mod nahi.", "Sequence flow."),
                code(
                    'print("Enter two numbers")\na = int(input("Enter first number: "))\nb = int(input("Enter second number: "))\ntotal = a + b\nprint("Sum =", total)',
                    "Pehle input, phir doosra input, phir jama, phir print. Upar se neeche.",
                    lang="python",
                ),
                check(
                    "Python ka default order kya hai?",
                    "Sequence. Upar wali line pehle, neeche wali baad mein.",
                ),
            ],
        ),
        lecture(
            "selection-if",
            "3.5.2",
            "if, elif, aur nested selection",
            10,
            [
                p("Selection condition dekhti hai. True ho to ek raasta, False ho to doosra. Golden topic hai. if aur else ke baad colon zaroori hai, aur andar indentation."),
                code(
                    'age = int(input("Enter your age: "))\nif age >= 18:\n    print("You are an Adult.")\nprint("Program continues...")',
                    "Sirf if ho to False pe block skip, lekin us ke baad wali line phir bhi chalti hai.",
                    lang="python",
                ),
                code(
                    'if age >= 18:\n    print("Apply for CNIC.")\nelse:\n    print("Apply for CRC, B-Form.")',
                    "if else mein dono mein se ek block zaroor chalta hai.",
                    lang="python",
                ),
                code(
                    'marks = int(input("Enter marks: "))\nif marks >= 80:\n    print("A-1 Grade")\nelif marks >= 70:\n    print("A Grade")\nelif marks >= 60:\n    print("B Grade")\nelse:\n    print("Fail or below B")',
                    "elif upar se neeche check karta hai. Pehli true condition milte hi baqi ignore.",
                    lang="python",
                ),
                p("Nested if ka matlab if ke andar if. Loan ki misaal: pehle age 18 ya zyada, phir salary 30000 ya zyada. Dono pass hon to loan approved. Age kam ho to too young. Age theek ho lekin salary kam ho to salary too low."),
                check(
                    "marks 75 hon to A-1 chalega ya A?",
                    "A Grade. 80 se kam hai is liye pehli condition false, 70 wali true, us ke baad kuch nahi chalta.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "loops",
            "3.5.3",
            "for, while, break, aur continue",
            11,
            [
                p("Loop ek block ko baar baar chalata hai taake same lines dobara na likhni parein. Golden topic hai. for tab jab dafa ka pata ho. while tab jab sirf condition pata ho."),
                math(r"\mathrm{range}(3) = 0,1,2", "range 3 zero se shuru hota hai aur 3 ko shamil nahi karta. Output 0, 1, 2."),
                table(
                    ["range", "Output"],
                    [
                        ["range(3)", "0 1 2"],
                        ["range(2, 5)", "2 3 4"],
                        ["range(1, 6, 2)", "1 3 5"],
                        ["range(0, 6, 2)", "Even 0 2 4"],
                    ],
                    "Stop value shamil nahi hoti. Step jump batata hai.",
                ),
                code(
                    "count = 1\nwhile count <= 3:\n    print(count)\n    count += 1",
                    "while tab tak chalti hai jab tak condition true ho. Counter update karna bhool gaye to infinite loop.",
                    lang="python",
                ),
                p("break loop ko foran khatam kar deta hai. continue sirf is dafa ko skip karta hai aur agli iteration pe chala jata hai. range 5 mein i barabar 3 pe break ho to 0 1 2 chhapte hain. continue ho to 0 1 2 4, teen gayab."),
                p("Nested loop: andar wali loop, bahar wali ki har dafa pe shuru se akhir tak chalti hai. Bahar 1 aur 2, andar 1 2 3, to total chhe lines."),
                table(
                    ["for", "while"],
                    [
                        ["Dafa ka pata hai", "Dafa ka pata nahi, condition hai"],
                        ["Counter khud badalta hai", "Counter aap badalte hain"],
                        ["Ginti ke kaam mein chhota", "Jab tak user Stop na kahe"],
                    ],
                    "for known count. while unknown, condition based.",
                ),
                code(
                    'total = 0.0\nshopping = True\nwhile shopping:\n    item = input("Item or done: ")\n    if item.lower() == "done":\n        shopping = False\n    else:\n        price = float(input("Price: "))\n        if price > 0:\n            total += price\nif total >= 5000:\n    total = total - total * 0.20',
                    "Shopping bill sequence, selection, aur repetition ek sath use karti hai. 5000 ya zyada pe 20 percent discount.",
                    lang="python",
                ),
                check(
                    "range(2, 5) kya print karega?",
                    "2, 3, aur 4. 5 shamil nahi.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "libraries",
            "3.6",
            "Built-in aur third-party libraries",
            8,
            [
                p("Library pehle se likha hua code hai. Aap har kaam zero se nahi likhte. Import ke paanch tareeqe hain."),
                code(
                    "import math\nprint(math.sqrt(25))\nimport math as m\nprint(m.sqrt(16))\nfrom math import sqrt, pi\nprint(sqrt(36))",
                    "Poora module import karo to naam dot function. Alias chhota naam. Specific function seedha.",
                    lang="python",
                ),
                tip("Star se sab import karna, from math import star, memory aur clarity dono ke liye kamzor hai. Jo chahiye sirf woh import karein."),
                p("math ke sath pi, ceil jo upar round karta hai, floor jo neeche, pow, aur sqrt. random.randint(1, 10) ek integer. random.random zero aur one ke beech float. datetime.datetime.now abhi ka waqt. strftime percent d dash percent m dash percent Y din mahina saal."),
                table(
                    ["Library", "Kaam", "Install"],
                    [
                        ["math, random, datetime", "Hisab, random, tareekh", "Python ke sath built-in"],
                        ["NumPy", "Bari arrays", "pip install numpy"],
                        ["Pandas", "Table data, Excel CSV", "pip install pandas"],
                        ["Matplotlib", "Graphs", "pip install matplotlib"],
                        ["TensorFlow, PyTorch", "AI", "pip install"],
                    ],
                    "Built-in sirf import. Third party pehle pip install.",
                ),
                check(
                    "math.ceil(4.3) kya dega?",
                    "5. Ceil hamesha upar round karta hai.",
                ),
            ],
        ),
        lecture(
            "debugging",
            "3.7",
            "Syntax, runtime, aur logical errors",
            8,
            [
                p("Debugging ka matlab bug dhoondhna, trace karna, aur theek karna taake program sahi kaam kare."),
                table(
                    ["Error", "Kab pata chalta hai", "Misal"],
                    [
                        ["Syntax", "Chalta hi nahi, grammar toot gaya", 'print("Hello"  — bracket kam'],
                        ["Runtime", "Chalna shuru, beech mein crash", "10 / 0 ZeroDivisionError"],
                        ["Logical", "Crash nahi, jawab galat", "area = length + width, zarb honi chahiye"],
                    ],
                    "Syntax grammar. Runtime crash. Logical galat formula jo chupke galat jawab de.",
                ),
                code(
                    'Traceback (most recent call last):\n  File "debug_program.py", line 1\n    x = int("abc")\nValueError: invalid literal for int() with base 10: \'abc\'',
                    "Traceback teen baatein kehta hai: error ki qisam, file, aur line number. Yahan line 1 pe abc ko int banana ValueError hai.",
                ),
                tip("Logical error sab se khatarnak is liye hai ke program khush ho kar galat jawab de deta hai. Trace table se expected aur actual compare karein."),
                check(
                    "Program chalta hai lekin area galat nikalta hai. Yeh kaun si error hai?",
                    "Logical error. Grammar theek hai, crash nahi, soch galat hai.",
                ),
            ],
        ),
    ],
}
