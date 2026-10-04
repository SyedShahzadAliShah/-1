package com.couplesguide.postures.util

import android.content.Context
import com.couplesguide.postures.data.LectureNotesRepository
import com.couplesguide.postures.data.LecturePageIndex
import com.couplesguide.postures.data.StudyChapter

/**
 * Embedded lecture reader: plays TTS from bundled per-page [en_tts] / [ur_tts] assets.
 * English only, Urdu only, or **both** (English then Urdu per page).
 */
object LectureEmbedTtsEngine {

    fun ttsLanguageMode(context: Context): String =
        NarrativeLanguageHelper.getMode(context)

    fun captionForPage(context: Context, indexAsset: String, pageNumber: Int): String =
        LecturePageIndex.narrationForPageWithMode(
            context,
            indexAsset,
            pageNumber,
            ttsLanguageMode(context)
        )

    fun segmentsForPage(context: Context, indexAsset: String, pageNumber: Int): List<Pair<String, String>> =
        LecturePageIndex.ttsSegmentsForPage(
            context,
            indexAsset,
            pageNumber,
            ttsLanguageMode(context)
        )

    class Session(private val narrator: VoiceNarrator) {
        private var cancelled = false

        fun stop() {
            cancelled = true
            narrator.stop()
        }

        fun isRunning(): Boolean = !cancelled && narrator.isSpeaking()

        fun readEntireClass(
            context: Context,
            classId: String,
            onPageStarted: (page: Int, total: Int) -> Unit,
            onFinished: () -> Unit
        ) {
            val studyClass = LectureNotesRepository.getClassById(context, classId) ?: return
        readPageRange(
            context,
            indexAsset = studyClass.pageIndexAsset,
            startPage = 1,
            endPage = studyClass.totalPages,
            progressTotal = studyClass.totalPages,
            onPageStarted = onPageStarted,
            onFinished = onFinished
        )
        }

        fun readChapter(
            context: Context,
            chapter: StudyChapter,
            onPageStarted: (page: Int, total: Int) -> Unit,
            onFinished: () -> Unit
        ) {
            val classId = chapter.id.substringBefore("_ch")
            val studyClass = LectureNotesRepository.getClassById(context, classId) ?: return
            readPageRange(
                context,
                indexAsset = studyClass.pageIndexAsset,
                startPage = chapter.pdfPageStart,
                endPage = chapter.pdfPageEnd,
                progressTotal = studyClass.totalPages,
                onPageStarted = onPageStarted,
                onFinished = onFinished
            )
        }

        fun readPageRange(
            context: Context,
            indexAsset: String,
            startPage: Int,
            endPage: Int,
            progressTotal: Int,
            onPageStarted: (page: Int, total: Int) -> Unit,
            onFinished: () -> Unit
        ) {
            cancelled = false
            readPageAt(
                context,
                indexAsset,
                startPage,
                endPage,
                progressTotal,
                onPageStarted,
                onFinished
            )
        }

        fun speakSinglePage(
            context: Context,
            indexAsset: String,
            pageNumber: Int,
            onComplete: (() -> Unit)? = null
        ) {
            val segments = segmentsForPage(context, indexAsset, pageNumber)
            if (segments.isEmpty()) {
                onComplete?.invoke()
                return
            }
            narrator.speakSegments(segments, onComplete)
        }

        private fun readPageAt(
            context: Context,
            indexAsset: String,
            page: Int,
            endPage: Int,
            progressTotal: Int,
            onPageStarted: (page: Int, total: Int) -> Unit,
            onFinished: () -> Unit
        ) {
            if (cancelled) {
                onFinished()
                return
            }
            if (page > endPage) {
                onFinished()
                return
            }
            onPageStarted(page, progressTotal)

            val segments = segmentsForPage(context, indexAsset, page)
            if (segments.isEmpty()) {
                readPageAt(context, indexAsset, page + 1, endPage, progressTotal, onPageStarted, onFinished)
                return
            }
            narrator.speakSegments(segments) {
                if (cancelled) {
                    onFinished()
                } else {
                    readPageAt(context, indexAsset, page + 1, endPage, progressTotal, onPageStarted, onFinished)
                }
            }
        }
    }
}
