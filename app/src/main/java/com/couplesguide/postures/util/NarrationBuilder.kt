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

    fun buildMainGuideNarration(context: Context): String {
        LectureNotesRepository.ensureLoaded(context)
        val lang = LectureEmbedTtsEngine.ttsLanguageMode(context)
        val sb = StringBuilder(buildWelcomeNarration(context))
        for (studyClass in LectureNotesRepository.getClasses(context)) {
            sb.append(" ").append(context.getString(R.string.class_section_label, studyClass.gradeLabel))
            for (chapter in studyClass.chapters) {
                val content = if (lang == NarrativeLanguageHelper.MODE_UR) chapter.urdu else chapter.english
                sb.append(" ").append(content.title).append(". ").append(content.summary)
            }
        }
        return sb.toString()
    }

    fun buildMainGuideNarrationSegments(context: Context): List<Pair<String, String>> {
        val lang = NarrativeLanguageHelper.ttsLanguageForMode(LectureEmbedTtsEngine.ttsLanguageMode(context))
        return listOf(buildMainGuideNarration(context) to lang)
    }

    fun buildStudyChapterNarration(context: Context, chapter: StudyChapter): String {
        val lang = LectureEmbedTtsEngine.ttsLanguageMode(context)
        val content = if (lang == NarrativeLanguageHelper.MODE_UR) chapter.urdu else chapter.english
        val points = content.keyPoints.joinToString(". ")
        return "${content.title}. ${content.summary}. ${content.body}. $points"
    }

    fun buildStudyChapterNarrationSegments(
        context: Context,
        chapter: StudyChapter
    ): List<Pair<String, String>> {
        val lang = NarrativeLanguageHelper.ttsLanguageForMode(LectureEmbedTtsEngine.ttsLanguageMode(context))
        return listOf(buildStudyChapterNarration(context, chapter) to lang)
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
