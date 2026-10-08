#!/usr/bin/env python3
"""Generate teach-yourself/js/curriculum.js — Urdish-only CS XI lectures."""
from __future__ import annotations

import json
from pathlib import Path

COACH = [
    "آپ آ گئے — یہ سب سے مشکل قدم تھا۔ ایک سلائیڈ، ایک تصور۔",
    "★ سنہری موضوعات امتحان میں بار بار آتے ہیں۔ انہیں زور سے پڑھیں۔",
    "فارمولا دیکھیں، مثال بنائیں، پھر خود آزمائی حل کریں۔",
    "Urdish میں سنیں: اردو وضاحت، انگریزی اصطلاح (AND, OSI, SDLC) ویسی کی ویسی۔",
    "دو منٹ ٹھہریں — دماغ گرم ہو رہا ہے۔",
]


def S(headline, body, narrator=None, diagram=None, quiz=None, tip=None, coach=None):
    html_free = (
        body.replace("<p>", " ").replace("</p>", " ").replace("<li>", " ")
        .replace("</li>", " ").replace("<ul>", " ").replace("</ul>", " ")
        .replace("<strong>", "").replace("</strong>", "")
        .replace('<p class="objectives">', " ").replace('<div class="objectives">', " ")
        .replace("</div>", " ")
    )
    return {
        "headline": headline,
        "body": body,
        "narrator": narrator or f"{headline}۔ {html_free}",
        "diagram": diagram,
        "quiz": quiz,
        "tip": tip,
        "coach": coach,
    }


def M(id, title, golden, slides):
    return {"id": id, "title": title, "golden": golden, "slides": slides}


def ch(id, number, title, modules):
    return {"id": id, "number": number, "title": title, "modules": modules}


def q(question, options, answer, explain):
    return {"q": question, "options": options, "answer": answer, "explain": explain}


def chapter1():
    return ch("ch1", 1, "کمپیوٹر سسٹمز", [
        M("1.1.1", "Discrete اور Continuous مقداریں", False, [
            S("سبق کا ہدف",
              '<div class="objectives"><p>اس سبق کے بعد آپ <strong>Discrete</strong> اور <strong>Continuous</strong> مقداروں میں فرق بتا سکیں گے، اور سیڑھی/ ramp کی مشابہت سے امتحانی مثال لکھ سکیں گے۔</p></div>'
              "<p>Discrete مقدار الگ الگ، گننے کے قابل ہوتی ہے — کلاس میں طلبہ، پارکنگ میں گاڑیاں۔ Continuous مقدار کسی حد میں کوئی بھی قیمت لے سکتی ہے — پانی کا درجہ حرارت، چلتی گاڑی کی رفتار۔</p>",
              diagram="stairsRamp"),
            S("سیڑھیاں بمقابلہ ramp",
              "<p>سیڑھیاں Discrete ہیں: ہر قدم مقرر۔ Ramp Continuous ہے: کوئی بھی نقطہ ممکن۔ کمپیوٹر Discrete bits استعمال کرتا ہے، اس لیے Continuous دنیا کو sample کر کے Discrete بنایا جاتا ہے۔</p>",
              tip="سوال میں 'گننا' آئے تو Discrete، 'پیمانہ/بہاؤ' آئے تو Continuous۔",
              quiz=q("گاڑی کی رفتار کون سی مقدار ہے؟",
                     ["Discrete", "Continuous", "Boolean", "Minterm"], 1,
                     "رفتار حد میں کوئی بھی قیمت لے سکتی ہے، لہٰذا Continuous۔")),
        ]),
        M("1.1.2", "ڈیجیٹل سسٹمز کا تعارف", False, [
            S("صرف دو حالتیں",
              "<p>Digital system الیکٹرانک نظام ہے جو صرف دو values استعمال کرتا ہے: <strong>0</strong> = OFF / LOW / FALSE اور <strong>1</strong> = ON / HIGH / TRUE۔ انہیں binary digits یا <strong>bits</strong> کہتے ہیں۔</p>"
              "<p>فائدے: Reliable (شور سے کم اثر)، Accurate (کاپی پر معیار نہیں گرتا)، Easy to Design (صرف دو states)، Programmable (سافٹ ویئر سے کنٹرول)۔</p>",
              diagram="binaryBits"),
            S("روزمرہ مثالیں",
              "<p>کمپیوٹر، اسمارٹ فون، ڈیجیٹل کیمرہ — سب photos اور music کو 0 اور 1 کے binary data کی صورت میں رکھتے ہیں۔</p>",
              quiz=q("Digital system میں 1 کیا ظاہر کرتا ہے؟",
                     ["OFF / FALSE", "ON / HIGH / TRUE", "Sine wave", "Noise"], 1,
                     "1 = ON, HIGH, TRUE۔")),
        ]),
        M("1.1.3", "Analog اور Digital سگنل", True, [
            S("★ سنہری: دو لہریں",
              '<div class="objectives"><p>امتحانی جدول یاد کریں: فطرت اور Reliability۔</p></div>'
              "<p><strong>Analog signal</strong> وقت کے ساتھ ہموار بدلتا ہے، جیسے sine wave — انسانی آواز، پرانا تھرمامیٹر۔</p>"
              "<p><strong>Digital signal</strong> صرف HIGH(1) اور LOW(0) — فوری چھلانگ، square wave — کمپیوٹر ڈیٹا۔</p>",
              diagram="analogDigitalWaves",
              tip="Analog: Continuous flow، شور سے متاثر۔ Digital: Discrete bits، شور کے خلاف مضبوط۔"),
            S("موازنہ کی جدول",
              "<p>Nature: Analog = مسلسل بہاؤ؛ Digital = الگ bits۔ Reliability: Analog کم، Digital زیادہ۔ امتحان میں یہ دو قطاریں اکثر آتی ہیں۔</p>",
              quiz=q("Square wave کس سگنل کی پہچان ہے؟",
                     ["Analog", "Digital", "Continuous temperature", "Ramp"], 1,
                     "Digital سگنل HIGH/LOW کے درمیان مربع لہر بناتا ہے۔")),
        ]),
        M("1.1.4-6", "Boolean Algebra، عملیات اور Truth Table", False, [
            S("George Boole کی الجبرا",
              "<p>Boolean algebra صرف TRUE (1) اور FALSE (0) پر کام کرتی ہے — digital electronics اور programming کی بنیاد۔</p>"
              "<p>Variables: A, B, C حروف جو 0 یا 1 رکھتے ہیں۔ Operations: AND، OR، NOT۔ Expression: متغیرات + عملیات، جیسے \\(Y = A + B\\)۔</p>"),
            S("تین بنیادی عملیات",
              "<p>AND \\(Y = A \\cdot B\\): آؤٹ پٹ 1 صرف جب تمام ان پٹ 1 — دو تالے والا دروازہ دونوں کھلیں تو کھلتا ہے۔</p>"
              "<p>OR \\(Y = A + B\\): کوئی ایک ان پٹ 1 — کمرے کے دو دروازوں میں سے کوئی کھلا ہو۔</p>"
              "<p>NOT \\(Y = A'\\): unary، ان پٹ الٹ — سوئچ ON تو روشنی، OFF تو اندھیرا۔</p>",
              diagram="gateAND"),
            S("Truth table کیسے بنے",
              "<p>1) ان پٹ گنیں \\(n\\)۔ 2) قطاریں \\(2^n\\)۔ 3) binary ترتیب میں تمام combinations۔ 4) ہر قطار کا آؤٹ پٹ۔ دو ان پٹ = 4 قطاریں؛ تین = 8۔</p>",
              diagram="truthTable2",
              quiz=q("3 ان پٹ کی truth table میں کتنی قطاریں؟",
                     ["3", "6", "8", "9"], 2, "\\(2^3 = 8\\)۔")),
        ]),
        M("1.1.7", "بنیادی Logic Gates (AND, OR, NOT)", True, [
            S("★ گیٹس یعنی سرکٹ کی اینٹیں",
              "<p>Logic gates الیکٹرانک سرکٹس ہیں جو Boolean عملیات کرتے ہیں۔ تمام digital systems انہی سے بنتے ہیں۔</p>"
              "<p>AND: \\(Y = A \\cdot B\\)۔ OR: \\(Y = A + B\\)۔ NOT: \\(Y = A'\\)۔</p>",
              diagram="gatesOverview",
              tip="گیٹ کا نام، علامت، expression، اور 4-قطار truth table — چاروں یاد کریں۔"),
            S("AND تفصیل",
              "<p>آؤٹ پٹ 1 صرف A=1 اور B=1 پر۔ باقی تین combinations پر 0۔</p>",
              diagram="gateAND"),
            S("OR اور NOT",
              "<p>OR کسی ایک 1 پر 1 دیتا ہے۔ NOT صرف ایک ان پٹ الٹ کرتا ہے۔</p>",
              diagram="gateOR",
              quiz=q("AND گیٹ 1 کب دیتا ہے؟",
                     ["کوئی ایک ان پٹ 1", "تمام ان پٹ 1", "ان پٹ مختلف", "ہمیشہ"], 1,
                     "AND = سب 1 تبھی 1۔")),
        ]),
        M("1.1.7u", "یونیورسل اور اعلیٰ گیٹس", False, [
            S("NAND اور NOR یونیورسل ہیں",
              "<p>NAND یعنی NOT AND: \\(Y = (A \\cdot B)'\\)۔ NOR یعنی NOT OR: \\(Y = (A + B)'\\)۔ دنیا کا کوئی بھی logic circuit صرف NAND یا صرف NOR سے بنایا جا سکتا ہے — اس لیے Universal Gates۔</p>",
              diagram="gateNAND"),
            S("XOR اور XNOR",
              "<p>XOR: ان پٹ <em>eXclusively</em> مختلف ہوں تو 1، \\(Y = A \\oplus B\\)۔ XNOR: ان پٹ ایک جیسے ہوں تو 1، \\(Y = (A \\oplus B)'\\)۔</p>",
              diagram="gateXOR",
              quiz=q("کون سے گیٹس Universal ہیں؟",
                     ["AND اور OR", "NAND اور NOR", "XOR اور XNOR", "NOT صرف"], 1,
                     "صرف NAND یا صرف NOR سے پورا سرکٹ ممکن۔")),
        ]),
        M("1.1.8-11", "Expressions، Minterms اور Logic Diagram", False, [
            S("ترتیبِ اولویت",
              "<p>Order of precedence: 1) Parentheses \\((\\,\\)\\) 2) NOT \\((\\,'\\,)\\) 3) AND \\((\\cdot)\\) 4) OR \\((+)\\)۔ پہلے اونچی اولویت کا گیٹ کھینچیں۔</p>"
              "<p>Minterm (SOP): وہ product جو truth table کی ایک قطار پر 1 ہو۔ Maxterm (POS): وہ sum جو 0 والی قطار پر ہو۔ مثال SOP: \\(Y = A'B + AB\\)۔</p>"),
            S("★ Logic diagram",
              "<p>مثال \\(Y = A \\cdot B + C\\)۔ AND کی اولویت OR سے زیادہ، اس لیے پہلے AND گیٹ، اس کا آؤٹ پٹ C کے ساتھ OR۔</p>",
              diagram="logicDiagram",
              tip="ڈایاگرام میں precedence بھولنا عام غلطی ہے۔",
              quiz=q("Y = A · B + C میں پہلے کون سا گیٹ؟",
                     ["OR", "AND", "NOT", "XOR"], 1, "AND کی اولویت زیادہ۔")),
        ]),
        M("1.1.13", "K-Maps — کارنو نقشے", True, [
            S("★ K-Map کیا ہے؟",
              "<p>K-map Boolean expression کو سادہ کرنے کا گرافیکل ٹول ہے۔ Grid میں ملحق خانے Gray code سے صرف ایک bit مختلف ہوتے ہیں۔ 1s کو 2 کی طاقتوں (1, 2, 4, 8) میں گروپ کریں — الجبرا کے بغیر سادہ term ملتی ہے۔</p>"
              "<p>دو متغیر: \\(2^2 = 4\\) خانے۔ تین متغیر: \\(2^3 = 8\\) خانے۔ کالم ترتیب: 00, 01, 11, 10۔</p>",
              diagram="kmap3var",
              tip="گروپ میں wrap-around (کنارے جوڑ) جائز ہے۔",
              quiz=q("3-variable K-map میں خانے؟",
                     ["3", "4", "6", "8"], 3, "\\(2^3 = 8\\)۔")),
        ]),
        M("logisim", "Logisim Evolution گائیڈ", False, [
            S("پہلے simulate، پھر سرکٹ",
              "<p>Logisim Evolution گرافیکل ٹول ہے: گیٹس رکھیں، تار جوڑیں، truth table آنکھوں سے چیک کریں — ہارڈویئر کے بغیر۔</p>"
              "<p>\\(Y = A \\cdot B\\): Toolbar سے AND، دو Input pins، ایک Output، تار جوڑیں، Poke tool سے 0/1 بدلیں۔</p>",
              diagram="logisim",
              quiz=q("Logisim میں ان پٹ 0/1 کیسے ٹیسٹ کریں؟",
                     ["صرف print()", "Poke tool", "K-map", "SDLC"], 1,
                     "Poke سے pins ٹوگل ہوتی ہیں۔")),
        ]),
        M("1.2.1-3", "SDLC — سافٹ ویئر لائف سائیکل", True, [
            S("★ ساخت یافتہ سفر",
              "<p>SDLC سافٹ ویئر کو شروع سے انجام تک لے جانے کا structured process ہے: واضح اہداف، بہتر منصوبہ، کم نقائص۔</p>"
              "<p>مراحل: Requirement Analysis → Design → Implementation/Coding → Testing → Deployment → Maintenance۔ ہر مرحلے کا deliverable ہوتا ہے (دستاویز، ماڈل، کوڈ، رپورٹ)۔</p>",
              diagram="sdlc",
              tip="مراحل کے نام ترتیب سے لکھنا golden سوال ہے۔",
              quiz=q("SDLC کا پہلا مرحلہ؟",
                     ["Testing", "Deployment", "Requirement Analysis", "Maintenance"], 2,
                     "پہلے ضروریات سمجھیں پھر ڈیزائن۔")),
        ]),
        M("1.2.4-7", "Waterfall بمقابلہ Agile", False, [
            S("دو ماڈل، دو مزاج",
              "<p><strong>Waterfall</strong>: لکیری، ترتیب وار — ایک مرحلہ مکمل بغیر اگلا نہیں۔ پیچھے لوٹنا مشکل۔ دستاویزات بھاری۔ جہاں ضرورت ثابت ہو (بینک، سرکاری)۔</p>"
              "<p><strong>Agile</strong>: چھوٹے cycles یعنی sprints (عموماً 2–4 ہفتے)۔ مسلسل کسٹمر فیڈ بیک، تبدیلی خوش آمدید۔</p>",
              diagram="waterfallAgile",
              quiz=q("تبدیلی سستے میں کون قبول کرتا ہے؟",
                     ["Waterfall", "Agile", "صرف K-map", "Analog signal"], 1,
                     "Agile iterative ہے، تبدیلی sprint میں سما جاتی ہے۔")),
        ]),
        M("1.3.1-4", "مواصلاتی ماڈل اور OSI سات پرتیں", True, [
            S("★ OSI 7-layer",
              "<p>Communication model بتاتا ہے ڈیٹا ایک آلے سے دوسرے تک کیسے جاتا ہے۔ OSI (Open Systems Interconnection) سات پرتوں کا حوالہ جاتی ماڈل ہے۔</p>"
              "<p>اوپر سے نیچے: 7 Application، 6 Presentation، 5 Session، 4 Transport، 3 Network، 2 Data Link، 1 Physical۔ یادداشت: <span class='ltr'>All People Seem To Need Data Processing</span>۔</p>",
              diagram="osi7",
              tip="ہر پرت کا بنیادی کام ایک جملے میں لکھ کے آئیں۔",
              quiz=q("IP addressing کس OSI پرت کا کام ہے؟",
                     ["Physical", "Transport", "Network", "Application"], 2,
                     "Network layer منطقی پتہ اور routing۔")),
        ]),
        M("1.3.5-6", "TCP/IP بمقابلہ OSI", False, [
            S("چار پرتیں، عملی انٹرنیٹ",
              "<p>TCP/IP عملی ماڈل ہے جو OSI کو سمیٹتا ہے: Application (OSI 5–7)، Transport (4)، Internet (3)، Network Access (1–2)۔ امتحان میں mapping جدول آتی ہے۔</p>",
              diagram="tcpOsi",
              quiz=q("TCP/IP میں کتنی پرتیں؟",
                     ["7", "5", "4", "2"], 2, "چار پرتیں۔")),
        ]),
    ])


def chapter2():
    return ch("ch2", 2, "Computational Thinking اور الگورتھم", [
        M("2.1", "Computational Thinking — حسابی سوچ", False, [
            S("مسئلہ حل کا نظام",
              "<p>Computational Thinking (CT) مسائل کو ترتیب سے حل کرنے کا طریقہ ہے: Decomposition، Pattern Recognition، Abstraction، اور Algorithms۔</p>",
              diagram="decomposition",
              quiz=q("CT کا پہلا عام قدم؟",
                     ["Abstraction", "Decomposition", "Binary search", "IoT"], 1,
                     "پہلے بڑا مسئلہ توڑیں۔")),
        ]),
        M("2.2.2", "Algorithm بمقابلہ Pseudocode", True, [
            S("★ نسخہ اور دستوری زبان",
              "<p><strong>Algorithm</strong>: زبان سے آزاد، قدم بہ قدم منطقی طریقہ — کیا کرنا ہے۔ <strong>Pseudocode</strong>: IF / FOR / WHILE جیسی ساخت سے لکھا گیا قریبی-کوڈ، اصل syntax سے پہلے۔</p>",
              tip="Algorithm خیال ہے؛ Pseudocode اس خیال کی پڑھنے لائق شکل۔",
              quiz=q("Pseudocode کس لیے؟",
                     ["ہارڈویئر جوڑنا", "کوڈ سے پہلے ساخت لکھنا", "شور مٹانا", "OSI پرت"], 1,
                     "ڈیزائن مرحلے میں پڑھنے لائق قدم۔")),
        ]),
        M("2.3.1", "Decomposition — تقسیمِ مسئلہ", True, [
            S("★ توڑو پھر جوڑو",
              "<p> Decomposition پیچیدہ کام کو چھوٹے sub-tasks میں بانٹتی ہے — زبان سیکھنا: الفاظ → گرامر → جملے۔</p>",
              diagram="decomposition",
              quiz=q("بڑے پروجیکٹ کو ماڈیولز میں بانٹنا کیا کہلاتا ہے؟",
                     ["Abstraction", "Decomposition", "Sorting", "Sampling"], 1,
                     "توڑنا = Decomposition۔")),
        ]),
        M("2.3.2", "Pattern Recognition — پیٹرن کی پہچان", False, [
            S("دہرائی پکڑو",
              "<p>Pattern Recognition ڈیٹا میں قاعدہ ڈھونڈنا ہے۔ ستاروں کا مثلث: قطار N میں N ستارے — پانچ print کی بجائے ایک loop۔ پوچھیں: کیا دہرا رہا ہے؟ کیا پیش قیاسی بدل رہا ہے؟</p>",
              quiz=q("ہر قطار میں ایک ستارہ بڑھے تو الگورتھم؟",
                     ["صرف 5 print", "عام loop", "Binary search", "XOR"], 1,
                     "پیٹرن کو loop میں generalize کریں۔")),
        ]),
        M("2.3.3", "Abstraction — خلاصہ", False, [
            S("شور چھپائیں",
              "<p>Abstraction غیر ضروری تفصیل چھپا کر اصل منطق رکھتی ہے۔ چائے: ابالو، پتی، دم، اوندیلو، پیش کرو — کیتلی کا برانڈ اور کپ کا رنگ noise ہے۔</p>",
              quiz=q("Abstraction کیا ہٹاتی ہے؟",
                     ["ضروری قدم", "غیر ضروری تفصیل", "Truth table", "Primary key"], 1,
                     "صرف essence رہتی ہے۔")),
        ]),
        M("2.4.1b", "Bubble Sort — بلبلہ ترتیب", True, [
            S("★ ملحق swap",
              "<p>Bubble sort ملحق عناصر موازنہ کر کے غلط ترتیب پر swap کرتا ہے، پاس دہراتا ہے۔ فہرست: 8, 4, 1, 9, 3۔ سادہ شکل کی پیچیدگی \\(O(n^2)\\)۔</p>",
              diagram="bubbleSort",
              tip="الگورتھم کے steps اور ایک مکمل پاس امتحان میں لکھوائیں۔",
              quiz=q("Bubble sort کس جوڑے کو دیکھتی ہے؟",
                     ["پہلا اور آخری صرف", "ملحق (adjacent)", "صرف درمیان", "رینڈم"], 1,
                     "Adjacent compare-and-swap۔")),
        ]),
        M("2.4.1s", "Selection Sort — انتخابی ترتیب", True, [
            S("★ سب سے چھوٹا چنیں",
              "<p>Selection sort غیر مرتب حصے سے smallest چن کر اگلی پوزیشن پر رکھتی ہے۔ پہلی پوزیشن کے لیے پوری فہرست scan۔</p>",
              diagram="selectionSort",
              quiz=q("Selection sort ہر پاس کیا کرتی ہے؟",
                     ["ملحق swap صرف", "باقی میں سے کم از کم چننا", "درمیان کاٹنا", "Hash"], 1,
                     "Unsorted سے minimum select۔")),
        ]),
        M("2.4.2l", "Linear Search — لکیری تلاش", False, [
            S("ایک ایک کر کے",
              "<p>Linear (sequential) search ہر عنصر چیک کرتی ہے جب تک ہدف نہ ملے۔ Sorted اور unsorted دونوں پر چلتی ہے؛ بدترین \\(O(n)\\)۔</p>",
              quiz=q("Linear search کس فہرست پر چلتی ہے؟",
                     ["صرف sorted", "sorted اور unsorted دونوں", "صرف خالی", "صرف bits"], 1,
                     "ترتیب شرط نہیں۔")),
        ]),
        M("2.4.2b", "Binary Search — ثنائی تلاش", True, [
            S("★ آدھا کاٹو",
              "<p>Binary search صرف <strong>sorted</strong> فہرست پر۔ mid دیکھو؛ چھوٹا ہو تو بائیں، بڑا تو دائیں — پیچیدگی \\(O(\\log n)\\)۔ مثال: [1..8] میں 3 تلاش، mid=4، 3&lt;4 اس لیے بائیں۔</p>",
              diagram="binarySearch",
              tip="شرط بھولنا: data مرتب ہونا لازمی۔",
              quiz=q("Binary search کی شرط؟",
                     ["فہرست sorted ہو", "فہرست خالی ہو", "n &lt; 3", "Agile"], 0,
                     "بغیر ترتیب کے mid بے معنی۔")),
        ]),
        M("2.5-6", "الگورتھم کی جانچ اور انتخاب", False, [
            S("صحیح، تیز، مناسب",
              "<p>Correctness: متوقع نتیجہ، edge cases۔ پھر وقت، میموری، ڈیٹا سائز، sorted ہے یا نہیں، اور پڑھنے کی آسانی۔ چھوٹی فہرست پر \\(O(n^2)\\) بھی ٹھیک؛ بڑی sorted تلاش پر binary۔</p>",
              quiz=q("بڑی sorted فہرست میں تلاش؟",
                     ["Linear ہمیشہ", "Binary search", "Bubble sort", "NOT gate"], 1,
                     "\\(O(\\log n)\\) بہتر۔")),
        ]),
    ])


def chapter3():
    return ch("ch3", 3, "پروگرامنگ کی بنیادیں", [
        M("3.1", "پروگرام اور زبانوں کی اقسام", False, [
            S("کمپیوٹر گونگا ہے",
              "<p>کمپیوٹر بغیر ہدایت سوچ نہیں سکتا۔ ہدایات کا مجموعہ <strong>program</strong> ہے، اور ہدایت دینے والی زبان programming language۔ High-level (Python, C++) انسان کے قریب؛ machine language 0/1۔</p>"
              "<p>C++ طاقتور، ہارڈویئر کے قریب — سسٹم سافٹ ویئر۔ Python سادہ نحو — Data Science، AI، ویب، ابتدائیہ۔</p>",
              quiz=q("Python کو beginner کیوں پسند کرتے ہیں؟",
                     ["صرف اسمبلی ہے", "سادہ readable syntax", "صرف NAND", "OSI 7"], 1,
                     "منطق پر توجہ، پیچیدہ نحو کم۔")),
        ]),
        M("3.2", "Python سے کیریئر", False, [
            S("پاکستان میں دروازے",
              "<p>Software development، Data Science، AI/ML، Django/Flask ویب، آٹومیشن، سائبر سیکیورٹی۔ Python مسئلہ حل پر فوکس رکھتی ہے، نحو رٹنے پر نہیں۔</p>",
              quiz=q("Django کس کام کے قریب؟",
                     ["K-map", "ویب ڈیولپمنٹ", "Analog wave", "Selection sort"], 1,
                     "Python web framework۔")),
        ]),
        M("3.3", "IDE اور VS Code", False, [
            S("ایک چھت تلے کام",
              "<p>IDE: editor، syntax highlighting، auto-complete، run، debugger۔ VS Code ہلکا editor ہے؛ extensions لگا کر Python IDE بن جاتا ہے — File/Edit/Run مینو، نیچے terminal۔</p>",
              quiz=q("Debugger کیا کرتا ہے؟",
                     ["صرف فونٹ بدلا", "غلطیاں ڈھونڈنا/ٹھیک کرنا", "IoT سینسر", "ER oval"], 1,
                     "غلطی کی جگہ روک کر دیکھیں۔")),
        ]),
        M("3.4", "Python پروگرام کی ساخت", True, [
            S("★ بیان، ڈیٹا، نتیجہ",
              "<p>Python پروگرام statements سے ڈیٹا پر عمل کرتا ہے پھر output دکھاتا ہے۔ ترتیب: input → process → output۔</p>",
              diagram="pythonIO",
              tip="print اور متغیر کی پہلی مثال زبانی بتا سکیں۔"),
        ]),
        M("3.4.1", "متغیرات اور Data Types", True, [
            S("★ ڈبہ جس پر نام ہو",
              "<p>Variable میموری کا نام شدہ خانہ ہے۔ Python میں قسم پہلے declare نہیں — value سے type بنتی ہے۔ int، float، str، bool، list۔</p>",
              quiz=q("x = 3.14 کی قسم؟",
                     ["int", "float", "bool", "NAND"], 1, "اعشاریہ = float۔")),
        ]),
        M("3.4.2", "Input اور Output", False, [
            S("print اور input",
              "<p><span class='ltr'>print(\"Hello Class!\")</span> اسکرین پر لکھتا ہے۔ <span class='ltr'>input()</span> صارف سے متن لیتا ہے؛ عدد کے لیے <span class='ltr'>int(input())</span>۔</p>",
              diagram="pythonIO",
              quiz=q("صارف سے عدد لینے کا عام طریقہ؟",
                     ["print صرف", "int(input())", "AND gate", "K-map"], 1,
                     "input سٹرنگ دیتا ہے، int بنانا پڑتا ہے۔")),
        ]),
        M("3.4.3", "Operators اور Operands", True, [
            S("★ عمل اور قیمت",
              "<p>Operand قیمت/متغیر؛ Operator علامت۔ \\(10 + 20\\) میں 10,20 operands، + operator۔ Arithmetic: + − * / // % **۔ Relational: == != &gt; &lt;۔ Logical: and or not۔ Bitwise bits پر: AND &amp;، OR |، XOR ^، NOT ~، shifts۔</p>"
              "<p>Bitwise XOR bits مختلف ہوں تو 1 — منطق XOR گیٹ جیسی۔</p>",
              tip="== موازنہ ہے، = تفویض۔",
              quiz=q("a = 10, b = 5 پر a &gt; b؟",
                     ["False", "True", "10", "Error"], 1, "10 بڑا ہے → True۔")),
        ]),
        M("3.5", "Control Structures — کنٹرول ڈھانچے", True, [
            S("★ ترتیب، انتخاب، دہراؤ",
              "<p>Sequence سیدھی لائن۔ Selection: if / elif / else راستہ چنتی ہے۔ Repetition: for، while شرط تک دہراتی ہے۔ امتحان میں loop کو کاغذ پر trace کریں۔</p>",
              quiz=q("if-elif-else کیا ہے؟",
                     ["تلاش الگورتھم", "Selection", "IoT", "Primary key"], 1,
                     "شرط کے مطابق شاخ۔")),
        ]),
        M("3.6", "لائبریریز اور غلطیاں", False, [
            S("Ready-made اوزار",
              "<p>Built-in: math، random، datetime۔ Third-party: pip سے numpy، pandas۔ غلطیاں: Syntax (لکھائی)، Runtime (چلتے ہوئے)، Logic (چلتا ہے مگر جواب غلط)۔ Traceback بتاتا ہے قسم اور لائن۔</p>",
              quiz=q("پروگرام چلے مگر جواب غلط ہو تو؟",
                     ["Syntax error", "Logic error", "Golden gate", "OSI 1"], 1,
                     "منطق میں خامی۔")),
        ]),
    ])


def chapter4():
    return ch("ch4", 4, "ڈیٹا بیس", [
        M("4.1-2", "ڈیٹا بیس اور اجزاء", False, [
            S("ٹیبل سے شروع",
              "<p>Database منظم ذخیرہ ہے۔ بنیادی ڈھانچہ table: قطاریں = records، کالم = fields/attributes۔ DBMS ان اشیاء کو سنبھالتا ہے۔</p>",
              quiz=q("Table کی قطار کو کیا کہتے ہیں؟",
                     ["Field", "Record", "Query", "Form"], 1, "ایک ریکارڈ ایک قطار۔")),
        ]),
        M("4.3", "Keys اور Integrity", True, [
            S("★ شناخت اور رشتہ",
              "<p>Primary Key ریکارڈ منفرد شناخت — NULL/duplicate نہیں۔ Candidate keys میں سے ایک PK بنتی ہے، باقی Alternate۔ Foreign Key دوسری ٹیبل کی PK کی طرف اشارہ — رشتہ جوڑتی ہے، duplicate/NULL ہو سکتے ہیں۔</p>"
              "<p>RDBMS کئی ٹیبلز + keys؛ redundancy کم، SQL سے سوال، کئی صارف۔</p>",
              diagram="keys",
              tip="PK vs FK جدول زبانی۔",
              quiz=q("Foreign Key کیا کرتی ہے؟",
                     ["ہمیشہ unique ہوتی ہے", "دو ٹیبلز جوڑتی ہے", "Analog بناتی ہے", "Sort کرتی ہے"], 1,
                     "دوسری ٹیبل کی PK کا حوالہ۔")),
        ]),
        M("4.4", "ER-Model — وجودی تعلق کا خاکہ", True, [
            S("★ معمار کا نقشہ",
              "<p>ER Model ڈیٹا بیس سے پہلے تصوراتی ڈیزائن: Entity (مستطیل)، Attribute (بیضوی)، Relationship (لوزی)۔ تعلق: 1:1، 1:M، M:N۔</p>",
              diagram="erModel",
              quiz=q("Entity کی علامت؟",
                     ["Oval", "Rectangle", "Diamond", "Circle bit"], 1,
                     "مستطیل = entity۔")),
        ]),
        M("4.5", "Referential Integrity — حوالہ جاتی درستگی", True, [
            S("★ یتیم ریکارڈ نہیں",
              "<p>Referential integrity یقینی بناتی ہے FK کی value اصل PK میں موجود ہو۔ Cascade Update: PK بدلی تو FK خود۔ Cascade Delete: parent گیا تو متعلقہ child۔</p>",
              tip="Library میں Member حذف تو BorrowRecord؟ پالیسی لکھیں۔",
              quiz=q("Cascade Delete کیا کرتا ہے؟",
                     ["صرف فونٹ", "والد کے ساتھ بچے ریکارڈ ختم", "K-map", "Sprint"], 1,
                     "تعلق برقرار رکھنے کے لیے خودکار حذف۔")),
        ]),
        M("4.6-7", "Relational Schema اور لائبریری کیس", False, [
            S("M:N کو توڑیں",
              "<p>Schema ٹیبل کا خاکہ ہے۔ لائبریری: Member، Book؛ M:N borrow براہ راست نہیں — BorrowRecord پل ٹیبل: Member 1:M BorrowRecord، Book 1:M BorrowRecord۔</p>",
              diagram="erModel",
              quiz=q("M:N کو relational میں کیسے؟",
                     ["نظر انداز", "associative/bridge table", "صرف Analog", "NAND"], 1,
                     "درمیانی entity۔")),
        ]),
        M("4.8-11", "Objects، Forms، Queries، Charts", True, [
            S("★ سوال پوچھو، دیکھ کر بھرو",
              "<p>Objects: Table، Query، Form، Report، Chart۔ Form اندراج کا انٹرفیس — غلطی کم۔ Query ڈیٹا چھانتی ہے بغیر اصل ٹیبل بدلے؛ Criteria سے فلٹر؛ Grouping سے مجموعہ۔ Charts: Bar موازنہ، Pie تناسب۔</p>",
              tip="Query اصل ڈیٹا نہیں مٹاتی — پوچھتی ہے۔",
              quiz=q("Access میں مخصوص قطاریں دیکھنے کا اوزار؟",
                     ["صرف Paint", "Query", "OSI", "Ramp"], 1,
                     "Query فلٹر/تلاش۔")),
        ]),
    ])


def chapter5():
    return ch("ch5", 5, "کمپیوٹنگ کے اثرات", [
        M("5.1.1", "مصنوعی ذہانت (AI)", True, [
            S("★ ڈیٹا سے فیصلے",
              "<p>AI مشینوں کو انسانی جیسے کام (پہچان، پیش گوئی، سفارش) سکھاتی ہے۔ پاکستان میں LMS، خودکار مارکنگ، کیریئر مشورہ — فائدہ: اپنی رفتار، مدد درکار طلبہ، disability support۔ چیلنج: دیہی انٹرنیٹ، آلات، استاد تربیت، پرائیویسی۔</p>",
              tip="فائدے اور پاکستانی چیلنج دونوں لکھیں۔",
              quiz=q("AI تعلیم میں ایک فائدہ؟",
                     ["انٹرنیٹ ختم", "ذاتی رفتار سے سیکھنا", "Bits ختم", "OSI 8"], 1,
                     "خودکار مدد اور رفتار۔")),
        ]),
        M("5.1.2", "IoT — انٹرنیٹ آف تھنگز", True, [
            S("★ چیزیں بات کرتی ہیں",
              "<p>IoT: فیزیکی آلات انٹرنیٹ سے جڑ کر ڈیٹا بھیجتے ہیں۔ اجزاء: Sensors، Connectivity (Wi-Fi/4G)، Data processing، Actuators/User interface۔</p>",
              diagram="iot",
              quiz=q("بغیر connectivity IoT؟",
                     ["بہتر ہوتا ہے", "سینسر سسٹم سے بات نہیں کر سکتا", "صرف K-map", "Primary key"], 1,
                     "رابطہ ضروری۔")),
        ]),
        M("5.1.3-2", "Data Analytics اور IoT کے استعمال", False, [
            S("صاف کرو، پڑھو، بتاؤ",
              "<p>Analytics: جمع، ترتیب، صفائی، مطالعہ، پیشکش۔ IoT: صحت، زراعت، ٹریفک، اسمارٹ کلاس، بایومیٹرک حاضری۔ کیریئر: IoT Engineer، Data Analyst — Python، نیٹ ورکنگ، سینسرز۔</p>",
              diagram="iot",
              quiz=q("Data analysis کا مقصد؟",
                     ["شور بڑھانا", "پیٹرن/معلومات نکلنا", "گیٹ توڑنا", "NULL PK"], 1,
                     "فیصلے کے لیے insight۔")),
        ]),
        M("5.3", "معلومات کے ذرائع", True, [
            S("★ تین پرتیں",
              "<p>Primary: اصل، firsthand — انٹرویو، تصویر، ڈائری، NADRA ریکارڈ۔ Secondary: کسی کی تشریح — کتاب، خبر، تحقیقی مقالہ۔ Tertiary: خلاصہ فہرست — انسائیکلوپیڈیا، انڈیکس۔ انٹرنیٹ وسیع ہے، سب درست نہیں۔</p>",
              tip="امتحان میں ہر قسم کی 2 مثالیں۔",
              quiz=q("NADRA ریکارڈ کون سا ماخذ؟",
                     ["Tertiary", "Primary", "صرف Agile", "Analog"], 1,
                     "سرکاری اصل ریکارڈ = primary۔")),
        ]),
        M("5.4-5", "سماجی اثرات اور Assistive Tech", True, [
            S("★ شمولیت",
              "<p>کمپیوٹنگ رفتار اور رابطہ بڑھاتی ہے مگر پرائیویسی کے خطرات بھی۔ Assistive technologies معذوری والے افراد کو برابر رسائی دیتی ہیں: screen readers، speech-to-text۔ تعلیم میں نابینا طلبہ ڈیجیٹل کتاب پڑھ سکتے ہیں۔</p>",
              quiz=q("Screen reader کسے مدد دیتا ہے؟",
                     ["صرف پرنٹر", "نابینا/کم بینا صارف", "XOR گیٹ", "Waterfall"], 1,
                     "متن کو آواز۔")),
        ]),
    ])


def chapter6():
    return ch("ch6", 6, "ڈیجیٹل خواندگی", [
        M("6.1-2", "Digital Literacy کیا ہے؟", False, [
            S("محفوظ اور سمجھ دار استعمال",
              "<p>Digital literacy: ڈیوائس، انٹرنیٹ، آن لائن اوزار کو محفوظ، مؤثر، ذمہ دار طریقے سے سمجھنا اور استعمال کرنا — صرف ٹیپ نہیں، سوچ۔</p>",
              quiz=q("Digital literacy کا حصہ؟",
                     ["صرف گیم", "محفوظ مؤثر آن لائن استعمال", "صرف NAND", "Gray code"], 1,
                     "سمجھ + حفاظت + اوزار۔")),
        ]),
        M("6.3", "Qualitative بمقابلہ Quantitative", True, [
            S("★ دو قسم کا ڈیٹا",
              "<p>Qualitative: زمرے/الفاظ — رنگ، رائے، ہاں/نہیں۔ Quantitative: اعداد — عمر، مارکس، گھنٹے۔ سروے ڈیزائن سے پہلے فیصلہ کریں۔</p>",
              diagram="dataTypes",
              tip="سوال کی قسم بتائے ڈیٹا کی قسم۔",
              quiz=q("روزانہ فون کے گھنٹے؟",
                     ["Qualitative", "Quantitative", "XOR", "Tertiary"], 1,
                     "عدد = quantitative۔")),
        ]),
        M("6.4", "ڈیٹا جمع کی حکمت عملی", True, [
            S("★ خود اصل معلومات",
              "<p>موجودہ معلومات ڈھونڈنا کافی نہیں — سروے، مشاہدہ، تجربہ، prototype (ابتدائی ماڈل تاکہ مہنگے بنانے سے پہلے ٹیسٹ)۔</p>",
              quiz=q("Prototype کیا ہے؟",
                     ["حتمی پروڈکٹ", "آزمائشی ابتدائی ورژن", "Primary key", "OSI 7"], 1,
                     "جلد ٹیسٹ، سستا سبق۔")),
        ]),
        M("6.5", "Primary اور Secondary ڈیٹا", True, [
            S("★ کنٹرول کس کا؟",
              "<p>Primary: آپ خود جمع — کنٹرول زیادہ، وقت/لاگت زیادہ۔ Secondary: پہلے سے موجود — تیز، سستا، مگر مقصد کسی اور کا ہو سکتا ہے۔</p>",
              quiz=q("Secondary data کا فائدہ؟",
                     ["ہمیشہ 100٪ درست", "تیز اور اکثر سستا", "صرف analog", "Cascade delete"], 1,
                     "موجودہ ماخذ استعمال۔")),
        ]),
        M("6.7", "ڈیجیٹل اوزار سے پیشکش", False, [
            S("چارٹ اور infographic",
              "<p>جمع کرنا آدھا کام ہے۔ Spreadsheet، گراف، infographic سے لوگ فوراً سمجھیں۔ Infographic: حقائق + تصویر + مختصر متن۔</p>",
              quiz=q("Infographic کا مقصد؟",
                     ["صرف کوڈ compile", "جلدی سمجھ آنے والی بصری کہانی", "Gate delay", "NULL FK"], 1,
                     "بصری خلاصہ۔")),
        ]),
        M("6.8", "کیس اسٹڈی: Digital Inquiry", True, [
            S("★ بارہ قدم، ایک artefact",
              "<p>مسئلہ: اسکرین ٹائم اور توجہ۔ Advanced search → سروے (consent، گمنامی) → secondary مضمون سے موازنہ → spreadsheet → چارٹ → نتیجہ → digital artefact (سلائیڈ/پوسٹر/ویڈیو)۔ اخلاقیات: اجازت، حساس ڈیٹا نہیں، صرف تعلیمی استعمال۔</p>",
              tip="Consent اور anonymity کے جملے رٹ لیں۔",
              quiz=q("سروے سے پہلے کیا لازمی؟",
                     ["Cascade XOR", "رضامندی (consent)", "NAND universal", "Waterfall صرف"], 1,
                     "اخلاقی تحقیق کی بنیاد۔")),
        ]),
    ])


def main():
    data = {
        "meta": {
            "title": "کمپیوٹر سائنس XI — خود سیکھو ایڈیشن",
            "edition": "Teach Yourself · Urdish lectures · Sindh 2026",
            "tts": "ur",
        },
        "chapters": [
            chapter1(),
            chapter2(),
            chapter3(),
            chapter4(),
            chapter5(),
            chapter6(),
        ],
    }
    out = Path(__file__).resolve().parents[1] / "teach-yourself" / "js" / "curriculum.js"
    payload = json.dumps(data, ensure_ascii=False, indent=2)
    js = f"""/** CS XI Teach Yourself — Urdish-only lectures (Sindh Curriculum 2026). */
const COACH_LINES = {json.dumps(COACH, ensure_ascii=False, indent=2)};

const CURRICULUM = {payload};

function allModules() {{
  const list = [];
  for (const ch of CURRICULUM.chapters) {{
    for (const m of ch.modules) list.push({{ chapter: ch, module: m }});
  }}
  return list;
}}

window.COACH_LINES = COACH_LINES;
window.CURRICULUM = CURRICULUM;
window.allModules = allModules;
"""
    out.write_text(js, encoding="utf-8")
    mods = sum(len(c["modules"]) for c in data["chapters"])
    slides = sum(len(m["slides"]) for c in data["chapters"] for m in c["modules"])
    print(f"wrote {out} modules={mods} slides={slides}")


if __name__ == "__main__":
    main()
