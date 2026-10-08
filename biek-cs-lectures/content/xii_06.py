from content.schema import lecture

LECTURE = lecture(
    id="xii-6",
    number=6,
    title="Entrepreneurship in the Digital Age",
    kicker="CLASS XII  ·  UNIT 6",
    unit="Unit 6 — Entrepreneurship in the Digital Age",
    domain="H. Entrepreneurship",
    periods="about 10 periods",
    intro=(
        "A business idea is a guess about a person and a problem. "
        "This lecture is about testing the guess cheaply: choose a beachhead market, name the riskiest assumption, "
        "and build a minimum viable product that can prove you wrong. "
        "Class XI’s paper prototype showed that a design could be used. The MVP asks whether the business idea survives contact with that user."
    ),
    outcomes=[
        "Distinguish a prototype from a minimum viable product.",
        "Define a beachhead market narrowly enough to test.",
        "Identify the riskiest assumption and design a test that could fail.",
        "Describe an ethical digital offer a student could actually run, and name a career path the work points toward.",
    ],
    blocks=[
        ("h2", "Prototype and MVP"),
        (
            "p",
            "A **prototype** is a learning model. It can be paper. Its question is “can a person understand and use this?” A **minimum viable product (MVP)** is the smallest real offer that lets a user complete the core job, so you can measure behaviour. Its question is “will the people in this market actually take this offer?” A slide that pretends to be an app is still a prototype. A single paid workshop, a working signup that delivers one chapter you wrote, or a weekly SMS that a farmer pays to receive, can be an MVP if a stranger to the design can finish the job.",
        ),
        (
            "callout",
            {
                "kind": "define",
                "title": "Minimum viable product",
                "text": "The smallest version of a product that is real enough for the target user to complete the main job, built so that the riskiest assumption can be tested. It is not a buggy version of every feature you hope to add later.",
            },
        ),
        ("h2", "The beachhead"),
        (
            "p",
            "A **beachhead market** is the first small group you will win, not the whole country you will mention in a speech. “Students” is not a market. “Class XI computer-science students in three colleges in one town, who already have a phone and who told a teacher they want extra practice on trees” is a beachhead. You can reach them, you can hear them, and a failure is visible. If the beachhead does not care, a larger market will not repair the idea.",
        ),
        ("h2", "The riskiest assumption"),
        (
            "p",
            "An idea is a pile of assumptions: the problem is real, this person feels it, they will try your solution, they will pay this price, you can deliver, and a rule or a parent or a college will allow it. The **riskiest assumption** is the one that, if false, kills the idea, and that you are least sure about. Often it is “they will pay”, or “they will come back next week”, not “we can draw a logo”.",
        ),
        (
            "p",
            "A real test can fail. If you only ask friends “would you like this?” they will say yes. A stronger test asks for a behaviour: a small payment, a second visit, a reply to an SMS, a form filled without you standing over the desk. Decide before the test what result would make you change or stop. Changing the price after everyone refused, and then announcing success, is not a test.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — practice cards for one beachhead",
                "text": (
                    "Beachhead: Class XII CS students in your own college who have a phone.\n\n"
                    "Offer: each week, one original practice card on a single topic (this week, inorder traversal), plus a short answer they can check. Delivered in a chat they already use.\n\n"
                    "Riskiest assumption: at least 15 students will complete the card two weeks in a row without the teacher making it compulsory. "
                    "The polite assumption “they will say it is useful” is weaker, because it cannot fail in public.\n\n"
                    "MVP: you write two original cards, not a full app, not a dump of a textbook. You send them. You count completions. "
                    "If fewer than the number you set in advance come back, you stop or you change the topic. "
                    "You do not paste pages from the Sindh Textbook Board book or from another author’s notes and call it a product."
                ),
            },
        ),
        ("h2", "What you may not sell"),
        (
            "p",
            "A digital business still has rules. You do not sell copied books, copied notes, or a paper that a student will submit as their own work. You do not collect identity cards “for registration” and leave them in a chat. You do not invent a result, a ranking, or a customer count. You do not spam people who did not ask. An MVP that grows by those methods has not validated a business. It has tested how long a nuisance can continue. The same privacy and usability lessons from the earlier units apply to something you run yourself: collect less, label the action honestly, and let the user stop.",
        ),
        ("h2", "A test plan you can write in an examination"),
        (
            "numbers",
            [
                "Name the beachhead in one sentence a stranger could use to find those people.",
                "State the core job in one sentence, from the user’s side.",
                "State the riskiest assumption.",
                "Describe the MVP as the smallest thing that tests that assumption.",
                "State the number or the behaviour that will count as failure.",
                "Say what you will do if it fails: change the offer, change the beachhead, or stop.",
            ],
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — failure written in advance",
                "text": (
                    "Assumption: shopkeepers on one street will reply to a weekly SMS that lists items they asked you to watch in nearby markets.\n\n"
                    "MVP: ten shopkeepers, one week, messages you type yourself. No app.\n\n"
                    "Failure: fewer than six reply with a real question or a thank-you that includes a new item. "
                    "A family member replying does not count. "
                    "If it fails, you do not build an app. You either visit the shops and change what the message contains, or you drop the idea."
                ),
            },
        ),
        ("h2", "Careers the subject is pointing at"),
        (
            "p",
            "The units in these two years line up with real work. Building and testing software is software development and quality work. Databases and SQL lead toward data and information-system roles. Networks, usability, and security lead toward support, administration, and security-minded design. The entrepreneurship unit is the version of that work in which you, rather than an employer, choose the user. After HSC, the usual academic doors are bachelor’s programmes in computer science, software engineering, information technology, and related data programmes, where the entrance rules are set by the university, not by this lecture. A college laboratory assistant, a junior developer, a data-entry analyst who can actually query, and a teacher are all coherent next steps. None of them requires you to have founded a company at 17. The MVP is practice at honesty about evidence.",
        ),
        (
            "callout",
            {
                "kind": "exam",
                "title": "Exam tip",
                "text": "A five-mark entrepreneurship question wants the beachhead, the MVP, the riskiest assumption, and the failure rule. A definition of “startup” with no user is the answer that loses the marks. Mention one ethical limit if the offer could easily become copied material or a pile of personal data.",
            },
        ),
    ],
    terms=[
        ("Prototype", "A model for learning whether people can use a design."),
        ("MVP", "The smallest real offer that tests whether the business assumption holds."),
        ("Beachhead market", "The first narrow group of users you will actually reach."),
        ("Riskiest assumption", "The belief that would kill the idea if it is false, and that you are least sure of."),
        ("Failure rule", "The result, chosen in advance, that will make you change or stop."),
    ],
    checks=[
        {
            "q": "Why is a paper screen not an MVP?",
            "a": "It can test understanding, which is a prototype question. An MVP must let the user complete the real job well enough that their behaviour tests the business assumption, such as coming back or paying.",
        },
        {
            "q": "Rewrite “all students in Pakistan” as a beachhead.",
            "a": "One possible beachhead is Class XII CS students in a single college who attend the Tuesday practical. You can reach them this month. You cannot honestly test “all students in Pakistan” with a class project.",
        },
        {
            "q": "Why must the failure rule be written before the test?",
            "a": "After the test it is easy to move the line until the result looks like success. A rule written first is what makes the test able to fail.",
        },
    ],
    mcqs=[
        {
            "q": "The riskiest assumption is the one that",
            "options": [
                "is the easiest to put on a poster",
                "would kill the idea if false, and is still unchecked",
                "the founder likes most",
                "requires the largest logo",
            ],
            "answer": "B",
            "why": "Risk here means both damage to the idea and lack of evidence. A logo is rarely that assumption.",
        },
        {
            "q": "An MVP differs from a prototype because the MVP",
            "options": [
                "includes every planned feature",
                "is real enough that user behaviour can test the business guess",
                "must be built in Python",
                "cannot be small",
            ],
            "answer": "B",
            "why": "The MVP is small on purpose. The difference is that the core job really happens.",
        },
        {
            "q": "Which offer is acceptable practical work?",
            "options": [
                "Selling scans of the textbook",
                "An original weekly practice card you wrote and measured",
                "A service that writes other students’ practicals",
                "A collected set of identity cards in a public chat",
            ],
            "answer": "B",
            "why": "Original work that is tested is the assignment. The other options copy, cheat, or expose people.",
        },
        {
            "q": "A beachhead market should be",
            "options": [
                "as large as possible in the first sentence",
                "narrow enough that you can reach those people and see a failure",
                "secret from the users",
                "defined only by age",
            ],
            "answer": "B",
            "why": "A test needs a group you can actually contact. A continent is not a first test.",
        },
    ],
    shorts=[
        {
            "q": "Distinguish a prototype and an MVP using the practice-card idea.",
            "a": "A paper sketch of the card, watched while a classmate tries to use it, is a prototype. It asks whether the layout is understandable. Sending a real card two weeks running and counting who completes it is an MVP. It asks whether the behaviour you need actually happens.",
        },
        {
            "q": "Write a failure rule for an SMS revision service aimed at ten classmates.",
            "a": "Before sending anything, decide that the test fails if fewer than six of the ten answer the mid-week question in both weeks. Replies from the founder do not count. If it fails, do not build an app; change the time of day or stop.",
        },
        {
            "q": "Name one career that uses SQL and one that uses usability tests, as this course described them.",
            "a": "SQL is daily work in data and information-system roles that answer questions from tables. Usability tests are daily work in design and in software teams that watch a user attempt a task before they call a screen finished. Neither job title is a promise of employment; both are coherent uses of the skills.",
        },
    ],
    longs=[
        {
            "marks": 5,
            "q": "Choose a problem in your college. Define the beachhead, the MVP, the riskiest assumption, and the failure rule. State one ethical limit.",
            "a": (
                "Problem: students arrive at the lab without the practical sheet.\n\n"
                "Beachhead: students of your own CS section who use the class chat.\n\n"
                "MVP: for two weeks, the day before each practical, you post the teacher’s own instruction in three lines plus a checklist you wrote. You do not scan a book.\n\n"
                "Riskiest assumption: at least half the section will open the message before the practical, which you will see from replies or from a one-tap poll, not from your impression.\n\n"
                "Failure rule: if fewer than half respond in both weeks, you stop the posts or you change the time. You do not add features.\n\n"
                "Ethical limit: you do not collect phone numbers beyond the chat that already exists, and you do not post anyone’s marks or identity card to “personalise” the reminder."
            ),
        },
        {
            "marks": 5,
            "q": "A classmate says their MVP is “an AI app for all Pakistani farmers”, with no users yet. Rewrite the plan so it could be tested this month, and explain why the original sentence is not an MVP.",
            "a": (
                "The original sentence names a technology and a continent-sized market, and it offers nothing a farmer can complete this month. That is a slogan. An MVP has to be usable for the core job.\n\n"
                "Rewrite: beachhead is ten vegetable growers the student’s family already knows on one road. "
                "The riskiest assumption is that they will answer a weekly message about tomorrow’s wholesale price at a named market. "
                "The MVP is the founder typing those messages from prices they themselves checked, for three weeks. "
                "Failure is fewer than six growers replying in week two or week three. "
                "There is no model, no app, and no claim of artificial intelligence until that behaviour exists. "
                "The ethical limit is that the prices must be ones the founder actually saw, not invented numbers, and the growers can tell them to stop."
            ),
        },
    ],
    labs=[
        {
            "title": "Lab 6 — An MVP test you can finish",
            "steps": [
                "Write the six lines: beachhead, job, riskiest assumption, MVP, failure rule, ethical limit.",
                "Build only what that MVP needs. Paper plus a real message counts if the job is a message.",
                "Run the test on the beachhead, not only on your project partner.",
                "Record the number you promised to watch, and the decision the rule requires.",
            ],
            "success": "The journal shows a number chosen in advance and a decision that follows it, including a decision to stop or change.",
        }
    ],
    summary=[
        "A prototype tests use. An MVP tests the business assumption with a real, minimal offer.",
        "A beachhead is a small group you can actually reach.",
        "The riskiest assumption kills the idea if it is false. Test that, not the logo.",
        "Write the failure rule before you start, and accept the result.",
        "Do not sell copied books, ghost-written practicals, or other people’s identity documents.",
        "The technical units point at development, data, support, security-minded design, and teaching. The MVP is practice at evidence.",
    ],
)
