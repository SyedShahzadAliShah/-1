package com.couplesguide.postures.data

data class RecipeLocalizedContent(
    val name: String,
    val category: String,
    val summary: String,
    val description: String,
    val ingredients: List<String>,
    val steps: List<String>,
    val tips: List<String>
)

data class Recipe(
    val id: String,
    val difficulty: Difficulty,
    val illustrationRes: Int,
    val categoryId: String,
    val prepMinutes: Int,
    val cookMinutes: Int,
    val servings: Int,
    val english: RecipeLocalizedContent,
    val urdu: RecipeLocalizedContent
) {
    fun content(language: String): RecipeLocalizedContent =
        if (language == "ur") urdu else english
}
