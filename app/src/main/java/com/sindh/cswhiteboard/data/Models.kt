package com.sindh.cswhiteboard.data

data class Curriculum(
    val version: String,
    val classes: List<ClassPack>
)

data class ClassPack(
    val id: String,
    val titleEn: String,
    val titleUr: String,
    val subtitleEn: String,
    val subtitleUr: String,
    val chapters: List<Chapter>
) {
    fun lectureCount(): Int = chapters.sumOf { it.lectures.size }
    fun goldenCount(): Int = chapters.sumOf { ch -> ch.lectures.count { it.golden } }
}

data class Chapter(
    val id: String,
    val number: Int,
    val titleEn: String,
    val titleUr: String,
    val lectures: List<Lecture>
)

data class Lecture(
    val id: String,
    val code: String,
    val titleEn: String,
    val titleUr: String,
    val golden: Boolean,
    val durationHintSec: Int,
    val segments: List<Segment>
)

data class Segment(
    val speakEn: String,
    val speakUr: String,
    val clear: Boolean,
    val actions: List<BoardAction>
)

data class BoardAction(
    val type: String,
    val text: String = "",
    val kind: String = "",
    val name: String = "",
    val lines: List<String> = emptyList(),
    val headers: List<String> = emptyList(),
    val rows: List<List<String>> = emptyList()
)
