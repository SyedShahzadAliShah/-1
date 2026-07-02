package com.couplesguide.postures.util

/**
 * Helpers for formatting Urdu text in PDF output.
 *
 * All methods return strings that start with a Right-to-Left Mark (U+200F) so
 * that Android's BiDi algorithm correctly identifies the paragraph direction as
 * RTL, even when the StaticLayout also has setTextDirection(RTL) set.  The RLM
 * is a zero-width character and does not affect glyph rendering.
 *
 * Character choices:
 *  - Bullet: EN DASH (–, U+2013) — present in every Unicode font including
 *    Noto Naskh Arabic; preferred over ▪/▸/◄ which are absent from the font.
 *  - Digits: Extended Arabic-Indic (۰–۹) — the script-native digit set.
 *  - Punctuation: Arabic Full Stop (۔, U+06D4).
 */
object UrduPdfText {

    private const val RLM = "\u200F"   // RIGHT-TO-LEFT MARK (invisible, zero-width)
    private const val NDASH = "\u2013" // EN DASH – safe in Naskh

    private val urduDigits = charArrayOf('۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹')

    /** Prepend RLM to ensure RTL paragraph direction. */
    fun normalize(text: String): String {
        val t = text.trim()
        return if (t.isEmpty()) t else "$RLM$t"
    }

    fun toUrduDigits(number: Int): String =
        number.toString().map { if (it.isDigit()) urduDigits[it - '0'] else it }.joinToString("")

    /**
     * Bullet item: `– text`
     * In RTL layout the dash appears at the visual start (right edge) and the
     * text extends to the left — correct for Urdu reading order.
     */
    fun bulletItem(text: String): String = normalize("$NDASH $text")

    /**
     * Numbered step: `۱۔ text`
     * The Urdu numeral + full stop appear on the right side in RTL layout.
     */
    fun numberedItem(index: Int, text: String): String =
        normalize("${toUrduDigits(index)}۔ $text")

    /**
     * Meta separator line: `category   |   difficulty`
     * In RTL layout the first argument appears on the right side.
     */
    fun metaLine(left: String, right: String): String =
        normalize("$left   |   $right")

    fun pageNumber(number: Int): String = toUrduDigits(number)
}
