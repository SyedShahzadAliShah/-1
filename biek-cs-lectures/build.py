"""Generate the BIEK Computer Science lecture PDFs."""

from pathlib import Path

from content_practical import LABS
from content_xi import LECTURES as XI_A
from content_xi import PREFACE as PREFACE_XI
from content_xi_end import END
from content_xi_more import MORE
from content_xii import LECTURES as XII_PART
from content_xii import PREFACE as PREFACE_XII
from content_xii_oop import OOP
from content_xii_rest import REST
from pdf_engine import (
    HeaderState,
    PageBreak,
    SetHeader,
    Bookmark,
    Spacer,
    build_pdf,
    cover_story,
    make_table,
    render_lab,
    render_lecture,
    slug,
)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "pdf"
UNITS = OUT / "units"

XI = XI_A + MORE + END
XII = sorted(XII_PART + [OOP] + REST, key=lambda lec: int(lec["unit"]))


def header_for(lec):
    if lec.get("unit"):
        right = f"Class {lec['grade']} | Unit {lec['unit']} | {lec['title']}"
    else:
        right = f"Class {lec['grade']} | {lec['title']}"
    return "BIEK Computer Science", right


def lecture_flows(lec):
    if lec.get("unit"):
        title = f"Unit {lec['unit']}  {lec['title']}"
        key = f"{lec['grade']}-U{lec['unit']}"
    else:
        title = lec["title"]
        key = f"{lec['grade']}-preface"
    return [Bookmark(key, title, 0)] + render_lecture(lec)


def book_story(grade, kicker, title, subtitle, paragraphs, preface, lectures):
    HeaderState.left = "BIEK Computer Science"
    HeaderState.right = f"Class {grade}"
    story = cover_story(kicker, title, subtitle, paragraphs)
    story.append(Spacer(1, 8))
    story.append(make_table(
        ["Unit", "Lecture", "Weight"],
        [[lec["unit"], lec["title"], lec["weight"]] for lec in lectures],
    ))
    left, right = header_for(preface)
    story.append(SetHeader(left, right))
    story.append(PageBreak())
    story.extend(lecture_flows(preface))
    for lec in lectures:
        left, right = header_for(lec)
        story.append(SetHeader(left, right))
        story.append(PageBreak())
        story.extend(lecture_flows(lec))
    return story


def unit_story(lec):
    left, right = header_for(lec)
    HeaderState.left = left
    HeaderState.right = right
    return lecture_flows(lec)


def practical_story():
    HeaderState.left = "BIEK Computer Science"
    HeaderState.right = "Practical journal"
    story = cover_story(
        "BOARD OF INTERMEDIATE EDUCATION, KARACHI",
        "Computer Science\nPractical Journal",
        "Class XI and Class XII",
        [
            "These are the laboratory activities named in the Sindh Curriculum for Computer Science, Grades XI-XII, 2019. Each practical states an aim, the steps, the program where the activity is code, what you should see, and two viva questions.",
            "Programming activities use the same source as the lectures. Hardware activities are done with the teacher, with the mains lead removed before a case is opened.",
            "The factor program, the pass-by-reference demonstration and the employee and string programs are printed in full in the Class XI lectures. Where one practical names several programs, the journal shows the first and the lecture shows the rest.",
        ],
    )
    current = None
    for lab in LABS:
        if lab["grade"] != current:
            current = lab["grade"]
            story.append(SetHeader("BIEK Computer Science", f"Class {current} practicals"))
            story.append(PageBreak())
            story.append(Bookmark(f"prac-{current}", f"Class {current} practicals", 0))
        else:
            story.append(PageBreak())
        story.append(Bookmark(f"prac-{lab['code']}", f"{lab['code']}  {lab['title']}", 1))
        story.extend(render_lab(lab))
    return story


def xi_paragraphs():
    return [
        "Seven classroom lectures for Computer Science Class XI, written for the Board of Intermediate Education, Karachi.",
        "The lectures follow the Sindh Curriculum for Computer Science, Grades XI-XII, 2019: the computer system, memory, the system unit, operating systems, C++ programming, arrays and structures, and networks. They are original teaching notes. They are not a reproduction of a textbook.",
        "Every complete C++ program in these notes was compiled and run. Sample inputs and the output to expect are stated beside the programs.",
        "The board paper associated with this course is three hours and 75 marks: 29 multiple-choice questions, ten short answers chosen from fifteen, and two detailed answers chosen from three. Before the annual examination, confirm the model paper and any reduced syllabus for your year at biek.edu.pk.",
        "Units inside this file: 1 Overview of the computer system. 2 Computer memory. 3 Inside the system unit. 4 Operating systems. 5 Programming in C++. 6 Arrays, strings and structures. 7 Computer communication and networks.",
    ]


def xii_paragraphs():
    return [
        "Seven classroom lectures for Computer Science Class XII, written for the Board of Intermediate Education, Karachi.",
        "The lectures follow the Sindh Curriculum for Computer Science, Grades XI-XII, 2019: the system development life cycle, pointers, object-oriented programming, file handling, databases, multimedia, and wireless and mobile communication.",
        "Object-oriented programming carries about a quarter of the Class XII weight. The programs for classes, pointers and files were compiled and run.",
        "Use the same 75-mark paper shape for practice, and confirm the current model paper at biek.edu.pk.",
        "Units inside this file: 1 System development life cycle. 2 Pointers. 3 Object-oriented programming. 4 File handling. 5 Database fundamentals. 6 Introduction to multimedia. 7 Wireless and mobile communication.",
    ]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    UNITS.mkdir(parents=True, exist_ok=True)
    if len(XI) != 7 or len(XII) != 7:
        raise SystemExit(f"Expected 7 units each, found XI={len(XI)} XII={len(XII)}")
    units = [int(lec["unit"]) for lec in XI + XII]
    if units != [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]:
        raise SystemExit(f"Unit order is wrong: {units}")

    xi_path = OUT / "BIEK-CS-XI-Lectures.pdf"
    xii_path = OUT / "BIEK-CS-XII-Lectures.pdf"
    prac_path = OUT / "BIEK-CS-XI-XII-Practical-Journal.pdf"

    build_pdf(
        xi_path,
        book_story(
            "XI",
            "BOARD OF INTERMEDIATE EDUCATION, KARACHI",
            "Computer Science\nClass XI Lectures",
            "Units 1 to 7  |  Sindh Curriculum 2019",
            xi_paragraphs(),
            PREFACE_XI,
            XI,
        ),
        "BIEK Computer Science Class XI Lectures",
    )
    build_pdf(
        xii_path,
        book_story(
            "XII",
            "BOARD OF INTERMEDIATE EDUCATION, KARACHI",
            "Computer Science\nClass XII Lectures",
            "Units 1 to 7  |  Sindh Curriculum 2019",
            xii_paragraphs(),
            PREFACE_XII,
            XII,
        ),
        "BIEK Computer Science Class XII Lectures",
    )
    build_pdf(prac_path, practical_story(), "BIEK Computer Science Practical Journal")

    made = [xi_path, xii_path, prac_path]
    for lec in XI + XII:
        path = UNITS / f"{lec['grade']}-Unit-{int(lec['unit']):02d}-{slug(lec['title'])}.pdf"
        build_pdf(path, unit_story(lec), f"BIEK CS {lec['grade']} Unit {lec['unit']}")
        made.append(path)
    for path in made:
        print(f"{path.name:60} {path.stat().st_size:8d} bytes")


if __name__ == "__main__":
    main()
