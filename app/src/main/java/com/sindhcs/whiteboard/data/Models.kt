package com.sindhcs.whiteboard.data

data class Mark(
    val k: String,
    val t: String = "",
    val tone: String = "",
    val items: List<String> = emptyList(),
    val headers: List<String> = emptyList(),
    val rows: List<List<String>> = emptyList(),
    val t2: String = "",
    val items2: List<String> = emptyList(),
    val hi: List<Int> = emptyList()
)

data class Board(
    val narration: String,
    val marks: List<Mark>
)

data class Lecture(
    val id: String,
    val title: String,
    val golden: Boolean,
    val boards: List<Board>
)

data class Chapter(
    val id: String,
    val number: Int,
    val title: String,
    val lectures: List<Lecture>
)

data class Grade(
    val id: String,
    val label: String,
    val title: String,
    val subtitle: String,
    val chapters: List<Chapter>
) {
    val lectureCount: Int get() = chapters.sumOf { it.lectures.size }
    val boardCount: Int get() = chapters.sumOf { ch -> ch.lectures.sumOf { it.boards.size } }
}

data class Catalog(val grades: List<Grade>) {
    fun grade(id: String): Grade = grades.first { it.id == id }

    fun chapter(id: String): Chapter = grades.flatMap { it.chapters }.first { it.id == id }

    fun lecture(id: String): Lecture =
        grades.flatMap { it.chapters }.flatMap { it.lectures }.first { it.id == id }

    fun gradeOf(lectureId: String): Grade? =
        grades.firstOrNull { grade ->
            grade.chapters.any { chapter -> chapter.lectures.any { it.id == lectureId } }
        }

    fun chapterOf(lectureId: String): Chapter? =
        grades.flatMap { it.chapters }.firstOrNull { chapter ->
            chapter.lectures.any { it.id == lectureId }
        }

    fun nextInGrade(lectureId: String): Lecture? {
        val grade = gradeOf(lectureId) ?: return null
        val lectures = grade.chapters.flatMap { it.lectures }
        val index = lectures.indexOfFirst { it.id == lectureId }
        if (index < 0) return null
        return lectures.getOrNull(index + 1)
    }
}
