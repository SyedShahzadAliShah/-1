package com.couplesguide.postures.data

import com.couplesguide.postures.R

object BuffetGuideRepository {

    fun getChapters(): List<GuideChapter> = chapters

    fun getChapterById(id: String): GuideChapter? = chapters.find { it.id == id }

    private val chapters = listOf(
        chapter(
            id = "buffet_culture",
            illustrationRes = R.drawable.pic_chapter_buffet_culture,
            enTitle = "Karachi Buffet Culture",
            urTitle = "کراچی بوفے کی ثقافت",
            enSummary = "Why buffets are central to Karachi dining.",
            urSummary = "کراچی میں بوفے کھانے کی اہمیت۔",
            enBody = "Karachi is Pakistan's food capital. From Burns Road to Clifton, weekend family buffets and wedding feasts feature biryani, karahi, BBQ, and mithai in generous spreads. Understanding local favorites helps you plan an authentic home buffet.",
            urBody = "کراچی پاکستان کا فوڈ ہب ہے۔ برنز روڈ سے کلِفٹن تک، ہفتہ وار خاندانی بوفے اور شادیوں کے دعووں میں بریانی، کڑاہی، باربی کیو اور مٹھائی وافر مقدار میں پیش کی جاتی ہے۔ مقامی پسندیدہ کھانوں کو سمجھنا گھر کے بوفے کی منصوبہ بندی میں مدد دیتا ہے۔",
            enPoints = listOf(
                "Karachi buffets usually open with appetizers and raita.",
                "Biryani and karahi are the star mains at most events.",
                "BBQ stations are popular at evening buffets.",
                "Desserts like kheer, gulab jamun, and zarda close the meal."
            ),
            urPoints = listOf(
                "کراچی کے بوفے عام طور پر اپیٹائزر اور رائتے سے شروع ہوتے ہیں۔",
                "بریانی اور کڑاہی زیادہ تر تقریبات میں مرکزی ڈش ہوتی ہیں۔",
                "شام کے بوفے میں باربی کیو اسٹیشن مقبول ہیں۔",
                "کھیر، گلاب جامن اور زردہ کھانے کا اختتام کرتے ہیں۔"
            )
        ),
        chapter(
            id = "buffet_planning",
            illustrationRes = R.drawable.pic_chapter_planning,
            enTitle = "Planning a Home Buffet",
            urTitle = "گھر کا بوفے منصوبہ بندی",
            enSummary = "Portions, timing, and menu balance for 10–50 guests.",
            urSummary = "۱۰ سے ۵۰ مہمانوں کے لیے مقدار، وقت اور مینو کا توازن۔",
            enBody = "A successful Karachi-style buffet balances rice dishes, gravies, BBQ, bread, salads, and desserts. Cook heavy items like biryani and haleem ahead; finish karahi and BBQ fresh. Allow 250–350 g cooked food per adult.",
            urBody = "کامیاب کراچی انداز کا بوفے چاول کی ڈشز، سالن، باربی کیو، روٹی، سلاد اور میٹھے کا توازن رکھتا ہے۔ بریانی اور حلیم جیسی بھاری ڈشز پہلے پکائیں؛ کڑاہی اور باربی کیو تازہ مکمل کریں۔ ہر بالغ کے لیے ۲۵۰ سے ۳۵۰ گرام پکا کھانا رکھیں۔",
            enPoints = listOf(
                "Plan 2 rice dishes, 2 curries, 1 BBQ item, and 2 desserts minimum.",
                "Prepare chutneys, raita, and salad one day ahead.",
                "Use chafing dishes or insulated pots to keep food hot.",
                "Label dishes in Urdu and English for mixed guest groups."
            ),
            urPoints = listOf(
                "کم از کم ۲ چاول کی ڈشز، ۲ سالن، ۱ باربی کیو اور ۲ میٹھے رکھیں۔",
                "چٹنیاں، رائتہ اور سلاد ایک دن پہلے تیار کریں۔",
                "کھانا گرم رکھنے کے لیے چافنگ ڈش یا تھرمس استعمال کریں۔",
                "مخلوط مہمانوں کے لیے اردو اور انگریزی میں لیبل لگائیں۔"
            )
        ),
        chapter(
            id = "serving_order",
            illustrationRes = R.drawable.pic_chapter_timing,
            enTitle = "Serving Order & Timing",
            urTitle = "پیش کرنے کا ترتیب اور وقت",
            enSummary = "When to serve each course at a Karachi buffet.",
            urSummary = "کراچی بوفے میں ہر کورس کب پیش کریں۔",
            enBody = "Serve cold starters first, then hot appetizers. Place biryani and pulao at the center. Karahi and nihari go out 15 minutes before guests sit. BBQ should be grilled live or replenished every 20 minutes. Desserts stay refrigerated until the main course winds down.",
            urBody = "پہلے ٹھنڈے اسٹارٹر، پھر گرم اپیٹائزر پیش کریں۔ بریانی اور پلاؤ مرکز میں رکھیں۔ کڑاہی اور نہاری مہمانوں کے بیٹھنے سے ۱۵ منٹ پہلے نکالیں۔ باربی کیو لائیو یا ہر ۲۰ منٹ میں تازہ کریں۔ میٹھا مین کورس ختم ہونے تک فریج میں رکھیں۔",
            enPoints = listOf(
                "Raita and salad: serve throughout the buffet.",
                "Biryani: replenish every 30 minutes for best texture.",
                "Karahi: cook in batches — do not leave on heat too long.",
                "Tea and doodh patti after desserts for an authentic finish."
            ),
            urPoints = listOf(
                "رائتہ اور سلاد: پورے بوفے میں دستیاب رکھیں۔",
                "بریانی: بہترین ٹیکسچر کے لیے ہر ۳۰ منٹ میں تازہ کریں۔",
                "کڑاہی: بیچ میں پکائیں — زیادہ دیر گرم نہ رکھیں۔",
                "میٹھے کے بعد چائے اور دودھ پتی اصلی اختتام کے لیے۔"
            )
        ),
        chapter(
            id = "food_safety",
            illustrationRes = R.drawable.pic_chapter_safety,
            enTitle = "Food Safety & Hygiene",
            urTitle = "خوراک کی حفاظت اور صفائی",
            enSummary = "Keep buffet food safe in Karachi's warm climate.",
            urSummary = "کراچی کی گرمی میں بوفے کا کھانا محفوظ رکھیں۔",
            enBody = "Karachi summers demand extra care. Keep hot food above 60°C and cold items below 5°C. Use separate utensils for each dish. Cover food between services. Discard anything left at room temperature for more than two hours.",
            urBody = "کراچی کی گرمی میں اضافی احتیاط ضروری ہے۔ گرم کھانا ۶۰ ڈگری سے اوپر اور ٹھنڈا ۵ ڈگری سے نیچے رکھیں۔ ہر ڈش کے لیے الگ برتن استعمال کریں۔ کھانا ڈھانپ کر رکھیں۔ دو گھنٹے سے زیادہ کمرے کے درجہ حرارت پر رہنے والا کھانا ضائع کر دیں۔",
            enPoints = listOf(
                "Wash hands before handling buffet food.",
                "Use fresh oil for frying; never reuse heavily smoked oil.",
                "Store raw meat separately from cooked dishes.",
                "Provide hand sanitizer near the buffet line."
            ),
            urPoints = listOf(
                "بوفے کا کھانا چھونے سے پہلے ہاتھ دھوئیں۔",
                "تلی کے لیے تازہ تیل استعمال کریں؛ جلا ہوا تیل دوبارہ نہ استعمال کریں۔",
                "کچا گوشت پکی ڈشز سے الگ رکھیں۔",
                "بوفے لائن کے پاس ہینڈ سینیٹائزر رکھیں۔"
            )
        )
    )

    private fun chapter(
        id: String,
        illustrationRes: Int,
        enTitle: String,
        urTitle: String,
        enSummary: String,
        urSummary: String,
        enBody: String,
        urBody: String,
        enPoints: List<String>,
        urPoints: List<String>
    ) = GuideChapter(
        id = id,
        illustrationRes = illustrationRes,
        english = ChapterContent(enTitle, enSummary, enBody, enPoints),
        urdu = ChapterContent(urTitle, urSummary, urBody, urPoints)
    )
}
