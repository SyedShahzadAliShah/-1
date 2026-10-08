package pk.edu.biek.cslectures.data

import pk.edu.biek.cslectures.model.Concept
import pk.edu.biek.cslectures.model.Lecture

private const val PDF = "pdf/BIEK-CS-XI-Lectures.pdf"

private fun c(term: String, english: String, urdu: String, urdish: String) =
    Concept(term, english, urdu, urdish)

fun xiLectures(): List<Lecture> = listOf(
    Lecture(
        id = "xi-1",
        year = "XI",
        number = 1,
        title = "Computer Systems",
        urduTitle = "کمپیوٹر سسٹم",
        pdfAsset = PDF,
        introUrdu = "یہ لیکچر bit، logic gate، SDLC، network اور حفاظت کے مختصر نکات سناتا ہے۔ اصطلاح انگریزی میں رہے گی۔",
        introUrdish = "Yeh lecture bit, logic gate, SDLC, network aur hifazat ke mukhtasar nikat sunata hai. Istilah Angrezi mein rahe gi.",
        concepts = listOf(
            c(
                "Digital",
                "A digital signal uses clean 0 and 1 values. An analog signal varies smoothly.",
                "Analog signal ہموار بدلتی ہے۔ Digital signal صرف 0 اور 1 رکھتی ہے۔ Computer ہر bit کو دوبارہ صاف 0 یا 1 بنا دیتا ہے، اس لیے نقل خراب نہیں ہوتی۔",
                "Analog signal hamaar badalti hai. Digital signal sirf 0 aur 1 rakhti hai. Computer har bit ko dobara saaf 0 ya 1 bana deta hai, is liye naqal kharab nahi hoti.",
            ),
            c(
                "AND OR NOT",
                "AND is 1 only when every input is 1. OR is 1 when at least one input is 1. NOT flips the bit.",
                "AND gate تب 1 دیتا ہے جب ہر input 1 ہو۔ OR gate تب 1 دیتا ہے جب کم از کم ایک input 1 ہو۔ NOT gate 0 کو 1 اور 1 کو 0 کر دیتا ہے۔",
                "AND gate tab 1 deta hai jab har input 1 ho. OR gate tab 1 deta hai jab kam az kam ek input 1 ho. NOT gate 0 ko 1 aur 1 ko 0 kar deta hai.",
            ),
            c(
                "NAND XOR De Morgan",
                "NAND is 0 only when all inputs are 1. XOR is 1 when the inputs differ. De Morgan swaps a bar over a sum into a product of bars.",
                "NAND تب 0 دیتا ہے جب دونوں inputs 1 ہوں۔ XOR تب 1 دیتا ہے جب inputs مختلف ہوں۔ De Morgan کہتا ہے کہ OR کے اوپر NOT، الگ الگ NOT کی AND کے برابر ہے۔",
                "NAND tab 0 deta hai jab dono inputs 1 hon. XOR tab 1 deta hai jab inputs mukhtalif hon. De Morgan kehta hai ke OR ke upar NOT, alag alag NOT ki AND ke barabar hai.",
            ),
            c(
                "SDLC",
                "The stages are analysis, design, coding, testing, deployment, and maintenance. Waterfall is one pass. Agile repeats short cycles.",
                "SDLC کے مراحل analysis، design، coding، testing، deployment اور maintenance ہیں۔ Waterfall ایک ہی سمت میں آگے بڑھتا ہے۔ Agile چھوٹے cycle میں بناتا ہے اور user سے رائے لیتا ہے۔",
                "SDLC ke marahil analysis, design, coding, testing, deployment aur maintenance hain. Waterfall ek hi samt mein aage barhta hai. Agile chhote cycle mein banata hai aur user se rae leta hai.",
            ),
            c(
                "Black-box and white-box",
                "Black-box testing checks inputs and outputs. White-box testing runs the paths inside the code.",
                "Black-box testing صرف input اور output دیکھتی ہے۔ White-box testing code کے اندر والے branch چلاتی ہے۔ دونوں خطرہ کم کرتی ہیں، مگر یہ ثابت نہیں کرتیں کہ کوئی bug باقی نہیں۔",
                "Black-box testing sirf input aur output dekhti hai. White-box testing code ke andar wale branch chalati hai. Dono khatra kam karti hain, magar yeh sabit nahi kartin ke koi bug baqi nahi.",
            ),
            c(
                "OSI and TCP/IP",
                "A switch and a MAC address belong to the data-link layer. A router and an IP address belong to the network layer. TCP is transport. HTTP is application.",
                "OSI model کی سات layers ہیں۔ Switch اور MAC address، data-link layer پر ہیں۔ Router اور IP address، network layer پر ہیں۔ TCP، transport layer پر بھروسے کی ترسیل دیتا ہے۔ HTTP، application layer کا protocol ہے۔",
                "OSI model ki saat layers hain. Switch aur MAC address, data-link layer par hain. Router aur IP address, network layer par hain. TCP, transport layer par bharose ki tarseel deta hai. HTTP, application layer ka protocol hai.",
            ),
            c(
                "Star and mesh",
                "A star is easy to extend, but the central switch is a single point of failure. A mesh has extra paths, so it is more reliable and more costly.",
                "Star topology میں ہر device مرکز کے switch سے جڑی ہوتی ہے۔ نیا PC لگانا آسان ہے، مگر switch بند ہو تو ساری lab رک جاتی ہے۔ Mesh میں راستے زیادہ ہوتے ہیں، اس لیے reliability بڑھتی ہے اور خرچ بھی۔",
                "Star topology mein har device markaz ke switch se juri hoti hai. Naya PC lagana asan hai, magar switch band ho to sari lab ruk jati hai. Mesh mein rastay zyada hotay hain, is liye reliability barhti hai aur kharch bhi.",
            ),
            c(
                "Encryption and hashing",
                "Encryption can be reversed with a key. A hash is a one-way fingerprint. Authentication checks identity. Authorisation checks permission.",
                "Encryption، plaintext کو ciphertext بناتی ہے اور key سے واپس پڑھا جا سکتا ہے۔ Hashing ایک طرفہ fingerprint ہے۔ Authentication بتاتی ہے آپ کون ہیں، اور authorisation بتاتی ہے آپ کو کیا کرنے کی اجازت ہے۔",
                "Encryption, plaintext ko ciphertext banati hai aur key se wapas parha ja sakta hai. Hashing ek tarfa fingerprint hai. Authentication batati hai aap kon hain, aur authorisation batati hai aap ko kya karne ki ijazat hai.",
            ),
        ),
    ),
    Lecture(
        id = "xi-2",
        year = "XI",
        number = 2,
        title = "Computational Thinking and Algorithms",
        urduTitle = "الگورتھم اور سوچ",
        pdfAsset = PDF,
        introUrdu = "پہلے مسئلہ توڑیں، پھر صاف steps لکھیں۔ Search اور sort کے trace کاغذ پر دکھانے ہیں۔",
        introUrdish = "Pehle masla torain, phir saaf steps likhain. Search aur sort ke trace kaghaz par dikhane hain.",
        concepts = listOf(
            c(
                "Algorithm",
                "An algorithm has input, output, definite steps, and an end. Nice is not a step.",
                "Algorithm کے steps واضح ہوں، ختم ہوں، اور ہر بار ایک ہی نتیجہ دیں۔ جملہ nicely sort کرو algorithm نہیں، کیونکہ دو طلبہ اسے مختلف طرح کریں گے۔",
                "Algorithm ke steps wazih hon, khatam hon, aur har bar ek hi nateeja den. Jumla nicely sort karo algorithm nahi, kyunke do talaba ise mukhtalif tarah karain ge.",
            ),
            c(
                "Linear search",
                "Check items from the start. The list need not be sorted. Report the first match.",
                "Linear search شروع سے ہر item دیکھتی ہے۔ List کا sorted ہونا ضروری نہیں۔ پہلا match ملے تو رک جائیں، اور نہ ملے تو Not found لکھیں۔",
                "Linear search shuru se har item dekhti hai. List ka sorted hona zaruri nahi. Pehla match milay to ruk jain, aur na milay to Not found likhain.",
            ),
            c(
                "Binary search",
                "The list must be sorted. Each comparison discards about half of the remaining items.",
                "Binary search صرف sorted list پر چلتی ہے۔ درمیان والی قدر دیکھو۔ ہدف چھوٹا ہو تو دایاں آدھا چھوڑ دو، بڑا ہو تو بایاں آدھا۔ Unsorted list پر یہ غلط ہے، سست نہیں۔",
                "Binary search sirf sorted list par chalti hai. Darmiyan wali qadar dekho. Hadaf chhota ho to dayan aadha chhor do, bara ho to bayan aadha. Unsorted list par yeh ghalat hai, sust nahi.",
            ),
            c(
                "Bubble sort",
                "Swap neighbours that are out of order. Show every pass, not only the final list.",
                "Bubble sort پڑوسی نمبر بدلتا ہے اگر وہ الٹے ہوں۔ پہلے pass کے بعد سب سے بڑی قدر آخر میں پہنچ جاتی ہے۔ امتحان میں ہر pass لکھیں، صرف آخری list نہیں۔",
                "Bubble sort parosi number badalta hai agar woh ultay hon. Pehle pass ke baad sab se bari qadar akhir mein pohonch jati hai. Imtehan mein har pass likhain, sirf akhiri list nahi.",
            ),
            c(
                "Insertion sort",
                "Grow a sorted portion on the left by inserting the next value into its place.",
                "Insertion sort بائیں طرف sorted حصہ بڑھاتا ہے۔ اگلی قدر کو اس کی جگہ ڈالیں، جیسے تاش کے پتے سنوارتے ہیں۔ برابر قدریں اپنی ترتیب رکھتی ہیں۔",
                "Insertion sort bayen taraf sorted hissa barhata hai. Agli qadar ko us ki jagah dalain, jese tash ke patte sanwarte hain. Barabar qadren apni tarteeb rakhti hain.",
            ),
        ),
    ),
    Lecture(
        id = "xi-3",
        year = "XI",
        number = 3,
        title = "Programming Fundamentals in Python",
        urduTitle = "پائتھن کی بنیاد",
        pdfAsset = PDF,
        introUrdu = "Python میں input متن دیتا ہے۔ حساب سے پہلے اسے عدد بنائیں۔ Function قدر واپس کرے، صرف screen پر نہ چھاپے۔",
        introUrdish = "Python mein input matn deta hai. Hisab se pehle ise adad banain. Function qadar wapas kare, sirf screen par na chhape.",
        concepts = listOf(
            c(
                "input and types",
                "input returns text. Use int or float before arithmetic. One equals sign assigns. Two equal signs compare.",
                "input ہمیشہ text دیتا ہے۔ حساب سے پہلے int یا float لگائیں۔ ایک برابر کی علامت قدر رکھتی ہے، اور دو برابر کی علامت موازنہ کرتی ہے۔ if marks = 40 غلط ہے۔",
                "input hamesha text deta hai. Hisab se pehle int ya float lagain. Ek barabar ki alamat qadar rakhti hai, aur do barabar ki alamat muwazana karti hai. if marks = 40 ghalat hai.",
            ),
            c(
                "if elif else",
                "Indentation is the structure. elif is the next test. The body is the indented lines.",
                "if، elif اور else میں نیچے کی سطر اندر ہونی چاہیے۔ وہی سطر branch کا حصہ ہے۔ غلط indent پروگرام چل سکتا ہے اور غلط جواب دے سکتا ہے۔",
                "if, elif aur else mein neeche ki satr andar honi chahiye. Wohi satr branch ka hissa hai. Ghalat indent program chal sakta hai aur ghalat jawab de sakta hai.",
            ),
            c(
                "range",
                "range of 5 gives 0, 1, 2, 3 and 4. The stop value is not included.",
                "range پانچ، صفر سے چار تک دیتا ہے، پانچ شامل نہیں۔ List کا پہلا index صفر ہے۔ Loop اگر ایک سے شروع ہو تو پہلی قدر رہ جاتی ہے۔",
                "range paanch, sifar se char tak deta hai, paanch shamil nahi. List ka pehla index sifar hai. Loop agar ek se shuru ho to pehli qadar reh jati hai.",
            ),
            c(
                "function",
                "A function takes parameters and returns a value. Test the return value, for example 0 Celsius is 32 Fahrenheit.",
                "Function پیرامیٹر لیتی ہے اور return سے قدر واپس دیتی ہے۔ صفر Celsius، 32 Fahrenheit بنتا ہے، اور سو Celsius، 212۔ جو function صرف print کرے اسے جانچنا مشکل ہے۔",
                "Function parameter leti hai aur return se qadar wapas deti hai. Sifar Celsius, 32 Fahrenheit banta hai, aur sau Celsius, 212. Jo function sirf print kare ise janchna mushkil hai.",
            ),
            c(
                "turtle and library",
                "penup moves without drawing. A square turns 90 degrees. Importing math is abstraction: you use the name, not the hidden method.",
                "turtle میں penup قلم اٹھاتا ہے تاکہ دو شکلوں کے درمیان لکیر نہ بنے۔ مربع ہر بار 90 ڈگری مڑتا ہے۔ math لائبریری استعمال کرنا abstraction ہے، اندرونی طریقہ پڑھے بغیر۔",
                "turtle mein penup qalam uthata hai take do shaklon ke darmiyan lakeer na banay. Murabba har bar 90 degree murta hai. math library istemal karna abstraction hai, andaruni tareeqa parhe baghair.",
            ),
        ),
    ),
    Lecture(
        id = "xi-4",
        year = "XI",
        number = 4,
        title = "Data and Analysis",
        urduTitle = "ڈیٹا اور تجزیہ",
        pdfAsset = PDF,
        introUrdu = "ایک حقیقت ایک جگہ رہے۔ چارٹ وہ سوال دکھائے جو آپ پوچھ رہے ہیں، اور تعلق کو سبب نہ کہیں۔",
        introUrdish = "Ek haqeeqat ek jagah rahe. Chart woh sawal dikhae jo aap pooch rahe hain, aur taaluq ko sabab na kahen.",
        concepts = listOf(
            c(
                "Primary key",
                "A primary key identifies one row. A name is a poor key because names repeat.",
                "Primary key ایک row کو پہچانتی ہے اور دہراتی نہیں۔ طالب علم کا نام کمزور key ہے، کیونکہ نام دہرتے ہیں۔ Roll number بہتر key ہے۔",
                "Primary key ek row ko pehchanti hai aur dohrati nahi. Talib ilm ka naam kamzor key hai, kyunke naam dohrte hain. Roll number behtar key hai.",
            ),
            c(
                "Foreign key",
                "A foreign key must match a real primary key. That rule is referential integrity.",
                "Foreign key دوسری table کی primary key کی طرف اشارہ کرتی ہے۔ Referential integrity کہتی ہے کہ ایسا roll number loan میں نہ ہو جو Student میں موجود نہیں۔",
                "Foreign key doosri table ki primary key ki taraf ishara karti hai. Referential integrity kehti hai ke aisa roll number loan mein na ho jo Student mein maujood nahi.",
            ),
            c(
                "Many to many",
                "Students and subjects need a third table of pairs. Do not make Book1, Book2, Book3 columns.",
                "جب ایک طالب علم کئی subjects لے اور ایک subject کے کئی طلبہ ہوں تو تیسری table بنتی ہے، جیسے Enrolment۔ ایک row میں Book1 Book2 رکھنا رشتہ نہیں۔",
                "Jab ek talib ilm kai subjects le aur ek subject ke kai talaba hon to teesri table banti hai, jaise Enrolment. Ek row mein Book1 Book2 rakhna rishta nahi.",
            ),
            c(
                "Mean and median",
                "The mean is the arithmetic average and moves when one extreme value is added. The median is the middle of the sorted list.",
                "Mean جمع تقسیم تعداد ہے۔ ایک بہت بڑی قدر mean کو اوپر کھینچتی ہے۔ Median ترتیب کے بعد درمیان کی قدر ہے۔ عام طالب علم کے لیے median ایماندار ہو سکتا ہے۔",
                "Mean jama taqseem tadad hai. Ek bohat bari qadar mean ko upar kheenchti hai. Median tarteeb ke baad darmiyan ki qadar hai. Aam talib ilm ke liye median imandar ho sakta hai.",
            ),
            c(
                "Correlation",
                "y equals m x plus c summarises a straight association. Correlation is not causation.",
                "لکیر y برابر m x جمع c صرف سیدھا تعلق دکھاتی ہے۔ Correlation سبب نہیں۔ آئس کریم اور پنکھے ایک ساتھ بڑھیں تو گرمی دونوں کی وجہ ہو سکتی ہے، آئس کریم پنکھے کی نہیں۔",
                "Lakeer y barabar m x jama c sirf seedha taaluq dikhati hai. Correlation sabab nahi. Ice cream aur pankhe ek sath barhein to garmi donon ki wajah ho sakti hai, ice cream pankhe ki nahi.",
            ),
        ),
    ),
    Lecture(
        id = "xi-5",
        year = "XI",
        number = 5,
        title = "Applications and Impacts",
        urduTitle = "استعمال اور اثر",
        pdfAsset = PDF,
        introUrdu = "ہر مثال میں user، data، ٹیکنالوجی اور ایک خطرہ لکھیں۔ تعریف اکیلے نمبر نہیں دیتی۔",
        introUrdish = "Har misal mein user, data, technology aur ek khatra likhain. Tareef akele number nahi deti.",
        concepts = listOf(
            c(
                "IoT",
                "An IoT chain is a sensor, a network, processing often in the cloud, and an action or a message.",
                "IoT میں sensor ناپتا ہے، network پڑھتا ہے، cloud محفوظ یا جانچتا ہے، اور پھر عمل ہوتا ہے یا آدمی کو پیغام جاتا ہے۔ سستا sensor اور سستا ریڈیو مل کر اسے ممکن بناتے ہیں۔",
                "IoT mein sensor napta hai, network parhta hai, cloud mehfooz ya janchta hai, aur phir amal hota hai ya aadmi ko paigham jata hai. Sasta sensor aur sasta radio mil kar ise mumkin banate hain.",
            ),
            c(
                "Cloud",
                "Cloud computing rents storage or processing over the network. It still needs access rules and a working link.",
                "Cloud computing سرور کرایے پر دیتی ہے تاکہ نتیجے کے دن گنجائش بڑھے اور اتوار کو کم ہو۔ یہ خود حفاظت نہیں۔ Link ٹوٹے تو dashboard خاموش ہو جاتا ہے۔",
                "Cloud computing server kiraye par deti hai take nateeje ke din gunjaish barhe aur itwar ko kam ho. Yeh khud hifazat nahi. Link toote to dashboard khamosh ho jata hai.",
            ),
            c(
                "Blockchain",
                "A blockchain is a shared ledger where changing an old record is obvious. It does not make false data true.",
                "Blockchain ایک مشترکہ ledger ہے جس میں پرانا ریکارڈ چپکے سے بدلنا ظاہر ہو جاتا ہے۔ یہ جھوٹے کاغذ کو سچا نہیں بناتی۔ مکمل میڈیکل فائل اس پر رکھنا رازداری کو نقصان دے سکتا ہے۔",
                "Blockchain ek mushtarka ledger hai jis mein purana record chupke se badalna zahir ho jata hai. Yeh jhoote kaghaz ko sacha nahi banati. Mukammal medical file is par rakhna razdari ko nuqsan de sakta hai.",
            ),
            c(
                "Reliable source",
                "A reliable source shows the author, the date, and the evidence. A forwarded screenshot of a date sheet does not.",
                "قابلِ اعتماد ماخذ پر لکھنے والا، تاریخ اور ثبوت نظر آئیں۔ بورڈ کی تاریخِ امتحان بورڈ کی اپنی سائٹ پر ہو۔ آگے بھیجا ہوا screenshot بدل سکتا ہے، اس لیے وہ ماخذ کمزور ہے۔",
                "Qabil-e-aitemad makhaz par likhne wala, tareekh aur saboot nazar aain. Board ki tareekh-e-imtehan board ki apni site par ho. Aage bheja hua screenshot badal sakta hai, is liye woh makhaz kamzor hai.",
            ),
            c(
                "Digital divide",
                "The gap is devices, connection, skill, language, and accessibility. Assistive technology, such as captions, reduces a barrier.",
                "Digital divide آلے، کنکشن، مہارت، زبان اور رسائی کا فرق ہے۔ Screen reader اور captions رکاوٹ کم کرتے ہیں۔ ایسا ہوم ورک جو گھر پر laptop مانگے، ہر طالب علم کا ایک جیسا کام نہیں۔",
                "Digital divide aale, connection, maharat, zaban aur rasai ka farq hai. Screen reader aur captions rukawat kam karte hain. Aisa home work jo ghar par laptop mange, har talib ilm ka ek jaisa kam nahi.",
            ),
        ),
    ),
    Lecture(
        id = "xi-6",
        year = "XI",
        number = 6,
        title = "Digital Literacy and a Prototype",
        urduTitle = "ڈیجیٹل خواندگی اور نمونہ",
        pdfAsset = PDF,
        introUrdu = "تلاش آپریٹر صفحے کو سچا نہیں کرتے۔ چارٹ کے ساتھ تعداد لکھیں، اور prototype ایک صارف سے جانچیں۔",
        introUrdish = "Talash operator safhe ko sacha nahi karte. Chart ke sath tadad likhain, aur prototype ek sarif se janchain.",
        concepts = listOf(
            c(
                "Search operators",
                "Quotes keep words together. site and filetype narrow the search. They do not prove the page is correct.",
                "جملے کے گرد quotes الفاظ کو ساتھ رکھتے ہیں۔ site اور filetype تلاش تنگ کرتے ہیں۔ یہ نہیں بتاتے کہ صفحہ درست یا تازہ ہے۔ پہلا لنک فیصلہ نہیں، درجہ ہے۔",
                "Jumle ke gird quotes alfaaz ko sath rakhte hain. site aur filetype talash tang karte hain. Yeh nahi batate ke safha durust ya taza hai. Pehla link faisla nahi, darja hai.",
            ),
            c(
                "Primary data",
                "Primary data is what you collect for this question. Secondary data was published by someone else and must be cited.",
                "Primary data وہ ہے جو آپ اس سوال کے لیے خود جمع کریں، جیسے اپنی کلاس کا survey۔ Secondary data کسی اور کی شائع شدہ جدول ہے، اسے اپنی جمع کردہ مت کہیں۔",
                "Primary data woh hai jo aap is sawal ke liye khud jama karain, jaise apni class ka survey. Secondary data kisi aur ki shaya shuda jadwal hai, ise apni jama karda mat kahen.",
            ),
            c(
                "Sample size",
                "Write n next to the chart. One section is not all of BIEK.",
                "چارٹ کے نیچے n لکھیں، یعنی کتنے طلبہ شامل تھے۔ ایک سیکشن کا نتیجہ پورے BIEK کا دعویٰ نہیں بنتا۔ عنوان وہ نتیجہ نہ چلائے جو اعداد نہیں دیتے۔",
                "Chart ke neeche n likhain, yani kitne talaba shamil thay. Ek section ka nateeja poore BIEK ka dawa nahi banta. Unwan woh nateeja na chalaye jo aadad nahi dete.",
            ),
            c(
                "Prototype",
                "A prototype is a cheap early version. Watch a user who did not design it, then change one thing.",
                "Prototype سستا ابتدائی نمونہ ہے تاکہ سیکھیں۔ اسے اس طالب علم کے ہاتھ دیں جس نے اسے نہیں بنایا، خاموش رہیں، اور جہاں وہ رکا وہاں ایک چیز بدلیں۔ خوبصورتی نمبر نہیں، تبدیلی نمبر ہے۔",
                "Prototype sasta ibtidai namoona hai take seekhain. Ise us talib ilm ke hath den jis ne ise nahi banaya, khamosh rahen, aur jahan woh ruka wahan ek cheez badlain. Khoobsurati number nahi, tabdeeli number hai.",
            ),
        ),
    ),
)
