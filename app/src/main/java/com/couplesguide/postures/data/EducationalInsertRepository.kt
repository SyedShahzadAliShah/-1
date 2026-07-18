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
            id = "edu_pakistani_tip",
            afterCategoryId = PostureRepository.CAT_PAKISTANI,
            illustrationRes = R.drawable.pic_edu_side_alignment,
            englishTitle = "Pakistani Station Tip",
            urduTitle = "پاکستانی سٹیشن مشورہ",
            englishCaption = "Pair biryani with raita and fresh salad. The karahi is best eaten immediately while sizzling hot.",
            urduCaption = "بریانی رائتہ اور تازہ سلاد کے ساتھ کھائیں۔ کڑاہی گرم گرم فوراً کھائیں۔"
        ),
        EducationalInsert(
            id = "edu_bbq_tip",
            afterCategoryId = PostureRepository.CAT_BBQ,
            illustrationRes = R.drawable.pic_edu_face_contact,
            englishTitle = "BBQ Station Tip",
            urduTitle = "باربی کیو سٹیشن مشورہ",
            englishCaption = "Visit the live grill when charcoal is at peak heat. Squeeze fresh lemon on kebabs before eating.",
            urduCaption = "کوئلے سب سے گرم ہونے پر گرل پر جائیں۔ کباب پر تازہ لیموں نچوڑیں۔"
        ),
        EducationalInsert(
            id = "edu_chinese_tip",
            afterCategoryId = PostureRepository.CAT_CHINESE,
            illustrationRes = R.drawable.pic_edu_rear_safety,
            englishTitle = "Chinese Station Tip",
            urduTitle = "چائنیز سٹیشن مشورہ",
            englishCaption = "Choose dishes straight from the wok for maximum freshness. Fried rice and Manchurian are the perfect combo.",
            urduCaption = "تازگی کے لیے ووک سے ابھی نکلی ڈشیں لیں۔ فرائیڈ رائس اور منچورین بہترین جوڑا۔"
        ),
        EducationalInsert(
            id = "edu_continental_tip",
            afterCategoryId = PostureRepository.CAT_CONTINENTAL,
            illustrationRes = R.drawable.pic_edu_body_map,
            englishTitle = "Continental Station Tip",
            urduTitle = "کونٹینینٹل سٹیشن مشورہ",
            englishCaption = "Grilled chicken pairs beautifully with mashed potatoes and garden salad for a balanced plate.",
            urduCaption = "گرل چکن مashed آلو اور گارڈن سلاد کے ساتھ متوازن پلیٹ بناتا ہے۔"
        ),
        EducationalInsert(
            id = "edu_salad_tip",
            afterCategoryId = PostureRepository.CAT_SALAD_SOUP,
            illustrationRes = R.drawable.pic_edu_body_map,
            englishTitle = "Salad Bar Tip",
            urduTitle = "سلاد بار مشورہ",
            englishCaption = "Start your buffet with light soups and salads. Corn soup with soy sauce and chili vinegar is a Lal Qila classic.",
            urduCaption = "بوفے ہلکے سوپ اور سلاد سے شروع کریں۔ سویا ساس اور چلی سرکہ والا کارن سوپ کلاسک ہے۔"
        ),
        EducationalInsert(
            id = "edu_bread_tip",
            afterCategoryId = PostureRepository.CAT_BREAD,
            illustrationRes = R.drawable.pic_edu_hip_pillow,
            englishTitle = "Tandoor Bread Tip",
            urduTitle = "تندور روٹی مشورہ",
            englishCaption = "Fresh naan from the tandoor is best with karahi and handi. Roghni naan is perfect with nihari.",
            urduCaption = "تندور سے تازہ نان کڑاہی اور ہانڈی کے ساتھ بہترین۔ روغنی نان نہاری کے ساتھ۔"
        )
    )

    fun getInsertAfterCategory(categoryId: String): EducationalInsert? =
        inserts.find { it.afterCategoryId == categoryId }
}
