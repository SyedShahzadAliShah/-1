"""Check lecture records and the runnable examples before trusting the PDF."""

import ast
import traceback
from pathlib import Path

from content import XI_LECTURES, XII_LECTURES

REQUIRED_ANSWERS = set("ABCD")


def check_shape(lecture):
    errors = []
    if len(lecture["mcqs"]) < 4:
        errors.append(f"{lecture['id']}: fewer than 4 MCQs")
    for index, mcq in enumerate(lecture["mcqs"], start=1):
        if len(mcq["options"]) != 4:
            errors.append(f"{lecture['id']} MCQ {index}: need 4 options")
        if mcq["answer"] not in REQUIRED_ANSWERS:
            errors.append(f"{lecture['id']} MCQ {index}: bad answer {mcq['answer']}")
    if not lecture["longs"] or not lecture["labs"] or not lecture["summary"]:
        errors.append(f"{lecture['id']}: missing long questions, labs, or summary")
    return errors


def run_python_blocks(lecture):
    errors = []
    for block in lecture["blocks"]:
        if block[0] != "code":
            continue
        spec = block[1]
        if spec.get("lang") != "Python":
            continue
        source = spec["text"]
        if "input(" in source or "turtle" in source:
            ast.parse(source)
            continue
        namespace = {}
        try:
            exec(source, namespace, namespace)
        except Exception:
            errors.append(f"{lecture['id']} Python block failed:\n{traceback.format_exc()}")
    leftover = Path("sample.txt")
    if leftover.exists():
        leftover.unlink()
    return errors


def check_facts():
    errors = []
    # Caesar
    plain = "BOARD"
    cipher = "".join(chr((ord(ch) - 65 + 3) % 26 + 65) for ch in plain)
    if cipher != "ERDUG":
        errors.append(f"Caesar expected ERDUG, got {cipher}")

    # Precision matrix from the Class XII data lecture
    tp, fn, fp, tn = 90, 10, 30, 70
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    accuracy = (tp + tn) / (tp + fn + fp + tn)
    if round(precision, 2) != 0.75 or round(recall, 2) != 0.90 or round(accuracy, 2) != 0.80:
        errors.append(f"metrics {precision} {recall} {accuracy}")

    # Coin
    p = 11 / 1024
    if not (0.010 < p < 0.011):
        errors.append(f"coin p {p}")

    # Means
    if sum([10, 12, 12, 15, 41]) / 5 != 18:
        errors.append("mean 18")
    if sum([6, 7, 7, 9, 21]) / 5 != 10:
        errors.append("mean 10")
    if (90000 + 70000 + 110000) / 3 != 90000:
        errors.append("salary average")

    def bubble(values):
        data = list(values)
        passes = []
        for _ in range(len(data)):
            swapped = False
            for i in range(len(data) - 1):
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]
                    swapped = True
            passes.append(list(data))
            if not swapped:
                break
        return passes

    passes = bubble([5, 1, 4, 2])
    if passes[0] != [1, 4, 2, 5] or passes[-1] != [1, 2, 4, 5]:
        errors.append(f"bubble {passes}")

    def insert(values):
        data = []
        stages = []
        for value in values:
            data.append(value)
            j = len(data) - 1
            while j > 0 and data[j - 1] > data[j]:
                data[j - 1], data[j] = data[j], data[j - 1]
                j -= 1
            stages.append(list(data))
        return stages

    stages = insert([5, 1, 4, 2])
    if stages != [[5], [1, 5], [1, 4, 5], [1, 2, 4, 5]]:
        errors.append(f"insertion {stages}")

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def bst_insert(root, value):
        if root is None:
            return Node(value)
        if value < root.value:
            root.left = bst_insert(root.left, value)
        else:
            root.right = bst_insert(root.right, value)
        return root

    def walk(node, order, out):
        if node is None:
            return
        if order == "pre":
            out.append(node.value)
        walk(node.left, order, out)
        if order == "in":
            out.append(node.value)
        walk(node.right, order, out)
        if order == "post":
            out.append(node.value)

    root = None
    for value in (50, 30, 70, 20, 40, 60, 80):
        root = bst_insert(root, value)
    pre, mid, post = [], [], []
    walk(root, "pre", pre)
    walk(root, "in", mid)
    walk(root, "post", post)
    if pre != [50, 30, 20, 40, 70, 60, 80]:
        errors.append(f"pre {pre}")
    if mid != [20, 30, 40, 50, 60, 70, 80]:
        errors.append(f"in {mid}")
    if post != [20, 40, 30, 60, 80, 70, 50]:
        errors.append(f"post {post}")

    root = None
    for value in (8, 3, 10, 1, 6, 14, 4):
        root = bst_insert(root, value)
    lab = []
    walk(root, "in", lab)
    if lab != [1, 3, 4, 6, 8, 10, 14]:
        errors.append(f"lab inorder {lab}")

    def binary_search(items, target):
        low, high = 0, len(items) - 1
        while low <= high:
            mid = (low + high) // 2
            if items[mid] == target:
                return mid
            if items[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return None

    data = [2, 5, 8, 12, 16, 23, 38]
    if binary_search(data, 16) != 4 or binary_search(data, 7) is not None:
        errors.append("binary search")
    # 1-based position of 21 in 4, 9, 15, 21, 28, 33, 40 is 4
    if binary_search([4, 9, 15, 21, 28, 33, 40], 21) != 3:
        errors.append("binary 21")
    return errors


def main():
    errors = []
    for lecture in XI_LECTURES + XII_LECTURES:
        errors.extend(check_shape(lecture))
        errors.extend(run_python_blocks(lecture))
    errors.extend(check_facts())
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Checked {len(XI_LECTURES) + len(XII_LECTURES)} lectures.")


if __name__ == "__main__":
    main()
