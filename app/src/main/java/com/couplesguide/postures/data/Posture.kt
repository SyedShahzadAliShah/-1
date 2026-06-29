package com.couplesguide.postures.data

data class Posture(
    val id: String,
    val name: String,
    val category: String,
    val summary: String,
    val description: String,
    val steps: List<String>,
    val tips: List<String>,
    val difficulty: Difficulty,
    val illustrationRes: Int
)

enum class Difficulty(val label: String) {
    BEGINNER("Beginner"),
    INTERMEDIATE("Intermediate"),
    ADVANCED("Advanced")
}
