from content.schema import lecture

LECTURE = lecture(
    id="xii-2",
    number=2,
    title="Data Structures, Trees, and Evaluation",
    kicker="CLASS XII  ·  UNIT 2",
    unit="Unit 2 — Computational Thinking and Algorithms",
    domain="B. Computational thinking and algorithms",
    periods="about 20 periods",
    intro=(
        "Class XI traced searches and sorts on a list. Class XII asks you to choose a structure, "
        "walk a tree in a stated order, and judge a solution by efficiency, clarity, and correctness. "
        "The structures are the list, the array, the stack, the queue, and the tree, with binary search on a sorted collection."
    ),
    outcomes=[
        "Evaluate an algorithm for efficiency, clarity, and correctness using a specific example.",
        "Describe lists, arrays, stacks, and queues and name a fitting use for each.",
        "Draw a binary search tree and produce inorder, preorder, and postorder traversals.",
        "Explain why binary search needs sorted data and how a tree supports that search.",
        "Show the visit order of a breadth-first and a depth-first walk on a small tree.",
    ],
    blocks=[
        ("h2", "Judging a solution"),
        (
            "p",
            "Three questions are enough. **Correctness:** does it meet the specification on the awkward cases, not only on the example in the notes? **Clarity:** can another student trace it, with names and structure that match the problem? **Efficiency:** how does the work grow as the data grows? At this level, compare “one pass through n items” with “about one comparison for each time you can halve n” or with “every item compared with every other item”. You may write O(n) and O(log n) if you have been taught the notation. A sentence in ordinary English scores the mark if it is accurate.",
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — judging a search",
                "text": (
                    "Specification: find a roll number in a list of 5,000 sorted roll numbers.\n\n"
                    "Linear search is correct and clear, and it may look at all 5,000. "
                    "Binary search is correct only because the list is sorted, it is clear if low and high are updated in the right direction, and it finishes in a handful of comparisons because each step discards half of what remains. "
                    "Binary search on an unsorted list is not “less efficient”. It is incorrect. "
                    "A clever one-line version with no names is less clear and can lose marks even when it is right."
                ),
            },
        ),
        ("h2", "Lists, arrays, stacks, and queues"),
        (
            "p",
            "A **list** is an ordered collection that can grow and shrink. You have used Python lists. An **array** is a fixed block of same-typed cells addressed by index. In exams, “array” often means the idea of indexed storage, while “list” means a sequence you can append to. The practical difference you must be able to say: finding an item by index is direct; finding it by value may require a search; inserting in the middle of an array shifts the later items.",
        ),
        (
            "p",
            "A **stack** is last-in, first-out. The operations are push and pop. The call stack of a program is the serious example: the most recently called function returns first. Undo in an editor is a stack of actions. You do not pull an item from the middle.",
        ),
        (
            "p",
            "A **queue** is first-in, first-out. Enqueue at the back, dequeue at the front. A printer queue, a lab signup, and the waiting list for breadth-first search are queues. A stack would print the most recent file first, which is the wrong promise.",
        ),
        ("h2", "Trees"),
        (
            "p",
            "A **tree** is a set of **nodes** with one **root** and a parent-to-child relation, and no cycles. A **leaf** has no children. The **height** is the number of steps on the longest path from the root to a leaf; some books count nodes instead of edges, so say which you mean if you state a number. A **binary tree** gives each node at most two children, usually called left and right.",
        ),
        (
            "p",
            "A **binary search tree** (BST) keeps an order. Every value in the left subtree is less than the node, and every value in the right subtree is greater. Duplicates need a stated policy; the trees in this lecture have none. The order is what makes a search able to ignore a whole subtree, the same idea as binary search.",
        ),
        (
            "code",
            {
                "lang": "Tree",
                "text": (
                    "           50\n"
                    "         /    \\\n"
                    "       30      70\n"
                    "      /  \\    /  \\\n"
                    "    20   40  60   80"
                ),
            },
        ),
        (
            "p",
            "That tree is a BST: 30 and its children are less than 50; 70 and its children are greater; the same rule holds at 30 and at 70. Searching for 60 starts at 50, goes right because 60 is greater, and goes left from 70 because 60 is smaller. Two comparisons reach it. Searching for 25 goes left from 50 to 30, then left to 20, and stops: 25 is not there, and there is no further child to open.",
        ),
        ("h2", "Traversals"),
        (
            "p",
            "A **traversal** visits every node in a stated order. For a binary tree the three classical orders, applied at every node, are:",
        ),
        (
            "bullets",
            [
                "**Preorder:** visit the node, then the left subtree, then the right subtree.",
                "**Inorder:** left subtree, then the node, then the right subtree.",
                "**Postorder:** left subtree, then the right subtree, then the node.",
            ],
        ),
        (
            "callout",
            {
                "kind": "example",
                "title": "Worked example — three orders of the tree above",
                "text": (
                    "Preorder (node, left, right): 50, 30, 20, 40, 70, 60, 80.\n\n"
                    "Inorder (left, node, right): 20, 30, 40, 50, 60, 70, 80. "
                    "On a BST, inorder visits the values in sorted order. That is a check you should do.\n\n"
                    "Postorder (left, right, node): 20, 40, 30, 60, 80, 70, 50.\n\n"
                    "If your inorder of a BST is not sorted, the tree is not a BST or the traversal is wrong. Find out which."
                ),
            },
        ),
        (
            "p",
            "Uses you should be able to name: inorder of a BST produces a sorted list; preorder copies a tree structure starting from the root; postorder is the natural order for deleting a tree, because the children go before the parent. A file system is a tree. An organisation chart is a tree if each person has one manager. A family tree with two parents is not a binary search tree and may not be a tree in the strict sense if you draw both parents; do not force it.",
        ),
        ("h2", "Breadth-first and depth-first walks"),
        (
            "p",
            "On a general tree or a small graph drawn as a hierarchy, two walks appear in questions. **Breadth-first search (BFS)** uses a queue. Visit the start, then its children left to right, then their children. **Depth-first search (DFS)** uses a stack, or recursion. Follow one child as far as it goes before the next sibling. If you visit a node when you first reach it, and you try children left to right, DFS matches preorder on a tree.",
        ),
        (
            "code",
            {
                "lang": "Tree",
                "text": (
                    "            CEO\n"
                    "           /   \\\n"
                    "         HR     IT\n"
                    "         |     /  \\\n"
                    "       Staff Dev  Accounts"
                ),
            },
        ),
        (
            "p",
            "BFS from CEO: CEO, HR, IT, Staff, Dev, Accounts. The queue after visiting CEO holds HR then IT. DFS from CEO, children left to right, recording the node when first seen: CEO, HR, Staff, IT, Dev, Accounts. If a question says “search the Security department”, walk until the node named Security is visited and write the nodes in the order visited up to and including that node. Do not skip the nodes on the way. They are the trace.",
        ),
        (
            "callout",
            {
                "kind": "warn",
                "title": "Common mistake",
                "text": "Inorder is not “top to bottom”. Preorder is not “left to right along the leaves”. Write the rule above the trace. If the question prints a tree, use that tree; a memorised 50-30-70 answer on a different diagram scores zero.",
            },
        ),
        (
            "callout",
            {
                "kind": "exam",
                "title": "Exam tip",
                "text": "A three-mark traversal wants the order and nothing else. A five-mark question wants the order plus why that structure fits the problem. Keep the visit list on its own line so a marker can tick it.",
            },
        ),
    ],
    terms=[
        ("Efficiency", "How the work grows as the data grows."),
        ("Clarity", "Whether another person can trace the steps."),
        ("Correctness", "Whether every allowed input meets the specification."),
        ("Stack", "Last-in, first-out. Push and pop."),
        ("Queue", "First-in, first-out. Enqueue and dequeue."),
        ("Binary search tree", "A binary tree ordered so left is smaller and right is larger."),
        ("Inorder", "Left, node, right. Sorted on a BST."),
        ("Preorder", "Node, left, right."),
        ("Postorder", "Left, right, node."),
        ("BFS / DFS", "Level by level with a queue, or down one branch with a stack."),
    ],
    checks=[
        {
            "q": "Inorder of the BST rooted at 50 above. Write only the sequence.",
            "a": "20, 30, 40, 50, 60, 70, 80.",
        },
        {
            "q": "Why is a stack the wrong structure for a printer queue?",
            "a": "A stack prints the most recent job first. A printer queue promises the earliest job first, which is a queue.",
        },
        {
            "q": "Is the tree with root 10, left child 40, right child 30 a BST?",
            "a": "No. 40 is in the left subtree and is greater than 10, which breaks the BST rule.",
        },
    ],
    mcqs=[
        {
            "q": "Inorder traversal of a binary search tree produces",
            "options": [
                "the insertion order",
                "the values in sorted order",
                "only the leaves",
                "the values in reverse height order",
            ],
            "answer": "B",
            "why": "Left, then node, then right, walks a BST from smallest to largest.",
        },
        {
            "q": "BFS uses which structure to hold the waiting nodes?",
            "options": ["A stack", "A queue", "A primary key", "A hash"],
            "answer": "B",
            "why": "The first node discovered is the first node expanded. That is a queue.",
        },
        {
            "q": "The main advantage of binary search over linear search on suitable data is that",
            "options": [
                "it works on unsorted data",
                "each comparison discards about half of the remaining items",
                "it never compares values",
                "it uses more memory and is therefore faster",
            ],
            "answer": "B",
            "why": "Halving is the advantage. It is invalid on unsorted data, so the first option is a common trap.",
        },
        {
            "q": "Postorder visits a node",
            "options": [
                "before its children",
                "between its children",
                "after its children",
                "only if it is the root",
            ],
            "answer": "C",
            "why": "The rule is left subtree, right subtree, then the node.",
        },
    ],
    shorts=[
        {
            "q": "Give one use of a stack and one use of a queue in computing, and the rule that makes each fit.",
            "a": "A call stack fits function calls because the last function called is the first to return. A printer queue fits because the first document submitted should be the first printed. Using the other structure would reverse the promise.",
        },
        {
            "q": "Preorder and postorder of the tree rooted at 50 with the usual children 30, 70, 20, 40, 60, 80.",
            "a": "Preorder: 50, 30, 20, 40, 70, 60, 80. Postorder: 20, 40, 30, 60, 80, 70, 50.",
        },
        {
            "q": "How do you judge efficiency without a formula, for linear versus binary search on a sorted list of a million names?",
            "a": "Linear search may examine every name. Binary search throws away about half the remaining names each time, so it still finishes after a small number of comparisons. Both can be correct. Binary search is the efficient one. Linear search may still be clearer to a beginner, which is a clarity comment, not an efficiency comment.",
        },
    ],
    longs=[
        {
            "marks": 5,
            "q": "Insert 50, 30, 70, 20, 40, 60, 80 into an empty BST in that order. Give the inorder traversal and use it as a check. Then state how a search for 60 proceeds.",
            "a": (
                "50 is the root. 30 goes left. 70 goes right. 20 goes left of 30. 40 goes right of 30. 60 goes left of 70. 80 goes right of 70. "
                "The drawing is the tree used throughout this lecture.\n\n"
                "Inorder is 20, 30, 40, 50, 60, 70, 80, which is sorted, so the BST order is consistent.\n\n"
                "Search for 60: compare with 50 and go right; compare with 70 and go left; compare with 60 and stop. "
                "The left subtree of 50 was never opened. That ignored subtree is the efficiency of the structure."
            ),
        },
        {
            "marks": 5,
            "q": "A company stores departments as the tree CEO → HR and IT; HR → Staff; IT → Dev and Accounts. A clerk must find Security, which is not in the tree, using DFS and then say what BFS would have visited first. Also recommend a structure if the real need is “who is the manager of this employee?” rather than a picture.",
            "a": (
                "DFS from CEO, left child first, recording a node when first reached: CEO, HR, Staff, IT, Dev, Accounts. "
                "Security is never visited. The correct report is that the search ends after Accounts and Security is absent. Inventing a Security node is a wrong trace.\n\n"
                "BFS visits CEO first, then HR and IT, then Staff, Dev, and Accounts. The first node is still CEO. "
                "BFS would discover a node near the root sooner than a node deep on the left, which is why it fits “shortest path in an unweighted tree”.\n\n"
                "If the frequent question is the manager of a known employee, a tree drawing is a poor daily tool. "
                "A table of Employee(Id, Name, ManagerId) answers that lookup directly, and the tree can be drawn from it when a chart is wanted. "
                "Clarity and efficiency depend on the question, not on which picture looks more advanced."
            ),
        },
    ],
    labs=[
        {
            "title": "Lab 2 — Build a tree and walk it",
            "steps": [
                "Insert 8, 3, 10, 1, 6, 14, 4 into a BST on paper, in that order.",
                "Write preorder, inorder, and postorder. Check that inorder is sorted.",
                "Search for 6 and for 7. Record the nodes compared.",
                "Write BFS and DFS visit orders from the root.",
            ],
            "success": "Inorder is 1, 3, 4, 6, 8, 10, 14. The search for 7 stops at a missing child and does not wander into 14.",
        }
    ],
    summary=[
        "Judge correctness, clarity, and efficiency separately. A fast wrong algorithm is still wrong.",
        "Stacks are last-in first-out. Queues are first-in first-out. Name a use that matches the rule.",
        "A BST puts smaller values on the left and larger values on the right.",
        "Preorder: node, left, right. Inorder: left, node, right. Postorder: left, right, node.",
        "Inorder of a BST is sorted. Use that as a check.",
        "BFS uses a queue and goes level by level. DFS goes down a branch first.",
        "Choose the structure for the question you actually ask, not for the most impressive name.",
    ],
)
