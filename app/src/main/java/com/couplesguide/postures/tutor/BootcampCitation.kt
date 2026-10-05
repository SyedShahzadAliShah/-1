package com.couplesguide.postures.tutor

import android.content.Context
import com.couplesguide.postures.data.LectureNotesRepository
import com.couplesguide.postures.data.StudyChapter

/**
 * Formats required bootcamp source citations (Sindh CS XI/XII teacher PDF + chapter + page).
 */
object BootcampCitation {

    private val SYLLABUS_REF = Regex("\\b(\\d+\\.\\d+(?:\\.\\d+)?)\\b")

    fun findChapterForPage(context: Context, classId: String, page: Int): StudyChapter? {
        LectureNotesRepository.ensureLoaded(context)
        return LectureNotesRepository.getChaptersForClass(context, classId)
            .find { page in it.pdfPageStart..it.pdfPageEnd }
    }

    fun extractSyllabusRef(text: String): String? {
        return SYLLABUS_REF.find(text)?.groupValues?.getOrNull(1)
    }

    fun format(
        context: Context,
        passage: TutorPassage,
        index: Int,
        useUrdu: Boolean
    ): String {
        val chapter = passage.chapterId?.let { LectureNotesRepository.getChapterById(context, it) }
            ?: passage.page?.let { findChapterForPage(context, passage.classId, it) }
        val page = passage.page
        val topicRef = extractSyllabusRef(passage.textEn) ?: extractSyllabusRef(passage.textUr)
        val golden = if (passage.isGolden) " ★" else ""

        return if (useUrdu) {
            buildString {
                append("[$index] سندھ CS جماعت ${passage.classLabel}")
                if (chapter != null) {
                    append(" • باب ${chapter.chapterNumber}: ${chapter.urdu.title}")
                    append(" • PDF صفحات ${chapter.pdfPageStart}–${chapter.pdfPageEnd}")
                    if (page != null) append(" • حوالہ صفحہ $page")
                } else if (page != null) {
                    append(" • PDF صفحہ $page")
                }
                if (topicRef != null) append(" • نصاب §$topicRef")
                append(golden)
                append(" • ${shortAssetName(chapter?.pdfAsset ?: passage.classId)}")
            }
        } else {
            buildString {
                append("[$index] Sindh CS Class ${passage.classLabel}")
                if (chapter != null) {
                    append(" • Ch.${chapter.chapterNumber} ${chapter.english.title}")
                    append(" • Teacher PDF pp. ${chapter.pdfPageStart}–${chapter.pdfPageEnd}")
                    if (page != null) append(" • cite p. $page")
                } else if (page != null) {
                    append(" • Teacher PDF p. $page")
                }
                if (topicRef != null) append(" • Syllabus §$topicRef")
                append(golden)
                append(" • ${shortAssetName(chapter?.pdfAsset ?: passage.classId)}")
            }
        }
    }

    fun referencesBlock(
        context: Context,
        passages: List<TutorPassage>,
        useUrdu: Boolean
    ): String {
        if (passages.isEmpty()) return ""
        val header = if (useUrdu) "📚 Bootcamp حوالہ جات (لازمی)" else "📚 Bootcamp references (required)"
        val lines = passages.distinctBy { it.classId + (it.page ?: 0) + (it.chapterId ?: "") }
            .take(4)
            .mapIndexed { i, p -> format(context, p, i + 1, useUrdu) }
        return header + "\n" + lines.joinToString("\n")
    }

    fun forChapter(context: Context, chapter: StudyChapter, useUrdu: Boolean): String {
        val passage = TutorPassage(
            classId = chapter.id.substringBefore("_ch"),
            classLabel = chapter.grade,
            chapterId = chapter.id,
            chapterTitle = chapter.english.title,
            page = chapter.pdfPageStart,
            textEn = chapter.english.title,
            textUr = chapter.urdu.title,
            isGolden = chapter.english.keyPoints.any { it.contains('★') },
            sourceLabel = "Chapter ${chapter.chapterNumber}"
        )
        return format(context, passage, 1, useUrdu)
    }

    fun groundingWithCitations(
        context: Context,
        passages: List<Pair<TutorPassage, String>>
    ): String {
        return passages.mapIndexed { index, (passage, excerpt) ->
            val cite = format(context, passage, index + 1, false)
            "$cite\n$excerpt"
        }.joinToString("\n\n---\n\n")
    }

    private fun shortAssetName(pdfAssetOrClassId: String): String {
        if (pdfAssetOrClassId.endsWith(".pdf")) {
            return pdfAssetOrClassId.substringAfterLast('/')
        }
        return "cs_${pdfAssetOrClassId}_lecture_notes.pdf"
    }
}
