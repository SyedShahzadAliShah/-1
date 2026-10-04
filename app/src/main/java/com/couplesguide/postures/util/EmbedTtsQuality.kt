package com.couplesguide.postures.util

object EmbedTtsQuality {

    private const val MIN_SPEAKABLE_CHARS = 24

    private val BOILERPLATE = Regex(
        "(?i)(table of contents|reference note|page \\d+\\s+of|-- \\d+ of \\d+ --|bilingual teacher)"
    )

    fun isMeaningfulForTts(raw: String, language: String): Boolean {
        val prepared = NaturalLanguageTtsPreparer.prepare(raw, language).trim()
        if (prepared.length < MIN_SPEAKABLE_CHARS) return false
        if (BOILERPLATE.containsMatchIn(prepared) && prepared.length < 80) return false
        val letters = prepared.count { it.isLetter() || it in '\u0600'..'\u06FF' }
        return letters >= 12
    }

    fun excerptForCaption(raw: String, language: String, maxLen: Int = 220): String {
        val prepared = NaturalLanguageTtsPreparer.prepare(raw, language).trim()
        if (prepared.isEmpty()) return ""
        return if (prepared.length <= maxLen) prepared else prepared.take(maxLen).trimEnd() + "…"
    }
}
