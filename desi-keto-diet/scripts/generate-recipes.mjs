/**
 * Generates ~200 keto recipe catalog entries from cuisine dish lists.
 * Run: node scripts/generate-recipes.mjs
 */
import { writeFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));

const AILMENTS = ['gastric', 'gyne', 'psyche', 'cardiac', 'diabetic', 'thyroid', 'joint', 'liver', 'kidney'];

const CUISINE_DISHES = {
  pakistani: [
    ['Keto Nihari', 'کیٹو نہاری', 'beef', 'slow-cooked'],
    ['Keto Haleem', 'کیٹو حلیم', 'beef', 'slow-cooked'],
    ['Paya Bone Broth', 'پائے ہڈی کا شوربہ', 'beef', 'soup'],
    ['Chapli Kabab', 'چپلی کباب', 'beef', 'grill'],
    ['Shinwari Karahi', 'شنواری کڑاہی', 'mutton', 'karahi'],
    ['Lahori Chargha', 'لاہوری چرغہ', 'chicken', 'roast'],
    ['White Chicken Karahi', 'وائٹ چکن کڑاہی', 'chicken', 'karahi'],
    ['Dumba Karahi', 'دنبہ کڑاہی', 'mutton', 'karahi'],
    ['Peshawari Namkeen Gosht', 'پشاوری نمکین گوشت', 'mutton', 'roast'],
    ['Keema Karela', 'قیمہ کریلا', 'beef', 'curry'],
    ['Bhindi Gosht', 'بھنڈی گوشت', 'mutton', 'curry'],
    ['Baingan Ka Bharta', 'بینگن کا بھرتہ', 'vegetable', 'curry'],
    ['Anda Curry Keto', 'کیٹو انڈا کری', 'egg', 'curry'],
    ['Keema Matar Keto', 'کیٹو قیمہ مٹر', 'beef', 'curry'],
    ['Dhaba Style Chicken', 'ڈھابہ اسٹائل چکن', 'chicken', 'curry'],
    ['Handi Gosht', 'ہانڈی گوشت', 'mutton', 'handi'],
    ['Chicken Jalfrezi', 'چکن جلفریزی', 'chicken', 'stir-fry'],
    ['Goat Chops Masala', 'بکرے کی چانپ مسالہ', 'mutton', 'grill'],
    ['Keto Aloo Gosht', 'کیٹو آلو گوشت', 'mutton', 'curry'],
    ['Mutton Brain Masala', 'مغز مسالہ', 'mutton', 'curry'],
    ['Liver Masala Keto', 'کیٹو کلیجی مسالہ', 'beef', 'curry'],
    ['Testi Kebab Bowl', 'ٹیسیٹی کباب', 'beef', 'grill'],
    ['Chapshoro Keto Bowl', 'کیٹو چپشورو', 'beef', 'bowl'],
    ['Kashmiri Gosht', 'کشمیری گوشت', 'mutton', 'curry'],
    ['Anda Shorba', 'انڈا شوربہ', 'egg', 'soup'],
  ],
  bbq: [
    ['Malai Boti', 'ملائی بوٹی', 'chicken', 'grill'],
    ['Reshmi Kabab', 'ریشمی کباب', 'chicken', 'grill'],
    ['Chapli Kabab BBQ', 'چپلی کباب BBQ', 'beef', 'grill'],
    ['Bihari Kabab', 'بہاری کباب', 'beef', 'grill'],
    ['Gola Kabab', 'گولہ کباب', 'beef', 'grill'],
    ['Lamb Chops Tikka', 'لیمب چاپس ٹکہ', 'mutton', 'grill'],
    ['Fish Tikka', 'فش ٹکہ', 'fish', 'grill'],
    ['Prawn Tikka', 'جنگا ٹکہ', 'prawn', 'grill'],
    ['Beef Boti', 'بیف بوٹی', 'beef', 'grill'],
    ['Mutton Boti', 'مٹن بوٹی', 'mutton', 'grill'],
    ['Chicken Afghan Boti', 'افغانی چکن بوٹی', 'chicken', 'grill'],
    ['Tandoori Chicken', 'تندوری چکن', 'chicken', 'grill'],
    ['Kastoori Murgh', 'کستوری مرغ', 'chicken', 'grill'],
    ['Behari Roll Keto', 'کیٹو بہاری رول', 'beef', 'wrap'],
    ['Kabab Paratha Roll', 'کباب رول', 'chicken', 'wrap'],
    ['Grilled Pomfret', 'گرل پامفلٹ', 'fish', 'grill'],
    ['Surmai Tikka', 'سرمئی ٹکہ', 'fish', 'grill'],
    ['Chicken Tangri', 'چکن ٹانگری', 'chicken', 'grill'],
    ['Mutton Ribs BBQ', 'مٹن ربس BBQ', 'mutton', 'grill'],
    ['Beef Seekh Roll', 'بیف سیخ رول', 'beef', 'wrap'],
    ['Chicken Malai Roll', 'چکن ملائی رول', 'chicken', 'wrap'],
    ['Grilled Paneer Tikka', 'گرل پنیر ٹکہ', 'paneer', 'grill'],
    ['Mushroom Tikka', 'مشروم ٹکہ', 'vegetable', 'grill'],
    ['Mixed Grill Platter', 'مکس گرل پلیٹر', 'mixed', 'grill'],
    ['Charcoal Lamb Leg', 'کوئلے کی بکرے کی ٹانگ', 'mutton', 'roast'],
  ],
  chinese: [
    ['Kung Pao Chicken', 'کنگ پاؤ چکن', 'chicken', 'stir-fry'],
    ['Szechuan Beef', 'سچوان بیف', 'beef', 'stir-fry'],
    ['Egg Foo Young', 'ایگ فو یانگ', 'egg', 'stir-fry'],
    ['Hot & Sour Soup', 'ہاٹ اینڈ ساؤر سوپ', 'chicken', 'soup'],
    ['Mongolian Beef', 'منگولین بیف', 'beef', 'stir-fry'],
    ['Chicken Manchurian Keto', 'کیٹو چکن منچورین', 'chicken', 'stir-fry'],
    ['Beef Broccoli', 'بیف بروکولی', 'beef', 'stir-fry'],
    ['Shrimp Garlic Noodles', 'لہسن جھینگا', 'prawn', 'stir-fry'],
    ['Cashew Chicken', 'کاجو چکن', 'chicken', 'stir-fry'],
    ['Mapo Tofu Keto', 'کیٹو ماپو ٹوفو', 'paneer', 'stir-fry'],
    ['Chinese Steamed Fish', 'چائنیز سٹیم فش', 'fish', 'steam'],
    ['Peking Duck Style', 'پیکن ڈک اسٹائل', 'chicken', 'roast'],
    ['Chili Garlic Prawns', 'مرچ لہسن جھینگا', 'prawn', 'stir-fry'],
    ['Black Bean Chicken', 'بلیک بین چکن', 'chicken', 'stir-fry'],
    ['Sesame Chicken', 'تل چکن', 'chicken', 'stir-fry'],
    ['Beef Chow Fun Keto', 'کیٹو بیف چاؤ فن', 'beef', 'stir-fry'],
    ['Wonton Soup Keto', 'کیٹو وونٹن سوپ', 'chicken', 'soup'],
    ['Chinese Egg Drop Soup', 'انڈا ڈراپ سوپ', 'egg', 'soup'],
    ['Stir Fry Bok Choy', 'بوک چائے اسٹِر فرائی', 'vegetable', 'stir-fry'],
    ['Five Spice Lamb', 'پانچ مصالحہ بکرا', 'mutton', 'stir-fry'],
    ['Chinese Chicken Salad', 'چائنیز چکن سلاد', 'chicken', 'salad'],
    ['Beef Pepper Steak', 'بیف پیپر اسٹیک', 'beef', 'stir-fry'],
    ['Garlic Green Beans', 'لہسن ہری پھلیاں', 'vegetable', 'stir-fry'],
    ['Sweet Sour Chicken Keto', 'کیٹو میٹھا کھٹا چکن', 'chicken', 'stir-fry'],
    ['Chinese Omelette', 'چائنیز املیٹ', 'egg', 'breakfast'],
  ],
  continental: [
    ['Herb Crusted Salmon', 'ہرب کرسٹڈ سامن', 'fish', 'roast'],
    ['Grilled Chicken Breast', 'گرل چکن بریسٹ', 'chicken', 'grill'],
    ['Beef Steak with Butter', 'مکھن بیف اسٹیک', 'beef', 'grill'],
    ['Creamy Mushroom Chicken', 'کریمی مشروم چکن', 'chicken', 'sauce'],
    ['Greek Salad Bowl', 'گریک سلاد', 'vegetable', 'salad'],
    ['Caesar Salad Keto', 'کیٹو سیزر سلاد', 'chicken', 'salad'],
    ['Zucchini Lasagna', 'زوچینی لیسنگیا', 'beef', 'bake'],
    ['Stuffed Bell Peppers', 'بھرے شملہ مرچ', 'beef', 'bake'],
    ['French Onion Soup', 'فرنچ پیاز سوپ', 'beef', 'soup'],
    ['Chicken Cordon Bleu', 'کورڈن بلیو چکن', 'chicken', 'bake'],
    ['Beef Bourguignon Keto', 'کیٹو بیف برگنئن', 'beef', 'slow-cooked'],
    ['Mediterranean Fish', 'میڈیٹیرینین فش', 'fish', 'roast'],
    ['Spinach Frittata', 'پالک فرٹاٹا', 'egg', 'breakfast'],
    ['Avocado Egg Bowl', 'ایووکاڈو انڈا', 'egg', 'breakfast'],
    ['Cauliflower Gratin', 'گوبھی گریٹن', 'vegetable', 'bake'],
    ['Chicken Alfredo Keto', 'کیٹو الفریڈو چکن', 'chicken', 'sauce'],
    ['Lamb Rack Herbs', 'ہرب لیمب ریک', 'mutton', 'roast'],
    ['Tuna Niçoise Salad', 'ٹونا سلاد', 'fish', 'salad'],
    ['Eggplant Parmesan', 'بینگن پرمژان', 'vegetable', 'bake'],
    ['Cabbage Rolls Keto', 'کیٹو بند گوبھی رول', 'beef', 'bake'],
    ['Broccoli Cheese Soup', 'بروکولی چیز سوپ', 'vegetable', 'soup'],
    ['Chicken Piccata', 'چکن پیکاٹا', 'chicken', 'sauce'],
    ['Beef Meatballs', 'بیف میٹ بالز', 'beef', 'bake'],
    ['Shrimp Scampi', 'جھینگا سکمپی', 'prawn', 'sauce'],
    ['Caprese Salad', 'کاپریزے سلاد', 'paneer', 'salad'],
  ],
  mughlai: [
    ['Keto Butter Chicken', 'کیٹو بٹر چکن', 'chicken', 'curry'],
    ['Chicken Korma Keto', 'کیٹو چکن قورمہ', 'chicken', 'curry'],
    ['Mutton Korma', 'مٹن قورمہ', 'mutton', 'curry'],
    ['Shahi Tukda Keto', 'کیٹو شاہی ٹکڑا', 'egg', 'dessert'],
    ['Mughlai Paratha Keto', 'کیٹو مغلئی پراٹھا', 'egg', 'bread'],
    ['Pasanda Keto', 'کیٹو پسندہ', 'beef', 'curry'],
    ['Nargisi Kofta', 'نرگسی کوفتہ', 'egg', 'curry'],
    ['Shami Kabab', 'شامی کباب', 'beef', 'grill'],
    ['Galouti Kabab', 'گلوتی کباب', 'beef', 'grill'],
    ['Kakori Kabab', 'کاکوری کباب', 'mutton', 'grill'],
    ['Mutton Rogan Josh', 'روگان جوش', 'mutton', 'curry'],
    ['Chicken Rezala', 'چکن ریزالہ', 'chicken', 'curry'],
    ['Mutton Do Pyaaza', 'دو پیازہ گوشت', 'mutton', 'curry'],
    ['Murgh Musallam', 'مرغ مصلم', 'chicken', 'roast'],
    ['Keema Samosa Keto', 'کیٹو قیمہ سموسہ', 'beef', 'snack'],
    ['Shahi Paneer', 'شاہی پنیر', 'paneer', 'curry'],
    ['Navratan Korma Keto', 'کیٹو نو رتن قورمہ', 'vegetable', 'curry'],
    ['Mutton Biryani Keto', 'کیٹو مٹن بریانی', 'mutton', 'biryani'],
    ['Chicken Biryani Keto', 'کیٹو چکن بریانی', 'chicken', 'biryani'],
    ['Zarda Keto', 'کیٹو زردہ', 'egg', 'dessert'],
    ['Firni Keto', 'کیٹو فرنی', 'paneer', 'dessert'],
    ['Mughlai Keema', 'مغلئی قیمہ', 'beef', 'curry'],
    ['Badami Murgh', 'بادامی مرغ', 'chicken', 'curry'],
    ['Shab Deg Keto', 'کیٹو شب دیگ', 'mutton', 'slow-cooked'],
    ['Chicken Changezi', 'چکن چنگیزی', 'chicken', 'curry'],
  ],
  punjabi: [
    ['Sarson Ka Saag Keto', 'کیٹو سرسوں کا ساگ', 'vegetable', 'curry'],
    ['Makki Roti Keto', 'کیٹو مکئی روٹی', 'vegetable', 'bread'],
    ['Amritsari Fish', 'امرتسری مچھلی', 'fish', 'fry'],
    ['Tandoori Murgh Punjabi', 'تندوری مرغ پنجابی', 'chicken', 'grill'],
    ['Punjabi Kadhi Keto', 'کیٹو پنجابی کڑھی', 'egg', 'curry'],
    ['Rajma Keto Bowl', 'کیٹو راجما', 'vegetable', 'curry'],
    ['Chole Keto', 'کیٹو چھولے', 'vegetable', 'curry'],
    ['Paneer Tikka Punjabi', 'پنیر ٹکہ پنجابی', 'paneer', 'grill'],
    ['Maa Ki Dal Keto', 'کیٹو ماں کی دال', 'vegetable', 'dal'],
    ['Aloo Paratha Keto', 'کیٹو آلو پراٹھا', 'vegetable', 'bread'],
    ['Lassi Keto', 'کیٹو لسی', 'paneer', 'drink'],
    ['Punjabi Chicken Curry', 'پنجابی چکن کری', 'chicken', 'curry'],
    ['Keema Naan Keto', 'کیٹو قیمہ نان', 'beef', 'bread'],
    ['Bhature Keto', 'کیٹو بھٹورے', 'egg', 'bread'],
    ['Gobhi Paratha Keto', 'کیٹو گوبھی پراٹھا', 'vegetable', 'bread'],
    ['Punjabi Egg Curry', 'پنجابی انڈا کری', 'egg', 'curry'],
    ['Fish Curry Punjabi', 'پنجابی مچھلی کری', 'fish', 'curry'],
    ['Mutton Curry Punjabi', 'پنجابی مٹن کری', 'mutton', 'curry'],
    ['Saag Gosht', 'ساگ گوشت', 'mutton', 'curry'],
    ['Punjabi Raita', 'پنجابی رائتہ', 'vegetable', 'salad'],
    ['Stuffed Karela', 'بھرا کریلا', 'vegetable', 'curry'],
    ['Punjabi Pickle Chicken', 'اچار چکن', 'chicken', 'curry'],
    ['Tandoori Roti Keto', 'کیٹو تندوری روٹی', 'vegetable', 'bread'],
    ['Makhan Chicken', 'مکھن چکن', 'chicken', 'curry'],
    ['Punjabi Keema', 'پنجابی قیمہ', 'beef', 'curry'],
  ],
  sindhi: [
    ['Sindhi Kadhi Keto', 'کیٹو سندھی کڑھی', 'vegetable', 'curry'],
    ['Sai Bhaji Keto', 'کیٹو سائی بھاجی', 'vegetable', 'curry'],
    ['Sindhi Biryani Keto', 'کیٹو سندھی بریانی', 'mutton', 'biryani'],
    ['Teevarn Keto', 'کیٹو تیورن', 'fish', 'curry'],
    ['Singhi Fish Curry', 'سنگھی مچھلی', 'fish', 'curry'],
    ['Sindhi Curry Keto', 'کیٹو سندھی کری', 'mutton', 'curry'],
    ['Koki Keto', 'کیٹو کوکی', 'vegetable', 'bread'],
    ['Lolo Keto', 'کیٹو لو لو', 'vegetable', 'bread'],
    ['Sindhi Pulao Keto', 'کیٹو سندھی پلاؤ', 'mutton', 'biryani'],
    ['Bhugal Teewarn', 'بھگل تیورن', 'fish', 'curry'],
    ['Sindhi Seyal', 'سندھی سیال', 'vegetable', 'curry'],
    ['Sindhi Pickle Raita', 'سندھی اچار رائتہ', 'vegetable', 'salad'],
    ['Sindhi Chicken Karahi', 'سندھی چکن کڑاہی', 'chicken', 'karahi'],
    ['Sindhi Daal Keto', 'کیٹو سندھی دال', 'vegetable', 'dal'],
    ['Sindhi Fish Fry', 'سندھی مچھلی فرائی', 'fish', 'fry'],
    ['Sindhi Mutton', 'سندھی بکرا', 'mutton', 'curry'],
    ['Sindhi Bhindi', 'سندھی بھنڈی', 'vegetable', 'curry'],
    ['Sindhi Tamatar Kadhi', 'ٹماٹر کڑھی', 'vegetable', 'curry'],
    ['Sindhi Aloo Tuk', 'آلو ٹک', 'vegetable', 'fry'],
    ['Sindhi Seyal Mani', 'سیال مانی', 'egg', 'curry'],
    ['Sindhi Koki with Raita', 'کوکی رائتہ', 'vegetable', 'bread'],
    ['Sindhi Pallo Fish', 'پالو مچھلی', 'fish', 'curry'],
    ['Sindhi Chicken Curry', 'سندھی چکن کری', 'chicken', 'curry'],
    ['Sindhi Vegetable Curry', 'سندھی سبزی', 'vegetable', 'curry'],
    ['Sindhi Tamatar Biryani', 'ٹماٹر بریانی', 'vegetable', 'biryani'],
  ],
  balochi: [
    ['Balochi Sajji Chicken', 'بلوچی سجی چکن', 'chicken', 'roast'],
    ['Balochi Sajji Lamb', 'بلوچی سجی بکرا', 'mutton', 'roast'],
    ['Kaak Bread Keto', 'کیٹو کاک', 'vegetable', 'bread'],
    ['Dampukht Keto', 'کیٹو دم پخت', 'mutton', 'slow-cooked'],
    ['Balochi Rosh', 'بلوچی روش', 'mutton', 'roast'],
    ['Landhi Keto Style', 'کیٹو لنڈھی', 'mutton', 'roast'],
    ['Balochi Fish', 'بلوچی مچھلی', 'fish', 'grill'],
    ['Khaddi Kebab', 'کھڈی کباب', 'mutton', 'grill'],
    ['Balochi Chicken Karahi', 'بلوچی چکن کڑاہی', 'chicken', 'karahi'],
    ['Abgoosht Keto', 'کیٹو آبگوشت', 'mutton', 'soup'],
    ['Balochi Dumba', 'بلوچی دنبہ', 'mutton', 'roast'],
    ['Mutton Khaddi', 'مٹن کھڈی', 'mutton', 'grill'],
    ['Balochi Tikka', 'بلوچی ٹکہ', 'mutton', 'grill'],
    ['Desert Spiced Chicken', 'صحرائی چکن', 'chicken', 'roast'],
    ['Balochi Meat Stew', 'بلوچی گوشتی اسٹیو', 'beef', 'slow-cooked'],
    ['Rock Salt Fish', 'پتھر نمک مچھلی', 'fish', 'grill'],
    ['Balochi Keema', 'بلوچی قیمہ', 'beef', 'curry'],
    ['Camel Meat Keto', 'کیٹو اونٹ کا گوشت', 'beef', 'roast'],
    ['Balochi Vegetable Stew', 'بلوچی سبزی اسٹیو', 'vegetable', 'slow-cooked'],
    ['Balochi Chicken Soup', 'بلوچی چکن سوپ', 'chicken', 'soup'],
    ['Balochi Mutton Chops', 'بلوچی مٹن چاپس', 'mutton', 'grill'],
    ['Balochi Egg Curry', 'بلوچی انڈا کری', 'egg', 'curry'],
    ['Balochi Raita', 'بلوچی رائتہ', 'vegetable', 'salad'],
    ['Balochi BBQ Platter', 'بلوچی BBQ پلیٹر', 'mixed', 'grill'],
    ['Balochi Bone Broth', 'بلوچی یخنی', 'mutton', 'soup'],
  ],
};

const PROTEIN_AILMENTS = {
  chicken: ['diabetic', 'gastric', 'cardiac'],
  mutton: ['joint', 'thyroid', 'cardiac'],
  beef: ['thyroid', 'gyne', 'joint'],
  fish: ['cardiac', 'psyche', 'joint'],
  prawn: ['cardiac', 'thyroid', 'liver'],
  egg: ['gastric', 'liver', 'psyche'],
  paneer: ['gyne', 'gastric', 'thyroid'],
  vegetable: ['diabetic', 'gastric', 'liver'],
  mixed: ['diabetic', 'cardiac', 'joint'],
};

const STYLE_MACROS = {
  grill: { calories: 310, protein: 38, fat: 18, carbs: 3, fiber: 0 },
  karahi: { calories: 340, protein: 32, fat: 22, carbs: 5, fiber: 1 },
  curry: { calories: 290, protein: 28, fat: 18, carbs: 6, fiber: 2 },
  'slow-cooked': { calories: 350, protein: 30, fat: 24, carbs: 4, fiber: 1 },
  soup: { calories: 180, protein: 18, fat: 10, carbs: 4, fiber: 1 },
  roast: { calories: 320, protein: 36, fat: 18, carbs: 2, fiber: 0 },
  'stir-fry': { calories: 270, protein: 30, fat: 14, carbs: 6, fiber: 2 },
  salad: { calories: 120, protein: 8, fat: 9, carbs: 4, fiber: 2 },
  biryani: { calories: 360, protein: 30, fat: 20, carbs: 8, fiber: 4 },
  wrap: { calories: 380, protein: 32, fat: 22, carbs: 5, fiber: 2 },
  bowl: { calories: 400, protein: 35, fat: 24, carbs: 6, fiber: 2 },
  handi: { calories: 330, protein: 30, fat: 20, carbs: 5, fiber: 1 },
  steam: { calories: 220, protein: 32, fat: 8, carbs: 3, fiber: 0 },
  sauce: { calories: 300, protein: 28, fat: 20, carbs: 5, fiber: 1 },
  bake: { calories: 310, protein: 26, fat: 20, carbs: 6, fiber: 2 },
  breakfast: { calories: 280, protein: 18, fat: 20, carbs: 4, fiber: 1 },
  dessert: { calories: 150, protein: 6, fat: 12, carbs: 3, fiber: 0 },
  bread: { calories: 200, protein: 10, fat: 16, carbs: 4, fiber: 3 },
  snack: { calories: 250, protein: 16, fat: 18, carbs: 4, fiber: 1 },
  dal: { calories: 190, protein: 12, fat: 12, carbs: 6, fiber: 4 },
  drink: { calories: 130, protein: 6, fat: 10, carbs: 3, fiber: 0 },
  fry: { calories: 300, protein: 28, fat: 18, carbs: 4, fiber: 1 },
};

const PROTEIN_ING = {
  chicken: { en: '500g chicken', ur: '500 گرام چکن' },
  mutton: { en: '500g mutton', ur: '500 گرام بکرے کا گوشت' },
  beef: { en: '500g beef', ur: '500 گرام گوشت' },
  fish: { en: '400g fish fillets', ur: '400 گرام مچھلی' },
  prawn: { en: '300g prawns', ur: '300 گرام جھینگا' },
  egg: { en: '4 large eggs', ur: '4 بڑے انڈے' },
  paneer: { en: '250g paneer', ur: '250 گرام پنیر' },
  vegetable: { en: 'Mixed low-carb vegetables', ur: 'کم کارب سبزیاں' },
  mixed: { en: 'Assorted meats and vegetables', ur: 'مختلف گوشت اور سبزیاں' },
};

function slugify(name) {
  return name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
}

function pickAilments(protein, style, index) {
  const base = PROTEIN_AILMENTS[protein] || PROTEIN_AILMENTS.chicken;
  const extra = AILMENTS[index % AILMENTS.length];
  const set = new Set([...base.slice(0, 2), extra]);
  if (style === 'soup') set.add('gastric');
  if (style === 'salad') set.add('liver');
  if (style === 'biryani') set.add('diabetic');
  return [...set].slice(0, 3);
}

function buildRecipe(cuisine, [titleEn, titleUr, protein, style], index) {
  const id = `keto-${cuisine}-${slugify(titleEn)}`;
  const macros = STYLE_MACROS[style] || STYLE_MACROS.curry;
  const jitter = (index % 5) * 8;
  const ailments = pickAilments(protein, style, index);
  const proteinIng = PROTEIN_ING[protein];

  return {
    id,
    title: { en: titleEn, ur: titleUr },
    cuisine,
    ailments,
    description: {
      en: `Authentic ${cuisine} ${titleEn.replace(/^Keto /, '')} adapted for ketogenic healing — low carb, high healthy fat, zero sugar. Supports ${ailments.join(', ')} wellness.`,
      ur: `اصلی ${titleUr} کیٹوجینک شفا کے لیے — کم کارب، صحت مند چکنائی، بغیر چینی۔ ${ailments.length} بیماریوں کی صحت میں مدد۔`,
    },
    ingredients: [
      proteinIng,
      { en: '2 tbsp ghee or coconut oil', ur: '2 چمچ گھی یا ناریل کا تیل' },
      { en: '1 tbsp ginger-garlic paste', ur: '1 چمچ ادرک لہسن پیسٹ' },
      { en: '1 tsp turmeric, cumin, garam masala', ur: '1 چمچ ہلدی، زیرہ، گرم مصالحہ' },
      { en: 'Salt and pepper to taste', ur: 'نمک کالی مرچ حسب ذائقہ' },
      { en: 'Fresh coriander for garnish', ur: 'سجاوٹ کے لیے تازہ دھنیا' },
    ],
    instructions: [
      { en: `Prepare ${protein} and marinate with spices and yogurt 30 minutes.`, ur: `${proteinIng.ur} تیار کریں، مصالحے دہی میں 30 منٹ میرینیٹ۔` },
      { en: `Cook using ${style} method with ghee on medium heat.`, ur: `گھی میں درمیانی آگ پر ${style} طریقے سے پکائیں۔` },
      { en: 'Add desi spices — turmeric, cumin, coriander for healing benefits.', ur: 'دیسی مصالحے ڈالیں — ہلدی، زیرہ، دھنیا شفا کے لیے۔' },
      { en: 'Serve hot with keto raita or cucumber salad. No roti or rice.', ur: 'گرم پیش کریں کیٹو رائتہ یا کھیرا سلاد۔ روٹی چاول نہیں۔' },
    ],
    macros: {
      calories: macros.calories + jitter,
      protein: macros.protein + (index % 3),
      fat: macros.fat + (index % 4),
      carbs: macros.carbs,
      fiber: macros.fiber,
    },
    prepTime: 10 + (index % 15),
    cookTime: 15 + (index % 25),
    servings: 3 + (index % 3),
    healingNotes: {
      en: `Keto-adapted ${cuisine} dish rich in anti-inflammatory spices. Turmeric and ginger support joint and gastric health. Low net carbs prevent blood sugar spikes for diabetics.`,
      ur: `کیٹو ${cuisine} کھانا سوزش مخالف مصالحوں سے بھرپور۔ ہلدی ادرک جوڑوں اور معدے کی صحت۔ کم نیٹ کارب ذیابیطس میں شوگر اسپائک روکتا ہے۔`,
    },
    tags: ['keto', cuisine, style, protein],
  };
}

const allRecipes = [];
for (const [cuisine, dishes] of Object.entries(CUISINE_DISHES)) {
  dishes.forEach((dish, i) => allRecipes.push(buildRecipe(cuisine, dish, i)));
}

const output = `// AUTO-GENERATED by scripts/generate-recipes.mjs — ${allRecipes.length} recipes
import type { Recipe } from '../types';

export const generatedRecipes: Recipe[] = ${JSON.stringify(allRecipes, null, 2)} as Recipe[];
`;

const outPath = join(__dirname, '../src/data/generatedRecipes.ts');
writeFileSync(outPath, output);
console.log(`Generated ${allRecipes.length} recipes → ${outPath}`);
