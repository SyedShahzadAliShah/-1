#!/usr/bin/env python3
"""Build the Teach Yourself Sketchnotes course from the CS XI and XII lecture PDFs.

English lesson text is taken from the PDF text layer. Urdu teaching lines are
Urdish (Urdu with the English technical terms students say in class). Original
pages are saved as JPEG plates so the Nastaliq sketchnote stays available.
"""

from __future__ import annotations

import json
import os
import re
import sys

import pymupdf

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT_DIR = os.path.join(ROOT, "teach", "src", "main", "assets", "www")
PLATE_DIR = os.path.join(OUT_DIR, "plates")

XI_PDF = os.environ.get(
    "XI_PDF",
    "/home/ubuntu/.cursor/projects/workspace/uploads/XI-compressed_e76f.pdf",
)
XII_PDF = os.environ.get(
    "XII_PDF",
    "/home/ubuntu/.cursor/projects/workspace/uploads/XII-compressed_9505.pdf",
)

ARABIC = re.compile(r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]")
PAGE_NO = re.compile(r"^Page\s+\d+$", re.I)
SECTION_NO = re.compile(r"^(?:\d+\.)+\d+\s+")
SIMPLE_NO = re.compile(r"^\d+\.\s+")

CALLOUT_RE = re.compile(
    r"(analogy|real-?\s*life|class discussion|activity|remember|exam tip|teacher tip|note\b|worked example)",
    re.I,
)

DIAGRAM_RULES = [
    ("kmap3", ["three-variable k-map", "k-map (a, b, c)"]),
    ("kmap", ["karnaugh", "k-map", "k-maps"]),
    ("gates-xor", ["xor", "xnor"]),
    ("gates-universal", ["nand", "nor", "universal logic"]),
    ("gates-basic", ["logic gates", "basic gates"]),
    ("logic-diagram", ["logic diagram"]),
    ("waves", ["analog and digital signal"]),
    ("stairs-ramp", ["discrete and continuous"]),
    ("truth", ["truth table"]),
    ("boolean", ["boolean algebra", "boolean operation"]),
    ("osi", ["osi"]),
    ("tcpip", ["tcp/ip", "tcpip"]),
    ("waterfall", ["waterfall"]),
    ("agile", ["agile"]),
    ("sdlc", ["software development life cycle", "sdlc"]),
    ("bubble", ["bubble sort"]),
    ("selection", ["selection sort"]),
    ("binary-search", ["binary search"]),
    ("linear-search", ["linear search"]),
    ("bigo", ["big o", "algorithm efficiency", "number of repetitions"]),
    ("pseudocode", ["pseudocode", "algorithm vs"]),
    ("stack", ["stack"]),
    ("queue", ["queue"]),
    ("linked", ["linked list"]),
    ("tree", ["tree"]),
    ("graph-ds", ["non-linear data structures: graph", "data structures: graph"]),
    ("array", ["data structures: array", ": array", "linear data structures: array"]),
    ("neural", ["neural network", "deep learning"]),
    ("hci-senses", ["human computer", "sensory", "traditional vs natural"]),
    ("hci-domains", ["applications of hci"]),
    ("er", ["er-model", "entity relationship", "types of relationships"]),
    ("keys", ["keys and integrity", "referential integrity"]),
    ("pie", ["pie chart"]),
    ("hist", ["histogram"]),
    ("scatter", ["scatter"]),
    ("box", ["box plot"]),
    ("linegraph", ["line graph"]),
    ("flowchart", ["flowchart"]),
    ("prototype", ["prototype"]),
    ("mvp", ["minimum viable", "mvp"]),
    ("pandas", ["pandas", "dataframe"]),
    ("missing", ["missing value"]),
    ("spread", ["measures of spread", "central tendency", "descriptive statistics"]),
    ("iot", ["internet of things", "iot"]),
    ("loop", ["repetition", "loop"]),
    ("selection-stmt", ["selection statement"]),
    ("variable", ["variable"]),
    ("bitwise", ["bitwise"]),
    ("file", ["file handling", "with statement"]),
    ("function", ["functions in python", "function components"]),
    ("security", ["security threat", "data protection", "secure collaboration"]),
    ("equity", ["equity", "equal access"]),
    ("beachhead", ["beachhead"]),
    ("entrepreneur", ["entrepreneur"]),
]

TITLE_UR = {
    "Discrete and Continuous Quantities": "مجرد اور مسلسل مقداریں",
    "Introduction to Digital Systems": "ڈیجیٹل سسٹمز کا تعارف",
    "Analog and Digital Signals": "اینالاگ اور ڈیجیٹل سگنلز",
    "Boolean Algebra": "بولین الجبرا",
    "Boolean Operations (Continued)": "بولین آپریشنز، آگے",
    "Truth Tables": "ٹروتھ ٹیبل",
    "Logic Gates (Basic Gates)": "بنیادی لاجک گیٹس",
    "Universal Logic Gates (NAND & NOR)": "یونیورسل گیٹس: NAND اور NOR",
    "Advanced Logic Gates (XOR & XNOR)": "اعلیٰ گیٹس: XOR اور XNOR",
    "Expressions & Minterms": "ایکسپریشنز اور منٹرمز",
    "Logic Diagrams": "لاجک ڈایاگرام",
    "Karnaugh Maps (K-Maps)": "کارنو نقشے، K-Maps",
    "Three-Variable K-Map (A, B, C)": "تین متغیر کا K-Map",
    "LogiSim Evolution: Simulation Tool": "LogiSim سمیولیشن ٹول",
    "Building a Circuit in LogiSim": "LogiSim میں سرکٹ بنانا",
    "Software Development Life Cycle": "سافٹ ویئر ڈیولپمنٹ لائف سائیکل",
    "Detailed SDLC Phases (1-3)": "SDLC کے مراحل ایک سے تین",
    "Detailed SDLC Phases (4-6)": "SDLC کے مراحل چار سے چھ",
    "The Waterfall Model": "واٹر فال ماڈل",
    "The Agile Model": "ایجائل ماڈل",
    "Waterfall vs Agile Comparison": "واٹر فال اور ایجائل کا موازنہ",
    "Communication Models (OSI)": "مواصلاتی ماڈل، OSI",
    "OSI Model Layers (Top Layers)": "OSI کے اوپری لیئرز",
    "OSI Bottom Layers & TCP/IP Model": "OSI کے نچلے لیئرز اور TCP/IP",
    "Computational Thinking": "کمپیوٹیشنل تھنکنگ",
    "Algorithm vs Pseudocode": "الگورتھم اور سوڈو کوڈ",
    "Algorithmic Strategies for Problem Solving": "مسئلہ حل کرنے کی حکمتِ عملی",
    "Pattern Recognition": "پیٹرن کی پہچان",
    "Abstraction": "ایبسٹریکشن",
    "Sorting and Searching Algorithms": "ترتیب اور تلاش کے الگورتھم",
    "Bubble Sort Example": "ببل سارٹ کی مثال",
    "Selection Sort": "سیلیکشن سارٹ",
    "Selection Sort Example": "سیلیکشن سارٹ کی مثال",
    "Linear Search": "لکیری تلاش",
    "Linear Search Example": "لکیری تلاش کی مثال",
    "Binary Search": "بائنری تلاش",
    "Binary Search Example": "بائنری تلاش کی مثال",
    "Evaluation Criteria of Algorithm": "الگورتھم جانچنے کے پیمانے",
    "How to Decide Which Algorithm to Use": "کون سا الگورتھم چنیں",
    "Programming": "پروگرامنگ",
    "Common High-Level Languages": "مشہور ہائی لیول زبانیں",
    "Integrated Development Environment (IDE)": "انٹیگریٹڈ ڈیولپمنٹ انوائرنمنٹ",
    "VS Code Interface Elements": "VS Code کے حصے",
    "Fundamentals of Python Programming": "پائتھن کے بنیادی اصول",
    "Variables": "ویری ایبلز",
    "Data Types in Python": "پائتھن میں ڈیٹا کی اقسام",
    "Input and Output Handling": "ان پٹ اور آؤٹ پٹ",
    "Operators and Operands": "آپریٹرز اور آپریئنڈز",
    "Other Important Operators": "مزید اہم آپریٹرز",
    "Bitwise Operators": "بٹ وائز آپریٹرز",
    "Bitwise Operators (Continued)": "بٹ وائز آپریٹرز، آگے",
    "Control Structures": "کنٹرول سٹرکچرز",
    "Selection Statements": "سلیکشن سٹیٹمنٹس",
    "Selection Statements (Continued)": "سلیکشن سٹیٹمنٹس، آگے",
    "Repetition Statements (Loops)": "دہرانے والے بیانات، لوپس",
    "Repetition Statements (Continued)": "لوپس، آگے",
    "Nested Loops & Comparison": "نیسٹڈ لوپس اور موازنہ",
    "Practical Activity: Shopping Bill Calculator": "عملی کام: خریداری کا بل",
    "Libraries in Python": "پائتھن کی لائبریریز",
    "Built-in Libraries": "بلٹ اِن لائبریریز",
    "Third-Party Libraries": "تھرڈ پارٹی لائبریریز",
    "Types of Errors (Bugs)": "غلطیوں کی اقسام",
    "Reading Error Messages (Tracebacks)": "ایرر میسج اور ٹریس بیک پڑھنا",
    "Concepts of Database and Elements": "ڈیٹا بیس کے تصورات",
    "Database and DBMS": "ڈیٹا بیس اور DBMS",
    "Database Components": "ڈیٹا بیس کے اجزاء",
    "Keys and Integrity Constraints": "کیز اور سالمیت کی شرائط",
    "Keys (Continued) & RDBMS": "کیز اور ریلیشنل DBMS",
    "Entity Relationship Model (ER-Model)": "اینٹیٹی ریلیشن شپ ماڈل",
    "Types of Relationships in ER Model": "ER ماڈل میں تعلق کی اقسام",
    "Referential Integrity": "ریفرنشل انٹیگریٹی",
    "Referential Integrity Operations": "ریفرنشل انٹیگریٹی کے عمل",
    "Relational Schema Development": "ریلیشنل سکیما بنانا",
    "Case Study: Library Management System": "کیس سٹڈی: لائبریری سسٹم",
    "Library Case Study (Continued)": "لائبریری کیس سٹڈی، آگے",
    "Library Case Study (Final ER Schema)": "لائبریری کا آخری ER سکیما",
    "Different Database Objects": "ڈیٹا بیس آبجیکٹس",
    "Database Objects (Continued)": "ڈیٹا بیس آبجیکٹس، آگے",
    "Creation of Tables in MS Access": "MS Access میں ٹیبل بنانا",
    "Table Creation (Design View)": "ڈیزائن ویو میں ٹیبل",
    "Designing Forms": "فارمز ڈیزائن کرنا",
    "Creating Queries in MS Access": "MS Access میں کوئری بنانا",
    "Filtering Query Data": "کوئری ڈیٹا فلٹر کرنا",
    "Data Summarization & Statistics": "ڈیٹا کا خلاصہ اور اعدادوشمار",
    "Data Visualization (Charts)": "ڈیٹا کو چارٹ میں دکھانا",
    "Data Visualization (Continued)": "ڈیٹا ویژولائزیشن، آگے",
    "Introduction to Computing": "کمپیوٹنگ کا تعارف",
    "Internet of Things (IoT)": "انٹرنیٹ آف تھنگز",
    "IoT Components (Continued)": "IoT کے اجزاء، آگے",
    "Data Analytics": "ڈیٹا اینالیٹکس",
    "Data Analytics (Continued)": "ڈیٹا اینالیٹکس، آگے",
    "Uses of IoT in Different Areas": "مختلف شعبوں میں IoT",
    "Uses of IoT (Continued)": "IoT کے استعمال، آگے",
    "AI in Education in Pakistan": "پاکستان میں تعلیم اور AI",
    "Information Sources": "معلومات کے ذرائع",
    "Information Sources (Continued)": "معلومات کے ذرائع، آگے",
    "Impacts of Computing in Various Fields": "مختلف شعبوں پر کمپیوٹنگ کے اثرات",
    "Assistive Technologies": "امدادی ٹیکنالوجی",
    "Assistive Tech Importance & Careers": "امدادی ٹیکنالوجی اور کیریئر",
    "Introduction to Digital Literacy": "ڈیجیٹل خواندگی کا تعارف",
    "Types of Data": "ڈیٹا کی اقسام",
    "Data-Collection Strategies": "ڈیٹا جمع کرنے کی حکمتِ عملی",
    "Data-Collection Strategies (Continued)": "ڈیٹا جمع کرنا، آگے",
    "Primary and Secondary Data": "پرائمری اور سیکنڈری ڈیٹا",
    "Primary vs Secondary & Approach Design": "پرائمری بمقابلہ سیکنڈری",
    "Presenting Data Using Digital Tools": "ڈیجیٹل ٹولز سے ڈیٹا پیش کرنا",
    "Presenting Data (Continued)": "ڈیٹا پیش کرنا، آگے",
    "Case Study: Digital Inquiry Project": "کیس سٹڈی: ڈیجیٹل انکوائری",
    "Methodology (Steps 1 to 3)": "طریقہ کار، قدم ایک سے تین",
    "Methodology (Steps 4 to 6)": "طریقہ کار، قدم چار سے چھ",
    "Methodology (Steps 7 to 9)": "طریقہ کار، قدم سات سے نو",
    "Analysis and Conclusion (Steps 10-12)": "تجزیہ اور نتیجہ، قدم دس سے بارہ",
    "The Final Digital Artefact": "آخری ڈیجیٹل آرٹیفیکٹ",
    "Careers & Summary": "کیریئر اور خلاصہ",
    "Fundamentals of Human Computer": "ہیومن کمپیوٹر انٹریکشن کی بنیاد",
    "Traditional vs Natural Interaction": "روایتی اور قدرتی تعامل",
    "Applications of HCI": "HCI کے استعمال",
    "Components of HCI": "HCI کے اجزاء",
    "Types of User Interaction": "صارف کے تعامل کی اقسام",
    "Types of User Interaction (Continued)": "تعامل کی اقسام، آگے",
    "Interfaces, Environment & Feedback": "انٹرفیس، ماحول اور فیڈبیک",
    "Importance of HCI": "HCI کی اہمیت",
    "Accessibility Principles": "رسائی کے اصول",
    "Need Analysis for Interface Design": "انٹرفیس کے لیے ضرورت کا تجزیہ",
    "Human Computer Interaction Problems": "HCI کے مسائل",
    "HCI Problems & 1.8 Improving HCI": "HCI کے مسائل اور بہتری",
    "User Interface Design (UI)": "یوزر انٹرفیس ڈیزائن",
    "Wireframing": "وائر فریم بنانا",
    "Figma & 1.9.5 Prototypes": "Figma اور پروٹوٹائپ",
    "Test and Evaluate HCI": "HCI کی جانچ اور تشخیص",
    "Testing Methods": "جانچ کے طریقے",
    "Testing Methods (Continued)": "جانچ کے طریقے، آگے",
    "Analyze algorithms for correctness": "الگورتھم کی درستگی جانچنا",
    "Trace Table Example": "ٹریس ٹیبل کی مثال",
    "Stepwise Reasoning": "قدم بہ قدم استدلال",
    "Comparing the Trace Table & Stepwise": "ٹریس ٹیبل اور قدم بہ قدم موازنہ",
    "Evaluating the Clarity of an Algorithm": "الگورتھم کی وضاحت جانچنا",
    "Modularity Example: Average of an Array": "ماڈیولرٹی: ارے کی اوسط",
    "Readability": "پڑھنے میں آسانی",
    "Assess Algorithm Efficiency": "الگورتھم کی کارکردگی",
    "Big O Notation (Continued)": "بگ او نوٹیشن، آگے",
    "Number of Repetitions": "دہرائے جانے کی تعداد",
    "Refinements to improve clarity": "وضاحت بڑھانے والی اصلاح",
    "Refinements to improve Efficiency": "کارکردگی بڑھانے والی اصلاح",
    "Concept of Data Structure": "ڈیٹا سٹرکچر کا تصور",
    "Linear Data Structures: Array": "لکیری ڈھانچہ: ارے",
    "Linear Data Structures: Linked List": "لکیری ڈھانچہ: لنکڈ لسٹ",
    "Linear Data Structures: Stack": "لکیری ڈھانچہ: اسٹیک",
    "Linear Data Structures: Queue": "لکیری ڈھانچہ: قطار",
    "Non-Linear Data Structures: Tree": "غیر لکیری ڈھانچہ: ٹری",
    "Non-Linear Data Structures: Graph": "غیر لکیری ڈھانچہ: گراف",
    "Identify data structures in problem scenarios": "مسئلے میں درست ڈھانچہ چننا",
    "Non-Linear Scenarios & Decision Guide": "غیر لکیری صورتحال اور فیصلہ",
    "Trace data retrieval in Array, List and Queue": "ارے، لسٹ اور قطار میں تلاش",
    "Retrieval in Queue & Careers": "قطار سے حصول اور کیریئر",
    "Summary of Chapter 2": "باب دو کا خلاصہ",
    "Data Structures in Python": "پائتھن میں ڈیٹا سٹرکچرز",
    "List Indexing (Positive & Negative)": "لسٹ انڈیکسنگ",
    "List Slicing and Traversal": "لسٹ سلائسنگ اور ٹراورسل",
    "Built-in List Methods & Advantages": "لسٹ کے بلٹ اِن میتھڈز",
    "Activity: Searching an Element in a List": "سرگرمی: لسٹ میں تلاش",
    "Tuples (Immutable Structure)": "ٹیوپل، ناقابلِ تبدیلی ڈھانچہ",
    "Tuple Immutability & Methods": "ٹیوپل کی مستقل مزاجی",
    "Sets (Unique & Unordered)": "سیٹ، منفرد اور بے ترتیب",
    "Mathematical Operations with Sets": "سیٹوں کے ریاضیاتی عمل",
    "Set Traversal & 3.1.4 Dictionaries": "سیٹ ٹراورسل اور ڈکشنری",
    "Dictionary Operations (Mutable & Duplicates)": "ڈکشنری کے عمل",
    "Accessing Dictionary Elements Safely": "ڈکشنری سے محفوظ رسائی",
    "Dictionary Views & Traversal": "ڈکشنری ویوز اور ٹراورسل",
    "Common Built-in Functions": "عام بلٹ اِن فنکشنز",
    "Activity: Student Attendance System": "سرگرمی: حاضری کا نظام",
    "Activity: Word Frequency Counter": "سرگرمی: لفظ کی گنتی",
    "Functions in Python": "پائتھن میں فنکشنز",
    "Function Components & Types": "فنکشن کے اجزاء اور اقسام",
    "Functions with Return Values": "واپسی والی فنکشنز",
    "Scope of Local and Global Variables": "لوکل اور گلوبل ویری ایبل کی حد",
    "File Handling Overview": "فائل ہینڈلنگ کا جائزہ",
    "File Methods & Writing Data": "فائل میتھڈز اور لکھنا",
    "with Statement & Reading Files": "with بیان اور فائل پڑھنا",
    "Errors and Exceptions (Try-Except)": "ایرر اور ایکسپشن، try-except",
    "Mini File Handling Project: Grade Tracker": "منی پروجیکٹ: گریڈ ٹریکر",
    "Concept of Data Analysis": "ڈیٹا اینالسس کا تصور",
    "Data Sources & 4.1.2 Connectivity": "ڈیٹا کے ذرائع اور کنیکٹیوٹی",
    "Flowchart of Python Connecting to Database": "پائتھن سے ڈیٹا بیس کا فلو چارٹ",
    "Creating a SQLite Database in Python": "پائتھن میں SQLite ڈیٹا بیس",
    "Creating a SQLite Database (Continued)": "SQLite ڈیٹا بیس، آگے",
    "Basic Operations on Data using Pandas": "Pandas سے بنیادی عمل",
    "DataFrames (Syntax and Creation)": "ڈیٹا فریم بنانا",
    "Creating and Loading Data (Files)": "فائل سے ڈیٹا لادنا",
    "Creating New Variables (Data Manipulation)": "نئے متغیر اور ڈیٹا میں ردوبدل",
    "Handling Missing Values": "خالی قدروں کا علاج",
    "Handling Missing Values (Continued)": "خالی قدریں، آگے",
    "Data Organization and Representation": "ڈیٹا کی ترتیب اور پیشکش",
    "Graphical Representation": "تصویری پیشکش",
    "Types of Graphs": "گراف کی اقسام",
    "Line Graphs": "لائن گراف",
    "Pie Charts": "پائی چارٹ",
    "Histograms": "ہسٹوگرام",
    "Scatter Plots": "اسکیٹر پلاٹ",
    "Box Plots": "باکس پلاٹ",
    "Descriptive Statistics": "وضاحتی اعدادوشمار",
    "Measures of Central Tendency (Continued)": "مرکزی رجحان کے پیمانے",
    "Measures of Spread (Dispersion)": "پھیلاؤ کے پیمانے",
    "Measures of Spread (Continued)": "پھیلاؤ کے پیمانے، آگے",
    "Career Opportunities": "کیریئر کے مواقع",
    "Summary of Chapter 4": "باب چار کا خلاصہ",
    "Machine Learning, Neural Networks and Deep": "مشین لرننگ، نیورل نیٹ ورک اور ڈیپ لرننگ",
    "Neural Networks": "نیورل نیٹ ورکس",
    "Deep Learning": "ڈیپ لرننگ",
    "Components of Neural Networks": "نیورل نیٹ ورک کے اجزاء",
    "Components of Deep Learning": "ڈیپ لرننگ کے اجزاء",
    "Future of AI, NN, and DL in Pakistan": "پاکستان میں AI، NN اور DL کا مستقبل",
    "Applications of Neural Networks & Deep": "نیورل نیٹ ورکس کے استعمال",
    "Applications (Continued)": "استعمال، آگے",
    "Secure Collaboration and Data Protection": "محفوظ اشتراک اور ڈیٹا کا تحفظ",
    "Secure Collaboration (Continued)": "محفوظ اشتراک، آگے",
    "Data Protection": "ڈیٹا کا تحفظ",
    "Security Threats and Mitigation": "سیکیورٹی خطرات اور بچاؤ",
    "Security Threats (Continued)": "سیکیورٹی خطرات، آگے",
    "Identifying Security Threats": "خطروں کی پہچان",
    "Apply Mitigation Techniques": "بچاؤ کے طریقے لگائیں",
    "Equity and Equal Access in Collaboration": "اشتراک میں انصاف اور برابر رسائی",
    "Collaboration Tools": "اشتراک کے ٹولز",
    "Summary of Chapter 5": "باب پانچ کا خلاصہ",
    "Entrepreneur & Entrepreneurship": "کاروباری شخص اور کاروباری سوچ",
    "Entrepreneurship in the Digital Age": "ڈیجیٹل دور میں کاروبار",
    "Local Examples of Digital Entrepreneurship": "ڈیجیٹل کاروبار کی مقامی مثالیں",
    "From Problem to Business Idea": "مسئلے سے کاروباری خیال تک",
    "From Problem to Business Idea (Continued)": "کاروباری خیال، آگے",
    "Prototype": "پروٹوٹائپ",
    "Types of Prototypes": "پروٹوٹائپ کی اقسام",
    "Comparison of Prototype Types": "پروٹوٹائپ اقسام کا موازنہ",
    "Prototype Development Cycle": "پروٹوٹائپ کا دائرہ",
    "Class Activity: Create a Prototype": "کلاس سرگرمی: پروٹوٹائپ بنائیں",
    "Class Activity (Continued)": "کلاس سرگرمی، آگے",
    "Minimum Viable Product (MVP)": "کم از کم قابلِ استعمال مصنوعہ",
    "Difference between Prototype and MVP": "پروٹوٹائپ اور MVP کا فرق",
    "Identifying the Riskiest Assumption": "سب سے خطرناک مفروضہ",
    "Developing an MVP": "MVP بنانا",
    "Case Study: MVP for a Canteen": "کیس سٹڈی: کینٹین کا MVP",
    "Testing an MVP": "MVP کی جانچ",
    "Beachhead Market": "بیچ ہیڈ مارکیٹ",
    "Complete Student Project": "مکمل طلبہ پروجیکٹ",
    "Project Rubric & Ethical Use": "پروجیکٹ روبرک اور اخلاقی استعمال",
    "Summary of Chapter 6": "باب چھ کا خلاصہ",
}

BLURBS = {
    "Analog and Digital Signals": "اینالاگ سگنل ہموار بدلتا ہے، جیسے آواز۔ ڈیجیٹل سگنل صرف HIGH یعنی 1 اور LOW یعنی 0 ہوتا ہے، اس لیے noise اسے کم خراب کرتا ہے۔",
    "Logic Gates (Basic Gates)": "AND تب 1 دیتا ہے جب سارے inputs 1 ہوں۔ OR تب 1 دیتا ہے جب کوئی ایک input 1 ہو۔ NOT input کو الٹ دیتا ہے۔",
    "Logic Diagrams": "لاجک ڈایاگرام گیٹس کو تاروں سے جوڑتا ہے۔ بائیں طرف inputs جائیں اور دائیں طرف output نکلیں۔",
    "Karnaugh Maps (K-Maps)": "K-Map بولین اظہار کو سادہ بناتا ہے۔ پڑوسی خانے صرف ایک bit میں بدلتے ہیں، اور گروپ ایک، دو، چار یا آٹھ کا ہوتا ہے۔",
    "Software Development Life Cycle": "SDLC کے مراحل ہیں: منصوبہ، تجزیہ، ڈیزائن، تعمیر، جانچ، اور دیکھ بھال۔",
    "The Waterfall Model": "واٹر فال میں ہر مرحلہ ختم ہو کر اگلا شروع ہوتا ہے۔ جب ضرورتیں شروع سے واضح ہوں تب یہ ٹھیک رہتا ہے۔",
    "The Agile Model": "ایجائل چھوٹے چکر یعنی sprints میں کام کرتا ہے۔ صارف کی رائے جلدی آتی ہے اور تبدیلی ممکن رہتی ہے۔",
    "Communication Models (OSI)": "OSI کے سات لیئر ہیں: Application، Presentation، Session، Transport، Network، Data Link، اور Physical۔",
    "Computational Thinking": "کمپیوٹیشنل تھنکنگ مسئلے کو توڑتی ہے: حصے کرنا، نمونہ دیکھنا، فضول تفصیل ہٹانا، پھر الگورتھم لکھنا۔",
    "Algorithm vs Pseudocode": "الگورتھم قدم بہ قدم حل ہے۔ سوڈو کوڈ وہی حل عام زبان میں ہے، کسی ایک پروگرامنگ زبان کے بغیر۔",
    "Algorithmic Strategies for Problem Solving": "پہلے مسئلہ چھوٹے حصوں میں بانٹیں، دہرایا نمونہ ڈھونڈیں، غیر ضروری بات ہٹائیں، پھر واضح قدم لکھیں۔",
    "Sorting and Searching Algorithms": "سارٹنگ ترتیب دیتی ہے اور سرچنگ مطلوبہ قدر ڈھونڈتی ہے۔ درست چناؤ وقت بچاتا ہے۔",
    "Selection Sort": "سیلیکشن سارٹ ہر بار باقی فہرست سے سب سے چھوٹی قدر چن کر اس کی جگہ رکھتا ہے۔",
    "Binary Search": "بائنری سرچ صرف ترتیب شدہ فہرست پر چلتی ہے۔ ہر قدم فہرست آدھی کرتا ہے، اس لیے یہ لکیری تلاش سے تیز ہے۔",
    "Fundamentals of Python Programming": "پائتھن ہائی لیول زبان ہے۔ کوڈ پڑھنا آسان ہے اور indentation سے بلاک بنتا ہے۔",
    "Variables": "ویری ایبل میموری کا نام ہے۔ نام حرف یا underscore سے شروع ہو، درمیان میں space نہ ہو، اور keyword استعمال نہ ہو۔",
    "Operators and Operands": "آپریٹر عمل کا نشان ہے اور آپریئنڈ وہ قدر ہے جس پر عمل ہوتا ہے۔ جمع، تفریق، ضرب، تقسیم اور موازنہ یہی کام کرتے ہیں۔",
    "Control Structures": "Sequence سیدھا چلتا ہے۔ Selection شرط دیکھ کر راستہ بدلتا ہے۔ Loop کام دہراتا ہے۔",
    "Repetition Statements (Loops)": "for تب جب گنتی معلوم ہو۔ while تب جب شرط کے سچ رہنے تک دہراتے رہنا ہو۔",
    "Keys and Integrity Constraints": "پرائمری کی ہر ریکارڈ کو منفرد بناتی ہے۔ فارن کی دوسری ٹیبل سے جوڑتی ہے۔ شرائط غلط ڈیٹا روکتی ہیں۔",
    "Entity Relationship Model (ER-Model)": "اینٹیٹی چیز ہے، ایٹریبیوٹ اس کی صفت ہے، اور ریلیشن شپ دو اینٹیٹی کے بیچ تعلق ہے۔",
    "Referential Integrity": "فارن کی یا تو موجود پرائمری کی کی طرف اشارہ کرے یا خالی رہے۔ یتیم ریکارڈ نہیں بننا چاہیے۔",
    "Creating Queries in MS Access": "کوئری ڈیٹا بیس سے سوال ہے۔ اس سے فلٹر، ترتیب، اور حساب ایک ساتھ ہوتے ہیں۔",
    "Introduction to Computing": "کمپیوٹنگ ڈیٹا کو معلومات بناتی ہے۔ آج کے نظام انسان، آلہ، اور نیٹ ورک کو جوڑتے ہیں۔",
    "Internet of Things (IoT)": "IoT وہ آلات ہیں جو انٹرنیٹ سے جڑ کر سینسر کا ڈیٹا بھیجتے ہیں، جیسے سمارٹ ڈیوائس۔",
    "Information Sources": "ذریعہ پرائمری یا سیکنڈری ہو سکتا ہے۔ قابلِ اعتماد ذریعہ مصنف، تاریخ، اور ثبوت دکھاتا ہے۔",
    "Assistive Technologies": "امدادی ٹیکنالوجی سیکھنے کی رکاوٹ ہٹاتی ہے، جیسے اسکرین ریڈر، کیپشن، اور آواز سے حکم۔",
    "Types of Data": "ڈیٹا کوالیٹیٹو یا کوانٹیٹیٹو ہوتا ہے۔ کوانٹیٹیٹو ڈیٹا مجرد بھی ہو سکتا ہے اور مسلسل بھی۔",
    "Data-Collection Strategies": "ڈیٹا سروے، انٹرویو، مشاہدے، یا سینسر سے جمع ہوتا ہے۔ طریقہ سوال کے مطابق چنیں۔",
    "Primary and Secondary Data": "پرائمری ڈیٹا آپ خود جمع کرتے ہیں۔ سیکنڈری ڈیٹا پہلے سے موجود رپورٹ یا ڈیٹا بیس ہوتا ہے۔",
    "Case Study: Digital Inquiry Project": "ڈیجیٹل انکوائری میں سوال، ڈیٹا، تجزیہ، اور آخر میں ڈیجیٹل آرٹیفیکٹ آتا ہے۔",
    "Applications of HCI": "HCI صحت، بینک، تعلیم، اور رابطے میں انسانی ضرورت کے مطابق نظام بناتی ہے۔",
    "Importance of HCI": "اچھی HCI غلطی کم کرتی ہے، کام تیز کرتی ہے، اور زیادہ لوگوں کو نظام استعمال کرنے دیتی ہے۔",
    "Human Computer Interaction Problems": "الجھن، کم فیڈبیک، چھوٹے بٹن، اور ایسا ڈیزائن جو سب کے لیے نہ ہو، HCI کے عام مسئلے ہیں۔",
    "User Interface Design (UI)": "UI وہ ہے جو صارف دیکھے اور چھواے۔ UX پورا تجربہ ہے۔ اچھا UI صاف، یکساں، اور قابلِ رسائی ہوتا ہے۔",
    "Testing Methods": "یوزیبلٹی ٹیسٹ اصلی صارف سے ہوتا ہے۔ A/B ٹیسٹ دو ڈیزائن کا موازنہ ہے۔ آٹومیٹڈ ٹیسٹ بار بار چلتا ہے۔",
    "Analyze algorithms for correctness": "درست الگورتھم ہر جائز ان پٹ پر درست آؤٹ پٹ دیتا ہے۔ ٹریس ٹیبل ہر قدم کی قدر دکھاتی ہے۔",
    "Assess Algorithm Efficiency": "کارکردگی وقت اور میموری ہے۔ Big O بتاتا ہے کہ بڑی ان پٹ پر کام کتنی تیزی سے بڑھتا ہے۔",
    "Concept of Data Structure": "ڈیٹا سٹرکچر ڈیٹا سنبھالنے کا طریقہ ہے تاکہ تلاش، اضافہ، اور حذف آسان ہوں۔",
    "Linear Data Structures: Stack": "اسٹیک LIFO ہے: جو آخر میں آیا وہ پہلے نکلتا ہے۔ Push رکھتا ہے اور Pop نکالتا ہے۔",
    "Linear Data Structures: Queue": "قطار FIFO ہے: جو پہلے آیا وہ پہلے نکلتا ہے۔ Enqueue پیچھے لگاتی ہے اور Dequeue آگے سے نکالتی ہے۔",
    "Data Structures in Python": "لسٹ ترتیب شدہ اور قابلِ تبدیلی ہے۔ انڈیکس سے قدر تک سیدھی رسائی ہوتی ہے۔",
    "Tuples (Immutable Structure)": "ٹیوپل ترتیب شدہ ہے مگر بننے کے بعد بدل نہیں سکتا۔",
    "Set Traversal & 3.1.4 Dictionaries": "ڈکشنری میں کی اور ویلیو کی جوڑی ہوتی ہے۔ کی منفرد ہوتی ہے اور ویلیو جلدی مل جاتی ہے۔",
    "Functions in Python": "فنکشن نام والا کوڈ بلاک ہے تاکہ ایک کام بار بار نہ لکھنا پڑے۔",
    "File Handling Overview": "فائل ہینڈلنگ ڈیٹا کو پروگرام بند ہونے کے بعد بھی رکھتی ہے۔ کھولنا، پڑھنا، لکھنا، اور بند کرنا بنیادی قدم ہیں۔",
    "with Statement & Reading Files": "with بیان فائل خود بند کر دیتا ہے، چاہے بیچ میں غلطی آئے۔",
    "Data Sources & 4.1.2 Connectivity": "ڈیٹا فائل، ڈیٹا بیس، یا API سے آتا ہے۔ پائتھن میں SQLite کے لیے sqlite3 استعمال ہوتا ہے۔",
    "Basic Operations on Data using Pandas": "Pandas کا DataFrame جدول ہے۔ قطار، کالم، اور حساب اسی پر ہوتے ہیں۔",
    "Handling Missing Values": "خالی خانہ چھوڑا جا سکتا ہے یا اوسط، درمیانی قدر، یا موزوں قدر سے بھرا جا سکتا ہے۔",
    "Types of Graphs": "بار موازنہ، لائن رجحان، پائی حصہ، ہسٹوگرام تقسیم، اسکیٹر تعلق، اور باکس پھیلاؤ دکھاتا ہے۔",
    "Box Plots": "باکس پلاٹ درمیانی قدر، چوتھائی، اور outlier ایک ساتھ دکھاتا ہے۔",
    "Measures of Spread (Dispersion)": "پھیلاؤ بتاتا ہے کہ قدریں مرکز سے کتنی دور ہیں۔ رینج، ویریئنس، اور سٹینڈرڈ ڈیوی ایشن یہی ناپتے ہیں۔",
    "Neural Networks": "نیورل نیٹ ورک تہوں والا ماڈل ہے جو مثالوں سے سیکھتا ہے: ان پٹ، پوشیدہ تہیں، اور آؤٹ پٹ۔",
    "Components of Neural Networks": "نیوران ان پٹ لیتا ہے، weight لگاتا ہے، bias جوڑتا ہے، پھر activation سے آؤٹ پٹ نکالتا ہے۔",
    "Secure Collaboration and Data Protection": "محفوظ اشتراک میں صرف اجازت والا شخص ڈیٹا دیکھے۔ مضبوط پاس ورڈ، خفیہ کاری، اور رسائی کی حد ضروری ہے۔",
    "Security Threats and Mitigation": "خطرے میں مالویئر، فشنگ، کمزور پاس ورڈ، اور کھلا اشتراک آتا ہے۔ اپ ڈیٹ، بیک اپ، اور احتیاط بچاؤ ہے۔",
    "Equity and Equal Access in Collaboration": "برابر رسائی ہر طالبِ علم کو اوزار دیتی ہے۔ انصاف وہاں اضافی مدد دیتا ہے جہاں رکاوٹ ہو۔",
    "Entrepreneurship in the Digital Age": "ڈیجیٹل دور میں کاروبار انٹرنیٹ اور ایپ سے بڑھتا ہے۔ مسئلہ حل کرنا موقع بن جاتا ہے۔",
    "Prototype": "پروٹوٹائپ خیال کا ابتدائی نمونہ ہے تاکہ جلدی پتہ چلے کہ خیال کام کرتا ہے یا نہیں۔",
    "Prototype Development Cycle": "چکر ہے: منصوبہ، تعمیر، جانچ، اور بہتری، جب تک نمونہ ضرورت پوری نہ کرے۔",
    "Minimum Viable Product (MVP)": "MVP سب سے چھوٹی مصنوعات ہے جس سے اصلی گاہک پر سب سے خطرناک مفروضہ جانا جائے۔",
    "Beachhead Market": "بیچ ہیڈ مارکیٹ چھوٹی مخصوص مارکیٹ ہے جہاں پہلے جیت حاصل کی جائے، پھر پھیلا جائے۔",
}

CLASSES = [
    {
        "id": "xi",
        "pdf": XI_PDF,
        "title": "Computer Science XI",
        "urdu": "کمپیوٹر سائنس، گیارہویں",
        "curriculum": "سندھ نصاب 2026",
        "chapters": [
            (1, "Computer Systems", "کمپیوٹر سسٹمز"),
            (2, "Computational Thinking & Algorithms", "کمپیوٹیشنل تھنکنگ اور الگورتھم"),
            (3, "Programming Fundamentals", "پروگرامنگ کے بنیادی اصول"),
            (4, "Data and Analysis", "ڈیٹا اور تجزیہ"),
            (5, "Applications and Impacts of Computing", "کمپیوٹنگ کے استعمال اور اثرات"),
            (6, "Digital Literacy", "ڈیجیٹل خواندگی"),
        ],
    },
    {
        "id": "xii",
        "pdf": XII_PDF,
        "title": "Computer Science XII",
        "urdu": "کمپیوٹر سائنس، بارہویں",
        "curriculum": "سندھ نصاب 2024 / 2025-27",
        "chapters": [
            (1, "Computer Systems (HCI)", "ہیومن کمپیوٹر انٹریکشن"),
            (2, "Computational Thinking & Algorithms", "کمپیوٹیشنل تھنکنگ اور الگورتھمز"),
            (3, "Programming Fundamentals", "پروگرامنگ کے بنیادی اصول"),
            (4, "Data and Analysis", "ڈیٹا اور تجزیہ"),
            (5, "Applications and Impacts of Computing", "کمپیوٹنگ کے استعمال اور اثرات"),
            (6, "Entrepreneurship in the Digital Age", "ڈیجیٹل دور میں کاروبار"),
        ],
    },
]


def norm_title(title: str) -> str:
    title = title.replace("★", "").strip()
    title = SECTION_NO.sub("", title)
    title = SIMPLE_NO.sub("", title)
    title = re.sub(r"\s+", " ", title).strip(" -:")
    return title


def urdu_title(title: str) -> str:
    key = norm_title(title)
    if key in TITLE_UR:
        return TITLE_UR[key]
    # Longest phrase wins so partial titles still become Urdish.
    best = ""
    best_len = 0
    for phrase, ur in TITLE_UR.items():
        if phrase.lower() in key.lower() and len(phrase) > best_len:
            best = ur
            best_len = len(phrase)
    return best or key


def pick_diagram(title: str) -> str | None:
    hay = norm_title(title).lower()
    for diagram_id, keys in DIAGRAM_RULES:
        if any(k in hay for k in keys):
            return diagram_id
    return None


def extract_items(page: pymupdf.Page) -> list[dict]:
    items = []
    data = page.get_text("dict")
    for block in data["blocks"]:
        if block.get("type") != 0:
            continue
        for line in block["lines"]:
            kept = []
            for span in line["spans"]:
                text = span["text"]
                if not text.strip() or ARABIC.search(text):
                    continue
                kept.append(span)
            if not kept:
                continue
            parts = []
            previous_end = None
            for span in kept:
                if previous_end is not None and span["bbox"][0] - previous_end > 2.2:
                    parts.append(" ")
                parts.append(span["text"])
                previous_end = span["bbox"][2]
            text = re.sub(r"\s+", " ", "".join(parts)).strip()
            if not text or PAGE_NO.match(text):
                continue
            if text in {"V", "t", "HIGH(1)", "LOW(0)"}:
                continue
            fonts = [s["font"] for s in kept]
            bold_flags = ["Bold" in font for font in fonts]
            items.append(
                {
                    "x": min(s["bbox"][0] for s in kept),
                    "x1": max(s["bbox"][2] for s in kept),
                    "y": min(s["bbox"][1] for s in kept),
                    "size": max(s["size"] for s in kept),
                    "bold": all(bold_flags),
                    "lead": any(bold_flags) and not all(bold_flags),
                    "mono": all("Poppins" not in font for font in fonts),
                    "white": kept[0]["color"] == 16777215,
                    "text": text,
                }
            )
    items = [item for item in items if not drop_noise(item)]
    items.sort(key=lambda it: (round(it["y"], 1), it["x"]))
    return items


def drop_noise(item: dict) -> bool:
    """Drop English scraps that were painted inside the Urdu column."""
    text = item["text"].strip()
    if not item["mono"]:
        return False
    if "GOLDEN" in text.upper() or is_code_item(item):
        return False
    if re.fullmatch(r"[\W_]+", text) or re.fullmatch(r"\d+", text):
        return True
    if text.startswith((")", ":")) or ")(" in text or re.search(r"\)[A-Za-z]+\(", text):
        return True
    return False


def cluster_rows(items: list[dict]) -> list[list[dict]]:
    rows: list[list[dict]] = []
    for item in items:
        if rows and abs(item["y"] - rows[-1][0]["y"]) <= 6.5:
            rows[-1].append(item)
        else:
            rows.append([item])
    for row in rows:
        row.sort(key=lambda it: it["x"])
    return rows


def is_code_item(item: dict) -> bool:
    text = item["text"]
    if text.upper().startswith("GOLDEN"):
        return False
    if item["mono"] and (
        "=" in text
        or text.startswith("#")
        or text.startswith("def ")
        or text.startswith("for ")
        or text.startswith("if ")
        or text.startswith("print")
        or text.startswith("import ")
        or text.startswith("while ")
        or text.startswith("return ")
        or "()" in text
    ):
        return True
    return False


def is_heading_item(item: dict) -> bool:
    text = item["text"]
    if text.upper().startswith("GOLDEN") or item.get("lead"):
        return False
    if is_code_item(item) or is_bullet(text):
        return False
    if item["bold"] and item["size"] >= 13.2:
        return True
    if item["bold"] and item["size"] >= 10.5 and len(text) <= 72 and not text.endswith("."):
        return True
    return False


def is_bullet(text: str) -> bool:
    return bool(re.match(r"^([•●▪\-\*]|\d+[\.\)])\s+\S", text))


def looks_indented_bullet(item: dict) -> bool:
    text = item["text"]
    if "." in text or ":" in text or item.get("lead"):
        return False
    return (
        70 <= item["x"] <= 100
        and not item["bold"]
        and not item["mono"]
        and 8 <= len(text) <= 70
        and not is_bullet(text)
    )


def side_blocks(items: list[dict]) -> list[dict]:
    """Turn one column of a side-by-side pair into paragraphs and headings."""
    blocks = []
    buf: list[dict] = []

    def flush():
        nonlocal buf
        if not buf:
            return
        text = " ".join(it["text"] for it in buf)
        kind = "h" if buf[0]["bold"] and is_heading_item(buf[0]) else "p"
        blocks.append({"type": kind, "text": tidy(text), "math": True})
        buf = []

    for item in items:
        if is_heading_item(item) or is_bullet(item["text"]):
            flush()
            kind = "li" if is_bullet(item["text"]) else "h"
            blocks.append({"type": kind, "text": tidy(strip_bullet(item["text"])), "math": True})
            continue
        if buf and abs(item["size"] - buf[-1]["size"]) > 2:
            flush()
        buf.append(item)
    flush()
    return merge_list_items(blocks)


def two_col_is_table(run: list[list[dict]]) -> bool:
    texts = [cell["text"] for row in run for cell in row]
    if not texts:
        return False
    short = sum(1 for text in texts if len(text) <= 22)
    return short / len(texts) >= 0.8


def parallel_tables(run: list[list[dict]]) -> dict | None:
    """Split two truth tables that share a baseline into a flex pair."""
    left_rows: list[list[dict]] = []
    right_rows: list[list[dict]] = []
    cuts = 0
    for row in run:
        ordered = sorted(row, key=lambda cell: cell["x"])
        cut = None
        for index in range(1, len(ordered)):
            gap = ordered[index]["x"] - ordered[index - 1].get("x1", ordered[index - 1]["x"])
            if gap > 85 and index >= 2 and len(ordered) - index >= 2:
                cut = index
                break
        if cut:
            cuts += 1
            left_rows.append(ordered[:cut])
            right_rows.append(ordered[cut:])
        elif ordered[0]["x"] > 270:
            right_rows.append(ordered)
        else:
            left_rows.append(ordered)
    if cuts < 2 or not left_rows or not right_rows:
        return None
    return {
        "type": "split",
        "left": [table_from_rows(left_rows)],
        "right": [table_from_rows(right_rows)],
    }


def table_from_rows(run: list[list[dict]]) -> dict:
    rows = []
    for index, row in enumerate(run):
        cells = [tidy(cell["text"]) for cell in row]
        header = index == 0 or any(cell["white"] or (cell["bold"] and len(cell["text"]) < 28) for cell in row)
        # Only the first bold/white row stays a header. Later bold labels are body.
        if index > 0:
            header = all(cell["white"] for cell in row)
        rows.append({"header": header and index == 0, "cells": cells})
    if rows:
        rows[0]["header"] = True
    return {"type": "table", "rows": rows}


def tidy(text: str) -> str:
    text = text.replace("★", "").strip()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+([,.;:)])", r"\1", text)
    return text.strip()


def strip_bullet(text: str) -> str:
    return re.sub(r"^([•●▪\-\*]|\d+[\.\)])\s+", "", text).strip()


def merge_list_items(blocks: list[dict]) -> list[dict]:
    merged = []
    for block in blocks:
        if block["type"] == "li" and merged and merged[-1]["type"] == "list":
            merged[-1]["items"].append(block["text"])
        elif block["type"] == "li":
            merged.append({"type": "list", "items": [block["text"]]})
        else:
            merged.append(block)
    return merged


def apply_math(text: str) -> str:
    rules = [
        (r"Y\s*=\s*A\s*[·•⋅]\s*B", r"\\(Y = A \\cdot B\\)"),
        (r"Y\s*=\s*A\s*\+\s*B", r"\\(Y = A + B\\)"),
        (r"Y\s*=\s*A\s*'", r"\\(Y = A'\\)"),
        (r"Y\s*=\s*A̅", r"\\(Y = \\bar{A}\\)"),
        (r"\b2ⁿ\b", r"\\(2^{n}\\)"),
        (r"\b2\^n\b", r"\\(2^{n}\\)"),
        (r"2²", r"\\(2^{2}\\)"),
        (r"2³", r"\\(2^{3}\\)"),
        (r"O\(n\^2\)", r"\\(O(n^{2})\\)"),
        (r"O\(n²\)", r"\\(O(n^{2})\\)"),
        (r"O\(n log n\)", r"\\(O(n \\log n)\\)"),
        (r"O\(log n\)", r"\\(O(\\log n)\\)"),
        (r"O\(1\)", r"\\(O(1)\\)"),
        (r"\bO\(n\)", r"\\(O(n)\\)"),
    ]
    for pattern, repl in rules:
        text = re.sub(pattern, repl, text)
    return text


def finalize_block(block: dict) -> dict:
    if block.get("math") and block.get("text"):
        block["text"] = apply_math(block["text"])
    if block.get("items"):
        block["items"] = [apply_math(item) for item in block["items"]]
    if block.get("rows"):
        for row in block["rows"]:
            row["cells"] = [apply_math(cell) for cell in row["cells"]]
    block.pop("math", None)
    block.pop("x", None)
    block.pop("bold", None)
    return block


def rows_to_blocks(rows: list[list[dict]]) -> tuple[str, bool, list[dict]]:
    # Drop the golden banner from the flow; keep the flag.
    golden = False
    cleaned = []
    for row in rows:
        texts = " ".join(cell["text"] for cell in row)
        if "GOLDEN TOPIC" in texts.upper():
            golden = True
            continue
        cleaned.append(row)
    rows = cleaned

    title_parts = []
    index = 0
    while index < len(rows) and len(rows[index]) == 1:
        item = rows[index][0]
        if item["size"] >= 15.5 and item["bold"] and not is_code_item(item):
            title_parts.append(item["text"])
            index += 1
            continue
        break
    title = tidy(" ".join(title_parts)) if title_parts else tidy(rows[0][0]["text"])
    if title_parts:
        rows = rows[index:]

    raw_blocks = []
    index = 0
    while index < len(rows):
        row = rows[index]
        if len(row) >= 3:
            run = []
            while index < len(rows) and len(rows[index]) >= 3:
                run.append(rows[index])
                index += 1
            parallel = parallel_tables(run)
            raw_blocks.append(parallel or table_from_rows(run))
            continue
        if len(row) == 2:
            run = []
            while index < len(rows) and len(rows[index]) == 2:
                run.append(rows[index])
                index += 1
            if two_col_is_table(run):
                raw_blocks.append(table_from_rows(run))
            else:
                left = [pair[0] for pair in run]
                right = [pair[1] for pair in run]
                raw_blocks.append(
                    {
                        "type": "split",
                        "left": side_blocks(left),
                        "right": side_blocks(right),
                    }
                )
            continue
        item = row[0]
        raw_blocks.append(
            {
                "type": "line",
                "text": item["text"],
                "bold": item["bold"],
                "lead": item.get("lead", False),
                "size": item["size"],
                "x": item["x"],
                "code": is_code_item(item),
                "bullet": is_bullet(item["text"]) or looks_indented_bullet(item),
                "heading": is_heading_item(item),
            }
        )
        index += 1

    blocks: list[dict] = []
    para: list[dict] = []
    code: list[str] = []

    def flush_para():
        nonlocal para
        if not para:
            return
        text = tidy(" ".join(it["text"] for it in para))
        if text:
            if CALLOUT_RE.search(text):
                lowered = text.lower()
                if "analogy" in lowered:
                    kind = "analogy"
                elif "real" in lowered:
                    kind = "reallife"
                elif "activity" in lowered or "class discussion" in lowered:
                    kind = "activity"
                else:
                    kind = "note"
                blocks.append({"type": "callout", "kind": kind, "text": text, "math": True})
            else:
                blocks.append({"type": "p", "text": text, "math": True, "x": para[0]["x"]})
        para = []

    def flush_code():
        nonlocal code
        if not code:
            return
        blocks.append({"type": "code", "text": "\n".join(code).rstrip()})
        code = []

    for block in raw_blocks:
        if block["type"] != "line":
            flush_para()
            flush_code()
            blocks.append(block)
            continue
        if block["code"]:
            flush_para()
            code.append(block["text"])
            continue
        flush_code()
        if block["heading"] or block["bullet"]:
            flush_para()
            if block["bullet"]:
                blocks.append({"type": "li", "text": tidy(strip_bullet(block["text"])), "math": True})
            else:
                blocks.append({"type": "h", "text": tidy(block["text"]), "math": True})
            continue
        if block.get("lead") and para:
            flush_para()
        if para and abs(block["x"] - para[-1]["x"]) > 28:
            flush_para()
        if para and abs(block["size"] - para[-1]["size"]) > 2.2:
            flush_para()
        para.append(block)
    flush_para()
    flush_code()

    blocks = merge_list_items(blocks)
    blocks = absorb_callouts(blocks)
    blocks = polish_blocks(blocks)
    return title, golden, [finalize_block(block) for block in blocks if not empty_block(block)]


def table_ok(block: dict) -> bool:
    rows = block.get("rows") or []
    if len(rows) < 2:
        return False
    lengths = [len(row["cells"]) for row in rows]
    return max(lengths) == min(lengths)


def polish_blocks(blocks: list[dict]) -> list[dict]:
    output = []
    for block in blocks:
        if block["type"] == "split":
            block["left"] = polish_blocks(block["left"])
            block["right"] = polish_blocks(block["right"])
            if block["left"] or block["right"]:
                output.append(block)
            continue
        if block["type"] == "table" and not table_ok(block):
            seen = set()
            for row in block["rows"]:
                for cell in row["cells"]:
                    if "\\(" not in cell and "Y =" not in cell:
                        continue
                    cleaned = re.sub(r"^\d+\s+", "", cell).strip()
                    if cleaned and cleaned not in seen:
                        seen.add(cleaned)
                        output.append({"type": "p", "text": cleaned, "math": True})
            continue
        output.append(block)
    return output


def empty_block(block: dict) -> bool:
    if block["type"] in {"p", "h", "code"}:
        return not block.get("text")
    if block["type"] == "list":
        return not block.get("items")
    if block["type"] == "table":
        return not block.get("rows")
    if block["type"] == "split":
        return not block.get("left") and not block.get("right")
    return False


def absorb_callouts(blocks: list[dict]) -> list[dict]:
    output = []
    index = 0
    while index < len(blocks):
        block = blocks[index]
        if block["type"] == "h" and CALLOUT_RE.search(block["text"]):
            kind = "note"
            lowered = block["text"].lower()
            if "analog" in lowered or "analogy" in lowered:
                kind = "analogy"
            elif "real" in lowered:
                kind = "reallife"
            elif "activity" in lowered or "class" in lowered:
                kind = "activity"
            parts = [block["text"]]
            index += 1
            while index < len(blocks) and blocks[index]["type"] in {"p", "list"}:
                nxt = blocks[index]
                if nxt["type"] == "p":
                    parts.append(nxt["text"])
                else:
                    parts.extend(nxt["items"])
                index += 1
                if len(parts) >= 4:
                    break
            output.append({"type": "callout", "kind": kind, "text": " ".join(parts), "math": True})
            continue
        output.append(block)
        index += 1
    return output


def plain_text(blocks: list[dict]) -> str:
    chunks = []

    def walk(block_list: list[dict]):
        for block in block_list:
            if block["type"] in {"p", "h", "callout"}:
                chunks.append(re.sub(r"\\\(|\\\)", "", block["text"]))
            elif block["type"] == "list":
                chunks.extend(block["items"])
            elif block["type"] == "code":
                chunks.append(block["text"])
            elif block["type"] == "split":
                walk(block["left"])
                walk(block["right"])
            elif block["type"] == "table":
                for row in block["rows"]:
                    chunks.append(" | ".join(row["cells"]))

    walk(blocks)
    return re.sub(r"\s+", " ", " ".join(chunks)).strip()


def key_line(blocks: list[dict]) -> str:
    for block in blocks:
        if block["type"] == "p" and len(block["text"]) > 40:
            text = re.sub(r"\\\(|\\\)", "", block["text"])
            return text[:220].rstrip()
        if block["type"] == "split":
            found = key_line(block["left"]) or key_line(block["right"])
            if found:
                return found
    return ""


def is_cover(page: pymupdf.Page) -> bool:
    text = page.get_text("text")
    return "BILINGUAL TEACHER" in text and "CHAPTER" in text


def is_toc(page: pymupdf.Page) -> bool:
    return "TABLE OF CONTENTS" in page.get_text("text")


def chapter_number(page: pymupdf.Page) -> int | None:
    match = re.search(r"CHAPTER\s+(\d+)", page.get_text("text"))
    return int(match.group(1)) if match else None


def save_plate(page: pymupdf.Page, path: str) -> None:
    pix = page.get_pixmap(matrix=pymupdf.Matrix(1.2, 1.2), alpha=False)
    pix.save(path, jpg_quality=55)


def build_class(spec: dict, write_plates: bool) -> dict:
    doc = pymupdf.open(spec["pdf"])
    chapter_meta = {num: (title, ur) for num, title, ur in spec["chapters"]}
    chapters = []
    current = None
    for page_index, page in enumerate(doc):
        page_no = page_index + 1
        if is_cover(page):
            number = chapter_number(page)
            title, ur = chapter_meta.get(number, (f"Chapter {number}", f"باب {number}"))
            current = {
                "id": f"{spec['id']}-ch{number}",
                "number": number,
                "title": title,
                "urdu": ur,
                "lessons": [],
            }
            chapters.append(current)
            continue
        if is_toc(page) or current is None:
            continue
        items = extract_items(page)
        if not items:
            continue
        rows = cluster_rows(items)
        title, golden, blocks = rows_to_blocks(rows)
        if not title:
            title = f"Page {page_no}"
        plate_name = f"{spec['id']}-{page_no:03d}.jpg"
        if write_plates:
            save_plate(page, os.path.join(PLATE_DIR, plate_name))
        lesson = {
            "id": f"{spec['id']}-{page_no:03d}",
            "page": page_no,
            "title": title,
            "urduTitle": urdu_title(title),
            "golden": golden,
            "diagram": pick_diagram(title),
            "plate": f"plates/{plate_name}",
            "blocks": blocks,
            "recall": key_line(blocks),
            "blurb": BLURBS.get(norm_title(title), ""),
        }
        current["lessons"].append(lesson)
    return {
        "id": spec["id"],
        "title": spec["title"],
        "urdu": spec["urdu"],
        "curriculum": spec["curriculum"],
        "chapters": chapters,
    }


def main() -> None:
    sample = "--sample" in sys.argv
    write_plates = not sample
    os.makedirs(PLATE_DIR, exist_ok=True)
    course = {
        "title": "Teach Yourself Sketchnotes",
        "version": "1.0.0",
        "subject": "Computer Science",
        "board": "Sindh Curriculum",
        "classes": [],
    }
    if sample:
        # Build only the first class's first few content pages for inspection.
        spec = dict(CLASSES[0])
        built = build_class(spec, write_plates=False)
        keep_pages = {3, 5, 8, 9, 14, 51}
        for chapter in built["chapters"]:
            chapter["lessons"] = [ls for ls in chapter["lessons"] if ls["page"] in keep_pages]
        built["chapters"] = [ch for ch in built["chapters"] if ch["lessons"]]
        print(json.dumps(built, ensure_ascii=False, indent=2)[:20000])
        return

    for spec in CLASSES:
        print(f"building {spec['id']} ...", flush=True)
        course["classes"].append(build_class(spec, write_plates=write_plates))

    out_path = os.path.join(OUT_DIR, "course.json")
    with open(out_path, "w", encoding="utf-8") as handle:
        json.dump(course, handle, ensure_ascii=False, separators=(",", ":"))

    lessons = [ls for cls in course["classes"] for ch in cls["chapters"] for ls in ch["lessons"]]
    missing_ur = [ls["title"] for ls in lessons if ls["urduTitle"] == norm_title(ls["title"])]
    golden = sum(1 for ls in lessons if ls["golden"])
    diagrams = sum(1 for ls in lessons if ls["diagram"])
    plates = sum(1 for ls in lessons if os.path.exists(os.path.join(OUT_DIR, ls["plate"])))
    print(f"lessons {len(lessons)} golden {golden} diagrams {diagrams} plates {plates}")
    print(f"course.json {os.path.getsize(out_path)} bytes")
    if missing_ur:
        print("TITLES WITHOUT URDU:")
        for title in missing_ur:
            print(" -", title)
    blurbless = [norm_title(ls["title"]) for ls in lessons if ls["golden"] and not ls["blurb"]]
    if blurbless:
        print("GOLDEN WITHOUT BLURB:")
        for title in blurbless:
            print(" -", title)


if __name__ == "__main__":
    main()
