"""Map original topic HTML onto BIEK textbook lecture order.

Each lecture is a list of 1-based topic indices from booklets/src/<grade>/chN.html.
Topics that were added beyond the book (career extras, over-split pages) are
either merged into the matching textbook lecture or omitted.
"""

from __future__ import annotations

# (title, golden, topic_indices)
Lecture = tuple[str, bool, list[int]]

XI: dict[int, list[Lecture]] = {
    1: [
        ("1.1.1 & 1.1.2 Discrete vs Continuous & Digital Systems", False, [1, 2]),
        ("1.1.3 Analog and Digital Signals", True, [3]),
        ("1.1.4 – 1.1.6 Boolean Algebra, Operations & Truth Tables", False, [4, 5, 6]),
        ("1.1.7 Basic Logic Gates (AND, OR, NOT)", True, [7]),
        ("1.1.7 Universal & Advanced Logic Gates", False, [8, 9]),
        ("1.1.8 – 1.1.11 Logic Expressions, Minterms & Diagrams", True, [10, 11]),
        ("1.1.13 Karnaugh Maps (K-Maps) Simplification", True, [12]),
        ("LogiSim Simulation Tool Guide", False, [13, 14]),
        ("1.2.1 – 1.2.3 Software Development Life Cycle (SDLC)", True, [15]),
        ("1.2.4 – 1.2.7 Waterfall vs Agile Models & Case Studies", True, [16, 17, 18]),
        ("1.3.1 – 1.3.4 Communication Models & OSI 7-Layer Model", True, [19]),
        ("1.3.5 – 1.3.6 TCP/IP Model vs OSI Model", False, [20]),
    ],
    2: [
        ("2.1 & 2.2 Introduction to CT & Algorithms", True, [1, 2]),
        ("2.2.2 Algorithm vs Pseudocode", True, [3]),
        ("2.3.1 Algorithmic Strategy: Decomposition", True, [4]),
        ("2.3.2 Algorithmic Strategy: Pattern Recognition", False, [5]),
        ("2.3.3 Algorithmic Strategy: Abstraction", False, [6]),
        ("2.4.1 Sorting Algorithms: Bubble Sort", True, [7, 8]),
        ("2.4.1 Sorting Algorithms: Selection Sort", True, [9]),
        ("2.4.2 Searching Algorithms: Linear Search", False, [10]),
        ("2.4.2 Searching Algorithms: Binary Search", True, [11]),
        ("2.5 Evaluation Criteria of Algorithm", False, [12]),
        ("2.6 How to Decide Which Algorithm to Use", False, [13]),
    ],
    3: [
        ("3.1 Programming & Language Types", False, [1, 2]),
        ("3.2 Career Growth with Python", False, [3]),
        ("3.3 Integrated Development Environment (IDE) & VS Code", False, [4, 5]),
        ("3.4 Fundamentals of Python Programming", True, [6]),
        ("3.4.1 Variables and Data Types", True, [7, 8]),
        ("3.4.2 Input Output Handling", False, [9]),
        ("3.4.3 Operators and Operands (Arithmetic, Relational, Bitwise)", True, [10, 11, 12]),
        ("3.5 Control Structures Overview", True, [13]),
        ("3.5.1 Sequence", False, [14]),
        ("3.5.2 Selection Statements (if, if-else, if-elif-else, nested)", True, [15, 16]),
        ("3.5.3 Repetition Statements (for loop, while loop)", True, [17, 18, 19, 20]),
        ("3.6 Libraries in Python (Built-in & Third-Party)", False, [21, 22, 23]),
        ("3.7 Debugging Code in Python", False, [24]),
    ],
    4: [
        ("4.1.1 Data, Information and Database", False, [1]),
        ("4.1.2 Database Management System (DBMS)", False, [2]),
        ("4.2 Database Components (Tables, Records, Fields)", False, [3]),
        ("4.3.1 Keys and Integrity Constraints", True, [4]),
        ("4.3 Relational Database Management System (RDBMS)", False, [5]),
        ("4.4 Entity Relationship Model (ER-Model)", True, [6]),
        ("4.5 Referential Integrity (Cascade Update & Delete)", True, [7]),
        ("4.6 Relational Schema Development", False, [8]),
        ("4.7 Case Study — Library Management System", False, [9]),
        ("4.8 Different Database Objects (Tables, Forms, Queries, Reports)", False, [10]),
        ("4.9 Creation of Tables in Microsoft Access", False, [11]),
        ("4.10 Designing Forms for Data Manipulation", False, [12]),
        ("4.11 Creating Queries in MS Access", True, [13]),
        ("4.11.4 Data Summarization & Statistical Analysis", False, [14]),
        ("4.11.6 Data Visualization in MS Access (Charts)", False, [15]),
    ],
    5: [
        ("5.1 Introduction to Computing Impacts", False, [1]),
        ("5.1.1 Artificial Intelligence (AI)", True, [2]),
        ("5.1.2 Internet of Things (IoT) & Components", True, [3]),
        ("5.1.3 Data Analytics & Components", False, [4]),
        ("Table: IoT vs AI vs Data Analytics Comparison", False, [5]),
        ("5.2 Uses of IoT in Different Areas", False, [6]),
        ("5.2.1 Scope of AI in Education in Pakistan", False, [7]),
        # original topic 8 (Career Connection in IoT and AI) is extra — dropped
        ("5.3 Information Sources (Primary, Secondary, Tertiary)", True, [9]),
        ("5.4 Impacts of Computing in Various Fields", False, [10]),
        ("5.5 Assistive Technologies", True, [11]),
        ("5.5.1 Importance of Assistive Technologies", False, [12]),
        ("5.5.2 Career Connection in Assistive Tech", False, [13]),
    ],
    6: [
        ("6.1 & 6.2 Introduction to Digital Literacy", False, [1, 2]),
        ("6.3 Types of Data (Qualitative vs Quantitative)", True, [3]),
        ("6.4 Data-Collection Strategies", True, [4]),
        ("6.4.1 – 6.4.2 Interviews and Surveys", True, [5]),
        ("6.4.3 – 6.4.5 Prototypes, Observation, and Simulations", True, [6]),
        ("6.5 Primary and Secondary Data", True, [7]),
        ("6.6 Designing a Data-Collection Approach", False, [8]),
        ("6.7 Presenting Data Using Digital Tools", False, [9]),
        ("6.7.1 – 6.7.4 Spreadsheets, Presentations, Infographics, Reports", False, [10]),
        ("6.8 Case Study: Digital Inquiry Project", True, [11]),
        ("Step 1 – 3: Advanced Search & Methodology", True, [12]),
        ("Step 4 – 6: Survey Prep & Primary Data Collection", True, [13]),
        ("Step 7 – 9: Secondary Data & Spreadsheet Organization", True, [14]),
        ("Step 10 – 12: Data Analysis, Conclusion & Artefact", True, [15, 16]),
        # original topic 17 (Careers in Digital Research) is extra — dropped
    ],
}

XII: dict[int, list[Lecture]] = {
    1: [
        ("1.1 Fundamentals of Human Computer Interaction (HCI)", False, [1]),
        ("1.1.1 – 1.1.2 Traditional vs Natural Interaction", False, [2]),
        ("1.2 Applications of HCI (Domains of Life)", True, [3]),
        ("1.3 Components of HCI", False, [4]),
        ("1.3 Types of User Interaction", False, [5]),
        ("1.3 Interface Types, Environment & Feedback", False, [6]),
        ("1.4 Importance of HCI", True, [7]),
        ("1.5 Accessibility Principles", False, [8]),
        ("1.6 Need Analysis for Interface Design", False, [9]),
        ("1.7 Human Computer Interaction Problems", True, [10]),
        ("1.8 Methods for Improving HCI", False, [11]),
        ("1.9 User Interface Design (UI vs UX)", True, [12]),
        ("1.9.3 – 1.9.5 Wireframing, Figma, and Prototypes", False, [13]),
        ("1.11 Test and Evaluate HCI (Evaluation Methods)", False, [14]),
        ("1.11.2 Testing Methods (Usability, A/B, Automated)", True, [15]),
        # original topic 16 (Career Opportunities in UI/UX) is extra — dropped
    ],
    2: [
        ("2.1 Analyze algorithms for correctness", False, [1]),
        ("2.1.1 – 2.1.3 Trace Tables vs Stepwise Reasoning", True, [2, 3, 4]),
        ("2.2 Evaluating the Clarity of an Algorithm", False, [5]),
        ("2.2.1 – 2.2.2 Modularity and Readability", False, [6, 7]),
        ("2.3 Assess Algorithm Efficiency", True, [8]),
        ("2.3.1 Number of Steps (Big O Notation)", True, [9]),
        ("2.3.2 Number of Conditions", False, [10]),
        ("2.3.3 Number of Repetitions", False, [11]),
        ("2.3.4 The Efficiency Evaluation Framework", False, [12]),
        ("2.4 Refinements to improve clarity and efficiency", False, [13]),
        ("2.5 Concept of Data Structure", True, [14]),
        ("2.5.1 Linear Data Structures (Array, Linked List, Stack, Queue)", True, [15, 16, 17, 18]),
        ("2.5.2 Non-Linear Data Structures (Tree, Graph)", False, [19, 20]),
        ("2.5.3 Operations on Data Structures", False, [21]),
        ("2.6 Identify data structures in problem scenarios", False, [22]),
        ("2.7 Trace data retrieval in Array, List and Queue", False, [23]),
        # original topic 24 career extra — dropped
    ],
    3: [
        ("3.1 Data Structures in Python", False, [1]),
        ("3.1.1 Lists (Ordered, Mutable, Methods)", True, [2]),
        ("3.1.2 Tuples (Ordered, Immutable)", True, [3]),
        ("3.1.3 Sets (Unordered, Unique, Math Operations)", False, [4]),
        ("3.1.4 Dictionaries (Key-Value pairs)", True, [5]),
        ("3.1.5 Common Built-in Functions (min, max, len, sum)", False, [6]),
        ("3.1.6 Activity: Students Attendance Program", False, [7]),
        ("3.1.7 Activity: Word Frequency Counter", False, [8]),
        ("3.2 Functions in Python", True, [9]),
        ("3.2.1 Types of Functions (Built-in vs User-defined)", False, [10]),
        ("3.2.2 Functions with Return Values", False, [11]),
        ("3.2.3 Activity: Arithmetic Calculator Using Functions", False, [12]),
        ("3.2.4 Scope of Local and Global Variables", False, [13]),
        ("3.3 & 3.4 File Handling and Operations (Modes r, w, a)", True, [14]),
        ("3.6 with Statement (Context Manager)", True, [15]),
        ("3.8 Errors and Exceptions (Try-Except)", False, [16]),
        ("3.9 Mini File Handling Project: Grade Tracker", False, [17]),
        # original topic 18 career extra — dropped
    ],
    4: [
        ("4.1 Concept of Data Analysis", False, [1]),
        ("4.1.1 – 4.1.2 Data Sources and Database Connection", True, [2]),
        ("4.2 Creating a SQLite Database in Python", False, [3]),
        ("4.3 Basic Operations on Data using Pandas", True, [4]),
        ("4.3.3 Handling Missing Values (NaN)", True, [5]),
        ("4.4 Data Organization and Representation", False, [6]),
        ("4.5 Data Visualization & Types of Graphs", True, [7]),
        ("4.6 Descriptive Statistics", True, [8]),
        # original topic 9 career extra — dropped
    ],
    5: [
        ("5.1 Machine Learning, Neural Networks & Deep Learning", False, [1]),
        ("5.1.1 Machine Learning (ML)", False, [2]),
        ("5.1.2 Neural Networks (NN)", True, [3]),
        ("5.1.3 Deep Learning (DL)", False, [4]),
        ("5.1.4 Components of Neural Networks", True, [5]),
        ("5.1.5 Components of Deep Learning", False, [6]),
        ("5.2 Applications of Neural Networks and Deep Learning", False, [7, 8]),
        ("5.3 Secure Collaboration (Authentication, Access Control)", True, [9]),
        ("5.3.2 Data Protection (Encryption, Passwords, Backup, Firewall)", False, [10]),
        ("5.4 Security Threats and Mitigation Techniques", True, [11]),
        ("5.4.2 Identify Security Threats", False, [12]),
        ("5.4.3 Apply Mitigation Techniques", False, [13]),
        ("5.5 Equity and Equal Access in Digital Collaboration", False, [14]),
        ("5.5.1 Functions of Equity and Equal Access", True, [15]),
        ("5.5.2 Collaboration Tools", False, [16]),
        # original topic 17 career extra — dropped
    ],
    6: [
        ("6.1 Entrepreneur and Entrepreneurship", False, [1]),
        ("6.2 Entrepreneurship in the Digital Age", True, [2]),
        ("Table 6.1 Local examples of digital entrepreneurship", False, [3]),
        ("6.3 From Problem to Business Idea", False, [4]),
        ("6.4 Prototype", True, [5]),
        ("6.5 Types of Prototypes (Low, Mid, High-Fidelity)", False, [6]),
        ("6.6 Prototype Development Cycle (Design, Build, Test, Iterate)", True, [7]),
        ("6.7 Class Activity: Create a Prototype", False, [8]),
        ("6.8 Minimum Viable Product (MVP)", True, [9]),
        ("6.9 Difference between Prototype and MVP", False, [10]),
        ("6.10 Identifying the Riskiest Assumption", False, [11]),
        ("6.11 Developing an MVP", False, [12]),
        ("6.12 Case Study: MVP for a Canteen Pre-Order System", False, [13]),
        ("6.13 Testing an MVP", False, [14]),
        ("6.14 Beachhead Market", True, [15]),
        ("6.15 & 6.16 Complete Student Project & Ethical Use", False, [16, 17]),
        # original topic 18 career extra — dropped
    ],
}

MAP = {"xi": XI, "xii": XII}


def lectures_for(grade: str, chapter: int) -> list[Lecture]:
    return MAP[grade][chapter]
