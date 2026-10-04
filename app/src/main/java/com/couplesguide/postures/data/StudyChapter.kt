package com.couplesguide.postures.data

data class StudyChapter(
    val id: String,
    val grade: String,
    val chapterNumber: Int,
    val illustrationRes: Int,
    val pdfAsset: String,
    val pdfPageStart: Int,
    val pdfPageEnd: Int,
    val english: ChapterContent,
    val urdu: ChapterContent
) {
    fun content(language: String): ChapterContent =
        if (language == "ur") urdu else english
}

data class StudyClass(
    val id: String,
    val gradeLabel: String,
    val pdfAsset: String,
    val pageIndexAsset: String,
    val totalPages: Int,
    val chapters: List<StudyChapter>
)
