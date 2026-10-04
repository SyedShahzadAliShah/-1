package com.couplesguide.postures.util

/**
 * Adds gentle pauses between sentences for Google Text-to-speech (SSML).
 */
object TtsSsmlBuilder {

    private val SENTENCE_END = Regex("(?<=[.!?؟۔])\\s+")

    fun addNaturalPauses(plain: String): String {
        val trimmed = plain.trim()
        if (trimmed.isEmpty()) return trimmed
        if (trimmed.startsWith("<speak", ignoreCase = true)) return trimmed

        val escaped = escapeForSsml(trimmed)
        val sentences = escaped.split(SENTENCE_END).filter { it.isNotBlank() }
        if (sentences.size <= 1) {
            return "<speak>$escaped</speak>"
        }
        val body = sentences.joinToString("") { sentence ->
            "<s>${sentence.trim()}</s><break time=\"420ms\"/>"
        }
        return "<speak>$body</speak>"
    }

    private fun escapeForSsml(text: String): String {
        return text
            .replace("&", "&amp;")
            .replace("<", "")
            .replace(">", "")
    }
}
