package com.couplesguide.postures.teaching

enum class LessonStep(val order: Int, val prefKey: String) {
    OBJECTIVES(0, "objectives"),
    LECTURE(1, "lecture"),
    READ(2, "read"),
    FLASHCARDS(3, "flashcards"),
    QUIZ(4, "quiz"),
    REFLECT(5, "reflect");

    companion object {
        val all = entries.sortedBy { it.order }
    }
}
