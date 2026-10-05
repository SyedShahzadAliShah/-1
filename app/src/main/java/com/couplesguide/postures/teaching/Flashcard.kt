package com.couplesguide.postures.teaching

data class Flashcard(
    val front: String,
    val back: String,
    val isGolden: Boolean
)

object FlashcardDeckBuilder {

    fun forChapter(chapterId: String, language: String, chapters: List<com.couplesguide.postures.data.StudyChapter>): List<Flashcard> {
        val chapter = chapters.find { it.id == chapterId } ?: return emptyList()
        val content = chapter.content(language)
        val cards = mutableListOf<Flashcard>()
        content.keyPoints.forEach { point ->
            val clean = point.replace('★', ' ').trim()
            if (clean.length < 8) return@forEach
            val front = if (language == "ur") {
                "باب ${chapter.chapterNumber}: یاد کریں"
            } else {
                "Ch.${chapter.chapterNumber}: Recall"
            }
            cards.add(
                Flashcard(
                    front = front,
                    back = clean,
                    isGolden = point.contains('★')
                )
            )
        }
        if (cards.isEmpty()) {
            cards.add(
                Flashcard(
                    front = content.title,
                    back = content.summary,
                    isGolden = false
                )
            )
        }
        return cards
    }
}
