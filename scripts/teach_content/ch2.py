from .blocks import check, code, lecture, math, p, steps, svg, table, tip

CHAPTER = {
    "id": "ch2",
    "num": "02",
    "title": "Computational Thinking",
    "blurb": "Algorithms, pseudocode, decomposition, sorting, aur searching.",
    "lectures": [
        lecture(
            "ct-intro",
            "2.1 – 2.2",
            "Computational thinking aur algorithm",
            8,
            [
                p("Computational thinking maslon ko systematically hal karne ka tareeqa hai. Aap problem ko todte hain, pattern dekhte hain, faltu detail chhupate hain, aur algorithm banate hain."),
                p("Algorithm ek step by step logical procedure hai jo problem solve kare. Yeh concept hai. Kisi ek programming language ka ghulam nahi. Pehle algorithm, phir code."),
                steps(
                    "Algorithm kyun zaroori hai",
                    [
                        "Bada kaam chhote steps mein aa jata hai.",
                        "Time aur memory dono sochne ka mauqa milta hai.",
                        "Milta julta masla dobara same steps se hal ho sakta hai.",
                        "Galti kam hoti hai kyunke steps clear hote hain.",
                        "Code se pehle blueprint mil jata hai.",
                    ],
                    "Algorithm structure, efficiency, reuse, accuracy, aur blueprint deta hai.",
                ),
                tip("Pseudocode algorithm ko aisi angrezi mein likhta hai jo insaan parh le aur programmer code bana le. Yeh insaan aur machine ke beech ka pul hai."),
                check(
                    "Algorithm kisi khasi language se bandha hota hai?",
                    "Nahi. Algorithm language-independent logical steps hain.",
                ),
            ],
        ),
        lecture(
            "algo-pseudo",
            "2.2.2",
            "Algorithm aur pseudocode ka farq",
            8,
            [
                p("Dono design phase mein aate hain, lekin kaam alag hai. Algorithm batata hai kya karna hai. Pseudocode batata hai woh kaam parhne layak structure mein kaise likha jaye."),
                table(
                    ["Point", "Algorithm", "Pseudocode"],
                    [
                        ["Shakal", "Plain numbered steps", "IF, FOR, WHILE jaise words"],
                        ["Language", "Kisi language se azad", "Code jaisa, lekin chalta nahi"],
                        ["Focus", "Logic kya hai", "Steps kitne clear hain"],
                        ["Parhne wala", "Koi bhi", "Zyada tar student ya programmer"],
                    ],
                    "Algorithm recipe hai. Pseudocode kitchen ka structured manual hai.",
                ),
                p("Analogy: algorithm kehta hai cake 350 degree pe bake karo. Pseudocode kehta hai SET temperature TO 350. WHILE cake baked nahi, WAIT."),
                code(
                    "SET temperature TO 350\nWHILE cake is not baked\n    WAIT\nEND WHILE",
                    "Pseudocode structured keywords use karta hai, lekin yeh executable program nahi.",
                ),
                check(
                    "Recipe algorithm hai ya pseudocode?",
                    "Recipe algorithm hai. SET aur WHILE wala manual pseudocode hai.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "decomposition",
            "2.3.1",
            "Decomposition",
            7,
            [
                p("Decomposition ka matlab hai bara masla chhote hisso mein todna. Har hissa alag samajh aata hai, alag banta hai, aur galti bhi alag nazar aati hai. Golden topic hai."),
                p("Nayi zaban seekhna decomposition ki misaal hai. Pehle vocabulary: log, kaam, cheezein. Phir grammar: subject, verb, object. Phir tenses: I eat aur I ate. Phir in sab ko jod kar jumla."),
                table(
                    ["Subtask", "Kaam"],
                    [
                        ["Vocabulary", "Log, actions, cheezon ke lafz"],
                        ["Grammar", "Subject, phir verb, phir object"],
                        ["Tenses", "Present, past, future"],
                        ["Sentences", "Rules se sahi jumle"],
                    ],
                    "Bari zaban ko chaar chhote subtasks mein tod diya.",
                ),
                steps(
                    "Faida",
                    [
                        "Ek waqt pe ek tukda, complexity kam.",
                        "Bug mil jaye to pata chale verb galat hai ya lafz.",
                        "Ek dafa seekha hua tukda doosri jagah dobara use ho.",
                    ],
                    "Decomposition complexity kam karta hai, debugging asaan karta hai, aur reuse deta hai.",
                ),
                check(
                    "Decomposition ka seedha matlab kya hai?",
                    "Complex kaam ko chhote manageable hisson mein todna.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "patterns",
            "2.3.2",
            "Pattern recognition",
            7,
            [
                p("Pattern recognition ka matlab hai data mein dohrav, qayeda, ya rule dekhna. Is se algorithm chhota ho jata hai. Loops ki bunyad yahi hai."),
                p("Teen sawal poochhein. Kya dohra raha hai? Kya ek predicted tareeqe se badal raha hai? Kya main isay ek general rule bana sakta hoon?"),
                code(
                    "*\n**\n***\n****\n*****",
                    "Har row pichli row se ek star zyada hai. Row N pe N stars.",
                ),
                p("Agar pattern na dekhein to aap paanch alag print statements likhenge. Pattern dekh kar ek loop likh dete hain: row number jitne stars."),
                tip("Jab bhi aapko copy-paste karne ka dil kare, ruk jayein. Wahan pattern chhupa hai, aur pattern loop ban jata hai."),
                check(
                    "Star triangle mein row 4 pe kitne stars honge?",
                    "Char stars. Row N pe N stars.",
                ),
            ],
        ),
        lecture(
            "abstraction",
            "2.3.3",
            "Abstraction",
            7,
            [
                p("Abstraction ka matlab hai jo zaroori nahi usay chhupa dena, aur sirf woh rakhna jo masla hal kare. Noise hatao, core logic rakho."),
                table(
                    ["Chai banane ke zaroori steps", "Jo situation se badle", "Jo ignore karein"],
                    [
                        ["Pani ubalen", "Black, green, ya doodh", "Kettle ka brand"],
                        ["Chai dalein", "Cheeni ya lemon", "Cup ka rang"],
                        ["Kuch der rukein", "Stove ya kettle", "Kitchen hai ya office"],
                        ["Cup mein dalein aur serve karein", "Maza apni pasand", "Yeh noise hai"],
                    ],
                    "Core logic paanch steps hai. Brand aur cup ka rang algorithm mein nahi aate.",
                ),
                p("Abstracted algorithm yahi rehta hai: ubalen, chai dalein, rukein, cup mein dalein, serve karein. Yeh kettle ke brand se azad hai."),
                check(
                    "Chai ke algorithm mein cup ka rang kyun nahi aata?",
                    "Kyunke woh noise hai. Chai banne pe asar nahi karta.",
                ),
            ],
        ),
        lecture(
            "bubble",
            "2.4.1",
            "Bubble sort",
            10,
            [
                p("Sorting ka matlab cheezon ko order mein lagana hai, chhote se bara ya bara se chhota. Searching ka matlab list mein cheez dhoondhna hai. Bubble sort bagal walon ko compare karta hai aur galat order ho to swap kar deta hai. Golden topic hai."),
                svg("bubble", "List 8, 4, 1, 9, 3. Pehle pass mein 9 end pe pohonch jata hai.", "Bubble sort, first pass."),
                steps(
                    "Pehla pass, list 8 4 1 9 3",
                    [
                        "8 aur 4: 8 bara hai, swap. Ab 4, 8, 1, 9, 3.",
                        "8 aur 1: swap. Ab 4, 1, 8, 9, 3.",
                        "8 aur 9: 8 chhota hai, koi swap nahi.",
                        "9 aur 3: swap. Ab 4, 1, 8, 3, 9. 9 apni jagah pe hai.",
                    ],
                    "Har pass mein sab se bara number end ki taraf bubble karta hai.",
                ),
                code(
                    "DATA = [8, 4, 1, 9, 3]\nN = 5\nfor outer in range(N - 1):\n    for inner in range(N - 1 - outer):\n        if DATA[inner] > DATA[inner + 1]:\n            DATA[inner], DATA[inner + 1] = DATA[inner + 1], DATA[inner]",
                    "Nested loops. Inner loop hamesha shuru se chalti hai, lekin har pass mein end chhota hota jata hai.",
                    lang="python",
                ),
                p("Sorted list 1, 3, 4, 8, 9 banti hai. Faida: samajhna asaan hai, extra memory nahi, aur equal items apni order mein rehte hain, is liye stable hai. Nuqsan: swaps bohot hain, bari list pe bohot slow hai."),
                check(
                    "Bubble sort stable kyun kehlata hai?",
                    "Equal items apni relative order nahi badalte.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "selection",
            "2.4.1",
            "Selection sort",
            9,
            [
                p("Selection sort baar baar unsorted hisse se sab se chhota element chunta hai aur usay aage ki sahi jagah pe rakh deta hai. Golden topic hai."),
                svg("selection", "Pehle position ke liye poori list mein sab se chhota dhoondh kar aage rakh dein. Yahan 1 aa jata hai.", "Selection sort idea."),
                p("List 8, 4, 1, 9, 3. Pehle position pe 8 hai. 4 chhota hai, swap. Phir 1 us se bhi chhota hai, swap. 9 aur 3 dono 1 se bare hain, is liye 1 wahin ruk jata hai."),
                code(
                    "DATA = [8, 4, 1, 9, 3]\nN = 5\nfor outer in range(N - 1):\n    for inner in range(outer + 1, N):\n        if DATA[outer] > DATA[inner]:\n            DATA[outer], DATA[inner] = DATA[inner], DATA[outer]",
                    "Farq yeh hai ke inner loop outer plus one se shuru hoti hai. Bubble sort ki inner loop zero se shuru hoti hai.",
                    lang="python",
                ),
                tip("Teacher ka tip: inner loop ka start compare karein. Selection outer plus one se. Bubble hamesha zero se."),
                p("Faida: code chhota hai, swaps bubble se kam hain, extra memory nahi. Nuqsan: phir bhi nested loops, sorted list pe bhi poora kaam karta hai, aur stable nahi, equal items ki order badal sakti hai."),
                check(
                    "Selection sort ki inner loop kahan se shuru hoti hai?",
                    "Outer index ke agle element se, yaani outer plus one.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "linear",
            "2.4.2",
            "Linear search",
            8,
            [
                p("Linear search, ya sequential search, list ke har element ko ek ek karke dekhti hai jab tak target na mil jaye. Sorted ho ya unsorted, dono pe chalti hai."),
                steps(
                    "List 8, 3, 6, 1, 7, 2, 4, 5 mein 7 dhoondhein",
                    [
                        "8 check kiya, 7 nahi.",
                        "3 check kiya, 7 nahi.",
                        "6 check kiya, 7 nahi.",
                        "1 check kiya, 7 nahi.",
                        "7 check kiya, mil gaya. Loop yahin ruk jati hai.",
                    ],
                    "Paanchwe element pe 7 mil jata hai.",
                ),
                code(
                    "DATA = [8, 3, 6, 1, 7, 2, 4, 5]\nfind = 7\nfound = False\nfor value in DATA:\n    if value == find:\n        found = True\n        break\nif not found:\n    print(\"Data Not Found\")",
                    "Ek loop aur ek if. Milte hi break.",
                    lang="python",
                ),
                p("Faida: sort ki zaroorat nahi, code seedha, chhoti list pe tez, extra space nahi. Nuqsan: agar target das lakh ke end pe ho to das lakh checks. List double ho to time bhi lagbhag double."),
                check(
                    "Linear search sorted list maangti hai?",
                    "Nahi. Sorted aur unsorted dono pe chalti hai.",
                ),
            ],
        ),
        lecture(
            "binary",
            "2.4.2",
            "Binary search",
            10,
            [
                p("Binary search list ko baar baar aadha karti hai. Bahut tez hai, lekin sirf sorted list pe chalti hai. Unsorted pe yeh galat jawab de sakti hai. Golden topic hai."),
                math(
                    r"\mathrm{MID} = \left\lfloor \frac{\mathrm{BEG}+\mathrm{END}}{2} \right\rfloor",
                    "Mid barabar beg plus end, taqseem do, decimal gira dein.",
                ),
                svg("binary", "Sorted list 1 se 8. Item 3 dhoondhna hai. Pehle mid ki value 4 hai. 3 chhota hai, is liye left jao.", "Binary search first cut."),
                steps(
                    "Item 3, list 1 2 3 4 5 6 7 8",
                    [
                        "Mid value 4. 3 chhota hai, right half hata dein.",
                        "Bachi list 1 2 3. Mid value 2. 3 bara hai, right jao.",
                        "Bachi value 3. Barabar hai. Mil gaya.",
                    ],
                    "Teen steps mein 3 mil jata hai.",
                ),
                p("Das lakh sorted items mein binary search lagbhag bees steps mein dhoondh leti hai. Nuqsan: pehle sort chahiye, random access chahiye jaise array, aur off by one ki galti asaan hai."),
                tip("Agar list scrambled ho to binary search use na karein. Pehle sort karein, ya linear search use karein."),
                check(
                    "Binary search unsorted list pe kyun fail hoti hai?",
                    "Kyunke yeh assume karti hai ke left chhota hai aur right bara. Bina sort yeh assumption jhoot hai.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "evaluate",
            "2.5",
            "Algorithm ko parakhna",
            8,
            [
                p("Algorithm teen hisaab se parakha jata hai: correctness, efficiency, aur clarity."),
                p("Correct algorithm wohi output deta hai jo ummeed hai, edge cases sambhalta hai, aur kabhi infinite loop mein nahi phans ta. Yeh khatam hona zaroori hai."),
                table(
                    ["Input", "2 se divide, remainder", "Remainder zero?", "Result"],
                    [
                        ["3", "3 / 2, remainder 1", "Nahi", "Odd"],
                        ["6", "6 / 2, remainder 0", "Haan", "Even"],
                        ["15", "15 / 2, remainder 1", "Nahi", "Odd"],
                    ],
                    "Trace table even odd checker dikhati hai. Remainder zero ho to even.",
                ),
                math(r"n \bmod 2 = 0", "Agar n mod 2 zero ho to number even hai."),
                p("Efficiency do cheezon se map hoti hai. Time: input barhne pe kitni der. Space: kitni memory. Clarity: koi doosra student steps parh kar samajh jaye."),
                check(
                    "Teen evaluation criteria ke naam batao.",
                    "Correctness, efficiency yaani time aur space, aur clarity.",
                ),
            ],
        ),
        lecture(
            "choose-algo",
            "2.6",
            "Kaun sa algorithm chunein",
            6,
            [
                p("Algorithm choose karne se pehle teen sawal: input kitna bara hai? Data sorted hai? Hamein speed chahiye ya memory ki bachat?"),
                table(
                    ["Halat", "Choice"],
                    [
                        ["Unsorted list mein dhoondhna", "Linear search"],
                        ["Sorted list mein dhoondhna", "Binary search"],
                        ["Data ko order mein lana", "Bubble ya selection, bari data pe yeh slow hain"],
                        ["Samajhna aur trace karna", "Bubble, kyunke picture clear hai"],
                        ["Swaps kam rakhne hain", "Selection, bubble se kam swaps"],
                    ],
                    "Unsorted pe linear. Sorted pe binary. Order chahiye to sorting.",
                ),
                p("Chapter ka khulasa: computational thinking decomposition, pattern, abstraction, aur algorithm hai. Pseudocode structured angrezi hai. Bubble aur selection chhoti lists ke liye seekhne layak hain, bari data ke liye slow. Linear har list pe, binary sirf sorted pe."),
                check(
                    "Sorted hazaar numbers mein ek value, kaun si search?",
                    "Binary search.",
                ),
            ],
        ),
    ],
}
