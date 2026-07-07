package com.couplesguide.postures.data

data class PdfBookPage(
    val pageNumber: Int,
    val assetImage: String,
    val titleUr: String,
    val narrationUr: String,
    val sectionType: SectionType = SectionType.CONTENT
) {
    enum class SectionType {
        COVER, INTRO, ETHICS, POSITIONS, MASSAGE, AFTERCARE, FANTASY, PROHIBITED, CLOSING, CONTENT
    }
}
