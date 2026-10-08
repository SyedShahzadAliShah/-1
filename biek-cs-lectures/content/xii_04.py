from content.schema import lecture

LECTURE = lecture(
    id="xii-4",
    number=4,
    title="Data, Models, and Hypothesis Tests",
    kicker="CLASS XII  ·  UNIT 4",
    unit="Unit 4 — Data and Analysis",
    domain="D. Data and analysis",
    periods="about 25 periods",
    intro=(
        "Class XI fitted a straight line and refused to call it a cause. Class XII asks how a model learns from examples, "
        "how you tell a good prediction from a flattering one, and how a hypothesis test keeps a lucky pattern from being announced as a discovery. "
        "You also tell the story of a dataset with a chart or a query, not with a single dramatic number."
    ),
    outcomes=[
        "Contrast a rule-based method with machine learning, and describe features, a train-test split, and a metric.",
        "Compute precision from a confusion matrix and say what the number does not mean.",
        "State a null and an alternative hypothesis, and use a p-value against a significance level.",
        "Choose a visualisation or an SQL summary that answers a stated question, and limit the claim.",
    ],
    blocks=[
        ("h2", "Rules and learning"),
        (
            "p",
            "A **rule-based** method follows instructions a person wrote: if attendance is below 75 percent, do not allow the exam; if the mark is at least 40, record a pass. The rule does not change when new rows arrive, unless a person edits it. **Machine learning** builds a model by adjusting it on examples. The model is then used to predict a label for a new row. It is useful when the rule is hard to write by hand, such as “does this photograph look like a cotton leaf with a particular damage?”, and dangerous when people treat the prediction as a cause or as a verdict that nobody may appeal.",
        ),
        (
            "p",
            "A **feature** is an input the model is allowed to see, such as hours of practice or the number of past quizzes attempted. A **label** is the outcome on the training rows, such as pass or fail, or the quiz mark. **Feature engineering** is the work of turning raw records into those inputs: three monthly tests become one average, a date of birth becomes an age, a free-text comment is left out because the model was not given a careful way to read it. A bad feature list produces a confident wrong model. Leaving out a feature that simply copies the answer (for example, including “passed” as a feature when predicting “passed”) is a cheat, not engineering.",
        ),
        ("h2", "Train, test, and the metrics"),
        (
            "p",
            "If you measure a model on the same rows it learned from, it can memorise them and look brilliant. A **train-test split** holds some rows back. The model learns only on the training rows. The test rows estimate how it behaves on data it has not memorised. A common classroom split is most of the rows for training and the rest for testing, chosen so that both parts still contain the kinds of cases you care about. Splitting one student’s repeated rows into both sides can leak the answer. Say how you split.",
        ),
        ("figure", "train-test", "Figure 13. Keep the test rows out of training, or the score flatters the model."),
        (
            "p",
            "A **confusion matrix** counts the test predictions against the truth. For a yes/no prediction:",
        ),
        (
            "table",
            {
                "caption": "Table 13. Names of the four counts. Positive means the event you are trying to detect.",
                "headers": ["", "Predicted positive", "Predicted negative"],
                "rows": [
                    ["Actual positive", "True positive (TP)", "False negative (FN)"],
                    ["Actual negative", "False positive (FP)", "True negative (TN)"],
                ],
                "widths": [0.34, 0.33, 0.33],
            },
        ),
        (
            "p",
            "**Accuracy** is (TP + TN) / all rows. **Precision** is TP / (TP + FP): of the rows you called positive, how many were. **Recall** is TP / (TP + FN): of the truly positive rows, how many you caught. A model can have high accuracy and still be useless if the event is rare and it never predicts the rare event. Choose the metric the decision needs. A scholarship screen that must not miss a qualifying student cares about recall. A screen that triggers an expensive interview cares about precision.",
        ),
        ("math", r"\mathrm{Precision}=\frac{TP}{TP+FP}"),
        ("math", r"\mathrm{Recall}=\frac{TP}{TP+FN}"),
        ("math", r"\mathrm{Accuracy}=\frac{TP+TN}{TP+TN+FP+FN}"),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — precision",
                "text": (
                    "Predicted positive and actually positive: 90. Predicted negative and actually positive: 10. "
                    "Predicted positive and actually negative: 30. Predicted negative and actually negative: 70.\n\n"
                    "TP = 90, FN = 10, FP = 30, TN = 70. There are 200 rows.\n\n"
                    "Precision = 90 / (90 + 30) = 90 / 120 = 0.75, which is 75 percent. "
                    "Recall = 90 / (90 + 10) = 90 percent. "
                    "Accuracy = (90 + 70) / 200 = 80 percent.\n\n"
                    "The 75 percent does not mean “75 percent of students passed”. It means three quarters of the positive predictions were right."
                ),
            },
        ),
        (
            "p",
            "A **hyperparameter** is a setting you choose rather than a value the model learns from the labels, such as how many groups to look for, or how flexible the model is allowed to be. Trying many settings and keeping the one that looks best on the *test* set makes the test set part of the training. The honest report says which data the choice was based on. You are not required to tune a large model in this course. You are required to know that the setting is a choice and that the metric must match the decision.",
        ),
        (
            "callout",
            {
                "kind": "warn",
                "title": "Prediction is not a cause",
                "text": "A model that predicts quiz marks from practice hours has found an association in the rows it was given. It has not proved that changing the hours will change the marks. Class XI’s warning still stands. Do not write “the model shows that practice causes success”. Write “the model predicts, on similar rows, with this error rate”.",
            },
        ),
        ("h2", "Hypothesis testing"),
        (
            "p",
            "A **hypothesis** is a claim you can challenge with data. The **null hypothesis (H0)** is the default of no effect or no difference: the new study technique has the same mean score as the old one; the coin is fair. The **alternative hypothesis (H1)** is the challenge: the means differ, or the new mean is higher, or the coin is not fair. Write both before you look at a dramatic number. Changing the hypothesis after you see the data is a different, weaker story, and you should admit it if you did it.",
        ),
        (
            "p",
            "A **p-value** is the probability of seeing a result at least as extreme as yours **if the null hypothesis is true**. It is not the probability that the null is true. A **significance level**, written alpha, is the threshold you chose in advance, often 0.05. If the p-value is smaller than alpha, you **reject the null**. If it is not, you **do not reject the null**. “Do not reject” is not the same sentence as “the null is true”. It means this dataset did not supply strong evidence against it.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — a coin, small enough to count",
                "text": (
                    "H0: the coin is fair, so the chance of heads on a toss is 0.5. H1: the chance of heads is greater than 0.5. Alpha = 0.05. You plan to toss 10 times.\n\n"
                    "You observe 9 heads. Under a fair coin, the number of ways to get 9 or 10 heads is 10 + 1 = 11, and there are 2^10 = 1024 equally likely sequences. "
                    "The one-sided p-value is 11/1024, about 0.011.\n\n"
                    "0.011 is less than 0.05, so you reject the null at this level. "
                    "You have not proved the coin is biased. You have said that nine or ten heads would be unusual for a fair coin, and you saw that kind of result. "
                    "Ten tosses are a classroom count, not a pub trick to accuse a person. Say the sample size in the same breath as the decision."
                ),
            },
        ),
        (
            "p",
            "A study-technique question uses the same shape and usually cannot be computed by hand from a binomial. You still write H0 and H1, you name alpha, you say you would compare the p-value with alpha, and you tie the conclusion to a chart: the two groups’ score distributions, not a slogan. If a question gives you the p-value, use it. Do not invent one.",
        ),
        ("h2", "Telling the story of the data"),
        (
            "p",
            "**Data storytelling** is a sequence: the question, the source of the rows, the picture, and the sentence you are willing to defend. Several views beat one view. A mean can rise while the median stays still because of a few high scores. A bar chart of averages and a note of the sample size answer different doubts. **Descriptive statistics** — mean, median, spread — describe the rows you have. They are not yet a hypothesis test.",
        ),
        (
            "p",
            "SQL belongs here as well as in programming. `SELECT Subject, AVG(Mark) FROM Result GROUP BY Subject` is a summary a chart can use. A Python plot or a spreadsheet chart of that summary is the visualisation. Criticise a published chart the way you did in Class XI: missing axis, a truncated scale, a pie of things that are not parts of a whole, a claim about a population the sample does not represent.",
        ),
        (
            "callout",
            {
                "kind": "exam",
                "title": "Exam tip",
                "text": "If the question gives a matrix, compute the ratio it names and state the formula in symbols or words before the arithmetic. If it gives a study, write H0 and H1 in the language of that study. A generic definition copied beside an unused scenario loses the application marks.",
            },
        ),
    ],
    terms=[
        ("Rule-based method", "Fixed instructions written by a person."),
        ("Machine learning", "A model adjusted on examples and then used to predict."),
        ("Feature / label", "An input column, and the outcome the model is asked to predict."),
        ("Train-test split", "Learn on some rows; measure on rows that were held back."),
        ("Precision", "TP / (TP + FP). How many positive predictions were right."),
        ("Recall", "TP / (TP + FN). How many real positives were caught."),
        ("Null hypothesis", "The claim of no effect or no difference, written before the test."),
        ("P-value", "How surprising the data are if the null is true. Not the probability the null is true."),
        ("Significance level", "The threshold, alpha, below which you reject the null."),
    ],
    checks=[
        {
            "q": "Precision is 75 percent in the worked matrix. What is the matching fraction?",
            "a": "90 / (90 + 30) = 90/120 = 0.75. The 30 are the false positives.",
        },
        {
            "q": "Why hold back test rows?",
            "a": "A model can memorise the training rows. The held-back rows estimate how it behaves on data it was not shown.",
        },
        {
            "q": "A p-value of 0.20 and alpha of 0.05. What do you decide?",
            "a": "Do not reject the null. 0.20 is not smaller than 0.05. This is not proof that the null is true.",
        },
    ],
    mcqs=[
        {
            "q": "The train-test split exists so that",
            "options": [
                "the model is scored on rows it learned from",
                "the model is scored on rows it did not learn from",
                "every row is used twice",
                "the null hypothesis becomes true",
            ],
            "answer": "B",
            "why": "Held-back rows estimate performance beyond memorisation.",
        },
        {
            "q": "Alpha is",
            "options": [
                "the probability you accept a false null",
                "the threshold for rejecting the null when it is true, chosen in advance",
                "the sample size",
                "the mean of the sample",
            ],
            "answer": "B",
            "why": "Alpha is the significance level: the false-rejection risk you decided to tolerate if the null is true.",
        },
        {
            "q": "Feature engineering means",
            "options": [
                "hiding the test set inside the training set",
                "turning raw records into the inputs a model will use",
                "deleting the metric",
                "replacing SQL",
            ],
            "answer": "B",
            "why": "Features are the prepared inputs. Including the answer itself as a feature is a fault, not a goal.",
        },
        {
            "q": "A high accuracy on a rare event can still be a weak model if",
            "options": [
                "it never predicts the rare event",
                "it uses a confusion matrix",
                "precision is defined",
                "the chart has a title",
            ],
            "answer": "A",
            "why": "Always saying “no” can be accurate when positives are rare, and it catches none of them. Recall exposes that.",
        },
    ],
    shorts=[
        {
            "q": "Define precision and compute it when TP = 90 and FP = 30.",
            "a": "Precision is the share of positive predictions that were actually positive, TP / (TP + FP). Here 90 / 120 = 0.75, or 75 percent.",
        },
        {
            "q": "Write H0 and H1 for a test of a new study technique against the usual one, two-sided.",
            "a": "H0: the mean score with the new technique equals the mean score with the usual technique. H1: the two means differ. A one-sided H1 would instead say the new mean is higher. The question asked for two-sided, so “differ” is the right alternative.",
        },
        {
            "q": "Give one SQL summary and one chart that could present average marks by subject.",
            "a": "SELECT Subject, AVG(Mark) AS average_mark FROM Result GROUP BY Subject. A bar chart of those averages, axis from zero, with the number of students per subject written somewhere, presents the comparison. A pie chart of averages is the wrong picture.",
        },
    ],
    longs=[
        {
            "marks": 5,
            "q": "A model predicts whether a student will score 80 or above. On the test set, TP = 90, FN = 10, FP = 30, TN = 70. Compute precision, recall, and accuracy. Say which metric you would watch if the cost of a false alarm (extra tutoring offered to someone who would have scored well anyway) is the main worry, and state one thing the model has not proved.",
            "a": (
                "Precision = 90/(90+30) = 75 percent. Recall = 90/(90+10) = 90 percent. Accuracy = (90+70)/200 = 80 percent.\n\n"
                "A false alarm is a false positive. Precision is the metric that falls when false positives grow, so it matches that worry. "
                "Recall would matter more if missing a student who needed support were the expensive mistake.\n\n"
                "The model has not proved that any particular habit causes a distinction. It has classified held-back rows with these error counts, and only for data like the data it was given."
            ),
        },
        {
            "marks": 5,
            "q": "A teacher tosses a coin 10 times to demonstrate a test and gets 9 heads. Take H0 as “fair coin”, H1 as “heads is more likely than tails”, and alpha as 0.05. Use p ≈ 0.011. Decide, and explain the decision in a way that would also fit a study-technique experiment whose p-value you were given.",
            "a": (
                "The p-value is about 0.011, which is smaller than 0.05, so reject H0 at the 5 percent level. "
                "Under a fair coin, 9 or 10 heads in 10 tosses is uncommon (11 sequences out of 1024). "
                "Rejecting H0 does not certify the coin, and n = 10 should be stated.\n\n"
                "The same sentences fit a study technique. Write H0 as equal means and H1 as the direction you chose. "
                "If the given p-value is below alpha, reject H0 and show the two score distributions so the reader sees the difference the test is about. "
                "If the p-value is above alpha, do not reject H0, and do not rewrite H1 after peeking. "
                "In both stories the p-value is the surprise of the data assuming the null, not the probability that the null is true."
            ),
        },
    ],
    labs=[
        {
            "title": "Lab 4 — A metric and a hypothesis write-up",
            "steps": [
                "Copy the confusion matrix from the worked example and compute precision, recall, and accuracy by hand and in a few lines of Python.",
                "Write H0, H1, alpha, and the decision for the coin example in your journal.",
                "Using any small table of marks, produce an average by subject in SQL or in a spreadsheet and chart it.",
                "Under the chart, write one causal sentence you refuse to make.",
            ],
            "success": "The three percentages are 75, 90, and 80. The chart has a title and a sample size. The refused sentence is written down, not only implied.",
        }
    ],
    summary=[
        "Rules are written by people. Machine learning adjusts a model on examples. Neither is a proof of cause.",
        "Features are inputs. Labels are known outcomes. Do not feed the model the answer as a feature.",
        "Train on some rows and measure on held-back rows.",
        "Precision = TP/(TP+FP). Recall = TP/(TP+FN). Accuracy can hide a rare event.",
        "H0 is no difference. A p-value is surprise assuming H0. Compare it with alpha. Do not reject is not proof.",
        "Tell the story with more than one view: a summary query, a chart, and a limit on the claim.",
    ],
)
