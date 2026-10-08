# -*- coding: utf-8 -*-
"""Original Urdish Teach Yourself lectures for Sindh CS XII chapters 1–6."""

def L(i, chapter, title, minutes, diagram, caption, html, checks, golden=False):
    return {
        "id": i,
        "chapter": chapter,
        "title": title,
        "minutes": minutes,
        "diagram": diagram,
        "caption": caption,
        "html": html.strip(),
        "golden": golden,
        "checks": [
            {"q": q, "options": opts, "answer": ans, "why": why}
            for q, opts, ans, why in checks
        ],
    }


CHAPTERS = [
    {"id": 1, "title": "کمپیوٹر سسٹم اور HCI", "en": "Computer Systems — HCI", "blurb": "انسان کے مطابق interface، رسائی، UI اور test"},
    {"id": 2, "title": "سوچ اور الگورتھم", "en": "Computational Thinking & Algorithms", "blurb": "trace، Big O، stack، queue، tree"},
    {"id": 3, "title": "Python کی بنیاد", "en": "Programming Fundamentals", "blurb": "list، set، function، file، exception"},
    {"id": 4, "title": "ڈیٹا اور تجزیہ", "en": "Data and Analysis", "blurb": "SQLite، Pandas، چارٹ، اوسط"},
    {"id": 5, "title": "کمپیوٹنگ کے اثرات", "en": "Applications and Impacts", "blurb": "neural network، حفاظت، equity"},
    {"id": 6, "title": "ڈیجیٹل کاروبار", "en": "Entrepreneurship in the Digital Age", "blurb": "prototype، MVP، beachhead"},
]


LECTURES = [
    L(
        "c1-hci", 1, "HCI اور حسی راستے", 8, "channels",
        "انسان اور کمپیوٹر پانچ حسی راستوں سے بات کرتے ہیں۔",
        r"""
        <p>یہ لیکچر تم خود پڑھنے کے لیے ہے۔ استاد کے دوہری نوٹ کی نقل نہیں۔ جملے اردو میں ہیں، اور امتحان کی اصطلاحیں English میں۔</p>
        <h2><span class="en">HCI</span> کیا ہے؟</h2>
        <p><span class="en">Human-Computer Interaction</span>، مختصر <span class="en">HCI</span>، وہ ڈیزائن ہے جس میں technology انسان کی خدمت کرے: استعمال آسان ہو، کام تیز ہو، اور نظام انسان کی ضرورت کا جواب دے۔</p>
        <p>یہی خیال دو اور ناموں سے بھی پوچھا جاتا ہے: <span class="en">CHI</span> یعنی <span class="en">Computer-Human Interface</span>، اور <span class="en">MMI</span> یعنی <span class="en">Man-Machine Interaction</span>۔</p>
        <h2>حسی راستے</h2>
        <ul>
          <li><b>بصارت، <span class="en">sight</span>:</b> تم اسکرین، گراف یا ویڈیو دیکھتے ہو۔ کمپیوٹر monitor پر تصویر دکھاتا ہے۔</li>
          <li><b>چھونا، <span class="en">touch</span>:</b> تم tap، type یا swipe کرتے ہو۔ مشین click یا vibration دیتی ہے۔ اس لمس والے جواب کو <span class="en">haptics</span> کہتے ہیں۔</li>
          <li><b>سننا، <span class="en">hearing</span>:</b> تم آواز سنتے ہو۔ speaker سے audio feedback آتا ہے۔</li>
          <li><b>آواز، <span class="en">voice</span>:</b> تم بول کر حکم دیتے ہو، جیسے کوئی نام پکارنا۔ نظام speech سمجھ کر جواب دیتا ہے۔</li>
          <li><b>مکانی، <span class="en">spatial</span>:</b> تم جسم یا جگہ میں حرکت کرتے ہو۔ <span class="en">VR</span> جیسا نظام position track کرتا ہے۔</li>
        </ul>
        <div class="callout gold"><b>امتحانی جملہ:</b> HCI کا مرکز انسان ہے، مشین نہیں۔ اچھا نظام انسان کی حسوں کے ذریعے بات کرتا ہے۔</div>
        """,
        [
            ("HCI کا دوسرا نام کیا ہو سکتا ہے؟", ["صرف HTML", "CHI یا MMI", "صرف CPU", "صرف URL"], 1, "CHI اور MMI اسی انسان–مشین تعلق کے پرانے نام ہیں۔"),
            ("Phone کی vibration کس حس کا جواب ہے؟", ["sight", "touch / haptics", "spatial map", "CLI"], 1, "چھونے کے عمل پر جسمانی جواب haptics کہلاتا ہے۔"),
        ],
    ),
    L(
        "c1-trad", 1, "Traditional اور Natural interaction", 8, "trad",
        "بائیں جانب mouse اور keyboard، دائیں جانب voice اور gesture۔",
        r"""
        <h2><span class="en">Traditional interaction</span></h2>
        <p>یہ روزمرہ آلات کا پرانا، واضح طریقہ ہے۔ انسان standard input دیتا ہے اور output لیتا ہے۔</p>
        <div class="compare">
          <div class="col"><h3>Computer</h3><p>Mouse ہلانا اور keyboard پر لکھنا۔ Output monitor اور speakers سے آتا ہے۔</p></div>
          <div class="col"><h3>Smartphone</h3><p>Touchscreen پر tap اور swipe۔ Output روشنی اور vibration ہے۔</p></div>
        </div>
        <p>TV کا remote اور ATM کا keypad بھی traditional مثالیں ہیں۔ انسان کو بٹن کا قاعدہ پہلے سے پتا ہوتا ہے۔</p>
        <h2><span class="en">Natural interaction</span></h2>
        <p>یہ وہ طریقہ ہے جس میں mouse یا keyboard لازمی نہیں۔ نظام انسان کی اپنی حرکت اور بولی کے قریب ہوتا ہے۔</p>
        <ul>
          <li><b><span class="en">Voice</span>:</b> آلہ سے بولنا، مثلاً گانا چلانے کا حکم۔</li>
          <li><b><span class="en">Body &amp; gesture</span>:</b> چہرے سے فون کھولنا، یا ہاتھ ہلا کر VR کھیلنا۔</li>
        </ul>
        <div class="callout do"><b>خود کرو:</b> آج کے تین traditional interface اور تین natural interface اپنی کاپی میں لکھو۔ FaceID، voice assistant، اور Kinect طرز کے کھیل natural طرف آتے ہیں۔</div>
        """,
        [
            ("Keyboard اور mouse کس قسم کی interaction ہیں؟", ["Natural", "Traditional", "صرف haptic", "صرف biometric"], 1, "معیاری input/output والے روزمرہ طریقے traditional کہلاتے ہیں۔"),
            ("بغیر mouse کے بول کر حکم دینا کیا ہے؟", ["CLI صرف", "Natural voice interaction", "Form fill", "Low-fidelity wireframe"], 1, "بولی سے براہِ راست حکم natural interaction کی مثال ہے۔"),
        ],
    ),
    L(
        "c1-apps", 1, "زندگی کے میدانوں میں HCI", 9, "domains",
        "صحت، بینک، تعلیم، اور رابطہ: چار میدان جہاں HCI کام آتی ہے۔",
        r"""
        <p class="callout gold">یہ golden topic ہے۔ Paper میں مثال سمیت میدان پوچھے جاتے ہیں۔</p>
        <p><span class="en">HCI</span> صرف تعریف نہیں۔ اس سے desktop app، website، اور mobile app ایسے بنتے ہیں جو انسان کی ضرورت کے گرد ہوں۔</p>
        <div class="compare">
          <div class="col"><h3>صحت</h3><p>Patient portal، telemedicine، اور assistive technology۔ فائدہ: علاج تک دور سے رسائی۔</p></div>
          <div class="col"><h3>بینکاری</h3><p>Mobile banking اور محفوظ ATM۔ فائدہ: تیز لین دین اور رقم کا نظم۔</p></div>
          <div class="col"><h3>تعلیم</h3><p><span class="en">LMS</span> اور online exam۔ فائدہ: پڑھائی اور مشق میں شمولیت۔</p></div>
          <div class="col"><h3>رابطہ</h3><p>Messaging اور video call۔ فائدہ: دور بیٹھے لوگ ایک کام میں شریک ہو سکتے ہیں۔</p></div>
        </div>
        <p>جواب لکھتے وقت تین حصے رکھو: میدان کا نام، ایک ٹھوس مثال، اور user کو فائدہ۔ صرف یہ مت لکھو کہ “app آسان ہے”۔</p>
        """,
        [
            ("Telemedicine کس میدان کی HCI مثال ہے؟", ["صرف gaming", "Health care", "Stack", "Beachhead"], 1, "مریض کا دور سے معائنہ صحت کے میدان میں آتا ہے۔"),
            ("LMS کس کا فائدہ بڑھاتا ہے؟", ["صرف printer کی سیاہی", "تعلیم، سیکھنا، اور student کی شمولیت", "صرف hard disk", "صرف IP address"], 1, "LMS کلاس، مواد، اور امتحان کو ایک انسانی بہاؤ میں جوڑتا ہے۔"),
        ],
        golden=True,
    ),
    L(
        "c1-parts", 1, "اجزاء اور interaction کی اقسام", 10, "ui",
        "Interface کی شکلیں: GUI، CLI، touch، voice، اور natural۔",
        r"""
        <h2>HCI کے بنیادی اجزاء</h2>
        <ul>
          <li><b><span class="en">User</span>:</b> وہ فرد یا گروہ جو مقصد کے لیے نظام چلاتا ہے۔ <span class="en">End user</span> خود چلاتا ہے۔ <span class="en">Stakeholder</span> نتیجے میں دلچسپی رکھتا ہے، جیسے manager یا client۔</li>
          <li><b><span class="en">Computer system</span>:</b> وہ پلیٹ فارم جہاں input، output، اور feedback ایک interface سے جڑتے ہیں۔</li>
          <li><b><span class="en">User interaction</span>:</b> click، tap، type، یا بولنے سے ارادہ نظام کے جواب میں بدلتا ہے۔</li>
          <li><b><span class="en">Task</span>:</b> مخصوص کام، جیسے ٹکٹ بک کرنا۔ اس کی complexity، درکار مہارت، اور وقت الگ الگ ہوتے ہیں۔ فارم بھرنا ہلکا task ہے؛ 3D model بھاری۔</li>
        </ul>
        <h2>Interaction کی اقسام</h2>
        <ul>
          <li><b><span class="en">Manipulation</span>:</b> فائل گھسیٹنا، انگلی سے zoom۔</li>
          <li><b><span class="en">Command-based</span>:</b> متن کا حکم، جیسے terminal۔</li>
          <li><b><span class="en">Menu-driven</span>:</b> تیار فہرست سے انتخاب۔</li>
          <li><b><span class="en">Form fill</span>:</b> خانوں میں منظم ڈیٹا۔</li>
          <li><b><span class="en">Conversational</span>:</b> chatbot یا voice assistant سے قدرتی زبان۔</li>
          <li><b><span class="en">Gesture</span>، <span class="en">voice</span>، <span class="en">biometric</span>:</b> ہاتھ، بولی، یا انگلی کا نشان۔</li>
          <li><b><span class="en">Context-aware</span>:</b> نظام کمرے میں داخلے پر خود بتی جلا دے۔</li>
          <li><b><span class="en">Haptic</span>:</b> عمل کی تصدیق کے لیے vibration۔</li>
          <li><b><span class="en">Multimodal</span>:</b> دو یا زیادہ طریقے اکٹھے، جیسے بول کر ڈھونڈنا پھر انگلی سے چننا۔</li>
        </ul>
        """,
        [
            ("Manager جو نظام خود نہ چلائے مگر نتیجہ چاہے، کیا کہلائے گا؟", ["صرف icon", "Stakeholder", "Haptic pixel", "Wireframe"], 1, "Stakeholder نتیجے میں شریک ہوتا ہے؛ end user براہِ راست چلاتا ہے۔"),
            ("Terminal میں متن لکھ کر حکم دینا کون سی قسم ہے؟", ["Command-based", "Pie chart", "Beachhead", "Median"], 0, "ٹائپ کیا ہوا دقیق حکم command-based interaction ہے۔"),
        ],
    ),
    L(
        "c1-feedback", 1, "Interface، ماحول، اور feedback", 8, "ui",
        "پانچ طرح کے interface ایک ہی کام کو مختلف احساس دیتے ہیں۔",
        r"""
        <h2><span class="en">User interface</span></h2>
        <p>UI وہ وسیلہ ہے جس سے انسان نظام کو چھوتا ہے۔</p>
        <ul>
          <li><b><span class="en">GUI</span>:</b> windows، icons، menus۔ مثال: desktop OS۔</li>
          <li><b><span class="en">CLI</span>:</b> صرف متن۔ مثال: Linux terminal۔</li>
          <li><b><span class="en">Touch</span>:</b> tap، swipe، pinch۔</li>
          <li><b><span class="en">VUI</span>:</b> بولی سے حکم، جیسے smart speaker۔</li>
          <li><b><span class="en">NUI</span>:</b> جسم کی حرکت یا VR جیسا ماحول۔</li>
        </ul>
        <h2>ماحول</h2>
        <p><span class="en">Environment</span> وہ اصلی جگہ ہے جہاں نظام چلتا ہے۔ دھوپ میں ATM، خاموش کلاس، اور کمزور network تین مختلف ماحول ہیں۔ ڈیزائن کو روشنی، شور، اور hardware دیکھ کر بدلنا پڑتا ہے۔</p>
        <h2>Feedback</h2>
        <div class="compare">
          <div class="col"><h3>System feedback</h3><p>مشین بتاتی ہے کہ ہوا کیا۔ “لوڈ ہو رہا ہے”، بھیجا گیا کا نشان، یا error۔</p></div>
          <div class="col"><h3>User feedback</h3><p>انسان نظام کو بتاتا ہے: Submit دبانا، یا پانچ میں سے ستارے دینا۔</p></div>
        </div>
        """,
        [
            ("Smart speaker پر بولنا کس interface کی مثال ہے؟", ["CLI", "VUI", "صرف histogram", "Tuple"], 1, "Voice User Interface بولی کو input بناتا ہے۔"),
            ("Loading کا نشان کس قسم کا feedback ہے؟", ["User feedback", "System feedback", "Beachhead", "Variance"], 1, "یہ مشین کی طرف سے تصدیق ہے کہ کام جاری ہے۔"),
        ],
    ),
    L(
        "c1-access", 1, "اہمیت، رسائی، اور need analysis", 10, "equity",
        "Equal access ایک جیسا دروازہ ہے؛ equity اضافی سہارا ہے۔ یہ خیال HCI میں بھی کام آتا ہے۔",
        r"""
        <p class="callout gold">Importance of HCI امتحان کا سنہری حصہ ہے۔</p>
        <p>اچھا HCI مشین کو قریب اور قابلِ استعمال بناتا ہے۔ Touchscreen نے پیچیدہ کمپیوٹر کو روزمرہ آلہ بنا دیا۔ کمزور ڈیزائن الجھن اور خطرہ پیدا کرتا ہے، جیسے طبی آلے پر دھندلے بٹن۔</p>
        <ul>
          <li><b>پیداوار:</b> کم غلطی، تیز مقصد۔</li>
          <li><b>شمولیت:</b> screen reader اور voice command ان لوگوں کو شامل کرتے ہیں جو بصارت یا ہاتھ کی حد سے رکے ہوں۔</li>
          <li><b>ایجاد:</b> AR، VR، AI، اور IoT تب اپنائے جاتے ہیں جب HCI صاف ہو۔</li>
          <li><b>معیشت:</b> آسان مصنوعات زیادہ بکتیں ہیں اور اعتماد رکھتی ہیں۔</li>
          <li><b>ذمہ داری:</b> privacy، کم bias، اور انسان کی بھلائی۔</li>
        </ul>
        <h2>Accessibility کے اصول</h2>
        <ul>
          <li><b>High contrast:</b> دھوپ میں بھی متن الگ دکھے۔</li>
          <li><b>پڑھنے کے قابل فونٹ:</b> سادہ رسم، مناسب سائز اور فاصلہ۔</li>
          <li><b>Colour-blind friendly:</b> صرف رنگ پر بھروسہ نہیں؛ نشان یا لفظ بھی ہو، جیسے سرخ دائرے کے ساتھ STOP۔</li>
          <li><b>Inclusive navigation:</b> mouse کے علاوہ Tab سے بٹن تک پہنچنا۔</li>
          <li><b>Multimodal:</b> ویڈیو کے ساتھ caption، یا خاموش الارم کے لیے vibration۔</li>
        </ul>
        <h2><span class="en">Need analysis</span></h2>
        <p>ڈیزائن سے پہلے یہ خلا دیکھو: اب کیا ہے، اور ہونا کیا چاہیے۔ ترتیب یہ ہے: user کون ہے، interview یا observation سے معلومات، ضرورتوں کا تجزیہ، ترجیح، پھر حل۔</p>
        <div class="callout do"><b>مثال:</b> بینک app سے پہلے گاہک بتاتے ہیں کہ fingerprint login چاہیے، بزرگوں کو بڑے بٹن چاہییں، اور مقامی زبان بھی۔ UI ان ثابت شدہ ضرورتوں کے گرد بنتا ہے۔</div>
        """,
        [
            ("صرف سرخ رنگ سے خطرہ دکھانا کس اصول کے خلاف ہے؟", ["Colour-blind friendly design", "Stack overflow", "FIFO", "Median"], 0, "رنگ کے ساتھ لفظ یا نشان بھی ہونا چاہیے۔"),
            ("Need analysis کب ہوتی ہے؟", ["صرف app چھپنے کے بعد", "UI ڈیزائن سے پہلے", "صرف hard disk فارمیٹ پر", "صرف امتحان کے دن"], 1, "ضرورت سمجھے بغیر اسکرین بنانا اندھا ڈیزائن ہے۔"),
        ],
        golden=True,
    ),
    L(
        "c1-problems", 1, "HCI کے مسائل اور بہتری", 9, "trad",
        "مسئلہ انسان کی حد سے ٹکراؤ ہے؛ بہتری usability اور feedback سے آتی ہے۔",
        r"""
        <p class="callout gold">Problems of HCI سنہری topic ہے۔ ہر مسئلے کے ساتھ ایک زندگی کی مثال لکھنا۔</p>
        <ul>
          <li><b><span class="en">Interface complexity</span>:</b> اتنے مینو کہ checkout ملے ہی نہیں۔</li>
          <li><b><span class="en">Poor feedback</span>:</b> Submit کے بعد سکرین جم جائے، نہ کامیابی نہ error۔</li>
          <li><b><span class="en">Inconsistency</span>:</b> ایک صفحے پر search کا ذرہ بین، دوسرے پر کوئی اور نشان۔</li>
          <li><b><span class="en">Accessibility gaps</span>:</b> ویڈیو سبق بغیر caption۔</li>
          <li><b><span class="en">Compatibility</span>:</b> laptop پر چلے، mobile browser پر ٹوٹ جائے۔</li>
          <li><b><span class="en">Contextual neglect</span>:</b> رات کو نقشے میں dark mode نہ ہو اور ڈرائیور کو روشنی اندھا کر دے۔</li>
          <li><b><span class="en">High cognitive load</span>:</b> ایک ساتھ تین SMS کوڈ یاد رکھنے کی شرط۔</li>
          <li><b><span class="en">Trust deficiency</span>:</b> ادائیگی مانگو مگر محفوظ کنکشن کا کوئی نشان نہ دو۔</li>
        </ul>
        <h2>بہتری کے طریقے</h2>
        <p>Navigation سادہ کرو۔ Accessibility بڑھاؤ۔ ایک جیسا Save بٹن رکھو۔ “ادائیگی ہو گئی” جیسا صاف feedback دو۔ اسکرین چھوٹی ہو تو layout ڈھل جائے۔ <span class="en">User-centered design</span> میں اصلی user کے مقصد سے شروع کرو اور چھوٹا pilot test لو۔ Touch اور voice کو اکٹھا کرنے دو۔ پھر feedback سے مسلسل سدھارتے رہو۔</p>
        """,
        [
            ("Submit کے بعد کوئی پیغام نہ آنا کون سا مسئلہ ہے؟", ["Poor feedback", "Beachhead", "Tuple immutability", "Mean"], 0, "نظام نے یہ نہیں بتایا کہ عمل ہوا یا ناکام۔"),
            ("User-centered design کس پر مرکوز ہے؟", ["صرف مشین کی رفتار", "اصلی user کے مقصد", "صرف فونٹ کا نام", "صرف IP"], 1, "UCD انسان کے کام سے ڈیزائن شروع کرتا ہے۔"),
        ],
        golden=True,
    ),
    L(
        "c1-design", 1, "UI، UX، wireframe، اور testing", 11, "wire",
        "بائیں خاکہ ساخت ہے، دائیں نمونہ رنگ اور بٹن کے ساتھ۔",
        r"""
        <p class="callout gold">UI بمقابلہ UX، اور testing کے طریقے، دونوں سنہری ہیں۔</p>
        <p><span class="en">UI design</span> نظر آنے والے حصوں کو یوں سجاتا ہے کہ کام آسان ہو: button، menu، icon، text field، checkbox، radio، slider۔</p>
        <p><span class="en">UX</span> پورا احساس ہے: رفتار، سہولت، اور اطمینان۔ کھانے کی app میں برگر کی تصویر UI ہے۔ یہ UX ہے کہ آرڈر جلدی لگے، ٹریکنگ سمجھ آئے، اور آدمی بیزار نہ ہو۔ یاد رکھو: UI وہ ہے جو نظر آئے؛ UX وہ ہے جو محسوس ہو۔</p>
        <h2>Wireframe اور prototype</h2>
        <div class="compare">
          <div class="col"><h3>Low-fidelity</h3><p>سیاہ سفید خاکہ۔ ڈبے اور لکیریں۔ شروع میں ساخت جانچنے کے لیے۔ رنگ ابھی موضوع نہیں۔</p></div>
          <div class="col"><h3>High-fidelity</h3><p>لگ بھگ اصلی اسکرین: فونٹ، رنگ، تصویر، دبنے والے بٹن۔ آخری جانچ کے لیے۔</p></div>
        </div>
        <p><span class="en">Figma</span> براؤزر میں UI اور prototype بنانے کا آلہ ہے۔ Frame سے موبائل اسکرین، shapes سے بٹن، text سے عنوان، پھر frame نقل کر کے اگلی اسکرین۔ Prototype ٹیب میں trigger، جیسے tap، اور action، جیسے اگلی اسکرین پر جانا، جوڑتے ہیں۔ کوڈ سے پہلے لوگ جعلی app چلا کر راستہ دیکھتے ہیں۔</p>
        <h2>Test اور evaluation</h2>
        <p><span class="en">Testing</span> پوچھتا ہے کہ چیز ٹوٹتی تو نہیں۔ <span class="en">Evaluation</span> پوچھتا ہے کہ انسان کی ضرورت پوری ہوتی ہے یا نہیں۔</p>
        <ul>
          <li><b><span class="en">SUS</span>:</b> دس سوالوں کا usability اسکور۔</li>
          <li><b><span class="en">NPS</span>:</b> “کیا دوست کو تجویز کرو گے؟” وفاداری کا ناپ۔</li>
          <li><b>Formative:</b> بناتے وقت سدھار۔ <b>Summative:</b> آخر میں کامیابی ناپنا۔</li>
          <li><b>Expert review:</b> ماہر heuristics سے جائزہ۔</li>
          <li><b>Usability testing:</b> اصلی user سے کام کراؤ اور اٹکاؤ دیکھو۔</li>
          <li><b>Task-based:</b> “کارٹ میں ڈالو” جیسا کام؛ وقت، کامیابی، غلطیاں لکھو۔</li>
          <li><b>Automated audit:</b> بوٹ ٹوٹی link، سست صفحہ، یا کم contrast ڈھونڈے۔</li>
          <li><b>A/B testing:</b> آدھے لوگ نسخہ A دیکھیں، آدھے B۔ جس پر زیادہ مکمل کام ہو وہ جیتے گا۔</li>
          <li><b>Compatibility:</b> مختلف browser، فون، اور OS۔</li>
          <li><b>Performance / load:</b> بیک وقت بہت سے user پر رفتار اور سرور۔</li>
          <li><b>Keyboard اور screen reader:</b> صرف Tab اور مددگار آواز سے راستہ۔</li>
        </ul>
        <div class="callout"><b>کام:</b> UX designer ضرورت جانتا ہے۔ UI designer شکل بناتا ہے۔ Interaction designer اسکرینوں کا بہاؤ۔ Usability researcher ٹیسٹ چلاتا ہے۔ Accessibility specialist شمولیت کا معیار دیکھتا ہے۔</div>
        """,
        [
            ("کھانے کی app میں خوبصورت بٹن UI ہے یا UX؟", ["صرف UX", "نظر آنے والا حصہ UI ہے", "نہ UI نہ UX", "صرف Big O"], 1, "شکل UI ہے؛ بے جھنجٹ مکمل تجربہ UX ہے۔"),
            ("دو ڈیزائن میں سے بہتر چننے کا ٹیسٹ کیا کہلاتا ہے؟", ["A/B testing", "Stack push", "Mode of a list", "Encryption key"], 0, "نسخہ A اور B ایک ہی کام پر مقابلے میں رکھے جاتے ہیں۔"),
        ],
        golden=True,
    ),
    L(
        "c2-trace", 2, "درستگی اور trace table", 10, "array",
        "Trace table ہر قدم پر متغیر کا خانہ دکھاتی ہے، جیسے array کے خانے۔",
        r"""
        <p>الگورتھم تب درست ہے جب ہر جائز input پر وہی output آئے جو مقصد ہو۔ دو مشہور طریقے ہیں: <span class="en">trace table</span> اور <span class="en">stepwise reasoning</span>۔</p>
        <p class="callout gold">Trace table سنہرا طریقہ ہے: کاغذ پر dry run۔</p>
        <p>اس سے تین کام ہوتے ہیں: خط بہ خط چلانا، منطقی غلطی پکڑنا، اور یہ دیکھنا کہ الگورتھم وعدہ پورا کرتا ہے۔ کالم ہوتے ہیں: لائن، متغیر، input/output، اور شرط۔</p>
        <h2>خود چلاؤ</h2>
        <p>کالج گیٹ پر حاضری کا فیصد 75 سے 100 کے درمیان ہو تو طالب علم شمار ہو۔</p>
        <div class="math" data-speak="حاضری پچھتر سے بڑی یا برابر، اور سو سے چھوٹی یا برابر">\[75 \le a \le 100\]</div>
        <pre class="code" data-speak="حاضری گننے کے نو قدم۔ کل صفر سے شروع، پھر ہر عدد پر شرط۔">Total = 0
marks = [80, 70, 90, 75, 60]
FOR each a in marks
  IF a &gt;= 75 AND a &lt;= 100 THEN
    Total = Total + 1
  END IF
END FOR
PRINT Total</pre>
        <table class="data">
          <tr><th>a</th><th>شرط</th><th>Total</th></tr>
          <tr><td>80</td><td>سچ</td><td>1</td></tr>
          <tr><td>70</td><td>جھوٹ</td><td>1</td></tr>
          <tr><td>90</td><td>سچ</td><td>2</td></tr>
          <tr><td>75</td><td>سچ</td><td>3</td></tr>
          <tr><td>60</td><td>جھوٹ</td><td>3</td></tr>
        </table>
        <p>آخری چھاپ 3 ہے۔ 70 اور 60 شرط کے باہر ہیں۔ 75 شامل ہے کیونکہ نشان برابر کو بھی مانتا ہے۔</p>
        """,
        [
            ("Trace table کس کام آتی ہے؟", ["صرف رنگ چننے", "متغیرات کا کاغذی dry run", "صرف فونٹ", "MVP بیچنا"], 1, "یہ الگورتھم کو ہاتھ سے چلا کر قدریں لکھتی ہے۔"),
            ("اوپر والی جدول میں Total آخر میں کتنا ہے؟", ["2", "3", "5", "0"], 1, "80، 90، اور 75 تین جائز قدریں ہیں۔"),
        ],
        golden=True,
    ),
    L(
        "c2-step", 2, "Stepwise reasoning اور موازنہ", 8, "func",
        "Stepwise reasoning پورے بلاک کی حالت دیکھتا ہے، ایک ایک خانہ نہیں۔",
        r"""
        <p><span class="en">Stepwise reasoning</span> الگورتھم کو منطقی ٹکڑوں میں توڑ کر ہر مرحلے کی state جانچتا ہے۔ اسے logic verification بھی کہتے ہیں۔ جدول کی ہر صف ضروری نہیں؛ سوچ یہ دیکھتی ہے کہ حالت درست رہتی ہے یا نہیں۔</p>
        <p>سوال یہ ہیں: شروع کی state جائز ہے؟ ہر کیس سنبھلتا ہے؟ شرطیں صحیح ہیں؟ اگر لوپ ایک چکر کے شروع پر درست ہے تو چکر کے آخر پر بھی درست رہتا ہے؟</p>
        <h2>1 سے N تک جمع</h2>
        <div class="math" data-speak="ایک سے این تک جمع، این ضرب این جمع ایک، تقسیم دو">\[\sum_{i=1}^{N} i = \frac{N(N+1)}{2}\]</div>
        <p>شروع میں Sum = 0، یہ جائز ہے۔ لوپ ٹھیک 1 سے N تک چلتا ہے۔ ہر عدد جمع میں شامل ہوتا ہے۔ N = 0 پر لوپ نہیں چلتا، Sum صفر رہتا ہے۔ N = 5 پر Sum پندرہ ہوتا ہے۔ دونوں کنارے درست ہیں۔</p>
        <div class="compare">
          <div class="col"><h3>Trace table</h3><p>چھوٹے بلاک، الجھے لوپ، اور ابتدائی سیکھنے والے کے لیے۔ محنت زیادہ۔ ایک ایک قدر پکڑتی ہے۔</p></div>
          <div class="col"><h3>Stepwise</h3><p>بڑے نظام اور خیال کی درستگی کے لیے۔ محنت درمیانی۔ ساخت کی خرابی پکڑتی ہے۔</p></div>
        </div>
        """,
        [
            ("N = 5 پر 1 سے N کی جمع کتنی ہے؟", ["10", "15", "25", "5"], 1, "فارمولا 5 ضرب 6 تقسیم 2 = 15 دیتا ہے۔"),
            ("ہزار چکر والے لوپ کی ہر قدر لکھنا کس کے لیے بھاری ہے؟", ["Trace table", "صرف icon", "Caption", "Equity"], 0, "Trace table بڑے لوپ پر تھکا دینے والی ہو جاتی ہے۔"),
        ],
        golden=True,
    ),
    L(
        "c2-clear", 2, "وضاحت: modularity اور readability", 8, "func",
        "فنکشن input لیتا ہے، ایک کام کرتا ہے، اور return نکالتا ہے۔",
        r"""
        <p>Clarity کا مطلب ہے کہ دوسرا شخص بغیر چلائے منطق پڑھ لے۔ اکثر رفتار سے پہلے وضاحت ضروری ہے، کیونکہ صاف الگورتھم سدھرتا اور بڑھتا ہے۔ دو ستون ہیں: <span class="en">modularity</span> اور <span class="en">readability</span>۔</p>
        <h2>Modularity</h2>
        <ul>
          <li><b><span class="en">Single responsibility</span>:</b> ایک ماڈیول ایک کام۔ جمع اور چھپائی الگ ہوں۔</li>
          <li><b>Loose coupling:</b> ایک حصہ بدلے تو باقی نہ ٹوٹے۔</li>
          <li><b>Abstraction:</b> sort بلانے والے کو یہ جاننے کی ضرورت نہیں کہ اندر bubble ہے یا کوئی اور طریقہ۔</li>
        </ul>
        <p>کمزور ڈھانچہ ساری اوسط ایک بلاک میں گنتا ہے۔ بہتر ڈھانچہ <span class="en">sum</span> اور <span class="en">average</span> کو الگ فنکشن بنا دیتا ہے تاکہ دونوں دوبارہ استعمال ہوں۔</p>
        <h2>Readability</h2>
        <p>نام معنی رکھیں۔ <span class="en">a = b / c</span> کی جگہ <span class="en">average = total / count</span>۔ اندر کی طرف یکساں وقفہ۔ تبصرہ یہ بتائے کہ کیوں، نہ کہ کوڈ نے جو ظاہر کیا ہے اسے دہرائے۔ گہری شرطیں توڑ کر نام دو۔</p>
        """,
        [
            ("ایک فنکشن جو جمع بھی کرے، فائل بھی لکھے، اور اسکرین بھی رنگے، کس اصول کو توڑتا ہے؟", ["Single responsibility", "FIFO", "Contrast", "Median"], 0, "ایک ماڈیول پر ایک ذمہ داری ہونی چاہیے۔"),
            ("Readability کس بات کا نام ہے؟", ["صرف تیز ترین CPU", "بغیر چلائے منطق سمجھ آنا", "صرف encrypted disk", "صرف VPN"], 1, "پڑھنے والا بہاؤ اور ناموں سے مقصد پہچان لے۔"),
        ],
    ),
    L(
        "c2-bigo", 2, "Efficiency اور Big O", 12, "bigo",
        "O(1) سیدھی لکیر، O(n) ترچھی، O(n²) تیزی سے اوپر اٹھتی ہے۔",
        r"""
        <p class="callout gold">Big O سنہری topic ہے۔ وقت اور جگہ دونوں پوچھے جاتے ہیں: الگورتھم کتنا تیز ہے اور کتنی memory لیتا ہے۔</p>
        <p>ہم یہ دیکھتے ہیں کہ input کا سائز n بڑھے تو کام کیسے بڑھتا ہے۔</p>
        <ul>
          <li><b>Constant، </b> <span class="en">O(1)</span>: دس ہوں یا دس لاکھ، پہلا خانہ ایک ہی وقت میں کھلتا ہے۔</li>
          <li><b>Linear، </b> <span class="en">O(n)</span>: فہرست دگنی ہو تو لکیری تلاش کا وقت بھی لگ بھگ دگنا۔</li>
          <li><b>Logarithmic، </b> <span class="en">O(log n)</span>: ہر قدم مسئلہ آدھا۔ ترتیب شدہ فہرست پر binary search۔</li>
          <li><b>Quadratic، </b> <span class="en">O(n^2)</span>: اندر اندر لوپ، جیسے ہر جوڑے کا موازنہ۔ بڑے n پر مہنگا۔</li>
        </ul>
        <div class="math" data-speak="او آف لاگ این، اور او آف این اسکوائر">\[O(1),\quad O(\log n),\quad O(n),\quad O(n^{2})\]</div>
        <p>Binary search میں قدموں کی تعداد لگ بھگ یہ ہے:</p>
        <div class="math" data-speak="فلور لاگ بیس دو این، جمع ایک">\[\lfloor \log_2 n \rfloor + 1\]</div>
        <h2>شرطیں اور تکرار</h2>
        <p>ہر <span class="en">IF</span> فیصلہ ہے۔ اندر اندر شرطیں پڑھنا اور رفتار دونوں خراب کرتی ہیں۔ <span class="en">Short-circuit</span> میں نتیجہ ملتے ہی مزید شرط نہ جانچو۔</p>
        <p>لوپ سب سے بڑا اثر رکھتا ہے۔ ایک لکیری لوپ O(n) ہے۔ آدھا کرتے رہنے والا لوپ O(log n) ہے۔ nested لوپ O(n²) کی طرف جاتا ہے۔</p>
        <h2>تین سوال</h2>
        <ol>
          <li>اگر n دس گنا ہو تو وقت دس گنا بڑھے گا یا سو گنا؟ سو گنا quadratic ناکامی ہے۔</li>
          <li>رکاوٹ کہاں ہے؟ اکثر گہرا لوپ۔</li>
          <li>کیا یہ قیمت فائدے کے لائق ہے؟ بہت تیز مگر نہ پڑھے جانے والا طریقہ ہمیشہ جیت نہیں۔</li>
        </ol>
        """,
        [
            ("ترتیب شدہ فہرست میں binary search کی نشوونما کیا ہے؟", ["O(n²)", "O(log n)", "O(n!)", "O(n³) لازماً"], 1, "ہر قدم تلاش آدھی رہ جاتی ہے۔"),
            ("اندر اندر دو لوپ اکثر کون سی کلاس دیتے ہیں؟", ["O(1)", "O(n²)", "O(0)", "صرف median"], 1, "ہر عنصر کے لیے باقی عناصر دیکھنا مربع وقت ہے۔"),
        ],
        golden=True,
    ),
    L(
        "c2-refine", 2, "وضاحت اور رفتار کی اصلاح", 8, "bigo",
        "اصلاح کا مقصد بے کار قدم ہٹانا اور مناسب ڈھانچہ چننا ہے۔",
        r"""
        <h2>وضاحت کی اصلاح</h2>
        <ul>
          <li>معنی والے نام: <span class="en">average = totalSum / totalItems</span>۔</li>
          <li>کاموں کو فنکشن میں بانٹو۔</li>
          <li>اندر کی جگہ یکساں رکھو تاکہ لوپ کی گہرائی نظر آئے۔</li>
          <li>مختصر تبصرہ، خاص کر وہاں جہاں سبب چھپا ہو۔</li>
        </ul>
        <h2>رفتار کی اصلاح</h2>
        <ul>
          <li>بے کار قدم کاٹو۔ Bubble sort کے ایک پاس کے بعد آخری بڑی قدر اپنی جگہ بیٹھ جاتی ہے؛ اگلا اندرونی لوپ اسے دوبارہ نہ چھیڑے۔</li>
          <li>کام کے مطابق طریقہ: دس لاکھ ترتیب شدہ ریکارڈ میں linear search کی جگہ binary search۔</li>
          <li>جو قدر لوپ میں نہیں بدلتی اسے باہر ایک بار نکالو اور دوبارہ استعمال کرو۔</li>
          <li>ڈھانچہ کام کے مطابق ہو: بار بار آخر سے نکالنا ہو تو stack سوچو؛ باری کی قطار ہو تو queue۔</li>
        </ul>
        <pre class="code" data-speak="مستقل ضرب لوپ کے باہر ایک بار نکالو">c = price * rate
for i in range(1, n + 1):
    print(c * i)</pre>
        """,
        [
            ("لوپ کے اندر وہ ضرب جو ہر چکر میں نہیں بدلتی، کہاں ہونی چاہیے؟", ["ہر چکر میں دوبارہ", "لوپ سے باہر ایک بار", "صرف تبصرے میں", "صرف گراف میں"], 1, "مستقل کام ایک بار کر کے متغیر میں رکھو۔"),
            ("Bubble sort کی اصلاح کیا کرتی ہے؟", ["پہلے سے آخری جگہ بیٹھی قدر کو اگلے پاس میں چھوڑ دیتی ہے", "ہر قدر کو random کر دیتی ہے", "فائل مٹا دیتی ہے", "صرف رنگ بدلتی ہے"], 0, "چھوٹا اندرونی لوپ بے کار موازنہ ہٹا دیتا ہے۔"),
        ],
    ),
    L(
        "c2-linear", 2, "Array، list، stack، queue", 11, "stack",
        "Stack میں اوپر سے push اور pop ہوتے ہیں۔ آخری اندر، پہلی باہر۔",
        r"""
        <p class="callout gold">Data structure، stack، اور queue سنہری تعریفیں ہیں۔</p>
        <p>Data structure ڈیٹا کو یوں سنبھالنے کا طریقہ ہے کہ پڑھنا، بدلنا، اور عمل تیز ہوں۔ الماری میں کتابوں کی ترتیب اسی خیال کی انسانی مثال ہے۔</p>
        <p><b>Linear</b> میں عنصر قطار میں ہوتے ہیں۔ سرے کے علاوہ ہر ایک کا ایک پہلے والا اور ایک بعد والا ہوتا ہے۔ <b>Non-linear</b> میں شاخیں یا جال ہوتا ہے۔</p>
        <h2>Array</h2>
        <p>ایک جیسی قسم کے خانے ملے ہوئے memory میں۔ نمبر سے سیدھا خانہ کھلتا ہے، اس لیے پہلا یا کوئی معلوم index اکثر O(1) ہے۔ بیچ میں ڈالنا مہنگا ہو سکتا ہے کیونکہ پڑوسی کھسکتے ہیں۔</p>
        <h2>Linked list</h2>
        <p>ہر node میں قدر اور اگلے پتے کا نشان ہوتا ہے۔ خانے ملی ہوئی قطار میں ہونا ضروری نہیں۔ شروع میں ڈالنا سستا ہے۔ نمبر سے سیدھا چھلانگ نہیں؛ nویں node تک چلنا پڑتا ہے۔</p>
        <h2>Stack</h2>
        <p><span class="en">LIFO</span>: جو آخر میں چڑھا، پہلے اترے گا۔ اوپر رکھنا <span class="en">push</span>، اوپر سے ہٹانا <span class="en">pop</span>۔ مثال: واپس جانے کا بٹن، یا قوسین کی جانچ۔</p>
        <h2>Queue</h2>
        <p><span class="en">FIFO</span>: جو پہلے آیا پہلے کام ہو۔ پچھلے سرے پر <span class="en">enqueue</span>، اگلے سرے سے <span class="en">dequeue</span>۔ مثال: پرنٹر کی لائن، یا ٹکٹ کی کھڑکی۔</p>
        <p>مشترک عمل: داخل کرنا، مٹانا، ڈھونڈنا، اور ترتیب دیکھنا۔ عمل کا نام ڈھانچے کے ساتھ بدل جاتا ہے، خیال نہیں۔</p>
        """,
        [
            ("Stack کا اصول کیا ہے؟", ["FIFO", "LIFO", "random", "صرف tree"], 1, "آخری رکھی چیز پہلے نکلتی ہے۔"),
            ("پرنٹر پر پہلے بھیجی فائل پہلے چھپے، یہ کیا ہے؟", ["Queue", "صرف graph cycle", "Set union", "NaN"], 0, "یہ FIFO قطار ہے۔"),
        ],
        golden=True,
    ),
    L(
        "c2-tree", 2, "Tree، graph، اور retrieval", 10, "tree",
        "Tree کی جڑ سے شاخیں نکلتی ہیں۔ ہر بچے کا ایک والدین ہوتا ہے۔",
        r"""
        <h2>Tree</h2>
        <p>جڑ <span class="en">root</span> سے درجہ بند شاخیں۔ والدین سے بچوں کی طرف ایک سے زیادہ رشتہ ہو سکتا ہے، مگر اوپر ایک ہی راستہ ہوتا ہے۔ کالج کا چارٹ: پرنسپل جڑ، نیچے شعبے، پھر استاد۔</p>
        <h2>Graph</h2>
        <p><span class="en">Node</span> اور <span class="en">edge</span>۔ سخت درجہ نہیں؛ کوئی بھی کسی سے جڑ سکتا ہے۔ شہر کے راستے، یا دوستوں کا جال۔ Tree دراصل ایک خاص graph ہے جس میں چکر نہیں اور جڑ ایک ہے۔</p>
        <div class="compare">
          <div class="col"><h3>لکیری منظر</h3><p>حاضری کی فہرست: array۔ واپسی کا تاریخچہ: stack۔ کینٹین کی لائن: queue۔</p></div>
          <div class="col"><h3>غیر لکیری منظر</h3><p>خاندانی یا دفتری درجہ: tree۔ بس روٹس جہاں راستے مڑ کر ملیں: graph۔</p></div>
        </div>
        <h2>پڑھنے کا راستہ</h2>
        <ul>
          <li><b>Array:</b> index سے سیدھا خانہ۔</li>
          <li><b>Linked list:</b> سر سے نشان پکڑ پکڑ کر آگے۔</li>
          <li><b>Queue:</b> صرف اگلا شخص نکلتا ہے؛ بیچ والا اپنی باری سے پہلے نہیں نکلتا۔</li>
        </ul>
        <div class="callout do"><b>خود کرو:</b> تین مقامی مثالیں لکھو، ہر ایک کے ساتھ ڈھانچے کا نام اور ایک جملے میں وجہ۔</div>
        """,
        [
            ("پرنسپل سے شعبہ جات کا چارٹ کس ڈھانچے جیسا ہے؟", ["Tree", "صرف queue", "صرف set", "CSV"], 0, "ایک جڑ اور درجہ بند بچے tree ہیں۔"),
            ("Linked list میں دسواں node کیسے ملتا ہے؟", ["ہمیشہ ایک چھلانگ میں", "سر سے اشاروں پر چل کر", "صرف hash بغیر پڑھے", "صرف pie chart"], 1, "فہرست میں نمبر سے براہِ راست خانہ نہیں کھلتا۔"),
        ],
    ),
]
