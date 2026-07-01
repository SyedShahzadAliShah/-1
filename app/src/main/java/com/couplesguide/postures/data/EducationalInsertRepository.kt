package com.couplesguide.postures.data

import com.couplesguide.postures.R

data class EducationalInsert(
    val id: String,
    val afterCategoryId: String,
    val illustrationRes: Int,
    val englishTitle: String,
    val urduTitle: String,
    val englishCaption: String,
    val urduCaption: String
)

object EducationalInsertRepository {

    private val inserts = listOf(
        EducationalInsert(
            id = "edu_face_contact",
            afterCategoryId = PostureRepository.CAT_CLASSIC,
            illustrationRes = R.drawable.pic_edu_face_contact,
            englishTitle = "Face-to-Face Education",
            urduTitle = "آمنے سامنے تعلیم",
            englishCaption = "Eye contact, kissing, and verbal check-ins deepen connection and safety.",
            urduCaption = "آنکھوں کا رابطہ، بوسہ، اور زبانی پوچھ گچھ تعلق اور محفوظ احساس بڑھاتے ہیں۔"
        ),
        EducationalInsert(
            id = "edu_consent_talk",
            afterCategoryId = PostureRepository.CAT_NON_PENETRATIVE,
            illustrationRes = R.drawable.pic_edu_consent_talk,
            englishTitle = "Ongoing Consent",
            urduTitle = "مسلسل رضامندی",
            englishCaption = "Ask what feels good. Either partner can pause or adjust at any time.",
            urduCaption = "پوچھیں کیا اچھا لگتا ہے۔ کوئی بھی ساتھی کسی وقت رک یا تبدیلی کر سکتا ہے۔"
        ),
        EducationalInsert(
            id = "edu_hip_pillow",
            afterCategoryId = PostureRepository.CAT_ELEVATED,
            illustrationRes = R.drawable.pic_edu_hip_pillow,
            englishTitle = "Hip Support Guide",
            urduTitle = "کولہے کی سہارا گائیڈ",
            englishCaption = "Elevating hips with a firm pillow improves angle and comfort for many couples.",
            urduCaption = "مضبوط تکیے سے کولہے اونچے کرنے سے بہت جوڑوں کے لیے زاویہ اور آرام بہتر ہوتا ہے۔"
        ),
        EducationalInsert(
            id = "edu_rear_safety",
            afterCategoryId = PostureRepository.CAT_ANAL,
            illustrationRes = R.drawable.pic_edu_rear_safety,
            englishTitle = "Anal Comfort & Safety",
            urduTitle = "پیچھے سے آرام اور حفاظت",
            englishCaption = "Generous lube, slow pace, and frequent check-ins are essential for anal play.",
            urduCaption = "کافی لوبریکنٹ، آہستہ رفتار، اور بار بار پوچھ گچھ پیچھے سے لطف کے لیے ضروری ہے۔"
        ),
        EducationalInsert(
            id = "edu_body_map",
            afterCategoryId = PostureRepository.CAT_CREATIVE,
            illustrationRes = R.drawable.pic_edu_body_map,
            englishTitle = "Know Your Body",
            urduTitle = "اپنے جسم کو جانیں",
            englishCaption = "Understanding body zones helps partners communicate about comfort and pleasure.",
            urduCaption = "جسم کے حصوں کو سمجھنا ساتھیوں کو آرام اور لطف کے بارے میں بات کرنے میں مدد دیتا ہے۔"
        )
    )

    fun getInsertAfterCategory(categoryId: String): EducationalInsert? =
        inserts.find { it.afterCategoryId == categoryId }

    fun getAllInserts(): List<EducationalInsert> = inserts
}
