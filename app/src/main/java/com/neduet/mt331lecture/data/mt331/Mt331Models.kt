package com.neduet.mt331lecture.data.mt331

data class LectureBeat(
    val id: String,
    val glyph: String,
    val titleEn: String,
    val titleUr: String,
    val narrationEn: String,
    val narrationUr: String,
    val formulaEn: String = "",
    val formulaUr: String = ""
)

data class LectureChapter(
    val id: String,
    val chapterNumber: Int,
    val titleEn: String,
    val titleUr: String,
    val taglineEn: String,
    val taglineUr: String,
    val beats: List<LectureBeat>
) {
    fun title(language: String): String = if (language == "ur") titleUr else titleEn

    fun tagline(language: String): String = if (language == "ur") taglineUr else taglineEn
}
