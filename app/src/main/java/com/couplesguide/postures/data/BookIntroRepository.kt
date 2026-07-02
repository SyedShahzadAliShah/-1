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
        summary = "سونیا بورگ کی کتاب سے ۳۰ منفرد پوزیشنز اور تکنیکیں۔",
        body = "یہ ایپ Sonia Borg کی کتاب \"Spectacular Sex Moves She'll Never Forget\" " +
            "پر مبنی ہے۔ نو حصوں میں ۳۰ حرکتیں ہیں — ہر ایک مختصر اردو وضاحت، " +
            "آواز میں سننے اور PDF برآمد کے ساتھ۔ رضامندی، آرام اور باہمی احترام ہمیشہ پہلے۔",
        keyPoints = listOf(
            "۳۰ منفرد حرکتیں — ۹ زمرے",
            "مختصر اردو وضاحتیں",
            "آواز میں سنیں (اردو TTS)",
            "مکمل PDF برآمد"
        )
    )
}
