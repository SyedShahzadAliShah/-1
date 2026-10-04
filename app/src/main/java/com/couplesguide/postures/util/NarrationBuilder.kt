package com.couplesguide.postures.util

import android.content.Context
import com.couplesguide.postures.R
import com.couplesguide.postures.data.GuideRepository
import com.couplesguide.postures.data.LectureNotesRepository
import com.couplesguide.postures.data.Posture
import com.couplesguide.postures.data.StudyChapter

object NarrationBuilder {

    fun buildWelcomeNarration(context: Context): String {
        val title = context.getString(R.string.welcome_title)
        val message = context.getString(R.string.welcome_message)
        return "$title. $message"
    }

    private fun buildMainGuideNarration(context: Context, useUrdu: Boolean): String {
        LectureNotesRepository.ensureLoaded(context)
        val sb = StringBuilder(buildWelcomeNarration(context))
        for (studyClass in LectureNotesRepository.getClasses(context)) {
            sb.append(" ").append(context.getString(R.string.class_section_label, studyClass.gradeLabel))
            for (chapter in studyClass.chapters) {
                val content = if (useUrdu) chapter.urdu else chapter.english
                sb.append(" ").append(content.title).append(". ").append(content.summary)
            }
        }
        return sb.toString()
    }

    fun buildMainGuideNarrationSegments(context: Context): List<Pair<String, String>> {
        return segmentsForMode(context) { mode ->
            when (mode) {
                NarrativeLanguageHelper.MODE_UR ->
                    listOf(buildMainGuideNarration(context, useUrdu = true) to LocaleHelper.LANG_UR)
                NarrativeLanguageHelper.MODE_BOTH -> listOf(
                    buildMainGuideNarration(context, useUrdu = false) to LocaleHelper.LANG_EN,
                    buildMainGuideNarration(context, useUrdu = true) to LocaleHelper.LANG_UR
                )
                else ->
                    listOf(buildMainGuideNarration(context, useUrdu = false) to LocaleHelper.LANG_EN)
            }
        }
    }

    private fun buildStudyChapterNarration(context: Context, chapter: StudyChapter, useUrdu: Boolean): String {
        val content = if (useUrdu) chapter.urdu else chapter.english
        val points = content.keyPoints.joinToString(". ")
        return "${content.title}. ${content.summary}. ${content.body}. $points"
    }

    fun buildStudyChapterNarrationSegments(
        context: Context,
        chapter: StudyChapter
    ): List<Pair<String, String>> {
        return segmentsForMode(context) { mode ->
            when (mode) {
                NarrativeLanguageHelper.MODE_UR ->
                    listOf(buildStudyChapterNarration(context, chapter, useUrdu = true) to LocaleHelper.LANG_UR)
                NarrativeLanguageHelper.MODE_BOTH -> listOf(
                    buildStudyChapterNarration(context, chapter, useUrdu = false) to LocaleHelper.LANG_EN,
                    buildStudyChapterNarration(context, chapter, useUrdu = true) to LocaleHelper.LANG_UR
                )
                else ->
                    listOf(buildStudyChapterNarration(context, chapter, useUrdu = false) to LocaleHelper.LANG_EN)
            }
        }
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

    private inline fun segmentsForMode(
        context: Context,
        block: (mode: String) -> List<Pair<String, String>>
    ): List<Pair<String, String>> {
        val mode = NarrativeLanguageHelper.getMode(context)
        return block(mode).filter { it.first.isNotBlank() }
    }
}
