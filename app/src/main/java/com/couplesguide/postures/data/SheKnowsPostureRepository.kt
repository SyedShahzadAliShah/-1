package com.couplesguide.postures.data

import com.couplesguide.postures.R

/** Auto-generated from SheKnows 69-position slideshow. Do not edit by hand. */
object SheKnowsPostureRepository {

    const val CAT_ALL = "all"
    const val CAT_CLASSIC = "classic"
    const val CAT_NON_PENETRATIVE = "non_penetrative"
    const val CAT_ELEVATED = "elevated"
    const val CAT_SHOWER = "shower"
    const val CAT_BONDAGE = "bondage"
    const val CAT_CAR = "car"
    const val CAT_SOLO = "solo"
    const val CAT_FLAT = "flat"
    const val CAT_BLINDFOLD = "blindfold"
    const val CAT_ANAL = "anal"
    const val CAT_BEACH = "beach"
    const val CAT_ORGASM = "orgasm"
    const val CAT_CREATIVE = "creative"
    const val CAT_IMAGINATION = "imagination"
    const val SOURCE_URL = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/"

    private val categoryLabels = mapOf(
        CAT_ALL to ("All" to "سب"),
        CAT_CLASSIC to ("Classic" to "کلاسک"),
        CAT_NON_PENETRATIVE to ("Non-Penetrative" to "غیر داخلی"),
        CAT_ELEVATED to ("Elevated" to "اونچی سطح"),
        CAT_SHOWER to ("Shower" to "شاور"),
        CAT_BONDAGE to ("Bondage" to "بندھن"),
        CAT_CAR to ("Car" to "گاڑی"),
        CAT_SOLO to ("Solo / Masturbation" to "اکیلے"),
        CAT_FLAT to ("Flat" to "سیدھے لیٹ کر"),
        CAT_BLINDFOLD to ("Blindfolded" to "آنکھوں پر پٹی"),
        CAT_ANAL to ("Anal Variations" to "پیچھے سے متبادل"),
        CAT_BEACH to ("Beach-Inspired" to "ساحل"),
        CAT_ORGASM to ("For Vaginal Orgasm" to "اندام نہانی لطف"),
        CAT_CREATIVE to ("Creative" to "تخلیقی"),
        CAT_IMAGINATION to ("Imagination" to "تخیل")
    )

    fun getCategoryIds(): List<String> = listOf(
        CAT_ALL, CAT_CLASSIC, CAT_NON_PENETRATIVE, CAT_ELEVATED, CAT_SHOWER, CAT_BONDAGE, CAT_CAR, CAT_SOLO, CAT_FLAT, CAT_BLINDFOLD, CAT_ANAL, CAT_BEACH, CAT_ORGASM, CAT_CREATIVE, CAT_IMAGINATION
    )

    fun getCategoryLabel(categoryId: String, language: String): String {
        val labels = categoryLabels[categoryId] ?: return categoryId
        return if (language == "ur") labels.second else labels.first
    }

    fun getSheKnowsPostures(): List<Posture> = postures

    private val postures: List<Posture> = listOf(
        Posture(
            id = "sk_cat",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_cat,
            categoryId = CAT_CLASSIC,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Modified Coital-Alignment Technique",
                category = "Classic",
                summary = "Face-to-face with upward grinding instead of thrusting.",
                description = "An upgraded missionary where the penetrating partner shifts weight forward so contact presses along the external vulva and clitoris while moving in circles rather than in and out.",
                steps = listOf(
                    "Receiving partner lies on back.",
                    "Penetrating partner enters from above.",
                    "Shift weight forward — avoid deep thrusting.",
                    "Move hips in slow circles.",
                    "Receiver tilts hips and wraps legs as comfortable.",
                ),
                tips = listOf(
                    "Massages G-spot and clitoris together.",
                    "Great for couples wanting more clitoral contact.",
                    "Communicate about hip angle.",
                ),
                forMan = PartnerRole(
                    position = "On top, weight forward, circular hip motion",
                    guidance = listOf(
                            "Position: On top, weight forward, circular hip motion",
                            "Massages G-spot and clitoris together.",
                            "Receiving partner lies on back.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "On back, experiment with hip tilt and leg wrap",
                    guidance = listOf(
                            "Position: On back, experiment with hip tilt and leg wrap",
                            "Great for couples wanting more clitoral contact.",
                            "Penetrating partner enters from above.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "ترمیم شدہ CAT مشنری",
                category = "کلاسک",
                summary = "آمنے سامنے، جھٹکوں کی بجائے اوپر نیچے رگڑ۔",
                description = "بہتر مشنری جہاں اوپر والا وزن آگے رکھے تاکہ کلائٹورس اور بیرونی حصے پر دباؤ آئے اور گول حرکت کرے۔",
                steps = listOf(
                    "سامنے والا پیٹ کے بل لیٹے۔",
                    "دوسرا اوپر سے داخل ہو۔",
                    "وزن آگے رکھیں — گہری جھٹکوں سے بچیں۔",
                    "کولہے آہستہ گول گھمائیں۔",
                    "لیٹا والا کولہے کا زاویہ بدلے۔",
                ),
                tips = listOf(
                    "جی سپاٹ اور کلائٹورس ساتھ محرک ہوتے ہیں۔",
                    "زیادہ کلائٹورل رابطے کے لیے بہترین۔",
                    "کولہے کے زاویے پر بات کریں۔",
                ),
                forMan = PartnerRole(
                    position = "اوپر، وزن آگے، گول حرکت",
                    guidance = listOf(
                            "پوزیشن: اوپر، وزن آگے، گول حرکت",
                            "جی سپاٹ اور کلائٹورس ساتھ محرک ہوتے ہیں۔",
                            "سامنے والا پیٹ کے بل لیٹے۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "پیٹ کے بل، کولہے اور ٹانگیں ایڈجسٹ کریں",
                    guidance = listOf(
                            "پوزیشن: پیٹ کے بل، کولہے اور ٹانگیں ایڈجسٹ کریں",
                            "زیادہ کلائٹورل رابطے کے لیے بہترین۔",
                            "دوسرا اوپر سے داخل ہو۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_doggy",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_doggy,
            categoryId = CAT_CLASSIC,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Doggy Style",
                category = "Classic",
                summary = "Receiving partner on all fours; partner enters from behind.",
                description = "Classic rear-entry position. The receiving partner gets on all fours while the penetrating partner kneels or stands behind. Allows cat-cow pelvic movement and manual stimulation.",
                steps = listOf(
                    "Receiver gets on hands and knees.",
                    "Partner kneels or stands behind.",
                    "Receiver cat-cows pelvis for pressure.",
                    "Partner grips hips as both prefer.",
                    "Adjust depth and pace together.",
                ),
                tips = listOf(
                    "Access to G-spot or A-spot by angle.",
                    "Receiver can stimulate clitoris by hand.",
                    "Try flat doggy or wheelbarrow variations.",
                ),
                forMan = PartnerRole(
                    position = "Behind receiver, kneeling or standing",
                    guidance = listOf(
                            "Position: Behind receiver, kneeling or standing",
                            "Access to G-spot or A-spot by angle.",
                            "Receiver gets on hands and knees.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "On all fours, control depth with hip shift",
                    guidance = listOf(
                            "Position: On all fours, control depth with hip shift",
                            "Receiver can stimulate clitoris by hand.",
                            "Partner kneels or stands behind.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "ڈوگی سٹائل",
                category = "کلاسک",
                summary = "سامنے والا چاروں پر، پیچھے سے داخلہ۔",
                description = "کلاسک پیچھے سے پوزیشن۔ سامنے والا ہاتھ گھٹنوں پر، دوسرا پیچھے سے۔ کولہے کی حرکت اور ہاتھ سے محرک ممکن۔",
                steps = listOf(
                    "سامنے والا ہاتھ گھٹنوں پر آئے۔",
                    "ساتھی پیچھے گھٹنوں یا کھڑے ہو۔",
                    "کولہے آگے پیچھے ہلائیں۔",
                    "کولہے پکڑیں جیسا آرام ہو۔",
                    "گہرائی اور رفتار ساتھ طے کریں۔",
                ),
                tips = listOf(
                    "زاویے سے جی یا اے سپاٹ تک رسائی۔",
                    "ہاتھ سے کلائٹورل محرک۔",
                    "فلیٹ ڈوگی یا وہیل بیرو آزمائیں۔",
                ),
                forMan = PartnerRole(
                    position = "پیچھے، گھٹنوں یا کھڑے",
                    guidance = listOf(
                            "پوزیشن: پیچھے، گھٹنوں یا کھڑے",
                            "زاویے سے جی یا اے سپاٹ تک رسائی۔",
                            "سامنے والا ہاتھ گھٹنوں پر آئے۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "چاروں پر، کولہے سے گہرائی کنٹرول",
                    guidance = listOf(
                            "پوزیشن: چاروں پر، کولہے سے گہرائی کنٹرول",
                            "ہاتھ سے کلائٹورل محرک۔",
                            "ساتھی پیچھے گھٹنوں یا کھڑے ہو۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_pushing_tush",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_pushing_tush,
            categoryId = CAT_CLASSIC,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Pushing Tush",
                category = "Classic",
                summary = "Face-to-face missionary with anal entry.",
                description = "Missionary position with anal rather than vaginal entry. Use a pillow under hips and plenty of lubricant.",
                steps = listOf(
                    "Assume missionary alignment.",
                    "Place pillow under receiver's hips.",
                    "Apply generous lubricant inside and out.",
                    "Enter slowly watching facial cues.",
                    "Receiver tilts hips to open anal canal.",
                ),
                tips = listOf(
                    "Lube is essential — anal canal is not self-lubricating.",
                    "Face-to-face allows comfort reading.",
                    "Consider vibrating plug for dual stimulation.",
                ),
                forMan = PartnerRole(
                    position = "On top, slow face-to-face anal entry",
                    guidance = listOf(
                            "Position: On top, slow face-to-face anal entry",
                            "Lube is essential — anal canal is not self-lubricating.",
                            "Assume missionary alignment.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "On back with hip pillow, guide pace verbally",
                    guidance = listOf(
                            "Position: On back with hip pillow, guide pace verbally",
                            "Face-to-face allows comfort reading.",
                            "Place pillow under receiver's hips.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "پشنگ ٹش",
                category = "کلاسک",
                summary = "آمنے سامنے مشنری، پیچھے سے داخلہ۔",
                description = "مشنری پوزیشن میں پیچھے سے داخلہ۔ کولہے کے نیچے تکیہ اور کافی لوبریکنٹ استعمال کریں۔",
                steps = listOf(
                    "مشنری کی پوزیشن لیں۔",
                    "کولہے کے نیچے تکیہ رکھیں۔",
                    "اندر باہر لوبریکنٹ لگائیں۔",
                    "آہستہ داخل ہوں، چہرے کے اشارے دیکھیں۔",
                    "کولہے کا زاویہ کھولیں۔",
                ),
                tips = listOf(
                    "لوبریکنٹ ضروری ہے۔",
                    "آمنے سامنے آرام پڑھنا آسان ہے۔",
                    "دگہری محرک کے لیے وائبریٹنگ پلگ آزمائیں۔",
                ),
                forMan = PartnerRole(
                    position = "اوپر، آہستہ آمنے سامنے",
                    guidance = listOf(
                            "پوزیشن: اوپر، آہستہ آمنے سامنے",
                            "لوبریکنٹ ضروری ہے۔",
                            "مشنری کی پوزیشن لیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "تکیے کے ساتھ پیٹ کے بل، رفتار بتائیں",
                    guidance = listOf(
                            "پوزیشن: تکیے کے ساتھ پیٹ کے بل، رفتار بتائیں",
                            "آمنے سامنے آرام پڑھنا آسان ہے۔",
                            "کولہے کے نیچے تکیہ رکھیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_rocking_horse",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_rocking_horse,
            categoryId = CAT_CLASSIC,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Rocking Horse",
                category = "Classic",
                summary = "Receiver sits between partner's legs; both rock together.",
                description = "Seated face-to-face with intimate eye contact. Receiver sits between penetrating partner's legs with legs nearly wrapped around them.",
                steps = listOf(
                    "Penetrating partner sits with legs extended.",
                    "Receiver sits between their legs.",
                    "Wrap legs loosely around partner.",
                    "Rock hips together to control depth.",
                    "Hold each other close.",
                ),
                tips = listOf(
                    "Excellent G-spot stimulation.",
                    "Can be gentle or passionate.",
                    "Control depth by rocking rhythm.",
                ),
                forMan = PartnerRole(
                    position = "Seated base, supports receiver while rocking",
                    guidance = listOf(
                            "Position: Seated base, supports receiver while rocking",
                            "Excellent G-spot stimulation.",
                            "Penetrating partner sits with legs extended.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Sits on lap between legs, sets rocking pace",
                    guidance = listOf(
                            "Position: Sits on lap between legs, sets rocking pace",
                            "Can be gentle or passionate.",
                            "Receiver sits between their legs.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "راکنگ ہارس",
                category = "کلاسک",
                summary = "سامنے والا ساتھی کی ٹانگوں کے درمیان بیٹھے؛ دونوں ساتھ جھولیں۔",
                description = "بیٹھ کر آمنے سامنے، آنکھوں کا رابطہ۔ سامنے والا ساتھی کی ٹانگوں کے بیچ بیٹھے۔",
                steps = listOf(
                    "ساتھی بیٹھے ٹانگیں پھیلائے۔",
                    "سامنے والا درمیان میں بیٹھے۔",
                    "ٹانگیں ہلکے لپیٹیں۔",
                    "کولہے ساتھ جھولائیں۔",
                    "قریب رہیں۔",
                ),
                tips = listOf(
                    "جی سپاٹ محرک بہترین۔",
                    "نرم یا پرجوش دونوں ہو سکتا ہے۔",
                    "جھولنے کی تال سے گہرائی کنٹرول۔",
                ),
                forMan = PartnerRole(
                    position = "بیٹھے، سہارا دے کر جھولیں",
                    guidance = listOf(
                            "پوزیشن: بیٹھے، سہارا دے کر جھولیں",
                            "جی سپاٹ محرک بہترین۔",
                            "ساتھی بیٹھے ٹانگیں پھیلائے۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "گود میں بیٹھ کر تال طے کریں",
                    guidance = listOf(
                            "پوزیشن: گود میں بیٹھ کر تال طے کریں",
                            "نرم یا پرجوش دونوں ہو سکتا ہے۔",
                            "سامنے والا درمیان میں بیٹھے۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_seated_scissors",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_seated_scissors,
            categoryId = CAT_CLASSIC,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Seated Scissors",
                category = "Classic",
                summary = "Playful reverse-cowgirl variation on a bent leg.",
                description = "Penetrating partner lies back with one leg bent. Receiver straddles the bent leg and arranges legs comfortably on top.",
                steps = listOf(
                    "Partner lies on back, one knee bent.",
                    "Receiver straddles bent leg.",
                    "Arrange top legs for comfort.",
                    "Bounce, bump, or grind.",
                    "Bottom partner relaxes and enjoys the view.",
                ),
                tips = listOf(
                    "Fun for both partners.",
                    "Receiver controls most movement.",
                    "Plenty of room to experiment.",
                ),
                forMan = PartnerRole(
                    position = "Lies back with one leg bent as anchor",
                    guidance = listOf(
                            "Position: Lies back with one leg bent as anchor",
                            "Fun for both partners.",
                            "Partner lies on back, one knee bent.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Straddles bent leg, controls bounce and grind",
                    guidance = listOf(
                            "Position: Straddles bent leg, controls bounce and grind",
                            "Receiver controls most movement.",
                            "Receiver straddles bent leg.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "بیٹھی قینچی",
                category = "کلاسک",
                summary = "موڑی ہوئی ٹانگ پر الٹ کاؤگرل جیسی تفریحی پوزیشن۔",
                description = "نیچے والا پیٹ کے بل ایک ٹانگ موڑے۔ اوپر والا موڑی ٹانگ پر بیٹھے۔",
                steps = listOf(
                    "نیچے والا پیٹ کے بل، ایک گھٹنا موڑے۔",
                    "اوپر والا اس ٹانگ پر بیٹھے۔",
                    "ٹانگیں آرام سے رکھیں۔",
                    "اچھلیں یا رگڑیں۔",
                    "نیچے والا آرام کرے۔",
                ),
                tips = listOf(
                    "دونوں کے لیے مزیدار۔",
                    "اوپر والا حرکت کنٹرول کرے۔",
                    "تجربے کی گنجائش زیادہ۔",
                ),
                forMan = PartnerRole(
                    position = "پیٹ کے بل، ایک ٹانگ موڑی",
                    guidance = listOf(
                            "پوزیشن: پیٹ کے بل، ایک ٹانگ موڑی",
                            "دونوں کے لیے مزیدار۔",
                            "نیچے والا پیٹ کے بل، ایک گھٹنا موڑے۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "موڑی ٹانگ پر بیٹھ کر حرکت کریں",
                    guidance = listOf(
                            "پوزیشن: موڑی ٹانگ پر بیٹھ کر حرکت کریں",
                            "اوپر والا حرکت کنٹرول کرے۔",
                            "اوپر والا اس ٹانگ پر بیٹھے۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_spooning",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_spooning,
            categoryId = CAT_CLASSIC,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Spooning",
                category = "Classic",
                summary = "Side-by-side rear entry like cuddling spoons.",
                description = "Big spoon enters from behind while both lie on their sides. Ultra-intimate with free hands for touch and clitoral stimulation.",
                steps = listOf(
                    "Both lie on sides, same direction.",
                    "Big spoon curls behind little spoon.",
                    "Enter vaginally or anally from behind.",
                    "Use free hands for touch.",
                    "Move slowly — easy to snuggle after.",
                ),
                tips = listOf(
                    "Great for slow mornings.",
                    "Remember to urinate after sex.",
                    "Hands free for clitoral play.",
                ),
                forMan = PartnerRole(
                    position = "Big spoon behind, enters gently",
                    guidance = listOf(
                            "Position: Big spoon behind, enters gently",
                            "Great for slow mornings.",
                            "Both lie on sides, same direction.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Little spoon in front, guides with hips and hand",
                    guidance = listOf(
                            "Position: Little spoon in front, guides with hips and hand",
                            "Remember to urinate after sex.",
                            "Big spoon curls behind little spoon.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "چمچے والی",
                category = "کلاسک",
                summary = "ساتھ لیٹ کر پیچھے سے، گلے ملنے جیسا۔",
                description = "پیچھے والا سیدھے لیٹ کر پیچھے سے داخل ہو۔ ہاتھ آزاد چھونے کے لیے۔",
                steps = listOf(
                    "دونوں ایک سمت سیدھے لیٹیں۔",
                    "پیچھے والا آگے والے کے پیچھے۔",
                    "آہستہ داخل ہوں۔",
                    "ہاتھ سے محرک دیں۔",
                    "بعد میں گلے مل سکتے ہیں۔",
                ),
                tips = listOf(
                    "صبح کی آرام دہ قربت کے لیے بہترین۔",
                    "بعد میں پیشاب کریں۔",
                    "ہاتھ سے کلائٹورل لطف۔",
                ),
                forMan = PartnerRole(
                    position = "پیچھے سے آہستہ داخل ہوں",
                    guidance = listOf(
                            "پوزیشن: پیچھے سے آہستہ داخل ہوں",
                            "صبح کی آرام دہ قربت کے لیے بہترین۔",
                            "دونوں ایک سمت سیدھے لیٹیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "سامنے لیٹیں، کولہے اور ہاتھ سے رہنمائی",
                    guidance = listOf(
                            "پوزیشن: سامنے لیٹیں، کولہے اور ہاتھ سے رہنمائی",
                            "بعد میں پیشاب کریں۔",
                            "پیچھے والا آگے والے کے پیچھے۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_scissoring",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_scissoring,
            categoryId = CAT_CLASSIC,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Scissoring",
                category = "Classic",
                summary = "Genital-to-genital grinding for any gender pairing.",
                description = "Partners lie with heads opposite, straddling legs to grind pubic areas together. Focus is external stimulation, not penetration.",
                steps = listOf(
                    "Lie with heads at opposite ends.",
                    "Straddle each other's legs.",
                    "Grind calves, knees, or genitals together.",
                    "Or shimmy until genital contact.",
                    "Find rhythm that feels good.",
                ),
                tips = listOf(
                    "Penetration isn't required for great sex.",
                    "Lower STI risk without genital contact variant.",
                    "Works across body types.",
                ),
                forMan = PartnerRole(
                    position = "Grinds with partner at chosen angle",
                    guidance = listOf(
                            "Position: Grinds with partner at chosen angle",
                            "Penetration isn't required for great sex.",
                            "Lie with heads at opposite ends.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Controls pressure and grinding rhythm",
                    guidance = listOf(
                            "Position: Controls pressure and grinding rhythm",
                            "Lower STI risk without genital contact variant.",
                            "Straddle each other's legs.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "سیزرنگ",
                category = "کلاسک",
                summary = "کسی بھی جوڑے کے لیے رگڑ کر خارجی محرک۔",
                description = "سر مخالف سمت، ٹانگیں ملاکر عضو ٹھانیوں کو رگڑیں۔ داخلہ نہیں، خارجی لطف۔",
                steps = listOf(
                    "سر مخالف سمت لیٹیں۔",
                    "ٹانگیں ایک دوسرے پر رکھیں۔",
                    "رانوں یا عضو ٹھانی رگڑیں۔",
                    "جب رابطہ ہو تو تال بنائیں۔",
                    "آرام دہ رفتار تلاش کریں۔",
                ),
                tips = listOf(
                    "داخلہ ضروری نہیں۔",
                    "بغیر رابطے والے متبادل میں کم خطرہ۔",
                    "ہر جسم کے لیے موزوں۔",
                ),
                forMan = PartnerRole(
                    position = "ساتھی کے ساتھ زاویے پر رگڑیں",
                    guidance = listOf(
                            "پوزیشن: ساتھی کے ساتھ زاویے پر رگڑیں",
                            "داخلہ ضروری نہیں۔",
                            "سر مخالف سمت لیٹیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "دباؤ اور رفتار کنٹرول کریں",
                    guidance = listOf(
                            "پوزیشن: دباؤ اور رفتار کنٹرول کریں",
                            "بغیر رابطے والے متبادل میں کم خطرہ۔",
                            "ٹانگیں ایک دوسرے پر رکھیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_bend_over",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_bend_over,
            categoryId = CAT_CLASSIC,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Bend Over, Baby",
                category = "Classic",
                summary = "90-degree bend for shallow penetration.",
                description = "Receiver bends at 90 degrees. Ideal when a smaller penis needs to feel fuller through angle and pelvic tilt.",
                steps = listOf(
                    "Receiver bends forward at waist.",
                    "Keep back relatively flat.",
                    "Tilt pelvis to find hot spots.",
                    "Partner enters from behind.",
                    "Adjust angle together.",
                ),
                tips = listOf(
                    "Shallow penetration can feel intense.",
                    "Great for targeted stimulation.",
                    "Communicate about depth.",
                ),
                forMan = PartnerRole(
                    position = "Enters from behind at bent angle",
                    guidance = listOf(
                            "Position: Enters from behind at bent angle",
                            "Shallow penetration can feel intense.",
                            "Receiver bends forward at waist.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Bent at 90°, tilts pelvis for sensation",
                    guidance = listOf(
                            "Position: Bent at 90°, tilts pelvis for sensation",
                            "Great for targeted stimulation.",
                            "Keep back relatively flat.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "جھک جاؤ بیبی",
                category = "کلاسک",
                summary = "نوے ڈگری جھکاؤ، کم گہرائی۔",
                description = "سامنے والا نوے ڈگری جھکے۔ چھوٹے سائز کے لیے زاویہ بہتر بناتا ہے۔",
                steps = listOf(
                    "کمر سے آگے جھکیں۔",
                    "پیٹھ سیدھی رکھیں۔",
                    "کولہے کا زاویہ بدلیں۔",
                    "پیچھے سے داخل ہوں۔",
                    "زاویہ ساتھ مل کر ٹھیک کریں۔",
                ),
                tips = listOf(
                    "کم گہرائی بھی شدید محسوس ہو سکتی ہے۔",
                    "مخصوص محرک کے لیے اچھا۔",
                    "گہرائی پر بات کریں۔",
                ),
                forMan = PartnerRole(
                    position = "جھکے ہوئے پیچھے سے",
                    guidance = listOf(
                            "پوزیشن: جھکے ہوئے پیچھے سے",
                            "کم گہرائی بھی شدید محسوس ہو سکتی ہے۔",
                            "کمر سے آگے جھکیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "نوے ڈگری جھکیں، کولہے ہلائیں",
                    guidance = listOf(
                            "پوزیشن: نوے ڈگری جھکیں، کولہے ہلائیں",
                            "مخصوص محرک کے لیے اچھا۔",
                            "پیٹھ سیدھی رکھیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_scissors_classic",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_scissors_classic,
            categoryId = CAT_CLASSIC,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Scissors (Side)",
                category = "Classic",
                summary = "Side-lying facing each other for thicker anatomy.",
                description = "Partners lie on sides facing each other with heads on opposite bed sides. Receiver straddles a leg for comfortable penetration.",
                steps = listOf(
                    "Lie on sides facing each other.",
                    "Heads on opposite sides of bed.",
                    "Receiver straddles partner's leg.",
                    "Lift one leg to open for entry.",
                    "Use friction and close contact.",
                ),
                tips = listOf(
                    "Good for thicker penis comfort.",
                    "Creates friction and closeness.",
                    "Fireworks from start to finish.",
                ),
                forMan = PartnerRole(
                    position = "Lies on side, provides stable leg for straddle",
                    guidance = listOf(
                            "Position: Lies on side, provides stable leg for straddle",
                            "Good for thicker penis comfort.",
                            "Lie on sides facing each other.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Straddles leg, controls angle of entry",
                    guidance = listOf(
                            "Position: Straddles leg, controls angle of entry",
                            "Creates friction and closeness.",
                            "Heads on opposite sides of bed.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "قینچی (سیدھے)",
                category = "کلاسک",
                summary = "آمنے سامنے سیدھے، موٹے سائز کے لیے۔",
                description = "دونوں سیدھے آمنے سامنے، سر بستر کے مخالف کناروں پر۔ ایک ٹانگ پر بیٹھ کر داخلہ۔",
                steps = listOf(
                    "سیدھے آمنے سامنے لیٹیں۔",
                    "سر مخالف سمت۔",
                    "ساتھی کی ٹانگ پر بیٹھیں۔",
                    "ایک ٹانگ اٹھا کر کھولیں۔",
                    "رگڑ اور قربت استعمال کریں۔",
                ),
                tips = listOf(
                    "موٹے سائز کے لیے آرام دہ۔",
                    "رگڑ اور قربت بڑھتی ہے۔",
                    "شروع سے لطف۔",
                ),
                forMan = PartnerRole(
                    position = "سیدھے لیٹیں، ٹانگ سہارا دے",
                    guidance = listOf(
                            "پوزیشن: سیدھے لیٹیں، ٹانگ سہارا دے",
                            "موٹے سائز کے لیے آرام دہ۔",
                            "سیدھے آمنے سامنے لیٹیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "ٹانگ پر بیٹھ کر زاویہ کنٹرول",
                    guidance = listOf(
                            "پوزیشن: ٹانگ پر بیٹھ کر زاویہ کنٹرول",
                            "رگڑ اور قربت بڑھتی ہے۔",
                            "سر مخالف سمت۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_uncloak",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_uncloak,
            categoryId = CAT_NON_PENETRATIVE,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Uncloak the Clitoris",
                category = "Non-Penetrative",
                summary = "Manual clitoral focus with communication.",
                description = "Hands-only position focusing on glans clitoris stimulation with partner communication about touch style.",
                steps = listOf(
                    "Ask what touch they prefer.",
                    "Try tapping, pressing, or circling.",
                    "Some need indirect touch through labia.",
                    "Stay attuned to feedback.",
                    "Build rhythm together.",
                ),
                tips = listOf(
                    "70% of women need clitoral stimulation.",
                    "Encourages bedroom communication.",
                    "No penetration required.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "70% of women need clitoral stimulation.",
                            "Ask what touch they prefer.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Encourages bedroom communication.",
                            "Try tapping, pressing, or circling.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "کلائٹورس کو بے نقاب کریں",
                category = "غیر داخلی",
                summary = "ہاتھ سے کلائٹورل محرک، بات چیت کے ساتھ۔",
                description = "ہاتھ سے کلائٹورس کی نوک کو محرک دینا، ساتھی سے پوچھ کر طریقہ طے کرنا۔",
                steps = listOf(
                    "پوچھیں کون سا چھونا پسند ہے۔",
                    "تپ، دباؤ یا گول گھماؤ آزمائیں۔",
                    "کچھ کو بالوں کے ذریعے نرم چھونا چاہیے۔",
                    "ردعمل دیکھتے رہیں۔",
                    "تال ساتھ بنائیں۔",
                ),
                tips = listOf(
                    "زیادہ تر خواتین کو کلائٹورل محرک چاہیے۔",
                    "بات چیت بڑھاتی ہے۔",
                    "داخلہ ضروری نہیں۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "زیادہ تر خواتین کو کلائٹورل محرک چاہیے۔",
                            "پوچھیں کون سا چھونا پسند ہے۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "بات چیت بڑھاتی ہے۔",
                            "تپ، دباؤ یا گول گھماؤ آزمائیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_scepter",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_scepter,
            categoryId = CAT_NON_PENETRATIVE,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Baring the Scepter",
                category = "Non-Penetrative",
                summary = "DIY vibrating ring with fingers at penis base.",
                description = "Partner forms thumb-forefinger ring at penis base and pulls slightly during intercourse for firmer erection.",
                steps = listOf(
                    "Form ring at penis base.",
                    "Pull skin taut gently.",
                    "Maintain during intercourse if possible.",
                    "Communicate pressure level.",
                    "Alternative to store-bought ring.",
                ),
                tips = listOf(
                    "Slows blood flow for harder erection.",
                    "No toy required.",
                    "Rock-hard erection not mandatory for pleasure.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Slows blood flow for harder erection.",
                            "Form ring at penis base.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "No toy required.",
                            "Pull skin taut gently.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "بیرینگ دی سپیئرر",
                category = "غیر داخلی",
                summary = "انگلیوں سے عضو مخصوص کی جڑ پر حلقہ۔",
                description = "انگوٹھا اور شہادت سے جڑ پر حلقہ بنا کر ہلکا کھینچیں تاکہ سختی بڑھے۔",
                steps = listOf(
                    "عضو کی جڑ پر حلقہ بنائیں۔",
                    "جلد ہلکے کھینچیں۔",
                    "ممکن ہو تو عمل کے دوران رکھیں۔",
                    "دباؤ کے بارے میں بات کریں۔",
                    "خریدی انگوٹی کا متبادل۔",
                ),
                tips = listOf(
                    "خون کے بہاؤ کو روک کر سختی بڑھاتا ہے۔",
                    "کھلونے کی ضرورت نہیں۔",
                    "مکمل سختی لطف کے لیے ضروری نہیں۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "خون کے بہاؤ کو روک کر سختی بڑھاتا ہے۔",
                            "عضو کی جڑ پر حلقہ بنائیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "کھلونے کی ضرورت نہیں۔",
                            "جلد ہلکے کھینچیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_self_loving",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_self_loving,
            categoryId = CAT_NON_PENETRATIVE,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Self-Loving (On Your Knees)",
                category = "Non-Penetrative",
                summary = "Solo or partnered masturbation on pillow or thigh.",
                description = "Straddle a firm pillow or partner's thigh and grind to preferred rhythm. Great for showing partner what you like.",
                steps = listOf(
                    "Choose firm pillow or thigh.",
                    "Straddle and set rhythm.",
                    "Grind for desired friction.",
                    "Share with partner if desired.",
                    "No toys needed.",
                ),
                tips = listOf(
                    "Simple yet effective.",
                    "Helps vulva owners get friction.",
                    "Educational for couples.",
                ),
            ),
            urdu = LocalizedContent(
                name = "خود محبت (گھٹنوں پر)",
                category = "غیر داخلی",
                summary = "تکیے یا ران پر اکیلے یا ساتھی کے ساتھ۔",
                description = "مضبوط تکیے یا ساتھی کی ران پر بیٹھ کر رفتار سے رگڑیں۔ ساتھی کو دکھانے کے لیے بہترین۔",
                steps = listOf(
                    "مضبوط تکیہ یا ران چنیں۔",
                    "بیٹھ کر تال طے کریں۔",
                    "رگڑ سے لطف لیں۔",
                    "چاہیں تو ساتھی کو دکھائیں۔",
                    "کھلونے ضروری نہیں۔",
                ),
                tips = listOf(
                    "سادہ مگر مؤثر۔",
                    "خواتین کے لیے رگڑ بہترین۔",
                    "جوڑوں کی تعلیم کے لیے۔",
                ),
            )
        ),        Posture(
            id = "sk_queening",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_queening,
            categoryId = CAT_NON_PENETRATIVE,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Queening in Bondage",
                category = "Non-Penetrative",
                summary = "Oral receiving on top with optional restraint.",
                description = "Receiver rests on or above partner's mouth for oral stimulation. Weight on knees and thighs — communicate pressure.",
                steps = listOf(
                    "Receiver kneels over partner's face.",
                    "Support weight on thighs.",
                    "Set pace and pressure.",
                    "Optional restraint for power play.",
                    "Use safe words if binding.",
                ),
                tips = listOf(
                    "Power dynamic is enticing.",
                    "Receiver controls pace.",
                    "Restraint intensifies sensation.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Power dynamic is enticing.",
                            "Receiver kneels over partner's face.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Receiver controls pace.",
                            "Support weight on thighs.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "کویننگ بندھن میں",
                category = "غیر داخلی",
                summary = "اوپر بیٹھ کر زبانی لطف، اختیاری بندھن۔",
                description = "وصول کنندہ ساتھی کے منہ پر یا اوپر بیٹھے۔ وزن گھٹنوں پر — دباؤ بتائیں۔",
                steps = listOf(
                    "وصول کنندہ منہ پر بیٹھے۔",
                    "وزن رانوں پر رکھیں۔",
                    "رفتار اور دباؤ طے کریں۔",
                    "اختیاری بندھن۔",
                    "بندھن ہو تو محفوظ لفظ استعمال کریں۔",
                ),
                tips = listOf(
                    "اختیار کا عنصر پرکشش۔",
                    "وصول کنندہ رفتار طے کرے۔",
                    "بندھن سے شدت بڑھتی ہے۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "اختیار کا عنصر پرکشش۔",
                            "وصول کنندہ منہ پر بیٹھے۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "وصول کنندہ رفتار طے کرے۔",
                            "وزن رانوں پر رکھیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_countertop",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_countertop,
            categoryId = CAT_ELEVATED,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Countertop",
                category = "Elevated",
                summary = "Sex on any hip-height flat surface.",
                description = "Receiver lies or sits on sturdy counter, desk, or table. Penetrating partner stands between legs.",
                steps = listOf(
                    "Find sturdy hip-height surface.",
                    "Receiver lies or sits securely.",
                    "Partner stands between legs.",
                    "Hands free for nipple and clitoral touch.",
                    "Works for penetration or oral.",
                ),
                tips = listOf(
                    "Fulfills kitchen or office fantasies.",
                    "Both hands free.",
                    "Oral variation: giver kneels.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Fulfills kitchen or office fantasies.",
                            "Find sturdy hip-height surface.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Both hands free.",
                            "Receiver lies or sits securely.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "کاؤنٹر ٹاپ",
                category = "اونچی سطح",
                summary = "کولہے کی اونچائی کی کسی بھی سطح پر۔",
                description = "وصول کنندہ کاؤنٹر یا میز پر بیٹھے یا لیٹے۔ دوسرا درمیان میں کھڑا ہو۔",
                steps = listOf(
                    "مضبوط سطح تلاش کریں۔",
                    "وصول کنندہ محفوظ بیٹھے یا لیٹیں۔",
                    "ساتھی درمیان کھڑا ہو۔",
                    "ہاتھ آزاد محرک کے لیے۔",
                    "داخلہ یا زبانی دونوں۔",
                ),
                tips = listOf(
                    "کچن یا دفتر کی فنتاسی۔",
                    "دونوں کے ہاتھ آزاد۔",
                    "زبانی: دینے والا گھٹنوں پر۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "کچن یا دفتر کی فنتاسی۔",
                            "مضبوط سطح تلاش کریں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "دونوں کے ہاتھ آزاد۔",
                            "وصول کنندہ محفوظ بیٹھے یا لیٹیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_happy_scissors",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_happy_scissors,
            categoryId = CAT_ELEVATED,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Happy Scissors",
                category = "Elevated",
                summary = "Receiver on surface with legs splayed upward.",
                description = "Like Countertop but receiver splays legs and points toes to ceiling for open, erotic access.",
                steps = listOf(
                    "Receiver on hip-height surface.",
                    "Splay legs wide, toes up.",
                    "Partner stands and enters.",
                    "Explore power dynamics.",
                    "Access legs and feet erogenous zones.",
                ),
                tips = listOf(
                    "Open-legged pose is erotic.",
                    "Submission energy for some.",
                    "Try toe play if curious.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Open-legged pose is erotic.",
                            "Receiver on hip-height surface.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Submission energy for some.",
                            "Splay legs wide, toes up.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "ہیپی سیزرز",
                category = "اونچی سطح",
                summary = "سطح پر لیٹے، ٹانگیں اوپر پھیلائیں۔",
                description = "کاؤنٹر ٹاپ جیسا لیکن ٹانگیں کھول کر پاؤں چھت کی طرف۔",
                steps = listOf(
                    "کولہے کی اونچائی پر لیٹیں۔",
                    "ٹانگیں چوڑی کھولیں۔",
                    "ساتھی کھڑا داخل ہو۔",
                    "اختیار کھیلیں۔",
                    "ٹانگوں اور پاؤں کو چھوئیں۔",
                ),
                tips = listOf(
                    "کھلی ٹانگیں پرکشش۔",
                    "کچھ کے لیے تسلیم کا عنصر۔",
                    "پاؤں کا لطف آزمائیں۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "کھلی ٹانگیں پرکشش۔",
                            "کولہے کی اونچائی پر لیٹیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "کچھ کے لیے تسلیم کا عنصر۔",
                            "ٹانگیں چوڑی کھولیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_butterfly",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_butterfly,
            categoryId = CAT_ELEVATED,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "The Butterfly",
                category = "Elevated",
                summary = "Heels on shoulders for deep penetration.",
                description = "Receiver on elevated surface with heels over partner's shoulders. Standing partner uses athletic stance.",
                steps = listOf(
                    "Receiver lies on elevated bed or table.",
                    "Place heels on partner's shoulders.",
                    "Partner stands in athletic stance.",
                    "Receiver's hands free for clitoral play.",
                    "Adjust elevation for comfort.",
                ),
                tips = listOf(
                    "Great visual for standing partner.",
                    "Allows cervical stimulation.",
                    "Deeper is the motto.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Great visual for standing partner.",
                            "Receiver lies on elevated bed or table.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Allows cervical stimulation.",
                            "Place heels on partner's shoulders.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "تتلی",
                category = "اونچی سطح",
                summary = "ایڑیاں کندھوں پر، زیادہ گہرائی۔",
                description = "وصول کنندہ اونچی سطح پر، ایڑیاں ساتھی کے کندھوں پر۔",
                steps = listOf(
                    "اونچی سطح پر لیٹیں۔",
                    "ایڑیاں کندھوں پر رکھیں۔",
                    "ساتھی کھڑا مضبوط پوزیشن۔",
                    "ہاتھ سے کلائٹورس۔",
                    "اونچائی ایڈجسٹ کریں۔",
                ),
                tips = listOf(
                    "کھڑے ساتھی کے لیے منظر۔",
                    "گریوائیکل محرک۔",
                    "زیادہ گہرائی کے لیے۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "کھڑے ساتھی کے لیے منظر۔",
                            "اونچی سطح پر لیٹیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "گریوائیکل محرک۔",
                            "ایڑیاں کندھوں پر رکھیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_lap_dance",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_lap_dance,
            categoryId = CAT_ELEVATED,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Lap Dance",
                category = "Elevated",
                summary = "Receiver straddles seated partner's lap.",
                description = "Use armless chair or surface. Receiver straddles lap face-to-face or front-to-back and grinds.",
                steps = listOf(
                    "Partner sits on sturdy chair.",
                    "Receiver straddles lap.",
                    "Feet on floor for leverage.",
                    "Rotate, bounce, grind.",
                    "Deep penetration and eye contact.",
                ),
                tips = listOf(
                    "Accessible for different heights.",
                    "Top partner does the work.",
                    "Wheelchair-friendly option.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Accessible for different heights.",
                            "Partner sits on sturdy chair.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Top partner does the work.",
                            "Receiver straddles lap.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "لیپ ڈانس",
                category = "اونچی سطح",
                summary = "وصول کنندہ بیٹھے ساتھی کی گود میں۔",
                description = "کرسی پر بیٹھے ساتھی کی گود میں آمنے سامنے یا پیٹھ کر کے۔",
                steps = listOf(
                    "ساتھی مضبوط کرسی پر بیٹھے۔",
                    "گود میں بیٹھیں۔",
                    "پاؤں فرش پر۔",
                    "گھمائیں، اچھلیں، رگڑیں۔",
                    "گہرائی اور آنکھوں کا رابطہ۔",
                ),
                tips = listOf(
                    "اونچائی کے فرق میں آسان۔",
                    "اوپر والا محنت کرے۔",
                    "وہیل چیئر کے لیے موزوں۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "اونچائی کے فرق میں آسان۔",
                            "ساتھی مضبوط کرسی پر بیٹھے۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "اوپر والا محنت کرے۔",
                            "گود میں بیٹھیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_shower_front",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_shower_front,
            categoryId = CAT_SHOWER,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Standing Up Full-Frontal",
                category = "Shower",
                summary = "Shower sex with one leg lifted on tub edge.",
                description = "Penetrating partner keeps balance on wet floor. Receiver lifts one leg to wrap or rest on tub rim.",
                steps = listOf(
                    "Lock door for privacy.",
                    "Use tub bench or wide rim.",
                    "Receiver lifts one leg.",
                    "Set pace together on wet surface.",
                    "Move to dry area when water cools.",
                ),
                tips = listOf(
                    "Sleek and sensual with water.",
                    "Both can set pace.",
                    "Easy transition when water runs out.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Sleek and sensual with water.",
                            "Lock door for privacy.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Both can set pace.",
                            "Use tub bench or wide rim.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "شاور میں سامنے سے کھڑے",
                category = "شاور",
                summary = "شاور میں ایک ٹانگ اٹھا کر سامنے سے۔",
                description = "گیلے فرش پر توازن رکھیں۔ وصول کنندہ ایک ٹانگ اٹھائے۔",
                steps = listOf(
                    "دروازہ بند کریں۔",
                    "ٹب کے کنارے کا سہارا لیں۔",
                    "ایک ٹانگ اٹھائیں۔",
                    "مل کر رفتار طے کریں۔",
                    "پانی ٹھنڈا ہو تو خشک جگہ جائیں۔",
                ),
                tips = listOf(
                    "پانی کے ساتھ پرکشش۔",
                    "دونوں رفتار طے کر سکتے ہیں۔",
                    "آسان منتقلی۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "پانی کے ساتھ پرکشش۔",
                            "دروازہ بند کریں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "دونوں رفتار طے کر سکتے ہیں۔",
                            "ٹب کے کنارے کا سہارا لیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_soap_grope",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_soap_grope,
            categoryId = CAT_SHOWER,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Soap'n'Grope",
                category = "Shower",
                summary = "Shower rear entry against wall.",
                description = "Receiver braces on wall; penetrating partner enters from behind in shower.",
                steps = listOf(
                    "Receiver braces on shower wall.",
                    "Partner enters from behind.",
                    "Explore with soapy hands.",
                    "Watch footing on wet floor.",
                    "Keep it playful and safe.",
                ),
                tips = listOf(
                    "Hands-on shower exploration.",
                    "Sexy angle from behind.",
                    "Good clean fun.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Hands-on shower exploration.",
                            "Receiver braces on shower wall.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Sexy angle from behind.",
                            "Partner enters from behind.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "صابن اور چھونا",
                category = "شاور",
                summary = "دیوار سے ٹیک لگا کر شاور میں پیچھے سے۔",
                description = "وصول کنندہ دیوار پکڑے؛ دوسرا پیچھے سے داخل ہو۔",
                steps = listOf(
                    "وصول کنندہ دیوار پکڑے۔",
                    "پیچھے سے داخل ہوں۔",
                    "صابن والے ہاتھوں سے چھوئیں۔",
                    "پھسلن سے بچیں۔",
                    "تفریحی اور محفوظ رہیں۔",
                ),
                tips = listOf(
                    "شاور میں ہاتھوں سے کھوج۔",
                    "پیچھے سے پرکشش زاویہ۔",
                    "صاف ستھرا مزہ۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "شاور میں ہاتھوں سے کھوج۔",
                            "وصول کنندہ دیوار پکڑے۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "پیچھے سے پرکشش زاویہ۔",
                            "پیچھے سے داخل ہوں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_hands_ankles",
            difficulty = Difficulty.ADVANCED,
            illustrationRes = R.drawable.pic_sk_hands_ankles,
            categoryId = CAT_BONDAGE,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Hands Behind Ankles",
                category = "Bondage",
                summary = "Hogtie-style bondage with cuffs and flexibility.",
                description = "Receiver lies prone, bends legs up, cuffs wrists behind ankles. Requires safe words and aftercare.",
                steps = listOf(
                    "Discuss comfort and safe words first.",
                    "Receiver lies belly-down, legs bent.",
                    "Cuff wrists behind ankles.",
                    "Partner enters carefully.",
                    "Plan cozy aftercare.",
                ),
                tips = listOf(
                    "Vulnerability builds trust.",
                    "Hip stretch increases stimulation.",
                    "Use toys if maneuvering is hard.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Vulnerability builds trust.",
                            "Discuss comfort and safe words first.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Hip stretch increases stimulation.",
                            "Receiver lies belly-down, legs bent.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "ہاتھ ایڑیوں کے پیچھے",
                category = "بندھن",
                summary = "کف اور لچک کے ساتھ بندھن۔",
                description = "پیٹ کے بل، ٹانگیں موڑ کر کلائیوں کو ایڑیوں سے باندھیں۔ محفوظ الفاظ ضروری۔",
                steps = listOf(
                    "پہلے بات چیت اور محفوظ الفاظ۔",
                    "پیٹ کے بل ٹانگیں موڑیں۔",
                    "کلائیاں ایڑیوں کے پیچھے باندھیں۔",
                    "احتیاط سے داخل ہوں۔",
                    "بعد میں آرام دہ دیکھ بھال۔",
                ),
                tips = listOf(
                    "نازک پن اعتماد بڑھاتا ہے۔",
                    "کولہے کی کھلائی محرک بڑھاتی ہے۔",
                    "مشکل ہو تو کھلونا استعمال کریں۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "نازک پن اعتماد بڑھاتا ہے۔",
                            "پہلے بات چیت اور محفوظ الفاظ۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "کولہے کی کھلائی محرک بڑھاتی ہے۔",
                            "پیٹ کے بل ٹانگیں موڑیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_kinky_missionary",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_kinky_missionary,
            categoryId = CAT_BONDAGE,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "The Kinky Missionary",
                category = "Bondage",
                summary = "Missionary with under-bed or headboard restraints.",
                description = "Restrain partner to bed then approach standard missionary. Face-to-face adds safety for BDSM beginners.",
                steps = listOf(
                    "Set up mattress or headboard cuffs.",
                    "Restrain willing partner comfortably.",
                    "Approach missionary position.",
                    "Use facial cues and words.",
                    "Try blindfolds or sensation play.",
                ),
                tips = listOf(
                    "Face-to-face feels safer.",
                    "Power play with blindfolds possible.",
                    "Troubleshoot together first time.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Face-to-face feels safer.",
                            "Set up mattress or headboard cuffs.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Power play with blindfolds possible.",
                            "Restrain willing partner comfortably.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "کنکی مشنری",
                category = "بندھن",
                summary = "بستر کی کفوں کے ساتھ مشنری۔",
                description = "ساتھی کو بستر سے باندھ کر معمولی مشنری۔ آمنے سامنے ابتدائیوں کے لیے محفوظ۔",
                steps = listOf(
                    "کف لگائیں۔",
                    "رضامندی سے باندھیں۔",
                    "مشنری پوزیشن لیں۔",
                    "چہرے اور الفاظ سے پڑھیں۔",
                    "آنکھوں پر پٹی آزمائیں۔",
                ),
                tips = listOf(
                    "آمنے سامنے محفوظ محسوس ہوتا ہے۔",
                    "پٹی سے اختیار کھیل۔",
                    "پہلی بار مل کر درست کریں۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "آمنے سامنے محفوظ محسوس ہوتا ہے۔",
                            "کف لگائیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "پٹی سے اختیار کھیل۔",
                            "رضامندی سے باندھیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_standing_room",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_standing_room,
            categoryId = CAT_BONDAGE,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Standing Room Only",
                category = "Bondage",
                summary = "Standing sex with cuff restraint.",
                description = "Standing position with cuffs. Usually receiver is cuffed with leg slung around partner's waist or thigh.",
                steps = listOf(
                    "Choose over-door or sturdy cuffs.",
                    "Cuffed partner adjusts leg position.",
                    "Uncuffed partner supports weight.",
                    "Check restraints aren't too tight.",
                    "Switch if cuffed partner tires.",
                ),
                tips = listOf(
                    "Feels like an erotic movie scene.",
                    "Angle plus cuffs intensifies.",
                    "Over-door cuffs work well.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Feels like an erotic movie scene.",
                            "Choose over-door or sturdy cuffs.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Angle plus cuffs intensifies.",
                            "Cuffed partner adjusts leg position.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "کھڑے بندھن",
                category = "بندھن",
                summary = "کھڑے ہو کر کفوں کے ساتھ۔",
                description = "کھڑے ہو کر کف۔ عام طور پر وصول کنندہ بندھا، ٹانگ کمر یا ران پر۔",
                steps = listOf(
                    "مضبوط کف چنیں۔",
                    "ٹانگ کی پوزیشن ایڈجسٹ کریں۔",
                    "دوسرا ساتھی سہارا دے۔",
                    "بندھن تنگ نہ ہو۔",
                    "تھکیں تو بدلیں۔",
                ),
                tips = listOf(
                    "فلمی منظر جیسا۔",
                    "زاویہ اور کف شدت بڑھاتے ہیں۔",
                    "دروازے کی کف بہترین۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "فلمی منظر جیسا۔",
                            "مضبوط کف چنیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "زاویہ اور کف شدت بڑھاتے ہیں۔",
                            "ٹانگ کی پوزیشن ایڈجسٹ کریں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_backseat",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_backseat,
            categoryId = CAT_CAR,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Backseat Driver",
                category = "Car",
                summary = "Straddling in the car backseat.",
                description = "Hop in backseat; receiver assumes straddling position for kissing or penetration.",
                steps = listOf(
                    "Park in private driveway.",
                    "Receiver straddles in backseat.",
                    "Customize kissing or penetration.",
                    "Mind headroom and seats.",
                    "Keep activity private and legal.",
                ),
                tips = listOf(
                    "Highly customizable.",
                    "Public sex is illegal most places.",
                    "Private driveway recommended.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Highly customizable.",
                            "Park in private driveway.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Public sex is illegal most places.",
                            "Receiver straddles in backseat.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "بیک سیٹ ڈرائیور",
                category = "گاڑی",
                summary = "گاڑی کی پچھلی سیٹ پر اوپر بیٹھنا۔",
                description = "پچھلی سیٹ میں اوپر بیٹھنے والی پوزیشن۔",
                steps = listOf(
                    "نجی جگہ پارک کریں۔",
                    "پچھلی سیٹ میں اوپر بیٹھیں۔",
                    "بوسہ یا داخلہ طے کریں۔",
                    "سر کی جگہ دیکھیں۔",
                    "قانونی اور نجی رہیں۔",
                ),
                tips = listOf(
                    "بہت لچکدار۔",
                    "عوامی جگہ غیر قانونی۔",
                    "نجی ڈرائیو وے بہتر۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "بہت لچکدار۔",
                            "نجی جگہ پارک کریں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "عوامی جگہ غیر قانونی۔",
                            "پچھلی سیٹ میں اوپر بیٹھیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_belt_bondage",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_belt_bondage,
            categoryId = CAT_CAR,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Belt Bondage",
                category = "Car",
                summary = "DIY seatbelt handcuffs in the car.",
                description = "Loop seatbelt in figure-eight around wrists for light restraint during car play.",
                steps = listOf(
                    "Cuffed partner hands above head.",
                    "Loop belt in figure-eight.",
                    "Keep loose for quick release.",
                    "Enjoy oral, hand, or penetrative sex.",
                    "Return to front seat if needed.",
                ),
                tips = listOf(
                    "No bondage gear needed.",
                    "Customizable once restrained.",
                    "Loose belts allow quick exit.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "No bondage gear needed.",
                            "Cuffed partner hands above head.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Customizable once restrained.",
                            "Loop belt in figure-eight.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "بیلٹ بندھن",
                category = "گاڑی",
                summary = "سیٹ بیلٹ سے ہاتھ باندھنا۔",
                description = "سیٹ بیلٹ سے کلائیوں پر آٹھ کی شکل میں ہلکا بندھن۔",
                steps = listOf(
                    "ہاتھ اوپر رکھیں۔",
                    "بیلٹ آٹھ کی شکل میں لپیٹیں۔",
                    "ڈھیلا رکھیں۔",
                    "زبانی، ہاتھ یا داخلہ۔",
                    "ضرورت ہو تو اگلی سیٹ جائیں۔",
                ),
                tips = listOf(
                    "سامان کی ضرورت نہیں۔",
                    "باندھنے کے بعد لچک۔",
                    "ڈھیلا بندھن فوری نکاس۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "سامان کی ضرورت نہیں۔",
                            "ہاتھ اوپر رکھیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "باندھنے کے بعد لچک۔",
                            "بیلٹ آٹھ کی شکل میں لپیٹیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_car_seated_rear",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_car_seated_rear,
            categoryId = CAT_CAR,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Seated Rear Entry",
                category = "Car",
                summary = "Stealthy driver-seat lap position.",
                description = "Shift driver seat back; receiver sits in lap facing forward for discreet car intimacy.",
                steps = listOf(
                    "Turn car off, set emergency brake.",
                    "Push driver seat fully back.",
                    "Receiver sits in lap facing forward.",
                    "Skirt or dress allows discretion.",
                    "Lower risk than backseat climbing.",
                ),
                tips = listOf(
                    "Less commitment than backseat.",
                    "Can stay partially dressed.",
                    "Ideal for quick private moments.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Less commitment than backseat.",
                            "Turn car off, set emergency brake.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Can stay partially dressed.",
                            "Push driver seat fully back.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "گاڑی میں بیٹھے پیچھے سے",
                category = "گاڑی",
                summary = "ڈرائیور سیٹ پر گود میں پیٹھ کر کے۔",
                description = "ڈرائیور سیٹ پیچھے؛ وصول کنندہ آگے منہ کر کے گود میں۔",
                steps = listOf(
                    "گاڑی بند، ہینڈ بریک۔",
                    "سیٹ پیچھے کریں۔",
                    "آگے منہ کر کے گود میں بیٹھیں۔",
                    "اسکرٹ سے چھپاؤ۔",
                    "پچھلی سیٹ سے آسان۔",
                ),
                tips = listOf(
                    "پچھلی سیٹ سے آسان۔",
                    "جزوی لباس ممکن۔",
                    "فوری نجی لمحات کے لیے۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "پچھلی سیٹ سے آسان۔",
                            "گاڑی بند، ہینڈ بریک۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "جزوی لباس ممکن۔",
                            "سیٹ پیچھے کریں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_yab_yum",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_yab_yum,
            categoryId = CAT_CAR,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Yab-Yum",
                category = "Car",
                summary = "Tantric seated face-to-face embrace.",
                description = "Insertive partner sits cross-legged; receiver sits in lap legs around back. Rock side-to-side slowly.",
                steps = listOf(
                    "Partner sits cross-legged on floor or seat.",
                    "Receiver sits in lap facing them.",
                    "Wrap legs around partner.",
                    "Rock side-to-side slowly.",
                    "Maintain eye contact and shared breath.",
                ),
                tips = listOf(
                    "Popular Tantric position.",
                    "Promotes deep romance.",
                    "Try eye-gazing for intimacy.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Popular Tantric position.",
                            "Partner sits cross-legged on floor or seat.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Promotes deep romance.",
                            "Receiver sits in lap facing them.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "یب یم",
                category = "گاڑی",
                summary = "ٹینٹرک بیٹھے آمنے سامنے آغوش۔",
                description = "نیچے والا پیر باندھ کر بیٹھے؛ اوپر والا گود میں ٹانگیں کمر کے گرد۔",
                steps = listOf(
                    "پیر باندھ کر بیٹھیں۔",
                    "آمنے سامنے گود میں بیٹھیں۔",
                    "ٹانگیں لپیٹیں۔",
                    "آہستہ ساتھ جھولیں۔",
                    "آنکھیں اور سانس ملائیں۔",
                ),
                tips = listOf(
                    "مشہور ٹینٹرک پوزیشن۔",
                    "گہری رومانویت۔",
                    "آنکھوں میں دیکھیں۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "مشہور ٹینٹرک پوزیشن۔",
                            "پیر باندھ کر بیٹھیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "گہری رومانویت۔",
                            "آمنے سامنے گود میں بیٹھیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_trunk",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_trunk,
            categoryId = CAT_CAR,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Trunk Space",
                category = "Car",
                summary = "Car-friendly doggy on lowered seats.",
                description = "Lower front seat; receiver face-down on headrest while partner enters from behind. SUV back seats offer more room.",
                steps = listOf(
                    "Lower front seat for space.",
                    "Receiver face-down on headrest.",
                    "Partner enters from behind.",
                    "SUV: fold back seats for room.",
                    "Skin contact feels intimate.",
                ),
                tips = listOf(
                    "More connected than standard doggy.",
                    "Leverage for deep penetration.",
                    "Hand play opportunities.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "More connected than standard doggy.",
                            "Lower front seat for space.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Leverage for deep penetration.",
                            "Receiver face-down on headrest.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "ٹرنک اسپیس",
                category = "گاڑی",
                summary = "سیٹیں جھکا کر گاڑی میں ڈوگی۔",
                description = "اگلی سیٹ جھکائیں؛ وصول کنندہ سرے پر؛ پیچھے سے داخلہ۔",
                steps = listOf(
                    "سیٹ جھکائیں۔",
                    "منہ نیچے سرے پر۔",
                    "پیچھے سے داخل ہوں۔",
                    "SUV میں زیادہ جگہ۔",
                    "جلد کا رابطہ قریبی۔",
                ),
                tips = listOf(
                    "معمولی ڈوگی سے زیادہ رابطہ۔",
                    "گہری داخلہ کے لیے۔",
                    "ہاتھ سے لطف۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "معمولی ڈوگی سے زیادہ رابطہ۔",
                            "سیٹ جھکائیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "گہری داخلہ کے لیے۔",
                            "منہ نیچے سرے پر۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_over_hump",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_over_hump,
            categoryId = CAT_SOLO,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Over the Hump",
                category = "Solo / Masturbation",
                summary = "Face-down solo grinding on pillow.",
                description = "Lie on stomach with pillow under pelvis and grind until pleasurable sensation peaks.",
                steps = listOf(
                    "Lie on stomach.",
                    "Place pillow under pelvis.",
                    "Shimmy hips to find sensation.",
                    "Grind until peak.",
                    "Add hand or wand between legs.",
                ),
                tips = listOf(
                    "Doggy-style variation for solo.",
                    "Works on vacation without toys.",
                    "Wand vibrators excel here.",
                ),
            ),
            urdu = LocalizedContent(
                name = "اوور دی ہمپ",
                category = "اکیلے",
                summary = "پیٹ کے بل تکیے پر اکیلے رگڑنا۔",
                description = "پیٹ کے بل تکیہ کولہے کے نیچے رکھ کر رگڑیں۔",
                steps = listOf(
                    "پیٹ کے بل لیٹیں۔",
                    "تکیہ کولہے کے نیچے۔",
                    "کولہے ہلائیں۔",
                    "لطف تک رگڑیں۔",
                    "ہاتھ یا وائبریٹر شامل کریں۔",
                ),
                tips = listOf(
                    "اکیلے کے لیے ڈوگی جیسا۔",
                    "سفر میں بغیر کھلونے۔",
                    "وائبریٹر بہترین۔",
                ),
            )
        ),        Posture(
            id = "sk_superstar",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_superstar,
            categoryId = CAT_SOLO,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Superstar",
                category = "Solo / Masturbation",
                summary = "Kneeling upright solo masturbation.",
                description = "Kneel on soft surface, torso upright, knees open. Explore new angles for self-pleasure.",
                steps = listOf(
                    "Kneel on soft surface.",
                    "Keep torso upright.",
                    "Open knees comfortably.",
                    "Use wall for support if needed.",
                    "Try mirror for body awareness.",
                ),
                tips = listOf(
                    "Spices up solo routine.",
                    "New orgasm angles possible.",
                    "Mirror adds voyeur feeling.",
                ),
            ),
            urdu = LocalizedContent(
                name = "سپر اسٹار",
                category = "اکیلے",
                summary = "گھٹنوں پر سیدھے اکیلے لطف۔",
                description = "نرم سطح پر گھٹنوں کے بل سیدھے، گھٹنے کھولیں۔",
                steps = listOf(
                    "نرم جگہ پر گھٹنوں پر۔",
                    "سینہ سیدھا۔",
                    "گھٹنے کھولیں۔",
                    "دیوار سے سہارا۔",
                    "آئینے میں دیکھیں۔",
                ),
                tips = listOf(
                    "اکیلے کے معمول میں تنوع۔",
                    "نئے زاویے۔",
                    "آئینہ اضافی لطف۔",
                ),
            )
        ),        Posture(
            id = "sk_solo_snake",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_solo_snake,
            categoryId = CAT_SOLO,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "The Solo Snake",
                category = "Solo / Masturbation",
                summary = "Face-down grinding on palm vibrator.",
                description = "Lie on belly with vibrator under pelvis; body weight intensifies vibration.",
                steps = listOf(
                    "Power on palm vibrator.",
                    "Lie face-down on belly.",
                    "Position toy under pelvis.",
                    "Grind to preferred pressure.",
                    "Adjust angle with hips.",
                ),
                tips = listOf(
                    "Body weight intensifies vibe.",
                    "Simple setup.",
                    "Great for targeted external play.",
                ),
            ),
            urdu = LocalizedContent(
                name = "سولو سنیک",
                category = "اکیلے",
                summary = "وائبریٹر پر پیٹ کے بل رگڑنا۔",
                description = "پیٹ کے بل وائبریٹر کولہے کے نیچے؛ وزن سے شدت بڑھے۔",
                steps = listOf(
                    "وائبریٹر چالو کریں۔",
                    "پیٹ کے بل لیٹیں۔",
                    "کولہے کے نیچے رکھیں۔",
                    "دباؤ سے رگڑیں۔",
                    "کولہے سے زاویہ بدلیں۔",
                ),
                tips = listOf(
                    "جسم کا وزن وائبریشن بڑھاتا ہے۔",
                    "آسان ترتیب۔",
                    "خارجی لطف کے لیے۔",
                ),
            )
        ),        Posture(
            id = "sk_opening_up",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_opening_up,
            categoryId = CAT_SOLO,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Opening Up",
                category = "Solo / Masturbation",
                summary = "Chair-based solo with legs braced.",
                description = "Sit on chair, ankles wound around legs, open thighs and touch as desired.",
                steps = listOf(
                    "Sit on sturdy chair.",
                    "Wrap ankles around chair legs.",
                    "Open thighs wide.",
                    "Touch and tease at your pace.",
                    "Use leverage from braced legs.",
                ),
                tips = listOf(
                    "Leverage and support from chair.",
                    "Keeps solo time interesting.",
                    "Spine-tingling new sensations.",
                ),
            ),
            urdu = LocalizedContent(
                name = "اوپننگ اپ",
                category = "اکیلے",
                summary = "کرسی پر ٹانگیں پھیلا کر اکیلے لطف۔",
                description = "کرسی پر بیٹھیں، ٹانگیں کرسی کی لکڑیوں سے لپٹائیں۔",
                steps = listOf(
                    "مضبوط کرسی پر بیٹھیں۔",
                    "ٹانگیں کرسی سے لپٹائیں۔",
                    "رانیں کھولیں۔",
                    "اپنی رفتار سے چھوئیں۔",
                    "ٹانگوں کا سہارا لیں۔",
                ),
                tips = listOf(
                    "کرسی سے سہارا۔",
                    "اکیلے کے وقت میں تنوع۔",
                    "نئے احساسات۔",
                ),
            )
        ),        Posture(
            id = "sk_layer_cake",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_layer_cake,
            categoryId = CAT_FLAT,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Layer Cake",
                category = "Flat",
                summary = "External grinding missionary stack.",
                description = "One partner on back, other lies flat on top facing them. Press genitals together with rhythm and lube.",
                steps = listOf(
                    "Bottom partner lies on back.",
                    "Top partner lies flat facing them.",
                    "Press genitals together.",
                    "Rock at pleasurable rhythm.",
                    "Use lube for comfort.",
                ),
                tips = listOf(
                    "Maximum clitoral stimulation.",
                    "No penetration needed.",
                    "Good during menstruation.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Maximum clitoral stimulation.",
                            "Bottom partner lies on back.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "No penetration needed.",
                            "Top partner lies flat facing them.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "لیئر کیک",
                category = "سیدھے لیٹ کر",
                summary = "اوپر نیچے رگڑ، بغیر داخلہ۔",
                description = "ایک پیٹ کے بل، دوسرا اوپر آمنے سامنے۔ عضو ٹھانیاں ساتھ رگڑیں۔",
                steps = listOf(
                    "نیچے والا پیٹ کے بل۔",
                    "اوپر والا آمنے سامنے لیٹے۔",
                    "عضو ٹھانیاں ملائیں۔",
                    "تال سے رگڑیں۔",
                    "لوبریکنٹ استعمال کریں۔",
                ),
                tips = listOf(
                    "زیادہ کلائٹورل محرک۔",
                    "داخلہ نہیں۔",
                    "حیض میں موزوں۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "زیادہ کلائٹورل محرک۔",
                            "نیچے والا پیٹ کے بل۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "داخلہ نہیں۔",
                            "اوپر والا آمنے سامنے لیٹے۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_reverse_slither",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_reverse_slither,
            categoryId = CAT_FLAT,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "The Reverse Slither",
                category = "Flat",
                summary = "Full skin contact rear entry while lying flat.",
                description = "Receiver lies on top prone; penetrating partner enters from behind for deep penetration plus intimacy.",
                steps = listOf(
                    "Receiver lies on top facing away.",
                    "Partner enters from behind.",
                    "Maintain full body contact.",
                    "Stimulate breasts and clitoris.",
                    "Whisper near each other's heads.",
                ),
                tips = listOf(
                    "Deep penetration plus intimacy.",
                    "Breast and clit access.",
                    "Great for dirty talk.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Deep penetration plus intimacy.",
                            "Receiver lies on top facing away.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Breast and clit access.",
                            "Partner enters from behind.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "ریورس سلتھر",
                category = "سیدھے لیٹ کر",
                summary = "سیدھے لیٹ کر مکمل جلد رابطے میں پیچھے سے۔",
                description = "وصول کنندہ اوپر پیٹ کے بل؛ دوسرا پیچھے سے۔",
                steps = listOf(
                    "وصول کنندہ اوپر پیٹ کے بل۔",
                    "پیچھے سے داخل ہوں۔",
                    "پورے جسم کا رابطہ۔",
                    "سینے اور کلائٹورس۔",
                    "کان کے پاس آہستہ بات۔",
                ),
                tips = listOf(
                    "گہری داخلہ اور قربت۔",
                    "سینے اور کلائٹورس تک رسائی۔",
                    "آہستہ گندی بات۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "گہری داخلہ اور قربت۔",
                            "وصول کنندہ اوپر پیٹ کے بل۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "سینے اور کلائٹورس تک رسائی۔",
                            "پیچھے سے داخل ہوں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_stacked_snakes",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_stacked_snakes,
            categoryId = CAT_FLAT,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Stacked Snakes",
                category = "Flat",
                summary = "Both prone with rear entry on top.",
                description = "Penetrating partner on top enters receiver from behind while both lie totally prone.",
                steps = listOf(
                    "Both lie flat prone.",
                    "Penetrating partner on top.",
                    "Enter from behind.",
                    "Receiver slips hand underneath.",
                    "Low-effort combined grinding.",
                ),
                tips = listOf(
                    "Combines penetration and grinding.",
                    "Receiver can self-touch.",
                    "Ultimate low-key pleasure.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Combines penetration and grinding.",
                            "Both lie flat prone.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Receiver can self-touch.",
                            "Penetrating partner on top.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "سٹیکڈ سنیکس",
                category = "سیدھے لیٹ کر",
                summary = "دونوں پیٹ کے بل، اوپر سے پیچھے۔",
                description = "دونوں پیٹ کے بل؛ اوپر والا پیچھے سے داخل ہو۔",
                steps = listOf(
                    "دونوں پیٹ کے بل۔",
                    "اوپر والا دوسرے پر۔",
                    "پیچھے سے داخلہ۔",
                    "نیچے ہاتھ نیچے رکھے۔",
                    "کم محنت والی رگڑ۔",
                ),
                tips = listOf(
                    "داخلہ اور رگڑ ساتھ۔",
                    "خود چھونے کی گنجائش۔",
                    "آرام دہ لطف۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "داخلہ اور رگڑ ساتھ۔",
                            "دونوں پیٹ کے بل۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "خود چھونے کی گنجائش۔",
                            "اوپر والا دوسرے پر۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_anal_spoon",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_anal_spoon,
            categoryId = CAT_FLAT,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Anal Spoon",
                category = "Flat",
                summary = "Relaxed side-lying anal entry.",
                description = "Big spoon enters anally while snuggled side-by-side. Use plenty of lube and exhale to relax sphincter.",
                steps = listOf(
                    "Lie side-by-side spooning.",
                    "Apply generous anal lube.",
                    "Enter slowly from behind.",
                    "Receiver pulls knees to chest.",
                    "Exhale to relax sphincter.",
                ),
                tips = listOf(
                    "Snuggliest anal option.",
                    "Hands free for touch.",
                    "Very relaxing.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Snuggliest anal option.",
                            "Lie side-by-side spooning.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Hands free for touch.",
                            "Apply generous anal lube.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "اینل چمچہ",
                category = "سیدھے لیٹ کر",
                summary = "سیدھے لیٹ کر آرام دہ پیچھے سے داخلہ۔",
                description = "چمچے والی پوزیشن میں پیچھے سے؛ کافی لوبریکنٹ۔",
                steps = listOf(
                    "سیدھے چمچے کی طرح۔",
                    "لوبریکنٹ لگائیں۔",
                    "آہستہ داخل ہوں۔",
                    "گھٹنے سینے کی طرف۔",
                    "سانس چھوڑ کر آرام دیں۔",
                ),
                tips = listOf(
                    "سب سے آرام دہ پیچھے سے۔",
                    "ہاتھ آزاد۔",
                    "بہت پرسکون۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "سب سے آرام دہ پیچھے سے۔",
                            "سیدھے چمچے کی طرح۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "ہاتھ آزاد۔",
                            "لوبریکنٹ لگائیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_splitting_bamboo",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_splitting_bamboo,
            categoryId = CAT_BLINDFOLD,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Splitting of Bamboo",
                category = "Blindfolded",
                summary = "Tantric missionary with one leg raised and blindfolds.",
                description = "Receiver on back with one leg on partner's shoulder. Blindfolds heighten skin-on-skin sensation.",
                steps = listOf(
                    "Apply comfortable blindfolds.",
                    "Receiver lies on back.",
                    "One leg on partner's shoulder.",
                    "Partner straddles other leg.",
                    "Grind and enter at preferred pace.",
                ),
                tips = listOf(
                    "Excellent penetration angle.",
                    "Blindfolds intensify touch.",
                    "Less flexibility needed than it looks.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Excellent penetration angle.",
                            "Apply comfortable blindfolds.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Blindfolds intensify touch.",
                            "Receiver lies on back.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "بانس کاٹنا",
                category = "آنکھوں پر پٹی",
                summary = "ایک ٹانگ اٹھا کر مشنری، آنکھوں پر پٹی۔",
                description = "پیٹ کے بل ایک ٹانگ کندھے پر؛ پٹی سے احساس بڑھے۔",
                steps = listOf(
                    "آرام دہ پٹی لگائیں۔",
                    "پیٹ کے بل لیٹیں۔",
                    "ایک ٹانگ کندھے پر۔",
                    "دوسری ٹانگ کے اوپر بیٹھیں۔",
                    "اپنی رفتار سے۔",
                ),
                tips = listOf(
                    "بہترین زاویہ۔",
                    "پٹی چھونے کو بڑھاتی ہے۔",
                    "لچک کم لگتی ہے۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "بہترین زاویہ۔",
                            "آرام دہ پٹی لگائیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "پٹی چھونے کو بڑھاتی ہے۔",
                            "پیٹ کے بل لیٹیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_private_dancer",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_private_dancer,
            categoryId = CAT_BLINDFOLD,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "The Private Dancer",
                category = "Blindfolded",
                summary = "Blindfolded lap dance with receiver on top.",
                description = "Penetrating partner blindfolded; receiver slides onto lap and grinds with full control.",
                steps = listOf(
                    "Blindfold bottom partner.",
                    "Receiver slides onto lap.",
                    "Grind and lean for sensation.",
                    "Receiver has all power.",
                    "Remove blindfold when ready.",
                ),
                tips = listOf(
                    "Frees awkward lap-dance feelings.",
                    "Receiver controls everything.",
                    "Very empowering.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Frees awkward lap-dance feelings.",
                            "Blindfold bottom partner.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Receiver controls everything.",
                            "Receiver slides onto lap.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "پرائیویٹ ڈانسر",
                category = "آنکھوں پر پٹی",
                summary = "پٹی بندھے ساتھی پر اوپر والا لیپ ڈانس۔",
                description = "نیچے والے کی آنکھوں پر پٹی؛ اوپر والا گود میں بیٹھ کر کنٹرول کرے۔",
                steps = listOf(
                    "نیچے والے کی پٹی باندھیں۔",
                    "گود میں بیٹھیں۔",
                    "رگڑیں اور جھکیں۔",
                    "اوپر والا اختیار رکھے۔",
                    "تیار ہوں تو پٹی کھولیں۔",
                ),
                tips = listOf(
                    "لیپ ڈانس کی جھجک کم۔",
                    "اوپر والا سب کنٹرول۔",
                    "اختیار بڑھاتا ہے۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "لیپ ڈانس کی جھجک کم۔",
                            "نیچے والے کی پٹی باندھیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "اوپر والا سب کنٹرول۔",
                            "گود میں بیٹھیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_x_marks",
            difficulty = Difficulty.ADVANCED,
            illustrationRes = R.drawable.pic_sk_x_marks,
            categoryId = CAT_BLINDFOLD,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "X Marks the Spot",
                category = "Blindfolded",
                summary = "Spread-eagle bondage with optional penetration.",
                description = "Blindfold partner and restrain wrists/ankles to bed. Kiss, lick, touch — penetration optional.",
                steps = listOf(
                    "Discuss boundaries first.",
                    "Blindfold willing partner.",
                    "Restrain wrists and ankles comfortably.",
                    "Explore with touch.",
                    "Penetration optional.",
                ),
                tips = listOf(
                    "Receiver can feel in control.",
                    "Highly customizable scene.",
                    "Fifty Shades energy.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Receiver can feel in control.",
                            "Discuss boundaries first.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Highly customizable scene.",
                            "Blindfold willing partner.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "ایکس مارکس دی سپاٹ",
                category = "آنکھوں پر پٹی",
                summary = "ہاتھ پاؤں بندھے، اختیاری داخلہ۔",
                description = "پٹی لگا کر بستر سے باندھیں۔ بوسہ، چھونا — داخلہ اختیاری۔",
                steps = listOf(
                    "حدود طے کریں۔",
                    "پٹی لگائیں۔",
                    "آرام سے باندھیں۔",
                    "چھو کر کھوجیں۔",
                    "داخلہ اختیاری۔",
                ),
                tips = listOf(
                    "وصول کنندہ اختیار محسوس کرے۔",
                    "بہت لچکدار۔",
                    "بندھن والا انداز۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "وصول کنندہ اختیار محسوس کرے۔",
                            "حدود طے کریں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "بہت لچکدار۔",
                            "پٹی لگائیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_rock_n_roll",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_rock_n_roll,
            categoryId = CAT_BLINDFOLD,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Rock'n'Roll",
                category = "Blindfolded",
                summary = "Both blindfolded with receiver on top.",
                description = "Receiver on top, heels planted for leverage. Both wear blindfolds before positioning.",
                steps = listOf(
                    "Get into position first.",
                    "Both partners wear blindfolds.",
                    "Receiver on top, heels down.",
                    "Use leverage from heels.",
                    "Let inhibitions fade.",
                ),
                tips = listOf(
                    "Dual blindfolds remove inhibition.",
                    "Receiver controls angle.",
                    "Trust exercise.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Dual blindfolds remove inhibition.",
                            "Get into position first.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Receiver controls angle.",
                            "Both partners wear blindfolds.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "راک این رول",
                category = "آنکھوں پر پٹی",
                summary = "دونوں کی آنکھوں پر پٹی، اوپر والا۔",
                description = "اوپر والا ایڑیاں بستر پر رکھے۔ پوزیشن سے پہلے دونوں کی پٹی۔",
                steps = listOf(
                    "پہلے پوزیشن لیں۔",
                    "دونوں کی پٹی باندھیں۔",
                    "اوپر والا ایڑیاں نیچے۔",
                    "ایڑیوں سے سہارا۔",
                    "جھجک چھوڑیں۔",
                ),
                tips = listOf(
                    "دونوں پٹی جھجک کم کرتی ہے۔",
                    "اوپر والا زاویہ طے کرے۔",
                    "اعتماد کی مشق۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "دونوں پٹی جھجک کم کرتی ہے۔",
                            "پہلے پوزیشن لیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "اوپر والا زاویہ طے کرے۔",
                            "دونوں کی پٹی باندھیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_anal_cowgirl",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_anal_cowgirl,
            categoryId = CAT_ANAL,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Cowgirl/Cowboy (Anal)",
                category = "Anal Variations",
                summary = "Face-to-face anal with receiver on top.",
                description = "Same as cowgirl but anal entry. Receiver controls pace and depth — ideal for first-timers.",
                steps = listOf(
                    "Apply anal lube generously.",
                    "Receiver straddles facing partner.",
                    "Lower slowly onto partner.",
                    "Control depth and pace.",
                    "Maintain eye contact.",
                ),
                tips = listOf(
                    "Best anal position for beginners.",
                    "Easy communication face-to-face.",
                    "Receiver owns the rhythm.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Best anal position for beginners.",
                            "Apply anal lube generously.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Easy communication face-to-face.",
                            "Receiver straddles facing partner.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "کاؤگرل اینل",
                category = "پیچھے سے متبادل",
                summary = "آمنے سامنے پیچھے سے، اوپر والا کنٹرول۔",
                description = "کاؤگرل جیسا لیکن پیچھے سے۔ اوپر والا رفتار طے کرے۔",
                steps = listOf(
                    "لوبریکنٹ لگائیں۔",
                    "آمنے سامنے اوپر بیٹھیں۔",
                    "آہستہ نیچے بیٹھیں۔",
                    "گہرائی کنٹرول کریں۔",
                    "آنکھوں کا رابطہ۔",
                ),
                tips = listOf(
                    "ابتدائیوں کے لیے بہترین۔",
                    "آمنے سامنے بات آسان۔",
                    "اوپر والا تال طے کرے۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "ابتدائیوں کے لیے بہترین۔",
                            "لوبریکنٹ لگائیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "آمنے سامنے بات آسان۔",
                            "آمنے سامنے اوپر بیٹھیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_anal_doggy",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_anal_doggy,
            categoryId = CAT_ANAL,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Doggy-Style (Anal)",
                category = "Anal Variations",
                summary = "Classic rear-entry anal with lots of lube.",
                description = "Standard doggy adapted for anal. Stay relaxed and communicate depth verbally.",
                steps = listOf(
                    "Generous lube on both partners.",
                    "Receiver on hands and knees.",
                    "Enter slowly from behind.",
                    "Communicate depth verbally.",
                    "Stay relaxed.",
                ),
                tips = listOf(
                    "Feels good in all variations.",
                    "Not face-to-face — talk more.",
                    "Relaxation is key.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Feels good in all variations.",
                            "Generous lube on both partners.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Not face-to-face — talk more.",
                            "Receiver on hands and knees.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "ڈوگی اینل",
                category = "پیچھے سے متبادل",
                summary = "کلاسک پیچھے سے، کافی لوبریکنٹ۔",
                description = "معمولی ڈوگی پیچھے سے داخلہ کے لیے۔ آرام سے رہیں اور بات کریں۔",
                steps = listOf(
                    "کافی لوبریکنٹ۔",
                    "چاروں پر۔",
                    "آہستہ پیچھے سے۔",
                    "گہرائی بتائیں۔",
                    "آرام رکھیں۔",
                ),
                tips = listOf(
                    "ہر متبادل میں اچھا۔",
                    "منہ نہیں دکھتا — زیادہ بات کریں۔",
                    "آرام کلید ہے۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "ہر متبادل میں اچھا۔",
                            "کافی لوبریکنٹ۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "منہ نہیں دکھتا — زیادہ بات کریں۔",
                            "چاروں پر۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_anal_face",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_anal_face,
            categoryId = CAT_ANAL,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Face to Face (Anal)",
                category = "Anal Variations",
                summary = "Straddling with anal or vaginal option.",
                description = "One straddles the other for tons of eye contact. Can rub, penetrate vaginally, or try anal.",
                steps = listOf(
                    "Partner sits or lies as base.",
                    "Other straddles facing them.",
                    "Apply lube if going anal.",
                    "Set rhythm together.",
                    "Kiss and touch freely.",
                ),
                tips = listOf(
                    "Extra intimacy during act.",
                    "Experiment with touch.",
                    "Shared rhythm building.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Extra intimacy during act.",
                            "Partner sits or lies as base.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Experiment with touch.",
                            "Other straddles facing them.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "آمنے سامنے اینل",
                category = "پیچھے سے متبادل",
                summary = "بیٹھ کر پیچھے یا اندام نہانی داخلہ۔",
                description = "ایک دوسرے پر بیٹھ کر آنکھوں کا رابطہ۔ رگڑ، اندام نہانی یا پیچھے سے۔",
                steps = listOf(
                    "نیچے والا بیٹھے یا لیٹے۔",
                    "اوپر آمنے سامنے بیٹھیں۔",
                    "پیچھے سے ہو تو لوبریکنٹ۔",
                    "تال ساتھ طے کریں۔",
                    "بوسہ اور چھونا۔",
                ),
                tips = listOf(
                    "عمل کے دوران قربت۔",
                    "چھونے کے تجربے۔",
                    "مشترکہ تال۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "عمل کے دوران قربت۔",
                            "نیچے والا بیٹھے یا لیٹے۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "چھونے کے تجربے۔",
                            "اوپر آمنے سامنے بیٹھیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_missionary_twist",
            difficulty = Difficulty.ADVANCED,
            illustrationRes = R.drawable.pic_sk_missionary_twist,
            categoryId = CAT_ANAL,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Missionary With a Twist",
                category = "Anal Variations",
                summary = "Anal missionary with knees by armpits.",
                description = "Receiver's knees folded toward armpits with hips open. Requires lube and flexibility.",
                steps = listOf(
                    "Open hips wide.",
                    "Fold knees toward armpits.",
                    "Partner enters anally from front.",
                    "Use pillows under hips.",
                    "Go slowly.",
                ),
                tips = listOf(
                    "Worth the flexibility effort.",
                    "Deep sensation.",
                    "Keep lube nearby.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Worth the flexibility effort.",
                            "Open hips wide.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Deep sensation.",
                            "Fold knees toward armpits.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "مشنری ٹوئسٹ اینل",
                category = "پیچھے سے متبادل",
                summary = "گھٹنے بغلوں تک، پیچھے سے مشنری۔",
                description = "گھٹنے بغلوں کی طرف، کولہے کھلے۔ لوبریکنٹ اور لچک چاہیے۔",
                steps = listOf(
                    "کولہے کھولیں۔",
                    "گھٹنے بغلوں کی طرف۔",
                    "سامنے سے پیچھے داخلہ۔",
                    "تکیہ کولہے کے نیچے۔",
                    "آہستہ جائیں۔",
                ),
                tips = listOf(
                    "لچک کی محنت قابل ہے۔",
                    "گہرا احساس۔",
                    "لوبریکنٹ پاس رکھیں۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "لچک کی محنت قابل ہے۔",
                            "کولہے کھولیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "گہرا احساس۔",
                            "گھٹنے بغلوں کی طرف۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_on_stomach",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_on_stomach,
            categoryId = CAT_ANAL,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "On the Stomach (Anal)",
                category = "Anal Variations",
                summary = "Prone anal for gentle deep penetration.",
                description = "Receiver relaxes on stomach with pillow under head. Partner enters gently from behind.",
                steps = listOf(
                    "Receiver lies on stomach.",
                    "Pillow under head.",
                    "Partner enters from behind.",
                    "Keep movements gentle.",
                    "Both stay relaxed.",
                ),
                tips = listOf(
                    "Great for anal beginners.",
                    "Receiver fully relaxed.",
                    "Comfortable and chill.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Great for anal beginners.",
                            "Receiver lies on stomach.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Receiver fully relaxed.",
                            "Pillow under head.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "پیٹ کے بل اینل",
                category = "پیچھے سے متبادل",
                summary = "پیٹ کے بل آہستہ گہری پیچھے سے۔",
                description = "سر کے نیچے تکیہ، پیٹ کے بل آرام۔ آہستہ پیچھے سے۔",
                steps = listOf(
                    "پیٹ کے بل لیٹیں۔",
                    "سر کے نیچے تکیہ۔",
                    "پیچھے سے داخل ہوں۔",
                    "نرم حرکت۔",
                    "آرام رکھیں۔",
                ),
                tips = listOf(
                    "ابتدائیوں کے لیے۔",
                    "وصول کنندہ آرام میں۔",
                    "پرسکون۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "ابتدائیوں کے لیے۔",
                            "پیٹ کے بل لیٹیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "وصول کنندہ آرام میں۔",
                            "سر کے نیچے تکیہ۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_spooning_twist",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_spooning_twist,
            categoryId = CAT_ANAL,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Spooning With a Twist",
                category = "Anal Variations",
                summary = "Side-lying anal spooning.",
                description = "Classic spooning adapted for anal. Rock together to find angle and depth.",
                steps = listOf(
                    "Lie back-to-front spooning.",
                    "Apply anal lube.",
                    "Enter slowly from behind.",
                    "Rock hips together.",
                    "Hands free for touch.",
                ),
                tips = listOf(
                    "Comfort and intimacy help relax.",
                    "Connected feeling.",
                    "Free hands for stimulation.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Comfort and intimacy help relax.",
                            "Lie back-to-front spooning.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Connected feeling.",
                            "Apply anal lube.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "چمچہ ٹوئسٹ اینل",
                category = "پیچھے سے متبادل",
                summary = "سیدھے چمچے میں پیچھے سے۔",
                description = "چمچے والی پوزیشن پیچھے سے داخلہ کے لیے۔ ساتھ جھولیں۔",
                steps = listOf(
                    "چمچے کی طرح لیٹیں۔",
                    "لوبریکنٹ لگائیں۔",
                    "آہستہ پیچھے سے۔",
                    "کولہے ساتھ ہلائیں۔",
                    "ہاتھ آزاد۔",
                ),
                tips = listOf(
                    "آرام اور قربت مدد کرتی ہے۔",
                    "جڑا ہوا احساس۔",
                    "ہاتھ سے محرک۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "آرام اور قربت مدد کرتی ہے۔",
                            "چمچے کی طرح لیٹیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "جڑا ہوا احساس۔",
                            "لوبریکنٹ لگائیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_bbq_quickie",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_bbq_quickie,
            categoryId = CAT_BEACH,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "The BBQ Quickie",
                category = "Beach-Inspired",
                summary = "Outdoor bench quickie (private only).",
                description = "Summer outdoor bend-over at secluded bench. Public sex is illegal — use private areas only.",
                steps = listOf(
                    "Find truly private secluded area.",
                    "Receiver bends over bench.",
                    "Lift hem or adjust clothing.",
                    "Partner enters from behind.",
                    "Never at family gatherings.",
                ),
                tips = listOf(
                    "Summer heat adds thrill.",
                    "Voyeur fantasy in private only.",
                    "Avoid pool sex — irritation risk.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Summer heat adds thrill.",
                            "Find truly private secluded area.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Voyeur fantasy in private only.",
                            "Receiver bends over bench.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "بی بی کیو فوری",
                category = "ساحل",
                summary = "باہر بینچ پر فوری (صرف نجی جگہ)۔",
                description = "گرمیوں میں نجی بینچ پر جھکنا۔ عوامی جگہ غیر قانونی۔",
                steps = listOf(
                    "مکمل نجی جگہ تلاش کریں۔",
                    "بینچ پر جھکیں۔",
                    "لباس ایڈجسٹ کریں۔",
                    "پیچھے سے۔",
                    "خاندانی تقریبات میں نہیں۔",
                ),
                tips = listOf(
                    "گرمی کا جوش۔",
                    "صرف نجی میں فنتاسی۔",
                    "پول سے بچیں۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "گرمی کا جوش۔",
                            "مکمل نجی جگہ تلاش کریں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "صرف نجی میں فنتاسی۔",
                            "بینچ پر جھکیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_lounging_lioness",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_lounging_lioness,
            categoryId = CAT_BEACH,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "The Lounging Lioness",
                category = "Beach-Inspired",
                summary = "Receiver on top with legs closed on deck chair.",
                description = "Penetrating partner on back; receiver lies on top legs closed for tighter sensation.",
                steps = listOf(
                    "Partner lies on back on chair.",
                    "Receiver lies on top.",
                    "Keep legs together when ready.",
                    "Increases pressure on pleasure zones.",
                    "Less leg work than cowgirl.",
                ),
                tips = listOf(
                    "Less leg work than cowgirl.",
                    "Tighter sensation when legs close.",
                    "Great on private deck chairs.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Less leg work than cowgirl.",
                            "Partner lies on back on chair.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Tighter sensation when legs close.",
                            "Receiver lies on top.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "آرام دہ شیرنی",
                category = "ساحل",
                summary = "ڈیک کرسی پر اوپر، ٹانگیں بند۔",
                description = "نیچے والا پیٹ کے بل؛ اوپر والا ٹانگیں بند کر لیٹے۔",
                steps = listOf(
                    "نیچے والا کرسی پر پیٹ کے بل۔",
                    "اوپر والا اوپر لیٹے۔",
                    "ٹانگیں بند رکھیں۔",
                    "دباؤ بڑھتا ہے۔",
                    "کاؤگرل سے کم محنت۔",
                ),
                tips = listOf(
                    "کاؤگرل سے کم محنت۔",
                    "ٹانگیں بند کرنے سے تنگ احساس۔",
                    "نجی ڈیک کرسی پر بہترین۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "کاؤگرل سے کم محنت۔",
                            "نیچے والا کرسی پر پیٹ کے بل۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "ٹانگیں بند کرنے سے تنگ احساس۔",
                            "اوپر والا اوپر لیٹے۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_pouncing_panther",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_pouncing_panther,
            categoryId = CAT_BEACH,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Pouncing Panther",
                category = "Beach-Inspired",
                summary = "Poolside doggy on chair or towel.",
                description = "Doggy-style poolside on private chair or towel. Optional cool temperature play with ice pack.",
                steps = listOf(
                    "Ensure complete privacy.",
                    "Receiver on all fours on chair.",
                    "Partner enters from behind.",
                    "Optional ice pack under stomach.",
                    "Vitamin D and pleasure.",
                ),
                tips = listOf(
                    "Vitamin D plus pleasure.",
                    "Ice pack for temperature play.",
                    "Poolside private chair works best.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Vitamin D plus pleasure.",
                            "Ensure complete privacy.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Ice pack for temperature play.",
                            "Receiver on all fours on chair.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "چھلانگ مارتی پینتھر",
                category = "ساحل",
                summary = "پول کے کنارے ڈوگی۔",
                description = "نجی کرسی یا تولیے پر ڈوگی۔ آئس پیک سے ٹھنڈک کا کھیل۔",
                steps = listOf(
                    "مکمل نجی ہونے کا یقین۔",
                    "چاروں پر کرسی پر۔",
                    "پیچھے سے۔",
                    "آئس پیک اختیاری۔",
                    "دھوپ اور لطف۔",
                ),
                tips = listOf(
                    "دھوپ اور لطف۔",
                    "آئس پیک سے ٹھنڈک کا کھیل۔",
                    "نجی پول کنارے کی کرسی بہترین۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "دھوپ اور لطف۔",
                            "مکمل نجی ہونے کا یقین۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "آئس پیک سے ٹھنڈک کا کھیل۔",
                            "چاروں پر کرسی پر۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_teddy_bear",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_teddy_bear,
            categoryId = CAT_BEACH,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "The Teddy Bear",
                category = "Beach-Inspired",
                summary = "Kneeling proposal pose with straddle.",
                description = "One kneels proposal-style; receiver straddles one leg sliding down. Use mattress or yoga mat.",
                steps = listOf(
                    "Penetrating partner kneels on one knee.",
                    "Receiver straddles that leg.",
                    "Feet reach floor for leverage.",
                    "Face-to-face kissing.",
                    "Avoid carpet and hardwood.",
                ),
                tips = listOf(
                    "Great leverage to bounce.",
                    "Very intimate eye contact.",
                    "Reserved for soft surfaces.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Great leverage to bounce.",
                            "Penetrating partner kneels on one knee.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Very intimate eye contact.",
                            "Receiver straddles that leg.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "ٹیڈی بیئر",
                category = "ساحل",
                summary = "گھٹنے پر گھٹنے، اوپر بیٹھنا۔",
                description = "ایک گھٹنے پر گھٹنے؛ دوسرا ٹانگ پر بیٹھ کر نیچے۔ بستر یا میٹ پر۔",
                steps = listOf(
                    "ایک گھٹنے پر۔",
                    "ٹانگ پر بیٹھیں۔",
                    "پاؤں فرش پر سہارا۔",
                    "آمنے سامنے بوسہ۔",
                    "کارپٹ اور لکڑی سے بچیں۔",
                ),
                tips = listOf(
                    "اچھالنے کا سہارا۔",
                    "قریبی آنکھیں۔",
                    "نرم سطح پر۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "اچھالنے کا سہارا۔",
                            "ایک گھٹنے پر۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "قریبی آنکھیں۔",
                            "ٹانگ پر بیٹھیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_beach_doggy",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_beach_doggy,
            categoryId = CAT_BEACH,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Beach-Safe Doggy-Style",
                category = "Beach-Inspired",
                summary = "Doggy on towel avoiding sand.",
                description = "Lay towel, adjust swimsuits, enjoy doggy without sand in sensitive areas.",
                steps = listOf(
                    "Lay large towel flat.",
                    "Receiver on all fours on towel.",
                    "Adjust swimwear aside.",
                    "Partner kneels behind.",
                    "Minimize sand contact.",
                ),
                tips = listOf(
                    "Tailor-made for beach.",
                    "Bodies not pressed in heat.",
                    "Keeps sand away.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Tailor-made for beach.",
                            "Lay large towel flat.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Bodies not pressed in heat.",
                            "Receiver on all fours on towel.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "محفوظ ساحلی ڈوگی",
                category = "ساحل",
                summary = "تولیے پر ڈوگی، ریت سے بچاؤ۔",
                description = "تولیہ بچھائیں، سوئم سوٹ ایڈجسٹ، ریت سے بچیں۔",
                steps = listOf(
                    "بڑا تولیہ بچھائیں۔",
                    "تولیے پر چاروں پر۔",
                    "سوئم سوٹ ہٹائیں۔",
                    "پیچھے گھٹنوں پر۔",
                    "ریت سے بچیں۔",
                ),
                tips = listOf(
                    "ساحل کے لیے۔",
                    "گرمی میں جسم الگ۔",
                    "ریت دور۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "ساحل کے لیے۔",
                            "بڑا تولیہ بچھائیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "گرمی میں جسم الگ۔",
                            "تولیے پر چاروں پر۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_in_water",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_in_water,
            categoryId = CAT_BEACH,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "In the Water",
                category = "Beach-Inspired",
                summary = "Standing water intimacy below surface.",
                description = "Standing in safe clean water — looks like cuddling above surface. Choose safe water without currents.",
                steps = listOf(
                    "Choose clean secluded water.",
                    "Stand chest-deep together.",
                    "Pull swimsuits aside.",
                    "Maintain balance.",
                    "No parasites or strong currents.",
                ),
                tips = listOf(
                    "Refreshing on hot days.",
                    "Hidden below surface.",
                    "Romantic in waves.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Refreshing on hot days.",
                            "Choose clean secluded water.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Hidden below surface.",
                            "Stand chest-deep together.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "پانی میں",
                category = "ساحل",
                summary = "پانی میں کھڑے، نیچے نظر نہیں آتا۔",
                description = "صاف پانی میں کھڑے — اوپر سے گلے ملنے جیسا۔ محفوظ پانی چنیں۔",
                steps = listOf(
                    "صاف نجی پانی۔",
                    "سینے تک کھڑے۔",
                    "سوئم سوٹ ہٹائیں۔",
                    "توازن رکھیں۔",
                    "طوفان یا کیڑوں سے بچیں۔",
                ),
                tips = listOf(
                    "گرمی میں تروتازہ۔",
                    "نیچے چھپا ہوا۔",
                    "لہروں میں رومانوی۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "گرمی میں تروتازہ۔",
                            "صاف نجی پانی۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "نیچے چھپا ہوا۔",
                            "سینے تک کھڑے۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_beach_ball",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_beach_ball,
            categoryId = CAT_BEACH,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "On a Beach Ball",
                category = "Beach-Inspired",
                summary = "Receiver leans over inflatable ball.",
                description = "Beach ball supports receiver leaning forward while partner enters from behind. Playful and silly.",
                steps = listOf(
                    "Inflate sturdy beach ball.",
                    "Receiver leans body over ball.",
                    "Partner enters from behind.",
                    "Works at home too.",
                    "Reduces sand contact at beach.",
                ),
                tips = listOf(
                    "Infuses play into practice.",
                    "Unserious and fun.",
                    "Elevates above sand.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Infuses play into practice.",
                            "Inflate sturdy beach ball.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Unserious and fun.",
                            "Receiver leans body over ball.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "بیچ بال پر",
                category = "ساحل",
                summary = "فلائیٹ بال پر جھکنا۔",
                description = "بال سہارا دے؛ پیچھے سے داخلہ۔ تفریحی۔",
                steps = listOf(
                    "بال پھلائیں۔",
                    "بال پر جھکیں۔",
                    "پیچھے سے۔",
                    "گھر پر بھی۔",
                    "ریت کم لگے۔",
                ),
                tips = listOf(
                    "کھیل کا عنصر۔",
                    "ہلکی پھلکی مزہ۔",
                    "ریت سے اوپر۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "کھیل کا عنصر۔",
                            "بال پھلائیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "ہلکی پھلکی مزہ۔",
                            "بال پر جھکیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_beach_reverse",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_beach_reverse,
            categoryId = CAT_BEACH,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Reverse Cowgirl (Beach)",
                category = "Beach-Inspired",
                summary = "Beach reverse cowgirl on towel.",
                description = "Receiver faces away on towel while partner reclines. Protects from sand with hot view.",
                steps = listOf(
                    "Partner reclines on towel.",
                    "Receiver straddles facing away.",
                    "Ride and grind.",
                    "Sand stays away from receiver.",
                    "Partner enjoys the view.",
                ),
                tips = listOf(
                    "Sand stays off receiver.",
                    "Hot view for partner.",
                    "Beach-friendly reverse cowgirl.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Sand stays off receiver.",
                            "Partner reclines on towel.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Hot view for partner.",
                            "Receiver straddles facing away.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "الٹ کاؤگرل ساحل",
                category = "ساحل",
                summary = "تولیے پر الٹ کاؤگرل۔",
                description = "تولیے پر پیٹھ کر کے اوپر۔ ریت سے بچاؤ۔",
                steps = listOf(
                    "تولیے پر لیٹیں۔",
                    "پیٹھ کر کے اوپر بیٹھیں۔",
                    "رگڑیں۔",
                    "ریت دور۔",
                    "منظر لطف۔",
                ),
                tips = listOf(
                    "وصول کنندہ پر ریت نہیں۔",
                    "ساتھی کے لیے منظر۔",
                    "ساحل کے لیے الٹ کاؤگرل۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "وصول کنندہ پر ریت نہیں۔",
                            "تولیے پر لیٹیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "ساتھی کے لیے منظر۔",
                            "پیٹھ کر کے اوپر بیٹھیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_beach_standing",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_beach_standing,
            categoryId = CAT_BEACH,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Standing Up (Beach)",
                category = "Beach-Inspired",
                summary = "Wind-protected standing beach sex.",
                description = "Find secluded wind-protected spot, lean on sturdy support, pull swimsuits aside.",
                steps = listOf(
                    "Find secluded area.",
                    "Lean on sturdy support.",
                    "Pull swimwear aside.",
                    "Maintain eye contact.",
                    "Enjoy sun and waves.",
                ),
                tips = listOf(
                    "Eye contact in sun feels intimate.",
                    "Classic beach 101.",
                    "Wind protection helps.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Eye contact in sun feels intimate.",
                            "Find secluded area.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Classic beach 101.",
                            "Lean on sturdy support.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "ساحل پر کھڑے",
                category = "ساحل",
                summary = "ہوا سے محفوظ کھڑے ساحلی لطف۔",
                description = "نجی جگہ، مضبوط سہارا، سوئم سوٹ ہٹائیں۔",
                steps = listOf(
                    "نجی جگہ۔",
                    "مضبوط سہارا۔",
                    "سوئم سوٹ ہٹائیں۔",
                    "آنکھوں کا رابطہ۔",
                    "دھوپ اور لہریں۔",
                ),
                tips = listOf(
                    "دھوپ میں آنکھیں قریبی۔",
                    "ساحلی کلاسک۔",
                    "ہوا سے بچاؤ مددگار۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "دھوپ میں آنکھیں قریبی۔",
                            "نجی جگہ۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "ساحلی کلاسک۔",
                            "مضبوط سہارا۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_under_blanket",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_under_blanket,
            categoryId = CAT_BEACH,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Under a Blanket",
                category = "Beach-Inspired",
                summary = "Discreet spooning under beach blanket.",
                description = "Simple spooning wrapped in blanket after beach clears. Subtle and intimate.",
                steps = listOf(
                    "Wait until beach is mostly empty.",
                    "Wrap in large blanket.",
                    "Spoon together intimately.",
                    "Move slowly and quietly.",
                    "Stay aware of surroundings.",
                ),
                tips = listOf(
                    "Hotter because it's hidden.",
                    "More subtle.",
                    "Extra closeness.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Hotter because it's hidden.",
                            "Wait until beach is mostly empty.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "More subtle.",
                            "Wrap in large blanket.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "کمبل تلے",
                category = "ساحل",
                summary = "ساحلی کمبل میں چمچہ۔",
                description = "ساحل خالی ہونے کے بعد کمبل میں چمچہ۔ چھپا اور قریبی۔",
                steps = listOf(
                    "ساحل خالی ہو۔",
                    "بڑے کمبل میں لپیٹیں۔",
                    "چمچے کی طرح۔",
                    "آہستہ حرکت۔",
                    "ارد گرد دیکھتے رہیں۔",
                ),
                tips = listOf(
                    "چھپا ہونے سے پرکشش۔",
                    "زیادہ باریک۔",
                    "اضافی قربت۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "چھپا ہونے سے پرکشش۔",
                            "ساحل خالی ہو۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "زیادہ باریک۔",
                            "بڑے کمبل میں لپیٹیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_closed_business",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_closed_business,
            categoryId = CAT_ORGASM,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Closed for Business",
                category = "For Vaginal Orgasm",
                summary = "Oral with receiver's legs closed.",
                description = "Receiver lies on back legs closed while partner performs oral — pressure where many want it.",
                steps = listOf(
                    "Receiver lies back legs together.",
                    "Partner performs oral over closed legs.",
                    "Build heat with pressure.",
                    "Play with power dynamic.",
                    "Communicate intensity.",
                ),
                tips = listOf(
                    "Intense orgasm potential.",
                    "Power play dynamic.",
                    "Targets clitoral pressure.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Intense orgasm potential.",
                            "Receiver lies back legs together.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Power play dynamic.",
                            "Partner performs oral over closed legs.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "بند کاروبار",
                category = "اندام نہانی لطف",
                summary = "ٹانگیں بند، زبانی کلائٹورل محرک۔",
                description = "پیٹ کے بل ٹانگیں بند؛ ساتھی زبانی محرک دے۔",
                steps = listOf(
                    "پیٹ کے بل ٹانگیں ملائیں۔",
                    "زبانی محرک دیں۔",
                    "دباؤ سے گرمی بڑھائیں۔",
                    "اختیار کھیلیں۔",
                    "شدت بتائیں۔",
                ),
                tips = listOf(
                    "شدید لطف کا امکان۔",
                    "اختیار کا کھیل۔",
                    "کلائٹورل دباؤ۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "شدید لطف کا امکان۔",
                            "پیٹ کے بل ٹانگیں ملائیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "اختیار کا کھیل۔",
                            "زبانی محرک دیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_high_heels",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_high_heels,
            categoryId = CAT_ORGASM,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "In High Heels",
                category = "For Vaginal Orgasm",
                summary = "Standing bent-forward at counter or stairs.",
                description = "Receiver bends at counter or sink. Heels or stairs help height differences.",
                steps = listOf(
                    "Receiver bends over sturdy surface.",
                    "Use heels for height match.",
                    "Stairs with banister work too.",
                    "Partner enters from behind.",
                    "Try bathroom mirror.",
                ),
                tips = listOf(
                    "Animalistic standing energy.",
                    "Mirror adds performer vibe.",
                    "Mind height differences.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Animalistic standing energy.",
                            "Receiver bends over sturdy surface.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Mirror adds performer vibe.",
                            "Use heels for height match.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "اونچی ایڑیوں میں",
                category = "اندام نہانی لطف",
                summary = "کاؤنٹر یا سیڑھی پر جھک کر کھڑے۔",
                description = "کاؤنٹر پر جھکیں۔ ایڑی یا سیڑھی اونچائی کے فرق میں مدد۔",
                steps = listOf(
                    "مضبوط سطح پر جھکیں۔",
                    "ایڑی سے اونچائی ملائیں۔",
                    "سیڑھی بھی چلے۔",
                    "پیچھے سے۔",
                    "آئینہ آزمائیں۔",
                ),
                tips = listOf(
                    "کھڑے جانوری جوش۔",
                    "آئینہ پرفارمر والا۔",
                    "اونچائی کا فرق دیکھیں۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "کھڑے جانوری جوش۔",
                            "مضبوط سطح پر جھکیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "آئینہ پرفارمر والا۔",
                            "ایڑی سے اونچائی ملائیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_drop_box",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_drop_box,
            categoryId = CAT_ORGASM,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "The Drop Box",
                category = "For Vaginal Orgasm",
                summary = "Hips dangling off bed edge.",
                description = "Receiver lies at bed edge hips dangling. Partner bends knees to align. Hands free for clitoral stimulation.",
                steps = listOf(
                    "Receiver lies at bed edge.",
                    "Hips hang off slightly.",
                    "Partner stands between legs.",
                    "Wrap legs or rest on shoulders.",
                    "Both hands free for clitoral play.",
                ),
                tips = listOf(
                    "Simultaneous clitoral and vaginal stimulation.",
                    "Great hip angle.",
                    "Works for all anatomies.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Simultaneous clitoral and vaginal stimulation.",
                            "Receiver lies at bed edge.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Great hip angle.",
                            "Hips hang off slightly.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "ڈراپ باکس",
                category = "اندام نہانی لطف",
                summary = "کولہے بستر کے کنارے باہر۔",
                description = "بستر کے کنارے کولہے باہر؛ ہاتھ سے کلائٹورس۔",
                steps = listOf(
                    "بستر کے کنارے لیٹیں۔",
                    "کولہے باہر۔",
                    "درمیان کھڑا ساتھی۔",
                    "ٹانگیں لپیٹیں یا کندھوں پر۔",
                    "ہاتھ سے کلائٹورس۔",
                ),
                tips = listOf(
                    "کلائٹورل اور اندام نہانی ساتھ۔",
                    "بہترین کولہے زاویہ۔",
                    "ہر جسم کے لیے۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "کلائٹورل اور اندام نہانی ساتھ۔",
                            "بستر کے کنارے لیٹیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "بہترین کولہے زاویہ۔",
                            "کولہے باہر۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_g_whiz",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_g_whiz,
            categoryId = CAT_ORGASM,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "The G-Whiz",
                category = "For Vaginal Orgasm",
                summary = "Lifted missionary with hip cushion.",
                description = "Receiver props hips on wedge or firm cushion for maximum G-zone stimulation.",
                steps = listOf(
                    "Place wedge under receiver's hips.",
                    "Receiver lies back comfortably.",
                    "Partner enters from front.",
                    "Adjust cushion height.",
                    "Maximize depth for G-spot.",
                ),
                tips = listOf(
                    "Named for G-zone focus.",
                    "Helps shorter phallus depth.",
                    "Shifts bellies out of way.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Named for G-zone focus.",
                            "Place wedge under receiver's hips.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Helps shorter phallus depth.",
                            "Receiver lies back comfortably.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "جی وہز",
                category = "اندام نہانی لطف",
                summary = "تکیے پر اونچے کولہے والی مشنری۔",
                description = "مثلثی تکیہ یا گدا سے جی سپاٹ محرک۔",
                steps = listOf(
                    "تکیہ کولہے کے نیچے۔",
                    "آرام سے پیٹ کے بل۔",
                    "سامنے سے داخلہ۔",
                    "اونچائی ایڈجسٹ۔",
                    "جی سپاٹ کے لیے گہرائی۔",
                ),
                tips = listOf(
                    "جی زون کے لیے۔",
                    "چھوٹے سائز میں مدد۔",
                    "پیٹ ہٹ جاتا ہے۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "جی زون کے لیے۔",
                            "تکیہ کولہے کے نیچے۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "چھوٹے سائز میں مدد۔",
                            "آرام سے پیٹ کے بل۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_tilt_whirl",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_tilt_whirl,
            categoryId = CAT_ORGASM,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "The Tilt-a-Whirl",
                category = "For Vaginal Orgasm",
                summary = "Face-to-face seated lean-back grind.",
                description = "Partner sits feet on floor; receiver sits lap face-to-face. Lean back holding arms and grind.",
                steps = listOf(
                    "Partner sits feet on floor.",
                    "Receiver sits lap facing.",
                    "Hold each other's arms.",
                    "Lean back together.",
                    "Find rhythm and balance.",
                ),
                tips = listOf(
                    "Trust exercise plus pleasure.",
                    "Unique G-spot angle.",
                    "Use wall for support if needed.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Trust exercise plus pleasure.",
                            "Partner sits feet on floor.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Unique G-spot angle.",
                            "Receiver sits lap facing.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "ٹلٹ اے وہرل",
                category = "اندام نہانی لطف",
                summary = "بیٹھ کر آگے جھک کر رگڑنا۔",
                description = "نیچے والا پاؤں فرش پر؛ اوپر گود میں آمنے سامنے۔ پیچھے جھک کر رگڑیں۔",
                steps = listOf(
                    "پاؤں فرش پر بیٹھیں۔",
                    "گود میں آمنے سامنے۔",
                    "بازو پکڑیں۔",
                    "ساتھ پیچھے جھکیں۔",
                    "تال اور توازن۔",
                ),
                tips = listOf(
                    "اعتماد اور لطف۔",
                    "منفرد جی زاویہ۔",
                    "دیوار سے سہارا۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "اعتماد اور لطف۔",
                            "پاؤں فرش پر بیٹھیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "منفرد جی زاویہ۔",
                            "گود میں آمنے سامنے۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_circus_freak",
            difficulty = Difficulty.ADVANCED,
            illustrationRes = R.drawable.pic_sk_circus_freak,
            categoryId = CAT_CREATIVE,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "The Circus Freak / Cowpoke",
                category = "Creative",
                summary = "Deep squat reverse ride with legs pulled in.",
                description = "Penetrating partner lies back legs to chest. Receiver squats facing away lowering fully.",
                steps = listOf(
                    "Partner lies back legs pulled to chest.",
                    "Receiver faces away squatting.",
                    "Lower until thighs touch.",
                    "Bounce with leg muscles.",
                    "Switch to reverse cowgirl if needed.",
                ),
                tips = listOf(
                    "Rider controls internal hot spots.",
                    "Needs flexibility or length.",
                    "Easy fallback positions.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Rider controls internal hot spots.",
                            "Partner lies back legs pulled to chest.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Needs flexibility or length.",
                            "Receiver faces away squatting.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "سرکس فریک / کاوپوک",
                category = "تخلیقی",
                summary = "گہری اسکواٹ الٹ سواری۔",
                description = "نیچے والا ٹانگیں سینے کی طرف؛ اوپر الٹ بیٹھ کر نیچے۔",
                steps = listOf(
                    "پیٹ کے بل ٹانگیں کھینچیں۔",
                    "الٹ اسکواٹ میں بیٹھیں۔",
                    "مکمل نیچے بیٹھیں۔",
                    "رانوں سے اچھلیں۔",
                    "ضرورت ہو تو الٹ کاؤگرل۔",
                ),
                tips = listOf(
                    "اندرونی محرک کنٹرول۔",
                    "لچک یا لمبائی چاہیے۔",
                    "آسان متبادل۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "اندرونی محرک کنٹرول۔",
                            "پیٹ کے بل ٹانگیں کھینچیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "لچک یا لمبائی چاہیے۔",
                            "الٹ اسکواٹ میں بیٹھیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_froggie",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_froggie,
            categoryId = CAT_CREATIVE,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Froggie-Style",
                category = "Creative",
                summary = "Receiver crouches like frog on hands and feet.",
                description = "Receiver crouches in front balancing on feet and hands while partner kneels behind.",
                steps = listOf(
                    "Partner kneels behind.",
                    "Receiver crouches frog-like.",
                    "Balance on feet and hands.",
                    "Lean forward or back for depth.",
                    "Switch positions easily.",
                ),
                tips = listOf(
                    "Strange at first then loved.",
                    "Easy depth adjustment.",
                    "Keeps fun going.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Strange at first then loved.",
                            "Partner kneels behind.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Easy depth adjustment.",
                            "Receiver crouches frog-like.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "فروگی سٹائل",
                category = "تخلیقی",
                summary = "مینڈک کی طرح ہاتھ اور پاؤں پر۔",
                description = "سامنے والا مینڈک کی طرح جھکے؛ پیچھے والا گھٹنوں پر۔",
                steps = listOf(
                    "پیچھے گھٹنوں پر۔",
                    "مینڈک جیسا جھکیں۔",
                    "پاؤں اور ہاتھ پر توازن۔",
                    "آگے پیچھے سے گہرائی۔",
                    "آسانی سے بدلیں۔",
                ),
                tips = listOf(
                    "پہلے عجیب پھر پسند۔",
                    "گہرائی آسان۔",
                    "تفریح جاری۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "پہلے عجیب پھر پسند۔",
                            "پیچھے گھٹنوں پر۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "گہرائی آسان۔",
                            "مینڈک جیسا جھکیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_lap_dance_creative",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_lap_dance_creative,
            categoryId = CAT_CREATIVE,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Lap Dance (Creative)",
                category = "Creative",
                summary = "Music-driven lap dance to penetration.",
                description = "Partner sits while you move to music, tease, then slide down facing away for extra spice.",
                steps = listOf(
                    "Turn on music.",
                    "Partner sits on chair or bed.",
                    "Dance and tease.",
                    "Slide down for penetration.",
                    "Facing away adds spice.",
                ),
                tips = listOf(
                    "Fulfills lap dance fantasies.",
                    "Receiver controls heat.",
                    "Fast mutual turn-on.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Fulfills lap dance fantasies.",
                            "Turn on music.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Receiver controls heat.",
                            "Partner sits on chair or bed.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "لیپ ڈانس تخلیقی",
                category = "تخلیقی",
                summary = "موسیقی پر لیپ ڈانس سے داخلہ۔",
                description = "ساتھی بیٹھے؛ موسیقی پر حرکت، چھوا، پھر پیٹھ کر کے نیچے۔",
                steps = listOf(
                    "موسیقی چلائیں۔",
                    "ساتھی بیٹھے۔",
                    "ناچیں اور چھوئیں۔",
                    "نیچے بیٹھ کر داخلہ۔",
                    "پیٹھ کر کے تیز۔",
                ),
                tips = listOf(
                    "لیپ ڈانس خواب۔",
                    "اوپر والا گرمی طے کرے۔",
                    "جلدی جوش۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "لیپ ڈانس خواب۔",
                            "موسیقی چلائیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "اوپر والا گرمی طے کرے۔",
                            "ساتھی بیٹھے۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_yogi",
            difficulty = Difficulty.ADVANCED,
            illustrationRes = R.drawable.pic_sk_yogi,
            categoryId = CAT_CREATIVE,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "The Yogi",
                category = "Creative",
                summary = "Upside-down wheelbarrow yoga pose.",
                description = "Receiver mimics wheelbarrow pushing off floor arching back. Needs firm floor and strength.",
                steps = listOf(
                    "Use firm floor surface.",
                    "Receiver pushes off with arms and feet.",
                    "Arch back for angle.",
                    "Partner enters from behind.",
                    "Practice balance first.",
                ),
                tips = listOf(
                    "Worth strength effort.",
                    "Hot penetration angle.",
                    "Hip movement adds stimulation.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Worth strength effort.",
                            "Use firm floor surface.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Hot penetration angle.",
                            "Receiver pushes off with arms and feet.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "یوگی",
                category = "تخلیقی",
                summary = "الٹا وہیل بیرو یوگا۔",
                description = "وہیل بیرو جیسا فرش سے دھکا؛ مضبوط فرش اور طاقت۔",
                steps = listOf(
                    "مضبوط فرش۔",
                    "بازو اور پاؤں سے اٹھیں۔",
                    "کمر آرچ کریں۔",
                    "پیچھے سے۔",
                    "پہلے توازن مشق۔",
                ),
                tips = listOf(
                    "طاقت قابل ہے۔",
                    "پرکشش زاویہ۔",
                    "کولہے کی حرکت۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "طاقت قابل ہے۔",
                            "مضبوط فرش۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "پرکشش زاویہ۔",
                            "بازو اور پاؤں سے اٹھیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_inverted_missionary",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_inverted_missionary,
            categoryId = CAT_CREATIVE,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Inverted Missionary",
                category = "Creative",
                summary = "Reverse cowgirl on top with drag control.",
                description = "Receiver on top facing away controlling penetration with forward and back lean.",
                steps = listOf(
                    "Partner lies on back.",
                    "Receiver mounts facing away.",
                    "Lean forward and back.",
                    "Control penetration drag.",
                    "Enjoy the view for partner.",
                ),
                tips = listOf(
                    "Receiver fully in control.",
                    "Delicious drag sensation.",
                    "Reverse cowgirl upgrade.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Receiver fully in control.",
                            "Partner lies on back.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Delicious drag sensation.",
                            "Receiver mounts facing away.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "الٹ مشنری",
                category = "تخلیقی",
                summary = "اوپر الٹ کاؤگرل، گھسیٹنے کا کنٹرول۔",
                description = "اوپر پیٹھ کر کے؛ آگے پیچھے جھک کر گہرائی۔",
                steps = listOf(
                    "نیچے پیٹ کے بل۔",
                    "الٹ اوپر بیٹھیں۔",
                    "آگے پیچھے جھکیں۔",
                    "گہرائی کنٹرول۔",
                    "منظر لطف۔",
                ),
                tips = listOf(
                    "اوپر والا مکمل کنٹرول۔",
                    "گھسیٹنے کا لطف۔",
                    "بہتر الٹ کاؤگرل۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "اوپر والا مکمل کنٹرول۔",
                            "نیچے پیٹ کے بل۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "گھسیٹنے کا لطف۔",
                            "الٹ اوپر بیٹھیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_cowpoke",
            difficulty = Difficulty.ADVANCED,
            illustrationRes = R.drawable.pic_sk_cowpoke,
            categoryId = CAT_CREATIVE,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "The Cowpoke",
                category = "Creative",
                summary = "Squatting reverse ride legs-to-chest base.",
                description = "Same as Circus Freak — partner legs to chest, receiver squats and bounces controlling depth.",
                steps = listOf(
                    "Base partner pulls legs to chest.",
                    "Receiver squats facing away.",
                    "Lower fully onto partner.",
                    "Bounce at preferred rhythm.",
                    "Switch if flexibility lacking.",
                ),
                tips = listOf(
                    "Stimulates G, A, and cervix.",
                    "Best with flexibility.",
                    "Easy switch to classic reverse.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Stimulates G, A, and cervix.",
                            "Base partner pulls legs to chest.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Best with flexibility.",
                            "Receiver squats facing away.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "کاؤپوک",
                category = "تخلیقی",
                summary = "اسکواٹ الٹ سواری۔",
                description = "نیچے والی ٹانگیں سینے کی طرف؛ اوپر اسکواٹ میں اچھال۔",
                steps = listOf(
                    "نیچے ٹانگیں کھینچیں۔",
                    "الٹ اسکواٹ۔",
                    "مکمل بیٹھیں۔",
                    "اپنی تال سے اچھلیں۔",
                    "لچک کم ہو تو بدلیں۔",
                ),
                tips = listOf(
                    "جی، اے، گریوائیکس۔",
                    "لچک کے ساتھ بہتر۔",
                    "آسان متبادل۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "جی، اے، گریوائیکس۔",
                            "نیچے ٹانگیں کھینچیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "لچک کے ساتھ بہتر۔",
                            "الٹ اسکواٹ۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_field_goal",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_field_goal,
            categoryId = CAT_CREATIVE,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Field Goal",
                category = "Creative",
                summary = "Receiver hips on partner's lap field-goal style.",
                description = "Receiver lies back hips on partner's lap in field goal position for unique penetration angle.",
                steps = listOf(
                    "Partner sits with lap accessible.",
                    "Receiver lies back hips on lap.",
                    "Extend legs in field goal shape.",
                    "Partner supports and thrusts.",
                    "Optional touchdown arms.",
                ),
                tips = listOf(
                    "Funny look, great angle.",
                    "Needs core strength.",
                    "Partner supports during thrusts.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Funny look, great angle.",
                            "Partner sits with lap accessible.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Needs core strength.",
                            "Receiver lies back hips on lap.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "فیلڈ گول",
                category = "تخلیقی",
                summary = "کولہے ساتھی کی گود پر فیلڈ گول۔",
                description = "پیٹ کے بل کولہے ساتھی کی گود پر، منفرد زاویہ۔",
                steps = listOf(
                    "ساتھی بیٹھے۔",
                    "کولہے گود پر لیٹیں۔",
                    "ٹانگیں فیلڈ گول۔",
                    "ساتھی سہارا دے۔",
                    "ہاتھ اختیاری۔",
                ),
                tips = listOf(
                    "عجیب منظر، اچھا زاویہ۔",
                    "کور طاقت۔",
                    "ساتھی سہارا۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "عجیب منظر، اچھا زاویہ۔",
                            "ساتھی بیٹھے۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "کور طاقت۔",
                            "کولہے گود پر لیٹیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_fumble",
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_sk_fumble,
            categoryId = CAT_CREATIVE,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Fumble",
                category = "Creative",
                summary = "All-hands creative touching position.",
                description = "Pull partner close with hands everywhere — between legs, belly, chest. Creativity and dirty talk welcome.",
                steps = listOf(
                    "Lie facing each other.",
                    "Touch wherever feels good.",
                    "Between legs, down belly, chest.",
                    "Pull partner close.",
                    "Add dirty talk freely.",
                ),
                tips = listOf(
                    "All about creativity.",
                    "No single correct form.",
                    "Communication is pleasure.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "All about creativity.",
                            "Lie facing each other.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "No single correct form.",
                            "Touch wherever feels good.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "فمبل",
                category = "تخلیقی",
                summary = "ہاتھوں سے تخلیقی چھونا۔",
                description = "قریب کھینچیں، ہاتھ ہر جگہ — رانوں، پیٹ، سینے۔ تخلیق اور بات۔",
                steps = listOf(
                    "آمنے سامنے لیٹیں۔",
                    "جہاں اچھا لگے چھوئیں۔",
                    "رانوں، پیٹ، سینے۔",
                    "قریب کھینچیں۔",
                    "آہستہ گندی بات۔",
                ),
                tips = listOf(
                    "تخلیق پر مبنی۔",
                    "ایک صحیح شکل نہیں۔",
                    "بات چیت لطف ہے۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "تخلیق پر مبنی۔",
                            "آمنے سامنے لیٹیں۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "ایک صحیح شکل نہیں۔",
                            "جہاں اچھا لگے چھوئیں۔",
                        )
                ),
            )
        ),        Posture(
            id = "sk_wide_receiver",
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_sk_wide_receiver,
            categoryId = CAT_CREATIVE,
            sourceUrl = "https://www.sheknows.com/health-and-wellness/slideshow/5919/sex-positions-to-try-before-you-die/",
            isImagination = false,
            english = LocalizedContent(
                name = "Wide Receiver",
                category = "Creative",
                summary = "Legs elevated spread wide for oral or penetration.",
                description = "Receiver on back legs elevated and spread. Partner kneels with room for oral, penetration, or manual — or all three.",
                steps = listOf(
                    "Receiver lies back.",
                    "Elevate and spread legs wide.",
                    "Partner kneels before them.",
                    "Oral, penetrative, or manual.",
                    "Receiver directs with hands on head.",
                ),
                tips = listOf(
                    "Sexy power dynamic.",
                    "Receiver calls the plays.",
                    "Room for combination play.",
                ),
                forMan = PartnerRole(
                    position = "Active partner",
                    guidance = listOf(
                            "Position: Active partner",
                            "Sexy power dynamic.",
                            "Receiver lies back.",
                        )
                ),
                forWoman = PartnerRole(
                    position = "Receiving partner",
                    guidance = listOf(
                            "Position: Receiving partner",
                            "Receiver calls the plays.",
                            "Elevate and spread legs wide.",
                        )
                ),
            ),
            urdu = LocalizedContent(
                name = "وائڈ ریسیور",
                category = "تخلیقی",
                summary = "ٹانگیں اونچی چوڑی — زبانی یا داخلہ۔",
                description = "پیٹ کے بل ٹانگیں اونچی کھولیں۔ ساتھی گھٹنوں پر — زبانی، داخلہ، ہاتھ۔",
                steps = listOf(
                    "پیٹ کے بل۔",
                    "ٹانگیں اونچی چوڑی۔",
                    "ساتھی سامنے گھٹنوں پر۔",
                    "زبانی، داخلہ یا ہاتھ۔",
                    "سر رہنمائی کریں۔",
                ),
                tips = listOf(
                    "پرکشش اختیار۔",
                    "وصول کنندہ حکم دے۔",
                    "ملا جلا لطف۔",
                ),
                forMan = PartnerRole(
                    position = "فعال ساتھی",
                    guidance = listOf(
                            "پوزیشن: فعال ساتھی",
                            "پرکشش اختیار۔",
                            "پیٹ کے بل۔",
                        )
                ),
                forWoman = PartnerRole(
                    position = "وصول کنندہ",
                    guidance = listOf(
                            "پوزیشن: وصول کنندہ",
                            "وصول کنندہ حکم دے۔",
                            "ٹانگیں اونچی چوڑی۔",
                        )
                ),
            )
        )
    )
}
