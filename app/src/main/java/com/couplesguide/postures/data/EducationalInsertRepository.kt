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
            afterCategoryId = PostureRepository.CAT_FACE,
            illustrationRes = R.drawable.pic_edu_face_contact,
            englishTitle = "Face-to-Face Education",
            urduTitle = "آمنے سامنے تعلیم",
            englishCaption = "Eye contact, kissing, and verbal check-ins deepen connection and safety.",
            urduCaption = "آنکھوں کا رابطہ، بوسہ، اور زبانی پوچھ گچھ تعلق اور محفوظ احساس بڑھاتے ہیں۔"
        ),
        EducationalInsert(
            id = "edu_side_alignment",
            afterCategoryId = PostureRepository.CAT_SIDE,
            illustrationRes = R.drawable.pic_edu_side_alignment,
            englishTitle = "Side-by-Side Alignment",
            urduTitle = "ساتھ ساتھ ہم آہنگی",
            englishCaption = "Use a pillow between knees to align hips and reduce strain.",
            urduCaption = "گھٹنوں کے درمیان تکیہ رکھیں تاکہ کولہے ہم آہنگ رہیں اور دباؤ کم ہو۔"
        ),
        EducationalInsert(
            id = "edu_rear_safety",
            afterCategoryId = PostureRepository.CAT_REAR,
            illustrationRes = R.drawable.pic_edu_rear_safety,
            englishTitle = "Rear Entry Comfort",
            urduTitle = "پیچھے سے آرام",
            englishCaption = "Hip pillows, slow pace, and frequent check-ins keep this position comfortable.",
            urduCaption = "کولہے کے تکیے، آہستہ رفتار، اور بار بار پوچھ گچھ اس پوزیشن کو آرام دہ رکھتی ہے۔"
        ),
        EducationalInsert(
            id = "edu_hip_pillow",
            afterCategoryId = PostureRepository.CAT_STANDING,
            illustrationRes = R.drawable.pic_edu_hip_pillow,
            englishTitle = "Hip Support Guide",
            urduTitle = "کولہے کی سہارا گائیڈ",
            englishCaption = "Elevating hips with a firm pillow improves angle and comfort for many couples.",
            urduCaption = "مضبوط تکیے سے کولہے اونچے کرنے سے بہت جوڑوں کے لیے زاویہ اور آرام بہتر ہوتا ہے۔"
        ),
        EducationalInsert(
            id = "edu_body_map",
            afterCategoryId = PostureRepository.CAT_VARIATIONS,
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
