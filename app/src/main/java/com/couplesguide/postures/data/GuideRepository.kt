package com.couplesguide.postures.data

import com.couplesguide.postures.R

object GuideRepository {

    fun getChapters(): List<GuideChapter> = chapters

    fun getChapterById(id: String): GuideChapter? =
        chapters.find { it.id == id } ?: GenderEducationRepository.getChapterById(id)

    private val chapters = listOf(
        GuideChapter(
            id = "consent",
            illustrationRes = R.drawable.pic_chapter_consent,
            english = ChapterContent(
                title = "Communication & Consent",
                summary = "The foundation of every intimate experience.",
                body = "Before exploring any posture, establish open dialogue with your partner. " +
                    "Consent is ongoing — either partner can pause or stop at any time. " +
                    "Use simple phrases like \"Is this okay?\" or \"Would you like to try something different?\" " +
                    "Great intimacy begins with feeling heard, respected, and safe.",
                keyPoints = listOf(
                    "Ask before trying something new",
                    "Respect a pause or stop immediately",
                    "Discuss boundaries before and after intimacy",
                    "Non-verbal cues matter — check in often"
                )
            ),
            urdu = ChapterContent(
                title = "مواصلات اور رضامندی",
                summary = "ہر قریبی تجربے کی بنیاد۔",
                body = "کسی بھی پوزیشن کو آزمانے سے پہلے اپنے ساتھی سے کھل کر بات کریں۔ " +
                    "رضامندی مسلسل ہوتی ہے — کوئی بھی شریک کسی بھی وقت رک سکتا ہے۔ " +
                    "\"کیا یہ ٹھیک ہے؟\" یا \"کیا آپ کچھ مختلف آزمانا چاہیں گے؟\" جیسے جملے استعمال کریں۔ " +
                    "بہترین قربت اس وقت شروع ہوتی ہے جب آپ محفوظ اور قدر محسوس کریں۔",
                keyPoints = listOf(
                    "نیا کچھ آزمانے سے پہلے پوچھیں",
                    "رکنے کی درخواست کا فوری احترام کریں",
                    "حدود پر پہلے اور بعد میں بات کریں",
                    "غیر زبانی اشارے بھی اہم ہیں — بار بار پوچھتے رہیں"
                )
            )
        ),
        GuideChapter(
            id = "connection",
            illustrationRes = R.drawable.pic_chapter_connection,
            english = ChapterContent(
                title = "Building Connection",
                summary = "Emotional closeness enhances physical intimacy.",
                body = "Take time for eye contact, gentle touch, and unhurried foreplay. " +
                    "Rushing to intercourse often reduces pleasure for both partners. " +
                    "Kissing, massage, and whispered affection create arousal naturally. " +
                    "When you feel emotionally connected, physical positions become more enjoyable.",
                keyPoints = listOf(
                    "Don't rush — build anticipation together",
                    "Use touch, kiss, and words of affection",
                    "Match your partner's pace and energy",
                    "Eye contact deepens intimacy significantly"
                )
            ),
            urdu = ChapterContent(
                title = "تعلق کی تعمیر",
                summary = "جذباتی قربت جسمانی قربت کو بہتر بناتی ہے۔",
                body = "آنکھوں سے رابطے، نرم چھونے، اور بغیر جلدی کے پیش بازی کے لیے وقت نکالیں۔ " +
                    "جلدی میں جانے سے دونوں کے لیے لطف کم ہو سکتا ہے۔ " +
                    "بوسہ، مساج، اور محبت بھری باتیں قدرتی طور پر جوش بڑھاتی ہیں۔ " +
                    "جب جذباتی تعلق مضبوط ہو تو جسمانی پوزیشنز زیادہ لذیذ ہوتی ہیں۔",
                keyPoints = listOf(
                    "جلدی نہ کریں — ساتھ مل کر انتظار بڑھائیں",
                    "چھونے، بوسے اور محبت بھری باتیں استعمال کریں",
                    "ساتھی کی رفتار اور توانائی سے ہم آہنگ رہیں",
                    "آنکھوں کا رابطہ قربت کو گہرا کرتا ہے"
                )
            )
        ),
        GuideChapter(
            id = "comfort",
            illustrationRes = R.drawable.pic_chapter_comfort,
            english = ChapterContent(
                title = "Comfort & Safety",
                summary = "Physical comfort makes exploration enjoyable.",
                body = "Use pillows to support hips, knees, and lower back. " +
                    "Lubricant reduces friction and increases comfort. " +
                    "If a position causes pain, numbness, or strain — change immediately. " +
                    "Every body is different; adjust angles and depth to suit both partners.",
                keyPoints = listOf(
                    "Pillows and cushions improve most positions",
                    "Use lubricant when needed",
                    "Stop if anything feels painful or uncomfortable",
                    "Small adjustments often make a big difference"
                )
            ),
            urdu = ChapterContent(
                title = "آرام اور حفاظت",
                summary = "جسمانی آرام تجربے کو لذیذ بناتا ہے۔",
                body = "کولہے، گھٹنوں اور کمر کے لیے تکیے استعمال کریں۔ " +
                    "لوبریکنٹ رگڑ کم کر کے آرام بڑھاتا ہے۔ " +
                    "اگر کوئی پوزیشن درد، سن ہون یا تکلیف دے — فوراً بدلیں۔ " +
                    "ہر جسم مختلف ہے؛ زاویے اور گہرائی دونوں کے مطابق رکھیں۔",
                keyPoints = listOf(
                    "تکیے زیادہ تر پوزیشنز بہتر بناتے ہیں",
                    "ضرورت پر لوبریکنٹ استعمال کریں",
                    "درد یا بے آرامی محسوس ہو تو رک جائیں",
                    "چھوٹی تبدیلیاں بڑا فرق ڈالتی ہیں"
                )
            )
        ),
        GuideChapter(
            id = "exploration",
            illustrationRes = R.drawable.pic_chapter_explore,
            english = ChapterContent(
                title = "Exploring Together",
                summary = "Variety keeps intimacy fresh and exciting.",
                body = "Try one new posture at a time rather than many at once. " +
                    "Discuss what felt good afterward — this builds trust and knowledge. " +
                    "Some positions work better on certain days depending on mood, energy, and flexibility. " +
                    "There is no \"perfect\" position — only what works for you as a couple.",
                keyPoints = listOf(
                    "Try one new posture at a time",
                    "Talk about what you enjoyed afterward",
                    "Energy and mood change — adapt accordingly",
                    "Focus on pleasure, not performance"
                )
            ),
            urdu = ChapterContent(
                title = "ساتھ مل کر دریافت",
                summary = "تنوع قربت کو تازہ اور دلچسپ رکھتا ہے۔",
                body = "ایک وقت میں ایک نئی پوزیشن آزمائیں، بہت سی ایک ساتھ نہیں۔ " +
                    "بعد میں بات کریں کہ کیا اچھا لگا — اس سے اعتماد بڑھتا ہے۔ " +
                    "موڈ، توانائی اور لچک کے مطابق کچھ دن کچھ پوزیشنز بہتر ہوتی ہیں۔ " +
                    "کوئی \"کامل\" پوزیشن نہیں — صرف وہ جو آپ دونوں کے لیے ٹھیک ہو۔",
                keyPoints = listOf(
                    "ایک وقت میں ایک نئی پوزیشن آزمائیں",
                    "بعد میں لطف اندوز ہونے والی باتیں شیئر کریں",
                    "توانائی اور موڈ بدلتے ہیں — اس کے مطابق رہیں",
                    "کارکردگی نہیں، لطف پر توجہ دیں"
                )
            )
        )
    )
}
