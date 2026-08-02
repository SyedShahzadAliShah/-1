package com.couplesguide.postures.data

import com.couplesguide.postures.R

object RecipeRepository {

    const val CAT_ALL = "all"
    const val CAT_BIRYANI = "biryani"
    const val CAT_BBQ = "bbq"
    const val CAT_KARAHI = "karahi"
    const val CAT_CURRY = "curry"
    const val CAT_APPETIZER = "appetizer"
    const val CAT_SEAFOOD = "seafood"
    const val CAT_DESSERT = "dessert"

    fun getCategoryIds(): List<String> = listOf(
        CAT_ALL, CAT_BIRYANI, CAT_KARAHI, CAT_BBQ, CAT_CURRY,
        CAT_APPETIZER, CAT_SEAFOOD, CAT_DESSERT
    )

    fun getCategoryLabel(categoryId: String, language: String): String {
        val labels = categoryLabels[categoryId] ?: return categoryId
        return if (language == "ur") labels.second else labels.first
    }

    private val categoryLabels = mapOf(
        CAT_ALL to ("All" to "سب"),
        CAT_BIRYANI to ("Biryani & Rice" to "بریانی اور چاول"),
        CAT_BBQ to ("BBQ & Grill" to "باربی کیو"),
        CAT_KARAHI to ("Karahi" to "کڑاہی"),
        CAT_CURRY to ("Curries" to "سالن"),
        CAT_APPETIZER to ("Appetizers" to "اسٹارٹر"),
        CAT_SEAFOOD to ("Seafood" to "سمندری کھانا"),
        CAT_DESSERT to ("Desserts" to "میٹھا")
    )

    fun getRecipesByCategory(categoryId: String): List<Recipe> =
        if (categoryId == CAT_ALL) recipes else recipes.filter { it.categoryId == categoryId }

    fun getRecipeById(id: String): Recipe? = recipes.find { it.id == id }

    fun getAllRecipes(): List<Recipe> = recipes

    private val recipes: List<Recipe> = listOf(
        recipe(
            id = "beef_biryani", categoryId = CAT_BIRYANI, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_beef_biryani, prep = 45, cook = 90, servings = 12,
            enName = "Karachi Beef Biryani", urName = "کراچی بیف بریانی",
            enCat = "Biryani & Rice", urCat = "بریانی اور چاول",
            enSummary = "The crown jewel of Karachi buffets — layered rice with tender beef.",
            urSummary = "کراچی بوفے کی شان — نرم بیف کے ساتھ تہ دار چاول۔",
            enDesc = "Authentic Karachi-style beef biryani with potatoes, fried onions, and aromatic spices. A staple at wedding buffets across the city.",
            urDesc = "اصلی کراچی انداز کی بیف بریانی آلو، فرائی پیاز اور خوشبودار مسالوں کے ساتھ۔ شہر بھر کی شادیوں کے بوفے میں لازمی ڈش۔",
            enIngredients = listOf(
                "1.5 kg beef cubes", "1 kg basmati rice", "4 large potatoes halved",
                "3 cups fried onions", "1 cup yogurt", "Biryani masala 3 tbsp",
                "Whole spices: bay leaf, cloves, cardamom", "Saffron in warm milk",
                "Fresh coriander and mint", "Ghee 1/2 cup"
            ),
            urIngredients = listOf(
                "ڈیڑھ کلو بیف کے ٹکڑے", "۱ کلو باسمتی چاول", "۴ بڑے آلو آدھے",
                "۳ کپ فرائی پیاز", "۱ کپ دہی", "بریانی مسالہ ۳ چمچ",
                "ثابت مسالے: تیز پات، لونگ، الائچی", "زعفران گرم دودھ میں",
                "تازہ دھنیا اور پودینہ", "گھی آدھا کپ"
            ),
            enSteps = listOf(
                "Marinate beef with yogurt, biryani masala, ginger-garlic paste for 2 hours.",
                "Boil rice until 70% cooked; drain and set aside.",
                "Cook marinated beef with potatoes until tender; reduce gravy.",
                "Layer rice over beef, top with fried onions, herbs, saffron milk, and ghee.",
                "Dum on low heat for 25 minutes. Rest 10 minutes before serving."
            ),
            urSteps = listOf(
                "بیف کو دہی، بریانی مسالہ، ادرک لہسن کے پیسٹ میں ۲ گھنٹے میرینیٹ کریں۔",
                "چاول ۷۰ فیصد پکا کر چھان لیں۔",
                "میرینیٹ بیف آلو کے ساتھ نرم ہونے تک پکائیں؛ سالن گاڑھا کریں۔",
                "بیف پر چاول کی تہ، فرائی پیاز، سبزے، زعفران دودھ اور گھی ڈالیں۔",
                "ہلکی آنچ پر ۲۵ منٹ دم دیں۔ پیش کرنے سے ۱۰ منٹ پہلے آرام دیں۔"
            ),
            enTips = listOf(
                "Use aged basmati for long grains.",
                "Do not stir after layering — it breaks the rice.",
                "Serve with raita and shami kebab at Karachi buffets."
            ),
            urTips = listOf(
                "لمبے دانے کے لیے پرانا باسمتی استعمال کریں۔",
                "تہ کے بعد ہلائیں نہیں — چاول ٹوٹ جاتے ہیں۔",
                "کراچی بوفے میں رائتہ اور شامی کباب کے ساتھ پیش کریں۔"
            )
        ),
        recipe(
            id = "chicken_biryani", categoryId = CAT_BIRYANI, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_chicken_biryani, prep = 30, cook = 60, servings = 10,
            enName = "Chicken Tikka Biryani", urName = "چکن ٹکہ بریانی",
            enCat = "Biryani & Rice", urCat = "بریانی اور چاول",
            enSummary = "Smoky tikka pieces layered with fragrant rice.",
            urSummary = "خوشبودار چاول کے ساتھ دھوئیں دار ٹکہ کے ٹکڑے۔",
            enDesc = "A lighter biryani popular at Karachi lunch buffets. Marinated chicken tikka adds a smoky depth to classic biryani layers.",
            urDesc = "کراچی لنچ بوفے میں مقبول ہلکی بریانی۔ میرینیٹ چکن ٹکہ کلاسک تہوں میں دھوئیں کا ذائقہ دیتا ہے۔",
            enIngredients = listOf(
                "1 kg chicken bone-in pieces", "750 g basmati rice", "Tikka masala 2 tbsp",
                "Yogurt 1 cup", "Fried onions 2 cups", "Green chilies 6",
                "Coriander-mint paste", "Lemon juice", "Ghee and oil"
            ),
            urIngredients = listOf(
                "۱ کلو ہڈی والا چکن", "۷۵۰ گرام باسمتی چاول", "ٹکہ مسالہ ۲ چمچ",
                "دہی ۱ کپ", "فرائی پیاز ۲ کپ", "ہری مرچ ۶",
                "دھنیا پودینہ پیسٹ", "لیموں کا رس", "گھی اور تیل"
            ),
            enSteps = listOf(
                "Marinate chicken with tikka masala, yogurt, and lemon for 1 hour.",
                "Grill or pan-sear chicken until charred at edges.",
                "Parboil rice with whole spices; drain.",
                "Layer rice and chicken with fried onions and herbs.",
                "Steam on dum for 20 minutes. Fluff gently and serve."
            ),
            urSteps = listOf(
                "چکن کو ٹکہ مسالہ، دہی اور لیموں میں ۱ گھنٹہ میرینیٹ کریں۔",
                "چکن گرل یا پین میں کناروں پر جلنے تک پکائیں۔",
                "ثابت مسالوں کے ساتھ چاول ادھا پکائیں؛ چھان لیں۔",
                "چاول اور چکن کی تہ فرائی پیاز اور سبزوں کے ساتھ۔",
                "۲۰ منٹ دم پر پکائیں۔ ہلکے ہاتھ سے کھولیں اور پیش کریں۔"
            ),
            enTips = listOf("Char the chicken well for authentic tikka flavor.", "Add a few drops of kewra water for aroma."),
            urTips = listOf("ٹکہ ذائقے کے لیے چکن اچھی طرح بھونیں۔", "خوشبو کے لیے چند قطرے کیوڑا پانی ڈالیں۔")
        ),
        recipe(
            id = "mutton_karahi", categoryId = CAT_KARAHI, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_mutton_karahi, prep = 20, cook = 50, servings = 8,
            enName = "Karachi Mutton Karahi", urName = "کراچی مٹن کڑاہی",
            enCat = "Karahi", urCat = "کڑاہی",
            enSummary = "Tomato-rich karahi with tender mutton — a buffet essential.",
            urSummary = "نرم مٹن والی ٹماٹر بھری کڑاہی — بوفے کی لازمی ڈش۔",
            enDesc = "Cooked in a wok-style karahi with tomatoes, ginger, and green chilies. Found at every major Karachi buffet from Saddar to DHA.",
            urDesc = "کڑاہی میں ٹماٹر، ادرک اور ہری مرچ کے ساتھ پکی۔ صدر سے ڈی ایچ اے تک ہر بڑے کراچی بوفے میں موجود۔",
            enIngredients = listOf("1 kg mutton on bone", "6 tomatoes chopped", "Ginger 2 tbsp", "Garlic 1 tbsp", "Green chilies 8", "Black pepper 1 tsp", "Cumin 1 tsp", "Oil/ghee 1/2 cup", "Fresh coriander"),
            urIngredients = listOf("۱ کلو ہڈی والا مٹن", "۶ ٹماٹر کٹے", "ادرک ۲ چمچ", "لہسن ۱ چمچ", "ہری مرچ ۸", "کالی مرچ ۱ چمچ", "زیرہ ۱ چمچ", "تیل/گھی آدھا کپ", "تازہ دھنیا"),
            enSteps = listOf(
                "Brown mutton in karahi with ginger-garlic.",
                "Add tomatoes; cook until oil separates.",
                "Add spices and slow-cook until mutton is tender.",
                "Finish with black pepper, green chilies, and coriander.",
                "Serve sizzling directly from the karahi."
            ),
            urSteps = listOf(
                "کڑاہی میں ادرک لہسن کے ساتھ مٹن بھونیں۔",
                "ٹماٹر ڈالیں؛ تیل الگ ہونے تک پکائیں۔",
                "مسالے ڈال کر مٹن نرم ہونے تک دم دیں۔",
                "کالی مرچ، ہری مرچ اور دھنیا سے ختم کریں۔",
                "کڑاہی سے ہی گرم گرم پیش کریں۔"
            ),
            enTips = listOf("Use ripe Karachi tomatoes for natural sweetness.", "Do not add water — tomatoes provide moisture."),
            urTips = listOf("قدرتی مٹھاس کے لیے پکے کراچی کے ٹماٹر استعمال کریں۔", "پانی نہ ڈالیں — ٹماٹر نمی دیتے ہیں۔")
        ),
        recipe(
            id = "chicken_karahi", categoryId = CAT_KARAHI, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_chicken_karahi, prep = 15, cook = 35, servings = 8,
            enName = "Chicken Karahi", urName = "چکن کڑاہی",
            enCat = "Karahi", urCat = "کڑاہی",
            enSummary = "Quick-cooking karahi perfect for live buffet stations.",
            urSummary = "لائیو بوفے اسٹیشن کے لیے تیز پکنے والی کڑاہی۔",
            enDesc = "Boneless chicken in a spicy tomato base. Cooks fast and stays popular at Karachi corporate lunch buffets.",
            urDesc = "بغیر ہڈی چکن مسالے دار ٹماٹر میں۔ تیزی سے پکتی ہے اور کراچی کے آفس لنچ بوفے میں مقبول ہے۔",
            enIngredients = listOf("1 kg boneless chicken", "5 tomatoes", "Ginger-garlic paste", "Karahi masala 2 tbsp", "Butter 3 tbsp", "Cream 2 tbsp optional", "Green chilies and coriander"),
            urIngredients = listOf("۱ کلو بون لیس چکن", "۵ ٹماٹر", "ادرک لہسن پیسٹ", "کڑاہی مسالہ ۲ چمچ", "مکھن ۳ چمچ", "کریم ۲ چمچ اختیاری", "ہری مرچ اور دھنیا"),
            enSteps = listOf(
                "Sauté chicken in butter until white.",
                "Add ginger-garlic and karahi masala; cook 2 minutes.",
                "Add chopped tomatoes; cook until thick.",
                "Stir in cream if using. Garnish with chilies and coriander."
            ),
            urSteps = listOf(
                "مکھن میں چکن سفید ہونے تک پکائیں۔",
                "ادرک لہسن اور کڑاہی مسالہ ڈالیں؛ ۲ منٹ پکائیں۔",
                "کٹے ٹماٹر ڈالیں؛ گاڑھا ہونے تک پکائیں۔",
                "چاہیں تو کریم ملائیں۔ مرچ اور دھنیا سے سجائیں۔"
            ),
            enTips = listOf("Cook in batches at buffets to keep it fresh.", "Serve with naan or tandoori roti."),
            urTips = listOf("بوفے میں بیچ میں پکائیں تاکہ تازہ رہے۔", "نان یا تندوری روٹی کے ساتھ پیش کریں۔")
        ),
        recipe(
            id = "seekh_kebab", categoryId = CAT_BBQ, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_seekh_kebab, prep = 40, cook = 20, servings = 10,
            enName = "Seekh Kebab", urName = "سیخ کباب",
            enCat = "BBQ & Grill", urCat = "باربی کیو",
            enSummary = "Minced meat skewers — essential for evening Karachi buffets.",
            urSummary = "قیمے کے سیخ — شام کے کراچی بوفے کی لازمی ڈش۔",
            enDesc = "Spiced minced beef or mutton grilled on skewers. A must-have at BBQ stations from Port Grand to beachside buffets.",
            urDesc = "مسالے دار قیمہ سیخ پر گرل۔ پورٹ گرانڈ سے ساحلی بوفے تک باربی کیو اسٹیشن کی لازمی ڈش۔",
            enIngredients = listOf("1 kg minced beef/mutton", "Onion 1 finely chopped", "Ginger-garlic paste", "Cumin, coriander, garam masala", "Green chilies minced", "Egg 1", "Fat trimmings optional", "Skewers soaked in water"),
            urIngredients = listOf("۱ کلو قیمہ بیف/مٹن", "۱ پیاز باریک", "ادرک لہسن پیسٹ", "زیرہ، دھنیا، گرم مسالہ", "ہری مرچ باریک", "انڈا ۱", "چربی اختیاری", "پانی میں بھگوئی سیخ"),
            enSteps = listOf(
                "Mix mince with all spices, onion, egg. Knead 5 minutes.",
                "Rest mixture 30 minutes in refrigerator.",
                "Mold onto skewers in sausage shapes.",
                "Grill over charcoal, turning until cooked through.",
                "Serve with mint chutney and onion rings."
            ),
            urSteps = listOf(
                "قیمے میں مسالے، پیاز، انڈا ملائیں۔ ۵ منٹ گوندھیں۔",
                "۳۰ منٹ فریج میں آرام دیں۔",
                "سیخ پر ساسیج کی شکل میں لگائیں۔",
                "کوئلے پر پلٹتے ہوئے پکائیں۔",
                "پودینہ چٹنی اور پیاز کے ساتھ پیش کریں۔"
            ),
            enTips = listOf("Wet hands prevent sticking when molding.", "Charcoal gives the best smoky flavor."),
            urTips = listOf("گیلے ہاتھ لگाने میں چپکنے سے بچاتے ہیں۔", "دھوئیں کے لیے کوئلہ بہترین ہے۔")
        ),
        recipe(
            id = "chicken_tikka", categoryId = CAT_BBQ, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_chicken_tikka, prep = 30, cook = 25, servings = 8,
            enName = "Chicken Tikka", urName = "چکن ٹکہ",
            enCat = "BBQ & Grill", urCat = "باربی کیو",
            enSummary = "Classic red tikka from Karachi's BBQ houses.",
            urSummary = "کراچی باربی کیو ہاؤسز کی کلاسک سرخ ٹکہ۔",
            enDesc = "Boneless chicken marinated in yogurt and spices, grilled until charred. Standard at every Karachi buffet BBQ counter.",
            urDesc = "دہی اور مسالوں میں میرینیٹ بون لیس چکن، جلنے تک گرل۔ ہر کراچی بوفے باربی کیو کاؤنٹر پر موجود۔",
            enIngredients = listOf("1 kg boneless chicken cubes", "Yogurt 1 cup", "Tikka masala 3 tbsp", "Kashmiri chili for color", "Lemon juice", "Mustard oil 2 tbsp", "Bell peppers and onion chunks"),
            urIngredients = listOf("۱ کلو چکن کے کیوبز", "دہی ۱ کپ", "ٹکہ مسالہ ۳ چمچ", "کشمیری مرچ رنگ کے لیے", "لیموں کا رس", "سرسوں کا تیل ۲ چمچ", "شملہ مرچ اور پیاز"),
            enSteps = listOf(
                "Marinate chicken 2–4 hours with all ingredients.",
                "Thread onto skewers alternating with peppers and onion.",
                "Grill on high heat, basting with butter.",
                "Serve with lemon wedges and naan."
            ),
            urSteps = listOf(
                "چکن کو ۲–۴ گھنٹے تمام اجزاء میں میرینیٹ کریں۔",
                "شملہ مرچ اور پیاز کے ساتھ سیخ پر لگائیں۔",
                "تیز آنچ پر مکھن لگاتے ہوئے گرل کریں۔",
                "لیموں اور نان کے ساتھ پیش کریں۔"
            ),
            enTips = listOf("Overnight marination deepens flavor.", "Squeeze lemon before eating."),
            urTips = listOf("رات بھر میرینیٹ ذائقہ گہرا کرتا ہے۔", "کھانے سے پہلے لیموں نچوڑیں۔")
        ),
        recipe(
            id = "chapli_kebab", categoryId = CAT_BBQ, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_chapli_kebab, prep = 25, cook = 15, servings = 8,
            enName = "Chapli Kebab", urName = "چپلی کباب",
            enCat = "BBQ & Grill", urCat = "باربی کیو",
            enSummary = "Peshawari-style flat kebabs popular at Karachi buffets.",
            urSummary = "پشاوری انداز کے چپٹے کباب — کراچی بوفے میں مقبول۔",
            enDesc = "Flat minced meat patties with pomegranate seeds and corn flour. Crispy outside, juicy inside.",
            urDesc = "انار دانے اور مکئی کے آٹے والے چپٹے قیمے کے کباب۔ باہر کرکرے، اندر رسیلے۔",
            enIngredients = listOf("750 g minced beef", "Corn flour 2 tbsp", "Pomegranate seeds dried", "Tomato 1 chopped", "Coriander seeds crushed", "Egg 1", "Oil for frying"),
            urIngredients = listOf("۷۵۰ گرام قیمہ", "مکئی کا آٹا ۲ چمچ", "خشک انار دانے", "۱ ٹماٹر", "کچلا ہوا دھنیا", "انڈا ۱", "تلی کے لیے تیل"),
            enSteps = listOf(
                "Mix all ingredients except oil.",
                "Shape into flat patties with a dent in center.",
                "Shallow fry on high heat until crispy both sides.",
                "Drain on paper and serve hot with chutney."
            ),
            urSteps = listOf(
                "تیل کے علاوہ سب ملائیں۔",
                "بیچ میں دھنس کے ساتھ چپٹے کباب بنائیں۔",
                "تیز آنچ پر دونوں طرف کرکرے ہونے تک تلیں۔",
                "کاغذ پر نکالیں اور چٹنی کے ساتھ گرم پیش کریں۔"
            ),
            enTips = listOf("The center dent helps even cooking.", "Serve in pita or with naan."),
            urTips = listOf("بیچ کی دھنس یکساں پکانے میں مدد کرتی ہے۔", "پیٹا یا نان کے ساتھ پیش کریں۔")
        ),
        recipe(
            id = "nihari", categoryId = CAT_CURRY, difficulty = Difficulty.ADVANCED,
            illustrationRes = R.drawable.pic_nihari, prep = 30, cook = 360, servings = 10,
            enName = "Beef Nihari", urName = "بیف نہاری",
            enCat = "Curries", urCat = "سالن",
            enSummary = "Slow-cooked breakfast classic adapted for buffet service.",
            urSummary = "آہستہ پکی ناشتے کی کلاسک — بوفے سروس کے لیے۔",
            enDesc = "Originally a Karachi breakfast dish, nihari now appears at brunch buffets. Rich, slow-cooked beef shank in spiced flour gravy.",
            urDesc = "اصل میں کراچی کا ناشتے کا کھانا، اب برنچ بوفے میں۔ مسالے دار آٹے کے سالن میں آہستہ پکا بیف۔",
            enIngredients = listOf("1.5 kg beef shank", "Nihari masala 4 tbsp", "Wheat flour 4 tbsp roasted", "Ghee 1/2 cup", "Ginger julienne", "Lemon", "Fresh coriander"),
            urIngredients = listOf("ڈیڑھ کلو بیف شانک", "نہاری مسالہ ۴ چمچ", "بھuna ہوا گندم آٹا ۴ چمچ", "گھی آدھا کپ", "ادرک کی سلائیاں", "لیموں", "تازہ دھنیا"),
            enSteps = listOf(
                "Slow-cook beef with nihari masala and water 5–6 hours.",
                "Make slurry with roasted flour; add to thicken.",
                "Simmer until meat falls off bone.",
                "Temper with ghee and serve with ginger, lemon, naan."
            ),
            urSteps = listOf(
                "بیف نہاری مسالے اور پانی میں ۵–۶ گھنٹے دم پر پکائیں۔",
                "بھune آٹے کی slurry ڈال کر گاڑھا کریں۔",
                "گوشت ہڈی سے الگ ہونے تک پکائیں۔",
                "گھی کی تڑکا لگائیں؛ ادرک، لیموں، نان کے ساتھ پیش کریں۔"
            ),
            enTips = listOf("Start nihari the night before for buffets.", "Keep warm in a slow cooker."),
            urTips = listOf("بوفے کے لیے نہاری رات سے شروع کریں۔", "سست پکانے والے برتن میں گرم رکھیں۔")
        ),
        recipe(
            id = "haleem", categoryId = CAT_CURRY, difficulty = Difficulty.ADVANCED,
            illustrationRes = R.drawable.pic_haleem, prep = 60, cook = 300, servings = 15,
            enName = "Beef Haleem", urName = "بیف حلیم",
            enCat = "Curries", urCat = "سالن",
            enSummary = "Ramadan and wedding buffet favorite across Karachi.",
            urSummary = "کراچی بھر میں رمضان اور شادی بوفے کی پسندیدہ ڈش۔",
            enDesc = "A thick porridge of wheat, lentils, and shredded beef. Topped with fried onions, lemon, and coriander at the buffet station.",
            urDesc = "گندم، دال اور ریشہ دار بیف کا گاڑھا شوربہ۔ بوفے پر فرائی پیاز، لیموں اور دھنیا سے سجایا جاتا ہے۔",
            enIngredients = listOf("500 g beef", "Wheat 1 cup", "Mixed lentils 1 cup", "Haleem masala", "Fried onions", "Ginger-garlic", "Ghee for tempering"),
            urIngredients = listOf("۵۰۰ گرام بیف", "گندم ۱ کپ", "مخلوط دال ۱ کپ", "حلیم مسالہ", "فرائی پیاز", "ادرک لہسن", "تڑکے کے لیے گھی"),
            enSteps = listOf(
                "Soak wheat and lentils overnight.",
                "Pressure-cook beef until very tender; shred.",
                "Cook grains with beef and masala until mushy.",
                "Blend partially for smooth texture.",
                "Temper with ghee, fried onions; serve with garnishes."
            ),
            urSteps = listOf(
                "گندم اور دال رات بھر بھگوئیں۔",
                "بیف پریشر میں بہت نرم پکائیں؛ ریشہ کریں۔",
                "اناج بیف اور مسالے کے ساتھ پکائیں۔",
                "ہموار ٹیکسچر کے لیے جزوی بلینڈ کریں۔",
                "گھی، فرائی پیاز کی تڑکا؛ سجاوٹ کے ساتھ پیش کریں۔"
            ),
            enTips = listOf("Stir constantly in the last hour to prevent sticking.", "Add bone marrow for richness."),
            urTips = listOf("آخری گھنٹے مسلسل ہلائیں۔", "چربے کے لیے ہڈی کا گودا ڈالیں۔")
        ),
        recipe(
            id = "aloo_gosht", categoryId = CAT_CURRY, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_aloo_gosht, prep = 15, cook = 60, servings = 8,
            enName = "Aloo Gosht", urName = "آلو گوشت",
            enCat = "Curries", urCat = "سالن",
            enSummary = "Comfort curry staple at family buffets.",
            urSummary = "خاندانی بوفے کی آرام دہ سالن ڈش۔",
            enDesc = "Mutton and potato curry in a home-style masala. Reliable crowd-pleaser at Karachi home buffets.",
            urDesc = "گھر کے انداز میں مٹن اور آلو کا سالن۔ کراچی گھریلو بوفے میں ہر کسی کی پسند۔",
            enIngredients = listOf("750 g mutton", "4 potatoes", "Onion 2", "Tomato 2", "Ginger-garlic", "Red chili, turmeric, coriander powder"),
            urIngredients = listOf("۷۵۰ گرام مٹن", "۴ آلو", "۲ پیاز", "۲ ٹماٹر", "ادرک لہسن", "لال مرچ، ہلدی، دھنیا پاؤڈر"),
            enSteps = listOf(
                "Brown onions; add ginger-garlic and spices.",
                "Add mutton; cook until color changes.",
                "Add tomatoes and potatoes with water.",
                "Simmer until mutton and potatoes are tender."
            ),
            urSteps = listOf(
                "پیاز بھونیں؛ ادرک لہسن اور مسالے ڈالیں۔",
                "مٹن ڈالیں؛ رنگ بدلنے تک پکائیں۔",
                "ٹماٹر، آلو اور پانی ڈالیں۔",
                "مٹن اور آلو نرم ہونے تک دم دیں۔"
            ),
            enTips = listOf("Use waxy potatoes so they hold shape.", "Serve with tandoori roti."),
            urTips = listOf("آلو کی شکل برقرار رہے اس لیے صحیح قسم کے آلو لیں۔", "تندوری روٹی کے ساتھ پیش کریں۔")
        ),
        recipe(
            id = "daal_chawal", categoryId = CAT_CURRY, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_daal_chawal, prep = 10, cook = 45, servings = 10,
            enName = "Daal Chawal", urName = "دال چاول",
            enCat = "Curries", urCat = "سالن",
            enSummary = "Simple lentil and rice — essential buffet filler.",
            urSummary = "سادہ دال چاول — بوفے کی بنیادی ڈش۔",
            enDesc = "Masoor or moong daal with steamed basmati rice. Budget-friendly and beloved at Karachi community buffets.",
            urDesc = "مسور یا مونگ دال بھاپ میں پکے باسمتی چاول کے ساتھ۔ کراچی کمیونٹی بوفے کی سستی اور پسندیدہ ڈش۔",
            enIngredients = listOf("2 cups masoor daal", "1 kg basmati rice", "Cumin, garlic, dried red chili", "Ghee", "Onion for tadka"),
            urIngredients = listOf("۲ کپ مسور دال", "۱ کلو باسمتی چاول", "زیرہ، لہسن، خشک لال مرچ", "گھی", "تڑکے کے لیے پیاز"),
            enSteps = listOf(
                "Boil daal with turmeric and salt until soft.",
                "Cook rice separately with whole spices.",
                "Temper daal with ghee, cumin, garlic, and fried onion.",
                "Serve daal over rice or side by side."
            ),
            urSteps = listOf(
                "دال ہلدی نمک کے ساتھ نرم ہونے تک ابالیں۔",
                "چاول الگ ثابت مسالوں کے ساتھ پکائیں۔",
                "دال میں گھی، زیرہ، لہسن، فرائی پیاز کی تڑکا لگائیں۔",
                "دال چاول پر یا ساتھ پیش کریں۔"
            ),
            enTips = listOf("A squeeze of lemon brightens the daal.", "Pair with achaar at buffets."),
            urTips = listOf("لیموں کا رس دال کو تازہ بناتا ہے۔", "بوفے میں اچار کے ساتھ پیش کریں۔")
        ),
        recipe(
            id = "fried_fish", categoryId = CAT_SEAFOOD, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_fried_fish, prep = 30, cook = 20, servings = 8,
            enName = "Karachi Fried Fish", urName = "کراچی فرائی فش",
            enCat = "Seafood", urCat = "سمندری کھانا",
            enSummary = "Crispy spiced fish from Karachi's coastal buffets.",
            urSummary = "کراچی ساحلی بوفے کی مسالے دار کرکرے مچھلی۔",
            enDesc = "Fresh pomfret or surmai coated in spiced gram flour and deep-fried. A highlight at seafood buffets near Kemari and Clifton.",
            urDesc = "تازہ پاپلیٹ یا سرمئی کو مسالے دار بیسن میں لپیٹ کر تلی۔ کیماڑی اور کلِفٹن کے سمندری بوفے کی خاص ڈش۔",
            enIngredients = listOf("1 kg fish fillets", "Gram flour 1 cup", "Ajwain, red chili, turmeric", "Lemon juice", "Oil for deep frying", "Chat masala for serving"),
            urIngredients = listOf("۱ کلو مچھلی فلیٹ", "بیسن ۱ کپ", "اجوائن، لال مرچ، ہلدی", "لیموں کا رس", "تلی کے لیے تیل", "چاٹ مسالہ"),
            enSteps = listOf(
                "Marinate fish with lemon and spices 20 minutes.",
                "Coat in seasoned gram flour batter.",
                "Deep fry until golden and crispy.",
                "Drain and sprinkle chat masala. Serve with raita."
            ),
            urSteps = listOf(
                "مچھلی لیموں اور مسالوں میں ۲۰ منٹ میرینیٹ کریں۔",
                "مسالے دار بیسن میں کوٹ کریں۔",
                "سنہری کرکرے ہونے تک تلیں۔",
                "نکالیں، چاٹ مسالہ چھڑکیں۔ رائتہ کے ساتھ پیش کریں۔"
            ),
            enTips = listOf("Use very hot oil for a crisp crust.", "Serve immediately — fish softens when held."),
            urTips = listOf("کرکرے crust کے لیے بہت گرم تیل استعمال کریں۔", "فوراً پیش کریں — دیر سے نرم ہو جاتی ہے۔")
        ),
        recipe(
            id = "prawn_masala", categoryId = CAT_SEAFOOD, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_prawn_masala, prep = 20, cook = 25, servings = 6,
            enName = "Prawn Masala", urName = "جھینگا مسالا",
            enCat = "Seafood", urCat = "سمندری کھانا",
            enSummary = "Spicy prawn curry for premium Karachi buffets.",
            urSummary = "پریمیم کراچی بوفے کے لیے مسالے دار جھینگے۔",
            enDesc = "Jumbo prawns in onion-tomato masala. Popular at hotel buffets along Shahrah-e-Faisal and the beach.",
            urDesc = "بڑے جھینگے پیاز ٹماٹر مسالے میں۔ شاہراہ فیصل اور ساحل کے ہوٹل بوفے میں مقبول۔",
            enIngredients = listOf("750 g jumbo prawns cleaned", "Onion 2", "Tomato 3", "Ginger-garlic", "Coconut milk optional", "Curry leaves", "Kashmiri chili"),
            urIngredients = listOf("۷۵۰ گرام صاف جھینگے", "۲ پیاز", "۳ ٹماٹر", "ادرک لہسن", "ناریل کا دودھ اختیاری", "کری پتے", "کشمیری مرچ"),
            enSteps = listOf(
                "Sauté onions until golden; add ginger-garlic.",
                "Add tomatoes and spices; cook to thick masala.",
                "Add prawns; cook 5–7 minutes until pink.",
                "Finish with curry leaves and coriander."
            ),
            urSteps = listOf(
                "پیاز سنہری ہونے تک بھونیں؛ ادرک لہسن ڈالیں۔",
                "ٹماٹر اور مسالے؛ گاڑھا مسالہ بنائیں۔",
                "جھینگے ڈالیں؛ گلابی ہونے تک ۵–۷ منٹ پکائیں۔",
                "کری پتے اور دھنیا سے ختم کریں۔"
            ),
            enTips = listOf("Do not overcook prawns — they turn rubbery.", "Add coconut milk for a milder coastal version."),
            urTips = listOf("جھینگے زیادہ نہ پکائیں — سخت ہو جاتے ہیں۔", "ہلکے ساحلی ذائقے کے لیے ناریل کا دودھ ڈالیں۔")
        ),
        recipe(
            id = "samosa_chaat", categoryId = CAT_APPETIZER, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_samosa_chaat, prep = 20, cook = 10, servings = 8,
            enName = "Samosa Chaat", urName = "سموسہ چاٹ",
            enCat = "Appetizers", urCat = "اسٹارٹر",
            enSummary = "Crushed samosas with chutneys — buffet starter favorite.",
            urSummary = "توڑے سموسے چٹنیوں کے ساتھ — بوفے اسٹارٹر کی پسند۔",
            enDesc = "Store-bought or homemade samosas crushed and topped with yogurt, tamarind chutney, and sev. Opens every Karachi buffet.",
            urDesc = "بازار یا گھر کے سموسے توڑ کر دہی، املی چٹنی اور سیو سے سجائے۔ ہر کراچی بوفے کی شروعات۔",
            enIngredients = listOf("12 samosas", "Yogurt whisked", "Tamarind chutney", "Green chutney", "Sev", "Chaat masala", "Onion and coriander"),
            urIngredients = listOf("۱۲ سموسے", "پھینٹی دہی", "املی چٹنی", "ہری چٹنی", "سیو", "چاٹ مسالہ", "پیاز اور دھنیا"),
            enSteps = listOf(
                "Warm samosas and break into a serving platter.",
                "Drizzle yogurt and both chutneys.",
                "Top with sev, onion, coriander, and chaat masala.",
                "Serve immediately while samosas are crisp."
            ),
            urSteps = listOf(
                "سموسے گرم کر کے پلیٹ میں توڑیں۔",
                "دہی اور دونوں چٹنیاں ڈالیں۔",
                "سیو، پیاز، دھنیا، چاٹ مسالہ سے سجائیں۔",
                "سموسے کرکرے ہوں تو فوراً پیش کریں۔"
            ),
            enTips = listOf("Set up a live chaat station at buffets.", "Offer mild and spicy chutney options."),
            urTips = listOf("بوفے میں لائیو چاٹ اسٹیشن رکھیں۔", "ہلکی اور تیز چٹنی دونوں رکھیں۔")
        ),
        recipe(
            id = "dahi_bhalla", categoryId = CAT_APPETIZER, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_dahi_bhalla, prep = 30, cook = 20, servings = 8,
            enName = "Dahi Bhalla", urName = "دہی بھلے",
            enCat = "Appetizers", urCat = "اسٹارٹر",
            enSummary = "Soft lentil dumplings in yogurt — Ramadan buffet classic.",
            urSummary = "دہی میں نرم دال کے بھلے — رمضان بوفے کی کلاسک۔",
            enDesc = "Urda daal fritters soaked and served in spiced yogurt with chutneys. Essential at Karachi iftar buffets.",
            urDesc = "ارہڑ دال کے پکوڑے دہی میں مسالے دار چٹنیوں کے ساتھ۔ کراچی افطار بوفے کی لازمی ڈش۔",
            enIngredients = listOf("Urad daal 1 cup soaked", "Yogurt 2 cups", "Roasted cumin", "Red chili powder", "Tamarind and green chutney", "Papri optional"),
            urIngredients = listOf("۱ کپ بھگوئی ارہڑ دال", "۲ کپ دہی", "بھuna زیرہ", "لال مرچ پاؤڈر", "املی اور ہری چٹنی", "پپڑی اختیاری"),
            enSteps = listOf(
                "Grind daal to thick batter; fry walnut-sized balls.",
                "Soak fried bhallas in warm water 15 minutes; squeeze gently.",
                "Whisk yogurt with cumin, salt, and chili.",
                "Arrange bhallas in yogurt; top with chutneys."
            ),
            urSteps = listOf(
                "دال پیس کر گاڑھی batter؛ اخروٹ جتنے پکوڑے تلیں۔",
                "بھلے گرم پانی میں ۱۵ منٹ بھگوئیں؛ ہلکے نچوڑیں۔",
                "دہی میں زیرہ، نمک، مرچ ملائیں۔",
                "بھلے دہی میں رکھیں؛ چٹنیوں سے سجائیں۔"
            ),
            enTips = listOf("Make bhallas a day ahead and refrigerate.", "Squeeze well so yogurt absorbs."),
            urTips = listOf("بھلے ایک دن پہلے بنا کر فریج میں رکھیں۔", "اچھی طرح نچوڑیں تاکہ دہی جذب ہو۔")
        ),
        recipe(
            id = "raita", categoryId = CAT_APPETIZER, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_raita, prep = 10, cook = 0, servings = 10,
            enName = "Boondi Raita", urName = "بوندی رائتہ",
            enCat = "Appetizers", urCat = "اسٹارٹر",
            enSummary = "Cooling yogurt side for biryani and BBQ buffets.",
            urSummary = "بریانی اور باربی کیو بوفے کے لیے ٹھنڈا دہی کا سائڈ۔",
            enDesc = "Thick yogurt with boondi, cumin, and mint. Served alongside every rice and grilled dish at Karachi buffets.",
            urDesc = "گاڑھی دہی بوندی، زیرہ اور پودینے کے ساتھ۔ کراچی بوفے میں ہر چاول اور گرل ڈش کے ساتھ۔",
            enIngredients = listOf("Yogurt 1 kg", "Boondi 1 cup", "Roasted cumin", "Salt", "Mint leaves", "Black salt optional"),
            urIngredients = listOf("۱ کلو دہی", "بوندی ۱ کپ", "بھuna زیرہ", "نمک", "پودینہ", "کالا نمک اختیاری"),
            enSteps = listOf(
                "Whisk yogurt smooth with salt and cumin.",
                "Soak boondi 5 minutes; squeeze lightly.",
                "Fold boondi and chopped mint into yogurt.",
                "Chill until serving."
            ),
            urSteps = listOf(
                "دہی نمک زیرے کے ساتھ پھینٹیں۔",
                "بوندی ۵ منٹ بھگوئیں؛ ہلکا نچوڑیں۔",
                "بوندی اور کٹا پودینہ دہی میں ملائیں۔",
                "پیش کرنے تک ٹھنڈا رکھیں۔"
            ),
            enTips = listOf("Keep refrigerated on the buffet line.", "Add cucumber for a fresher variant."),
            urTips = listOf("بوفے لائن پر فریج میں رکھیں۔", "تازگی کے لیے کھیرا ڈالیں۔")
        ),
        recipe(
            id = "gulab_jamun", categoryId = CAT_DESSERT, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_gulab_jamun, prep = 25, cook = 30, servings = 12,
            enName = "Gulab Jamun", urName = "گلاب جامن",
            enCat = "Desserts", urCat = "میٹھا",
            enSummary = "Syrup-soaked milk dumplings — every buffet's sweet finale.",
            urSummary = "شربت میں ڈوبے دودھ کے گولے — ہر بوفے کا میٹھا اختتام۔",
            enDesc = "Soft khoya balls fried and soaked in cardamom sugar syrup. The most requested dessert at Karachi wedding buffets.",
            urDesc = "نرم کھویا کے گولے تل کر الائچی شربت میں بھگوئے۔ کراچی شادی بوفے میں سب سے زیادہ مانگی جانے والی میٹھائی۔",
            enIngredients = listOf("Khoya 250 g", "Maida 3 tbsp", "Baking soda pinch", "Sugar 2 cups", "Water 2 cups", "Cardamom", "Rose water"),
            urIngredients = listOf("کھویا ۲۵۰ گرام", "میدہ ۳ چمچ", "چٹکی بیکنگ سوڈا", "چینی ۲ کپ", "پانی ۲ کپ", "الائچی", "گلاب جل"),
            enSteps = listOf(
                "Knead khoya with maida and soda into smooth dough.",
                "Roll small balls; fry on low until golden brown.",
                "Make sugar syrup with cardamom and rose water.",
                "Soak warm jamuns in warm syrup 2 hours."
            ),
            urSteps = listOf(
                "کھویا میدہ سوڈا مل کر ہموار آٹا گوندھیں۔",
                "چھوٹے گولے بنائیں؛ ہلکی آنچ پر سنہری تلیں۔",
                "الائچی گلاب جل والا شربت بنائیں۔",
                "گرم جامن گرم شربت میں ۲ گھنٹے بھگوئیں۔"
            ),
            enTips = listOf("Oil must be low heat — high heat leaves raw centers.", "Serve slightly warm at buffets."),
            urTips = listOf("تیل ہلکی آنچ پر — تیز آنچ سے اندر کچا رہ جاتا ہے۔", "بوفے میں ہلکا گرم پیش کریں۔")
        ),
        recipe(
            id = "kheer", categoryId = CAT_DESSERT, difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.pic_kheer, prep = 10, cook = 60, servings = 10,
            enName = "Chawal Ki Kheer", urName = "چاول کی کھیر",
            enCat = "Desserts", urCat = "میٹھا",
            enSummary = "Creamy rice pudding served at every Karachi celebration.",
            urSummary = "ملائ دار چاول کی کھیر — ہر کراچی تقریب میں۔",
            enDesc = "Slow-cooked basmati rice in milk with cardamom, saffron, and nuts. A buffet dessert that never goes out of style.",
            urDesc = "باسمتی چاول دودھ میں الائچی، زعفران اور خشک میووں کے ساتھ۔ کبھی فیشن سے باہر نہ ہونے والی بوفے میٹھائی۔",
            enIngredients = listOf("1/2 cup basmati rice", "1.5 liters milk", "Sugar 3/4 cup", "Cardamom", "Saffron", "Almonds and pistachios"),
            urIngredients = listOf("آدھا کپ باسمتی چاول", "ڈیڑھ لیٹر دودھ", "چینی تین چوتھائی کپ", "الائچی", "زعفران", "بادام اور پستہ"),
            enSteps = listOf(
                "Wash rice; boil in milk on low heat.",
                "Stir frequently until rice breaks down and thickens.",
                "Add sugar, cardamom, saffron.",
                "Garnish with nuts. Serve chilled or warm."
            ),
            urSteps = listOf(
                "چاول دھوئیں؛ ہلکی آنچ پر دودھ میں پکائیں۔",
                "چاول گلنے اور گاڑھا ہونے تک ہلاتے رہیں۔",
                "چینی، الائچی، زعفران ڈالیں۔",
                "میوے سے سجائیں۔ ٹھنڈا یا گرم پیش کریں۔"
            ),
            enTips = listOf("Use a heavy pot to prevent scorching.", "Kheer thickens as it cools."),
            urTips = listOf("جلنے سے بچنے کے لیے بھاری برتن استعمال کریں۔", "ٹھنڈا ہونے پر کھیر گاڑھی ہوتی ہے۔")
        ),
        recipe(
            id = "zarda", categoryId = CAT_DESSERT, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_zarda, prep = 20, cook = 45, servings = 10,
            enName = "Meetha Zarda", urName = "میٹھا زردہ",
            enCat = "Desserts", urCat = "میٹھا",
            enSummary = "Golden sweet rice with nuts — wedding buffet tradition.",
            urSummary = "سنہری میٹھے چاول میووں کے ساتھ — شادی بوفے کی روایت۔",
            enDesc = "Saffron-tinted sweet rice with raisins, coconut, and nuts. A celebratory dessert at Karachi nikah and walima buffets.",
            urDesc = "زعفرانی میٹھے چاول کشمش، ناریل اور میووں کے ساتھ۔ کراچی نکاح اور ولیمہ بوفے کی تقریبی میٹھائی۔",
            enIngredients = listOf("2 cups basmati rice", "Sugar 1.5 cups", "Ghee 1/2 cup", "Saffron", "Raisins", "Coconut flakes", "Mixed nuts", "Cardamom"),
            urIngredients = listOf("۲ کپ باسمتی چاول", "چینی ڈیڑھ کپ", "گھی آدھا کپ", "زعفران", "کشمش", "ناریل", "مخلوط میوے", "الائچی"),
            enSteps = listOf(
                "Boil rice with saffron until 80% done; drain.",
                "In ghee, sauté nuts, raisins, and coconut.",
                "Layer rice with sugar and nut mixture.",
                "Dum on low 20 minutes. Fluff and serve."
            ),
            urSteps = listOf(
                "چاول زعفران میں ۸۰ فیصد پکائیں؛ چھان لیں۔",
                "گھی میں میوے، کشمش، ناریل بھونیں۔",
                "چاول چینی اور میووں کی تہ بنائیں۔",
                "۲۰ منٹ دم دیں۔ کھولیں اور پیش کریں۔"
            ),
            enTips = listOf("Use orange food color if saffron is limited.", "Serve warm for best aroma."),
            urTips = listOf("زعفران کم ہو تو نارنجی رنگ استعمال کریں۔", "خوشبو کے لیے گرم پیش کریں۔")
        ),
        recipe(
            id = "gajar_halwa", categoryId = CAT_DESSERT, difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.pic_gajar_halwa, prep = 15, cook = 60, servings = 8,
            enName = "Gajar Ka Halwa", urName = "گاجر کا حلوہ",
            enCat = "Desserts", urCat = "میٹھا",
            enSummary = "Winter carrot pudding — popular at Karachi winter buffets.",
            urSummary = "سردیوں کا گاجر کا حلوہ — کراچی سردی بوفے میں مقبول۔",
            enDesc = "Grated red carrots slow-cooked in milk and khoya. A seasonal favorite when Karachi carrots are at their sweetest.",
            urDesc = "کٹی لال گاجر دودھ کھویا میں آہستہ پکی۔ کراچی کی میٹھی گاجر کے موسم کی پسندیدہ میٹھائی۔",
            enIngredients = listOf("1 kg carrots grated", "1 liter milk", "Khoya 150 g", "Sugar 1 cup", "Ghee 4 tbsp", "Cardamom", "Almonds"),
            urIngredients = listOf("۱ کلو کٹی گاجر", "۱ لیٹر دودھ", "کھویا ۱۵۰ گرام", "چینی ۱ کپ", "گھی ۴ چمچ", "الائچی", "بادام"),
            enSteps = listOf(
                "Cook carrots in milk until milk evaporates.",
                "Add khoya, sugar, and ghee.",
                "Stir on medium heat until halwa leaves the pan.",
                "Garnish with cardamom and almonds."
            ),
            urSteps = listOf(
                "گاجر دودھ میں پکائیں جب تک دودھ خشک نہ ہو۔",
                "کھویا، چینی، گھی ڈالیں۔",
                "درمیانی آنچ پر ہلائیں جب تک حلوہ پین سے الگ نہ ہو۔",
                "الائچی بادام سے سجائیں۔"
            ),
            enTips = listOf("Use red Karachi carrots for best color.", "Can be made ahead and reheated."),
            urTips = listOf("بہتر رنگ کے لیے لال کراچی گاجر لیں۔", "پہلے سے بنا کر گرم کیا جا سکتا ہے۔")
        )
    )

    private fun recipe(
        id: String,
        categoryId: String,
        difficulty: Difficulty,
        illustrationRes: Int,
        prep: Int,
        cook: Int,
        servings: Int,
        enName: String,
        urName: String,
        enCat: String,
        urCat: String,
        enSummary: String,
        urSummary: String,
        enDesc: String,
        urDesc: String,
        enIngredients: List<String>,
        urIngredients: List<String>,
        enSteps: List<String>,
        urSteps: List<String>,
        enTips: List<String>,
        urTips: List<String>
    ) = Recipe(
        id = id,
        categoryId = categoryId,
        difficulty = difficulty,
        illustrationRes = illustrationRes,
        prepMinutes = prep,
        cookMinutes = cook,
        servings = servings,
        english = RecipeLocalizedContent(enName, enCat, enSummary, enDesc, enIngredients, enSteps, enTips),
        urdu = RecipeLocalizedContent(urName, urCat, urSummary, urDesc, urIngredients, urSteps, urTips)
    )
}
