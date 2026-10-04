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
        val mode = NarrativeLanguageHelper.getMode(context)
        val sb = StringBuilder(buildWelcomeNarration(context))
        for (studyClass in LectureNotesRepository.getClasses(context)) {
            sb.append(" ").append(context.getString(R.string.class_section_label, studyClass.gradeLabel))
            for (chapter in studyClass.chapters) {
                sb.append(" ").append(chapterNarrationText(context, chapter.english, chapter.urdu, mode))
            }
        }
        return sb.toString()
    }

    fun buildMainGuideNarrationSegments(context: Context): List<Pair<String, String>> {
        val mode = NarrativeLanguageHelper.getMode(context)
        if (mode != NarrativeLanguageHelper.MODE_EMBED) {
            val lang = NarrativeLanguageHelper.ttsLanguageForMode(mode)
            return listOf(buildMainGuideNarration(context) to lang)
        }
        LectureNotesRepository.ensureLoaded(context)
        val segments = mutableListOf<Pair<String, String>>()
        segments.add(buildWelcomeNarration(context) to LocaleHelper.LANG_EN)
        for (studyClass in LectureNotesRepository.getClasses(context)) {
            for (chapter in studyClass.chapters) {
                val en = chapter.english
                val enText = "${en.title}. ${en.summary}. ${en.body}. ${en.keyPoints.joinToString(". ")}"
                segments.add(enText to LocaleHelper.LANG_EN)
                val ur = chapter.urdu
                val urText = "${ur.title}. ${ur.summary}. ${ur.body}. ${ur.keyPoints.joinToString(". ")}"
                segments.add(urText to LocaleHelper.LANG_UR)
            }
        }
        return segments
    }

    fun buildStudyChapterNarration(context: Context, chapter: StudyChapter): String {
        val mode = NarrativeLanguageHelper.getMode(context)
        return chapterNarrationText(context, chapter.english, chapter.urdu, mode)
    }

    fun buildStudyChapterNarrationSegments(
        context: Context,
        chapter: StudyChapter
    ): List<Pair<String, String>> {
        val mode = NarrativeLanguageHelper.getMode(context)
        val en = chapter.english
        val ur = chapter.urdu
        val enText = "${en.title}. ${en.summary}. ${en.body}. ${en.keyPoints.joinToString(". ")}"
        val urText = "${ur.title}. ${ur.summary}. ${ur.body}. ${ur.keyPoints.joinToString(". ")}"
        return when (mode) {
            NarrativeLanguageHelper.MODE_UR -> listOf(urText to LocaleHelper.LANG_UR)
            NarrativeLanguageHelper.MODE_EMBED -> listOf(
                enText to LocaleHelper.LANG_EN,
                urText to LocaleHelper.LANG_UR
            )
            else -> listOf(enText to LocaleHelper.LANG_EN)
        }
    }

    private fun chapterNarrationText(
        context: Context,
        english: com.couplesguide.postures.data.ChapterContent,
        urdu: com.couplesguide.postures.data.ChapterContent,
        mode: String
    ): String {
        val enText = "${english.title}. ${english.summary}. ${english.body}. ${english.keyPoints.joinToString(". ")}"
        val urText = "${urdu.title}. ${urdu.summary}. ${urdu.body}. ${urdu.keyPoints.joinToString(". ")}"
        return when (mode) {
            NarrativeLanguageHelper.MODE_UR -> urText
            NarrativeLanguageHelper.MODE_EMBED -> {
                val enLabel = context.getString(R.string.narrative_embed_en_label)
                val urLabel = context.getString(R.string.narrative_embed_ur_label)
                "$enLabel $enText $urLabel $urText"
            }
            else -> enText
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
}
