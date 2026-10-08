/** CS XI Teach Yourself — Urdish-only lectures (Sindh Curriculum 2026). */
const COACH_LINES = [
  "آپ آ گئے — یہ سب سے مشکل قدم تھا۔ ایک سلائیڈ، ایک تصور۔",
  "★ سنہری موضوعات امتحان میں بار بار آتے ہیں۔ انہیں زور سے پڑھیں۔",
  "فارمولا دیکھیں، مثال بنائیں، پھر خود آزمائی حل کریں۔",
  "Urdish میں سنیں: اردو وضاحت، انگریزی اصطلاح (AND, OSI, SDLC) ویسی کی ویسی۔",
  "دو منٹ ٹھہریں — دماغ گرم ہو رہا ہے۔"
];

const CURRICULUM = {
  "meta": {
    "title": "کمپیوٹر سائنس XI — خود سیکھو ایڈیشن",
    "edition": "Teach Yourself · Urdish lectures · Sindh 2026",
    "tts": "ur"
  },
  "chapters": [
    {
      "id": "ch1",
      "number": 1,
      "title": "کمپیوٹر سسٹمز",
      "modules": [
        {
          "id": "1.1.1",
          "title": "Discrete اور Continuous مقداریں",
          "golden": false,
          "slides": [
            {
              "headline": "سبق کا ہدف",
              "body": "<div class=\"objectives\"><p>اس سبق کے بعد آپ <strong>Discrete</strong> اور <strong>Continuous</strong> مقداروں میں فرق بتا سکیں گے، اور سیڑھی/ ramp کی مشابہت سے امتحانی مثال لکھ سکیں گے۔</p></div><p>Discrete مقدار الگ الگ، گننے کے قابل ہوتی ہے — کلاس میں طلبہ، پارکنگ میں گاڑیاں۔ Continuous مقدار کسی حد میں کوئی بھی قیمت لے سکتی ہے — پانی کا درجہ حرارت، چلتی گاڑی کی رفتار۔</p>",
              "narrator": "سبق کا ہدف۔   اس سبق کے بعد آپ Discrete اور Continuous مقداروں میں فرق بتا سکیں گے، اور سیڑھی/ ramp کی مشابہت سے امتحانی مثال لکھ سکیں گے۔   Discrete مقدار الگ الگ، گننے کے قابل ہوتی ہے — کلاس میں طلبہ، پارکنگ میں گاڑیاں۔ Continuous مقدار کسی حد میں کوئی بھی قیمت لے سکتی ہے — پانی کا درجہ حرارت، چلتی گاڑی کی رفتار۔ ",
              "diagram": "stairsRamp",
              "quiz": null,
              "tip": null,
              "coach": null
            },
            {
              "headline": "سیڑھیاں بمقابلہ ramp",
              "body": "<p>سیڑھیاں Discrete ہیں: ہر قدم مقرر۔ Ramp Continuous ہے: کوئی بھی نقطہ ممکن۔ کمپیوٹر Discrete bits استعمال کرتا ہے، اس لیے Continuous دنیا کو sample کر کے Discrete بنایا جاتا ہے۔</p>",
              "narrator": "سیڑھیاں بمقابلہ ramp۔  سیڑھیاں Discrete ہیں: ہر قدم مقرر۔ Ramp Continuous ہے: کوئی بھی نقطہ ممکن۔ کمپیوٹر Discrete bits استعمال کرتا ہے، اس لیے Continuous دنیا کو sample کر کے Discrete بنایا جاتا ہے۔ ",
              "diagram": null,
              "quiz": {
                "q": "گاڑی کی رفتار کون سی مقدار ہے؟",
                "options": [
                  "Discrete",
                  "Continuous",
                  "Boolean",
                  "Minterm"
                ],
                "answer": 1,
                "explain": "رفتار حد میں کوئی بھی قیمت لے سکتی ہے، لہٰذا Continuous۔"
              },
              "tip": "سوال میں 'گننا' آئے تو Discrete، 'پیمانہ/بہاؤ' آئے تو Continuous۔",
              "coach": null
            }
          ]
        },
        {
          "id": "1.1.2",
          "title": "ڈیجیٹل سسٹمز کا تعارف",
          "golden": false,
          "slides": [
            {
              "headline": "صرف دو حالتیں",
              "body": "<p>Digital system الیکٹرانک نظام ہے جو صرف دو values استعمال کرتا ہے: <strong>0</strong> = OFF / LOW / FALSE اور <strong>1</strong> = ON / HIGH / TRUE۔ انہیں binary digits یا <strong>bits</strong> کہتے ہیں۔</p><p>فائدے: Reliable (شور سے کم اثر)، Accurate (کاپی پر معیار نہیں گرتا)، Easy to Design (صرف دو states)، Programmable (سافٹ ویئر سے کنٹرول)۔</p>",
              "narrator": "صرف دو حالتیں۔  Digital system الیکٹرانک نظام ہے جو صرف دو values استعمال کرتا ہے: 0 = OFF / LOW / FALSE اور 1 = ON / HIGH / TRUE۔ انہیں binary digits یا bits کہتے ہیں۔  فائدے: Reliable (شور سے کم اثر)، Accurate (کاپی پر معیار نہیں گرتا)، Easy to Design (صرف دو states)، Programmable (سافٹ ویئر سے کنٹرول)۔ ",
              "diagram": "binaryBits",
              "quiz": null,
              "tip": null,
              "coach": null
            },
            {
              "headline": "روزمرہ مثالیں",
              "body": "<p>کمپیوٹر، اسمارٹ فون، ڈیجیٹل کیمرہ — سب photos اور music کو 0 اور 1 کے binary data کی صورت میں رکھتے ہیں۔</p>",
              "narrator": "روزمرہ مثالیں۔  کمپیوٹر، اسمارٹ فون، ڈیجیٹل کیمرہ — سب photos اور music کو 0 اور 1 کے binary data کی صورت میں رکھتے ہیں۔ ",
              "diagram": null,
              "quiz": {
                "q": "Digital system میں 1 کیا ظاہر کرتا ہے؟",
                "options": [
                  "OFF / FALSE",
                  "ON / HIGH / TRUE",
                  "Sine wave",
                  "Noise"
                ],
                "answer": 1,
                "explain": "1 = ON, HIGH, TRUE۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "1.1.3",
          "title": "Analog اور Digital سگنل",
          "golden": true,
          "slides": [
            {
              "headline": "★ سنہری: دو لہریں",
              "body": "<div class=\"objectives\"><p>امتحانی جدول یاد کریں: فطرت اور Reliability۔</p></div><p><strong>Analog signal</strong> وقت کے ساتھ ہموار بدلتا ہے، جیسے sine wave — انسانی آواز، پرانا تھرمامیٹر۔</p><p><strong>Digital signal</strong> صرف HIGH(1) اور LOW(0) — فوری چھلانگ، square wave — کمپیوٹر ڈیٹا۔</p>",
              "narrator": "★ سنہری: دو لہریں۔   امتحانی جدول یاد کریں: فطرت اور Reliability۔   Analog signal وقت کے ساتھ ہموار بدلتا ہے، جیسے sine wave — انسانی آواز، پرانا تھرمامیٹر۔  Digital signal صرف HIGH(1) اور LOW(0) — فوری چھلانگ، square wave — کمپیوٹر ڈیٹا۔ ",
              "diagram": "analogDigitalWaves",
              "quiz": null,
              "tip": "Analog: Continuous flow، شور سے متاثر۔ Digital: Discrete bits، شور کے خلاف مضبوط۔",
              "coach": null
            },
            {
              "headline": "موازنہ کی جدول",
              "body": "<p>Nature: Analog = مسلسل بہاؤ؛ Digital = الگ bits۔ Reliability: Analog کم، Digital زیادہ۔ امتحان میں یہ دو قطاریں اکثر آتی ہیں۔</p>",
              "narrator": "موازنہ کی جدول۔  Nature: Analog = مسلسل بہاؤ؛ Digital = الگ bits۔ Reliability: Analog کم، Digital زیادہ۔ امتحان میں یہ دو قطاریں اکثر آتی ہیں۔ ",
              "diagram": null,
              "quiz": {
                "q": "Square wave کس سگنل کی پہچان ہے؟",
                "options": [
                  "Analog",
                  "Digital",
                  "Continuous temperature",
                  "Ramp"
                ],
                "answer": 1,
                "explain": "Digital سگنل HIGH/LOW کے درمیان مربع لہر بناتا ہے۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "1.1.4-6",
          "title": "Boolean Algebra، عملیات اور Truth Table",
          "golden": false,
          "slides": [
            {
              "headline": "George Boole کی الجبرا",
              "body": "<p>Boolean algebra صرف TRUE (1) اور FALSE (0) پر کام کرتی ہے — digital electronics اور programming کی بنیاد۔</p><p>Variables: A, B, C حروف جو 0 یا 1 رکھتے ہیں۔ Operations: AND، OR، NOT۔ Expression: متغیرات + عملیات، جیسے \\(Y = A + B\\)۔</p>",
              "narrator": "George Boole کی الجبرا۔  Boolean algebra صرف TRUE (1) اور FALSE (0) پر کام کرتی ہے — digital electronics اور programming کی بنیاد۔  Variables: A, B, C حروف جو 0 یا 1 رکھتے ہیں۔ Operations: AND، OR، NOT۔ Expression: متغیرات + عملیات، جیسے \\(Y = A + B\\)۔ ",
              "diagram": null,
              "quiz": null,
              "tip": null,
              "coach": null
            },
            {
              "headline": "تین بنیادی عملیات",
              "body": "<p>AND \\(Y = A \\cdot B\\): آؤٹ پٹ 1 صرف جب تمام ان پٹ 1 — دو تالے والا دروازہ دونوں کھلیں تو کھلتا ہے۔</p><p>OR \\(Y = A + B\\): کوئی ایک ان پٹ 1 — کمرے کے دو دروازوں میں سے کوئی کھلا ہو۔</p><p>NOT \\(Y = A'\\): unary، ان پٹ الٹ — سوئچ ON تو روشنی، OFF تو اندھیرا۔</p>",
              "narrator": "تین بنیادی عملیات۔  AND \\(Y = A \\cdot B\\): آؤٹ پٹ 1 صرف جب تمام ان پٹ 1 — دو تالے والا دروازہ دونوں کھلیں تو کھلتا ہے۔  OR \\(Y = A + B\\): کوئی ایک ان پٹ 1 — کمرے کے دو دروازوں میں سے کوئی کھلا ہو۔  NOT \\(Y = A'\\): unary، ان پٹ الٹ — سوئچ ON تو روشنی، OFF تو اندھیرا۔ ",
              "diagram": "gateAND",
              "quiz": null,
              "tip": null,
              "coach": null
            },
            {
              "headline": "Truth table کیسے بنے",
              "body": "<p>1) ان پٹ گنیں \\(n\\)۔ 2) قطاریں \\(2^n\\)۔ 3) binary ترتیب میں تمام combinations۔ 4) ہر قطار کا آؤٹ پٹ۔ دو ان پٹ = 4 قطاریں؛ تین = 8۔</p>",
              "narrator": "Truth table کیسے بنے۔  1) ان پٹ گنیں \\(n\\)۔ 2) قطاریں \\(2^n\\)۔ 3) binary ترتیب میں تمام combinations۔ 4) ہر قطار کا آؤٹ پٹ۔ دو ان پٹ = 4 قطاریں؛ تین = 8۔ ",
              "diagram": "truthTable2",
              "quiz": {
                "q": "3 ان پٹ کی truth table میں کتنی قطاریں؟",
                "options": [
                  "3",
                  "6",
                  "8",
                  "9"
                ],
                "answer": 2,
                "explain": "\\(2^3 = 8\\)۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "1.1.7",
          "title": "بنیادی Logic Gates (AND, OR, NOT)",
          "golden": true,
          "slides": [
            {
              "headline": "★ گیٹس یعنی سرکٹ کی اینٹیں",
              "body": "<p>Logic gates الیکٹرانک سرکٹس ہیں جو Boolean عملیات کرتے ہیں۔ تمام digital systems انہی سے بنتے ہیں۔</p><p>AND: \\(Y = A \\cdot B\\)۔ OR: \\(Y = A + B\\)۔ NOT: \\(Y = A'\\)۔</p>",
              "narrator": "★ گیٹس یعنی سرکٹ کی اینٹیں۔  Logic gates الیکٹرانک سرکٹس ہیں جو Boolean عملیات کرتے ہیں۔ تمام digital systems انہی سے بنتے ہیں۔  AND: \\(Y = A \\cdot B\\)۔ OR: \\(Y = A + B\\)۔ NOT: \\(Y = A'\\)۔ ",
              "diagram": "gatesOverview",
              "quiz": null,
              "tip": "گیٹ کا نام، علامت، expression، اور 4-قطار truth table — چاروں یاد کریں۔",
              "coach": null
            },
            {
              "headline": "AND تفصیل",
              "body": "<p>آؤٹ پٹ 1 صرف A=1 اور B=1 پر۔ باقی تین combinations پر 0۔</p>",
              "narrator": "AND تفصیل۔  آؤٹ پٹ 1 صرف A=1 اور B=1 پر۔ باقی تین combinations پر 0۔ ",
              "diagram": "gateAND",
              "quiz": null,
              "tip": null,
              "coach": null
            },
            {
              "headline": "OR اور NOT",
              "body": "<p>OR کسی ایک 1 پر 1 دیتا ہے۔ NOT صرف ایک ان پٹ الٹ کرتا ہے۔</p>",
              "narrator": "OR اور NOT۔  OR کسی ایک 1 پر 1 دیتا ہے۔ NOT صرف ایک ان پٹ الٹ کرتا ہے۔ ",
              "diagram": "gateOR",
              "quiz": {
                "q": "AND گیٹ 1 کب دیتا ہے؟",
                "options": [
                  "کوئی ایک ان پٹ 1",
                  "تمام ان پٹ 1",
                  "ان پٹ مختلف",
                  "ہمیشہ"
                ],
                "answer": 1,
                "explain": "AND = سب 1 تبھی 1۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "1.1.7u",
          "title": "یونیورسل اور اعلیٰ گیٹس",
          "golden": false,
          "slides": [
            {
              "headline": "NAND اور NOR یونیورسل ہیں",
              "body": "<p>NAND یعنی NOT AND: \\(Y = (A \\cdot B)'\\)۔ NOR یعنی NOT OR: \\(Y = (A + B)'\\)۔ دنیا کا کوئی بھی logic circuit صرف NAND یا صرف NOR سے بنایا جا سکتا ہے — اس لیے Universal Gates۔</p>",
              "narrator": "NAND اور NOR یونیورسل ہیں۔  NAND یعنی NOT AND: \\(Y = (A \\cdot B)'\\)۔ NOR یعنی NOT OR: \\(Y = (A + B)'\\)۔ دنیا کا کوئی بھی logic circuit صرف NAND یا صرف NOR سے بنایا جا سکتا ہے — اس لیے Universal Gates۔ ",
              "diagram": "gateNAND",
              "quiz": null,
              "tip": null,
              "coach": null
            },
            {
              "headline": "XOR اور XNOR",
              "body": "<p>XOR: ان پٹ <em>eXclusively</em> مختلف ہوں تو 1، \\(Y = A \\oplus B\\)۔ XNOR: ان پٹ ایک جیسے ہوں تو 1، \\(Y = (A \\oplus B)'\\)۔</p>",
              "narrator": "XOR اور XNOR۔  XOR: ان پٹ <em>eXclusively</em> مختلف ہوں تو 1، \\(Y = A \\oplus B\\)۔ XNOR: ان پٹ ایک جیسے ہوں تو 1، \\(Y = (A \\oplus B)'\\)۔ ",
              "diagram": "gateXOR",
              "quiz": {
                "q": "کون سے گیٹس Universal ہیں؟",
                "options": [
                  "AND اور OR",
                  "NAND اور NOR",
                  "XOR اور XNOR",
                  "NOT صرف"
                ],
                "answer": 1,
                "explain": "صرف NAND یا صرف NOR سے پورا سرکٹ ممکن۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "1.1.8-11",
          "title": "Expressions، Minterms اور Logic Diagram",
          "golden": false,
          "slides": [
            {
              "headline": "ترتیبِ اولویت",
              "body": "<p>Order of precedence: 1) Parentheses \\((\\,\\)\\) 2) NOT \\((\\,'\\,)\\) 3) AND \\((\\cdot)\\) 4) OR \\((+)\\)۔ پہلے اونچی اولویت کا گیٹ کھینچیں۔</p><p>Minterm (SOP): وہ product جو truth table کی ایک قطار پر 1 ہو۔ Maxterm (POS): وہ sum جو 0 والی قطار پر ہو۔ مثال SOP: \\(Y = A'B + AB\\)۔</p>",
              "narrator": "ترتیبِ اولویت۔  Order of precedence: 1) Parentheses \\((\\,\\)\\) 2) NOT \\((\\,'\\,)\\) 3) AND \\((\\cdot)\\) 4) OR \\((+)\\)۔ پہلے اونچی اولویت کا گیٹ کھینچیں۔  Minterm (SOP): وہ product جو truth table کی ایک قطار پر 1 ہو۔ Maxterm (POS): وہ sum جو 0 والی قطار پر ہو۔ مثال SOP: \\(Y = A'B + AB\\)۔ ",
              "diagram": null,
              "quiz": null,
              "tip": null,
              "coach": null
            },
            {
              "headline": "★ Logic diagram",
              "body": "<p>مثال \\(Y = A \\cdot B + C\\)۔ AND کی اولویت OR سے زیادہ، اس لیے پہلے AND گیٹ، اس کا آؤٹ پٹ C کے ساتھ OR۔</p>",
              "narrator": "★ Logic diagram۔  مثال \\(Y = A \\cdot B + C\\)۔ AND کی اولویت OR سے زیادہ، اس لیے پہلے AND گیٹ، اس کا آؤٹ پٹ C کے ساتھ OR۔ ",
              "diagram": "logicDiagram",
              "quiz": {
                "q": "Y = A · B + C میں پہلے کون سا گیٹ؟",
                "options": [
                  "OR",
                  "AND",
                  "NOT",
                  "XOR"
                ],
                "answer": 1,
                "explain": "AND کی اولویت زیادہ۔"
              },
              "tip": "ڈایاگرام میں precedence بھولنا عام غلطی ہے۔",
              "coach": null
            }
          ]
        },
        {
          "id": "1.1.13",
          "title": "K-Maps — کارنو نقشے",
          "golden": true,
          "slides": [
            {
              "headline": "★ K-Map کیا ہے؟",
              "body": "<p>K-map Boolean expression کو سادہ کرنے کا گرافیکل ٹول ہے۔ Grid میں ملحق خانے Gray code سے صرف ایک bit مختلف ہوتے ہیں۔ 1s کو 2 کی طاقتوں (1, 2, 4, 8) میں گروپ کریں — الجبرا کے بغیر سادہ term ملتی ہے۔</p><p>دو متغیر: \\(2^2 = 4\\) خانے۔ تین متغیر: \\(2^3 = 8\\) خانے۔ کالم ترتیب: 00, 01, 11, 10۔</p>",
              "narrator": "★ K-Map کیا ہے؟۔  K-map Boolean expression کو سادہ کرنے کا گرافیکل ٹول ہے۔ Grid میں ملحق خانے Gray code سے صرف ایک bit مختلف ہوتے ہیں۔ 1s کو 2 کی طاقتوں (1, 2, 4, 8) میں گروپ کریں — الجبرا کے بغیر سادہ term ملتی ہے۔  دو متغیر: \\(2^2 = 4\\) خانے۔ تین متغیر: \\(2^3 = 8\\) خانے۔ کالم ترتیب: 00, 01, 11, 10۔ ",
              "diagram": "kmap3var",
              "quiz": {
                "q": "3-variable K-map میں خانے؟",
                "options": [
                  "3",
                  "4",
                  "6",
                  "8"
                ],
                "answer": 3,
                "explain": "\\(2^3 = 8\\)۔"
              },
              "tip": "گروپ میں wrap-around (کنارے جوڑ) جائز ہے۔",
              "coach": null
            }
          ]
        },
        {
          "id": "logisim",
          "title": "Logisim Evolution گائیڈ",
          "golden": false,
          "slides": [
            {
              "headline": "پہلے simulate، پھر سرکٹ",
              "body": "<p>Logisim Evolution گرافیکل ٹول ہے: گیٹس رکھیں، تار جوڑیں، truth table آنکھوں سے چیک کریں — ہارڈویئر کے بغیر۔</p><p>\\(Y = A \\cdot B\\): Toolbar سے AND، دو Input pins، ایک Output، تار جوڑیں، Poke tool سے 0/1 بدلیں۔</p>",
              "narrator": "پہلے simulate، پھر سرکٹ۔  Logisim Evolution گرافیکل ٹول ہے: گیٹس رکھیں، تار جوڑیں، truth table آنکھوں سے چیک کریں — ہارڈویئر کے بغیر۔  \\(Y = A \\cdot B\\): Toolbar سے AND، دو Input pins، ایک Output، تار جوڑیں، Poke tool سے 0/1 بدلیں۔ ",
              "diagram": "logisim",
              "quiz": {
                "q": "Logisim میں ان پٹ 0/1 کیسے ٹیسٹ کریں؟",
                "options": [
                  "صرف print()",
                  "Poke tool",
                  "K-map",
                  "SDLC"
                ],
                "answer": 1,
                "explain": "Poke سے pins ٹوگل ہوتی ہیں۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "1.2.1-3",
          "title": "SDLC — سافٹ ویئر لائف سائیکل",
          "golden": true,
          "slides": [
            {
              "headline": "★ ساخت یافتہ سفر",
              "body": "<p>SDLC سافٹ ویئر کو شروع سے انجام تک لے جانے کا structured process ہے: واضح اہداف، بہتر منصوبہ، کم نقائص۔</p><p>مراحل: Requirement Analysis → Design → Implementation/Coding → Testing → Deployment → Maintenance۔ ہر مرحلے کا deliverable ہوتا ہے (دستاویز، ماڈل، کوڈ، رپورٹ)۔</p>",
              "narrator": "★ ساخت یافتہ سفر۔  SDLC سافٹ ویئر کو شروع سے انجام تک لے جانے کا structured process ہے: واضح اہداف، بہتر منصوبہ، کم نقائص۔  مراحل: Requirement Analysis → Design → Implementation/Coding → Testing → Deployment → Maintenance۔ ہر مرحلے کا deliverable ہوتا ہے (دستاویز، ماڈل، کوڈ، رپورٹ)۔ ",
              "diagram": "sdlc",
              "quiz": {
                "q": "SDLC کا پہلا مرحلہ؟",
                "options": [
                  "Testing",
                  "Deployment",
                  "Requirement Analysis",
                  "Maintenance"
                ],
                "answer": 2,
                "explain": "پہلے ضروریات سمجھیں پھر ڈیزائن۔"
              },
              "tip": "مراحل کے نام ترتیب سے لکھنا golden سوال ہے۔",
              "coach": null
            }
          ]
        },
        {
          "id": "1.2.4-7",
          "title": "Waterfall بمقابلہ Agile",
          "golden": false,
          "slides": [
            {
              "headline": "دو ماڈل، دو مزاج",
              "body": "<p><strong>Waterfall</strong>: لکیری، ترتیب وار — ایک مرحلہ مکمل بغیر اگلا نہیں۔ پیچھے لوٹنا مشکل۔ دستاویزات بھاری۔ جہاں ضرورت ثابت ہو (بینک، سرکاری)۔</p><p><strong>Agile</strong>: چھوٹے cycles یعنی sprints (عموماً 2–4 ہفتے)۔ مسلسل کسٹمر فیڈ بیک، تبدیلی خوش آمدید۔</p>",
              "narrator": "دو ماڈل، دو مزاج۔  Waterfall: لکیری، ترتیب وار — ایک مرحلہ مکمل بغیر اگلا نہیں۔ پیچھے لوٹنا مشکل۔ دستاویزات بھاری۔ جہاں ضرورت ثابت ہو (بینک، سرکاری)۔  Agile: چھوٹے cycles یعنی sprints (عموماً 2–4 ہفتے)۔ مسلسل کسٹمر فیڈ بیک، تبدیلی خوش آمدید۔ ",
              "diagram": "waterfallAgile",
              "quiz": {
                "q": "تبدیلی سستے میں کون قبول کرتا ہے؟",
                "options": [
                  "Waterfall",
                  "Agile",
                  "صرف K-map",
                  "Analog signal"
                ],
                "answer": 1,
                "explain": "Agile iterative ہے، تبدیلی sprint میں سما جاتی ہے۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "1.3.1-4",
          "title": "مواصلاتی ماڈل اور OSI سات پرتیں",
          "golden": true,
          "slides": [
            {
              "headline": "★ OSI 7-layer",
              "body": "<p>Communication model بتاتا ہے ڈیٹا ایک آلے سے دوسرے تک کیسے جاتا ہے۔ OSI (Open Systems Interconnection) سات پرتوں کا حوالہ جاتی ماڈل ہے۔</p><p>اوپر سے نیچے: 7 Application، 6 Presentation، 5 Session، 4 Transport، 3 Network، 2 Data Link، 1 Physical۔ یادداشت: <span class='ltr'>All People Seem To Need Data Processing</span>۔</p>",
              "narrator": "★ OSI 7-layer۔  Communication model بتاتا ہے ڈیٹا ایک آلے سے دوسرے تک کیسے جاتا ہے۔ OSI (Open Systems Interconnection) سات پرتوں کا حوالہ جاتی ماڈل ہے۔  اوپر سے نیچے: 7 Application، 6 Presentation، 5 Session، 4 Transport، 3 Network، 2 Data Link، 1 Physical۔ یادداشت: <span class='ltr'>All People Seem To Need Data Processing</span>۔ ",
              "diagram": "osi7",
              "quiz": {
                "q": "IP addressing کس OSI پرت کا کام ہے؟",
                "options": [
                  "Physical",
                  "Transport",
                  "Network",
                  "Application"
                ],
                "answer": 2,
                "explain": "Network layer منطقی پتہ اور routing۔"
              },
              "tip": "ہر پرت کا بنیادی کام ایک جملے میں لکھ کے آئیں۔",
              "coach": null
            }
          ]
        },
        {
          "id": "1.3.5-6",
          "title": "TCP/IP بمقابلہ OSI",
          "golden": false,
          "slides": [
            {
              "headline": "چار پرتیں، عملی انٹرنیٹ",
              "body": "<p>TCP/IP عملی ماڈل ہے جو OSI کو سمیٹتا ہے: Application (OSI 5–7)، Transport (4)، Internet (3)، Network Access (1–2)۔ امتحان میں mapping جدول آتی ہے۔</p>",
              "narrator": "چار پرتیں، عملی انٹرنیٹ۔  TCP/IP عملی ماڈل ہے جو OSI کو سمیٹتا ہے: Application (OSI 5–7)، Transport (4)، Internet (3)، Network Access (1–2)۔ امتحان میں mapping جدول آتی ہے۔ ",
              "diagram": "tcpOsi",
              "quiz": {
                "q": "TCP/IP میں کتنی پرتیں؟",
                "options": [
                  "7",
                  "5",
                  "4",
                  "2"
                ],
                "answer": 2,
                "explain": "چار پرتیں۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        }
      ]
    },
    {
      "id": "ch2",
      "number": 2,
      "title": "Computational Thinking اور الگورتھم",
      "modules": [
        {
          "id": "2.1",
          "title": "Computational Thinking — حسابی سوچ",
          "golden": false,
          "slides": [
            {
              "headline": "مسئلہ حل کا نظام",
              "body": "<p>Computational Thinking (CT) مسائل کو ترتیب سے حل کرنے کا طریقہ ہے: Decomposition، Pattern Recognition، Abstraction، اور Algorithms۔</p>",
              "narrator": "مسئلہ حل کا نظام۔  Computational Thinking (CT) مسائل کو ترتیب سے حل کرنے کا طریقہ ہے: Decomposition، Pattern Recognition، Abstraction، اور Algorithms۔ ",
              "diagram": "decomposition",
              "quiz": {
                "q": "CT کا پہلا عام قدم؟",
                "options": [
                  "Abstraction",
                  "Decomposition",
                  "Binary search",
                  "IoT"
                ],
                "answer": 1,
                "explain": "پہلے بڑا مسئلہ توڑیں۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "2.2.2",
          "title": "Algorithm بمقابلہ Pseudocode",
          "golden": true,
          "slides": [
            {
              "headline": "★ نسخہ اور دستوری زبان",
              "body": "<p><strong>Algorithm</strong>: زبان سے آزاد، قدم بہ قدم منطقی طریقہ — کیا کرنا ہے۔ <strong>Pseudocode</strong>: IF / FOR / WHILE جیسی ساخت سے لکھا گیا قریبی-کوڈ، اصل syntax سے پہلے۔</p>",
              "narrator": "★ نسخہ اور دستوری زبان۔  Algorithm: زبان سے آزاد، قدم بہ قدم منطقی طریقہ — کیا کرنا ہے۔ Pseudocode: IF / FOR / WHILE جیسی ساخت سے لکھا گیا قریبی-کوڈ، اصل syntax سے پہلے۔ ",
              "diagram": null,
              "quiz": {
                "q": "Pseudocode کس لیے؟",
                "options": [
                  "ہارڈویئر جوڑنا",
                  "کوڈ سے پہلے ساخت لکھنا",
                  "شور مٹانا",
                  "OSI پرت"
                ],
                "answer": 1,
                "explain": "ڈیزائن مرحلے میں پڑھنے لائق قدم۔"
              },
              "tip": "Algorithm خیال ہے؛ Pseudocode اس خیال کی پڑھنے لائق شکل۔",
              "coach": null
            }
          ]
        },
        {
          "id": "2.3.1",
          "title": "Decomposition — تقسیمِ مسئلہ",
          "golden": true,
          "slides": [
            {
              "headline": "★ توڑو پھر جوڑو",
              "body": "<p> Decomposition پیچیدہ کام کو چھوٹے sub-tasks میں بانٹتی ہے — زبان سیکھنا: الفاظ → گرامر → جملے۔</p>",
              "narrator": "★ توڑو پھر جوڑو۔   Decomposition پیچیدہ کام کو چھوٹے sub-tasks میں بانٹتی ہے — زبان سیکھنا: الفاظ → گرامر → جملے۔ ",
              "diagram": "decomposition",
              "quiz": {
                "q": "بڑے پروجیکٹ کو ماڈیولز میں بانٹنا کیا کہلاتا ہے؟",
                "options": [
                  "Abstraction",
                  "Decomposition",
                  "Sorting",
                  "Sampling"
                ],
                "answer": 1,
                "explain": "توڑنا = Decomposition۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "2.3.2",
          "title": "Pattern Recognition — پیٹرن کی پہچان",
          "golden": false,
          "slides": [
            {
              "headline": "دہرائی پکڑو",
              "body": "<p>Pattern Recognition ڈیٹا میں قاعدہ ڈھونڈنا ہے۔ ستاروں کا مثلث: قطار N میں N ستارے — پانچ print کی بجائے ایک loop۔ پوچھیں: کیا دہرا رہا ہے؟ کیا پیش قیاسی بدل رہا ہے؟</p>",
              "narrator": "دہرائی پکڑو۔  Pattern Recognition ڈیٹا میں قاعدہ ڈھونڈنا ہے۔ ستاروں کا مثلث: قطار N میں N ستارے — پانچ print کی بجائے ایک loop۔ پوچھیں: کیا دہرا رہا ہے؟ کیا پیش قیاسی بدل رہا ہے؟ ",
              "diagram": null,
              "quiz": {
                "q": "ہر قطار میں ایک ستارہ بڑھے تو الگورتھم؟",
                "options": [
                  "صرف 5 print",
                  "عام loop",
                  "Binary search",
                  "XOR"
                ],
                "answer": 1,
                "explain": "پیٹرن کو loop میں generalize کریں۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "2.3.3",
          "title": "Abstraction — خلاصہ",
          "golden": false,
          "slides": [
            {
              "headline": "شور چھپائیں",
              "body": "<p>Abstraction غیر ضروری تفصیل چھپا کر اصل منطق رکھتی ہے۔ چائے: ابالو، پتی، دم، اوندیلو، پیش کرو — کیتلی کا برانڈ اور کپ کا رنگ noise ہے۔</p>",
              "narrator": "شور چھپائیں۔  Abstraction غیر ضروری تفصیل چھپا کر اصل منطق رکھتی ہے۔ چائے: ابالو، پتی، دم، اوندیلو، پیش کرو — کیتلی کا برانڈ اور کپ کا رنگ noise ہے۔ ",
              "diagram": null,
              "quiz": {
                "q": "Abstraction کیا ہٹاتی ہے؟",
                "options": [
                  "ضروری قدم",
                  "غیر ضروری تفصیل",
                  "Truth table",
                  "Primary key"
                ],
                "answer": 1,
                "explain": "صرف essence رہتی ہے۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "2.4.1b",
          "title": "Bubble Sort — بلبلہ ترتیب",
          "golden": true,
          "slides": [
            {
              "headline": "★ ملحق swap",
              "body": "<p>Bubble sort ملحق عناصر موازنہ کر کے غلط ترتیب پر swap کرتا ہے، پاس دہراتا ہے۔ فہرست: 8, 4, 1, 9, 3۔ سادہ شکل کی پیچیدگی \\(O(n^2)\\)۔</p>",
              "narrator": "★ ملحق swap۔  Bubble sort ملحق عناصر موازنہ کر کے غلط ترتیب پر swap کرتا ہے، پاس دہراتا ہے۔ فہرست: 8, 4, 1, 9, 3۔ سادہ شکل کی پیچیدگی \\(O(n^2)\\)۔ ",
              "diagram": "bubbleSort",
              "quiz": {
                "q": "Bubble sort کس جوڑے کو دیکھتی ہے؟",
                "options": [
                  "پہلا اور آخری صرف",
                  "ملحق (adjacent)",
                  "صرف درمیان",
                  "رینڈم"
                ],
                "answer": 1,
                "explain": "Adjacent compare-and-swap۔"
              },
              "tip": "الگورتھم کے steps اور ایک مکمل پاس امتحان میں لکھوائیں۔",
              "coach": null
            }
          ]
        },
        {
          "id": "2.4.1s",
          "title": "Selection Sort — انتخابی ترتیب",
          "golden": true,
          "slides": [
            {
              "headline": "★ سب سے چھوٹا چنیں",
              "body": "<p>Selection sort غیر مرتب حصے سے smallest چن کر اگلی پوزیشن پر رکھتی ہے۔ پہلی پوزیشن کے لیے پوری فہرست scan۔</p>",
              "narrator": "★ سب سے چھوٹا چنیں۔  Selection sort غیر مرتب حصے سے smallest چن کر اگلی پوزیشن پر رکھتی ہے۔ پہلی پوزیشن کے لیے پوری فہرست scan۔ ",
              "diagram": "selectionSort",
              "quiz": {
                "q": "Selection sort ہر پاس کیا کرتی ہے؟",
                "options": [
                  "ملحق swap صرف",
                  "باقی میں سے کم از کم چننا",
                  "درمیان کاٹنا",
                  "Hash"
                ],
                "answer": 1,
                "explain": "Unsorted سے minimum select۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "2.4.2l",
          "title": "Linear Search — لکیری تلاش",
          "golden": false,
          "slides": [
            {
              "headline": "ایک ایک کر کے",
              "body": "<p>Linear (sequential) search ہر عنصر چیک کرتی ہے جب تک ہدف نہ ملے۔ Sorted اور unsorted دونوں پر چلتی ہے؛ بدترین \\(O(n)\\)۔</p>",
              "narrator": "ایک ایک کر کے۔  Linear (sequential) search ہر عنصر چیک کرتی ہے جب تک ہدف نہ ملے۔ Sorted اور unsorted دونوں پر چلتی ہے؛ بدترین \\(O(n)\\)۔ ",
              "diagram": null,
              "quiz": {
                "q": "Linear search کس فہرست پر چلتی ہے؟",
                "options": [
                  "صرف sorted",
                  "sorted اور unsorted دونوں",
                  "صرف خالی",
                  "صرف bits"
                ],
                "answer": 1,
                "explain": "ترتیب شرط نہیں۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "2.4.2b",
          "title": "Binary Search — ثنائی تلاش",
          "golden": true,
          "slides": [
            {
              "headline": "★ آدھا کاٹو",
              "body": "<p>Binary search صرف <strong>sorted</strong> فہرست پر۔ mid دیکھو؛ چھوٹا ہو تو بائیں، بڑا تو دائیں — پیچیدگی \\(O(\\log n)\\)۔ مثال: [1..8] میں 3 تلاش، mid=4، 3&lt;4 اس لیے بائیں۔</p>",
              "narrator": "★ آدھا کاٹو۔  Binary search صرف sorted فہرست پر۔ mid دیکھو؛ چھوٹا ہو تو بائیں، بڑا تو دائیں — پیچیدگی \\(O(\\log n)\\)۔ مثال: [1..8] میں 3 تلاش، mid=4، 3&lt;4 اس لیے بائیں۔ ",
              "diagram": "binarySearch",
              "quiz": {
                "q": "Binary search کی شرط؟",
                "options": [
                  "فہرست sorted ہو",
                  "فہرست خالی ہو",
                  "n &lt; 3",
                  "Agile"
                ],
                "answer": 0,
                "explain": "بغیر ترتیب کے mid بے معنی۔"
              },
              "tip": "شرط بھولنا: data مرتب ہونا لازمی۔",
              "coach": null
            }
          ]
        },
        {
          "id": "2.5-6",
          "title": "الگورتھم کی جانچ اور انتخاب",
          "golden": false,
          "slides": [
            {
              "headline": "صحیح، تیز، مناسب",
              "body": "<p>Correctness: متوقع نتیجہ، edge cases۔ پھر وقت، میموری، ڈیٹا سائز، sorted ہے یا نہیں، اور پڑھنے کی آسانی۔ چھوٹی فہرست پر \\(O(n^2)\\) بھی ٹھیک؛ بڑی sorted تلاش پر binary۔</p>",
              "narrator": "صحیح، تیز، مناسب۔  Correctness: متوقع نتیجہ، edge cases۔ پھر وقت، میموری، ڈیٹا سائز، sorted ہے یا نہیں، اور پڑھنے کی آسانی۔ چھوٹی فہرست پر \\(O(n^2)\\) بھی ٹھیک؛ بڑی sorted تلاش پر binary۔ ",
              "diagram": null,
              "quiz": {
                "q": "بڑی sorted فہرست میں تلاش؟",
                "options": [
                  "Linear ہمیشہ",
                  "Binary search",
                  "Bubble sort",
                  "NOT gate"
                ],
                "answer": 1,
                "explain": "\\(O(\\log n)\\) بہتر۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        }
      ]
    },
    {
      "id": "ch3",
      "number": 3,
      "title": "پروگرامنگ کی بنیادیں",
      "modules": [
        {
          "id": "3.1",
          "title": "پروگرام اور زبانوں کی اقسام",
          "golden": false,
          "slides": [
            {
              "headline": "کمپیوٹر گونگا ہے",
              "body": "<p>کمپیوٹر بغیر ہدایت سوچ نہیں سکتا۔ ہدایات کا مجموعہ <strong>program</strong> ہے، اور ہدایت دینے والی زبان programming language۔ High-level (Python, C++) انسان کے قریب؛ machine language 0/1۔</p><p>C++ طاقتور، ہارڈویئر کے قریب — سسٹم سافٹ ویئر۔ Python سادہ نحو — Data Science، AI، ویب، ابتدائیہ۔</p>",
              "narrator": "کمپیوٹر گونگا ہے۔  کمپیوٹر بغیر ہدایت سوچ نہیں سکتا۔ ہدایات کا مجموعہ program ہے، اور ہدایت دینے والی زبان programming language۔ High-level (Python, C++) انسان کے قریب؛ machine language 0/1۔  C++ طاقتور، ہارڈویئر کے قریب — سسٹم سافٹ ویئر۔ Python سادہ نحو — Data Science، AI، ویب، ابتدائیہ۔ ",
              "diagram": null,
              "quiz": {
                "q": "Python کو beginner کیوں پسند کرتے ہیں؟",
                "options": [
                  "صرف اسمبلی ہے",
                  "سادہ readable syntax",
                  "صرف NAND",
                  "OSI 7"
                ],
                "answer": 1,
                "explain": "منطق پر توجہ، پیچیدہ نحو کم۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "3.2",
          "title": "Python سے کیریئر",
          "golden": false,
          "slides": [
            {
              "headline": "پاکستان میں دروازے",
              "body": "<p>Software development، Data Science، AI/ML، Django/Flask ویب، آٹومیشن، سائبر سیکیورٹی۔ Python مسئلہ حل پر فوکس رکھتی ہے، نحو رٹنے پر نہیں۔</p>",
              "narrator": "پاکستان میں دروازے۔  Software development، Data Science، AI/ML، Django/Flask ویب، آٹومیشن، سائبر سیکیورٹی۔ Python مسئلہ حل پر فوکس رکھتی ہے، نحو رٹنے پر نہیں۔ ",
              "diagram": null,
              "quiz": {
                "q": "Django کس کام کے قریب؟",
                "options": [
                  "K-map",
                  "ویب ڈیولپمنٹ",
                  "Analog wave",
                  "Selection sort"
                ],
                "answer": 1,
                "explain": "Python web framework۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "3.3",
          "title": "IDE اور VS Code",
          "golden": false,
          "slides": [
            {
              "headline": "ایک چھت تلے کام",
              "body": "<p>IDE: editor، syntax highlighting، auto-complete، run، debugger۔ VS Code ہلکا editor ہے؛ extensions لگا کر Python IDE بن جاتا ہے — File/Edit/Run مینو، نیچے terminal۔</p>",
              "narrator": "ایک چھت تلے کام۔  IDE: editor، syntax highlighting، auto-complete، run، debugger۔ VS Code ہلکا editor ہے؛ extensions لگا کر Python IDE بن جاتا ہے — File/Edit/Run مینو، نیچے terminal۔ ",
              "diagram": null,
              "quiz": {
                "q": "Debugger کیا کرتا ہے؟",
                "options": [
                  "صرف فونٹ بدلا",
                  "غلطیاں ڈھونڈنا/ٹھیک کرنا",
                  "IoT سینسر",
                  "ER oval"
                ],
                "answer": 1,
                "explain": "غلطی کی جگہ روک کر دیکھیں۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "3.4",
          "title": "Python پروگرام کی ساخت",
          "golden": true,
          "slides": [
            {
              "headline": "★ بیان، ڈیٹا، نتیجہ",
              "body": "<p>Python پروگرام statements سے ڈیٹا پر عمل کرتا ہے پھر output دکھاتا ہے۔ ترتیب: input → process → output۔</p>",
              "narrator": "★ بیان، ڈیٹا، نتیجہ۔  Python پروگرام statements سے ڈیٹا پر عمل کرتا ہے پھر output دکھاتا ہے۔ ترتیب: input → process → output۔ ",
              "diagram": "pythonIO",
              "quiz": null,
              "tip": "print اور متغیر کی پہلی مثال زبانی بتا سکیں۔",
              "coach": null
            }
          ]
        },
        {
          "id": "3.4.1",
          "title": "متغیرات اور Data Types",
          "golden": true,
          "slides": [
            {
              "headline": "★ ڈبہ جس پر نام ہو",
              "body": "<p>Variable میموری کا نام شدہ خانہ ہے۔ Python میں قسم پہلے declare نہیں — value سے type بنتی ہے۔ int، float، str، bool، list۔</p>",
              "narrator": "★ ڈبہ جس پر نام ہو۔  Variable میموری کا نام شدہ خانہ ہے۔ Python میں قسم پہلے declare نہیں — value سے type بنتی ہے۔ int، float، str، bool، list۔ ",
              "diagram": null,
              "quiz": {
                "q": "x = 3.14 کی قسم؟",
                "options": [
                  "int",
                  "float",
                  "bool",
                  "NAND"
                ],
                "answer": 1,
                "explain": "اعشاریہ = float۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "3.4.2",
          "title": "Input اور Output",
          "golden": false,
          "slides": [
            {
              "headline": "print اور input",
              "body": "<p><span class='ltr'>print(\"Hello Class!\")</span> اسکرین پر لکھتا ہے۔ <span class='ltr'>input()</span> صارف سے متن لیتا ہے؛ عدد کے لیے <span class='ltr'>int(input())</span>۔</p>",
              "narrator": "print اور input۔  <span class='ltr'>print(\"Hello Class!\")</span> اسکرین پر لکھتا ہے۔ <span class='ltr'>input()</span> صارف سے متن لیتا ہے؛ عدد کے لیے <span class='ltr'>int(input())</span>۔ ",
              "diagram": "pythonIO",
              "quiz": {
                "q": "صارف سے عدد لینے کا عام طریقہ؟",
                "options": [
                  "print صرف",
                  "int(input())",
                  "AND gate",
                  "K-map"
                ],
                "answer": 1,
                "explain": "input سٹرنگ دیتا ہے، int بنانا پڑتا ہے۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "3.4.3",
          "title": "Operators اور Operands",
          "golden": true,
          "slides": [
            {
              "headline": "★ عمل اور قیمت",
              "body": "<p>Operand قیمت/متغیر؛ Operator علامت۔ \\(10 + 20\\) میں 10,20 operands، + operator۔ Arithmetic: + − * / // % **۔ Relational: == != &gt; &lt;۔ Logical: and or not۔ Bitwise bits پر: AND &amp;، OR |، XOR ^، NOT ~، shifts۔</p><p>Bitwise XOR bits مختلف ہوں تو 1 — منطق XOR گیٹ جیسی۔</p>",
              "narrator": "★ عمل اور قیمت۔  Operand قیمت/متغیر؛ Operator علامت۔ \\(10 + 20\\) میں 10,20 operands، + operator۔ Arithmetic: + − * / // % **۔ Relational: == != &gt; &lt;۔ Logical: and or not۔ Bitwise bits پر: AND &amp;، OR |، XOR ^، NOT ~، shifts۔  Bitwise XOR bits مختلف ہوں تو 1 — منطق XOR گیٹ جیسی۔ ",
              "diagram": null,
              "quiz": {
                "q": "a = 10, b = 5 پر a &gt; b؟",
                "options": [
                  "False",
                  "True",
                  "10",
                  "Error"
                ],
                "answer": 1,
                "explain": "10 بڑا ہے → True۔"
              },
              "tip": "== موازنہ ہے، = تفویض۔",
              "coach": null
            }
          ]
        },
        {
          "id": "3.5",
          "title": "Control Structures — کنٹرول ڈھانچے",
          "golden": true,
          "slides": [
            {
              "headline": "★ ترتیب، انتخاب، دہراؤ",
              "body": "<p>Sequence سیدھی لائن۔ Selection: if / elif / else راستہ چنتی ہے۔ Repetition: for، while شرط تک دہراتی ہے۔ امتحان میں loop کو کاغذ پر trace کریں۔</p>",
              "narrator": "★ ترتیب، انتخاب، دہراؤ۔  Sequence سیدھی لائن۔ Selection: if / elif / else راستہ چنتی ہے۔ Repetition: for، while شرط تک دہراتی ہے۔ امتحان میں loop کو کاغذ پر trace کریں۔ ",
              "diagram": null,
              "quiz": {
                "q": "if-elif-else کیا ہے؟",
                "options": [
                  "تلاش الگورتھم",
                  "Selection",
                  "IoT",
                  "Primary key"
                ],
                "answer": 1,
                "explain": "شرط کے مطابق شاخ۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "3.6",
          "title": "لائبریریز اور غلطیاں",
          "golden": false,
          "slides": [
            {
              "headline": "Ready-made اوزار",
              "body": "<p>Built-in: math، random، datetime۔ Third-party: pip سے numpy، pandas۔ غلطیاں: Syntax (لکھائی)، Runtime (چلتے ہوئے)، Logic (چلتا ہے مگر جواب غلط)۔ Traceback بتاتا ہے قسم اور لائن۔</p>",
              "narrator": "Ready-made اوزار۔  Built-in: math، random، datetime۔ Third-party: pip سے numpy، pandas۔ غلطیاں: Syntax (لکھائی)، Runtime (چلتے ہوئے)، Logic (چلتا ہے مگر جواب غلط)۔ Traceback بتاتا ہے قسم اور لائن۔ ",
              "diagram": null,
              "quiz": {
                "q": "پروگرام چلے مگر جواب غلط ہو تو؟",
                "options": [
                  "Syntax error",
                  "Logic error",
                  "Golden gate",
                  "OSI 1"
                ],
                "answer": 1,
                "explain": "منطق میں خامی۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        }
      ]
    },
    {
      "id": "ch4",
      "number": 4,
      "title": "ڈیٹا بیس",
      "modules": [
        {
          "id": "4.1-2",
          "title": "ڈیٹا بیس اور اجزاء",
          "golden": false,
          "slides": [
            {
              "headline": "ٹیبل سے شروع",
              "body": "<p>Database منظم ذخیرہ ہے۔ بنیادی ڈھانچہ table: قطاریں = records، کالم = fields/attributes۔ DBMS ان اشیاء کو سنبھالتا ہے۔</p>",
              "narrator": "ٹیبل سے شروع۔  Database منظم ذخیرہ ہے۔ بنیادی ڈھانچہ table: قطاریں = records، کالم = fields/attributes۔ DBMS ان اشیاء کو سنبھالتا ہے۔ ",
              "diagram": null,
              "quiz": {
                "q": "Table کی قطار کو کیا کہتے ہیں؟",
                "options": [
                  "Field",
                  "Record",
                  "Query",
                  "Form"
                ],
                "answer": 1,
                "explain": "ایک ریکارڈ ایک قطار۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "4.3",
          "title": "Keys اور Integrity",
          "golden": true,
          "slides": [
            {
              "headline": "★ شناخت اور رشتہ",
              "body": "<p>Primary Key ریکارڈ منفرد شناخت — NULL/duplicate نہیں۔ Candidate keys میں سے ایک PK بنتی ہے، باقی Alternate۔ Foreign Key دوسری ٹیبل کی PK کی طرف اشارہ — رشتہ جوڑتی ہے، duplicate/NULL ہو سکتے ہیں۔</p><p>RDBMS کئی ٹیبلز + keys؛ redundancy کم، SQL سے سوال، کئی صارف۔</p>",
              "narrator": "★ شناخت اور رشتہ۔  Primary Key ریکارڈ منفرد شناخت — NULL/duplicate نہیں۔ Candidate keys میں سے ایک PK بنتی ہے، باقی Alternate۔ Foreign Key دوسری ٹیبل کی PK کی طرف اشارہ — رشتہ جوڑتی ہے، duplicate/NULL ہو سکتے ہیں۔  RDBMS کئی ٹیبلز + keys؛ redundancy کم، SQL سے سوال، کئی صارف۔ ",
              "diagram": "keys",
              "quiz": {
                "q": "Foreign Key کیا کرتی ہے؟",
                "options": [
                  "ہمیشہ unique ہوتی ہے",
                  "دو ٹیبلز جوڑتی ہے",
                  "Analog بناتی ہے",
                  "Sort کرتی ہے"
                ],
                "answer": 1,
                "explain": "دوسری ٹیبل کی PK کا حوالہ۔"
              },
              "tip": "PK vs FK جدول زبانی۔",
              "coach": null
            }
          ]
        },
        {
          "id": "4.4",
          "title": "ER-Model — وجودی تعلق کا خاکہ",
          "golden": true,
          "slides": [
            {
              "headline": "★ معمار کا نقشہ",
              "body": "<p>ER Model ڈیٹا بیس سے پہلے تصوراتی ڈیزائن: Entity (مستطیل)، Attribute (بیضوی)، Relationship (لوزی)۔ تعلق: 1:1، 1:M، M:N۔</p>",
              "narrator": "★ معمار کا نقشہ۔  ER Model ڈیٹا بیس سے پہلے تصوراتی ڈیزائن: Entity (مستطیل)، Attribute (بیضوی)، Relationship (لوزی)۔ تعلق: 1:1، 1:M، M:N۔ ",
              "diagram": "erModel",
              "quiz": {
                "q": "Entity کی علامت؟",
                "options": [
                  "Oval",
                  "Rectangle",
                  "Diamond",
                  "Circle bit"
                ],
                "answer": 1,
                "explain": "مستطیل = entity۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "4.5",
          "title": "Referential Integrity — حوالہ جاتی درستگی",
          "golden": true,
          "slides": [
            {
              "headline": "★ یتیم ریکارڈ نہیں",
              "body": "<p>Referential integrity یقینی بناتی ہے FK کی value اصل PK میں موجود ہو۔ Cascade Update: PK بدلی تو FK خود۔ Cascade Delete: parent گیا تو متعلقہ child۔</p>",
              "narrator": "★ یتیم ریکارڈ نہیں۔  Referential integrity یقینی بناتی ہے FK کی value اصل PK میں موجود ہو۔ Cascade Update: PK بدلی تو FK خود۔ Cascade Delete: parent گیا تو متعلقہ child۔ ",
              "diagram": null,
              "quiz": {
                "q": "Cascade Delete کیا کرتا ہے؟",
                "options": [
                  "صرف فونٹ",
                  "والد کے ساتھ بچے ریکارڈ ختم",
                  "K-map",
                  "Sprint"
                ],
                "answer": 1,
                "explain": "تعلق برقرار رکھنے کے لیے خودکار حذف۔"
              },
              "tip": "Library میں Member حذف تو BorrowRecord؟ پالیسی لکھیں۔",
              "coach": null
            }
          ]
        },
        {
          "id": "4.6-7",
          "title": "Relational Schema اور لائبریری کیس",
          "golden": false,
          "slides": [
            {
              "headline": "M:N کو توڑیں",
              "body": "<p>Schema ٹیبل کا خاکہ ہے۔ لائبریری: Member، Book؛ M:N borrow براہ راست نہیں — BorrowRecord پل ٹیبل: Member 1:M BorrowRecord، Book 1:M BorrowRecord۔</p>",
              "narrator": "M:N کو توڑیں۔  Schema ٹیبل کا خاکہ ہے۔ لائبریری: Member، Book؛ M:N borrow براہ راست نہیں — BorrowRecord پل ٹیبل: Member 1:M BorrowRecord، Book 1:M BorrowRecord۔ ",
              "diagram": "erModel",
              "quiz": {
                "q": "M:N کو relational میں کیسے؟",
                "options": [
                  "نظر انداز",
                  "associative/bridge table",
                  "صرف Analog",
                  "NAND"
                ],
                "answer": 1,
                "explain": "درمیانی entity۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "4.8-11",
          "title": "Objects، Forms، Queries، Charts",
          "golden": true,
          "slides": [
            {
              "headline": "★ سوال پوچھو، دیکھ کر بھرو",
              "body": "<p>Objects: Table، Query، Form، Report، Chart۔ Form اندراج کا انٹرفیس — غلطی کم۔ Query ڈیٹا چھانتی ہے بغیر اصل ٹیبل بدلے؛ Criteria سے فلٹر؛ Grouping سے مجموعہ۔ Charts: Bar موازنہ، Pie تناسب۔</p>",
              "narrator": "★ سوال پوچھو، دیکھ کر بھرو۔  Objects: Table، Query، Form، Report، Chart۔ Form اندراج کا انٹرفیس — غلطی کم۔ Query ڈیٹا چھانتی ہے بغیر اصل ٹیبل بدلے؛ Criteria سے فلٹر؛ Grouping سے مجموعہ۔ Charts: Bar موازنہ، Pie تناسب۔ ",
              "diagram": null,
              "quiz": {
                "q": "Access میں مخصوص قطاریں دیکھنے کا اوزار؟",
                "options": [
                  "صرف Paint",
                  "Query",
                  "OSI",
                  "Ramp"
                ],
                "answer": 1,
                "explain": "Query فلٹر/تلاش۔"
              },
              "tip": "Query اصل ڈیٹا نہیں مٹاتی — پوچھتی ہے۔",
              "coach": null
            }
          ]
        }
      ]
    },
    {
      "id": "ch5",
      "number": 5,
      "title": "کمپیوٹنگ کے اثرات",
      "modules": [
        {
          "id": "5.1.1",
          "title": "مصنوعی ذہانت (AI)",
          "golden": true,
          "slides": [
            {
              "headline": "★ ڈیٹا سے فیصلے",
              "body": "<p>AI مشینوں کو انسانی جیسے کام (پہچان، پیش گوئی، سفارش) سکھاتی ہے۔ پاکستان میں LMS، خودکار مارکنگ، کیریئر مشورہ — فائدہ: اپنی رفتار، مدد درکار طلبہ، disability support۔ چیلنج: دیہی انٹرنیٹ، آلات، استاد تربیت، پرائیویسی۔</p>",
              "narrator": "★ ڈیٹا سے فیصلے۔  AI مشینوں کو انسانی جیسے کام (پہچان، پیش گوئی، سفارش) سکھاتی ہے۔ پاکستان میں LMS، خودکار مارکنگ، کیریئر مشورہ — فائدہ: اپنی رفتار، مدد درکار طلبہ، disability support۔ چیلنج: دیہی انٹرنیٹ، آلات، استاد تربیت، پرائیویسی۔ ",
              "diagram": null,
              "quiz": {
                "q": "AI تعلیم میں ایک فائدہ؟",
                "options": [
                  "انٹرنیٹ ختم",
                  "ذاتی رفتار سے سیکھنا",
                  "Bits ختم",
                  "OSI 8"
                ],
                "answer": 1,
                "explain": "خودکار مدد اور رفتار۔"
              },
              "tip": "فائدے اور پاکستانی چیلنج دونوں لکھیں۔",
              "coach": null
            }
          ]
        },
        {
          "id": "5.1.2",
          "title": "IoT — انٹرنیٹ آف تھنگز",
          "golden": true,
          "slides": [
            {
              "headline": "★ چیزیں بات کرتی ہیں",
              "body": "<p>IoT: فیزیکی آلات انٹرنیٹ سے جڑ کر ڈیٹا بھیجتے ہیں۔ اجزاء: Sensors، Connectivity (Wi-Fi/4G)، Data processing، Actuators/User interface۔</p>",
              "narrator": "★ چیزیں بات کرتی ہیں۔  IoT: فیزیکی آلات انٹرنیٹ سے جڑ کر ڈیٹا بھیجتے ہیں۔ اجزاء: Sensors، Connectivity (Wi-Fi/4G)، Data processing، Actuators/User interface۔ ",
              "diagram": "iot",
              "quiz": {
                "q": "بغیر connectivity IoT؟",
                "options": [
                  "بہتر ہوتا ہے",
                  "سینسر سسٹم سے بات نہیں کر سکتا",
                  "صرف K-map",
                  "Primary key"
                ],
                "answer": 1,
                "explain": "رابطہ ضروری۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "5.1.3-2",
          "title": "Data Analytics اور IoT کے استعمال",
          "golden": false,
          "slides": [
            {
              "headline": "صاف کرو، پڑھو، بتاؤ",
              "body": "<p>Analytics: جمع، ترتیب، صفائی، مطالعہ، پیشکش۔ IoT: صحت، زراعت، ٹریفک، اسمارٹ کلاس، بایومیٹرک حاضری۔ کیریئر: IoT Engineer، Data Analyst — Python، نیٹ ورکنگ، سینسرز۔</p>",
              "narrator": "صاف کرو، پڑھو، بتاؤ۔  Analytics: جمع، ترتیب، صفائی، مطالعہ، پیشکش۔ IoT: صحت، زراعت، ٹریفک، اسمارٹ کلاس، بایومیٹرک حاضری۔ کیریئر: IoT Engineer، Data Analyst — Python، نیٹ ورکنگ، سینسرز۔ ",
              "diagram": "iot",
              "quiz": {
                "q": "Data analysis کا مقصد؟",
                "options": [
                  "شور بڑھانا",
                  "پیٹرن/معلومات نکلنا",
                  "گیٹ توڑنا",
                  "NULL PK"
                ],
                "answer": 1,
                "explain": "فیصلے کے لیے insight۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "5.3",
          "title": "معلومات کے ذرائع",
          "golden": true,
          "slides": [
            {
              "headline": "★ تین پرتیں",
              "body": "<p>Primary: اصل، firsthand — انٹرویو، تصویر، ڈائری، NADRA ریکارڈ۔ Secondary: کسی کی تشریح — کتاب، خبر، تحقیقی مقالہ۔ Tertiary: خلاصہ فہرست — انسائیکلوپیڈیا، انڈیکس۔ انٹرنیٹ وسیع ہے، سب درست نہیں۔</p>",
              "narrator": "★ تین پرتیں۔  Primary: اصل، firsthand — انٹرویو، تصویر، ڈائری، NADRA ریکارڈ۔ Secondary: کسی کی تشریح — کتاب، خبر، تحقیقی مقالہ۔ Tertiary: خلاصہ فہرست — انسائیکلوپیڈیا، انڈیکس۔ انٹرنیٹ وسیع ہے، سب درست نہیں۔ ",
              "diagram": null,
              "quiz": {
                "q": "NADRA ریکارڈ کون سا ماخذ؟",
                "options": [
                  "Tertiary",
                  "Primary",
                  "صرف Agile",
                  "Analog"
                ],
                "answer": 1,
                "explain": "سرکاری اصل ریکارڈ = primary۔"
              },
              "tip": "امتحان میں ہر قسم کی 2 مثالیں۔",
              "coach": null
            }
          ]
        },
        {
          "id": "5.4-5",
          "title": "سماجی اثرات اور Assistive Tech",
          "golden": true,
          "slides": [
            {
              "headline": "★ شمولیت",
              "body": "<p>کمپیوٹنگ رفتار اور رابطہ بڑھاتی ہے مگر پرائیویسی کے خطرات بھی۔ Assistive technologies معذوری والے افراد کو برابر رسائی دیتی ہیں: screen readers، speech-to-text۔ تعلیم میں نابینا طلبہ ڈیجیٹل کتاب پڑھ سکتے ہیں۔</p>",
              "narrator": "★ شمولیت۔  کمپیوٹنگ رفتار اور رابطہ بڑھاتی ہے مگر پرائیویسی کے خطرات بھی۔ Assistive technologies معذوری والے افراد کو برابر رسائی دیتی ہیں: screen readers، speech-to-text۔ تعلیم میں نابینا طلبہ ڈیجیٹل کتاب پڑھ سکتے ہیں۔ ",
              "diagram": null,
              "quiz": {
                "q": "Screen reader کسے مدد دیتا ہے؟",
                "options": [
                  "صرف پرنٹر",
                  "نابینا/کم بینا صارف",
                  "XOR گیٹ",
                  "Waterfall"
                ],
                "answer": 1,
                "explain": "متن کو آواز۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        }
      ]
    },
    {
      "id": "ch6",
      "number": 6,
      "title": "ڈیجیٹل خواندگی",
      "modules": [
        {
          "id": "6.1-2",
          "title": "Digital Literacy کیا ہے؟",
          "golden": false,
          "slides": [
            {
              "headline": "محفوظ اور سمجھ دار استعمال",
              "body": "<p>Digital literacy: ڈیوائس، انٹرنیٹ، آن لائن اوزار کو محفوظ، مؤثر، ذمہ دار طریقے سے سمجھنا اور استعمال کرنا — صرف ٹیپ نہیں، سوچ۔</p>",
              "narrator": "محفوظ اور سمجھ دار استعمال۔  Digital literacy: ڈیوائس، انٹرنیٹ، آن لائن اوزار کو محفوظ، مؤثر، ذمہ دار طریقے سے سمجھنا اور استعمال کرنا — صرف ٹیپ نہیں، سوچ۔ ",
              "diagram": null,
              "quiz": {
                "q": "Digital literacy کا حصہ؟",
                "options": [
                  "صرف گیم",
                  "محفوظ مؤثر آن لائن استعمال",
                  "صرف NAND",
                  "Gray code"
                ],
                "answer": 1,
                "explain": "سمجھ + حفاظت + اوزار۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "6.3",
          "title": "Qualitative بمقابلہ Quantitative",
          "golden": true,
          "slides": [
            {
              "headline": "★ دو قسم کا ڈیٹا",
              "body": "<p>Qualitative: زمرے/الفاظ — رنگ، رائے، ہاں/نہیں۔ Quantitative: اعداد — عمر، مارکس، گھنٹے۔ سروے ڈیزائن سے پہلے فیصلہ کریں۔</p>",
              "narrator": "★ دو قسم کا ڈیٹا۔  Qualitative: زمرے/الفاظ — رنگ، رائے، ہاں/نہیں۔ Quantitative: اعداد — عمر، مارکس، گھنٹے۔ سروے ڈیزائن سے پہلے فیصلہ کریں۔ ",
              "diagram": "dataTypes",
              "quiz": {
                "q": "روزانہ فون کے گھنٹے؟",
                "options": [
                  "Qualitative",
                  "Quantitative",
                  "XOR",
                  "Tertiary"
                ],
                "answer": 1,
                "explain": "عدد = quantitative۔"
              },
              "tip": "سوال کی قسم بتائے ڈیٹا کی قسم۔",
              "coach": null
            }
          ]
        },
        {
          "id": "6.4",
          "title": "ڈیٹا جمع کی حکمت عملی",
          "golden": true,
          "slides": [
            {
              "headline": "★ خود اصل معلومات",
              "body": "<p>موجودہ معلومات ڈھونڈنا کافی نہیں — سروے، مشاہدہ، تجربہ، prototype (ابتدائی ماڈل تاکہ مہنگے بنانے سے پہلے ٹیسٹ)۔</p>",
              "narrator": "★ خود اصل معلومات۔  موجودہ معلومات ڈھونڈنا کافی نہیں — سروے، مشاہدہ، تجربہ، prototype (ابتدائی ماڈل تاکہ مہنگے بنانے سے پہلے ٹیسٹ)۔ ",
              "diagram": null,
              "quiz": {
                "q": "Prototype کیا ہے؟",
                "options": [
                  "حتمی پروڈکٹ",
                  "آزمائشی ابتدائی ورژن",
                  "Primary key",
                  "OSI 7"
                ],
                "answer": 1,
                "explain": "جلد ٹیسٹ، سستا سبق۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "6.5",
          "title": "Primary اور Secondary ڈیٹا",
          "golden": true,
          "slides": [
            {
              "headline": "★ کنٹرول کس کا؟",
              "body": "<p>Primary: آپ خود جمع — کنٹرول زیادہ، وقت/لاگت زیادہ۔ Secondary: پہلے سے موجود — تیز، سستا، مگر مقصد کسی اور کا ہو سکتا ہے۔</p>",
              "narrator": "★ کنٹرول کس کا؟۔  Primary: آپ خود جمع — کنٹرول زیادہ، وقت/لاگت زیادہ۔ Secondary: پہلے سے موجود — تیز، سستا، مگر مقصد کسی اور کا ہو سکتا ہے۔ ",
              "diagram": null,
              "quiz": {
                "q": "Secondary data کا فائدہ؟",
                "options": [
                  "ہمیشہ 100٪ درست",
                  "تیز اور اکثر سستا",
                  "صرف analog",
                  "Cascade delete"
                ],
                "answer": 1,
                "explain": "موجودہ ماخذ استعمال۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "6.7",
          "title": "ڈیجیٹل اوزار سے پیشکش",
          "golden": false,
          "slides": [
            {
              "headline": "چارٹ اور infographic",
              "body": "<p>جمع کرنا آدھا کام ہے۔ Spreadsheet، گراف، infographic سے لوگ فوراً سمجھیں۔ Infographic: حقائق + تصویر + مختصر متن۔</p>",
              "narrator": "چارٹ اور infographic۔  جمع کرنا آدھا کام ہے۔ Spreadsheet، گراف، infographic سے لوگ فوراً سمجھیں۔ Infographic: حقائق + تصویر + مختصر متن۔ ",
              "diagram": null,
              "quiz": {
                "q": "Infographic کا مقصد؟",
                "options": [
                  "صرف کوڈ compile",
                  "جلدی سمجھ آنے والی بصری کہانی",
                  "Gate delay",
                  "NULL FK"
                ],
                "answer": 1,
                "explain": "بصری خلاصہ۔"
              },
              "tip": null,
              "coach": null
            }
          ]
        },
        {
          "id": "6.8",
          "title": "کیس اسٹڈی: Digital Inquiry",
          "golden": true,
          "slides": [
            {
              "headline": "★ بارہ قدم، ایک artefact",
              "body": "<p>مسئلہ: اسکرین ٹائم اور توجہ۔ Advanced search → سروے (consent، گمنامی) → secondary مضمون سے موازنہ → spreadsheet → چارٹ → نتیجہ → digital artefact (سلائیڈ/پوسٹر/ویڈیو)۔ اخلاقیات: اجازت، حساس ڈیٹا نہیں، صرف تعلیمی استعمال۔</p>",
              "narrator": "★ بارہ قدم، ایک artefact۔  مسئلہ: اسکرین ٹائم اور توجہ۔ Advanced search → سروے (consent، گمنامی) → secondary مضمون سے موازنہ → spreadsheet → چارٹ → نتیجہ → digital artefact (سلائیڈ/پوسٹر/ویڈیو)۔ اخلاقیات: اجازت، حساس ڈیٹا نہیں، صرف تعلیمی استعمال۔ ",
              "diagram": null,
              "quiz": {
                "q": "سروے سے پہلے کیا لازمی؟",
                "options": [
                  "Cascade XOR",
                  "رضامندی (consent)",
                  "NAND universal",
                  "Waterfall صرف"
                ],
                "answer": 1,
                "explain": "اخلاقی تحقیق کی بنیاد۔"
              },
              "tip": "Consent اور anonymity کے جملے رٹ لیں۔",
              "coach": null
            }
          ]
        }
      ]
    }
  ]
};

function allModules() {
  const list = [];
  for (const ch of CURRICULUM.chapters) {
    for (const m of ch.modules) list.push({ chapter: ch, module: m });
  }
  return list;
}

window.COACH_LINES = COACH_LINES;
window.CURRICULUM = CURRICULUM;
window.allModules = allModules;
