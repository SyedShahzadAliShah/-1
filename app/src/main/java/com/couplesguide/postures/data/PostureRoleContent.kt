package com.couplesguide.postures.data

object PostureRoleContent {

    data class BilingualRoles(
        val enMan: PartnerRole,
        val urMan: PartnerRole,
        val enWoman: PartnerRole,
        val urWoman: PartnerRole
    )

    fun getRoles(postureId: String): BilingualRoles? = roles[postureId]

    private val roles: Map<String, BilingualRoles> = mapOf(
        "missionary" to BilingualRoles(
            enMan = PartnerRole(
                position = "On top, facing her, supporting weight on hands or forearms",
                guidance = listOf(
                    "Keep your weight distributed — don't press down heavily on her chest",
                    "Adjust hip angle by shifting knees wider or narrower",
                    "Maintain eye contact and check in with gentle words",
                    "Control depth and pace — start slow and respond to her feedback"
                )
            ),
            urMan = PartnerRole(
                position = "اوپر، اس کے سامنے، وزن ہاتھوں یا بازوؤں پر",
                guidance = listOf(
                    "وزن برابر رکھیں — سینے پر زیادہ دباؤ نہ ڈالیں",
                    "گھٹنوں کی چوڑائی بدل کر کولہے کا زاویہ ایڈجسٹ کریں",
                    "آنکھوں سے رابطہ رکھیں اور نرم الفاظ سے پوچھتے رہیں",
                    "گہرائی اور رفتار کنٹرول کریں — آہستہ شروع کریں"
                )
            ),
            enWoman = PartnerRole(
                position = "Lying on her back with knees slightly bent, facing him",
                guidance = listOf(
                    "Place a pillow under your lower back or hips for a better angle",
                    "Wrap legs around his waist or keep feet flat on the bed",
                    "Guide his hips with your hands to show preferred depth",
                    "Use your pelvic floor to adjust sensation — squeeze or relax as needed"
                )
            ),
            urWoman = PartnerRole(
                position = "پیٹ کے بل، گھٹنے ہلکے موڑے، اس کے سامنے",
                guidance = listOf(
                    "کمر یا کولہے کے نیچے تکیہ رکھیں بہتر زاویے کے لیے",
                    "ٹانگیں اس کی کمر کے گرد لپیٹیں یا پاؤں بستر پر رکھیں",
                    "ہاتھوں سے کولہے رہنمائی کریں پسندیدہ گہرائی دکھانے کے لیے",
                    "پیلویک پٹھوں سے احساس ایڈجسٹ کریں"
                )
            )
        ),
        "cowgirl" to BilingualRoles(
            enMan = PartnerRole(
                position = "Lying on his back, relaxed, hands free to touch her",
                guidance = listOf(
                    "Let her set the pace — your role is to support and respond",
                    "Place hands on her hips, waist, or breasts as she prefers",
                    "Lift hips slightly to meet her movement if it feels good",
                    "Communicate if depth becomes uncomfortable"
                )
            ),
            urMan = PartnerRole(
                position = "پیٹ کے بل لیٹا، آرام سے، ہاتھ آزاد چھونے کے لیے",
                guidance = listOf(
                    "اسے رفتار طے کرنے دیں — آپ کا کردار سہارا اور ردعمل ہے",
                    "ہاتھ کولہے، کمر یا سینے پر رکھیں جیسا وہ پسند کرے",
                    "اگر اچھا لگے تو کولہے ہلکا اٹھائیں",
                    "گہرائی تکلیف دہ ہو تو بتائیں"
                )
            ),
            enWoman = PartnerRole(
                position = "Straddling him on top, facing him, controlling movement",
                guidance = listOf(
                    "Kneel or sit on his hips — use thighs for balance and control",
                    "Rock forward and back or grind in circles to find your angle",
                    "Lean forward to kiss or sit upright for deeper penetration",
                    "Brace hands on his chest — you control depth and speed entirely"
                )
            ),
            urWoman = PartnerRole(
                position = "اوپر اس کے اوپر، آمنے سامنے، حرکت کنٹرول کرتے ہوئے",
                guidance = listOf(
                    "کولہوں پر بیٹھیں — رانوں سے توازن اور کنٹرول",
                    "آگے پیچھے یا گول گھمائیں اپنا زاویہ تلاش کرنے کے لیے",
                    "بوسے کے لیے جھکیں یا گہری داخلہ کے لیے سیدھے بیٹھیں",
                    "سینے پر ہاتھ رکھیں — گہرائی اور رفتار مکمل آپ کے کنٹرول میں"
                )
            )
        ),
        "spooning" to BilingualRoles(
            enMan = PartnerRole(
                position = "Behind her, curled around her body, entering from the rear",
                guidance = listOf(
                    "Wrap your arm around her waist or hold her close from behind",
                    "Keep movements slow and shallow — this position is about closeness",
                    "Kiss her neck and shoulder to deepen intimacy",
                    "Adjust your hip angle by bending your top knee forward"
                )
            ),
            urMan = PartnerRole(
                position = "اس کے پیچھے، جسم کے گرد لپٹا، پیچھے سے",
                guidance = listOf(
                    "بازو کمر کے گرد لپیٹیں یا پیچھے سے قریب رکھیں",
                    "حرکت آہستہ اور ہلکی رکھیں — یہ پوزیشن قربت کے لیے ہے",
                    "گردن اور کندھے پر بوسہ دیں",
                    "اوپر والے گھٹنے کو آگے موڑ کر زاویہ بدلیں"
                )
            ),
            enWoman = PartnerRole(
                position = "Lying on her side in front, slightly curled forward",
                guidance = listOf(
                    "Bend knees slightly and place a pillow between them for hip alignment",
                    "Reach back to guide his hips or hold his hand",
                    "Press back into him to control depth",
                    "Ideal for tired evenings — minimal effort required"
                )
            ),
            urWoman = PartnerRole(
                position = "سامنے سیدھے لیٹے، ہلکا آگے جھکے",
                guidance = listOf(
                    "گھٹنے ہلکے موڑیں اور درمیان تکیہ رکھیں",
                    "پیچھے ہاتھ بڑھا کر کولہے رہنمائی کریں",
                    "پیچھے دباؤ سے گہرائی کنٹرول کریں",
                    "تھکی ہوئی شاموں کے لیے بہترین — کم محنت"
                )
            )
        ),
        "side_by_side" to BilingualRoles(
            enMan = PartnerRole(
                position = "Lying on his side, facing her, legs intertwined with hers",
                guidance = listOf(
                    "Place top leg over her hip for closer contact",
                    "Use your hand on her lower back or hip to guide rhythm",
                    "Keep movements gentle — this position favors slow intimacy",
                    "Maintain eye contact at close range"
                )
            ),
            urMan = PartnerRole(
                position = "سیدھے اس کے سامنے، ٹانگیں آپس میں",
                guidance = listOf(
                    "اوپر والی ٹانگ اس کی ران پر رکھیں",
                    "کمر یا کولہے پر ہاتھ سے تال رہنمائی کریں",
                    "حرکت نرم رکھیں — یہ پوزیشن آہستہ قربت کے لیے ہے",
                    "قریب سے آنکھوں کا رابطہ رکھیں"
                )
            ),
            enWoman = PartnerRole(
                position = "Lying on her side, facing him, equal participation",
                guidance = listOf(
                    "Wrap top leg over his hip to pull him closer",
                    "Rock hips together to find a shared rhythm",
                    "Use your free hand to touch his chest or guide movement",
                    "Whisper and kiss — this position is built for emotional connection"
                )
            ),
            urWoman = PartnerRole(
                position = "سیدھے اس کے سامنے، برابر شرکت",
                guidance = listOf(
                    "اوپر والی ٹانگ اس کی ران پر لپیٹیں",
                    "کولہے ساتھ ہلائیں مشترکہ تال کے لیے",
                    "آزاد ہاتھ سے سینے کو چھوئیں یا رہنمائی کریں",
                    "آہستہ باتیں اور بوسے — جذباتی تعلق کے لیے بہترین"
                )
            )
        ),
        "doggy" to BilingualRoles(
            enMan = PartnerRole(
                position = "Kneeling or standing behind her, holding her hips",
                guidance = listOf(
                    "Grip her hips gently — never pull aggressively",
                    "Start with slow, shallow thrusts and increase only with her consent",
                    "Check in verbally — rear entry can feel intense",
                    "Vary angle by standing taller or kneeling lower"
                )
            ),
            urMan = PartnerRole(
                position = "پیچھے گھٹنوں یا کھڑے، کولہے پکڑے",
                guidance = listOf(
                    "کولہے نرمی سے پکڑیں — زبردستی نہ کھینچیں",
                    "آہستہ ہلکی جھٹکوں سے شروع کریں",
                    "زبانی پوچھتے رہیں — یہ پوزیشن شدید ہو سکتی ہے",
                    "اونچا کھڑے یا نیچے بیٹھ کر زاویہ بدلیں"
                )
            ),
            enWoman = PartnerRole(
                position = "On hands and knees (or lying flat), presenting from behind",
                guidance = listOf(
                    "Place a firm pillow under hips to raise angle and reduce strain",
                    "Drop to forearms for a more relaxed variation",
                    "Arch or flatten your back to change sensation",
                    "You control depth by shifting hips forward or back"
                )
            ),
            urWoman = PartnerRole(
                position = "ہاتھ گھٹنوں پر (یا پیٹ کے بل)، پیچھے سے",
                guidance = listOf(
                    "کولہے کے نیچے مضبوط تکیہ رکھیں",
                    "آرام کے لیے بازوؤں پر جھکیں",
                    "کمر آرچ یا سیدھی کر کے احساس بدلیں",
                    "کولہے آگے پیچھے ہلاکر گہرائی کنٹرول کریں"
                )
            )
        ),
        "lotus" to BilingualRoles(
            enMan = PartnerRole(
                position = "Seated with legs extended or cross-legged, supporting her weight",
                guidance = listOf(
                    "Sit against a headboard or wall for back support",
                    "Hold her waist firmly to help her balance on your lap",
                    "Move together with small rocking motions — not deep thrusting",
                    "Breathe in sync — this position is meditative and slow"
                )
            ),
            urMan = PartnerRole(
                position = "بیٹھا، ٹانگیں پھیلی یا پیر باندھے، اس کا وزن سہارا",
                guidance = listOf(
                    "سرے یا دیوار سے ٹیک لگائیں کمر کے لیے",
                    "کمر مضبوطی سے پکڑیں توازن کے لیے",
                    "چھوٹی ہلکی حرکتیں — گہری جھٹکیں نہیں",
                    "ہم آہنگ سانس — یہ پوزیشن آہستہ اور باخبر ہے"
                )
            ),
            enWoman = PartnerRole(
                position = "Sitting on his lap, facing him, legs wrapped around his waist",
                guidance = listOf(
                    "Wrap legs securely around his waist for stability",
                    "Use cushions under your hips if flexibility is limited",
                    "Rock your hips slowly — you both move as one unit",
                    "Keep arms around his neck or shoulders for balance"
                )
            ),
            urWoman = PartnerRole(
                position = "اس کی گود میں آمنے سامنے، ٹانگیں کمر کے گرد",
                guidance = listOf(
                    "ٹانگیں مضبوطی سے کمر کے گرد لپیٹیں",
                    "لچک کم ہو تو کولہے کے نیچے گدوے استعمال کریں",
                    "کولہے آہستہ ہلائیں — دونوں ایک اکائی کی طرح",
                    "توازن کے لیے گردن یا کندھوں کے گرد باہیں"
                )
            )
        ),
        "standing" to BilingualRoles(
            enMan = PartnerRole(
                position = "Standing, supporting her full weight against a wall",
                guidance = listOf(
                    "Stand with back firmly against a sturdy wall",
                    "Support her thighs with both hands — never let go suddenly",
                    "Keep movements small and controlled — balance is critical",
                    "Communicate before lifting or lowering her"
                )
            ),
            urMan = PartnerRole(
                position = "کھڑا، دیوار سے سہارا دے کر اس کا پورا وزن اٹھائے",
                guidance = listOf(
                    "مضبوط دیوار سے ٹیک لگا کر کھڑے ہوں",
                    "دونوں ہاتھوں سے رانیں سہاریں — اچانک نہ چھوڑیں",
                    "حرکت چھوٹی اور کنٹرول میں رکھیں",
                    "اٹھانے یا نیچے لانے سے پہلے بتائیں"
                )
            ),
            enWoman = PartnerRole(
                position = "Lifted against the wall, legs wrapped around his waist",
                guidance = listOf(
                    "Wrap legs tightly around his waist and grip his shoulders",
                    "Press back against the wall for stability",
                    "Keep core engaged to help maintain balance",
                    "If too strenuous, try one foot on a chair instead"
                )
            ),
            urWoman = PartnerRole(
                position = "دیوار سے لگی، ٹانگیں اس کی کمر کے گرد",
                guidance = listOf(
                    "ٹانگیں مضبوطی سے کمر کے گرد، کندھے پکڑیں",
                    "دیوار سے پیچھے دباؤ سے توازن",
                    "کور پٹھے استعمال کریں توازن کے لیے",
                    "بہت مشکل ہو تو ایک پاؤں کرسی پر رکھیں"
                )
            )
        ),
        "edge_of_bed" to BilingualRoles(
            enMan = PartnerRole(
                position = "Standing between her legs at the bed edge",
                guidance = listOf(
                    "Adjust bed height — her hips should be level with yours",
                    "Hold her thighs or hips for stability and connection",
                    "Standing gives you leverage — use it gently",
                    "Great position when she has limited mobility"
                )
            ),
            urMan = PartnerRole(
                position = "بستر کے کنارے اس کی ٹانگوں کے درمیان کھڑا",
                guidance = listOf(
                    "بستر کی اونچائی ایڈجسٹ کریں — کولہے آپ کے برابر",
                    "رانیں یا کولہے پکڑیں استحکام اور تعلق کے لیے",
                    "کھڑے ہونے سے فائدہ — نرمی سے استعمال کریں",
                    "جب اس کی حرکت محدود ہو تو بہترین"
                )
            ),
            enWoman = PartnerRole(
                position = "Sitting or lying at the very edge of the bed, legs open",
                guidance = listOf(
                    "Scoot to the bed edge so hips are at the perfect height",
                    "Rest calves on his shoulders or keep feet on the floor",
                    "Grip the bed edge for stability",
                    "Adjust leg position — bent, straight, or over shoulders"
                )
            ),
            urWoman = PartnerRole(
                position = "بستر کے بالکل کنارے، ٹانگیں کھولے",
                guidance = listOf(
                    "کنارے تک بیٹھیں یا لیٹیں تاکہ کولہے درست اونچائی پر",
                    "پنڈلیاں اس کے کندھوں پر یا پاؤں فرش پر",
                    "استحکام کے لیے بستر کا کنارہ پکڑیں",
                    "ٹانگیں موڑی، سیدھی یا کندھوں پر رکھ کر آزمائیں"
                )
            )
        ),
        "reverse_cowgirl" to BilingualRoles(
            enMan = PartnerRole(
                position = "Lying on his back, viewing her from behind",
                guidance = listOf(
                    "Enjoy the visual but communicate about depth — you have less control",
                    "Place hands on her hips to guide pace if needed",
                    "Tell her clearly if angle or depth needs adjustment",
                    "Resist the urge to thrust upward aggressively"
                )
            ),
            urMan = PartnerRole(
                position = "پیٹ کے بل، پیچھے سے دیکھتے ہوئے",
                guidance = listOf(
                    "لطف اندوز ہوں لیکن گہرائی کے بارے میں بتائیں",
                    "ضرورت ہو تو کولہے پر ہاتھ سے رفتار رہنمائی کریں",
                    "زاویہ یا گہرائی ایڈجسٹ چاہیے تو واضح بتائیں",
                    "اوپر زبردستی جھٹکنے سے بچیں"
                )
            ),
            enWoman = PartnerRole(
                position = "Straddling him facing away, full control of movement",
                guidance = listOf(
                    "Face toward his feet — lean forward on his thighs for balance",
                    "Control depth carefully since he cannot see your face easily",
                    "Try gentle hip circles or rocking for varied sensation",
                    "Turn to check his comfort if you're unsure"
                )
            ),
            urWoman = PartnerRole(
                position = "پیٹھ کر کے اوپر، مکمل حرکت کنٹرول",
                guidance = listOf(
                    "پاؤں کی طرف منہ — توازن کے لیے رانوں پر جھکیں",
                    "گہرائی احتیاط سے کنٹرول کریں — وہ آپ کا چہرہ نہیں دیکھ سکتا",
                    "کولہے گول گھمائیں یا ہلائیں تنوع کے لیے",
                    "یقین نہ ہو تو مڑ کر اس کا آرام پوچھیں"
                )
            )
        ),
        "butterfly" to BilingualRoles(
            enMan = PartnerRole(
                position = "Standing or kneeling at the bed edge, facing her elevated hips",
                guidance = listOf(
                    "Her elevated hips give you a direct angle — start gently",
                    "Hold her legs or ankles if she places them on your shoulders",
                    "This angle can be intense — check in frequently",
                    "Kneeling is easier on your knees than standing for longer sessions"
                )
            ),
            urMan = PartnerRole(
                position = "بستر کے کنارے کھڑا یا گھٹنوں پر، اونچے کولہوں کے سامنے",
                guidance = listOf(
                    "اونچے کولہے براہ راست زاویہ دیتے ہیں — نرمی سے شروع کریں",
                    "ٹانگیں کندھوں پر ہوں تو پکڑ سکتے ہیں",
                    "یہ زاویہ شدید ہو سکتا ہے — بار بار پوچھیں",
                    "لمبے سیشن کے لیے گھٹنوں پر بیٹھنا آسان"
                )
            ),
            enWoman = PartnerRole(
                position = "Lying on back with hips raised on a pillow, legs open wide",
                guidance = listOf(
                    "Use a wedge or firm pillow under hips for stable elevation",
                    "Pull knees toward chest or rest legs on his shoulders",
                    "Hold your own legs if needed for comfort",
                    "This position offers excellent G-spot access depending on anatomy"
                )
            ),
            urWoman = PartnerRole(
                position = "پیٹھ کے بل تکیے پر اونچے کولہے، ٹانگیں کھولے",
                guidance = listOf(
                    "مثلثی یا مضبوط تکیہ کولہے کے نیچے رکھیں",
                    "گھٹنے سینے کی طرف کھینچیں یا ٹانگیں کندھوں پر",
                    "آرام کے لیے اپنی ٹانگیں خود پکڑ سکتی ہیں",
                    "جسم کی ساخت کے مطابق بہترین زاویہ"
                )
            )
        ),
        "scissors" to BilingualRoles(
            enMan = PartnerRole(
                position = "Lying on his side at an angle, legs scissored with hers",
                guidance = listOf(
                    "Align your top thigh against her hip for contact",
                    "Use hip grinding rather than deep thrusting",
                    "This position favors mutual stimulation over penetration depth",
                    "Adjust the angle of your bodies until contact feels natural"
                )
            ),
            urMan = PartnerRole(
                position = "ترچھے سیدھے، ٹانگیں قینچی کی طرح",
                guidance = listOf(
                    "اوپر والی ران اس کے کولہے سے ملائیں",
                    "گہری جھٹکوں کی بجائے کولہے رگڑیں",
                    "یہ پوزیشن گہرائی سے زیادہ باہمی محرک کے لیے ہے",
                    "جسم کا زاویہ ایڈجسٹ کریں جب رابطہ قدرتی لگے"
                )
            ),
            enWoman = PartnerRole(
                position = "Lying on her side at an angle, legs intertwined with his",
                guidance = listOf(
                    "Place top leg over his hip and press close",
                    "Use your hand between bodies for added clitoral stimulation",
                    "Rock hips together in a slow grinding motion",
                    "Excellent for intimacy when deep penetration is uncomfortable"
                )
            ),
            urWoman = PartnerRole(
                position = "ترچھے سیدھے، ٹانگیں اس کے ساتھ ملی",
                guidance = listOf(
                    "اوپر والی ٹانگ اس کی ران پر رکھیں اور قریب دبائیں",
                    "جسموں کے درمیان ہاتھ سے اضافی محرک دیں",
                    "کولہے آہستہ رگڑ کر ہم آہنگ حرکت کریں",
                    "گہری داخلہ تکلیف دہ ہو تو قربت کے لیے بہترین"
                )
            )
        ),
        "lazy_dog" to BilingualRoles(
            enMan = PartnerRole(
                position = "Lying on top of her or positioned behind, minimal thrusting",
                guidance = listOf(
                    "Distribute your weight on forearms — don't press on her back",
                    "Use slow grinding motions instead of vigorous thrusting",
                    "Perfect when energy is low — intimacy without athletic effort",
                    "Whisper, kiss her neck, and keep movements languid"
                )
            ),
            urMan = PartnerRole(
                position = "اوپر یا پیچھے، کم جھٹکوں کے ساتھ",
                guidance = listOf(
                    "وزن بازوؤں پر رکھیں — کمر پر دباؤ نہ ڈالیں",
                    "تیز جھٹکوں کی بجائے آہستہ رگڑ",
                    "تھکاوٹ میں بہترین — کم محنت والی قربت",
                    "آہستہ باتیں، گردن پر بوسہ، سست حرکت"
                )
            ),
            enWoman = PartnerRole(
                position = "Lying flat on stomach with pillow under hips",
                guidance = listOf(
                    "Place a soft pillow under hips to raise angle comfortably",
                    "Keep legs slightly apart or together — try both",
                    "Relax completely — this is a restful, low-effort position",
                    "Reach back to guide his hips if you want more or less pressure"
                )
            ),
            urWoman = PartnerRole(
                position = "پیٹ کے بل لیٹے، کولہے کے نیچے تکیہ",
                guidance = listOf(
                    "کولہے کے نیچے نرم تکیہ آرام دہ زاویے کے لیے",
                    "ٹانگیں ہلکی فاصلے پر یا ساتھ — دونوں آزمائیں",
                    "مکمل آرام — یہ سست، کم محنت والی پوزیشن ہے",
                    "دباؤ زیادہ یا کم چاہیے تو پیچھے ہاتھ بڑھائیں"
                )
            )
        ),
        "cat" to BilingualRoles(
            enMan = PartnerRole(
                position = "On top with weight shifted forward, not thrusting",
                guidance = listOf(
                    "Shift your body higher so contact presses along her vulva, not deep inside",
                    "Move hips in slow circles — avoid in-and-out thrusting entirely",
                    "Keep forearms supporting your weight to stay comfortable",
                    "Watch her face and adjust angle when she guides you"
                )
            ),
            urMan = PartnerRole(
                position = "اوپر، وزن آگے، بغیر جھٹکوں کے",
                guidance = listOf(
                    "جسم اونچا رکھیں تاکہ رابطہ اس کے محرک پر ہو، گہرے اندر نہیں",
                    "کولہے آہستہ گول گھمائیں — اندر باہر جھٹکوں سے بچیں",
                    "بازوؤں سے وزن سہاریں آرام کے لیے",
                    "اس کا چہرہ دیکھیں اور رہنمائی پر زاویہ بدلیں"
                )
            ),
            enWoman = PartnerRole(
                position = "Lying on back, tilting hips to find the best contact angle",
                guidance = listOf(
                    "Tilt hips at different angles to discover what feels best",
                    "Wrap legs around his back to pull him closer",
                    "Guide his hips with your hands to show preferred pressure",
                    "Focus on the grinding sensation — communicate what angle works"
                )
            ),
            urWoman = PartnerRole(
                position = "پیٹ کے بل، کولہے جھکا کر بہترین زاویہ تلاش",
                guidance = listOf(
                    "کولہے مختلف زاویوں پر جھکائیں کیا بہتر لگے تلاش کریں",
                    "ٹانگیں اس کی پیٹھ کے گرد لپیٹیں قریب کھینچنے کے لیے",
                    "ہاتھوں سے کولہے رہنمائی کریں پسندیدہ دباؤ دکھائیں",
                    "رگڑ کے احساس پر توجہ دیں — کون سا زاویہ کام کرتا ہے بتائیں"
                )
            )
        ),
        "rocking_horse" to BilingualRoles(
            enMan = PartnerRole(
                position = "Seated with legs extended, supporting her on his lap",
                guidance = listOf(
                    "Sit against a headboard or wall for back support",
                    "Hold her waist and rock together in sync",
                    "Let her set the depth by how she positions on your lap",
                    "Keep movements slow and rhythmic — this is about connection"
                )
            ),
            urMan = PartnerRole(
                position = "بیٹھا، ٹانگیں پھیلی، گود میں سہارا",
                guidance = listOf(
                    "سرے یا دیوار سے ٹیک لگائیں",
                    "کمر پکڑیں اور ساتھ جھولیں",
                    "گود پر بیٹھنے کے انداز سے وہ گہرائی طے کرے",
                    "حرکت آہستہ اور تال میں رکھیں — تعلق اہم ہے"
                )
            ),
            enWoman = PartnerRole(
                position = "Sitting on his lap between his legs, facing him",
                guidance = listOf(
                    "Sit close and wrap legs partially around him",
                    "Rock your hips forward and back to control depth",
                    "Maintain eye contact — this position thrives on closeness",
                    "Use your arms around his neck for balance and intimacy"
                )
            ),
            urWoman = PartnerRole(
                position = "اس کی گود میں آمنے سامنے، ٹانگوں کے درمیان",
                guidance = listOf(
                    "قریب بیٹھیں اور ٹانگیں جزوی طور پر لپیٹیں",
                    "کولہے آگے پیچھے جھولیں گہرائی کنٹرول کرنے کے لیے",
                    "آنکھوں کا رابطہ رکھیں — یہ پوزیشن قربت پر ہے",
                    "گردن کے گرد باہیں توازن اور قربت کے لیے"
                )
            )
        ),
        "seated_scissors" to BilingualRoles(
            enMan = PartnerRole(
                position = "Lying on back with one knee bent, relaxed",
                guidance = listOf(
                    "Keep one leg bent for her to straddle — the other extended",
                    "Relax and enjoy — she controls pace and movement",
                    "Place hands on her hips or thighs if she wants guidance",
                    "Communicate about depth since you have limited visual feedback"
                )
            ),
            urMan = PartnerRole(
                position = "پیٹ کے بل ایک گھٹنا موڑے، آرام سے",
                guidance = listOf(
                    "ایک ٹانگ موڑی رکھیں تاکہ وہ اس پر بیٹھے",
                    "آرام کریں — وہ رفتار اور حرکت کنٹرول کرے",
                    "ضرورت ہو تو کولہے یا رانوں پر ہاتھ رکھیں",
                    "گہرائی کے بارے میں بتائیں — نظر محدود ہے"
                )
            ),
            enWoman = PartnerRole(
                position = "Straddling his bent leg, facing toward his feet",
                guidance = listOf(
                    "Straddle the bent leg and arrange your other leg comfortably",
                    "Bounce, grind, or rock — you have full control up top",
                    "Use his thighs for balance and leverage",
                    "Try alternating pace to find what feels best for both"
                )
            ),
            urWoman = PartnerRole(
                position = "موڑی ٹانگ پر بیٹھی، پاؤں کی طرف",
                guidance = listOf(
                    "موڑی ٹانگ پر بیٹھیں اور دوسری ٹانگ آرام سے رکھیں",
                    "اچھلیں، رگڑیں یا جھولیں — اوپر مکمل کنٹرول",
                    "توازن کے لیے اس کی رانیں استعمال کریں",
                    "رفتار بدل کر دونوں کے لیے بہترین تلاش کریں"
                )
            )
        ),
        "countertop" to BilingualRoles(
            enMan = PartnerRole(
                position = "Standing between her legs at hip-height surface",
                guidance = listOf(
                    "Ensure the surface is sturdy before she leans back",
                    "Stand at a height where hips align naturally",
                    "Use free hands for her breasts, clitoris, or hair",
                    "Adjust your stance — wider legs give better stability"
                )
            ),
            urMan = PartnerRole(
                position = "کولہے کی اونچائی کی سطح پر اس کی ٹانگوں کے درمیان کھڑا",
                guidance = listOf(
                    "اس کے جھکنے سے پہلے سطح مضبوط یقینی بنائیں",
                    "ایسی اونچائی کھڑے ہوں جہاں کولہے قدرتی ملیں",
                    "آزاد ہاتھوں سے سینے، محرک یا بال چھوئیں",
                    "پاؤں چوڑے رکھیں بہتر توازن کے لیے"
                )
            ),
            enWoman = PartnerRole(
                position = "Sitting or lying back on edge of sturdy surface",
                guidance = listOf(
                    "Scoot to the edge so hips are at the perfect height",
                    "Lean back on hands or elbows for support",
                    "Wrap legs around his waist or rest feet on his hips",
                    "Let him know if the surface height needs adjustment"
                )
            ),
            urWoman = PartnerRole(
                position = "مضبوط سطح کے کنارے بیٹھی یا پیٹھ کے بل",
                guidance = listOf(
                    "کنارے تک بیٹھیں تاکہ کولہے درست اونچائی پر ہوں",
                    "ہاتھوں یا کہنیوں پر ٹیک لگائیں",
                    "ٹانگیں اس کی کمر کے گرد لپیٹیں یا پاؤں اس کے کولہوں پر",
                    "اونچائی ایڈجسٹ چاہیے ہو تو بتائیں"
                )
            )
        ),
        "lap_dance" to BilingualRoles(
            enMan = PartnerRole(
                position = "Seated in chair, supporting her on his lap",
                guidance = listOf(
                    "Sit firmly with feet flat on floor for stability",
                    "Hold her hips or waist to guide rhythm if asked",
                    "Enjoy eye contact — let her lead the movement",
                    "Communicate if depth or angle needs adjustment"
                )
            ),
            urMan = PartnerRole(
                position = "کرسی میں بیٹھا، گود میں سہارا",
                guidance = listOf(
                    "پاؤں فرش پر مضبوطی سے بیٹھیں",
                    "کہے تو کولہے یا کمر پکڑ کر تال رہنمائی کریں",
                    "آنکھوں کا رابطہ — اسے حرکت کی قیادت دیں",
                    "گہرائی یا زاویہ ایڈجسٹ چاہیے ہو تو بتائیں"
                )
            ),
            enWoman = PartnerRole(
                position = "Straddling his lap, controlling all movement",
                guidance = listOf(
                    "Plant feet on floor for leverage to bounce and grind",
                    "Face him for intimacy or turn away for a new angle",
                    "Rotate hips in circles for varied sensation",
                    "You set the pace entirely — go as slow or fast as you like"
                )
            ),
            urWoman = PartnerRole(
                position = "گود میں بیٹھی، تمام حرکت کنٹرول",
                guidance = listOf(
                    "فرش پر پاؤں رکھیں اچھلنے اور رگڑنے کے لیے",
                    "قربت کے لیے آمنے سامنے یا نئے زاویے کے لیے پیٹھ کر",
                    "کولہے گول گھمائیں مختلف احساس کے لیے",
                    "رفتار مکمل آپ طے کریں — جتنی آہستہ یا تیز چاہیں"
                )
            )
        ),
        "layer_cake" to BilingualRoles(
            enMan = PartnerRole(
                position = "Lying flat on top of her, facing her, grinding together",
                guidance = listOf(
                    "Distribute weight on forearms — don't crush her",
                    "Align hips so genitals press together naturally",
                    "Rock and grind at a shared rhythm — no thrusting",
                    "Kiss and maintain eye contact throughout"
                )
            ),
            urMan = PartnerRole(
                position = "اوپر آمنے سامنے سیدھا، ساتھ رگڑ",
                guidance = listOf(
                    "وزن بازوؤں پر رکھیں — دباؤ نہ ڈالیں",
                    "کولہے ملائیں تاکہ محرک قدرتی رابطے میں آئیں",
                    "مشترکہ تال پر رگڑیں — جھٹکوں سے بچیں",
                    "بوسہ دیں اور آنکھوں کا رابطہ رکھیں"
                )
            ),
            enWoman = PartnerRole(
                position = "Lying on back with partner flat on top",
                guidance = listOf(
                    "Relax and let your bodies press together fully",
                    "Rock hips upward to meet his grinding motion",
                    "Use lubricant if friction feels too intense",
                    "Guide his rhythm with your hands on his hips or back"
                )
            ),
            urWoman = PartnerRole(
                position = "پیٹ کے بل، ساتھی اوپر سیدھا",
                guidance = listOf(
                    "آرام کریں اور جسم مکمل ملنے دیں",
                    "کولہے اوپر اٹھائیں اس کی رگڑ سے ملنے کے لیے",
                    "رگڑ زیادہ شدید لگے تو لوبریکنٹ استعمال کریں",
                    "کولہے یا پیٹھ پر ہاتھ سے تال رہنمائی کریں"
                )
            )
        ),
        "reverse_slither" to BilingualRoles(
            enMan = PartnerRole(
                position = "Lying on top of her, entering from behind, full body contact",
                guidance = listOf(
                    "Keep weight on forearms — chest against her back",
                    "Use slow grinding rather than deep thrusting",
                    "Whisper in her ear and kiss her neck",
                    "Reach around for clitoral or breast stimulation"
                )
            ),
            urMan = PartnerRole(
                position = "اوپر پیچھے سے، مکمل جسم رابطہ",
                guidance = listOf(
                    "وزن بازوؤں پر — سینہ اس کی پیٹھ سے ملے",
                    "گہری جھٹکوں کی بجائے آہستہ رگڑ",
                    "کان میں آہستہ باتیں، گردن پر بوسہ",
                    "ہاتھ بڑھا کر محرک یا سینے کو چھوئیں"
                )
            ),
            enWoman = PartnerRole(
                position = "Lying flat on stomach with partner on top",
                guidance = listOf(
                    "Place a pillow under hips for comfortable angle",
                    "Relax your body — let him provide the movement",
                    "Slip a hand underneath for self-stimulation if desired",
                    "Press back into him to control depth and pressure"
                )
            ),
            urWoman = PartnerRole(
                position = "پیٹ کے بل، ساتھی اوپر",
                guidance = listOf(
                    "کولہے کے نیچے تکیہ آرام دہ زاویے کے لیے",
                    "جسم ڈھیلا رکھیں — حرکت اسے دینے دیں",
                    "چاہیں تو ہاتھ نیچے بڑھا کر خود محرک دیں",
                    "پیچھے دباؤ سے گہرائی اور دباؤ کنٹرول کریں"
                )
            )
        ),
        "yab_yum" to BilingualRoles(
            enMan = PartnerRole(
                position = "Seated cross-legged, supporting her in his lap",
                guidance = listOf(
                    "Sit on cushions for comfort on hard surfaces",
                    "Hold her close and rock side-to-side slowly",
                    "Breathe in sync — exhale when she exhales",
                    "Maintain soft eye contact without forcing intensity"
                )
            ),
            urMan = PartnerRole(
                position = "پیر باندھ کر بیٹھا، گود میں سہارا",
                guidance = listOf(
                    "سخت سطح پر گدوے استعمال کریں",
                    "قریب پکڑیں اور آہستہ آگے پیچھے جھولیں",
                    "سانسیں ہم آہنگ — جب وہ چھوڑے آپ بھی چھوڑیں",
                    "نرم آنکھوں کا رابطہ — زبردستی شدت نہ ڈالیں"
                )
            ),
            enWoman = PartnerRole(
                position = "Sitting in his lap, legs wrapped around his waist",
                guidance = listOf(
                    "Wrap legs securely and press your chest to his",
                    "Rock together as one unit — small movements only",
                    "Try eye-gazing for two to three minutes to deepen bond",
                    "Let go of performance goals — feel present together"
                )
            ),
            urWoman = PartnerRole(
                position = "گود میں، ٹانگیں کمر کے گرد",
                guidance = listOf(
                    "ٹانگیں مضبوط لپیٹیں اور سینہ اس سے ملائیں",
                    "ایک اکائی کی طرح جھولیں — صرف چھوٹی حرکتیں",
                    "دو تین منٹ آنکھوں میں دیکھیں تعلق گہرا کرنے کے لیے",
                    "کارکردگی کا مقصد چھوڑیں — ساتھ موجود محسوس کریں"
                )
            )
        )
    )
}
