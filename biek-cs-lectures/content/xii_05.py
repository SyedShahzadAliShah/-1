from content.schema import lecture

LECTURE = lecture(
    id="xii-5",
    number=5,
    title="Applications, Privacy, and Safe Collaboration",
    kicker="CLASS XII  ·  UNIT 5",
    unit="Unit 5 — Applications and Impacts of Computing",
    domain="E, F, and G. Applications, impacts, and digital research",
    periods="about 40 periods",
    intro=(
        "Class XI introduced IoT, cloud, blockchain, bias, and the digital divide. "
        "Class XII asks you to design an application for a Pakistani setting, to explain deep learning without advertising it, "
        "and to handle the conflicts that appear when data is shared. "
        "It also asks how you work safely with other people online, and how you publish a finding with digital tools."
    ),
    outcomes=[
        "Propose an application for Pakistan that uses IoT, cloud computing, or blockchain, including a risk.",
        "Explain deep learning as layered neural networks that learn features, and name a use and a limit.",
        "Describe a data-sharing conflict and a policy compromise.",
        "Name common attacks by their impact and match them to 2FA, biometrics, and encryption in transit.",
        "Collaborate more safely, and publish a small research artifact with an advanced search behind it.",
    ],
    blocks=[
        ("h2", "An application for a real setting"),
        (
            "p",
            "A design answer has a user, a job to be done, the data, which of IoT, cloud, or blockchain is actually needed, and a risk. Adding all three technologies to sound modern is a weak answer. A soil sensor does not need a blockchain. A degree check might use a hash on a shared ledger and does not need a moisture sensor.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — flood marks along a river",
                "text": (
                    "User: a district officer and the villages upstream of a known low road.\n\n"
                    "Job: know when a water level is rising faster than usual, early enough to close the road.\n\n"
                    "Data: a water-level reading every few minutes, the sensor’s id, and the time. Not the names of residents.\n\n"
                    "Technology: IoT sensors send readings to a cloud dashboard. The cloud is justified because more than one office must see the same history, and a local memory card in a drowned box is a bad archive. Blockchain is not justified.\n\n"
                    "Risk: a failed radio looks the same as a calm river if the dashboard does not show “sensor silent”. The design must alarm on silence, not only on high water."
                ),
            },
        ),
        ("h2", "Deep learning"),
        (
            "p",
            "A **neural network** is a model made of many simple units in layers. Early layers transform the input. Later layers produce a prediction. **Deep learning** means a neural network with many layers, trained on a large number of examples. Its practical claim is that it can learn **features** from raw input — pixels, sound samples — instead of waiting for a person to invent every feature. That is why it shows up in image recognition, speech, and translation.",
        ),
        (
            "p",
            "The limits belong in the same paragraph. It needs a lot of examples and a lot of computing. If those examples are skewed, the errors are skewed. It can be hard to explain which part of a photograph drove a decision. A crop-disease photo tool may help a farmer decide to ask an expert. It is not itself the expert, and a Class XII answer should not claim a medical or agricultural diagnosis.",
        ),
        (
            "table",
            {
                "caption": "Table 14. Traditional machine learning versus deep learning, for a short comparison question.",
                "headers": ["", "Traditional machine learning", "Deep learning"],
                "rows": [
                    ["Features", "Often designed by a person", "Often learned from raw data"],
                    ["Data and compute", "Can work on smaller sets", "Usually wants much more of both"],
                    ["Explanation", "Sometimes easier to point at a feature", "Often harder to explain a single decision"],
                    ["A fitting job", "Predict a mark from a few numbers", "Classify a photograph or a sound"],
                ],
                "widths": [0.22, 0.39, 0.39],
            },
        ),
        ("h2", "Sharing data and keeping a boundary"),
        (
            "p",
            "**Data sharing** lets another party do something useful: a hospital shares case counts with a health department, a university confirms to an employer that a degree is real. **Privacy** says the person the data is about still has a boundary. The two goals conflict as soon as the useful share reveals more than the job needs. There is no design in which everybody gets everything and nobody is exposed. A policy is a compromise you can defend.",
        ),
        (
            "p",
            "Useful compromises are specific. Share counts, not names. Share a yes/no check of a degree, not the transcript. Keep the detailed rows with the organisation that collected them, and let outsiders ask a narrow question. Write down who may receive the data and for how long. Give the person a way to ask what is held. When stakeholders disagree — the company wants an advertisement profile, the student wants to be left alone, the college wants alumni news — the answer should say whose interest you would not sacrifice and why. “Balance” without a decision is not a policy.",
        ),
        ("h2", "Attacks and the controls that match them"),
        (
            "p",
            "You should recognise the following by the harm they cause, and refuse to confuse them. **Phishing** is a message that imitates a trusted party in order to collect a secret or a payment. **Malware** is software that harms a device or the data; **ransomware** is malware that locks files and demands payment; **spyware** is malware that reports what you do. A **virus** spreads by attaching to other files people open. A **DDoS** attack floods a service until genuine users cannot reach it. These are different jobs. A strong password does not stop a flood of a public website, and a backup does not by itself stop a phishing page.",
        ),
        (
            "table",
            {
                "caption": "Table 15. Controls to pair with threats. Describe the control; do not invent a system to carry the attack out.",
                "headers": ["Control", "What it improves", "The limit"],
                "rows": [
                    ["2FA", "A stolen password is not enough to log in", "A one-time code can itself be phished if the user is rushed"],
                    ["Biometric check", "The person is present, and they need not remember a long secret", "A fingerprint database leak cannot be “reset” like a password; some people cannot use the sensor"],
                    ["Encryption in transit", "Someone on the path sees ciphertext, not the message. HTTPS is the ordinary web example", "It does not make a fraudulent website honest. The lock icon is not a review of the business"],
                    ["Backup", "Ransomware or a failed disk does not end the only copy", "A backup that shares the same password and the same infection is a weak backup"],
                    ["Least privilege", "A stolen clerk account cannot do an administrator’s job", "It does nothing if everyone shares one administrator login"],
                ],
                "widths": [0.22, 0.40, 0.38],
            },
        ),
        (
            "p",
            "Safe collaboration uses the same controls. A shared folder has named people, not a link that anyone on the Internet can edit. A group project does not live in one student’s personal account with the password handed around. You agree what must not be uploaded: another person’s identity card, a full set of marks with names, a password “so you can submit for me”. Identity theft becomes easier when those documents are scattered across chats. The practical habit is to collect less and to share the document, not the login.",
        ),
        ("h2", "Publishing a small research artifact"),
        (
            "p",
            "Class XII’s digital-literacy outcome is an **artifact**: a short report, a slide deck, or a notebook that answers a question and shows the evidence. The search behind it should use operators from Class XI, and the page should be judged, not merely found. The artifact itself has a question, a method, a chart or a quoted official figure with a date, a conclusion, and a limit. Digital tools help because the chart, the source link, and the revision history are visible. They do not replace the reading.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — a one-page artifact",
                "text": (
                    "Question: what does our college actually collect before a student can use the lab network?\n\n"
                    "Method: read the college’s own notice (secondary, official) and interview the lab in-charge with five questions (primary). "
                    "Search used: the college name plus `site:.edu.pk` and the word “laboratory”.\n\n"
                    "Finding: the notice asks for a roll number and a parent phone number. The in-charge also keeps a photocopy of the identity card, which the notice does not mention.\n\n"
                    "Conclusion, limited: in this college the practice is wider than the notice. "
                    "Recommendation: stop the photocopy or add it to the notice and say who may see it. "
                    "This is a policy suggestion for one college, not a law you have drafted for the country."
                ),
            },
        ),
        (
            "callout",
            {
                "kind": "note",
                "title": "Equity",
                "text": "A design that only works in English, only on a new phone, or only with a camera on, shares its benefits with the students who already had the most access. When you propose an application, say how a student on a shared basic phone still gets the essential message, even if that message is an SMS rather than a dashboard.",
            },
        ),
    ],
    terms=[
        ("Deep learning", "Neural networks with many layers, trained to learn features from raw data."),
        ("Neural network", "A layered model of simple units that produces a prediction."),
        ("Data sharing", "Giving another party access to data for a stated job."),
        ("Privacy", "The boundary around a person the data is about."),
        ("Phishing", "A fake message aimed at stealing a secret or a payment."),
        ("Ransomware", "Malware that locks files and demands payment."),
        ("2FA", "A login that needs a second, different proof."),
        ("Artifact", "A digital product that states a finding and the evidence."),
    ],
    checks=[
        {
            "q": "Why is blockchain a mismatch for the flood-sensor example?",
            "a": "The problem is timely readings and a shared dashboard, which a cloud store already provides. A shared ledger does not detect a silent sensor and adds a design the user did not need.",
        },
        {
            "q": "What does encryption in transit fail to guarantee?",
            "a": "It hides the contents on the path. It does not prove the site is honest. A phishing site can also show a lock.",
        },
        {
            "q": "Name one equity feature for a parent who has a basic phone.",
            "a": "Send the essential alert as an SMS, not only as a page on a dashboard that the phone cannot open.",
        },
    ],
    mcqs=[
        {
            "q": "Deep learning differs from a small traditional model mainly because it",
            "options": [
                "never uses data",
                "can learn features from raw inputs such as pixels, using many layers",
                "is always easy to explain",
                "does not make errors",
            ],
            "answer": "B",
            "why": "Many layers and learned features are the distinction. Explanation and perfection are not promised.",
        },
        {
            "q": "A DDoS attack primarily harms",
            "options": [
                "availability",
                "the grammar of SQL",
                "inorder traversal",
                "the mean of a sample",
            ],
            "answer": "A",
            "why": "The service is flooded so genuine users cannot use it. That is an availability failure.",
        },
        {
            "q": "The better share of degree data with an employer is",
            "options": [
                "the full school file of every student",
                "a check that this named degree was awarded",
                "the student’s home address and marks in every class",
                "a public copy of the identity card",
            ],
            "answer": "B",
            "why": "The job is verification. The other options share far more than the job needs.",
        },
        {
            "q": "2FA helps most against",
            "options": [
                "a flood of traffic on a public site",
                "a stolen password used from elsewhere",
                "a lost backup disk that was never encrypted",
                "a chart with no axis",
            ],
            "answer": "B",
            "why": "The second factor blocks a password that is no longer secret. It does not stop a traffic flood.",
        },
    ],
    shorts=[
        {
            "q": "Give one Pakistani IoT idea and the risk you would mention in the same answer.",
            "a": "Moisture sensors in a field send readings to a cloud store, and the farmer gets an SMS when the soil stays dry. The risk is a dead battery or a missing signal looking like “no problem” unless the system alerts on silence. Names of the farmer’s family are not required.",
        },
        {
            "q": "Contrast phishing with ransomware in one sentence each, and name one control for each.",
            "a": "Phishing tricks a person into handing over a secret; a control is to open the service from a bookmark and to use 2FA so a captured password is incomplete. Ransomware locks files; a control is a backup that is not continuously open to the infected machine, plus not opening unexpected attachments. Paying is not a control you should describe as reliable.",
        },
        {
            "q": "What four parts should a one-page research artifact have?",
            "a": "A question, a method that says whether the data is primary or secondary, a result the reader can check, and a conclusion that does not outrun the sample. A date on the sources belongs with the method.",
        },
    ],
    longs=[
        {
            "marks": 5,
            "q": "Design a degree-verification idea using cloud computing or blockchain. Explain the choice, the privacy compromise, and one stakeholder who may dislike it.",
            "a": (
                "The user is an employer who wants to know whether a named person was awarded a named degree. "
                "The university keeps the full record. What is shared is a check: yes or no, plus the year and the title of the award. "
                "A hash of that record, or a signature the university can verify, can be looked up without copying the transcript. "
                "A blockchain fits only if several universities and employers need a ledger none of them alone controls. "
                "A single university can do the same job with a cloud service and a signed answer, which is simpler. Choose one and say why.\n\n"
                "Privacy: the employer does not receive address, grades, or identity-card scans. "
                "The student should be able to see who asked. "
                "A stakeholder who may dislike it is a vendor of paper certificates, or an employer who wanted the full transcript for other, less declared uses. "
                "The policy refuses that wider share."
            ),
        },
        {
            "marks": 5,
            "q": "Your project group works in a shared online folder and on a chat. Describe three unsafe habits and the safer practice for each. Then say how you would present the group’s findings so a marker can check them.",
            "a": (
                "Sharing one login is unsafe because you cannot tell who changed a file and you cannot remove one person later. Invite named accounts instead. "
                "Posting a classmate’s identity card “for the report” is unsafe because that image is enough for identity theft. Collect roll numbers only if the question needs them, and do not put them in the chat. "
                "A public editing link is unsafe because strangers, not only the group, can change the work. Restrict the folder to the group and the teacher.\n\n"
                "The artifact is a short report or a few slides: the question, the method, one chart with n, the sources with dates, and a limit. "
                "The folder’s history shows who wrote what. The chat is not the report."
            ),
        },
    ],
    labs=[
        {
            "title": "Lab 5 — A design page and a safer folder",
            "steps": [
                "Write a one-page design: user, job, data, one technology, one risk, one equity note.",
                "Write a privacy rule for that design in two sentences: what is shared, what is not.",
                "Create a shared folder for your pair with named access. Record one unsafe alternative you refused.",
                "Add a five-line artifact that cites one source you found with a search operator.",
            ],
            "success": "The design names a technology it refused, as well as one it used. The folder is not shared by a single password.",
        }
    ],
    summary=[
        "Use IoT, cloud, or blockchain only when the job needs it. Name the risk and the user.",
        "Deep learning learns features in many layers from raw data. It wants data and compute, and it can copy bias.",
        "Share the minimum that does the job. A policy names who gets what, not a vague balance.",
        "Phishing, ransomware, and DDoS are different harms. Match 2FA, backups, and service-level defences correctly.",
        "Encryption in transit hides the message on the path. It does not make the sender honest.",
        "Collaborate with named access. Do not pass logins or identity documents through a chat.",
        "An artifact has a question, a method, a checkable result, and a limited conclusion.",
    ],
)
