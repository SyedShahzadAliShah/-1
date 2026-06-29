package com.couplesguide.postures.data

import com.couplesguide.postures.R

object PostureRepository {

    const val CAT_ALL = "all"
    const val CAT_FACE = "face_to_face"
    const val CAT_SIDE = "side_by_side"
    const val CAT_REAR = "rear_entry"
    const val CAT_STANDING = "standing_seated"
    const val CAT_VARIATIONS = "variations"

    fun getCategoryIds(): List<String> = listOf(
        CAT_ALL, CAT_FACE, CAT_SIDE, CAT_REAR, CAT_STANDING, CAT_VARIATIONS
    )

    fun getCategoryLabel(categoryId: String, language: String): String {
        val labels = categoryLabels[categoryId] ?: return categoryId
        return if (language == "ur") labels.second else labels.first
    }

    private val categoryLabels = mapOf(
        CAT_ALL to ("All" to "سب"),
        CAT_FACE to ("Face to Face" to "آمنے سامنے"),
        CAT_SIDE to ("Side by Side" to "ساتھ ساتھ"),
        CAT_REAR to ("Rear Entry" to "پیچھے سے"),
        CAT_STANDING to ("Standing & Seated" to "کھڑے اور بیٹھے"),
        CAT_VARIATIONS to ("Variations" to "تبدیلیاں")
    )

    private val postures: List<Posture> = listOf(
        posture(
            id = "missionary", categoryId = CAT_FACE, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.ill_missionary,
            enName = "Missionary", urName = "مشنری",
            enCat = "Face to Face", urCat = "آمنے سامنے",
            enSummary = "Classic face-to-face position with one partner on top.",
            urSummary = "کلاسک آمنے سامنے پوزیشن جس میں ایک ساتھی اوپر ہوتا ہے۔",
            enDesc = "One of the most common intimate positions. One partner lies on their back while the other lies on top, facing them. It allows eye contact, kissing, and easy communication.",
            urDesc = "سب سے عام قریبی پوزیشنز میں سے ایک۔ ایک ساتھی پیٹ کے بل لیٹتا ہے اور دوسرا اوپر آمنے سامنے ہوتا ہے۔ آنکھوں کا رابطہ، بوسہ اور آسان گفتگو ممکن ہے۔",
            enSteps = listOf(
                "One partner lies comfortably on their back with knees slightly bent.",
                "The other partner positions themselves on top, supporting weight on hands or forearms.",
                "Adjust hip height and leg placement until both feel comfortable.",
                "Move slowly at first and check in with each other."
            ),
            urSteps = listOf(
                "ایک ساتھی پیٹ کے بل آرام سے لیٹے، گھٹنے ہلکے موڑے ہوئے۔",
                "دوسرا ساتھی اوپر آئے، وزن ہاتھوں یا بازوؤں پر رکھے۔",
                "کولہے کی اونچائی اور ٹانگوں کی جگہ ایڈجسٹ کریں۔",
                "آہستہ شروع کریں اور ایک دوسرے سے پوچھتے رہیں۔"
            ),
            enTips = listOf(
                "Place a pillow under the lower back for better angle.",
                "Keep communication open — small adjustments help.",
                "Try varying depth and pace together."
            ),
            urTips = listOf(
                "کمر کے نیچے تکیہ رکھیں بہتر زاویے کے لیے۔",
                "بات چیت جاری رکھیں — چھوٹی تبدیلیاں مدد کرتی ہیں۔",
                "گہرائی اور رفتار ساتھ مل کر بدلیں۔"
            )
        ),
        posture(
            id = "cowgirl", categoryId = CAT_FACE, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.ill_cowgirl,
            enName = "Cowgirl (Woman on Top)", urName = "کاؤگرل (عورت اوپر)",
            enCat = "Face to Face", urCat = "آمنے سامنے",
            enSummary = "One partner straddles the other while facing them.",
            urSummary = "ایک ساتھی دوسرے کے اوپر آمنے سامنے بیٹھتا یا بیٹھتی ہے۔",
            enDesc = "The partner on top sits or kneels astride the other, facing them. This gives the top partner control over movement, depth, and pace.",
            urDesc = "اوپر والا ساتھی آمنے سامنے بیٹھ کر حرکت، گہرائی اور رفتار کنٹرول کرتا ہے۔",
            enSteps = listOf(
                "One partner lies on their back.",
                "The other kneels or sits astride their hips, facing them.",
                "Top partner braces hands on chest or thighs for balance.",
                "Rock hips gently to find a comfortable rhythm."
            ),
            urSteps = listOf(
                "ایک ساتھی پیٹ کے بل لیٹے۔",
                "دوسرا کولہوں پر آمنے سامنے بیٹھے یا گھٹنوں کے بل۔",
                "اوپر والا سینے یا رانوں پر ہاتھ رکھے توازن کے لیے۔",
                "کولہے آہستہ ہلائیں آرام دہ تال کے لیے۔"
            ),
            enTips = listOf(
                "The partner on top sets the pace — communicate openly.",
                "Lean forward for closeness or sit upright for a new angle.",
                "Use a wall or headboard for support if needed."
            ),
            urTips = listOf(
                "اوپر والا رفتار طے کرے — کھل کر بات کریں۔",
                "قربت کے لیے جھکیں یا سیدھے بیٹھیں نئے زاویے کے لیے۔",
                "ضرورت ہو تو دیوار یا سرے کی مدد لیں۔"
            )
        ),
        posture(
            id = "spooning", categoryId = CAT_SIDE, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.ill_spooning,
            enName = "Spooning", urName = "چمچے والی پوزیشن",
            enCat = "Side by Side", urCat = "ساتھ ساتھ",
            enSummary = "Both partners lie on their sides, nestled together.",
            urSummary = "دونوں ساتھی سیدھے لیٹ کر ایک دوسرے سے لپٹے ہوئے۔",
            enDesc = "Partners lie on their sides facing the same direction, like spoons. Gentle, intimate, and low-effort — ideal for relaxed moments.",
            urDesc = "دونوں ایک سمت دیکھتے ہوئے سیدھے لیٹتے ہیں، جیسے چمچے۔ نرم، قریبی اور آسان — آرام کے لیے بہترین۔",
            enSteps = listOf(
                "Both lie on their sides facing the same direction.",
                "The partner behind curls around the front partner.",
                "Front partner may bend knees slightly.",
                "Move together slowly and stay attuned to comfort."
            ),
            urSteps = listOf(
                "دونوں ایک سمت دیکھتے ہوئے سیدھے لیٹیں۔",
                "پیچھے والا ساتھی سامنے والے کے گرد لپٹے۔",
                "سامنے والا گھٹنے ہلکے موڑ سکتا ہے۔",
                "آہستہ ساتھ حرکت کریں اور آرام کا خیال رکھیں۔"
            ),
            enTips = listOf(
                "Place a pillow between knees for hip alignment.",
                "Great for morning intimacy or calm moments.",
                "Front partner can reach back to guide movement."
            ),
            urTips = listOf(
                "گھٹنوں کے درمیان تکیہ رکھیں۔",
                "صبح کی قربت یا پرسکون لمحات کے لیے بہترین۔",
                "سامنے والا پیچھے ہاتھ بڑھا کر رہنمائی کر سکتا ہے۔"
            )
        ),
        posture(
            id = "side_by_side", categoryId = CAT_SIDE, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.ill_side_by_side,
            enName = "Side by Side (Facing)", urName = "سامنے سامنے سیدھے",
            enCat = "Side by Side", urCat = "ساتھ ساتھ",
            enSummary = "Partners lie facing each other on their sides.",
            urSummary = "دونوں ساتھی سیدھے لیٹ کر آمنے سامنے۔",
            enDesc = "Both partners lie on their sides facing one another. Creates closeness and equal participation with less strain.",
            urDesc = "دونوں سیدھے لیٹ کر آمنے سامنے۔ قربت اور برابر شرکت، کم جسمانی دباؤ۔",
            enSteps = listOf(
                "Both lie on sides, facing each other.",
                "Intertwine legs — top leg over partner's hip works well.",
                "Stay close with arms around each other.",
                "Rock hips gently to find a shared rhythm."
            ),
            urSteps = listOf(
                "دونوں سیدھے آمنے سامنے لیٹیں۔",
                "ٹانگیں آپس میں ملائیں — اوپر والی ران پر رکھیں۔",
                "بازوؤں سے ایک دوسرے کو قریب رکھیں۔",
                "کولہے آہستہ ہلائیں مشترکہ تال کے لیے۔"
            ),
            enTips = listOf(
                "Excellent for eye contact and whispered conversation.",
                "Adjust leg intertwining to change sensation.",
                "Works well on a firm mattress or padded floor."
            ),
            urTips = listOf(
                "آنکھوں کے رابطے اور آہستہ بات کے لیے بہترین۔",
                "ٹانگوں کی گرفت بدل کر احساس تبدیل کریں۔",
                "سخت بستر یا فرش پر کمبل کے ساتھ اچھا کام کرتا ہے۔"
            )
        ),
        posture(
            id = "doggy", categoryId = CAT_REAR, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.ill_doggy,
            enName = "Rear Entry", urName = "پیچھے سے داخلہ",
            enCat = "Rear Entry", urCat = "پیچھے سے",
            enSummary = "One partner kneels while the other enters from behind.",
            urSummary = "ایک گھٹنوں کے بل، دوسرا پیچھے سے۔",
            enDesc = "One partner is on hands and knees while the other kneels or stands behind. Allows deeper penetration and a different angle.",
            urDesc = "ایک ہاتھ اور گھٹنوں پر، دوسرا پیچھے کھڑا یا گھٹنوں پر۔ زیادہ گہرائی اور مختلف زاویہ۔",
            enSteps = listOf(
                "One partner positions on hands and knees, or lies flat.",
                "The other kneels or stands behind at comfortable height.",
                "Front partner can lower to forearms or use a hip pillow.",
                "Start slowly and adjust knee width or hip height."
            ),
            urSteps = listOf(
                "ایک ہاتھ گھٹنوں پر یا پیٹ کے بل لیٹے۔",
                "دوسرا آرام دہ اونچائی پر پیچھے کھڑا یا بیٹھے۔",
                "سامنے والا بازوؤں پر جھکے یا کولہے کے نیچے تکیہ رکھے۔",
                "آہستہ شروع کریں، گھٹنوں کی چوڑائی یا کولہے ایڈجسٹ کریں۔"
            ),
            enTips = listOf(
                "A pillow under hips improves comfort and angle.",
                "Front partner controls depth by shifting hips.",
                "Check in frequently — this position can be intense."
            ),
            urTips = listOf(
                "کولہے کے نیچے تکیہ آرام اور زاویہ بہتر بناتا ہے۔",
                "سامنے والا کولہے ہلاکر گہرائی کنٹرول کرے۔",
                "بار بار پوچھتے رہیں — یہ پوزیشن شدید ہو سکتی ہے۔"
            )
        ),
        posture(
            id = "lotus", categoryId = CAT_STANDING, difficulty = Difficulty.ADVANCED,
            illustrationRes = R.drawable.ill_lotus,
            enName = "Lotus", urName = "کمل پوزیشن",
            enCat = "Standing & Seated", urCat = "کھڑے اور بیٹھے",
            enSummary = "Seated face-to-face with legs wrapped around each other.",
            urSummary = "بیٹھ کر آمنے سامنے، ٹانگیں ایک دوسرے کے گرد۔",
            enDesc = "Both partners sit facing each other with legs intertwined. Emphasizes closeness, slow movement, and synchronized breathing.",
            urDesc = "دونوں آمنے سامنے بیٹھ کر ٹانگیں ملائیں۔ قربت، آہستہ حرکت اور ہم آہنگ سانس۔",
            enSteps = listOf(
                "One partner sits cross-legged or with legs extended.",
                "The other sits on their lap, wrapping legs around their waist.",
                "Wrap arms around each other for balance.",
                "Rock together slowly — small movements are often best."
            ),
            urSteps = listOf(
                "ایک ساتھی پیر باندھ کر یا پھیلا کر بیٹھے۔",
                "دوسرا گود میں بیٹھے، ٹانگیں کمر کے گرد لپیٹے۔",
                "توازن کے لیے باہیں ایک دوسرے کے گرد۔",
                "آہستہ ساتھ ہلیں — چھوٹی حرکتیں اکثر بہترین ہوتی ہیں۔"
            ),
            enTips = listOf(
                "Requires flexibility — use cushions under hips.",
                "Ideal for slow, mindful intimacy.",
                "Maintain eye contact to deepen connection."
            ),
            urTips = listOf(
                "لچک چاہیے — کولہے کے نیچے گدوے استعمال کریں۔",
                "آہستہ، باخبر قربت کے لیے بہترین۔",
                "آنکھوں کا رابطہ تعلق گہرا کرتا ہے۔"
            )
        ),
        posture(
            id = "standing", categoryId = CAT_STANDING, difficulty = Difficulty.ADVANCED,
            illustrationRes = R.drawable.ill_standing,
            enName = "Standing", urName = "کھڑے ہوئے",
            enCat = "Standing & Seated", urCat = "کھڑے اور بیٹھے",
            enSummary = "One partner lifts or supports the other while standing.",
            urSummary = "کھڑے ہو کر ایک دوسرے کو سہارا دینا۔",
            enDesc = "Partners stand, often with one lifted or braced against a wall. Spontaneous but requires strength and stability.",
            urDesc = "کھڑے ہو کر، اکثر ایک اٹھایا ہوا یا دیوار سے سہارا۔ اچانک لیکن طاقت اور توازن چاہیے۔",
            enSteps = listOf(
                "One partner stands with back against a sturdy wall.",
                "The other faces them, legs wrapped around their waist.",
                "Standing partner supports weight with hands under thighs.",
                "Move carefully — balance and communication are essential."
            ),
            urSteps = listOf(
                "ایک مضبوط دیوار سے ٹیک لگا کر کھڑے ہوں۔",
                "دوسرا آمنے سامنے، ٹانگیں کمر کے گرد۔",
                "کھڑا ساتھی رانوں کے نیچے ہاتھوں سے سہارا دے۔",
                "احتیاط سے حرکت کریں — توازن اور بات چیت ضروری ہے۔"
            ),
            enTips = listOf(
                "Use a wall for support — never rely on balance alone.",
                "Lifted partner can grip shoulders or the wall.",
                "Try one foot on a chair for an easier variation."
            ),
            urTips = listOf(
                "دیوار سے سہارا لیں — صرف توازن پر بھروسہ نہ کریں۔",
                "اٹھا ہوا ساتھی کندھے یا دیوار پکڑ سکتا ہے۔",
                "ایک پاؤں کرسی پر رکھ کر آسان متبادل آزمائیں۔"
            )
        ),
        posture(
            id = "edge_of_bed", categoryId = CAT_VARIATIONS, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.ill_edge_bed,
            enName = "Edge of Bed", urName = "بستر کے کنارے",
            enCat = "Variations", urCat = "تبدیلیاں",
            enSummary = "One partner at the bed edge while the other stands.",
            urSummary = "ایک بستر کے کنارے، دوسرا کھڑا۔",
            enDesc = "One partner sits or lies at the bed edge with legs draped over. The other stands between their legs. Comfortable and accessible.",
            urDesc = "ایک بستر کے کنارے بیٹھے یا لیٹے، ٹانگیں باہر۔ دوسرا درمیان میں کھڑا۔ آرام دہ اور آسان۔",
            enSteps = listOf(
                "One partner sits or lies at the very edge of the bed.",
                "Feet on floor or calves on standing partner's shoulders.",
                "Standing partner positions between their legs.",
                "Adjust bed height for the best alignment."
            ),
            urSteps = listOf(
                "ایک بستر کے بالکل کنارے بیٹھے یا لیٹیں۔",
                "پاؤں فرش پر یا پنڈلیاں کھڑے ساتھی کے کندھوں پر۔",
                "کھڑا ساتھی ٹانگوں کے درمیان کھڑا ہو۔",
                "بستر کی اونچائی ایڈجسٹ کریں بہتر ہم آہنگی کے لیے۔"
            ),
            enTips = listOf(
                "Works well when one partner has limited mobility.",
                "Lying partner can grip the bed edge for stability.",
                "Try bent, straight, or over-shoulder leg positions."
            ),
            urTips = listOf(
                "جب ایک ساتھی کی حرکت محدود ہو تو بہترین۔",
                "لیٹا ساتھی بستر کا کنارہ پکڑ سکتا ہے۔",
                "ٹانگیں موڑی، سیدھی یا کندھوں پر رکھ کر آزمائیں۔"
            )
        ),
        posture(
            id = "reverse_cowgirl", categoryId = CAT_VARIATIONS, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.ill_reverse_cowgirl,
            enName = "Reverse Cowgirl", urName = "الٹ کاؤگرل",
            enCat = "Variations", urCat = "تبدیلیاں",
            enSummary = "Top partner faces away while straddling the other.",
            urSummary = "اوپر والا پیٹھ کر کے بیٹھے۔",
            enDesc = "Like cowgirl, but the top partner faces away. Offers a different angle and new perspective.",
            urDesc = "کاؤگرل جیسی لیکن اوپر والا منہ دوسری طرف۔ مختلف زاویہ اور نیا تجربہ۔",
            enSteps = listOf(
                "One partner lies on their back.",
                "The other straddles facing away toward their feet.",
                "Top partner places hands on thighs for balance.",
                "Lean forward or sit upright to change sensation."
            ),
            urSteps = listOf(
                "ایک پیٹ کے بل لیٹے۔",
                "دوسرا پاؤں کی طرف منہ کر کے اوپر بیٹھے۔",
                "اوازن کے لیے رانوں پر ہاتھ رکھیں۔",
                "آگے جھکیں یا سیدھے بیٹھیں احساس بدلنے کے لیے۔"
            ),
            enTips = listOf(
                "Bottom partner should communicate about depth.",
                "Top partner controls pace — go slowly at first.",
                "Try gentle hip circles for variety."
            ),
            urTips = listOf(
                "نیچے والا گہرائی کے بارے میں بتائے۔",
                "اوپر والا رفتار کنٹرول کرے — آہستہ شروع کریں۔",
                "کولہے آہستہ گول گھمائیں تنوع کے لیے۔"
            )
        ),
        posture(
            id = "butterfly", categoryId = CAT_VARIATIONS, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.ill_butterfly,
            enName = "Butterfly", urName = "تتلی پوزیشن",
            enCat = "Variations", urCat = "تبدیلیاں",
            enSummary = "Reclining partner's hips elevated with legs open wide.",
            urSummary = "لیٹے ہوئے کے کولہے اونچے، ٹانگیں کھلی۔",
            enDesc = "One partner lies on their back with hips raised on a pillow, legs open. The other stands or kneels at the bed edge.",
            urDesc = "ایک پیٹ کے بل تکیے پر اونچے کولہے، ٹانگیں کھولے۔ دوسرا کنارے پر کھڑا یا گھٹنوں پر۔",
            enSteps = listOf(
                "Place a firm pillow under the reclining partner's hips.",
                "Lie back with knees toward chest or legs on partner's shoulders.",
                "Other partner stands or kneels at the bed edge.",
                "Adjust pillow height until comfortable for both."
            ),
            urSteps = listOf(
                "مضبوط تکیہ کولہے کے نیچے رکھیں۔",
                "پیٹھ کے بل لیٹیں، گھٹنے سینے کی طرف یا ٹانگیں کندھوں پر۔",
                "دوسرا ساتھی بستر کے کنارے کھڑا یا گھٹنوں پر۔",
                "تکیے کی اونچائی دونوں کے آرام کے مطابق رکھیں۔"
            ),
            enTips = listOf(
                "Excellent for targeted stimulation depending on anatomy.",
                "Use a wedge pillow for stable elevation.",
                "Reclining partner can hold their own legs."
            ),
            urTips = listOf(
                "جسم کی ساخت کے مطابق بہتر محرک کے لیے۔",
                "مثلثی تکیہ مستحکم اونچائی کے لیے استعمال کریں۔",
                "لیٹا ساتھی اپنی ٹانگیں خود پکڑ سکتا ہے۔"
            )
        ),
        posture(
            id = "scissors", categoryId = CAT_SIDE, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.ill_scissors,
            enName = "Scissors", urName = "قینچی پوزیشن",
            enCat = "Side by Side", urCat = "ساتھ ساتھ",
            enSummary = "Partners lie at an angle with legs intertwined.",
            urSummary = "ترچھے لیٹ کر ٹانگیں آپس میں۔",
            enDesc = "Partners lie on sides at a 90-degree angle with legs scissored. Allows mutual stimulation with less depth.",
            urDesc = "دونوں ترچھے زاویے پر سیدھے، ٹانگیں قینچی کی طرح۔ کم گہرائی میں باہمی لطف۔",
            enSteps = listOf(
                "Both lie on sides facing each other at a slight angle.",
                "Intertwine legs so thighs and hips align.",
                "Use hand or hip movement for stimulation.",
                "Adjust body angle until contact feels natural."
            ),
            urSteps = listOf(
                "دونوں ہلکے زاویے پر آمنے سامنے سیدھے لیٹیں۔",
                "ٹانگیں ملائیں تاکہ رانیں اور کولہے ہم آہنگ ہوں۔",
                "ہاتھ یا کولہے کی حرکت سے محرک دیں۔",
                "جسم کا زاویہ ایڈجسٹ کریں جب رابطہ قدرتی لگے۔"
            ),
            enTips = listOf(
                "Works well for intimacy with less physical intensity.",
                "Add lubricant if needed for comfortable friction.",
                "Great for mutual pleasure and synchronized movement."
            ),
            urTips = listOf(
                "کم جسمانی شدت میں قربت کے لیے بہترین۔",
                "ضرورت ہو تو لوبریکنٹ استعمال کریں۔",
                "باہمی لطف اور ہم آہنگ حرکت کے لیے بہترین۔"
            )
        ),
        posture(
            id = "lazy_dog", categoryId = CAT_REAR, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.ill_lazy_dog,
            enName = "Lazy Dog", urName = "آرام دہ پیچھے سے",
            enCat = "Rear Entry", urCat = "پیچھے سے",
            enSummary = "A relaxed rear-entry variation lying flat.",
            urSummary = "پیٹ کے بل آرام دہ پیچھے سے متبادل۔",
            enDesc = "A gentler rear entry where the receiving partner lies flat on their stomach. Lower effort and very comfortable.",
            urDesc = "نرم پیچھے سے داخلہ جہاں سامنے والا پیٹ کے بل لیٹا ہو۔ کم محنت، زیادہ آرام۔",
            enSteps = listOf(
                "One partner lies flat on stomach with pillow under hips.",
                "The other lies on top or positions behind.",
                "Top partner keeps weight distributed lightly.",
                "Use slow grinding rather than deep thrusting."
            ),
            urSteps = listOf(
                "ایک پیٹ کے بل کولہے کے نیچے تکیے کے ساتھ۔",
                "دوسرا اوپر یا پیچھے سے۔",
                "اوپر والا وزن ہلکا رکھے۔",
                "گہری جھٹکوں کی بجائے آہستہ رگڑ استعمال کریں۔"
            ),
            enTips = listOf(
                "Ideal when one or both partners are tired.",
                "Bottom partner adjusts hip height with pillow thickness.",
                "Combine with gentle massage for relaxation."
            ),
            urTips = listOf(
                "جب تھکاوٹ ہو تو بہترین۔",
                "نیچے والا تکیے کی موٹائی سے کولہے کی اونچائی بدلے۔",
                "نرم مساج کے ساتھ ملا کر آرام دہ بنائیں۔"
            )
        )
    )

    private fun posture(
        id: String, categoryId: String, difficulty: Difficulty, illustrationRes: Int,
        enName: String, urName: String, enCat: String, urCat: String,
        enSummary: String, urSummary: String, enDesc: String, urDesc: String,
        enSteps: List<String>, urSteps: List<String>,
        enTips: List<String>, urTips: List<String>
    ) = Posture(
        id = id,
        difficulty = difficulty,
        illustrationRes = illustrationRes,
        categoryId = categoryId,
        english = LocalizedContent(enName, enCat, enSummary, enDesc, enSteps, enTips),
        urdu = LocalizedContent(urName, urCat, urSummary, urDesc, urSteps, urTips)
    )

    fun getAllPostures(): List<Posture> = postures

    fun getPosturesByCategory(categoryId: String): List<Posture> {
        if (categoryId == CAT_ALL) return postures
        return postures.filter { it.categoryId == categoryId }
    }

    fun getPostureById(id: String): Posture? = postures.find { it.id == id }
}
