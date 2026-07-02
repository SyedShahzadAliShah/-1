package com.couplesguide.postures.data

import com.couplesguide.postures.R

object PostureRepository {

    const val CAT_ALL = "all"
    const val CAT_IMAGINATION = "imagination"

    fun getCategoryIds(): List<String> = SpectacularMovesRepository.getCategoryIds()

    fun getCategoryLabel(categoryId: String, language: String): String =
        SpectacularMovesRepository.getCategoryLabel(categoryId)

    fun getAllPostures(): List<Posture> = SpectacularMovesRepository.getAllMoves()

    fun getPhysicalPostures(): List<Posture> = SpectacularMovesRepository.getAllMoves()

    fun getImaginationPostures(): List<Posture> = emptyList()

    fun getPosturesByCategory(categoryId: String): List<Posture> =
        SpectacularMovesRepository.getMovesByCategory(categoryId)

    fun getPostureById(id: String): Posture? = SpectacularMovesRepository.getMoveById(id)
}
