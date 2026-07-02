package com.couplesguide.postures.data

import com.couplesguide.postures.R

object GenderEducationRepository {

    fun getForHimChapters(): List<GuideChapter> = forHimChapters

    fun getForHerChapters(): List<GuideChapter> = forHerChapters

    fun getChapterById(id: String): GuideChapter? =
        forHimChapters.find { it.id == id } ?: forHerChapters.find { it.id == id }

    private val forHimChapters = listOf(
        GuideChapter(
            id = "him_arousal",
            illustrationRes = R.drawable.pic_edu_body_map,
            english = ChapterContent(
                title = "Understanding Male Arousal",
                summary = "How arousal works and what helps you stay present.",
                body = "Male arousal involves physical stimulation, mental focus, and emotional connection. " +
                    "Erections can vary with stress, fatigue, alcohol, and mood — this is normal. " +
                    "Rushing or performance pressure often reduces pleasure for both partners. " +
                    "Slow down, breathe, and focus on sensation rather than outcome.",
                keyPoints = listOf(
                    "Arousal builds gradually — foreplay matters for men too",
                    "Stress and fatigue affect erections — be patient with yourself",
                    "Communication reduces performance anxiety",
                    "Pleasure is not only about penetration"
                )
            ),
            urdu = ChapterContent(
                title = "مردانہ جوش کو سمجھنا",
                summary = "جوش کیسے بڑھتا ہے اور موجود رہنے میں کیا مدد کرتا ہے۔",
                body = "مردانہ جوش جسمانی محرک، ذہنی توجہ اور جذباتی تعلق سے جڑا ہے۔ " +
                    "تناؤ، تھکاوٹ، شراب اور موڈ سے تبدیلی آ سکتی ہے — یہ عام ہے۔ " +
                    "جلدی یا کارکردگی کا دباؤ دونوں کے لیے لطف کم کرتا ہے۔ " +
                    "آہستہ چلیں، سانس لیں، اور نتیجے کی بجائے احساس پر توجہ دیں۔",
                keyPoints = listOf(
                    "جوش آہستہ بڑھتا ہے — پیش بازی مردوں کے لیے بھی اہم ہے",
                    "تناؤ اور تھکاوٹ اثر ڈالتے ہیں — اپنے ساتھ صبر کریں",
                    "بات چیت کارکردگی کے خوف کو کم کرتی ہے",
                    "لطف صرف داخلہ تک محدود نہیں"
                )
            )
        ),
        GuideChapter(
            id = "him_pleasure",
            illustrationRes = R.drawable.pic_chapter_connection,
            english = ChapterContent(
                title = "Pleasuring Your Partner",
                summary = "Techniques and mindset for giving pleasure.",
                body = "Focus on your partner's responses — breathing, sounds, and body movement tell you what feels good. " +
                    "Use your hands, mouth, and words before and during intercourse. " +
                    "Ask \"Does this feel good?\" and adjust based on her answers. " +
                    "Her pleasure often deepens intimacy and makes the experience better for both of you.",
                keyPoints = listOf(
                    "Watch and listen to her body's signals",
                    "Combine touch, kissing, and verbal affection",
                    "Clitoral stimulation often enhances pleasure",
                    "Ask rather than assume what she enjoys"
                )
            ),
            urdu = ChapterContent(
                title = "ساتھی کو لطف دینا",
                summary = "لطف دینے کی تکنیک اور سوچ۔",
                body = "ساتھی کے ردعمل پر توجہ دیں — سانس، آوازیں اور جسم کی حرکت بتاتی ہیں کیا اچھا لگ رہا ہے۔ " +
                    "داخلہ سے پہلے اور دوران ہاتھ، منہ اور الفاظ استعمال کریں۔ " +
                    "\"کیا اچھا لگ رہا ہے؟\" پوچھیں اور جواب کے مطابق ایڈجسٹ کریں۔ " +
                    "اس کا لطف قربت گہرا کرتا ہے اور تجربہ دونوں کے لیے بہتر بناتا ہے۔",
                keyPoints = listOf(
                    "اس کے جسم کے اشارے دیکھیں اور سنیں",
                    "چھونا، بوسہ اور محبت بھری باتیں ملائیں",
                    "کلائیٹورل محرک اکثر لطف بڑھاتا ہے",
                    "اندازہ نہ لگائیں — پوچھیں کیا پسند ہے"
                )
            )
        ),
        GuideChapter(
            id = "him_stamina",
            illustrationRes = R.drawable.pic_chapter_comfort,
            english = ChapterContent(
                title = "Stamina & Pacing",
                summary = "Lasting longer without rushing or forcing control.",
                body = "Pacing is more effective than trying to \"last\" at all costs. " +
                    "Pause, switch positions, or focus on non-penetrative pleasure when you feel close. " +
                    "Deep breathing and relaxing pelvic muscles help delay climax naturally. " +
                    "Remember: intimacy is a shared journey, not a race.",
                keyPoints = listOf(
                    "Slow down or pause when intensity rises",
                    "Change positions to reset sensation",
                    "Breathe deeply and relax — tension speeds climax",
                    "Mutual pleasure matters more than duration"
                )
            ),
            urdu = ChapterContent(
                title = "برداشت اور رفتار",
                summary = "بغیر جلدی یا زبردستی کنٹرول کے زیادہ دیر تک۔",
                body = "رفتار طے کرنا \"زیادہ دیر\" کے زبردستی کوشش سے بہتر ہے۔ " +
                    "جب قریب محسوس ہو تو رکیں، پوزیشن بدلیں، یا غیر داخلہ لطف پر توجہ دیں۔ " +
                    "گہری سانس اور پیلویک پٹھوں کو آرام دہ رکھنا قدرتی طور پر تاخیر میں مدد کرتا ہے۔ " +
                    "یاد رکھیں: قربت مشترکہ سفر ہے، مقابلہ نہیں۔",
                keyPoints = listOf(
                    "شدت بڑھے تو آہستہ چلیں یا رک جائیں",
                    "احساس ری سیٹ کرنے کے لیے پوزیشن بدلیں",
                    "گہری سانس لیں — تناؤ جلدی ختم کرتا ہے",
                    "دیر سے زیادہ باہمی لطف اہم ہے"
                )
            )
        ),
        GuideChapter(
            id = "him_confidence",
            illustrationRes = R.drawable.pic_chapter_explore,
            english = ChapterContent(
                title = "Body Confidence for Men",
                summary = "Feeling comfortable in your own skin.",
                body = "Every man's body is different — size, shape, and stamina vary widely and are rarely the main factor in partner satisfaction. " +
                    "Confidence comes from attentiveness, respect, and willingness to learn. " +
                    "Talk openly about insecurities if they arise; vulnerability often strengthens connection.",
                keyPoints = listOf(
                    "Partner satisfaction comes from connection, not anatomy alone",
                    "Insecurities are normal — discuss them honestly",
                    "Focus on what you can give, not what you lack",
                    "Practice and communication improve over time"
                )
            ),
            urdu = ChapterContent(
                title = "مردوں کے لیے جسمانی اعتماد",
                summary = "اپنے جسم میں آرام دہ محسوس کرنا۔",
                body = "ہر مرد کا جسم مختلف ہے — سائز، شکل اور برداشت میں فرق عام ہے اور شریک کی اطمینان کا بنیادی سبب شاذ و نادر ہی ہوتا ہے۔ " +
                    "اعتماد توجہ، احترام اور سیکھنے کی خواہش سے آتا ہے۔ " +
                    "کمزوریوں پر کھل کر بات کریں — نازک پن اکثر تعلق مضبوط کرتا ہے۔",
                keyPoints = listOf(
                    "اطمینان تعلق سے آتا ہے، صرف جسمانی ساخت سے نہیں",
                    "کمزوریاں عام ہیں — ایمانداری سے بات کریں",
                    "جو دے سکتے ہیں اس پر توجہ دیں",
                    "مشق اور بات چیت سے بہتری آتی ہے"
                )
            )
        )
    )

    private val forHerChapters = listOf(
        GuideChapter(
            id = "her_arousal",
            illustrationRes = R.drawable.pic_edu_body_map,
            english = ChapterContent(
                title = "Understanding Female Arousal",
                summary = "How desire builds and why patience matters.",
                body = "Female arousal often takes longer to build than male arousal and benefits greatly from foreplay. " +
                    "Mental and emotional readiness are as important as physical touch. " +
                    "Lubrication varies — using lubricant is normal and helpful. " +
                    "There is no fixed timeline; your body sets its own pace.",
                keyPoints = listOf(
                    "Desire builds gradually — allow time for foreplay",
                    "Emotional safety enhances physical arousal",
                    "Lubricant is helpful and completely normal",
                    "Every woman's response pattern is unique"
                )
            ),
            urdu = ChapterContent(
                title = "زنانہ جوش کو سمجھنا",
                summary = "خواہش کیسے بڑھتی ہے اور صبر کیوں ضروری ہے۔",
                body = "زنانہ جوش اکثر مردانہ سے آہستہ بڑھتا ہے اور پیش بازی سے بہت فائدہ ہوتا ہے۔ " +
                    "ذہنی اور جذباتی تیاری جسمانی چھونے جتنی اہم ہے۔ " +
                    "نمی میں فرق آتا ہے — لوبریکنٹ عام اور مفید ہے۔ " +
                    "کوئی مقررہ وقت نہیں؛ آپ کا جسم اپنی رفتار طے کرتا ہے۔",
                keyPoints = listOf(
                    "خواہش آہستہ بڑھتی ہے — پیش بازی کا وقت دیں",
                    "جذباتی محفوظیت جسمانی جوش بڑھاتی ہے",
                    "لوبریکنٹ مفید اور بالکل عام ہے",
                    "ہر عورت کا ردعمل مختلف ہے"
                )
            )
        ),
        GuideChapter(
            id = "her_pleasure",
            illustrationRes = R.drawable.pic_chapter_connection,
            english = ChapterContent(
                title = "Finding Your Pleasure",
                summary = "Knowing your body and communicating desires.",
                body = "Understanding what feels good for you is an ongoing process of self-discovery. " +
                    "The clitoris has many nerve endings and external stimulation often plays a key role in orgasm. " +
                    "Guide your partner's hands or suggest positions that give you the angle you need. " +
                    "There is no shame in asking for what you want.",
                keyPoints = listOf(
                    "Explore your own body to learn what you enjoy",
                    "External stimulation is important for many women",
                    "Verbally guide your partner during intimacy",
                    "Orgasm is not required for a fulfilling experience"
                )
            ),
            urdu = ChapterContent(
                title = "اپنا لطف تلاش کرنا",
                summary = "اپنے جسم کو جاننا اور خواہشات بتانا۔",
                body = "آپ کے لیے کیا اچھا لگتا ہے یہ خود دریافت کا مسلسل عمل ہے۔ " +
                    "کلائیٹورس میں بہت اعصاب ہیں اور بیرونی محرک اکثر اختتام میں اہم کردار ادا کرتا ہے۔ " +
                    "ساتھی کے ہاتھ رہنمائی کریں یا وہ پوزیشنز تجویز کریں جو آپ کو درکار زاویہ دیں۔ " +
                    "جو چاہیں مانگنے میں کوئی شرم نہیں۔",
                keyPoints = listOf(
                    "اپنے جسم کو سمجھنے کے لیے دریافت کریں",
                    "بیرونی محرک بہت سی عورتوں کے لیے اہم ہے",
                    "قربت کے دوران زبانی رہنمائی کریں",
                    "مکمل تجربے کے لیے اختتام ضروری نہیں"
                )
            )
        ),
        GuideChapter(
            id = "her_comfort",
            illustrationRes = R.drawable.pic_edu_hip_pillow,
            english = ChapterContent(
                title = "Comfort & Pain Prevention",
                summary = "Staying comfortable during and after intimacy.",
                body = "Pain during sex is not normal and should never be ignored. " +
                    "Use pillows to support your hips, knees, and lower back in any position. " +
                    "Lubricant reduces friction and prevents soreness. " +
                    "If something hurts, say so immediately — your comfort is essential.",
                keyPoints = listOf(
                    "Pain is a signal to stop or adjust — never push through",
                    "Pillows improve alignment in most positions",
                    "Empty bladder before intimacy to reduce pressure",
                    "Gentle positions like spooning are great starting points"
                )
            ),
            urdu = ChapterContent(
                title = "آرام اور درد سے بچاؤ",
                summary = "قربت کے دوران اور بعد میں آرام دہ رہنا۔",
                body = "جنسی تعلق میں درد عام نہیں اور نظرانداز نہیں کرنا چاہیے۔ " +
                    "کسی بھی پوزیشن میں کولہے، گھٹنوں اور کمر کے لیے تکیے استعمال کریں۔ " +
                    "لوبریکنٹ رگڑ کم کر کے دکھ کم کرتا ہے۔ " +
                    "اگر کچھ تکلیف دے تو فوراً بتائیں — آپ کا آرام ضروری ہے۔",
                keyPoints = listOf(
                    "درد رکنے یا بدلنے کا اشارہ ہے — برداشت نہ کریں",
                    "تکیے زیادہ تر پوزیشنز میں ہم آہنگی بہتر بناتے ہیں",
                    "قبل از قربت مثانہ خالی کریں دباؤ کم کرنے کے لیے",
                    "چمچے جیسی نرم پوزیشنز شروعات کے لیے بہترین"
                )
            )
        ),
        GuideChapter(
            id = "her_confidence",
            illustrationRes = R.drawable.pic_chapter_explore,
            english = ChapterContent(
                title = "Body Confidence for Women",
                summary = "Embracing your body and owning your desires.",
                body = "Societal pressure can make women feel self-conscious about their bodies during intimacy. " +
                    "Your partner chose to be with you — attraction is emotional as well as physical. " +
                    "Lighting, positions, and clothing (or lack thereof) can all be adjusted to help you feel at ease. " +
                    "Confidence grows when you communicate openly about what makes you comfortable.",
                keyPoints = listOf(
                    "Your partner values you beyond appearance",
                    "Dim lighting or covered positions can ease anxiety",
                    "Desire and initiation are equally valid from women",
                    "Open communication builds lasting confidence"
                )
            ),
            urdu = ChapterContent(
                title = "عورتوں کے لیے جسمانی اعتماد",
                summary = "اپنے جسم کو قبول کرنا اور اپنی خواہشات کا مالک بننا۔",
                body = "معاشرتی دباؤ عورتوں کو قربت میں اپنے جسم کے بارے میں خود آگاہ محسوس کرا سکتا ہے۔ " +
                    "آپ کا ساتھی آپ کے ساتھ رہنے کا انتخاب کر چکا — کشش جذباتی بھی ہے جسمانی بھی۔ " +
                    "روشنی، پوزیشنز اور لباس سب ایڈجسٹ ہو سکتے ہیں تاکہ آپ آرام محسوس کریں۔ " +
                    "کھل کر بات کرنے سے اعتماد بڑھتا ہے کہ کیا آپ کو آرام دہ لگتا ہے۔",
                keyPoints = listOf(
                    "آپ کا ساتھی صرف ظاہر سے زیادہ آپ کو قدر دیتا ہے",
                    "مدھم روشنی یا ڈھکی پوزیشنز بے چینی کم کر سکتی ہیں",
                    "خواہش اور شروعات عورتوں کی طرف سے بھی درست ہے",
                    "کھلی بات چیت پائیدار اعتماد بناتی ہے"
                )
            )
        )
    )
}
