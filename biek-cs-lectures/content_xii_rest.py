"""Class XII units 5, 6 and 7."""

from reportlab.lib.units import mm

REST = []

REST.append({
    "grade": "XII",
    "unit": "5",
    "kicker": "Class XII  |  Unit 5  |  weight 15%",
    "title": "Database fundamentals",
    "weight": "15%",
    "periods": "20 theory periods and 10 lab periods",
    "intro": "A database stores related data so that many programs can use it without keeping their own conflicting copies. This lecture moves from that idea to tables, relationships, normal forms and SQL, and ends with the design of a library.",
    "slos": [
        "Contrast a flat file with a database management system and name DBMS components, characteristics, models and users.",
        "Describe the three levels of data abstraction and the basic relational terms.",
        "Draw entities, attributes and relationships, and apply 1NF, 2NF and 3NF.",
        "Use keys, integrity constraints and the four relationship types.",
        "Write SQL for selection, projection, conditions, joins and simple DML.",
        "Design a library schema through the standard design steps.",
    ],
    "path": [
        "Start with one messy spreadsheet of library issues and show the repeated names.",
        "Normalise that sheet to 3NF on the board. The SQL afterwards uses those tables.",
        "Keep selection and projection in one pair of examples so the words stay attached to WHERE and to the column list.",
    ],
    "sections": [
        ("h", "5.1 From files to a database"),
        ("p", "A **flat file** is a single file of records, often one fact repeated on many rows, with no enforced link to other files. A class list in one spreadsheet and an issue list that copies every student's name into every row is a flat-file habit. A **database management system** is software that stores related data, controls access, and lets programs ask questions without each program knowing the physical layout."),
        ("p", "Databases run college records, bank accounts, hospital patients, shop stock and examination results. Anywhere the same fact is used by more than one process, a shared database avoids a pile of disagreeing copies."),
        ("table", "Components of a DBMS", ["Component", "Meaning"], [
            ["Hardware", "The computers and disks the data lives on."],
            ["Software", "The DBMS itself, together with the application programs."],
            ["Data", "The stored facts, and the data dictionary that describes them."],
            ["Procedures", "The rules for backup, access and recovery."],
            ["Data access language", "The language used to define and manipulate the data. SQL is the one in this course."],
        ]),
        ("table", "Characteristics you should be able to name", ["Characteristic", "What it means here"], [
            ["Controlled redundancy", "A fact is stored once and referred to, rather than copied everywhere."],
            ["Data accuracy", "The stored values match the real world they describe."],
            ["Integrity", "The data obeys rules, such as a mark being within range and a book issue pointing at a real book."],
            ["Normalisation", "A design discipline that splits tables so that redundancy and update problems shrink."],
            ["Security", "Only authorised users perform the actions allowed to them."],
            ["Scalability", "The system can grow in data and users."],
        ]),
        ("p", "The **entity-relationship model** describes the world as entities, attributes and relationships, before tables are chosen. The curriculum calls this the entity relational model. The **relational model** stores data in tables. An **object-relational model** keeps tables and adds object features such as richer data types. Draw the ER model when the question says conceptual design. Draw tables when it says relational."),
        ("p", "A **database administrator** controls the structure, the accounts, the backup and the security. A **database application programmer** writes the programs that use the database, such as the library screens."),
        ("h", "5.2 Architecture, tables and normal forms"),
        ("diagram", "levels", "Figure 5.1  Three levels of data abstraction.", 58 * mm),
        ("p", "The **external level** is a view for one kind of user. A student may see his own issues and not every member's phone number. The **conceptual level** is the whole logical database: all the tables, keys and relationships. The **physical level** is how the data is stored in files and indexes. Users work at the top. The DBMS hides the bottom. This separation is data abstraction."),
        ("table", "Relational words", ["Word", "Meaning"], [
            ["Table", "A named collection of rows of the same kind. Also called a relation."],
            ["Record or tuple", "One row."],
            ["Field, column or attribute", "One named property, such as Title."],
            ["Schema", "The design of the tables, columns and keys, as distinct from the rows currently stored."],
            ["Primary key", "A column, or a group of columns, that identifies one row and never repeats."],
            ["Foreign key", "A column that refers to the primary key of another table."],
        ]),
        ("p", "In an ER diagram an **entity** is a rectangle, an **attribute** is an oval joined to its entity, and a **relationship** is a diamond joined to the entities it connects. Underline the key attribute. For the library, BOOK, MEMBER and the relationship ISSUES are enough to start."),
        ("table", "Relationship types", ["Type", "Library meaning"], [
            ["One to one", "A member has one current library card. That card belongs to one member."],
            ["One to many", "One member may borrow many books. From the book side, one copy is issued to one member at a time."],
            ["Many to one", "Many issue-rows point at one member. This is the same fact as one-to-many, read from the other side."],
            ["Many to many", "Over time many members borrow many books. A junction table, ISSUE, holds one row per loan and breaks the many-to-many into two one-to-many links."],
        ]),
        ("h3", "A normalisation you can reproduce"),
        ("p", "Start with this repeated sheet. The intended key of one result row is StudentID together with SubjectID."),
        ("table", "Before the split", ["StudentID", "SubjectID", "StudentName", "Dept", "HOD", "SubjectName", "Marks"], [
            ["S1", "M", "Ayesha", "Science", "Khan", "Maths", "80"],
            ["S1", "P", "Ayesha", "Science", "Khan", "Physics", "74"],
            ["S2", "M", "Bilal", "Science", "Khan", "Maths", "61"],
        ]),
        ("p", "**First normal form** requires atomic values and no repeating group. Each cell above already holds one value, and each subject is its own row, so the sheet is in 1NF. A cell that contained 'Maths, Physics' would have to be split into two rows first."),
        ("p", "**Second normal form** requires 1NF, and every non-key column must depend on the whole key, not on part of it. StudentName depends only on StudentID. SubjectName depends only on SubjectID. Those are partial dependencies. Move them out. Marks depends on the whole key, so it stays."),
        ("table", "After 2NF", ["Table", "Columns", "Key"], [
            ["STUDENT", "StudentID, StudentName, Dept, HOD", "StudentID"],
            ["SUBJECT", "SubjectID, SubjectName", "SubjectID"],
            ["RESULT", "StudentID, SubjectID, Marks", "StudentID + SubjectID"],
        ]),
        ("p", "**Third normal form** requires 2NF, and no non-key column may depend on another non-key column. In STUDENT, HOD depends on Dept, and Dept depends on StudentID. That is a transitive dependency. Move the department out. The curriculum's heading once writes 3NF beside the letters 2NF. Write **3NF** and mean third normal form."),
        ("table", "After 3NF", ["Table", "Columns", "Key"], [
            ["DEPT", "Dept, HOD", "Dept"],
            ["STUDENT", "StudentID, StudentName, Dept", "StudentID, and Dept refers to DEPT"],
            ["SUBJECT", "SubjectID, SubjectName", "SubjectID"],
            ["RESULT", "StudentID, SubjectID, Marks", "StudentID + SubjectID"],
        ]),
        ("p", "Changing the head of Science now changes one row in DEPT, not every student row. That is the practical gain."),
        ("p", "**Integrity constraints** protect that design. A **NOT NULL** constraint refuses an empty student name. A **primary key** refuses a duplicate StudentID and refuses to leave it empty. A **foreign key** refuses a RESULT row whose StudentID is not in STUDENT, and refuses a STUDENT whose Dept is not in DEPT."),
        ("h", "5.3 SQL"),
        ("def", "SQL", "Structured Query Language. The language used to define tables and to retrieve and change the data in a relational database."),
        ("p", "**Projection** chooses columns. **Selection** chooses rows. In SQL the column list after SELECT is the projection, and the WHERE clause is the selection."),
        ("code", "Projection and selection", """SELECT StudentName, Dept
FROM STUDENT;

SELECT StudentName, Dept
FROM STUDENT
WHERE Dept = 'Science';
"""),
        ("p", "The first statement projects two columns of every row. The second also selects the Science rows. Arithmetic in the select list calculates a value: `SELECT Marks, Marks + 5 FROM RESULT`. Comparison operators are `=`, `<>`, `>`, `<`, `>=` and `<=`. Logical operators are `AND`, `OR` and `NOT`."),
        ("p", "An **equijoin** combines rows that have equal key values. A **cross join** combines every row of one table with every row of another and is rarely the result you want. The explicit join and the older WHERE form both appear in classrooms. Know one of them fluently and recognise the other."),
        ("code", "Equijoin of students with their marks", """SELECT STUDENT.StudentName, RESULT.SubjectID, RESULT.Marks
FROM STUDENT
INNER JOIN RESULT
ON STUDENT.StudentID = RESULT.StudentID
WHERE RESULT.Marks >= 50;
"""),
        ("code", "Create, insert, update and delete", """CREATE TABLE STUDENT (
    StudentID VARCHAR(6) PRIMARY KEY,
    StudentName VARCHAR(40) NOT NULL,
    Dept VARCHAR(20)
);

INSERT INTO STUDENT (StudentID, StudentName, Dept)
VALUES ('S1', 'Ayesha', 'Science');

UPDATE STUDENT
SET Dept = 'Arts'
WHERE StudentID = 'S1';

DELETE FROM STUDENT
WHERE StudentID = 'S1';

DROP TABLE STUDENT;
"""),
        ("p", "Microsoft Access uses the same SELECT, WHERE, INSERT, UPDATE and DELETE ideas. In Access query criteria the wildcard for a pattern is often `*`, while standard SQL uses `%` with LIKE. Use the form your lab software accepts, and name the operation correctly in the written paper."),
        ("h", "5.4 Designing the library"),
        ("ol", [
            "Purpose: record books, members and which member has which book.",
            "Tables: BOOK, MEMBER and ISSUE. ISSUE is needed because borrowing is many-to-many over time.",
            "Fields: BOOK has BookID, Title, Author and Subject. MEMBER has MemberID, MemberName and Class. ISSUE has IssueID, BookID, MemberID, IssueDate and ReturnDate.",
            "Unique fields: BookID, MemberID and IssueID are the primary keys.",
            "Relationships: ISSUE.BookID refers to BOOK. ISSUE.MemberID refers to MEMBER. Each relationship is many issues to one book or one member, and the design is in 3NF because names and titles are not repeated on every loan.",
            "Refine: a ReturnDate may be empty while the book is out, so that column allows null. BookID on a loan must not be null.",
        ]),
        ("tip", "If the long question is the library, draw three rectangles, two relationships, the primary keys underlined, and the foreign keys marked FK. Then write one SELECT that lists the member name and the book title for loans not yet returned."),
    ],
    "terms": [
        ["DBMS", "Software that manages a shared, structured collection of related data."],
        ["Schema", "The design of the database."],
        ["Primary key", "The column or columns that identify one row."],
        ["Foreign key", "A column that refers to a primary key in another table."],
        ["1NF", "Atomic values, with no repeating group."],
        ["2NF", "1NF, and no partial dependency on a composite key."],
        ["3NF", "2NF, and no transitive dependency."],
        ["Selection", "Choosing rows, written with WHERE."],
        ["Projection", "Choosing columns, written in the SELECT list."],
    ],
    "summary": [
        "A DBMS shares related data with control of redundancy, integrity and security.",
        "External, conceptual and physical levels separate the user's view from storage.",
        "ER diagrams use rectangles, ovals and diamonds. Tables then receive keys.",
        "1NF, 2NF and 3NF remove repeating groups, partial dependencies and transitive dependencies.",
        "SQL selects, projects, joins, inserts, updates and deletes.",
    ],
    "labs": [
        "Create the STUDENT table, then alter it by adding a column, and drop a practice table you no longer need.",
        "Insert, update and delete rows.",
        "Write SELECT statements that filter with WHERE, compare numbers, and join STUDENT to RESULT.",
    ],
    "mcqs": [
        {"q": "A primary key:", "options": ["Identifies one row and does not repeat", "Must be a picture", "Is always a foreign key of the same table only", "Replaces the DBMS"], "a": "A", "why": "The primary key uniquely identifies a tuple."},
        {"q": "Third normal form removes:", "options": ["Transitive dependencies", "All tables", "The need for a key", "Hardware"], "a": "A", "why": "3NF removes non-key columns that depend on other non-key columns."},
        {"q": "WHERE in SQL performs:", "options": ["Selection of rows", "Projection only, with no row test", "A flowchart", "Inheritance"], "a": "A", "why": "WHERE filters rows. The column list projects columns."},
        {"q": "A foreign key:", "options": ["Refers to a primary key, usually of another table", "Is a monitor port", "Deletes the schema by itself", "Is a wireless cell"], "a": "A", "why": "The foreign key implements a relationship."},
        {"q": "The external level of a database is:", "options": ["A user's view of part of the data", "The physical placement on disk", "A C++ destructor", "A bus topology"], "a": "A", "why": "The external level is the view level."},
        {"q": "INSERT is used to:", "options": ["Add a row", "Draw an entity oval", "Boot the operating system", "Measure a nibble"], "a": "A", "why": "INSERT is the DML statement that adds data."},
        {"q": "Many-to-many in a library loan is stored with:", "options": ["A junction table such as ISSUE", "A single cell listing every book", "No table at all", "A pointer only"], "a": "A", "why": "A junction table holds one row per loan and carries both foreign keys."},
        {"q": "NOT NULL means:", "options": ["The column must contain a value", "The table is secret", "The column is a flowchart", "The row is a topology"], "a": "A", "why": "NOT NULL is an integrity constraint that rejects an empty value."},
    ],
    "shorts": [
        {"q": "Differentiate a flat file and a database.", "a": "A flat file stores records in one file, and the same fact is often copied onto many rows. A database, managed by a DBMS, stores related tables, reduces that repetition, enforces keys and lets several programs share one controlled copy. A change to a student's name can be made once in the student table."},
        {"q": "Define primary key and foreign key.", "a": "A primary key is a column or group of columns that identifies one row and cannot be duplicated or left empty. A foreign key is a column that stores the primary key of a row in another table, which creates the relationship. ISSUE.MemberID is a foreign key referring to MEMBER.MemberID."},
        {"q": "State the rule of each normal form.", "a": "1NF: each value is atomic and there is no repeating group. 2NF: the table is in 1NF and every non-key column depends on the whole key. 3NF: the table is in 2NF and no non-key column depends on another non-key column."},
        {"q": "Differentiate selection and projection.", "a": "Selection chooses rows that meet a condition, written with WHERE. Projection chooses columns, written as the list after SELECT. SELECT StudentName FROM STUDENT WHERE Dept = 'Science' does both: it projects StudentName and selects the Science rows."},
        {"q": "What is an equijoin?", "a": "An equijoin combines rows from two tables when related columns are equal, typically a foreign key and a primary key. STUDENT joined to RESULT on StudentID produces one row for each result, carrying the student's name. A cross join has no such condition and pairs every row with every row."},
    ],
    "longs": [
        {"q": "Explain the three levels of abstraction, ER diagrams and normalisation up to 3NF.", "points": [
            "Describe external, conceptual and physical levels.",
            "Draw or describe entity, attribute and relationship symbols, with BOOK, MEMBER and ISSUES.",
            "Define 1NF, 2NF and 3NF.",
            "Walk the student-subject example: partial dependency out at 2NF, HOD out at 3NF.",
            "Name primary key, foreign key and NOT NULL on the finished tables.",
        ]},
        {"q": "Design a library database and write SQL to create a table and to list books on loan.", "points": [
            "State the purpose and the three tables BOOK, MEMBER and ISSUE.",
            "Give the columns and the primary and foreign keys.",
            "Justify 3NF: title and member name are not repeated on every loan.",
            "Write CREATE TABLE for MEMBER or BOOK.",
            "Write a SELECT with a join that shows member name and book title where ReturnDate is null.",
        ]},
    ],
})

REST.append({
    "grade": "XII",
    "unit": "6",
    "kicker": "Class XII  |  Unit 6  |  weight 15%",
    "title": "Introduction to multimedia",
    "weight": "15%",
    "periods": "20 theory periods and 20 lab periods",
    "intro": "Multimedia is the use of more than one medium, such as text, picture, sound and moving image, in one presentation. This lecture names the parts, the file types, the software, and the steps that produce a short video.",
    "slos": [
        "Define multimedia and explain its importance.",
        "Describe text, graphics, animation, audio and video, and name file types for each.",
        "Distinguish web-based and non-web multimedia applications, and name editing tools.",
        "Use the ideas of scene, layer and keyframe, and describe export and sharing.",
    ],
    "path": [
        "Play a one-minute clip and ask students to name every medium they can see or hear.",
        "Attach a file extension to each medium before opening the editor.",
        "Build a 20-second version in the lab first. The curriculum's two-minute video is the full project.",
    ],
    "sections": [
        ("h", "6.1 What multimedia is"),
        ("def", "Multimedia", "The combination of two or more media, such as text, graphics, animation, audio and video, in a single digital presentation."),
        ("p", "A textbook page of plain text is one medium. A lesson that shows a labelled diagram, speaks the definition and plays a short clip is multimedia. Colleges use it for lessons, laboratory briefings and presentations. It helps a learner who follows a picture more easily than a paragraph, and it lets one package carry the explanation, the example and the sound."),
        ("ul", [
            "A difficult process can be shown as well as described.",
            "The same lesson can be watched again.",
            "Text can be searched, while the picture carries the part that is hard to search.",
            "A presentation can serve a class in the room and a class joining over a network.",
        ]),
        ("h", "6.2 Components and file types"),
        ("table", "The five components", ["Component", "What it contributes", "File types to remember"], [
            ["Text", "Titles, labels and definitions", "txt, doc, pdf"],
            ["Graphics", "Still pictures and diagrams", "jpg, png, gif"],
            ["Animation", "A sequence of drawn or generated frames", "gif, and video formats that hold the result"],
            ["Audio", "Speech, music and effects", "mp3, wav"],
            ["Video", "Moving pictures, usually with sound", "mp4, avi"],
        ]),
        ("p", "GIF can be a still picture or a short animation. PNG keeps sharp diagrams and can include transparency. JPEG suits photographs and is lossy: it saves space by discarding some detail. WAV is a full recorded waveform and is large. MP3 is compressed audio. MP4 is the usual container for a finished student video. Use these names in answers even if the lab also produces other types."),
        ("h", "6.3 Applications and packages"),
        ("p", "A **web-based** multimedia application runs in a browser or is delivered as a site: an online lesson, a video page, an interactive diagram. A **non-web** application runs as a program on the computer: a slide show, a video editor, a player. The curriculum names packages such as ProShow Gold for photo and slide video, and JetAudio for playing and working with audio. Current labs often use OpenShot or Shotcut for video and Audacity for sound. Name the curriculum examples, and also name the tool you actually used in the practical."),
        ("h", "6.4 Making the video"),
        ("def", "Scene or canvas", "The frame in which you place the parts of the presentation. It is the visible area the viewer will see."),
        ("def", "Layer", "One level of content stacked with others. A background image can sit on a lower layer and a title on a higher layer, so the title remains editable on its own."),
        ("def", "Keyframe", "A frame in which you set a property, such as position or size. The software creates the in-between frames, which produces the motion."),
        ("ol", [
            "Open a new project and set the canvas to a standard frame such as 1280 by 720.",
            "Import or record the pictures, the voice and any existing clip. Keep the source files in one project folder.",
            "Place the background on a lower layer and titles and labels on higher layers.",
            "Set keyframes where an object should start and where it should finish. Keep motion slow enough to read.",
            "Record or import narration. Match the length of each sentence to the picture it describes.",
            "Watch the whole piece from the start and repair a wrong order before you export.",
            "Export to MP4 for sharing, and keep a second export such as AVI if the question asks for more than one format.",
            "Upload the finished file to the sharing place your college uses, or to a video site the teacher names, and send the link to the class. Respect the privacy of any person who appears in the clip, and use only pictures and music you have the right to use.",
        ]),
        ("p", "The curriculum project is a video of about two minutes on a topic from this course, for example the OSI layers or the states of a process. Two minutes is long enough to need a plan and short enough to finish in the lab periods."),
        ("note", "Plan the two minutes on paper first: four scenes of about 30 seconds. Scene 1 states the definition. Scene 2 labels a diagram. Scene 3 gives an example. Scene 4 repeats the definition in one sentence. Then open the editor."),
    ],
    "terms": [
        ["Multimedia", "More than one medium combined in one presentation."],
        ["Graphics", "Still images."],
        ["Animation", "Change across frames that creates the sense of motion."],
        ["Layer", "A separate level of content stacked in a scene."],
        ["Keyframe", "A frame where a property is set so the software can fill the frames between."],
        ["Export", "Saving the finished project as a playable file such as MP4."],
    ],
    "summary": [
        "Multimedia combines text, graphics, animation, audio and video.",
        "Learn one file type for each component.",
        "Web applications are delivered in the browser. Desktop editors such as a video or audio package are non-web applications.",
        "A scene holds layers. Keyframes set motion. Export, then share with permission to use the material.",
    ],
    "labs": [
        "Place a title and an imported image on separate layers and save the picture in two formats.",
        "Import one audio file and one image into one project.",
        "Add two keyframes that move a label across the canvas.",
        "Produce a short video, export it as MP4, and show the file to your teacher. Build toward the two-minute piece.",
    ],
    "mcqs": [
        {"q": "Multimedia means:", "options": ["Using more than one medium together", "Using only plain text", "A type of RAM", "A bus topology"], "a": "A", "why": "The word names a combination of media."},
        {"q": "Which extension is typical of a photograph?", "options": ["jpg", "mp3", "txt only", "sql"], "a": "A", "why": "JPEG is a common photographic image format."},
        {"q": "A keyframe is:", "options": ["A frame where you set a property for the animation", "A primary key", "A keyboard port", "An operating system"], "a": "A", "why": "The editor interpolates between keyframes."},
        {"q": "A layer is used so that:", "options": ["Parts of a scene can be edited separately", "RAM is refreshed", "A file is binary", "A pointer is declared"], "a": "A", "why": "Stacked layers keep the title independent of the background."},
        {"q": "MP3 is:", "options": ["Compressed audio", "A still photograph standard", "A C++ keyword", "A normal form"], "a": "A", "why": "MP3 is an audio format."},
        {"q": "A web-based multimedia application:", "options": ["Is delivered through a browser or the web", "Cannot contain sound", "Is always stored in ROM", "Replaces the DBMS"], "a": "A", "why": "Web-based means the user reaches it through the web."},
        {"q": "Exporting a video means:", "options": ["Saving the finished presentation as a playable file", "Deleting the project", "Printing the motherboard", "Normalising a table"], "a": "A", "why": "Export produces the file you can play or upload."},
        {"q": "PNG is most suitable in class for:", "options": ["A sharp diagram", "A database key", "A process state only", "A twisted-pair cable"], "a": "A", "why": "PNG keeps crisp edges, which suits diagrams and text in pictures."},
    ],
    "shorts": [
        {"q": "Define multimedia and give two advantages.", "a": "Multimedia combines two or more media, such as text, sound and video, in one presentation. It can show a process that is hard to follow from text alone, and the learner can play the lesson again. A labelled diagram with a spoken definition is a simple example."},
        {"q": "Name the five components and one file type for each.", "a": "Text uses txt or pdf. Graphics use jpg or png. Animation may use gif. Audio uses mp3 or wav. Video uses mp4 or avi. The component is the kind of content. The file type is how that content is stored."},
        {"q": "Differentiate a web-based and a non-web multimedia application.", "a": "A web-based application is reached through a browser, such as an online lesson with video. A non-web application is a program on the computer, such as a video editor or a desktop player. Both can contain the same five components. They differ in how the user starts them."},
        {"q": "Define scene, layer and keyframe.", "a": "The scene or canvas is the visible frame. A layer is one stacked level of content, so a title can sit above a picture. A keyframe is a frame where a property such as position is set. The software fills in the frames between keyframes to make movement."},
        {"q": "Why keep source files in one folder before exporting?", "a": "The project refers to the imported pictures and sounds by their location. If a file is moved, the editor cannot find it and the export is incomplete. One project folder keeps the path stable until the video has been exported."},
    ],
    "longs": [
        {"q": "Explain the components of multimedia and the file types used to store them.", "points": [
            "Define multimedia and give its importance in one short paragraph.",
            "Explain text, graphics, animation, audio and video, each with a classroom example.",
            "Attach at least one file type to each, and say when jpg is a better photo format than png is for a diagram, or keep the comparison inside the graphics row.",
            "Distinguish a web delivery and a desktop package, naming one package.",
        ]},
        {"q": "Describe how you would make a two-minute educational video and share it.", "points": [
            "Plan four short scenes on a syllabus topic.",
            "Set the canvas, import media, and arrange layers.",
            "Use keyframes for one simple movement and add narration.",
            "Export to MP4 and name a second format.",
            "Upload or share the file with the teacher's method, and use only material you have permission to use.",
        ]},
    ],
})

REST.append({
    "grade": "XII",
    "unit": "7",
    "kicker": "Class XII  |  Unit 7  |  weight 10%",
    "title": "Wireless and mobile communication",
    "weight": "10%",
    "periods": "15 theory periods",
    "intro": "Wireless communication carries data without a cable between the devices. Mobile communication is wireless communication that continues while the user moves. This lecture compares the short-range technologies, the satellite orbits, and the cellular network that a phone actually uses.",
    "slos": [
        "Define wireless and mobile communication and the basic radio terms.",
        "Compare Wi-Fi, WiMAX, Bluetooth, infrared and microwave on range, speed and frequency.",
        "Describe long-distance wireless links and the GEO, MEO and LEO orbits.",
        "Explain cells, base stations, frequency reuse, MSC and BTS.",
        "Describe the generations of mobile networks and distinguish a fixed ad hoc network from a MANET.",
    ],
    "path": [
        "Separate wireless from mobile with two examples: a fixed microwave link, and a phone in a moving bus.",
        "Put the short-range table on one board. It is a favourite short question.",
        "Draw three hexagons, a BTS in each, and one MSC. Then attach the generations to that drawing.",
    ],
    "sections": [
        ("h", "7.1 Terms"),
        ("def", "Wireless communication", "Communication that uses electromagnetic waves rather than a cable between the sender and the receiver."),
        ("def", "Mobile communication", "Wireless communication that allows the user to move and to keep the connection, typically through a cellular network."),
        ("ul", [
            "The **frequency spectrum** is the range of frequencies available for radio signals. Different services are given different bands so they do not all talk on top of each other.",
            "A **radio signal** is the electromagnetic wave that carries the data.",
            "A **radio transceiver** both transmits and receives. A phone contains one. The name joins transmitter and receiver.",
            "An **access point** is the device that joins wireless users to a wired network. A home or lab Wi-Fi box is an access point, often combined with a router.",
            "**Line of sight** means the path between two antennas is clear. Microwave links need it. A hill or a building in the path interrupts them.",
        ]),
        ("h", "7.2 Short-range technologies"),
        ("p", "The figures below are the textbook comparisons used for this unit. A particular product can differ. In an answer, the order matters more than a single brand's specification: Bluetooth is personal, Wi-Fi is a room or a building, WiMAX was designed for a city, infrared is a short beam, and microwave can jump between distant towers when the path is clear."),
        ("table", "Short-distance wireless technologies", ["Technology", "Typical range", "Speed in this comparison", "Frequency band"], [
            ["Bluetooth", "About 10 metres, more for some classes", "Lower than Wi-Fi, enough for headsets and small file transfers", "2.4 GHz"],
            ["Infrared", "About a metre to a few metres, and only in a clear beam", "Low, suitable for a remote control or a short link", "Infrared light, above radio frequencies"],
            ["Wi-Fi", "Tens of metres indoors, more in the open", "High, from many megabits per second upward", "2.4 GHz and 5 GHz"],
            ["Microwave", "Kilometres between aligned antennas", "High on a point-to-point link", "Microwave bands, and the path must be line of sight"],
            ["WiMAX", "A metropolitan area, up to tens of kilometres in the design", "Broadband, lower or comparable to later Wi-Fi in practice", "Licensed bands around 2 to 11 GHz in the original designs"],
        ]),
        ("h", "7.3 Long distance and satellites"),
        ("p", "Long-distance wireless communication crosses cities, countries or oceans by radio towers, microwave chains or satellites. A satellite receives a signal on one frequency, the uplink, and sends it back toward Earth on another, the downlink. The height of the orbit decides the delay, the coverage and the number of satellites needed."),
        ("table", "Orbits used with satellite communication and navigation", ["Orbit", "Height and behaviour", "What to remember"], [
            ["GEO, geostationary", "About 36,000 km above the equator. The orbital period matches the Earth's rotation, so the satellite stays over the same region.", "One satellite covers a large fixed area. The signal has a noticeable delay. Weather and television links use this idea."],
            ["MEO, medium Earth orbit", "Roughly 2,000 to 20,000 km.", "Navigation constellations such as GPS use MEO, around 20,000 km. Coverage of the globe needs a group of satellites, fewer than a low orbit needs."],
            ["LEO, low Earth orbit", "Below about 2,000 km.", "The delay is smaller and the satellite moves quickly across the sky. Continuous coverage needs many satellites. The curriculum's phrase 'types of GPS' is answered with these three orbits, and you should add that the GPS constellation itself flies in MEO."],
        ]),
        ("h", "7.4 The cellular network"),
        ("diagram", "cellular", "Figure 7.1  Cells, a base transceiver in each, and a mobile switching centre.", 62 * mm),
        ("ul", [
            "A **cell** is the area served by one base station. Diagrams draw it as a hexagon so the cells tile a map.",
            "A **base transceiver station (BTS)** is the radio equipment and antenna in that cell. It is the part the phone talks to.",
            "A **base station** is the broader name for the equipment that serves a cell, including the BTS and its controller.",
            "**Frequency reuse** means the same channel frequencies can be used again in cells that are far enough apart. Neighbouring cells use different frequencies so their calls do not collide. That reuse is why a limited spectrum can serve a whole city.",
            "The **mobile switching centre (MSC)** connects cells to each other and to the ordinary telephone network. It tracks which cell a phone is in and supports the handover when a caller crosses a boundary.",
            "The **interface between cells** is the handover: the call is passed from one base station to the next while the conversation continues.",
        ]),
        ("h", "7.5 Generations"),
        ("p", "Each generation is a family of technologies for the cellular network. The 2019 curriculum pairs the names as 2G (GSM), 3G (GPRS), 4G (LTE) and 5G. Write those pairs if the question uses them. For a precise answer, add the engineering names: GSM is 2G voice and digital service, GPRS is the packet-data step often called 2.5G, 3G is the UMTS family, 4G is LTE, and 5G is the following generation. The curriculum's bracket '5G (Future)' reflects the year of the curriculum. 5G networks have since been deployed in many countries. What you should say about 5G is that it is designed for higher data rates and lower delay than LTE, and for a much larger number of connected devices."),
        ("table", "Generations", ["Name in the question", "What the user gained"], [
            ["2G GSM", "Digital mobile calls and text messages."],
            ["GPRS, listed with 3G in the curriculum note", "Packet data over the mobile network, so the phone could carry internet traffic. Technically this step is 2.5G, and 3G then raised the data rate further."],
            ["4G LTE", "Much higher data rates for video and ordinary internet use on the phone."],
            ["5G", "A further rise in rate and a fall in delay, and support for many more devices."],
        ]),
        ("h", "7.6 Ad hoc networks"),
        ("def", "Ad hoc network", "A network formed by devices that communicate directly and cooperate to forward data, without depending on fixed infrastructure such as an access point or a base station."),
        ("p", "A **fixed ad hoc network** is set up for a time among nodes that do not move, for example laptops in a hall that forward for one another. A **mobile ad hoc network (MANET)** is an ad hoc network whose nodes move. Routes change as devices come and go, so the network has to rediscover paths. A disaster team whose radios form a network without a tower is the example to give."),
        ("tip", "Keep three comparisons ready: Wi-Fi with Bluetooth, GEO with LEO, and a cellular network with a MANET. Each is a 3-mark table."),
    ],
    "terms": [
        ["Wireless", "Communication by electromagnetic waves, without a data cable between the ends."],
        ["Access point", "A device that connects wireless stations to a network."],
        ["Line of sight", "A clear path between antennas."],
        ["Cell", "The geographic area served by one base station."],
        ["BTS", "The radio transmitter and receiver that serves a cell."],
        ["MSC", "The switch that connects cells and handles handover."],
        ["GEO", "A geostationary orbit, fixed relative to the ground."],
        ["MANET", "A mobile ad hoc network, with moving nodes and no fixed infrastructure."],
    ],
    "summary": [
        "Wireless removes the cable. Mobile communication also survives movement.",
        "Bluetooth, infrared, Wi-Fi, microwave and WiMAX differ in range, speed and band.",
        "GEO stays over one region at great height. GPS uses MEO. LEO needs many fast-moving satellites.",
        "A cellular network reuses frequencies across cells and hands a call over at the boundary through the MSC.",
        "GSM, GPRS, LTE and 5G are the generation story. An ad hoc network has no fixed base station. A MANET also has moving nodes.",
    ],
    "labs": [
        "From the lab Wi-Fi, identify the access point name and compare its range with a Bluetooth headset in the same room.",
        "Draw a three-cell sketch of the college area and mark where a handover would happen if a caller walked between them.",
    ],
    "mcqs": [
        {"q": "A transceiver:", "options": ["Transmits and receives", "Only prints", "Stores a primary key", "Compiles C++"], "a": "A", "why": "The device combines a transmitter and a receiver."},
        {"q": "Infrared communication typically requires:", "options": ["A short, clear beam", "A geostationary satellite", "A coaxial backbone across a city", "An MSC"], "a": "A", "why": "Infrared is short range and does not pass through walls."},
        {"q": "Wi-Fi is described by the family:", "options": ["IEEE 802.11", "ASCII", "1NF", "BIOS"], "a": "A", "why": "IEEE 802.11 is the wireless LAN standard behind Wi-Fi."},
        {"q": "A geostationary satellite:", "options": ["Stays over the same region of the Earth", "Orbits inside the classroom", "Is a type of RAM", "Replaces the SIM card"], "a": "A", "why": "Its period matches the Earth's rotation."},
        {"q": "GPS satellites operate in:", "options": ["Medium Earth orbit", "The CMOS battery", "A register of the CPU", "A text file"], "a": "A", "why": "The GPS constellation uses MEO."},
        {"q": "Frequency reuse in cellular networks allows:", "options": ["The same frequencies to be used again in distant cells", "One frequency for the entire world with no planning", "Removal of the need for a phone", "Text files to become binary"], "a": "A", "why": "Cells far apart can reuse channels, which multiplies capacity."},
        {"q": "The MSC is responsible for:", "options": ["Switching calls and supporting handover between cells", "Erasing EPROM", "Compiling a class", "Drawing a flowchart oval"], "a": "A", "why": "The mobile switching centre connects the cells and the wider telephone network."},
        {"q": "A MANET differs from a fixed ad hoc network because:", "options": ["Its nodes move", "It uses only fibre", "It is a normal form", "It cannot forward data"], "a": "A", "why": "MANET means a mobile ad hoc network."},
    ],
    "shorts": [
        {"q": "Differentiate wireless communication and mobile communication.", "a": "Wireless communication sends data by electromagnetic waves without a cable between the ends. A fixed microwave link is wireless and the ends stay still. Mobile communication is wireless communication that continues while the user moves, as in a cellular phone call. Mobile communication is therefore a moving form of wireless communication."},
        {"q": "Compare Wi-Fi and Bluetooth on range and use.", "a": "Bluetooth is a short personal link, about 10 metres, used for a headset or a small accessory, in the 2.4 GHz band. Wi-Fi covers a room or a building, carries much more data, and joins devices to a local network through an access point, using 2.4 GHz or 5 GHz. Wi-Fi is the network. Bluetooth is the short personal connection."},
        {"q": "Differentiate GEO and LEO.", "a": "A GEO satellite orbits at about 36,000 km and stays over one region, so a fixed dish can use it, at the cost of a longer delay. A LEO satellite orbits below about 2,000 km, moves quickly across the sky and has a shorter delay. Continuous service from LEO needs a large constellation."},
        {"q": "What is a cell, and why do neighbouring cells use different frequencies?", "a": "A cell is the area covered by one base station. Neighbouring cells use different frequencies so that calls near the boundary do not interfere. The same frequency can be reused in a cell that is farther away. That is frequency reuse."},
        {"q": "Define an ad hoc network and a MANET.", "a": "An ad hoc network is formed by devices that talk directly and forward data for one another, without a fixed access point or base station. A MANET is an ad hoc network whose nodes move, so the routes have to be found again as the topology changes."},
    ],
    "longs": [
        {"q": "Explain the parts of a cellular network and the idea of frequency reuse and handover.", "points": [
            "Define wireless and mobile communication.",
            "Define cell, BTS, base station and MSC, and describe how a phone reaches the wider network.",
            "Explain frequency reuse with neighbouring cells on different channels.",
            "Explain handover as the caller crosses a cell boundary.",
            "Add one sentence on 2G, 4G and 5G so the network has a technology as well as a map.",
        ]},
        {"q": "Compare short-distance wireless technologies and the three satellite orbits.", "points": [
            "Give the comparison table for Bluetooth, infrared, Wi-Fi, microwave and WiMAX: range, speed and frequency.",
            "Define line of sight and attach it to microwave and infrared.",
            "Describe GEO, MEO and LEO with height and one use.",
            "State that GPS flies in MEO.",
            "Close with the access point as the device that joins a short-range Wi-Fi user to the wired network.",
        ]},
    ],
})
