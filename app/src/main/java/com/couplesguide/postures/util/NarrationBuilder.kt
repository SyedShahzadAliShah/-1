package com.couplesguide.postures.util

import android.content.Context
import com.couplesguide.postures.R
import com.couplesguide.postures.data.LectureNotesRepository
import com.couplesguide.postures.data.GuideRepository
import com.couplesguide.postures.data.Posture
import com.couplesguide.postures.data.StudyChapter

object NarrationBuilder {

    fun buildWelcomeNarration(
        context: Context,
        @Suppress("UNUSED_PARAMETER") language: String
    ): String {
        val title = context.getString(R.string.welcome_title)
        val message = context.getString(R.string.welcome_message)
        return "$title. $message"
    }

    fun buildMainGuideNarration(context: Context, language: String): String {
        LectureNotesRepository.ensureLoaded(context)
        val sb = StringBuilder(buildWelcomeNarration(context, language))
        for (studyClass in LectureNotesRepository.getClasses(context)) {
            sb.append(" ").append(context.getString(R.string.class_section_label, studyClass.gradeLabel))
            for (chapter in studyClass.chapters) {
                val c = chapter.content(language)
                sb.append(" ").append(c.title).append(". ").append(c.summary)
            }
        }
        return sb.toString()
    }

    fun buildStudyChapterNarration(chapter: StudyChapter, language: String): String {
        val content = chapter.content(language)
        val points = content.keyPoints.joinToString(". ")
        return "${content.title}. ${content.summary}. ${content.body}. $points"
    }

    fun buildChapterNarration(chapterId: String, language: String): String {
        val chapter = GuideRepository.getChapterById(chapterId) ?: return ""
        val content = chapter.content(language)
        val points = content.keyPoints.joinToString(". ")
        return "${content.title}. ${content.summary}. ${content.body}. $points"
    }

    fun buildPostureNarration(context: Context, posture: Posture, language: String): String {
        val content = posture.content(language)
        val stepsPrefix = if (posture.isImagination) {
            context.getString(R.string.imagination_exercise)
        } else {
            context.getString(R.string.how_to)
        }
        val tipsLabel = context.getString(R.string.tips)
        val steps = content.steps.mapIndexed { i, s ->
            val label = if (language == LocaleHelper.LANG_UR) {
                context.getString(R.string.step_label_ur, i + 1)
            } else {
                context.getString(R.string.step_label_en, i + 1)
            }
            "$label $s"
        }.joinToString(". ")
        val tips = content.tips.joinToString(". ")
        return "${content.name}. ${content.summary}. ${content.description}. $stepsPrefix. $steps. $tipsLabel. $tips"
    }
}
