package com.couplesguide.postures.data

import com.couplesguide.postures.R

object GuideRepository {

    fun getChapters(): List<GuideChapter> = chapters

    fun getChapterById(id: String): GuideChapter? =
        chapters.find { it.id == id } ?: GenderEducationRepository.getChapterById(id)

    private val chapters = listOf(
        GuideChapter(
            id = "about_lal_qila",
            illustrationRes = R.drawable.pic_chapter_consent,
            english = ChapterContent(
                title = "About Lal Qila Restaurant",
                summary = "Karachi's legendary buffet destination since decades.",
                body = "Lal Qila Restaurant is one of Pakistan's most celebrated dining destinations, " +
                    "famous for its lavish all-you-can-eat buffet featuring Pakistani, BBQ, Chinese, " +
                    "Continental, and dessert stations. This app brings you the complete recipe collection " +
                    "with pictures, Urdu voice narration, and printable PDF export.",
                keyPoints = listOf(
                    "Multiple live cooking stations",
                    "Over 100 dishes daily",
                    "Famous for biryani and karahi",
                    "Family-friendly dining experience"
                )
            ),
            urdu = ChapterContent(
                title = "لال قلعہ ریسٹورنٹ کے بارے میں",
                summary = "دہائیوں سے کراچی کا مشہور بوفے مقام۔",
                body = "لال قلعہ ریسٹورنٹ پاکستان کے مشہور ترین کھانے کے مقامات میں سے ایک ہے، " +
                    "جہاں پاکستانی، باربی کیو، چائنیز، کونٹینینٹل اور میٹھے کے سٹیشنز پر لامحدود بوفے ملتا ہے۔ " +
                    "یہ ایپ مکمل ترکیبیں، تصاویر، اردو آواز اور PDF برآمد کے ساتھ پیش کرتی ہے۔",
                keyPoints = listOf(
                    "متعدد لائیو پکانے کے سٹیشنز",
                    "روزانہ 100 سے زیادہ ڈشیں",
                    "بریانی اور کڑاہی کے لیے مشہور",
                    "خاندانی ماحول"
                )
            )
        ),
        GuideChapter(
            id = "buffet_experience",
            illustrationRes = R.drawable.pic_chapter_connection,
            english = ChapterContent(
                title = "The Lal Qila Buffet Experience",
                summary = "How to make the most of your visit.",
                body = "A Lal Qila buffet is a journey through flavors. Start with soups and salads, " +
                    "move to Pakistani mains and live BBQ, explore Chinese and Continental stations, " +
                    "and finish with the legendary dessert counter. Pace yourself and try a little of everything.",
                keyPoints = listOf(
                    "Start light with salads and soups",
                    "Visit live BBQ station while hot",
                    "Save room for desserts",
                    "Try the chef's specials first"
                )
            ),
            urdu = ChapterContent(
                title = "لال قلعہ بوفے کا تجربہ",
                summary = "اپنی زیارت سے زیادہ سے زیادہ فائدہ کیسے اٹھائیں۔",
                body = "لال قلعہ بوفے ذائقوں کا سفر ہے۔ سوپ اور سلاد سے شروع کریں، " +
                    "پاکستانی کھانوں اور لائیو باربی کیو پر جائیں، چائنیز اور کونٹینینٹل آزمائیں، " +
                    "اور میٹھے کے کاؤنٹر پر ختم کریں۔ آہستہ چلیں اور ہر چیز تھوڑی آزمائیں۔",
                keyPoints = listOf(
                    "سلاد اور سوپ سے ہلکا آغاز",
                    "گرم باربی کیو سٹیشن پر جائیں",
                    "میٹھے کے لیے جگہ رکھیں",
                    "پہلے شیف سپیشل آزمائیں"
                )
            )
        ),
        GuideChapter(
            id = "buffet_stations",
            illustrationRes = R.drawable.pic_chapter_comfort,
            english = ChapterContent(
                title = "Buffet Stations Guide",
                summary = "Navigate every station like a pro.",
                body = "Lal Qila's buffet is organized into themed stations: Pakistani (biryani, karahi, nihari), " +
                    "Live BBQ (seekh kebab, tikka, malai boti), Chinese (fried rice, chow mein, Manchurian), " +
                    "Continental (grilled chicken, pasta, steak), Salad Bar, Tandoor Breads, Desserts, and Beverages.",
                keyPoints = listOf(
                    "Pakistani station — heart of the buffet",
                    "BBQ station — best when freshly grilled",
                    "Chinese counter — wok-fresh dishes",
                    "Dessert station — don't miss gulab jamun"
                )
            ),
            urdu = ChapterContent(
                title = "بوفے سٹیشنز کی رہنمائی",
                summary = "ہر سٹیشن ماہر کی طرح نیویگیٹ کریں۔",
                body = "لال قلعہ بوفے تھیم سٹیشنز میں منظم ہے: پاکستانی (بریانی، کڑاہی، نہاری)، " +
                    "لائیو باربی کیو (سیخ کباب، تکہ، ملائی بوٹی)، چائنیز (فرائیڈ رائس، چاؤ مین)، " +
                    "کونٹینینٹل، سلاد بار، تندور روٹیاں، میٹھا اور مشروبات۔",
                keyPoints = listOf(
                    "پاکستانی سٹیشن — بوفے کا دل",
                    "باربی کیو — تازہ گرل پر بہترین",
                    "چائنیز — ووک تازہ ڈشیں",
                    "میٹھا — گلاب جامن ضرور لیں"
                )
            )
        ),
        GuideChapter(
            id = "dining_tips",
            illustrationRes = R.drawable.pic_chapter_explore,
            english = ChapterContent(
                title = "Dining Tips & Etiquette",
                summary = "Buffet manners and smart choices.",
                body = "Use a clean plate for each round. Take small portions to taste more dishes. " +
                    "Don't waste food — you can always return for seconds. Compliment the live BBQ chef. " +
                    "Share your favorite dishes with family. And remember: the biryani line moves fast on weekends!",
                keyPoints = listOf(
                    "Small portions, multiple rounds",
                    "Fresh plate each visit to station",
                    "Weekend? Arrive early for best selection",
                    "Export recipes as PDF for home cooking"
                )
            ),
            urdu = ChapterContent(
                title = "کھانے کے مشورے اور آداب",
                summary = "بوفے کے آداب اور ہوشیار انتخاب۔",
                body = "ہر راؤنڈ میں صاف پلیٹ استعمال کریں۔ چھوٹے حصے لیں تاکہ زیادہ ڈشیں چکھیں۔ " +
                    "کھانا ضائع نہ کریں — دوبارہ آ سکتے ہیں۔ لائیو باربی کیو شیف کی تعریف کریں۔ " +
                    "خاندان کے ساتھ پسندیدہ ڈشیں شیئر کریں۔ ہفتے کے آخر میں بریانی کی لائن تیز چلتی ہے!",
                keyPoints = listOf(
                    "چھوٹے حصے، کئی راؤنڈ",
                    "ہر سٹیشن پر تازہ پلیٹ",
                    "ہفتے کے آخر؟ جلدی آئیں",
                    "گھر پکانے کے لیے PDF برآمد کریں"
                )
            )
        )
    )
}
