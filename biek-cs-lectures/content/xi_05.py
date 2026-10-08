from content.schema import lecture

LECTURE = lecture(
    id="xi-5",
    number=5,
    title="Applications and Impacts of Computing",
    kicker="CLASS XI  ·  UNIT 5",
    unit="Unit 5 — Applications and Impacts of Computing",
    domain="E and F. Applications and impacts",
    periods="about 30 periods",
    intro=(
        "The same ideas from systems, programs, and data show up in devices that sense the world, "
        "in services that rent computing instead of buying it, and in records that many parties can check. "
        "This lecture treats the Internet of Things, cloud computing, and blockchain at the level of what makes them possible and where they help in Pakistan. "
        "It then turns to the human side: whose interests an automated decision serves, which sources deserve trust, and who is left out when connectivity grows."
    ),
    outcomes=[
        "Describe the parts of an IoT system and the technologies that made IoT, cloud computing, and blockchain practical.",
        "Give a concrete use in a Pakistani setting without exaggerating what the technology guarantees.",
        "Identify stakeholders in an AI-style decision and a conflict between their interests.",
        "Separate a reliable information source from an unreliable one, and name bias in data.",
        "Discuss connectivity, assistive technology, the digital divide, and one environmental impact.",
    ],
    blocks=[
        ("h2", "Internet of Things"),
        (
            "p",
            "The **Internet of Things (IoT)** is ordinary objects — meters, pumps, wristbands, classroom sensors — that collect data and communicate it so a person or another system can act. A typical chain has four parts. A **sensor** measures something physical, such as moisture or temperature. A **network** carries that reading. A **processor**, often helped by a **cloud** service, stores or judges it. An **actuator** does something in the world, such as opening a valve, or the “action” is simply a message to a person.",
        ),
        (
            "p",
            "This became ordinary because several older limits moved at once: devices got smaller, they use less power, radios got cheap, and distant servers can store what a tiny device cannot. None of those is the IoT by itself. A thermometer with no link is just a thermometer.",
        ),
        (
            "table",
            {
                "caption": "Table 9. Uses named in the Class XI course, with a limit beside each so the answer stays honest.",
                "headers": ["Setting", "What the system does", "What it does not do"],
                "rows": [
                    ["Smart city", "Traffic or bin sensors report status to a dashboard", "It does not replace road building or a maintenance budget"],
                    ["Industry", "A machine reports vibration before it fails", "A sensor does not repair the machine"],
                    ["Healthcare", "A wearable shares a pulse trend with a clinic", "It is not a diagnosis"],
                    ["Education", "A lab logs equipment use", "It does not teach the practical"],
                    ["Smart grid", "Meters report use so supply can be planned", "It does not create electricity"],
                    ["Smart farming", "Soil sensors suggest when to irrigate", "It does not know a pest it was not built to detect"],
                    ["Wearable", "A band counts steps or heart rate", "The reading can be wrong if the band is loose"],
                ],
                "widths": [0.18, 0.42, 0.40],
            },
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — a Sindh farm, kept small",
                "text": (
                    "A cotton field has three moisture sensors. Twice a day they send a number over the mobile network to a small cloud store. "
                    "If the reading stays below a threshold the farmer chose, the farmer gets an SMS. The actuator is the farmer’s own pump, not a fantasy robot.\n\n"
                    "The enabling technologies are a cheap sensor, a radio, and remote storage. The failure modes belong in the answer: no signal, a flat battery, a sensor in a puddle that is not typical of the field. "
                    "A good design says who is allowed to see the farm’s data. An open map of every field’s water use may not be what the farmer agreed to."
                ),
            },
        ),
        ("h2", "Cloud computing"),
        (
            "p",
            "**Cloud computing** is renting storage, processing, or applications over the network instead of housing every server in the college. The college reaches them through the Internet. The appeal is scale: a result day needs more capacity than a Sunday, and the extra capacity can be temporary. The costs are a subscription, a dependence on the link, and a duty to know which country holds the data and who can be asked for it. “It is in the cloud” is not a security design. Access rules, encryption on the link, and backups still have to be chosen.",
        ),
        ("h2", "Blockchain, at the level this course needs"),
        (
            "p",
            "A **blockchain** is a shared ledger of records, grouped into blocks, linked so that changing an old record is obvious. Copies sit with more than one party. **Cryptography** — hashes and digital signatures — is what makes tampering visible and ties a record to the holder of a private key. The ledger does not need a single clerk whom everyone must trust to be the only copy.",
        ),
        (
            "p",
            "That is useful when the problem is “we do not share one office, and we need to agree what was recorded”: a degree verification hash that a university and an employer can both check, or a shipment log. It is a poor fit when the data changes every minute, when privacy requires that the data be deletable, or when a normal database with a responsible owner would do. A blockchain does not make a false document true. It makes a later silent edit harder. Putting a student’s full record on a public ledger can itself be the harm.",
        ),
        (
            "callout",
            {
                "kind": "exam",
                "title": "Exam tip",
                "text": "A question that says “design an idea for Pakistan” wants the user, the data, the technology, and one risk. A definition of IoT with no scene, or a scene with no risk, is a thinner answer than one paragraph that has all four.",
            },
        ),
        ("h2", "Stakeholders and automated decisions"),
        (
            "p",
            "An **artificial intelligence** system, even a simple one that ranks applications, has **stakeholders**: the people who gain or lose from its output. They rarely want the same thing. A college wants fast shortlisting. An applicant wants a fair chance and an explanation. A vendor wants the contract renewed. A parent wants to know the data will not be sold. Culture and values change what “fair” means: a form that assumes one kind of name, one language, or one kind of school will quietly disadvantage everyone else.",
        ),
        (
            "p",
            "When you evaluate a design, name at least three stakeholders and one conflict. Then name a policy that reduces the harm: a right to ask for a human review, a limit on what is collected, a test of the system on more than one group before it is trusted, or a refusal to use the system for that decision at all. “The computer said so” is not an explanation.",
        ),
        ("h2", "Reliable and unreliable information"),
        (
            "p",
            "A **reliable source** can be checked. You can see who wrote it, when, and what evidence they used, and another careful source can be compared with it. An official board notification on the board’s own site, a textbook passage, and a dataset with a described method are in that family. An **unreliable source** hides the author, uses urgency instead of evidence, or cannot be matched to anything else: a forwarded screenshot of a date sheet, an unnamed “expert”, a chart with no axis.",
        ),
        (
            "p",
            "**Bias** enters before the chart. If a survey about college facilities is filled only by students who already have phones and data packages, the answers miss the students the question most concerns. If a face-detection demo is trained mostly on one kind of face, its errors will not be evenly spread. Humans are biased in what they bother to record. Computing does not wash that out. It can copy it quickly. Part of responsible use is to ask what was not collected.",
        ),
        ("h2", "Connectivity, people, and the environment"),
        (
            "p",
            "Computing raised **connectivity**. Email, the web, **Wi-Fi**, and **Bluetooth** let people and devices share data without a dedicated wire for every pair. Commerce uses that for orders and payments. Families use it to stay in touch. The same links carry harassment, scams, and rumours at the same speed as the useful messages. The impact is not “good” or “bad” as a single word. It depends on the design and on who can join.",
        ),
        (
            "p",
            "**Assistive technology** is computing that reduces a barrier: a screen reader, captions on a video, a high-contrast display, voice input, a larger target on a touch screen. It is not a special favour added at the end. A portal that only works with a mouse, or a lecture video with no captions, excludes a student the college already enrolled. The same features help people on a noisy bus or in bright sun, so they are ordinary good design.",
        ),
        (
            "p",
            "The **digital divide** is the gap in devices, connections, skills, language, and accessibility. A homework task that assumes a laptop and a quiet broadband evening is a different task in a household that shares one phone. Equity is not solved by a slogan. Practical steps include an offline copy of the worksheet, a lab hour, more than one language where the content allows, and not requiring a camera-on policy that some homes cannot meet.",
        ),
        (
            "p",
            "The **environmental** impact is physical. Devices become **e-waste** when they are discarded with batteries and circuit boards still in them. Data centres use electricity, and so do blockchains that constantly recompute. The relieving side is also real: a form that removes a repeated rickshaw trip, a sensor that stops a pump watering a wet field. A balanced answer names one cost and one saving, and does not pretend the saving is automatic.",
        ),
        (
            "callout",
            {
                "kind": "note",
                "title": "Culture and daily life",
                "text": "Connectivity changes how people coordinate family events, how shopkeepers take orders, and which language a young person reads most often. Those are cultural impacts. Mention one that you have actually seen, and keep it specific. A marker can tell a lived example from a slogan.",
            },
        ),
    ],
    terms=[
        ("IoT", "Objects that sense, communicate, and support an action."),
        ("Sensor / actuator", "A device that measures, and a device that acts."),
        ("Cloud computing", "Rented storage or processing reached over the network."),
        ("Blockchain", "A shared, tamper-evident ledger held in more than one place."),
        ("Stakeholder", "A person or group affected by a system’s decisions."),
        ("Reliable source", "An account whose author, date, and evidence can be checked."),
        ("Bias", "A systematic tilt in what was collected or how it is judged."),
        ("Assistive technology", "Tools that reduce a barrier to using computing."),
        ("Digital divide", "Unequal access to devices, links, skills, language, or accessibility."),
        ("E-waste", "Discarded electronic equipment, including batteries."),
    ],
    checks=[
        {
            "q": "Name the four parts of a simple IoT chain.",
            "a": "A sensor, a network, processing or storage (often in the cloud), and an action — either an actuator or a message to a person.",
        },
        {
            "q": "Why is a public blockchain a bad place for a full medical file?",
            "a": "Many copies make deletion and privacy difficult, and the patient may not want every holder of the ledger to see the file. A hash used for checking a record is a different, smaller idea than publishing the record itself.",
        },
        {
            "q": "Give one check that a forwarded date-sheet image fails.",
            "a": "You cannot confirm the author or the date against the board’s own notice. A screenshot can be edited. The reliable step is to open the board’s site or the college’s official notice.",
        },
    ],
    mcqs=[
        {
            "q": "Which set made IoT practical?",
            "options": [
                "Larger devices, no radios, and local-only files",
                "Smaller low-power devices, cheap connectivity, and remote computing",
                "Paper forms and a single clerk",
                "A faster printer",
            ],
            "answer": "B",
            "why": "The curriculum point is that size, power, connectivity, and processing moved together.",
        },
        {
            "q": "A blockchain’s useful property in this course is that",
            "options": [
                "it makes false data true",
                "altering an old record is evident and copies are shared",
                "it replaces every database",
                "it uses no cryptography",
            ],
            "answer": "B",
            "why": "Tamper-evidence and a shared copy are the point. Cryptography is how that is achieved, so D is the opposite.",
        },
        {
            "q": "A screen reader is best classified as",
            "options": [
                "e-waste",
                "assistive technology",
                "a network topology",
                "a primary key",
            ],
            "answer": "B",
            "why": "It reduces a barrier to using a computer.",
        },
        {
            "q": "A survey answered only by students with home broadband is a weak basis for a claim about all students because of",
            "options": [
                "referential integrity",
                "bias in who could respond",
                "bubble sort",
                "symmetric encryption",
            ],
            "answer": "B",
            "why": "The people who could not respond are exactly the people a digital-divide question is about.",
        },
    ],
    shorts=[
        {
            "q": "Distinguish cloud computing from “saving a file on the PC in the lab”.",
            "a": "The lab PC keeps the file on local hardware the college owns and that others cannot reach once they leave. Cloud computing stores or processes the file on rented machines reached over the network, so it can be opened from elsewhere and scaled, and so it depends on the link and on the provider’s rules.",
        },
        {
            "q": "Name three stakeholders in an automated college-admission shortlist and one conflict.",
            "a": "Applicants want a fair and explainable decision. The college wants speed and fewer clerks. The software vendor wants the product accepted. A conflict: the college’s wish for fully automatic rejection conflicts with the applicant’s wish for a human review when a certificate was scanned badly.",
        },
        {
            "q": "State one environmental cost of computing and one way computing can reduce waste.",
            "a": "Discarded phones and lab PCs are e-waste if they are thrown out with their batteries. A moisture sensor that stops a pump on a wet field can save water and electricity. The saving happens only if someone acts on the reading.",
        },
    ],
    longs=[
        {
            "marks": 5,
            "q": "Propose an IoT idea for a public school in Karachi during hot months. Include the sensor, the network, the action, the cloud’s role, and one privacy or reliability risk.",
            "a": (
                "Each classroom has a temperature sensor. Readings go over the school’s Wi-Fi to a small cloud dashboard the head teacher can open. "
                "The action is not an automatic air conditioner the school may not have; it is a warning when a room stays above a chosen temperature, so the timetable can move that class, or a fan can be checked. "
                "The cloud stores the week’s readings so a single hot afternoon is not mistaken for a broken fan.\n\n"
                "Reliability: if the Wi-Fi fails, the dashboard goes quiet, so the design needs a local display on the sensor itself. "
                "Privacy: the system measures rooms, not students’ bodies, and it does not need names. Adding cameras “while we are at it” would be a different, much harder decision and is not required for this idea."
            ),
        },
        {
            "marks": 5,
            "q": "A video claims that a new vitamin “doubles marks”, and the only evidence is a chart with no axis and no author. Explain how you would judge the source, and connect your judgement to bias and the digital divide.",
            "a": (
                "The source fails the basic checks: no author, no date, no method, and a chart that cannot be read. "
                "I would look for a named study, a sample size, and a comparison that could be found again. A forwarded video is not that study.\n\n"
                "Bias: the claim may come from an advertiser who selected only the students who improved. "
                "The digital divide matters because students who only meet the claim on a shared phone, in a language they are less sure of, have less chance to open the original source. "
                "Teaching people to ask for the author and the axis is part of equal access to information, not a separate moral lesson."
            ),
        },
    ],
    labs=[
        {
            "title": "Lab 7 — One technology, one page",
            "steps": [
                "Choose IoT, cloud, or blockchain.",
                "Describe a user in Pakistan, the data, where it is stored, and the action.",
                "Name two stakeholders and one conflict.",
                "Name one reliability risk and one privacy risk.",
                "Find one source you would trust for a definition of the technology, and write why you trust it (author, organisation, date).",
            ],
            "success": "The page has a specific user and a specific risk. The source note says who published it and when, not only the website name.",
        }
    ],
    summary=[
        "IoT is sensor, network, processing, and an action. Small, low-power, connected devices plus the cloud made it practical.",
        "Name a Pakistani scene, and name what the system cannot do.",
        "Cloud computing rents capacity. It still needs access rules and a working link.",
        "A blockchain is a shared tamper-evident ledger. It does not make false data true, and it is a bad home for a secret file.",
        "List stakeholders and the conflict between them before you praise an automated decision.",
        "A reliable source has an author, a date, and evidence. Bias often begins with who was never measured.",
        "Assistive technology and the digital divide belong in the same answer as the benefits of Wi-Fi. E-waste is part of the environmental cost.",
    ],
)
