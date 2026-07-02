package com.couplesguide.postures.util

import android.content.Context
import com.couplesguide.postures.R
import com.couplesguide.postures.data.BookIntroRepository
import com.couplesguide.postures.data.Posture
import com.couplesguide.postures.data.PostureRepository
import com.couplesguide.postures.data.SpectacularMovesRepository

object NarrationBuilder {

    fun buildWelcomeNarration(context: Context, @Suppress("UNUSED_PARAMETER") language: String): String {
        val intro = BookIntroRepository.getIntroChapter().urdu
        return "${intro.title}. ${intro.summary}. ${intro.body}"
    }

    fun buildMainGuideNarration(context: Context, @Suppress("UNUSED_PARAMETER") language: String): String {
        val sb = StringBuilder(buildWelcomeNarration(context, LocaleHelper.LANG_UR))
        sb.append(" ").append(context.getString(R.string.all_postures)).append(".")
        for (posture in PostureRepository.getAllPostures()) {
            val c = posture.urdu
            sb.append(" ").append(c.name).append(". ").append(c.summary)
                .append(". ").append(c.description)
            c.steps.forEachIndexed { i, step ->
                sb.append(" قدم ").append(i + 1).append("۔ ").append(step)
            }
        }
        return sb.toString()
    }

    fun buildChapterNarration(chapterId: String, @Suppress("UNUSED_PARAMETER") language: String): String {
        if (chapterId != BookIntroRepository.getIntroChapter().id) return ""
        val content = BookIntroRepository.getIntroChapter().urdu
        val points = content.keyPoints.joinToString(". ")
        return "${content.title}. ${content.summary}. ${content.body}. $points"
    }

    fun buildPostureNarration(context: Context, posture: Posture, @Suppress("UNUSED_PARAMETER") language: String): String {
        val content = posture.urdu
        val steps = content.steps.mapIndexed { i, s ->
            "${context.getString(R.string.step_label_ur, i + 1)} $s"
        }.joinToString(". ")
        val tips = content.tips.joinToString(". ")
        return "${content.name}. ${content.summary}. ${content.description}. " +
            "${context.getString(R.string.how_to)}. $steps. ${context.getString(R.string.tips)}. $tips"
    }

    fun buildCategoryNarration(categoryId: String): String {
        if (categoryId == PostureRepository.CAT_ALL) return ""
        val label = SpectacularMovesRepository.getCategoryLabel(categoryId)
        val moves = SpectacularMovesRepository.getMovesByCategory(categoryId)
        val sb = StringBuilder("$label۔")
        for (move in moves) {
            sb.append(" ").append(move.urdu.name).append(". ").append(move.urdu.summary)
        }
        return sb.toString()
    }
}
