package com.couplesguide.postures.data

import com.couplesguide.postures.R

object GenderEducationRepository {

    fun getForHimChapters(): List<GuideChapter> = stationGuidesPart1

    fun getForHerChapters(): List<GuideChapter> = stationGuidesPart2

    fun getChapterById(id: String): GuideChapter? =
        (stationGuidesPart1 + stationGuidesPart2).find { it.id == id }

    private val stationGuidesPart1 = listOf(
        GuideChapter(
            id = "bbq_station",
            illustrationRes = R.drawable.pic_edu_face_contact,
            english = ChapterContent(
                title = "Live BBQ Station",
                summary = "Charcoal-grilled perfection.",
                body = "The live BBQ station is Lal Qila's most popular corner. Watch chefs grill seekh kebab, " +
                    "chicken tikka, malai boti, and grilled fish over charcoal. Visit when coals are hottest " +
                    "for the best char and juiciness.",
                keyPoints = listOf(
                    "Best visited during peak dinner hours",
                    "Ask for extra mint chutney",
                    "Malai boti for mild spice lovers",
                    "Pair with fresh naan from tandoor"
                )
            ),
            urdu = ChapterContent(
                title = "لائیو باربی کیو سٹیشن",
                summary = "کوئلے پر گرل کی کمال۔",
                body = "لائیو باربی کیو سٹیشن لال قلعہ کا سب سے مقبول کونہ ہے۔ شیف کوئلے پر سیخ کباب، " +
                    "چکن تکہ، ملائی بوٹی اور مچھلی گرل کرتے ہیں۔ کوئلے سب سے گرم ہوں تو جائیں " +
                    "بہترین بھننے اور رسیلے پن کے لیے۔",
                keyPoints = listOf(
                    "رات کے کھانے کے اوقات میں بہترین",
                    "اضافی پودینے کی چٹنی مانگیں",
                    "کم تیکھے کے لیے ملائی بوٹی",
                    "تندور سے تازہ نان کے ساتھ"
                )
            )
        ),
        GuideChapter(
            id = "pakistani_station",
            illustrationRes = R.drawable.pic_edu_side_alignment,
            english = ChapterContent(
                title = "Pakistani Station",
                summary = "The soul of Lal Qila buffet.",
                body = "Biryani, karahi, nihari, handi, and haleem — the Pakistani station defines Lal Qila. " +
                    "The biryani pot is replenished constantly. Karahi is cooked to order in traditional woks. " +
                    "Nihari is a weekend breakfast specialty.",
                keyPoints = listOf(
                    "Biryani — arrive early on weekends",
                    "Karahi — ask for extra naan",
                    "Nihari — weekend mornings only",
                    "Haleem — Ramadan specialty"
                )
            ),
            urdu = ChapterContent(
                title = "پاکستانی سٹیشن",
                summary = "لال قلعہ بوفے کی روح۔",
                body = "بریانی، کڑاہی، نہاری، ہانڈی، حلیم — پاکستانی سٹیشن لال قلعہ کی پہچان ہے۔ " +
                    "بریانی کا برتن مسلسل بھرا جاتا ہے۔ کڑاہی روایتی کڑاہی میں آرڈر پر پکتی ہے۔ " +
                    "نہاری ہفتے کے آخر ناشتے کی خاصیت ہے۔",
                keyPoints = listOf(
                    "بریانی — ہفتے کے آخر جلدی آئیں",
                    "کڑاہی — اضافی نان مانگیں",
                    "نہاری — صرف ہفتے کے آخر صبح",
                    "حلیم — رمضان کی خاصیت"
                )
            )
        )
    )

    private val stationGuidesPart2 = listOf(
        GuideChapter(
            id = "chinese_station",
            illustrationRes = R.drawable.pic_edu_rear_safety,
            english = ChapterContent(
                title = "Chinese Station",
                summary = "Wok-tossed favorites.",
                body = "Lal Qila's Chinese counter serves fresh wok-fried rice, chow mein, Manchurian, " +
                    "and sweet & sour chicken. Dishes are replenished frequently — look for the steam rising " +
                    "from the wok for the freshest picks.",
                keyPoints = listOf(
                    "Fried rice pairs with Manchurian",
                    "Spring rolls as appetizer",
                    "Chow mein best when just tossed",
                    "Ask for chili sauce on the side"
                )
            ),
            urdu = ChapterContent(
                title = "چائنیز سٹیشن",
                summary = "ووک میں تلی پسندیدہ ڈشیں۔",
                body = "لال قلعہ چائنیز کاؤنٹر تازہ ووک فرائیڈ رائس، چاؤ مین، منچورین اور سویٹ ساؤر چکن پیش کرتا ہے۔ " +
                    "ڈشیں بار بار بھرتی ہیں — ووک سے اٹھتے دھوئیں والے تازہ ترین انتخاب ہیں۔",
                keyPoints = listOf(
                    "فرائیڈ رائس منچورین کے ساتھ",
                    "سپرنگ رول اپیٹائزر",
                    "چاؤ مین ابھی تلی ہوئی بہترین",
                    "چلی ساس الگ مانگیں"
                )
            )
        ),
        GuideChapter(
            id = "dessert_station",
            illustrationRes = R.drawable.pic_edu_hip_pillow,
            english = ChapterContent(
                title = "Dessert & Beverage Station",
                summary = "Sweet endings and refreshing drinks.",
                body = "End your Lal Qila feast at the dessert counter: gulab jamun, kheer, rasmalai, " +
                    "gajar halwa, and assorted ice cream. Wash it down with mint margarita, Kashmiri chai, " +
                    "or fresh fruit juice.",
                keyPoints = listOf(
                    "Gulab jamun — must try, served warm",
                    "Kheer — best chilled",
                    "Mint margarita cools spicy palates",
                    "Kashmiri chai — winter specialty"
                )
            ),
            urdu = ChapterContent(
                title = "میٹھا اور مشروبات سٹیشن",
                summary = "میٹا اختتام اور تروتازہ مشروبات۔",
                body = "لال قلعہ کا دعوا میٹھے کے کاؤنٹر پر ختم کریں: گلاب جامن، کھیر، رس ملائی، " +
                    "گاجر کا حلوہ، اور آئس کریم۔ پودینہ مارگیریٹا، کشمیری چائے، " +
                    "یا تازہ پھلوں کا جوس پیئیں۔",
                keyPoints = listOf(
                    "گلاب جامن — گرم ضرور چکھیں",
                    "کھیر — ٹھنڈی بہترین",
                    "پودینہ مارگیریٹا تیکھے منہ کو ٹھنڈا کرے",
                    "کشمیری چائے — سردیوں کی خاصیت"
                )
            )
        )
    )
}
