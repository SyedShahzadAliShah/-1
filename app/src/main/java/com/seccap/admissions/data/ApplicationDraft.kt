package com.seccap.admissions.data

data class ApplicationDraft(
    var matricRollNumber: String = "",
    var ninthRollNumber: String = "",
    var boardName: String = "",
    var passingYear: String = "",
    var totalMarks: String = "",
    var obtainedMarks: String = "",
    var grade: String = "",
    var schoolName: String = "",
    var studentName: String = "",
    var fatherName: String = "",
    var gender: String = "",
    var dateOfBirth: String = "",
    var bFormNumber: String = "",
    var cnicNumber: String = "",
    var religion: String = "",
    var domicile: String = "",
    var phoneNumber: String = "",
    var email: String = "",
    var address: String = "",
    var facultyId: String = "",
    var zoneId: String = "",
    var collegePreferences: List<String> = emptyList(),
    var documentsChecked: Set<String> = emptySet(),
    var lastUpdated: Long = System.currentTimeMillis()
) {
    val percentage: Double
        get() {
            val total = totalMarks.toDoubleOrNull() ?: return 0.0
            val obtained = obtainedMarks.toDoubleOrNull() ?: return 0.0
            return if (total > 0) (obtained / total) * 100 else 0.0
        }

    val applicationId: String
        get() {
            val roll = matricRollNumber.ifBlank { ninthRollNumber }
            return if (roll.isBlank()) "DRAFT" else "SECCAP-$roll"
        }

    fun isEducationalComplete(): Boolean =
        matricRollNumber.isNotBlank() &&
            ninthRollNumber.isNotBlank() &&
            boardName.isNotBlank() &&
            passingYear.isNotBlank() &&
            totalMarks.isNotBlank() &&
            obtainedMarks.isNotBlank() &&
            schoolName.isNotBlank()

    fun isPersonalComplete(): Boolean =
        studentName.isNotBlank() &&
            fatherName.isNotBlank() &&
            gender.isNotBlank() &&
            dateOfBirth.isNotBlank() &&
            bFormNumber.isNotBlank() &&
            phoneNumber.isNotBlank() &&
            domicile.isNotBlank()

    fun isFacultyComplete(): Boolean = facultyId.isNotBlank()

    fun isZoneComplete(): Boolean = zoneId.isNotBlank()

    fun isCollegesComplete(): Boolean = collegePreferences.size in 1..5

    fun isDocumentsComplete(): Boolean = documentsChecked.size >= 4

    fun completionPercent(): Int {
        var done = 0
        if (isEducationalComplete()) done++
        if (isPersonalComplete()) done++
        if (isFacultyComplete()) done++
        if (isZoneComplete() && isCollegesComplete()) done++
        if (isDocumentsComplete()) done++
        return (done * 100) / 5
    }
}
