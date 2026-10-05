package com.couplesguide.postures.teaching

import android.content.Context
import com.couplesguide.postures.data.LectureNotesRepository
import com.couplesguide.postures.data.StudyChapter

object LessonPlanner {

    fun suggestNextChapter(context: Context): StudyChapter? {
        LectureNotesRepository.ensureLoaded(context)
        val chapters = LectureNotesRepository.getClasses(context).flatMap { it.chapters }
        return chapters.firstOrNull { TeachingProgressStore.chapterProgressPercent(context, it.id) < 100 }
            ?: chapters.lastOrNull()
    }

    fun nextIncompleteStep(context: Context, chapterId: String): LessonStep? {
        return LessonStep.all.firstOrNull { !TeachingProgressStore.isStepComplete(context, chapterId, it) }
    }
}
