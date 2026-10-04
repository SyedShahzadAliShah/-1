package com.neduet.mt331lecture.data.mt331

object Mt331LectureRepository {

    fun getChapters(): List<LectureChapter> = chapters

    fun getChapterById(id: String): LectureChapter? = chapters.find { it.id == id }

    private fun beat(
        id: String,
        glyph: String,
        titleEn: String,
        titleUr: String,
        narrationEn: String,
        narrationUr: String,
        formulaEn: String = "",
        formulaUr: String = ""
    ) = LectureBeat(
        id = id,
        glyph = glyph,
        titleEn = titleEn,
        titleUr = titleUr,
        narrationEn = narrationEn,
        narrationUr = narrationUr,
        formulaEn = formulaEn,
        formulaUr = formulaUr
    )

    private val chapters = listOf(
        LectureChapter(
            id = "ch1_intro",
            chapterNumber = 1,
            titleEn = "Introduction to Statistics",
            titleUr = "شماریات کا تعارف",
            taglineEn = "Population, sample, and descriptive measures",
            taglineUr = "آبادی، نمونہ، اور تفصیلی پیمانے",
            beats = listOf(
                beat(
                    "ch1_pop_sample",
                    "📊",
                    "Population versus sample",
                    "آبادی بمقابلہ نمونہ",
                    "The population is the entire group we study, described by parameters mu and sigma squared. " +
                        "A sample is a subset of size n, summarized by statistics such as x-bar and s squared.",
                    "آبادی وہ مکمل گروہ ہے جس پر مطالعہ ہوتا ہے اور اسے پیرامیٹرز مائیو اور سگما اسکوائر سے بیان کیا جاتا ہے۔ " +
                        "نمونہ آبادی کا ایک ذیلی حصہ ہے جس کا حجم n ہوتا ہے اور اسے اعداد x-bar اور s squared جیسے شماریات سے بیان کیا جاتا ہے۔",
                    "N, μ, σ²  |  n, x̄, s²",
                    "N، μ، σ²  |  n، x̄، s²"
                ),
                beat(
                    "ch1_location",
                    "📍",
                    "Measures of central tendency",
                    "مرکزی رجحان کے پیمانے",
                    "The mean is the arithmetic average and is sensitive to outliers. " +
                        "The median is the middle value after sorting and resists outliers. " +
                        "The mode is the most frequent observation and may be unimodal or multimodal.",
                    "میان اوسط حسابی اوسط ہے اور غیر معمولی قدریں اسے متاثر کرتی ہیں۔ " +
                        "درمیانی قدر ترتیب کے بعد درمیان والی قیمت ہے اور غیر معمولی قدریں اسے کم متاثر کرتی ہیں۔ " +
                        "نمونہ سب سے زیادہ بار آنے والی قدر ہے جو یک نمائی یا کثیر نمائی ہو سکتی ہے۔",
                    "x̄ = (1/n)Σxᵢ",
                    "x̄ = (1/n)Σxᵢ"
                ),
                beat(
                    "ch1_spread",
                    "↔",
                    "Measures of variability",
                    "تغیر پذیری کے پیمانے",
                    "Sample variance divides the sum of squared deviations by n minus one for unbiased estimation. " +
                        "Standard deviation s is the square root of variance and shares the original data units.",
                    "نمونے کی variance مربع انحرافات کے مجموعے کو n منفی ایک سے تقسیم کرتی ہے تاکہ غیر جانبدار تخمینہ حاصل ہو۔ " +
                        "معیاری انحراف s variance کا مربع جذر ہے اور اصل ڈیٹا کی اکائیوں میں ہوتا ہے۔",
                    "s² = Σ(xᵢ−x̄)²/(n−1),  s = √s²",
                    "s² = Σ(xᵢ−x̄)²/(n−1)،  s = √s²"
                )
            )
        ),
        LectureChapter(
            id = "ch2_probability",
            chapterNumber = 2,
            titleEn = "Probability Concepts & Rules",
            titleUr = "احتمال کے تصورات اور قواعد",
            taglineEn = "Events, Venn logic, addition, multiplication, Bayes",
            taglineUr = "واقعات، Venn منطق، جمع، ضرب، بائیز",
            beats = listOf(
                beat(
                    "ch2_space",
                    "🎲",
                    "Sample space and events",
                    "نمونہ فضا اور واقعات",
                    "The sample space S lists all possible outcomes. An event A is any subset of S. " +
                        "Mutually exclusive events share no outcomes, so the intersection is empty.",
                    "نمونہ فضا S تمام ممکنہ نتائج کی فہرست ہے۔ واقعہ A، S کا کوئی بھی ذیلی مجموعہ ہے۔ " +
                        "باہم متناقض واقعات میں مشترک نتیجہ نہیں ہوتا، اس لیے اشتراک خالی ہوتا ہے۔",
                    "0 ≤ P(A) ≤ 1,  P(S) = 1",
                    "0 ≤ P(A) ≤ 1،  P(S) = 1"
                ),
                beat(
                    "ch2_rules",
                    "∪∩",
                    "Addition and multiplication",
                    "جمع اور ضرب کے قواعد",
                    "For any events A and B, P of A union B equals P(A) plus P(B) minus P of A intersect B. " +
                        "Conditional probability P(B given A) equals P of A intersect B divided by P(A). " +
                        "Independent events satisfy P of A intersect B equals P(A) times P(B).",
                    "کسی بھی واقعات A اور B کے لیے P(A ∪ B) = P(A) + P(B) − P(A ∩ B)۔ " +
                        "مشروط احتمال P(B|A) = P(A ∩ B)/P(A)۔ " +
                        "مستقل واقعات میں P(A ∩ B) = P(A)·P(B)۔",
                    "P(A∪B)=P(A)+P(B)−P(A∩B)",
                    "P(A∪B)=P(A)+P(B)−P(A∩B)"
                ),
                beat(
                    "ch2_bayes",
                    "🛡",
                    "Bayes' theorem",
                    "بائیز کا قضیہ",
                    "Bayes' rule reverses conditional probability: update beliefs about a cause after observing an effect. " +
                        "Engineers use it in fault analysis and diagnostic testing.",
                    "بائیز کا اصول مشروط احتمال کو الٹ دیتا ہے: کسی اثر کے مشاہدے کے بعد سبب کے بارے میں یقین کو اپ ڈیٹ کریں۔ " +
                        "انجینئر اسے خرابی کی تشخیص اور ٹیسٹنگ میں استعمال کرتے ہیں۔",
                    "P(Bᵣ|A) = P(Bᵣ)P(A|Bᵣ) / Σ P(Bᵢ)P(A|Bᵢ)",
                    "P(Bᵣ|A) = P(Bᵣ)P(A|Bᵣ) / Σ P(Bᵢ)P(A|Bᵢ)"
                )
            )
        ),
        LectureChapter(
            id = "ch3_rv",
            chapterNumber = 3,
            titleEn = "Random Variables & Distributions",
            titleUr = "تصادفی متغیرات اور تقسیمات",
            taglineEn = "Discrete pmf, continuous pdf, CDF, joint models",
            taglineUr = "مجرد pmf، مسلسل pdf، CDF، مشترکہ ماڈل",
            beats = listOf(
                beat(
                    "ch3_types",
                    "🔢",
                    "Discrete versus continuous",
                    "مجرد بمقابلہ مسلسل",
                    "A random variable maps each outcome to a real number. Discrete variables have countable values with a pmf. " +
                        "Continuous variables take values on an interval with a pdf; point probability at any exact value is zero.",
                    "تصادفی متغیر ہر نتیجے کو حقیقی عدد سے جوڑتا ہے۔ مجرد متغیرات قابل شمار قدریں اور pmf رکھتے ہیں۔ " +
                        "مسلسل متغیرات وقفے پر قدریں لیتے ہیں اور pdf رکھتے ہیں؛ کسی ایک نقطے پر احتمال صفر ہے۔",
                    "Σf(x)=1  |  ∫f(x)dx=1",
                    "Σf(x)=1  |  ∫f(x)dx=1"
                ),
                beat(
                    "ch3_cdf",
                    "📈",
                    "CDF and marginal distributions",
                    "CDF اور حاشیہ تقسیمات",
                    "The cumulative distribution F(x) gives P(X ≤ x). From a joint distribution, marginals sum or integrate out the other variable. " +
                        "Variables are independent when the joint density factors into the product of marginals.",
                    "مجموعی تقسیم F(x)، P(X ≤ x) دیتی ہے۔ مشترکہ تقسیم سے حاشیہ تقسیم دوسرے متغیر کو جمع یا انٹیگرٹ کر کے نکالتے ہیں۔ " +
                        "متغیرات مستقل ہوتے ہیں جب مشترکہ کثافت حاشیہ تقسیمات کے حاصل ضرب بن جائے۔",
                    "F(x)=P(X≤x)",
                    "F(x)=P(X≤x)"
                )
            )
        ),
        LectureChapter(
            id = "ch4_expectation",
            chapterNumber = 4,
            titleEn = "Mathematical Expectation",
            titleUr = "ریاضیاتی توقع",
            taglineEn = "Mean, variance, covariance rules",
            taglineUr = "میان، variance، covariance کے قواعد",
            beats = listOf(
                beat(
                    "ch4_mean_var",
                    "⚖",
                    "Expected value and variance",
                    "متوقع قدر اور variance",
                    "The expected value is the probability-weighted center of a distribution. " +
                        "Variance measures squared deviation from the mean and can be computed as E(X squared) minus E(X) squared.",
                    "متوقع قدر تقسیم کا احتمالی وزن والا مرکز ہے۔ " +
                        "variance میان سے مربع انحراف کی پیمائش ہے اور E(X²) − [E(X)]² سے بھی حاصل ہو سکتی ہے۔",
                    "μ=E(X),  σ²=V(X)=E(X²)−[E(X)]²",
                    "μ=E(X)،  σ²=V(X)=E(X²)−[E(X)]²"
                ),
                beat(
                    "ch4_rules",
                    "➕",
                    "Linearity and covariance",
                    "خطییت اور covariance",
                    "Expectation is linear: E(aX+b)=aE(X)+b and E(X+Y)=E(X)+E(Y). " +
                        "Variance scales with a squared factor. Covariance is zero when X and Y are independent.",
                    "توقع خطی ہے: E(aX+b)=aE(X)+b اور E(X+Y)=E(X)+E(Y)۔ " +
                        "variance a² کے عامل سے بدلتی ہے۔ X اور Y مستقل ہوں تو covariance صفر ہوتی ہے۔",
                    "Cov(X,Y)=E(XY)−μₓμᵧ",
                    "Cov(X,Y)=E(XY)−μₓμᵧ"
                )
            )
        ),
        LectureChapter(
            id = "ch5_discrete",
            chapterNumber = 5,
            titleEn = "Discrete Probability Distributions",
            titleUr = "مجرد احتمالی تقسیمات",
            taglineEn = "Binomial, multinomial, hypergeometric, Poisson",
            taglineUr = "دو جزوی، کثیر جزوی، ہائپرجیومیٹرک، پوآسن",
            beats = listOf(
                beat(
                    "ch5_binomial",
                    "🎯",
                    "Binomial and multinomial",
                    "دو جزوی اور کثیر جزوی",
                    "Binomial models n independent Bernoulli trials with constant success probability p. " +
                        "Multinomial extends this to more than two categories with probabilities that sum to one.",
                    "دو جزوی تقسیم n مستقل برنولی آزمائشوں کو مستقل کامیابی کے احتمال p کے ساتھ ماڈل کرتی ہے۔ " +
                        "کثیر جزوی تقسیم اسے دو سے زیادہ زمروں پر بڑھاتی ہے جہاں احتمالات کا مجموعہ ایک ہے۔",
                    "μ=np, σ²=npq",
                    "μ=np، σ²=npq"
                ),
                beat(
                    "ch5_hyper_pois",
                    "⏱",
                    "Hypergeometric and Poisson",
                    "ہائپرجیومیٹرک اور پوآسن",
                    "Hypergeometric sampling is without replacement from a finite population. " +
                        "Poisson counts rare events in time or space; its mean equals its variance lambda t.",
                    "ہائپرجیومیٹرک نمونہ بندی بغیر تبدیلی کے محدود آبادی سے ہوتی ہے۔ " +
                        "پوآسن وقت یا جگہ میں نایاب واقعات گنتا ہے؛ اس کا میان variance λt کے برابر ہے۔",
                    "P(X=x)=e^(−λt)(λt)^x/x!",
                    "P(X=x)=e^(−λt)(λt)^x/x!"
                )
            )
        ),
        LectureChapter(
            id = "ch6_continuous",
            chapterNumber = 6,
            titleEn = "Continuous Distributions",
            titleUr = "مسلسل تقسیمات",
            taglineEn = "Uniform, normal, exponential, gamma",
            taglineUr = "یکساں، نارمل، exponential، gamma",
            beats = listOf(
                beat(
                    "ch6_normal",
                    "🔔",
                    "Normal distribution",
                    "نارمل تقسیم",
                    "The Gaussian curve is symmetric about the mean with total area one. " +
                        "The empirical rule gives about sixty-eight, ninety-five, and ninety-nine point seven percent within one, two, and three standard deviations.",
                    "گاؤسین منحنی میان کے گرد متناسب ہے اور کل رقبہ ایک ہے۔ " +
                        "تجرباتی قاعدہ ایک، دو، اور تین معیاری انحراف کے اندر تقریباً 68، 95، اور 99.7 فیصد دیتا ہے۔",
                    "Z=(X−μ)/σ",
                    "Z=(X−μ)/σ"
                ),
                beat(
                    "ch6_approx",
                    "⭐",
                    "Normal approximation to binomial",
                    "دو جزوی کی نارمل تقریب",
                    "When n is large and np and nq are at least five, approximate binomial probabilities with a normal curve. " +
                        "Apply continuity correction by shifting discrete counts by one half.",
                    "جب n بڑا ہو اور np اور nq کم از کم پانچ ہوں تو دو جزوی احتمالات کو نارمل منحنی سے تقریب دیں۔ " +
                        "تسلسل کی اصلاح کے لیے مجرد شمار کو آدھے سے شفٹ کریں۔",
                    "Z=(X±0.5−np)/√(npq)",
                    "Z=(X±0.5−np)/√(npq)"
                ),
                beat(
                    "ch6_exp",
                    "⏳",
                    "Exponential and gamma",
                    "exponential اور gamma",
                    "Exponential models waiting time between Poisson events with mean beta. " +
                        "Its survival probability P(X>x) equals e to the minus x over beta. Gamma generalizes waiting for the alpha-th event.",
                    "exponential پوآسن واقعات کے درمیان انتظار کا وقت ماڈل کرتا ہے جس کا میان β ہے۔ " +
                        "P(X>x)=e^(−x/β)۔ gamma تقسیم αویں واقعہ تک انتظار کو عام کرتی ہے۔",
                    "P(X>x)=e^(−x/β)",
                    "P(X>x)=e^(−x/β)"
                )
            )
        ),
        LectureChapter(
            id = "ch8_sampling",
            chapterNumber = 8,
            titleEn = "Sampling Distributions & CLT",
            titleUr = "نمونہ تقسیمات اور CLT",
            taglineEn = "Central limit theorem, t, chi-square, F",
            taglineUr = "مرکزی حد نظریہ، t، chi-square، F",
            beats = listOf(
                beat(
                    "ch8_clt",
                    "✨",
                    "Central limit theorem",
                    "مرکزی حد نظریہ",
                    "For large sample size, the sampling distribution of x-bar is approximately normal even if the population is not. " +
                        "The standard error is sigma divided by root n.",
                    "بڑے نمونے کے لیے x-bar کی نمونہ تقسیم تقریباً نارمل ہوتی ہے چاہے آبادی نارمل نہ ہو۔ " +
                        "معیاری خرابی σ/√n ہے۔",
                    "Z=(x̄−μ)/(σ/√n)",
                    "Z=(x̄−μ)/(σ/√n)"
                ),
                beat(
                    "ch8_t_f",
                    "📉",
                    "t, chi-square, and F",
                    "t، chi-square، اور F",
                    "Use Student's t when sigma is unknown and n is small. Chi-square tests variance. " +
                        "The F distribution compares variances of two populations with numerator and denominator degrees of freedom.",
                    "جب σ نامعلوم ہو اور n چھوٹا ہو تو Student's t استعمال کریں۔ chi-square variance کی جانچ کرتا ہے۔ " +
                        "F تقسیم دو آبادیوں کی variance کا موازنہ کرتی ہے۔",
                    "t=(x̄−μ)/(s/√n),  v=n−1",
                    "t=(x̄−μ)/(s/√n)،  v=n−1"
                )
            )
        ),
        LectureChapter(
            id = "ch9_estimation",
            chapterNumber = 9,
            titleEn = "Statistical Estimation",
            titleUr = "شماریاتی تخمینہ",
            taglineEn = "Confidence intervals for means and proportions",
            taglineUr = "میانوں اور تناسب کے اعتماد وقفے",
            beats = listOf(
                beat(
                    "ch9_one_mean",
                    "🎯",
                    "One-sample mean intervals",
                    "یک نمونہ میان کے وقفے",
                    "When variance is known or n is large, use z with x-bar plus minus z alpha over two sigma over root n. " +
                        "When variance is unknown and n is small, replace sigma with s and use the t table with n minus one degrees of freedom.",
                    "جب variance معلوم ہو یا n بڑا ہو تو z استعمال کریں: x̄ ± z_{α/2}·σ/√n۔ " +
                        "جب variance نامعلوم ہو اور n چھوٹا ہو تو σ کی جگہ s رکھیں اور t ٹیبل n−1 ڈگری آزادی سے استعمال کریں۔",
                    "x̄ ± z_{α/2}·σ/√n",
                    "x̄ ± z_{α/2}·σ/√n"
                ),
                beat(
                    "ch9_prop_var",
                    "📐",
                    "Proportions and variance",
                    "تناسب اور variance",
                    "For a sample proportion p-hat, the interval is p-hat plus minus z times root p-hat q-hat over n. " +
                        "Variance intervals use chi-square with n minus one times s squared divided by sigma squared.",
                    "نمونہ تناسب p̂ کے لیے وقفہ p̂ ± z·√(p̂q̂/n)۔ " +
                        "variance کے وقفے chi-square استعمال کرتے ہیں: (n−1)s²/σ²۔",
                    "p̂ ± z·√(p̂q̂/n)",
                    "p̂ ± z·√(p̂q̂/n)"
                )
            )
        ),
        LectureChapter(
            id = "ch10_hypothesis",
            chapterNumber = 10,
            titleEn = "Hypothesis Testing",
            titleUr = "مفروضے کی آزمائش",
            taglineEn = "H0, H1, errors, and test statistics",
            taglineUr = "H0، H1، غلطیاں، اور ٹیسٹ شماریات",
            beats = listOf(
                beat(
                    "ch10_framework",
                    "⚖",
                    "Null and alternative hypotheses",
                    "صفر اور متبادل مفروضے",
                    "H0 is the status quo with equality. H1 is what we seek evidence for. " +
                        "Type I error rejects a true H0 with probability alpha. Type II error fails to reject a false H0 with probability beta.",
                    "H0 موجودہ حالت ہے اور مساوات رکھتا ہے۔ H1 وہ دعویٰ ہے جس کے لیے ثبوت چاہیے۔ " +
                        "قسم I غلطی سچے H0 کو مسترد کرتی ہے جس کا احتمال α ہے۔ قسم II غلطی غلط H0 کو نہ مسترد کرنا ہے جس کا احتمال β ہے۔",
                    "α = P(Type I),  β = P(Type II)",
                    "α = P(قسم I)،  β = P(قسم II)"
                ),
                beat(
                    "ch10_tests",
                    "🧪",
                    "Common test statistics",
                    "عام ٹیسٹ شماریات",
                    "Use z or t for means, z for proportions, chi-square for variance, and F for comparing two variances. " +
                        "Paired t-tests analyze differences on the same subjects before and after treatment.",
                    "میانوں کے لیے z یا t، تناسب کے لیے z، variance کے لیے chi-square، اور دو variance کے موازنہ کے لیے F استعمال کریں۔ " +
                        "جوڑی دار t ٹیسٹ ایک ہی مضامین پر قبل و بعد کے فرق کا تجزیہ کرتا ہے۔",
                    "t=(d̄−d₀)/(s_d/√n)",
                    "t=(d̄−d₀)/(s_d/√n)"
                )
            )
        ),
        LectureChapter(
            id = "ch11_regression",
            chapterNumber = 11,
            titleEn = "Regression & Correlation",
            titleUr = "انحدار اور تعلق",
            taglineEn = "Least squares line and Pearson r",
            taglineUr = "کم از کم مربعات خط اور Pearson r",
            beats = listOf(
                beat(
                    "ch11_ls",
                    "📏",
                    "Least squares regression",
                    "کم از کم مربعات رجgression",
                    "The regression line y-hat equals b0 plus b1 x minimizes sum of squared residuals. " +
                        "Slope b1 can be computed from sums of squares Sxy divided by Sxx.",
                    "رجgression خط ŷ = b₀ + b₁x مربع باقیات کے مجموعے کو کم سے کم کرتا ہے۔ " +
                        "ڈھلوان b₁ کو Sxy/Sxx سے حاصل کیا جا سکتا ہے۔",
                    "b₁=Sxy/Sxx,  b₀=ȳ−b₁x̄",
                    "b₁=Sxy/Sxx،  b₀=ȳ−b₁x̄"
                ),
                beat(
                    "ch11_corr",
                    "🔗",
                    "Pearson correlation",
                    "Pearson correlation",
                    "Correlation r measures linear strength between minus one and plus one. " +
                        "Values near plus or minus one indicate strong linear association; zero means no linear trend.",
                    "correlation r خطی تعلق کی طاقت کو منفی ایک اور مثبت ایک کے درمیان پیمائش کرتا ہے۔ " +
                        "±1 کے قریب مضبوط خطی تعلق؛ صفر کا مطلب کوئی خطی رجحان نہیں۔",
                    "−1 ≤ r ≤ 1",
                    "−1 ≤ r ≤ 1"
                )
            )
        ),
        LectureChapter(
            id = "ch13_anova",
            chapterNumber = 13,
            titleEn = "One-Way ANOVA",
            titleUr = "یک طرفہ ANOVA",
            taglineEn = "Comparing three or more means",
            taglineUr = "تین یا زیادہ میانوں کا موازنہ",
            beats = listOf(
                beat(
                    "ch13_table",
                    "📋",
                    "ANOVA decomposition",
                    "ANOVA کی تقسیم",
                    "ANOVA splits total variation into between-group and within-group components. " +
                        "The F ratio compares mean square treatment to mean square error.",
                    "ANOVA کل تغیر کو گروہوں کے درمیان اور گروہوں کے اندر حصوں میں تقسیم کرتا ہے۔ " +
                        "F تناسب علاج کے اوسط مربع کو غلطی کے اوسط مربع سے موازنہ کرتا ہے۔",
                    "F=MSA/MSE",
                    "F=MSA/MSE"
                )
            )
        ),
        LectureChapter(
            id = "ch16_sqc",
            chapterNumber = 16,
            titleEn = "Statistical Quality Control",
            titleUr = "شماریاتی معیار کنٹرول",
            taglineEn = "X-bar, R charts, and capability",
            taglineUr = "X-bar، R چارٹ، اور capability",
            beats = listOf(
                beat(
                    "ch16_charts",
                    "⚙",
                    "Control charts",
                    "کنٹرول چارٹ",
                    "X-bar charts monitor process centering using limits based on average range. " +
                        "R charts track dispersion. Points outside control limits signal special-cause variation.",
                    "X-bar چارٹ اوسط رینج پر مبنی حدود سے عمل کے مرکز کی نگرانی کرتا ہے۔ " +
                        "R چارٹ پھیلاؤ کو دیکھتا ہے۔ کنٹرول حدود سے باہر نقطے خاص وجہ کی تغیر کی نشانی ہیں۔",
                    "UCL, CL, LCL for X̄ and R",
                    "X̄ اور R کے لیے UCL، CL، LCL"
                ),
                beat(
                    "ch16_cap",
                    "✅",
                    "Process capability",
                    "عمل کی صلاحیت",
                    "Cp compares specification width to six sigma spread. Cpk additionally checks centering within customer limits.",
                    "Cp وضاحتی حدود کی چوڑائی کو چھ سگما پھیلاؤ سے موازنہ کرتا ہے۔ Cpk مرکزیت کو گاہک کی حدود میں بھی جانچتا ہے۔",
                    "Cp=(USL−LSL)/(6σ)",
                    "Cp=(USL−LSL)/(6σ)"
                )
            )
        )
    )
}
