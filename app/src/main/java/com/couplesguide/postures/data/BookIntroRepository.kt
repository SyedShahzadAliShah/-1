package com.couplesguide.postures.data

import com.couplesguide.postures.R

object BookIntroRepository {

    fun getIntroChapter(): GuideChapter = GuideChapter(
        id = "book_intro",
        illustrationRes = R.drawable.pic_guide_cover,
        english = introContent(),
        urdu = introContent()
    )

    private fun introContent() = ChapterContent(
        title = "شاندار حرکتیں — وہ کبھی نہیں بھولے گی",
        summary = "Sonia Borg کی کتاب سے ۳۰ تصویری حرکتیں — مکمل اردو تعلیم۔",
        body = "یہ ایپ \"Spectacular Sex Moves She'll Never Forget\" کی م attachment سے تیار ہے۔ " +
            "ہر حرکت کی اصل تصویر ایمبیڈ ہے، ساتھ میں گہرائی سے اردو وضاحت: تصور کیا ہے، کیوں کام کرتا ہے، " +
            "قدم بہ قدم طریقہ، اور مشورے۔ آواز میں سنیں (اردو TTS) یا مکمل PDF برآمد کریں۔ " +
            "رضامندی، آرام، اور باہمی احترام ہر حرکت سے پہلے ضروری ہے۔",
        keyPoints = listOf(
            "۳۰ حرکتیں — اصل PDF تصاویر ایمبیڈ",
            "تصور، طریقہ، اور کیوں یہ مؤثر ہے — اردو میں",
            "آواز میں سنیں (اردو TTS)",
            "مکمل یا الگ حرکت PDF برآمد"
        )
    )
}
