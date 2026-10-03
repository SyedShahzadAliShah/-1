package com.couplesguide.postures.util

import android.content.Context
import com.couplesguide.postures.R
import com.couplesguide.postures.data.CsTeacherRepository
import com.couplesguide.postures.data.CsTopic

object NarrationBuilder {

    fun buildWelcomeNarration(context: Context): String {
        val books = CsTeacherRepository.getBooks(context)
        val intro = context.getString(R.string.welcome_narration_urdu)
        val bookTitles = books.map { it.title }.joinToString("۔ ")
        return "$intro $bookTitles"
    }

    fun buildTopicNarration(topic: CsTopic): String {
        val narration = topic.urduNarration.trim()
        if (narration.isNotEmpty()) {
            return narration
        }
        return topic.title
    }
}
