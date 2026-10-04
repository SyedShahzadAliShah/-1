package com.couplesguide.postures.tutor

data class TutorPassage(
    val classId: String,
    val classLabel: String,
    val chapterId: String?,
    val chapterTitle: String,
    val page: Int?,
    val textEn: String,
    val textUr: String,
    val isGolden: Boolean,
    val sourceLabel: String
)

data class TutorChatMessage(
    val role: Role,
    val text: String,
    val timestampMs: Long = System.currentTimeMillis()
) {
    enum class Role { USER, TUTOR }
}

data class TutorContext(
    val chapterId: String? = null,
    val classId: String? = null,
    val page: Int? = null
)
