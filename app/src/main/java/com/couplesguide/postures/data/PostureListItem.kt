package com.couplesguide.postures.data

sealed class PostureListItem {
    data class PostureEntry(val posture: Posture) : PostureListItem()
    data class EducationalCard(val insert: EducationalInsert) : PostureListItem()
}

object PostureListBuilder {

    fun build(postures: List<Posture>, @Suppress("UNUSED_PARAMETER") includeEducationalCards: Boolean): List<PostureListItem> =
        postures.map { PostureListItem.PostureEntry(it) }
}
