window.LECTURES = {
  "chapters": [
    {
      "id": 1,
      "title": "کمپیوٹر سسٹم اور HCI",
      "en": "Computer Systems — HCI",
      "blurb": "انسان کے مطابق interface، رسائی، UI اور test"
    },
    {
      "id": 2,
      "title": "سوچ اور الگورتھم",
      "en": "Computational Thinking & Algorithms",
      "blurb": "trace، Big O، stack، queue، tree"
    },
    {
      "id": 3,
      "title": "Python کی بنیاد",
      "en": "Programming Fundamentals",
      "blurb": "list، set، function، file، exception"
    },
    {
      "id": 4,
      "title": "ڈیٹا اور تجزیہ",
      "en": "Data and Analysis",
      "blurb": "SQLite، Pandas، چارٹ، اوسط"
    },
    {
      "id": 5,
      "title": "کمپیوٹنگ کے اثرات",
      "en": "Applications and Impacts",
      "blurb": "neural network، حفاظت، equity"
    },
    {
      "id": 6,
      "title": "ڈیجیٹل کاروبار",
      "en": "Entrepreneurship in the Digital Age",
      "blurb": "prototype، MVP، beachhead"
    }
  ],
  "lectures": [
    {
      "id": "c1-hci",
      "chapter": 1,
      "title": "HCI اور حسی راستے",
      "minutes": 8,
      "diagram": "channels",
      "caption": "انسان اور کمپیوٹر پانچ حسی راستوں سے بات کرتے ہیں۔",
      "html": "<p>یہ لیکچر تم خود پڑھنے کے لیے ہے۔ استاد کے دوہری نوٹ کی نقل نہیں۔ جملے اردو میں ہیں، اور امتحان کی اصطلاحیں English میں۔</p>\n        <h2><span class=\"en\">HCI</span> کیا ہے؟</h2>\n        <p><span class=\"en\">Human-Computer Interaction</span>، مختصر <span class=\"en\">HCI</span>، وہ ڈیزائن ہے جس میں technology انسان کی خدمت کرے: استعمال آسان ہو، کام تیز ہو، اور نظام انسان کی ضرورت کا جواب دے۔</p>\n        <p>یہی خیال دو اور ناموں سے بھی پوچھا جاتا ہے: <span class=\"en\">CHI</span> یعنی <span class=\"en\">Computer-Human Interface</span>، اور <span class=\"en\">MMI</span> یعنی <span class=\"en\">Man-Machine Interaction</span>۔</p>\n        <h2>حسی راستے</h2>\n        <ul>\n          <li><b>بصارت، <span class=\"en\">sight</span>:</b> تم اسکرین، گراف یا ویڈیو دیکھتے ہو۔ کمپیوٹر monitor پر تصویر دکھاتا ہے۔</li>\n          <li><b>چھونا، <span class=\"en\">touch</span>:</b> تم tap، type یا swipe کرتے ہو۔ مشین click یا vibration دیتی ہے۔ اس لمس والے جواب کو <span class=\"en\">haptics</span> کہتے ہیں۔</li>\n          <li><b>سننا، <span class=\"en\">hearing</span>:</b> تم آواز سنتے ہو۔ speaker سے audio feedback آتا ہے۔</li>\n          <li><b>آواز، <span class=\"en\">voice</span>:</b> تم بول کر حکم دیتے ہو، جیسے کوئی نام پکارنا۔ نظام speech سمجھ کر جواب دیتا ہے۔</li>\n          <li><b>مکانی، <span class=\"en\">spatial</span>:</b> تم جسم یا جگہ میں حرکت کرتے ہو۔ <span class=\"en\">VR</span> جیسا نظام position track کرتا ہے۔</li>\n        </ul>\n        <div class=\"callout gold\"><b>امتحانی جملہ:</b> HCI کا مرکز انسان ہے، مشین نہیں۔ اچھا نظام انسان کی حسوں کے ذریعے بات کرتا ہے۔</div>",
      "golden": false,
      "checks": [
        {
          "q": "HCI کا دوسرا نام کیا ہو سکتا ہے؟",
          "options": [
            "صرف HTML",
            "CHI یا MMI",
            "صرف CPU",
            "صرف URL"
          ],
          "answer": 1,
          "why": "CHI اور MMI اسی انسان–مشین تعلق کے پرانے نام ہیں۔"
        },
        {
          "q": "Phone کی vibration کس حس کا جواب ہے؟",
          "options": [
            "sight",
            "touch / haptics",
            "spatial map",
            "CLI"
          ],
          "answer": 1,
          "why": "چھونے کے عمل پر جسمانی جواب haptics کہلاتا ہے۔"
        }
      ]
    },
    {
      "id": "c1-trad",
      "chapter": 1,
      "title": "Traditional اور Natural interaction",
      "minutes": 8,
      "diagram": "trad",
      "caption": "بائیں جانب mouse اور keyboard، دائیں جانب voice اور gesture۔",
      "html": "<h2><span class=\"en\">Traditional interaction</span></h2>\n        <p>یہ روزمرہ آلات کا پرانا، واضح طریقہ ہے۔ انسان standard input دیتا ہے اور output لیتا ہے۔</p>\n        <div class=\"compare\">\n          <div class=\"col\"><h3>Computer</h3><p>Mouse ہلانا اور keyboard پر لکھنا۔ Output monitor اور speakers سے آتا ہے۔</p></div>\n          <div class=\"col\"><h3>Smartphone</h3><p>Touchscreen پر tap اور swipe۔ Output روشنی اور vibration ہے۔</p></div>\n        </div>\n        <p>TV کا remote اور ATM کا keypad بھی traditional مثالیں ہیں۔ انسان کو بٹن کا قاعدہ پہلے سے پتا ہوتا ہے۔</p>\n        <h2><span class=\"en\">Natural interaction</span></h2>\n        <p>یہ وہ طریقہ ہے جس میں mouse یا keyboard لازمی نہیں۔ نظام انسان کی اپنی حرکت اور بولی کے قریب ہوتا ہے۔</p>\n        <ul>\n          <li><b><span class=\"en\">Voice</span>:</b> آلہ سے بولنا، مثلاً گانا چلانے کا حکم۔</li>\n          <li><b><span class=\"en\">Body &amp; gesture</span>:</b> چہرے سے فون کھولنا، یا ہاتھ ہلا کر VR کھیلنا۔</li>\n        </ul>\n        <div class=\"callout do\"><b>خود کرو:</b> آج کے تین traditional interface اور تین natural interface اپنی کاپی میں لکھو۔ FaceID، voice assistant، اور Kinect طرز کے کھیل natural طرف آتے ہیں۔</div>",
      "golden": false,
      "checks": [
        {
          "q": "Keyboard اور mouse کس قسم کی interaction ہیں؟",
          "options": [
            "Natural",
            "Traditional",
            "صرف haptic",
            "صرف biometric"
          ],
          "answer": 1,
          "why": "معیاری input/output والے روزمرہ طریقے traditional کہلاتے ہیں۔"
        },
        {
          "q": "بغیر mouse کے بول کر حکم دینا کیا ہے؟",
          "options": [
            "CLI صرف",
            "Natural voice interaction",
            "Form fill",
            "Low-fidelity wireframe"
          ],
          "answer": 1,
          "why": "بولی سے براہِ راست حکم natural interaction کی مثال ہے۔"
        }
      ]
    },
    {
      "id": "c1-apps",
      "chapter": 1,
      "title": "زندگی کے میدانوں میں HCI",
      "minutes": 9,
      "diagram": "domains",
      "caption": "صحت، بینک، تعلیم، اور رابطہ: چار میدان جہاں HCI کام آتی ہے۔",
      "html": "<p class=\"callout gold\">یہ golden topic ہے۔ Paper میں مثال سمیت میدان پوچھے جاتے ہیں۔</p>\n        <p><span class=\"en\">HCI</span> صرف تعریف نہیں۔ اس سے desktop app، website، اور mobile app ایسے بنتے ہیں جو انسان کی ضرورت کے گرد ہوں۔</p>\n        <div class=\"compare\">\n          <div class=\"col\"><h3>صحت</h3><p>Patient portal، telemedicine، اور assistive technology۔ فائدہ: علاج تک دور سے رسائی۔</p></div>\n          <div class=\"col\"><h3>بینکاری</h3><p>Mobile banking اور محفوظ ATM۔ فائدہ: تیز لین دین اور رقم کا نظم۔</p></div>\n          <div class=\"col\"><h3>تعلیم</h3><p><span class=\"en\">LMS</span> اور online exam۔ فائدہ: پڑھائی اور مشق میں شمولیت۔</p></div>\n          <div class=\"col\"><h3>رابطہ</h3><p>Messaging اور video call۔ فائدہ: دور بیٹھے لوگ ایک کام میں شریک ہو سکتے ہیں۔</p></div>\n        </div>\n        <p>جواب لکھتے وقت تین حصے رکھو: میدان کا نام، ایک ٹھوس مثال، اور user کو فائدہ۔ صرف یہ مت لکھو کہ “app آسان ہے”۔</p>",
      "golden": true,
      "checks": [
        {
          "q": "Telemedicine کس میدان کی HCI مثال ہے؟",
          "options": [
            "صرف gaming",
            "Health care",
            "Stack",
            "Beachhead"
          ],
          "answer": 1,
          "why": "مریض کا دور سے معائنہ صحت کے میدان میں آتا ہے۔"
        },
        {
          "q": "LMS کس کا فائدہ بڑھاتا ہے؟",
          "options": [
            "صرف printer کی سیاہی",
            "تعلیم، سیکھنا، اور student کی شمولیت",
            "صرف hard disk",
            "صرف IP address"
          ],
          "answer": 1,
          "why": "LMS کلاس، مواد، اور امتحان کو ایک انسانی بہاؤ میں جوڑتا ہے۔"
        }
      ]
    },
    {
      "id": "c1-parts",
      "chapter": 1,
      "title": "اجزاء اور interaction کی اقسام",
      "minutes": 10,
      "diagram": "ui",
      "caption": "Interface کی شکلیں: GUI، CLI، touch، voice، اور natural۔",
      "html": "<h2>HCI کے بنیادی اجزاء</h2>\n        <ul>\n          <li><b><span class=\"en\">User</span>:</b> وہ فرد یا گروہ جو مقصد کے لیے نظام چلاتا ہے۔ <span class=\"en\">End user</span> خود چلاتا ہے۔ <span class=\"en\">Stakeholder</span> نتیجے میں دلچسپی رکھتا ہے، جیسے manager یا client۔</li>\n          <li><b><span class=\"en\">Computer system</span>:</b> وہ پلیٹ فارم جہاں input، output، اور feedback ایک interface سے جڑتے ہیں۔</li>\n          <li><b><span class=\"en\">User interaction</span>:</b> click، tap، type، یا بولنے سے ارادہ نظام کے جواب میں بدلتا ہے۔</li>\n          <li><b><span class=\"en\">Task</span>:</b> مخصوص کام، جیسے ٹکٹ بک کرنا۔ اس کی complexity، درکار مہارت، اور وقت الگ الگ ہوتے ہیں۔ فارم بھرنا ہلکا task ہے؛ 3D model بھاری۔</li>\n        </ul>\n        <h2>Interaction کی اقسام</h2>\n        <ul>\n          <li><b><span class=\"en\">Manipulation</span>:</b> فائل گھسیٹنا، انگلی سے zoom۔</li>\n          <li><b><span class=\"en\">Command-based</span>:</b> متن کا حکم، جیسے terminal۔</li>\n          <li><b><span class=\"en\">Menu-driven</span>:</b> تیار فہرست سے انتخاب۔</li>\n          <li><b><span class=\"en\">Form fill</span>:</b> خانوں میں منظم ڈیٹا۔</li>\n          <li><b><span class=\"en\">Conversational</span>:</b> chatbot یا voice assistant سے قدرتی زبان۔</li>\n          <li><b><span class=\"en\">Gesture</span>، <span class=\"en\">voice</span>، <span class=\"en\">biometric</span>:</b> ہاتھ، بولی، یا انگلی کا نشان۔</li>\n          <li><b><span class=\"en\">Context-aware</span>:</b> نظام کمرے میں داخلے پر خود بتی جلا دے۔</li>\n          <li><b><span class=\"en\">Haptic</span>:</b> عمل کی تصدیق کے لیے vibration۔</li>\n          <li><b><span class=\"en\">Multimodal</span>:</b> دو یا زیادہ طریقے اکٹھے، جیسے بول کر ڈھونڈنا پھر انگلی سے چننا۔</li>\n        </ul>",
      "golden": false,
      "checks": [
        {
          "q": "Manager جو نظام خود نہ چلائے مگر نتیجہ چاہے، کیا کہلائے گا؟",
          "options": [
            "صرف icon",
            "Stakeholder",
            "Haptic pixel",
            "Wireframe"
          ],
          "answer": 1,
          "why": "Stakeholder نتیجے میں شریک ہوتا ہے؛ end user براہِ راست چلاتا ہے۔"
        },
        {
          "q": "Terminal میں متن لکھ کر حکم دینا کون سی قسم ہے؟",
          "options": [
            "Command-based",
            "Pie chart",
            "Beachhead",
            "Median"
          ],
          "answer": 0,
          "why": "ٹائپ کیا ہوا دقیق حکم command-based interaction ہے۔"
        }
      ]
    },
    {
      "id": "c1-feedback",
      "chapter": 1,
      "title": "Interface، ماحول، اور feedback",
      "minutes": 8,
      "diagram": "ui",
      "caption": "پانچ طرح کے interface ایک ہی کام کو مختلف احساس دیتے ہیں۔",
      "html": "<h2><span class=\"en\">User interface</span></h2>\n        <p>UI وہ وسیلہ ہے جس سے انسان نظام کو چھوتا ہے۔</p>\n        <ul>\n          <li><b><span class=\"en\">GUI</span>:</b> windows، icons، menus۔ مثال: desktop OS۔</li>\n          <li><b><span class=\"en\">CLI</span>:</b> صرف متن۔ مثال: Linux terminal۔</li>\n          <li><b><span class=\"en\">Touch</span>:</b> tap، swipe، pinch۔</li>\n          <li><b><span class=\"en\">VUI</span>:</b> بولی سے حکم، جیسے smart speaker۔</li>\n          <li><b><span class=\"en\">NUI</span>:</b> جسم کی حرکت یا VR جیسا ماحول۔</li>\n        </ul>\n        <h2>ماحول</h2>\n        <p><span class=\"en\">Environment</span> وہ اصلی جگہ ہے جہاں نظام چلتا ہے۔ دھوپ میں ATM، خاموش کلاس، اور کمزور network تین مختلف ماحول ہیں۔ ڈیزائن کو روشنی، شور، اور hardware دیکھ کر بدلنا پڑتا ہے۔</p>\n        <h2>Feedback</h2>\n        <div class=\"compare\">\n          <div class=\"col\"><h3>System feedback</h3><p>مشین بتاتی ہے کہ ہوا کیا۔ “لوڈ ہو رہا ہے”، بھیجا گیا کا نشان، یا error۔</p></div>\n          <div class=\"col\"><h3>User feedback</h3><p>انسان نظام کو بتاتا ہے: Submit دبانا، یا پانچ میں سے ستارے دینا۔</p></div>\n        </div>",
      "golden": false,
      "checks": [
        {
          "q": "Smart speaker پر بولنا کس interface کی مثال ہے؟",
          "options": [
            "CLI",
            "VUI",
            "صرف histogram",
            "Tuple"
          ],
          "answer": 1,
          "why": "Voice User Interface بولی کو input بناتا ہے۔"
        },
        {
          "q": "Loading کا نشان کس قسم کا feedback ہے؟",
          "options": [
            "User feedback",
            "System feedback",
            "Beachhead",
            "Variance"
          ],
          "answer": 1,
          "why": "یہ مشین کی طرف سے تصدیق ہے کہ کام جاری ہے۔"
        }
      ]
    },
    {
      "id": "c1-access",
      "chapter": 1,
      "title": "اہمیت، رسائی، اور need analysis",
      "minutes": 10,
      "diagram": "equity",
      "caption": "Equal access ایک جیسا دروازہ ہے؛ equity اضافی سہارا ہے۔ یہ خیال HCI میں بھی کام آتا ہے۔",
      "html": "<p class=\"callout gold\">Importance of HCI امتحان کا سنہری حصہ ہے۔</p>\n        <p>اچھا HCI مشین کو قریب اور قابلِ استعمال بناتا ہے۔ Touchscreen نے پیچیدہ کمپیوٹر کو روزمرہ آلہ بنا دیا۔ کمزور ڈیزائن الجھن اور خطرہ پیدا کرتا ہے، جیسے طبی آلے پر دھندلے بٹن۔</p>\n        <ul>\n          <li><b>پیداوار:</b> کم غلطی، تیز مقصد۔</li>\n          <li><b>شمولیت:</b> screen reader اور voice command ان لوگوں کو شامل کرتے ہیں جو بصارت یا ہاتھ کی حد سے رکے ہوں۔</li>\n          <li><b>ایجاد:</b> AR، VR، AI، اور IoT تب اپنائے جاتے ہیں جب HCI صاف ہو۔</li>\n          <li><b>معیشت:</b> آسان مصنوعات زیادہ بکتیں ہیں اور اعتماد رکھتی ہیں۔</li>\n          <li><b>ذمہ داری:</b> privacy، کم bias، اور انسان کی بھلائی۔</li>\n        </ul>\n        <h2>Accessibility کے اصول</h2>\n        <ul>\n          <li><b>High contrast:</b> دھوپ میں بھی متن الگ دکھے۔</li>\n          <li><b>پڑھنے کے قابل فونٹ:</b> سادہ رسم، مناسب سائز اور فاصلہ۔</li>\n          <li><b>Colour-blind friendly:</b> صرف رنگ پر بھروسہ نہیں؛ نشان یا لفظ بھی ہو، جیسے سرخ دائرے کے ساتھ STOP۔</li>\n          <li><b>Inclusive navigation:</b> mouse کے علاوہ Tab سے بٹن تک پہنچنا۔</li>\n          <li><b>Multimodal:</b> ویڈیو کے ساتھ caption، یا خاموش الارم کے لیے vibration۔</li>\n        </ul>\n        <h2><span class=\"en\">Need analysis</span></h2>\n        <p>ڈیزائن سے پہلے یہ خلا دیکھو: اب کیا ہے، اور ہونا کیا چاہیے۔ ترتیب یہ ہے: user کون ہے، interview یا observation سے معلومات، ضرورتوں کا تجزیہ، ترجیح، پھر حل۔</p>\n        <div class=\"callout do\"><b>مثال:</b> بینک app سے پہلے گاہک بتاتے ہیں کہ fingerprint login چاہیے، بزرگوں کو بڑے بٹن چاہییں، اور مقامی زبان بھی۔ UI ان ثابت شدہ ضرورتوں کے گرد بنتا ہے۔</div>",
      "golden": true,
      "checks": [
        {
          "q": "صرف سرخ رنگ سے خطرہ دکھانا کس اصول کے خلاف ہے؟",
          "options": [
            "Colour-blind friendly design",
            "Stack overflow",
            "FIFO",
            "Median"
          ],
          "answer": 0,
          "why": "رنگ کے ساتھ لفظ یا نشان بھی ہونا چاہیے۔"
        },
        {
          "q": "Need analysis کب ہوتی ہے؟",
          "options": [
            "صرف app چھپنے کے بعد",
            "UI ڈیزائن سے پہلے",
            "صرف hard disk فارمیٹ پر",
            "صرف امتحان کے دن"
          ],
          "answer": 1,
          "why": "ضرورت سمجھے بغیر اسکرین بنانا اندھا ڈیزائن ہے۔"
        }
      ]
    },
    {
      "id": "c1-problems",
      "chapter": 1,
      "title": "HCI کے مسائل اور بہتری",
      "minutes": 9,
      "diagram": "trad",
      "caption": "مسئلہ انسان کی حد سے ٹکراؤ ہے؛ بہتری usability اور feedback سے آتی ہے۔",
      "html": "<p class=\"callout gold\">Problems of HCI سنہری topic ہے۔ ہر مسئلے کے ساتھ ایک زندگی کی مثال لکھنا۔</p>\n        <ul>\n          <li><b><span class=\"en\">Interface complexity</span>:</b> اتنے مینو کہ checkout ملے ہی نہیں۔</li>\n          <li><b><span class=\"en\">Poor feedback</span>:</b> Submit کے بعد سکرین جم جائے، نہ کامیابی نہ error۔</li>\n          <li><b><span class=\"en\">Inconsistency</span>:</b> ایک صفحے پر search کا ذرہ بین، دوسرے پر کوئی اور نشان۔</li>\n          <li><b><span class=\"en\">Accessibility gaps</span>:</b> ویڈیو سبق بغیر caption۔</li>\n          <li><b><span class=\"en\">Compatibility</span>:</b> laptop پر چلے، mobile browser پر ٹوٹ جائے۔</li>\n          <li><b><span class=\"en\">Contextual neglect</span>:</b> رات کو نقشے میں dark mode نہ ہو اور ڈرائیور کو روشنی اندھا کر دے۔</li>\n          <li><b><span class=\"en\">High cognitive load</span>:</b> ایک ساتھ تین SMS کوڈ یاد رکھنے کی شرط۔</li>\n          <li><b><span class=\"en\">Trust deficiency</span>:</b> ادائیگی مانگو مگر محفوظ کنکشن کا کوئی نشان نہ دو۔</li>\n        </ul>\n        <h2>بہتری کے طریقے</h2>\n        <p>Navigation سادہ کرو۔ Accessibility بڑھاؤ۔ ایک جیسا Save بٹن رکھو۔ “ادائیگی ہو گئی” جیسا صاف feedback دو۔ اسکرین چھوٹی ہو تو layout ڈھل جائے۔ <span class=\"en\">User-centered design</span> میں اصلی user کے مقصد سے شروع کرو اور چھوٹا pilot test لو۔ Touch اور voice کو اکٹھا کرنے دو۔ پھر feedback سے مسلسل سدھارتے رہو۔</p>",
      "golden": true,
      "checks": [
        {
          "q": "Submit کے بعد کوئی پیغام نہ آنا کون سا مسئلہ ہے؟",
          "options": [
            "Poor feedback",
            "Beachhead",
            "Tuple immutability",
            "Mean"
          ],
          "answer": 0,
          "why": "نظام نے یہ نہیں بتایا کہ عمل ہوا یا ناکام۔"
        },
        {
          "q": "User-centered design کس پر مرکوز ہے؟",
          "options": [
            "صرف مشین کی رفتار",
            "اصلی user کے مقصد",
            "صرف فونٹ کا نام",
            "صرف IP"
          ],
          "answer": 1,
          "why": "UCD انسان کے کام سے ڈیزائن شروع کرتا ہے۔"
        }
      ]
    },
    {
      "id": "c1-design",
      "chapter": 1,
      "title": "UI، UX، wireframe، اور testing",
      "minutes": 11,
      "diagram": "wire",
      "caption": "بائیں خاکہ ساخت ہے، دائیں نمونہ رنگ اور بٹن کے ساتھ۔",
      "html": "<p class=\"callout gold\">UI بمقابلہ UX، اور testing کے طریقے، دونوں سنہری ہیں۔</p>\n        <p><span class=\"en\">UI design</span> نظر آنے والے حصوں کو یوں سجاتا ہے کہ کام آسان ہو: button، menu، icon، text field، checkbox، radio، slider۔</p>\n        <p><span class=\"en\">UX</span> پورا احساس ہے: رفتار، سہولت، اور اطمینان۔ کھانے کی app میں برگر کی تصویر UI ہے۔ یہ UX ہے کہ آرڈر جلدی لگے، ٹریکنگ سمجھ آئے، اور آدمی بیزار نہ ہو۔ یاد رکھو: UI وہ ہے جو نظر آئے؛ UX وہ ہے جو محسوس ہو۔</p>\n        <h2>Wireframe اور prototype</h2>\n        <div class=\"compare\">\n          <div class=\"col\"><h3>Low-fidelity</h3><p>سیاہ سفید خاکہ۔ ڈبے اور لکیریں۔ شروع میں ساخت جانچنے کے لیے۔ رنگ ابھی موضوع نہیں۔</p></div>\n          <div class=\"col\"><h3>High-fidelity</h3><p>لگ بھگ اصلی اسکرین: فونٹ، رنگ، تصویر، دبنے والے بٹن۔ آخری جانچ کے لیے۔</p></div>\n        </div>\n        <p><span class=\"en\">Figma</span> براؤزر میں UI اور prototype بنانے کا آلہ ہے۔ Frame سے موبائل اسکرین، shapes سے بٹن، text سے عنوان، پھر frame نقل کر کے اگلی اسکرین۔ Prototype ٹیب میں trigger، جیسے tap، اور action، جیسے اگلی اسکرین پر جانا، جوڑتے ہیں۔ کوڈ سے پہلے لوگ جعلی app چلا کر راستہ دیکھتے ہیں۔</p>\n        <h2>Test اور evaluation</h2>\n        <p><span class=\"en\">Testing</span> پوچھتا ہے کہ چیز ٹوٹتی تو نہیں۔ <span class=\"en\">Evaluation</span> پوچھتا ہے کہ انسان کی ضرورت پوری ہوتی ہے یا نہیں۔</p>\n        <ul>\n          <li><b><span class=\"en\">SUS</span>:</b> دس سوالوں کا usability اسکور۔</li>\n          <li><b><span class=\"en\">NPS</span>:</b> “کیا دوست کو تجویز کرو گے؟” وفاداری کا ناپ۔</li>\n          <li><b>Formative:</b> بناتے وقت سدھار۔ <b>Summative:</b> آخر میں کامیابی ناپنا۔</li>\n          <li><b>Expert review:</b> ماہر heuristics سے جائزہ۔</li>\n          <li><b>Usability testing:</b> اصلی user سے کام کراؤ اور اٹکاؤ دیکھو۔</li>\n          <li><b>Task-based:</b> “کارٹ میں ڈالو” جیسا کام؛ وقت، کامیابی، غلطیاں لکھو۔</li>\n          <li><b>Automated audit:</b> بوٹ ٹوٹی link، سست صفحہ، یا کم contrast ڈھونڈے۔</li>\n          <li><b>A/B testing:</b> آدھے لوگ نسخہ A دیکھیں، آدھے B۔ جس پر زیادہ مکمل کام ہو وہ جیتے گا۔</li>\n          <li><b>Compatibility:</b> مختلف browser، فون، اور OS۔</li>\n          <li><b>Performance / load:</b> بیک وقت بہت سے user پر رفتار اور سرور۔</li>\n          <li><b>Keyboard اور screen reader:</b> صرف Tab اور مددگار آواز سے راستہ۔</li>\n        </ul>\n        <div class=\"callout\"><b>کام:</b> UX designer ضرورت جانتا ہے۔ UI designer شکل بناتا ہے۔ Interaction designer اسکرینوں کا بہاؤ۔ Usability researcher ٹیسٹ چلاتا ہے۔ Accessibility specialist شمولیت کا معیار دیکھتا ہے۔</div>",
      "golden": true,
      "checks": [
        {
          "q": "کھانے کی app میں خوبصورت بٹن UI ہے یا UX؟",
          "options": [
            "صرف UX",
            "نظر آنے والا حصہ UI ہے",
            "نہ UI نہ UX",
            "صرف Big O"
          ],
          "answer": 1,
          "why": "شکل UI ہے؛ بے جھنجٹ مکمل تجربہ UX ہے۔"
        },
        {
          "q": "دو ڈیزائن میں سے بہتر چننے کا ٹیسٹ کیا کہلاتا ہے؟",
          "options": [
            "A/B testing",
            "Stack push",
            "Mode of a list",
            "Encryption key"
          ],
          "answer": 0,
          "why": "نسخہ A اور B ایک ہی کام پر مقابلے میں رکھے جاتے ہیں۔"
        }
      ]
    },
    {
      "id": "c2-trace",
      "chapter": 2,
      "title": "درستگی اور trace table",
      "minutes": 10,
      "diagram": "array",
      "caption": "Trace table ہر قدم پر متغیر کا خانہ دکھاتی ہے، جیسے array کے خانے۔",
      "html": "<p>الگورتھم تب درست ہے جب ہر جائز input پر وہی output آئے جو مقصد ہو۔ دو مشہور طریقے ہیں: <span class=\"en\">trace table</span> اور <span class=\"en\">stepwise reasoning</span>۔</p>\n        <p class=\"callout gold\">Trace table سنہرا طریقہ ہے: کاغذ پر dry run۔</p>\n        <p>اس سے تین کام ہوتے ہیں: خط بہ خط چلانا، منطقی غلطی پکڑنا، اور یہ دیکھنا کہ الگورتھم وعدہ پورا کرتا ہے۔ کالم ہوتے ہیں: لائن، متغیر، input/output، اور شرط۔</p>\n        <h2>خود چلاؤ</h2>\n        <p>کالج گیٹ پر حاضری کا فیصد 75 سے 100 کے درمیان ہو تو طالب علم شمار ہو۔</p>\n        <div class=\"math\" data-speak=\"حاضری پچھتر سے بڑی یا برابر، اور سو سے چھوٹی یا برابر\">\\[75 \\le a \\le 100\\]</div>\n        <pre class=\"code\" data-speak=\"حاضری گننے کے نو قدم۔ کل صفر سے شروع، پھر ہر عدد پر شرط۔\">Total = 0\nmarks = [80, 70, 90, 75, 60]\nFOR each a in marks\n  IF a &gt;= 75 AND a &lt;= 100 THEN\n    Total = Total + 1\n  END IF\nEND FOR\nPRINT Total</pre>\n        <table class=\"data\">\n          <tr><th>a</th><th>شرط</th><th>Total</th></tr>\n          <tr><td>80</td><td>سچ</td><td>1</td></tr>\n          <tr><td>70</td><td>جھوٹ</td><td>1</td></tr>\n          <tr><td>90</td><td>سچ</td><td>2</td></tr>\n          <tr><td>75</td><td>سچ</td><td>3</td></tr>\n          <tr><td>60</td><td>جھوٹ</td><td>3</td></tr>\n        </table>\n        <p>آخری چھاپ 3 ہے۔ 70 اور 60 شرط کے باہر ہیں۔ 75 شامل ہے کیونکہ نشان برابر کو بھی مانتا ہے۔</p>",
      "golden": true,
      "checks": [
        {
          "q": "Trace table کس کام آتی ہے؟",
          "options": [
            "صرف رنگ چننے",
            "متغیرات کا کاغذی dry run",
            "صرف فونٹ",
            "MVP بیچنا"
          ],
          "answer": 1,
          "why": "یہ الگورتھم کو ہاتھ سے چلا کر قدریں لکھتی ہے۔"
        },
        {
          "q": "اوپر والی جدول میں Total آخر میں کتنا ہے؟",
          "options": [
            "2",
            "3",
            "5",
            "0"
          ],
          "answer": 1,
          "why": "80، 90، اور 75 تین جائز قدریں ہیں۔"
        }
      ]
    },
    {
      "id": "c2-step",
      "chapter": 2,
      "title": "Stepwise reasoning اور موازنہ",
      "minutes": 8,
      "diagram": "func",
      "caption": "Stepwise reasoning پورے بلاک کی حالت دیکھتا ہے، ایک ایک خانہ نہیں۔",
      "html": "<p><span class=\"en\">Stepwise reasoning</span> الگورتھم کو منطقی ٹکڑوں میں توڑ کر ہر مرحلے کی state جانچتا ہے۔ اسے logic verification بھی کہتے ہیں۔ جدول کی ہر صف ضروری نہیں؛ سوچ یہ دیکھتی ہے کہ حالت درست رہتی ہے یا نہیں۔</p>\n        <p>سوال یہ ہیں: شروع کی state جائز ہے؟ ہر کیس سنبھلتا ہے؟ شرطیں صحیح ہیں؟ اگر لوپ ایک چکر کے شروع پر درست ہے تو چکر کے آخر پر بھی درست رہتا ہے؟</p>\n        <h2>1 سے N تک جمع</h2>\n        <div class=\"math\" data-speak=\"ایک سے این تک جمع، این ضرب این جمع ایک، تقسیم دو\">\\[\\sum_{i=1}^{N} i = \\frac{N(N+1)}{2}\\]</div>\n        <p>شروع میں Sum = 0، یہ جائز ہے۔ لوپ ٹھیک 1 سے N تک چلتا ہے۔ ہر عدد جمع میں شامل ہوتا ہے۔ N = 0 پر لوپ نہیں چلتا، Sum صفر رہتا ہے۔ N = 5 پر Sum پندرہ ہوتا ہے۔ دونوں کنارے درست ہیں۔</p>\n        <div class=\"compare\">\n          <div class=\"col\"><h3>Trace table</h3><p>چھوٹے بلاک، الجھے لوپ، اور ابتدائی سیکھنے والے کے لیے۔ محنت زیادہ۔ ایک ایک قدر پکڑتی ہے۔</p></div>\n          <div class=\"col\"><h3>Stepwise</h3><p>بڑے نظام اور خیال کی درستگی کے لیے۔ محنت درمیانی۔ ساخت کی خرابی پکڑتی ہے۔</p></div>\n        </div>",
      "golden": true,
      "checks": [
        {
          "q": "N = 5 پر 1 سے N کی جمع کتنی ہے؟",
          "options": [
            "10",
            "15",
            "25",
            "5"
          ],
          "answer": 1,
          "why": "فارمولا 5 ضرب 6 تقسیم 2 = 15 دیتا ہے۔"
        },
        {
          "q": "ہزار چکر والے لوپ کی ہر قدر لکھنا کس کے لیے بھاری ہے؟",
          "options": [
            "Trace table",
            "صرف icon",
            "Caption",
            "Equity"
          ],
          "answer": 0,
          "why": "Trace table بڑے لوپ پر تھکا دینے والی ہو جاتی ہے۔"
        }
      ]
    },
    {
      "id": "c2-clear",
      "chapter": 2,
      "title": "وضاحت: modularity اور readability",
      "minutes": 8,
      "diagram": "func",
      "caption": "فنکشن input لیتا ہے، ایک کام کرتا ہے، اور return نکالتا ہے۔",
      "html": "<p>Clarity کا مطلب ہے کہ دوسرا شخص بغیر چلائے منطق پڑھ لے۔ اکثر رفتار سے پہلے وضاحت ضروری ہے، کیونکہ صاف الگورتھم سدھرتا اور بڑھتا ہے۔ دو ستون ہیں: <span class=\"en\">modularity</span> اور <span class=\"en\">readability</span>۔</p>\n        <h2>Modularity</h2>\n        <ul>\n          <li><b><span class=\"en\">Single responsibility</span>:</b> ایک ماڈیول ایک کام۔ جمع اور چھپائی الگ ہوں۔</li>\n          <li><b>Loose coupling:</b> ایک حصہ بدلے تو باقی نہ ٹوٹے۔</li>\n          <li><b>Abstraction:</b> sort بلانے والے کو یہ جاننے کی ضرورت نہیں کہ اندر bubble ہے یا کوئی اور طریقہ۔</li>\n        </ul>\n        <p>کمزور ڈھانچہ ساری اوسط ایک بلاک میں گنتا ہے۔ بہتر ڈھانچہ <span class=\"en\">sum</span> اور <span class=\"en\">average</span> کو الگ فنکشن بنا دیتا ہے تاکہ دونوں دوبارہ استعمال ہوں۔</p>\n        <h2>Readability</h2>\n        <p>نام معنی رکھیں۔ <span class=\"en\">a = b / c</span> کی جگہ <span class=\"en\">average = total / count</span>۔ اندر کی طرف یکساں وقفہ۔ تبصرہ یہ بتائے کہ کیوں، نہ کہ کوڈ نے جو ظاہر کیا ہے اسے دہرائے۔ گہری شرطیں توڑ کر نام دو۔</p>",
      "golden": false,
      "checks": [
        {
          "q": "ایک فنکشن جو جمع بھی کرے، فائل بھی لکھے، اور اسکرین بھی رنگے، کس اصول کو توڑتا ہے؟",
          "options": [
            "Single responsibility",
            "FIFO",
            "Contrast",
            "Median"
          ],
          "answer": 0,
          "why": "ایک ماڈیول پر ایک ذمہ داری ہونی چاہیے۔"
        },
        {
          "q": "Readability کس بات کا نام ہے؟",
          "options": [
            "صرف تیز ترین CPU",
            "بغیر چلائے منطق سمجھ آنا",
            "صرف encrypted disk",
            "صرف VPN"
          ],
          "answer": 1,
          "why": "پڑھنے والا بہاؤ اور ناموں سے مقصد پہچان لے۔"
        }
      ]
    },
    {
      "id": "c2-bigo",
      "chapter": 2,
      "title": "Efficiency اور Big O",
      "minutes": 12,
      "diagram": "bigo",
      "caption": "O(1) سیدھی لکیر، O(n) ترچھی، O(n²) تیزی سے اوپر اٹھتی ہے۔",
      "html": "<p class=\"callout gold\">Big O سنہری topic ہے۔ وقت اور جگہ دونوں پوچھے جاتے ہیں: الگورتھم کتنا تیز ہے اور کتنی memory لیتا ہے۔</p>\n        <p>ہم یہ دیکھتے ہیں کہ input کا سائز n بڑھے تو کام کیسے بڑھتا ہے۔</p>\n        <ul>\n          <li><b>Constant، </b> <span class=\"en\">O(1)</span>: دس ہوں یا دس لاکھ، پہلا خانہ ایک ہی وقت میں کھلتا ہے۔</li>\n          <li><b>Linear، </b> <span class=\"en\">O(n)</span>: فہرست دگنی ہو تو لکیری تلاش کا وقت بھی لگ بھگ دگنا۔</li>\n          <li><b>Logarithmic، </b> <span class=\"en\">O(log n)</span>: ہر قدم مسئلہ آدھا۔ ترتیب شدہ فہرست پر binary search۔</li>\n          <li><b>Quadratic، </b> <span class=\"en\">O(n^2)</span>: اندر اندر لوپ، جیسے ہر جوڑے کا موازنہ۔ بڑے n پر مہنگا۔</li>\n        </ul>\n        <div class=\"math\" data-speak=\"او آف لاگ این، اور او آف این اسکوائر\">\\[O(1),\\quad O(\\log n),\\quad O(n),\\quad O(n^{2})\\]</div>\n        <p>Binary search میں قدموں کی تعداد لگ بھگ یہ ہے:</p>\n        <div class=\"math\" data-speak=\"فلور لاگ بیس دو این، جمع ایک\">\\[\\lfloor \\log_2 n \\rfloor + 1\\]</div>\n        <h2>شرطیں اور تکرار</h2>\n        <p>ہر <span class=\"en\">IF</span> فیصلہ ہے۔ اندر اندر شرطیں پڑھنا اور رفتار دونوں خراب کرتی ہیں۔ <span class=\"en\">Short-circuit</span> میں نتیجہ ملتے ہی مزید شرط نہ جانچو۔</p>\n        <p>لوپ سب سے بڑا اثر رکھتا ہے۔ ایک لکیری لوپ O(n) ہے۔ آدھا کرتے رہنے والا لوپ O(log n) ہے۔ nested لوپ O(n²) کی طرف جاتا ہے۔</p>\n        <h2>تین سوال</h2>\n        <ol>\n          <li>اگر n دس گنا ہو تو وقت دس گنا بڑھے گا یا سو گنا؟ سو گنا quadratic ناکامی ہے۔</li>\n          <li>رکاوٹ کہاں ہے؟ اکثر گہرا لوپ۔</li>\n          <li>کیا یہ قیمت فائدے کے لائق ہے؟ بہت تیز مگر نہ پڑھے جانے والا طریقہ ہمیشہ جیت نہیں۔</li>\n        </ol>",
      "golden": true,
      "checks": [
        {
          "q": "ترتیب شدہ فہرست میں binary search کی نشوونما کیا ہے؟",
          "options": [
            "O(n²)",
            "O(log n)",
            "O(n!)",
            "O(n³) لازماً"
          ],
          "answer": 1,
          "why": "ہر قدم تلاش آدھی رہ جاتی ہے۔"
        },
        {
          "q": "اندر اندر دو لوپ اکثر کون سی کلاس دیتے ہیں؟",
          "options": [
            "O(1)",
            "O(n²)",
            "O(0)",
            "صرف median"
          ],
          "answer": 1,
          "why": "ہر عنصر کے لیے باقی عناصر دیکھنا مربع وقت ہے۔"
        }
      ]
    },
    {
      "id": "c2-refine",
      "chapter": 2,
      "title": "وضاحت اور رفتار کی اصلاح",
      "minutes": 8,
      "diagram": "bigo",
      "caption": "اصلاح کا مقصد بے کار قدم ہٹانا اور مناسب ڈھانچہ چننا ہے۔",
      "html": "<h2>وضاحت کی اصلاح</h2>\n        <ul>\n          <li>معنی والے نام: <span class=\"en\">average = totalSum / totalItems</span>۔</li>\n          <li>کاموں کو فنکشن میں بانٹو۔</li>\n          <li>اندر کی جگہ یکساں رکھو تاکہ لوپ کی گہرائی نظر آئے۔</li>\n          <li>مختصر تبصرہ، خاص کر وہاں جہاں سبب چھپا ہو۔</li>\n        </ul>\n        <h2>رفتار کی اصلاح</h2>\n        <ul>\n          <li>بے کار قدم کاٹو۔ Bubble sort کے ایک پاس کے بعد آخری بڑی قدر اپنی جگہ بیٹھ جاتی ہے؛ اگلا اندرونی لوپ اسے دوبارہ نہ چھیڑے۔</li>\n          <li>کام کے مطابق طریقہ: دس لاکھ ترتیب شدہ ریکارڈ میں linear search کی جگہ binary search۔</li>\n          <li>جو قدر لوپ میں نہیں بدلتی اسے باہر ایک بار نکالو اور دوبارہ استعمال کرو۔</li>\n          <li>ڈھانچہ کام کے مطابق ہو: بار بار آخر سے نکالنا ہو تو stack سوچو؛ باری کی قطار ہو تو queue۔</li>\n        </ul>\n        <pre class=\"code\" data-speak=\"مستقل ضرب لوپ کے باہر ایک بار نکالو\">c = price * rate\nfor i in range(1, n + 1):\n    print(c * i)</pre>",
      "golden": false,
      "checks": [
        {
          "q": "لوپ کے اندر وہ ضرب جو ہر چکر میں نہیں بدلتی، کہاں ہونی چاہیے؟",
          "options": [
            "ہر چکر میں دوبارہ",
            "لوپ سے باہر ایک بار",
            "صرف تبصرے میں",
            "صرف گراف میں"
          ],
          "answer": 1,
          "why": "مستقل کام ایک بار کر کے متغیر میں رکھو۔"
        },
        {
          "q": "Bubble sort کی اصلاح کیا کرتی ہے؟",
          "options": [
            "پہلے سے آخری جگہ بیٹھی قدر کو اگلے پاس میں چھوڑ دیتی ہے",
            "ہر قدر کو random کر دیتی ہے",
            "فائل مٹا دیتی ہے",
            "صرف رنگ بدلتی ہے"
          ],
          "answer": 0,
          "why": "چھوٹا اندرونی لوپ بے کار موازنہ ہٹا دیتا ہے۔"
        }
      ]
    },
    {
      "id": "c2-linear",
      "chapter": 2,
      "title": "Array، list، stack، queue",
      "minutes": 11,
      "diagram": "stack",
      "caption": "Stack میں اوپر سے push اور pop ہوتے ہیں۔ آخری اندر، پہلی باہر۔",
      "html": "<p class=\"callout gold\">Data structure، stack، اور queue سنہری تعریفیں ہیں۔</p>\n        <p>Data structure ڈیٹا کو یوں سنبھالنے کا طریقہ ہے کہ پڑھنا، بدلنا، اور عمل تیز ہوں۔ الماری میں کتابوں کی ترتیب اسی خیال کی انسانی مثال ہے۔</p>\n        <p><b>Linear</b> میں عنصر قطار میں ہوتے ہیں۔ سرے کے علاوہ ہر ایک کا ایک پہلے والا اور ایک بعد والا ہوتا ہے۔ <b>Non-linear</b> میں شاخیں یا جال ہوتا ہے۔</p>\n        <h2>Array</h2>\n        <p>ایک جیسی قسم کے خانے ملے ہوئے memory میں۔ نمبر سے سیدھا خانہ کھلتا ہے، اس لیے پہلا یا کوئی معلوم index اکثر O(1) ہے۔ بیچ میں ڈالنا مہنگا ہو سکتا ہے کیونکہ پڑوسی کھسکتے ہیں۔</p>\n        <h2>Linked list</h2>\n        <p>ہر node میں قدر اور اگلے پتے کا نشان ہوتا ہے۔ خانے ملی ہوئی قطار میں ہونا ضروری نہیں۔ شروع میں ڈالنا سستا ہے۔ نمبر سے سیدھا چھلانگ نہیں؛ nویں node تک چلنا پڑتا ہے۔</p>\n        <h2>Stack</h2>\n        <p><span class=\"en\">LIFO</span>: جو آخر میں چڑھا، پہلے اترے گا۔ اوپر رکھنا <span class=\"en\">push</span>، اوپر سے ہٹانا <span class=\"en\">pop</span>۔ مثال: واپس جانے کا بٹن، یا قوسین کی جانچ۔</p>\n        <h2>Queue</h2>\n        <p><span class=\"en\">FIFO</span>: جو پہلے آیا پہلے کام ہو۔ پچھلے سرے پر <span class=\"en\">enqueue</span>، اگلے سرے سے <span class=\"en\">dequeue</span>۔ مثال: پرنٹر کی لائن، یا ٹکٹ کی کھڑکی۔</p>\n        <p>مشترک عمل: داخل کرنا، مٹانا، ڈھونڈنا، اور ترتیب دیکھنا۔ عمل کا نام ڈھانچے کے ساتھ بدل جاتا ہے، خیال نہیں۔</p>",
      "golden": true,
      "checks": [
        {
          "q": "Stack کا اصول کیا ہے؟",
          "options": [
            "FIFO",
            "LIFO",
            "random",
            "صرف tree"
          ],
          "answer": 1,
          "why": "آخری رکھی چیز پہلے نکلتی ہے۔"
        },
        {
          "q": "پرنٹر پر پہلے بھیجی فائل پہلے چھپے، یہ کیا ہے؟",
          "options": [
            "Queue",
            "صرف graph cycle",
            "Set union",
            "NaN"
          ],
          "answer": 0,
          "why": "یہ FIFO قطار ہے۔"
        }
      ]
    },
    {
      "id": "c2-tree",
      "chapter": 2,
      "title": "Tree، graph، اور retrieval",
      "minutes": 10,
      "diagram": "tree",
      "caption": "Tree کی جڑ سے شاخیں نکلتی ہیں۔ ہر بچے کا ایک والدین ہوتا ہے۔",
      "html": "<h2>Tree</h2>\n        <p>جڑ <span class=\"en\">root</span> سے درجہ بند شاخیں۔ والدین سے بچوں کی طرف ایک سے زیادہ رشتہ ہو سکتا ہے، مگر اوپر ایک ہی راستہ ہوتا ہے۔ کالج کا چارٹ: پرنسپل جڑ، نیچے شعبے، پھر استاد۔</p>\n        <h2>Graph</h2>\n        <p><span class=\"en\">Node</span> اور <span class=\"en\">edge</span>۔ سخت درجہ نہیں؛ کوئی بھی کسی سے جڑ سکتا ہے۔ شہر کے راستے، یا دوستوں کا جال۔ Tree دراصل ایک خاص graph ہے جس میں چکر نہیں اور جڑ ایک ہے۔</p>\n        <div class=\"compare\">\n          <div class=\"col\"><h3>لکیری منظر</h3><p>حاضری کی فہرست: array۔ واپسی کا تاریخچہ: stack۔ کینٹین کی لائن: queue۔</p></div>\n          <div class=\"col\"><h3>غیر لکیری منظر</h3><p>خاندانی یا دفتری درجہ: tree۔ بس روٹس جہاں راستے مڑ کر ملیں: graph۔</p></div>\n        </div>\n        <h2>پڑھنے کا راستہ</h2>\n        <ul>\n          <li><b>Array:</b> index سے سیدھا خانہ۔</li>\n          <li><b>Linked list:</b> سر سے نشان پکڑ پکڑ کر آگے۔</li>\n          <li><b>Queue:</b> صرف اگلا شخص نکلتا ہے؛ بیچ والا اپنی باری سے پہلے نہیں نکلتا۔</li>\n        </ul>\n        <div class=\"callout do\"><b>خود کرو:</b> تین مقامی مثالیں لکھو، ہر ایک کے ساتھ ڈھانچے کا نام اور ایک جملے میں وجہ۔</div>",
      "golden": false,
      "checks": [
        {
          "q": "پرنسپل سے شعبہ جات کا چارٹ کس ڈھانچے جیسا ہے؟",
          "options": [
            "Tree",
            "صرف queue",
            "صرف set",
            "CSV"
          ],
          "answer": 0,
          "why": "ایک جڑ اور درجہ بند بچے tree ہیں۔"
        },
        {
          "q": "Linked list میں دسواں node کیسے ملتا ہے؟",
          "options": [
            "ہمیشہ ایک چھلانگ میں",
            "سر سے اشاروں پر چل کر",
            "صرف hash بغیر پڑھے",
            "صرف pie chart"
          ],
          "answer": 1,
          "why": "فہرست میں نمبر سے براہِ راست خانہ نہیں کھلتا۔"
        }
      ]
    },
    {
      "id": "c3-list",
      "chapter": 3,
      "title": "List: ترتیب، کٹائی، اور طریقے",
      "minutes": 10,
      "diagram": "array",
      "caption": "List کے خانے نمبر سے کھلتے ہیں، صفر سے۔",
      "html": "<p>Python میں <span class=\"en\">list</span> ترتیب شدہ اور <span class=\"en\">mutable</span> ہے: بدل سکتی ہے، دہرایا عنصر رکھ سکتی ہے، اور ملا جلا ڈیٹا بھی۔ قوسین مربع ہوتے ہیں۔</p>\n        <p>کٹائی نئی فہرست دیتی ہے، اصلی کو نہیں کاٹتی۔ رکنے والا index شامل نہیں ہوتا۔</p>\n        <pre class=\"code\" data-speak=\"فہرست کی کٹائی: دو سے چھ کے پہلے تک، اور الٹی فہرست\">nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\nprint(nums[2:6])   # [2, 3, 4, 5]\nprint(nums[:4])    # شروع سے\nprint(nums[6:])    # آخر تک\nprint(nums[::2])   # ایک چھوڑ کر\nprint(nums[::-1])  # الٹی</pre>\n        <p>چکر <span class=\"en\">for num in nums</span> سے سب سے صاف ہے۔ index چاہیے تو <span class=\"en\">while</span> اور لمبائی۔</p>\n        <ul>\n          <li><span class=\"en\">append</span> آخر میں جوڑتا ہے۔ <span class=\"en\">insert</span> مقرر جگہ پر۔</li>\n          <li><span class=\"en\">remove</span> پہلی ملتی قدر ہٹاتا ہے؛ نہ ملے تو <span class=\"en\">ValueError</span>۔</li>\n          <li><span class=\"en\">count</span>، <span class=\"en\">index</span>، <span class=\"en\">sort</span>، <span class=\"en\">reverse</span>، <span class=\"en\">clear</span>۔</li>\n        </ul>\n        <p>فائدہ: ایک نام میں ہزار قدریں، اضافہ اور کمی، ملا جلا مواد۔</p>\n        <div class=\"callout do\"><b>خود کرو:</b> فہرست میں نمبر ڈھونڈو۔ جھنڈا <span class=\"en\">found</span> رکھو۔ ملے تو <span class=\"en\">break</span>، تاکہ باقی ہزار خانے بے کار نہ چلیں۔</div>",
      "golden": false,
      "checks": [
        {
          "q": "nums[2:6] میں index 6 کی قدر شامل ہے؟",
          "options": [
            "ہاں",
            "نہیں، رکنا exclusive ہے",
            "صرف اگر sort ہو",
            "صرف tuple میں"
          ],
          "answer": 1,
          "why": "کٹائی رکنے والے index کو چھوڑ دیتی ہے۔"
        },
        {
          "q": "remove وہ قدر نہ ہٹائے جو فہرست میں نہیں، تو کیا ہوتا ہے؟",
          "options": [
            "خاموشی",
            "ValueError",
            "نئی فائل",
            "NaN ہمیشہ"
          ],
          "answer": 1,
          "why": "remove سخت ہے؛ نہ ملنے پر exception۔"
        }
      ]
    },
    {
      "id": "c3-tuple-set",
      "chapter": 3,
      "title": "Tuple اور set",
      "minutes": 10,
      "diagram": "sets",
      "caption": "دو دائرے: مشترک حصہ intersection، دونوں ملا کر union۔",
      "html": "<p class=\"callout gold\">Tuple کی immutability سنہری فرق ہے۔</p>\n        <p><span class=\"en\">Tuple</span> ترتیب شدہ ہے مگر بند: گول قوسین، دہراؤ جائز، index اور کٹائی list جیسی۔ خانہ بدلنا <span class=\"en\">TypeError</span> ہے۔ اگر اندر list ہو تو اس list کا مواد بدل سکتا ہے، tuple کا ڈھانچہ نہیں۔ طریقے صرف <span class=\"en\">count</span> اور <span class=\"en\">index</span>۔ فائدہ: محفوظ ریکارڈ، جیسے نقطہ کے محدد، اور تھوڑی تیز پڑھائی۔</p>\n        <h2>Set</h2>\n        <p>گھنگریالے قوسین، بے ترتیب، ہر قدر ایک بار۔ <span class=\"en\">myset[0]</span> نہیں چلتا۔ خود دہراؤ مٹا دیتا ہے۔ عناصر بدلنے کے قابل نہیں ہونے چاہییں، مگر set میں <span class=\"en\">add</span> اور ہٹانا ہو سکتا ہے۔</p>\n        <ul>\n          <li><span class=\"en\">add</span> ایک قدر۔ <span class=\"en\">update</span> کئی۔</li>\n          <li><span class=\"en\">remove</span> نہ ملے تو <span class=\"en\">KeyError</span>۔ <span class=\"en\">discard</span> نہ ملے تو چپ۔ امتحان میں discard کو محفوظ کہو۔</li>\n        </ul>\n        <p>ریاضی والے عمل، A اور B پر:</p>\n        <div class=\"math\" data-speak=\"یونین، انٹرسیکشن، ڈفرنس، اور سمٹرک ڈفرنس\">\\[A \\cup B,\\quad A \\cap B,\\quad A \\setminus B,\\quad A \\triangle B\\]</div>\n        <p>Python میں یہ <span class=\"en\">|</span>، <span class=\"en\">&amp;</span>، <span class=\"en\">-</span>، اور <span class=\"en\">^</span> ہیں۔ چکر <span class=\"en\">for</span> سے ہے؛ ترتیب کی قسم نہیں۔ حروف کی ترتیب چاہیے تو <span class=\"en\">sorted</span>۔</p>",
      "golden": true,
      "checks": [
        {
          "q": "tuple کے خانے کو نئی قدر دینا کیا دیتا ہے؟",
          "options": [
            "ہمیشہ کامیابی",
            "TypeError",
            "نئی database",
            "صرف warning بغیر رکے"
          ],
          "answer": 1,
          "why": "Tuple item assignment نہیں مانتا۔"
        },
        {
          "q": "Set میں غائب قدر ہٹانے کا محفوظ طریقہ؟",
          "options": [
            "remove",
            "discard",
            "append",
            "push"
          ],
          "answer": 1,
          "why": "discard نہ ملنے پر پروگرام نہیں توڑتا۔"
        }
      ]
    },
    {
      "id": "c3-dict",
      "chapter": 3,
      "title": "Dictionary اور built-in functions",
      "minutes": 9,
      "diagram": "frame",
      "caption": "Dictionary بھی قطاروں جیسا جدول ہے: کلید اور قدر۔",
      "html": "<p class=\"callout gold\">Dictionary سنہری ڈھانچہ ہے: کلید سے قدر۔</p>\n        <p>اصل لغت کی طرح لفظ ڈھونڈو، معنی ملے۔ جوڑا <span class=\"en\">key: value</span>۔ Python 3.7 کے بعد ڈالنے کی ترتیب رہتی ہے۔ بدلنے کے قابل ہے۔ ایک کلید دوبارہ آئے تو پچھلی قدر مٹ کر نئی رہتی ہے۔ کلیدیں یکتا ہوتی ہیں۔</p>\n        <pre class=\"code\" data-speak=\"ڈکشنری میں نام اور نمبر، پھر نئی کلید\">student = {\"name\": \"Ayesha\", \"roll\": 12}\nstudent[\"city\"] = \"Hyderabad\"\nstudent[\"roll\"] = 15\nprint(student[\"name\"])</pre>\n        <p>چابیوں پر چکر <span class=\"en\">for key in student</span>۔ قدر سمیت <span class=\"en\">items</span>۔ غائب چابی پر سیدھا index <span class=\"en\">KeyError</span> دے سکتا ہے؛ <span class=\"en\">get</span> نرم ہے۔</p>\n        <h2>مشترک فنکشن</h2>\n        <p><span class=\"en\">len</span> تعداد، <span class=\"en\">min</span> اور <span class=\"en\">max</span> کنارے، <span class=\"en\">sum</span> جمع۔ یہ list پر بھی چلتے ہیں۔ خالی فہرست پر min بے معنی ہے، اس لیے پہلے لمبائی دیکھو۔</p>\n        <div class=\"callout do\"><b>دو مشقیں:</b> حاضری کا پروگرام نام سے حاضر یا غیر حاضر رکھے۔ دوسرا، جملے کے الفاظ گننے کے لیے dictionary میں شمار بڑھاؤ۔</div>",
      "golden": true,
      "checks": [
        {
          "q": "ایک کلید دو بار لکھی جائے تو کیا رہتا ہے؟",
          "options": [
            "دونوں قدریں",
            "آخری قدر",
            "پہلی قدر ہمیشہ",
            "set بن جاتا ہے"
          ],
          "answer": 1,
          "why": "دہرائی کلید پر نئی قدر پرانی کو بدل دیتی ہے۔"
        },
        {
          "q": "len خالی list پر کیا دیتا ہے؟",
          "options": [
            "None ہمیشہ",
            "0",
            "error لازماً",
            "NaN"
          ],
          "answer": 1,
          "why": "تعداد صفر ہے۔ min خالی پر الگ مسئلہ ہے۔"
        }
      ]
    },
    {
      "id": "c3-func",
      "chapter": 3,
      "title": "Functions، return، اور scope",
      "minutes": 9,
      "diagram": "func",
      "caption": "فنکشن کے بائیں input، بیچ میں کام، دائیں return۔",
      "html": "<p>فنکشن نام رکھا ہوا کام ہے۔ <span class=\"en\">Built-in</span> زبان کے ساتھ آتے ہیں، جیسے <span class=\"en\">print</span>۔ <span class=\"en\">User-defined</span> تم <span class=\"en\">def</span> سے بناتے ہو۔</p>\n        <p>جو فنکشن <span class=\"en\">return</span> کرے وہ قدر واپس دیتا ہے، تاکہ آگے حساب بنے، نہ کہ صرف اسکرین پر چھپے۔ واپسی کے بعد فنکشن رک جاتا ہے۔</p>\n        <pre class=\"code\" data-speak=\"جمع اور تقسیم کے دو فنکشن۔ تقسیم سے پہلے صفر دیکھو۔\">def add(a, b):\n    return a + b\n\ndef divide(a, b):\n    if b == 0:\n        return None\n    return a / b</pre>\n        <p>ایک چھوٹا calculator چار عملوں کو چار فنکشن میں رکھے، اور مینو صرف ان کو بلائے۔ یہی modularity ہے۔</p>\n        <h2>Scope</h2>\n        <div class=\"compare\">\n          <div class=\"col\"><h3>Local</h3><p>فنکشن کے اندر بنا نام باہر نہیں دکھتا۔ کام ختم، نام ختم۔</p></div>\n          <div class=\"col\"><h3>Global</h3><p>فنکشن کے باہر بنا نام اندر پڑھا جا سکتا ہے۔ اندر سے بدلنا ہو تو جان بوجھ کر <span class=\"en\">global</span> لکھنا پڑتا ہے۔ بغیر اس کے اندر نیا local نام بن جاتا ہے۔</p></div>\n        </div>\n        <p>امتحان میں یہ لکھو: global کم استعمال کرو، کیونکہ چھپا رشتہ خرابی چھپاتا ہے۔ قدر argument سے دو اور return سے واپس لو۔</p>",
      "golden": false,
      "checks": [
        {
          "q": "return کے بعد فنکشن کی اگلی لائن چلتی ہے؟",
          "options": [
            "ہمیشہ",
            "نہیں، فنکشن وہیں سے واپس ہوتا ہے",
            "صرف tuple میں",
            "صرف graph میں"
          ],
          "answer": 1,
          "why": "return قدر دے کر فنکشن ختم کرتا ہے۔"
        },
        {
          "q": "فنکشن کے اندر بنا متغیر باہر عام طور پر؟",
          "options": [
            "global ہو جاتا ہے",
            "local رہتا ہے",
            "database میں لکھ جاتا ہے",
            "set بنتا ہے"
          ],
          "answer": 1,
          "why": "بغیر global کے اندر کا نام باہر نہیں جاتا۔"
        }
      ]
    },
    {
      "id": "c3-file",
      "chapter": 3,
      "title": "فائل، with، اور exception",
      "minutes": 10,
      "diagram": "file",
      "caption": "تین موڈ: پڑھنا، لکھ کر پرانا مٹانا، اور آخر میں جوڑنا۔",
      "html": "<p>فائل کھولنے کے عام موڈ: <span class=\"en\">r</span> پڑھنا، <span class=\"en\">w</span> لکھنا اور پرانا مواد مٹانا، <span class=\"en\">a</span> آخر میں جوڑنا۔ فائل نہ ہو تو r ناکام ہوتا ہے؛ w نئی بنا سکتا ہے۔</p>\n        <p><span class=\"en\">with</span> کام کے بعد فائل خود بند کرتا ہے، چاہے بیچ میں خرابی آئے۔ اسے context manager کہتے ہیں۔</p>\n        <pre class=\"code\" data-speak=\"ودھ کے ساتھ نمبر لکھنا، پھر پڑھنا\">with open(\"marks.txt\", \"w\", encoding=\"utf-8\") as f:\n    f.write(\"Ayesha 78\\n\")\nwith open(\"marks.txt\", \"r\", encoding=\"utf-8\") as f:\n    text = f.read()</pre>\n        <h2>Errors اور exceptions</h2>\n        <p>نحو کی غلطی چلنے سے پہلے رکتی ہے۔ <span class=\"en\">Exception</span> چلتے وقت آتی ہے: صفر سے تقسیم، غلط <span class=\"en\">int</span>، یا غائب فائل۔ <span class=\"en\">try</span> خطرے والا حصہ، <span class=\"en\">except</span> سنبھالنے والا۔ خاموش خالی except ہر خرابی نگل جاتا ہے؛ نام لے کر پکڑو۔</p>\n        <div class=\"callout do\"><b>Grade tracker:</b> نام اور نمبر فائل میں جوڑو۔ پڑھ کر اوسط نکالو۔ خراب لائن کو چھوڑ کر پیغام دو، پورا پروگرام نہ گراؤ۔ یہی چھوٹا منصوبہ باب کا عملی خلاصہ ہے۔</div>",
      "golden": false,
      "checks": [
        {
          "q": "موڈ w موجود فائل کے پرانے مواد کے ساتھ کیا کرتا ہے؟",
          "options": [
            "ہمیشہ آخر میں جوڑتا ہے",
            "لکھنے سے پہلے مواد ہٹا دیتا ہے",
            "صرف پڑھتا ہے",
            "فائل کو tuple بنا دیتا ہے"
          ],
          "answer": 1,
          "why": "w لکھائی سے پہلے فائل کو خالی کر دیتا ہے۔ a جوڑتا ہے۔"
        },
        {
          "q": "with کا خاص فائدہ کیا ہے؟",
          "options": [
            "فائل خود بند ہوتی ہے",
            "Big O ہمیشہ 1 ہو جاتا ہے",
            "انٹرنیٹ لازمی ہے",
            "GUI بن جاتا ہے"
          ],
          "answer": 0,
          "why": "Context manager وسیلہ واپس کرتا ہے حتیٰ کہ خرابی پر بھی۔"
        }
      ]
    },
    {
      "id": "c4-data",
      "chapter": 4,
      "title": "تجزیہ اور database connection",
      "minutes": 8,
      "diagram": "db",
      "caption": "Python سے کنکشن، پھر SQLite کے ڈبے تک راستہ۔",
      "html": "<p><span class=\"en\">Data analysis</span> جمع شدہ اعداد سے سوال کا جواب نکالتا ہے: کیا ہوا، کتنا، اور آگے کیا ممکن ہے۔ بغیر جوڑے ہوئے ڈیٹا صرف ڈھیر ہے۔</p>\n        <p>ذرائع: کلاس کی CSV، فارم، اسکول کا database، یا ہاتھ کا مشاہدہ۔ رابطہ اس لیے چاہیے کہ پروگرام محفوظ طریقے سے وہی قطاریں پڑھے جو سوال سے متعلق ہوں۔</p>\n        <h2>کنکشن کے حصے</h2>\n        <ul>\n          <li>ڈیٹا کہاں رہتا ہے: فائل یا <span class=\"en\">SQLite</span> فائل۔</li>\n          <li>رابطہ: <span class=\"en\">connect</span>۔</li>\n          <li>حکم لے جانے والا <span class=\"en\">cursor</span>۔</li>\n          <li>حکم: جدول بنانا، قطار ڈالنا، چننا۔</li>\n          <li>کام محفوظ کرنا: <span class=\"en\">commit</span>، پھر بند کرنا۔</li>\n        </ul>\n        <p>کنکشن کے بغیر تجزیہ یا تو پرانی نقل پر ہوتا ہے یا ہر بار ہاتھ سے نقل پر۔ چھوٹی کلاس کے لیے ایک فائل والا SQLite کافی ہے؛ علیحدہ سرور ضروری نہیں۔</p>",
      "golden": false,
      "checks": [
        {
          "q": "Cursor کس کام آتا ہے؟",
          "options": [
            "صرف تصویر رنگنے",
            "database کو حکم لے جانے",
            "صرف TTS",
            "صرف wireframe"
          ],
          "answer": 1,
          "why": "Cursor کے ذریعے SQL حکم چلتا ہے۔"
        },
        {
          "q": "تبدیلی database میں رکے، اس کے لیے عموماً کیا چاہیے؟",
          "options": [
            "commit",
            "صرف print",
            "pop",
            "median"
          ],
          "answer": 0,
          "why": "commit لکھائی کو مستقل کرتا ہے۔"
        }
      ]
    },
    {
      "id": "c4-sqlite",
      "chapter": 4,
      "title": "SQLite کو Python سے بنانا",
      "minutes": 9,
      "diagram": "db",
      "caption": "ایک فائل میں جدول؛ cursor حکم لے جاتا ہے۔",
      "html": "<p>SQLite پوری database ایک فائل میں رکھتا ہے۔ کلاس پروجیکٹ کے لیے یہ مناسب آغاز ہے۔</p>\n        <pre class=\"code\" data-speak=\"ایس کیو لائٹ میں طلبہ کا جدول، ایک قطار، پھر پڑھنا\">import sqlite3\ncon = sqlite3.connect(\"class.db\")\ncur = con.cursor()\ncur.execute(\"CREATE TABLE IF NOT EXISTS students (name TEXT, marks INTEGER)\")\ncur.execute(\"INSERT INTO students VALUES (?, ?)\", (\"Ayesha\", 78))\ncon.commit()\nfor row in cur.execute(\"SELECT name, marks FROM students\"):\n    print(row)\ncon.close()</pre>\n        <p>قدم یاد رکھو: ماڈیول، کنکشن، cursor، جدول، داخلہ، commit، انتخاب، بند۔ سوالیہ نشان قدر کو حکم سے الگ رکھتا ہے تاکہ متن غلط حکم نہ بن جائے۔</p>\n        <p><span class=\"en\">IF NOT EXISTS</span> دوسری بار چلانے پر جدول کو دوبارہ بنانے کی خرابی سے بچاتا ہے۔</p>",
      "golden": false,
      "checks": [
        {
          "q": "sqlite3.connect کیا واپس کرتا ہے؟",
          "options": [
            "صرف integer",
            "database کنکشن",
            "صرف PNG",
            "stack"
          ],
          "answer": 1,
          "why": "اسی کنکشن سے cursor اور commit ہوتے ہیں۔"
        },
        {
          "q": "INSERT کے بعد قطاریں مستقل رہیں، اس کے لیے؟",
          "options": [
            "commit",
            "SELECT صرف",
            "min()",
            "caption"
          ],
          "answer": 0,
          "why": "بغیر commit کے بند کرنے پر لکھائی رہ بھی سکتی ہے نہیں بھی؛ عادت commit کی بناؤ۔"
        }
      ]
    },
    {
      "id": "c4-pandas",
      "chapter": 4,
      "title": "Pandas، DataFrame، اور NaN",
      "minutes": 9,
      "diagram": "frame",
      "caption": "ایک قطار میں نام، نمبر، شہر۔ دوسری قطار میں NaN خالی نمبر ہے۔",
      "html": "<p><span class=\"en\">Pandas</span> جدول کو <span class=\"en\">DataFrame</span> کہتا ہے: قطار میں ریکارڈ، کالم میں خانہ۔ CSV یا Excel سے لوڈ ہوتا ہے۔</p>\n        <pre class=\"code\" data-speak=\"سی ایس وی پڑھنا، سر دیکھنا، خالی نمبر بھرنا\">import pandas as pd\ndf = pd.read_csv(\"marks.csv\")\nprint(df.head())\ndf[\"marks\"] = df[\"marks\"].fillna(df[\"marks\"].mean())\nclean = df.dropna()</pre>\n        <p><span class=\"en\">NaN</span> گمشدہ قدر ہے۔ دو ایماندار راستے: <span class=\"en\">dropna</span> وہ قطار ہٹا دے جہاں ضروری خانہ خالی ہو، یا <span class=\"en\">fillna</span> مناسب قدر سے بھرو، جیسے اسی کالم کی اوسط۔ امتحان میں یہ لکھو کہ اندھا صفر بھرنا معنی بدل سکتا ہے؛ سبب لکھو۔</p>\n        <p>ترتیب دینا، کالم چننا، اور گروہ کی گنتی وہی تنظیم ہے جو بعد میں گراف کو سچ بولنے دیتی ہے۔ گندا جدول خوبصورت چارٹ میں بھی جھوٹ بولتا ہے۔</p>",
      "golden": false,
      "checks": [
        {
          "q": "DataFrame میں قطار کس کی نمائندگی کرتی ہے؟",
          "options": [
            "ایک ریکارڈ",
            "صرف فونٹ",
            "صرف edge",
            "صرف OTP"
          ],
          "answer": 0,
          "why": "قطار ایک مشاہدہ ہے، کالم ایک خانہ۔"
        },
        {
          "q": "NaN کا مطلب؟",
          "options": [
            "گمشدہ قدر",
            "ہمیشہ صفر",
            "ہمیشہ سب سے بڑا نمبر",
            "فائل کا موڈ"
          ],
          "answer": 0,
          "why": "NaN خالی یا نامعلوم عدد کا نشان ہے۔"
        }
      ]
    },
    {
      "id": "c4-stats",
      "chapter": 4,
      "title": "چارٹ اور descriptive statistics",
      "minutes": 11,
      "diagram": "charts",
      "caption": "بار اونچائی سے مقدار، لکیر وقت سے، پائی حصہ دکھاتی ہے۔",
      "html": "<p>گراف وہ شکل ہے جو جدول سے تیز بات کرے۔ قسم کام کے مطابق چنو۔</p>\n        <ul>\n          <li><b>Bar / column:</b> زمروں کا موازنہ، جیسے شہروں کے نمبر۔</li>\n          <li><b>Line:</b> وقت کے ساتھ بدلنا، جیسے ہفتوں کی حاضری۔</li>\n          <li><b>Pie:</b> پورے کے حصے۔ زیادہ ٹکڑے الجھا دیتے ہیں۔</li>\n          <li><b>Histogram:</b> عدد کے وقفوں میں گنتی، جیسے نمبروں کے گروہ۔</li>\n          <li><b>Scatter:</b> دو عدد کا رشتہ، جیسے گھنٹے پڑھائی اور نمبر۔</li>\n          <li><b>Box:</b> درمیان، پھیلاؤ، اور اچھلے۔</li>\n        </ul>\n        <h2>مرکز</h2>\n        <div class=\"math\" data-speak=\"اوسط، مجموعہ تقسیم تعداد\">\\[\\bar{x} = \\frac{\\sum x}{n}\\]</div>\n        <p>اوسط سب کو جمع کر کے تعداد پر تقسیم۔ درمیانہ ترتیب کے بعد بیچ کی قدر؛ جفت تعداد ہو تو بیچ کی دو قدروں کی اوسط۔ منوال وہ قدر جو سب سے زیادہ بار آئے۔</p>\n        <h2>پھیلاؤ</h2>\n        <div class=\"math\" data-speak=\"رینج، بڑی منہا چھوٹی۔ ویریئنس، فرق کے مربع کی اوسط\">\\[\\mathrm{Range} = \\max - \\min\\]</div>\n        <div class=\"math\" data-speak=\"سگما اسکوائر، ایکس منہا ایکس بار کے مربع کا مجموعہ، تقسیم این\">\\[\\sigma^{2} = \\frac{\\sum (x-\\bar{x})^{2}}{n}\\]</div>\n        <p>معیاری انحراف variance کا جذر ہے۔ یہی یونٹ اصل عدد والا ہوتا ہے۔ بورڈ کی مشق میں اکثر تقسیم n سے ہوتی ہے؛ اگر سوال n−1 کہے تو وہی مانو۔</p>\n        <p>مثال: 2، 4، 6۔ اوسط 4۔ فرق −2، 0، 2۔ مربع 4، 0، 4۔ جمع 8۔ n = 3 تو variance 8/3۔ Range = 4۔</p>",
      "golden": true,
      "checks": [
        {
          "q": "2، 4، 6 کی اوسط کیا ہے؟",
          "options": [
            "4",
            "6",
            "12",
            "2"
          ],
          "answer": 0,
          "why": "بارہ تقسیم تین = چار۔"
        },
        {
          "q": "وقت کے ساتھ حاضری دکھانے کے لیے بہتر چارٹ؟",
          "options": [
            "Line",
            "صرف stack",
            "صرف CLI",
            "صرف tuple"
          ],
          "answer": 0,
          "why": "لکیر تسلسل کو جوڑ کر دکھاتی ہے۔"
        }
      ]
    },
    {
      "id": "c5-ml",
      "chapter": 5,
      "title": "مشین لرننگ، neural network، deep learning",
      "minutes": 11,
      "diagram": "neuron",
      "caption": "اعداد وزن سے گزر کر جمع ہوتے ہیں، پھر activation فنکشن سے نکلتے ہیں۔",
      "html": "<p>یہ تینوں <span class=\"en\">AI</span> کے اندر ہیں۔ مشین اعداد سے سیکھتی ہے، ہر کیس کے لیے الگ ہاتھ کا حکم نہیں لکھنا پڑتا۔</p>\n        <div class=\"compare\">\n          <div class=\"col\"><h3>Machine learning</h3><p>نمونوں سے قاعدہ سیکھ کر نئی مثال پر رائے۔ جیسے پرانی مارکس سے یہ اندازہ کہ کون سی عادت نمبر سے جڑی ہے۔</p></div>\n          <div class=\"col\"><h3>Neural network</h3><p>دماغی خیال سے بنا حسابی جال۔ <span class=\"en\">neuron</span> یا node قدر لے کر آگے بھیجتا ہے۔</p></div>\n          <div class=\"col\"><h3>Deep learning</h3><p>کئی hidden تہیں۔ “گہرا” اس لیے کہ ڈیٹا کئی تہوں سے گزرتا ہے۔ تصویر اور آواز جیسے پیچیدہ نمونوں میں یہی کام آتا ہے۔</p></div>\n        </div>\n        <p>ایک neuron کی اندرونی بات:</p>\n        <div class=\"math\" data-speak=\"زیڈ برابر وزن ضرب ان پٹ کا مجموعہ، جمع بائس\">\\[z = \\sum_{i} w_i x_i + b\\]</div>\n        <div class=\"math\" data-speak=\"سگما زیڈ، ایک تقسیم، ایک جمع ای کی طاقت منفی زیڈ\">\\[\\sigma(z) = \\frac{1}{1+e^{-z}}\\]</div>\n        <p><span class=\"en\">Weight</span> رشتے کی طاقت ہے۔ <span class=\"en\">Bias</span> اضافی مستقل ہے تاکہ نتیجہ کھسک سکے۔ <span class=\"en\">Activation</span> فیصلہ نرم یا تیز کرتا ہے۔</p>\n        <p>چہرہ کھولنے کی کہانی: کیمرہ input ہے۔ درمیانی تہہ آنکھوں کا فاصلہ اور ناک کی شکل دیکھتی ہے۔ output تالا کھولتا ہے یا نہیں۔</p>\n        <p>Deep learning کو بڑا ڈیٹا، کئی تہیں، اور مشق کے چکر چاہییں۔ پاکستان کی AI پالیسی انہی مہارتوں کو تعلیم اور صحت میں دیکھتی ہے؛ طالب علم کے لیے مطلب یہ ہے کہ تصور صاف ہو اور اعداد کی ذمہ داری بھی۔</p>",
      "golden": true,
      "checks": [
        {
          "q": "Deep میں گہرائی کس بات کی ہے؟",
          "options": [
            "کئی hidden تہیں",
            "صرف بڑا فونٹ",
            "صرف ایک IF",
            "صرف queue"
          ],
          "answer": 0,
          "why": "ڈیٹا کئی تہوں سے سیکھتا ہے۔"
        },
        {
          "q": "Weight کیا بتاتا ہے؟",
          "options": [
            "کنکشن کی طاقت",
            "فائل کا موڈ",
            "صرف شہر کا نام",
            "صرف pie کا رنگ"
          ],
          "answer": 0,
          "why": "بڑا وزن اس input کو زیادہ اثر دیتا ہے۔"
        }
      ]
    },
    {
      "id": "c5-uses",
      "chapter": 5,
      "title": "Neural network کہاں کام آتا ہے",
      "minutes": 7,
      "diagram": "layers",
      "caption": "تہیں: input، چھپی تہیں، پھر output۔",
      "html": "<p>بہت سے نظام پسِ پردہ یہی جال چلاتے ہیں۔</p>\n        <ul>\n          <li><b>تصویر:</b> چہرہ، نمبر پلیٹ، یا فصل کے پتے کی بیماری کی پہچان۔</li>\n          <li><b>زبان:</b> ترجمہ، املا، اور مددگار جواب۔</li>\n          <li><b>آواز:</b> بول کو متن میں بدلنا۔</li>\n          <li><b>صحت:</b> ایکس رے یا اسکین میں نشان، تاکہ ڈاکٹر جلد دیکھے۔ فیصلہ آخر میں ماہر انسان کا رہتا ہے۔</li>\n          <li><b>روزمرہ:</b> سپام چھانٹنا، راستے کی تجویز، دکان کی مانگ کا اندازہ۔</li>\n        </ul>\n        <p>جواب میں ہمیشہ یہ لکھو: input کیا ہے، چھپی تہہ کون سا نمونہ دیکھتی ہے، output کیا فیصلہ ہے۔ بغیر اس کہانی کے صرف “AI استعمال ہوتا ہے” ادھورا ہے۔</p>\n        <div class=\"callout\">حدود بھی بتاؤ: خراب یا یک طرفہ ڈیٹا غلط رائے دیتا ہے۔ کلاس میں یہ ethical نکتہ الگ سے پوچھا جا سکتا ہے۔</div>",
      "golden": false,
      "checks": [
        {
          "q": "اسکین میں نشان دیکھنا کس میدان کی مثال ہے؟",
          "options": [
            "صحت",
            "صرف stack",
            "صرف entrepreneurship کا beachhead",
            "صرف CSV موڈ"
          ],
          "answer": 0,
          "why": "طبی تصویر deep learning کا مشہور استعمال ہے۔"
        },
        {
          "q": "خراب ڈیٹا سے ماڈل؟",
          "options": [
            "بھی غلط نمونہ سیکھ سکتا ہے",
            "ہمیشہ کامل ہو جاتا ہے",
            "فائل موڈ a بن جاتا ہے",
            "Big O مٹا دیتا ہے"
          ],
          "answer": 0,
          "why": "سیکھنا اسی مواد جیسا ہوتا ہے جو ملا۔"
        }
      ]
    },
    {
      "id": "c5-secure",
      "chapter": 5,
      "title": "محفوظ تعاون اور data protection",
      "minutes": 9,
      "diagram": "shield",
      "caption": "حفاظت کی تہہ: پہچان، اجازت، خفیہ کاری، اور نقل۔",
      "html": "<p class=\"callout gold\">Secure collaboration سنہری موضوع ہے۔ اشتراک تب مفید ہے جب ڈیٹا محفوظ رہے۔</p>\n        <ul>\n          <li><b><span class=\"en\">Authentication</span>:</b> اندر آنے سے پہلے پہچان: پاس ورڈ، PIN، OTP، یا انگلی کا نشان۔ بینک کا ایک بار کا کوڈ اسی لیے آتا ہے۔</li>\n          <li><b><span class=\"en\">Access control</span>:</b> پہچان کے بعد اختیار: دیکھنا، لکھنا، یا صرف تبصرہ۔ استاد دستاویز طلبہ کو view دے اور گروہ کے سربراہ کو edit۔</li>\n          <li><b>حساب:</b> کون کھولا، کون بدلا، یہ ریکارڈ رہے۔ LMS میں یہی سراغ ہوتا ہے۔</li>\n        </ul>\n        <h2>Data protection</h2>\n        <p>بے اجازت پڑھنے، چوری، گم ہونے، اور اتفاقی مٹنے سے بچاؤ۔</p>\n        <ul>\n          <li><b><span class=\"en\">Encryption</span>:</b> بغیر چابی کے متن بے معنی۔</li>\n          <li>لمبا الگ پاس ورڈ، اور اسے بانٹنا نہیں۔</li>\n          <li>نقل، <span class=\"en\">backup</span>، دوسری جگہ۔</li>\n          <li><span class=\"en\">Firewall</span> ناپسندیدہ آمد کو روکتا ہے۔</li>\n          <li>اجازت کے بغیر فائل عام لنک پر نہیں۔</li>\n        </ul>",
      "golden": true,
      "checks": [
        {
          "q": "OTP کس قدم کی مثال ہے؟",
          "options": [
            "Authentication",
            "صرف pie chart",
            "صرف pop",
            "NaN بھرنا"
          ],
          "answer": 0,
          "why": "ایک بار کا کوڈ پہچان کی تصدیق ہے۔"
        },
        {
          "q": "View اور edit کا فرق کس اصول میں ہے؟",
          "options": [
            "Access control",
            "Mean",
            "Wireframe fidelity",
            "Queue فقط"
          ],
          "answer": 0,
          "why": "پہچان کے بعد یہ طے ہوتا ہے کہ کسے کیا کرنے دیا ہے۔"
        }
      ]
    },
    {
      "id": "c5-threats",
      "chapter": 5,
      "title": "خطرات، بچاؤ، اور equity",
      "minutes": 10,
      "diagram": "equity",
      "caption": "Equal access ایک جیسا موقع؛ equity وہ اضافی سہارا جس سے نتیجہ برابر ہو۔",
      "html": "<p class=\"callout gold\">خطرات اور equity دونوں سنہری ہیں۔ نام، اثر، اور بچاؤ لکھو۔ حملے کا طریقہ نہ لکھو اور نہ آزماؤ۔</p>\n        <ul>\n          <li><b><span class=\"en\">Malware</span>:</b> نقصان یا چوری کے لیے بنا سافٹ ویئر۔ نام: virus، worm، spyware، ransomware، Trojan۔ اثر: فائل خراب، یا ڈیٹا یرغمال۔</li>\n          <li><b><span class=\"en\">Phishing</span>:</b> جعلی پیغام جو پاس ورڈ یا کوڈ مانگے۔ اثر: شناخت کی چوری۔</li>\n          <li><b>بے اجازت داخلہ:</b> کمزور یا بانٹا پاس ورڈ، یا کھلا چھوڑا آلہ۔</li>\n          <li><b>ڈیٹا یا شناخت کی چوری:</b> نام، شناختی نمبر، یا بینک کی تفصیل سے کسی اور کے بھیس میں کام۔</li>\n          <li><b><span class=\"en\">DoS</span>:</b> خدمت کو اتنے بوجھ سے بھرنا کہ اصلی لوگ استعمال نہ کر سکیں۔ اثر: کلاس یا بینک کی سائٹ بند۔</li>\n        </ul>\n        <h2>نشان اور بچاؤ</h2>\n        <p>اچانک سست آلہ، انجان لاگ اِن، یا عجیب لنک۔ بچاؤ: تازہ antivirus، firewall، اپڈیٹ، backup، الگ پاس ورڈ، اور ناواقف لنک نہ کھولنا۔ مشکوک پیغام استاد یا بینک کے اصل راستے سے جانچو، پیغام والے نمبر پر نہیں۔</p>\n        <h2>Equity اور equal access</h2>\n        <div class=\"compare\">\n          <div class=\"col\"><h3>Equal access</h3><p>سب کو ایک جیسا دروازہ۔ مثال: ہر طالب علم کو ایک ہی Zoom لاگ اِن۔</p></div>\n          <div class=\"col\"><h3>Equity</h3><p>جسے اضافی سہارا چاہیے اسے دو، تاکہ نتیجہ برابر ہو۔ مثال: سننے میں دقت ہو تو live captions۔</p></div>\n        </div>\n        <p>آلات: مشترکہ دستاویز، کلاس کا LMS، ویڈیو کال، اور فارم۔ انصاف یہ ہے کہ زبان، معذوری، اور سست نیٹ والے طالب علم کے لیے راستہ بھی سوچا جائے۔</p>",
      "golden": true,
      "checks": [
        {
          "q": "جعلی پیغام سے پاس ورڈ مانگنا کیا کہلاتا ہے؟",
          "options": [
            "Phishing",
            "Median",
            "Prototype",
            "Append"
          ],
          "answer": 0,
          "why": "دھوکے سے راز لے جانا phishing ہے۔"
        },
        {
          "q": "سب کو ایک جیسا لاگ اِن، مگر بہرے طالب علم کو caption، یہ دوسرا حصہ کیا ہے؟",
          "options": [
            "Equity",
            "صرف malware",
            "صرف stack",
            "صرف mode w"
          ],
          "answer": 0,
          "why": "Equity اضافی سہارے سے برابر نتیجہ چاہتی ہے۔"
        }
      ]
    },
    {
      "id": "c6-idea",
      "chapter": 6,
      "title": "کاروبار، ڈیجیٹل دور، اور خیال",
      "minutes": 9,
      "diagram": "cycle",
      "caption": "خیال ایک چکر ہے: دیکھنا، بنانا، آزمانا، سدھارنا۔",
      "html": "<p><span class=\"en\">Entrepreneur</span> مسئلہ دیکھتا ہے، حل سوچتا ہے، اور اسے چیز یا خدمت بنانے کی کوشش کرتا ہے۔ شروع میں بڑا دفتر ضروری نہیں۔ <span class=\"en\">Entrepreneurship</span> اسی کوشش کا عمل ہے۔</p>\n        <p class=\"callout gold\">ڈیجیٹل دور میں یہ کام فون، سوشل پیج، فارم، نقشہ، ویڈیو، اور ادائیگی کے چھوٹے آلے سے شروع ہو سکتا ہے۔</p>\n        <p>پورا app ہمیشہ پہلا قدم نہیں۔ WhatsApp فہرست، ایک صفحہ، یا Google Form بھی خیال کو آزما دیتے ہیں۔ اگر لوگ نہ چاہیں تو پیسہ زیادہ بہانے سے پہلے رخ بدل جاتا ہے۔</p>\n        <p>سندھ کے قریب مثالیں: ہاتھ کے کارت کا صفحہ، اجرک کی دکان کا پیغام والا کیٹلاگ، یا کالج کے دروازے پر پانی کی بوتل کا پہلے سے آرڈر۔ مسئلہ روزمرہ کا ہو۔</p>\n        <h2>مسئلے سے خیال</h2>\n        <ol>\n          <li>دیکھو: گھر، کالج، بازار میں کون سی تکلیف بار بار ہے۔</li>\n          <li>لکھو: کسے تکلیف ہے، کب، اور اب وہ کیا کرتا ہے۔</li>\n          <li>خیال: سب سے چھوٹا مددگار قدم کیا ہو سکتا ہے۔</li>\n          <li>پوچھو: کیا لوگ اس کے لیے وقت یا پیسہ دیں گے۔</li>\n        </ol>",
      "golden": true,
      "checks": [
        {
          "q": "ڈیجیٹل entrepreneurship کے لیے پہلا قدم ہمیشہ مکمل app ہے؟",
          "options": [
            "ہاں",
            "نہیں، چھوٹا ڈیجیٹل آلہ بھی خیال آزماتا ہے",
            "صرف tree بنانا",
            "صرف variance"
          ],
          "answer": 1,
          "why": "فارم یا پیغام والا کیٹلاگ بھی آغاز ہے۔"
        },
        {
          "q": "اچھا خیال عموماً کہاں سے شروع ہوتا ہے؟",
          "options": [
            "دیکھے ہوئے مسئلے سے",
            "صرف خوبصورت لوگو سے",
            "صرف بڑے قرض سے",
            "صرف random نام سے"
          ],
          "answer": 0,
          "why": "مسئلہ پہلے، مصنوعات بعد میں۔"
        }
      ]
    },
    {
      "id": "c6-proto",
      "chapter": 6,
      "title": "Prototype اور اس کا چکر",
      "minutes": 9,
      "diagram": "cycle",
      "caption": "Design، Build، Test، پھر Iterate۔ تیر اگلے قدم کو دکھاتے ہیں۔",
      "html": "<p class=\"callout gold\">Prototype سنہری تعریف ہے۔ یہ آخری مصنوعات نہیں۔ یہ ابتدائی نمونہ ہے تاکہ خیال دکھے اور رائے ملے۔</p>\n        <p>فائدہ: جلدی غلطی، سستا سبق، اور یہ کہ لوگ بٹن ڈھونڈ سکیں یا نہیں۔ شکل کاغذ، گتا، سلائیڈ، Canva، Figma، یا خدمت کا چارٹ ہو سکتی ہے۔</p>\n        <h2>وفاداری</h2>\n        <ul>\n          <li><b>Low-fidelity:</b> کھردرا خاکہ۔ کلاس کے زیادہ تر منصوبے یہیں سے شروع ہوں۔</li>\n          <li><b>Mid-fidelity:</b> زیادہ صاف اسکرین، مگر ابھی اصلی نظام نہیں۔</li>\n          <li><b>High-fidelity:</b> لگ بھگ اصلی رنگ اور دبنے والے راستے۔</li>\n        </ul>\n        <p>غلطي یہ ہے کہ ضرورت جانے بغیر پورا app لکھ دیا جائے۔</p>\n        <h2>چکر</h2>\n        <p><span class=\"en\">Iteration</span> یعنی وہی نمونہ بار بار بہتر ہو۔ Design میں یہ طے کرو کہ نمونہ کیا دکھائے۔ Build میں دکھائی دو، خوبصورتی بعد میں۔ Test میں خاموش دیکھو کہ آدمی کہاں رکے۔ Iterate میں بے کار ہٹاؤ اور کمی پورو کرو۔</p>\n        <div class=\"callout do\"><b>کلاس سرگرمی:</b> ہوم ورک کی تاریخ بھولنے کا مددگار۔ کاغذ کی تین اسکرینیں: آج کا کام، تاریخ، یاددہانی۔ پانچ ساتھیوں کو دو۔ مبصر چپ رہے۔ جہاں انگلی رکی، وہاں خاکہ سدھارو۔</div>",
      "golden": true,
      "checks": [
        {
          "q": "Prototype آخری مصنوعات ہوتا ہے؟",
          "options": [
            "ہمیشہ",
            "نہیں، یہ آزمائشی نمونہ ہے",
            "صرف جب encryption ہو",
            "صرف queue میں"
          ],
          "answer": 1,
          "why": "نمونہ رائے کے لیے ہے، رہائی کے لیے نہیں۔"
        },
        {
          "q": "Iteration کا مطلب؟",
          "options": [
            "ایک بار بنا کر چھوڑ دینا",
            "رائے سے دوبارہ سدھارنا",
            "صرف اوسط",
            "صرف pop"
          ],
          "answer": 1,
          "why": "ڈیزائن، تعمیر، ٹیسٹ، پھر پھر سے۔"
        }
      ]
    },
    {
      "id": "c6-mvp",
      "chapter": 6,
      "title": "MVP اور سب سے خطرناک قیاس",
      "minutes": 9,
      "diagram": "mvp",
      "caption": "Prototype دکھاتا ہے؛ MVP سب سے چھوٹا کام کرنے والا نسخہ ہے۔",
      "html": "<p class=\"callout gold\">MVP سنہری فرق ہے۔</p>\n        <p><span class=\"en\">Minimum</span>: صرف لازمی حصے۔ <span class=\"en\">Viable</span>: اتنا چلے کہ اصل مسئلہ کم ہو۔ یہ خاکہ نہیں، اور آخری دکان بھی نہیں۔</p>\n        <div class=\"compare\">\n          <div class=\"col\"><h3>Prototype</h3><p>خیال کی شکل اور راستہ آزماتا ہے۔ لوگ دیکھ کر بتاتے ہیں کہ سمجھ آیا یا نہیں۔</p></div>\n          <div class=\"col\"><h3>MVP</h3><p>اصل استعمال آزماتا ہے۔ سوال: کیا لوگ واقعی یہ کریں گے؟</p></div>\n        </div>\n        <p>کینٹین کی مکمل app میں لاگ اِن، ادائیگی، اور ٹریکنگ ہو سکتے ہیں۔ MVP ایک فارم ہو سکتا ہے: بریک سے پہلے ناشتہ چن لو۔ اگر کوئی فارم نہ بھرے تو app لکھنا فضول تھا۔</p>\n        <h2>Riskiest assumption</h2>\n        <p>قیاس وہ بات ہے جسے ہم سچ مانتے ہیں مگر ابھی جانچا نہیں۔ سب سے خطرناک قیاس وہ ہے جس کے جھوٹ ہونے پر سارا خیال گر جائے۔ مثال: “طلبہ بریک سے پہلے آرڈر کرنا چاہتے ہیں”۔ یہی پہلا ٹیسٹ ہونا چاہیے، رنگ کا لوگو نہیں۔</p>\n        <p>MVP بناتے وقت فہرست کاٹو۔ اضافی فیچر بعد میں۔ سب ایک ساتھ بنانا سیکھنے کو مہنگا کر دیتا ہے۔</p>",
      "golden": true,
      "checks": [
        {
          "q": "کینٹین کے لیے گوگل فارم کس چیز کے قریب ہے؟",
          "options": [
            "MVP",
            "صرف final branded app",
            "صرف variance",
            "malware"
          ],
          "answer": 0,
          "why": "یہ سب سے چھوٹا کام کا نسخہ ہے جو اصل مانگ جانچے۔"
        },
        {
          "q": "Riskiest assumption کیا ہے؟",
          "options": [
            "وہ قیاس جس کے گرنے سے خیال گر جائے",
            "سب سے خوبصورت رنگ",
            "فائل کا موڈ",
            "اوسط"
          ],
          "answer": 0,
          "why": "پہلے اسی قیاس کو آزماؤ۔"
        }
      ]
    },
    {
      "id": "c6-beach",
      "chapter": 6,
      "title": "Beachhead، منصوبہ، اور ethics",
      "minutes": 8,
      "diagram": "beach",
      "caption": "سب سے چھوٹا دائرہ پہلے صارف ہیں۔ بڑا دائرہ “سب لوگ” ابھی نہیں۔",
      "html": "<p>MVP کی جانچ میں اصلی لوگ استعمال کریں۔ گنتی بھی لکھو اور جملہ بھی: کتنے فارم بھرے، کہاں رکے، کیا شکایت کی۔</p>\n        <p class=\"callout gold\"><span class=\"en\">Beachhead market</span> پہلا چھوٹا گروہ ہے جسے ضرورت فوری ہو اور تم تک پہنچ سکو۔</p>\n        <ul>\n          <li>تنگ تعریف۔</li>\n          <li>تمہاری پہنچ میں۔</li>\n          <li>تکلیف ابھی کی ہو۔</li>\n        </ul>\n        <p>“پاکستان کے سب طالب علم” کمزور پہلا بازار ہے۔ “ایک کالج کے بارہویں جماعت کے بورڈ والے طالب علم” بہتر beachhead ہے۔</p>\n        <h2>مکمل منصوبہ</h2>\n        <p>گروہ ایک مقامی خیال لے: مسئلہ، beachhead، کاغذی prototype، ایک قیاس، چھوٹا MVP، پانچ صارف، پھر سدھار۔ معیار: مسئلہ واضح ہو، نمونہ دکھائی دے، ٹیسٹ لکھا ہو، اور دعویٰ ثبوت سے بڑا نہ ہو۔</p>\n        <div class=\"callout\"><b>Ethics:</b> لوگوں کا نام اور نمبر اجازت کے بغیر نہ بیچو۔ جعلی جائزے نہ لکھواؤ۔ جو کام نہیں کرتا اسے “تیار دکان” مت کہو۔ کلاس کا ڈیٹا منصوبے کے بعد مٹا دو اگر اس کی ضرورت نہ رہے۔</div>",
      "golden": true,
      "checks": [
        {
          "q": "Beachhead market کیا ہے؟",
          "options": [
            "پہلا تنگ گروہِ صارف",
            "پورا ملک ایک ساتھ",
            "صرف logo",
            "صرف standard deviation"
          ],
          "answer": 0,
          "why": "پہلے چھوٹے، پہنچ میں، اور ضرورت والے گروہ پر توجہ۔"
        },
        {
          "q": "منصوبے میں دوسروں کا ڈیٹا؟",
          "options": [
            "اجازت اور حد کے ساتھ",
            "ہمیشہ عام لنک پر",
            "بے نام بیچ دو",
            "malware میں رکھو"
          ],
          "answer": 0,
          "why": "اخلاق کا مطلب اجازت، سچ، اور حد ہے۔"
        }
      ]
    }
  ]
};
