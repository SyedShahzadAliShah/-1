package com.couplesguide.postures.teaching

import com.couplesguide.postures.data.StudyChapter
data class QuizQuestion(
    val prompt: String,
    val choices: List<String>,
    val correctIndex: Int,
    val citationHint: String
)

object TeachingQuizBank {

    private const val QUESTIONS_PER_SESSION = 5

    fun buildSession(
        chapter: StudyChapter,
        allChapters: List<StudyChapter>,
        useUrdu: Boolean
    ): List<QuizQuestion> {
        val content = if (useUrdu) chapter.urdu else chapter.english
        val points = content.keyPoints
            .map { it.replace('★', ' ').trim() }
            .filter { it.length > 12 }
        if (points.isEmpty()) {
            return listOf(summaryQuestion(chapter, allChapters, useUrdu))
        }
        val pool = points.shuffled().take(QUESTIONS_PER_SESSION)
        val distractorPool = allChapters
            .filter { it.id != chapter.id }
            .flatMap { (if (useUrdu) it.urdu else it.english).keyPoints }
            .map { it.replace('★', ' ').trim() }
            .filter { it.length > 12 }
            .distinct()

        return pool.map { correct ->
            val distractors = distractorPool
                .filter { it != correct }
                .shuffled()
                .take(3)
            val choices = (distractors + correct).shuffled()
            val correctIndex = choices.indexOf(correct)
            val prompt = if (useUrdu) {
                "اس باب کے نوٹس میں درست نکتہ کون سا ہے؟"
            } else {
                "Which key point belongs to ${content.title} in your bootcamp notes?"
            }
            QuizQuestion(
                prompt = prompt,
                choices = choices,
                correctIndex = correctIndex.coerceAtLeast(0),
                citationHint = "Ch.${chapter.chapterNumber} pp.${chapter.pdfPageStart}–${chapter.pdfPageEnd}"
            )
        }
    }

    private fun summaryQuestion(
        chapter: StudyChapter,
        allChapters: List<StudyChapter>,
        useUrdu: Boolean
    ): QuizQuestion {
        val content = if (useUrdu) chapter.urdu else chapter.english
        val correct = content.title
        val distractors = allChapters
            .filter { it.id != chapter.id }
            .map { (if (useUrdu) it.urdu else it.english).title }
            .shuffled()
            .take(3)
        val choices = (distractors + correct).shuffled()
        return QuizQuestion(
            prompt = if (useUrdu) "یہ باب کس عنوان سے ہے؟" else "What is the title of this chapter?",
            choices = choices,
            correctIndex = choices.indexOf(correct).coerceAtLeast(0),
            citationHint = "Ch.${chapter.chapterNumber}"
        )
    }
}
