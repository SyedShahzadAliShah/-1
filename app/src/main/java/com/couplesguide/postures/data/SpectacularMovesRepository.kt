package com.couplesguide.postures.data

import com.couplesguide.postures.R

/**
 * 30 moves from "Spectacular Sex Moves She'll Never Forget" (Sonia Borg).
 * Concise Urdu descriptions for voice narration and PDF export.
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
        CAT_HES_ON_TOP,
        CAT_SHES_ON_TOP,
        CAT_REAR,
        CAT_SITTING,
        CAT_STANDING,
        CAT_SIDE,
        CAT_ORAL,
        CAT_HAND,
        CAT_ORGASM
    )

    fun getCategoryLabel(categoryId: String): String = when (categoryId) {
        PostureRepository.CAT_ALL -> "سب"
        CAT_HES_ON_TOP -> "وہ اوپر"
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
            difficulty = Difficulty.BEGINNER, illustrationRes = R.drawable.pic_missionary,
            urName = "کلیٹی کیٹ",
            urSummary = "مشنری میں کلitoral رگڑ — انزال میں ۵۶٪ اضافے والی تکنیک۔",
            urDesc = "آدمی اوپر، عانوی ہڈی ہمیشہ کلitoris پر دباؤ رکھے۔ تیز جھٹکوں کی بجائے آہستہ جھولنے والی حرکت۔",
            urSteps = listOf(
                "وہ پیٹ کے بل، گھٹنے ہلکے موڑے۔",
                "آپ گھٹنوں پر اوپر، عانوی ہڈی کلitoris پر رکھیں۔",
                "اندر باہر کی بجائے اوپر نیچے جھولیں۔",
                "آہستہ تال پیدا کریں اور پوچھتے رہیں کیا اچھا لگ رہا ہے۔"
            ),
            urTips = listOf(
                "کمر کے نیچے تکیہ زاویہ بہتر بناتا ہے۔",
                "اس کی ٹانگیں آپ کی کمر پر کراس کر سکتی ہیں۔",
                "رابطہ برقرار رکھنا کلید ہے۔"
            )
        ),
        move(
            id = "zen_hero", num = 2, categoryId = CAT_HES_ON_TOP,
            difficulty = Difficulty.BEGINNER, illustrationRes = R.drawable.pic_butterfly,
            urName = "زین ہیرو",
            urSummary = "تناؤ دور کرنے کے لیے آہستہ rocking penetration۔",
            urDesc = "تھکے ہوئے دن کے بعد پرسکون قربت۔ گھٹنے سینے کی طرف، rhythmic rock سے سکون ملتا ہے۔",
            urSteps = listOf(
                "غسل، موم بتیاں اور پرسکون موسیقی تیار کریں۔",
                "وہ پیٹ کے بل، گھٹنے سینے کی طرف۔",
                "آپ سامنے گھٹنوں پر، ہاتھوں سے اس کے گھٹنوں کو پکڑیں۔",
                "آہستہ rock کریں — G-spot یا cervix زاویہ بدل سکتے ہیں۔"
            ),
            urTips = listOf(
                "نرٹuring اور grounding کا بہترین موقع۔",
                "آہستہ رفتار آپ کو زیادہ دیر تک رہنے میں مدد کرتی ہے۔",
                "آخر میں fetal position میں spoon کریں۔"
            )
        ),
        move(
            id = "backyard_bonk", num = 3, categoryId = CAT_HES_ON_TOP,
            difficulty = Difficulty.ADVANCED, illustrationRes = R.drawable.pic_missionary,
            urName = "بیک یارڈ بونک",
            urSummary = "ٹرampoline پر playful bouncing missionary۔",
            urDesc = "باہر کھیل کا مزہ۔ trampoline کی bounce سے گہرائی ملتی ہے، کم محنت میں زیادہ لطف۔",
            urSteps = listOf(
                "ٹرampoline صاف کریں، تولیہ اور sprinkler تیار رکھیں۔",
                "مل کر naked bounce کریں، مزاح کریں۔",
                "وہ پیٹ کے بل، تولیہ پر لیٹے۔",
                "مشنری میں داخل ہوں — trampoline کی rhythm تلاش کریں، depth پر focus کریں۔"
            ),
            urTips = listOf(
                "آہستہ شروع کریں، timing سیکھنے میں وقت لگتا ہے۔",
                "گرمی میں sprinkler کے نیچے foreplay کریں۔",
                "متبادل: وہ الٹ بیٹھ کر reverse cowgirl آزمائے۔"
            )
        ),
        move(
            id = "alchemist", num = 4, categoryId = CAT_HES_ON_TOP,
            difficulty = Difficulty.ADVANCED, illustrationRes = R.drawable.pic_missionary,
            urName = "الکیمسٹ",
            urSummary = "تناؤ کو جذبے میں بدلنے والی passionate control position۔",
            urDesc = "بازو اوپر، ٹانگیں کھولی — playful dominance اور emotional release۔ safety word طے کریں۔",
            urSteps = listOf(
                "۶ فٹ رسی اور safety word (مثلاً \"آلو چپ\") طے کریں۔",
                "پرسکون لیکن assertive انداز میں قربت شروع کریں۔",
                "بازو اوپر باندھیں، ٹانگیں کھولیں۔",
                "passionate thrusts — emotions کو sex میں transform کریں۔"
            ),
            urTips = listOf(
                "یہ energy اور intention کے بارے میں ہے، صرف act نہیں۔",
                "hog tie variation گہری penetration دے سکتی ہے۔",
                "ہمیشہ safety word کا احترام کریں۔"
            )
        ),
        move(
            id = "easy_glider", num = 5, categoryId = CAT_SHES_ON_TOP,
            difficulty = Difficulty.BEGINNER, illustrationRes = R.drawable.pic_cowgirl,
            urName = "ایزی گلائڈر",
            urSummary = "تیل لگا کر پورے جسم کی slide اور massage۔",
            urDesc = "baby oil سے دونوں جسموں کا full contact glide۔ massage اور sex ایک ساتھ۔",
            urSteps = listOf(
                "بستر پر تولیے، baby oil، موم بتیاں تیار کریں۔",
                "دونوں nude، تیل لگائیں۔",
                "وہ آپ کے اوپر بیٹھے، سینے سے سینہ ملائیں۔",
                "آہستہ slide کریں — کم penetration، زیادہ body contact۔"
            ),
            urTips = listOf(
                "یہ position premature ejaculation میں control میں مدد کرتی ہے۔",
                "pelvic muscles relax رکھیں تاکہ دیر تک رہ سکیں۔",
                "آوازیں اور moans سے feedback دیں۔"
            )
        ),
        move(
            id = "bucking_bronco", num = 6, categoryId = CAT_SHES_ON_TOP,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_cowgirl,
            urName = "بکنگ برونکو",
            urSummary = "وہ اوپر — آپ ہاتھوں سے hips guide کریں۔",
            urDesc = "country vibe کے ساتھ woman-on-top control۔ آپ active coach بنیں، rhythm مل کر بنائیں۔",
            urSteps = listOf(
                "country music اور hat تیار رکھیں۔",
                "آپ پیٹ کے بل، وہ اوپر بیٹھے۔",
                "ہاتھوں سے hips آگے پیچھے اور گول گھمائیں۔",
                "cheer کریں، مل کر rhythm پکڑیں۔"
            ),
            urTips = listOf(
                "آپ active participant ہیں، passive نہیں۔",
                "یہ position میں آپ کا control بہتر ہوتا ہے۔",
                "آہستہ شروع کریں، پھر tempo بڑھائیں۔"
            )
        ),
        move(
            id = "call_of_wild", num = 7, categoryId = CAT_REAR,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_doggy,
            urName = "کال آف دی وائلڈ",
            urSummary = "جانوروں جیسی wild rear-entry fantasy۔",
            urDesc = "بال پکڑیں، growl کریں — primal energy سے carnal side آزاد ہوتی ہے۔",
            urSteps = listOf(
                "جانوروں کی mating والی فلم دیکھیں، scene cue کریں۔",
                "ghar صاف، mood تیار کریں۔",
                "وہ hands and knees پر — یا مختلف rear variations آزمائیں۔",
                "primal sounds، hair pull، deep thrusts — wild rhythm۔"
            ),
            urTips = listOf(
                "یہ fantasy اور role-play پر مبنی ہے۔",
                "بار بار check-in کریں — comfort ضروری ہے۔",
                "کئی rear-entry زاویے آزمائیں۔"
            )
        ),
        move(
            id = "bedtime_stories", num = 8, categoryId = CAT_REAR,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_lazy_dog,
            urName = "بیڈ ٹائم سٹوریز",
            urSummary = "erotic story پڑھتے ہوئے folded rear-entry۔",
            urDesc = "گھٹنے سینے کی طرف، آپ اوپر — الفاظ اور physical ایک ساتھ۔",
            urSteps = listOf(
                "erotic story یا submission story منتخب کریں۔",
                "warming lube یا clitoral stimulator تیار رکھیں۔",
                "وہ folded position میں، آپ پیچھے سے mount کریں۔",
                "آہستہ آواز میں story پڑھیں، thrusts story کے rhythm میں۔"
            ),
            urTips = listOf(
                "عورتیں الفاظ سے highly aroused ہوتی ہیں۔",
                "آپ کو Casanova نہیں — صرف story پڑھنی ہے۔",
                "اس کی PC muscle squeeze آپ کو intense sensation دیتی ہے۔"
            )
        ),
        move(
            id = "go_green", num = 9, categoryId = CAT_REAR,
            difficulty = Difficulty.ADVANCED, illustrationRes = R.drawable.pic_standing,
            urName = "گو گرین",
            urSummary = "sprinkler کے نیچے wheelbarrow rear-entry۔",
            urDesc = "باغ میں sprinkler — پani clitoris پر، آپ پیچھے سے۔ گرمی میں refreshing adventure۔",
            urSteps = listOf(
                "باغ میں sprinkler لگائیں، bathing suit تیار رکھیں۔",
                "surprise کے طور پر باہر بلائیں۔",
                "وہ ہاتھ زمین پر wheelbarrow position۔",
                "spray clitoris stimulate کرے، آپ پیچھے سے penetrate کریں۔"
            ),
            urTips = listOf(
                "پani کا pressure clitoris کے لیے natural stimulator ہے۔",
                "standing position muscle tension بڑھاتی ہے — orgasm intense ہو سکتا ہے۔",
                "پہلے sprinkler pressure test کریں۔"
            )
        ),
        move(
            id = "the_office", num = 10, categoryId = CAT_SITTING,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_lotus,
            urName = "دی آفس",
            urSummary = "office chair پر adjustable seated sex۔",
            urDesc = "پہیوں والی chair leverage دیتی ہے — depth اور pace control آسان۔",
            urSteps = listOf(
                "office chair تیار کریں (wheels والی بہتر)۔",
                "وہ chair پر بیٹھے، آپ سامنے یا پیچھے position۔",
                "chair adjust کر کے depth control کریں۔",
                "آگے پیچھے roll کریں — work stress کو pleasure میں بدلیں۔"
            ),
            urTips = listOf(
                "late night office fantasy کے لیے بہترین۔",
                "chair height adjust کرنا key ہے۔",
                "privately practice کریں پہلے۔"
            )
        ),
        move(
            id = "naked_hug", num = 11, categoryId = CAT_SITTING,
            difficulty = Difficulty.BEGINNER, illustrationRes = R.drawable.pic_lotus,
            urName = "ننگا آغوش",
            urSummary = "cross-legged بیٹھ کر گلے ملنے والی intimate position۔",
            urDesc = "وہ آپ کی گود میں، ٹانگیں کمر کے گرد — safety اور surrender۔",
            urSteps = listOf(
                "موم بتیاں، گدے، گرم کمرہ تیار کریں۔",
                "آپ cross-legged بیٹھیں۔",
                "وہ سامنے بیٹھے، ٹانگیں آپ کی کمر لپیٹیں۔",
                "آہستہ rock کریں — \"سب ٹھیک ہو جائے گا\" کہیں۔"
            ),
            urTips = listOf(
                "semierect penis سے بھی شروع ہو سکتا ہے۔",
                "premature ejaculation والے مردوں کے لیے ideal۔",
                "eye contact اور slow breathing اہم ہے۔"
            )
        ),
        move(
            id = "oh_my_gondola", num = 12, categoryId = CAT_SITTING,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_lotus,
            urName = "گondola والا لمحہ",
            urSummary = "بیٹھے بیٹھے کلitoris محرک — گondola ride fantasy۔",
            urDesc = "وہ آپ کی گود میں، آپ کلitoris رگڑیں۔ سرد موسم adventure fantasy۔",
            urSteps = listOf(
                "pocket vibrator، hand warmer تیار رکھیں۔",
                "آپ بیٹھیں، وہ lap پر بیٹھے۔",
                "ایک ہاتھ سے clitoris stimulate کریں۔",
                "view اور fantasy کو enjoy کریں — orgasm تک slow build۔"
            ),
            urTips = listOf(
                "یہ اس کے لیے ہے — orgasm پر focus نہ کریں۔",
                "ہر phase کو savor کریں۔",
                "seated angle سے confidence ملتی ہے۔"
            )
        ),
        move(
            id = "balls_out", num = 13, categoryId = CAT_SITTING,
            difficulty = Difficulty.ADVANCED, illustrationRes = R.drawable.pic_edge_bed,
            urName = "بالز آؤٹ",
            urSummary = "کnee-standing position — deep penetration اور clit rub۔",
            urDesc = "balance چاہیے — گہری penetration اور simultaneous clitoral stimulation۔",
            urSteps = listOf(
                "balance practice کریں پہلے۔",
                "وہ پیٹ کے بل یا edge پر، آپ knees پر۔",
                "deep penetration کے ساتھ clitoris rub کریں۔",
                "balance ملنے پر rhythm پکڑیں۔"
            ),
            urTips = listOf(
                "شروع میں wall support استعمال کریں۔",
                "balance سیکھنے میں وقت لگتا ہے۔",
                "clit rub + depth combo powerful ہے۔"
            )
        ),
        move(
            id = "getting_jiggy", num = 14, categoryId = CAT_STANDING,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_standing,
            urName = "گیٹنگ جیگی",
            urSummary = "رقص کے ساتھ standing grinding sex۔",
            urDesc = "dance club یا home disco — hip grinding سے arousal build۔",
            urSteps = listOf(
                "dance music اور sexy clothes تیار کریں۔",
                "dark corner یا home disco بنائیں۔",
                "hip grinding practice کریں۔",
                "رقص سے standing sex — rhythm میں merge کریں۔"
            ),
            urTips = listOf(
                "Patrick Swayze بننے کی ضرورت نہیں۔",
                "hip circles اور grinding key ہیں۔",
                "دیوار support کے لیے استعمال کریں۔"
            )
        ),
        move(
            id = "fashion_show", num = 15, categoryId = CAT_STANDING,
            difficulty = Difficulty.BEGINNER, illustrationRes = R.drawable.pic_standing,
            urName = "فیشن شو",
            urSummary = "کپڑے اتارتے ہوئے admiration اور seduction۔",
            urDesc = "وہ model بنے، آپ appreciative audience — body positivity اور desire۔",
            urSteps = listOf(
                "نئے کپڑے یا gifts تیار رکھیں۔",
                "runway یا room میں fashion show setup۔",
                "ہر piece پر genuine compliment دیں۔",
                "ہر layer کے ساتھ intimacy بڑھائیں۔"
            ),
            urTips = listOf(
                "body image issues orgasm روک سکتی ہیں — acceptance دکھائیں۔",
                "سچی تعریف powerful aphrodisiac ہے۔",
                "پوچھنے سے پہلے بتائیں وہ beautiful ہے۔"
            )
        ),
        move(
            id = "sexy_tai_chi", num = 16, categoryId = CAT_STANDING,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_standing,
            urName = "سیکسی ٹائی چی",
            urSummary = "energy flow والی standing face-to-face movement۔",
            urDesc = "dual meditation + movement + sex — arousal phase کی perfect شروعات۔",
            urSteps = listOf(
                "خاموش room، soft music۔",
                "آمنے سامنے کھڑے، ہاتھ ملائیں۔",
                "slow tai chi movements — energy feel کریں۔",
                "movement gradually intimate بنائیں۔"
            ),
            urTips = listOf(
                "foreplay phase کو skip نہ کریں۔",
                "resistance feel ہو تو flow break ہوتا ہے۔",
                "mindfulness orgasm intense بناتی ہے۔"
            )
        ),
        move(
            id = "real_campers", num = 17, categoryId = CAT_SIDE,
            difficulty = Difficulty.BEGINNER, illustrationRes = R.drawable.pic_spooning,
            urName = "ریئل کیمپرز",
            urSummary = "sleeping bag میں sideways intimate camping sex۔",
            urDesc = "تاروں کے نیچے، bag کی constraint resistance بن کر deeper penetration دیتی ہے۔",
            urSteps = listOf(
                "extra sleeping bag، towels، lube pack کریں۔",
                "camping spot یا bedroom camping setup۔",
                "sleeping bag میں sideways position۔",
                "constraint use کر کے slow deep movement۔"
            ),
            urTips = listOf(
                "mummy bag بہت tight — regular bag بہتر۔",
                "stars اور moonlight mood بڑھاتے ہیں۔",
                "baby wipes handy رکھیں۔"
            )
        ),
        move(
            id = "pleasure_party", num = 18, categoryId = CAT_SIDE,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_side_by_side,
            urName = "پلیژر پارٹی",
            urSummary = "ساتھ ساتھ mutual pleasure party position۔",
            urDesc = "دونوں equal participants — side by side exploration اور shared climax۔",
            urSteps = listOf(
                "toys، lube، mood lighting تیار کریں۔",
                "ساتھ ساتھ لیٹیں، آمنے سامنے یا یکساں سمت۔",
                "hand exploration اور mutual stimulation۔",
                "مل کر rhythm بنائیں — party vibe رکھیں۔"
            ),
            urTips = listOf(
                "fantasy share کرنا arousal بڑھاتا ہے۔",
                "ہر partner equally pleasure پائے۔",
                "playful attitude رکھیں۔"
            )
        ),
        move(
            id = "shagalicious", num = 19, categoryId = CAT_ORAL,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_imagine_embrace,
            urName = "شاندار زبانی",
            urSummary = "ریشمی بستر اور زبانی لطف — بغیر جلدی کے۔",
            urDesc = "پنکھڑیاں، موم بتیاں — وہ آرام سے، آپ U-spot محرک دیں۔",
            urSteps = listOf(
                "ریشمی چادر، پنکھڑیاں، ٹائیوں کا sling بنائیں۔",
                "رومانوی بستر تیار کریں۔",
                "وہ sling میں، ٹانگیں کھولے۔",
                "ہموار زبان U-spot پر — آہستہ زبانی لطف۔"
            ),
            urTips = listOf(
                "یہ دینے کا عمل ہے — جلدی نہ کریں۔",
                "خیال اہم ہے — پیسہ ضروری نہیں۔",
                "پر اور تیل حسیت بڑھاتے ہیں۔"
            )
        ),
        move(
            id = "kiss_of_date", num = 20, categoryId = CAT_ORAL,
            difficulty = Difficulty.BEGINNER, illustrationRes = R.drawable.pic_imagine_candlelight,
            urName = "ڈیٹ کا بوسہ",
            urSummary = "ڈیٹ نائٹ زبانی لطف — رومانوی buildup۔",
            urDesc = "خصوصی ماحول — بوسوں سے زبانی لطف تک آہستہ منتقلی۔",
            urSteps = listOf(
                "ڈنر، موم بتیاں، موسیقی — ڈیٹ پلان۔",
                "گہرے بوسے اور ہلکی تحریک۔",
                "آہستہ نیچے زبانی لطف کی طرف۔",
                "ڈیٹ کی energy برقرار، انزال تک۔"
            ),
            urTips = listOf(
                "گہرے بوسے عورتوں کی اطمینان کی کلید ہیں۔",
                "جلدی نہ کریں — انتظار بڑھائیں۔",
                "آنکھوں کا رابطہ اور خوشبو یادگار بناتے ہیں۔"
            )
        ),
        move(
            id = "oh_my_goddess", num = 21, categoryId = CAT_ORAL,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_imagine_starlight,
            urName = "او مائی دیوی",
            urSummary = "عبادت انداز زبانی لطف — دیوی کا سلوک۔",
            urDesc = "وہ دیوی، آپ عبادت گزار — ارادت سے زبانی لطف۔",
            urSteps = listOf(
                "موم بتیاں، نرم کپڑا — خاص ماحول۔",
                "وہ ملکہ والی پوزیشن میں۔",
                "ادب سے قریب جائیں — عبادت کا mindset۔",
                "آہستہ devoted زبانی — انزال جشن۔"
            ),
            urTips = listOf(
                "نیت زبانی لطف کو یادگار بناتی ہے۔",
                "وہ عزت محسوس کرے۔",
                "یہ mindset بدل سکتا ہے۔"
            )
        ),
        move(
            id = "sex_101", num = 22, categoryId = CAT_HAND,
            difficulty = Difficulty.BEGINNER, illustrationRes = R.drawable.pic_imagine_breath,
            urName = "سیکس ۱۰۱",
            urSummary = "انٹرویو + ویڈیو — باہمی سیکھنا۔",
            urDesc = "اس کی پسند سیکھیں، ویڈیو بنائیں — بہترین ساتھی بنیں۔",
            urSteps = listOf(
                "شراب کے ساتھ playful انٹرویو — خواب پوچھیں۔",
                "کیمرہ (رضامندی سے)۔",
                "وہ اپنی technique دکھائے۔",
                "مل کر فلم بنائیں — راز سیکھیں۔"
            ),
            urTips = listOf(
                "رضامندی اور privacy ضروری۔",
                "بغیر judgment سوالات پوچھیں۔",
                "یہ سیکھنے کا مشق ہے۔"
            )
        ),
        move(
            id = "splash", num = 23, categoryId = CAT_HAND,
            difficulty = Difficulty.BEGINNER, illustrationRes = R.drawable.pic_imagine_ocean,
            urName = "چھپاکا",
            urSummary = "پانی + ہاتھ — غسل یا shower adventure۔",
            urDesc = "گرم پانی میں ہath exploration — حسی overload۔",
            urSteps = listOf(
                "گرم غسل یا shower تیار کریں۔",
                "پani کے بہاؤ سے شروع۔",
                "لubricated ہath techniques۔",
                "پani کا درجہ حرارت آرام دہ رکھیں۔"
            ),
            urTips = listOf(
                "صابن sensitive areas کو چبھا سکتا ہے۔",
                "پھسلن روک mat safety کے لیے۔",
                "پani کی sensation منفرد جوش دیتی ہے۔"
            )
        ),
        move(
            id = "summer_concert", num = 24, categoryId = CAT_HAND,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_imagine_morning,
            urName = "گرمیوں کا کنسرٹ",
            urSummary = "موسیقی کی تال میں ہath سے لطف۔",
            urDesc = "concert rhythm follow — موسیقی synced hand stimulation۔",
            urSteps = listOf(
                "live music یا playlist تیار۔",
                "concert ماحول (اندھیرا کمرہ، lights)۔",
                "music beat follow کرتے hand movement۔",
                "crescendo پر انزال build۔"
            ),
            urTips = listOf(
                "تال sync انزال intense بناتا ہے۔",
                "concert memory recreate کریں۔",
                "tempo آہستہ بڑھائیں۔"
            )
        ),
        move(
            id = "blue_pussy", num = 25, categoryId = CAT_ORGASM,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_butterfly,
            urName = "انتہائی جوش",
            urSummary = "شدید پیش بازی — پھر گہری penetration۔",
            urDesc = "انتہائی تحریک کے بعد satisfying release — teasing پھر انزال۔",
            urSteps = listOf(
                "اس کی masturbation preferences یاد کریں (Sex 101 سے)۔",
                "extended foreplay — high arousal تک۔",
                "knees-to-chest position میں deep penetration۔",
                "clitoral contact برقرار رکھیں۔"
            ),
            urTips = listOf(
                "music anchor arousal state trigger کر سکتا ہے۔",
                "tease longer = release stronger۔",
                "cervix zone gentle approach چاہیے۔"
            )
        ),
        move(
            id = "sandy_shenanigans", num = 26, categoryId = CAT_ORGASM,
            difficulty = Difficulty.ADVANCED, illustrationRes = R.drawable.pic_imagine_ocean,
            urName = "ریت کے کرتب",
            urSummary = "beach sand play + orgasm adventure۔",
            urDesc = "ساحل پر playful shenanigans — sand sensation unique experience۔",
            urSteps = listOf(
                "private beach spot یا sandbox setup۔",
                "towel بچھائیں sand سے بچنے کے لیے۔",
                "playful wrestling اور teasing۔",
                "protected intimate play — sand sensitive areas avoid۔"
            ),
            urTips = listOf(
                "sand irritation سے بچیں — careful positioning۔",
                "shower nearby رکھیں afterward۔",
                "playfulness key ہے۔"
            )
        ),
        move(
            id = "medicine_man", num = 27, categoryId = CAT_ORGASM,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_edge_bed,
            urName = "معالج",
            urSummary = "healing touch + therapeutic orgasm session۔",
            urDesc = "massage سے orgasm تک — body mind spirit connection۔",
            urSteps = listOf(
                "massage oil، warm room تیار کریں۔",
                "full body massage — no rush۔",
                "erogenous zones gradually include کریں۔",
                "therapeutic orgasm — emotional + physical release۔"
            ),
            urTips = listOf(
                "orgasm صرف physical نہیں — emotional بھی۔",
                "loved feel کروana essential۔",
                "healing intention رکھیں۔"
            )
        ),
        move(
            id = "xtra_mileage", num = 28, categoryId = CAT_ORGASM,
            difficulty = Difficulty.INTERMEDIATE, illustrationRes = R.drawable.pic_missionary,
            urName = "اضافی برداشت",
            urSummary = "stamina control techniques — longer lasting pleasure۔",
            urDesc = "ejaculation control سیکھیں — start-stop، breathing، pelvic floor۔",
            urSteps = listOf(
                "breathing exercises practice کریں۔",
                "start-stop technique during intercourse۔",
                "pelvic floor muscles control۔",
                "awareness بڑھائیں — longer sessions۔"
            ),
            urTips = listOf(
                "Clitty Cat کے ساتھ مل کر best results۔",
                "muscle tension کم = longer lasting۔",
                "practice سے control آتا ہے۔"
            )
        ),
        move(
            id = "day_at_improv", num = 29, categoryId = CAT_ORGASM,
            difficulty = Difficulty.ADVANCED, illustrationRes = R.drawable.pic_scissors,
            urName = "بے ساختہ دن",
            urSummary = "spontaneous creative sex — no script improvisation۔",
            urDesc = "کچھ plan نہیں — creativity، humor، surprise سے orgasm۔",
            urSteps = listOf(
                "rules: no plan، yes to everything (consent limits内)۔",
                "random props use کریں۔",
                "humor اور surprise embrace کریں۔",
                "flow میں orgasm naturally آئے۔"
            ),
            urTips = listOf(
                "perfectionism چھوڑ دیں۔",
                "laughter intimacy بڑھاتی ہے۔",
                "consent boundaries clear رکھیں۔"
            )
        ),
        move(
            id = "grand_finale", num = 30, categoryId = CAT_ORGASM,
            difficulty = Difficulty.ADVANCED, illustrationRes = R.drawable.pic_reverse_cowgirl,
            urName = "گرینڈ فائنل",
            urSummary = "تمام techniques کا epic finale combination۔",
            urDesc = "book کا climax — سب کچھ مل کر unforgettable orgasm experience۔",
            urSteps = listOf(
                "پسندیدہ moves review کریں۔",
                "extended session plan — foreplay سے finale۔",
                "positions بدلتے رہیں۔",
                "grand mutual orgasm — celebration ending۔"
            ),
            urTips = listOf(
                "یہ journey کا end ہے — enjoy کریں۔",
                "feedback لیتے رہیں۔",
                "aftercare نہ بھولیں۔"
            )
        )
    )

    private fun move(
        id: String,
        num: Int,
        categoryId: String,
        difficulty: Difficulty,
        illustrationRes: Int,
        urName: String,
        urSummary: String,
        urDesc: String,
        urSteps: List<String>,
        urTips: List<String>
    ): Posture {
        val category = getCategoryLabel(categoryId)
        val displayName = "$num. $urName"
        return Posture(
            id = id,
            difficulty = difficulty,
            illustrationRes = illustrationRes,
            categoryId = categoryId,
            english = LocalizedContent(
                name = displayName,
                category = category,
                summary = urSummary,
                description = urDesc,
                steps = urSteps,
                tips = urTips
            ),
            urdu = LocalizedContent(
                name = displayName,
                category = category,
                summary = urSummary,
                description = urDesc,
                steps = urSteps,
                tips = urTips
            )
        )
    }
}
