package com.couplesguide.postures.data

data class PdfPage(
    val pageNumber: Int,
    val drawableRes: Int,
    val urduTitle: String,
    val urduNarration: String,
    val englishTitle: String,
    val englishNarration: String
)
