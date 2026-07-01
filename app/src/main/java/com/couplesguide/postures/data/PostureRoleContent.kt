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
        "bicycle" to BilingualRoles(
            enMan = PartnerRole(
                position = "At bed edge holding partner's ankles",
                guidance = listOf(
                    "Guide leg movement gently",
                    "Keep communication open",
                    "Adjust pace together",
                    "Support partner's lower back if needed"
                )
            ),
            urMan = PartnerRole(
                position = "بستر کے کنارے ساتھی کے ٹخنوں کو پکڑے",
                guidance = listOf(
                    "ٹانگوں کی حرکت آہستہ رہنمائی کریں",
                    "بات چیت جاری رکھیں",
                    "رفتار ساتھ مل کر",
                    "ضرورت ہو تو کمر سہارا دیں"
                )
            ),
            enWoman = PartnerRole(
                position = "Lying back with legs lifted in cycling motion",
                guidance = listOf(
                    "Hold bed edge for stability",
                    "Bend knees comfortably toward chest",
                    "Tell partner your preferred pace",
                    "Relax shoulders and breathe"
                )
            ),
            urWoman = PartnerRole(
                position = "پیٹھ کے بل ٹانگیں سائیکلنگ انداز میں اٹھائے",
                guidance = listOf(
                    "استحکام کے لیے بستر پکڑیں",
                    "گھٹنے آرام سے سینے کی طرف",
                    "پسندیدہ رفتار بتائیں",
                    "کندھے ڈھیلے، سانس لیں"
                )
            )
        ),
        "face_to_face" to BilingualRoles(
            enMan = PartnerRole(
                position = "Seated with partner on lap facing you",
                guidance = listOf(
                    "Wrap arms around her back",
                    "Rock together slowly",
                    "Maintain eye contact",
                    "Let her set depth on your lap"
                )
            ),
            urMan = PartnerRole(
                position = "بیٹھے، ساتھی گود میں آمنے سامنے",
                guidance = listOf(
                    "کمر کے گرد باہیں لپیٹیں",
                    "آہستہ ساتھ ہلیں",
                    "آنکھوں سے رابطہ",
                    "گود میں گہرائی وہ طے کرے"
                )
            ),
            enWoman = PartnerRole(
                position = "Sitting on his lap, facing him",
                guidance = listOf(
                    "Wrap arms around his neck or shoulders",
                    "Rock hips to find rhythm",
                    "Kiss and stay connected",
                    "Control movement from on top"
                )
            ),
            urWoman = PartnerRole(
                position = "اس کی گود میں آمنے سامنے",
                guidance = listOf(
                    "گردن یا کندھوں کے گرد باہیں",
                    "کولہے ہلائیں تال تلاش کرنے کے لیے",
                    "بوسہ اور قربت",
                    "اوپر سے حرکت کنٹرول کریں"
                )
            )
        ),
        "the_plug" to BilingualRoles(
            enMan = PartnerRole(
                position = "Behind partner in rear-entry position",
                guidance = listOf(
                    "Start slow and shallow",
                    "Grip hips gently",
                    "Check in about depth",
                    "Adjust angle with knee position"
                )
            ),
            urMan = PartnerRole(
                position = "پیچھے سے داخلہ",
                guidance = listOf(
                    "آہستہ ہلکی شروعات",
                    "کولہے نرمی سے پکڑیں",
                    "گہرائی پوچھتے رہیں",
                    "گھٹنوں سے زاویہ بدلیں"
                )
            ),
            enWoman = PartnerRole(
                position = "On hands and knees or forward-leaning",
                guidance = listOf(
                    "Use pillow under hips",
                    "Arch or flatten back to adjust",
                    "Control depth by shifting hips",
                    "Speak up about comfort"
                )
            ),
            urWoman = PartnerRole(
                position = "ہاتھ گھٹنوں پر یا آگے جھکی",
                guidance = listOf(
                    "کولہے کے نیچے تکیہ",
                    "کمر آرچ یا سیدھی کریں",
                    "کولہے ہلاکر گہرائی کنٹرول",
                    "آرام کے بارے میں بتائیں"
                )
            )
        ),
        "lying_dog" to BilingualRoles(
            enMan = PartnerRole(
                position = "Lying on top or behind, slow grinding",
                guidance = listOf(
                    "Keep weight on forearms",
                    "Grind slowly instead of thrusting",
                    "Whisper and stay connected",
                    "Perfect for low-energy nights"
                )
            ),
            urMan = PartnerRole(
                position = "اوپر یا پیچھے، آہستہ رگڑ",
                guidance = listOf(
                    "وزن بازوؤں پر",
                    "جھٹکوں کی بجائے رگڑ",
                    "آہستہ باتیں کریں",
                    "تھکاوٹ میں بہترین"
                )
            ),
            enWoman = PartnerRole(
                position = "Flat on stomach with pillow under hips",
                guidance = listOf(
                    "Relax completely",
                    "Pillow raises angle comfortably",
                    "Reach back to guide hips",
                    "Minimal effort needed"
                )
            ),
            urWoman = PartnerRole(
                position = "پیٹ کے بل تکیے کے ساتھ",
                guidance = listOf(
                    "مکمل آرام",
                    "تکیہ زاویہ بہتر بناتا ہے",
                    "ہاتھ پیچھے رہنمائی کے لیے",
                    "کم محنت"
                )
            )
        ),
        "spooning" to BilingualRoles(
            enMan = PartnerRole(
                position = "Behind her, curled close from the rear",
                guidance = listOf(
                    "Wrap arm around waist",
                    "Keep movements slow",
                    "Kiss neck and shoulder",
                    "Bend top knee for angle"
                )
            ),
            urMan = PartnerRole(
                position = "پیچھے قریب لپٹا",
                guidance = listOf(
                    "کمر کے گرد بازو",
                    "آہستہ حرکت",
                    "گردن پر بوسہ",
                    "زاویے کے لیے گھٹنا موڑیں"
                )
            ),
            enWoman = PartnerRole(
                position = "Lying on side in front",
                guidance = listOf(
                    "Pillow between knees",
                    "Reach back to guide",
                    "Press back for depth control",
                    "Low effort and cozy"
                )
            ),
            urWoman = PartnerRole(
                position = "سامنے سیدھے لیٹے",
                guidance = listOf(
                    "گھٹنوں کے درمیان تکیہ",
                    "پیچھے ہاتھ رہنمائی",
                    "پیچھے دباؤ سے گہرائی",
                    "آرام دہ"
                )
            )
        ),
        "bridge_69" to BilingualRoles(
            enMan = PartnerRole(
                position = "Active partner — communicate and adjust together",
                guidance = listOf(
                    "Start slowly",
                    "Check in frequently",
                    "Adjust angle as needed",
                    "Respond to partner's feedback"
                )
            ),
            urMan = PartnerRole(
                position = "فعال ساتھی — بات چیت اور ایڈجسٹمنٹ",
                guidance = listOf(
                    "آہستہ شروع کریں",
                    "بار بار پوچھیں",
                    "زاویہ بدلیں",
                    "ساتھی کے ردعمل پر توجہ"
                )
            ),
            enWoman = PartnerRole(
                position = "Receiving partner — relax and guide your partner",
                guidance = listOf(
                    "Speak up about comfort",
                    "Use pillows for support",
                    "Guide with hands or words",
                    "Breathe and stay present"
                )
            ),
            urWoman = PartnerRole(
                position = "وصول کنندہ — آرام کریں اور رہنمائی کریں",
                guidance = listOf(
                    "آرام کے بارے میں بتائیں",
                    "تکیے استعمال کریں",
                    "ہاتھ یا الفاظ سے رہنمائی",
                    "سانس لیں، موجود رہیں"
                )
            )
        ),
        "waterfall" to BilingualRoles(
            enMan = PartnerRole(
                position = "Active partner — communicate and adjust together",
                guidance = listOf(
                    "Start slowly",
                    "Check in frequently",
                    "Adjust angle as needed",
                    "Respond to partner's feedback"
                )
            ),
            urMan = PartnerRole(
                position = "فعال ساتھی — بات چیت اور ایڈجسٹمنٹ",
                guidance = listOf(
                    "آہستہ شروع کریں",
                    "بار بار پوچھیں",
                    "زاویہ بدلیں",
                    "ساتھی کے ردعمل پر توجہ"
                )
            ),
            enWoman = PartnerRole(
                position = "Receiving partner — relax and guide your partner",
                guidance = listOf(
                    "Speak up about comfort",
                    "Use pillows for support",
                    "Guide with hands or words",
                    "Breathe and stay present"
                )
            ),
            urWoman = PartnerRole(
                position = "وصول کنندہ — آرام کریں اور رہنمائی کریں",
                guidance = listOf(
                    "آرام کے بارے میں بتائیں",
                    "تکیے استعمال کریں",
                    "ہاتھ یا الفاظ سے رہنمائی",
                    "سانس لیں، موجود رہیں"
                )
            )
        ),
        "one_up" to BilingualRoles(
            enMan = PartnerRole(
                position = "Active partner — communicate and adjust together",
                guidance = listOf(
                    "Start slowly",
                    "Check in frequently",
                    "Adjust angle as needed",
                    "Respond to partner's feedback"
                )
            ),
            urMan = PartnerRole(
                position = "فعال ساتھی — بات چیت اور ایڈجسٹمنٹ",
                guidance = listOf(
                    "آہستہ شروع کریں",
                    "بار بار پوچھیں",
                    "زاویہ بدلیں",
                    "ساتھی کے ردعمل پر توجہ"
                )
            ),
            enWoman = PartnerRole(
                position = "Receiving partner — relax and guide your partner",
                guidance = listOf(
                    "Speak up about comfort",
                    "Use pillows for support",
                    "Guide with hands or words",
                    "Breathe and stay present"
                )
            ),
            urWoman = PartnerRole(
                position = "وصول کنندہ — آرام کریں اور رہنمائی کریں",
                guidance = listOf(
                    "آرام کے بارے میں بتائیں",
                    "تکیے استعمال کریں",
                    "ہاتھ یا الفاظ سے رہنمائی",
                    "سانس لیں، موجود رہیں"
                )
            )
        ),
        "cowgirl" to BilingualRoles(
            enMan = PartnerRole(
                position = "Lying on back, hands on her hips",
                guidance = listOf(
                    "Let her set pace",
                    "Lift hips to meet her",
                    "Communicate about depth",
                    "Enjoy the view and connection"
                )
            ),
            urMan = PartnerRole(
                position = "پیٹھ کے بل، کولہے پر ہاتھ",
                guidance = listOf(
                    "اسے رفتار طے کرنے دیں",
                    "ملنے کے لیے کولہے اٹھائیں",
                    "گہرائی کے بارے میں بات کریں",
                    "قربت سے لطف اٹھائیں"
                )
            ),
            enWoman = PartnerRole(
                position = "Straddling on top, facing him",
                guidance = listOf(
                    "Use thighs for balance",
                    "Rock or grind to find angle",
                    "Lean forward to kiss",
                    "You control depth entirely"
                )
            ),
            urWoman = PartnerRole(
                position = "اوپر آمنے سامنے",
                guidance = listOf(
                    "رانوں سے توازن",
                    "کولہے ہلائیں زاویہ تلاش کرنے کے لیے",
                    "بوسے کے لیے جھکیں",
                    "گہرائی آپ کنٹرول کریں"
                )
            )
        ),
        "hot_seat" to BilingualRoles(
            enMan = PartnerRole(
                position = "Seated, partner facing away on your lap",
                guidance = listOf(
                    "Guide forward-back movement",
                    "Support partner leaning back",
                    "Communicate about depth",
                    "Use chair arms for stability"
                )
            ),
            urMan = PartnerRole(
                position = "بیٹھے، ساتھی الٹ گود میں",
                guidance = listOf(
                    "آگے پیچھے رہنمائی",
                    "پیچھے جھکنے میں سہارا",
                    "گہرائی کے بارے میں بات",
                    "کرسی کے بازو استعمال کریں"
                )
            ),
            enWoman = PartnerRole(
                position = "Straddling facing away, leaning back",
                guidance = listOf(
                    "Lean back on his thighs",
                    "Control by rocking hips",
                    "Find G-spot angle",
                    "Brace on chair arms"
                )
            ),
            urWoman = PartnerRole(
                position = "الٹ اوپر پیچھے جھکے",
                guidance = listOf(
                    "رانوں پر جھکیں",
                    "کولہے ہلاکر کنٹرول",
                    "جی سپاٹ زاویہ تلاش کریں",
                    "بازوؤں پر سہارا"
                )
            )
        ),
        "pole_position" to BilingualRoles(
            enMan = PartnerRole(
                position = "Active partner — communicate and adjust together",
                guidance = listOf(
                    "Start slowly",
                    "Check in frequently",
                    "Adjust angle as needed",
                    "Respond to partner's feedback"
                )
            ),
            urMan = PartnerRole(
                position = "فعال ساتھی — بات چیت اور ایڈجسٹمنٹ",
                guidance = listOf(
                    "آہستہ شروع کریں",
                    "بار بار پوچھیں",
                    "زاویہ بدلیں",
                    "ساتھی کے ردعمل پر توجہ"
                )
            ),
            enWoman = PartnerRole(
                position = "Receiving partner — relax and guide your partner",
                guidance = listOf(
                    "Speak up about comfort",
                    "Use pillows for support",
                    "Guide with hands or words",
                    "Breathe and stay present"
                )
            ),
            urWoman = PartnerRole(
                position = "وصول کنندہ — آرام کریں اور رہنمائی کریں",
                guidance = listOf(
                    "آرام کے بارے میں بتائیں",
                    "تکیے استعمال کریں",
                    "ہاتھ یا الفاظ سے رہنمائی",
                    "سانس لیں، موجود رہیں"
                )
            )
        ),
        "david_copperfield" to BilingualRoles(
            enMan = PartnerRole(
                position = "Active partner — communicate and adjust together",
                guidance = listOf(
                    "Start slowly",
                    "Check in frequently",
                    "Adjust angle as needed",
                    "Respond to partner's feedback"
                )
            ),
            urMan = PartnerRole(
                position = "فعال ساتھی — بات چیت اور ایڈجسٹمنٹ",
                guidance = listOf(
                    "آہستہ شروع کریں",
                    "بار بار پوچھیں",
                    "زاویہ بدلیں",
                    "ساتھی کے ردعمل پر توجہ"
                )
            ),
            enWoman = PartnerRole(
                position = "Receiving partner — relax and guide your partner",
                guidance = listOf(
                    "Speak up about comfort",
                    "Use pillows for support",
                    "Guide with hands or words",
                    "Breathe and stay present"
                )
            ),
            urWoman = PartnerRole(
                position = "وصول کنندہ — آرام کریں اور رہنمائی کریں",
                guidance = listOf(
                    "آرام کے بارے میں بتائیں",
                    "تکیے استعمال کریں",
                    "ہاتھ یا الفاظ سے رہنمائی",
                    "سانس لیں، موجود رہیں"
                )
            )
        ),
        "the_throne" to BilingualRoles(
            enMan = PartnerRole(
                position = "Kneeling between partner's open legs",
                guidance = listOf(
                    "Maintain eye contact",
                    "Use varied tongue and finger techniques",
                    "Ask what feels good",
                    "Take breaks if jaw tires"
                )
            ),
            urMan = PartnerRole(
                position = "کھلے پاؤں کے درمیان گھٹنے ٹیکے",
                guidance = listOf(
                    "آنکھوں سے رابطہ",
                    "مختلف تکنیکیں",
                    "پوچھیں کیا اچھا لگے",
                    "تھکاوٹ ہو تو وقفہ"
                )
            ),
            enWoman = PartnerRole(
                position = "Seated in chair, legs apart",
                guidance = listOf(
                    "Relax into the chair",
                    "Guide with hands on head or shoulders",
                    "Communicate preferences clearly",
                    "Let go and enjoy"
                )
            ),
            urWoman = PartnerRole(
                position = "کرسی پر ٹانگیں پھیلا کر",
                guidance = listOf(
                    "کرسی میں آرام کریں",
                    "سر یا کندھے پر ہاتھ رہنمائی",
                    "پسند واضح بتائیں",
                    "لطف اٹھائیں"
                )
            )
        ),
        "the_pretzel" to BilingualRoles(
            enMan = PartnerRole(
                position = "Active partner — communicate and adjust together",
                guidance = listOf(
                    "Start slowly",
                    "Check in frequently",
                    "Adjust angle as needed",
                    "Respond to partner's feedback"
                )
            ),
            urMan = PartnerRole(
                position = "فعال ساتھی — بات چیت اور ایڈجسٹمنٹ",
                guidance = listOf(
                    "آہستہ شروع کریں",
                    "بار بار پوچھیں",
                    "زاویہ بدلیں",
                    "ساتھی کے ردعمل پر توجہ"
                )
            ),
            enWoman = PartnerRole(
                position = "Receiving partner — relax and guide your partner",
                guidance = listOf(
                    "Speak up about comfort",
                    "Use pillows for support",
                    "Guide with hands or words",
                    "Breathe and stay present"
                )
            ),
            urWoman = PartnerRole(
                position = "وصول کنندہ — آرام کریں اور رہنمائی کریں",
                guidance = listOf(
                    "آرام کے بارے میں بتائیں",
                    "تکیے استعمال کریں",
                    "ہاتھ یا الفاظ سے رہنمائی",
                    "سانس لیں، موجود رہیں"
                )
            )
        ),
        "the_shelf" to BilingualRoles(
            enMan = PartnerRole(
                position = "Standing or kneeling at bed edge between her legs",
                guidance = listOf(
                    "Hold hips firmly for stability",
                    "Adjust for clitoral contact",
                    "Match bed height to yours",
                    "Communicate about angle"
                )
            ),
            urMan = PartnerRole(
                position = "بستر کے کنارے درمیان میں",
                guidance = listOf(
                    "کولہے مضبوط پکڑیں",
                    "کلائیٹورل رابطے کے لیے زاویہ",
                    "بستر کی اونچائی ایڈجسٹ",
                    "زاویے کے بارے میں بات"
                )
            ),
            enWoman = PartnerRole(
                position = "Hips at bed edge, leaning on hands",
                guidance = listOf(
                    "Scoot to perfect edge height",
                    "Grip bed for stability",
                    "Guide his hips",
                    "Adjust leg position"
                )
            ),
            urWoman = PartnerRole(
                position = "کولہے بستر کے کنارے، ہاتھوں پر",
                guidance = listOf(
                    "درست اونچائی پر بیٹھیں",
                    "بستر پکڑیں",
                    "کولہے رہنمائی کریں",
                    "ٹانگیں ایڈجسٹ کریں"
                )
            )
        ),
        "butter" to BilingualRoles(
            enMan = PartnerRole(
                position = "Active partner — communicate and adjust together",
                guidance = listOf(
                    "Start slowly",
                    "Check in frequently",
                    "Adjust angle as needed",
                    "Respond to partner's feedback"
                )
            ),
            urMan = PartnerRole(
                position = "فعال ساتھی — بات چیت اور ایڈجسٹمنٹ",
                guidance = listOf(
                    "آہستہ شروع کریں",
                    "بار بار پوچھیں",
                    "زاویہ بدلیں",
                    "ساتھی کے ردعمل پر توجہ"
                )
            ),
            enWoman = PartnerRole(
                position = "Receiving partner — relax and guide your partner",
                guidance = listOf(
                    "Speak up about comfort",
                    "Use pillows for support",
                    "Guide with hands or words",
                    "Breathe and stay present"
                )
            ),
            urWoman = PartnerRole(
                position = "وصول کنندہ — آرام کریں اور رہنمائی کریں",
                guidance = listOf(
                    "آرام کے بارے میں بتائیں",
                    "تکیے استعمال کریں",
                    "ہاتھ یا الفاظ سے رہنمائی",
                    "سانس لیں، موجود رہیں"
                )
            )
        ),
        "wheelbarrow" to BilingualRoles(
            enMan = PartnerRole(
                position = "Standing behind, holding partner's hips/legs",
                guidance = listOf(
                    "Support weight carefully",
                    "Start with short holds",
                    "Build strength gradually",
                    "Have soft surface nearby"
                )
            ),
            urMan = PartnerRole(
                position = "پیچھے کھڑے کولہے پکڑے",
                guidance = listOf(
                    "وزن احتیاط سے",
                    "چھوٹے عرصے سے شروع",
                    "آہستہ طاقت بڑھائیں",
                    "نرم سطح قریب"
                )
            ),
            enWoman = PartnerRole(
                position = "Hands on floor, body angled down",
                guidance = listOf(
                    "Keep arms strong",
                    "Communicate if arms tire",
                    "Engage core for stability",
                    "Stop if uncomfortable"
                )
            ),
            urWoman = PartnerRole(
                position = "ہاتھ فرش پر جسم جھکا",
                guidance = listOf(
                    "بازو مضبوط رکھیں",
                    "تھکاوٹ ہو تو بتائیں",
                    "کور ٹائٹ",
                    "تکلیف ہو تو رکیں"
                )
            )
        ),
        "mountain_climber" to BilingualRoles(
            enMan = PartnerRole(
                position = "Active partner — communicate and adjust together",
                guidance = listOf(
                    "Start slowly",
                    "Check in frequently",
                    "Adjust angle as needed",
                    "Respond to partner's feedback"
                )
            ),
            urMan = PartnerRole(
                position = "فعال ساتھی — بات چیت اور ایڈجسٹمنٹ",
                guidance = listOf(
                    "آہستہ شروع کریں",
                    "بار بار پوچھیں",
                    "زاویہ بدلیں",
                    "ساتھی کے ردعمل پر توجہ"
                )
            ),
            enWoman = PartnerRole(
                position = "Receiving partner — relax and guide your partner",
                guidance = listOf(
                    "Speak up about comfort",
                    "Use pillows for support",
                    "Guide with hands or words",
                    "Breathe and stay present"
                )
            ),
            urWoman = PartnerRole(
                position = "وصول کنندہ — آرام کریں اور رہنمائی کریں",
                guidance = listOf(
                    "آرام کے بارے میں بتائیں",
                    "تکیے استعمال کریں",
                    "ہاتھ یا الفاظ سے رہنمائی",
                    "سانس لیں، موجود رہیں"
                )
            )
        ),
        "spork" to BilingualRoles(
            enMan = PartnerRole(
                position = "Active partner — communicate and adjust together",
                guidance = listOf(
                    "Start slowly",
                    "Check in frequently",
                    "Adjust angle as needed",
                    "Respond to partner's feedback"
                )
            ),
            urMan = PartnerRole(
                position = "فعال ساتھی — بات چیت اور ایڈجسٹمنٹ",
                guidance = listOf(
                    "آہستہ شروع کریں",
                    "بار بار پوچھیں",
                    "زاویہ بدلیں",
                    "ساتھی کے ردعمل پر توجہ"
                )
            ),
            enWoman = PartnerRole(
                position = "Receiving partner — relax and guide your partner",
                guidance = listOf(
                    "Speak up about comfort",
                    "Use pillows for support",
                    "Guide with hands or words",
                    "Breathe and stay present"
                )
            ),
            urWoman = PartnerRole(
                position = "وصول کنندہ — آرام کریں اور رہنمائی کریں",
                guidance = listOf(
                    "آرام کے بارے میں بتائیں",
                    "تکیے استعمال کریں",
                    "ہاتھ یا الفاظ سے رہنمائی",
                    "سانس لیں، موجود رہیں"
                )
            )
        ),
        "the_x" to BilingualRoles(
            enMan = PartnerRole(
                position = "Active partner — communicate and adjust together",
                guidance = listOf(
                    "Start slowly",
                    "Check in frequently",
                    "Adjust angle as needed",
                    "Respond to partner's feedback"
                )
            ),
            urMan = PartnerRole(
                position = "فعال ساتھی — بات چیت اور ایڈجسٹمنٹ",
                guidance = listOf(
                    "آہستہ شروع کریں",
                    "بار بار پوچھیں",
                    "زاویہ بدلیں",
                    "ساتھی کے ردعمل پر توجہ"
                )
            ),
            enWoman = PartnerRole(
                position = "Receiving partner — relax and guide your partner",
                guidance = listOf(
                    "Speak up about comfort",
                    "Use pillows for support",
                    "Guide with hands or words",
                    "Breathe and stay present"
                )
            ),
            urWoman = PartnerRole(
                position = "وصول کنندہ — آرام کریں اور رہنمائی کریں",
                guidance = listOf(
                    "آرام کے بارے میں بتائیں",
                    "تکیے استعمال کریں",
                    "ہاتھ یا الفاظ سے رہنمائی",
                    "سانس لیں، موجود رہیں"
                )
            )
        ),
        "angel_of_snows" to BilingualRoles(
            enMan = PartnerRole(
                position = "Active partner — communicate and adjust together",
                guidance = listOf(
                    "Start slowly",
                    "Check in frequently",
                    "Adjust angle as needed",
                    "Respond to partner's feedback"
                )
            ),
            urMan = PartnerRole(
                position = "فعال ساتھی — بات چیت اور ایڈجسٹمنٹ",
                guidance = listOf(
                    "آہستہ شروع کریں",
                    "بار بار پوچھیں",
                    "زاویہ بدلیں",
                    "ساتھی کے ردعمل پر توجہ"
                )
            ),
            enWoman = PartnerRole(
                position = "Receiving partner — relax and guide your partner",
                guidance = listOf(
                    "Speak up about comfort",
                    "Use pillows for support",
                    "Guide with hands or words",
                    "Breathe and stay present"
                )
            ),
            urWoman = PartnerRole(
                position = "وصول کنندہ — آرام کریں اور رہنمائی کریں",
                guidance = listOf(
                    "آرام کے بارے میں بتائیں",
                    "تکیے استعمال کریں",
                    "ہاتھ یا الفاظ سے رہنمائی",
                    "سانس لیں، موجود رہیں"
                )
            )
        ),
        "the_spider" to BilingualRoles(
            enMan = PartnerRole(
                position = "Active partner — communicate and adjust together",
                guidance = listOf(
                    "Start slowly",
                    "Check in frequently",
                    "Adjust angle as needed",
                    "Respond to partner's feedback"
                )
            ),
            urMan = PartnerRole(
                position = "فعال ساتھی — بات چیت اور ایڈجسٹمنٹ",
                guidance = listOf(
                    "آہستہ شروع کریں",
                    "بار بار پوچھیں",
                    "زاویہ بدلیں",
                    "ساتھی کے ردعمل پر توجہ"
                )
            ),
            enWoman = PartnerRole(
                position = "Receiving partner — relax and guide your partner",
                guidance = listOf(
                    "Speak up about comfort",
                    "Use pillows for support",
                    "Guide with hands or words",
                    "Breathe and stay present"
                )
            ),
            urWoman = PartnerRole(
                position = "وصول کنندہ — آرام کریں اور رہنمائی کریں",
                guidance = listOf(
                    "آرام کے بارے میں بتائیں",
                    "تکیے استعمال کریں",
                    "ہاتھ یا الفاظ سے رہنمائی",
                    "سانس لیں، موجود رہیں"
                )
            )
        ),
        "the_standard" to BilingualRoles(
            enMan = PartnerRole(
                position = "Kneeling between partner's open legs",
                guidance = listOf(
                    "Maintain eye contact",
                    "Use varied tongue and finger techniques",
                    "Ask what feels good",
                    "Take breaks if jaw tires"
                )
            ),
            urMan = PartnerRole(
                position = "کھلے پاؤں کے درمیان گھٹنے ٹیکے",
                guidance = listOf(
                    "آنکھوں سے رابطہ",
                    "مختلف تکنیکیں",
                    "پوچھیں کیا اچھا لگے",
                    "تھکاوٹ ہو تو وقفہ"
                )
            ),
            enWoman = PartnerRole(
                position = "Seated in chair, legs apart",
                guidance = listOf(
                    "Relax into the chair",
                    "Guide with hands on head or shoulders",
                    "Communicate preferences clearly",
                    "Let go and enjoy"
                )
            ),
            urWoman = PartnerRole(
                position = "کرسی پر ٹانگیں پھیلا کر",
                guidance = listOf(
                    "کرسی میں آرام کریں",
                    "سر یا کندھے پر ہاتھ رہنمائی",
                    "پسند واضح بتائیں",
                    "لطف اٹھائیں"
                )
            )
        )
    )
}
