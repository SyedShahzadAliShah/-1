package com.couplesguide.postures.data

object PdfBookRepository {

    private const val ASSET_DIR = "pdf_source"

    fun getPages(): List<PdfBookPage> = pages

    fun getPage(pageNumber: Int): PdfBookPage? = pages.find { it.pageNumber == pageNumber }

    fun getTotalPages(): Int = pages.size

    fun buildFullNarration(): String = pages.joinToString(" ") { it.narrationUr }

    fun buildNarrationForPage(pageNumber: Int): String =
        getPage(pageNumber)?.narrationUr.orEmpty()

    private val pages = listOf(
        PdfBookPage(
            pageNumber = 1,
            assetImage = "$ASSET_DIR/page_01.png",
            titleUr = "مسلم کاما سُترا — جنسی پوزیشنز",
            narrationUr = "خوش آمدید۔ مسلم کاما سُترا جنسی پوزیشنز۔ موضوع کی حساس نوعیت کی وجہ سے، یہ رہنما شوہر اور بیوی کے درمیان حلال قربت کے بارے میں ہے۔ مصنف: گمنام۔",
            sectionType = PdfBookPage.SectionType.COVER
        ),
        PdfBookPage(
            pageNumber = 2,
            assetImage = "$ASSET_DIR/page_02.png",
            titleUr = "تعارف",
            narrationUr = "تعارف۔ اسلام زندگی کا مکمل ضابطہ ہے۔ اس میں شوہر اور بیوی کے درمیان سب سے قریبی تعلقات کا طریقہ بھی شامل ہے۔ اس موضوع پر اسلامی متون میں سے ایک مشہور کتاب معطر باغِ لذت ہے۔ ڈاکٹر احمد صخر کی کتاب بھی بہترین ہے۔ بہت سے صحیح احادیث بھی موجود ہیں۔ جو حرام نہیں وہ جائز ہے۔ ہم صرف نکاح میں، ایک مرد اور ایک عورت کے ساتھ جنسی تعلق رکھتے ہیں۔ ہم اپنے شریکِ حیات کی جائز جنسی ضروریات اور خواہشات کو محبت سے پورا کرتے ہیں۔",
            sectionType = PdfBookPage.SectionType.INTRO
        ),
        PdfBookPage(
            pageNumber = 3,
            assetImage = "$ASSET_DIR/page_03.png",
            titleUr = "جنسی اخلاقیات",
            narrationUr = "جنسی اخلاقیات۔ جنسی تعلق محبت کی انتہائی عکاسی ہے اور یہ جسمانی اور جذباتی مکمل ملاقات ہے۔ قرآنِ کریم میں شوہر اور بیوی کے اس تعلق کا خوبصورت اظہار ہے: وہ تمہارے لباس ہیں اور تم ان کے لباس ہو۔ سورۃ البقرہ آیت ایک سو ستاسی۔",
            sectionType = PdfBookPage.SectionType.ETHICS
        ),
        PdfBookPage(
            pageNumber = 4,
            assetImage = "$ASSET_DIR/page_04.png",
            titleUr = "جنسی تعلق صدقہ کے طور پر",
            narrationUr = "شوہر اور بیوی کے درمیان جنسی اتحاد صرف خواہش کی تکلیف سے نجات حاصل کرنے سے زیادہ ہے۔ نبی کریم نے سکھایا کہ یہ اسلام میں صدقات میں سے ایک ہے۔ آپ نے صحابہ سے فرمایا: جب تم میں سے کوئی اپنی بیوی سے حلال تعلق قائم کرے تو یہ اجر والا صدقہ ہے۔",
            sectionType = PdfBookPage.SectionType.ETHICS
        ),
        PdfBookPage(
            pageNumber = 5,
            assetImage = "$ASSET_DIR/page_05.png",
            titleUr = "جنسی پوزیشنز — تعارف",
            narrationUr = "جنسی پوزیشنز۔ آگے کی سلائیڈز میں کچھ عام پوزیشنز ہیں۔ سب سے عام مشنری ہے۔ آخر میں وہی اختیار کریں جو دونوں ساتھیوں کو اطمینان دے۔ تخلیقی بنیں۔ احترام کریں۔ جو اللہ نے حلال کیا اس سے لطف اٹھائیں۔",
            sectionType = PdfBookPage.SectionType.POSITIONS
        ),
        PdfBookPage(
            pageNumber = 6,
            assetImage = "$ASSET_DIR/page_06.png",
            titleUr = "پوزیشنز — تصویری رہنما",
            narrationUr = "اب ہم مختلف پوزیشنز کی تصویری رہنمائی دیکھیں گے۔ ہر پوزیشن میں آرام، بات چیت اور باہمی رضامندی اہم ہے۔",
            sectionType = PdfBookPage.SectionType.POSITIONS
        ),
        PdfBookPage(
            pageNumber = 7,
            assetImage = "$ASSET_DIR/page_07.png",
            titleUr = "مشنری، عورت اوپر، کنول",
            narrationUr = "پہلی پوزیشن: مشنری۔ مرد اوپر، عورت نیچے، آمنے سامنے۔ دوسری: عورت اوپر۔ عورت اوپر بیٹھ کر حرکت اور رفتار کنٹرول کرتی ہے۔ تیسری: کنول یا لوٹس۔ دونوں ساتھی آمنے سامنے بیٹھ کر گھیر لیتے ہیں۔",
            sectionType = PdfBookPage.SectionType.POSITIONS
        ),
        PdfBookPage(
            pageNumber = 8,
            assetImage = "$ASSET_DIR/page_08.png",
            titleUr = "کھڑے، قینچی، پل",
            narrationUr = "کھڑے ہوئے پوزیشن۔ مرد کھڑا ہو کر عورت کو اٹھاتا ہے۔ قینچی پوزیشن۔ دونوں ساتھی آمنے سامنے لیٹ کر ٹانگیں باہم گھیرتے ہیں۔ پل پوزیشن۔ عورت گھٹنوں کے بل، مرد پیچھے سے۔",
            sectionType = PdfBookPage.SectionType.POSITIONS
        ),
        PdfBookPage(
            pageNumber = 9,
            assetImage = "$ASSET_DIR/page_09.png",
            titleUr = "مہراب، لنجز",
            narrationUr = "مہراب پوزیشن۔ مرد عورت کے اوپر جھکا ہوا۔ لنجز پوزیشن۔ عورت اوپر، مرد پیٹ کے بل۔ دونوں میں توازن اور آرام ضروری ہے۔",
            sectionType = PdfBookPage.SectionType.POSITIONS
        ),
        PdfBookPage(
            pageNumber = 10,
            assetImage = "$ASSET_DIR/page_10.png",
            titleUr = "بیٹھے ہوئے، چمچہ، ٹی شکل",
            narrationUr = "بیٹھے ہوئے پوزیشن۔ مرد کرسی پر بیٹھا، عورت اس کی گود میں۔ چمچہ پوزیشن۔ دونوں ایک طرف لیٹے، مرد پیچھے سے۔ ٹی شکل پوزیشن۔ دونوں ساتھی عمودی زاویے پر لیٹے ہوئے۔",
            sectionType = PdfBookPage.SectionType.POSITIONS
        ),
        PdfBookPage(
            pageNumber = 11,
            assetImage = "$ASSET_DIR/page_11.png",
            titleUr = "مساج پوزیشنز",
            narrationUr = "مساج پوزیشنز۔ قربت سے پہلے اور بعد میں مساج تعلق مضبوط کرتا ہے۔ پیٹ کے بل مساج آرام دہ ہے۔ ہلکے ہاتھوں سے کندھوں اور کمر کی مالش شریکِ حیات کو سکون دیتی ہے۔",
            sectionType = PdfBookPage.SectionType.MASSAGE
        ),
        PdfBookPage(
            pageNumber = 12,
            assetImage = "$ASSET_DIR/page_12.png",
            titleUr = "تعلق کے بعد",
            narrationUr = "تعلق کے بعد۔ دونوں کو غسل کرنا چاہیے۔ اگر فوراً ممکن نہ ہو تو وضو کر لیں، اور بعد میں مکمل غسل یا غسل کر لیں۔ یہ اسلامی طہارت کے احکام ہیں۔",
            sectionType = PdfBookPage.SectionType.AFTERCARE
        ),
        PdfBookPage(
            pageNumber = 13,
            assetImage = "$ASSET_DIR/page_13.png",
            titleUr = "رول پلے اور تخیل",
            narrationUr = "رول پلے اور تخیل۔ یہ وسیع موضوع ہے۔ اپنے اور اپنے شریکِ حیات کے درمیان تخیل کرنا ایک بات ہے، غیر اخلاقی تخیل دوسری۔ اللہ ہمارے خیالات کا بھی خیال رکھتے ہیں۔ محفوظ طریقہ یہ ہے کہ جو حقیقت میں غلط ہو اس کی تخیل نہ کریں۔ ہمیشہ خود کو ہی ادا کریں، شادی شدہ جوڑے کے طور پر۔ تخیل میں بھی آپ شوہر بیوی ہی رہیں۔",
            sectionType = PdfBookPage.SectionType.FANTASY
        ),
        PdfBookPage(
            pageNumber = 14,
            assetImage = "$ASSET_DIR/page_14.png",
            titleUr = "ممنوعہ جنسی تعلق",
            narrationUr = "ممنوعہ جنسی تعلق۔ حیض کے دوران۔ مقعدی تعلق۔ زچگی کے بعد جب تک اجازت نہ ہو۔ روزے کی حالت میں۔ ہم بدکاری، زنا، ہم جنس پرستی، بہیمیت، فحش کاری اور محارم سے بچیں۔ سوتے کمرے کے راز دوستوں سے نہ شیئر کریں۔ حدیث: قیامت کے دن سب سے نیچے درجے والے میں سے ایک وہ شخص ہے جو اپنے راز افشا کرے۔",
            sectionType = PdfBookPage.SectionType.PROHIBITED
        ),
        PdfBookPage(
            pageNumber = 15,
            assetImage = "$ASSET_DIR/page_15.png",
            titleUr = "مزید تفصیلات",
            narrationUr = "مزید تفصیلات کے لیے islamsexlove.wordpress.com ملاحظہ کریں۔ یہ اردو سینماٹک رہنما یہیں ختم ہوتا ہے۔ آپ مکمل کتاب پی ڈی ایف میں برآمد کر سکتے ہیں۔ اللہ آپ کے تعلق کو برکت دے۔",
            sectionType = PdfBookPage.SectionType.CLOSING
        )
    )
}
