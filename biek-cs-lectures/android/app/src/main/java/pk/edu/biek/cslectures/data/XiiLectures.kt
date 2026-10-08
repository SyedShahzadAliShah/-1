package pk.edu.biek.cslectures.data

import pk.edu.biek.cslectures.model.Concept
import pk.edu.biek.cslectures.model.Lecture

private const val PDF = "pdf/BIEK-CS-XII-Lectures.pdf"

private fun c(term: String, english: String, urdu: String, urdish: String) =
    Concept(term, english, urdu, urdish)

fun xiiLectures(): List<Lecture> = listOf(
    Lecture(
        id = "xii-1",
        year = "XII",
        number = 1,
        title = "Usable, Accessible, and Secure Systems",
        urduTitle = "استعمال، رسائی اور حفاظت",
        pdfAsset = PDF,
        introUrdu = "محفوظ دروازہ جو کوئی نہ کھول سکے بے کار ہے۔ ہر کنٹرول کے ساتھ بتائیں کہ کون باہر رہ سکتا ہے۔",
        introUrdish = "Mehfooz darwaza jo koi na khol sake be kar hai. Har control ke sath batain ke kon bahar reh sakta hai.",
        concepts = listOf(
            c(
                "Usability",
                "Usability is effectiveness, efficiency, and satisfaction for a stated user and task.",
                "Usability تین باتیں ہیں: کام مکمل ہو، محنت مناسب ہو، اور تجربہ سزا نہ لگے۔ ایک usability test میں صارف خود ماؤس چلاتا ہے اور ڈیزائنر خاموش رہتا ہے۔ یہ نمائش نہیں۔",
                "Usability teen baten hain: kam mukammal ho, mehnat munasib ho, aur tajurba saza na lage. Ek usability test mein sarif khud mouse chalata hai aur designer khamosh rehta hai. Yeh numayish nahi.",
            ),
            c(
                "Accessibility",
                "Colour must not be the only signal. Captions and keyboard access are part of the same task, not a favour.",
                "Accessibility کہتی ہے کہ وہی کام وہ طالب علم بھی کرے جو رنگ نہ پہچانے، سن نہ سکے، یا ماؤس نہ چلا سکے۔ صرف سرخ رنگ سے فیل دکھانا ناکافی ہے۔ ساتھ لفظ یا نشان ہونا چاہیے۔",
                "Accessibility kehti hai ke wohi kam woh talib ilm bhi kare jo rang na pehchane, sun na sake, ya mouse na chala sake. Sirf surkh rang se fail dikhana nakafi hai. Sath lafz ya nishan hona chahiye.",
            ),
            c(
                "Security tradeoff",
                "A stricter password can reduce security if people write it down. Name efficiency, cost, privacy, and ethics.",
                "بہت سخت password اگر یاد نہ رہے تو کاغذ پر لکھا جاتا ہے، اور حفاظت کم ہو جاتی ہے۔ جواب میں efficiency، cost، privacy اور ethics کا نام لیں۔ کنٹرول کے ساتھ واپسی کا راستہ بھی لکھیں۔",
                "Bohat sakht password agar yad na rahe to kaghaz par likha jata hai, aur hifazat kam ho jati hai. Jawab mein efficiency, cost, privacy aur ethics ka naam lain. Control ke sath wapsi ka rasta bhi likhain.",
            ),
            c(
                "Zero trust",
                "Being on the college network is not proof. Every request is checked, and the account gets only the access its job needs.",
                "Zero trust کہتی ہے کہ عمارت کے اندر ہونا کافی نہیں۔ ہر درخواست دوبارہ دیکھی جائے۔ Least privilege کہتی ہے کہ کلرک کا اکاؤنٹ صرف اپنے کلاس کے نمبر لکھے، پورا بورڈ نہ کھولے۔",
                "Zero trust kehti hai ke imarat ke andar hona kafi nahi. Har darkhwast dobara dekhi jaye. Least privilege kehti hai ke clerk ka account sirf apne class ke number likhe, poora board na khole.",
            ),
        ),
    ),
    Lecture(
        id = "xii-2",
        year = "XII",
        number = 2,
        title = "Trees, Stacks, and Queues",
        urduTitle = "درخت، اسٹیک اور قطار",
        pdfAsset = PDF,
        introUrdu = "پہلے قاعدہ لکھیں، پھر node کی فہرست۔ سوال والا درخت استعمال کریں، یاد کیا ہوا 50 والا نہیں۔",
        introUrdish = "Pehle qaida likhain, phir node ki fehrist. Sawal wala darakht istemal karain, yad kiya hua 50 wala nahi.",
        concepts = listOf(
            c(
                "Stack and queue",
                "A stack is last in, first out, like function calls. A queue is first in, first out, like a printer.",
                "Stack میں جو چیز آخر میں آئی وہ پہلے نکلتی ہے، جیسے function call۔ Queue میں جو کام پہلے آیا وہ پہلے چھپتا ہے، جیسے printer۔ پرنٹر پر stack لگانا وعدہ توڑتا ہے۔",
                "Stack mein jo cheez akhir mein ai woh pehle nikalti hai, jaise function call. Queue mein jo kam pehle aya woh pehle chhupta hai, jaise printer. Printer par stack lagana wada torta hai.",
            ),
            c(
                "Binary search tree",
                "Smaller values go left and larger values go right. Searching ignores one whole subtree.",
                "Binary search tree میں چھوٹی قدر بائیں اور بڑی قدر دائیں۔ 60 کی تلاش 50 سے دائیں جاتی ہے اور 70 سے بائیں۔ بایاں پورا درخت نہیں کھلتا، یہی بچت ہے۔",
                "Binary search tree mein chhoti qadar bayen aur bari qadar dain. 60 ki talash 50 se dayen jati hai aur 70 se bayen. Bayan poora darakht nahi khulta, yahi bachat hai.",
            ),
            c(
                "Traversals",
                "Preorder visits the node first. Inorder visits left, node, right, and is sorted on a BST. Postorder visits the node last.",
                "Preorder پہلے node، پھر بایاں، پھر دایاں۔ Inorder بایاں، node، دایاں، اور BST پر یہ ترتیب شدہ فہرست دیتی ہے۔ Postorder بچے پہلے اور node آخر میں۔ اگر inorder ترتیب میں نہ ہو تو درخت یا چال غلط ہے۔",
                "Preorder pehle node, phir bayan, phir dayan. Inorder bayan, node, dayan, aur BST par yeh tarteeb shuda fehrist deti hai. Postorder bache pehle aur node akhir mein. Agar inorder tarteeb mein na ho to darakht ya chaal ghalat hai.",
            ),
            c(
                "BFS and DFS",
                "Breadth-first search uses a queue and visits level by level. Depth-first search follows one branch first.",
                "BFS قطار استعمال کرتی ہے اور ایک منزل مکمل کر کے اگلی کھولتی ہے۔ DFS ایک شاخ آخر تک جاتی ہے، پھر بہن شاخ۔ CEO سے DFS پہلے HR اور Staff دیکھتی ہے، پھر IT۔",
                "BFS qatar istemal karti hai aur ek manzil mukammal kar ke agli kholti hai. DFS ek shakh akhir tak jati hai, phir behan shakh. CEO se DFS pehle HR aur Staff dekhti hai, phir IT.",
            ),
        ),
    ),
    Lecture(
        id = "xii-3",
        year = "XII",
        number = 3,
        title = "Objects, Files, and Databases",
        urduTitle = "آبجیکٹ، فائل اور ڈیٹابیس",
        pdfAsset = PDF,
        introUrdu = "Class اپنے ڈیٹا کو اپنے کام کے ساتھ رکھتی ہے۔ فائل کل بھی رہتی ہے۔ 3NF ایک حقیقت ایک جگہ رکھتی ہے۔",
        introUrdish = "Class apne data ko apne kam ke sath rakhti hai. File kal bhi rehti hai. 3NF ek haqeeqat ek jagah rakhti hai.",
        concepts = listOf(
            c(
                "Class and object",
                "A class is the pattern. An object is one vehicle. update mileage on the car must not change the van.",
                "Class نقشہ ہے اور object ایک گاڑی۔ Constructor صفات سنبھالتا ہے۔ کار کا mileage بدلنے سے وین نہیں بدلتی، کیونکہ ہر object کی اپنی صفات ہیں۔",
                "Class naqsha hai aur object ek gari. Constructor sifat sanbhalta hai. Car ka mileage badalne se van nahi badalti, kyunke har object ki apni sifat hain.",
            ),
            c(
                "Dictionary",
                "A dictionary answers a question by key. A nested list keeps row order and is scanned from the start.",
                "Dictionary چابی سے قدر دیتی ہے، جیسے roll number 103 سے نام۔ Nested list قطار میں رہتی ہے اور شروع سے دیکھی جاتی ہے۔ جب سوال یہ ہو کہ اس id کا کیا ریکارڈ ہے، dictionary موزوں ہے۔",
                "Dictionary chabi se qadar deti hai, jaise roll number 103 se naam. Nested list qatar mein rehti hai aur shuru se dekhi jati hai. Jab sawal yeh ho ke is id ka kya record hai, dictionary mauzoon hai.",
            ),
            c(
                "File mode",
                "Mode w replaces the file. Mode a appends. Mode r reads. with closes the file even if a later line fails.",
                "فائل موڈ w پرانی فائل مٹا کر لکھتی ہے۔ a آخر میں جوڑتی ہے۔ r صرف پڑھتی ہے۔ with فائل بند کر دیتی ہے چاہے آگے غلطی ہو۔ حروف گنتی سے پہلے lower کریں اگر بڑے چھوٹے حروف ایک ہوں۔",
                "File mode w purani file mita kar likhti hai. a akhir mein jorti hai. r sirf parhti hai. with file band kar deti hai chahe aage ghalti ho. Huroof ginti se pehle lower karain agar bare chhote huroof ek hon.",
            ),
            c(
                "Third normal form",
                "1NF removes repeating groups. 2NF removes dependence on only part of the key. 3NF removes a fact that depends on another non-key column.",
                "1NF ایک خانے میں ایک قدر رکھتی ہے۔ 2NF کہتی ہے کہ غیر کلیدی کالم پوری key پر منحصر ہو، آدھے پر نہیں۔ 3NF کہتی ہے کہ دفتر کا کمرہ instructor پر منحصر ہے، course پر نہیں، اس لیے الگ table بنے۔",
                "1NF ek khane mein ek qadar rakhti hai. 2NF kehti hai ke ghair kalidi column poori key par munhasir ho, aadhe par nahi. 3NF kehti hai ke daftar ka kamra instructor par munhasir hai, course par nahi, is liye alag table bane.",
            ),
            c(
                "SQL filter",
                "WHERE chooses rows before the average. Without WHERE, AVG covers the whole table.",
                "SQL میں WHERE قطاریں چنتا ہے، پھر اوسط بنتی ہے۔ WHERE کے بغیر AVG پوری table کا اوسط ہے، صرف IT کا نہیں۔ ORDER BY ترتیب بدلتا ہے، قطاریں نہیں کاٹتا۔",
                "SQL mein WHERE qataren chunta hai, phir ausat banti hai. WHERE ke baghair AVG poori table ka ausat hai, sirf IT ka nahi. ORDER BY tarteeb badalta hai, qataren nahi katta.",
            ),
        ),
    ),
    Lecture(
        id = "xii-4",
        year = "XII",
        number = 4,
        title = "Models and Hypothesis Tests",
        urduTitle = "ماڈل اور مفروضہ",
        pdfAsset = PDF,
        introUrdu = "تربیت والی قطاروں پر نمبر یادداشت ہو سکتا ہے۔ پی ویلیو یہ امکان نہیں کہ null سچ ہے۔",
        introUrdish = "Tarbiyat wali qataron par number yad-dasht ho sakta hai. P-value yeh imkan nahi ke null sach hai.",
        concepts = listOf(
            c(
                "Train-test split",
                "Learn on some rows and measure on rows the model has not seen. Otherwise the score can be memorisation.",
                "Model کو کچھ rows پر سکھائیں اور الگ رکھی rows پر ناپیں۔ اگر وہی rows دوبارہ دیکھو تو model یاد کر سکتا ہے۔ Feature میں جواب خود شامل کرنا دھوکا ہے، انجینئرنگ نہیں۔",
                "Model ko kuch rows par sikhain aur alag rakhi rows par napain. Agar wohi rows dobara dekho to model yad kar sakta hai. Feature mein jawab khud shamil karna dhoka hai, engineering nahi.",
            ),
            c(
                "Precision",
                "Precision is true positives divided by true positives plus false positives. In the lecture matrix that is 90 over 120, or 75 percent.",
                "Precision ان مثبت پیشن گوئیوں کا حصہ ہے جو واقعی مثبت تھیں۔ 90 سچے مثبت اور 30 جھوٹے مثبت ہوں تو 90 تقسیم 120، یعنی 75 فیصد۔ یہ یہ نہیں کہ 75 فیصد طلبہ پاس ہوئے۔",
                "Precision un musbat paishangoiyon ka hissa hai jo waqai musbat thin. 90 sache musbat aur 30 jhoote musbat hon to 90 taqseem 120, yani 75 feesad. Yeh yeh nahi ke 75 feesad talaba paas hue.",
            ),
            c(
                "Recall and accuracy",
                "Recall is true positives divided by all real positives. Accuracy can look high if a rare event is never predicted.",
                "Recall بتاتی ہے کہ حقیقی مثبت میں سے کتنے پکڑے گئے۔ Accuracy کل درست پیشن گوئی ہے۔ اگر واقعہ نادر ہو اور model ہمیشہ نہیں کہے تو accuracy اونچی اور recall صفر ہو سکتی ہے۔",
                "Recall batati hai ke haqeeqi musbat mein se kitne pakre gaye. Accuracy kul durust paishangoi hai. Agar waqia nadir ho aur model hamesha nahi kahe to accuracy oonchi aur recall sifar ho sakti hai.",
            ),
            c(
                "Null hypothesis",
                "The null hypothesis is no difference. A p-value is how surprising the data are if that null is true. It is not the probability that the null is true.",
                "Null hypothesis کہتی ہے کہ فرق نہیں۔ P-value بتاتی ہے کہ اگر null سچ ہو تو اتنا انتہائی نتیجہ کتنا عجیب ہے۔ یہ اس بات کا امکان نہیں کہ null سچ ہے۔ الفا سے چھوٹی p-value پر null رد ہوتی ہے۔",
                "Null hypothesis kehti hai ke farq nahi. P-value batati hai ke agar null sach ho to itna intehai nateeja kitna ajeeb hai. Yeh is bat ka imkan nahi ke null sach hai. Alpha se chhoti p-value par null radd hoti hai.",
            ),
            c(
                "Do not reject",
                "If the p-value is 0.20 and alpha is 0.05, do not reject the null. That is not proof that the null is true.",
                "اگر p-value 0.20 ہو اور alpha 0.05، تو null رد نہ کریں۔ یہ ثبوت نہیں کہ null سچ ہے۔ نمونہ چھوٹا ہو تو یہ بات ساتھ لکھیں۔ نتیجہ دیکھ کر مفروضہ بدلنا کمزور کہانی ہے۔",
                "Agar p-value 0.20 ho aur alpha 0.05, to null radd na karain. Yeh saboot nahi ke null sach hai. Namoona chhota ho to yeh bat sath likhain. Nateeja dekh kar mafrooza badalna kamzor kahani hai.",
            ),
        ),
    ),
    Lecture(
        id = "xii-5",
        year = "XII",
        number = 5,
        title = "Applications, Privacy, and Safety",
        urduTitle = "اطلاق، رازداری اور حفاظت",
        pdfAsset = PDF,
        introUrdu = "تینوں ٹیکنالوجی ایک جملے میں نہ ٹھونسیں۔ جو ٹیکنالوجی کام نہیں آتی اسے بھی نام دیں، اور کم سے کم data بانٹیں۔",
        introUrdish = "Teeno technology ek jumle mein na thonsain. Jo technology kam nahi aati ise bhi naam den, aur kam se kam data bantain.",
        concepts = listOf(
            c(
                "Choose one technology",
                "A flood sensor needs IoT and a cloud dashboard. It does not need a blockchain. Say which technology you refused.",
                "سیلابی پانی کے لیے sensor اور cloud dashboard کافی ہیں۔ Blockchain یہاں فضول ہے۔ جواب میں user، data، چنی ہوئی ٹیکنالوجی، اور ایک خطرہ لکھیں۔ خاموش sensor کو امن مت سمجھیں، خاموشی کا الارم ہونا چاہیے۔",
                "Sailabi pani ke liye sensor aur cloud dashboard kafi hain. Blockchain yahan fazool hai. Jawab mein user, data, chuni hui technology, aur ek khatra likhain. Khamosh sensor ko aman mat samjhein, khamoshi ka alarm hona chahiye.",
            ),
            c(
                "Deep learning",
                "Deep learning uses many layers and can learn features from pixels or sound. It needs data and computing, and it can copy bias.",
                "Deep learning کئی layers والا neural network ہے جو تصویر کے pixel سے خود خصوصیت سیکھ سکتا ہے۔ اسے بہت data اور حساب چاہیے۔ اگر مثالیں یک طرفہ ہوں تو غلطیاں بھی یک طرفہ ہوں گی۔ یہ ڈاکٹر نہیں۔",
                "Deep learning kai layers wala neural network hai jo tasveer ke pixel se khud khusoosiyat seekh sakta hai. Ise bohat data aur hisab chahiye. Agar misalen ek tarfa hon to ghaltiyan bhi ek tarfa hon gi. Yeh doctor nahi.",
            ),
            c(
                "Minimum share",
                "An employer checking a degree needs yes or no, the title, and the year. Not the address and not the identity card.",
                "آجر کو ڈگری کی تصدیق چاہیے: ہاں یا نہیں، عنوان اور سال۔ پتہ، نمبر اور شناختی کارڈ کی نقل نہیں۔ Policy یہ بتائے کہ کس کو کیا ملتا ہے، صرف لفظ توازن کافی نہیں۔",
                "Ajir ko degree ki tasdeeq chahiye: haan ya nahi, unwan aur saal. Pata, number aur shanakhti card ki naqal nahi. Policy yeh batae ke kis ko kya milta hai, sirf lafz tawazun kafi nahi.",
            ),
            c(
                "Phishing and 2FA",
                "Phishing tries to collect a secret. 2FA means a stolen password is not enough. It does not stop a flood of a public website.",
                "Phishing جعلی پیغام سے پاس ورڈ یا رقم مانگتا ہے۔ 2FA کہتی ہے کہ چوری شدہ password اکیلے کافی نہیں۔ یہ عوامی سائٹ پر ٹریفک کے سیلاب کو نہیں روکتی۔ تالا کا نشان دکان کو ایماندار نہیں بناتا۔",
                "Phishing jali paigham se password ya raqam mangta hai. 2FA kehti hai ke chori shuda password akele kafi nahi. Yeh awami site par traffic ke selab ko nahi rokti. Tala ka nishan dukan ko imandar nahi banata.",
            ),
            c(
                "Shared folder",
                "Invite named accounts. Do not share one login, a public edit link, or a classmate identity card.",
                "مشترکہ فولڈر میں نام والے اکاؤنٹ بلائیں۔ ایک password سب کو دینا اور شناختی کارڈ چیٹ میں لگانا دونوں غیر محفوظ ہیں۔ رپورٹ سوال، طریقہ، چارٹ، ماخذ اور حد رکھے، چیٹ رپورٹ نہیں۔",
                "Mushtarka folder mein naam wale account bulain. Ek password sab ko dena aur shanakhti card chat mein lagana donon ghair mehfooz hain. Report sawal, tareeqa, chart, makhaz aur had rakhe, chat report nahi.",
            ),
        ),
    ),
    Lecture(
        id = "xii-6",
        year = "XII",
        number = 6,
        title = "Entrepreneurship in the Digital Age",
        urduTitle = "ڈیجیٹل کاروبار",
        pdfAsset = PDF,
        introUrdu = "MVP چھوٹی حقیقی پیشکش ہے جس کا ناکام ہونا پہلے سے لکھا ہو۔ نقل شدہ کتاب فروخت کرنا کام نہیں۔",
        introUrdish = "MVP chhoti haqeeqi paishkash hai jis ka nakam hona pehle se likha ho. Naqal shuda kitab farokht karna kam nahi.",
        concepts = listOf(
            c(
                "Prototype and MVP",
                "A prototype asks whether a person can use the design. An MVP lets the user complete the real job so behaviour can be measured.",
                "Prototype پوچھتا ہے کہ آدمی ڈیزائن سمجھتا ہے یا نہیں، کاغذ کافی ہو سکتا ہے۔ MVP اتنا حقیقی ہو کہ صارف اصل کام پورا کرے، جیسے دو ہفتے اصل کارڈ مکمل کرنا۔ سلائیڈ ابھی MVP نہیں۔",
                "Prototype poochta hai ke aadmi design samajhta hai ya nahi, kaghaz kafi ho sakta hai. MVP itna haqeeqi ho ke sarif asal kam poora kare, jaise do hafte asal card mukammal karna. Slide abhi MVP nahi.",
            ),
            c(
                "Beachhead",
                "The first market is a small group you can actually reach this month, not all students in Pakistan.",
                "Beachhead پہلا چھوٹا گروہ ہے جس تک آپ اس مہینے پہنچ سکیں، مثلاً اپنی کالج کی ایک CS کلاس۔ تمام طلبہِ پاکستان جملہ ہے، آزمائش نہیں۔",
                "Beachhead pehla chhota groh hai jis tak aap is mahine pohonch saken, maslan apni college ki ek CS class. Tamam talaba-e-Pakistan jumla hai, azmaish nahi.",
            ),
            c(
                "Riskiest assumption",
                "Test the belief that would kill the idea if it is false. Friends saying they like it is a weak test.",
                "Riskiest assumption وہ بات ہے جو جھوٹی ہو تو خیال مر جائے۔ اکثر یہ ہے کہ لوگ لوٹ کر آئیں گے یا قیمت دیں گے، لوگو نہیں۔ دوستوں کا پسند ہے کہنا کمزور امتحان ہے، کیونکہ وہ شاذ ہی نہیں کہتے۔",
                "Riskiest assumption woh bat hai jo jhooti ho to khayal mar jaye. Aksar yeh hai ke log laut kar aain ge ya qeemat den ge, logo nahi. Doston ka pasand hai kehna kamzor imtehan hai, kyunke woh shaz hi nahi kehte.",
            ),
            c(
                "Failure rule",
                "Write the failing number before you start. If the test fails, change the offer or stop. Do not build the app yet.",
                "ناکامی کا عدد شروع سے پہلے لکھیں۔ مثلاً دس میں سے چھ دونوں ہفتے جواب نہ دیں تو رک جائیں۔ بعد میں لکیر ہٹانا کامیابی نہیں۔ ناکامی پر ایپ نہ بنائیں، پیشکش بدلیں یا خیال چھوڑیں۔",
                "Nakami ka adad shuru se pehle likhain. Maslan das mein se chheh donon hafte jawab na den to ruk jain. Baad mein lakeer hatana kamyabi nahi. Nakami par app na banain, paishkash badlain ya khayal chhorain.",
            ),
            c(
                "Ethical limit",
                "Do not sell copied textbooks, write someone else practical, or collect identity cards in a chat.",
                "اپنا لکھا ہوا کارڈ بیچنا جائز مشق ہے۔ درسی کتاب کے سکین، کسی کا پریکٹیکل، یا چیٹ میں شناختی کارڈ کاروبار نہیں۔ قیمت وہ لکھیں جو آپ نے خود دیکھی ہو، بنائی ہوئی نہیں۔",
                "Apna likha hua card baichna jaiz mashq hai. Darsi kitab ke scan, kisi ka practical, ya chat mein shanakhti card karobar nahi. Qeemat woh likhain jo aap ne khud dekhi ho, banai hui nahi.",
            ),
        ),
    ),
)
