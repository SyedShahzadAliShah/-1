package com.couplesguide.postures.teaching

import com.couplesguide.postures.data.ChapterContent
import com.couplesguide.postures.data.StudyChapter
import org.junit.Assert.assertTrue
import org.junit.Test

class TeachingQuizBankTest {

    @Test
    fun buildSession_hasValidCorrectIndex() {
        val chapter = sampleChapter(
            id = "xi_ch1",
            grade = "XI",
            number = 1,
            title = "Computer Systems",
            points = listOf("★ CPU is the brain of computer", "RAM is volatile memory storage")
        )
        val other = sampleChapter(
            id = "xi_ch2",
            grade = "XI",
            number = 2,
            title = "Algorithms",
            points = listOf("An algorithm is a step-by-step procedure")
        )
        val questions = TeachingQuizBank.buildSession(chapter, listOf(chapter, other), false)
        assertTrue(questions.isNotEmpty())
        questions.forEach { q ->
            assertTrue(q.correctIndex in q.choices.indices)
            assertTrue(q.choices[q.correctIndex].isNotBlank())
        }
    }

    private fun sampleChapter(
        id: String,
        grade: String,
        number: Int,
        title: String,
        points: List<String>
    ): StudyChapter {
        val content = ChapterContent(title, "summary", "body", points)
        return StudyChapter(
            id = id,
            grade = grade,
            chapterNumber = number,
            illustrationRes = 0,
            pdfAsset = "lecture_notes/cs_xi_lecture_notes.pdf",
            pdfPageStart = 1,
            pdfPageEnd = 10,
            english = content,
            urdu = content
        )
    }
}
