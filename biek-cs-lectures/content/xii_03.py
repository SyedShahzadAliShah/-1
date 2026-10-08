from content.schema import lecture

LECTURE = lecture(
    id="xii-3",
    number=3,
    title="Python: Objects, Files, and Databases",
    kicker="CLASS XII  ·  UNIT 3",
    unit="Unit 3 — Programming Fundamentals",
    domain="C. Programming fundamentals",
    periods="about 40 periods",
    intro=(
        "Class XI functions and lists are still the foundation. This lecture adds the reasons programming languages offer more than one style, "
        "then the Class XII toolkit: a small class, dictionaries, files, and a database you can normalise and query. "
        "Debugging moves from a single dry run to a unit test and a breakpoint."
    ),
    outcomes=[
        "Compare object-oriented and functional styles at the level of purpose, benefits, and costs.",
        "Define a Python class with a constructor, attributes, and methods, and create two objects.",
        "Use lists, nested lists, and dictionaries, and say when a dictionary fits better.",
        "Read and write a text file, and count letters in a file.",
        "Explain normalisation to third normal form and write a filtered, ordered SQL query.",
        "Describe a unit test and use a print or a breakpoint to locate a fault.",
    ],
    blocks=[
        ("h2", "Why there is more than one style"),
        (
            "p",
            "A **paradigm** is a style of organising a program so that a large problem stays understandable. **Imperative** code is the sequence, selection, and loops you already write. **Object-oriented programming** groups data and the operations on that data into objects, so a vehicle’s mileage is updated by a vehicle, not by a loose function that might be handed the wrong variables. **Functional** programming emphasises functions that return results from inputs and avoid hidden changes to shared data, which makes some reasoning and testing easier. Python can host all three. This unit asks you to write a small object-oriented program and to say, in prose, what the functional emphasis would protect you from.",
        ),
        (
            "table",
            {
                "caption": "Table 12. A comparison you can reproduce in a short question. It is about organisation, not about which language is fashionable.",
                "headers": ["Style", "What you gain", "What it costs"],
                "rows": [
                    ["Imperative", "Direct steps, easy to trace", "A long script becomes a tangle of shared variables"],
                    ["Object-oriented", "Data and its operations stay together; pieces can be reused", "A tiny task can be over-wrapped in classes"],
                    ["Functional", "Functions are easier to test when they do not secretly change other data", "Some problems read awkwardly if you ban every change"],
                ],
                "widths": [0.22, 0.40, 0.38],
            },
        ),
        ("h2", "A class in Python"),
        (
            "p",
            "A **class** is the pattern. An **object** is one instance. **Attributes** are the data kept on the object. **Methods** are functions defined in the class; their first parameter is `self`, the object itself. `__init__` is the **constructor**: it runs when the object is created and usually stores the attributes. Outside the class you do not need to pass `self`. `Vehicle(\"Car\", ...)` is enough.",
        ),
        (
            "code",
            {
                "lang": "Python",
                "text": (
                    "class Vehicle:\n"
                    "    def __init__(self, vehicle_type, brand, model, mileage):\n"
                    "        self.vehicle_type = vehicle_type\n"
                    "        self.brand = brand\n"
                    "        self.model = model\n"
                    "        self.mileage = mileage\n"
                    "\n"
                    "    def update_mileage(self, new_mileage):\n"
                    "        self.mileage = new_mileage\n"
                    "\n"
                    "    def display(self):\n"
                    "        print(\n"
                    "            self.vehicle_type,\n"
                    "            self.brand,\n"
                    "            self.model,\n"
                    "            self.mileage,\n"
                    "        )\n"
                    "\n"
                    "\n"
                    "car = Vehicle(\"Car\", \"Suzuki\", \"Alto\", 12000)\n"
                    "van = Vehicle(\"Van\", \"Toyota\", \"Hiace\", 54000)\n"
                    "car.update_mileage(12500)\n"
                    "car.display()\n"
                    "van.display()"
                ),
            },
        ),
        (
            "p",
            "The run prints `Car Suzuki Alto 12500` and then `Van Toyota Hiace 54000`. The van is unchanged, which shows that each object has its own attributes. Encapsulation, at the level of this course, means those attributes are meant to be changed through methods such as `update_mileage` rather than by scattered assignments all over the program. Python will not stop you reaching in, but the method is the clear door.",
        ),
        ("h2", "Lists and dictionaries"),
        (
            "p",
            "A **nested list** is a list whose items are lists: one row per student, columns for id, name, and grade. A **dictionary** stores **values under keys**. Lookup by a key does not walk the whole collection the way a search of a list does. For a handful of rows you will not feel the difference. The design difference is already real: a dictionary says the id is the way you ask.",
        ),
        (
            "code",
            {
                "lang": "Python",
                "text": (
                    "rows = [\n"
                    "    [101, \"Ali\", 85],\n"
                    "    [102, \"Babar\", 90],\n"
                    "    [103, \"Sana\", 78],\n"
                    "]\n"
                    "by_id = {\n"
                    "    101: {\"name\": \"Ali\", \"grade\": 85},\n"
                    "    102: {\"name\": \"Babar\", \"grade\": 90},\n"
                    "    103: {\"name\": \"Sana\", \"grade\": 78},\n"
                    "}\n"
                    "\n"
                    "print(by_id[103][\"name\"])\n"
                    "found = None\n"
                    "for row in rows:\n"
                    "    if row[0] == 103:\n"
                    "        found = row[1]\n"
                    "print(found)"
                ),
            },
        ),
        (
            "p",
            "Both prints are `Sana`. The dictionary reaches the key 103 directly. The nested list scans rows until the id matches. Use the list when the order of rows is the point, or when you will walk every row anyway. Use the dictionary when the question is “what do we know about this id?”. A list can be a value inside a dictionary, and a dictionary can sit inside a list. Do not nest them so deeply that you cannot say, in one sentence, what the outer collection means.",
        ),
        ("h2", "Files"),
        (
            "p",
            "Variables disappear when the program ends. A **file** keeps data on disk. `open` connects the program to a file. A mode of `\"w\"` starts a text file for writing and **replaces** existing contents. `\"a\"` appends. `\"r\"` reads. Always close the file, or use `with`, which closes it even if a later line fails. Disk input and output matters because results, logs, and datasets are larger than a screen and must still be there tomorrow.",
        ),
        (
            "code",
            {
                "lang": "Python",
                "text": (
                    "def count_letters(path):\n"
                    "    counts = {}\n"
                    "    with open(path, encoding=\"utf-8\") as handle:\n"
                    "        text = handle.read().lower()\n"
                    "    for ch in text:\n"
                    "        if \"a\" <= ch <= \"z\":\n"
                    "            counts[ch] = counts.get(ch, 0) + 1\n"
                    "    return counts\n"
                    "\n"
                    "\n"
                    "with open(\"sample.txt\", \"w\", encoding=\"utf-8\") as handle:\n"
                    "    handle.write(\"Abba!\")\n"
                    "print(count_letters(\"sample.txt\"))"
                ),
            },
        ),
        (
            "p",
            "The file contains A, b, b, a, and an exclamation mark. After lowering, the counts are a: 2, b: 2. The exclamation mark is ignored because the test keeps only `a` to `z`. `dict.get(ch, 0)` returns 0 when the letter has not been seen, so the first time a letter appears the count becomes 1. This is the standard “occurrences of each letter” practical.",
        ),
        ("h2", "Normalisation"),
        (
            "p",
            "**Normalisation** organises tables so that a fact is stored once and update anomalies shrink. You should be able to reach **third normal form** on a small example and say what was wrong before.",
        ),
        (
            "numbers",
            [
                "**First normal form (1NF):** each column holds one value, not a list. Repeating groups such as Subject1, Subject2 are removed.",
                "**Second normal form (2NF):** the table is in 1NF, and every non-key column depends on the whole key, not on part of it. This bites when the key is made of two columns.",
                "**Third normal form (3NF):** the table is in 2NF, and no non-key column depends on another non-key column. A fact about an instructor does not live in the course row if it depends only on the instructor.",
            ],
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — from a wide row to 3NF",
                "text": (
                    "Start with Result(StudentId, CourseId, StudentName, CourseName, InstructorId, InstructorOffice, Grade). "
                    "The intended key is (StudentId, CourseId).\n\n"
                    "StudentName depends only on StudentId. CourseName and InstructorId depend only on CourseId. "
                    "Those are partial dependencies, so the table is not in 2NF. Split:\n\n"
                    "Student(StudentId, StudentName)\n"
                    "Course(CourseId, CourseName, InstructorId, InstructorOffice)\n"
                    "Result(StudentId, CourseId, Grade)\n\n"
                    "Result is now in 3NF: Grade depends on the whole key. "
                    "Course is in 2NF but not in 3NF, because InstructorOffice depends on InstructorId, and InstructorId depends on CourseId. Split again:\n\n"
                    "Course(CourseId, CourseName, InstructorId)\n"
                    "Instructor(InstructorId, InstructorOffice)\n\n"
                    "Changing an office is now one edit. Grade is still stored per student per course."
                ),
            },
        ),
        ("h2", "SQL you can write by hand"),
        (
            "p",
            "The queries in this course read a table, filter it, summarise it, and order it. Learn this pattern and you can answer the paper even if the lab uses a particular product.",
        ),
        (
            "code",
            {
                "lang": "SQL",
                "text": (
                    "SELECT name, salary\n"
                    "FROM employees\n"
                    "WHERE department = 'IT'\n"
                    "ORDER BY salary DESC;\n"
                    "\n"
                    "SELECT AVG(salary) AS average_salary\n"
                    "FROM employees;"
                ),
            },
        ),
        (
            "p",
            "Suppose the rows are Hina, IT, 90000; Omar, Sales, 70000; and Sara, IT, 110000. The first query returns Sara then Hina, because of the descending salary order, and does not return Omar. The average of all three salaries is (90000 + 70000 + 110000) / 3 = 90000. `WHERE` filters before the average if you put it on that query. Without `WHERE`, Sales is included. Say which table the question printed before you compute.",
        ),
        (
            "p",
            "A Python program can talk to a database through a library: open a connection, execute a statement, commit a change, close the connection. The paper may not ask for the connection syntax of a particular product. It will ask what the query returns and why the tables were split. If your lab uses SQLite, the same SQL above is enough.",
        ),
        ("h2", "Tests and breakpoints"),
        (
            "p",
            "A **unit test** calls one function or one method with a known input and checks the returned value or the new attribute. `celsius_to_fahrenheit(0)` should be 32. `update_mileage` on a fresh vehicle should leave the other vehicle alone. A test that requires you to type at the keyboard is a weaker test. **Breakpoints** pause a running program so you can see attributes at that line. A **watch** is the variable you have asked the debugger to show. Until the debugger is familiar, print the id and the grade just before the line you distrust, then delete that print.",
        ),
        (
            "callout",
            {
                "kind": "warn",
                "title": "Common mistake",
                "text": "Opening a file with mode \"w\" to read it erases it first. Counting letters without `.lower()` treats `A` and `a` as different, which may or may not match the question. Storing InstructorOffice in every course row means one move of office must be edited many times, and one of those edits will be missed.",
            },
        ),
    ],
    terms=[
        ("Paradigm", "A style of organising a program."),
        ("Class / object", "The pattern, and one instance of it."),
        ("Constructor", "`__init__`, which stores the new object’s attributes."),
        ("Dictionary", "Values stored under keys, for lookup by key."),
        ("Nested list", "A list of lists, often one row per record."),
        ("Unit test", "A check that one function does one known job."),
        ("1NF, 2NF, 3NF", "Atomic values; full dependence on the key; no dependence on another non-key column."),
        ("WHERE / ORDER BY", "The filter and the sort of an SQL query."),
    ],
    checks=[
        {
            "q": "What does the sample Vehicle program print for the car after update_mileage(12500)?",
            "a": "Car Suzuki Alto 12500. The van remains Van Toyota Hiace 54000.",
        },
        {
            "q": "Why is InstructorOffice removed from Course on the way to 3NF?",
            "a": "It depends on InstructorId, not on CourseId. InstructorId is not the key of Course. A non-key column depending on another non-key column violates 3NF.",
        },
        {
            "q": "What does count_letters return for a file whose text is Abba! ?",
            "a": "A dictionary with a: 2 and b: 2. The exclamation mark is ignored and the letters are lowered before counting.",
        },
    ],
    mcqs=[
        {
            "q": "A primary benefit of object-oriented programming, at this level, is that",
            "options": [
                "it forbids all functions",
                "data and the operations on it can be kept and reused together",
                "it removes the need for variables",
                "it is always the fastest possible style",
            ],
            "answer": "B",
            "why": "The point of a class is to keep related data and behaviour together. The other options are false.",
        },
        {
            "q": "Mode \"w\" in open",
            "options": [
                "appends safely",
                "replaces the file’s contents for writing",
                "reads only",
                "normalises to 3NF",
            ],
            "answer": "B",
            "why": "Write mode truncates an existing file. Append is \"a\". Read is \"r\".",
        },
        {
            "q": "AVG(salary) without a WHERE clause",
            "options": [
                "averages only the IT rows",
                "averages every row of the table",
                "sorts the table",
                "deletes the Sales rows",
            ],
            "answer": "B",
            "why": "The filter is what restricts the average. No filter means the whole table.",
        },
        {
            "q": "A unit test is most useful when the function",
            "options": [
                "returns a value you can check",
                "only clears the screen",
                "has no name",
                "must be retyped by the user on every run",
            ],
            "answer": "A",
            "why": "The test compares a known input with an expected result. A return value makes that comparison direct.",
        },
    ],
    shorts=[
        {
            "q": "Write a Python dictionary for the three students Ali 85, Babar 90, and Sana 78, keyed by 101, 102, and 103. How do you print Sana’s grade?",
            "a": "by_id = {101: {\"name\": \"Ali\", \"grade\": 85}, 102: {\"name\": \"Babar\", \"grade\": 90}, 103: {\"name\": \"Sana\", \"grade\": 78}}. Print by_id[103][\"grade\"], which is 78. The outer key is the id. The inner keys are the field names.",
        },
        {
            "q": "State one partial dependency and one transitive dependency in the wide Result table from this lecture.",
            "a": "StudentName depends only on StudentId, which is part of the key (StudentId, CourseId). That is partial. After Course is split out, InstructorOffice depends on InstructorId rather than on CourseId. That is transitive, and it is why Instructor becomes its own table.",
        },
        {
            "q": "What should a unit test for update_mileage check?",
            "a": "Create a vehicle with mileage 100, call update_mileage(150), and check that the attribute is 150. Create a second vehicle and check that its mileage did not change. A test that only prints the first vehicle can hide the second fault.",
        },
    ],
    longs=[
        {
            "marks": 5,
            "q": "Design a Vehicle class in Python with type, brand, model, and mileage. Include a constructor, a method to update mileage, and a method to display the vehicle. Show two objects and one update.",
            "a": (
                "The class in this lecture is the answer. The constructor stores the four attributes on self. "
                "update_mileage replaces self.mileage. display prints the four attributes. "
                "car = Vehicle(\"Car\", \"Suzuki\", \"Alto\", 12000) and van = Vehicle(\"Van\", \"Toyota\", \"Hiace\", 54000) create two independent objects. "
                "car.update_mileage(12500) changes only the car. The printed lines are Car Suzuki Alto 12500 and Van Toyota Hiace 54000.\n\n"
                "A functional style would instead return a new description without changing an object. "
                "The object-oriented version fits here because the mileage is a lasting fact about one vehicle and several operations share those attributes."
            ),
        },
        {
            "marks": 5,
            "q": "Normalise Result(StudentId, CourseId, StudentName, CourseName, InstructorId, InstructorOffice, Grade), with key (StudentId, CourseId), to 3NF. Then write a query idea, in SQL or in clear words, for the average grade of one course.",
            "a": (
                "Student(StudentId, StudentName). Instructor(InstructorId, InstructorOffice). "
                "Course(CourseId, CourseName, InstructorId). Result(StudentId, CourseId, Grade). "
                "StudentName was partial on StudentId. Course facts were partial on CourseId. "
                "InstructorOffice was transitive through InstructorId and therefore left the Course table.\n\n"
                "SELECT AVG(Grade) AS average_grade FROM Result WHERE CourseId = 'CS12';\n\n"
                "The WHERE must be present or the average mixes every course. "
                "The student name is not in Result anymore, which is the point of the split: you join Student if you need the name, and you do not repeat the name on every grade."
            ),
        },
    ],
    labs=[
        {
            "title": "Lab 3 — Class, file, and a query",
            "steps": [
                "Implement Vehicle and print the two lines from the worked example.",
                "Write sample.txt containing Abba! and print the letter counts. Add a capital letter and confirm it merges after lowercasing.",
                "Create the 3NF tables in SQLite or on paper. Insert two students, two instructors, two courses, and three results.",
                "Run the average-grade query for one course and check it by hand.",
                "Add one assert, or a small test function, that update_mileage does not change the other object.",
            ],
            "success": "The car prints 12500, the letter count shows a and b, and the SQL average matches the hand average of that course only.",
        }
    ],
    summary=[
        "Paradigms organise programs. Objects keep data with behaviour. Functions are easier to test when they do not change hidden state.",
        "A class has a constructor, attributes, and methods. Each object keeps its own attributes.",
        "A dictionary answers “this key”. A nested list keeps rows in order and is scanned.",
        "Use with to open a file. Mode w replaces the file. Lowercase before counting letters if case should not matter.",
        "1NF removes repeating groups. 2NF removes partial dependencies. 3NF removes transitive dependencies.",
        "WHERE filters. ORDER BY sorts. AVG without WHERE covers the whole table.",
        "A unit test checks one known result. A breakpoint shows the variables in the middle of a run.",
    ],
)
