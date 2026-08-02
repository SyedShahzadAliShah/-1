package com.couplesguide.postures.util

import android.content.Context
import com.couplesguide.postures.R
import com.couplesguide.postures.data.BuffetGuideRepository
import com.couplesguide.postures.data.Recipe
import com.couplesguide.postures.data.RecipeRepository

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
        val sb = StringBuilder(buildWelcomeNarration(context, language))
        sb.append(" ").append(sectionLabel(context, R.string.guide_chapters, language)).append(".")
        for (chapter in BuffetGuideRepository.getChapters()) {
            val c = chapter.content(language)
            sb.append(" ").append(c.title).append(". ").append(c.summary)
        }
        sb.append(" ").append(sectionLabel(context, R.string.all_recipes, language)).append(".")
        for (recipe in RecipeRepository.getAllRecipes()) {
            val c = recipe.content(language)
            sb.append(" ").append(c.name).append(". ").append(c.summary)
        }
        return sb.toString()
    }

    fun buildChapterNarration(chapterId: String, language: String): String {
        val chapter = BuffetGuideRepository.getChapterById(chapterId) ?: return ""
        val content = chapter.content(language)
        val points = content.keyPoints.joinToString(". ")
        return "${content.title}. ${content.summary}. ${content.body}. $points"
    }

    fun buildRecipeNarration(context: Context, recipe: Recipe, language: String): String {
        val content = recipe.content(language)
        val ingredientsLabel = context.getString(R.string.ingredients)
        val methodLabel = context.getString(R.string.method)
        val tipsLabel = context.getString(R.string.tips)
        val ingredients = content.ingredients.joinToString(". ")
        val steps = content.steps.mapIndexed { i, s ->
            "${stepLabel(context, i + 1, language)} $s"
        }.joinToString(". ")
        val tips = content.tips.joinToString(". ")
        val timeInfo = if (language == LocaleHelper.LANG_UR) {
            "تیاری ${recipe.prepMinutes} منٹ۔ پکانا ${recipe.cookMinutes} منٹ۔ ${recipe.servings} افرد کے لیے۔"
        } else {
            "Preparation ${recipe.prepMinutes} minutes. Cooking ${recipe.cookMinutes} minutes. Serves ${recipe.servings}."
        }
        return "${content.name}. ${content.summary}. ${content.description}. $timeInfo. " +
            "$ingredientsLabel. $ingredients. $methodLabel. $steps. $tipsLabel. $tips"
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
