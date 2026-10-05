package com.couplesguide.postures.teaching

import android.content.Context
import com.couplesguide.postures.data.LectureNotesRepository

object TeachingProgressStore {

    private const val PREFS = "teaching_progress"

    fun isStepComplete(context: Context, chapterId: String, step: LessonStep): Boolean {
        return prefs(context).getBoolean(key(chapterId, step), false)
    }

    fun markStepComplete(context: Context, chapterId: String, step: LessonStep) {
        prefs(context).edit().putBoolean(key(chapterId, step), true).apply()
    }

    fun clearStep(context: Context, chapterId: String, step: LessonStep) {
        prefs(context).edit().putBoolean(key(chapterId, step), false).apply()
    }

    fun getQuizBestPercent(context: Context, chapterId: String): Int {
        return prefs(context).getInt("quiz_best_$chapterId", 0)
    }

    fun saveQuizResult(context: Context, chapterId: String, correct: Int, total: Int) {
        if (total <= 0) return
        val percent = (correct * 100) / total
        val prev = getQuizBestPercent(context, chapterId)
        if (percent > prev) {
            prefs(context).edit().putInt("quiz_best_$chapterId", percent).apply()
        }
        if (percent >= 60) {
            markStepComplete(context, chapterId, LessonStep.QUIZ)
        }
    }

    fun chapterProgressPercent(context: Context, chapterId: String): Int {
        val done = LessonStep.all.count { isStepComplete(context, chapterId, it) }
        return (done * 100) / LessonStep.all.size
    }

    fun overallProgressPercent(context: Context): Int {
        LectureNotesRepository.ensureLoaded(context)
        val chapters = LectureNotesRepository.getClasses(context).flatMap { it.chapters }
        if (chapters.isEmpty()) return 0
        val sum = chapters.sumOf { chapterProgressPercent(context, it.id) }
        return sum / chapters.size
    }

    fun completedChapterCount(context: Context): Int {
        LectureNotesRepository.ensureLoaded(context)
        return LectureNotesRepository.getClasses(context)
            .flatMap { it.chapters }
            .count { chapterProgressPercent(context, it.id) >= 100 }
    }

    private fun prefs(context: Context) =
        context.applicationContext.getSharedPreferences(PREFS, Context.MODE_PRIVATE)

    private fun key(chapterId: String, step: LessonStep) = "step_${chapterId}_${step.prefKey}"
}
