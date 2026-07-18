package com.couplesguide.postures.data

import com.couplesguide.postures.R

object ImaginationPostureRepository {

    fun getImaginationPostures(): List<Posture> = chefSpecials

    private val chefSpecials = listOf(
        special(
            id = "dum_biryani", illustrationRes = R.drawable.pic_dum_biryani,
            enName = "Lal Qila Dum Biryani", urName = "لال قلعہ دم بریانی",
            enCat = "Chef Special", urCat = "شیف کی خاص ڈش",
            enSummary = "The crown jewel — sealed pot biryani with saffron and aged basmati.",
            urSummary = "تاج کی جڑ — زعفران اور پرانے باسمتی کے ساتھ بند برتن بریانی۔",
            enDesc = "Lal Qila's most celebrated dish. Premium basmati layered with tender mutton, sealed with dough, and slow-cooked on dum for hours. Only at the chef's special station.",
            urDesc = "لال قلعہ کی سب سے مشہور ڈش۔ پریمیم باسمتی، نرم مٹن، آٹے سے بند، گھنٹوں دم پر۔ صرف شیف سپیشل سٹیشن پر۔",
            enSteps = listOf(
                "Marinate mutton overnight in royal biryani spices.",
                "Parboil premium aged basmati with whole spices.",
                "Layer rice and mutton with fried onions, mint, and saffron.",
                "Seal pot with wheat dough and cook on very low heat 45 minutes.",
                "Open at table for dramatic presentation."
            ),
            urSteps = listOf(
                "مٹن کو شاہی بریانی مسالوں میں رات بھر میرینیٹ کریں۔",
                "پریمیم باسمتی سابت مسالوں کے ساتھ 70% پکائیں۔",
                "چاول اور مٹن کی پرتیں، بھنی پیاز، پودینہ، زعفران۔",
                "آٹے سے بند کر 45 منٹ بہت ہلکی آنچ پر پکائیں۔",
                "میز پر کھول کر پیش کریں۔"
            ),
            enTips = listOf("Arrive early — this sells out first.", "Ask for extra raita.", "Photograph the dum opening!"),
            urTips = listOf("جلدی آئیں — سب سے پہلے ختم ہوتی ہے۔", "اضافی رائتہ مانگیں۔", "دم کھولنے کی تصویر لیں!")
        ),
        special(
            id = "lq_karahi", illustrationRes = R.drawable.pic_lq_karahi,
            enName = "Lal Qila Special Karahi", urName = "لال قلعہ سپیشل کڑاہی",
            enCat = "Chef Special", urCat = "شیف کی خاص ڈش",
            enSummary = "Secret-recipe karahi with double-cooked tomatoes and special masala.",
            urSummary = "خفیہ نسخہ کڑاہی، دو بار پکے ٹماٹر اور خاص مسالہ۔",
            enDesc = "The house signature karahi unavailable anywhere else. Chef's proprietary spice blend with lamb cooked in a cast-iron karahi over open flame.",
            urDesc = "گھر کی دستخط کڑاہی۔ شیف کا خاص مسالہ، کھلے شعلے پر لوہے کی کڑاہی میں مٹن۔",
            enSteps = listOf(
                "Heat karahi with ghee until smoking.",
                "Add Lal Qila special masala and lamb.",
                "Cook tomatoes twice for deeper flavor.",
                "Finish with butter, ginger, and green chilies.",
                "Serve sizzling directly in the karahi."
            ),
            urSteps = listOf(
                "کڑاہی میں گھی دھوئیں تک گرم کریں۔",
                "لال قلعہ سپیشل مسالہ اور مٹن ڈالیں۔",
                "ٹماٹر دو بار پکائیں گہرے ذائقے کے لیے۔",
                "مکھن، ادرک، ہری مرچ سے ختم کریں۔",
                "کڑاہی میں گرم گرم پیش کریں۔"
            ),
            enTips = listOf("Limited portions daily.", "Best with roghni naan.", "Medium spice level."),
            urTips = listOf("روزانہ محدود مقدار۔", "روغنی نان کے ساتھ بہترین۔", "درمیانی تیکھا۔")
        ),
        special(
            id = "shahi_tukda", illustrationRes = R.drawable.pic_shahi_tukda,
            enName = "Shahi Tukda", urName = "شاہی ٹکڑا",
            enCat = "Chef Special", urCat = "شیف کی خاص ڈش",
            enSummary = "Royal bread pudding with rabri and silver leaf.",
            urSummary = "ربڑی اور چاندی ورق والا شاہی بریڈ پڈنگ۔",
            enDesc = "Fried bread soaked in saffron milk, topped with thick rabri, pistachios, and edible silver. A Mughal-era dessert revived at Lal Qila.",
            urDesc = "زعفران دودھ میں تلی روٹی، گاڑھی ربڑی، پستے، چاندی ورق۔ لال قلعہ پر مغل دور کا میٹھا۔",
            enSteps = listOf(
                "Fry bread slices golden in ghee.",
                "Soak in warm saffron-cardamom milk.",
                "Prepare thick rabri from reduced milk.",
                "Layer bread, rabri, and nuts.",
                "Garnish with silver leaf and rose petals."
            ),
            urSteps = listOf(
                "روٹی کے ٹکڑے گھی میں سنہری تلیں۔",
                "گرم زعفران ایلیچی دودھ میں بھگوئیں۔",
                "گاڑھا دودھ سے ربڑی بنائیں۔",
                "روٹی، ربڑی، مغز کی پرتیں۔",
                "چاندی ورق اور گلاب کی پنکھڑیاں۔"
            ),
            enTips = listOf("Serve at room temperature.", "Small portions — very rich."),
            urTips = listOf("کمرے کے درجے حرارت پر۔", "چھوٹے حصے — بہت غنی۔")
        ),
        special(
            id = "prawn_tempura", illustrationRes = R.drawable.pic_prawn_tempura,
            enName = "Prawn Tempura", urName = "پرawn ٹیمپورا",
            enCat = "Chef Special", urCat = "شیف کی خاص ڈش",
            enSummary = "Crispy battered prawns with wasabi mayo.",
            urSummary = "وسابی مایو کے ساتھ کرسپی پرawn۔",
            enDesc = "Fresh jumbo prawns in light tempura batter, fried until golden. Served with wasabi mayo and pickled ginger at Lal Qila's fusion counter.",
            urDesc = "بھاری پرawn ہلکے ٹیمپورا بیٹر میں، سنہری تلے۔ وسابی مایو اور اچار ادرک کے ساتھ۔",
            enSteps = listOf(
                "Clean and devein jumbo prawns.",
                "Make ice-cold tempura batter.",
                "Dip prawns and deep-fry until crispy.",
                "Serve immediately with wasabi mayo.",
                "Garnish with pickled ginger and lemon."
            ),
            urSteps = listOf(
                "بھاری پرawn صاف کریں۔",
                "برف ٹھنڈا ٹیمپورا بیٹر بنائیں۔",
                "پرawn ڈبو کر کرسپی تلیں۔",
                "وسابی مایو کے ساتھ فوراً پیش کریں۔",
                "اچار ادرک اور لیموں سے سجائیں۔"
            ),
            enTips = listOf("Weekend special only.", "Eat immediately while crispy."),
            urTips = listOf("صرف ہفتے کے آخر میں۔", "کرسپی ہوتے ہی کھائیں۔")
        ),
        special(
            id = "sizzling_brownie", illustrationRes = R.drawable.pic_sizzling_brownie,
            enName = "Sizzling Brownie", urName = "سزلنگ براؤنی",
            enCat = "Chef Special", urCat = "شیف کی خاص ڈش",
            enSummary = "Hot chocolate brownie on sizzler with ice cream.",
            urSummary = "آئس کریم کے ساتھ سزلر پر گرم چاکلیٹ براؤنی۔",
            enDesc = "Warm fudge brownie served on a sizzling hot plate with vanilla ice cream and chocolate sauce. A dramatic Lal Qila dessert experience.",
            urDesc = "گرم فیج براؤنی سزلنگ پلیٹ پر ونیلا آئس کریم اور چاکلیٹ ساس کے ساتھ۔",
            enSteps = listOf(
                "Bake rich chocolate brownie.",
                "Heat sizzler plate until smoking.",
                "Place brownie on hot plate.",
                "Top with ice cream and chocolate sauce.",
                "Serve immediately — listen for the sizzle!"
            ),
            urSteps = listOf(
                "غنی چاکلیٹ براؤنی پکائیں۔",
                "سزلر پلیٹ دھوئیں تک گرم کریں۔",
                "براؤنی گرم پلیٹ پر رکھیں۔",
                "آئس کریم اور چاکلیٹ ساس اوپر۔",
                "فوراً پیش کریں — سزل کی آواز سنیں!"
            ),
            enTips = listOf("Order after main course.", "Share between two."),
            urTips = listOf("کھانے کے بعد آرڈر کریں۔", "دو لوگوں میں شیئر کریں۔")
        ),
        special(
            id = "kunafa", illustrationRes = R.drawable.pic_kunafa,
            enName = "Kunafa", urName = "کنفی",
            enCat = "Chef Special", urCat = "شیف کی خاص ڈش",
            enSummary = "Crispy shredded pastry with sweet cheese and syrup.",
            urSummary = "میٹے پنیر اور شربت والی کرسپی کنفی۔",
            enDesc = "Middle Eastern kunafa with crispy kataifi threads, melted cheese, and rose-scented syrup. A Lal Qila Ramadan and special occasion dessert.",
            urDesc = "کریسپی کٹائیفی، پگھلا پنیر، گلاب کی شربت۔ لال قلعہ رمضان اور خاص مواقع کا میٹھا۔",
            enSteps = listOf(
                "Layer buttered kataifi in pan.",
                "Add sweet cheese filling.",
                "Top with more kataifi and press.",
                "Bake until golden and crispy.",
                "Pour warm syrup and garnish with pistachios."
            ),
            urSteps = listOf(
                "مکھن لگی کٹائیفی پرت لگائیں۔",
                "میٹا پنیر بھرتہ ڈالیں۔",
                "اوپر کٹائیفی دبائیں۔",
                "سنہری کرسپی پکائیں۔",
                "گرم شربت اور پستے۔"
            ),
            enTips = listOf("Best served warm.", "Available on weekends and Ramadan."),
            urTips = listOf("گرم بہترین۔", "ہفتے کے آخر اور رمضان میں۔")
        )
    )

    private fun special(
        id: String, illustrationRes: Int,
        enName: String, urName: String, enCat: String, urCat: String,
        enSummary: String, urSummary: String, enDesc: String, urDesc: String,
        enSteps: List<String>, urSteps: List<String>,
        enTips: List<String>, urTips: List<String>
    ): Posture = Posture(
        id = id,
        difficulty = Difficulty.ADVANCED,
        illustrationRes = illustrationRes,
        categoryId = PostureRepository.CAT_SPECIAL,
        english = LocalizedContent(enName, enCat, enSummary, enDesc, enSteps, enTips),
        urdu = LocalizedContent(urName, urCat, urSummary, urDesc, urSteps, urTips),
        isImagination = true
    )
}
