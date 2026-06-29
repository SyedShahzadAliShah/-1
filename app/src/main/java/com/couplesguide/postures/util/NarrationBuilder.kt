package com.couplesguide.postures.util

import android.content.Context
import com.couplesguide.postures.R
import com.couplesguide.postures.data.GuideRepository
import com.couplesguide.postures.data.Posture
import com.couplesguide.postures.data.PostureRepository

object NarrationBuilder {

    fun buildWelcomeNarration(context: Context, language: String): String {
        val title = context.getString(R.string.welcome_title)
        val message = context.getString(R.string.welcome_message)
        return "$title. $message"
    }

    fun buildMainGuideNarration(context: Context, language: String): String {
        val sb = StringBuilder(buildWelcomeNarration(context, language))
        sb.append(" ").append(sectionLabel(context, R.string.guide_chapters, language)).append(".")
        for (chapter in GuideRepository.getChapters()) {
            val c = chapter.content(language)
            sb.append(" ").append(c.title).append(". ").append(c.summary)
        }
        sb.append(" ").append(sectionLabel(context, R.string.imagination_postures, language)).append(".")
        for (posture in PostureRepository.getImaginationPostures()) {
            val c = posture.content(language)
            sb.append(" ").append(c.name).append(". ").append(c.summary)
        }
        sb.append(" ").append(sectionLabel(context, R.string.all_postures, language)).append(".")
        for (posture in PostureRepository.getPhysicalPostures()) {
            val c = posture.content(language)
            sb.append(" ").append(c.name).append(". ").append(c.summary)
        }
        return sb.toString()
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
            "${stepLabel(context, i + 1, language)} $s"
        }.joinToString(". ")
        val tips = content.tips.joinToString(". ")
        return "${content.name}. ${content.summary}. ${content.description}. $stepsPrefix. $steps. $tipsLabel. $tips"
    }

    private fun sectionLabel(context: Context, resId: Int, @Suppress("UNUSED_PARAMETER") language: String): String =
        context.getString(resId)

    private fun stepLabel(context: Context, number: Int, language: String): String {
        return if (language == LocaleHelper.LANG_UR) {
            context.getString(R.string.step_label_ur, number)
        } else {
            context.getString(R.string.step_label_en, number)
        }
    }
}
