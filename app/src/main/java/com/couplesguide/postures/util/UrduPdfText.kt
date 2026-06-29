package com.couplesguide.postures.util

object UrduPdfText {

    private const val RLM = "\u200F"
    private val urduDigits = charArrayOf('۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹')

    fun normalize(text: String): String {
        if (text.isBlank()) return text
        val trimmed = text.trim()
        return if (trimmed.startsWith(RLM)) trimmed else RLM + trimmed
    }

    fun toUrduDigits(number: Int): String =
        number.toString().map { if (it.isDigit()) urduDigits[it - '0'] else it }.joinToString("")

    fun bulletItem(text: String): String = normalize("▪ $text")

    fun numberedItem(index: Int, text: String): String =
        normalize("${toUrduDigits(index)}۔ $text")

    fun metaLine(left: String, right: String): String =
        normalize("$left   |   $right")

    fun pageNumber(number: Int): String = toUrduDigits(number)
}
