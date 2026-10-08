from content.schema import lecture

LECTURE = lecture(
    id="xi-6",
    number=6,
    title="Digital Literacy and a First Prototype",
    kicker="CLASS XI  ·  UNIT 6",
    unit="Unit 6 — Digital Literacy",
    domain="G and H. Digital literacy, and the Class XI prototype",
    periods="about 20 periods",
    intro=(
        "Digital literacy is the skill of finding, judging, collecting, and presenting information with digital tools. "
        "The Class XI textbook centres on advanced search and on designing a way to collect original data. "
        "The national outcomes also ask you to build and test a prototype of a small idea. "
        "That prototype closes this lecture, and Class XII will turn a surviving idea into a minimum viable product."
    ),
    outcomes=[
        "Use advanced search operators and explain why the first result is not automatically the best.",
        "Write a research question and choose among interviews, surveys, prototypes, and simulations.",
        "Distinguish primary and secondary data and present findings in a fitting digital form.",
        "Design a small prototype, test it with a real user, and change one thing because of what you saw.",
    ],
    blocks=[
        ("h2", "Advanced search"),
        (
            "p",
            "A search box is a tool with a grammar. A quoted phrase, `\"binary search\"`, asks for those words together. A minus sign excludes a word: `jaguar -car` if you wanted the animal. `site:.edu.pk` limits the search to a kind of site. `filetype:pdf` limits the file type. `OR` keeps either term. These operators are how you locate a board notification, a dataset, or a definition without scrolling past advertisements.",
        ),
        (
            "p",
            "The first link is a ranking, not a verdict. Rankings follow the search engine’s formula and the advertiser’s money. After you arrive, you still judge the page: who wrote it, which organisation they belong to, the date, and whether the evidence is on the page or merely asserted. Two sources that copy each other are not two sources. Prefer the organisation that owns the fact — the board for a date sheet, the statistics agency for a population figure.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — finding a syllabus fact",
                "text": (
                    "You need the official name of the Class XI computer science book, not a shop’s description.\n\n"
                    "Search `\"Computer Science\" \"Grade XI\" site:.gov.pk` and, separately, the Sindh Textbook Board’s own pages. "
                    "A shop page is useful as a clue to the chapter titles and must be labelled as a shop page if you cite it. "
                    "The board or the directorate is the authority for what is prescribed. Write the date you looked, because pages change."
                ),
            },
        ),
        ("h2", "A research question worth collecting data for"),
        (
            "p",
            "A useful question says who, what, and the comparison or description you will actually make. “Is social media bad?” cannot be answered by a survey of your friends. “In our CS section, how many students used a paper trace before writing binary search, and did they finish the lab?” can be answered, and the answer is about that section only.",
        ),
        (
            "p",
            "**Primary data** is data you collect for this question: your survey responses, your interview notes, your own measurements. **Secondary data** is data somebody else already published: a statistical yearbook, a previous practical’s anonymous results, a dataset on a government site. Secondary data is not worse. It is often better, if you understand how it was collected. Say which kind you are using. Do not present a downloaded table as if you had surveyed the country.",
        ),
        ("h2", "Choosing a collection method"),
        (
            "table",
            {
                "caption": "Table 10. Methods named in the unit. Pick one main method and say why the others were worse for this question.",
                "headers": ["Method", "You use it when", "Watch out for"],
                "rows": [
                    ["Survey", "You need the same questions answered by many people", "Vague wording; only the willing respond"],
                    ["Qualitative interview", "You need the story behind a few people’s choices", "A small number cannot be written as a percentage of Pakistan"],
                    ["Prototype test", "You need to see whether a design can be used", "Polite classmates may say it is fine when it is not"],
                    ["Simulation", "Trying the real system would be unsafe, slow, or impossible", "A simulation is only as honest as its assumptions"],
                ],
                "widths": [0.22, 0.40, 0.38],
            },
        ),
        (
            "p",
            "A survey question should be one question. “Do you like practicals and have a laptop?” cannot be answered with one yes. Offer a scale or clear options, and include “I don’t know” when that is a real answer. An interview needs a few open questions and the patience to write what was said, not what you hoped. A simulation, such as a paper model of a queue in the college canteen, should list the assumptions: how many servers, how long an order takes.",
        ),
        (
            "p",
            "Collect only what the question needs. Names are usually unnecessary on a class survey about study habits; a tick is enough. Tell people what the data is for, that they can refuse, and that you will not pass the sheet to anyone outside the practical. That is the minimum of respectful data collection. It is also the habit behind the privacy talk in the previous lecture.",
        ),
        ("h2", "Presenting the result"),
        (
            "p",
            "The form follows the audience. A teacher marking a practical can read a one-page report: question, method, table, chart, and a limit on the claim. A class noticeboard might need an **infographic** with one chart and one sentence. A short slide deck fits a three-minute presentation. A spreadsheet holds the workings so the chart can be checked. Do not paste a spreadsheet onto a slide.",
        ),
        (
            "p",
            "Every chart needs a title, labelled axes or a legend, and the source and sample size nearby: “n = 32 students in Section A, 8 October 2026.” A sentence under the chart should say what a careful reader may conclude. “Most of this section starts the practical on paper” is allowed if the numbers say so. “Pakistani students prefer paper” is not.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — a one-page finding",
                "text": (
                    "Question: in our section, did students who said they traced binary search on paper also finish the lab task?\n\n"
                    "Method: an anonymous survey of one section, four questions, done at the end of the lab. Primary data. n = 28 of 32 present.\n\n"
                    "Result: 18 said they traced on paper; 16 of those finished. 10 said they did not; 4 of those finished. "
                    "A grouped bar chart shows finished and not finished for the two groups.\n\n"
                    "Limit: people may misremember, the section is not all of BIEK, and finishing the lab has other causes. "
                    "The prototype of a “trace-first checklist” can be tested next, which is a different question."
                ),
            },
        ),
        ("h2", "A prototype of a small idea"),
        (
            "p",
            "A **prototype** is a cheap, early version of an idea, built so you can learn. It can be a paper screen, a slide that pretends to be an app, or a script that does one step. It is not the finished product and it is not a business yet. You **test** it by watching somebody who was not the designer try to use it, without you explaining. You **iterate** by changing the prototype because of what you saw, then testing again.",
        ),
        (
            "p",
            "Pick a problem you have actually met. A one-page “which search do I use?” card for Class XI, a paper timetable of the lab PCs, or a three-screen sketch of a lost-and-found board are all large enough. A plan to “disrupt education in Pakistan” is not a prototype. It has no user you can sit next to this week.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — paper prototype of a lab checklist",
                "text": (
                    "Problem: students skip the trace and then cannot explain a wrong index.\n\n"
                    "Prototype: a paper card with three boxes — list, target, low/high/middle — and a final line “index or not found”.\n\n"
                    "Test: two classmates use it on a new list while you stay quiet. One of them does not know where to write the middle value. "
                    "Iteration: add the words “middle value” under the third box and test with a third classmate.\n\n"
                    "What you learned is about the card, not about the whole country. Class XII will ask which assumption is the riskiest if you ever try to offer the card as a product."
                ),
            },
        ),
        (
            "callout",
            {
                "kind": "warn",
                "title": "Common mistake",
                "text": "Do not paste pages from the textbook or from another author’s notes into a prototype you claim as yours. A prototype can show your own examples, your own layout, and your own questions. Copying a book is not design, and it is not allowed as practical work.",
            },
        ),
        (
            "callout",
            {
                "kind": "exam",
                "title": "Exam tip",
                "text": "Digital-literacy questions reward a method matched to a question, a labelled chart, and a sentence that limits the claim. Prototype questions reward a user, what you built, what you saw in the test, and what you changed. A definition of “survey” with no question attached is the weak version of this answer.",
            },
        ),
    ],
    terms=[
        ("Search operator", "Grammar in the search box, such as quotes, minus, site:, and filetype:."),
        ("Primary data", "Data you collect to answer this question."),
        ("Secondary data", "Data already collected by someone else."),
        ("Survey", "The same questions asked of many people."),
        ("Qualitative interview", "A conversation that collects an account, not only a tick."),
        ("Simulation", "A model of a system you cannot safely or cheaply run for real."),
        ("Infographic", "A visual summary aimed at a quick reading."),
        ("Prototype", "An early, cheap version built so a test can teach you."),
        ("Iteration", "A change made because of a test, followed by another test."),
    ],
    checks=[
        {
            "q": "What does the search `filetype:pdf site:.edu.pk binary search` try to do?",
            "a": "It looks for PDF files on .edu.pk sites that mention binary search. It does not prove that those files are correct or current.",
        },
        {
            "q": "Why is “n = 28 in Section A” required next to a chart?",
            "a": "The reader must know who was measured. Without it, a bar can be mistaken for a national fact.",
        },
        {
            "q": "What is the difference between a prototype and a finished app?",
            "a": "A prototype is built to learn, often on paper or as a thin sketch, and it is expected to change after a test. A finished app is built to be used for real and maintained. This year you are marked on the learning, not on a polished product.",
        },
    ],
    mcqs=[
        {
            "q": "Quotes around a phrase in a search box",
            "options": [
                "exclude that phrase",
                "ask for those words together",
                "limit the search to books you own",
                "prove the page is official",
            ],
            "answer": "B",
            "why": "Quotes mean the words should appear as a phrase. They say nothing about whether the page is trustworthy.",
        },
        {
            "q": "Data you download from a statistics agency is",
            "options": [
                "primary data for you",
                "secondary data",
                "a prototype",
                "a primary key",
            ],
            "answer": "B",
            "why": "Somebody else collected it. It becomes part of your study as secondary data, clearly cited.",
        },
        {
            "q": "The best reason to interview three students instead of surveying them is that you want",
            "options": [
                "a percentage for the whole city",
                "a detailed account of how they study",
                "a pie chart with three slices",
                "to avoid writing anything down",
            ],
            "answer": "B",
            "why": "Interviews collect depth. Three people are not a percentage of a city.",
        },
        {
            "q": "After a prototype test you should",
            "options": [
                "hide the problems so the marks stay high",
                "change the prototype because of what the user did",
                "add every feature you can imagine",
                "throw away the notes",
            ],
            "answer": "B",
            "why": "Iteration is the point of the test. The notes are the evidence.",
        },
    ],
    shorts=[
        {
            "q": "Write one research question about your own CS class that a survey can answer, and one claim that the survey must not make.",
            "a": "Question: of the students present in this section today, how many have used the college lab printer this month? The survey must not claim that “BIEK students lack printers”, because one section on one day is not the board and the question did not ask about home printers.",
        },
        {
            "q": "Give two rules for an honest chart in a practical report.",
            "a": "Label the axes or the slices, and start a bar chart’s quantity axis at zero unless you have a reason you are willing to explain. State the sample size and who was included. The title should describe the chart, not shout a conclusion the data does not carry.",
        },
        {
            "q": "Describe a prototype test in three steps.",
            "a": "Give the prototype to a user who did not design it. Set a task and stay quiet. Write what they did and where they stopped, then change one part of the prototype and, if there is time, test that change.",
        },
    ],
    longs=[
        {
            "marks": 5,
            "q": "You want to know how Class XI CS students in your college find past papers. Design the data collection. Include the question, the method, primary or secondary data, one ethical point, and how you would present the result.",
            "a": (
                "Research question: in our college, which sources do Class XI CS students report using when they look for past papers, and do they check the board site?\n\n"
                "Method: a short anonymous survey of the CS sections, with options such as board site, teacher, shop notes, and forwarded messages, plus a yes/no on checking the official site. "
                "This is primary data. A secondary source, such as the board site itself, can be described separately so you know what the official source is, but it does not answer what students do.\n\n"
                "Ethics: no names, a sentence at the top saying the practical is the only use, and the right to leave it blank.\n\n"
                "Presentation: a bar chart of the sources, n written under it, and a sentence limited to the students who responded. "
                "A slide with that one chart is enough for the class. The spreadsheet stays in the journal so the bars can be checked."
            ),
        },
        {
            "marks": 5,
            "q": "Design a prototype that helps a classmate choose between linear search and binary search. Describe the test and one iteration.",
            "a": (
                "The user is a Class XI student who has met both algorithms. The prototype is a paper card. "
                "Line 1 asks: is the list sorted? If no, it points to linear search. If yes, it points to binary search and reminds the user to write low, high, and middle. "
                "A tiny example list sits at the bottom, written by the designer, not copied from a book.\n\n"
                "Test: a classmate is given an unsorted list and asked to choose an algorithm using only the card. "
                "Suppose they still try binary search. The iteration adds the words “Stop. Do not use binary search on an unsorted list” on the No branch, in larger writing, and the card is tested with another person.\n\n"
                "Success is not that the card is pretty. Success is that the second user takes the correct branch without an oral hint."
            ),
        },
    ],
    labs=[
        {
            "title": "Lab 8 — Search, survey, and a prototype",
            "steps": [
                "Write down two different searches you used, including at least one operator, and what you decided about the pages you opened.",
                "Run a five-question anonymous survey in your own section, or analyse a data table your teacher provides and label it secondary.",
                "Produce one chart with a title, a sample size, and a two-sentence limit on the claim.",
                "Make a paper prototype of one study aid. Test it with one classmate. Change one thing. Photograph or redraw both versions for the journal.",
            ],
            "success": "The journal shows the search strings, the chart with n, and both versions of the prototype with a sentence on what the user did.",
        }
    ],
    summary=[
        "Quotes, minus, site:, and filetype: narrow a search. They do not certify the page.",
        "Judge the author, the date, and the evidence. Two copies of the same rumour are one source.",
        "A research question names the group and the fact you will actually collect.",
        "Primary data is yours. Secondary data is cited as someone else’s.",
        "Surveys count the same questions. Interviews collect accounts. Prototypes test a design. Simulations stand in when the real run is impossible.",
        "Charts need labels and a sample size. The sentence under the chart must fit the sample.",
        "A prototype is for learning. Watch a user, change one thing, and keep the notes.",
    ],
)
