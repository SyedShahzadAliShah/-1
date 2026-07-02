package com.seccap.admissions.util

object UrduPdfText {

    private const val RLM = "\u200F"
    private const val NDASH = "\u2013"

    private val urduDigits = charArrayOf('۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹')

    fun normalize(text: String): String {
        val t = text.trim()
        return if (t.isEmpty()) t else "$RLM$t"
    }

    fun toUrduDigits(number: Int): String =
        number.toString().map { if (it.isDigit()) urduDigits[it - '0'] else it }.joinToString("")

    fun bulletItem(text: String): String = normalize("$NDASH $text")

    fun numberedItem(index: Int, text: String): String =
        normalize("${toUrduDigits(index)}۔ $text")

    fun metaLine(left: String, right: String): String =
        normalize("$left   |   $right")

    fun pageNumber(number: Int): String = toUrduDigits(number)
}
