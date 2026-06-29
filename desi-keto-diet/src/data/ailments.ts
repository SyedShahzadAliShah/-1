import type { AilmentGuide } from '../types';

export const ailmentGuides: AilmentGuide[] = [
  {
    id: 'gastric',
    title: { en: 'Gastric & Digestive Health', ur: 'معدہ و ہاضمہ کی صحت' },
    summary: {
      en: 'GERD, IBS, acidity, bloating, and leaky gut respond powerfully to ketogenic anti-inflammatory nutrition. Reducing refined carbs and inflammatory seed oils while emphasizing bone broth, fermented foods, and gentle spices can reverse years of antacid dependency.',
      ur: 'GERD، IBS، تیزابیت، پھولاؤ، اور لیکی گٹ کیٹوجینک سوزش مخالف غذائیت سے بہتر ہوتے ہیں۔ ریفائنڈ کاربس اور سوزش والی تیلیں کم کر کے ہڈی کا شوربہ، خمیر شدہ غذائیں، اور ہلکی مصالحے استعمال کرنے سے سالوں کی اینٹاسیڈ کی عادت ختم ہو سکتی ہے۔',
    },
    ketoApproach: {
      en: 'Target under 25g net carbs daily. Use coconut oil and ghee instead of vegetable oils. Bone broth (yakhni) heals gut lining. Add ginger, fennel (saunf), and ajwain for digestion. Eliminate wheat roti — use almond or coconut flour alternatives. Intermittent fasting (16:8) gives digestive rest.',
      ur: 'روزانہ 25 گرام نیٹ کاربس سے کم رکھیں۔ سبزی تیل کی بجائے ناریل کا تیل اور گھی استعمال کریں۔ ہڈی کا شوربہ (یخنی) آنتوں کی تہہ کو ٹھیک کرتا ہے۔ ہاضمے کے لیے ادرک، سونف، اور اجوائن شامل کریں۔ گندم کی روٹی چھوڑیں — بادام یا ناریل کے آٹے کے متبادل استعمال کریں۔ وقفے وقفے سے روزہ (16:8) ہاضمے کو آرام دیتا ہے۔',
    },
    foodsToEat: [
      { en: 'Bone broth (desi yakhni) — collagen heals gut lining', ur: 'ہڈی کا شوربہ (دیسی یخنی) — کولیجن آنتوں کی تہہ کو ٹھیک کرتا ہے' },
      { en: 'Fermented raita with full-fat yogurt and probiotics', ur: 'مکمل چکنائی والی دہی سے خمیر شدہ رائتہ اور پروبایوٹکس' },
      { en: 'Ginger-garlic paste, turmeric, cumin (zeera)', ur: 'ادرک لہسن پیسٹ، ہلدی، زیرہ' },
      { en: 'Leafy greens: spinach (palak), fenugreek (methi)', ur: 'پتہ دار سبزیاں: پالک، میتھی' },
      { en: 'Coconut, almonds, walnuts — healthy fats soothe inflammation', ur: 'ناریل، بادام، اخروٹ — صحت مند چکنائیاں سوزش کم کرتی ہیں' },
    ],
    foodsToAvoid: [
      { en: 'Refined wheat (maida), white rice, sugary chai', ur: 'ریفائنڈ گندم (میدہ)، سفید چاول، میٹھی چائے' },
      { en: 'Deep-fried pakoras, samosas in vegetable oil', ur: 'سبزی تیل میں تلے پکوڑے، سموسے' },
      { en: 'Carbonated drinks and commercial antacids long-term', ur: 'کاربونیٹڈ مشروبات اور تجارتی اینٹاسیڈز طویل مدت' },
      { en: 'Excess red chili causing gastric erosion', ur: 'زیادہ لال مرچ جو معدے کو نقصان پہنچائے' },
    ],
    lifestyleTips: [
      { en: 'Eat slowly, chew 20+ times — desi wisdom of mindful eating', ur: 'آہستہ کھائیں، 20+ بار چبائیں — سوچ سمجھ کر کھانے کی دیسی حکمت' },
      { en: 'Walk 15 minutes after meals (chaal maarna)', ur: 'کھانے کے بعد 15 منٹ چلیں' },
      { en: 'Sleep on left side to reduce acid reflux', ur: 'تیزابیت کم کرنے کے لیے بائیں کروٹ سوئیں' },
      { en: 'Practice diaphragmatic breathing to reduce stress-related acidity', ur: 'تناؤ سے تیزابیت کم کرنے کے لیے ڈایافرام کی سانس لیں' },
    ],
    medicationAlternatives: {
      en: 'Instead of daily PPIs (omeprazole) or antacids: Start with 1 tbsp apple cider vinegar before meals (paradoxically reduces acidity), slippery elm tea, and licorice root (mulethi) under supervision. Keto eliminates the carb fermentation that drives most bloating. Many patients reduce PPIs within 4-8 weeks under medical guidance.',
      ur: 'روزانہ PPIs (اومپرازول) یا اینٹاسیڈز کی بجائے: کھانے سے پہلے 1 چمچ سیب کا سرکہ (عجیب طور پر تیزابیت کم کرتا ہے)، سلپری ایلم چائے، اور نگرانی میں ملیٹھی۔ کیٹو کارب خمیر کاری ختم کرتا ہے جو زیادہ تر پھولاؤ کا سبب ہے۔ بہت سے مریض 4-8 ہفتوں میں ڈاکٹر کی نگرانی میں PPIs کم کرتے ہیں۔',
    },
  },
  {
    id: 'gyne',
    title: { en: 'Gynecological & Hormonal Balance', ur: 'نسائی و ہارمونل توازن' },
    summary: {
      en: 'PCOS, irregular cycles, endometriosis, and menopausal symptoms improve dramatically on keto. Insulin resistance drives 70% of PCOS cases — cutting carbs restores ovulation and reduces androgen excess naturally.',
      ur: 'PCOS، بے قاعدہ ماہواری، اینڈومیٹریوسس، اور مینوپاز کی علامات کیٹو پر بہت بہتر ہوتی ہیں۔ انسولن مزاحمت PCOS کے 70% کیسز کی وجہ ہے — کاربس کم کرنے سے قدرتی طور پر بیضہ دانی بحال اور اینڈروجن کم ہوتا ہے۔',
    },
    ketoApproach: {
      en: 'Keep carbs under 20g for PCOS. Prioritize omega-3 from fish (rohu, salmon), flaxseed (alsi), and walnuts. Include cinnamon (dalchini) and fenugreek seeds for insulin sensitivity. Avoid soy-heavy processed foods. Seed cycling with pumpkin and flax seeds supports cycle regulation.',
      ur: 'PCOS کے لیے کاربس 20 گرام سے کم رکھیں۔ مچھلی (روہو، سامن)، السی، اور اخروٹ سے اومیگا-3 کو ترجیح دیں۔ انسولن حساسیت کے لیے دار چینی اور میتھی کے بیج شامل کریں۔ سویا والے پروسیسڈ کھانوں سے بچیں۔ کدو اور السی کے بیج سائیکلنگ سے ماہواری منظم ہوتی ہے۔',
    },
    foodsToEat: [
      { en: 'Fatty fish: rohu, salmon, mackerel — anti-inflammatory omega-3', ur: 'چکنائی والی مچھلی: روہو، سامن — سوزش مخالف اومیگا-3' },
      { en: 'Flaxseed (alsi) and chia — lignans balance estrogen', ur: 'السی اور چیا — لگننس ایسٹروجن متوازن کرتے ہیں' },
      { en: 'Cruciferous vegetables: cauliflower, broccoli — estrogen metabolism', ur: 'گوبھی، بروکولی — ایسٹروجن میٹابولزم' },
      { en: 'Full-fat dairy: paneer, desi ghee in moderation', ur: 'مکمل چکنائی والی دہی مصنوعات: پنیر، دیسی گھی اعتدال میں' },
    ],
    foodsToAvoid: [
      { en: 'Sugar, jalebi, gulab jamun — spike insulin and worsen PCOS', ur: 'چینی، جلیبی، گلاب جامن — انسولن بڑھاتے اور PCOS خراب کرتے ہیں' },
      { en: 'Refined carbs: naan, paratha, biryani rice', ur: 'ریفائنڈ کاربس: نان، پراٹھا، بریانی چاول' },
      { en: 'Trans fats in commercial bakery items', ur: 'تجارتی بیکری اشیاء میں ٹرانس چکنائیاں' },
    ],
    lifestyleTips: [
      { en: 'Strength training 3x/week improves insulin sensitivity', ur: 'ہفتے میں 3 بار طاقت کی تربیت انسولن حساسیت بہتر کرتی ہے' },
      { en: 'Track cycles alongside carb intake — correlation becomes clear', ur: 'ماہواری اور کارب انٹیک ساتھ ٹریک کریں' },
      { en: 'Reduce endocrine disruptors: plastic containers, BPA', ur: 'ہارمون خلل ڈالنے والے کم کریں: پلاسٹک، BPA' },
    ],
    medicationAlternatives: {
      en: 'Metformin for PCOS may be reduced as insulin normalizes on keto. Birth control for symptom management can be discussed with your gynecologist as natural ovulation returns. Myo-inositol (4g daily) combined with keto shows comparable results to metformin in studies.',
      ur: 'PCOS کے لیے میٹفارمن کیٹو پر انسولن معمول پر آنے سے کم ہو سکتا ہے۔ علامات کے لیے birth control گائنیکالوجسٹ سے بات کریں جیسے قدرتی بیضہ دانی بحال ہو۔ مایو-انوسیٹول (روزانہ 4 گرام) کیٹو کے ساتھ مطالعوں میں میٹفارمن جیسے نتائج دیتا ہے۔',
    },
  },
  {
    id: 'psyche',
    title: { en: 'Mental Health & Cognitive Clarity', ur: 'ذہنی صحت و علمی وضاحت' },
    summary: {
      en: 'Anxiety, depression, brain fog, and ADHD symptoms often stem from blood sugar rollercoasters and neuroinflammation. Keto provides stable ketone fuel for the brain, reducing reliance on SSRIs and benzodiazepines for many patients.',
      ur: 'بے چینی، ڈپریشن، دماغی دھند، اور ADHD کی علامات اکثر بلڈ شوگر کے اتار چڑھاؤ اور اعصابی سوزش سے ہوتی ہیں۔ کیٹو دماغ کے لیے مستحکم کیٹون ایندھن فراہم کرتا ہے، بہت سے مریضوں میں SSRIs اور بینزودیازیپائنز پر انحصار کم کرتا ہے۔',
    },
    ketoApproach: {
      en: 'Stable ketones (0.5-3.0 mmol/L) provide alternative brain fuel. Include magnesium-rich foods: pumpkin seeds, spinach. Omega-3 from fish supports neurotransmitter production. Avoid caffeine overload from excessive chai. Ashwagandha and brahmi (traditional adaptogens) complement keto for stress.',
      ur: 'مستحکم کیٹونز (0.5-3.0 mmol/L) دماغ کے لیے متبادل ایندھن۔ میگنیشیم والی غذائیں: کدو کے بیج، پالک۔ مچھلی کا اومیگا-3 نیوروٹرانسمیٹر بناتا ہے۔ زیادہ چائے سے کیفین اوورلوڈ سے بچیں۔ اشوگندھا اور برہمی (روایتی ایڈاپٹوجنز) تناؤ میں کیٹو کا ساتھ دیتے ہیں۔',
    },
    foodsToEat: [
      { en: 'Fatty fish, eggs — choline and DHA for brain health', ur: 'چکنائی والی مچھلی، انڈے — دماغ کے لیے کولین اور DHA' },
      { en: 'Dark chocolate (85%+) — magnesium and mood support', ur: 'ڈارک چاکلیٹ (85%+) — میگنیشیم اور موڈ سپورٹ' },
      { en: 'Walnuts (akhrot) — shape of brain, rich in omega-3', ur: 'اخروٹ — دماغ کی شکل، اومیگا-3 سے بھرپور' },
      { en: 'Turmeric with black pepper — crosses blood-brain barrier', ur: 'کالی مرچ کے ساتھ ہلدی — خون دماغ رکاوٹ عبور کرتی ہے' },
    ],
    foodsToAvoid: [
      { en: 'Sugar crashes from mithai, cola, sweet lassi', ur: 'مٹھائی، کولا، میٹھی لسی سے شوگر کریش' },
      { en: 'Excess caffeine — anxiety and sleep disruption', ur: 'زیادہ کیفین — بے چینی اور نیند میں خلل' },
      { en: 'Processed foods with MSG and artificial colors', ur: 'MSG اور مصنوعی رنگ والی پروسیسڈ غذائیں' },
    ],
    lifestyleTips: [
      { en: 'Morning sunlight exposure — regulates circadian rhythm', ur: 'صبح دھوپ — جسمانی گھڑی منظم کرتی ہے' },
      { en: 'Yoga and pranayama (breath work) daily', ur: 'روزانہ یوگا اور پرانایام' },
      { en: 'Sleep 7-8 hours — ketosis deepens restorative sleep', ur: '7-8 گھنٹے نیند — کیٹوسس بحالی والی نیند گہری کرتا ہے' },
    ],
    medicationAlternatives: {
      en: 'Never stop psychiatric medications abruptly. Work with your psychiatrist: many patients on keto reduce SSRI doses gradually as mood stabilizes over 8-12 weeks. Ketogenic diet is being studied at Johns Hopkins for treatment-resistant depression. MCT oil (1-2 tbsp) can boost ketones for acute brain fog.',
      ur: 'نفسیاتی دوائیں اچانک نہ چھوڑیں۔ ماہر نفسیات کے ساتھ کام کریں: کیٹو پر بہت سے مریض 8-12 ہفتوں میں موڈ مستحکم ہونے پر SSRI آہستہ کم کرتے ہیں۔ Johns Hopkins میں علاج مزاحم ڈپریشن پر کیٹوجینک ڈائٹ کا مطالعہ ہو رہا ہے۔ MCT تیل (1-2 چمچ) فوری دماغی دھند میں کیٹون بڑھا سکتا ہے۔',
    },
  },
  {
    id: 'cardiac',
    title: { en: 'Heart & Cardiovascular Health', ur: 'دل و دل کی شریانوں کی صحت' },
    summary: {
      en: 'Contrary to outdated advice, ketogenic diets rich in healthy fats improve lipid profiles, reduce triglycerides, and increase HDL. Combined with desi spices like garlic and haldi, this approach can reduce statin dependency.',
      ur: 'پرانی غلط مشورے کے برعکس، صحت مند چکنائیوں والی کیٹوجینک ڈائٹ لپڈ پروفائل بہتر، ٹرائی گلیسرائڈز کم، HDL بڑھاتی ہے۔ لہسن اور ہلدی جیسے دیسی مصالحوں کے ساتھ یہ طریقہ سٹیٹن انحصار کم کر سکتا ہے۔',
    },
    ketoApproach: {
      en: 'Focus on monounsaturated fats: olive oil, avocados, almonds. Omega-3 from fish 3x/week. Eliminate trans fats and seed oils. Garlic (lehsan), ginger, and turmeric are cardioprotective. Monitor electrolytes — magnesium and potassium prevent palpitations during keto adaptation.',
      ur: 'مونو انسیچوریٹڈ چکنائی: زیتون کا تیل، ایووکاڈو، بادام۔ ہفتے میں 3 بار مچھلی کا اومیگا-3۔ ٹرانس چکنائیاں اور بیج تیل ختم کریں۔ لہسن، ادرک، ہلدی دل کی حفاظت کرتے ہیں۔ الیکٹرولائٹس نگرانی — میگنیشیم اور پوٹاشیم کیٹو ایڈاپٹیشن میں دھڑکن روکتے ہیں۔',
    },
    foodsToEat: [
      { en: 'Salmon, sardines — omega-3 reduces arterial inflammation', ur: 'سامن، سارڈین — اومیگا-3 شریانوں کی سوزش کم' },
      { en: 'Garlic (lehsan) — natural blood thinner, lowers BP', ur: 'لہسن — قدرتی بلڈ تھنر، بلڈ پریشر کم' },
      { en: 'Leafy greens — nitrates improve endothelial function', ur: 'پتہ دار سبزیاں — نائٹرٹس اینڈوتیلیل فنکشن بہتر' },
    ],
    foodsToAvoid: [
      { en: 'Vegetable/seed oils used in desi frying', ur: 'دیسی تلنے میں سبزی/بیج تیل' },
      { en: 'Excess sodium from commercial masala packets', ur: 'تجارتی مصالحہ پیکٹوں سے زیادہ نمک' },
      { en: 'Sugar — drives small dense LDL particles', ur: 'چینی — چھوٹے گھنے LDL ذرات بڑھاتی ہے' },
    ],
    lifestyleTips: [
      { en: '30 min brisk walking daily (tahal) — proven cardiac benefit', ur: 'روزانہ 30 منٹ تیز چہل قدمی — ثابت شدہ فائدہ' },
      { en: 'Stress management through meditation', ur: 'مراقبہ سے تناؤ کا انتظام' },
    ],
    medicationAlternatives: {
      en: 'Under cardiologist supervision, patients often reduce statins as triglycerides normalize and HDL rises on keto. CoQ10 supplementation supports heart muscle if on statins. L-carnitine and magnesium orotate are natural cardiac supports studied in literature.',
      ur: 'دل کے ماہر کی نگرانی میں مریض اکثر ٹرائی گلیسرائڈز معمول اور HDL بڑھنے پر سٹیٹنز کم کرتے ہیں۔ سٹیٹنز پر CoQ10 دل کی پٹھوں کو سپورٹ۔ L-carnitine اور میگنیشیم اورٹیٹ مطالعوں میں قدرتی دل کی سپورٹ۔',
    },
  },
  {
    id: 'diabetic',
    title: { en: 'Diabetes & Blood Sugar Control', ur: 'ذیابیطس و بلڈ شوگر کنٹرول' },
    summary: {
      en: 'Type 2 diabetes is reversible through carbohydrate restriction. Pakistani diets heavy in roti, rice, and sugar drive insulin resistance. Keto can achieve HbA1c below diabetic range within 3-6 months, often eliminating metformin and insulin needs.',
      ur: 'ٹائپ 2 ذیابیطس کاربس کی کمی سے الٹ ہو سکتی ہے۔ پاکستانی کھانوں میں روٹی، چاول، چینی انسولن مزاحمت بڑھاتی ہے۔ کیٹو 3-6 ماہ میں HbA1c ذیابیطس سے نیچے لا سکتا ہے، اکثر میٹفارمن اور انسولن کی ضرورت ختم۔',
    },
    ketoApproach: {
      en: 'Strict under 20g net carbs. Replace roti with almond flour roti or lettuce wraps. Cauliflower rice instead of chawal. Bitter melon (karela), fenugreek, and cinnamon are desi glucose-lowering allies. Monitor blood glucose — medications MUST be adjusted to prevent hypoglycemia.',
      ur: 'سخت 20 گرام نیٹ کاربس سے کم۔ روٹی کی جگہ بادام آٹے کی روٹی یا لیٹس ریپ۔ چاول کی جگہ گوبھی کا چاول۔ کریلا، میتھی، دار چینی دیسی گلوکوز کم کرنے والے۔ بلڈ گلوکوز نگرانی — دوائیں ایڈجسٹ کریں ہائپوگلائیسیمیا روکنے کے لیے۔',
    },
    foodsToEat: [
      { en: 'Bitter melon (karela) — natural insulin sensitizer', ur: 'کریلا — قدرتی انسولن sensitiser' },
      { en: 'Cinnamon (dalchini) in chai — lowers post-meal glucose', ur: 'چائے میں دار چینی — کھانے کے بعد گلوکوز کم' },
      { en: 'High-fiber vegetables: okra (bhindi), eggplant', ur: 'زیادہ فائبر سبزیاں: بھنڈی، بینگن' },
    ],
    foodsToAvoid: [
      { en: 'All forms of sugar: gur, shakkar, white sugar', ur: 'ہر قسم کی چینی: گڑ، شکر، سفید چینی' },
      { en: 'Fruit juices, mangoes, bananas, grapes', ur: 'فروٹ جوس، آم، کیلے، انگور' },
      { en: 'Rice, bread, potatoes — staple carb sources', ur: 'چاول، روٹی، آلو — بنیادی کارب ذرائع' },
    ],
    lifestyleTips: [
      { en: 'Post-meal walking reduces glucose spikes by 30%', ur: 'کھانے کے بعد چلنا گلوکوز 30% کم کرتا ہے' },
      { en: 'Test ketones and glucose — data drives decisions', ur: 'کیٹونز اور گلوکوز ٹیسٹ — ڈیٹا فیصلے چلاتا ہے' },
    ],
    medicationAlternatives: {
      en: 'Dr. Jason Fung and Pakistani physicians report T2D remission on therapeutic keto. NEVER reduce insulin without medical supervision — hypoglycemia is dangerous. Metformin may be continued or reduced as HbA1c normalizes. Berberine (1000mg) shows metformin-comparable effects in trials.',
      ur: 'ڈاکٹر جیسن فنگ اور پاکستانی ڈاکٹرز علاجی کیٹو پر T2D ریمیشن رپورٹ کرتے ہیں۔ انسولن بغیر نگرانی نہ کم کریں — ہائپوگلائیسیمیا خطرناک۔ HbA1c معمول پر میٹفارمن جاری یا کم۔ بربیرین (1000mg) ٹرائلز میں میٹفارمن جیسے اثر۔',
    },
  },
  {
    id: 'thyroid',
    title: { en: 'Thyroid & Metabolic Health', ur: 'تھائیرائیڈ و میٹابولک صحت' },
    summary: {
      en: 'Hypothyroidism and Hashimoto\'s respond to anti-inflammatory keto, especially when combined with eliminating gluten (which mimics thyroid tissue). Selenium from desi nuts and iodine from seafood support thyroid hormone conversion.',
      ur: 'ہائپوتھائیرائیڈزم اور ہاشیموٹو\'س سوزش مخالف کیٹو سے بہتر ہوتے ہیں، خاص طور پر گلٹن ختم کرنے سے (جو تھائیرائیڈ ٹشو جیسا ہے)۔ دیسی گری دار میوے سے سیلینیم اور سمندری غذا سے آیوڈین تھائیرائیڈ ہارمون تبدیلی میں مدد۔',
    },
    ketoApproach: {
      en: 'Moderate keto (30-50g carbs) may suit hypothyroid better than strict keto. Ensure adequate selenium (2-3 Brazil nuts or Pakistani almonds daily), zinc from meat, and iodine from fish. Avoid raw cruciferous in excess — cook cauliflower and broccoli. Ashwagandha supports T4 to T3 conversion.',
      ur: 'اعتدال پسند کیٹو (30-50 گرام کارب) سخت کیٹو سے بہتر ہو سکتا ہے۔ کافی سیلینیم (2-3 برازیل nuts یا پاکستانی بادام)، گوشت سے زنک، مچھلی سے آیوڈین۔ خام کراسیفروس زیادہ نہ — گوبھی پکائیں۔ اشوگندھا T4 سے T3 تبدیلی میں مدد۔',
    },
    foodsToEat: [
      { en: 'Brazil nuts — richest selenium source for thyroid', ur: 'برازیل nuts — تھائیرائیڈ کے لیے بہترین سیلینیم' },
      { en: 'Seaweed, fish — natural iodine', ur: 'سمندری گھاس، مچھلی — قدرتی آیوڈین' },
      { en: 'Cooked cruciferous in moderation', ur: 'اعتدال میں پکی کراسیفروس' },
    ],
    foodsToAvoid: [
      { en: 'Gluten: wheat roti, naan — molecular mimicry in Hashimoto\'s', ur: 'گلٹن: گندم روٹی، نان — ہاشیموٹو میں مالیکیولر mimicry' },
      { en: 'Soy products — goitrogenic when overconsumed', ur: 'سویا — زیادہ کھانے سے goitrogenic' },
    ],
    lifestyleTips: [
      { en: 'Consistent sleep schedule supports TSH rhythm', ur: 'مستقل نیند کا شیڈول TSH ریتم سپورٹ' },
      { en: 'Reduce stress — cortisol blocks T3 conversion', ur: 'تناؤ کم — کورٹیسول T3 تبدیلی روکتا ہے' },
    ],
    medicationAlternatives: {
      en: 'Levothyroxine dosing may need adjustment as metabolism changes on keto. Some Hashimoto\'s patients reduce antibodies on gluten-free keto. Work with endocrinologist — do not self-adjust thyroid medication.',
      ur: 'کیٹو پر میٹابولزم بدلنے پر لیووتھائیروکسین کی مقدار ایڈجسٹ ہو سکتی ہے۔ کچھ ہاشیموٹو مریض گلٹن فری کیٹو پر اینٹی باڈیز کم۔ اینڈوکرینالوجسٹ کے ساتھ کام — تھائیرائیڈ دوائی خود ایڈجسٹ نہ کریں۔',
    },
  },
  {
    id: 'joint',
    title: { en: 'Joints & Inflammation', ur: 'جوڑوں کا سوزش' },
    summary: {
      en: 'Arthritis, gout, and chronic joint pain are driven by inflammatory foods — sugar, seed oils, and processed carbs. Keto\'s anti-inflammatory ketones and omega-3 rich desi foods can replace NSAIDs for many sufferers.',
      ur: 'گٹھیا، گاؤٹ، اور دائمی جوڑوں کا درد سوزش والی غذائیں — چینی، بیج تیل، پروسیسڈ کاربس — سے ہوتا ہے۔ کیٹو کی سوزش مخالف کیٹونز اور اومیگا-3 دیسی غذائیں بہت سے مریضوں میں NSAIDs کی جگہ لے سکتے ہیں۔',
    },
    ketoApproach: {
      en: 'Eliminate sugar completely for gout (uric acid). Bone broth provides collagen for cartilage repair. Turmeric-ginger paste daily. Omega-3 from fish and flaxseed. Cherry extract for gout flares. Maintain healthy weight — each kg lost reduces knee load by 4kg.',
      ur: 'گاؤٹ کے لیے چینی مکمل ختم (یورک ایسڈ)۔ ہڈی کا شوربہ کارٹیلیج مرمت کے لیے کولیجن۔ روزانہ ہلدی ادرک پیسٹ۔ مچھلی اور السی اومیگا-3۔ گاؤٹ کے لیے چیری۔ صحت مند وزن — ہر کلو گھٹنے پر بوجھ 4 کلو کم۔',
    },
    foodsToEat: [
      { en: 'Bone broth — glucosamine and chondroitin naturally', ur: 'ہڈی کا شوربہ — قدرتی گلوکوسامائن' },
      { en: 'Turmeric with black pepper — potent anti-inflammatory', ur: 'کالی مرچ ہلدی — طاقتور سوزش مخالف' },
      { en: 'Fatty fish — reduces joint stiffness', ur: 'چکنائی والی مچھلی — جوڑوں کی سختی کم' },
    ],
    foodsToAvoid: [
      { en: 'Sugar and high-fructose corn syrup — gout trigger', ur: 'چینی اور HFCS — گاؤٹ ٹرگر' },
      { en: 'Beer and alcohol — uric acid elevation', ur: 'بیئر اور شراب — یورک ایسڈ بڑھاتے' },
      { en: 'Nightshades if sensitive: tomatoes, peppers', ur: 'حساسیت میں نائٹ شیڈ: ٹماٹر، مرچ' },
    ],
    lifestyleTips: [
      { en: 'Gentle yoga improves joint mobility without impact', ur: 'ہلکی یوگا بغیر دباؤ جوڑوں کی حرکت بہتر' },
      { en: 'Warm sesame oil massage (tel maalish)', ur: 'گرم تل کا مساج' },
    ],
    medicationAlternatives: {
      en: 'Curcumin (1000mg with piperine) shows NSAID-comparable anti-inflammatory effects. Omega-3 (2-4g EPA/DHA) reduces need for ibuprofen. Collagen peptides (10g daily) support cartilage. Always transition off NSAIDs with physician guidance due to rebound inflammation risk.',
      ur: 'کرکیومن (1000mg پائپرین) NSAID جیسے سوزش مخالف اثر۔ اومیگا-3 (2-4g EPA/DHA) ibuprofen کی ضرورت کم۔ کولیجن پپٹائڈز (10g روزانہ) کارٹیلیج۔ NSAIDs چھوڑیں ڈاکٹر کی رہنمائی — rebound سوزش خطرہ۔',
    },
  },
  {
    id: 'liver',
    title: { en: 'Liver Health & Fatty Liver', ur: 'جگر کی صحت و فیٹی لیور' },
    summary: {
      en: 'NAFLD (non-alcoholic fatty liver) affects 30%+ of Pakistanis. It is driven by fructose and refined carbs, not dietary fat. Keto rapidly reverses hepatic steatosis — often normalizing liver enzymes within 12 weeks.',
      ur: 'NAFLD 30%+ پاکستانیوں کو متاثر کرتا ہے۔ یہ فروکٹوز اور ریفائنڈ کاربس سے ہوتا ہے، غذائی چکنائی سے نہیں۔ کیٹو تیزی سے hepatic steatosis الٹ — اکثر 12 ہفتوں میں جگر انزائم معمول۔',
    },
    ketoApproach: {
      en: 'Zero sugar and fructose — eliminate cold drinks, fruit juice, and sweets. Coffee (black, no sugar) is hepatoprotective. Milk thistle (kateli) supports liver regeneration. Choline from eggs prevents fat accumulation. Cruciferous vegetables upregulate detox enzymes.',
      ur: 'صفر چینی اور فروکٹوز — کولڈ ڈرنکس، جوس، مٹھائی ختم۔ کالی کافی جگر کی حفاظت۔ کٹیلی جگر کی تجدید۔ انڈوں کا کولین چکنائی جمع روکتا ہے۔ کراسیفروس ڈیٹاکس انزائم بڑھاتے۔',
    },
    foodsToEat: [
      { en: 'Eggs — choline prevents fatty liver', ur: 'انڈے — کولین فیٹی لیور روکتا ہے' },
      { en: 'Coffee (black) — reduces liver fibrosis risk', ur: 'کالی کافی — جگر fibrosis خطرہ کم' },
      { en: 'Garlic and onions — sulfur supports Phase 2 detox', ur: 'لہسن پیاز — گندک Phase 2 ڈیٹاکس' },
    ],
    foodsToAvoid: [
      { en: 'Fructose: sodas, packaged juices, honey excess', ur: 'فروکٹوز: سوڈا، پیک جوس، زیادہ شہد' },
      { en: 'Alcohol — even moderate damages liver on NAFLD', ur: 'شراب — NAFLD پر اعتدال بھی نقصان' },
      { en: 'Refined carbs driving de novo lipogenesis', ur: 'ریفائنڈ کاربس de novo lipogenesis بڑھاتے' },
    ],
    lifestyleTips: [
      { en: 'Exercise — even 150 min/week reverses fatty liver', ur: 'ورزش — ہفتے میں 150 منٹ فیٹی لیور الٹ' },
      { en: 'Avoid paracetamol excess — hepatotoxic', ur: 'زیادہ پیراسیٹامول — جگر کو نقصان' },
    ],
    medicationAlternatives: {
      en: 'No medication equals diet for NAFLD reversal. Ursodeoxycholic acid may be used in advanced cases but keto addresses root cause. NAC (600mg) and alpha-lipoic acid support glutathione — master liver antioxidant.',
      ur: 'NAFLD الٹنے میں کوئی دوائی غذا کے برابر نہیں۔ ترقی یافتہ کیسز میں ursodeoxycholic acid مگر کیٹو جڑ کا سبب۔ NAC (600mg) اور alpha-lipoic acid گلوتاتھائیون — جگر کا ماسٹر اینٹی آکسیڈنٹ۔',
    },
  },
  {
    id: 'kidney',
    title: { en: 'Kidney Health', ur: 'گردے کی صحت' },
    summary: {
      en: 'Early CKD and kidney stones benefit from moderated keto with adequate hydration. Low-carb reduces insulin which drives kidney damage. Oxalate-aware food choices prevent stone recurrence.',
      ur: 'ابتدائی CKD اور گردے کی پتھریاں اعتدال پسند کیٹو اور کافی پانی سے فائدہ۔ کم کارب انسولن کم جو گردے کو نقصان۔ oxalate آگاہ انتخاب پتھریاں دوبارہ روکتے۔',
    },
    ketoApproach: {
      en: 'Moderate protein (0.8g/kg) — excess protein stresses kidneys. Hydrate well with lemon water. Limit oxalates: spinach, almonds in moderation. Citrate from lemon prevents calcium stones. Monitor eGFR with nephrologist if CKD present.',
      ur: 'اعتدال پسند پروٹین (0.8g/kg) — زیادہ پروٹین گردوں پر بوجھ۔ نیموں پانی سے ہائیڈریٹ۔ oxalates محدود: پالک، بادام اعتدال۔ نیموں citrate کیلشیم پتھریاں روکتا ہے۔ CKD میں nephrologist سے eGFR نگرانی۔',
    },
    foodsToEat: [
      { en: 'Lemon water — citrate prevents stone formation', ur: 'نیموں پانی — citrate پتھریاں روکتا ہے' },
      { en: 'Cucumber, celery — natural diuretics', ur: 'کھیرا، اجوائن — قدرتی پیشاب آور' },
      { en: 'Eggs, fish — quality protein in moderation', ur: 'انڈے، مچھلی — اعتدال میں معیاری پروٹین' },
    ],
    foodsToAvoid: [
      { en: 'Excess salt and commercial namkeen', ur: 'زیادہ نمک اور تجارتی نمکین' },
      { en: 'High-oxalate foods in excess: spinach, beets', ur: 'زیادہ oxalate: پالک، چقندر' },
      { en: 'Cola drinks — phosphoric acid damages kidneys', ur: 'کولا — فاسفورک ایسڈ گردوں کو نقصان' },
    ],
    lifestyleTips: [
      { en: 'Drink 2-3 liters water daily', ur: 'روزانہ 2-3 لیٹر پانی' },
      { en: 'Control blood pressure — top kidney protector', ur: 'بلڈ پریشر کنٹرول — گردے کا بہترین محافظ' },
    ],
    medicationAlternatives: {
      en: 'Potassium citrate for stone prevention may complement keto. Blood pressure medications often need reduction as keto lowers BP naturally. Advanced CKD requires specialized medical keto protocol — not standard keto.',
      ur: 'پتھریاں روکنے کے لیے پوٹاشیم citrate کیٹو کا ساتھ۔ بلڈ پریشر دوائیں اکثر کم کیٹو قدرتی BP کم کرتا ہے۔ ترقی یافتہ CKD خصوصی طبی کیٹو — معیاری کیٹو نہیں۔',
    },
  },
];
