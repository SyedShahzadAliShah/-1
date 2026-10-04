package com.couplesguide.postures.tutor

import android.content.Context
import com.couplesguide.postures.data.LectureNotesRepository
import com.couplesguide.postures.data.LecturePageIndex
import com.couplesguide.postures.data.StudyChapter
object TutorCorpus {

    @Volatile
    private var passages: List<TutorPassage>? = null

    fun ensureLoaded(context: Context): List<TutorPassage> {
        passages?.let { return it }
        return synchronized(this) {
            passages?.let { return it }
            val built = buildPassages(context.applicationContext)
            passages = built
            built
        }
    }

    fun invalidate() {
        passages = null
    }

    private fun buildPassages(context: Context): List<TutorPassage> {
        LectureNotesRepository.ensureLoaded(context)
        val out = mutableListOf<TutorPassage>()

        for (studyClass in LectureNotesRepository.getClasses(context)) {
            val classLabel = studyClass.gradeLabel
            for (chapter in studyClass.chapters) {
                addChapterPassages(out, studyClass.id, classLabel, chapter)
            }
            val indexAsset = "lecture_notes/cs_${studyClass.id}_pages.json"
            addPagePassages(context, out, studyClass.id, classLabel, indexAsset)
        }
        return out
    }

    private fun addChapterPassages(
        out: MutableList<TutorPassage>,
        classId: String,
        classLabel: String,
        chapter: StudyChapter
    ) {
        val combinedEn = buildString {
            append(chapter.english.summary)
            append(' ')
            append(chapter.english.body)
            chapter.english.keyPoints.forEach { append(' ').append(it) }
        }.trim()
        val combinedUr = buildString {
            append(chapter.urdu.summary)
            append(' ')
            append(chapter.urdu.body)
            chapter.urdu.keyPoints.forEach { append(' ').append(it) }
        }.trim()
        if (combinedEn.isNotBlank()) {
            out.add(
                TutorPassage(
                    classId = classId,
                    classLabel = classLabel,
                    chapterId = chapter.id,
                    chapterTitle = chapter.english.title,
                    page = chapter.pdfPageStart,
                    textEn = combinedEn,
                    textUr = combinedUr.ifBlank { combinedEn },
                    isGolden = combinedEn.contains('★') || chapter.english.keyPoints.any { it.contains('★') },
                    sourceLabel = "Chapter ${chapter.chapterNumber}: ${chapter.english.title}"
                )
            )
        }
        chapter.english.keyPoints.filter { it.length > 12 }.forEach { point ->
            val clean = point.trim()
            if (clean.isEmpty()) return@forEach
            out.add(
                TutorPassage(
                    classId = classId,
                    classLabel = classLabel,
                    chapterId = chapter.id,
                    chapterTitle = chapter.english.title,
                    page = chapter.pdfPageStart,
                    textEn = clean,
                    textUr = clean,
                    isGolden = clean.contains('★'),
                    sourceLabel = "Key point — ${chapter.english.title}"
                )
            )
        }
    }

    private fun addPagePassages(
        context: Context,
        out: MutableList<TutorPassage>,
        classId: String,
        classLabel: String,
        indexAsset: String
    ) {
        val pages = LecturePageIndex.load(context, indexAsset)
        for (page in pages) {
            val en = page.english.trim()
            if (en.length < 40) continue
            val ur = page.urdu.trim().ifBlank { page.urduTts.trim() }
            out.add(
                TutorPassage(
                    classId = classId,
                    classLabel = classLabel,
                    chapterId = null,
                    chapterTitle = "",
                    page = page.page,
                    textEn = en,
                    textUr = ur.ifBlank { en },
                    isGolden = en.contains('★') || en.contains("GOLDEN", ignoreCase = true),
                    sourceLabel = "PDF page ${page.page}"
                )
            )
        }
    }
}
