import type { KnowledgeArticle } from '../types';

export const knowledgeArticles: KnowledgeArticle[] = [
  {
    id: 'keto-science',
    title: { en: 'The Science of Ketosis & Healing', ur: 'کیٹوسس اور شفا کی سائنس' },
    category: 'fundamentals',
    content: {
      en: 'Ketosis is a metabolic state where your body burns fat for fuel instead of glucose, producing ketone bodies (beta-hydroxybutyrate, acetoacetate). These ketones are not just fuel — they are signaling molecules that reduce inflammation, protect neurons, and improve mitochondrial function.\n\nWhen carbohydrates are restricted below 50g daily (20g for therapeutic applications), insulin drops, freeing stored fat for energy. The liver converts fatty acids into ketones, which cross the blood-brain barrier providing stable energy without glucose spikes.\n\nResearch from leading institutions shows ketogenic diets can reverse type 2 diabetes, reduce seizure frequency, improve PCOS markers, and support mental health. The key is sustained nutritional ketosis — not just low-carb, but adequate fat intake (70-75% calories) and moderate protein (20-25%).\n\nFor South Asians, the challenge is adapting carb-heavy traditional diets. The solution: replace roti with almond/coconut flour alternatives, rice with cauliflower rice, and sugar with stevia — while keeping the spices, flavors, and cultural identity intact.',
      ur: 'کیٹوسس میٹابولک حالت ہے جہاں جسم گلوکوز کی بجائے چربی ایندھن جلاتا ہے، کیٹون باڈیز (بیٹا ہائیڈروکسی بیوٹیریٹ) بناتا ہے۔ یہ کیٹونز صرف ایندھن نہیں — سگنلنگ مالیکیولز جو سوزش کم، نیورونز محفوظ، مائٹوکونڈریل فنکشن بہتر کرتے ہیں۔\n\nکاربس 50 گرام سے کم (علاجی 20 گرام) پر انسولن گرتا ہے، ذخیرہ چربی آزاد۔ جگر چکنائی ایسڈ کیٹونز میں، خون دماغ رکاوٹ عبور مستحکم ایندھن بغیر گلوکوز اسپائک۔\n\nمعروف اداروں کے مطالعے کیٹوجینک ڈائٹ ٹائپ 2 ذیابیطس الٹ، دورے کم، PCOS بہتر، ذہنی صحت سپورٹ۔ کلید مستقل غذائی کیٹوسس — صرف کم کارب نہیں، کافی چکنائی (70-75%) اعتدال پسند پروٹین (20-25%)۔\n\nجنوبی ایشیائیوں کے لیے چیلنج کارب بھاری روایتی کھانا۔ حل: روٹی بادام/ناریل آٹے، چاول گوبھی، چینی اسٹیویا — مصالحے ذائقے ثقافت برقرار۔',
    },
    keyTakeaways: [
      { en: 'Ketones are healing signaling molecules, not just fuel', ur: 'کیٹونز شفا کے سگنلنگ مالیکیولز، صرف ایندھن نہیں' },
      { en: 'Sustained ketosis requires under 50g carbs daily', ur: 'مستقل کیٹوسس روزانہ 50 گرام کارب سے کم' },
      { en: 'Desi cuisine can be fully adapted without losing identity', ur: 'دیسی کھانا مکمل ڈھالا جا سکتا ہے بغیر شناخت کھوئے' },
    ],
  },
  {
    id: 'medication-reduction',
    title: { en: 'Reducing Medication Through Diet — Safely', ur: 'غذا سے دوائیں کم کرنا — محفوظ طریقے' },
    category: 'healing',
    content: {
      en: 'Many chronic conditions treated with lifelong medications — metformin for diabetes, PPIs for acidity, statins for cholesterol, SSRIs for depression — have dietary root causes that keto addresses.\n\nIMPORTANT SAFETY PROTOCOL:\n1. Never stop medications abruptly — work with your doctor\n2. Monitor blood glucose if diabetic — hypoglycemia risk when on insulin/metformin\n3. Blood pressure may drop — adjust antihypertensives with physician\n4. Thyroid medication may need dose adjustment as metabolism changes\n5. Psychiatric medications require gradual tapering under psychiatrist supervision\n\nTimeline expectations: Most patients see measurable improvements in 4-8 weeks. HbA1c, lipid panels, liver enzymes, and inflammatory markers (CRP) should be tracked. Medication reduction typically begins at 8-12 weeks when markers normalize.\n\nPakistani physicians increasingly recognize therapeutic nutrition. Find a doctor who supports dietary intervention alongside conventional care.',
      ur: 'بہت سی دائمی بیماریاں زندگی بھر دوائیں — ذیابیطس میٹفارمن، تیزابیت PPIs، کولیسٹرول سٹیٹنز، ڈپریشن SSRIs — غذائی جڑیں کیٹو حل کرتا ہے۔\n\nاہم حفاظتی پروٹوکول:\n1. دوائیں اچانک نہ چھوڑیں — ڈاکٹر سے کام\n2. ذیابیطس میں گلوکوز نگرانی — انسولن/میٹفارمن پر ہائپوگلائیسیمیا\n3. بلڈ پریشر گر سکتا — ڈاکٹر سے ایڈجسٹ\n4. تھائیرائیڈ دوائی میٹابولزم بدلنے پر ایڈجسٹ\n5. نفسیاتی دوائیں ماہر نفسیات نگرانی آہستہ کم\n\nوقت کی توقع: 4-8 ہفتوں میں بہتری۔ HbA1c، لپڈ، جگر انزائم، CRP ٹریک۔ 8-12 ہفتوں پر دوائی کم جب مارکرز معمول۔\n\nپاکستانی ڈاکٹرز علاجی غذائیت تسلیم کرتے ہیں۔ ایسا ڈاکٹر تلاش کریں جو روایتی علاج کے ساتھ غذائی مداخلت سپورٹ کرے۔',
    },
    keyTakeaways: [
      { en: 'Always work with your doctor — never self-taper medications', ur: 'ہمیشہ ڈاکٹر سے — دوائیں خود کم نہ کریں' },
      { en: 'Monitor markers at 4, 8, and 12 weeks', ur: '4، 8، 12 ہفتوں پر مارکرز نگرانی' },
      { en: 'Hypoglycemia and BP drops are real risks — be prepared', ur: 'ہائپوگلائیسیمیا BP گرنا حقیقی خطرے — تیار رہیں' },
    ],
  },
  {
    id: 'desi-spices-healing',
    title: { en: 'Healing Power of Desi Spices', ur: 'دیسی مصالحوں کی شفا کی طاقت' },
    category: 'nutrition',
    content: {
      en: 'Pakistani and South Asian spices are pharmacological powerhouses that complement ketogenic healing:\n\nTURMERIC (Haldi): Curcumin reduces inflammation comparable to NSAIDs. Crosses blood-brain barrier. Combine with black pepper (piperine) for 2000% better absorption. 1 tsp daily in golden milk (with coconut milk, no sugar).\n\nGINGER (Adrak): Anti-nausea, prokinetic for GERD, thermogenic for metabolism. Fresh ginger tea aids digestion and reduces joint pain.\n\nCINNAMON (Dalchini): Mimics insulin, lowers fasting glucose 10-29%. Add to keto chai. Ceylon cinnamon preferred over cassia for liver safety.\n\nFENUGREEK (Methi): Seeds soaked overnight reduce PCOS insulin resistance. Leaves in palak methi provide iron and fiber.\n\nGARLIC (Lehsan): Natural ACE inhibitor, blood thinner, antimicrobial. 2-3 cloves daily supports cardiac health.\n\nAJWAIN: Carminative for bloating and IBS. Chew 1 tsp with warm water after meals.\n\nThese spices make desi keto not just tolerable but delicious — the bridge between ancestral wisdom and modern metabolic science.',
      ur: 'پاکستانی جنوبی ایشیائی مصالحے کیٹوجینک شفا میں مدد:\n\nہلدی: کرکیومن NSAIDs جیسا سوزش مخالف۔ خون دماغ رکاوٹ عبور۔ کالی مرچ (پائپرین) 2000% جذب بہتر۔ روزانہ 1 چمچ گولڈن ملک (ناریل دودھ، بغیر چینی)۔\n\nادرک: متلی مخالف، GERD prokinetic، میٹابولزم thermogenic۔ تازہ ادرک چائے ہاضمہ جوڑوں کا درد کم۔\n\nدار چینی: انسولن جیسا، فاسٹنگ گلوکوز 10-29% کم۔ کیٹو چائے میں۔ جگر کے لیے سیلون نہ کیسیا۔\n\nمیتھی: رات بھگوئے بیج PCOS انسولن مزاحمت کم۔ پتے پالک میتھی آئرن فائبر۔\n\nلہسن: قدرتی ACE inhibitor، بلڈ تھنر، جراثیم کش۔ روزانہ 2-3 جوے دل کی صحت۔\n\nاجوائن: پھولاؤ IBS carminative۔ کھانے بعد گرم پانی 1 چمچ چبائیں۔\n\nیہ مصالحے دیسی کیٹو صرف قابل برداشت نہیں لذیذ — اجداد کی حکمت اور جدید میٹابولک سائنس کا پل۔',
    },
    keyTakeaways: [
      { en: 'Turmeric + black pepper = 2000% better absorption', ur: 'ہلدی + کالی مرچ = 2000% بہتر جذب' },
      { en: 'Cinnamon lowers fasting glucose 10-29%', ur: 'دار چینی فاسٹنگ گلوکوز 10-29% کم' },
      { en: 'Daily spice use turns meals into medicine', ur: 'روزانہ مصالحے کھانا دوائی بناتے ہیں' },
    ],
  },
  {
    id: 'intermittent-fasting',
    title: { en: 'Intermittent Fasting & Desi Lifestyle', ur: 'وقفے وقفے سے روزہ اور دیسی طرز زندگی' },
    category: 'lifestyle',
    content: {
      en: 'Intermittent fasting (IF) synergizes powerfully with keto — accelerating ketosis, autophagy (cellular cleanup), and insulin sensitivity. Muslims already practice annual Ramadan fasting; IF extends this wisdom daily.\n\nPOPULAR PROTOCOLS:\n16:8 — Fast 16 hours, eat within 8-hour window. Skip breakfast, first meal at 12pm, last by 8pm. Natural for desi culture (late breakfast, early dinner).\n18:6 — More aggressive, better for diabetes reversal.\nOMAD — One meal a day for advanced healing (under medical supervision).\n\nBENEFITS WITH KETO:\n- Deeper ketosis and higher ketone levels\n- Autophagy clears damaged cells — anti-aging, anti-cancer\n- Gut rest reduces IBS and bloating\n- Mental clarity peaks during fasting hours\n- Matches Prophet\'s dietary wisdom (moderation, not constant eating)\n\nBREAKING FAST DESI-STYLE: Start with dates (1-2 only, high carb) then protein and fat — bone broth, eggs, or chicken. Avoid breaking fast with heavy carbs (paratha, halwa).\n\nWomen with PCOS: Start with 14:10, gradually extend. Monitor cycle changes.',
      ur: 'وقفے وقفے روزہ (IF) کیٹو کے ساتھ طاقتور — کیٹوسس، autophagy (خلیوں کی صفائی)، انسولن حساسیت تیز۔ مسلمان رمضان روزہ کرتے؛ IF یہ حکمت روزانہ۔\n\nمشہور پروٹوکول:\n16:8 — 16 گھنٹے روزہ، 8 میں کھانا۔ ناشتا چھوڑیں، پہلا 12 بجے، آخری 8 بجے۔ دیسی ثقافت (دیر ناشتا، جلدی رات کا کھانا)۔\n18:6 — زیادہ، ذیابیطس الٹ بہتر۔\nOMAD — دن میں ایک کھانا (طبی نگرانی)۔\n\nکیٹو فوائد:\n- گہرا کیٹوسس زیادہ کیٹون\n- autophagy خراب خلیے صاف — ضد پیری، ضد کینسر\n- آنتوں کو آرام IBS پھولاؤ کم\n- روزے میں دماغی وضاحت چوٹی\n- نبی کی غذائی حکمت (اعتدال، مسلسل کھانا نہیں)\n\nروزہ افطار دیسی: کھجور (1-2، زیادہ کارب) پھر پروٹین چکنائی — یخنی، انڈے، چکن۔ بھاری کارب (پراٹھا، حلوہ) سے افطار نہ۔\n\nPCOS والی خواتین: 14:10 سے شروع، آہستہ بڑھائیں۔ سائیکل نگرانی۔',
    },
    keyTakeaways: [
      { en: '16:8 fasting fits naturally with desi meal timing', ur: '16:8 روزہ دیسی کھانے کے وقت سے ملتا ہے' },
      { en: 'Break fast with protein/fat, not carbs', ur: 'روزہ پروٹین چکنائی سے توڑیں، کارب نہیں' },
      { en: 'Autophagy during fasting clears damaged cells', ur: 'روزے میں autophagy خراب خلیے صاف' },
    ],
  },
  {
    id: 'electrolytes-keto',
    title: { en: 'Electrolytes: The Keto Flu Solution', ur: 'الیکٹرولائٹس: کیٹو فلو کا حل' },
    category: 'fundamentals',
    content: {
      en: 'The "keto flu" — headaches, fatigue, cramps, irritability in the first 1-2 weeks — is NOT inevitable. It is electrolyte depletion as insulin drops and kidneys excrete sodium.\n\nDAILY ELECTROLYTE TARGETS ON KETO:\nSodium: 3000-5000mg (desi namak in bone broth, pickle juice, salted foods)\nPotassium: 3000-4000mg (avocado, spinach, mushrooms, cream of tartar 1/4 tsp)\nMagnesium: 300-500mg (supplement: magnesium glycinate before bed)\n\nDESI ELECTROLYTE DRINK:\n- 1 liter water\n- 1/2 tsp pink Himalayan salt (kala namak)\n- 1/4 tsp cream of tartar (potassium)\n- Juice of 1 lemon\n- Stevia to taste\nDrink 2-3 glasses daily, especially in Pakistani heat.\n\nBone broth (yakhni) is the ultimate desi electrolyte drink — simmer bones 12-24 hours with salt, ginger, and spices. Drink a cup morning and evening during keto adaptation.\n\nNever restrict salt on keto — this is the most common mistake causing unnecessary suffering.',
      ur: 'کیٹو فلو — سر درد، تھکاوٹ، کھنچاؤ، چڑچڑاپن پہلے 1-2 ہفتوں — لازمی نہیں۔ انسولن گرنے گردے سوڈیم خارج — الیکٹرولائٹ ختم۔\n\nروزانہ الیکٹرولائٹ کیٹو:\nسوڈیم: 3000-5000mg (یخنی نمک اچار، نمکین)\nپوٹاشیم: 3000-4000mg (ایووکاڈو، پالک، مشروم، cream of tartar 1/4 چمچ)\nمیگنیشیم: 300-500mg (سپلیمنٹ glycinate سونے سے پہلے)\n\nدیسی الیکٹرولائٹ مشروب:\n- 1 لیٹر پانی\n- 1/2 چمچ ہمالیائی نمک\n- 1/4 چمچ cream of tartar\n- 1 لیموں رس\n- اسٹیویا\nروزانہ 2-3 گلاس، پاکستانی گرمی میں۔\n\nہڈی کا شوربہ (یخنی) بہترین دیسی الیکٹرولائٹ — ہڈیاں 12-24 گھنٹے نمک ادرک مصالحے۔ صبح شام ایک کپ کیٹو ایڈاپٹیشن میں۔\n\nکیٹو پر نمک محدود نہ کریں — سب سے عام غلطی غیر ضروری تکلیف۔',
    },
    keyTakeaways: [
      { en: 'Keto flu is electrolyte deficiency, not carb withdrawal', ur: 'کیٹو فلو الیکٹرولائٹ کی کمی، کارب واپسی نہیں' },
      { en: 'Bone broth (yakhni) is the ultimate desi electrolyte drink', ur: 'یخنی بہترین دیسی الیکٹرولائٹ مشروب' },
      { en: 'Do NOT restrict salt on keto — increase it', ur: 'کیٹو پر نمک محدود نہ — بڑھائیں' },
    ],
  },
];
