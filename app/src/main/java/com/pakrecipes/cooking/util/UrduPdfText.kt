package com.pakrecipes.cooking.util

import android.icu.text.Bidi
import android.os.Build

object UrduPdfText {

    fun normalize(text: String): String {
        return if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.N) {
            try {
                val bidi = Bidi(text, Bidi.DIRECTION_DEFAULT_RIGHT_TO_LEFT.toInt())
                bidi.writeReordered(Bidi.DO_MIRRORING.toInt())
            } catch (_: Exception) {
                text
            }
        } else {
            text
        }
    }

    fun bulletItem(text: String): String = "• $text"

    fun numberedItem(number: Int, text: String): String {
        val urduNum = toUrduDigits(number.toString())
        return "$urduNum۔ $text"
    }

    fun pageNumber(number: Int): String = toUrduDigits(number.toString())

    fun metaLine(category: String, difficulty: String): String =
        "$category  |  $difficulty"

    private fun toUrduDigits(s: String): String {
        return s.map {
            when (it) {
                '0' -> '۰'
                '1' -> '۱'
                '2' -> '۲'
                '3' -> '۳'
                '4' -> '۴'
                '5' -> '۵'
                '6' -> '۶'
                '7' -> '۷'
                '8' -> '۸'
                '9' -> '۹'
                else -> it
            }
        }.joinToString("")
    }
}
