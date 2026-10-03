package com.couplesguide.postures.data

data class TeacherGuide(
    val title: String,
    val subtitle: String,
    val curriculum: String,
    val referenceNote: String,
    val chapters: List<TeacherChapter>
)

data class TeacherChapter(
    val id: String,
    val title: String,
    val topics: List<TeacherTopic>
)

data class TeacherTopic(
    val id: String,
    val title: String,
    val critical: Boolean,
    val englishText: String,
    val urduNarration: String,
    val startPage: Int,
    val endPage: Int
)
