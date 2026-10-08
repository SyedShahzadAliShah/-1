window.COURSE = {
  "edition": "Teach Yourself Edition",
  "language": "Urdish",
  "title": "Computer Science XI",
  "curriculum": "Sindh Curriculum 2026",
  "chapters": [
    {
      "id": "ch1",
      "num": "01",
      "title": "Computer Systems",
      "blurb": "Discrete data, Boolean algebra, logic gates, K-maps, SDLC, aur OSI model.",
      "lectures": [
        {
          "id": "discrete-digital",
          "code": "1.1.1 – 1.1.2",
          "title": "Discrete, continuous, aur digital systems",
          "minutes": 8,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Aaj ki pehli lecture do qisam ki quantities se shuru hoti hai: discrete aur continuous. Discrete woh cheez hai jo alag alag ginne layak ho. Aap classroom ke students ek ek karke gin sakte hain. Parking ki cars bhi discrete hain. Inki value jump karti hai, beech ki adhi value nahi hoti.",
              "html": "Aaj ki pehli lecture do qisam ki quantities se shuru hoti hai: discrete aur continuous. Discrete woh cheez hai jo alag alag ginne layak ho. Aap classroom ke students ek ek karke gin sakte hain. Parking ki cars bhi discrete hain. Inki value jump karti hai, beech ki adhi value nahi hoti."
            },
            {
              "type": "p",
              "say": "Continuous quantity ek range ke andar koi bhi value le sakti hai. Pani ka temperature 30 bhi ho sakta hai, 30.2 bhi, aur us ke beech ki koi bhi reading. Chalti hui car ki speed bhi continuous hai, kyunke woh smoothly badalti hai.",
              "html": "Continuous quantity ek range ke andar koi bhi value le sakti hai. Pani ka temperature 30 bhi ho sakta hai, 30.2 bhi, aur us ke beech ki koi bhi reading. Chalti hui car ki speed bhi continuous hai, kyunke woh smoothly badalti hai."
            },
            {
              "type": "svg",
              "name": "stairs",
              "say": "Stairs discrete hain, har step ek fixed value. Ramp continuous hai, aap us pe kahin bhi ruk sakte hain.",
              "caption": "Stairs discrete, ramp continuous."
            },
            {
              "type": "p",
              "say": "Digital system ek electronic system hai jo sirf do values use karta hai: zero aur one. In dono ko binary digits, ya bits, kehte hain. Zero ka matlab OFF, LOW, ya FALSE hai. One ka matlab ON, HIGH, ya TRUE hai.",
              "html": "Digital system ek electronic system hai jo sirf do values use karta hai: zero aur one. In dono ko binary digits, ya bits, kehte hain. Zero ka matlab OFF, LOW, ya FALSE hai. One ka matlab ON, HIGH, ya TRUE hai."
            },
            {
              "type": "table",
              "headers": [
                "Faida",
                "Urdish matlab"
              ],
              "rows": [
                [
                  "Reliable",
                  "Noise aur interference se kam bigadta hai."
                ],
                [
                  "Accurate",
                  "Copy karne pe quality kharab nahi hoti."
                ],
                [
                  "Easy design",
                  "Sirf do states handle karni hoti hain."
                ],
                [
                  "Programmable",
                  "Software se control karna asaan hai."
                ]
              ],
              "say": "Digital systems reliable, accurate, easy to design, aur programmable hoti hain."
            },
            {
              "type": "p",
              "say": "Misal: computer data ko zero aur one mein process karta hai. Smartphone photos aur music ko binary mein store karta hai. Digital camera image ko binary code mein capture karti hai.",
              "html": "Misal: computer data ko zero aur one mein process karta hai. Smartphone photos aur music ko binary mein store karta hai. Digital camera image ko binary code mein capture karti hai."
            },
            {
              "type": "tip",
              "say": "Exam mein stairs versus ramp wali analogy likh dena. Examiner ko foran pata chal jata hai ke discrete aur continuous clear hain."
            },
            {
              "type": "check",
              "q": "Temperature of water discrete hai ya continuous?",
              "a": "Continuous, kyunke woh range ke andar koi bhi value le sakti hai.",
              "say": "Temperature of water discrete hai ya continuous? Jawab. Continuous, kyunke woh range ke andar koi bhi value le sakti hai."
            }
          ]
        },
        {
          "id": "analog-digital",
          "code": "1.1.3",
          "title": "Analog aur digital signals",
          "minutes": 8,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Yeh golden topic hai. Analog signal continuous hoti hai. Waqt ke sath smoothly badalti hai, bilkul sine wave ki tarah. Insan ki awaaz aur purana thermometer analog misaal hain.",
              "html": "Yeh golden topic hai. Analog signal continuous hoti hai. Waqt ke sath smoothly badalti hai, bilkul sine wave ki tarah. Insan ki awaaz aur purana thermometer analog misaal hain."
            },
            {
              "type": "p",
              "say": "Digital signal ke sirf do level hote hain: HIGH, yaani one, aur LOW, yaani zero. Yeh ek value se doosri value pe foran jump karti hai, is liye square wave banti hai. Computer ka data digital signal hai.",
              "html": "Digital signal ke sirf do level hote hain: HIGH, yaani one, aur LOW, yaani zero. Yeh ek value se doosri value pe foran jump karti hai, is liye square wave banti hai. Computer ka data digital signal hai."
            },
            {
              "type": "svg",
              "name": "waves",
              "say": "Analog sine wave smooth hai. Digital square wave sirf high aur low pe rehti hai.",
              "caption": "Sine wave aur square wave."
            },
            {
              "type": "table",
              "headers": [
                "Feature",
                "Analog data",
                "Digital data"
              ],
              "rows": [
                [
                  "Nature",
                  "Continuous flow",
                  "Discrete bits"
                ],
                [
                  "Reliability",
                  "Noise se bigad jati hai",
                  "Noise ke khilaf mazboot"
                ],
                [
                  "Copy",
                  "Quality gir sakti hai",
                  "Copy same rehti hai"
                ]
              ],
              "say": "Analog continuous aur noise se kamzor hai. Digital discrete hai aur noise resist karti hai."
            },
            {
              "type": "check",
              "q": "Square wave analog hai ya digital?",
              "a": "Digital. Sirf HIGH one aur LOW zero.",
              "say": "Square wave analog hai ya digital? Jawab. Digital. Sirf HIGH one aur LOW zero."
            }
          ]
        },
        {
          "id": "boolean",
          "code": "1.1.4 – 1.1.6",
          "title": "Boolean algebra, operations, aur truth tables",
          "minutes": 12,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Boolean algebra George Boole ne banai. Is mein sirf do values hain: TRUE jo one hai, aur FALSE jo zero hai. Digital electronics aur programming ki bunyad yahi hai.",
              "html": "Boolean algebra George Boole ne banai. Is mein sirf do values hain: TRUE jo one hai, aur FALSE jo zero hai. Digital electronics aur programming ki bunyad yahi hai."
            },
            {
              "type": "table",
              "headers": [
                "Concept",
                "Matlab",
                "Example"
              ],
              "rows": [
                [
                  "Variable",
                  "Letter jo zero ya one rakhe",
                  "A, B, C, X, Y"
                ],
                [
                  "Operation",
                  "Variable pe action",
                  "AND, OR, NOT"
                ],
                [
                  "Expression",
                  "Variables aur operations ka mel",
                  "Y = A + B"
                ]
              ],
              "say": "Variable letter hai, operation action hai, expression unka combination hai."
            },
            {
              "type": "p",
              "say": "AND operation ka output one sirf tab hota hai jab tamam inputs one hon. Darwaze pe do taale hon, darwaza tab khulega jab dono taale khul jayen.",
              "html": "AND operation ka output one sirf tab hota hai jab tamam inputs one hon. Darwaze pe do taale hon, darwaza tab khulega jab dono taale khul jayen."
            },
            {
              "type": "math",
              "tex": "Y = A \\cdot B",
              "say": "Y barabar A dot B. Dot ka matlab AND hai.",
              "display": true
            },
            {
              "type": "p",
              "say": "OR operation ka output one ho jata hai jab koi bhi ek input one ho. Kamre ke do darwaze hon, aap kisi ek se andar aa sakte hain.",
              "html": "OR operation ka output one ho jata hai jab koi bhi ek input one ho. Kamre ke do darwaze hon, aap kisi ek se andar aa sakte hain."
            },
            {
              "type": "math",
              "tex": "Y = A + B",
              "say": "Y barabar A plus B. Boolean plus ka matlab OR hai, normal jama nahi.",
              "display": true
            },
            {
              "type": "p",
              "say": "NOT operation input ko ulta kar deta hai. Yeh unary hai, sirf ek operand pe chalti hai. Input one ho to output zero. Switch ON ho to kamra roshan, switch OFF ho to kamra andhera. Yahan switch ki misaal inversion samjhane ke liye hai.",
              "html": "NOT operation input ko ulta kar deta hai. Yeh unary hai, sirf ek operand pe chalti hai. Input one ho to output zero. Switch ON ho to kamra roshan, switch OFF ho to kamra andhera. Yahan switch ki misaal inversion samjhane ke liye hai."
            },
            {
              "type": "math",
              "tex": "Y = A'",
              "say": "Y barabar A prime, yaani NOT A.",
              "display": true
            },
            {
              "type": "steps",
              "title": "Truth table kaise banain",
              "items": [
                "Inputs ginain. Unki tadad n hai.",
                "Rows nikalain: 2 ki power n.",
                "Tamam combinations binary order mein likhein.",
                "Har row ka output calculate karein."
              ],
              "say": "Pehle inputs ginain, phir do ki power n rows, phir binary combinations, phir output."
            },
            {
              "type": "math",
              "tex": "\\text{rows} = 2^{n}",
              "say": "Rows barabar two to the power n. Do inputs hon to char rows. Teen inputs hon to aath rows.",
              "display": true
            },
            {
              "type": "tip",
              "say": "Plus yahan jama nahi hai. Boolean mein plus OR hai, aur dot AND hai."
            },
            {
              "type": "check",
              "q": "Do inputs ki truth table mein kitni rows hoti hain?",
              "a": "Char rows, kyunke 2 ki power 2 barabar 4.",
              "say": "Do inputs ki truth table mein kitni rows hoti hain? Jawab. Char rows, kyunke 2 ki power 2 barabar 4."
            }
          ]
        },
        {
          "id": "basic-gates",
          "code": "1.1.7",
          "title": "Basic logic gates: AND, OR, NOT",
          "minutes": 9,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Logic gates electronic circuits hain jo Boolean operations karti hain. Yeh tamam digital systems ki eentein hain. Golden topic hai, symbol aur truth table dono yaad rakhne hain.",
              "html": "Logic gates electronic circuits hain jo Boolean operations karti hain. Yeh tamam digital systems ki eentein hain. Golden topic hai, symbol aur truth table dono yaad rakhne hain."
            },
            {
              "type": "svg",
              "name": "gate",
              "say": "AND gate ka output tab one hota hai jab A bhi one ho aur B bhi one ho.",
              "caption": "AND gate.",
              "gate": "and"
            },
            {
              "type": "table",
              "headers": [
                "A",
                "B",
                "AND",
                "OR"
              ],
              "rows": [
                [
                  "0",
                  "0",
                  "0",
                  "0"
                ],
                [
                  "0",
                  "1",
                  "0",
                  "1"
                ],
                [
                  "1",
                  "0",
                  "0",
                  "1"
                ],
                [
                  "1",
                  "1",
                  "1",
                  "1"
                ]
              ],
              "say": "AND sirf last row mein one deta hai. OR pehli row ke ilawa har jagah one deta hai."
            },
            {
              "type": "svg",
              "name": "gate",
              "say": "NOT gate ka ek hi input hota hai, aur output hamesha ulta hota hai.",
              "caption": "NOT gate.",
              "gate": "not"
            },
            {
              "type": "table",
              "headers": [
                "A",
                "NOT Y"
              ],
              "rows": [
                [
                  "0",
                  "1"
                ],
                [
                  "1",
                  "0"
                ]
              ],
              "say": "NOT zero ko one banata hai aur one ko zero."
            },
            {
              "type": "check",
              "q": "A one hai aur B zero hai. AND ka output kya hoga?",
              "a": "Zero. AND ko dono inputs one chahiye.",
              "say": "A one hai aur B zero hai. AND ka output kya hoga? Jawab. Zero. AND ko dono inputs one chahiye."
            }
          ]
        },
        {
          "id": "universal-gates",
          "code": "1.1.7",
          "title": "Universal aur advanced gates",
          "minutes": 10,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "NAND aur NOR ko universal gates kehte hain, kyunke dunya ka koi bhi logic circuit sirf in gates se bana sakte hain. NAND ka matlab NOT AND hai. NOR ka matlab NOT OR hai.",
              "html": "NAND aur NOR ko universal gates kehte hain, kyunke dunya ka koi bhi logic circuit sirf in gates se bana sakte hain. NAND ka matlab NOT AND hai. NOR ka matlab NOT OR hai."
            },
            {
              "type": "svg",
              "name": "gate",
              "say": "NAND, AND ke output pe bubble laga kar inversion kar deta hai.",
              "caption": "NAND gate.",
              "gate": "nand"
            },
            {
              "type": "math",
              "tex": "Y = (A \\cdot B)'",
              "say": "NAND: Y barabar A dot B, poori cheez prime.",
              "display": true
            },
            {
              "type": "svg",
              "name": "gate",
              "say": "NOR, OR ke output ko ulta kar deta hai.",
              "caption": "NOR gate.",
              "gate": "nor"
            },
            {
              "type": "math",
              "tex": "Y = (A + B)'",
              "say": "NOR: Y barabar A plus B, poori cheez prime.",
              "display": true
            },
            {
              "type": "table",
              "headers": [
                "A",
                "B",
                "NAND",
                "NOR",
                "XOR",
                "XNOR"
              ],
              "rows": [
                [
                  "0",
                  "0",
                  "1",
                  "1",
                  "0",
                  "1"
                ],
                [
                  "0",
                  "1",
                  "1",
                  "0",
                  "1",
                  "0"
                ],
                [
                  "1",
                  "0",
                  "1",
                  "0",
                  "1",
                  "0"
                ],
                [
                  "1",
                  "1",
                  "0",
                  "0",
                  "0",
                  "1"
                ]
              ],
              "say": "XOR tab one hai jab inputs alag hon. XNOR tab one hai jab inputs same hon."
            },
            {
              "type": "svg",
              "name": "gate",
              "say": "XOR exclusive OR hai. Inputs alag hon to output one.",
              "caption": "XOR gate.",
              "gate": "xor"
            },
            {
              "type": "math",
              "tex": "Y = A \\oplus B",
              "say": "Y barabar A xor B.",
              "display": true
            },
            {
              "type": "tip",
              "say": "Yaad rakhein: XOR one deta hai jab inputs exclusively different hon. XNOR one deta hai jab inputs same hon."
            },
            {
              "type": "check",
              "q": "NAND aur NOR ko universal kyun kehte hain?",
              "a": "Kyunke koi bhi logic circuit sirf NAND se, ya sirf NOR se, bana sakte hain.",
              "say": "NAND aur NOR ko universal kyun kehte hain? Jawab. Kyunke koi bhi logic circuit sirf NAND se, ya sirf NOR se, bana sakte hain."
            }
          ]
        },
        {
          "id": "minterms",
          "code": "1.1.8 – 1.1.11",
          "title": "Expressions, minterms, aur logic diagrams",
          "minutes": 11,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Boolean expression solve karte waqt order zaroori hai. Pehle parentheses, phir NOT, phir AND, phir OR. Jaise normal math mein multiply pehle hota hai, yahan AND, OR se pehle hota hai.",
              "html": "Boolean expression solve karte waqt order zaroori hai. Pehle parentheses, phir NOT, phir AND, phir OR. Jaise normal math mein multiply pehle hota hai, yahan AND, OR se pehle hota hai."
            },
            {
              "type": "steps",
              "title": "Order of precedence",
              "items": [
                "Parentheses",
                "NOT, yaani prime",
                "AND, yaani dot",
                "OR, yaani plus"
              ],
              "say": "Pehle brackets, phir NOT, phir AND, phir OR."
            },
            {
              "type": "p",
              "say": "Minterm SOP hai, sum of products. Yeh un tamam variables ka AND product hai jahan output one aata hai. Jis variable ki value zero ho us pe prime lagta hai. Jis ki value one ho woh seedha rehta hai.",
              "html": "Minterm SOP hai, sum of products. Yeh un tamam variables ka AND product hai jahan output one aata hai. Jis variable ki value zero ho us pe prime lagta hai. Jis ki value one ho woh seedha rehta hai."
            },
            {
              "type": "p",
              "say": "Maxterm POS hai, product of sums. Yeh un rows ka OR sum hai jahan output zero aata hai. Yahan rule ulta hai: value one ho to prime, value zero ho to seedha.",
              "html": "Maxterm POS hai, product of sums. Yeh un rows ka OR sum hai jahan output zero aata hai. Yahan rule ulta hai: value one ho to prime, value zero ho to seedha."
            },
            {
              "type": "table",
              "headers": [
                "A",
                "B",
                "Y",
                "Minterm",
                "Maxterm"
              ],
              "rows": [
                [
                  "0",
                  "0",
                  "0",
                  "—",
                  "A + B"
                ],
                [
                  "0",
                  "1",
                  "1",
                  "A'B",
                  "—"
                ],
                [
                  "1",
                  "0",
                  "0",
                  "—",
                  "A' + B"
                ],
                [
                  "1",
                  "1",
                  "1",
                  "AB",
                  "—"
                ]
              ],
              "say": "Jahan Y one hai wahan minterm likhein. Jahan Y zero hai wahan maxterm."
            },
            {
              "type": "math",
              "tex": "Y = A'B + AB",
              "say": "Final SOP: Y barabar A prime B, plus A B.",
              "display": true
            },
            {
              "type": "p",
              "say": "Logic diagram dikhata hai ke gates kaise judi hain. Sab se pehle woh operation draw karein jiski precedence zyada ho.",
              "html": "Logic diagram dikhata hai ke gates kaise judi hain. Sab se pehle woh operation draw karein jiski precedence zyada ho."
            },
            {
              "type": "svg",
              "name": "circuit",
              "say": "Y barabar A dot B plus C. Pehle AND gate A aur B ko jodti hai, phir OR gate us result ko C ke sath jodti hai.",
              "caption": "Logic diagram of Y = A·B + C."
            },
            {
              "type": "check",
              "q": "Expression Y = A dot B + C mein pehle kaun si gate draw hogi?",
              "a": "AND gate, kyunke AND ki precedence OR se zyada hai.",
              "say": "Expression Y = A dot B + C mein pehle kaun si gate draw hogi? Jawab. AND gate, kyunke AND ki precedence OR se zyada hai."
            }
          ]
        },
        {
          "id": "kmaps",
          "code": "1.1.13",
          "title": "Karnaugh maps se simplification",
          "minutes": 10,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "K-map Boolean expression ko simplify karne ka graphical tareeqa hai. Grid Gray code mein hoti hai, is liye bagal wale cells sirf ek bit se farq rakhte hain. Hum ones ko groups mein jodte hain. Group ka size one, two, four, ya eight hota hai, yaani two ki power.",
              "html": "K-map Boolean expression ko simplify karne ka graphical tareeqa hai. Grid Gray code mein hoti hai, is liye bagal wale cells sirf ek bit se farq rakhte hain. Hum ones ko groups mein jodte hain. Group ka size one, two, four, ya eight hota hai, yaani two ki power."
            },
            {
              "type": "svg",
              "name": "kmap2",
              "say": "Do variables A aur B ke liye char cells chahiye, kyunke two squared barabar four.",
              "caption": "Two-variable K-map."
            },
            {
              "type": "math",
              "tex": "\\text{cells} = 2^{n}",
              "say": "Cells barabar two to the power n. Do variables, char cells. Teen variables, aath cells.",
              "display": true
            },
            {
              "type": "p",
              "say": "Grouping rule: groups jitne bare ho saken utne bare banayein, lekin size sirf two ki power ho. Overlap allowed hai. Group ke andar jo variable zero se one pe badal jaye, woh hat jata hai.",
              "html": "Grouping rule: groups jitne bare ho saken utne bare banayein, lekin size sirf two ki power ho. Overlap allowed hai. Group ke andar jo variable zero se one pe badal jaye, woh hat jata hai."
            },
            {
              "type": "svg",
              "name": "kmap3",
              "say": "Teen variables mein columns Gray code hain: zero zero, zero one, one one, one zero. Kinare wrap ho sakte hain. Left cell right cell ke sath group ho sakti hai.",
              "caption": "Three-variable K-map."
            },
            {
              "type": "tip",
              "say": "Gray code yaad rakhein: 00, 01, 11, 10. 01 ke baad 10 nahi, 11 aata hai, taake sirf ek bit badle."
            },
            {
              "type": "check",
              "q": "K-map mein group ka size kya ho sakta hai?",
              "a": "1, 2, 4, ya 8. Yaani two ki powers. Overlap allowed hai.",
              "say": "K-map mein group ka size kya ho sakta hai? Jawab. 1, 2, 4, ya 8. Yaani two ki powers. Overlap allowed hai."
            }
          ]
        },
        {
          "id": "logisim",
          "code": "LogiSim",
          "title": "LogiSim Evolution mein circuit banana",
          "minutes": 8,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "LogiSim Evolution ek graphical tool hai. Is mein aap wohi truth tables aur Boolean expressions simulate karte hain jo theory mein seekhte hain.",
              "html": "LogiSim Evolution ek graphical tool hai. Is mein aap wohi truth tables aur Boolean expressions simulate karte hain jo theory mein seekhte hain."
            },
            {
              "type": "svg",
              "name": "logisim",
              "say": "Left side library hai, right side canvas. Simulation mein bright green logic one hai, dark green logic zero, blue unknown, aur red error ya short circuit.",
              "caption": "LogiSim areas and wire colors."
            },
            {
              "type": "steps",
              "title": "Y = A dot B kaise banayein",
              "items": [
                "Toolbar se AND gate canvas pe rakhein.",
                "Do input pins left side pe rakhein aur unhein A aur B likhein.",
                "Output pin right side pe rakhein aur usay Y likhein.",
                "Wiring tool se sirf seedhi horizontal ya vertical wires khainchein.",
                "Poke tool, yaani ungli wala icon, se A aur B ko zero one kar ke test karein."
              ],
              "say": "AND gate rakhein, do inputs A aur B, output Y, wires jodein, phir poke tool se test karein."
            },
            {
              "type": "check",
              "q": "LogiSim mein bright green wire ka kya matlab hai?",
              "a": "Logic one, yaani HIGH.",
              "say": "LogiSim mein bright green wire ka kya matlab hai? Jawab. Logic one, yaani HIGH."
            }
          ]
        },
        {
          "id": "sdlc",
          "code": "1.2.1 – 1.2.3",
          "title": "Software Development Life Cycle",
          "minutes": 10,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "SDLC ek structured process hai jo software ko shuru se akhir tak guide karti hai. Is se goals clear rehte hain, planning behtar hoti hai, risk kam hota hai, aur quality barhti hai. Yeh golden topic hai.",
              "html": "SDLC ek structured process hai jo software ko shuru se akhir tak guide karti hai. Is se goals clear rehte hain, planning behtar hoti hai, risk kam hota hai, aur quality barhti hai. Yeh golden topic hai."
            },
            {
              "type": "steps",
              "title": "SDLC ke 6 phases",
              "items": [
                "Requirement analysis: client se zarooratain, features ki list, SRS document.",
                "System design: architecture, database, screens, flowcharts. Design document.",
                "Implementation: Python ya Java mein asal code.",
                "Testing: bugs dhoondhna. Test reports.",
                "Deployment: users tak pohanchana. Direct, phased, ya pilot.",
                "Maintenance: support, updates, patches."
              ],
              "say": "Chhe phases: requirements, design, implementation, testing, deployment, maintenance."
            },
            {
              "type": "tip",
              "say": "Ghar banane ki analogy yaad rakhein. Phase one family se poochna ke kitne kamre chahiye. Phase two architect ka naqsha. Phase three mazdooron ka kaam."
            },
            {
              "type": "table",
              "headers": [
                "Testing",
                "Tester code dekhta hai?",
                "Kya check hota hai"
              ],
              "rows": [
                [
                  "Black box",
                  "Nahi",
                  "Inputs aur outputs, functionality"
                ],
                [
                  "White box",
                  "Haan",
                  "Andar ki logic aur structure"
                ]
              ],
              "say": "Black box sirf bahar se test karta hai. White box code ke andar dekhta hai."
            },
            {
              "type": "check",
              "q": "Sab se important SDLC phase kaun si hai, notes ke mutabiq?",
              "a": "Requirement analysis, kyunke yahin se SRS banta hai.",
              "say": "Sab se important SDLC phase kaun si hai, notes ke mutabiq? Jawab. Requirement analysis, kyunke yahin se SRS banta hai."
            }
          ]
        },
        {
          "id": "waterfall-agile",
          "code": "1.2.4 – 1.2.7",
          "title": "Waterfall aur Agile",
          "minutes": 10,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Waterfall linear hai. Ek phase poora hue baghair agla shuru nahi hota. Wapas jana mushkil hai. Istemal tab karein jab requirements clear, fixed, aur samajh aa chuki hon, project chhota ya medium ho, aur technology stable ho.",
              "html": "Waterfall linear hai. Ek phase poora hue baghair agla shuru nahi hota. Wapas jana mushkil hai. Istemal tab karein jab requirements clear, fixed, aur samajh aa chuki hon, project chhota ya medium ho, aur technology stable ho."
            },
            {
              "type": "svg",
              "name": "waterfall",
              "say": "Waterfall seedhi line mein neeche girta hai. Testing bohot der se hoti hai.",
              "caption": "Waterfall phases."
            },
            {
              "type": "p",
              "say": "Al-Noor Library Management System waterfall ki case study hai, kyunke coding se pehle requirements sau feesad fixed thin.",
              "html": "Al-Noor Library Management System waterfall ki case study hai, kyunke coding se pehle requirements sau feesad fixed thin."
            },
            {
              "type": "p",
              "say": "Agile iterative hai. Software chhote cycles mein banta hai jinhein sprints kehte hain, aam tor pe do se char hafte. Customer ki feedback lagatar aati hai. Tab use karein jab requirements badal sakti hon, ya jaldi working software chahiye.",
              "html": "Agile iterative hai. Software chhote cycles mein banta hai jinhein sprints kehte hain, aam tor pe do se char hafte. Customer ki feedback lagatar aati hai. Tab use karein jab requirements badal sakti hon, ya jaldi working software chahiye."
            },
            {
              "type": "svg",
              "name": "agile",
              "say": "Har sprint ke baad feedback milti hai aur agla sprint us hisaab se mud jata hai.",
              "caption": "Agile sprint loop."
            },
            {
              "type": "p",
              "say": "Al-Noor Student Mobile Application agile ki case study hai, kyunke teachers, parents, aur students development ke dauran naye features mangte rahe.",
              "html": "Al-Noor Student Mobile Application agile ki case study hai, kyunke teachers, parents, aur students development ke dauran naye features mangte rahe."
            },
            {
              "type": "table",
              "headers": [
                "Dimension",
                "Waterfall",
                "Agile"
              ],
              "rows": [
                [
                  "Flexibility",
                  "Sakht, baad mein change mushkil",
                  "Agle sprint mein change asaan"
                ],
                [
                  "Customer",
                  "Sirf shuru aur akhir",
                  "Har sprint ke baad"
                ],
                [
                  "Delivery",
                  "Ek dafa bilkul akhir mein",
                  "Har sprint ke baad thora software"
                ],
                [
                  "Testing",
                  "Der se, alag phase",
                  "Har sprint ke andar"
                ],
                [
                  "Documents",
                  "Bhari documentation",
                  "Halki, kaam karta software zaroori"
                ]
              ],
              "say": "Waterfall sakht aur akhir mein deliver karta hai. Agile flexible hai aur baar baar deliver karta hai."
            },
            {
              "type": "check",
              "q": "Requirements agar beech mein badal rahi hon to kaun sa model behtar hai?",
              "a": "Agile, kyunke agla sprint nayi requirement le sakta hai.",
              "say": "Requirements agar beech mein badal rahi hon to kaun sa model behtar hai? Jawab. Agile, kyunke agla sprint nayi requirement le sakta hai."
            }
          ]
        },
        {
          "id": "osi",
          "code": "1.3.1 – 1.3.4",
          "title": "OSI ke saat layers",
          "minutes": 10,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Communication model batata hai ke data ek device se doosre device tak kaise jata hai. OSI model ISO ne 1984 mein banaya. Yeh communication ko saat layers mein baantta hai. Golden topic hai.",
              "html": "Communication model batata hai ke data ek device se doosre device tak kaise jata hai. OSI model ISO ne 1984 mein banaya. Yeh communication ko saat layers mein baantta hai. Golden topic hai."
            },
            {
              "type": "svg",
              "name": "osi",
              "say": "Upar application hai, neeche physical. Mnemonic neeche se upar: Please Do Not Throw Sausage Pizza Away.",
              "caption": "OSI seven layers."
            },
            {
              "type": "tip",
              "say": "Mnemonic: Please Do Not Throw Sausage Pizza Away. Physical, Data link, Network, Transport, Session, Presentation, Application."
            },
            {
              "type": "table",
              "headers": [
                "Layer",
                "Kaam",
                "Misal"
              ],
              "rows": [
                [
                  "7 Application",
                  "User apps ko network service",
                  "HTTP, HTTPS, FTP, SMTP, DNS"
                ],
                [
                  "6 Presentation",
                  "Translation, encryption, compression",
                  "SSL/TLS, JPEG, MP3, ASCII"
                ],
                [
                  "5 Session",
                  "Session kholna, rakhna, band karna",
                  "NetBIOS, RPC"
                ],
                [
                  "4 Transport",
                  "End to end delivery, ports, errors",
                  "TCP reliable, UDP fast"
                ]
              ],
              "say": "Upar ki char layers: application, presentation, session, transport."
            },
            {
              "type": "p",
              "say": "Transport layer pe yaad rakhein: TCP tab jab accuracy chahiye, jaise web aur email. UDP tab jab speed zyada zaroori ho, jaise video streaming aur online game. UDP thodi packets kho bhi de to chal jata hai.",
              "html": "Transport layer pe yaad rakhein: TCP tab jab accuracy chahiye, jaise web aur email. UDP tab jab speed zyada zaroori ho, jaise video streaming aur online game. UDP thodi packets kho bhi de to chal jata hai."
            },
            {
              "type": "table",
              "headers": [
                "Layer",
                "Kaam",
                "Misal"
              ],
              "rows": [
                [
                  "3 Network",
                  "IP address aur routing",
                  "IP, ICMP ping, routers"
                ],
                [
                  "2 Data link",
                  "MAC address aur frames",
                  "Ethernet, switches"
                ],
                [
                  "1 Physical",
                  "Raw bits zero one",
                  "Cables, hubs, Wi-Fi radio"
                ]
              ],
              "say": "Neeche teen layers hardware ke qareeb hain: network, data link, physical."
            },
            {
              "type": "check",
              "q": "Online game ke liye TCP behtar hai ya UDP?",
              "a": "UDP, kyunke speed accuracy se zyada zaroori hai.",
              "say": "Online game ke liye TCP behtar hai ya UDP? Jawab. UDP, kyunke speed accuracy se zyada zaroori hai."
            }
          ]
        },
        {
          "id": "tcpip",
          "code": "1.3.5 – 1.3.6",
          "title": "TCP/IP model aur OSI se farq",
          "minutes": 7,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "TCP/IP woh practical model hai jo asal internet pe chalta hai. Yeh OSI ki saat layers ko char layers mein sama leta hai.",
              "html": "TCP/IP woh practical model hai jo asal internet pe chalta hai. Yeh OSI ki saat layers ko char layers mein sama leta hai."
            },
            {
              "type": "svg",
              "name": "tcpip",
              "say": "Application OSI ke 7, 6, 5 ko cover karti hai. Transport sirf 4. Internet sirf 3. Network access 2 aur 1.",
              "caption": "TCP/IP mapped onto OSI."
            },
            {
              "type": "table",
              "headers": [
                "TCP/IP layer",
                "OSI layers"
              ],
              "rows": [
                [
                  "1 Application",
                  "Application, Presentation, Session"
                ],
                [
                  "2 Transport",
                  "Transport"
                ],
                [
                  "3 Internet",
                  "Network"
                ],
                [
                  "4 Network Access",
                  "Data Link aur Physical"
                ]
              ],
              "say": "Char TCP/IP layers saat OSI layers ko cover karti hain."
            },
            {
              "type": "check",
              "q": "OSI ka network layer TCP/IP mein kis naam se hai?",
              "a": "Internet layer.",
              "say": "OSI ka network layer TCP/IP mein kis naam se hai? Jawab. Internet layer."
            }
          ]
        }
      ]
    },
    {
      "id": "ch2",
      "num": "02",
      "title": "Computational Thinking",
      "blurb": "Algorithms, pseudocode, decomposition, sorting, aur searching.",
      "lectures": [
        {
          "id": "ct-intro",
          "code": "2.1 – 2.2",
          "title": "Computational thinking aur algorithm",
          "minutes": 8,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Computational thinking maslon ko systematically hal karne ka tareeqa hai. Aap problem ko todte hain, pattern dekhte hain, faltu detail chhupate hain, aur algorithm banate hain.",
              "html": "Computational thinking maslon ko systematically hal karne ka tareeqa hai. Aap problem ko todte hain, pattern dekhte hain, faltu detail chhupate hain, aur algorithm banate hain."
            },
            {
              "type": "p",
              "say": "Algorithm ek step by step logical procedure hai jo problem solve kare. Yeh concept hai. Kisi ek programming language ka ghulam nahi. Pehle algorithm, phir code.",
              "html": "Algorithm ek step by step logical procedure hai jo problem solve kare. Yeh concept hai. Kisi ek programming language ka ghulam nahi. Pehle algorithm, phir code."
            },
            {
              "type": "steps",
              "title": "Algorithm kyun zaroori hai",
              "items": [
                "Bada kaam chhote steps mein aa jata hai.",
                "Time aur memory dono sochne ka mauqa milta hai.",
                "Milta julta masla dobara same steps se hal ho sakta hai.",
                "Galti kam hoti hai kyunke steps clear hote hain.",
                "Code se pehle blueprint mil jata hai."
              ],
              "say": "Algorithm structure, efficiency, reuse, accuracy, aur blueprint deta hai."
            },
            {
              "type": "tip",
              "say": "Pseudocode algorithm ko aisi angrezi mein likhta hai jo insaan parh le aur programmer code bana le. Yeh insaan aur machine ke beech ka pul hai."
            },
            {
              "type": "check",
              "q": "Algorithm kisi khasi language se bandha hota hai?",
              "a": "Nahi. Algorithm language-independent logical steps hain.",
              "say": "Algorithm kisi khasi language se bandha hota hai? Jawab. Nahi. Algorithm language-independent logical steps hain."
            }
          ]
        },
        {
          "id": "algo-pseudo",
          "code": "2.2.2",
          "title": "Algorithm aur pseudocode ka farq",
          "minutes": 8,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Dono design phase mein aate hain, lekin kaam alag hai. Algorithm batata hai kya karna hai. Pseudocode batata hai woh kaam parhne layak structure mein kaise likha jaye.",
              "html": "Dono design phase mein aate hain, lekin kaam alag hai. Algorithm batata hai kya karna hai. Pseudocode batata hai woh kaam parhne layak structure mein kaise likha jaye."
            },
            {
              "type": "table",
              "headers": [
                "Point",
                "Algorithm",
                "Pseudocode"
              ],
              "rows": [
                [
                  "Shakal",
                  "Plain numbered steps",
                  "IF, FOR, WHILE jaise words"
                ],
                [
                  "Language",
                  "Kisi language se azad",
                  "Code jaisa, lekin chalta nahi"
                ],
                [
                  "Focus",
                  "Logic kya hai",
                  "Steps kitne clear hain"
                ],
                [
                  "Parhne wala",
                  "Koi bhi",
                  "Zyada tar student ya programmer"
                ]
              ],
              "say": "Algorithm recipe hai. Pseudocode kitchen ka structured manual hai."
            },
            {
              "type": "p",
              "say": "Analogy: algorithm kehta hai cake 350 degree pe bake karo. Pseudocode kehta hai SET temperature TO 350. WHILE cake baked nahi, WAIT.",
              "html": "Analogy: algorithm kehta hai cake 350 degree pe bake karo. Pseudocode kehta hai SET temperature TO 350. WHILE cake baked nahi, WAIT."
            },
            {
              "type": "code",
              "lang": "text",
              "text": "SET temperature TO 350\nWHILE cake is not baked\n    WAIT\nEND WHILE",
              "say": "Pseudocode structured keywords use karta hai, lekin yeh executable program nahi."
            },
            {
              "type": "check",
              "q": "Recipe algorithm hai ya pseudocode?",
              "a": "Recipe algorithm hai. SET aur WHILE wala manual pseudocode hai.",
              "say": "Recipe algorithm hai ya pseudocode? Jawab. Recipe algorithm hai. SET aur WHILE wala manual pseudocode hai."
            }
          ]
        },
        {
          "id": "decomposition",
          "code": "2.3.1",
          "title": "Decomposition",
          "minutes": 7,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Decomposition ka matlab hai bara masla chhote hisso mein todna. Har hissa alag samajh aata hai, alag banta hai, aur galti bhi alag nazar aati hai. Golden topic hai.",
              "html": "Decomposition ka matlab hai bara masla chhote hisso mein todna. Har hissa alag samajh aata hai, alag banta hai, aur galti bhi alag nazar aati hai. Golden topic hai."
            },
            {
              "type": "p",
              "say": "Nayi zaban seekhna decomposition ki misaal hai. Pehle vocabulary: log, kaam, cheezein. Phir grammar: subject, verb, object. Phir tenses: I eat aur I ate. Phir in sab ko jod kar jumla.",
              "html": "Nayi zaban seekhna decomposition ki misaal hai. Pehle vocabulary: log, kaam, cheezein. Phir grammar: subject, verb, object. Phir tenses: I eat aur I ate. Phir in sab ko jod kar jumla."
            },
            {
              "type": "table",
              "headers": [
                "Subtask",
                "Kaam"
              ],
              "rows": [
                [
                  "Vocabulary",
                  "Log, actions, cheezon ke lafz"
                ],
                [
                  "Grammar",
                  "Subject, phir verb, phir object"
                ],
                [
                  "Tenses",
                  "Present, past, future"
                ],
                [
                  "Sentences",
                  "Rules se sahi jumle"
                ]
              ],
              "say": "Bari zaban ko chaar chhote subtasks mein tod diya."
            },
            {
              "type": "steps",
              "title": "Faida",
              "items": [
                "Ek waqt pe ek tukda, complexity kam.",
                "Bug mil jaye to pata chale verb galat hai ya lafz.",
                "Ek dafa seekha hua tukda doosri jagah dobara use ho."
              ],
              "say": "Decomposition complexity kam karta hai, debugging asaan karta hai, aur reuse deta hai."
            },
            {
              "type": "check",
              "q": "Decomposition ka seedha matlab kya hai?",
              "a": "Complex kaam ko chhote manageable hisson mein todna.",
              "say": "Decomposition ka seedha matlab kya hai? Jawab. Complex kaam ko chhote manageable hisson mein todna."
            }
          ]
        },
        {
          "id": "patterns",
          "code": "2.3.2",
          "title": "Pattern recognition",
          "minutes": 7,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Pattern recognition ka matlab hai data mein dohrav, qayeda, ya rule dekhna. Is se algorithm chhota ho jata hai. Loops ki bunyad yahi hai.",
              "html": "Pattern recognition ka matlab hai data mein dohrav, qayeda, ya rule dekhna. Is se algorithm chhota ho jata hai. Loops ki bunyad yahi hai."
            },
            {
              "type": "p",
              "say": "Teen sawal poochhein. Kya dohra raha hai? Kya ek predicted tareeqe se badal raha hai? Kya main isay ek general rule bana sakta hoon?",
              "html": "Teen sawal poochhein. Kya dohra raha hai? Kya ek predicted tareeqe se badal raha hai? Kya main isay ek general rule bana sakta hoon?"
            },
            {
              "type": "code",
              "lang": "text",
              "text": "*\n**\n***\n****\n*****",
              "say": "Har row pichli row se ek star zyada hai. Row N pe N stars."
            },
            {
              "type": "p",
              "say": "Agar pattern na dekhein to aap paanch alag print statements likhenge. Pattern dekh kar ek loop likh dete hain: row number jitne stars.",
              "html": "Agar pattern na dekhein to aap paanch alag print statements likhenge. Pattern dekh kar ek loop likh dete hain: row number jitne stars."
            },
            {
              "type": "tip",
              "say": "Jab bhi aapko copy-paste karne ka dil kare, ruk jayein. Wahan pattern chhupa hai, aur pattern loop ban jata hai."
            },
            {
              "type": "check",
              "q": "Star triangle mein row 4 pe kitne stars honge?",
              "a": "Char stars. Row N pe N stars.",
              "say": "Star triangle mein row 4 pe kitne stars honge? Jawab. Char stars. Row N pe N stars."
            }
          ]
        },
        {
          "id": "abstraction",
          "code": "2.3.3",
          "title": "Abstraction",
          "minutes": 7,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Abstraction ka matlab hai jo zaroori nahi usay chhupa dena, aur sirf woh rakhna jo masla hal kare. Noise hatao, core logic rakho.",
              "html": "Abstraction ka matlab hai jo zaroori nahi usay chhupa dena, aur sirf woh rakhna jo masla hal kare. Noise hatao, core logic rakho."
            },
            {
              "type": "table",
              "headers": [
                "Chai banane ke zaroori steps",
                "Jo situation se badle",
                "Jo ignore karein"
              ],
              "rows": [
                [
                  "Pani ubalen",
                  "Black, green, ya doodh",
                  "Kettle ka brand"
                ],
                [
                  "Chai dalein",
                  "Cheeni ya lemon",
                  "Cup ka rang"
                ],
                [
                  "Kuch der rukein",
                  "Stove ya kettle",
                  "Kitchen hai ya office"
                ],
                [
                  "Cup mein dalein aur serve karein",
                  "Maza apni pasand",
                  "Yeh noise hai"
                ]
              ],
              "say": "Core logic paanch steps hai. Brand aur cup ka rang algorithm mein nahi aate."
            },
            {
              "type": "p",
              "say": "Abstracted algorithm yahi rehta hai: ubalen, chai dalein, rukein, cup mein dalein, serve karein. Yeh kettle ke brand se azad hai.",
              "html": "Abstracted algorithm yahi rehta hai: ubalen, chai dalein, rukein, cup mein dalein, serve karein. Yeh kettle ke brand se azad hai."
            },
            {
              "type": "check",
              "q": "Chai ke algorithm mein cup ka rang kyun nahi aata?",
              "a": "Kyunke woh noise hai. Chai banne pe asar nahi karta.",
              "say": "Chai ke algorithm mein cup ka rang kyun nahi aata? Jawab. Kyunke woh noise hai. Chai banne pe asar nahi karta."
            }
          ]
        },
        {
          "id": "bubble",
          "code": "2.4.1",
          "title": "Bubble sort",
          "minutes": 10,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Sorting ka matlab cheezon ko order mein lagana hai, chhote se bara ya bara se chhota. Searching ka matlab list mein cheez dhoondhna hai. Bubble sort bagal walon ko compare karta hai aur galat order ho to swap kar deta hai. Golden topic hai.",
              "html": "Sorting ka matlab cheezon ko order mein lagana hai, chhote se bara ya bara se chhota. Searching ka matlab list mein cheez dhoondhna hai. Bubble sort bagal walon ko compare karta hai aur galat order ho to swap kar deta hai. Golden topic hai."
            },
            {
              "type": "svg",
              "name": "bubble",
              "say": "List 8, 4, 1, 9, 3. Pehle pass mein 9 end pe pohonch jata hai.",
              "caption": "Bubble sort, first pass."
            },
            {
              "type": "steps",
              "title": "Pehla pass, list 8 4 1 9 3",
              "items": [
                "8 aur 4: 8 bara hai, swap. Ab 4, 8, 1, 9, 3.",
                "8 aur 1: swap. Ab 4, 1, 8, 9, 3.",
                "8 aur 9: 8 chhota hai, koi swap nahi.",
                "9 aur 3: swap. Ab 4, 1, 8, 3, 9. 9 apni jagah pe hai."
              ],
              "say": "Har pass mein sab se bara number end ki taraf bubble karta hai."
            },
            {
              "type": "code",
              "lang": "python",
              "text": "DATA = [8, 4, 1, 9, 3]\nN = 5\nfor outer in range(N - 1):\n    for inner in range(N - 1 - outer):\n        if DATA[inner] > DATA[inner + 1]:\n            DATA[inner], DATA[inner + 1] = DATA[inner + 1], DATA[inner]",
              "say": "Nested loops. Inner loop hamesha shuru se chalti hai, lekin har pass mein end chhota hota jata hai."
            },
            {
              "type": "p",
              "say": "Sorted list 1, 3, 4, 8, 9 banti hai. Faida: samajhna asaan hai, extra memory nahi, aur equal items apni order mein rehte hain, is liye stable hai. Nuqsan: swaps bohot hain, bari list pe bohot slow hai.",
              "html": "Sorted list 1, 3, 4, 8, 9 banti hai. Faida: samajhna asaan hai, extra memory nahi, aur equal items apni order mein rehte hain, is liye stable hai. Nuqsan: swaps bohot hain, bari list pe bohot slow hai."
            },
            {
              "type": "check",
              "q": "Bubble sort stable kyun kehlata hai?",
              "a": "Equal items apni relative order nahi badalte.",
              "say": "Bubble sort stable kyun kehlata hai? Jawab. Equal items apni relative order nahi badalte."
            }
          ]
        },
        {
          "id": "selection",
          "code": "2.4.1",
          "title": "Selection sort",
          "minutes": 9,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Selection sort baar baar unsorted hisse se sab se chhota element chunta hai aur usay aage ki sahi jagah pe rakh deta hai. Golden topic hai.",
              "html": "Selection sort baar baar unsorted hisse se sab se chhota element chunta hai aur usay aage ki sahi jagah pe rakh deta hai. Golden topic hai."
            },
            {
              "type": "svg",
              "name": "selection",
              "say": "Pehle position ke liye poori list mein sab se chhota dhoondh kar aage rakh dein. Yahan 1 aa jata hai.",
              "caption": "Selection sort idea."
            },
            {
              "type": "p",
              "say": "List 8, 4, 1, 9, 3. Pehle position pe 8 hai. 4 chhota hai, swap. Phir 1 us se bhi chhota hai, swap. 9 aur 3 dono 1 se bare hain, is liye 1 wahin ruk jata hai.",
              "html": "List 8, 4, 1, 9, 3. Pehle position pe 8 hai. 4 chhota hai, swap. Phir 1 us se bhi chhota hai, swap. 9 aur 3 dono 1 se bare hain, is liye 1 wahin ruk jata hai."
            },
            {
              "type": "code",
              "lang": "python",
              "text": "DATA = [8, 4, 1, 9, 3]\nN = 5\nfor outer in range(N - 1):\n    for inner in range(outer + 1, N):\n        if DATA[outer] > DATA[inner]:\n            DATA[outer], DATA[inner] = DATA[inner], DATA[outer]",
              "say": "Farq yeh hai ke inner loop outer plus one se shuru hoti hai. Bubble sort ki inner loop zero se shuru hoti hai."
            },
            {
              "type": "tip",
              "say": "Teacher ka tip: inner loop ka start compare karein. Selection outer plus one se. Bubble hamesha zero se."
            },
            {
              "type": "p",
              "say": "Faida: code chhota hai, swaps bubble se kam hain, extra memory nahi. Nuqsan: phir bhi nested loops, sorted list pe bhi poora kaam karta hai, aur stable nahi, equal items ki order badal sakti hai.",
              "html": "Faida: code chhota hai, swaps bubble se kam hain, extra memory nahi. Nuqsan: phir bhi nested loops, sorted list pe bhi poora kaam karta hai, aur stable nahi, equal items ki order badal sakti hai."
            },
            {
              "type": "check",
              "q": "Selection sort ki inner loop kahan se shuru hoti hai?",
              "a": "Outer index ke agle element se, yaani outer plus one.",
              "say": "Selection sort ki inner loop kahan se shuru hoti hai? Jawab. Outer index ke agle element se, yaani outer plus one."
            }
          ]
        },
        {
          "id": "linear",
          "code": "2.4.2",
          "title": "Linear search",
          "minutes": 8,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Linear search, ya sequential search, list ke har element ko ek ek karke dekhti hai jab tak target na mil jaye. Sorted ho ya unsorted, dono pe chalti hai.",
              "html": "Linear search, ya sequential search, list ke har element ko ek ek karke dekhti hai jab tak target na mil jaye. Sorted ho ya unsorted, dono pe chalti hai."
            },
            {
              "type": "steps",
              "title": "List 8, 3, 6, 1, 7, 2, 4, 5 mein 7 dhoondhein",
              "items": [
                "8 check kiya, 7 nahi.",
                "3 check kiya, 7 nahi.",
                "6 check kiya, 7 nahi.",
                "1 check kiya, 7 nahi.",
                "7 check kiya, mil gaya. Loop yahin ruk jati hai."
              ],
              "say": "Paanchwe element pe 7 mil jata hai."
            },
            {
              "type": "code",
              "lang": "python",
              "text": "DATA = [8, 3, 6, 1, 7, 2, 4, 5]\nfind = 7\nfound = False\nfor value in DATA:\n    if value == find:\n        found = True\n        break\nif not found:\n    print(\"Data Not Found\")",
              "say": "Ek loop aur ek if. Milte hi break."
            },
            {
              "type": "p",
              "say": "Faida: sort ki zaroorat nahi, code seedha, chhoti list pe tez, extra space nahi. Nuqsan: agar target das lakh ke end pe ho to das lakh checks. List double ho to time bhi lagbhag double.",
              "html": "Faida: sort ki zaroorat nahi, code seedha, chhoti list pe tez, extra space nahi. Nuqsan: agar target das lakh ke end pe ho to das lakh checks. List double ho to time bhi lagbhag double."
            },
            {
              "type": "check",
              "q": "Linear search sorted list maangti hai?",
              "a": "Nahi. Sorted aur unsorted dono pe chalti hai.",
              "say": "Linear search sorted list maangti hai? Jawab. Nahi. Sorted aur unsorted dono pe chalti hai."
            }
          ]
        },
        {
          "id": "binary",
          "code": "2.4.2",
          "title": "Binary search",
          "minutes": 10,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Binary search list ko baar baar aadha karti hai. Bahut tez hai, lekin sirf sorted list pe chalti hai. Unsorted pe yeh galat jawab de sakti hai. Golden topic hai.",
              "html": "Binary search list ko baar baar aadha karti hai. Bahut tez hai, lekin sirf sorted list pe chalti hai. Unsorted pe yeh galat jawab de sakti hai. Golden topic hai."
            },
            {
              "type": "math",
              "tex": "\\mathrm{MID} = \\left\\lfloor \\frac{\\mathrm{BEG}+\\mathrm{END}}{2} \\right\\rfloor",
              "say": "Mid barabar beg plus end, taqseem do, decimal gira dein.",
              "display": true
            },
            {
              "type": "svg",
              "name": "binary",
              "say": "Sorted list 1 se 8. Item 3 dhoondhna hai. Pehle mid ki value 4 hai. 3 chhota hai, is liye left jao.",
              "caption": "Binary search first cut."
            },
            {
              "type": "steps",
              "title": "Item 3, list 1 2 3 4 5 6 7 8",
              "items": [
                "Mid value 4. 3 chhota hai, right half hata dein.",
                "Bachi list 1 2 3. Mid value 2. 3 bara hai, right jao.",
                "Bachi value 3. Barabar hai. Mil gaya."
              ],
              "say": "Teen steps mein 3 mil jata hai."
            },
            {
              "type": "p",
              "say": "Das lakh sorted items mein binary search lagbhag bees steps mein dhoondh leti hai. Nuqsan: pehle sort chahiye, random access chahiye jaise array, aur off by one ki galti asaan hai.",
              "html": "Das lakh sorted items mein binary search lagbhag bees steps mein dhoondh leti hai. Nuqsan: pehle sort chahiye, random access chahiye jaise array, aur off by one ki galti asaan hai."
            },
            {
              "type": "tip",
              "say": "Agar list scrambled ho to binary search use na karein. Pehle sort karein, ya linear search use karein."
            },
            {
              "type": "check",
              "q": "Binary search unsorted list pe kyun fail hoti hai?",
              "a": "Kyunke yeh assume karti hai ke left chhota hai aur right bara. Bina sort yeh assumption jhoot hai.",
              "say": "Binary search unsorted list pe kyun fail hoti hai? Jawab. Kyunke yeh assume karti hai ke left chhota hai aur right bara. Bina sort yeh assumption jhoot hai."
            }
          ]
        },
        {
          "id": "evaluate",
          "code": "2.5",
          "title": "Algorithm ko parakhna",
          "minutes": 8,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Algorithm teen hisaab se parakha jata hai: correctness, efficiency, aur clarity.",
              "html": "Algorithm teen hisaab se parakha jata hai: correctness, efficiency, aur clarity."
            },
            {
              "type": "p",
              "say": "Correct algorithm wohi output deta hai jo ummeed hai, edge cases sambhalta hai, aur kabhi infinite loop mein nahi phans ta. Yeh khatam hona zaroori hai.",
              "html": "Correct algorithm wohi output deta hai jo ummeed hai, edge cases sambhalta hai, aur kabhi infinite loop mein nahi phans ta. Yeh khatam hona zaroori hai."
            },
            {
              "type": "table",
              "headers": [
                "Input",
                "2 se divide, remainder",
                "Remainder zero?",
                "Result"
              ],
              "rows": [
                [
                  "3",
                  "3 / 2, remainder 1",
                  "Nahi",
                  "Odd"
                ],
                [
                  "6",
                  "6 / 2, remainder 0",
                  "Haan",
                  "Even"
                ],
                [
                  "15",
                  "15 / 2, remainder 1",
                  "Nahi",
                  "Odd"
                ]
              ],
              "say": "Trace table even odd checker dikhati hai. Remainder zero ho to even."
            },
            {
              "type": "math",
              "tex": "n \\bmod 2 = 0",
              "say": "Agar n mod 2 zero ho to number even hai.",
              "display": true
            },
            {
              "type": "p",
              "say": "Efficiency do cheezon se map hoti hai. Time: input barhne pe kitni der. Space: kitni memory. Clarity: koi doosra student steps parh kar samajh jaye.",
              "html": "Efficiency do cheezon se map hoti hai. Time: input barhne pe kitni der. Space: kitni memory. Clarity: koi doosra student steps parh kar samajh jaye."
            },
            {
              "type": "check",
              "q": "Teen evaluation criteria ke naam batao.",
              "a": "Correctness, efficiency yaani time aur space, aur clarity.",
              "say": "Teen evaluation criteria ke naam batao. Jawab. Correctness, efficiency yaani time aur space, aur clarity."
            }
          ]
        },
        {
          "id": "choose-algo",
          "code": "2.6",
          "title": "Kaun sa algorithm chunein",
          "minutes": 6,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Algorithm choose karne se pehle teen sawal: input kitna bara hai? Data sorted hai? Hamein speed chahiye ya memory ki bachat?",
              "html": "Algorithm choose karne se pehle teen sawal: input kitna bara hai? Data sorted hai? Hamein speed chahiye ya memory ki bachat?"
            },
            {
              "type": "table",
              "headers": [
                "Halat",
                "Choice"
              ],
              "rows": [
                [
                  "Unsorted list mein dhoondhna",
                  "Linear search"
                ],
                [
                  "Sorted list mein dhoondhna",
                  "Binary search"
                ],
                [
                  "Data ko order mein lana",
                  "Bubble ya selection, bari data pe yeh slow hain"
                ],
                [
                  "Samajhna aur trace karna",
                  "Bubble, kyunke picture clear hai"
                ],
                [
                  "Swaps kam rakhne hain",
                  "Selection, bubble se kam swaps"
                ]
              ],
              "say": "Unsorted pe linear. Sorted pe binary. Order chahiye to sorting."
            },
            {
              "type": "p",
              "say": "Chapter ka khulasa: computational thinking decomposition, pattern, abstraction, aur algorithm hai. Pseudocode structured angrezi hai. Bubble aur selection chhoti lists ke liye seekhne layak hain, bari data ke liye slow. Linear har list pe, binary sirf sorted pe.",
              "html": "Chapter ka khulasa: computational thinking decomposition, pattern, abstraction, aur algorithm hai. Pseudocode structured angrezi hai. Bubble aur selection chhoti lists ke liye seekhne layak hain, bari data ke liye slow. Linear har list pe, binary sirf sorted pe."
            },
            {
              "type": "check",
              "q": "Sorted hazaar numbers mein ek value, kaun si search?",
              "a": "Binary search.",
              "say": "Sorted hazaar numbers mein ek value, kaun si search? Jawab. Binary search."
            }
          ]
        }
      ]
    },
    {
      "id": "ch3",
      "num": "03",
      "title": "Programming Fundamentals",
      "blurb": "Python, variables, operators, if else, loops, libraries, aur bugs.",
      "lectures": [
        {
          "id": "languages",
          "code": "3.1",
          "title": "Programming aur language ki qismen",
          "minutes": 8,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Computer khud se nahi sochta. Bina instructions ke woh kuch nahi karta. Instructions ke set ko program kehte hain, aur un instructions ki zaban programming language hai.",
              "html": "Computer khud se nahi sochta. Bina instructions ke woh kuch nahi karta. Instructions ke set ko program kehte hain, aur un instructions ki zaban programming language hai."
            },
            {
              "type": "svg",
              "name": "languages",
              "say": "Low level binary hai, mid level assembly mnemonics, high level angrezi jaise lafz.",
              "caption": "Three language levels."
            },
            {
              "type": "table",
              "headers": [
                "Level",
                "Matlab",
                "Misal"
              ],
              "rows": [
                [
                  "Low",
                  "Machine ki apni zaban, zero one, insaan ke liye mushkil",
                  "Binary machine language"
                ],
                [
                  "Mid",
                  "Hardware ke qareeb, lekin words se, mnemonics",
                  "Assembly, MOV AX, BX"
                ],
                [
                  "High",
                  "Insaan ke liye asaan, angrezi jaise",
                  "C++, Java, Python"
                ]
              ],
              "say": "Teen levels: low binary, mid assembly, high C++ Java Python."
            },
            {
              "type": "p",
              "say": "C++ hardware ke qareeb hai, operating system aur games mein. Java ka naara write once run anywhere hai, enterprise aur Android mein. Python ka syntax seedha hai, data science, AI, web, aur beginners ke liye.",
              "html": "C++ hardware ke qareeb hai, operating system aur games mein. Java ka naara write once run anywhere hai, enterprise aur Android mein. Python ka syntax seedha hai, data science, AI, web, aur beginners ke liye."
            },
            {
              "type": "check",
              "q": "Assembly language low hai, mid, ya high?",
              "a": "Mid level. Mnemonics use karti hai, jaise MOV AX, BX.",
              "say": "Assembly language low hai, mid, ya high? Jawab. Mid level. Mnemonics use karti hai, jaise MOV AX, BX."
            }
          ]
        },
        {
          "id": "python-careers",
          "code": "3.2",
          "title": "Python se career",
          "minutes": 6,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Python is liye seekhte hain ke dimagh logic pe lage, syntax yaad karne pe nahi. Sindh curriculum bhi Python ko shuruat ki zaban banata hai.",
              "html": "Python is liye seekhte hain ke dimagh logic pe lage, syntax yaad karne pe nahi. Sindh curriculum bhi Python ko shuruat ki zaban banata hai."
            },
            {
              "type": "steps",
              "title": "Python kahan kaam aati hai",
              "items": [
                "Desktop aur web applications.",
                "Data science: reports aur predictions.",
                "AI aur machine learning, chatbots, recommendations.",
                "Django aur Flask se websites.",
                "Office ke repetitive kaam automate karna.",
                "Security tools aur network data."
              ],
              "say": "Software, data, AI, web, automation, aur cybersecurity."
            },
            {
              "type": "check",
              "q": "Python beginner ko syntax se zyada kis cheez pe focus karne deti hai?",
              "a": "Problem solving aur logic pe.",
              "say": "Python beginner ko syntax se zyada kis cheez pe focus karne deti hai? Jawab. Problem solving aur logic pe."
            }
          ]
        },
        {
          "id": "ide",
          "code": "3.3",
          "title": "IDE aur VS Code",
          "minutes": 7,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "IDE woh jagah hai jahan aap code likhte, chalate, aur sambhalte hain. Ek hi workspace.",
              "html": "IDE woh jagah hai jahan aap code likhte, chalate, aur sambhalte hain. Ek hi workspace."
            },
            {
              "type": "steps",
              "title": "IDE ke hisse",
              "items": [
                "Code editor, jahan likhte hain.",
                "Syntax highlighting, rang se parhna asaan.",
                "Auto completion, likhte waqt suggestion.",
                "Run button.",
                "Debugger, galti dhoondhne ke liye."
              ],
              "say": "Editor, colors, suggestions, run, aur debugger."
            },
            {
              "type": "p",
              "say": "VS Code muft aur halka editor hai. Default mein poora IDE nahi, lekin extensions se ban jata hai. Microsoft ka Python extension laga lein, tab highlighting aur run dono aa jate hain.",
              "html": "VS Code muft aur halka editor hai. Default mein poora IDE nahi, lekin extensions se ban jata hai. Microsoft ka Python extension laga lein, tab highlighting aur run dono aa jate hain."
            },
            {
              "type": "table",
              "headers": [
                "Hissa",
                "Kaam"
              ],
              "rows": [
                [
                  "Explorer",
                  "Files aur folders"
                ],
                [
                  "Search",
                  "Project mein lafz dhoondhna"
                ],
                [
                  "Source Control",
                  "Git se changes"
                ],
                [
                  "Run and Debug",
                  "Code chalana, line pe rukna, variables dekhna"
                ],
                [
                  "Extensions",
                  "Python extension jaisi extra cheezein"
                ]
              ],
              "say": "Side bar: explorer, search, git, debug, extensions."
            },
            {
              "type": "check",
              "q": "VS Code ko Python IDE banane ke liye kya chahiye?",
              "a": "Python extension, aam tor pe Microsoft wali.",
              "say": "VS Code ko Python IDE banane ke liye kya chahiye? Jawab. Python extension, aam tor pe Microsoft wali."
            }
          ]
        },
        {
          "id": "python-basics",
          "code": "3.4",
          "title": "Python program ki bunyad",
          "minutes": 7,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Python program upar se neeche chalta hai. Comments insaan ke liye note hain. Hash se shuru hote hain. Interpreter unhein ignore kar deta hai.",
              "html": "Python program upar se neeche chalta hai. Comments insaan ke liye note hain. Hash se shuru hote hain. Interpreter unhein ignore kar deta hai."
            },
            {
              "type": "p",
              "say": "C++ aur Java curly brackets se block banate hain. Python indentation se. Andar wali line shuru mein spaces leti hai. Standard char spaces hain. Indentation optional nahi, zaroori hai.",
              "html": "C++ aur Java curly brackets se block banate hain. Python indentation se. Andar wali line shuru mein spaces leti hai. Standard char spaces hain. Indentation optional nahi, zaroori hai."
            },
            {
              "type": "code",
              "lang": "python",
              "text": "# yeh comment hai, interpreter ignore karega\nprint(\"Hello, World!\")\nif 5 > 2:\n    print(\"Five is greater than two!\")",
              "say": "Hash comment hai. If ke neeche print indented hai, warna program nahi chalta."
            },
            {
              "type": "tip",
              "say": "IndentationError aaye to spaces check karein. Tabs aur spaces mila kar program toot jata hai."
            },
            {
              "type": "check",
              "q": "Python block curly brackets se banta hai ya indentation se?",
              "a": "Indentation se. Standard char spaces.",
              "say": "Python block curly brackets se banta hai ya indentation se? Jawab. Indentation se. Standard char spaces."
            }
          ]
        },
        {
          "id": "variables",
          "code": "3.4.1",
          "title": "Variables aur data types",
          "minutes": 10,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Variable memory ka naam wala container hai. Python mein type alag se declare nahi karte. Value dekh kar Python khud type laga leta hai. Golden topic hai.",
              "html": "Variable memory ka naam wala container hai. Python mein type alag se declare nahi karte. Value dekh kar Python khud type laga leta hai. Golden topic hai."
            },
            {
              "type": "steps",
              "title": "Naam ke rules",
              "items": [
                "Letters, numbers, aur underscore chalenge.",
                "Shuru letter ya underscore se ho, number se nahi. 1name galat hai.",
                "age aur Age alag variables hain. Case sensitive.",
                "if, for, while jaise keywords naam nahi ban sakte.",
                "Beech mein space nahi. my height galat, my_height theek."
              ],
              "say": "Letter se shuru, space nahi, keyword nahi, case alag."
            },
            {
              "type": "table",
              "headers": [
                "Type",
                "Misal"
              ],
              "rows": [
                [
                  "int",
                  "age = 16"
                ],
                [
                  "float",
                  "height = 5.7"
                ],
                [
                  "str",
                  "name = \"Sammy\""
                ],
                [
                  "bool",
                  "is_student = True"
                ],
                [
                  "list",
                  "marks = [85, 90, 75]"
                ],
                [
                  "tuple",
                  "coords = (10, 20). Badal nahi sakte"
                ],
                [
                  "dict",
                  "student = {\"name\": \"Ahmed\", \"age\": 16}"
                ],
                [
                  "set",
                  "vowels = {'a', 'e', 'i'}. Unique cheezein"
                ]
              ],
              "say": "Int whole number, float decimal, str text, bool True False, list badal sakti hai, tuple nahi, dict key value, set unique."
            },
            {
              "type": "tip",
              "say": "Boolean mein True aur False ka pehla letter capital hai. true chhota likhoge to naam ban jayega, Boolean value nahi."
            },
            {
              "type": "check",
              "q": "List aur tuple mein farq kya hai?",
              "a": "List badal sakti hai, square brackets. Tuple badal nahi sakta, round brackets.",
              "say": "List aur tuple mein farq kya hai? Jawab. List badal sakti hai, square brackets. Tuple badal nahi sakta, round brackets."
            }
          ]
        },
        {
          "id": "io",
          "code": "3.4.2",
          "title": "Input aur output",
          "minutes": 7,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "print screen pe dikhata hai. Comma se text aur variable dono ek line mein aa jate hain. f-string sab se parhne layak tareeqa hai.",
              "html": "print screen pe dikhata hai. Comma se text aur variable dono ek line mein aa jate hain. f-string sab se parhne layak tareeqa hai."
            },
            {
              "type": "code",
              "lang": "python",
              "text": "name = \"Ali\"\nage = 16\nprint(\"Welcome,\", name)\nprint(f\"My name is {name} and I am {age} years old.\")",
              "say": "f se pehle string, aur curly brackets ke andar variable."
            },
            {
              "type": "p",
              "say": "input program ko rok deta hai jab tak user kuch likhe. Jo bhi aata hai, woh hamesha string hota hai, chahe user ne number hi kyun na likha ho. Number chahiye to int ya float se type cast karein.",
              "html": "input program ko rok deta hai jab tak user kuch likhe. Jo bhi aata hai, woh hamesha string hota hai, chahe user ne number hi kyun na likha ho. Number chahiye to int ya float se type cast karein."
            },
            {
              "type": "code",
              "lang": "python",
              "text": "user_name = input(\"Enter your name: \")\nage = int(input(\"Enter your age: \"))\nheight = float(input(\"Enter your height: \"))",
              "say": "input string deta hai. int aur float us string ko number bana dete hain."
            },
            {
              "type": "check",
              "q": "input() number return karta hai ya string?",
              "a": "Hamesha string. Number chahiye to int ya float lagayein.",
              "say": "input() number return karta hai ya string? Jawab. Hamesha string. Number chahiye to int ya float lagayein."
            }
          ]
        },
        {
          "id": "operators",
          "code": "3.4.3",
          "title": "Operators aur operands",
          "minutes": 12,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Operand value hai, operator nishaan hai. 10 operand, plus operator, 20 operand. Golden topic hai.",
              "html": "Operand value hai, operator nishaan hai. 10 operand, plus operator, 20 operand. Golden topic hai."
            },
            {
              "type": "math",
              "tex": "9 / 2 = 4.5 \\qquad 9 // 2 = 4 \\qquad 9 \\% 2 = 1 \\qquad 2^{3} = 8",
              "say": "Nau taqseem do float 4.5 hai. Double slash floor 4 hai. Percent remainder 1 hai. Do star star teen, yaani do ki power teen, barabar 8.",
              "display": true
            },
            {
              "type": "table",
              "headers": [
                "Operator",
                "Kaam",
                "Misal"
              ],
              "rows": [
                [
                  "+",
                  "Jama",
                  "5 + 3 = 8"
                ],
                [
                  "-",
                  "Tafreeq",
                  "10 - 4 = 6"
                ],
                [
                  "*",
                  "Zarb",
                  "4 * 2 = 8"
                ],
                [
                  "/",
                  "Taqseem, hamesha float",
                  "9 / 2 = 4.5"
                ],
                [
                  "//",
                  "Floor, decimal girao",
                  "9 // 2 = 4"
                ],
                [
                  "%",
                  "Baqi",
                  "9 % 2 = 1"
                ],
                [
                  "**",
                  "Power",
                  "2 ** 3 = 8"
                ]
              ],
              "say": "Division slash float deta hai. Double slash decimal gira deta hai."
            },
            {
              "type": "p",
              "say": "Assignment: x = 5. x += 2 ka matlab x = x + 2. Relational operators True ya False dete hain. == barabar, != na barabar. Ek equals assign karta hai, do equals compare karte hain.",
              "html": "Assignment: x = 5. x += 2 ka matlab x = x + 2. Relational operators True ya False dete hain. == barabar, != na barabar. Ek equals assign karta hai, do equals compare karte hain."
            },
            {
              "type": "p",
              "say": "and tab True jab dono conditions true hon. or tab True jab ek bhi true ho. not ulta kar deta hai. in check karta hai ke value andar hai ya nahi.",
              "html": "and tab True jab dono conditions true hon. or tab True jab ek bhi true ho. not ulta kar deta hai. in check karta hai ke value andar hai ya nahi."
            },
            {
              "type": "code",
              "lang": "python",
              "text": "name = \"Python\"\nprint(\"P\" in name)       # True\nprint(\"z\" not in name)   # True\nprint(10 & 6)            # 2\nprint(10 | 6)            # 14\nprint(5 << 1)            # 10\nprint(20 >> 1)           # 10",
              "say": "Membership in aur not in. Bitwise AND 10 aur 6 ka result 2 hai, OR ka 14. Left shift zarb do, right shift floor taqseem do."
            },
            {
              "type": "table",
              "headers": [
                "Bits",
                "AND",
                "OR",
                "XOR"
              ],
              "rows": [
                [
                  "0 0",
                  "0",
                  "0",
                  "0"
                ],
                [
                  "0 1",
                  "0",
                  "1",
                  "1"
                ],
                [
                  "1 0",
                  "0",
                  "1",
                  "1"
                ],
                [
                  "1 1",
                  "1",
                  "1",
                  "0"
                ]
              ],
              "say": "Bitwise AND dono one tab one. OR koi ek one. XOR jab bits alag hon."
            },
            {
              "type": "p",
              "say": "10 binary 1010 hai, 6 binary 0110. AND 0010 deta hai jo decimal 2 hai. OR 1110 deta hai jo 14 hai. NOT of 10, tilde 10, result negative 11 hai. Left shift ek bit se 5 ko 10 bana deta hai.",
              "html": "10 binary 1010 hai, 6 binary 0110. AND 0010 deta hai jo decimal 2 hai. OR 1110 deta hai jo 14 hai. NOT of 10, tilde 10, result negative 11 hai. Left shift ek bit se 5 ko 10 bana deta hai."
            },
            {
              "type": "tip",
              "say": "Slash aur double slash ka farq exam ka favourite hai. 9 slash 2 barabar 4.5. 9 double slash 2 barabar 4."
            },
            {
              "type": "check",
              "q": "10 AND 6 bitwise ka decimal result?",
              "a": "2. Binary 1010 aur 0110 ka AND 0010 hai.",
              "say": "10 AND 6 bitwise ka decimal result? Jawab. 2. Binary 1010 aur 0110 ka AND 0010 hai."
            }
          ]
        },
        {
          "id": "sequence",
          "code": "3.5 – 3.5.1",
          "title": "Control structures aur sequence",
          "minutes": 6,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Control structure yeh faisla karti hai ke statements kis order mein chalenge. Teen bunyadi structures hain: sequence, selection, aur repetition.",
              "html": "Control structure yeh faisla karti hai ke statements kis order mein chalenge. Teen bunyadi structures hain: sequence, selection, aur repetition."
            },
            {
              "type": "svg",
              "name": "flow",
              "say": "Sequence seedhi line hai. Start, statement, statement, end. Koi mod nahi.",
              "caption": "Sequence flow."
            },
            {
              "type": "code",
              "lang": "python",
              "text": "print(\"Enter two numbers\")\na = int(input(\"Enter first number: \"))\nb = int(input(\"Enter second number: \"))\ntotal = a + b\nprint(\"Sum =\", total)",
              "say": "Pehle input, phir doosra input, phir jama, phir print. Upar se neeche."
            },
            {
              "type": "check",
              "q": "Python ka default order kya hai?",
              "a": "Sequence. Upar wali line pehle, neeche wali baad mein.",
              "say": "Python ka default order kya hai? Jawab. Sequence. Upar wali line pehle, neeche wali baad mein."
            }
          ]
        },
        {
          "id": "selection-if",
          "code": "3.5.2",
          "title": "if, elif, aur nested selection",
          "minutes": 10,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Selection condition dekhti hai. True ho to ek raasta, False ho to doosra. Golden topic hai. if aur else ke baad colon zaroori hai, aur andar indentation.",
              "html": "Selection condition dekhti hai. True ho to ek raasta, False ho to doosra. Golden topic hai. if aur else ke baad colon zaroori hai, aur andar indentation."
            },
            {
              "type": "code",
              "lang": "python",
              "text": "age = int(input(\"Enter your age: \"))\nif age >= 18:\n    print(\"You are an Adult.\")\nprint(\"Program continues...\")",
              "say": "Sirf if ho to False pe block skip, lekin us ke baad wali line phir bhi chalti hai."
            },
            {
              "type": "code",
              "lang": "python",
              "text": "if age >= 18:\n    print(\"Apply for CNIC.\")\nelse:\n    print(\"Apply for CRC, B-Form.\")",
              "say": "if else mein dono mein se ek block zaroor chalta hai."
            },
            {
              "type": "code",
              "lang": "python",
              "text": "marks = int(input(\"Enter marks: \"))\nif marks >= 80:\n    print(\"A-1 Grade\")\nelif marks >= 70:\n    print(\"A Grade\")\nelif marks >= 60:\n    print(\"B Grade\")\nelse:\n    print(\"Fail or below B\")",
              "say": "elif upar se neeche check karta hai. Pehli true condition milte hi baqi ignore."
            },
            {
              "type": "p",
              "say": "Nested if ka matlab if ke andar if. Loan ki misaal: pehle age 18 ya zyada, phir salary 30000 ya zyada. Dono pass hon to loan approved. Age kam ho to too young. Age theek ho lekin salary kam ho to salary too low.",
              "html": "Nested if ka matlab if ke andar if. Loan ki misaal: pehle age 18 ya zyada, phir salary 30000 ya zyada. Dono pass hon to loan approved. Age kam ho to too young. Age theek ho lekin salary kam ho to salary too low."
            },
            {
              "type": "check",
              "q": "marks 75 hon to A-1 chalega ya A?",
              "a": "A Grade. 80 se kam hai is liye pehli condition false, 70 wali true, us ke baad kuch nahi chalta.",
              "say": "marks 75 hon to A-1 chalega ya A? Jawab. A Grade. 80 se kam hai is liye pehli condition false, 70 wali true, us ke baad kuch nahi chalta."
            }
          ]
        },
        {
          "id": "loops",
          "code": "3.5.3",
          "title": "for, while, break, aur continue",
          "minutes": 11,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Loop ek block ko baar baar chalata hai taake same lines dobara na likhni parein. Golden topic hai. for tab jab dafa ka pata ho. while tab jab sirf condition pata ho.",
              "html": "Loop ek block ko baar baar chalata hai taake same lines dobara na likhni parein. Golden topic hai. for tab jab dafa ka pata ho. while tab jab sirf condition pata ho."
            },
            {
              "type": "math",
              "tex": "\\mathrm{range}(3) = 0,1,2",
              "say": "range 3 zero se shuru hota hai aur 3 ko shamil nahi karta. Output 0, 1, 2.",
              "display": true
            },
            {
              "type": "table",
              "headers": [
                "range",
                "Output"
              ],
              "rows": [
                [
                  "range(3)",
                  "0 1 2"
                ],
                [
                  "range(2, 5)",
                  "2 3 4"
                ],
                [
                  "range(1, 6, 2)",
                  "1 3 5"
                ],
                [
                  "range(0, 6, 2)",
                  "Even 0 2 4"
                ]
              ],
              "say": "Stop value shamil nahi hoti. Step jump batata hai."
            },
            {
              "type": "code",
              "lang": "python",
              "text": "count = 1\nwhile count <= 3:\n    print(count)\n    count += 1",
              "say": "while tab tak chalti hai jab tak condition true ho. Counter update karna bhool gaye to infinite loop."
            },
            {
              "type": "p",
              "say": "break loop ko foran khatam kar deta hai. continue sirf is dafa ko skip karta hai aur agli iteration pe chala jata hai. range 5 mein i barabar 3 pe break ho to 0 1 2 chhapte hain. continue ho to 0 1 2 4, teen gayab.",
              "html": "break loop ko foran khatam kar deta hai. continue sirf is dafa ko skip karta hai aur agli iteration pe chala jata hai. range 5 mein i barabar 3 pe break ho to 0 1 2 chhapte hain. continue ho to 0 1 2 4, teen gayab."
            },
            {
              "type": "p",
              "say": "Nested loop: andar wali loop, bahar wali ki har dafa pe shuru se akhir tak chalti hai. Bahar 1 aur 2, andar 1 2 3, to total chhe lines.",
              "html": "Nested loop: andar wali loop, bahar wali ki har dafa pe shuru se akhir tak chalti hai. Bahar 1 aur 2, andar 1 2 3, to total chhe lines."
            },
            {
              "type": "table",
              "headers": [
                "for",
                "while"
              ],
              "rows": [
                [
                  "Dafa ka pata hai",
                  "Dafa ka pata nahi, condition hai"
                ],
                [
                  "Counter khud badalta hai",
                  "Counter aap badalte hain"
                ],
                [
                  "Ginti ke kaam mein chhota",
                  "Jab tak user Stop na kahe"
                ]
              ],
              "say": "for known count. while unknown, condition based."
            },
            {
              "type": "code",
              "lang": "python",
              "text": "total = 0.0\nshopping = True\nwhile shopping:\n    item = input(\"Item or done: \")\n    if item.lower() == \"done\":\n        shopping = False\n    else:\n        price = float(input(\"Price: \"))\n        if price > 0:\n            total += price\nif total >= 5000:\n    total = total - total * 0.20",
              "say": "Shopping bill sequence, selection, aur repetition ek sath use karti hai. 5000 ya zyada pe 20 percent discount."
            },
            {
              "type": "check",
              "q": "range(2, 5) kya print karega?",
              "a": "2, 3, aur 4. 5 shamil nahi.",
              "say": "range(2, 5) kya print karega? Jawab. 2, 3, aur 4. 5 shamil nahi."
            }
          ]
        },
        {
          "id": "libraries",
          "code": "3.6",
          "title": "Built-in aur third-party libraries",
          "minutes": 8,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Library pehle se likha hua code hai. Aap har kaam zero se nahi likhte. Import ke paanch tareeqe hain.",
              "html": "Library pehle se likha hua code hai. Aap har kaam zero se nahi likhte. Import ke paanch tareeqe hain."
            },
            {
              "type": "code",
              "lang": "python",
              "text": "import math\nprint(math.sqrt(25))\nimport math as m\nprint(m.sqrt(16))\nfrom math import sqrt, pi\nprint(sqrt(36))",
              "say": "Poora module import karo to naam dot function. Alias chhota naam. Specific function seedha."
            },
            {
              "type": "tip",
              "say": "Star se sab import karna, from math import star, memory aur clarity dono ke liye kamzor hai. Jo chahiye sirf woh import karein."
            },
            {
              "type": "p",
              "say": "math ke sath pi, ceil jo upar round karta hai, floor jo neeche, pow, aur sqrt. random.randint(1, 10) ek integer. random.random zero aur one ke beech float. datetime.datetime.now abhi ka waqt. strftime percent d dash percent m dash percent Y din mahina saal.",
              "html": "math ke sath pi, ceil jo upar round karta hai, floor jo neeche, pow, aur sqrt. random.randint(1, 10) ek integer. random.random zero aur one ke beech float. datetime.datetime.now abhi ka waqt. strftime percent d dash percent m dash percent Y din mahina saal."
            },
            {
              "type": "table",
              "headers": [
                "Library",
                "Kaam",
                "Install"
              ],
              "rows": [
                [
                  "math, random, datetime",
                  "Hisab, random, tareekh",
                  "Python ke sath built-in"
                ],
                [
                  "NumPy",
                  "Bari arrays",
                  "pip install numpy"
                ],
                [
                  "Pandas",
                  "Table data, Excel CSV",
                  "pip install pandas"
                ],
                [
                  "Matplotlib",
                  "Graphs",
                  "pip install matplotlib"
                ],
                [
                  "TensorFlow, PyTorch",
                  "AI",
                  "pip install"
                ]
              ],
              "say": "Built-in sirf import. Third party pehle pip install."
            },
            {
              "type": "check",
              "q": "math.ceil(4.3) kya dega?",
              "a": "5. Ceil hamesha upar round karta hai.",
              "say": "math.ceil(4.3) kya dega? Jawab. 5. Ceil hamesha upar round karta hai."
            }
          ]
        },
        {
          "id": "debugging",
          "code": "3.7",
          "title": "Syntax, runtime, aur logical errors",
          "minutes": 8,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Debugging ka matlab bug dhoondhna, trace karna, aur theek karna taake program sahi kaam kare.",
              "html": "Debugging ka matlab bug dhoondhna, trace karna, aur theek karna taake program sahi kaam kare."
            },
            {
              "type": "table",
              "headers": [
                "Error",
                "Kab pata chalta hai",
                "Misal"
              ],
              "rows": [
                [
                  "Syntax",
                  "Chalta hi nahi, grammar toot gaya",
                  "print(\"Hello\"  — bracket kam"
                ],
                [
                  "Runtime",
                  "Chalna shuru, beech mein crash",
                  "10 / 0 ZeroDivisionError"
                ],
                [
                  "Logical",
                  "Crash nahi, jawab galat",
                  "area = length + width, zarb honi chahiye"
                ]
              ],
              "say": "Syntax grammar. Runtime crash. Logical galat formula jo chupke galat jawab de."
            },
            {
              "type": "code",
              "lang": "text",
              "text": "Traceback (most recent call last):\n  File \"debug_program.py\", line 1\n    x = int(\"abc\")\nValueError: invalid literal for int() with base 10: 'abc'",
              "say": "Traceback teen baatein kehta hai: error ki qisam, file, aur line number. Yahan line 1 pe abc ko int banana ValueError hai."
            },
            {
              "type": "tip",
              "say": "Logical error sab se khatarnak is liye hai ke program khush ho kar galat jawab de deta hai. Trace table se expected aur actual compare karein."
            },
            {
              "type": "check",
              "q": "Program chalta hai lekin area galat nikalta hai. Yeh kaun si error hai?",
              "a": "Logical error. Grammar theek hai, crash nahi, soch galat hai.",
              "say": "Program chalta hai lekin area galat nikalta hai. Yeh kaun si error hai? Jawab. Logical error. Grammar theek hai, crash nahi, soch galat hai."
            }
          ]
        }
      ]
    },
    {
      "id": "ch4",
      "num": "04",
      "title": "Data and Analysis",
      "blurb": "Database, keys, ER model, referential integrity, aur MS Access.",
      "lectures": [
        {
          "id": "data-info",
          "code": "4.1.1",
          "title": "Data, information, aur database",
          "minutes": 7,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Data kachcha fact hai. Numbers 80, 75, 90, 70, 85 data hain. Parking mein caron ke rang bhi data hain. Jab inhein process karke matlab nikalte hain to information banti hai. Misal: class ka average 80 percent hai. Information faisla karne mein madad karti hai.",
              "html": "Data kachcha fact hai. Numbers 80, 75, 90, 70, 85 data hain. Parking mein caron ke rang bhi data hain. Jab inhein process karke matlab nikalte hain to information banti hai. Misal: class ka average 80 percent hai. Information faisla karne mein madad karti hai."
            },
            {
              "type": "table",
              "headers": [
                "",
                "Data",
                "Information"
              ],
              "rows": [
                [
                  "Definition",
                  "Raw facts",
                  "Processed, meaningful"
                ],
                [
                  "Misal",
                  "85, 90, 75",
                  "Average marks 83.3 percent"
                ],
                [
                  "Faida",
                  "Akela kam useful",
                  "Decision ke kaam ka"
                ]
              ],
              "say": "Data kachcha hai. Information us ka matlab hai."
            },
            {
              "type": "p",
              "say": "Database related data ka organised collection hai, taake dhoondhna, badalna, aur update karna asaan ho. Purane files aur registers mein search mushkil thi. Database woh mushkil hal karta hai.",
              "html": "Database related data ka organised collection hai, taake dhoondhna, badalna, aur update karna asaan ho. Purane files aur registers mein search mushkil thi. Database woh mushkil hal karta hai."
            },
            {
              "type": "check",
              "q": "85, 90, 75 data hai ya information?",
              "a": "Data. Average nikal jaye to woh information ban jati hai.",
              "say": "85, 90, 75 data hai ya information? Jawab. Data. Average nikal jaye to woh information ban jati hai."
            }
          ]
        },
        {
          "id": "dbms",
          "code": "4.1.2",
          "title": "Database Management System",
          "minutes": 7,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "DBMS woh software hai jis se user database banata, sambhalta, aur use karta hai. User files se seedha nahi ladta. DBMS beech mein pul hai. MySQL aur Oracle DBMS ki misaal hain.",
              "html": "DBMS woh software hai jis se user database banata, sambhalta, aur use karta hai. User files se seedha nahi ladta. DBMS beech mein pul hai. MySQL aur Oracle DBMS ki misaal hain."
            },
            {
              "type": "steps",
              "title": "DBMS ke faide",
              "items": [
                "Redundancy kam: department ka naam har student row mein dobara nahi.",
                "Consistency: phone number ek jagah badla to sab ko naya number mile.",
                "Security: admin marks dekhe, staff sirf naam.",
                "Integrity: do students ka same roll number na ho."
              ],
              "say": "Kam dohrav, ek jaisa data, ijazat, aur sahi data."
            },
            {
              "type": "check",
              "q": "DBMS user aur database ke beech kya hai?",
              "a": "Pul. User DBMS se baat karta hai, files se seedha nahi.",
              "say": "DBMS user aur database ke beech kya hai? Jawab. Pul. User DBMS se baat karta hai, files se seedha nahi."
            }
          ]
        },
        {
          "id": "components",
          "code": "4.2",
          "title": "Table, record, aur field",
          "minutes": 6,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Table rows aur columns mein data rakhti hai, spreadsheet ki tarah. Har table ek entity ke baare mein hoti hai, jaise Students ya Teachers.",
              "html": "Table rows aur columns mein data rakhti hai, spreadsheet ki tarah. Har table ek entity ke baare mein hoti hai, jaise Students ya Teachers."
            },
            {
              "type": "table",
              "headers": [
                "Roll No",
                "Name",
                "Course",
                "Grade"
              ],
              "rows": [
                [
                  "101",
                  "Ali",
                  "CS",
                  "A"
                ],
                [
                  "102",
                  "Sara",
                  "IT",
                  "B+"
                ],
                [
                  "103",
                  "Ahmed",
                  "CS",
                  "A"
                ]
              ],
              "say": "Ek poori row record hai, jaise Ali ki tamam maloomat. Ek column field hai, jaise sirf names."
            },
            {
              "type": "p",
              "say": "Record ek instance ki poori kahani hai. Field ek hi qisam ki maloomat hai. Roll number column field hai. Ali ki poori line record hai.",
              "html": "Record ek instance ki poori kahani hai. Field ek hi qisam ki maloomat hai. Roll number column field hai. Ali ki poori line record hai."
            },
            {
              "type": "check",
              "q": "Sirf names wala column record hai ya field?",
              "a": "Field. Record poori row hoti hai.",
              "say": "Sirf names wala column record hai ya field? Jawab. Field. Record poori row hoti hai."
            }
          ]
        },
        {
          "id": "keys",
          "code": "4.3.1",
          "title": "Keys aur integrity",
          "minutes": 10,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Key woh field hai jo record ko unique banaye aur tables ko jode. Golden topic hai. Candidate key koi bhi aisi field, ya fields ka set, hai jo record alag pehchan sake. Ek table mein kai candidate keys ho sakti hain. Null allowed nahi, duplicate allowed nahi.",
              "html": "Key woh field hai jo record ko unique banaye aur tables ko jode. Golden topic hai. Candidate key koi bhi aisi field, ya fields ka set, hai jo record alag pehchan sake. Ek table mein kai candidate keys ho sakti hain. Null allowed nahi, duplicate allowed nahi."
            },
            {
              "type": "svg",
              "name": "keys",
              "say": "EmpID, license, aur passport teeno candidate hain. School jaisa, hum EmpID ko primary chun lete hain. Baqi alternate ban jati hain.",
              "caption": "Candidate, primary, alternate."
            },
            {
              "type": "p",
              "say": "Primary key un candidate keys mein se woh ek hai jo hum chun lein. Har table ki sirf ek primary key. Unique, aur null nahi. Classroom mein roll number, B-form, aur phone teeno candidate ho sakte hain. School roll number ko primary bana deta hai.",
              "html": "Primary key un candidate keys mein se woh ek hai jo hum chun lein. Har table ki sirf ek primary key. Unique, aur null nahi. Classroom mein roll number, B-form, aur phone teeno candidate ho sakte hain. School roll number ko primary bana deta hai."
            },
            {
              "type": "p",
              "say": "Jo candidate keys primary nahi bani, woh alternate keys hain. License aur passport alternate reh jate hain. Woh ab bhi unique hain.",
              "html": "Jo candidate keys primary nahi bani, woh alternate keys hain. License aur passport alternate reh jate hain. Woh ab bhi unique hain."
            },
            {
              "type": "p",
              "say": "Foreign key doosri table ki primary key ki taraf ishara karti hai. Employee table ka DeptID, Department table ke DeptID se judta hai. Foreign key duplicate ho sakti hai, kyunke kai employees ek department mein ho sakte hain. Kabhi kabhi null bhi ho sakti hai.",
              "html": "Foreign key doosri table ki primary key ki taraf ishara karti hai. Employee table ka DeptID, Department table ke DeptID se judta hai. Foreign key duplicate ho sakti hai, kyunke kai employees ek department mein ho sakte hain. Kabhi kabhi null bhi ho sakti hai."
            },
            {
              "type": "check",
              "q": "Primary key null ho sakti hai?",
              "a": "Nahi. Na duplicate, na null. Aur ek table mein sirf ek primary key.",
              "say": "Primary key null ho sakti hai? Jawab. Nahi. Na duplicate, na null. Aur ek table mein sirf ek primary key."
            }
          ]
        },
        {
          "id": "rdbms",
          "code": "4.3",
          "title": "Relational database",
          "minutes": 6,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "RDBMS data ko kai tables mein rakhta hai aur primary aur foreign keys se unhein jodta hai. Banks aur universities isi structure pe chalte hain.",
              "html": "RDBMS data ko kai tables mein rakhta hai aur primary aur foreign keys se unhein jodta hai. Banks aur universities isi structure pe chalte hain."
            },
            {
              "type": "steps",
              "title": "RDBMS kyun",
              "items": [
                "Dohrana data kam ho jata hai.",
                "Kai users security ke sath kaam kar sakte hain.",
                "SQL se sawal poochna asaan hai."
              ],
              "say": "Kam redundancy, multi user, aur SQL."
            },
            {
              "type": "p",
              "say": "SQL ka matlab Structured Query Language hai. Table se specific rows nikalne ka tareeqa yahi hai.",
              "html": "SQL ka matlab Structured Query Language hai. Table se specific rows nikalne ka tareeqa yahi hai."
            },
            {
              "type": "check",
              "q": "RDBMS tables ko kis cheez se jodta hai?",
              "a": "Keys se, khas tor pe primary aur foreign key.",
              "say": "RDBMS tables ko kis cheez se jodta hai? Jawab. Keys se, khas tor pe primary aur foreign key."
            }
          ]
        },
        {
          "id": "er-model",
          "code": "4.4",
          "title": "Entity relationship model",
          "minutes": 9,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "ER model database banane se pehle ka naqsha hai. Architect ka blueprint. Golden topic hai. Teen cheezein: entity, attribute, relationship.",
              "html": "ER model database banane se pehle ka naqsha hai. Architect ka blueprint. Golden topic hai. Teen cheezein: entity, attribute, relationship."
            },
            {
              "type": "svg",
              "name": "er",
              "say": "Rectangle entity hai, jaise STUDENT. Oval attribute hai, jaise Name. Diamond relationship hai, jaise Enrolls. Primary key attribute ke neeche line hoti hai.",
              "caption": "ER symbols."
            },
            {
              "type": "table",
              "headers": [
                "Relationship",
                "Matlab",
                "Misal"
              ],
              "rows": [
                [
                  "One to one",
                  "Ek record sirf ek se juda",
                  "Ek student ki ek ID card"
                ],
                [
                  "One to many",
                  "Ek record kai se juda. Sab se common",
                  "Ek teacher, kai students"
                ],
                [
                  "Many to many",
                  "Dono taraf kai",
                  "Kai students, kai classes"
                ]
              ],
              "say": "1:1 rare hai. 1:M common hai. M:N ko seedha nahi rakhte."
            },
            {
              "type": "tip",
              "say": "Relational database many to many seedha nahi sambhalta. Dono taraf dohrav ho jata hai. Beech mein junction table rakho, jaise Enrollment, taake do one-to-many ban jayen."
            },
            {
              "type": "check",
              "q": "ER diagram mein diamond kya dikhata hai?",
              "a": "Relationship. Rectangle entity hai, oval attribute.",
              "say": "ER diagram mein diamond kya dikhata hai? Jawab. Relationship. Rectangle entity hai, oval attribute."
            }
          ]
        },
        {
          "id": "referential",
          "code": "4.5",
          "title": "Referential integrity, cascade update aur delete",
          "minutes": 8,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Referential integrity ka matlab hai foreign key hamesha kisi maujooda primary key ki taraf ishara kare. Orphan record nahi banne deti. Golden topic hai.",
              "html": "Referential integrity ka matlab hai foreign key hamesha kisi maujooda primary key ki taraf ishara kare. Orphan record nahi banne deti. Golden topic hai."
            },
            {
              "type": "svg",
              "name": "integrity",
              "say": "Student parent mein 101 Ali aur 102 Sara hain. Result child mein 101 allowed hai. 999 reject, kyunke parent mein 999 hai hi nahi.",
              "caption": "Parent rejects an orphan foreign key."
            },
            {
              "type": "p",
              "say": "Agar integrity on ho to aap student 999 ka result nahi daal sakte jab 999 student table mein na ho. Aur aap us student ko delete nahi kar sakte jis ke marks ab bhi result table mein hon, jab tak related rows ka faisla na ho.",
              "html": "Agar integrity on ho to aap student 999 ka result nahi daal sakte jab 999 student table mein na ho. Aur aap us student ko delete nahi kar sakte jis ke marks ab bhi result table mein hon, jab tak related rows ka faisla na ho."
            },
            {
              "type": "steps",
              "title": "Do automatic operations",
              "items": [
                "Cascade update: parent ki primary key badle to child ki foreign key bhi badal jaye. Ali ka 101, 201 ho jaye to enrollment mein bhi 201.",
                "Cascade delete: parent ki row delete ho to child ki related rows bhi delete. Sara school chhor de to us ke enrollments aur results bhi mit jayen."
              ],
              "say": "Cascade update id sath badalta hai. Cascade delete bacchon ko bhi mita deta hai."
            },
            {
              "type": "check",
              "q": "999 parent mein nahi aur child mein aa jaye. Isay kya kehte hain?",
              "a": "Orphan record. Referential integrity isay reject karti hai.",
              "say": "999 parent mein nahi aur child mein aa jaye. Isay kya kehte hain? Jawab. Orphan record. Referential integrity isay reject karti hai."
            }
          ]
        },
        {
          "id": "schema",
          "code": "4.6",
          "title": "Relational schema",
          "minutes": 6,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Relational schema database ka formal naqsha hai, software mein banane se pehle. Yeh batata hai tables kaun si hain, fields kya hain, primary aur foreign keys kaun si hain, aur tables kaise judi hain.",
              "html": "Relational schema database ka formal naqsha hai, software mein banane se pehle. Yeh batata hai tables kaun si hain, fields kya hain, primary aur foreign keys kaun si hain, aur tables kaise judi hain."
            },
            {
              "type": "steps",
              "title": "Schema kyun pehle",
              "items": [
                "Dohrav pehle hi kam ho jata hai.",
                "Keys pehle plan hon to integrity behtar.",
                "Baad mein barhana asaan."
              ],
              "say": "Bina naqshe ke ghar jaisa. Schema skip karoge to database messy hogi."
            },
            {
              "type": "tip",
              "say": "Ghar bina architect ke drawing ke mat banao. Database bina schema ke mat banao."
            },
            {
              "type": "check",
              "q": "Schema asal data store karta hai ya structure describe karta hai?",
              "a": "Structure describe karta hai. Data baad mein tables mein jata hai.",
              "say": "Schema asal data store karta hai ya structure describe karta hai? Jawab. Structure describe karta hai. Data baad mein tables mein jata hai."
            }
          ]
        },
        {
          "id": "library-case",
          "code": "4.7",
          "title": "Library case study",
          "minutes": 9,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "College library ka ER schema step by step. Book ki id, title, author, publisher. Member ki id, name, contact. Member kai books le sakta hai, aur ek book waqt ke sath kai members le sakte hain. Issue date aur return date record hone chahiye.",
              "html": "College library ka ER schema step by step. Book ki id, title, author, publisher. Member ki id, name, contact. Member kai books le sakta hai, aur ek book waqt ke sath kai members le sakte hain. Issue date aur return date record hone chahiye."
            },
            {
              "type": "steps",
              "title": "Saat steps",
              "items": [
                "Requirements likho.",
                "Entities: Book aur Member.",
                "Attributes: BookID primary, MemberID primary.",
                "Relationship: member borrows book.",
                "Cardinality many to many.",
                "Junction entity BorrowRecord se M:N tod do.",
                "Final: Member one to many BorrowRecord, Book one to many BorrowRecord."
              ],
              "say": "Do entities, many to many, phir BorrowRecord beech mein."
            },
            {
              "type": "svg",
              "name": "library",
              "say": "Member ek taraf, Book doosri taraf, beech BorrowRecord. Dono relationships one to many hain junction ki taraf.",
              "caption": "Resolved library schema."
            },
            {
              "type": "p",
              "say": "BorrowRecord ke attributes: BorrowID primary, MemberID foreign, BookID foreign, IssueDate, ReturnDate. Ab ek borrowing ek alag row hai. Dohrana data nahi.",
              "html": "BorrowRecord ke attributes: BorrowID primary, MemberID foreign, BookID foreign, IssueDate, ReturnDate. Ab ek borrowing ek alag row hai. Dohrana data nahi."
            },
            {
              "type": "check",
              "q": "Member aur Book ki many to many ko kaun si table todti hai?",
              "a": "BorrowRecord, junction table.",
              "say": "Member aur Book ki many to many ko kaun si table todti hai? Jawab. BorrowRecord, junction table."
            }
          ]
        },
        {
          "id": "objects",
          "code": "4.8",
          "title": "Tables, forms, queries, reports",
          "minutes": 7,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Access jaise DBMS mein char bade objects hain. Table asal data rakhti hai. Form user ko saaf screen deta hai enter aur edit ke liye. Query sawal hai: mujhe woh students dikhao jin ke marks 80 se upar hain. Report print ya share karne ki sajawat hai, aksar query ke result pe.",
              "html": "Access jaise DBMS mein char bade objects hain. Table asal data rakhti hai. Form user ko saaf screen deta hai enter aur edit ke liye. Query sawal hai: mujhe woh students dikhao jin ke marks 80 se upar hain. Report print ya share karne ki sajawat hai, aksar query ke result pe."
            },
            {
              "type": "table",
              "headers": [
                "Object",
                "Kaam"
              ],
              "rows": [
                [
                  "Table",
                  "Data store, rows aur columns"
                ],
                [
                  "Form",
                  "Data enter, edit, dekhna, galti kam"
                ],
                [
                  "Query",
                  "Specific data nikalna, filter"
                ],
                [
                  "Report",
                  "Khubsurat output, print"
                ]
              ],
              "say": "Table store, form enter, query poochho, report dikhao."
            },
            {
              "type": "p",
              "say": "Query table ko badalta nahi. Sirf poochta hai. Is liye analysis ke liye safe hai.",
              "html": "Query table ko badalta nahi. Sirf poochta hai. Is liye analysis ke liye safe hai."
            },
            {
              "type": "check",
              "q": "Data asal kis object mein rehta hai?",
              "a": "Table mein. Form aur report us data ko dikhate hain.",
              "say": "Data asal kis object mein rehta hai? Jawab. Table mein. Form aur report us data ko dikhate hain."
            }
          ]
        },
        {
          "id": "access-tables",
          "code": "4.9",
          "title": "MS Access mein table banana",
          "minutes": 7,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Table banana database ka pehla asal kaam hai. Pehle plan: kaun se fields, kaun sa data type, kaun si primary key, kaun se rules. Galat type baad mein query ko slow aur data ko ghalat kar deta hai.",
              "html": "Table banana database ka pehla asal kaam hai. Pehle plan: kaun se fields, kaun sa data type, kaun si primary key, kaun se rules. Galat type baad mein query ko slow aur data ko ghalat kar deta hai."
            },
            {
              "type": "steps",
              "title": "Design View",
              "items": [
                "Create, phir Table Design.",
                "Field name likho, data type chuno: Short Text, Number, Date, Yes/No, AutoNumber.",
                "Neeche field properties: field size, format, required, validation rule.",
                "Primary key select karke key icon dabao.",
                "Save karo, table ka naam do. Tab data enter karo."
              ],
              "say": "Design view pehle structure, phir data. Professional tareeqa yahi hai."
            },
            {
              "type": "tip",
              "say": "Datasheet view jaldi hoti hai lekin types khud guess karti hai. Exam mein Design View likhna, kyunke wahan control poora hota hai."
            },
            {
              "type": "check",
              "q": "Primary key Access mein kahan set hoti hai?",
              "a": "Design View mein field select karke key icon se.",
              "say": "Primary key Access mein kahan set hoti hai? Jawab. Design View mein field select karke key icon se."
            }
          ]
        },
        {
          "id": "forms",
          "code": "4.10",
          "title": "Forms se data enter karna",
          "minutes": 6,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Form table ki jagah ek record ek screen pe dikhata hai. Galti kam hoti hai, validation nazar aati hai, aur user ko columns ka jungle nahi milta.",
              "html": "Form table ki jagah ek record ek screen pe dikhata hai. Galti kam hoti hai, validation nazar aati hai, aur user ko columns ka jungle nahi milta."
            },
            {
              "type": "steps",
              "title": "Form ka data source",
              "items": [
                "Har form kisi table ya query se juda hona chahiye. Bina source ke form kahan save kare?",
                "Form wizard se table chuno, fields chuno, layout chuno.",
                "Design view mein label saaf karo aur required fields nazar pe rakho."
              ],
              "say": "Form ka source table ya query hota hai. Wizard se shuru karo."
            },
            {
              "type": "check",
              "q": "Form data khud store karta hai?",
              "a": "Nahi. Form table ya query ka interface hai. Data table mein rehta hai.",
              "say": "Form data khud store karta hai? Jawab. Nahi. Form table ya query ka interface hai. Data table mein rehta hai."
            }
          ]
        },
        {
          "id": "queries",
          "code": "4.11",
          "title": "MS Access queries",
          "minutes": 8,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Query Access ki sab se taqatwar cheez hai. Data nikalti, filter karti, aur analyse karti hai, asal table ko badle baghair. Golden topic hai.",
              "html": "Query Access ki sab se taqatwar cheez hai. Data nikalti, filter karti, aur analyse karti hai, asal table ko badle baghair. Golden topic hai."
            },
            {
              "type": "steps",
              "title": "Simple select query",
              "items": [
                "Create, Query Design.",
                "Table add karo, jaise Students.",
                "Fields neeche grid mein kheench lo: Name, Department, Marks.",
                "Criteria row mein rule likho. Department ke neeche Computer Science.",
                "Run. Sirf wohi rows aayengi."
              ],
              "say": "Design grid mein fields upar, criteria neeche. Computer Science sirf us department ki rows rakhega."
            },
            {
              "type": "code",
              "lang": "sql",
              "text": "SELECT Name, Department, Marks\nFROM Students\nWHERE Department = \"Computer Science\";",
              "say": "Yahi baat SQL mein. Criteria row WHERE ban jati hai."
            },
            {
              "type": "p",
              "say": "Criteria khali ho to saari rows aati hain. Text criteria quotes mein. Number bina quotes. Ek se zyada columns pe criteria AND ki tarah judte hain.",
              "html": "Criteria khali ho to saari rows aati hain. Text criteria quotes mein. Number bina quotes. Ek se zyada columns pe criteria AND ki tarah judte hain."
            },
            {
              "type": "check",
              "q": "Query chalane se table ka asal data badalta hai?",
              "a": "Nahi. Select query sirf dikhati hai.",
              "say": "Query chalane se table ka asal data badalta hai? Jawab. Nahi. Select query sirf dikhati hai."
            }
          ]
        },
        {
          "id": "totals",
          "code": "4.11.4",
          "title": "Grouping aur statistics",
          "minutes": 6,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Grouping milti julti rows ko jod kar total nikalti hai. Misal: department ke hisaab se students ki tadad, ya average marks.",
              "html": "Grouping milti julti rows ko jod kar total nikalti hai. Misal: department ke hisaab se students ki tadad, ya average marks."
            },
            {
              "type": "steps",
              "title": "Totals row",
              "items": [
                "Query design mein Totals button dabao. Grid mein Total row aa jati hai.",
                "Department pe Group By rakho.",
                "Marks pe Avg chuno, ya Count, Sum, Min, Max.",
                "Run. Har department ki ek line aayegi."
              ],
              "say": "Group By department, phir Avg marks. Ek group, ek number."
            },
            {
              "type": "table",
              "headers": [
                "Total option",
                "Kaam"
              ],
              "rows": [
                [
                  "Group By",
                  "Milti values ikatthi"
                ],
                [
                  "Count",
                  "Rows ginna"
                ],
                [
                  "Sum",
                  "Jama"
                ],
                [
                  "Avg",
                  "Average"
                ],
                [
                  "Min / Max",
                  "Sab se chhota ya bara"
                ]
              ],
              "say": "Group By ke sath Count, Sum, Avg, Min, Max."
            },
            {
              "type": "check",
              "q": "Har department ka average marks chahiye. Department pe kya hoga?",
              "a": "Group By. Marks pe Avg.",
              "say": "Har department ka average marks chahiye. Department pe kya hoga? Jawab. Group By. Marks pe Avg."
            }
          ]
        },
        {
          "id": "charts",
          "code": "4.11.6",
          "title": "Charts se data dikhana",
          "minutes": 6,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Visualization numbers ko shakal deta hai taake pattern ek nazar mein dikhe.",
              "html": "Visualization numbers ko shakal deta hai taake pattern ek nazar mein dikhe."
            },
            {
              "type": "svg",
              "name": "bars",
              "say": "Bar chart categories compare karti hai. Lamba bar bara number.",
              "caption": "Bar chart of categories."
            },
            {
              "type": "svg",
              "name": "pie",
              "say": "Pie chart hisse dikhati hai, poore ka percent. Pass aur needs-help jaisa.",
              "caption": "Pie chart of a whole."
            },
            {
              "type": "table",
              "headers": [
                "Chart",
                "Kab"
              ],
              "rows": [
                [
                  "Bar",
                  "Categories ka muqabla, jaise departments"
                ],
                [
                  "Column",
                  "Wahi muqabla, khadi bars"
                ],
                [
                  "Line",
                  "Waqt ke sath trend"
                ],
                [
                  "Pie",
                  "Poore ke hisse, percent"
                ]
              ],
              "say": "Bar muqabla, line trend, pie hissa."
            },
            {
              "type": "tip",
              "say": "Pie tab jab hisse mila kar poora banen. Bahut zyada slices pie ko bekar kar deti hain. Us waqt bar behtar hai."
            },
            {
              "type": "check",
              "q": "Mahine ke sath marks ka trend kaun sa chart?",
              "a": "Line chart.",
              "say": "Mahine ke sath marks ka trend kaun sa chart? Jawab. Line chart."
            }
          ]
        }
      ]
    },
    {
      "id": "ch5",
      "num": "05",
      "title": "Impacts of Computing",
      "blurb": "AI, IoT, data analytics, sources, aur assistive technology.",
      "lectures": [
        {
          "id": "computing-ai",
          "code": "5.1 – 5.1.1",
          "title": "Computing aur artificial intelligence",
          "minutes": 8,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Computing ab roz ki zindagi hai. Pakistan mein school, hospital, bank, khet, aur factory sab mein computer aa rahe hain. Phone aur internet bhi isi daire mein hain.",
              "html": "Computing ab roz ki zindagi hai. Pakistan mein school, hospital, bank, khet, aur factory sab mein computer aa rahe hain. Phone aur internet bhi isi daire mein hain."
            },
            {
              "type": "p",
              "say": "AI is liye artificial hai ke insaan ne banaya, aur intelligence is liye ke woh aisa kaam kare jis mein soch chahiye. AI data se faisla karta hai. Golden topic hai.",
              "html": "AI is liye artificial hai ke insaan ne banaya, aur intelligence is liye ke woh aisa kaam kare jis mein soch chahiye. AI data se faisla karta hai. Golden topic hai."
            },
            {
              "type": "steps",
              "title": "Aas paas ki misaal",
              "items": [
                "Phone ka face unlock.",
                "YouTube jo aap ki pasand ki videos dikhaye.",
                "Website ka chatbot.",
                "Garm kamre mein sensor data dekh kar AC on kar dena."
              ],
              "say": "Face, recommendation, chatbot, aur AC ka faisla. AI system ka dimagh hai."
            },
            {
              "type": "p",
              "say": "IoT aankhein hain, data ikattha karti hain. Analytics us data ko saaf karta hai. AI faisla karta hai. Phir actuator action leta hai.",
              "html": "IoT aankhein hain, data ikattha karti hain. Analytics us data ko saaf karta hai. AI faisla karta hai. Phir actuator action leta hai."
            },
            {
              "type": "check",
              "q": "AI ko system ka dimagh kyun kehte hain?",
              "a": "Kyunke sensor data aane ke baad faisla AI karta hai, jaise AC on karna.",
              "say": "AI ko system ka dimagh kyun kehte hain? Jawab. Kyunke sensor data aane ke baad faisla AI karta hai, jaise AC on karna."
            }
          ]
        },
        {
          "id": "iot",
          "code": "5.1.2",
          "title": "Internet of Things aur us ke components",
          "minutes": 9,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "IoT woh system hai jismein physical devices internet se jud kar data ikattha karte aur share karte hain, aur kaam khud ho jata hai. Smartwatch heart rate phone pe bhej de. Golden topic hai.",
              "html": "IoT woh system hai jismein physical devices internet se jud kar data ikattha karte aur share karte hain, aur kaam khud ho jata hai. Smartwatch heart rate phone pe bhej de. Golden topic hai."
            },
            {
              "type": "svg",
              "name": "iot",
              "say": "Sensor collect karta hai, Wi-Fi le jati hai, cloud process karta hai, AI faisla karta hai, actuator kaam karta hai.",
              "caption": "IoT path from sensor to action."
            },
            {
              "type": "table",
              "headers": [
                "Component",
                "Kaam",
                "Misal"
              ],
              "rows": [
                [
                  "Sensor",
                  "Dunya se data, aankh kaan",
                  "Temperature, motion, fingerprint, soil"
                ],
                [
                  "Actuator",
                  "Digital ishare ko jismani kaam",
                  "Motor, door, valve, fan"
                ],
                [
                  "Connectivity",
                  "Bina iske device behera hai",
                  "Wi-Fi, Bluetooth, ZigBee, 4G, 5G"
                ],
                [
                  "Processing",
                  "Kachche data se faisla",
                  "Kamra garam hai to AC"
                ],
                [
                  "Cloud",
                  "Bara data door store aur service",
                  "Google Drive, online LMS"
                ],
                [
                  "User interface",
                  "Insaan dekhe aur hukum de",
                  "App, touch screen, voice"
                ]
              ],
              "say": "Chhe hisse: sensor, actuator, connectivity, processing, cloud, interface."
            },
            {
              "type": "check",
              "q": "Sensor aur actuator mein farq?",
              "a": "Sensor data leta hai. Actuator kaam karta hai, jaise pump ya motor.",
              "say": "Sensor aur actuator mein farq? Jawab. Sensor data leta hai. Actuator kaam karta hai, jaise pump ya motor."
            }
          ]
        },
        {
          "id": "analytics",
          "code": "5.1.3",
          "title": "Data analytics ke paanch hisse",
          "minutes": 7,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Data analytics data ko ikattha, saaf, study, aur present karta hai taake behtar faisla ho. College marks ikattha kare, percent nikale, aur dekhe kin students ko extra help chahiye. Yeh poora amal analytics hai.",
              "html": "Data analytics data ko ikattha, saaf, study, aur present karta hai taake behtar faisla ho. College marks ikattha kare, percent nikale, aur dekhe kin students ko extra help chahiye. Yeh poora amal analytics hai."
            },
            {
              "type": "steps",
              "title": "Paanch components",
              "items": [
                "Collection: websites, surveys, sensors, hospital, bank.",
                "Storage: file, database, spreadsheet, cloud.",
                "Cleaning: duplicate, typo, missing, galat format hatao.",
                "Analysis: pattern. Kaun se subject mein fail zyada.",
                "Visualization: chart, jaise pass aur fail ka pie."
              ],
              "say": "Collect, store, clean, analyse, phir chart."
            },
            {
              "type": "svg",
              "name": "pie",
              "say": "Pie chart pass aur needs-help ka hissa ek nazar mein dikha deta hai.",
              "caption": "Pass versus needs help."
            },
            {
              "type": "check",
              "q": "Duplicate rows kis step mein hat-ti hain?",
              "a": "Data cleaning.",
              "say": "Duplicate rows kis step mein hat-ti hain? Jawab. Data cleaning."
            }
          ]
        },
        {
          "id": "compare-three",
          "code": "5.1",
          "title": "IoT, AI, aur analytics ka muqabla",
          "minutes": 6,
          "golden": false,
          "blocks": [
            {
              "type": "table",
              "headers": [
                "",
                "IoT",
                "AI",
                "Data analytics"
              ],
              "rows": [
                [
                  "Definition",
                  "Devices internet pe",
                  "Machine sochay aur faisla kare",
                  "Data se pattern"
                ],
                [
                  "Purpose",
                  "Data aur automation",
                  "Smart decision",
                  "Insight"
                ],
                [
                  "Kaam",
                  "Hardware devices",
                  "Smart software",
                  "Numbers aur records"
                ],
                [
                  "Output",
                  "Environment ka raw data",
                  "Faisla ya action",
                  "Report aur graph"
                ]
              ],
              "say": "IoT jism hai, AI dimagh, analytics samajh. Teeno mil kar smart system bante hain."
            },
            {
              "type": "p",
              "say": "Khet ki misaal: soil sensor IoT hai. Numbers saaf karke dekhna analytics hai. Pani chahiye ya nahi, yeh faisla AI kare to pump chal jati hai.",
              "html": "Khet ki misaal: soil sensor IoT hai. Numbers saaf karke dekhna analytics hai. Pani chahiye ya nahi, yeh faisla AI kare to pump chal jati hai."
            },
            {
              "type": "check",
              "q": "Report aur graph kis ka output hai?",
              "a": "Data analytics ka.",
              "say": "Report aur graph kis ka output hai? Jawab. Data analytics ka."
            }
          ]
        },
        {
          "id": "iot-uses",
          "code": "5.2",
          "title": "IoT shehron, sehat, aur kheton mein",
          "minutes": 8,
          "golden": false,
          "blocks": [
            {
              "type": "table",
              "headers": [
                "Jagah",
                "Kaam"
              ],
              "rows": [
                [
                  "Smart city",
                  "Signal, lights, parking, kachre ka dabba jab bhar jaye"
                ],
                [
                  "Factory",
                  "Machine ki garmi aur vibration, Sindh textile quality"
                ],
                [
                  "Health",
                  "Smartwatch, dehaat se doctor tak data, emergency alert"
                ],
                [
                  "School",
                  "Digital board, biometric attendance, AC"
                ],
                [
                  "Ghar",
                  "Light app se, camera, voice assistant"
                ],
                [
                  "Kheti",
                  "Soil moisture, pump on off, drone se fasal"
                ]
              ],
              "say": "Sheher, factory, sehat, school, ghar, aur khet. Pakistan mein paani bachane ke liye smart farming khas hai."
            },
            {
              "type": "p",
              "say": "Smart farming ka flow: soil sensor, cloud, sawal ke paani chahiye, phir water pump. Sindh aur Punjab dono mein paani mehnga aur kam hai, is liye yeh misaal syllabus mein zaroori hai.",
              "html": "Smart farming ka flow: soil sensor, cloud, sawal ke paani chahiye, phir water pump. Sindh aur Punjab dono mein paani mehnga aur kam hai, is liye yeh misaal syllabus mein zaroori hai."
            },
            {
              "type": "check",
              "q": "Smart bin IoT mein kya karta hai?",
              "a": "Jab bhar jaye to alert bhejta hai, taake gaadi khali safar na kare.",
              "say": "Smart bin IoT mein kya karta hai? Jawab. Jab bhar jaye to alert bhejta hai, taake gaadi khali safar na kare."
            }
          ]
        },
        {
          "id": "ai-pakistan",
          "code": "5.2.1",
          "title": "Pakistan ki taleem mein AI",
          "minutes": 7,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "AI dheere dheere Pakistan ke schools mein aa raha hai: parhana, seekhna, aur administration.",
              "html": "AI dheere dheere Pakistan ke schools mein aa raha hai: parhana, seekhna, aur administration."
            },
            {
              "type": "steps",
              "title": "Istemal aur faida",
              "items": [
                "Learning management system.",
                "Automatic grading aur digital test.",
                "Career counselling.",
                "Har student apni raftar se seekhe.",
                "Jo student peeche hai usay pehchanen.",
                "Disability mein assistive AI."
              ],
              "say": "LMS, grading, counselling, apni speed, extra help, assistive support."
            },
            {
              "type": "p",
              "say": "Mushkilein bhi sach hain: dehaat mein internet kam, har student ke paas device nahi, teachers ki training kam, aur data privacy ka khatra.",
              "html": "Mushkilein bhi sach hain: dehaat mein internet kam, har student ke paas device nahi, teachers ki training kam, aur data privacy ka khatra."
            },
            {
              "type": "p",
              "say": "Career: IoT engineer devices design kare. Data analyst IoT ka data parhe. Skills: Python ya C++, networking, sensors, aur problem solving. Jazz, Telenor, banks, aur government IT departments jagah hain.",
              "html": "Career: IoT engineer devices design kare. Data analyst IoT ka data parhe. Skills: Python ya C++, networking, sensors, aur problem solving. Jazz, Telenor, banks, aur government IT departments jagah hain."
            },
            {
              "type": "check",
              "q": "Pakistan mein AI education ki ek bari mushkil?",
              "a": "Dehaat mein limited internet, devices ki kami, ya teacher training.",
              "say": "Pakistan mein AI education ki ek bari mushkil? Jawab. Dehaat mein limited internet, devices ki kami, ya teacher training."
            }
          ]
        },
        {
          "id": "sources",
          "code": "5.3",
          "title": "Primary, secondary, tertiary sources",
          "minutes": 8,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Information source woh raasta hai jahan se ilm milta hai. Internet pe sab sach nahi hota. Teen qismen hain. Golden topic hai.",
              "html": "Information source woh raasta hai jahan se ilm milta hai. Internet pe sab sach nahi hota. Teen qismen hain. Golden topic hai."
            },
            {
              "type": "svg",
              "name": "sources",
              "say": "Neeche primary, asli data. Beech secondary, kisi aur ki sharah. Upar tertiary, mukhtasar reference.",
              "caption": "Source pyramid."
            },
            {
              "type": "table",
              "headers": [
                "Source",
                "Kya hai",
                "Misal"
              ],
              "rows": [
                [
                  "Primary",
                  "Pehli haath, event ya record",
                  "Interview, photo, diary, NADRA record"
                ],
                [
                  "Secondary",
                  "Kisi aur ne samjhaya hua",
                  "Textbook, news, research paper, statistics report"
                ],
                [
                  "Tertiary",
                  "Dono ka khulasa, jaldi dekhne ke liye",
                  "Encyclopedia, Wikipedia, dictionary, handbook"
                ]
              ],
              "say": "Primary asli, secondary sharah, tertiary khulasa."
            },
            {
              "type": "p",
              "say": "Source bharosa ke qabil nahi jab primary adhoori ya jaan boojh kar jhoot ho, secondary purani ho ya reference na ho, tertiary anjaan website se ho ya itni simple ho ke fact hi marr jaye.",
              "html": "Source bharosa ke qabil nahi jab primary adhoori ya jaan boojh kar jhoot ho, secondary purani ho ya reference na ho, tertiary anjaan website se ho ya itni simple ho ke fact hi marr jaye."
            },
            {
              "type": "tip",
              "say": "Online article pe naam nahi, tareekh nahi, references nahi, to academic kaam ke liye usay mat maano."
            },
            {
              "type": "check",
              "q": "Wikipedia primary hai ya tertiary?",
              "a": "Tertiary. Khulasa hai, pehli haath ka record nahi.",
              "say": "Wikipedia primary hai ya tertiary? Jawab. Tertiary. Khulasa hai, pehli haath ka record nahi."
            }
          ]
        },
        {
          "id": "impacts",
          "code": "5.4",
          "title": "Computing ke asraat",
          "minutes": 7,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Computing zindagi tez aur judi hui banata hai, lekin privacy, naukri, aur screen ki lat bhi laata hai. Har field mein dono pehlu likhna exam mein behtar hai.",
              "html": "Computing zindagi tez aur judi hui banata hai, lekin privacy, naukri, aur screen ki lat bhi laata hai. Har field mein dono pehlu likhna exam mein behtar hai."
            },
            {
              "type": "table",
              "headers": [
                "Field",
                "Faida",
                "Khatra"
              ],
              "rows": [
                [
                  "Taleem",
                  "Door se seekhna, digital books",
                  "Screen, copy paste bina samjhe"
                ],
                [
                  "Sehat",
                  "Records, remote doctor",
                  "Patient data leak"
                ],
                [
                  "Karobar",
                  "Tez hisaab, online dukaan",
                  "Naukriyon ka badalna, cyber attack"
                ],
                [
                  "Samaj",
                  "Rabta asaan",
                  "Privacy, rumour, lat"
                ]
              ],
              "say": "Faida tez raabta hai. Khatra privacy, job change, aur addiction hai."
            },
            {
              "type": "check",
              "q": "Computing ka ek social khatra batao.",
              "a": "Privacy ka khatra, ya technology ki lat.",
              "say": "Computing ka ek social khatra batao. Jawab. Privacy ka khatra, ya technology ki lat."
            }
          ]
        },
        {
          "id": "assistive",
          "code": "5.5",
          "title": "Assistive technologies",
          "minutes": 7,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Assistive technology woh device, software, ya system hai jo disability ya functional limitation mein madad kare, taake zyada log barabari se shamil ho saken. Golden topic hai.",
              "html": "Assistive technology woh device, software, ya system hai jo disability ya functional limitation mein madad kare, taake zyada log barabari se shamil ho saken. Golden topic hai."
            },
            {
              "type": "steps",
              "title": "Misalen",
              "items": [
                "Screen reader, jo screen ki likhai sunaye. Andhe student ke liye.",
                "Captions aur hearing aids, sunne mein madad.",
                "Voice control, haath se mouse mushkil ho to.",
                "Smart wheelchair aur ramp ke sath digital access.",
                "Text ko bari font ya high contrast."
              ],
              "say": "Screen reader, captions, voice, wheelchair, bari font."
            },
            {
              "type": "p",
              "say": "Yeh course khud bhi assistive soch rakhta hai: lecture sunai de, sirf parhne pe depend na ho. Sunain button isi wajah se hai.",
              "html": "Yeh course khud bhi assistive soch rakhta hai: lecture sunai de, sirf parhne pe depend na ho. Sunain button isi wajah se hai."
            },
            {
              "type": "check",
              "q": "Screen reader kis student ki madad karta hai?",
              "a": "Jo screen ki likhai nahi dekh sakta. Software text bol kar sunata hai.",
              "say": "Screen reader kis student ki madad karta hai? Jawab. Jo screen ki likhai nahi dekh sakta. Software text bol kar sunata hai."
            }
          ]
        },
        {
          "id": "assistive-why",
          "code": "5.5.1",
          "title": "Assistive technology kyun zaroori hai",
          "minutes": 6,
          "golden": false,
          "blocks": [
            {
              "type": "steps",
              "title": "Teen wajuhat",
              "items": [
                "Taleem mein barabari: screen reader se digital kitab usi tarah khule jaise doosre students ke liye.",
                "Roz marra ki azadi: khud message, khud form, khud safar.",
                "Shirkat: class, naukri, aur samaj se bahar na rahen."
              ],
              "say": "Barabari, azadi, aur shirkat."
            },
            {
              "type": "p",
              "say": "Agar school ki website sirf mouse se chale aur keyboard se nahi, to kai students bahar reh jate hain. Access baad ki soch nahi, shuru ki soch hai.",
              "html": "Agar school ki website sirf mouse se chale aur keyboard se nahi, to kai students bahar reh jate hain. Access baad ki soch nahi, shuru ki soch hai."
            },
            {
              "type": "check",
              "q": "Equal access ka matlab kya hai?",
              "a": "Disability ke bawajood wahi taleem aur mauqa jo baqi students ko milta hai.",
              "say": "Equal access ka matlab kya hai? Jawab. Disability ke bawajood wahi taleem aur mauqa jo baqi students ko milta hai."
            }
          ]
        },
        {
          "id": "assistive-career",
          "code": "5.5.2",
          "title": "Assistive technology mein career",
          "minutes": 6,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Jo student computing seekh raha hai woh aise tools bana sakta hai jo logon ko shamil karein. Yeh sirf charity nahi, asli software kaam hai.",
              "html": "Jo student computing seekh raha hai woh aise tools bana sakta hai jo logon ko shamil karein. Yeh sirf charity nahi, asli software kaam hai."
            },
            {
              "type": "table",
              "headers": [
                "Role",
                "Kaam"
              ],
              "rows": [
                [
                  "Accessibility specialist",
                  "Apps ko screen reader aur keyboard se chalana"
                ],
                [
                  "Speech and language tech",
                  "Awaaz se likhai, text se awaaz"
                ],
                [
                  "Rehab engineer",
                  "Wheelchair, prosthetic, sensors"
                ],
                [
                  "UX researcher",
                  "Disabled users ke sath test karna"
                ]
              ],
              "say": "Accessibility, speech tech, rehab engineering, aur inclusive UX."
            },
            {
              "type": "p",
              "say": "Shuruat chhoti ho sakti hai: apni class ki website pe captions, contrast, aur clear Urdu-English labels. Wahi skill baad mein product ban jati hai.",
              "html": "Shuruat chhoti ho sakti hai: apni class ki website pe captions, contrast, aur clear Urdu-English labels. Wahi skill baad mein product ban jati hai."
            },
            {
              "type": "check",
              "q": "Accessibility specialist kya check karta hai?",
              "a": "Ke app screen reader, keyboard, aur clear layout se chale.",
              "say": "Accessibility specialist kya check karta hai? Jawab. Ke app screen reader, keyboard, aur clear layout se chale."
            }
          ]
        }
      ]
    },
    {
      "id": "ch6",
      "num": "06",
      "title": "Digital Literacy",
      "blurb": "Data ki qismen, collection, primary secondary, aur digital inquiry.",
      "lectures": [
        {
          "id": "literacy-intro",
          "code": "6.1 – 6.2",
          "title": "Digital literacy aur information age",
          "minutes": 7,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Digital literacy ka matlab sirf phone chalana nahi. Devices, internet, aur online tools ko mehfooz, asar dar, aur zimmedari se use karna. Maloomat dhoondhna, raabta, digital cheez banana, aur masla hal karna.",
              "html": "Digital literacy ka matlab sirf phone chalana nahi. Devices, internet, aur online tools ko mehfooz, asar dar, aur zimmedari se use karna. Maloomat dhoondhna, raabta, digital cheez banana, aur masla hal karna."
            },
            {
              "type": "p",
              "say": "Information age woh daur hai jismein data foran banta, banta, aur milta hai. Device ka hona kafi nahi. Samajhna, sambhalna, aur hikmat se use karna alag skill hai. Is mein technical, sochne wali, aur social teen qabiliyatain hain.",
              "html": "Information age woh daur hai jismein data foran banta, banta, aur milta hai. Device ka hona kafi nahi. Samajhna, sambhalna, aur hikmat se use karna alag skill hai. Is mein technical, sochne wali, aur social teen qabiliyatain hain."
            },
            {
              "type": "tip",
              "say": "Digitally literate student information dhoondhta hai, usay sajata hai, kaam ki cheez banata hai, aur share karte waqt zimmedari nibhata hai."
            },
            {
              "type": "check",
              "q": "Digital literacy sirf typing hai?",
              "a": "Nahi. Mehfooz, samajhdar, aur zimmedar istemal hai.",
              "say": "Digital literacy sirf typing hai? Jawab. Nahi. Mehfooz, samajhdar, aur zimmedar istemal hai."
            }
          ]
        },
        {
          "id": "qual-quant",
          "code": "6.3",
          "title": "Qualitative aur quantitative data",
          "minutes": 7,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Survey ya class project ka data do tarah ka hota hai. Farq samajhna analysis ke liye zaroori hai. Golden topic hai.",
              "html": "Survey ya class project ka data do tarah ka hota hai. Farq samajhna analysis ke liye zaroori hai. Golden topic hai."
            },
            {
              "type": "table",
              "headers": [
                "",
                "Qualitative",
                "Quantitative"
              ],
              "rows": [
                [
                  "Nature",
                  "Bayaan, number nahi",
                  "Number, ginne ya mapne layak"
                ],
                [
                  "Misal",
                  "Online class ke baare mein rai, study habit ka note",
                  "Roz internet use karne wale students, marks, ghante"
                ],
                [
                  "Kaam",
                  "Kyun aur kaise",
                  "Muqabla, average, chart"
                ]
              ],
              "say": "Qualitative kyun aur kaise. Quantitative kitna."
            },
            {
              "type": "p",
              "say": "Sawal ghalat type mangta hai to jawab bekar ho jata hai. Kitne ghante phone, yeh quantitative hai. Phone padhai mein madad kyun karta hai ya nahi, yeh qualitative hai.",
              "html": "Sawal ghalat type mangta hai to jawab bekar ho jata hai. Kitne ghante phone, yeh quantitative hai. Phone padhai mein madad kyun karta hai ya nahi, yeh qualitative hai."
            },
            {
              "type": "check",
              "q": "Students ki rai qualitative hai ya quantitative?",
              "a": "Qualitative, jab tak aap usay number na bana do.",
              "say": "Students ki rai qualitative hai ya quantitative? Jawab. Qualitative, jab tak aap usay number na bana do."
            }
          ]
        },
        {
          "id": "strategies",
          "code": "6.4",
          "title": "Data collect karne ke tareeqe",
          "minutes": 6,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Digital literacy sirf maujooda article dhoondhna nahi. Khud asli data ikattha karna bhi hai. Golden topic hai. Paanch tareeqe: interview, survey, prototype, observation, simulation.",
              "html": "Digital literacy sirf maujooda article dhoondhna nahi. Khud asli data ikattha karna bhi hai. Golden topic hai. Paanch tareeqe: interview, survey, prototype, observation, simulation."
            },
            {
              "type": "svg",
              "name": "inquiry",
              "say": "Sawaal se shuru, phir dhoondho, ikattha karo, analyse karo, aur artefact banao.",
              "caption": "Inquiry flow, collection beech mein hai."
            },
            {
              "type": "tip",
              "say": "8 baje kitni cars intersection cross karti hain? Observation, kyunke ginna hai. Canteen ke khane pe students kya mehsoos karte hain? Survey ya interview."
            },
            {
              "type": "check",
              "q": "Paanch collection strategies ke naam?",
              "a": "Interview, survey, prototype, observation, simulation.",
              "say": "Paanch collection strategies ke naam? Jawab. Interview, survey, prototype, observation, simulation."
            }
          ]
        },
        {
          "id": "interview-survey",
          "code": "6.4.1 – 6.4.2",
          "title": "Interview aur survey",
          "minutes": 7,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Interview plan shuda baat cheet hai, ek bande se ya chhote group se. Sawalat pehle se likhe hote hain. Jawab aksar qualitative hota hai: wajah, mehsoos, tafseel.",
              "html": "Interview plan shuda baat cheet hai, ek bande se ya chhote group se. Sawalat pehle se likhe hote hain. Jawab aksar qualitative hota hai: wajah, mehsoos, tafseel."
            },
            {
              "type": "p",
              "say": "Survey wohi sawalat kai logon se poochta hai. Kaghaz pe ho sakta hai, ya Google Forms aur Microsoft Forms pe. Online tool jawab khud ikattha kar leta hai aur seedha chart bana deta hai.",
              "html": "Survey wohi sawalat kai logon se poochta hai. Kaghaz pe ho sakta hai, ya Google Forms aur Microsoft Forms pe. Online tool jawab khud ikattha kar leta hai aur seedha chart bana deta hai."
            },
            {
              "type": "table",
              "headers": [
                "",
                "Interview",
                "Survey"
              ],
              "rows": [
                [
                  "Log",
                  "Kam, gehra",
                  "Zyada, ek jaisa sawal"
                ],
                [
                  "Jawab",
                  "Zyada tar qualitative",
                  "Qualitative aur quantitative dono"
                ],
                [
                  "Waqt",
                  "Lambi baat",
                  "Chhota form"
                ]
              ],
              "say": "Interview gehra. Survey choura."
            },
            {
              "type": "tip",
              "say": "Survey ka sawal aisa na ho jo jawab munh mein rakh de. Leading question data ko jhoota kar deta hai."
            },
            {
              "type": "check",
              "q": "Kai logon se same sawal, kaun sa tareeqa?",
              "a": "Survey ya questionnaire.",
              "say": "Kai logon se same sawal, kaun sa tareeqa? Jawab. Survey ya questionnaire."
            }
          ]
        },
        {
          "id": "prototype-obs",
          "code": "6.4.3 – 6.4.5",
          "title": "Prototype, observation, simulation",
          "minutes": 7,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Prototype product ka sasta pehla version hai. Log try karte hain, feedback dete hain, aur woh feedback data ban jata hai. Poora banane se pehle pata chal jata hai ke idea chalega ya nahi.",
              "html": "Prototype product ka sasta pehla version hai. Log try karte hain, feedback dete hain, aur woh feedback data ban jata hai. Poora banane se pehle pata chal jata hai ke idea chalega ya nahi."
            },
            {
              "type": "p",
              "say": "Observation mein aap dekhte ho, sawal nahi poochte. Note qualitative ho sakta hai, ginati quantitative. Jaise kitni cars 8 baje cross karti hain.",
              "html": "Observation mein aap dekhte ho, sawal nahi poochte. Note qualitative ho sakta hai, ginati quantitative. Jaise kitni cars 8 baje cross karti hain."
            },
            {
              "type": "p",
              "say": "Simulation computer pe asli situation ka model hai. Variables badal kar dekhte hain kya hoga. Tab use karo jab asli tajurba mehnga, khatarnak, ya mushkil ho.",
              "html": "Simulation computer pe asli situation ka model hai. Variables badal kar dekhte hain kya hoga. Tab use karo jab asli tajurba mehnga, khatarnak, ya mushkil ho."
            },
            {
              "type": "table",
              "headers": [
                "Tareeqa",
                "Sawal poochte ho?",
                "Achhi misaal"
              ],
              "rows": [
                [
                  "Prototype",
                  "Try karwa ke feedback",
                  "App ka kachcha screen"
                ],
                [
                  "Observation",
                  "Nahi, sirf dekhna",
                  "Traffic count"
                ],
                [
                  "Simulation",
                  "Model ke andar",
                  "Mahngi lab ki jagah software"
                ]
              ],
              "say": "Prototype try, observation dekhna, simulation model."
            },
            {
              "type": "check",
              "q": "Asli tajurba khatarnak ho to kaun sa tareeqa?",
              "a": "Simulation.",
              "say": "Asli tajurba khatarnak ho to kaun sa tareeqa? Jawab. Simulation."
            }
          ]
        },
        {
          "id": "primary-secondary",
          "code": "6.5",
          "title": "Primary aur secondary data",
          "minutes": 7,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Data kahan se aaya, yeh bharose ka sawal hai. Golden topic hai. Primary data aap ne isi sawal ke liye khud ikattha kiya: interview, survey, observation, experiment.",
              "html": "Data kahan se aaya, yeh bharose ka sawal hai. Golden topic hai. Primary data aap ne isi sawal ke liye khud ikattha kiya: interview, survey, observation, experiment."
            },
            {
              "type": "p",
              "say": "Secondary data pehle kisi aur ne ikattha kiya, aap naye kaam ke liye dobara use kar rahe ho: kitab, article, official report, website statistics, database.",
              "html": "Secondary data pehle kisi aur ne ikattha kiya, aap naye kaam ke liye dobara use kar rahe ho: kitab, article, official report, website statistics, database."
            },
            {
              "type": "table",
              "headers": [
                "",
                "Primary",
                "Secondary"
              ],
              "rows": [
                [
                  "Source",
                  "Researcher khud",
                  "Pehle se maujood"
                ],
                [
                  "Misal",
                  "Aap ka survey",
                  "Report, article, website"
                ],
                [
                  "Purpose",
                  "Isi study ke liye",
                  "Naye maqsad ke liye reuse"
                ],
                [
                  "Control",
                  "Sawal aap ke",
                  "Data pehle se qaid hai"
                ]
              ],
              "say": "Primary taza aur aap ke control mein. Secondary pehle se maujood, control kam."
            },
            {
              "type": "check",
              "q": "Aap ne Google Form se class se jawab liye. Primary hai ya secondary?",
              "a": "Primary. Aap ne khud isi sawal ke liye ikattha kiya.",
              "say": "Aap ne Google Form se class se jawab liye. Primary hai ya secondary? Jawab. Primary. Aap ne khud isi sawal ke liye ikattha kiya."
            }
          ]
        },
        {
          "id": "approach",
          "code": "6.6",
          "title": "Data collection ka plan",
          "minutes": 6,
          "golden": false,
          "blocks": [
            {
              "type": "steps",
              "title": "Plan ke aath qadam",
              "items": [
                "Research question saaf likho.",
                "Quantitative, qualitative, ya dono.",
                "Tareeqa chuno: survey, interview, observation.",
                "Sample ya group chuno.",
                "Form, sawalat, observation sheet taiyar karo.",
                "Ehtiyat se data lo.",
                "Spreadsheet mein rakho aur backup rakho.",
                "Ijazat lo. Privacy zaroori hai. Consent ke baghair nahi."
              ],
              "say": "Sawaal, type, tareeqa, sample, tool, collection, storage, ethics."
            },
            {
              "type": "tip",
              "say": "Bina consent ke doosre student ka naam ya phone data mein mat daalo."
            },
            {
              "type": "check",
              "q": "Collection se pehle aakhri ethical qadam kya hai?",
              "a": "Consent. Logon ki ijazat aur privacy.",
              "say": "Collection se pehle aakhri ethical qadam kya hai? Jawab. Consent. Logon ki ijazat aur privacy."
            }
          ]
        },
        {
          "id": "presenting",
          "code": "6.7",
          "title": "Digital tools se data pesh karna",
          "minutes": 6,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Data ikattha kar lena aadha kaam hai. Doosra hissa yeh hai ke doosra insaan jaldi samajh jaye. Digital tools yahi karte hain.",
              "html": "Data ikattha kar lena aadha kaam hai. Doosra hissa yeh hai ke doosra insaan jaldi samajh jaye. Digital tools yahi karte hain."
            },
            {
              "type": "svg",
              "name": "bars",
              "say": "Spreadsheet se chart, chart slides mein. Number se shakal.",
              "caption": "From sheet to chart."
            },
            {
              "type": "p",
              "say": "Behtar chart lamba paragraph se tez samjhata hai. Lekin chart asal data pe ho, mubaligha nahi. Galat scale se chhoti farq ko pahaad mat banao.",
              "html": "Behtar chart lamba paragraph se tez samjhata hai. Lekin chart asal data pe ho, mubaligha nahi. Galat scale se chhoti farq ko pahaad mat banao."
            },
            {
              "type": "check",
              "q": "Chart tez samjhata hai, lekin shart kya hai?",
              "a": "Woh asal data pe ho, exaggerate na ho.",
              "say": "Chart tez samjhata hai, lekin shart kya hai? Jawab. Woh asal data pe ho, exaggerate na ho."
            }
          ]
        },
        {
          "id": "tools",
          "code": "6.7.1 – 6.7.4",
          "title": "Sheet, slides, infographic, report",
          "minutes": 8,
          "golden": false,
          "blocks": [
            {
              "type": "table",
              "headers": [
                "Tool",
                "Kaam",
                "Misal"
              ],
              "rows": [
                [
                  "Spreadsheet",
                  "Rows, total, average, sort, chart",
                  "Excel, Google Sheets"
                ],
                [
                  "Slides",
                  "Audience ko short points",
                  "PowerPoint, Google Slides, Canva"
                ],
                [
                  "Infographic",
                  "Ek nazar mein asal baat",
                  "Canva, Power BI, Tableau"
                ],
                [
                  "Report",
                  "Title, data, findings, conclusion",
                  "Word, Google Docs"
                ]
              ],
              "say": "Sheet hisaab, slides bolna, infographic ikhtisar, report poori kahani."
            },
            {
              "type": "steps",
              "title": "Slides ka usool",
              "items": [
                "Title aur research question pehle.",
                "Lambay paragraph ki jagah chhote points.",
                "Table ya chart jahan number ho.",
                "Design saaf, parhne layak."
              ],
              "say": "Sawaal dikhao, points chhote rakho, chart lagao, design saaf."
            },
            {
              "type": "p",
              "say": "Report mein title, introduction, purpose, tables, simple zaban mein findings, aur recommendations. AI se jumla sanwarna ho sakta hai, lekin aap khud check karo ke number jhoot na ho gaye hon.",
              "html": "Report mein title, introduction, purpose, tables, simple zaban mein findings, aur recommendations. AI se jumla sanwarna ho sakta hai, lekin aap khud check karo ke number jhoot na ho gaye hon."
            },
            {
              "type": "check",
              "q": "Average aur sort kis tool ka kaam hai?",
              "a": "Spreadsheet.",
              "say": "Average aur sort kis tool ka kaam hai? Jawab. Spreadsheet."
            }
          ]
        },
        {
          "id": "inquiry",
          "code": "6.8",
          "title": "Digital inquiry: phone aur padhai",
          "minutes": 7,
          "golden": true,
          "blocks": [
            {
              "type": "p",
              "say": "Yeh golden case study hai. Poora chapter ek sawal pe lag jata hai. Research question: rozana mobile phone ka istemal students ki study habits pe kya asar dalta hai?",
              "html": "Yeh golden case study hai. Poora chapter ek sawal pe lag jata hai. Research question: rozana mobile phone ka istemal students ki study habits pe kya asar dalta hai?"
            },
            {
              "type": "p",
              "say": "Manzar: free period mein phones nazar aate hain. Koi kehta hai seekhne mein madad, koi kehta hai waqt zaya. Class ko tahqeeq karni hai, rai nahi.",
              "html": "Manzar: free period mein phones nazar aate hain. Koi kehta hai seekhne mein madad, koi kehta hai waqt zaya. Class ko tahqeeq karni hai, rai nahi."
            },
            {
              "type": "svg",
              "name": "inquiry",
              "say": "Question, search, collect, analyze, create. Yahi paanch qadam poore project ke hain.",
              "caption": "Digital inquiry workflow."
            },
            {
              "type": "steps",
              "title": "Workflow",
              "items": [
                "Question saaf karo.",
                "Pehle secondary search, background.",
                "Primary data ikattha karo.",
                "Spreadsheet aur charts se analyse.",
                "Aakhir mein digital artefact banao jo sawal ka jawab de."
              ],
              "say": "Sawaal, search, collect, analyse, create."
            },
            {
              "type": "check",
              "q": "Case study ka research question kya hai?",
              "a": "Rozana phone use study habits pe kya asar dalta hai.",
              "say": "Case study ka research question kya hai? Jawab. Rozana phone use study habits pe kya asar dalta hai."
            }
          ]
        },
        {
          "id": "inquiry-search",
          "code": "6.8 steps 1–3",
          "title": "Advanced search aur methodology",
          "minutes": 7,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Pehle background. Search engine pe secondary data, lekin khuli search ka dher nahi. Advanced operators se ghera tang karo.",
              "html": "Pehle background. Search engine pe secondary data, lekin khuli search ka dher nahi. Advanced operators se ghera tang karo."
            },
            {
              "type": "code",
              "lang": "text",
              "text": "\"screen time\" students concentration\nsite:.edu mobile learning\nsmartphone study habits 2024..2026",
              "say": "Quotes se exact jumla. site se domain. Do dots se saal ka darmiyan."
            },
            {
              "type": "steps",
              "title": "Pehle teen qadam",
              "items": [
                "Advanced search se bharosa ke qabil secondary articles.",
                "Author, date, aur reference check karo. Warna chhor do.",
                "Methodology likho: kaun se students, kaun sa tool, primary aur secondary dono."
              ],
              "say": "Search narrow karo, source check karo, methodology likho."
            },
            {
              "type": "check",
              "q": "Quotes search mein kya karte hain?",
              "a": "Exact phrase dhoondhte hain, alag alag lafz nahi.",
              "say": "Quotes search mein kya karte hain? Jawab. Exact phrase dhoondhte hain, alag alag lafz nahi."
            }
          ]
        },
        {
          "id": "inquiry-survey",
          "code": "6.8 steps 4–6",
          "title": "Survey likhna aur primary data",
          "minutes": 7,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Survey saaf aur unbiased ho. Ek sawal ek hi cheez pooche.",
              "html": "Survey saaf aur unbiased ho. Ek sawal ek hi cheez pooche."
            },
            {
              "type": "table",
              "headers": [
                "Sawal",
                "Data ki qisam"
              ],
              "rows": [
                [
                  "Roz phone kitne ghante?",
                  "Quantitative"
                ],
                [
                  "Phone sab se zyada kis kaam?",
                  "Qualitative, ya categories"
                ],
                [
                  "Padhai ke dauran phone madad karta hai ya nuksan? 1 se 5",
                  "Quantitative scale"
                ]
              ],
              "say": "Ghante number hain. Wajah ya activity qualitative ho sakti hai. Scale quantitative hai."
            },
            {
              "type": "steps",
              "title": "Primary collection",
              "items": [
                "Sample class ke students hon, naam optional rakho.",
                "Consent ki line form ke upar likho.",
                "Google Form ya paper, phir jawab spreadsheet mein.",
                "Khali ya mazaq wale jawab cleaning mein hatao."
              ],
              "say": "Sample, consent, form, phir cleaning."
            },
            {
              "type": "check",
              "q": "Ghante wala sawal qualitative hai?",
              "a": "Nahi. Woh quantitative hai.",
              "say": "Ghante wala sawal qualitative hai? Jawab. Nahi. Woh quantitative hai."
            }
          ]
        },
        {
          "id": "inquiry-sheet",
          "code": "6.8 steps 7–9",
          "title": "Secondary data aur spreadsheet",
          "minutes": 7,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Secondary data apni survey ke sath rakho. Misal: koi bharosa ke qabil article kehta hai ke zyada screen time concentration kam karta hai. Apne primary numbers se isay compare karo. Agar dono milen to baat mazboot. Agar na milen to wajah likho, chhupao mat.",
              "html": "Secondary data apni survey ke sath rakho. Misal: koi bharosa ke qabil article kehta hai ke zyada screen time concentration kam karta hai. Apne primary numbers se isay compare karo. Agar dono milen to baat mazboot. Agar na milen to wajah likho, chhupao mat."
            },
            {
              "type": "code",
              "lang": "text",
              "text": "Hours | Activity | Focus score\n4     | social   | 2\n1     | notes    | 5\n5     | video    | 2",
              "say": "Har column ek field. Average hours, aur activity ki count, dono nikal sakte ho."
            },
            {
              "type": "steps",
              "title": "Sheet ka intizam",
              "items": [
                "Ek header row, neeche sirf data.",
                "Ghante number format mein, text nahi.",
                "Average aur count formulas se, haath se nahi.",
                "Backup: doosri copy ya drive."
              ],
              "say": "Header, number format, formula, backup."
            },
            {
              "type": "check",
              "q": "Article ka screen-time claim primary hai ya secondary?",
              "a": "Secondary. Kisi aur ne pehle ikattha kiya.",
              "say": "Article ka screen-time claim primary hai ya secondary? Jawab. Secondary. Kisi aur ne pehle ikattha kiya."
            }
          ]
        },
        {
          "id": "inquiry-end",
          "code": "6.8 steps 10–12",
          "title": "Analysis, natija, aur artefact",
          "minutes": 8,
          "golden": false,
          "blocks": [
            {
              "type": "p",
              "say": "Charts dekh kar trend likho. Notes ki misaal isi sawal ki ek mumkin kahani hai: zyada tar students 3 se 5 ghante phone use karte hain, aadhe entertainment pe, aur lambay ghante walon ka focus score kam. Apni class ke asal numbers alag ho sakte hain. Natija unhi pe likho.",
              "html": "Charts dekh kar trend likho. Notes ki misaal isi sawal ki ek mumkin kahani hai: zyada tar students 3 se 5 ghante phone use karte hain, aadhe entertainment pe, aur lambay ghante walon ka focus score kam. Apni class ke asal numbers alag ho sakte hain. Natija unhi pe likho."
            },
            {
              "type": "svg",
              "name": "bars",
              "say": "3 se 5 ghante wali category sab se lambi ho to wahi trend hai. Chart ko apne asal counts se bharna.",
              "caption": "Example distribution of phone hours."
            },
            {
              "type": "p",
              "say": "Natija sawal ka seedha jawab ho: is class mein zyada phone, khas kar entertainment, padhai ke focus se juda nazar aaya. Had yeh hai ke ek class ki survey poore sheher ka qanoon nahi.",
              "html": "Natija sawal ka seedha jawab ho: is class mein zyada phone, khas kar entertainment, padhai ke focus se juda nazar aaya. Had yeh hai ke ek class ki survey poore sheher ka qanoon nahi."
            },
            {
              "type": "p",
              "say": "Digital artefact aakhri product hai jo asal sawal ka jawab de. Sirf sajawat nahi. Slides, infographic, ya chhota report: sawal, tareeqa, chart, natija, aur ek recommendation. Misal: padhai ke 25 minute mein phone doosre kamre mein.",
              "html": "Digital artefact aakhri product hai jo asal sawal ka jawab de. Sirf sajawat nahi. Slides, infographic, ya chhota report: sawal, tareeqa, chart, natija, aur ek recommendation. Misal: padhai ke 25 minute mein phone doosre kamre mein."
            },
            {
              "type": "table",
              "headers": [
                "Career",
                "Yahi skill"
              ],
              "rows": [
                [
                  "Market research analyst",
                  "Survey se primary data, business faisla"
                ],
                [
                  "UX researcher",
                  "Qualitative aur quantitative dono se product"
                ],
                [
                  "Data journalist",
                  "Number ko seedhi kahani"
                ]
              ],
              "say": "Survey, interview, sheet, aur chart wahi kaam hai jo yeh careers karti hain."
            },
            {
              "type": "tip",
              "say": "Artefact mein har number ki jagah likho: primary survey ya secondary article. Bina source ke chart bharosa nahi karta."
            },
            {
              "type": "check",
              "q": "Digital artefact sirf khubsurat poster hai?",
              "a": "Nahi. Woh sawal ka jawab hai: tareeqa, data, natija, aur recommendation.",
              "say": "Digital artefact sirf khubsurat poster hai? Jawab. Nahi. Woh sawal ka jawab hai: tareeqa, data, natija, aur recommendation."
            }
          ]
        }
      ]
    }
  ]
};
