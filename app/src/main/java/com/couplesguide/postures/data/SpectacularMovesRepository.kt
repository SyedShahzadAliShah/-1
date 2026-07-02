package com.couplesguide.postures.data

import com.couplesguide.postures.R

/**
 * 30 moves from "Spectacular Sex Moves She'll Never Forget" (Sonia Borg).
 * Embedded PDF photos, in-depth Urdu concept tutorials, voice narration, PDF export.
 */
object SpectacularMovesRepository {

    const val CAT_HES_ON_TOP = "hes_on_top"
    const val CAT_SHES_ON_TOP = "shes_on_top"
    const val CAT_REAR = "rear_entry"
    const val CAT_SITTING = "sitting_kneeling"
    const val CAT_STANDING = "standing"
    const val CAT_SIDE = "side_by_side"
    const val CAT_ORAL = "oral"
    const val CAT_HAND = "hand_jobs"
    const val CAT_ORGASM = "moregasms"

    fun getCategoryIds(): List<String> = listOf(
        PostureRepository.CAT_ALL,
        CAT_HES_ON_TOP, CAT_SHES_ON_TOP, CAT_REAR, CAT_SITTING,
        CAT_STANDING, CAT_SIDE, CAT_ORAL, CAT_HAND, CAT_ORGASM
    )

    fun getCategoryLabel(categoryId: String): String = when (categoryId) {
        PostureRepository.CAT_ALL -> "سب"
        CAT_HES_ON_TOP -> "وہ اوپر (مرد)"
        CAT_SHES_ON_TOP -> "وہ اوپر (عورت)"
        CAT_REAR -> "پیچھے سے"
        CAT_SITTING -> "بیٹھے اور گھٹنوں پر"
        CAT_STANDING -> "کھڑے"
        CAT_SIDE -> "ساتھ ساتھ"
        CAT_ORAL -> "زبانی لطف"
        CAT_HAND -> "ہاتھ سے"
        CAT_ORGASM -> "انزال تک"
        else -> categoryId
    }

    fun getAllMoves(): List<Posture> = moves
    fun getMoveById(id: String): Posture? = moves.find { it.id == id }
    fun getMovesByCategory(categoryId: String): List<Posture> {
        if (categoryId == PostureRepository.CAT_ALL) return moves
        return moves.filter { it.categoryId == categoryId }
    }

    private val moves: List<Posture> = listOf(
        move(
            id = "clitty_cat", num = 1, categoryId = CAT_HES_ON_TOP,
            difficulty = Difficulty.BEGINNER, illustrationRes = R.drawable.pic_move_01,
            urName = "کلیٹی کیٹ",
            urSummary = "Coital Alignment Technique — مشنری میں کلائیٹورل تحریک",
            urDesc = "تصور: مشنری میں جسموں کی سیدھ اکثر کلائیٹورس تک نہیں پہنچتی۔ یہ تکنیک (CAT) عانوی ہڈی کو کلائیٹورس پر رکھ کر جھولنے والی حرکت سے رگڑ پیدا کرتی ہے۔ تحقیق میں ۵۶٪ خواتین نے اس سے انزال میں بہتری رپورٹ کی۔",
            urSteps = listOf(
                "وہ آرام سے پیٹ کے بل لیٹے، گھٹنے ہلکے موڑے۔",
                "آپ گھٹنوں پر اوپر آئیں، عانوی ہڈی براہ راست کلائیٹورس پر رکھیں۔",
                "اندر-باہر کی بجائے اوپر-نیچے آہستہ جھولیں۔",
                "ہر ۳۰ سیکنڈ بعد پوچھیں: زاویہ ٹھیک ہے؟",
                "تال مل کر پکڑیں — جلدی نہ کریں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: کلائیٹورل تحریک انزال کی کلید ہے۔",
                "کیوں آپ کے لیے: مسلسل رابطہ erection برقرار رکھتا ہے۔",
                "کمر کے نیچے تکیہ زاویہ بہتر بناتا ہے۔",
                "اس کی ٹانگیں آپ کی کمر پر کراس کر سکتی ہیں۔",
            )
        ),
        move(
            id = "zen_hero", num = 2, categoryId = CAT_HES_ON_TOP,
            difficulty = Difficulty.BEGINNER, illustrationRes = R.drawable.pic_move_02,
            urName = "زین ہیرو",
            urSummary = "آہستہ rocking penetration — تناؤ سے سکون تک",
            urDesc = "تصور: مرد کی موجودگی اور زمین سے جڑی توانائی عورت کے لیے تحفہ ہے۔ یہ منظر نامہ rhythmic rocking سے جسم کو پرسکون کرتا ہے — کارکردگی نہیں، قربت مقصد ہے۔",
            urSteps = listOf(
                "غسل، موم بتیاں، پرسکون موسیقی تیار کریں۔",
                "وہ پیٹ کے بل، گھٹنے سینے کی طرف لائیں۔",
                "آپ سامنے گھٹنوں پر، ہاتھوں سے اس کے گھٹنوں کو ہلکے پکڑیں۔",
                "آہستہ آگے-پیچھے rock کریں — G-spot یا cervix زاویہ بدلیں۔",
                "آخر میں spoon position میں آرام کریں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: تناؤ دور ہو کر جسم نرم ہوتا ہے۔",
                "کیوں آپ کے لیے: آہستہ رفتار دیر تک رہنے میں مدد کرتی ہے۔",
                "نرچرنگ اور grounding کا بہترین موقع۔",
                "آنکھیں بند کر کے سانسیں ہم آہنگ کریں۔",
            )
        ),
        move(
            id = "backyard_bonk", num = 3, categoryId = CAT_HES_ON_TOP,
            difficulty = Difficulty.ADVANCED, illustrationRes = R.drawable.pic_move_03,
            urName = "بیک یارڈ بونک",
            urSummary = "ٹرampoline پر playful bouncing missionary",
            urDesc = "تصور: ننگے، بے فکر، کھیل کا مزہ۔ ٹرampoline کی قدرتی bounce گہرائی دیتی ہے — gravity آپ کا ساتھی ہے۔ آزادی کا احساس جوش بڑھاتا ہے۔",
            urSteps = listOf(
                "ٹرampoline صاف کریں، تولیہ اور sprinkler تیار رکھیں۔",
                "مل کر ہلکی bounce اور مزاح کریں۔",
                "وہ تولیے پر پیٹ کے بل لیٹے۔",
                "مشنری میں داخل ہوں — bounce کی rhythm تلاش کریں۔",
                "گرمی میں sprinkler کے نیچے foreplay کریں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: آزادی اور playfulness جوش بڑھاتی ہے۔",
                "کیوں آپ کے لیے: bounce سے کم محنت میں گہرائی ملتی ہے۔",
                "آہستہ شروع کریں — timing سیکھنے میں وقت لگتا ہے۔",
                "محفوظ ٹرampoline استعمال کریں۔",
            )
        ),
        move(
            id = "alchemist", num = 4, categoryId = CAT_HES_ON_TOP,
            difficulty = Difficulty.ADVANCED, illustrationRes = R.drawable.pic_move_04,
            urName = "الکیمسٹ",
            urSummary = "جذباتی توانائی کو جذباتی اور جسمانی release میں بدلنا",
            urDesc = "تصور: کبھی کبھی عورت تناؤ یا غصے میں ہوتی ہے۔ یہ منظر نامہ playful dominance، محبت اور sex سے emotional release دیتا ہے — force fantasy کو محفوظ طریقے سے پورا کرتا ہے۔",
            urSteps = listOf(
                "۶ فٹ نرم رسی اور safety word (مثلاً \"آلو\") طے کریں۔",
                "پرسکون لیکن assertive انداز میں قربت شروع کریں۔",
                "بازو اوپر باندھیں، ٹانگیں کھولیں — رضامندی سے۔",
                "passionate thrusts — emotions کو transform کریں۔",
                "بعد میں گلے لگائیں اور احساسات سنیں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: جذبات کا محفوظ اظہار orgasm گہرا کرتا ہے۔",
                "کیوں آپ کے لیے: directive role erection مضبوط رکھتا ہے۔",
                "ہمیشہ safety word کا فوری احترام کریں۔",
                "یہ energy اور intention کے بارے میں ہے۔",
            )
        ),
        move(
            id = "easy_glider", num = 5, categoryId = CAT_SHES_ON_TOP,
            difficulty = Difficulty.BEGINNER, illustrationRes = R.drawable.pic_move_05,
            urName = "ایزی گلائڈر",
            urSummary = "تیل سے full-body slide — massage اور sex ایک ساتھ",
            urDesc = "تصور: baby oil سے دونوں جسموں کا مکمل رابطہ۔ massage اور قربت ایک ساتھ — دینا اور لینا ایک ہی لمحے میں۔ premature ejaculation والے مردوں کے لیے بھی مفید۔",
            urSteps = listOf(
                "بستر پر تولیے، baby oil، موم بتیاں تیار کریں۔",
                "دونوں nude، تیل لگائیں۔",
                "وہ آپ کے اوپر سینے سے سینہ ملائے بیٹھے۔",
                "آہستہ slide کریں — کم penetration، زیادہ body contact۔",
                "pelvic muscles relax رکھیں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: مکمل جسمانی رابطہ محفوظ احساس دیتا ہے۔",
                "کیوں آپ کے لیے: کم شدت control میں مدد کرتی ہے۔",
                "تیل فرش پر پھسلن — تولیہ بچھائیں۔",
                "آوازیں اور moans سے feedback دیں۔",
            )
        ),
        move(
            id = "bucking_bronco", num = 6, categoryId = CAT_SHES_ON_TOP,
            difficulty = Difficulty.BEGINNER, illustrationRes = R.drawable.pic_move_06,
            urName = "بکنگ برونکو",
            urSummary = "وہ اوپر — آپ active coach بنیں",
            urDesc = "تصور: woman-on-top میں مرد بھی active رہے۔ ہاتھوں سے hips guide کریں، cheer کریں — یہ partnership ہے، نہ کہ passive دیکھنا۔",
            urSteps = listOf(
                "country music تیار رکھیں۔",
                "آپ پیٹ کے بل، وہ اوپر crouching position میں۔",
                "ہاتھوں سے hips آگے-پیچھے اور گول گھمائیں۔",
                "cheer کریں: \"ہاں!\" — مل کر rhythm پکڑیں۔",
                "تھکاوٹ پر reverse cowgirl آزمائیں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: آپ کی شمولیت اسے confident محسوس کراتی ہے۔",
                "کیوں آپ کے لیے: control اور view بہترین ہے۔",
                "آپ active participant ہیں۔",
                "آہستہ شروع کریں، پھر tempo بڑھائیں۔",
            )
        ),
        move(
            id = "call_of_wild", num = 7, categoryId = CAT_REAR,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_move_07,
            urName = "کال آف دی وائلڈ",
            urSummary = "Primal rear-entry — جانوروں جیسی توانائی",
            urDesc = "تصور: بہت سی خواتین چاہتی ہیں کہ ساتھی wild اور passionate ہو۔ growl، moan، hair pull — carnal side آزاد کریں، رضامندی کے ساتھ۔",
            urSteps = listOf(
                "mood تیار کریں — اندھیرا کمرہ یا fantasy setup۔",
                "وہ hands and knees پر — مختلف rear زاویے آزمائیں۔",
                "primal sounds نکالیں — howl، growl۔",
                "leg position بدل کر مختلف spots stimulate کریں۔",
                "بار بار check-in: \"ٹھیک ہے؟\"",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: ravished ہونے کی fantasy پوری ہوتی ہے۔",
                "کیوں آپ کے لیے: commanding persona erection بہتر بناتا ہے۔",
                "یہ fantasy ہے — حقیقی زبردستی نہیں۔",
                "کئی rear-entry زاویے آزمائیں۔",
            )
        ),
        move(
            id = "bedtime_stories", num = 8, categoryId = CAT_REAR,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_move_08,
            urName = "بیڈ ٹائم سٹوریز",
            urSummary = "erotic story پڑھتے ہوئے folded rear-entry",
            urDesc = "تصور: عورتیں الفاظ سے highly aroused ہوتی ہیں۔ آپ کا آواز، آپ کا جسم، erotic story — تینوں ایک ساتھ۔ ذہن اور جسم دونوں engage ہوں۔",
            urSteps = listOf(
                "erotic story یا submission story منتخب کریں۔",
                "warming lube تیار رکھیں۔",
                "وہ folded position: گھٹنے سینے کی طرف۔",
                "آپ پیچھے سے mount کریں۔",
                "آہستہ آواز میں story پڑھیں — thrusts story rhythm میں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: G-spot اور cervix stimulation + fantasy۔",
                "کیوں آپ کے لیے: PC muscle squeeze intense sensation۔",
                "آپ کو Casanova نہیں — صرف پڑھنا ہے۔",
                "story اس کی پسند کی ہو تو بہتر۔",
            )
        ),
        move(
            id = "go_green", num = 9, categoryId = CAT_REAR,
            difficulty = Difficulty.ADVANCED, illustrationRes = R.drawable.pic_move_09,
            urName = "گو گرین",
            urSummary = "sprinkler کے نیچے wheelbarrow — باغ میں adventure",
            urDesc = "تصور: پانی clitoris پر natural stimulator ہے۔ wheelbarrow position میں پیچھے سے — گرمی میں refreshing، باہر کی آزادی۔",
            urSteps = listOf(
                "باغ میں sprinkler لگائیں۔",
                "surprise کے طور پر باہر بلائیں۔",
                "وہ ہاتھ زمین پر wheelbarrow position۔",
                "spray clitoris stimulate کرے، آپ پیچھے سے penetrate کریں۔",
                "پہلے sprinkler pressure test کریں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: پانی + باہر کی فضا unique sensation۔",
                "کیوں آپ کے لیے: standing position muscle tension intense orgasm۔",
                "پھسلن سے بچنے کے لیے grass یا mat استعمال کریں۔",
                "پانی کا درجہ حرارت چیک کریں۔",
            )
        ),
        move(
            id = "the_office", num = 10, categoryId = CAT_SITTING,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_move_10,
            urName = "دی آفس",
            urSummary = "office chair پر adjustable seated sex",
            urDesc = "تصور: پہیوں والی chair leverage دیتی ہے — depth، pace، angle control آسان۔ کام کے stress کو pleasure میں بدلیں۔",
            urSteps = listOf(
                "office chair تیار کریں (wheels والی)۔",
                "وہ chair پر بیٹھے، آپ سامنے یا پیچھے۔",
                "chair adjust کر کے depth control کریں۔",
                "آگے-پیچھے roll کریں۔",
                "privately practice کریں پہلے۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: work fantasy + unexpected pleasure۔",
                "کیوں آپ کے لیے: chair depth undeniable ہے۔",
                "late night office fantasy کے لیے بہترین۔",
                "chair height adjust کرنا key ہے۔",
            )
        ),
        move(
            id = "naked_hug", num = 11, categoryId = CAT_SITTING,
            difficulty = Difficulty.BEGINNER, illustrationRes = R.drawable.pic_move_11,
            urName = "ننگا آغوش",
            urSummary = "cross-legged بیٹھ کر گلے ملنے والی intimate position",
            urDesc = "تصور: وہ آپ کی گود میں، ٹانگیں کمر کے گرد — safety، surrender، energy flow۔ emotional orgasm intense ہو سکتا ہے۔",
            urSteps = listOf(
                "موم بتیاں، گدے، گرم کمرہ تیار کریں۔",
                "آپ cross-legged بیٹھیں۔",
                "وہ سامنے بیٹھے، ٹانگیں آپ کی کمر لپیٹیں۔",
                "آہستہ rock کریں — \"سب ٹھیک ہو جائے گا\" کہیں۔",
                "eye contact اور slow breathing۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: محفوظ surrender space۔",
                "کیوں آپ کے لیے: semierect سے بھی شروع ہو سکتا ہے۔",
                "premature ejaculation والے مردوں کے لیے ideal۔",
                "energy body میں flow ہوتی ہے۔",
            )
        ),
        move(
            id = "oh_my_gondola", num = 12, categoryId = CAT_SITTING,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_move_12,
            urName = "گونڈولا والا لمحہ",
            urSummary = "بیٹھے بیٹھے کلائیٹورل تحریک — سرد موسم fantasy",
            urDesc = "تصور: وہ آپ کی گود میں، آپ کلائیٹورس stimulate کریں۔ gondola ride fantasy — سرد موسم، adventure، slow build۔",
            urSteps = listOf(
                "pocket vibrator، hand warmer تیار رکھیں۔",
                "آپ بیٹھیں، وہ lap پر بیٹھے۔",
                "ایک ہاتھ سے clitoris stimulate کریں۔",
                "ہر phase savor کریں — orgasm پر جلدی نہ جائیں۔",
                "view اور fantasy enjoy کریں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: seated angle confidence دیتی ہے۔",
                "کیوں آپ کے لیے: ہاتھ آزاد — اسے focus کر سکتے ہیں۔",
                "یہ اس کے لیے ہے — orgasm optional۔",
                "سرد موسم ambiance بنائیں۔",
            )
        ),
        move(
            id = "balls_out", num = 13, categoryId = CAT_SITTING,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_move_13,
            urName = "بالز آؤٹ",
            urSummary = "knee-standing — deep penetration + clit rub",
            urDesc = "تصور: balance چاہیے لیکن combo powerful ہے — گہری penetration اور simultaneous clitoral stimulation۔",
            urSteps = listOf(
                "balance practice کریں پہلے — wall support۔",
                "وہ bed edge پر پیٹ کے بل۔",
                "آپ knees پر، deep penetration۔",
                "ایک ہاتھ سے clitoris rub کریں۔",
                "balance ملنے پر rhythm پکڑیں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: depth + clit rub = intense orgasm۔",
                "کیوں آپ کے لیے: shaft full coverage sensation۔",
                "شروع میں wall support استعمال کریں۔",
                "balance سیکھنے میں وقت لگتا ہے۔",
            )
        ),
        move(
            id = "getting_jiggy", num = 14, categoryId = CAT_STANDING,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_move_14,
            urName = "گیٹنگ جیگی",
            urSummary = "رقص کے ساتھ standing grinding",
            urDesc = "تصور: dance club fantasy — hip grinding سے arousal build۔ Patrick Swayze بننے کی ضرورت نہیں۔",
            urSteps = listOf(
                "dance music اور sexy clothes تیار کریں۔",
                "dark corner یا home disco بنائیں۔",
                "hip grinding practice کریں۔",
                "رقص سے standing sex — rhythm merge کریں۔",
                "دیوار support کے لیے استعمال کریں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: dancing top fantasy list پر ہے۔",
                "کیوں آپ کے لیے: grinding آپ کو control دیتی ہے۔",
                "hip circles key ہیں۔",
                "screen پر نہ دکھائی گئی positions آزمائیں۔",
            )
        ),
        move(
            id = "fashion_show", num = 15, categoryId = CAT_STANDING,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_move_15,
            urName = "فیشن شو",
            urSummary = "کپڑے اتارتے ہوئے admiration اور seduction",
            urDesc = "تصور: shopping arousing ہے — وہ model بنے، آپ appreciative audience۔ body positivity + desire۔",
            urSteps = listOf(
                "نئے کپڑے یا gifts تیار رکھیں۔",
                "runway یا room میں fashion show setup۔",
                "ہر piece پر genuine compliment دیں۔",
                "ہر layer کے ساتھ intimacy بڑھائیں۔",
                "\"تم خوبصورت لگ رہی ہو\" — پہلے کہیں، پوچھنے سے پہلے۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: admiration اور words of affirmation۔",
                "کیوں آپ کے لیے: anticipation build کرتا ہے۔",
                "سچی تعریف کریں۔",
                "ہر کپڑے کے ساتھ نیا زاویہ آزمائیں۔",
            )
        ),
        move(
            id = "sexy_tai_chi", num = 16, categoryId = CAT_STANDING,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_move_16,
            urName = "سیکسی ٹائی چی",
            urSummary = "standing energy work — movement + meditation + sex",
            urDesc = "تصور: martial arts کی modified exercise — opponent کی energy feel کریں۔ arousal phase کو properly initiate کریں۔",
            urSteps = listOf(
                "پرسکون music، clear space تیار کریں۔",
                "وہ دیوار کے ساتھ، ٹانگیں آپ کی کمر پر۔",
                "آہستہ energy exchange — breathing sync۔",
                "micro-movements سے arousal build۔",
                "foreplay phase کو rush نہ کریں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: arousal phase often overlooked — یہ اسے پورا کرتا ہے۔",
                "کیوں آپ کے لیے: dual meditation connection بڑھاتی ہے۔",
                "moment میں رہیں۔",
                "standing position core strength چاہیے۔",
            )
        ),
        move(
            id = "real_campers", num = 17, categoryId = CAT_SIDE,
            difficulty = Difficulty.BEGINNER, illustrationRes = R.drawable.pic_move_17,
            urName = "ریئل کیمپرز",
            urSummary = "sleeping bag میں sideways — camping intimacy",
            urDesc = "تصور: stars، moonlight، sleeping bag constraints — resistance سے deeper penetration۔ outdoor romance۔",
            urSteps = listOf(
                "sleeping bag، camping mat تیار کریں۔",
                "دونوں bag میں sideways لیٹیں۔",
                "skin-to-skin contact maximize کریں۔",
                "bag کی resistance سے controlled movement۔",
                "باہر کی فضا enjoy کریں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: outdoor + muscle contact fantasy۔",
                "کیوں آپ کے لیے: bag leverage control دیتی ہے۔",
                "سردی میں bag گرم رکھتا ہے۔",
                "privacy چیک کریں۔",
            )
        ),
        move(
            id = "pleasure_party", num = 18, categoryId = CAT_SIDE,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_move_18,
            urName = "پلیژر پارٹی",
            urSummary = "side-lying — cock + nipples + story + dildo",
            urDesc = "تصور: group sex کا قریب ترین تجربہ — کئی stimulation ایک ساتھ۔ blindfold sensory focus بڑھاتا ہے۔",
            urSteps = listOf(
                "blindfold، dildo، lube تیار رکھیں۔",
                "وہ side-lying، blindfold پہنائیں۔",
                "penetration + nipple stimulation + whispered story۔",
                "dildo ass میں (رضامندی سے)۔",
                "ہر sensation کو savor کریں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: multiple hotspots = overwhelming pleasure۔",
                "کیوں آپ کے لیے: hands free different zones۔",
                "blindfold trust بڑھاتی ہے۔",
                "lube ضروری ہے۔",
            )
        ),
        move(
            id = "shagalicious", num = 19, categoryId = CAT_ORAL,
            difficulty = Difficulty.BEGINNER, illustrationRes = R.drawable.pic_move_19,
            urName = "شاگلicious",
            urSummary = "oral sex sling — U-spot stimulation",
            urDesc = "تصور: satin sheets، candles، rose petals — unconditional giving۔ spa سے بہتر massage with release۔",
            urSteps = listOf(
                "oral sex sling یا ankle straps تیار کریں۔",
                "satin sheets، candles، rose petals۔",
                "وہ sling میں legs spread — passive receive۔",
                "U-spot، G-spot، commissure — hand then mouth۔",
                "اسے صرف enjoy کرنے دیں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: passive receiving = deep relaxation = orgasmic۔",
                "کیوں آپ کے لیے: hands free maneuvering۔",
                "thoughtfulness counts — cash نہیں۔",
                "sling handcuffs کے طور پر بھی استعمال ہو سکتا ہے۔",
            )
        ),
        move(
            id = "kiss_of_date", num = 20, categoryId = CAT_ORAL,
            difficulty = Difficulty.BEGINNER, illustrationRes = R.drawable.pic_move_20,
            urName = "ڈیٹ کا بوسہ",
            urSummary = "passionate kissing date — south تک slow journey",
            urDesc = "تصور: women equate kissing with satisfaction۔ anticipation build — mouth آہستہ آہستہ نیچے۔",
            urSteps = listOf(
                "candles، romantic setting تیار کریں۔",
                "passionate kisses شروع کریں — face، neck۔",
                "ہر kiss farther south — slow journey۔",
                "high arousal پر pause کر کے kiss — stamina technique۔",
                "clitoris پر پہنچنے سے پہلے peak arousal۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: kissing = satisfaction correlation۔",
                "کیوں آپ کے لیے: tongue powerful tool — oral skills۔",
                "anticipation بڑھائیں۔",
                "pause + kiss = last longer technique۔",
            )
        ),
        move(
            id = "oh_my_goddess", num = 21, categoryId = CAT_ORAL,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_move_21,
            urName = "او مائی دیوی",
            urSummary = "vulva worship — goddess fantasy",
            urDesc = "تصور: knight kneels before queen۔ ego چھوڑیں — worship، devotion، begging for her magic vulva۔",
            urSteps = listOf(
                "romantic setting، knee cushion تیار کریں۔",
                "آپ گھٹنوں پر — begging posture۔",
                "foreplay سے پہلے devotion express کریں۔",
                "oral worship — slow، intentional۔",
                "اسے goddess کی طرح glow میں دیکھیں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: worship common female fantasy۔",
                "کیوں آپ کے لیے: seeing her glow unforgettable۔",
                "foreplay women کو men سے زیادہ چاہیے۔",
                "regular practice — glow بڑھتا ہے۔",
            )
        ),
        move(
            id = "sex_101", num = 22, categoryId = CAT_HAND,
            difficulty = Difficulty.BEGINNER, illustrationRes = R.drawable.pic_move_22,
            urName = "سیکس ۱۰۱",
            urSummary = "انٹرویو + ویڈیو — باہمی سیکھنا",
            urDesc = "تصور: اس کی پسند سیکھیں، ویڈیو بنائیں — best lover بنیں۔ judgment-free curiosity۔",
            urSteps = listOf(
                "شراب کے ساتھ playful انٹرویو — fantasies پوچھیں۔",
                "کیمرہ (رضامندی سے) setup۔",
                "وہ اپنی technique دکھائے۔",
                "مل کر فلم بنائیں — secrets سیکھیں۔",
                "privacy اور consent clear رکھیں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: heard اور understood محسوس کرنا۔",
                "کیوں آپ کے لیے: direct feedback best teacher۔",
                "رضامندی اور privacy ضروری۔",
                "بغیر judgment سوالات پوچھیں۔",
            )
        ),
        move(
            id = "splash", num = 23, categoryId = CAT_HAND,
            difficulty = Difficulty.BEGINNER, illustrationRes = R.drawable.pic_move_23,
            urName = "چھپاکا",
            urSummary = "female ejaculation — Skene's glands coaching",
            urDesc = "تصور: female ejaculation empowering ہو سکتی ہے۔ Skene's glands (paraurethral) — alkaline liquid، prostate جیسا۔ \"come here\" beckoning motion۔",
            urSteps = listOf(
                "گرم غسل یا shower تیار کریں۔",
                "پانی کے بہاؤ سے شروع۔",
                "G-spot پر beckoning finger motion۔",
                "clitoral + vaginal stimulation combine۔",
                "pressure نہ ڈالیں — explore کریں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: body control اور intimacy۔",
                "کیوں آپ کے لیے: shared experience connection۔",
                "ہر woman مختلف — big deal نہیں بھی ہو سکتا۔",
                "صابن sensitive areas avoid کریں۔",
            )
        ),
        move(
            id = "summer_concert", num = 24, categoryId = CAT_HAND,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_move_24,
            urName = "گرمیوں کا کنسرٹ",
            urSummary = "picnic blanket — hand sonata under blanket",
            urDesc = "تصور: concert fantasy — high and low notes۔ blanket کے نیچے digital delight — public thrill، private act۔",
            urSteps = listOf(
                "picnic blanket، outdoor spot تیار۔",
                "concert music یا live event۔",
                "blanket کے نیچے hand techniques۔",
                "tempo music کے ساتھ sync۔",
                "کبھی blanket نہ اٹھائیں — pro move۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: public thrill + skilled hands۔",
                "کیوں آپ کے لیے: finger dexterity practice۔",
                "slow tempo music love resonate کرتی ہے۔",
                "privacy چیک کریں۔",
            )
        ),
        move(
            id = "blue_pussy", num = 25, categoryId = CAT_ORGASM,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_move_25,
            urName = "انتہائی جوش",
            urSummary = "heavy foreplay — blue balls کا female equivalent",
            urDesc = "تصور: highly aroused anticipatory state — پھر satisfying release۔ extended foreplay craving build کرتا ہے۔",
            urSteps = listOf(
                "اس کی masturbation preferences یاد کریں۔",
                "extended foreplay — high arousal تک۔",
                "knees-to-chest position میں deep penetration۔",
                "clitoral contact برقرار رکھیں۔",
                "tease longer = release stronger۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: anticipation orgasm intense بناتی ہے۔",
                "کیوں آپ کے لیے: feedback سے control سیکھیں۔",
                "music arousal state trigger کر سکتا ہے۔",
                "cervix zone gentle approach۔",
            )
        ),
        move(
            id = "sandy_shenanigans", num = 26, categoryId = CAT_ORGASM,
            difficulty = Difficulty.ADVANCED, illustrationRes = R.drawable.pic_move_26,
            urName = "ریت کے کرتب",
            urSummary = "beach sex — sand burns سے بچیں",
            urDesc = "تصور: beach fantasy — get away، get off۔ thoughtfulness سے pro بنیں، experience نہ ہو تو بھی۔",
            urSteps = listOf(
                "private beach یا sandbox setup۔",
                "towel بچھائیں sand سے بچنے کے لیے۔",
                "playful wrestling اور teasing۔",
                "protected intimate play۔",
                "shower afterward تیار رکھیں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: fantasy fulfilled + thoughtful partner۔",
                "کیوں آپ کے لیے: adventure memory۔",
                "sand irritation avoid — careful positioning۔",
                "sunrise to sunset sexy feeling۔",
            )
        ),
        move(
            id = "medicine_man", num = 27, categoryId = CAT_ORGASM,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_move_27,
            urName = "معالج",
            urSummary = "healing oral orgasm — sexual medicine",
            urDesc = "تصور: orgasm natural drugs release کرتا ہے۔ doctor fantasy — pelvic exam، cure-all oral orgasm۔",
            urSteps = listOf(
                "massage oil، warm room تیار۔",
                "وہ پیٹ کے بل — pelvic tilt۔",
                "full access oral — therapeutic intention۔",
                "emotional + physical release۔",
                "aftercare — hug، water۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: healing touch + cared for feeling۔",
                "کیوں آپ کے لیے: easy entrance، magic touch role۔",
                "Taoist genital reflexology concept۔",
                "orgasm pain alleviate کر سکتا ہے۔",
            )
        ),
        move(
            id = "xtra_mileage", num = 28, categoryId = CAT_ORGASM,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_move_28,
            urName = "اضافی برداشت",
            urSummary = "stamina — orgasm without ejaculation",
            urDesc = "تصور: longer lovemaking positions۔ orgasm without ejaculating — cock hard رہے، pleasure share کریں۔",
            urSteps = listOf(
                "breathing exercises practice۔",
                "start-stop technique during intercourse۔",
                "pelvic floor control۔",
                "variety of positions for stamina۔",
                "Clitty Cat کے ساتھ combine کریں۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: longer sessions = more orgasms possible۔",
                "کیوں آپ کے لیے: confidence as lover۔",
                "muscle tension کم = longer lasting۔",
                "practice سے control آتا ہے۔",
            )
        ),
        move(
            id = "day_at_improv", num = 29, categoryId = CAT_ORGASM,
            difficulty = Difficulty.ADVANCED, illustrationRes = R.drawable.pic_move_29,
            urName = "بے ساختہ دن",
            urSummary = "role-play improv — 7 minutes to get in character",
            urDesc = "تصور: dress up fantasy — saloon girl، police officer، superhero۔ improv sex moves — no script۔",
            urSteps = listOf(
                "7 minute timer setup۔",
                "character costumes تیار۔",
                "وہ character میں آئے — آپ seduce کریں۔",
                "humor اور surprise embrace۔",
                "consent boundaries clear۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: dress up + fantasy fulfillment۔",
                "کیوں آپ کے لیے: creativity keeps fresh۔",
                "perfectionism چھوڑ دیں۔",
                "laughter intimacy بڑھاتی ہے۔",
            )
        ),
        move(
            id = "grand_finale", num = 30, categoryId = CAT_ORGASM,
            difficulty = Difficulty.ADVANCED, illustrationRes = R.drawable.pic_move_30,
            urName = "گرینڈ فائنل",
            urSummary = "24 hours — sex, sleep, eat, sex only",
            urDesc = "تصور: tour de sex کا climax۔ no phones، no TV — full-body orgasms، rejuvenation vacation۔",
            urSteps = listOf(
                "24 hour block plan کریں۔",
                "phones off — distractions zero۔",
                "positions rotate — favorites combine۔",
                "sleep، eat، sex cycle۔",
                "aftercare — world میں واپسی fresh۔",
            ),
            urTips = listOf(
                "کیوں اس کے لیے: ultimate connection experience۔",
                "کیوں آپ کے لیے: all techniques showcase۔",
                "یہ journey کا celebration ہے۔",
                "aftercare essential۔",
            )
        ),
    )

    private fun move(
        id: String, num: Int, categoryId: String, difficulty: Difficulty,
        illustrationRes: Int, urName: String, urSummary: String, urDesc: String,
        urSteps: List<String>, urTips: List<String>
    ): Posture {
        val category = getCategoryLabel(categoryId)
        val displayName = "$num. $urName"
        val content = LocalizedContent(
            name = displayName, category = category, summary = urSummary,
            description = urDesc, steps = urSteps, tips = urTips
        )
        return Posture(
            id = id, difficulty = difficulty, illustrationRes = illustrationRes,
            categoryId = categoryId, english = content, urdu = content
        )
    }
}
