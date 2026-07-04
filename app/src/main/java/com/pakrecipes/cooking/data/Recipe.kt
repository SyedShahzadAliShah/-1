package com.pakrecipes.cooking.data

enum class Difficulty(val labelUrdu: String) {
    EASY("آسان"),
    MEDIUM("درمیانہ"),
    HARD("مشکل")
}

data class Recipe(
    val id: String,
    val nameUrdu: String,
    val cityId: String,
    val descriptionUrdu: String,
    val prepTimeMinutes: Int,
    val cookTimeMinutes: Int,
    val servings: Int,
    val difficulty: Difficulty,
    val ingredientsUrdu: List<String>,
    val stepsUrdu: List<String>,
    val tipsUrdu: List<String>
)
