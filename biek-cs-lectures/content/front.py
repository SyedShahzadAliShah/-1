"""Shared front matter and end matter for the two lecture books."""

XI_FRONT = [
    (
        "p",
        "These notes are for classroom teaching of Computer Science at the Board of Intermediate Education Karachi. "
        "They follow the six units of the Sindh Textbook Board Class XI book for the session that uses the New Sindh Curriculum of Computer Science 2024, aligned with the National Curriculum of Pakistan 2022–23. "
        "They are original teaching notes. They are not an official BIEK paper, not a Sindh Textbook Board book, and not a replacement for the prescribed textbook or the current model paper.",
    ),
    ("h2", "How the book is arranged"),
    (
        "p",
        "Each lecture states what a student should be able to do, teaches the idea with a worked example, and then gives board-style questions with model answers. "
        "Equations are typeset with MathJax and the figures are SVG drawings embedded in the PDF. "
        "Read the example before the answer key. In class, cover the model answer until the attempt is on paper. "
        "The practicals match the 25 practical marks: keep a journal with the aim, the steps, the output, and one fault you fixed.",
    ),
    (
        "table",
        {
            "caption": "The Class XI book, and the national domains those units carry.",
            "headers": ["Lecture", "Textbook unit", "You will be asked to"],
            "rows": [
                ["1", "Computer Systems", "Use gates and truth tables, describe the SDLC, and compare topologies and basic security"],
                ["2", "Computational Thinking and Algorithms", "Write and trace pseudocode, linear search, binary search, bubble sort, and insertion sort"],
                ["3", "Programming Fundamentals", "Write Python with decisions, loops, turtle graphics, lists, and functions"],
                ["4", "Data and Analysis", "Model a small database and describe data without calling an association a cause"],
                ["5", "Applications and Impacts", "Explain IoT, cloud, and blockchain in a real setting, and judge a source"],
                ["6", "Digital Literacy", "Search, collect, and present data, and test a small prototype"],
            ],
            "widths": [0.14, 0.36, 0.50],
        },
    ),
    ("h2", "Marks"),
    (
        "p",
        "In the BIEK scheme of studies, Computer Science Paper I is 75 marks of theory and 25 marks of practical. "
        "Recent higher-secondary patterns split theory into multiple choice, short answers, and long answers, often near 20, 40, and 40 percent. "
        "Confirm the model paper for the year you will sit. These notes practise all three kinds. A practical journal that only contains printed output, with no input and no fault, is a weak practical.",
    ),
    ("h2", "How to write an answer"),
    (
        "bullets",
        [
            "Start a short answer with the definition the question named, then one precise point or a tiny example. Stop.",
            "Start a long answer with a one-line claim, then headings. A table or a trace on its own line is easier to mark than a paragraph that hides the numbers.",
            "Use the scenario in the question. A memorised definition that never mentions the college, the list, or the sensor loses the application marks.",
            "If you are unsure of a figure, show the working. A wrong final line with a correct method can still earn method marks. An invented p-value cannot.",
            "For a program, write the sample input and the output your code would actually produce.",
        ],
    ),
    (
        "callout",
        {
            "kind": "note",
            "title": "A limit on security topics",
            "text": "Where the curriculum names an attack, these notes say what harm it causes and what a student or a college should do instead. They do not give instructions for breaking into a system, building malware, or sending phishing messages. That work is not the practical.",
        },
    ),
]

XII_FRONT = [
    (
        "p",
        "These notes are for classroom teaching of Computer Science at the Board of Intermediate Education Karachi, Paper II, Class XII. "
        "They follow the six units of the Sindh Textbook Board Class XII book under the New Sindh Curriculum of Computer Science 2024, aligned with the National Curriculum of Pakistan 2022–23. "
        "They assume the Class XI lectures: gates, searches, Python functions, a first database, and a prototype. "
        "They are original teaching notes, not an official board publication and not a substitute for the prescribed textbook or the year’s model paper.",
    ),
    ("h2", "How the book is arranged"),
    (
        "table",
        {
            "caption": "The Class XII book.",
            "headers": ["Lecture", "Textbook unit", "You will be asked to"],
            "rows": [
                ["1", "Computer Systems", "Judge usability, accessibility, and security together"],
                ["2", "Computational Thinking and Algorithms", "Use stacks, queues, and trees, and evaluate a solution"],
                ["3", "Programming Fundamentals", "Write a class, use files and dictionaries, and normalise to 3NF"],
                ["4", "Data and Analysis", "Measure a model and write a hypothesis test without over-claiming"],
                ["5", "Applications and Impacts", "Design a Pakistani application and a privacy compromise"],
                ["6", "Entrepreneurship", "Test a minimum viable product against a failure rule"],
            ],
            "widths": [0.14, 0.36, 0.50],
        },
    ),
    ("h2", "Marks"),
    (
        "p",
        "Paper II is 75 marks of theory and 25 marks of practical, as in the BIEK scheme of studies. "
        "Practise multiple choice, short answers, and long answers, and confirm the current model paper’s exact split. "
        "Several Class XII questions are two-part: a calculation or a traversal, then a sentence that limits the claim. Leave time for the sentence. It is often the difference between a mechanical answer and full marks.",
    ),
    ("h2", "How to write an answer"),
    (
        "bullets",
        [
            "For a tree, write the rule (inorder, preorder, postorder, BFS, or DFS) before the list of nodes. Use the diagram printed in the question.",
            "For a metric, write the formula, then the substitution, then the percent. Say what the percent counts.",
            "For a hypothesis, write H0 and H1 in the words of the study. Do not invent a p-value the question did not give.",
            "For a design, name the user, the data, the technology you refused, and one risk.",
            "For an MVP, write the failure rule. An answer with no way to fail is a poster, not a test.",
        ],
    ),
]

XI_CLOSING = [
    ("h2", "Formulas and traces worth memorising"),
    (
        "table",
        {
            "headers": ["Item", "Keep this exact"],
            "rows": [
                ["NOT", "0→1 and 1→0"],
                ["AND / OR", "AND is 1 only if all inputs are 1. OR is 0 only if all inputs are 0."],
                ["NAND", "Opposite of AND. Universal."],
                ["XOR", "1 when the inputs differ. A XOR B = A'B + AB'."],
                ["De Morgan", "(A+B)' = A'·B' and (A·B)' = A'+B'."],
                ["Duality", "Swap AND with OR and 0 with 1. Variables stay."],
                ["Binary search", "Sorted list only. Middle by integer division. Move low or high. Stop when found or low passes high."],
                ["Bubble sort", "Swap unordered neighbours. Show each pass."],
                ["Insertion sort", "Grow a sorted portion on the left."],
                ["Mean", "Sum divided by count. Median is the middle of the sorted list."],
                ["Line", "y = mx + c. Correlation is not causation."],
                ["List index", "Python starts at 0. Board pseudocode in these notes starts at 1 unless a question says otherwise."],
            ],
            "widths": [0.24, 0.76],
        },
    ),
    ("h2", "Practical journal for the 25 marks"),
    (
        "bullets",
        [
            "Lab 1: an eight-row truth table that matches a circuit.",
            "Lab 2: an SDLC page with three black-box tests.",
            "Lab 3: a binary-search trace, including a missing item.",
            "Lab 4: a tested function and a list search, with a dry run.",
            "Lab 5: a turtle compound shape and the angle you chose.",
            "Lab 6: a schema that rejects a bad foreign key, plus a chart with a refused causal claim.",
            "Lab 7: one technology, two stakeholders, one source you trust, and why.",
            "Lab 8: a search string, a chart with n, and two versions of a prototype.",
        ],
    ),
    (
        "p",
        "Take the journal to the practical. A marker should be able to repeat one test from your notes and get your result.",
    ),
]

XII_CLOSING = [
    ("h2", "Results worth being able to reproduce"),
    (
        "table",
        {
            "headers": ["Topic", "A check you can do in one minute"],
            "rows": [
                ["BST inorder", "The sequence is sorted. If it is not, the tree or the walk is wrong."],
                ["Preorder / postorder", "Node first, or node last, with left before right unless the question says otherwise."],
                ["Precision", "TP / (TP + FP). In the lecture matrix, 90/120 = 75 percent."],
                ["P-value", "Surprise if H0 is true. Not the probability that H0 is true."],
                ["3NF", "No non-key column depends on another non-key column."],
                ["File mode w", "Replaces the file. Use it when you mean to."],
                ["MVP", "A real minimal offer plus a failure rule written beforehand."],
            ],
            "widths": [0.28, 0.72],
        },
    ),
    ("h2", "The lecture tree, for the journal"),
    (
        "p",
        "Root 50; left 30 with children 20 and 40; right 70 with children 60 and 80. "
        "Preorder: 50, 30, 20, 40, 70, 60, 80. "
        "Inorder: 20, 30, 40, 50, 60, 70, 80. "
        "Postorder: 20, 40, 30, 60, 80, 70, 50. "
        "Use the question’s tree in the examination. Use this one only as a check that your method works.",
    ),
    ("h2", "Practical journal for the 25 marks"),
    (
        "bullets",
        [
            "Lab 1: two usability tests and one security control with a recovery path.",
            "Lab 2: a BST with three traversals and a missing-value search.",
            "Lab 3: the Vehicle program, a letter count, a 3NF schema, and a checked SQL average.",
            "Lab 4: precision, recall, accuracy, and a chart you refuse to over-claim.",
            "Lab 5: a design that names a technology it did not use, and a folder that is not shared by one password.",
            "Lab 6: an MVP test with a failure rule and the decision that followed from it.",
        ],
    ),
    (
        "p",
        "If the practical slot is short, do the tree, the class, the query, and the metric. Those four cover the calculations markers can mark quickly, and your journal still shows the design writing for the rest.",
    ),
]
