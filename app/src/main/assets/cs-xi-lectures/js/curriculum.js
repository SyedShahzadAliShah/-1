/**
 * CS XI — Cinematic Self-Taught Teacher's Lecture Notes (Ultimate Edition)
 * Based on Sindh Curriculum 2026 teacher's edition structure.
 */

export const COACH_MESSAGES = {
  en: [
    "You showed up — that's the hardest part. One slide at a time.",
    "Reluctance is normal. Your brain is warming up; stay for 120 seconds.",
    "Golden ★ topics are exam magnets. Master these first.",
    "Pause, breathe, hit Narrate — let the teacher voice carry you.",
    "Small win logged. You are closer than yesterday's you."
  ],
  ur: [
    "آپ آ گئے — یہ سب سے مشکل قدم تھا۔ ایک سلائیڈ ایک وقت میں۔",
    "سستی عام ہے۔ دماغ گرم ہو رہا ہے؛ دو منٹ رہیں۔",
    "★ سنہری موضوعات امتحان کے لیے اہم ہیں۔ پہلے یہ سیکھیں۔",
    "رکیں، سانس لیں، Narrate دبائیں — آواز آپ کو سنبھالے گی۔",
    "چھوٹی کامیابی محفوظ۔ آپ کل سے آگے ہیں۔"
  ]
};

export const CURRICULUM = {
  meta: {
    titleEn: "Computer Science XI",
    titleUr: "کمپیوٹر سائنس گیارہویں",
    edition: "Ultimate · Self-Taught Cinema"
  },
  chapters: [
    chapter1(),
    chapter2(),
    chapter3(),
    chapter4(),
    chapter5(),
    chapter6()
  ]
};

function slide(opts) {
  return {
    headlineEn: opts.headlineEn || "",
    headlineUr: opts.headlineUr || "",
    bodyEn: opts.bodyEn || "",
    bodyUr: opts.bodyUr || "",
    narratorEn: opts.narratorEn || opts.bodyEn?.replace(/<[^>]+>/g, " ") || "",
    narratorUr: opts.narratorUr || opts.bodyUr || "",
    diagram: opts.diagram || null,
    coachEn: opts.coachEn,
    coachUr: opts.coachUr
  };
}

function mod(id, titleEn, titleUr, golden, slides) {
  return { id, titleEn, titleUr, golden, slides };
}

function chapter1() {
  return {
    id: "ch1",
    number: 1,
    titleEn: "Computer Systems",
    titleUr: "کمپیوٹر سسٹمز",
    modules: [
      mod("1.1.1", "Discrete & Continuous Quantities", "الگ اور مسلسل مقداریں", false, [
        slide({
          headlineEn: "Discrete quantities",
          headlineUr: "الگ (Discrete) مقداریں",
          bodyEn: `<p><strong>Discrete</strong> values are separate and countable — students in a class, cars in a lot.</p>`,
          bodyUr: `<p class="urdu-block"><strong>الگ مقداریں</strong> الگ اور گننے والی ہوتی ہیں — جیسے کلاس میں طلبہ یا پارکنگ میں گاڑیاں۔</p>`,
          diagram: "stairsRamp",
          coachEn: "Count on your fingers — that's discrete thinking. Easy win."
        }),
        slide({
          headlineEn: "Continuous quantities",
          headlineUr: "مسلسل (Continuous) مقداریں",
          bodyEn: `<p><strong>Continuous</strong> values can be any point in a range — temperature, speed.</p>
          <p>💡 <em>Stairs = discrete. Ramp = continuous.</em></p>`,
          bodyUr: `<p class="urdu-block"><strong>مسلسل</strong> مقداریں کسی حد میں کوئی بھی قیمت لے سکتی ہیں — درجہ حرارت، رفتار۔</p>`,
          diagram: "stairsRamp"
        })
      ]),
      mod("1.1.2", "Introduction to Digital Systems", "ڈیجیٹل سسٹمز کا تعارف", false, [
        slide({
          headlineEn: "Bits: 0 and 1",
          headlineUr: "بٹس: 0 اور 1",
          bodyEn: `<p>A <strong>digital system</strong> uses only <strong>0</strong> (OFF/LOW/FALSE) and <strong>1</strong> (ON/HIGH/TRUE).</p>
          <ul><li>Reliable against noise</li><li>Accurate copying</li><li>Easy to design</li><li>Programmable by software</li></ul>`,
          bodyUr: `<p class="urdu-block"><strong>ڈیجیٹل سسٹم</strong> صرف <strong>0</strong> اور <strong>1</strong> استعمال کرتا ہے۔ شور سے محفوظ، نقل درست، ڈیزائن آسان۔</p>`,
          diagram: "binaryBits"
        })
      ]),
      mod("1.1.3", "Analog and Digital Signals", "اینالاگ اور ڈیجیٹل سگنل", true, [
        slide({
          headlineEn: "★ Golden: Signal types",
          headlineUr: "★ سنہری: سگنل کی اقسام",
          bodyEn: `<p><strong>Analog</strong>: smooth continuous wave (voice, old thermometers).</p>
          <p><strong>Digital</strong>: only HIGH(1) and LOW(0) — square wave (computer data).</p>
          <table><tr><th>Feature</th><th>Analog</th><th>Digital</th></tr>
          <tr><td>Nature</td><td>Continuous</td><td>Discrete bits</td></tr>
          <tr><td>Reliability</td><td>Low (noise)</td><td>High</td></tr></table>`,
          bodyUr: `<p class="urdu-block"><strong>اینالاگ</strong>: ہموار لہر۔ <strong>ڈیجیٹل</strong>: صرف اونچا/نیچا — کمپیوٹر ڈیٹا۔</p>`,
          diagram: "analogDigitalWaves",
          coachEn: "Examiners love this table. Read it twice out loud."
        })
      ]),
      mod("1.1.4-6", "Boolean Algebra & Truth Tables", "بولین الجبرا اور ٹرٹھ ٹیبل", false, [
        slide({
          headlineEn: "Boolean algebra",
          headlineUr: "بولین الجبرا",
          bodyEn: `<p>George Boole's algebra uses TRUE (1) and FALSE (0) — foundation of digital logic.</p>
          <p>AND \(Y = A \cdot B\) · OR \(Y = A + B\) · NOT \(Y = A'\)</p>`,
          bodyUr: `<p class="urdu-block">بولین الجبرا TRUE (1) اور FALSE (0) پر مبنی ہے۔ AND، OR، NOT بنیادی عمل ہیں۔</p>`,
          narratorEn: "Boolean algebra uses TRUE one and FALSE zero. AND gives one only when all inputs are one. OR when any input is one. NOT inverts."
        }),
        slide({
          headlineEn: "Truth tables",
          headlineUr: "ٹرٹھ ٹیبل",
          bodyEn: `<p>Steps: count inputs <em>n</em>, rows = \(2^n\), list binary combinations, compute output.</p>`,
          bodyUr: `<p class="urdu-block">ان پٹ n ہیں تو قطاریں \(2^n\)۔ تمام امتزاج لکھیں، پھر آؤٹ پٹ۔</p>`,
          diagram: "truthTable2"
        })
      ]),
      mod("1.1.7", "Basic Logic Gates (AND, OR, NOT)", "بنیادی لاجک گیٹس", true, [
        slide({
          headlineEn: "★ AND, OR, NOT",
          headlineUr: "★ AND، OR، NOT",
          bodyEn: `<p>Logic gates are electronic circuits performing Boolean operations — building blocks of all digital systems.</p>`,
          bodyUr: `<p class="urdu-block">لاجک گیٹس سرکٹ ہیں جو بولین عمل کرتے ہیں — ڈیجیٹل دنیا کی اینٹیں۔</p>`,
          diagram: "gatesOverview"
        }),
        slide({
          headlineEn: "AND gate detail",
          headlineUr: "AND گیٹ",
          bodyEn: `<p>Output 1 <strong>only</strong> when A=1 AND B=1. Expression: \(Y = A \cdot B\)</p>`,
          bodyUr: `<p class="urdu-block">آؤٹ پٹ 1 صرف جب دونوں ان پٹ 1 ہوں۔</p>`,
          diagram: "gateAND"
        }),
        slide({
          headlineEn: "OR & NOT",
          headlineUr: "OR اور NOT",
          bodyEn: `<p>OR: 1 if <em>any</em> input is 1. NOT: inverts input.</p>`,
          bodyUr: `<p class="urdu-block">OR: کوئی ایک 1 ہو تو آؤٹ پٹ 1۔ NOT: الٹ دیتا ہے۔</p>`,
          diagram: "gateOR"
        })
      ]),
      mod("1.1.7u", "Universal Logic Gates", "یونیورسل گیٹس", false, [
        slide({
          headlineEn: "NAND & NOR are universal",
          headlineUr: "NAND اور NOR یونیورسل ہیں",
          bodyEn: `<p><strong>Teacher tip:</strong> Any logic circuit can be built using <em>only</em> NAND or <em>only</em> NOR gates.</p>`,
          bodyUr: `<p class="urdu-block">کوئی بھی سرکٹ صرف NAND یا صرف NOR سے بن سکتا ہے۔</p>`,
          diagram: "gatesOverview"
        })
      ]),
      mod("1.1.8-11", "Expressions, Minterms & Diagrams", "ایکسپریشنز اور ڈایاگرام", false, [
        slide({
          headlineEn: "Minterms & logic diagrams",
          headlineUr: "مائن ٹرمز اور لاجک ڈایاگرام",
          bodyEn: `<p>A <strong>minterm</strong> is a product term that is 1 for exactly one row of the truth table. Logic diagrams wire gates to match expressions.</p>`,
          bodyUr: `<p class="urdu-block"><strong>مائن ٹرم</strong> وہ جملہ ہے جو ٹرٹھ ٹیبل کی ایک قطار پر 1 ہو۔</p>`
        })
      ]),
      mod("1.1.13", "Karnaugh Maps (K-Maps)", "کے میپس", true, [
        slide({
          headlineEn: "★ K-Map simplification",
          headlineUr: "★ کے میپ سے سادہ کرنا",
          bodyEn: `<p>Group adjacent 1s in powers of 2 (1, 2, 4, 8…). Each group removes one variable from the final expression.</p>`,
          bodyUr: `<p class="urdu-block">ملحق 1s کو 2 کی طاقتوں میں گروپ کریں — ہر گروپ ایک متغیر کم کرتا ہے۔</p>`,
          diagram: "kmap3var",
          coachEn: "Draw one 3-variable K-map today — that's enough for momentum."
        })
      ]),
      mod("logisim", "Logisim Simulation Guide", "Logisim گائیڈ", false, [
        slide({
          headlineEn: "Simulate before you solder",
          headlineUr: "پہلے Logisim میں مشق",
          bodyEn: `<p>Use <strong>Logisim</strong> to drag gates, wire inputs, and verify truth tables without hardware. Match your textbook circuits slide-for-slide.</p>`,
          bodyUr: `<p class="urdu-block"><strong>Logisim</strong> میں گیٹ لگائیں، تار جوڑیں، ٹرٹھ ٹیبل چیک کریں۔</p>`
        })
      ]),
      mod("1.2.1-3", "Software Development Life Cycle (SDLC)", "SDLC", true, [
        slide({
          headlineEn: "★ SDLC phases",
          headlineUr: "★ SDLC مراحل",
          bodyEn: `<p>Planning → Analysis → Design → Implementation → Testing → Deployment → Maintenance. Each phase has deliverables and reviews.</p>`,
          bodyUr: `<p class="urdu-block">منصوبہ بندی سے دیکھ بھال تک — ہر مرحلے میں واضح نتائج۔</p>`,
          diagram: "sdlc"
        })
      ]),
      mod("1.2.4-7", "Waterfall vs Agile", "واٹرفال بمقابلہ ایجائل", false, [
        slide({
          headlineEn: "Models compared",
          headlineUr: "ماڈلز کا موازنہ",
          bodyEn: `<p><strong>Waterfall</strong>: sequential, documents heavy, change is costly late.</p>
          <p><strong>Agile</strong>: iterative sprints, customer feedback, embraces change.</p>`,
          bodyUr: `<p class="urdu-block"><strong>واٹرفال</strong>: ترتیب وار۔ <strong>ایجائل</strong>: چھوٹے چکر، تبدیلی قابل قبول۔</p>`,
          diagram: "waterfallAgile"
        })
      ]),
      mod("1.3.1-4", "Communication & OSI Model", "OSI سات پرتیں", true, [
        slide({
          headlineEn: "★ OSI 7-layer model",
          headlineUr: "★ OSI سات پرتیں",
          bodyEn: `<p>Remember top-to-bottom: <strong>A</strong>pplication, <strong>P</strong>resentation, <strong>S</strong>ession, <strong>T</strong>ransport, <strong>N</strong>etwork, <strong>D</strong>ata Link, <strong>P</strong>hysical.</p>
          <p>Mnemonic: <em>All People Seem To Need Data Processing</em>.</p>`,
          bodyUr: `<p class="urdu-block">اوپر سے نیچے سات پرتیں — امتحان میں نام یاد رکھیں۔</p>`,
          diagram: "osi7"
        })
      ]),
      mod("1.3.5-6", "TCP/IP vs OSI", "TCP/IP اور OSI", false, [
        slide({
          headlineEn: "Four vs seven layers",
          headlineUr: "چار بمقابلہ سات پرتیں",
          bodyEn: `<p>TCP/IP merges OSI layers into <strong>Application</strong>, <strong>Transport</strong>, <strong>Internet</strong>, <strong>Network Access</strong>.</p>`,
          bodyUr: `<p class="urdu-block">TCP/IP چار پرتوں میں OSI کو سمیٹتا ہے۔</p>`,
          diagram: "tcpOsi"
        })
      ])
    ]
  };
}

function chapter2() {
  return {
    id: "ch2",
    number: 2,
    titleEn: "Computational Thinking & Algorithms",
    titleUr: "تفکّرِ کمپیوٹیشنل اور الگورتھم",
    modules: [
      mod("2.1", "Computational Thinking", "تفکّرِ کمپیوٹیشنل", false, [
        slide({
          headlineEn: "CT in one breath",
          headlineUr: "CT کا خلاصہ",
          bodyEn: `<p>Decomposition, pattern recognition, abstraction, and algorithms — a systematic way to solve problems.</p>`,
          bodyUr: `<p class="urdu-block">تقسیم، پیٹرن، خلاصہ، الگورتھم — مسئلہ حل کا طریقہ۔</p>`
        })
      ]),
      mod("2.2", "Algorithms", "الگورتھم", true, [
        slide({
          headlineEn: "★ What is an algorithm?",
          headlineUr: "★ الگورتھم کیا ہے؟",
          bodyEn: `<p>A step-by-step logical procedure — independent of any programming language. Blueprint before code.</p>`,
          bodyUr: `<p class="urdu-block">قدم بہ قدم منطقی طریقہ — زبان سے آزاد۔</p>`
        })
      ]),
      mod("2.2.2", "Algorithm vs Pseudocode", "الگورتھم بمقابلہ سودو کوڈ", true, [
        slide({
          headlineEn: "★ Recipe vs kitchen manual",
          headlineUr: "★ نسخہ بمقابلہ دستی کتاب",
          bodyEn: `<p><strong>Algorithm</strong>: what to do. <strong>Pseudocode</strong>: structured IF/FOR/WHILE readable steps before coding.</p>`,
          bodyUr: `<p class="urdu-block"><strong>الگورتھم</strong>: کیا کرنا ہے۔ <strong>سودو کوڈ</strong>: کوڈ سے پہلے ساخت۔</p>`
        })
      ]),
      mod("2.3.1", "Decomposition", "تقسیم", true, [
        slide({
          headlineEn: "★ Break it down",
          headlineUr: "★ چھوٹے حصے بنائیں",
          bodyEn: `<p>Split complex tasks into sub-tasks (learn vocabulary → grammar → sentences).</p>`,
          bodyUr: `<p class="urdu-block">بڑا کام چھوٹے حصوں میں — زبان سیکھنے جیسا۔</p>`,
          diagram: "decomposition"
        })
      ]),
      mod("2.3.2", "Pattern Recognition", "پیٹرن کی شناخت", false, [
        slide({
          headlineEn: "See the repeating rule",
          headlineUr: "دہرائی دیکھیں",
          bodyEn: `<p>Row N of stars has N stars — that pattern becomes a loop instead of five print statements.</p>`,
          bodyUr: `<p class="urdu-block">ہر قطار میں ستاروں کی تعداد بڑھتی ہے — لوپ لکھیں۔</p>`
        })
      ]),
      mod("2.3.3", "Abstraction", "خلاصہ (Abstraction)", false, [
        slide({
          headlineEn: "Hide the noise",
          headlineUr: "غیر ضروری چھپائیں",
          bodyEn: `<p>Tea algorithm: boil → steep → pour. Ignore cup colour and kettle brand.</p>`,
          bodyUr: `<p class="urdu-block">چائے کے ضروری قدم — برتن کا رنگ اہم نہیں۔</p>`
        })
      ]),
      mod("2.4.1", "Bubble & Selection Sort", "سورٹنگ", true, [
        slide({
          headlineEn: "★ Bubble sort",
          headlineUr: "★ بلبل سورٹ",
          bodyEn: `<p>Compare adjacent elements; swap if out of order; repeat until sorted. Time complexity \(O(n^2)\) for naive version.</p>`,
          bodyUr: `<p class="urdu-block">ملحق جوڑوں کو ترتیب دیں — دہرائیں۔</p>`,
          diagram: "bubbleSort"
        })
      ]),
      mod("2.4.2", "Linear & Binary Search", "تلاش", true, [
        slide({
          headlineEn: "★ Binary search",
          headlineUr: "★ بائنری سرچ",
          bodyEn: `<p>Requires sorted data. Check middle; go left or right. Complexity \(O(\log n)\).</p>`,
          bodyUr: `<p class="urdu-block">ترتیب شدہ فہرست — درمیان چیک کریں۔</p>`,
          diagram: "binarySearch"
        })
      ]),
      mod("2.5-2.6", "Algorithm Evaluation", "الگورتھم کا انتخاب", false, [
        slide({
          headlineEn: "Pick the right tool",
          headlineUr: "صحیح طریقہ",
          bodyEn: `<p>Consider time, memory, data size, sorted or not, and clarity for maintainers.</p>`,
          bodyUr: `<p class="urdu-block">وقت، میموری، ڈیٹا — سب سوچیں۔</p>`
        })
      ])
    ]
  };
}

function chapter3() {
  return {
    id: "ch3",
    number: 3,
    titleEn: "Programming Fundamentals",
    titleUr: "پروگرامنگ کی بنیادیں",
    modules: [
      mod("3.intro", "Variables, Data Types & I/O", "متغیرات اور I/O", true, [
        slide({
          headlineEn: "★ Program building blocks",
          headlineUr: "★ بنیادی اجزاء",
          bodyEn: `<p>Variables store values; data types (int, float, char, bool) tell the compiler how to interpret bits. Input/Output connects user and program.</p>`,
          bodyUr: `<p class="urdu-block">متغیرات values رکھتے ہیں؛ ڈیٹا ٹائپ معنی بتاتی ہے۔</p>`
        })
      ]),
      mod("3.control", "Control Structures", "کنٹرول سٹرکچر", true, [
        slide({
          headlineEn: "★ Sequence, selection, iteration",
          headlineUr: "★ ترتیب، انتخاب، دہراؤ",
          bodyEn: `<p><code>if/else</code> chooses paths; <code>for</code> and <code>while</code> repeat until condition ends. Trace one loop on paper — exam skill.</p>`,
          bodyUr: `<p class="urdu-block">if/else اور لوپ — کاغذ پر trace کریں۔</p>`
        })
      ]),
      mod("3.functions", "Functions & Modularity", "فنکشنز", false, [
        slide({
          headlineEn: "Reuse with functions",
          headlineUr: "فنکشن سے دوبارہ استعمال",
          bodyEn: `<p>Parameters in, return value out. Break programs into testable pieces.</p>`,
          bodyUr: `<p class="urdu-block">پیرامیٹر اندر، نتیجہ باہر۔</p>`
        })
      ])
    ]
  };
}

function chapter4() {
  return {
    id: "ch4",
    number: 4,
    titleEn: "Data & Databases",
    titleUr: "ڈیٹا اور ڈیٹابیس",
    modules: [
      mod("4.model", "Data Models", "ڈیٹا ماڈل", true, [
        slide({
          headlineEn: "★ Tables, keys, relationships",
          headlineUr: "★ ٹیبل، کیز، رشتے",
          bodyEn: `<p>Relational model: rows and columns. Primary key uniquely identifies a row; foreign keys link tables.</p>`,
          bodyUr: `<p class="urdu-block">قطاریں اور کالم — primary key منفرد۔</p>`
        })
      ]),
      mod("4.sql", "SQL Essentials", "SQL بنیادی", true, [
        slide({
          headlineEn: "★ SELECT, INSERT, UPDATE",
          headlineUr: "★ بنیادی SQL",
          bodyEn: `<p><code>SELECT</code> reads; <code>INSERT</code> adds; <code>UPDATE</code> changes; <code>DELETE</code> removes. Always <code>WHERE</code> carefully.</p>`,
          bodyUr: `<p class="urdu-block">SELECT پڑھیں؛ INSERT شامل؛ UPDATE تبدیل۔</p>`
        })
      ])
    ]
  };
}

function chapter5() {
  return {
    id: "ch5",
    number: 5,
    titleEn: "Networks & Security",
    titleUr: "نیٹ ورک اور سیکیورٹی",
    modules: [
      mod("5.net", "Network Devices & Topologies", "نیٹ ورک ٹاپولوجی", true, [
        slide({
          headlineEn: "★ LAN, WAN, devices",
          headlineUr: "★ LAN اور WAN",
          bodyEn: `<p>Hub, switch, router roles. Star vs bus topology — know diagrams and failure points.</p>`,
          bodyUr: `<p class="urdu-block">سوئچ اور روٹر کا فرق یاد رکھیں۔</p>`
        })
      ]),
      mod("5.sec", "Cybersecurity Basics", "سائبر سیکیورٹی", true, [
        slide({
          headlineEn: "★ Threats & protection",
          headlineUr: "★ خطرات اور حفاظت",
          bodyEn: `<p>Malware, phishing, strong passwords, encryption, backups — culture beats tools alone.</p>`,
          bodyUr: `<p class="urdu-block">فشنگ سے بچیں؛ مضبوط پاس ورڈ۔</p>`
        })
      ])
    ]
  };
}

function chapter6() {
  return {
    id: "ch6",
    number: 6,
    titleEn: "Emerging Technologies",
    titleUr: "ابھرتی ہوئی ٹیکنالوجی",
    modules: [
      mod("6.ai", "AI & Machine Learning intro", "AI تعارف", true, [
        slide({
          headlineEn: "★ Data → patterns → decisions",
          headlineUr: "★ ڈیٹا سے فیصلے",
          bodyEn: `<p>Machine learning finds patterns in data to predict or classify. Ethics: bias, privacy, human oversight.</p>`,
          bodyUr: `<p class="urdu-block">مشین لرننگ ڈیٹا میں پیٹرن — اخلاقیات نہ بھولیں۔</p>`
        })
      ]),
      mod("6.cloud", "Cloud & IoT overview", "کلاؤڈ اور IoT", false, [
        slide({
          headlineEn: "Always-on services",
          headlineUr: "کلاؤڈ خدمات",
          bodyEn: `<p>Cloud: rent compute/storage. IoT: sensors + network + actuators — smart homes, agriculture, health.</p>`,
          bodyUr: `<p class="urdu-block">کلاؤڈ وسائل؛ IoT سینسرز۔</p>`
        })
      ])
    ]
  };
}

/** Flat list of every module for progress & navigation */
export function allModules() {
  const list = [];
  for (const ch of CURRICULUM.chapters) {
    for (const m of ch.modules) {
      list.push({ chapter: ch, module: m });
    }
  }
  return list;
}
