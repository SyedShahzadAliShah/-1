package com.couplesguide.postures.data

data class PartnerRole(
    val position: String,
    val guidance: List<String>
)

data class LocalizedContent(
    val name: String,
    val category: String,
    val summary: String,
    val description: String,
    val steps: List<String>,
    val tips: List<String>,
    val forMan: PartnerRole? = null,
    val forWoman: PartnerRole? = null
)

data class Posture(
    val id: String,
    val difficulty: Difficulty,
    val illustrationRes: Int,
    val categoryId: String,
    val english: LocalizedContent,
    val urdu: LocalizedContent,
    val isImagination: Boolean = false
) {
    fun content(language: String): LocalizedContent =
        if (language == "ur") urdu else english
}

enum class Difficulty(val en: String, val ur: String) {
    BEGINNER("Beginner", "آسان"),
    INTERMEDIATE("Intermediate", "درمیانہ"),
    ADVANCED("Advanced", "مشکل");

    fun label(language: String): String = if (language == "ur") ur else en
}

data class GuideChapter(
    val id: String,
    val illustrationRes: Int,
    val english: ChapterContent,
    val urdu: ChapterContent
) {
    fun content(language: String): ChapterContent =
        if (language == "ur") urdu else english
}

data class ChapterContent(
    val title: String,
    val summary: String,
    val body: String,
    val keyPoints: List<String>
)
