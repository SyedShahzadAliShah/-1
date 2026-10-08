from .blocks import check, code, lecture, p, steps, svg, table, tip

CHAPTER = {
    "id": "ch4",
    "num": "04",
    "title": "Data and Analysis",
    "blurb": "Database, keys, ER model, referential integrity, aur MS Access.",
    "lectures": [
        lecture(
            "data-info",
            "4.1.1",
            "Data, information, aur database",
            7,
            [
                p("Data kachcha fact hai. Numbers 80, 75, 90, 70, 85 data hain. Parking mein caron ke rang bhi data hain. Jab inhein process karke matlab nikalte hain to information banti hai. Misal: class ka average 80 percent hai. Information faisla karne mein madad karti hai."),
                table(
                    ["", "Data", "Information"],
                    [
                        ["Definition", "Raw facts", "Processed, meaningful"],
                        ["Misal", "85, 90, 75", "Average marks 83.3 percent"],
                        ["Faida", "Akela kam useful", "Decision ke kaam ka"],
                    ],
                    "Data kachcha hai. Information us ka matlab hai.",
                ),
                p("Database related data ka organised collection hai, taake dhoondhna, badalna, aur update karna asaan ho. Purane files aur registers mein search mushkil thi. Database woh mushkil hal karta hai."),
                check(
                    "85, 90, 75 data hai ya information?",
                    "Data. Average nikal jaye to woh information ban jati hai.",
                ),
            ],
        ),
        lecture(
            "dbms",
            "4.1.2",
            "Database Management System",
            7,
            [
                p("DBMS woh software hai jis se user database banata, sambhalta, aur use karta hai. User files se seedha nahi ladta. DBMS beech mein pul hai. MySQL aur Oracle DBMS ki misaal hain."),
                steps(
                    "DBMS ke faide",
                    [
                        "Redundancy kam: department ka naam har student row mein dobara nahi.",
                        "Consistency: phone number ek jagah badla to sab ko naya number mile.",
                        "Security: admin marks dekhe, staff sirf naam.",
                        "Integrity: do students ka same roll number na ho.",
                    ],
                    "Kam dohrav, ek jaisa data, ijazat, aur sahi data.",
                ),
                check(
                    "DBMS user aur database ke beech kya hai?",
                    "Pul. User DBMS se baat karta hai, files se seedha nahi.",
                ),
            ],
        ),
        lecture(
            "components",
            "4.2",
            "Table, record, aur field",
            6,
            [
                p("Table rows aur columns mein data rakhti hai, spreadsheet ki tarah. Har table ek entity ke baare mein hoti hai, jaise Students ya Teachers."),
                table(
                    ["Roll No", "Name", "Course", "Grade"],
                    [
                        ["101", "Ali", "CS", "A"],
                        ["102", "Sara", "IT", "B+"],
                        ["103", "Ahmed", "CS", "A"],
                    ],
                    "Ek poori row record hai, jaise Ali ki tamam maloomat. Ek column field hai, jaise sirf names.",
                ),
                p("Record ek instance ki poori kahani hai. Field ek hi qisam ki maloomat hai. Roll number column field hai. Ali ki poori line record hai."),
                check(
                    "Sirf names wala column record hai ya field?",
                    "Field. Record poori row hoti hai.",
                ),
            ],
        ),
        lecture(
            "keys",
            "4.3.1",
            "Keys aur integrity",
            10,
            [
                p("Key woh field hai jo record ko unique banaye aur tables ko jode. Golden topic hai. Candidate key koi bhi aisi field, ya fields ka set, hai jo record alag pehchan sake. Ek table mein kai candidate keys ho sakti hain. Null allowed nahi, duplicate allowed nahi."),
                svg("keys", "EmpID, license, aur passport teeno candidate hain. School jaisa, hum EmpID ko primary chun lete hain. Baqi alternate ban jati hain.", "Candidate, primary, alternate."),
                p("Primary key un candidate keys mein se woh ek hai jo hum chun lein. Har table ki sirf ek primary key. Unique, aur null nahi. Classroom mein roll number, B-form, aur phone teeno candidate ho sakte hain. School roll number ko primary bana deta hai."),
                p("Jo candidate keys primary nahi bani, woh alternate keys hain. License aur passport alternate reh jate hain. Woh ab bhi unique hain."),
                p("Foreign key doosri table ki primary key ki taraf ishara karti hai. Employee table ka DeptID, Department table ke DeptID se judta hai. Foreign key duplicate ho sakti hai, kyunke kai employees ek department mein ho sakte hain. Kabhi kabhi null bhi ho sakti hai."),
                check(
                    "Primary key null ho sakti hai?",
                    "Nahi. Na duplicate, na null. Aur ek table mein sirf ek primary key.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "rdbms",
            "4.3",
            "Relational database",
            6,
            [
                p("RDBMS data ko kai tables mein rakhta hai aur primary aur foreign keys se unhein jodta hai. Banks aur universities isi structure pe chalte hain."),
                steps(
                    "RDBMS kyun",
                    [
                        "Dohrana data kam ho jata hai.",
                        "Kai users security ke sath kaam kar sakte hain.",
                        "SQL se sawal poochna asaan hai.",
                    ],
                    "Kam redundancy, multi user, aur SQL.",
                ),
                p("SQL ka matlab Structured Query Language hai. Table se specific rows nikalne ka tareeqa yahi hai."),
                check(
                    "RDBMS tables ko kis cheez se jodta hai?",
                    "Keys se, khas tor pe primary aur foreign key.",
                ),
            ],
        ),
        lecture(
            "er-model",
            "4.4",
            "Entity relationship model",
            9,
            [
                p("ER model database banane se pehle ka naqsha hai. Architect ka blueprint. Golden topic hai. Teen cheezein: entity, attribute, relationship."),
                svg("er", "Rectangle entity hai, jaise STUDENT. Oval attribute hai, jaise Name. Diamond relationship hai, jaise Enrolls. Primary key attribute ke neeche line hoti hai.", "ER symbols."),
                table(
                    ["Relationship", "Matlab", "Misal"],
                    [
                        ["One to one", "Ek record sirf ek se juda", "Ek student ki ek ID card"],
                        ["One to many", "Ek record kai se juda. Sab se common", "Ek teacher, kai students"],
                        ["Many to many", "Dono taraf kai", "Kai students, kai classes"],
                    ],
                    "1:1 rare hai. 1:M common hai. M:N ko seedha nahi rakhte.",
                ),
                tip("Relational database many to many seedha nahi sambhalta. Dono taraf dohrav ho jata hai. Beech mein junction table rakho, jaise Enrollment, taake do one-to-many ban jayen."),
                check(
                    "ER diagram mein diamond kya dikhata hai?",
                    "Relationship. Rectangle entity hai, oval attribute.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "referential",
            "4.5",
            "Referential integrity, cascade update aur delete",
            8,
            [
                p("Referential integrity ka matlab hai foreign key hamesha kisi maujooda primary key ki taraf ishara kare. Orphan record nahi banne deti. Golden topic hai."),
                svg("integrity", "Student parent mein 101 Ali aur 102 Sara hain. Result child mein 101 allowed hai. 999 reject, kyunke parent mein 999 hai hi nahi.", "Parent rejects an orphan foreign key."),
                p("Agar integrity on ho to aap student 999 ka result nahi daal sakte jab 999 student table mein na ho. Aur aap us student ko delete nahi kar sakte jis ke marks ab bhi result table mein hon, jab tak related rows ka faisla na ho."),
                steps(
                    "Do automatic operations",
                    [
                        "Cascade update: parent ki primary key badle to child ki foreign key bhi badal jaye. Ali ka 101, 201 ho jaye to enrollment mein bhi 201.",
                        "Cascade delete: parent ki row delete ho to child ki related rows bhi delete. Sara school chhor de to us ke enrollments aur results bhi mit jayen.",
                    ],
                    "Cascade update id sath badalta hai. Cascade delete bacchon ko bhi mita deta hai.",
                ),
                check(
                    "999 parent mein nahi aur child mein aa jaye. Isay kya kehte hain?",
                    "Orphan record. Referential integrity isay reject karti hai.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "schema",
            "4.6",
            "Relational schema",
            6,
            [
                p("Relational schema database ka formal naqsha hai, software mein banane se pehle. Yeh batata hai tables kaun si hain, fields kya hain, primary aur foreign keys kaun si hain, aur tables kaise judi hain."),
                steps(
                    "Schema kyun pehle",
                    [
                        "Dohrav pehle hi kam ho jata hai.",
                        "Keys pehle plan hon to integrity behtar.",
                        "Baad mein barhana asaan.",
                    ],
                    "Bina naqshe ke ghar jaisa. Schema skip karoge to database messy hogi.",
                ),
                tip("Ghar bina architect ke drawing ke mat banao. Database bina schema ke mat banao."),
                check(
                    "Schema asal data store karta hai ya structure describe karta hai?",
                    "Structure describe karta hai. Data baad mein tables mein jata hai.",
                ),
            ],
        ),
        lecture(
            "library-case",
            "4.7",
            "Library case study",
            9,
            [
                p("College library ka ER schema step by step. Book ki id, title, author, publisher. Member ki id, name, contact. Member kai books le sakta hai, aur ek book waqt ke sath kai members le sakte hain. Issue date aur return date record hone chahiye."),
                steps(
                    "Saat steps",
                    [
                        "Requirements likho.",
                        "Entities: Book aur Member.",
                        "Attributes: BookID primary, MemberID primary.",
                        "Relationship: member borrows book.",
                        "Cardinality many to many.",
                        "Junction entity BorrowRecord se M:N tod do.",
                        "Final: Member one to many BorrowRecord, Book one to many BorrowRecord.",
                    ],
                    "Do entities, many to many, phir BorrowRecord beech mein.",
                ),
                svg("library", "Member ek taraf, Book doosri taraf, beech BorrowRecord. Dono relationships one to many hain junction ki taraf.", "Resolved library schema."),
                p("BorrowRecord ke attributes: BorrowID primary, MemberID foreign, BookID foreign, IssueDate, ReturnDate. Ab ek borrowing ek alag row hai. Dohrana data nahi."),
                check(
                    "Member aur Book ki many to many ko kaun si table todti hai?",
                    "BorrowRecord, junction table.",
                ),
            ],
        ),
        lecture(
            "objects",
            "4.8",
            "Tables, forms, queries, reports",
            7,
            [
                p("Access jaise DBMS mein char bade objects hain. Table asal data rakhti hai. Form user ko saaf screen deta hai enter aur edit ke liye. Query sawal hai: mujhe woh students dikhao jin ke marks 80 se upar hain. Report print ya share karne ki sajawat hai, aksar query ke result pe."),
                table(
                    ["Object", "Kaam"],
                    [
                        ["Table", "Data store, rows aur columns"],
                        ["Form", "Data enter, edit, dekhna, galti kam"],
                        ["Query", "Specific data nikalna, filter"],
                        ["Report", "Khubsurat output, print"],
                    ],
                    "Table store, form enter, query poochho, report dikhao.",
                ),
                p("Query table ko badalta nahi. Sirf poochta hai. Is liye analysis ke liye safe hai."),
                check(
                    "Data asal kis object mein rehta hai?",
                    "Table mein. Form aur report us data ko dikhate hain.",
                ),
            ],
        ),
        lecture(
            "access-tables",
            "4.9",
            "MS Access mein table banana",
            7,
            [
                p("Table banana database ka pehla asal kaam hai. Pehle plan: kaun se fields, kaun sa data type, kaun si primary key, kaun se rules. Galat type baad mein query ko slow aur data ko ghalat kar deta hai."),
                steps(
                    "Design View",
                    [
                        "Create, phir Table Design.",
                        "Field name likho, data type chuno: Short Text, Number, Date, Yes/No, AutoNumber.",
                        "Neeche field properties: field size, format, required, validation rule.",
                        "Primary key select karke key icon dabao.",
                        "Save karo, table ka naam do. Tab data enter karo.",
                    ],
                    "Design view pehle structure, phir data. Professional tareeqa yahi hai.",
                ),
                tip("Datasheet view jaldi hoti hai lekin types khud guess karti hai. Exam mein Design View likhna, kyunke wahan control poora hota hai."),
                check(
                    "Primary key Access mein kahan set hoti hai?",
                    "Design View mein field select karke key icon se.",
                ),
            ],
        ),
        lecture(
            "forms",
            "4.10",
            "Forms se data enter karna",
            6,
            [
                p("Form table ki jagah ek record ek screen pe dikhata hai. Galti kam hoti hai, validation nazar aati hai, aur user ko columns ka jungle nahi milta."),
                steps(
                    "Form ka data source",
                    [
                        "Har form kisi table ya query se juda hona chahiye. Bina source ke form kahan save kare?",
                        "Form wizard se table chuno, fields chuno, layout chuno.",
                        "Design view mein label saaf karo aur required fields nazar pe rakho.",
                    ],
                    "Form ka source table ya query hota hai. Wizard se shuru karo.",
                ),
                check(
                    "Form data khud store karta hai?",
                    "Nahi. Form table ya query ka interface hai. Data table mein rehta hai.",
                ),
            ],
        ),
        lecture(
            "queries",
            "4.11",
            "MS Access queries",
            8,
            [
                p("Query Access ki sab se taqatwar cheez hai. Data nikalti, filter karti, aur analyse karti hai, asal table ko badle baghair. Golden topic hai."),
                steps(
                    "Simple select query",
                    [
                        "Create, Query Design.",
                        "Table add karo, jaise Students.",
                        "Fields neeche grid mein kheench lo: Name, Department, Marks.",
                        "Criteria row mein rule likho. Department ke neeche Computer Science.",
                        "Run. Sirf wohi rows aayengi.",
                    ],
                    "Design grid mein fields upar, criteria neeche. Computer Science sirf us department ki rows rakhega.",
                ),
                code(
                    "SELECT Name, Department, Marks\nFROM Students\nWHERE Department = \"Computer Science\";",
                    "Yahi baat SQL mein. Criteria row WHERE ban jati hai.",
                    lang="sql",
                ),
                p("Criteria khali ho to saari rows aati hain. Text criteria quotes mein. Number bina quotes. Ek se zyada columns pe criteria AND ki tarah judte hain."),
                check(
                    "Query chalane se table ka asal data badalta hai?",
                    "Nahi. Select query sirf dikhati hai.",
                ),
            ],
            golden=True,
        ),
        lecture(
            "totals",
            "4.11.4",
            "Grouping aur statistics",
            6,
            [
                p("Grouping milti julti rows ko jod kar total nikalti hai. Misal: department ke hisaab se students ki tadad, ya average marks."),
                steps(
                    "Totals row",
                    [
                        "Query design mein Totals button dabao. Grid mein Total row aa jati hai.",
                        "Department pe Group By rakho.",
                        "Marks pe Avg chuno, ya Count, Sum, Min, Max.",
                        "Run. Har department ki ek line aayegi.",
                    ],
                    "Group By department, phir Avg marks. Ek group, ek number.",
                ),
                table(
                    ["Total option", "Kaam"],
                    [
                        ["Group By", "Milti values ikatthi"],
                        ["Count", "Rows ginna"],
                        ["Sum", "Jama"],
                        ["Avg", "Average"],
                        ["Min / Max", "Sab se chhota ya bara"],
                    ],
                    "Group By ke sath Count, Sum, Avg, Min, Max.",
                ),
                check(
                    "Har department ka average marks chahiye. Department pe kya hoga?",
                    "Group By. Marks pe Avg.",
                ),
            ],
        ),
        lecture(
            "charts",
            "4.11.6",
            "Charts se data dikhana",
            6,
            [
                p("Visualization numbers ko shakal deta hai taake pattern ek nazar mein dikhe."),
                svg("bars", "Bar chart categories compare karti hai. Lamba bar bara number.", "Bar chart of categories."),
                svg("pie", "Pie chart hisse dikhati hai, poore ka percent. Pass aur needs-help jaisa.", "Pie chart of a whole."),
                table(
                    ["Chart", "Kab"],
                    [
                        ["Bar", "Categories ka muqabla, jaise departments"],
                        ["Column", "Wahi muqabla, khadi bars"],
                        ["Line", "Waqt ke sath trend"],
                        ["Pie", "Poore ke hisse, percent"],
                    ],
                    "Bar muqabla, line trend, pie hissa.",
                ),
                tip("Pie tab jab hisse mila kar poora banen. Bahut zyada slices pie ko bekar kar deti hain. Us waqt bar behtar hai."),
                check(
                    "Mahine ke sath marks ka trend kaun sa chart?",
                    "Line chart.",
                ),
            ],
        ),
    ],
}
