from content.schema import lecture

LECTURE = lecture(
    id="xi-4",
    number=4,
    title="Data and Analysis",
    kicker="CLASS XI  ·  UNIT 4",
    unit="Unit 4 — Data and Analysis",
    domain="D. Data and analysis",
    periods="about 25 periods",
    intro=(
        "This unit joins two ideas the textbook treats together: keeping data in a database so it stays consistent, "
        "and looking at data so a claim is more than a feeling. You will model a small college database, "
        "then compute a summary, draw an honest chart, and say the difference between a pattern and a cause."
    ),
    outcomes=[
        "Explain tables, keys, relationships, referential integrity, and an entity-relationship model.",
        "Choose a sensible data type and describe forms, queries, and reports.",
        "Compute mean, median, and mode, and match a chart to a question.",
        "Describe a straight-line model y = mx + c and separate correlation from causation.",
        "Distinguish population and sample, parameter and statistic, and an experiment from an observation.",
    ],
    blocks=[
        ("h2", "From lists of files to a database"),
        (
            "p",
            "A **database** is an organised collection of related data. A **database management system** (DBMS), such as the relational tools used in the lab, stores that data, checks the rules, and answers questions. A folder of spreadsheets can hold the same facts, and then the same student is spelled three ways and nobody knows which phone number is current. The database’s job is one copy of each fact, with rules that reject nonsense.",
        ),
        (
            "p",
            "A **table** is about one kind of thing. A **row** (record) is one instance. A **column** (field) is one fact about it. A **primary key** identifies a row and does not repeat: a roll number, not a student name. A **foreign key** is a column that points at a primary key in another table, such as a result row that stores a roll number. **Referential integrity** means every foreign key either is empty, when the rules allow that, or matches a real row. You cannot record a result for a roll number that was never admitted.",
        ),
        (
            "table",
            {
                "caption": "Table 7. Data types you should be able to choose.",
                "headers": ["Fact", "A sensible type", "Why not the neighbour"],
                "rows": [
                    ["Roll number used only as an identifier", "Text, or a whole number if it is truly numeric", "If it has a leading zero, a number type will drop it"],
                    ["Marks", "Number", "Text cannot be averaged reliably"],
                    ["Fee paid or not", "Yes/No (Boolean)", "A text field of “yes” and “Y” and “paid” will not count"],
                    ["Date of admission", "Date", "Text dates sort alphabetically, so 01/12 comes before 02/01"],
                    ["Remarks", "Long text", "A short text field cuts the sentence off"],
                ],
                "widths": [0.34, 0.33, 0.33],
            },
        ),
        ("h2", "Relationships and the ER model"),
        (
            "p",
            "An **entity** is a thing we store: Student, Book, Subject. An **attribute** is a fact about it. A **relationship** is how entities belong together. In a relational database the relationship becomes a key that both tables share.",
        ),
        (
            "table",
            {
                "caption": "Table 8. The three relationship degrees, with a college example.",
                "headers": ["Degree", "Meaning", "Example", "How it is stored"],
                "rows": [
                    ["One-to-one", "Each A matches at most one B", "A student and that student’s identity card", "The card row holds the roll number, unique"],
                    ["One-to-many", "One A matches many B; each B matches one A", "One class, many students", "The student row holds the class id"],
                    ["Many-to-many", "Each side matches many of the other", "Students and subjects", "A third table of pairs, such as Enrolment"],
                ],
                "widths": [0.16, 0.28, 0.28, 0.28],
            },
        ),
        (
            "p",
            "A **relational schema** is the written plan of the tables and keys, without the data. An **entity-relationship diagram** draws entities as rectangles, attributes as ovals or as a list inside the rectangle, and relationships as diamonds or as labelled lines. For a paper sketch, rectangles and labelled lines are enough if the degree is written on the line: 1 and M, or the words “one” and “many”.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — a library schema",
                "text": (
                    "Student(RollNo, Name, ClassName). Book(BookId, Title). Loan(LoanId, RollNo, BookId, DueDate).\n\n"
                    "RollNo is the primary key of Student. BookId is the primary key of Book. "
                    "Loan.RollNo is a foreign key. Loan.BookId is a foreign key. "
                    "One student can have many loans, and one book can appear in many loans over the year, so Student to Loan is one-to-many and Book to Loan is one-to-many. "
                    "The many-to-many between students and books is carried by Loan, not by stuffing several book titles into one student cell. "
                    "Referential integrity rejects a loan whose RollNo is not in Student."
                ),
            },
        ),
        ("figure", "library-er", "Figure 9. Student to Loan is one-to-many, and Book to Loan is one-to-many."),
        (
            "callout",
            {
                "kind": "warn",
                "title": "Common mistake",
                "text": "Repeating groups, such as Book1, Book2, Book3 as columns of Student, are not a relationship. They waste space, they cannot store a fourth book, and they make a query for “who has this title” miserable. Use another table.",
            },
        ),
        ("h2", "Forms, queries, and reports"),
        (
            "p",
            "A **form** is a screen for entering or editing one row, with labels and checks, so the user never types into the raw table. A **query** is a question: which loans are due this week, which students have no loan, what is the average mark in Chemistry. A **criterion** is the condition, such as `DueDate <= today` or `Subject = \"Chemistry\"`. A **report** lays the answer out for printing, with a title, the rows, and a summary such as a count or a total. The same query can feed a report. Do not retype the numbers into a poster.",
        ),
        ("h2", "Summary statistics"),
        (
            "p",
            "A **summary statistic** compresses many values into one careful number. The **mean** is the sum divided by the count. The **median** is the middle value after sorting; if the count is even, average the two middle values. The **mode** is the most frequent value; a list can have more than one mode, or no single mode if every value appears once. The **range** is largest minus smallest. The mean moves when one extreme value is added. The median does not move as much. Say which one you used and why.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — five quiz scores",
                "text": (
                    "Scores: 10, 12, 12, 15, 41.\n\n"
                    "Mean = (10+12+12+15+41) / 5 = 90 / 5 = 18. Median = 12, the third value in the sorted list. Mode = 12. Range = 41 − 10 = 31.\n\n"
                    "The mean is pulled up by 41. If the question is “what did a typical student score?”, the median describes the middle of this tiny class more honestly. "
                    "If the question is “what was the class total worth?”, you need the sum, and the mean is the right average of that sum. The chart and the sentence must ask the same question."
                ),
            },
        ),
        ("h2", "Charts that match the question"),
        (
            "p",
            "A **bar chart** compares categories, such as mean mark by subject. A **pie chart** shows parts of one whole, and only when the parts add to that whole; too many slices make it unreadable. A **line graph** shows change over time, such as lab attendance by week. A **histogram** shows how a numeric measurement is spread, by grouping it into bins. A **scatter plot** shows two numeric variables together, one on each axis, so you can see whether they rise together. A **box plot** shows median and spread. Read a chart by naming it, reading both axes including the units, and only then describing the trend.",
        ),
        (
            "callout",
            {
                "kind": "warn",
                "title": "Common mistake",
                "text": "A bar chart that does not start at zero can make a small difference look huge. A pie chart of average marks is the wrong picture, because those averages are not parts of one whole. Name the deception if a question asks you to criticise a chart.",
            },
        ),
        ("h2", "A straight line, and what it does not prove"),
        (
            "p",
            "When a scatter plot looks roughly straight, a simple model is the line below. Here \\(x\\) is the input you use to predict, \\(y\\) is the value you predict, \\(m\\) is the slope (how much \\(y\\) changes when \\(x\\) increases by 1), and \\(c\\) is the intercept (the predicted \\(y\\) when \\(x\\) is 0). A spreadsheet can fit the line and also report a **correlation** number. Correlation near 1 means the points rise together. Near −1 they move in opposite directions. Near 0 there is little straight-line relationship.",
        ),
        ("math", r"y = mx + c"),
        (
            "p",
            "**Correlation is not causation.** Ice-cream sales and the use of fans rise together because summer drives both, not because ice-cream switches fans on. A model can still be useful for prediction: if study hours and quiz scores move together in your class data, the line is a summary of that association. It does not, by itself, prove that forcing extra hours will raise scores. Other factors — the test’s difficulty, who was absent — may be the real drivers. Those hidden factors are **confounding** factors.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — reading a line",
                "text": (
                    "A fitted line says predicted quiz mark = 4 × (hours of practice) + 20.\n\n"
                    "The slope is 4: one extra hour goes with 4 extra marks in this dataset. The intercept is 20: the line predicts 20 marks at 0 hours. "
                    "Predicting 3 hours gives 4×3+20 = 32. That is a prediction inside the range of the data, not a promise, and it is not a reason to claim the hours caused the marks. "
                    "If nobody in the data practised 0 hours, do not make a speech about the intercept as a real student."
                ),
            },
        ),
        ("h2", "Population, sample, experiment"),
        (
            "p",
            "The **population** is everyone you want the conclusion to cover. A **sample** is the group you actually measure. A **parameter** is a number about the population, often unknown, such as the mean mark of every Class XI CS student in Karachi. A **statistic** is the matching number computed from the sample, such as the mean of your own section. A statistic estimates a parameter. It is not the parameter, and a sample of one section does not authorise a sentence that begins “Karachi students are…”.",
        ),
        (
            "p",
            "An **experiment** assigns the condition: this group uses the new worksheet, that group uses the old one, and the assignment is by chance. An **observational study** measures what people already do, without assigning it. A **survey** asks them. Only a careful experiment supports a cautious causal sentence, and even then only about the people and the conditions you studied. Observation can suggest a hypothesis. It should not be dressed up as proof.",
        ),
        (
            "p",
            "Class XI stops at this idea of a model. You are not required to derive a formula for the slope by hand. You should be able to say what m and c mean, read a chart, and refuse a causal claim the data cannot carry. Building the line in a spreadsheet, and saying in one sentence what it does not prove, is the practical.",
        ),
        (
            "callout",
            {
                "kind": "exam",
                "title": "Exam tip",
                "text": "Database questions want the keys named on a specific scenario, not a definition copied in isolation. Statistics questions want the number and the choice: mean or median, and why. If both parts appear in one long question, use a heading for the schema and a heading for the chart.",
            },
        ),
    ],
    terms=[
        ("DBMS", "Software that stores related data and enforces rules."),
        ("Primary key", "The column, or columns, that identify one row."),
        ("Foreign key", "A column that must match a primary key in another table."),
        ("Referential integrity", "No foreign key points at a missing row."),
        ("ER model", "A drawing of entities, attributes, and relationships."),
        ("Query / criterion", "A question, and the condition that filters the rows."),
        ("Mean / median / mode", "Arithmetic average, middle of the sorted list, most frequent value."),
        ("Correlation", "A measure of straight-line association, not a cause."),
        ("Population / sample", "The whole group of interest, and the part you measured."),
        ("Parameter / statistic", "A number about the population, and the estimate from the sample."),
        ("Experiment", "A study where the condition is assigned, preferably at random."),
    ],
    checks=[
        {
            "q": "Why is a student name a poor primary key?",
            "a": "Names repeat, spellings change, and two students can share a name. A key must identify one row. A roll number is designed to do that.",
        },
        {
            "q": "Scores 4, 8, 8, 10. State the mode and the median.",
            "a": "The sorted list is already in order. Mode is 8. There are four values, so the median is the average of the second and third, (8+8)/2 = 8.",
        },
        {
            "q": "Your section’s mean is 61. Is 61 a parameter?",
            "a": "No. It is a statistic about the sample you measured. It would estimate a parameter only if you had defined a wider population and treated the section as a sample of it — and one section is a weak sample of all BIEK candidates.",
        },
    ],
    mcqs=[
        {
            "q": "Referential integrity is broken when",
            "options": [
                "a foreign key matches no primary key",
                "a table has more than ten rows",
                "a query uses a criterion",
                "a report has a title",
            ],
            "answer": "A",
            "why": "The foreign key is supposed to point at a real row. A dangling reference breaks the rule.",
        },
        {
            "q": "Students and subjects, where each student takes many subjects and each subject has many students, need",
            "options": [
                "one table with a subject column only",
                "a third table of pairs",
                "a pie chart",
                "two copies of the student name in the subject table",
            ],
            "answer": "B",
            "why": "Many-to-many is stored as a linking table, such as Enrolment(RollNo, SubjectCode).",
        },
        {
            "q": "A line graph is the fitting chart for",
            "options": [
                "weekly attendance over a term",
                "the share of one fixed total among three clubs",
                "a list of phone numbers",
                "the primary key",
            ],
            "answer": "A",
            "why": "A line is for change over time. A share of a whole is a pie, if the slices are few.",
        },
        {
            "q": "Two variables rise together. The justified sentence is",
            "options": [
                "one must cause the other",
                "they are associated in this data",
                "the intercept is the cause",
                "the sample is the population",
            ],
            "answer": "B",
            "why": "Association is what the scatter plot shows. Cause needs a design that can separate other explanations.",
        },
    ],
    shorts=[
        {
            "q": "Define primary key and foreign key using the Loan and Student tables.",
            "a": "Student.RollNo is a primary key: it identifies one student and does not repeat. Loan.RollNo is a foreign key: it stores a roll number that must already exist in Student. Referential integrity is that rule.",
        },
        {
            "q": "When is the median a better single summary than the mean?",
            "a": "When a few extreme values pull the mean away from the middle of the group. In 10, 12, 12, 15, 41 the mean is 18 and the median is 12. If the question is about a typical score, report the median and mention the extreme value rather than hiding it.",
        },
        {
            "q": "Give one example of an experiment and one of an observation in a college.",
            "a": "An experiment assigns, at random, one section to a new worksheet and another to the old worksheet, then compares quiz scores. An observation asks students how many hours they already study and compares those reports with scores, without assigning the hours. Only the first can support a careful sentence about the worksheet.",
        },
    ],
    longs=[
        {
            "marks": 5,
            "q": "A clinic stores patients and appointments. A patient may have many appointments. An appointment is with one patient. Design the schema, name the keys, and state the relationship degree.",
            "a": (
                "Patient(PatientId, Name, Phone). Appointment(AppointmentId, PatientId, ApptDate, Reason).\n\n"
                "PatientId is the primary key of Patient. AppointmentId is the primary key of Appointment. "
                "Appointment.PatientId is a foreign key referencing Patient.PatientId. "
                "The relationship is one-to-many: one patient, many appointments, and each appointment belongs to one patient. "
                "Referential integrity forbids an appointment whose PatientId is not in Patient. "
                "Phone is not the primary key, because two patients can share a household number and a patient can change phones."
            ),
        },
        {
            "marks": 5,
            "q": "Quiz marks in one section are 6, 7, 7, 9, 21. Compute the mean and the median. Recommend a chart if you must compare this section with two other sections, and write two sentences you are willing to say about a positive correlation between practice hours and these marks.",
            "a": (
                "Mean = (6+7+7+9+21)/5 = 50/5 = 10. Sorted, the middle value is 7, so the median is 7. "
                "The single 21 pulls the mean up; a comparison of “typical” performance should show the median as well as the mean.\n\n"
                "A bar chart of the three section medians, with the axis starting at 0, compares categories. A pie chart does not.\n\n"
                "A positive correlation would mean that, in this sample, higher practice hours go with higher marks along a rough straight line. "
                "It does not prove that practice caused the marks, because ability, the particular quiz, and who chose to practise are not controlled here. "
                "The honest second sentence limits the claim to this section’s data."
            ),
        },
    ],
    labs=[
        {
            "title": "Lab 6 — Schema, query, and a chart",
            "steps": [
                "In the DBMS available in the lab (or on paper if the lab PCs are down), create Student and Result with a foreign key.",
                "Enter four students and six results. Try to enter a result for a roll number that does not exist, and record the error.",
                "Write a query for one subject and a report that shows the rows and the average.",
                "In a spreadsheet, compute the mean and median of those marks and draw a bar chart of average by subject. State one thing the chart does not prove.",
            ],
            "success": "The illegal result is rejected. The average on the report matches a hand calculation. The written sentence refuses a causal claim.",
        }
    ],
    summary=[
        "One fact lives in one place. Primary keys identify rows. Foreign keys link tables. Referential integrity keeps the links real.",
        "One-to-many puts the key on the “many” side. Many-to-many needs a third table.",
        "Forms edit, queries ask, criteria filter, reports present.",
        "Mean is the arithmetic average. Median is the middle. Mode is the most common. Extremes pull the mean.",
        "Bars compare categories, lines show time, pies show a whole, scatter shows two numbers.",
        "y = mx + c summarises a straight association. Correlation does not prove cause.",
        "A statistic describes a sample. A parameter describes a population. Experiments assign the condition; observations do not.",
    ],
)
