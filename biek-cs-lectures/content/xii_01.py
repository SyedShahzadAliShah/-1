from content.schema import lecture

LECTURE = lecture(
    id="xii-1",
    number=1,
    title="Usable, Accessible, and Secure Systems",
    kicker="CLASS XII  ·  UNIT 1",
    unit="Unit 1 — Computer Systems",
    domain="A. Computer systems",
    periods="about 30 periods",
    intro=(
        "Class XI asked how a system is built and how bits move. Class XII asks whether a person can actually use what was built, "
        "whether someone who sees, hears, or moves differently can use it, and whether the security added along the way makes the system so awkward that people route around it. "
        "Human-computer interaction is the name of that design work."
    ),
    outcomes=[
        "Explain usability, accessibility, and security, and give an example of each failing on a familiar system.",
        "Describe human-computer interaction in terms of usability, common problems, improvements, and ethical, social, economic, and environmental effects.",
        "Explain a usability test in enough detail to carry one out on a paper screen.",
        "Recommend a security measure that respects efficiency, cost, privacy, and ethics, including the idea of a zero-trust design.",
    ],
    blocks=[
        ("h2", "Three words that are not the same"),
        (
            "p",
            "**Usability** is how effectively, efficiently, and satisfactorily a stated user can complete a stated task. Effectively means they can finish it. Efficiently means the effort is reasonable. Satisfactorily means the experience is not a punishment. **Accessibility** means people with disabilities, and people in hard conditions, can complete the same task. **Security** means the system resists harm to confidentiality, integrity, and availability. A door that nobody can open is secure and useless. A door with no lock is usable and unsafe. The design work is the space between those jokes.",
        ),
        (
            "callout",
            {
                "kind": "define",
                "title": "Human-computer interaction",
                "text": "Human-computer interaction (HCI) studies how people use computing systems and how to design those systems so the use is effective, efficient, and satisfying. It includes the layout of a screen, the words on a button, the time a task takes, the errors people make, and the consequences when the design ignores a group of users.",
            },
        ),
        ("h2", "Usability: problems and improvements"),
        (
            "p",
            "Common problems are dull and expensive. The label does not match the user’s word (“submit” when the user thinks “save”). There is no confirmation, so people press twice. The error message says “invalid” and not what to fix. Text is grey on a pale background. The only way forward is a tiny link. A long form asks for a father’s name when the task is to see a date sheet. Each of these is a usability fault even if the database behind it is correct.",
        ),
        (
            "p",
            "Improvements are equally concrete. Use the user’s words. Put the primary action where the eye arrives, and make it look like a button. Keep a consistent place for navigation. Show the password rules before the user fails them. Let the user undo. Test with five people who are not the programmer and watch where they stop. A **usability test** gives a person a goal, stays quiet, and records the stops. It is not a demo in which you drive the mouse while they watch.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — a college portal task",
                "text": (
                    "Task: a student must download this week’s CS practical sheet.\n\n"
                    "On the current portal the sheet is under “Academics → Resources → Misc → files (3)”. "
                    "Three test users look under “Computer Science” and give up. That is a usability finding, not a user failure.\n\n"
                    "Improvement: a heading “This week” on the CS page, the practical’s name in the link, and the upload date. "
                    "Retest with two new students. If they reach the file without help, the change did the job. "
                    "If the file is a 40 MB scan of a photocopy, you have found a second problem."
                ),
            },
        ),
        ("h2", "Accessibility"),
        (
            "p",
            "An inaccessible system excludes people the institution has already accepted. A screen-reader user needs real text, not a photograph of text, and needs every control to be reachable from the keyboard. A user with low vision needs contrast and the right to enlarge text without the layout collapsing. A deaf user needs captions on a teaching video. A user with a tremor needs a target that is not a few pixels wide. Colour must not be the only signal that a mark is failing; a word or an icon has to carry it too, because some users do not distinguish red and green.",
        ),
        (
            "p",
            "The effects of ignoring this are not limited to one annoyed person. A student misses the date sheet and the admission. A public service that only works in one language, on one expensive phone, teaches the public that the service is not for them. Accessibility overlaps the digital divide from Class XI. In Class XII you are expected to talk about the design, not only about the gap.",
        ),
        ("h2", "Effects of a bad design"),
        (
            "table",
            {
                "caption": "Table 11. Use this shape when a question lists ethical, social, economic, and environmental implications.",
                "headers": ["Kind", "A bad result", "A design response"],
                "rows": [
                    ["Ethical", "People are tricked by a button that does more than it says", "The label matches the action; consent is specific"],
                    ["Social", "A group cannot use the service and drops out of the activity", "Language, captions, and a path that works on a small screen"],
                    ["Economic", "Staff spend the day resetting passwords and retyping forms", "Clear errors and a cheaper support load"],
                    ["Environmental", "Users print every page because the screen version is unreadable", "A readable page and a single clean print"],
                ],
                "widths": [0.18, 0.42, 0.40],
            },
        ),
        ("h2", "Security that people will actually follow"),
        (
            "p",
            "There is a standing **tradeoff** between security and usability. A password of 30 random characters is harder to guess and harder to remember, so people write it on a sticky note, and the sticky note may be the weakest point. A session that expires every two minutes protects a shared lab PC and infuriates a teacher entering marks. The designer’s job is to say which risk is real in this setting and to pick a control that users will not bypass.",
        ),
        (
            "p",
            "The factors to name are **efficiency** (does the task still finish in a reasonable time?), **cost** (can the college pay for the control, and what does a breach cost?), **privacy** (are you collecting more data than the control needs?), and **ethics** (are you watching people who were not told, or locking out people who cannot use the chosen method?). Biometrics, for example, can be fast and can also be a problem for a student whose fingerprint is worn from work, and a fingerprint cannot be changed if the database leaks. A password can be changed. Say that limit if you recommend a fingerprint.",
        ),
        (
            "p",
            "A **zero-trust** approach means the network does not treat a device as safe merely because it is inside the building. Every request is authenticated and given only the access that request needs. In a college, that sounds like: the lab PC is not automatically allowed to open the result database; the clerk’s account can enter marks for this class and not download the whole board’s rolls; a forgotten laptop does not carry a permanent login. Zero trust is a design habit, not a product you buy and forget.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — a usable control",
                "text": (
                    "Risk: students reuse one weak password on the portal.\n\n"
                    "A poster that says “use a strong password” does almost nothing. "
                    "A usable design lets the student paste a password from a password manager, shows the rules before submission, and turns on a second factor that the student already has, such as a one-time code, with a recovery method that does not depend on a single lost phone. "
                    "Forcing a change every week looks strict and trains people to use Password2, Password3, and a notebook. That fails both usability and security.\n\n"
                    "Cost: the code-by-SMS path costs money and fails when the network fails, so a code from an authenticator app, plus a printed recovery code kept at home, may fit better. Privacy: the portal does not need the student’s contacts in order to protect the login."
                ),
            },
        ),
        (
            "callout",
            {
                "kind": "warn",
                "title": "Common mistake",
                "text": "“Add more passwords” is not an HCI answer. Name the user, the task, the risk, the control, and the way the control could itself be bypassed.",
            },
        ),
    ],
    terms=[
        ("Usability", "Effectiveness, efficiency, and satisfaction for a stated user and task."),
        ("Accessibility", "The same task can be completed by people with disabilities and in hard conditions."),
        ("HCI", "The study and practice of designing that use."),
        ("Usability test", "A user attempts a goal while the designer watches and does not help."),
        ("Tradeoff", "A gain in security that costs usability, money, privacy, or fairness."),
        ("Zero trust", "Every request is checked; being on the local network is not enough."),
        ("Least privilege", "An account can do only what its job needs."),
    ],
    checks=[
        {
            "q": "Why is a usability test not a demonstration?",
            "a": "In a demonstration the designer operates the system and the story succeeds. In a test the user operates it, the designer stays quiet, and the stops are the result.",
        },
        {
            "q": "Give one accessibility fault that is not about blindness.",
            "a": "A video with no captions excludes a deaf student and also fails a student in a noisy room. A button that is too small excludes someone with a tremor.",
        },
        {
            "q": "Why can a very strict password rule reduce security?",
            "a": "People who cannot remember it write it down or simplify it in a predictable series. The rule is bypassed, and the bypass may be weaker than a memorable long passphrase would have been.",
        },
    ],
    mcqs=[
        {
            "q": "Which situation is a usability-security tradeoff?",
            "options": [
                "A short password that is easy and easy to guess",
                "A faster processor",
                "A larger monitor that shows the same form",
                "A primary key",
            ],
            "answer": "A",
            "why": "Ease and resistance to guessing pull in opposite directions. The other options are not that conflict.",
        },
        {
            "q": "A usability test’s main evidence is",
            "options": [
                "the designer’s confidence",
                "where a real user stops or succeeds",
                "the number of colours",
                "the price of the server",
            ],
            "answer": "B",
            "why": "Watching the user’s attempt is the test. Confidence and decoration are not evidence.",
        },
        {
            "q": "Zero trust means",
            "options": [
                "nobody is allowed to log in",
                "a device on the office network is still checked on each request",
                "passwords are abolished",
                "users are not told the rules",
            ],
            "answer": "B",
            "why": "Location inside the building is not treated as proof. Access is checked and limited.",
        },
        {
            "q": "Using red alone to mark a failing grade fails",
            "options": [
                "only the database",
                "accessibility, because colour must not be the only signal",
                "binary search",
                "the mean",
            ],
            "answer": "B",
            "why": "Some users cannot distinguish the colour, so the word or an icon must carry the meaning too.",
        },
    ],
    shorts=[
        {
            "q": "Define usability using the three standard parts, and illustrate one part with a portal task.",
            "a": "Usability is effectiveness, efficiency, and satisfaction for a particular user and task. Effectiveness: the student can download the practical. Efficiency: they do it in a few steps, not a tour of the site. Satisfaction: the labels match what they expect, so the task is not frustrating. A test watches them try.",
        },
        {
            "q": "Give one economic and one environmental effect of an unreadable on-screen notice.",
            "a": "Staff reprint and re-explain the notice, which costs time. Users print it themselves because they cannot read it on the phone, which wastes paper and toner. A readable page with a single official print reduces both.",
        },
        {
            "q": "Recommend one security measure for a shared lab PC and say how you keep it usable.",
            "a": "End the session when the browser closes or after a short idle time, so the next student does not inherit the account. Keep the idle time long enough to read a question, and put a visible countdown, so people are not thrown out mid-sentence. Personal passwords on a shared desktop profile are the wrong control.",
        },
    ],
    longs=[
        {
            "marks": 5,
            "q": "Explain human-computer interaction for a result portal under the headings usability, common problems, methods of improvement, ethical and social impact, and economic impact.",
            "a": (
                "Usability: a student should open their own result in a few steps and understand every label.\n\n"
                "Common problems: the roll number is asked for in a format the admit card does not use; the error says only “invalid”; the result is a scanned image that a screen reader cannot read.\n\n"
                "Improvement: show an example of the roll-number format, name the error, publish HTML or text as well as a print file, and run a usability test with students who did not build the site.\n\n"
                "Ethical and social: publishing a full list in roll-number order on an open wall may shame students and exposes data the task does not require. Showing a student their own result after login is the tighter design. An inaccessible scan excludes a blind student from the same news everyone else has.\n\n"
                "Economic: a confusing portal fills the office with visitors who only needed a file, so the college pays in staff time. Clear self-service is the cheaper system after the first careful design."
            ),
        },
        {
            "marks": 5,
            "q": "A bank app wants both a fast login and protection against a stolen phone. Describe the tradeoff and a recommendation that mentions cost, privacy, and a user who might be locked out.",
            "a": (
                "A login that is only a swipe is fast and weak if the phone is unlocked. A login that demands a long password plus two extra codes is stronger and will be bypassed or abandoned. "
                "The tradeoff is real: every extra step stops some thieves and also stops some customers.\n\n"
                "A fitting recommendation is a device unlock the user already has, then a second factor for payments only, not for looking at the balance. "
                "Cost stays down if the second factor is an authenticator or a prompt rather than an SMS on every glance. "
                "Privacy: the app does not need the contact list to do this. "
                "Ethics and lockout: a customer whose fingerprint fails, or who has lost the phone, needs a recovery path that a branch or a pre-printed code can complete, or the security measure becomes a refusal of service. "
                "Zero trust shows up as the payment being checked again even though the balance screen was already open."
            ),
        },
    ],
    labs=[
        {
            "title": "Lab 1 — Watch a user, then recommend a control",
            "steps": [
                "Sketch three paper screens of a task you know (finding a practical, or logging into a lab account).",
                "Give the paper to a classmate. Set the goal. Do not help. Note every hesitation.",
                "Change one screen. Retest with a different classmate.",
                "Add one security control to the same task. Write who might be locked out by it and how they recover.",
            ],
            "success": "The journal has the two test notes, the change, and a security recommendation that names a recovery path.",
        }
    ],
    summary=[
        "Usability is effectiveness, efficiency, and satisfaction. Accessibility widens who can succeed. Security limits harm.",
        "HCI studies that use and designs for it.",
        "A usability test watches a user attempt a goal. It is not a demo.",
        "Bad design has ethical, social, economic, and environmental effects. Give one concrete effect, not four adjectives.",
        "Security and usability trade off. Name efficiency, cost, privacy, and ethics.",
        "Zero trust checks each request. Least privilege limits what the successful login may do.",
        "A control without a recovery path locks people out and will be bypassed.",
    ],
)
