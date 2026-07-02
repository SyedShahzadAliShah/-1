package com.couplesguide.postures.data

data class SexEdLesson(
    val id: String,
    val sectionId: String,
    val illustrationRes: Int,
    val title: String,
    val summary: String,
    val body: String,
    val keyPoints: List<String>
)

data class SexEdSection(
    val id: String,
    val title: String,
    val hint: String,
    val lessons: List<SexEdLesson>
)
