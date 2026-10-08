package com.couplesguide.postures.data

data class CsLecture(
    val id: String,
    val chapter: Int,
    val title: String,
    val englishSummary: String,
    val urduNarration: String,
    val topicIds: List<String>,
    val topicCount: Int,
    val goldenCount: Int
) {
    fun topics(allTopics: List<CsTopic>): List<CsTopic> {
        val order = topicIds.withIndex().associate { it.value to it.index }
        return allTopics
            .filter { order.containsKey(it.id) }
            .sortedBy { order[it.id] }
    }
}
