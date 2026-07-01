package com.couplesguide.postures.data

sealed class PostureListItem {
    data class PostureEntry(val posture: Posture) : PostureListItem()
    data class EducationalCard(val insert: EducationalInsert) : PostureListItem()
}

object PostureListBuilder {

    private val categoryOrder = listOf(
        PostureRepository.CAT_CLASSIC,
        PostureRepository.CAT_NON_PENETRATIVE,
        PostureRepository.CAT_ELEVATED,
        PostureRepository.CAT_SHOWER,
        PostureRepository.CAT_BONDAGE,
        PostureRepository.CAT_CAR,
        PostureRepository.CAT_SOLO,
        PostureRepository.CAT_FLAT,
        PostureRepository.CAT_BLINDFOLD,
        PostureRepository.CAT_ANAL,
        PostureRepository.CAT_BEACH,
        PostureRepository.CAT_ORGASM,
        PostureRepository.CAT_CREATIVE
    )

    fun build(postures: List<Posture>, includeEducationalCards: Boolean): List<PostureListItem> {
        if (!includeEducationalCards) {
            return postures.map { PostureListItem.PostureEntry(it) }
        }

        val imagination = postures.filter { it.isImagination }
        val physical = postures.filter { !it.isImagination }
        val orderedPhysical = categoryOrder.flatMap { categoryId ->
            physical.filter { it.categoryId == categoryId }
        }

        val items = mutableListOf<PostureListItem>()
        var lastCategory: String? = null

        for (posture in orderedPhysical) {
            if (lastCategory != null && lastCategory != posture.categoryId) {
                EducationalInsertRepository.getInsertAfterCategory(lastCategory)?.let { insert ->
                    items.add(PostureListItem.EducationalCard(insert))
                }
            }
            items.add(PostureListItem.PostureEntry(posture))
            lastCategory = posture.categoryId
        }

        lastCategory?.let { categoryId ->
            EducationalInsertRepository.getInsertAfterCategory(categoryId)?.let { insert ->
                if (items.none { it is PostureListItem.EducationalCard && it.insert.id == insert.id }) {
                    items.add(PostureListItem.EducationalCard(insert))
                }
            }
        }

        imagination.forEach { items.add(PostureListItem.PostureEntry(it)) }
        return items
    }
}
