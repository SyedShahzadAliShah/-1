package com.couplesguide.postures.data

object PostureRepository {

    const val CAT_ALL = SheKnowsPostureRepository.CAT_ALL
    const val CAT_CLASSIC = SheKnowsPostureRepository.CAT_CLASSIC
    const val CAT_NON_PENETRATIVE = SheKnowsPostureRepository.CAT_NON_PENETRATIVE
    const val CAT_ELEVATED = SheKnowsPostureRepository.CAT_ELEVATED
    const val CAT_SHOWER = SheKnowsPostureRepository.CAT_SHOWER
    const val CAT_BONDAGE = SheKnowsPostureRepository.CAT_BONDAGE
    const val CAT_CAR = SheKnowsPostureRepository.CAT_CAR
    const val CAT_SOLO = SheKnowsPostureRepository.CAT_SOLO
    const val CAT_FLAT = SheKnowsPostureRepository.CAT_FLAT
    const val CAT_BLINDFOLD = SheKnowsPostureRepository.CAT_BLINDFOLD
    const val CAT_ANAL = SheKnowsPostureRepository.CAT_ANAL
    const val CAT_BEACH = SheKnowsPostureRepository.CAT_BEACH
    const val CAT_ORGASM = SheKnowsPostureRepository.CAT_ORGASM
    const val CAT_CREATIVE = SheKnowsPostureRepository.CAT_CREATIVE
    const val CAT_IMAGINATION = SheKnowsPostureRepository.CAT_IMAGINATION

    const val SHEKNOWS_SOURCE_URL = SheKnowsPostureRepository.SOURCE_URL

    fun getCategoryIds(): List<String> = SheKnowsPostureRepository.getCategoryIds()

    fun getCategoryLabel(categoryId: String, language: String): String =
        SheKnowsPostureRepository.getCategoryLabel(categoryId, language)

    fun getAllPostures(): List<Posture> =
        SheKnowsPostureRepository.getSheKnowsPostures() + ImaginationPostureRepository.getImaginationPostures()

    fun getPhysicalPostures(): List<Posture> = SheKnowsPostureRepository.getSheKnowsPostures()

    fun getImaginationPostures(): List<Posture> =
        ImaginationPostureRepository.getImaginationPostures()

    fun getPosturesByCategory(categoryId: String): List<Posture> {
        val all = getAllPostures()
        if (categoryId == CAT_ALL) return all
        return all.filter { it.categoryId == categoryId }
    }

    fun getPostureById(id: String): Posture? = getAllPostures().find { it.id == id }
}
