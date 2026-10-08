from .blocks import check, code, lecture, p, steps, svg, table, tip

CHAPTER = {
    "id": "ch6",
    "num": "06",
    "title": "Digital Literacy",
    "blurb": "Data ki qismen, collection, primary secondary, aur digital inquiry.",
    "lectures": [
        lecture(
            "literacy-intro",
            "6.1 – 6.2",
            "Digital literacy aur information age",
            7,
            [
                p("Digital literacy ka matlab sirf phone chalana nahi. Devices, internet, aur online tools ko mehfooz, asar dar, aur zimmedari se use karna. Maloomat dhoondhna, raabta, digital cheez banana, aur masla hal karna."),
                p("Information age woh daur hai jismein data foran banta, banta, aur milta hai. Device ka hona kafi nahi. Samajhna, sambhalna, aur hikmat se use karna alag skill hai. Is mein technical, sochne wali, aur social teen qabiliyatain hain."),
                tip("Digitally literate student information dhoondhta hai, usay sajata hai, kaam ki cheez banata hai, aur share karte waqt zimmedari nibhata hai."),
                check(
                    "Digital literacy sirf typing hai?",
                    "Nahi. Mehfooz, samajhdar, aur zimmedar istemal hai.",
                ),
            ],
        ),
        lecture(
            "qual-quant",
            "6.3",
            "Qualitative aur quantitative data",
            7,
            [
                p("Survey ya class project ka data do tarah ka hota hai. Farq samajhna analysis ke liye zaroori hai. Golden topic hai."),
                table(
                    ["", "Qualitative", "Quantitative"],
                    [
                        ["Nature", "Bayaan, number nahi", "Number, ginne ya mapne layak"],
                        ["Misal", "Online class ke baare mein rai, study habit ka note", "Roz internet use karne wale students, marks, ghante"],
                        ["Kaam", "Kyun aur kaise", "Muqabla, average, chart"],
                    ],
                    "Qualitative kyun aur kaise. Quantitative kitna.",
                ),
                p("Sawal ghalat type mangta hai to jawab bekar ho jata hai. Kitne ghante phone, yeh quantitative hai. Phone padhai mein madad kyun karta hai ya nahi, yeh qualitative hai."),
                check(
                    "Students ki rai qualitative hai ya quantitative?",
                    "Qualitative, jab tak aap usay number na bana do.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "strategies",
            "6.4",
            "Data collect karne ke tareeqe",
            6,
            [
                p("Digital literacy sirf maujooda article dhoondhna nahi. Khud asli data ikattha karna bhi hai. Golden topic hai. Paanch tareeqe: interview, survey, prototype, observation, simulation."),
                svg("inquiry", "Sawaal se shuru, phir dhoondho, ikattha karo, analyse karo, aur artefact banao.", "Inquiry flow, collection beech mein hai."),
                tip("8 baje kitni cars intersection cross karti hain? Observation, kyunke ginna hai. Canteen ke khane pe students kya mehsoos karte hain? Survey ya interview."),
                check(
                    "Paanch collection strategies ke naam?",
                    "Interview, survey, prototype, observation, simulation.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "interview-survey",
            "6.4.1 – 6.4.2",
            "Interview aur survey",
            7,
            [
                p("Interview plan shuda baat cheet hai, ek bande se ya chhote group se. Sawalat pehle se likhe hote hain. Jawab aksar qualitative hota hai: wajah, mehsoos, tafseel."),
                p("Survey wohi sawalat kai logon se poochta hai. Kaghaz pe ho sakta hai, ya Google Forms aur Microsoft Forms pe. Online tool jawab khud ikattha kar leta hai aur seedha chart bana deta hai."),
                table(
                    ["", "Interview", "Survey"],
                    [
                        ["Log", "Kam, gehra", "Zyada, ek jaisa sawal"],
                        ["Jawab", "Zyada tar qualitative", "Qualitative aur quantitative dono"],
                        ["Waqt", "Lambi baat", "Chhota form"],
                    ],
                    "Interview gehra. Survey choura.",
                ),
                tip("Survey ka sawal aisa na ho jo jawab munh mein rakh de. Leading question data ko jhoota kar deta hai."),
                check(
                    "Kai logon se same sawal, kaun sa tareeqa?",
                    "Survey ya questionnaire.",
                ),
            ],
        ),
        lecture(
            "prototype-obs",
            "6.4.3 – 6.4.5",
            "Prototype, observation, simulation",
            7,
            [
                p("Prototype product ka sasta pehla version hai. Log try karte hain, feedback dete hain, aur woh feedback data ban jata hai. Poora banane se pehle pata chal jata hai ke idea chalega ya nahi."),
                p("Observation mein aap dekhte ho, sawal nahi poochte. Note qualitative ho sakta hai, ginati quantitative. Jaise kitni cars 8 baje cross karti hain."),
                p("Simulation computer pe asli situation ka model hai. Variables badal kar dekhte hain kya hoga. Tab use karo jab asli tajurba mehnga, khatarnak, ya mushkil ho."),
                table(
                    ["Tareeqa", "Sawal poochte ho?", "Achhi misaal"],
                    [
                        ["Prototype", "Try karwa ke feedback", "App ka kachcha screen"],
                        ["Observation", "Nahi, sirf dekhna", "Traffic count"],
                        ["Simulation", "Model ke andar", "Mahngi lab ki jagah software"],
                    ],
                    "Prototype try, observation dekhna, simulation model.",
                ),
                check(
                    "Asli tajurba khatarnak ho to kaun sa tareeqa?",
                    "Simulation.",
                ),
            ],
        ),
        lecture(
            "primary-secondary",
            "6.5",
            "Primary aur secondary data",
            7,
            [
                p("Data kahan se aaya, yeh bharose ka sawal hai. Golden topic hai. Primary data aap ne isi sawal ke liye khud ikattha kiya: interview, survey, observation, experiment."),
                p("Secondary data pehle kisi aur ne ikattha kiya, aap naye kaam ke liye dobara use kar rahe ho: kitab, article, official report, website statistics, database."),
                table(
                    ["", "Primary", "Secondary"],
                    [
                        ["Source", "Researcher khud", "Pehle se maujood"],
                        ["Misal", "Aap ka survey", "Report, article, website"],
                        ["Purpose", "Isi study ke liye", "Naye maqsad ke liye reuse"],
                        ["Control", "Sawal aap ke", "Data pehle se qaid hai"],
                    ],
                    "Primary taza aur aap ke control mein. Secondary pehle se maujood, control kam.",
                ),
                check(
                    "Aap ne Google Form se class se jawab liye. Primary hai ya secondary?",
                    "Primary. Aap ne khud isi sawal ke liye ikattha kiya.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "approach",
            "6.6",
            "Data collection ka plan",
            6,
            [
                steps(
                    "Plan ke aath qadam",
                    [
                        "Research question saaf likho.",
                        "Quantitative, qualitative, ya dono.",
                        "Tareeqa chuno: survey, interview, observation.",
                        "Sample ya group chuno.",
                        "Form, sawalat, observation sheet taiyar karo.",
                        "Ehtiyat se data lo.",
                        "Spreadsheet mein rakho aur backup rakho.",
                        "Ijazat lo. Privacy zaroori hai. Consent ke baghair nahi.",
                    ],
                    "Sawaal, type, tareeqa, sample, tool, collection, storage, ethics.",
                ),
                tip("Bina consent ke doosre student ka naam ya phone data mein mat daalo."),
                check(
                    "Collection se pehle aakhri ethical qadam kya hai?",
                    "Consent. Logon ki ijazat aur privacy.",
                ),
            ],
        ),
        lecture(
            "presenting",
            "6.7",
            "Digital tools se data pesh karna",
            6,
            [
                p("Data ikattha kar lena aadha kaam hai. Doosra hissa yeh hai ke doosra insaan jaldi samajh jaye. Digital tools yahi karte hain."),
                svg("bars", "Spreadsheet se chart, chart slides mein. Number se shakal.", "From sheet to chart."),
                p("Behtar chart lamba paragraph se tez samjhata hai. Lekin chart asal data pe ho, mubaligha nahi. Galat scale se chhoti farq ko pahaad mat banao."),
                check(
                    "Chart tez samjhata hai, lekin shart kya hai?",
                    "Woh asal data pe ho, exaggerate na ho.",
                ),
            ],
        ),
        lecture(
            "tools",
            "6.7.1 – 6.7.4",
            "Sheet, slides, infographic, report",
            8,
            [
                table(
                    ["Tool", "Kaam", "Misal"],
                    [
                        ["Spreadsheet", "Rows, total, average, sort, chart", "Excel, Google Sheets"],
                        ["Slides", "Audience ko short points", "PowerPoint, Google Slides, Canva"],
                        ["Infographic", "Ek nazar mein asal baat", "Canva, Power BI, Tableau"],
                        ["Report", "Title, data, findings, conclusion", "Word, Google Docs"],
                    ],
                    "Sheet hisaab, slides bolna, infographic ikhtisar, report poori kahani.",
                ),
                steps(
                    "Slides ka usool",
                    [
                        "Title aur research question pehle.",
                        "Lambay paragraph ki jagah chhote points.",
                        "Table ya chart jahan number ho.",
                        "Design saaf, parhne layak.",
                    ],
                    "Sawaal dikhao, points chhote rakho, chart lagao, design saaf.",
                ),
                p("Report mein title, introduction, purpose, tables, simple zaban mein findings, aur recommendations. AI se jumla sanwarna ho sakta hai, lekin aap khud check karo ke number jhoot na ho gaye hon."),
                check(
                    "Average aur sort kis tool ka kaam hai?",
                    "Spreadsheet.",
                ),
            ],
        ),
        lecture(
            "inquiry",
            "6.8",
            "Digital inquiry: phone aur padhai",
            7,
            [
                p("Yeh golden case study hai. Poora chapter ek sawal pe lag jata hai. Research question: rozana mobile phone ka istemal students ki study habits pe kya asar dalta hai?"),
                p("Manzar: free period mein phones nazar aate hain. Koi kehta hai seekhne mein madad, koi kehta hai waqt zaya. Class ko tahqeeq karni hai, rai nahi."),
                svg("inquiry", "Question, search, collect, analyze, create. Yahi paanch qadam poore project ke hain.", "Digital inquiry workflow."),
                steps(
                    "Workflow",
                    [
                        "Question saaf karo.",
                        "Pehle secondary search, background.",
                        "Primary data ikattha karo.",
                        "Spreadsheet aur charts se analyse.",
                        "Aakhir mein digital artefact banao jo sawal ka jawab de.",
                    ],
                    "Sawaal, search, collect, analyse, create.",
                ),
                check(
                    "Case study ka research question kya hai?",
                    "Rozana phone use study habits pe kya asar dalta hai.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "inquiry-search",
            "6.8 steps 1–3",
            "Advanced search aur methodology",
            7,
            [
                p("Pehle background. Search engine pe secondary data, lekin khuli search ka dher nahi. Advanced operators se ghera tang karo."),
                code(
                    "\"screen time\" students concentration\nsite:.edu mobile learning\nsmartphone study habits 2024..2026",
                    "Quotes se exact jumla. site se domain. Do dots se saal ka darmiyan.",
                ),
                steps(
                    "Pehle teen qadam",
                    [
                        "Advanced search se bharosa ke qabil secondary articles.",
                        "Author, date, aur reference check karo. Warna chhor do.",
                        "Methodology likho: kaun se students, kaun sa tool, primary aur secondary dono.",
                    ],
                    "Search narrow karo, source check karo, methodology likho.",
                ),
                check(
                    "Quotes search mein kya karte hain?",
                    "Exact phrase dhoondhte hain, alag alag lafz nahi.",
                ),
            ],
        ),
        lecture(
            "inquiry-survey",
            "6.8 steps 4–6",
            "Survey likhna aur primary data",
            7,
            [
                p("Survey saaf aur unbiased ho. Ek sawal ek hi cheez pooche."),
                table(
                    ["Sawal", "Data ki qisam"],
                    [
                        ["Roz phone kitne ghante?", "Quantitative"],
                        ["Phone sab se zyada kis kaam?", "Qualitative, ya categories"],
                        ["Padhai ke dauran phone madad karta hai ya nuksan? 1 se 5", "Quantitative scale"],
                    ],
                    "Ghante number hain. Wajah ya activity qualitative ho sakti hai. Scale quantitative hai.",
                ),
                steps(
                    "Primary collection",
                    [
                        "Sample class ke students hon, naam optional rakho.",
                        "Consent ki line form ke upar likho.",
                        "Google Form ya paper, phir jawab spreadsheet mein.",
                        "Khali ya mazaq wale jawab cleaning mein hatao.",
                    ],
                    "Sample, consent, form, phir cleaning.",
                ),
                check(
                    "Ghante wala sawal qualitative hai?",
                    "Nahi. Woh quantitative hai.",
                ),
            ],
        ),
        lecture(
            "inquiry-sheet",
            "6.8 steps 7–9",
            "Secondary data aur spreadsheet",
            7,
            [
                p("Secondary data apni survey ke sath rakho. Misal: koi bharosa ke qabil article kehta hai ke zyada screen time concentration kam karta hai. Apne primary numbers se isay compare karo. Agar dono milen to baat mazboot. Agar na milen to wajah likho, chhupao mat."),
                code(
                    "Hours | Activity | Focus score\n4     | social   | 2\n1     | notes    | 5\n5     | video    | 2",
                    "Har column ek field. Average hours, aur activity ki count, dono nikal sakte ho.",
                ),
                steps(
                    "Sheet ka intizam",
                    [
                        "Ek header row, neeche sirf data.",
                        "Ghante number format mein, text nahi.",
                        "Average aur count formulas se, haath se nahi.",
                        "Backup: doosri copy ya drive.",
                    ],
                    "Header, number format, formula, backup.",
                ),
                check(
                    "Article ka screen-time claim primary hai ya secondary?",
                    "Secondary. Kisi aur ne pehle ikattha kiya.",
                ),
            ],
        ),
        lecture(
            "inquiry-end",
            "6.8 steps 10–12",
            "Analysis, natija, aur artefact",
            8,
            [
                p("Charts dekh kar trend likho. Notes ki misaal isi sawal ki ek mumkin kahani hai: zyada tar students 3 se 5 ghante phone use karte hain, aadhe entertainment pe, aur lambay ghante walon ka focus score kam. Apni class ke asal numbers alag ho sakte hain. Natija unhi pe likho."),
                svg("bars", "3 se 5 ghante wali category sab se lambi ho to wahi trend hai. Chart ko apne asal counts se bharna.", "Example distribution of phone hours."),
                p("Natija sawal ka seedha jawab ho: is class mein zyada phone, khas kar entertainment, padhai ke focus se juda nazar aaya. Had yeh hai ke ek class ki survey poore sheher ka qanoon nahi."),
                p("Digital artefact aakhri product hai jo asal sawal ka jawab de. Sirf sajawat nahi. Slides, infographic, ya chhota report: sawal, tareeqa, chart, natija, aur ek recommendation. Misal: padhai ke 25 minute mein phone doosre kamre mein."),
                table(
                    ["Career", "Yahi skill"],
                    [
                        ["Market research analyst", "Survey se primary data, business faisla"],
                        ["UX researcher", "Qualitative aur quantitative dono se product"],
                        ["Data journalist", "Number ko seedhi kahani"],
                    ],
                    "Survey, interview, sheet, aur chart wahi kaam hai jo yeh careers karti hain.",
                ),
                tip("Artefact mein har number ki jagah likho: primary survey ya secondary article. Bina source ke chart bharosa nahi karta."),
                check(
                    "Digital artefact sirf khubsurat poster hai?",
                    "Nahi. Woh sawal ka jawab hai: tareeqa, data, natija, aur recommendation.",
                ),
            ],
        ),
    ],
}
