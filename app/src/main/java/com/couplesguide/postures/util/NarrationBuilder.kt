package com.couplesguide.postures.util

import android.content.Context
import com.couplesguide.postures.R
import com.couplesguide.postures.data.SexEdLesson
import com.couplesguide.postures.data.SexEducationRepository

object NarrationBuilder {

    fun buildWelcomeNarration(context: Context): String {
        val title = context.getString(R.string.welcome_title)
        val message = context.getString(R.string.welcome_message)
        return "$title. $message"
    }

    fun buildFullGuideNarration(context: Context): String {
        val sb = StringBuilder(buildWelcomeNarration(context))
        for (section in SexEducationRepository.getSections()) {
            sb.append(" ").append(section.title).append(". ")
            for (lesson in section.lessons) {
                sb.append(lesson.title).append(". ").append(lesson.summary).append(". ")
            }
        }
        return sb.toString()
    }

    fun buildLessonNarration(lesson: SexEdLesson): String {
        val points = lesson.keyPoints.joinToString(". ")
        return "${lesson.title}. ${lesson.summary}. ${lesson.body}. اہم نکات. $points"
    }

    fun buildLessonNarration(lessonId: String): String {
        val lesson = SexEducationRepository.getLessonById(lessonId) ?: return ""
        return buildLessonNarration(lesson)
    }
}
