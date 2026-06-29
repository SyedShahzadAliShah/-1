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

    fun buildChapterNarration(chapterId: String, language: String): String {
        val chapter = GuideRepository.getChapterById(chapterId) ?: return ""
        val content = chapter.content(language)
        val points = content.keyPoints.joinToString(". ")
        return "${content.title}. ${content.summary}. ${content.body}. $points"
    }

    fun buildPostureNarration(posture: Posture, language: String): String {
        val content = posture.content(language)
        val steps = content.steps.mapIndexed { i, s -> "Step ${i + 1}. $s" }.joinToString(". ")
        val tips = content.tips.joinToString(". ")
        return "${content.name}. ${content.summary}. ${content.description}. $steps. Tips. $tips"
    }

    fun buildFullGuideNarration(context: Context, language: String): String {
        val sb = StringBuilder(buildWelcomeNarration(context, language))
        for (chapter in GuideRepository.getChapters()) {
            val c = chapter.content(language)
            sb.append(" ").append(c.title).append(". ").append(c.summary)
        }
        for (posture in PostureRepository.getAllPostures()) {
            val c = posture.content(language)
            sb.append(" ").append(c.name).append(". ").append(c.summary)
        }
        return sb.toString()
    }
}
