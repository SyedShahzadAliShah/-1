package com.couplesguide.postures.util

import android.content.Context
import com.couplesguide.postures.data.LectureNotesRepository

/** @deprecated Use [LectureEmbedTtsEngine.Session] */
class FullPdfTtsReader(
    narrator: VoiceNarrator
) {
    private val session = LectureEmbedTtsEngine.Session(narrator)

    fun stop() = session.stop()

    fun isRunning(): Boolean = session.isRunning()

    fun start(
        context: Context,
        classId: String,
        onPageStarted: (page: Int, total: Int) -> Unit,
        onFinished: () -> Unit
    ) {
        val studyClass = LectureNotesRepository.getClassById(context, classId) ?: return
        session.readEntireClass(
            context,
            classId,
            onPageStarted = { page, _ -> onPageStarted(page, studyClass.totalPages) },
            onFinished = onFinished
        )
    }
}
