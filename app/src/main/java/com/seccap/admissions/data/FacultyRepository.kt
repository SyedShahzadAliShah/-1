package com.seccap.admissions.data

data class FacultyGroup(
    val id: String,
    val name: LocalizedText,
    val description: LocalizedText,
    val minPercentage: Double,
    val subjects: LocalizedText
)

object FacultyRepository {

    fun getAll(): List<FacultyGroup> = listOf(
        FacultyGroup(
            id = "pre_medical",
            name = LocalizedText("Pre-Medical", "پری میڈیکل"),
            description = LocalizedText(
                "For students pursuing MBBS, BDS, DPT, and allied health sciences.",
                "ایم بی بی ایس، بی ڈی ایس، ڈی پی ٹی اور متعلقہ صحت کی تعلیم کے لیے۔"
            ),
            minPercentage = 60.0,
            subjects = LocalizedText("Biology, Chemistry, Physics", "حیاتیات، کیمسٹری، طبیعیات")
        ),
        FacultyGroup(
            id = "pre_engineering",
            name = LocalizedText("Pre-Engineering", "پری انجینئرنگ"),
            description = LocalizedText(
                "For students pursuing engineering, architecture, and technology degrees.",
                "انجینئرنگ، آرکیٹیکچر اور ٹیکنالوجی کی ڈگریوں کے لیے۔"
            ),
            minPercentage = 55.0,
            subjects = LocalizedText("Mathematics, Physics, Chemistry", "ریاضی، طبیعیات، کیمسٹری")
        ),
        FacultyGroup(
            id = "computer_science",
            name = LocalizedText("Computer Science", "کمپیوٹر سائنس"),
            description = LocalizedText(
                "For BS Computer Science, IT, Software Engineering, and Data Science.",
                "بی ایس کمپیوٹر سائنس، آئی ٹی، سافٹ ویئر انجینئرنگ اور ڈیٹا سائنس کے لیے۔"
            ),
            minPercentage = 50.0,
            subjects = LocalizedText("Mathematics, Physics, Computer Science", "ریاضی، طبیعیات، کمپیوٹر سائنس")
        ),
        FacultyGroup(
            id = "commerce",
            name = LocalizedText("Commerce", "کامرس"),
            description = LocalizedText(
                "For B.Com, BBA, and business administration programs.",
                "بی کام، بی بی اے اور بزنس ایڈمنسٹریشن پروگراموں کے لیے۔"
            ),
            minPercentage = 45.0,
            subjects = LocalizedText("Accounting, Economics, Business Math", "اکاؤنٹنگ، معاشیات، بزنس ریاضی")
        ),
        FacultyGroup(
            id = "humanities",
            name = LocalizedText("Humanities", "ہیومینٹیز"),
            description = LocalizedText(
                "For arts, social sciences, languages, and general bachelor's programs.",
                "آرٹس، سماجی علوم، زبانیں اور عمومی بیچلر پروگراموں کے لیے۔"
            ),
            minPercentage = 40.0,
            subjects = LocalizedText("English, Urdu, Islamiat, Pakistan Studies", "انگریزی، اردو، اسلامیات، پاکستان اسٹڈیز")
        ),
        FacultyGroup(
            id = "home_economics",
            name = LocalizedText("Home Economics", "ہوم اکنامکس"),
            description = LocalizedText(
                "For nutrition, textile design, and family sciences programs.",
                "نیوٹریشن، ٹیکسٹائل ڈیزائن اور فیملی سائنسز پروگراموں کے لیے۔"
            ),
            minPercentage = 45.0,
            subjects = LocalizedText("Home Economics, Biology, Chemistry", "ہوم اکنامکس، حیاتیات، کیمسٹری")
        )
    )

    fun findById(id: String): FacultyGroup? = getAll().find { it.id == id }

    fun eligibleFaculties(percentage: Double): List<FacultyGroup> =
        getAll().filter { percentage >= it.minPercentage }
}
