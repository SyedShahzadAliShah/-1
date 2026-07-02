package com.seccap.admissions.data

data class Zone(
    val id: String,
    val name: LocalizedText
)

data class College(
    val id: String,
    val name: LocalizedText,
    val zoneId: String,
    val faculties: List<String>,
    val seats: Int,
    val lastYearCutoff: Double
)

object CollegeRepository {

    fun getZones(): List<Zone> = listOf(
        Zone("karachi", LocalizedText("Karachi", "کراچی")),
        Zone("hyderabad", LocalizedText("Hyderabad", "حیدرآباد")),
        Zone("sukkur", LocalizedText("Sukkur", "سکھر")),
        Zone("larkana", LocalizedText("Larkana", "لاڑکانہ")),
        Zone("mirpurkhas", LocalizedText("Mirpurkhas", "میرپورخاص")),
        Zone("nawabshah", LocalizedText("Shaheed Benazirabad", "شہید بینظیرآباد")),
        Zone("khairpur", LocalizedText("Khairpur", "خیرپور"))
    )

    fun getColleges(): List<College> = listOf(
        College("dj_science", LocalizedText("D.J. Science College Karachi", "ڈی جے سائنس کالج کراچی"), "karachi", listOf("pre_medical", "pre_engineering", "computer_science"), 450, 82.5),
        College("adamjee", LocalizedText("Adamjee Government Science College", "آدم جی گورنمنٹ سائنس کالج"), "karachi", listOf("pre_medical", "pre_engineering"), 400, 80.0),
        College("st_joseph", LocalizedText("St. Joseph Government College", "سینٹ جوزف گورنمنٹ کالج"), "karachi", listOf("commerce", "humanities", "computer_science"), 350, 65.0),
        College("govt_college_women_khi", LocalizedText("Government College for Women Karachi", "گورنمنٹ کالج فار ویمن کراچی"), "karachi", listOf("pre_medical", "home_economics", "humanities"), 300, 75.0),
        College("nabi_bux", LocalizedText("Nabi Bux Bhutto Government College", "نبی بخش بھٹو گورنمنٹ کالج"), "larkana", listOf("pre_medical", "pre_engineering", "commerce"), 280, 72.0),
        College("govt_college_hyd", LocalizedText("Government College Hyderabad", "گورنمنٹ کالج حیدرآباد"), "hyderabad", listOf("pre_medical", "pre_engineering", "computer_science", "commerce"), 380, 70.0),
        College("sachal_hyd", LocalizedText("Sachal Sarmast Government College", "سچل سرمست گورنمنٹ کالج"), "hyderabad", listOf("humanities", "commerce"), 250, 55.0),
        College("govt_college_sukkur", LocalizedText("Government College Sukkur", "گورنمنٹ کالج سکھر"), "sukkur", listOf("pre_medical", "pre_engineering", "commerce"), 320, 68.0),
        College("govt_college_mirpurkhas", LocalizedText("Government College Mirpurkhas", "گورنمنٹ کالج میرپورخاص"), "mirpurkhas", listOf("pre_medical", "commerce", "humanities"), 200, 60.0),
        College("govt_college_nawabshah", LocalizedText("Government College Nawabshah", "گورنمنٹ کالج نوابشاہ"), "nawabshah", listOf("pre_medical", "pre_engineering", "computer_science"), 300, 67.0),
        College("govt_college_khairpur", LocalizedText("Government College Khairpur", "گورنمنٹ کالج خیرپور"), "khairpur", listOf("pre_medical", "commerce", "humanities"), 220, 58.0),
        College("govt_science_college_khi", LocalizedText("Government Science College Karachi", "گورنمنٹ سائنس کالج کراچی"), "karachi", listOf("pre_engineering", "computer_science"), 350, 78.0),
        College("forman_christian", LocalizedText("Forman Christian College (Affiliated)", "فورمین کرسچن کالج (وابستہ)"), "karachi", listOf("humanities", "commerce"), 180, 62.0),
        College("govt_college_women_hyd", LocalizedText("Government College for Women Hyderabad", "گورنمنٹ کالج فار ویمن حیدرآباد"), "hyderabad", listOf("pre_medical", "home_economics", "humanities"), 260, 70.0),
        College("govt_college_larkana", LocalizedText("Government College Larkana", "گورنمنٹ کالج لاڑکانہ"), "larkana", listOf("pre_medical", "pre_engineering", "commerce"), 290, 65.0)
    )

    fun findZone(id: String): Zone? = getZones().find { it.id == id }

    fun findCollege(id: String): College? = getColleges().find { it.id == id }

    fun collegesInZone(zoneId: String, facultyId: String? = null): List<College> {
        return getColleges().filter { college ->
            college.zoneId == zoneId &&
                (facultyId == null || facultyId in college.faculties)
        }.sortedByDescending { it.lastYearCutoff }
    }

    fun collegesForFaculty(facultyId: String): List<College> =
        getColleges().filter { facultyId in it.faculties }
}
