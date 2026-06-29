export interface Posture {
  id: string;
  nameUrdu: string;
  nameEnglish: string;
  category: string;
  categoryUrdu: string;
  description: string;
  benefits: string;
  tips: string;
  difficulty: 'آسان' | 'درمیانہ' | 'مشکل';
  illustration: string;
  videoUrl: string;
  videoCaptionUrdu: string;
}

export const categories = [
  { id: 'basic', nameUrdu: 'بنیادی', nameEnglish: 'Basic' },
  { id: 'balanced', nameUrdu: 'متوازن', nameEnglish: 'Balanced' },
  { id: 'intimate', nameUrdu: 'گہری قربت', nameEnglish: 'Deep Intimacy' },
  { id: 'comfort', nameUrdu: 'آرام دہ', nameEnglish: 'Comfortable' },
];

export const postures: Posture[] = [
  {
    id: 'missionary',
    nameUrdu: 'مشترکہ وضع',
    nameEnglish: 'Missionary',
    category: 'basic',
    categoryUrdu: 'بنیادی',
    description:
      'یہ سب سے عام اور قدیم وضع ہے جس میں ایک شریک پیٹ کے بل لیٹا ہوتا ہے اور دوسرا اوپر ہوتا ہے۔ چہرے سے چہرہ ملاقات سے جذباتی قربت بڑھتی ہے۔ گردن اور کندھوں کو نرم رکھیں، آنکھوں میں دیکھیں، اور سانسوں کو ہم آہنگ کریں۔',
    benefits:
      'زیادہ جذباتی رابطہ، آسان مواصلات، نرم رفتار کے لیے موزوں۔ حاملہ خواتین کے لیے محتاط زاویہ میں آرام دہ ہو سکتا ہے۔',
    tips:
      'تکیے کے نیچے کولہے اٹھائیں تاکہ زاویہ بہتر ہو۔ ہاتھوں سے پیٹ، کمر اور پیروں کو سہارا دیں۔ رفتار آہستہ سے شروع کریں۔',
    difficulty: 'آسان',
    illustration: 'missionary',
    videoUrl: 'videos/missionary.mp4',
    videoCaptionUrdu: 'مشترکہ وضع کی عملی مثال — آہستہ ہم آہنگ حرکت دکھائی گئی ہے',
  },
  {
    id: 'spooning',
    nameUrdu: 'چمچے کی وضع',
    nameEnglish: 'Spooning',
    category: 'comfort',
    categoryUrdu: 'آرام دہ',
    description:
      'دونوں شریک ایک ہی سمت لیٹے ہوتے ہیں، جیسے دو چمچے ایک دوسرے میں ملے ہوں۔ پیچھے والے شریک نے سامنے والے کو گلے لگایا ہوتا ہے۔ یہ وضع تھکاوٹ کے بعد یا سونے سے پہلے بہت آرام دہ ہے۔',
    benefits:
      'کم جسمانی محنت، گرمائی اور قربت، لمبی مدت کے لیے سہولت، پیٹ کے بل لیٹنے سے بچاؤ۔',
    tips:
      'گھٹنے کے درمیان تکیہ رکھیں۔ اوپر والا پیر ہلکا سا اٹھائیں۔ ہاتھوں سے سینے یا پیٹ کو نرم چھوئیں۔',
    difficulty: 'آسان',
    illustration: 'spooning',
    videoUrl: 'videos/spooning.mp4',
    videoCaptionUrdu: 'چمچے کی وضع — پہلو کے بل قریب بیٹھنے کا طریقہ',
  },
  {
    id: 'lotus',
    nameUrdu: 'کمل کی وضع',
    nameEnglish: 'Lotus',
    category: 'intimate',
    categoryUrdu: 'گہری قربت',
    description:
      'دونوں شریک سامنے آمنے سامنے بیٹھے ہوتے ہیں اور ایک دوسرے کو گلے لگاتے ہیں۔ ٹانگیں ایک دوسرے کے گرد لپٹی ہوتی ہیں۔ یہ وضع قدیم ہندوستانی متون میں گہری روحانی اور جسمانی یکجہتی کی نمائندگی کرتی ہے۔',
    benefits:
      'زیادہ آنکھوں سے آنکھیں ملاقات، گہری سانسیں، دل کی دھڑکن محسوس کرنا، جذباتی بانڈ مضبوط۔',
    tips:
      'اگر گھٹنے میں درد ہو تو تکیے استعمال کریں۔ کمر سیدھی رکھیں۔ وزن یکساں تقسیم کریں۔',
    difficulty: 'درمیانہ',
    illustration: 'lotus',
    videoUrl: 'videos/lotus.mp4',
    videoCaptionUrdu: 'کمل کی وضع — سامنے بیٹھ کر گلے ملنے کی مثال',
  },
  {
    id: 'cowgirl',
    nameUrdu: 'سواری کی وضع',
    nameEnglish: 'Cowgirl',
    category: 'balanced',
    categoryUrdu: 'متوازن',
    description:
      'ایک شریک پیٹ کے بل لیٹا ہے اور دوسرا اوپر بیٹھ کر حرکت کرتا ہے۔ اوپر والا شریک رفتار اور گہرائی کنٹرول کرتا ہے۔ یہ وضع مساوات اور خود مختاری کو فروغ دیتی ہے۔',
    benefits:
      'اوپر والے شریک کو کنٹرول، نیچے والے کے لیے کم محنت، مختلف زاویے آزمانے کی سہولت۔',
    tips:
      'ہاتھوں کو سینے یا بستر پر سہارا دیں۔ آہستہ گھومنے سے زاویہ بدلیں۔ بات چیت سے رضامندی برقرار رکھیں۔',
    difficulty: 'درمیانہ',
    illustration: 'cowgirl',
    videoUrl: 'videos/cowgirl.mp4',
    videoCaptionUrdu: 'سواری کی وضع — اوپر والے شریک کی کنٹرول شدہ حرکت',
  },
  {
    id: 'side-by-side',
    nameUrdu: 'پہلو بہ پہلو',
    nameEnglish: 'Side by Side',
    category: 'comfort',
    categoryUrdu: 'آرام دہ',
    description:
      'دونوں شریک پہلو کے بل ایک دوسرے کے سامنے لیٹے ہوتے ہیں۔ ایک ٹانگ اوپر والی شریک کے درمیان ہوتی ہے۔ یہ وضع باہمی احترام اور آہستہ قربت کے لیے بہترین ہے۔',
    benefits:
      'کمر پر کم دباؤ، چہرے سے چہرہ قریب، ہاتھ آزاد، حاملگی کے دوران محتاط استعمال ممکن۔',
    tips:
      'نیچے والی ٹانگ سیدھی رکھیں۔ اوپر والی ٹانگ ہلکی موڑ میں۔ کولہے کے نیچے چھوٹا تکیہ مددگار ہے۔',
    difficulty: 'آسان',
    illustration: 'side',
    videoUrl: 'videos/side-by-side.mp4',
    videoCaptionUrdu: 'پہلو بہ پہلو — آمنے سامنے لیٹنے کی وضع',
  },
  {
    id: 'standing',
    nameUrdu: 'کھڑے ہوئے',
    nameEnglish: 'Standing Supported',
    category: 'balanced',
    categoryUrdu: 'متوازن',
    description:
      'ایک شریک دیوار یا فرنیچر کے سہارے کھڑا ہوتا ہے اور دوسرا سامنے یا پیچھے سے قریب ہوتا ہے۔ یہ وضع جذبے اور فوریت کے لیے ہے مگر توازن ضروری ہے۔',
    benefits:
      'مختلف تجربہ، کم جگہ میں ممکن، جسمانی طاقت کا استعمال، تازگی۔',
    tips:
      'ہمیشہ مضبوط سہارا استعمال کریں۔ پھسلن سے بچنے کے لیے نرم سطح۔ تھکاوٹ محسوس ہو تو فوراً وضع بدلیں۔',
    difficulty: 'مشکل',
    illustration: 'standing',
    videoUrl: 'videos/standing.mp4',
    videoCaptionUrdu: 'کھڑے ہوئے — دیوار کے سہارے توازن برقرار رکھیں',
  },
  {
    id: 'doggy',
    nameUrdu: 'چار پایوں پر',
    nameEnglish: 'All Fours',
    category: 'basic',
    categoryUrdu: 'بنیادی',
    description:
      'ایک شریک چار پایوں پر ہوتا ہے اور دوسرا پیچھے سے قریب ہوتا ہے۔ یہ قدیم متون میں فطری حرکت اور گہرائی کی وضع کے طور پر بیان ہوتی ہے۔ کمر سیدھی رکھنا ضروری ہے۔',
    benefits:
      'گہرائی کا کنٹرول، کمر کے لیے مختلف زاویہ، ہاتھ آزاد۔',
    tips:
      'گھٹنے کے نیچے تکیہ رکھیں۔ کمر نہ جھکائیں۔ باقاعدہ وقفے لیں اور بات چیت کریں۔',
    difficulty: 'درمیانہ',
    illustration: 'doggy',
    videoUrl: 'videos/doggy.mp4',
    videoCaptionUrdu: 'چار پایوں پر — کمر سیدھی اور آہستہ رفتار',
  },
  {
    id: 'reverse-cowgirl',
    nameUrdu: 'الٹ سواری',
    nameEnglish: 'Reverse Seated',
    category: 'balanced',
    categoryUrdu: 'متوازن',
    description:
      'اوپر والا شریک نیچے والے کی طرف پیٹھ کر کے بیٹھا ہوتا ہے۔ یہ وضع مختلف محسوسات اور زاویے فراہم کرتی ہے۔ احتیاط اور آہستہ آغاز ضروری ہے۔',
    benefits:
      'نئی محسوسات، اوپر والے کو کنٹرول، مختلف گہرائی۔',
    tips:
      'ہاتھوں سے سہارا لیں۔ آہستہ حرکت کریں۔ اگر تکلیف ہو تو فوراً رک جائیں۔',
    difficulty: 'مشکل',
    illustration: 'reverse',
    videoUrl: 'videos/reverse-cowgirl.mp4',
    videoCaptionUrdu: 'الٹ سواری — پیٹھ کی طرف بیٹھنے کی مثال',
  },
  {
    id: 'butterfly',
    nameUrdu: 'تتلی کی وضع',
    nameEnglish: 'Butterfly',
    category: 'intimate',
    categoryUrdu: 'گہری قربت',
    description:
      'نیچے والا شریک کمر کے بل لیٹا ہوتا ہے اور ٹانگیں اوپر اٹھی ہوتی ہیں۔ اوپر والا سامنے سے قریب ہوتا ہے۔ میز یا بستر کے کنارے پر یہ وضع آسان ہو جاتی ہے۔',
    benefits:
      'گہرائی، آنکھوں سے ملاقات، ٹانگوں کی لچک استعمال۔',
    tips:
      'ٹانگوں کو نرم سہارا دیں۔ کولہے کے نیچے تکیہ۔ زیادہ دیر تک نہ رکھیں اگر خون کا بہاؤ محسوس ہو۔',
    difficulty: 'درمیانہ',
    illustration: 'butterfly',
    videoUrl: 'videos/butterfly.mp4',
    videoCaptionUrdu: 'تتلی کی وضع — اٹھی ہوئی ٹانگوں کے ساتھ',
  },
  {
    id: 'yab-yum',
    nameUrdu: 'یاب یوم',
    nameEnglish: 'Yab Yum',
    category: 'intimate',
    categoryUrdu: 'گہری قربت',
    description:
      'تانترا اور قدیم متون کی مشہور وضع: ایک شریک بیٹھا ہوتا ہے اور دوسرا اس کی گود میں سامنے بیٹھتا ہے۔ سانسیں، آنکھیں اور دل کی دھڑکن ایک ساتھ محسوس ہوتی ہے۔',
    benefits:
      'روحانی اور جسمانی یکجہتی، گہری قربت، آہستہ رفتار، توانائی کا تبادلہ۔',
    tips:
      'پہلے گہری سانسیں لیں۔ کمر سیدھی۔ آہستہ حرکت سے شروع کریں۔ خاموشی میں بھی رابطہ برقرار رکھیں۔',
    difficulty: 'درمیانہ',
    illustration: 'yabyum',
    videoUrl: 'videos/yab-yum.mp4',
    videoCaptionUrdu: 'یاب یوم — گود میں سامنے بیٹھنے کی روایتی وضع',
  },
  {
    id: 'scissors',
    nameUrdu: 'قینچی کی وضع',
    nameEnglish: 'Scissors',
    category: 'comfort',
    categoryUrdu: 'آرام دہ',
    description:
      'دونوں شریک سامنے آمنے سامنے لیٹے ہوتے ہیں اور ٹانگیں ایک دوسرے کے اوپر کراس ہوتی ہیں۔ یہ وضع مساوات اور باہمی قربت کو ظاہر کرتی ہے۔',
    benefits:
      'مساوی شرکت، کم محنت، چہرے سے چہرہ قریب، ہاتھوں کی آزادی۔',
    tips:
      'تکیے استعمال کریں۔ ٹانگیں زیادہ نہ اٹھائیں اگر درد ہو۔ آرام سے رفتار مقرر کریں۔',
    difficulty: 'آسان',
    illustration: 'scissors',
    videoUrl: 'videos/scissors.mp4',
    videoCaptionUrdu: 'قینچی کی وضع — کراس ٹانگوں کے ساتھ مساوی شرکت',
  },
  {
    id: 'bridge',
    nameUrdu: 'پل کی وضع',
    nameEnglish: 'Bridge',
    category: 'balanced',
    categoryUrdu: 'متوازن',
    description:
      'نیچے والا شریک کولہے اٹھا کر پل بناتا ہے۔ یہ وضع کمر اور ران کی طاقت استعمال کرتی ہے۔ صرف تندرست جوڑوں کے لیے تجویز ہے۔',
    benefits:
      'کمر کی مضبوطی، مختلف زاویہ، گہرائی۔',
    tips:
      'کولہے کے نیچے تکیہ رکھ سکتے ہیں۔ زیادہ دیر نہ رکھیں۔ کمر میں درد ہو تو فوراً چھوڑ دیں۔',
    difficulty: 'مشکل',
    illustration: 'bridge',
    videoUrl: 'videos/bridge.mp4',
    videoCaptionUrdu: 'پل کی وضع — کولہے اٹھا کر پل بنانے کی مثال',
  },
];
