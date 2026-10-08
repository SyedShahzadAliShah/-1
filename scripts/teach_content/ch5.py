from .blocks import check, lecture, p, steps, svg, table, tip

CHAPTER = {
    "id": "ch5",
    "num": "05",
    "title": "Impacts of Computing",
    "blurb": "AI, IoT, data analytics, sources, aur assistive technology.",
    "lectures": [
        lecture(
            "computing-ai",
            "5.1 – 5.1.1",
            "Computing aur artificial intelligence",
            8,
            [
                p("Computing ab roz ki zindagi hai. Pakistan mein school, hospital, bank, khet, aur factory sab mein computer aa rahe hain. Phone aur internet bhi isi daire mein hain."),
                p("AI is liye artificial hai ke insaan ne banaya, aur intelligence is liye ke woh aisa kaam kare jis mein soch chahiye. AI data se faisla karta hai. Golden topic hai."),
                steps(
                    "Aas paas ki misaal",
                    [
                        "Phone ka face unlock.",
                        "YouTube jo aap ki pasand ki videos dikhaye.",
                        "Website ka chatbot.",
                        "Garm kamre mein sensor data dekh kar AC on kar dena.",
                    ],
                    "Face, recommendation, chatbot, aur AC ka faisla. AI system ka dimagh hai.",
                ),
                p("IoT aankhein hain, data ikattha karti hain. Analytics us data ko saaf karta hai. AI faisla karta hai. Phir actuator action leta hai."),
                check(
                    "AI ko system ka dimagh kyun kehte hain?",
                    "Kyunke sensor data aane ke baad faisla AI karta hai, jaise AC on karna.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "iot",
            "5.1.2",
            "Internet of Things aur us ke components",
            9,
            [
                p("IoT woh system hai jismein physical devices internet se jud kar data ikattha karte aur share karte hain, aur kaam khud ho jata hai. Smartwatch heart rate phone pe bhej de. Golden topic hai."),
                svg("iot", "Sensor collect karta hai, Wi-Fi le jati hai, cloud process karta hai, AI faisla karta hai, actuator kaam karta hai.", "IoT path from sensor to action."),
                table(
                    ["Component", "Kaam", "Misal"],
                    [
                        ["Sensor", "Dunya se data, aankh kaan", "Temperature, motion, fingerprint, soil"],
                        ["Actuator", "Digital ishare ko jismani kaam", "Motor, door, valve, fan"],
                        ["Connectivity", "Bina iske device behera hai", "Wi-Fi, Bluetooth, ZigBee, 4G, 5G"],
                        ["Processing", "Kachche data se faisla", "Kamra garam hai to AC"],
                        ["Cloud", "Bara data door store aur service", "Google Drive, online LMS"],
                        ["User interface", "Insaan dekhe aur hukum de", "App, touch screen, voice"],
                    ],
                    "Chhe hisse: sensor, actuator, connectivity, processing, cloud, interface.",
                ),
                check(
                    "Sensor aur actuator mein farq?",
                    "Sensor data leta hai. Actuator kaam karta hai, jaise pump ya motor.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "analytics",
            "5.1.3",
            "Data analytics ke paanch hisse",
            7,
            [
                p("Data analytics data ko ikattha, saaf, study, aur present karta hai taake behtar faisla ho. College marks ikattha kare, percent nikale, aur dekhe kin students ko extra help chahiye. Yeh poora amal analytics hai."),
                steps(
                    "Paanch components",
                    [
                        "Collection: websites, surveys, sensors, hospital, bank.",
                        "Storage: file, database, spreadsheet, cloud.",
                        "Cleaning: duplicate, typo, missing, galat format hatao.",
                        "Analysis: pattern. Kaun se subject mein fail zyada.",
                        "Visualization: chart, jaise pass aur fail ka pie.",
                    ],
                    "Collect, store, clean, analyse, phir chart.",
                ),
                svg("pie", "Pie chart pass aur needs-help ka hissa ek nazar mein dikha deta hai.", "Pass versus needs help."),
                check(
                    "Duplicate rows kis step mein hat-ti hain?",
                    "Data cleaning.",
                ),
            ],
        ),
        lecture(
            "compare-three",
            "5.1",
            "IoT, AI, aur analytics ka muqabla",
            6,
            [
                table(
                    ["", "IoT", "AI", "Data analytics"],
                    [
                        ["Definition", "Devices internet pe", "Machine sochay aur faisla kare", "Data se pattern"],
                        ["Purpose", "Data aur automation", "Smart decision", "Insight"],
                        ["Kaam", "Hardware devices", "Smart software", "Numbers aur records"],
                        ["Output", "Environment ka raw data", "Faisla ya action", "Report aur graph"],
                    ],
                    "IoT jism hai, AI dimagh, analytics samajh. Teeno mil kar smart system bante hain.",
                ),
                p("Khet ki misaal: soil sensor IoT hai. Numbers saaf karke dekhna analytics hai. Pani chahiye ya nahi, yeh faisla AI kare to pump chal jati hai."),
                check(
                    "Report aur graph kis ka output hai?",
                    "Data analytics ka.",
                ),
            ],
        ),
        lecture(
            "iot-uses",
            "5.2",
            "IoT shehron, sehat, aur kheton mein",
            8,
            [
                table(
                    ["Jagah", "Kaam"],
                    [
                        ["Smart city", "Signal, lights, parking, kachre ka dabba jab bhar jaye"],
                        ["Factory", "Machine ki garmi aur vibration, Sindh textile quality"],
                        ["Health", "Smartwatch, dehaat se doctor tak data, emergency alert"],
                        ["School", "Digital board, biometric attendance, AC"],
                        ["Ghar", "Light app se, camera, voice assistant"],
                        ["Kheti", "Soil moisture, pump on off, drone se fasal"],
                    ],
                    "Sheher, factory, sehat, school, ghar, aur khet. Pakistan mein paani bachane ke liye smart farming khas hai.",
                ),
                p("Smart farming ka flow: soil sensor, cloud, sawal ke paani chahiye, phir water pump. Sindh aur Punjab dono mein paani mehnga aur kam hai, is liye yeh misaal syllabus mein zaroori hai."),
                check(
                    "Smart bin IoT mein kya karta hai?",
                    "Jab bhar jaye to alert bhejta hai, taake gaadi khali safar na kare.",
                ),
            ],
        ),
        lecture(
            "ai-pakistan",
            "5.2.1",
            "Pakistan ki taleem mein AI",
            7,
            [
                p("AI dheere dheere Pakistan ke schools mein aa raha hai: parhana, seekhna, aur administration."),
                steps(
                    "Istemal aur faida",
                    [
                        "Learning management system.",
                        "Automatic grading aur digital test.",
                        "Career counselling.",
                        "Har student apni raftar se seekhe.",
                        "Jo student peeche hai usay pehchanen.",
                        "Disability mein assistive AI.",
                    ],
                    "LMS, grading, counselling, apni speed, extra help, assistive support.",
                ),
                p("Mushkilein bhi sach hain: dehaat mein internet kam, har student ke paas device nahi, teachers ki training kam, aur data privacy ka khatra."),
                p("Career: IoT engineer devices design kare. Data analyst IoT ka data parhe. Skills: Python ya C++, networking, sensors, aur problem solving. Jazz, Telenor, banks, aur government IT departments jagah hain."),
                check(
                    "Pakistan mein AI education ki ek bari mushkil?",
                    "Dehaat mein limited internet, devices ki kami, ya teacher training.",
                ),
            ],
        ),
        lecture(
            "sources",
            "5.3",
            "Primary, secondary, tertiary sources",
            8,
            [
                p("Information source woh raasta hai jahan se ilm milta hai. Internet pe sab sach nahi hota. Teen qismen hain. Golden topic hai."),
                svg("sources", "Neeche primary, asli data. Beech secondary, kisi aur ki sharah. Upar tertiary, mukhtasar reference.", "Source pyramid."),
                table(
                    ["Source", "Kya hai", "Misal"],
                    [
                        ["Primary", "Pehli haath, event ya record", "Interview, photo, diary, NADRA record"],
                        ["Secondary", "Kisi aur ne samjhaya hua", "Textbook, news, research paper, statistics report"],
                        ["Tertiary", "Dono ka khulasa, jaldi dekhne ke liye", "Encyclopedia, Wikipedia, dictionary, handbook"],
                    ],
                    "Primary asli, secondary sharah, tertiary khulasa.",
                ),
                p("Source bharosa ke qabil nahi jab primary adhoori ya jaan boojh kar jhoot ho, secondary purani ho ya reference na ho, tertiary anjaan website se ho ya itni simple ho ke fact hi marr jaye."),
                tip("Online article pe naam nahi, tareekh nahi, references nahi, to academic kaam ke liye usay mat maano."),
                check(
                    "Wikipedia primary hai ya tertiary?",
                    "Tertiary. Khulasa hai, pehli haath ka record nahi.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "impacts",
            "5.4",
            "Computing ke asraat",
            7,
            [
                p("Computing zindagi tez aur judi hui banata hai, lekin privacy, naukri, aur screen ki lat bhi laata hai. Har field mein dono pehlu likhna exam mein behtar hai."),
                table(
                    ["Field", "Faida", "Khatra"],
                    [
                        ["Taleem", "Door se seekhna, digital books", "Screen, copy paste bina samjhe"],
                        ["Sehat", "Records, remote doctor", "Patient data leak"],
                        ["Karobar", "Tez hisaab, online dukaan", "Naukriyon ka badalna, cyber attack"],
                        ["Samaj", "Rabta asaan", "Privacy, rumour, lat"],
                    ],
                    "Faida tez raabta hai. Khatra privacy, job change, aur addiction hai.",
                ),
                check(
                    "Computing ka ek social khatra batao.",
                    "Privacy ka khatra, ya technology ki lat.",
                ),
            ],
        ),
        lecture(
            "assistive",
            "5.5",
            "Assistive technologies",
            7,
            [
                p("Assistive technology woh device, software, ya system hai jo disability ya functional limitation mein madad kare, taake zyada log barabari se shamil ho saken. Golden topic hai."),
                steps(
                    "Misalen",
                    [
                        "Screen reader, jo screen ki likhai sunaye. Andhe student ke liye.",
                        "Captions aur hearing aids, sunne mein madad.",
                        "Voice control, haath se mouse mushkil ho to.",
                        "Smart wheelchair aur ramp ke sath digital access.",
                        "Text ko bari font ya high contrast.",
                    ],
                    "Screen reader, captions, voice, wheelchair, bari font.",
                ),
                p("Yeh course khud bhi assistive soch rakhta hai: lecture sunai de, sirf parhne pe depend na ho. Sunain button isi wajah se hai."),
                check(
                    "Screen reader kis student ki madad karta hai?",
                    "Jo screen ki likhai nahi dekh sakta. Software text bol kar sunata hai.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "assistive-why",
            "5.5.1",
            "Assistive technology kyun zaroori hai",
            6,
            [
                steps(
                    "Teen wajuhat",
                    [
                        "Taleem mein barabari: screen reader se digital kitab usi tarah khule jaise doosre students ke liye.",
                        "Roz marra ki azadi: khud message, khud form, khud safar.",
                        "Shirkat: class, naukri, aur samaj se bahar na rahen.",
                    ],
                    "Barabari, azadi, aur shirkat.",
                ),
                p("Agar school ki website sirf mouse se chale aur keyboard se nahi, to kai students bahar reh jate hain. Access baad ki soch nahi, shuru ki soch hai."),
                check(
                    "Equal access ka matlab kya hai?",
                    "Disability ke bawajood wahi taleem aur mauqa jo baqi students ko milta hai.",
                ),
            ],
        ),
        lecture(
            "assistive-career",
            "5.5.2",
            "Assistive technology mein career",
            6,
            [
                p("Jo student computing seekh raha hai woh aise tools bana sakta hai jo logon ko shamil karein. Yeh sirf charity nahi, asli software kaam hai."),
                table(
                    ["Role", "Kaam"],
                    [
                        ["Accessibility specialist", "Apps ko screen reader aur keyboard se chalana"],
                        ["Speech and language tech", "Awaaz se likhai, text se awaaz"],
                        ["Rehab engineer", "Wheelchair, prosthetic, sensors"],
                        ["UX researcher", "Disabled users ke sath test karna"],
                    ],
                    "Accessibility, speech tech, rehab engineering, aur inclusive UX.",
                ),
                p("Shuruat chhoti ho sakti hai: apni class ki website pe captions, contrast, aur clear Urdu-English labels. Wahi skill baad mein product ban jati hai."),
                check(
                    "Accessibility specialist kya check karta hai?",
                    "Ke app screen reader, keyboard, aur clear layout se chale.",
                ),
            ],
        ),
    ],
}
