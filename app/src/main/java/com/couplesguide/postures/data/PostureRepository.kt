package com.couplesguide.postures.data

import com.couplesguide.postures.R

object PostureRepository {

    const val CAT_ALL = "all"
    const val CAT_FACE = "face_to_face"
    const val CAT_SIDE = "side_by_side"
    const val CAT_REAR = "rear_entry"
    const val CAT_STANDING = "standing_seated"
    const val CAT_VARIATIONS = "variations"
    const val CAT_IMAGINATION = "imagination"

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
            id = "bicycle", categoryId = CAT_STANDING, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_bicycle,
            enName = "The Bicycle", urName = "بائیسکل",
            enCat = "Standing & Seated", urCat = "کھڑے اور بیٹھے",
            enSummary = "Partner at bed edge while other lifts legs in cycling motion.",
            urSummary = "بستر کے کنارے ایک ساتھی دوسرے کی سائیکلنگ والی ٹانگیں اٹھائے۔",
            enDesc = "Position yourself on the edge of the bed or desk while your partner lies back and lifts their legs up to the chest. Grab their ankles for support.",
            urDesc = "بستر یا میز کے کنارے بیٹھیں جبکہ ساتھی پیٹھ کے بل لیٹ کر ٹانگیں سینے کی طرف اٹھائے۔ ٹخنوں سے پکڑ کر سہارا دیں۔",
            enSteps = listOf(
                "Sit on the edge of the bed with feet on the floor.",
                "Partner lies back and lifts knees toward chest.",
                "Hold ankles gently and guide leg movement.",
                "Adjust pace together — start slowly.",
            ),
            urSteps = listOf(
                "بستر کے کنارے بیٹھیں، پاؤں فرش پر۔",
                "ساتھی پیٹھ کے بل لیٹ کر گھٹنے سینے کی طرف اٹھائے۔",
                "ٹخنوں سے آہستہ پکڑیں اور رہنمائی کریں۔",
                "رفتار ساتھ مل کر ایڈجسٹ کریں۔",
            ),
            enTips = listOf(
                "Great view and control for the seated partner.",
                "Bend knees like a bicycle for variety.",
                "Use pillows under partner's head if needed.",
            ),
            urTips = listOf(
                "بیٹھے ہوئے ساتھی کے لیے بہتر کنٹرول۔",
                "تنوع کے لیے سائیکلنگ والی ٹانگیں۔",
                "ضرورت ہو تو سر کے نیچے تکیہ۔",
            )
        ),
        posture(
            id = "face_to_face", categoryId = CAT_FACE, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_face_to_face,
            enName = "Face to Face", urName = "آمنے سامنے",
            enCat = "Face to Face", urCat = "آمنے سامنے",
            enSummary = "Seated lap embrace for cozy, prolonged intimacy.",
            urSummary = "بیٹھ کر گود میں آمنے سامنے قریبی لمس۔",
            enDesc = "Sit on a chair or bed edge. Your partner faces you, wraps arms around your back, and sits on your lap. Ideal for long, cozy sessions.",
            urDesc = "کرسی یا بستر کے کنارے بیٹھیں۔ ساتھی آمنے سامنے آکر کمر کے گرد باہیں لپیٹے اور گود میں بیٹھے۔ لمبے آرام دہ سیشن کے لیے بہترین۔",
            enSteps = listOf(
                "Sit on a sturdy chair or bed edge.",
                "Partner climbs onto your lap facing you.",
                "Wrap arms around each other for closeness.",
                "Rock gently together at a comfortable pace.",
            ),
            urSteps = listOf(
                "مضبوط کرسی یا بستر کے کنارے بیٹھیں۔",
                "ساتھی آمنے سامنے گود میں آئے۔",
                "قربت کے لیے باہیں ایک دوسرے کے گرد۔",
                "آہستہ ساتھ ہلیں۔",
            ),
            enTips = listOf(
                "Allows eye contact and kissing throughout.",
                "Cozy for extended sessions.",
                "Partner on top can control depth.",
            ),
            urTips = listOf(
                "آنکھوں کا رابطہ اور بوسہ ممکن۔",
                "لمبے سیشن کے لیے آرام دہ۔",
                "اوپر والا گہرائی کنٹرول کر سکتا ہے۔",
            )
        ),
        posture(
            id = "the_plug", categoryId = CAT_REAR, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_the_plug,
            enName = "The Plug", urName = "پلگ",
            enCat = "Rear Entry", urCat = "پیچھے سے",
            enSummary = "Rear-entry position offering a new perspective.",
            urSummary = "پیچھے سے نیا زاویہ دینے والی پوزیشن۔",
            enDesc = "A rear-entry variation that offers a fresh perspective on your partner. Take time to savor the sensations and communicate throughout.",
            urDesc = "پیچھے سے متبادل جو نیا زاویہ دیتا ہے۔ احساسات سے لطف اندوز ہوں اور بات چیت جاری رکھیں۔",
            enSteps = listOf(
                "Receiving partner positions comfortably on hands and knees or lying forward.",
                "Entering partner kneels behind at a comfortable height.",
                "Start slowly and adjust angle together.",
                "Check in frequently about depth and comfort.",
            ),
            urSteps = listOf(
                "سامنے والا ہاتھ گھٹنوں پر یا آگے جھکے۔",
                "پیچھے والا آرام دہ اونچائی پر گھٹنوں کے بل۔",
                "آہستہ شروع کریں، زاویہ ساتھ ایڈجسٹ کریں۔",
                "گہرائی اور آرام کے بارے میں پوچھتے رہیں۔",
            ),
            enTips = listOf(
                "Fantasy-friendly rear perspective.",
                "Go slowly at first.",
                "Use lubricant if needed.",
            ),
            urTips = listOf(
                "تخیل کے لیے موزوں پیچھے کا زاویہ۔",
                "آہستہ شروع کریں۔",
                "ضرورت ہو تو لوبریکنٹ۔",
            )
        ),
        posture(
            id = "lying_dog", categoryId = CAT_REAR, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_lying_dog,
            enName = "Lying Dog", urName = "لیٹا کتا",
            enCat = "Rear Entry", urCat = "پیچھے سے",
            enSummary = "Prone rear-entry for deep, comfortable penetration.",
            urSummary = "پیٹ کے بل پیچھے سے گہری اور آرام دہ داخلہ۔",
            enDesc = "An ideal position for deeper penetration. The receiving partner lies flat on their stomach while the other positions behind. Pleasant and comfortable for both.",
            urDesc = "گہری داخلہ کے لیے موزوں۔ سامنے والا پیٹ کے بل لیٹے، دوسرا پیچھے سے۔ دونوں کے لیے آرام دہ۔",
            enSteps = listOf(
                "Receiving partner lies flat on stomach with pillow under hips.",
                "Entering partner positions on top or behind.",
                "Keep weight distributed lightly.",
                "Use slow grinding movements.",
            ),
            urSteps = listOf(
                "سامنے والا پیٹ کے بل کولہے کے نیچے تکیے کے ساتھ۔",
                "دوسرا اوپر یا پیچھے سے۔",
                "وزن ہلکا رکھیں۔",
                "آہستہ رگڑ والی حرکتیں۔",
            ),
            enTips = listOf(
                "Great depth with low effort.",
                "Very comfortable for relaxed sessions.",
                "Bottom partner can adjust hip height with pillow.",
            ),
            urTips = listOf(
                "کم محنت میں زیادہ گہرائی۔",
                "آرام دہ سیشن کے لیے بہترین۔",
                "تکیے سے کولہے کی اونچائی بدلیں۔",
            )
        ),
        posture(
            id = "spooning", categoryId = CAT_SIDE, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_spooning,
            enName = "Spooning", urName = "چمچے والی",
            enCat = "Side by Side", urCat = "ساتھ ساتھ",
            enSummary = "Side-by-side position with clitoral stimulation potential.",
            urSummary = "ساتھ ساتھ لیٹنے والی پوزیشن کلائیٹورل محرک کے ساتھ۔",
            enDesc = "A great side position allowing clitoral stimulation with mouth or fingers. Both partners lie on their sides facing the same direction.",
            urDesc = "بہترین پہلو کی پوزیشن جس میں منہ یا انگلیوں سے محرک ممکن۔ دونوں ایک سمت دیکھتے ہوئے لیٹیں۔",
            enSteps = listOf(
                "Both lie on sides facing the same direction.",
                "Partner behind curls around the front partner.",
                "Front partner bends knees slightly.",
                "Move together slowly.",
            ),
            urSteps = listOf(
                "دونوں ایک سمت سیدھے لیٹیں۔",
                "پیچھے والا سامنے والے کے گرد لپٹے۔",
                "سامنے والا گھٹنے موڑے۔",
                "آہستہ ساتھ حرکت کریں۔",
            ),
            enTips = listOf(
                "Allows manual or oral stimulation.",
                "Low effort and intimate.",
                "Place pillow between knees for alignment.",
            ),
            urTips = listOf(
                "ہاتھ یا منہ سے محرک ممکن۔",
                "کم محنت، زیادہ قربت۔",
                "گھٹنوں کے درمیان تکیہ رکھیں۔",
            )
        ),
        posture(
            id = "bridge_69", categoryId = CAT_VARIATIONS, difficulty = Difficulty.ADVANCED,
            illustrationRes = R.drawable.pic_bridge_69,
            enName = "Bridge 69", urName = "پل 69",
            enCat = "Variations", urCat = "تبدیلیاں",
            enSummary = "Advanced mutual oral position requiring flexibility.",
            urSummary = "لچکدار باہمی زبانی پوزیشن۔",
            enDesc = "An advanced 69 variation. You may need to push your pelvis forward. Achieving this position is a victory — go slowly and communicate.",
            urDesc = "ترقی یافتہ 69 متبادل۔ کولہے آگے دھکیلنے کی ضرورت ہو سکتی ہے۔ آہستہ کریں اور بات چیت کریں۔",
            enSteps = listOf(
                "Partners position head-to-toe on their sides or angled.",
                "Support hips with pillows if needed.",
                "Push pelvis forward gently to align.",
                "Take breaks if any strain occurs.",
            ),
            urSteps = listOf(
                "سر سے پاؤں کی طرف پہلو پر یا زاویے پر۔",
                "ضرورت ہو تو کولہے کے نیچے تکیہ۔",
                "ہم آہنگی کے لیے کولہے آگے دھکیلیں۔",
                "تکلیف ہو تو وقفہ لیں۔",
            ),
            enTips = listOf(
                "Requires flexibility — don't force it.",
                "Use pillows for hip support.",
                "Communicate constantly.",
            ),
            urTips = listOf(
                "لچک چاہیے — زبردستی نہ کریں۔",
                "کولہے کے لیے تکیہ استعمال کریں۔",
                "مسلسل بات چیت کریں۔",
            )
        ),
        posture(
            id = "waterfall", categoryId = CAT_STANDING, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_waterfall,
            enName = "Waterfall", urName = "آبشار",
            enCat = "Standing & Seated", urCat = "کھڑے اور بیٹھے",
            enSummary = "Inverted position with partner straddling — intense sensations.",
            urSummary = "الٹا زاویہ جس میں ساتھی اوپر بیٹھے — شدید احساسات۔",
            enDesc = "Lie with head and shoulders off the bed while your partner straddles you. Blood flow creates unique sensations — be careful and communicate.",
            urDesc = "سر اور کندھے بستر سے باہر جھکائیں، ساتھی اوپر بیٹھے۔ خون کا بہاؤ منفرد احساسات دیتا ہے — احتیاط کریں۔",
            enSteps = listOf(
                "Lie on back with head hanging off bed edge.",
                "Partner straddles facing your feet or toward head.",
                "Partner supports themselves on hands.",
                "Limit duration — rise slowly afterward.",
            ),
            urSteps = listOf(
                "پیٹھ کے بل سر بستر کے کنارے سے باہر۔",
                "ساتھی پاؤں یا سر کی طرف اوپر بیٹھے۔",
                "ساتھی ہاتھوں سے سہارا لے۔",
                "وقت محدود رکھیں — آہستہ اٹھیں۔",
            ),
            enTips = listOf(
                "Intense sensations from blood flow.",
                "Not for extended periods.",
                "Have partner help you sit up slowly.",
            ),
            urTips = listOf(
                "خون کے بہاؤ سے شدید احساس۔",
                "لمبے عرصے کے لیے نہیں۔",
                "اٹھتے وقت ساتھی مدد کرے۔",
            )
        ),
        posture(
            id = "one_up", categoryId = CAT_STANDING, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_one_up,
            enName = "One Up", urName = "ایک اوپر",
            enCat = "Standing & Seated", urCat = "کھڑے اور بیٹھے",
            enSummary = "Edge-of-bed with one leg raised — great for clitoral sensitivity.",
            urSummary = "بستر کے کنارے ایک ٹانگ اٹھا کر — کلائیٹورل حساسیت کے لیے۔",
            enDesc = "Kneel on the floor with partner at bed edge. Raise one leg and rest it on partner's shoulder. Best for women sensitive in the clitoral area.",
            urDesc = "فرش پر گھٹنے ٹیکیں، ساتھی بستر کے کنارے۔ ایک ٹانگ اٹھا کر کندھے پر رکھیں۔ کلائیٹورل حساسیت کے لیے بہترین۔",
            enSteps = listOf(
                "Partner lies on back at bed edge.",
                "Kneel on floor between their legs.",
                "Raise one of their legs onto your shoulder.",
                "Adjust height and angle for comfort.",
            ),
            urSteps = listOf(
                "ساتھی بستر کے کنارے پیٹھ کے بل۔",
                "ٹانگوں کے درمیان فرش پر گھٹنے ٹیکیں۔",
                "ایک ٹانگ کندھے پر اٹھائیں۔",
                "آرام کے لیے زاویہ ایڈجسٹ کریں۔",
            ),
            enTips = listOf(
                "Excellent clitoral angle.",
                "Try alternating which leg is raised.",
                "Use bed height that suits both partners.",
            ),
            urTips = listOf(
                "بہترین کلائیٹورل زاویہ۔",
                "ٹانگ بدل کر آزمائیں۔",
                "دونوں کے لیے موزوں بستر کی اونچائی۔",
            )
        ),
        posture(
            id = "cowgirl", categoryId = CAT_FACE, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_cowgirl,
            enName = "Cowgirl", urName = "کاؤگرل",
            enCat = "Face to Face", urCat = "آمنے سامنے",
            enSummary = "Woman on top with G-spot and clitoral stimulation.",
            urSummary = "عورت اوپر — جی سپاٹ اور کلائیٹورل محرک۔",
            enDesc = "G-spot, clitoral, and cervical stimulation. The person on top controls pace and depth with a great view of everything happening.",
            urDesc = "جی سپاٹ، کلائیٹورل اور سرونیکل محرک۔ اوپر والا رفتار اور گہرائی کنٹرول کرتا ہے۔",
            enSteps = listOf(
                "One partner lies on back.",
                "Other straddles facing them.",
                "Top partner braces on thighs for balance.",
                "Rock hips to find rhythm.",
            ),
            urSteps = listOf(
                "ایک پیٹ کے بل لیٹے۔",
                "دوسرا آمنے سامنے اوپر بیٹھے۔",
                "توازن کے لیے رانوں پر ہاتھ۔",
                "کولہے ہلائیں تال تلاش کرنے کے لیے۔",
            ),
            enTips = listOf(
                "Top partner sets the pace.",
                "Lean forward or sit upright for different angles.",
                "Great for partner who wants control.",
            ),
            urTips = listOf(
                "اوپر والا رفتار طے کرے۔",
                "زاویے بدلنے کے لیے جھکیں یا سیدھے بیٹھیں۔",
                "کنٹرول چاہنے والے کے لیے بہترین۔",
            )
        ),
        posture(
            id = "hot_seat", categoryId = CAT_VARIATIONS, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_hot_seat,
            enName = "Hot Seat", urName = "گرم سیٹ",
            enCat = "Variations", urCat = "تبدیلیاں",
            enSummary = "Reverse seated on chair or bed edge — G-spot focus.",
            urSummary = "کرسی یا بستر کے کنارے الٹ بیٹھنا — جی سپاٹ پر توجہ۔",
            enDesc = "Sit on bed edge or chair. Partner faces away and moves between your legs, leaning back on chair arms. Excellent G-spot stimulation.",
            urDesc = "بستر کے کنارے یا کرسی پر بیٹھیں۔ ساتھی منہ دوسری طرف بیٹھ کر ٹانگوں کے درمیان حرکت کرے۔ بہترین جی سپاٹ محرک۔",
            enSteps = listOf(
                "Sit on edge of bed or sturdy chair.",
                "Partner straddles facing away.",
                "Partner leans back on your thighs or chair arms.",
                "Guide forward-backward movement together.",
            ),
            urSteps = listOf(
                "بستر کے کنارے یا مضبوط کرسی پر بیٹھیں۔",
                "ساتھی پیٹھ کر کے اوپر بیٹھے۔",
                "ساتھی رانوں یا کرسی کے بازوؤں پر جھکے۔",
                "آگے پیچھے حرکت ساتھ رہنمائی کریں۔",
            ),
            enTips = listOf(
                "Partner controls by leaning back.",
                "Use a chair with arms for support.",
                "Communicate about depth.",
            ),
            urTips = listOf(
                "ساتھی پیچھے جھک کر کنٹرول کرے۔",
                "بازو والی کرسی استعمال کریں۔",
                "گہرائی کے بارے میں بات کریں۔",
            )
        ),
        posture(
            id = "pole_position", categoryId = CAT_FACE, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_pole_position,
            enName = "Pole Position", urName = "پول پوزیشن",
            enCat = "Face to Face", urCat = "آمنے سامنے",
            enSummary = "One leg bent, partner straddles the raised thigh.",
            urSummary = "ایک ٹانگ موڑی، ساتھی اٹھی ران پر بیٹھے۔",
            enDesc = "Lie on back with one leg bent and the other extended. Partner straddles over the raised leg with a thigh on each side.",
            urDesc = "پیٹھ کے بل ایک ٹانگ موڑی دوسری سیدھی۔ ساتھی اٹی ہوئی ران پر دونوں رانوں کے ساتھ بیٹھے۔",
            enSteps = listOf(
                "Lie on back, bend one knee, keep other leg straight.",
                "Partner straddles your raised thigh.",
                "Partner lowers slowly onto you.",
                "Adjust leg position for comfort.",
            ),
            urSteps = listOf(
                "پیٹھ کے بل ایک گھٹنا موڑیں، دوسری ٹانگ سیدھی۔",
                "ساتھی اٹی ران پر بیٹھے۔",
                "ساتھی آہستہ نیچے آئے۔",
                "آرام کے لیے ٹانگ ایڈجسٹ کریں۔",
            ),
            enTips = listOf(
                "Double stimulation for partner.",
                "Great view for both.",
                "Try switching which leg is raised.",
            ),
            urTips = listOf(
                "ساتھی کے لیے دوہرا محرک۔",
                "دونوں کے لیے اچھا منظر۔",
                "کون سی ٹانگ اٹھانی ہے بدل کر آزمائیں۔",
            )
        ),
        posture(
            id = "david_copperfield", categoryId = CAT_VARIATIONS, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_david_copperfield,
            enName = "David Copperfield", urName = "ڈیوڈ کاپر فیلڈ",
            enCat = "Variations", urCat = "تبدیلیاں",
            enSummary = "Pillow under hips for strong upward movement.",
            urSummary = "کولہے کے نیچے تکیہ مضبوط اوپر کی حرکت کے لیے۔",
            enDesc = "Place a pillow under hips to tilt pelvis upward. Bend knees so partner can position legs on your shoulders. Strong ascending movement.",
            urDesc = "کولہے کے نیچے تکیہ رکھیں۔ گھٹنے موڑیں تاکہ ساتھی ٹانگیں کندھوں پر رکھ سکے۔",
            enSteps = listOf(
                "Receiving partner lies on back with pillow under hips.",
                "Bend knees toward chest.",
                "Partner positions between legs at bed edge.",
                "Adjust pillow height for best angle.",
            ),
            urSteps = listOf(
                "سامنے والا تکیے پر کولہے اٹھا کر لیٹے۔",
                "گھٹنے سینے کی طرف موڑیں۔",
                "ساتھی بستر کے کنارے درمیان میں۔",
                "تکیے کی اونچائی ایڈجسٹ کریں۔",
            ),
            enTips = listOf(
                "Pillow elevation is key.",
                "Strong upward thrusting angle.",
                "Hold legs gently on shoulders.",
            ),
            urTips = listOf(
                "تکیے کی اونچائی اہم ہے۔",
                "اوپر کی جھٹکوں کا زاویہ۔",
                "ٹانگیں کندھوں پر آہستہ رکھیں۔",
            )
        ),
        posture(
            id = "the_throne", categoryId = CAT_STANDING, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_the_throne,
            enName = "The Throne", urName = "تخت",
            enCat = "Standing & Seated", urCat = "کھڑے اور بیٹھے",
            enSummary = "Partner seated in chair — ideal for oral pleasure.",
            urSummary = "ساتھی کرسی پر بیٹھا — زبانی لطف کے لیے موزوں۔",
            enDesc = "Have partner sit in a chair with legs open. Ideal position for oral sex — helps partner relax and let go.",
            urDesc = "ساتھی کرسی پر ٹانگیں کھول کر بیٹھے۔ زبانی جنسیت کے لیے بہترین — آرام سے لطف اندوز ہوں۔",
            enSteps = listOf(
                "Partner sits in sturdy chair, legs apart.",
                "Kneel between their legs.",
                "Use hands on thighs for guidance.",
                "Maintain eye contact and check in.",
            ),
            urSteps = listOf(
                "ساتھی مضبوط کرسی پر ٹانگیں پھیلا کر بیٹھے۔",
                "ٹانگوں کے درمیان گھٹنے ٹیکیں۔",
                "رانوں پر ہاتھ رکھ کر رہنمائی کریں۔",
                "آنکھوں سے رابطہ رکھیں۔",
            ),
            enTips = listOf(
                "Chair provides stable support.",
                "Great for extended oral sessions.",
                "Partner can grip chair arms.",
            ),
            urTips = listOf(
                "کرسی مستحکم سہارا دیتی ہے۔",
                "لمبے زبانی سیشن کے لیے۔",
                "ساتھی کرسی کے بازو پکڑ سکتا ہے۔",
            )
        ),
        posture(
            id = "the_pretzel", categoryId = CAT_SIDE, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_the_pretzel,
            enName = "The Pretzel", urName = "پریٹزل",
            enCat = "Side by Side", urCat = "ساتھ ساتھ",
            enSummary = "Side-lying face-to-face with deep penetration.",
            urSummary = "سیدھے لیٹ کر آمنے سامنے گہری داخلہ۔",
            enDesc = "Deep penetration while face to face. Kneel and straddle partner's leg while they lie on their side, wrapping their leg around you.",
            urDesc = "آمنے سامنے گہری داخلہ۔ ساتھی کے پہلو پر گھٹنے ٹیک کر ان کی ٹانگ پر بیٹھیں۔",
            enSteps = listOf(
                "Bottom partner lies on left side.",
                "Top partner kneels, straddling their left leg.",
                "Bottom partner wraps right leg around top partner.",
                "Face each other and move slowly.",
            ),
            urSteps = listOf(
                "نیچے والا بائیں پہلو پر لیٹے۔",
                "اوپر والا گھٹنے ٹیک کر بائیں ٹانگ پر بیٹھے۔",
                "نیچے والا دائیں ٹانگ لپیٹے۔",
                "آمنے سامنے آہستہ حرکت کریں۔",
            ),
            enTips = listOf(
                "Face-to-face with depth.",
                "Requires some flexibility.",
                "Use pillow under bottom partner's head.",
            ),
            urTips = listOf(
                "آمنے سامنے گہرائی کے ساتھ۔",
                "تھوڑی لچک چاہیے۔",
                "سر کے نیچے تکیہ رکھیں۔",
            )
        ),
        posture(
            id = "the_shelf", categoryId = CAT_STANDING, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_the_shelf,
            enName = "The Shelf", urName = "شیلف",
            enCat = "Standing & Seated", urCat = "کھڑے اور بیٹھے",
            enSummary = "Partner's hips at bed edge for direct clitoral stimulation.",
            urSummary = "ساتھی کے کولہے بستر کے کنارے — براہ راست کلائیٹورل محرک۔",
            enDesc = "Partner leans butt on bed edge. Allows direct clitoral stimulation and a clear view. Hold tight for stability.",
            urDesc = "ساتھی کا کولہا بستر کے کنارے۔ براہ راست کلائیٹورل محرک اور واضح منظر۔ استحکام کے لیے مضبوط پکڑیں۔",
            enSteps = listOf(
                "Partner sits on bed edge, leaning back on hands.",
                "Stand or kneel between their legs.",
                "Hold their hips or thighs firmly.",
                "Adjust angle for clitoral contact.",
            ),
            urSteps = listOf(
                "ساتھی بستر کے کنارے ہاتھوں کے سہارے جھکے۔",
                "ٹانگوں کے درمیان کھڑے یا گھٹنے ٹیکیں۔",
                "کولہے یا رانیں مضبوط پکڑیں۔",
                "کلائیٹورل رابطے کے لیے زاویہ ایڈجسٹ کریں۔",
            ),
            enTips = listOf(
                "Direct clitoral stimulation.",
                "Partner supports weight on arms.",
                "Control depth with hip angle.",
            ),
            urTips = listOf(
                "براہ راست کلائیٹورل محرک۔",
                "ساتھی بازوؤں پر سہارا لے۔",
                "کولہے کے زاویے سے گہرائی کنٹرول کریں۔",
            )
        ),
        posture(
            id = "butter", categoryId = CAT_VARIATIONS, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_butter,
            enName = "Butter", urName = "مکھن",
            enCat = "Variations", urCat = "تبدیلیاں",
            enSummary = "Inverted angle increases blood flow to partner's head.",
            urSummary = "الٹا زاویہ سر میں خون کے بہاؤ کو بڑھاتا ہے۔",
            enDesc = "Extra blood flows to partner's head for increased ecstasy. Be careful not to rush — the angle can intensify sensations.",
            urDesc = "سر میں خون کا بہاؤ بڑھ کر لذت بڑھاتا ہے۔ جلدی نہ کریں — زاویہ احساسات بڑھا سکتا ہے۔",
            enSteps = listOf(
                "Partner lies on back near bed edge.",
                "Guide hips upward with pillow support.",
                "Position at an angle with head lower than hips.",
                "Move slowly and watch for dizziness.",
            ),
            urSteps = listOf(
                "ساتھی بستر کے کنارے پیٹھ کے بل۔",
                "تکیے سے کولہے اونچے کریں۔",
                "سر کولہے سے نیچے زاویے پر۔",
                "آہستہ حرکت کریں، چکر کا خیال رکھیں۔",
            ),
            enTips = listOf(
                "Intense sensations from blood flow.",
                "Limit duration in inverted angle.",
                "Stop if partner feels lightheaded.",
            ),
            urTips = listOf(
                "خون کے بہاؤ سے شدید احساس۔",
                "الٹے زاویے میں وقت محدود رکھیں۔",
                "چکر آئے تو رک جائیں۔",
            )
        ),
        posture(
            id = "wheelbarrow", categoryId = CAT_STANDING, difficulty = Difficulty.ADVANCED,
            illustrationRes = R.drawable.pic_wheelbarrow,
            enName = "Wheelbarrow", urName = "ہاتھ گاڑی",
            enCat = "Standing & Seated", urCat = "کھڑے اور بیٹھے",
            enSummary = "Athletic standing position — hold partner's legs while they support on hands.",
            urSummary = "کھڑی کھیلوں والی پوزیشن — ساتھی کے ہاتھ زمین پر، آپ ٹانگیں پکڑیں۔",
            enDesc = "Calorie-burning athletic position. Hold partner's hips while they support on hands. Lower the blinds — this one is adventurous!",
            urDesc = "مشقت والی کھڑی پوزیشن۔ ساتھی ہاتھوں پر سہارا لے، آپ کولہے پکڑیں۔",
            enSteps = listOf(
                "Partner places hands on floor, body angled down.",
                "Stand behind and lift their hips/legs.",
                "Support their weight carefully.",
                "Start with short holds and build strength.",
            ),
            urSteps = listOf(
                "ساتھی ہاتھ فرش پر، جسم نیچے جھکا۔",
                "پیچھے کھڑے کولہے/ٹانگیں اٹھائیں۔",
                "وزن احتیاط سے سنبھالیں۔",
                "چھوٹے عرصے سے شروع کریں۔",
            ),
            enTips = listOf(
                "Requires upper body strength.",
                "Not for beginners.",
                "Have a soft landing area nearby.",
            ),
            urTips = listOf(
                "اوپری جسم کی طاقت چاہیے۔",
                "شروع کرنے والوں کے لیے نہیں۔",
                "نرم سطح قریب رکھیں۔",
            )
        ),
        posture(
            id = "mountain_climber", categoryId = CAT_FACE, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_mountain_climber,
            enName = "Mountain Climber", urName = "پہاڑ چڑھنے والا",
            enCat = "Face to Face", urCat = "آمنے سامنے",
            enSummary = "Plank position over partner with great eye contact.",
            urSummary = "پلانک پوزیشن ساتھی کے اوپر — آنکھوں کا رابطہ۔",
            enDesc = "Athletic plank-style position over partner. Great eye contact and core engagement. Keep weight off partner's body.",
            urDesc = "پلانک انداز ساتھی کے اوپر۔ بہترین آنکھوں کا رابطہ۔ ساتھی پر وزن نہ ڈالیں۔",
            enSteps = listOf(
                "Partner lies on back.",
                "Position in plank above them, arms straight.",
                "Keep core engaged, weight on your arms.",
                "Make eye contact and move slowly.",
            ),
            urSteps = listOf(
                "ساتھی پیٹھ کے بل لیٹے۔",
                "اوپر پلانک میں بازو سیدھے۔",
                "کور ٹائٹ، وزن بازوؤں پر۔",
                "آنکھوں سے رابطہ، آہستہ حرکت۔",
            ),
            enTips = listOf(
                "Workout and intimacy combined.",
                "Requires arm strength.",
                "Don't collapse weight onto partner.",
            ),
            urTips = listOf(
                "ورزش اور قربت ایک ساتھ۔",
                "بازوؤں کی طاقت چاہیے۔",
                "ساتھی پر وزن نہ گرائیں۔",
            )
        ),
        posture(
            id = "spork", categoryId = CAT_SIDE, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_spork,
            enName = "Spork", urName = "سپورک",
            enCat = "Side by Side", urCat = "ساتھ ساتھ",
            enSummary = "Spoon-fork hybrid — partner raises one leg at 90 degrees.",
            urSummary = "چمچے اور کانٹے کا ملاپ — ساتھی ایک ٹانگ 90 ڈگری اٹھائے۔",
            enDesc = "Partner lies on back and raises right leg. Position between legs at 90 degrees. A natural bridge to more creative positions.",
            urDesc = "ساتھی پیٹھ کے بل ایک ٹانگ اٹھائے۔ 90 ڈگری زاویے پر درمیان میں آئیں۔",
            enSteps = listOf(
                "Partner lies on back, raises one leg.",
                "Position yourself between legs at right angle.",
                "Support raised leg on your shoulder or hip.",
                "Move gently at the new angle.",
            ),
            urSteps = listOf(
                "ساتھی پیٹھ کے بل ایک ٹانگ اٹھائے۔",
                "90 ڈگری پر درمیان میں آئیں۔",
                "اٹی ٹانگ کندھے یا کولہے پر سہارا دیں۔",
                "نئے زاویے پر آہستہ حرکت۔",
            ),
            enTips = listOf(
                "Bridge to creative positions.",
                "Try both legs raised for variety.",
                "Great side-entry angle.",
            ),
            urTips = listOf(
                "تخلیقی پوزیشنز کی طرف پل۔",
                "دونوں ٹانگیں اٹھا کر آزمائیں۔",
                "بہترین پہلو سے داخلہ۔",
            )
        ),
        posture(
            id = "the_x", categoryId = CAT_SIDE, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_the_x,
            enName = "The X", urName = "ایکس",
            enCat = "Side by Side", urCat = "ساتھ ساتھ",
            enSummary = "Seated facing each other with legs crossed — slow and sensual.",
            urSummary = "آمنے سامنے بیٹھ کر ٹانگیں ملائے — آہستہ اور حسین۔",
            enDesc = "Sit on bed facing each other with legs intertwined in an X. Ideal for slow, prolonged sessions. Shallow thrusts stimulate nerve endings.",
            urDesc = "بستر پر آمنے سامنے بیٹھ کر ٹانگیں ایکس میں ملائیں۔ آہستہ لمبے سیشن کے لیے بہترین۔",
            enSteps = listOf(
                "Both sit facing each other on bed.",
                "Cross and intertwine legs.",
                "Hold each other for balance.",
                "Rock together slowly.",
            ),
            urSteps = listOf(
                "دونوں بستر پر آمنے سامنے بیٹھیں۔",
                "ٹانگیں ملائیں۔",
                "توازن کے لیے ایک دوسرے کو پکڑیں۔",
                "آہستہ ساتھ ہلیں۔",
            ),
            enTips = listOf(
                "Slow and sensual.",
                "Shallow movements build excitement.",
                "Excellent for eye contact.",
            ),
            urTips = listOf(
                "آہستہ اور حسین۔",
                "ہلکی حرکتیں جوش بڑھائیں۔",
                "آنکھوں کا رابطہ بہترین۔",
            )
        ),
        posture(
            id = "angel_of_snows", categoryId = CAT_VARIATIONS, difficulty = Difficulty.ADVANCED,
            illustrationRes = R.drawable.pic_angel_of_snows,
            enName = "Angel of Snows", urName = "برف کا فرشتہ",
            enCat = "Variations", urCat = "تبدیلیاں",
            enSummary = "Reverse straddle with legs wrapped — challenging circus position.",
            urSummary = "الٹ اوپر بیٹھنا، ٹانگیں لپیٹنا — مشکل پوزیشن۔",
            enDesc = "Partner lies on back while you straddle facing away. Raise legs and wrap around your back. Challenging but rewarding.",
            urDesc = "ساتھی پیٹھ کے بل، آپ الٹ اوپر بیٹھیں۔ ٹانگیں اٹھا کر کمر کے گرد لپیٹیں۔",
            enSteps = listOf(
                "Partner lies flat on back.",
                "Straddle facing away from their face.",
                "Partner raises legs and wraps around your back.",
                "Support with hands on their thighs.",
            ),
            urSteps = listOf(
                "ساتھی پیٹھ کے بل لیٹے۔",
                "منہ دوسری طرف اوپر بیٹھیں۔",
                "ساتھی ٹانگیں اٹھا کر کمر لپیٹے۔",
                "رانوں پر ہاتھ سے سہارا لیں۔",
            ),
            enTips = listOf(
                "Challenging — take your time.",
                "Requires flexibility from both.",
                "Communicate about leg pressure.",
            ),
            urTips = listOf(
                "مشکل — وقت لیں۔",
                "دونوں کو لچک چاہیے۔",
                "ٹانگوں کے دباؤ کے بارے میں بات کریں۔",
            )
        ),
        posture(
            id = "the_spider", categoryId = CAT_FACE, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_the_spider,
            enName = "The Spider", urName = "مکڑی",
            enCat = "Face to Face", urCat = "آمنے سامنے",
            enSummary = "Both seated facing each other, leaning back on arms.",
            urSummary = "دونوں آمنے سامنے بیٹھے، بازوؤں کے سہارے پیچھے جھکے۔",
            enDesc = "Both sit on bed facing each other with legs toward each other, arms back for support. Move together with knees bent.",
            urDesc = "دونوں بستر پر آمنے سامنے، ٹانگیں ایک دوسرے کی طرف، بازو پیچھے سہارے۔ گھٹنے موڑ کر ساتھ حرکت۔",
            enSteps = listOf(
                "Sit facing each other on bed.",
                "Place hands behind you for support.",
                "Bring knees together, feet flat.",
                "Rock hips forward and back together.",
            ),
            urSteps = listOf(
                "بستر پر آمنے سامنے بیٹھیں۔",
                "سہارے کے لیے ہاتھ پیچھے رکھیں۔",
                "گھٹنے ملائیں، پاؤں فرش پر۔",
                "کولہے آگے پیچھے ساتھ ہلائیں۔",
            ),
            enTips = listOf(
                "Unique seated angle.",
                "Arms provide leverage.",
                "Great for slow grinding.",
            ),
            urTips = listOf(
                "منفرد بیٹھی ہوئی زاویہ۔",
                "بازو بلی کا فائدہ۔",
                "آہستہ رگڑ کے لیے بہترین۔",
            )
        ),
        posture(
            id = "the_standard", categoryId = CAT_STANDING, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_the_standard,
            enName = "The Standard", urName = "معیاری",
            enCat = "Standing & Seated", urCat = "کھڑے اور بیٹھے",
            enSummary = "Standing oral position — ideal for cunnilingus.",
            urSummary = "کھڑے زبانی — کنی لنگس کے لیے موزوں۔",
            enDesc = "On your knees while partner stands. Ideal for clitoral stimulation, rubbing, digital penetration, and G-spot access.",
            urDesc = "گھٹنے ٹیکیں، ساتھی کھڑا ہو۔ کلائیٹورل، رگڑ، انگلی اور جی سپاٹ کے لیے بہترین۔",
            enSteps = listOf(
                "Partner stands with feet shoulder-width apart.",
                "Kneel in front of them.",
                "Use hands on thighs or hips for guidance.",
                "Alternate mouth, fingers, and rhythm.",
            ),
            urSteps = listOf(
                "ساتھی کھڑا ہو، پاؤں کندھوں کے برابر۔",
                "سامنے گھٹنے ٹیکیں۔",
                "رانوں یا کولہے پر ہاتھ رکھیں۔",
                "منہ، انگلیاں اور تال بدلتے رہیں۔",
            ),
            enTips = listOf(
                "Versatile for oral techniques.",
                "Partner can hold your head gently.",
                "Try one leg over your shoulder.",
            ),
            urTips = listOf(
                "زبانی تکنیکوں کے لیے لچکدار۔",
                "ساتھی سر آہستہ پکڑ سکتا ہے۔",
                "ایک ٹانگ کندھے پر رکھیں آزمائیں۔",
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
