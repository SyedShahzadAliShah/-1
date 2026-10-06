from lecture_helpers import (
    array,
    board,
    bullet,
    chapter,
    chips,
    code,
    cols,
    flow,
    formula,
    kmap,
    layers,
    lecture,
    note,
    steps,
    table,
    title,
)


def chapters():
    return [
        chapter("xii-ch1", 1, "Computer Systems and HCI", [
            lecture("xii-hci", "People, tasks, and natural input", True, [
                board(
                    """
                    Human-computer interaction studies how a person and a computer system work
                    together to finish a task. The computer is not the whole story. The person's
                    goal, the device, and the place all matter. A timetable app that is clear on
                    a laptop can fail on a phone in bright sun. HCI asks you to design for that
                    real moment, not for a perfect demo.
                    """,
                    title("What HCI studies"),
                    chips("Person", "Task", "Device", "Place"),
                    note("If you cannot name the task, you cannot judge the interface."),
                ),
                board(
                    """
                    Traditional interaction uses a keyboard, a mouse, and menus. The person learns
                    the computer's language. Natural interaction tries to meet the person's body:
                    touch, speech, a pen, or a gesture. Touch is natural for a photo, and clumsy
                    for a long essay. Speech is useful when hands are busy, and weak in a noisy
                    corridor. Natural does not mean always better. It means matched to the task.
                    """,
                    title("Traditional and natural"),
                    cols(
                        "Traditional",
                        ["Keyboard and mouse", "Precise", "Needs training"],
                        "Natural",
                        ["Touch, speech, pen", "Fast to start", "Can be ambiguous"],
                    ),
                ),
                board(
                    """
                    HCI shows up anywhere a person must operate a system: a hospital screen, an
                    ATM, a class quiz, a farmer's moisture app. The same principles travel. Make
                    the next step obvious, let people undo, and speak their language. A career in
                    this area can be interface design, user research, or front-end building. All
                    of them start by watching a real user struggle.
                    """,
                    title("Domains and the habit"),
                    note("Watch one person try the task before you add another button.", "blue"),
                ),
            ]),
            lecture("xii-components", "Parts of an interaction", True, [
                board(
                    """
                    An interaction has a user, a task, an interface, and feedback. The interface
                    is the part the user can perceive and operate: buttons, words, sounds. Feedback
                    tells the user what just happened. A save button that does not change is a
                    broken interaction even if the file was saved. The environment matters too.
                    Gloves, glare, and a crowded desk change what is usable.
                    """,
                    title("User, interface, feedback"),
                    flow("User goal|io", "Control on the interface|process", "System acts|process", "Feedback the user notices|term"),
                ),
                board(
                    """
                    Interfaces take different forms. A command line asks for typed commands. A
                    graphical interface offers windows and icons. A touch interface uses fingers.
                    A conversational interface uses turns of speech or chat. Pick the form from the
                    task and the place. Issuing a one-time campus card in a noisy hall is a poor
                    match for a voice-only screen.
                    """,
                    title("Interface forms"),
                    chips("Command", "Graphical", "Touch", "Conversation"),
                    note("The environment can rule out an interface that looked fine indoors.", "red"),
                ),
                board(
                    """
                    Feedback should be timely and in the same place as the action. If a form field
                    is invalid, mark that field, not a mystery banner at the top after a delay.
                    Progress matters for slow work: show that the upload is moving. Silence makes
                    people press the button again, which often makes the problem worse.
                    """,
                    title("Feedback people can trust"),
                    note("Same place, soon, and honest. Do not say saved if it is only queued.", "green"),
                ),
            ]),
            lecture("xii-access-need", "Accessibility and need analysis", True, [
                board(
                    """
                    Accessibility means a person with a disability can complete the same task.
                    Practical checks for this course: text can be read by a screen reader, the
                    action can be done without a precise mouse, color is not the only signal,
                    and captions exist for speech. Low vision, deafness, and motor difficulty
                    are different barriers. One giant button does not solve all three.
                    """,
                    title("Accessibility checks"),
                    steps(
                        "Name the barrier",
                        "Offer a second way to do the action",
                        "Do not rely on color alone",
                        "Caption speech and label icons",
                    ),
                    note("Keyboard access helps more people than the one student you pictured.", "gold"),
                ),
                board(
                    """
                    Need analysis happens before you decorate a screen. Who is the user? What task
                    must finish? Where are they? What device do they actually have? What must never
                    happen? A canteen screen used by a queue in three minutes cannot ask for a long
                    account setup. Write those answers in sentences. They become the requirements
                    the interface is judged against.
                    """,
                    title("Need analysis"),
                    chips("Who", "What task", "Where", "Which device", "What must not fail"),
                ),
                board(
                    """
                    A short worked need: Class 12 students booking a lab seat between periods.
                    Users are in a hurry and on phones. The task is reserve one free seat for
                    today. The place is a corridor. Failure would be double-booking the same seat.
                    The interface should show free seats first and confirm the seat number in large
                    text. Login can wait if the school already knows the class list.
                    """,
                    title("Lab seats, analyzed"),
                    note("The need decides the screen. The screen does not decide the need.", "green"),
                ),
            ]),
            lecture("xii-problems", "HCI problems and improvements", False, [
                board(
                    """
                    Common HCI problems are overload, inconsistency, poor feedback, and language
                    the user does not use. Overload is twenty actions on one screen when the task
                    needs two. Inconsistency is Save on one screen and Commit on the next for the
                    same idea. Jargon such as null pointer on a student's form is a design bug,
                    even if it is a true technical message.
                    """,
                    title("How interfaces fail"),
                    chips("Too much", "Inconsistent words", "No feedback", "Expert jargon"),
                    note("If two screens mean the same action, use the same word.", "red"),
                ),
                board(
                    """
                    Improve an interface by removing steps, grouping related fields, writing labels
                    as actions, and testing with the actual user. Heuristic review is a checklist
                    pass you can do at your desk. A usability test is better: give a person the task
                    and stay quiet while they try. Their confusion is data. Do not explain the
                    button during the test. Fix the button after.
                    """,
                    title("Improve, then test"),
                    steps("Cut steps that are not the task", "Group what belongs together", "Watch a user in silence", "Fix the point where they stopped"),
                ),
                board(
                    """
                    A before-and-after sentence earns marks. Before: students typed a device code
                    from a sticker they could not see. After: the screen lists device names and
                    the code is secondary. You improved the interface because you removed a reading
                    barrier. That is HCI, not decoration.
                    """,
                    title("Write the before and after"),
                    cols("Before", ["Hidden code", "User guesses"], "After", ["Visible name", "Code still stored"]),
                ),
            ]),
            lecture("xii-uiux", "UI, UX, wireframes, and tests", True, [
                board(
                    """
                    The user interface is what the person sees and touches: layout, words, controls.
                    The user experience is the whole path, including waiting, errors, trust, and
                    whether the task felt worth it. A beautiful screen with a confusing sequence
                    is a weak experience. A plain screen that finishes the task in one confident
                    minute can be a strong experience. Do not use the two words as synonyms.
                    """,
                    title("UI is not the whole UX"),
                    cols("UI", ["Screens", "Controls", "Visual design"], "UX", ["The full task", "Waiting and errors", "Whether they would return"]),
                ),
                board(
                    """
                    A wireframe is a line drawing of a screen. Boxes, labels, and arrows. No colors,
                    no photos. Its job is to agree the structure before anyone paints it. A prototype
                    goes further: paper you can point at, or a clickable sequence that still may not
                    save real data. Figma is one tool for digital wireframes. Paper is still legal
                    and often faster for the first pass.
                    """,
                    title("Wireframe, then prototype"),
                    steps("Sketch the screens", "Mark what each button opens", "Try the clicks on paper", "Only then add color"),
                    note("A wireframe argument is cheaper than a coded argument.", "gold"),
                ),
                board(
                    """
                    Evaluation checks whether the design works. A usability test watches people do
                    a set task and records where they hesitate. An A/B test compares two versions
                    on the same task and sees which one succeeds more often. An automated check can
                    catch empty labels or tiny text, but it cannot tell you that the sentence is
                    confusing. Use the automated check as a net, and the human test as the judgment.
                    """,
                    title("Three ways to evaluate"),
                    chips("Usability test", "A/B comparison", "Automated checks"),
                    note("Automated tools do not replace watching a person.", "green"),
                ),
            ]),
        ]),
        chapter("xii-ch2", 2, "Algorithms and Data Structures", [
            lecture("xii-trace", "Trace tables and stepwise reasoning", True, [
                board(
                    """
                    A trace table proves an algorithm by writing the variables after each step.
                    You need one column per variable and one row each time something changes.
                    Stepwise reasoning is the commentary beside that table: why this branch ran.
                    The table is the evidence. The sentences explain the evidence. Exams often want
                    both, because a table with no story can hide a lucky guess.
                    """,
                    title("Evidence and explanation"),
                    cols("Trace table", ["Rows of variable values", "Shows what happened"], "Stepwise reason", ["Which line ran", "Why that branch"]),
                ),
                board(
                    """
                    Trace this total. Set s to 0. For i from 1 to 3, add i into s. Start s is 0.
                    When i is 1, s becomes 1. When i is 2, s becomes 3. When i is 3, s becomes 6.
                    If your table skips the start row, you may still get 6 and not see where a bug
                    entered. Always write the values before the loop as well.
                    """,
                    title("Sum of 1, 2, and 3"),
                    table(
                        ["step", "i", "s"],
                        [["start", "-", "0"], ["add", "1", "1"], ["add", "2", "3"], ["add", "3", "6"]],
                    ),
                    code("s = 0", "for i in range(1, 4):", "    s = s + i"),
                ),
                board(
                    """
                    Use a trace when the question gives code and asks what it prints. Use stepwise
                    reasoning when the question asks you to justify a branch, such as why the else
                    ran. If the input is 4 and the condition is n greater than 5, the else runs
                    because 4 is not greater than 5. Quote the comparison. Do not say it goes to
                    else because of logic.
                    """,
                    title("Match the method to the question"),
                    note("Name the comparison that failed or succeeded.", "green"),
                ),
            ]),
            lecture("xii-clarity", "Modularity and readable algorithms", False, [
                board(
                    """
                    Clarity means another student can check your algorithm without asking you.
                    Modularity helps: split a long method into named parts, such as read marks,
                    compute average, and decide grade. Each part should do one job and have a name
                    that says that job. A module you cannot name is probably two jobs tangled.
                    """,
                    title("One job per part"),
                    steps("Read the marks", "Compute the average", "Map the average to a grade", "Show the grade"),
                    note("A name like doStuff is a sign the part is not clear yet.", "red"),
                ),
                board(
                    """
                    Readability is the local writing. Use the same name for the same idea. Indent
                    nested steps. Prefer a condition a person can read aloud. Avoid a clever trick
                    that saves one line and costs five minutes of confusion. Comments should say
                    why, not repeat the line. If the line is total = total + mark, a comment that
                    says add mark is noise.
                    """,
                    title("Readable lines"),
                    cols("Clear", ["Same name throughout", "Condition in words you can say"], "Unclear", ["Reused temp for three ideas", "A trick with no reason"]),
                ),
                board(
                    """
                    You can judge clarity with a swap test. Hand the pseudocode to a classmate and
                    ask them to trace one input. If they stop to ask what a name means, the
                    algorithm is not clear yet. Fix the name or split the step. Clarity is not
                    decoration added after the code works. It is part of correctness in a team.
                    """,
                    title("The swap test"),
                    note("If a peer cannot trace it, it is not clear.", "green"),
                ),
            ]),
            lecture("xii-bigo", "Steps, conditions, and Big O", True, [
                board(
                    """
                    Efficiency asks how the work grows when the input grows. Count the important
                    steps, not the ink. A loop that runs once per item is linear, Big O of n.
                    A loop inside a loop over the same list is Big O of n squared. Binary search
                    halves the list, so it is Big O of log n. Big O describes the shape of the
                    growth, not the exact millisecond on your laptop.
                    """,
                    title("How work grows"),
                    chips("O(n) one pass", "O(n squared) nested passes", "O(log n) halve each time"),
                    note("Say Big O of n, not the speed of one computer.", "gold"),
                ),
                board(
                    """
                    Also count conditions and repetitions when the course asks for an efficiency
                    frame. A method with five separate if statements may still be linear if each
                    runs once. A method with one if inside two nested loops is the expensive one.
                    Repetition dominates. A clever condition that sits inside a double loop still
                    runs n squared times.
                    """,
                    title("What to count"),
                    table(
                        ["Pattern", "Growth"],
                        [["One loop over n", "O(n)"], ["Loop inside a loop", "O(n squared)"], ["Halve the range", "O(log n)"]],
                    ),
                ),
                board(
                    """
                    Compare two plans for finding a duplicate in a class list. Plan A compares
                    every pair. That is n squared comparisons. Plan B sorts, then checks neighbors
                    once. Sorting costs more than a single pass, but far less than every pair when
                    the class is huge. For thirty students, either plan is fine, and the clearer
                    one wins. Say the size you are judging.
                    """,
                    title("Same job, different growth"),
                    note("State n, then the pattern, then the Big O label.", "green"),
                ),
            ]),
            lecture("xii-refine", "Refine for clarity and cost", False, [
                board(
                    """
                    Refinement improves an algorithm that already works. You may split a step,
                    remove a repeated calculation, or stop early when the answer is known. Keep
                    the result the same. A refinement that changes who passes the course is not a
                    refinement. It is a different problem. Write a trace of the old and the new
                    on one input to show they still agree.
                    """,
                    title("Improve without changing the answer"),
                    steps("Keep a correct version", "Change one thing", "Trace the same input", "Keep the change only if the result matches"),
                ),
                board(
                    """
                    Example. A loop adds marks and also searches for the top mark. That is one
                    pass, which is enough. A first draft that walks the list twice still gets the
                    right totals, but it does extra work. Merging the two walks is a refinement.
                    Naming the pieces average and top is a clarity refinement. Do the clarity one
                    even when the list is short.
                    """,
                    title("One pass, clear names"),
                    code("total = 0", "top = marks[0]", "for m in marks:", "    total = total + m", "    if m > top: top = m"),
                ),
                board(
                    """
                    Stop early is another refinement. Linear search can return the moment the item
                    is found, instead of scanning the rest. Bubble sort can stop if a pass makes
                    no swaps, because the list is already in order. Mention the early stop in the
                    explanation so the reader knows the worst case is still the full scan.
                    """,
                    title("Stop when you already know"),
                    note("Early exit improves the lucky case. The worst case may be unchanged.", "blue"),
                ),
            ]),
            lecture("xii-linear-ds", "Arrays, lists, stacks, and queues", True, [
                board(
                    """
                    A data structure is a way of organizing items so certain operations are natural.
                    An array stores items in a row of slots, usually next to each other, reached by
                    an index starting at 0. A linked list stores items in nodes, and each node points
                    at the next. Arrays make index lookup easy. Linked lists make insert-in-the-middle
                    easier if you already hold the previous node, because you do not slide every later item.
                    """,
                    title("Array and linked list"),
                    cols("Array", ["Index reaches a slot", "Length is often fixed"], "Linked list", ["Node points to next", "Insert by rewiring a pointer"]),
                ),
                board(
                    """
                    A stack is last in, first out. The most recent item leaves first, like a stack
                    of trays. Push adds. Pop removes the top. A queue is first in, first out. The
                    oldest item leaves first, like a canteen line. Enqueue adds at the back.
                    Dequeue removes from the front. Using pop on a queue, or serving the newest
                    person first, breaks the definition.
                    """,
                    title("Stack and queue"),
                    cols("Stack", ["Push on top", "Pop the newest"], "Queue", ["Enqueue at the back", "Dequeue the oldest"]),
                    note("Last in first out is the stack. First in first out is the queue.", "green"),
                ),
                board(
                    """
                    Trace a queue of print jobs. Enqueue Essay, then enqueue Poster. The front is
                    Essay. Dequeue prints Essay. The front is now Poster. A stack of undo actions
                    works the other way. Push type, push delete. Undo pops delete first, because
                    it was last. Choose the structure from the sentence first in or last in.
                    """,
                    title("Trace a short queue"),
                    array(["Essay", "Poster"], hi=[0], caption="Front is Essay"),
                    note("After one dequeue, only Poster remains.", "blue"),
                ),
            ]),
            lecture("xii-trees", "Trees, graphs, and operations", True, [
                board(
                    """
                    A tree is a hierarchy. One root, and every other node has one parent. A folder
                    of folders is a tree. A graph is more general: nodes and edges, and an edge may
                    connect any pair. A road map is a graph, because a town can have many roads and
                    there may be a loop. If your picture has two parents for one node, it is not a
                    pure tree.
                    """,
                    title("Tree and graph"),
                    cols("Tree", ["One root", "One parent each", "No loops"], "Graph", ["Any connections", "Loops allowed", "A map of roads"]),
                ),
                board(
                    """
                    Common operations are insert, delete, search, and traverse. Traverse means visit
                    every node in a disciplined order. On an array, search by index is direct. On a
                    linked list, search walks next pointers from the head. On a queue, you normally
                    do not pull an item from the middle. If the problem needs middle access, a queue
                    is the wrong structure.
                    """,
                    title("Operations"),
                    chips("Insert", "Delete", "Search", "Traverse"),
                    note("Pick the structure whose cheap operation is the one you do most.", "gold"),
                ),
                board(
                    """
                    Match problems to structures. Browser back button: stack. Printer line: queue.
                    Student marks looked up by roll number index: array. A family chart with one
                    parent link in the simplified task: tree. Bus routes between towns: graph.
                    Say the operation that convinced you. The canteen serves whoever has waited
                    longest, so the structure is a queue.
                    """,
                    title("Which structure fits?"),
                    chips("Back button: stack", "Fair line: queue", "Index: array", "Routes: graph"),
                    note("The fairness rule first in, first out is the clue for a queue.", "green"),
                ),
            ]),
            lecture("xii-retrieve", "Tracing retrieval", False, [
                board(
                    """
                    Retrieval means getting a stored item back. In an array, compute the index and
                    read that slot. If marks are stored at indexes 0, 1, and 2, the second student
                    is index 1, not index 2. In a linked list, start at the head and follow next
                    until the value matches or you fall off the end. You cannot jump to the third
                    node without walking.
                    """,
                    title("Array index versus walking links"),
                    array(["70", "81", "64"], hi=[1], caption="Index 1 holds 81"),
                    note("People count from 1. Array indexes in this course start at 0.", "red"),
                ),
                board(
                    """
                    In a queue, retrieval of the next job always takes the front. You retrieve Essay
                    before Poster if Essay was enqueued first. If a question asks you to retrieve
                    the newest item from a queue, the honest answer is that a queue does not offer
                    that as its normal operation. A stack would. Do not invent a middle door.
                    """,
                    title("Retrieve from a queue"),
                    steps("Look at the front", "Return that item", "The next item becomes the front"),
                ),
                board(
                    """
                    Write retrieval traces in a small table: structure, operation, result, what is
                    left. That table is enough for a short exam question. For a list 4, 9, 1 stored
                    as a linked list, a search for 9 visits 4, then 9, and stops. It does not visit
                    1. Mention the early stop.
                    """,
                    title("A retrieval table"),
                    table(
                        ["visited", "result"],
                        [["4", "not yet"], ["9", "found, stop"]],
                    ),
                ),
            ]),
        ]),
        chapter("xii-ch3", 3, "Programming Fundamentals", [
            lecture("xii-collections", "Lists, tuples, sets, and dictionaries", True, [
                board(
                    """
                    A Python list is ordered and mutable, which means you may change it. Indexes
                    start at 0. append adds at the end. A tuple is ordered and immutable. After you
                    create a tuple, you do not assign a new value to one slot. Use a tuple for a
                    fact that should stay still, such as a coordinate or a date of birth stored as
                    year, month, day. Use a list when the collection will grow.
                    """,
                    title("List and tuple"),
                    code("marks = [70, 81, 64]", "marks.append(90)", "born = (2008, 5, 2)"),
                    cols("List", ["Ordered", "You may change it"], "Tuple", ["Ordered", "You do not change slots"]),
                ),
                board(
                    """
                    A set stores unique items and does not promise order. Adding 3 twice still
                    leaves one 3. Sets support math words you already know: union, intersection,
                    and difference. A dictionary stores key and value pairs. The key finds the value.
                    A roll number mapping to a name is a dictionary. Keys should be unique. Looking
                    up a missing key raises an error unless you check membership first.
                    """,
                    title("Set and dictionary"),
                    code("labs = {\"A\", \"B\", \"A\"}", "names = {15: \"Ayesha\", 16: \"Bilal\"}", "print(names[15])"),
                    note("A set drops duplicates. A dictionary key points at one value.", "gold"),
                ),
                board(
                    """
                    Built-in helpers cover a lot of attendance work. len counts items. sum adds
                    numbers. min and max find the ends. For an attendance dictionary of names to
                    present counts, max can find the highest count, and you still need a loop if
                    you want the name that owns that count. Do not assume max on a dictionary
                    returns the name. On a dictionary, max looks at the keys unless you tell it
                    otherwise.
                    """,
                    title("len, sum, min, max"),
                    code("present = [1, 1, 0, 1]", "print(sum(present), \"of\", len(present))"),
                    note("sum of that list is 3 and len is 4, so this student attended 3 of 4.", "blue"),
                ),
            ]),
            lecture("xii-functions", "Functions, return values, and scope", True, [
                board(
                    """
                    A function is a named block you can call. Built-in functions, such as print and
                    len, come with Python. A user-defined function is one you write with def.
                    Parameters are the names inside the function. Arguments are the values you pass
                    in the call. A function can print, or it can return a value for the caller to
                    use. If you need the result later, return it. Printing alone does not give the
                    caller a number.
                    """,
                    title("Define, call, return"),
                    code("def average(total, count):", "    return total / count", "print(average(245, 3))"),
                    note("return hands a value back. print only shows it.", "red"),
                ),
                board(
                    """
                    Scope is where a name is visible. A variable assigned inside a function is local.
                    The caller does not see it. A variable assigned outside is global, and functions
                    can read it, but assigning to that name inside the function creates a local
                    unless you have a clear reason to do otherwise. Prefer parameters and return
                    values. Global variables make traces harder because any function might change them.
                    """,
                    title("Local and global"),
                    cols("Local", ["Born inside the function", "Disappears after return"], "Parameter", ["The caller's value, named inside"]),
                    note("Pass data in. Return data out. That is the traceable path.", "green"),
                ),
                board(
                    """
                    An arithmetic calculator can be four functions: add, subtract, multiply, and
                    divide. Divide should refuse a zero divisor. Each function returns a number.
                    A main loop can read the operation and print the returned number. If add prints
                    by itself and also returns nothing, you cannot reuse add inside a bill. Return
                    the number and let the caller decide whether to print.
                    """,
                    title("Calculator functions"),
                    code("def add(a, b):", "    return a + b", "def divide(a, b):", "    if b == 0:", "        return None", "    return a / b"),
                    note("divide of 10 and 0 should not crash the whole lab session.", "blue"),
                ),
            ]),
            lecture("xii-files", "Files, with, and exceptions", True, [
                board(
                    """
                    A file keeps data after the program stops. Open a text file with a mode. Mode r
                    reads and fails if the file is missing. Mode w writes and erases what was there.
                    Mode a appends at the end. After writing, close the file so the data is flushed.
                    The with statement closes it for you, even when something goes wrong inside the
                    block. Prefer with over a bare open you might forget to close.
                    """,
                    title("Modes r, w, and a"),
                    code("with open(\"grades.txt\", \"a\") as f:", "    f.write(\"Ayesha 78\\n\")"),
                    note("Mode w deletes the old contents. Use a when you mean add a line.", "red"),
                ),
                board(
                    """
                    Errors and exceptions are how Python reports trouble it can name, such as a
                    missing file or a value that is not an integer. try wraps the risky lines.
                    except names the problem you are ready to handle. You might tell the user the
                    file was not found and continue. Do not wrap the entire program in one bare
                    except. You will hide mistakes you needed to see.
                    """,
                    title("try and except"),
                    code("try:", "    n = int(text)", "except ValueError:", "    print(\"Please type a whole number\")"),
                    note("Catch the error you expect. Let surprises stay visible.", "gold"),
                ),
                board(
                    """
                    A small grade tracker stores one line per student. The program asks for a name
                    and a mark, checks that the mark is an integer between 0 and 100, then appends
                    a line with the with statement. A second function opens the same file in mode r
                    and prints each line. Test by running it twice. The second run must still show
                    the first student, which proves you used append and not write.
                    """,
                    title("Grade tracker"),
                    steps("Read name and mark", "Reject a mark outside 0 to 100", "Append one line", "Read the file back to check"),
                    note("Run twice. Both students should still be in the file.", "green"),
                ),
            ]),
        ]),
        chapter("xii-ch4", 4, "Data and Analysis", [
            lecture("xii-sqlite", "Analysis and a SQLite table", True, [
                board(
                    """
                    Data analysis means turning records into a decision. The records might come from
                    a file, a survey, or a database. A database is the better home when many rows
                    share a shape and you will ask repeated questions. SQLite is a small database
                    engine you can use from Python. It stores the database in one file on disk.
                    You send it SQL statements: create a table, insert a row, select rows.
                    """,
                    title("From rows to a decision"),
                    flow("Rows in a table|io", "A precise question|process", "A result you can defend|term"),
                ),
                board(
                    """
                    Create a table of lab loans with an integer primary key, a student name, and a
                    device. Insert two rows. Then select only the rows for the laptop. The SQL key
                    words you need here are CREATE TABLE, INSERT INTO, and SELECT with WHERE.
                    Strings in SQL use quotes. The primary key should be unique so each loan has
                    an identity even if two students share a name.
                    """,
                    title("Create, insert, select"),
                    code(
                        "CREATE TABLE loan (",
                        "  id INTEGER PRIMARY KEY,",
                        "  student TEXT, device TEXT)",
                        "SELECT student FROM loan WHERE device = 'laptop'",
                    ),
                ),
                board(
                    """
                    In Python you open a connection to the database file, create a cursor, execute
                    the statement, and commit after a change. A select does not need a commit.
                    Close the connection when the work is done. If you forget to commit an insert,
                    the next program run will not see the new row. That looks like a logic bug and
                    is often only a missing commit.
                    """,
                    title("Commit the change"),
                    note("Insert or update: commit. Select: no commit required.", "green"),
                    note("A missing commit is the usual reason a new row vanishes.", "red"),
                ),
            ]),
            lecture("xii-pandas", "DataFrames and missing values", True, [
                board(
                    """
                    Pandas is a Python library for tables in memory. A DataFrame is that table: rows,
                    columns, and labels. You can load a CSV file into a DataFrame and then filter
                    rows without writing a loop yourself. It is still the same idea as a database
                    query. You are choosing rows and columns. The tool is different. Use it when
                    the data is already a file and you want statistics or a chart quickly.
                    """,
                    title("A DataFrame is a table"),
                    table(
                        ["name", "marks"],
                        [["Ayesha", "78"], ["Bilal", "64"], ["Sara", ""]],
                    ),
                    note("An empty cell is missing data, not a zero, until you decide otherwise.", "gold"),
                ),
                board(
                    """
                    Missing values are often shown as NaN, meaning not a number. Leaving them in an
                    average can change the result or poison it. Two honest choices: drop the rows
                    that are missing the column you need, or fill them with a stated value such as
                    the median. Say which choice you made. Filling every gap with zero pretends the
                    student scored nothing, which may be false.
                    """,
                    title("NaN is not automatically zero"),
                    cols("Drop", ["Remove rows you cannot use", "Say how many you removed"], "Fill", ["Use a stated substitute", "Do not silently use zero"]),
                    note("Zero is a real score. Missing is an unknown score.", "red"),
                ),
                board(
                    """
                    Organize the frame before you chart it. One row should be one observation.
                    One column should be one variable. A column of marks should be numeric, not a
                    mix of numbers and the word absent. Put absent in its own column if you need
                    it. Tidy columns are what make group totals and graphs trustworthy.
                    """,
                    title("Tidy rows and columns"),
                    note("One observation per row. One variable per column.", "green"),
                ),
            ]),
            lecture("xii-stats", "Charts and descriptive statistics", True, [
                board(
                    """
                    Descriptive statistics summarize a column without claiming a cause. The mean is
                    the arithmetic average. The median is the middle value after sorting. The mode
                    is the most common value. A single very high mark pulls the mean up and hardly
                    moves the median. If the question is what a typical student scored, the median
                    may be the fairer one-line summary. Say which one you chose and why.
                    """,
                    title("Mean, median, mode"),
                    array(["40", "45", "50", "55", "100"], hi=[2], caption="Median of five sorted marks is 50"),
                    note("The mean of these five is 58, pulled up by 100. The median stays 50.", "blue"),
                ),
                board(
                    """
                    Match the chart to the question. A bar chart compares categories, such as average
                    mark by section. A line chart shows change over time, such as attendance by week.
                    A pie chart shows parts of one whole, and only when there are few slices. A
                    scatter plot shows the relationship of two numeric variables. Do not use a line
                    chart for unrelated categories. The line implies a path that is not there.
                    """,
                    title("Pick the graph"),
                    cols("Bar", ["Compare sections"], "Line", ["Change over time"]),
                    cols("Pie", ["Parts of one whole"], "Scatter", ["Two numeric variables"]),
                ),
                board(
                    """
                    A complete answer names the statistic or chart, gives the number or the pattern,
                    and states the limit. Section A has a higher median than section B on this quiz,
                    with 30 students in each. That does not by itself prove a better teacher. You
                    did not measure prior knowledge. Careers that use this care include data analysis
                    and any role that reports numbers to a principal or a client.
                    """,
                    title("Say the limit"),
                    note("A comparison is not a cause. Write the sample size.", "green"),
                ),
            ]),
        ]),
        chapter("xii-ch5", 5, "Applications and Impacts of Computing", [
            lecture("xii-ml", "Machine learning, networks, and deep learning", True, [
                board(
                    """
                    Machine learning is a way to build a model from examples instead of writing every
                    rule by hand. You show many labeled examples, such as photos marked cat or not cat,
                    and the model adjusts until it predicts labels on new photos. It can still fail on
                    photos unlike the ones it saw. A rule you wrote yourself is not machine learning.
                    A model fitted from examples is.
                    """,
                    title("Learning from examples"),
                    flow("Examples with labels|io", "Training adjusts the model|process", "Prediction on a new case|term"),
                    note("If the training photos are only one breed of cat, other breeds may be missed.", "red"),
                ),
                board(
                    """
                    A neural network is a stack of simple units organized in layers. Each unit combines
                    its inputs and passes a result forward. Deep learning uses a network with many
                    layers, which can represent more complicated patterns, and it usually wants more
                    data and more computing. The words are nested. Deep learning is one kind of neural
                    network work, and neural networks are one family inside machine learning.
                    """,
                    title("Network and depth"),
                    layers(
                        "Machine learning: models from examples",
                        "Neural network: layers of simple units",
                        "Deep learning: many layers, more data",
                    ),
                ),
                board(
                    """
                    Parts you should be able to name: inputs, weights that scale those inputs, a way
                    to combine them, and an output. Training changes the weights to reduce mistakes
                    on the examples. Using the finished model on a new student photo is inference,
                    not training. Applications include reading handwritten digits, spotting a weed in
                    a crop photo, or turning speech into text. A person should still review high-stakes
                    decisions such as a medical flag.
                    """,
                    title("Weights, training, and use"),
                    chips("Inputs", "Weights", "Layers", "Training", "Inference"),
                    note("Training changes the model. Inference uses the model.", "green"),
                ),
            ]),
            lecture("xii-protect", "Sign-in, access, and protecting data", True, [
                board(
                    """
                    Secure collaboration starts by knowing who is at the keyboard and what they may
                    open. Authentication checks identity. A password is one factor, something you know.
                    Multi-factor authentication adds a second check, such as a short-lived code on your
                    phone. Access control then limits the files. A student should not open the whole
                    school's grade book. A teacher should not need the server password to enter marks.
                    """,
                    title("Prove who you are, then limit the door"),
                    steps("Authentication: who is this?", "Second factor when the account matters", "Access control: what may they open?"),
                    note("A shared class password means you can no longer tell who changed a file.", "red"),
                ),
                board(
                    """
                    Data protection keeps the contents from being read or lost. Encryption scrambles
                    data so someone who copies the file still cannot read it without the key. A good
                    password is long and unique to that account. A backup is a separate copy you can
                    restore after a mistake or a failure. A firewall is a filter that allows only the
                    network traffic the school expects. None of these replaces the others.
                    """,
                    title("Encryption, passwords, backup, firewall"),
                    chips("Encrypt stored and sent data", "Unique passwords", "Backups in another place", "Firewall"),
                    note("A backup on the same disk does not help when that disk dies.", "gold"),
                ),
                board(
                    """
                    Put the pieces in order for a shared project folder. Each student signs in as
                    themselves, with a second factor on the teacher account. The folder grants write
                    access only to that class. The disk is encrypted. A nightly backup is stored on a
                    different device. The firewall does not need to be explained as a brand. You only
                    need to say it blocks traffic the school did not allow.
                    """,
                    title("One folder, four controls"),
                    note("Identity, permission, encryption, and a copy. That is the set.", "green"),
                ),
            ]),
            lecture("xii-threats", "Recognizing threats and basic defenses", True, [
                board(
                    """
                    Malware is software written to harm a system or to sneak past the owner. The impact
                    can be deleted files, spying, or a locked screen that demands money. Phishing is a
                    fake message, page, or call that tries to trick a person into giving away a password
                    or a code. The impact is an account takeover. Denial of service floods a service
                    with junk so real users cannot reach it. The impact is that the site or network is
                    unavailable. These are different attacks with different results.
                    """,
                    title("Three threats, three impacts"),
                    table(
                        ["Threat", "Impact"],
                        [["Malware", "Damage, spying, or lockout"], ["Phishing", "Someone else enters your account"], ["Denial of service", "The service becomes unreachable"]],
                    ),
                ),
                board(
                    """
                    You can often recognize the situation without taking it apart. Unexpected attachments,
                    urgent threats, and a link that does not match the school domain are phishing signs.
                    A suddenly slow shared service for everyone, not just your laptop, fits a denial of
                    service more than a single full disk. Pop-ups you did not install, or files you did
                    not encrypt yourself, are reasons to stop and tell a teacher or technician. Do not
                    follow instructions inside the suspicious message.
                    """,
                    title("Signs a student can notice"),
                    note("Urgency plus a surprise link is a classic phishing shape.", "red"),
                    note("Stop and report. Do not type a password into a page you reached from that message.", "gold"),
                ),
                board(
                    """
                    Mitigations for this course are defensive habits. Keep the system updated so known
                    holes get closed. Turn on multi-factor authentication. Use a different password for
                    the school account than for any other site. Keep backups. Leave the firewall on.
                    Report the message instead of forwarding it to the class. These steps reduce harm.
                    They are not instructions for carrying out an attack, and the exam does not need those.
                    """,
                    title("Defenses you can actually do"),
                    steps(
                        "Update the device",
                        "Turn on a second sign-in factor",
                        "Use a unique password",
                        "Keep a backup",
                        "Report suspicious messages",
                    ),
                    note("Name the threat, the impact, and one matching defense.", "green"),
                ),
            ]),
            lecture("xii-equity", "Fair access and collaboration tools", False, [
                board(
                    """
                    Equity in digital collaboration means each student has a real chance to take part,
                    not that every student owns the same laptop. Some will share a phone. Some will
                    have expensive data. Some will need captions. A fair task can be completed on the
                    shared school machines, in the time available, with a file format everyone can open.
                    A task that only works on one expensive app excludes people before the learning starts.
                    """,
                    title("A real chance to take part"),
                    chips("Shared devices", "Low data", "Captions", "A file everyone can open"),
                ),
                board(
                    """
                    Collaboration tools include a shared document, a class folder, a chat channel, and
                    a video call. Choose the smallest tool that fits. A shared document is enough for
                    co-writing. A video call is for a discussion that needs voices. Turn on captions.
                    Do not require a camera in a home the student did not choose to show. Write the
                    norms: no one deletes another student's section, and criticism is about the work.
                    """,
                    title("Pick a tool and a norm"),
                    cols("Shared doc", ["Writing together"], "Video call", ["A live discussion, with captions"]),
                    note("Camera-off must still count as attendance in the work if the school promised equity.", "blue"),
                ),
                board(
                    """
                    Careers connected to this chapter include security awareness, data protection in a
                    company, machine learning assistance, and product roles that have to serve more than
                    one kind of user. In every one of them you will be asked to name a risk and a control,
                    or a barrier and a removal of that barrier. Practice that sentence shape now.
                    """,
                    title("The sentence that earns the mark"),
                    note("Risk plus control. Barrier plus how the design removes it.", "green"),
                ),
            ]),
        ]),
        chapter("xii-ch6", 6, "Entrepreneurship in the Digital Age", [
            lecture("xii-entrepreneur", "Problems worth a digital product", False, [
                board(
                    """
                    An entrepreneur notices a problem people care about and organizes a way to solve it.
                    Entrepreneurship is that work, including the risk that the idea may fail.
                    In the digital age the solution is often software, an online service, or a product
                    sold through a phone. The technology is the vehicle. The problem is the reason anyone
                    should care. A new app with no problem is a hobby.
                    """,
                    title("Problem first"),
                    flow("A painful problem|io", "A specific group of people|process", "A digital way to help|term"),
                ),
                board(
                    """
                    Classroom examples, not famous brands: a bakery near a school that takes Eid cake
                    orders in a form instead of a crowded counter. A student who sells neat revision
                    sheets as a small download after classmates keep asking for photos of notes. A tutor
                    who posts a weekly quiz and marks it from a sheet. Each one starts from a repeated
                    complaint. If you cannot quote the complaint, you do not have a business idea yet.
                    """,
                    title("Local classroom examples"),
                    chips("Order form for a bakery", "Revision sheets classmates already request", "A weekly quiz a tutor can mark"),
                ),
                board(
                    """
                    Turn a complaint into an idea with four lines. Who has the problem? What do they do
                    today? Why is that painful? What is the smallest digital help? The canteen queue is
                    painful because the break is short and the line is long. Today's method is standing
                    and hoping. The digital help might be choosing food before the break. That is enough
                    to start. It is not yet a company.
                    """,
                    title("Four lines"),
                    steps("Who", "What they do now", "Why it hurts", "Smallest digital help"),
                    note("If the pain is only yours, check that anyone else will use the fix.", "red"),
                ),
            ]),
            lecture("xii-prototype", "Prototypes and the build cycle", True, [
                board(
                    """
                    A prototype is an early version you build in order to learn. It is allowed to be
                    incomplete. A paper prototype is screens drawn on paper that a classmate can point
                    through. A digital prototype clicks from screen to screen but may not save data.
                    A working prototype performs the main action for real, on a narrow slice. Pick the
                    cheapest type that can answer your current question.
                    """,
                    title("Three kinds of prototype"),
                    cols("Paper", ["Fast", "Tests labels and order"], "Clickable", ["Tests the path", "Still may be fake data"]),
                    note("A working slice is for when the path is already agreed.", "gold"),
                ),
                board(
                    """
                    The cycle is build a little, test it with a real user, learn, and change the next
                    version. Do not vanish for a month to perfect version one. In class, a prototype
                    session can be twenty minutes of paper and one classmate trying to order lunch.
                    Watch their finger. Every hesitation is a note. Change the paper before you defend
                    the drawing.
                    """,
                    title("Build, test, learn, change"),
                    steps("Build the smallest version", "Watch one user", "Write what confused them", "Change the prototype"),
                ),
                board(
                    """
                    For the canteen, a paper prototype might be three screens: menu of five items,
                    confirm, and a pickup window. If the user cannot find the confirm button, move it.
                    You learned more from that failure than from adding ten more dishes. The cycle
                    rewards contact with a user, not extra features.
                    """,
                    title("Canteen on paper"),
                    flow("Five items|io", "Confirm|process", "Pickup window|term"),
                    note("Five items are enough to learn. Fifty items hide the lesson.", "green"),
                ),
            ]),
            lecture("xii-mvp", "MVP, risk, and a beachhead", True, [
                board(
                    """
                    A minimum viable product is the smallest version a real user can use in their real
                    routine. A prototype can be pretend. An MVP must deliver the core result, even if it
                    is ugly. The difference: a prototype answers whether people understand the idea. An
                    MVP answers whether they will actually use it when the break bell rings. Both are
                    small. They answer different questions.
                    """,
                    title("Prototype versus MVP"),
                    cols("Prototype", ["Learn if the idea is clear", "May use fake data"], "MVP", ["Learn if people use it", "Does the real job once"]),
                ),
                board(
                    """
                    The riskiest assumption is the belief that, if false, kills the idea. For the canteen,
                    the risky belief is not whether you can draw a logo. It is whether students will order
                    ahead instead of walking to the window. Test that. An MVP can be a form with five
                    items and a pickup time, checked by a person with a paper list. If nobody orders,
                    a fancier app would also have failed.
                    """,
                    title("Test the belief that matters"),
                    note("The riskiest assumption is about behavior, not about your favorite feature.", "red"),
                    steps("Write the belief", "Build only what tests it", "Count real uses", "Decide to continue or change"),
                ),
                board(
                    """
                    A beachhead market is the first narrow group you serve well, not everyone in the city.
                    For this canteen, the beachhead might be one break, one counter, Class 10 only.
                    You can talk to all of them. You can see the queue shrink or not. After that works,
                    you might add another break. Starting with every school in the district teaches you
                    nothing, because you cannot watch the line.
                    """,
                    title("A small first market"),
                    chips("One school", "One break", "One counter", "Then expand"),
                    note("Name the beachhead as a group you can actually reach.", "green"),
                ),
            ]),
            lecture("xii-ethics", "Ethics, safety, and the project story", False, [
                board(
                    """
                    A complete student project can be told in one page. Problem and who has it. The
                    riskiest assumption. The prototype and what you changed. The MVP and how many people
                    used it. The beachhead. What you will not build yet. That page is more convincing
                    than a slideshow of logos. Numbers from a real trial, even a small one, beat imaginary
                    millions.
                    """,
                    title("The one-page story"),
                    steps("Problem and person", "Riskiest assumption", "What the test showed", "What you refuse to build yet"),
                ),
                board(
                    """
                    Ethical and safe use is part of the product, not a footer. Ask before you collect
                    names. Do not sell a classmate's phone number. Do not copy paid notes and call them
                    your startup. Do not pretend a prototype saved time if you never timed it. If the
                    tool recommends a meal, say it is a suggestion, not a medical claim. Credit anyone
                    whose words or pictures you used.
                    """,
                    title("Honest by default"),
                    note("Ask, credit, and do not invent results.", "red"),
                    chips("Consent", "Credit", "No fake numbers", "No borrowed private data"),
                ),
                board(
                    """
                    Careers around this chapter include product work, small online businesses, and roles
                    inside larger firms that still need someone to test an assumption cheaply. The habit
                    that transfers is the cycle: name the risk, build little, watch a real user, tell the
                    truth about what happened. That habit is worth more than a particular app idea.
                    """,
                    title("The habit you keep"),
                    note("Risk, small build, real user, honest result.", "green"),
                ),
            ]),
            lecture("xii-revision", "Class XII revision boards", True, [
                board(
                    """
                    Revision for HCI. Name the person, the task, the device, and the place. UI is the
                    screen. UX is the whole task, including errors and waiting. A wireframe has structure
                    and no decoration. Accessibility means a second way to finish the task. Test by
                    watching a user stay quiet. Fix the step where they stopped.
                    """,
                    title("HCI, fast"),
                    chips("Person and task", "UI versus UX", "Wireframe", "Watch a user"),
                ),
                board(
                    """
                    Revision for structures and cost. A trace table records variables. Stack is last in,
                    first out. Queue is first in, first out. Array indexes start at 0. A tree has one
                    parent per node. A graph may loop. Nested loops are Big O of n squared. Halving is
                    Big O of log n. Early exit does not change the worst case unless you prove it does.
                    """,
                    title("Structures and Big O"),
                    cols("Stack", ["Last in, first out"], "Queue", ["First in, first out"]),
                    note("One parent and no loop: tree. Otherwise think graph.", "gold"),
                ),
                board(
                    """
                    Revision for Python data work. Lists change, tuples do not. Sets drop duplicates.
                    Dictionaries map a key to a value. return gives a value back, print does not. File
                    mode w erases, mode a adds. with closes the file. Missing data is not zero. Mean,
                    median, and mode answer different questions. Commit an insert or the row disappears.
                    """,
                    title("Python and tables"),
                    chips("return versus print", "w versus a", "NaN is not 0", "commit an insert"),
                ),
                board(
                    """
                    Revision for impact and enterprise. Machine learning fits a model to examples. Deep
                    learning uses many layers. Authentication says who you are. Access control says what
                    you may open. Malware harms the system. Phishing steals trust. Denial of service makes
                    a service unreachable. Defend by updating, using a second factor, unique passwords,
                    and backups. An MVP does the real job once. A prototype may still be pretend. Test the
                    riskiest assumption on a beachhead you can watch.
                    """,
                    title("Impact and the MVP"),
                    note("Threat, impact, defense. Assumption, small test, honest count.", "green"),
                ),
            ]),
        ]),
    ]
