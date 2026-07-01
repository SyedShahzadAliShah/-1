package com.couplesguide.postures.data

import com.couplesguide.postures.R

object PostureRepository {

    const val CAT_ALL = "all"
    const val CAT_FACE = "face_to_face"
    const val CAT_SIDE = "side_by_side"
    const val CAT_REAR = "rear_entry"
    const val CAT_STANDING = "standing_seated"
    const val CAT_IMAGINATION = "imagination"
    const val CAT_VARIATIONS = "variations"

    fun getCategoryIds(): List<String> = listOf(
        CAT_ALL, CAT_FACE, CAT_SIDE, CAT_REAR, CAT_STANDING, CAT_VARIATIONS, CAT_IMAGINATION
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
        CAT_VARIATIONS to ("Variations" to "تبدیلیاں"),
        CAT_IMAGINATION to ("Imagination" to "تخیل")
    )

    private val postures: List<Posture> = listOf(
        posture(
            id = "missionary", categoryId = CAT_FACE, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_missionary,
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
            illustrationRes = R.drawable.pic_cowgirl,
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
            illustrationRes = R.drawable.pic_spooning,
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
            illustrationRes = R.drawable.pic_side_by_side,
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
            illustrationRes = R.drawable.pic_doggy,
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
            illustrationRes = R.drawable.pic_lotus,
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
            illustrationRes = R.drawable.pic_standing,
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
            illustrationRes = R.drawable.pic_edge_bed,
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
            illustrationRes = R.drawable.pic_reverse_cowgirl,
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
            illustrationRes = R.drawable.pic_butterfly,
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
            illustrationRes = R.drawable.pic_scissors,
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
            illustrationRes = R.drawable.pic_lazy_dog,
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
        ),
        posture(
            id = "cat", categoryId = CAT_FACE, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_cat,
            enName = "Coital Alignment (CAT)", urName = "کوائٹل الائنمنٹ (CAT)",
            enCat = "Face to Face", urCat = "آمنے سامنے",
            enSummary = "An upgraded missionary with circular hip movement for dual stimulation.",
            urSummary = "مشنری کی بہتر شکل جس میں گول کولہے کی حرکت سے دہرا محرک ملتا ہے۔",
            enDesc = "Based on the Coital Alignment Technique: the penetrating partner shifts weight forward so contact presses along the external vulva rather than deep thrusting. Both partners move hips in circles to stimulate internal and clitoral zones simultaneously while maintaining face-to-face intimacy.",
            urDesc = "کوائٹل الائنمنٹ تکنیک پر مبنی: اوپر والا ساتھی وزن آگے رکھتا ہے تاکہ گہرے جھٹکوں کی بجائے بیرونی محرک کو دباؤ ملے۔ دونوں کولہے گول گھمائیں — اندرونی اور کلائیٹورل دونوں محرک ساتھ ساتھ، آمنے سامنے قربت برقرار۔",
            enSteps = listOf(
                "Receiving partner lies on their back with knees slightly bent.",
                "Penetrating partner enters from above, then shifts weight forward onto the partner.",
                "Avoid in-and-out thrusting — move hips in slow circles instead.",
                "Receiving partner tilts hips at different angles and may wrap legs around partner's back.",
                "Maintain eye contact and adjust pace together."
            ),
            urSteps = listOf(
                "سامنے والا ساتھی پیٹ کے بل لیٹے، گھٹنے ہلکے موڑے۔",
                "اوپر والا داخل ہو، پھر وزن آگے ساتھی پر رکھے۔",
                "اندر باہر جھٹکوں سے بچیں — کولہے آہستہ گول گھمائیں۔",
                "سامنے والا کولہے مختلف زاویوں پر جھکائے، ٹانگیں پیچھے لپیٹ سکتا ہے۔",
                "آنکھوں کا رابطہ رکھیں اور رفتار ساتھ مل کر طے کریں۔"
            ),
            enTips = listOf(
                "Focus on grinding, not thrusting — this is the key difference from missionary.",
                "Experiment with hip angles to find the sweet spot for both partners.",
                "Excellent for couples who want clitoral stimulation during penetration.",
                "Take your time — this position rewards patience over speed."
            ),
            urTips = listOf(
                "رگڑ پر توجہ دیں، جھٹکوں پر نہیں — یہ مشنری سے فرق ہے۔",
                "کولہے کے زاویے آزمائیں دونوں کے لیے بہترین نقطہ تلاش کریں۔",
                "داخلہ کے ساتھ کلائیٹورل محرک چاہنے والے جوڑوں کے لیے بہترین۔",
                "وقت لیں — یہ پوزیشن صبر کا انعام دیتی ہے۔"
            )
        ),
        posture(
            id = "rocking_horse", categoryId = CAT_FACE, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_rocking_horse,
            enName = "Rocking Horse", urName = "جھولنے والا گھوڑا",
            enCat = "Face to Face", urCat = "آمنے سامنے",
            enSummary = "Seated face-to-face with rocking motion for G-spot and closeness.",
            urSummary = "بیٹھ کر آمنے سامنے جھولنے والی حرکت — G-spot اور قربت کے لیے۔",
            enDesc = "The receiving partner sits between the penetrating partner's legs with legs nearly wrapped around them. Both partners rock into each other, controlling depth while staying physically close. Can be gentle or passionate.",
            urDesc = "سامنے والا ساتھی دوسرے کی ٹانگوں کے درمیان بیٹھے، ٹانگیں تقریباً لپیٹے۔ دونوں ایک دوسرے کی طرف جھولیں، گہرائی کنٹرول کرتے ہوئے قریب رہیں۔ نرم یا پرجوش — دونوں طرح ممکن۔",
            enSteps = listOf(
                "Penetrating partner sits with legs extended or slightly apart.",
                "Receiving partner sits facing them, straddling between their legs.",
                "Wrap arms around each other for balance and closeness.",
                "Rock hips together — forward and back or in gentle circles.",
                "Adjust leg wrap for more or less depth."
            ),
            urSteps = listOf(
                "پیچھے والا ساتھی ٹانگیں پھیلا کر یا ہلکا کھول کر بیٹھے۔",
                "سامنے والا آمنے سامنے ان کی ٹانگوں کے درمیان بیٹھے۔",
                "توازن اور قربت کے لیے باہیں ایک دوسرے کے گرد لپیٹیں۔",
                "کولہے ساتھ جھولیں — آگے پیچھے یا ہلکے گول۔",
                "گہرائی کے لیے ٹانگوں کی لپیٹ ایڈجسٹ کریں۔"
            ),
            enTips = listOf(
                "Ideal for G-spot stimulation with sustained eye contact.",
                "Use cushions under hips if flexibility is limited.",
                "Small rocking motions are often more effective than large ones.",
                "Great transition position from foreplay to intercourse."
            ),
            urTips = listOf(
                "G-spot محرک اور آنکھوں کے رابطے کے لیے بہترین۔",
                "لچک کم ہو تو کولہے کے نیچے گدوے استعمال کریں۔",
                "چھوٹی جھولنے والی حرکتیں اکثر بڑی سے زیادہ مؤثر۔",
                "پیش بازی سے داخلہ میں آنے کے لیے بہترین پل۔"
            )
        ),
        posture(
            id = "seated_scissors", categoryId = CAT_VARIATIONS, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_seated_scissors,
            enName = "Seated Scissors", urName = "بیٹھی قینچی",
            enCat = "Variations", urCat = "تبدیلیاں",
            enSummary = "A playful reverse-cowgirl variation with one bent leg.",
            urSummary = "الٹ کاؤگرل کی تفریحی شکل — ایک موڑی ہوئی ٹانگ کے ساتھ۔",
            enDesc = "The penetrating partner lies on their back with one leg bent. The receiving partner straddles the bent leg and arranges their legs for comfort. Plenty of support and room for both to experiment with bounce and grind.",
            urDesc = "پیچھے والا پیٹ کے بل ایک ٹانگ موڑے لیٹے۔ سامنے والا موڑی ٹانگ پر بیٹھے اور اپنی ٹانگیں آرام سے رکھے۔ دونوں کے لیے سہارا اور تجربے کی گنجائش۔",
            enSteps = listOf(
                "Penetrating partner lies on back with one knee bent upward.",
                "Receiving partner straddles the bent leg, facing toward partner's feet.",
                "Arrange remaining legs however feels most comfortable.",
                "Receiving partner bounces, grinds, or rocks at their own pace.",
                "Penetrating partner relaxes and enjoys the view."
            ),
            urSteps = listOf(
                "پیچھے والا پیٹ کے بل ایک گھٹنا اوپر موڑے لیٹے۔",
                "سامنے والا موڑی ٹانگ پر بیٹھے، پاؤں کی طرف منہ کرے۔",
                "باقی ٹانگیں جہاں آرام محسوس ہو وہاں رکھیں۔",
                "سامنے والا اپنی رفتار سے اچھلے، رگڑے یا جھولے۔",
                "پیچھے والا آرام کرے اور لطف اٹھائے۔"
            ),
            enTips = listOf(
                "Fun for both — top partner controls, bottom partner relaxes.",
                "Try alternating which leg is bent for variety.",
                "Excellent for couples who enjoy woman-on-top dynamics.",
                "Use hands on thighs for balance and guidance."
            ),
            urTips = listOf(
                "دونوں کے لیے مزہ — اوپر والا کنٹرول، نیچے والا آرام۔",
                "تنوع کے لیے موڑی ٹانگ بدل کر آزمائیں۔",
                "عورت اوپر پسند کرنے والے جوڑوں کے لیے بہترین۔",
                "توازن کے لیے رانوں پر ہاتھ رکھیں۔"
            )
        ),
        posture(
            id = "countertop", categoryId = CAT_STANDING, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_countertop,
            enName = "Countertop", urName = "کاؤنٹر ٹاپ",
            enCat = "Standing & Seated", urCat = "کھڑے اور بیٹھے",
            enSummary = "Use any sturdy hip-height surface for spontaneous intimacy.",
            urSummary = "کولہے کی اونچائی کی مضبوط سطح پر اچانک قربت۔",
            enDesc = "The receiving partner lies or sits on a sturdy flat surface at hip height — countertop, desk, or table. The penetrating partner stands before them. Both hands remain free for touch and stimulation.",
            urDesc = "سامنے والا کولہے کی اونچائی کی مضبوط سطح پر بیٹھے یا لیٹے — کاؤنٹر، میز یا ٹیبل۔ دوسرا سامنے کھڑا ہو۔ دونوں کے ہاتھ آزاد چھونے اور محرک دینے کے لیے۔",
            enSteps = listOf(
                "Find a sturdy surface at approximately hip height.",
                "Receiving partner sits or lies back on the edge.",
                "Penetrating partner stands between their legs.",
                "Adjust surface height with a step stool if needed.",
                "Use free hands for nipple, clitoral, or hair stimulation."
            ),
            urSteps = listOf(
                "کولہے کی اونچائی کی مضبوط سطح تلاش کریں۔",
                "سامنے والا کنارے پر بیٹھے یا پیٹھ کے بل لیٹے۔",
                "دوسرا ٹانگوں کے درمیان کھڑا ہو۔",
                "ضرورت ہو تو سٹیپ سے اونچائی ایڈجسٹ کریں۔",
                "آزاد ہاتھوں سے چھونے اور محرک دیں۔"
            ),
            enTips = listOf(
                "Also works well for oral sex — giver kneels instead of standing.",
                "Ensure the surface is stable before putting weight on it.",
                "Great for spontaneous moments outside the bedroom.",
                "Different heights? This position levels the playing field."
            ),
            urTips = listOf(
                "زبانی لطف کے لیے بھی اچھا — کھڑے کی بجائے گھٹنوں پر بیٹھیں۔",
                "وزن ڈالنے سے پہلے سطح مستحکم یقینی بنائیں۔",
                "بیڈروم سے باہر اچانک لمحات کے لیے بہترین۔",
                "اونچائی مختلف ہو؟ یہ پوزیشن برابر کر دیتی ہے۔"
            )
        ),
        posture(
            id = "lap_dance", categoryId = CAT_STANDING, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_lap_dance,
            enName = "Lap Dance", urName = "گود میں رقص",
            enCat = "Standing & Seated", urCat = "کھڑے اور بیٹھے",
            enSummary = "Seated straddle with deep eye contact and partner-controlled movement.",
            urSummary = "بیٹھ کر اوپر بیٹھنا — گہری آنکھوں کا رابطہ اور حرکت پر کنٹرول۔",
            enDesc = "Use an armless chair or firm surface. The receiving partner straddles the penetrating partner's lap, face-to-face or back-to-front. Feet on the floor provide leverage for bouncing, grinding, and rotation.",
            urDesc = "بغیر بازو کی کرسی یا مضبوط سطح استعمال کریں۔ سامنے والا گود میں بیٹھے — آمنے سامنے یا پیٹھ کر کے۔ فرش پر پاؤں سے اچھلنے، رگڑنے اور گھومنے کا فائدہ ملتا ہے۔",
            enSteps = listOf(
                "Penetrating partner sits firmly in a chair or on bed edge.",
                "Receiving partner straddles their lap, facing them or away.",
                "Plant feet on the floor for leverage and balance.",
                "Rotate, bounce, or grind to find the best rhythm.",
                "Maintain eye contact if face-to-face for deeper intimacy."
            ),
            urSteps = listOf(
                "پیچھے والا کرسی یا بستر کے کنارے مضبوطی سے بیٹھے۔",
                "سامنے والا گود میں بیٹھے — آمنے سامنے یا پیٹھ کر۔",
                "فرش پر پاؤں رکھیں توازن اور فائدے کے لیے۔",
                "گھمائیں، اچھلیں یا رگڑیں بہترین تال تلاش کرنے کے لیے۔",
                "آمنے سامنے ہوں تو آنکھوں کا رابطہ قربت بڑھاتا ہے۔"
            ),
            enTips = listOf(
                "Accessible for different heights and mobility levels.",
                "Top partner does the work — great when one partner is tired.",
                "Face-to-back variation adds a different sensation angle.",
                "Ideal for deep penetration with emotional connection."
            ),
            urTips = listOf(
                "مختلف قد اور حرکت کی سطحوں کے لیے آسان۔",
                "اوپر والا محنت کرے — جب ایک تھکا ہو تو بہترین۔",
                "پیٹھ کر کے مختلف احساس ملتا ہے۔",
                "گہری داخلہ اور جذباتی تعلق کے لیے بہترین۔"
            )
        ),
        posture(
            id = "layer_cake", categoryId = CAT_FACE, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_layer_cake,
            enName = "Layer Cake", urName = "لیئر کیک",
            enCat = "Face to Face", urCat = "آمنے سامنے",
            enSummary = "Full-body grinding without penetration — maximum clitoral contact.",
            urSummary = "بغیر داخلہ پورے جسم کی رگڑ — زیادہ سے زیادہ کلائیٹورل رابطہ۔",
            enDesc = "One partner lies on their back while the other lies flat on top, facing them. Both press genitals together and grind at a shared rhythm. No penetration — pure external stimulation and skin-to-skin closeness.",
            urDesc = "ایک پیٹ کے بل لیٹے، دوسرا اوپر آمنے سامنے لیٹے۔ دونوں محرک ایک دوسرے سے ملائیں اور مشترکہ تال پر رگڑیں۔ بغیر داخلہ — صرف بیرونی محرک اور جلد سے جلد قربت۔",
            enSteps = listOf(
                "Bottom partner lies on their back comfortably.",
                "Top partner lies flat on top, facing the bottom partner.",
                "Align hips so genitals press together naturally.",
                "Rock and grind together at a rhythm that feels good.",
                "Top partner may grip the bed edge for extra friction."
            ),
            urSteps = listOf(
                "نیچے والا آرام سے پیٹ کے بل لیٹے۔",
                "اوپر والا آمنے سامنے سیدھا اوپر لیٹے۔",
                "کولہے ایسے ملائیں کہ محرک قدرتی طور پر رابطے میں آئیں۔",
                "مشترکہ تال پر ساتھ رگڑیں۔",
                "اوپر والا بستر کا کنارہ پکڑ کر زیادہ رگڑ حاصل کر سکتا ہے۔"
            ),
            enTips = listOf(
                "Use lubricant to keep friction pleasurable, not painful.",
                "Perfect on days when penetration doesn't feel right.",
                "Excellent during menstruation or recovery periods.",
                "Builds intimacy through full-body contact and eye contact."
            ),
            urTips = listOf(
                "لوبریکنٹ استعمال کریں تاکہ رگڑ لذیذ رہے، تکلیف دہ نہیں۔",
                "جب داخلہ مناسب نہ لگے اس دن بہترین۔",
                "ماہواری یا صحت یابی کے دوران بہترین۔",
                "پورے جسم اور آنکھوں کے رابطے سے قربت بنتی ہے۔"
            )
        ),
        posture(
            id = "reverse_slither", categoryId = CAT_REAR, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_reverse_slither,
            enName = "Reverse Slither", urName = "الٹ رینگنا",
            enCat = "Rear Entry", urCat = "پیچھے سے",
            enSummary = "Rear entry with full skin contact and deep penetration.",
            urSummary = "پیچھے سے داخلہ مکمل جلد رابطے اور گہری داخلہ کے ساتھ۔",
            enDesc = "The receiving partner lies flat on their stomach while the penetrating partner lies on top, entering from behind. Combines the depth of rear entry with the intimacy of full-body contact. Heads close together for whispered words.",
            urDesc = "سامنے والا پیٹ کے بل لیٹے، دوسرا اوپر پیچھے سے داخل ہو۔ پیچھے سے گہرائی اور پورے جسم کے رابطے کی قربت ملتی ہے۔ سر قریب — آہستہ باتوں کے لیے۔",
            enSteps = listOf(
                "Receiving partner lies flat on stomach, optionally with pillow under hips.",
                "Penetrating partner lies on top, entering from behind.",
                "Keep weight distributed lightly on forearms.",
                "Use slow grinding and shallow thrusts.",
                "Whisper, kiss neck, and stay connected throughout."
            ),
            urSteps = listOf(
                "سامنے والا پیٹ کے بل لیٹے، اختیاری تکیہ کولہے کے نیچے۔",
                "دوسرا اوپر پیچھے سے داخل ہو۔",
                "وزن بازوؤں پر ہلکا رکھیں۔",
                "آہستہ رگڑ اور ہلکی جھٹکیں استعمال کریں۔",
                "آہستہ باتیں، گردن پر بوسہ، تعلق برقرار رکھیں۔"
            ),
            enTips = listOf(
                "Receiving partner can slip a hand underneath for self-stimulation.",
                "Pillow under hips improves angle and comfort.",
                "More intimate than traditional doggy — bodies fully connected.",
                "Great for breast and clitoral stimulation from behind."
            ),
            urTips = listOf(
                "سامنے والا ہاتھ نیچے بڑھا کر خود محرک دے سکتا ہے۔",
                "کولہے کے نیچے تکیہ زاویہ اور آرام بہتر بناتا ہے۔",
                "روایتی ڈاگی سے زیادہ قریبی — جسم مکمل جڑے۔",
                "پیچھے سے سینے اور کلائیٹورل محرک کے لیے بہترین۔"
            )
        ),
        posture(
            id = "yab_yum", categoryId = CAT_FACE, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_yab_yum,
            enName = "Yab-Yum", urName = "یب-یم",
            enCat = "Face to Face", urCat = "آمنے سامنے",
            enSummary = "Tantric seated embrace with synchronized breathing and slow rocking.",
            urSummary = "تانترک بیٹھی گلے ملنے والی قربت — ہم آہنگ سانس اور آہستہ جھولنا۔",
            enDesc = "A popular Tantric position: the penetrating partner sits cross-legged on the floor or bed. The receiving partner sits in their lap, legs wrapped around their back. Rock side-to-side while holding each other close rather than vigorous thrusting.",
            urDesc = "مشہور تانترک پوزیشن: پیچھے والا پیر باندھ کر فرش یا بستر پر بیٹھے۔ سامنے والا گود میں بیٹھے، ٹانگیں پیٹھ کے گرد۔ زور دار جھٹکوں کی بجائے قریب پکڑ کر آہستہ آگے پیچھے جھولیں۔",
            enSteps = listOf(
                "Penetrating partner sits cross-legged on a firm surface.",
                "Receiving partner sits in their lap, facing them, legs around their waist.",
                "Wrap arms tightly around each other.",
                "Rock side-to-side slowly — breathe in sync.",
                "Try eye-gazing to deepen emotional connection."
            ),
            urSteps = listOf(
                "پیچھے والا پیر باندھ کر مضبوط سطح پر بیٹھے۔",
                "سامنے والا گود میں آمنے سامنے، ٹانگیں کمر کے گرد۔",
                "باہیں مضبوطی سے ایک دوسرے کے گرد لپیٹیں۔",
                "آہستہ آگے پیچھے جھولیں — سانسیں ہم آہنگ رکھیں۔",
                "آنکھوں میں دیکھیں جذباتی تعلق گہرا کرنے کے لیے۔"
            ),
            enTips = listOf(
                "Focus on connection over performance — this is meditative intimacy.",
                "Use cushions under sit bones if floor is uncomfortable.",
                "Breathe each other's breath for a powerful bonding effect.",
                "Ideal for married couples reconnecting after busy periods."
            ),
            urTips = listOf(
                "کارکردگی سے زیادہ تعلق — یہ باخبر قربت ہے۔",
                "فرش سخت ہو تو بیٹھنے کی ہڈیوں کے نیچے گدوے رکھیں۔",
                "ایک دوسرے کی سانس محسوس کریں — مضبوط تعلق بنتا ہے۔",
                "مصروف دورانیے کے بعد دوبارہ جڑنے والے شادی شدہ جوڑوں کے لیے بہترین۔"
            )
        )
    )

    private fun posture(
        id: String, categoryId: String, difficulty: Difficulty, illustrationRes: Int,
        enName: String, urName: String, enCat: String, urCat: String,
        enSummary: String, urSummary: String, enDesc: String, urDesc: String,
        enSteps: List<String>, urSteps: List<String>,
        enTips: List<String>, urTips: List<String>
    ): Posture {
        val roles = PostureRoleContent.getRoles(id)
        return Posture(
            id = id,
            difficulty = difficulty,
            illustrationRes = illustrationRes,
            categoryId = categoryId,
            english = LocalizedContent(
                enName, enCat, enSummary, enDesc, enSteps, enTips,
                forMan = roles?.enMan,
                forWoman = roles?.enWoman
            ),
            urdu = LocalizedContent(
                urName, urCat, urSummary, urDesc, urSteps, urTips,
                forMan = roles?.urMan,
                forWoman = roles?.urWoman
            )
        )
    }

    fun getAllPostures(): List<Posture> =
        postures + ImaginationPostureRepository.getImaginationPostures()

    fun getPhysicalPostures(): List<Posture> = postures

    fun getImaginationPostures(): List<Posture> =
        ImaginationPostureRepository.getImaginationPostures()

    fun getPosturesByCategory(categoryId: String): List<Posture> {
        val all = getAllPostures()
        if (categoryId == CAT_ALL) return all
        return all.filter { it.categoryId == categoryId }
    }

    fun getPostureById(id: String): Posture? = getAllPostures().find { it.id == id }
}
