package com.seccap.admissions.data

import android.content.Context

object DraftRepository {

    private const val PREFS = "seccap_draft_prefs"

    private fun prefs(context: Context) =
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)

    fun load(context: Context): ApplicationDraft {
        val p = prefs(context)
        return ApplicationDraft(
            matricRollNumber = p.getString("matric_roll", "") ?: "",
            ninthRollNumber = p.getString("ninth_roll", "") ?: "",
            boardName = p.getString("board", "") ?: "",
            passingYear = p.getString("year", "") ?: "",
            totalMarks = p.getString("total_marks", "") ?: "",
            obtainedMarks = p.getString("obtained_marks", "") ?: "",
            grade = p.getString("grade", "") ?: "",
            schoolName = p.getString("school", "") ?: "",
            studentName = p.getString("name", "") ?: "",
            fatherName = p.getString("father", "") ?: "",
            gender = p.getString("gender", "") ?: "",
            dateOfBirth = p.getString("dob", "") ?: "",
            bFormNumber = p.getString("bform", "") ?: "",
            cnicNumber = p.getString("cnic", "") ?: "",
            religion = p.getString("religion", "") ?: "",
            domicile = p.getString("domicile", "") ?: "",
            phoneNumber = p.getString("phone", "") ?: "",
            email = p.getString("email", "") ?: "",
            address = p.getString("address", "") ?: "",
            facultyId = p.getString("faculty", "") ?: "",
            zoneId = p.getString("zone", "") ?: "",
            collegePreferences = p.getString("colleges", "")?.split("|")?.filter { it.isNotBlank() } ?: emptyList(),
            documentsChecked = p.getString("docs", "")?.split("|")?.filter { it.isNotBlank() }?.toSet() ?: emptySet(),
            lastUpdated = p.getLong("updated", 0L)
        )
    }

    fun save(context: Context, draft: ApplicationDraft) {
        draft.lastUpdated = System.currentTimeMillis()
        prefs(context).edit()
            .putString("matric_roll", draft.matricRollNumber)
            .putString("ninth_roll", draft.ninthRollNumber)
            .putString("board", draft.boardName)
            .putString("year", draft.passingYear)
            .putString("total_marks", draft.totalMarks)
            .putString("obtained_marks", draft.obtainedMarks)
            .putString("grade", draft.grade)
            .putString("school", draft.schoolName)
            .putString("name", draft.studentName)
            .putString("father", draft.fatherName)
            .putString("gender", draft.gender)
            .putString("dob", draft.dateOfBirth)
            .putString("bform", draft.bFormNumber)
            .putString("cnic", draft.cnicNumber)
            .putString("religion", draft.religion)
            .putString("domicile", draft.domicile)
            .putString("phone", draft.phoneNumber)
            .putString("email", draft.email)
            .putString("address", draft.address)
            .putString("faculty", draft.facultyId)
            .putString("zone", draft.zoneId)
            .putString("colleges", draft.collegePreferences.joinToString("|"))
            .putString("docs", draft.documentsChecked.joinToString("|"))
            .putLong("updated", draft.lastUpdated)
            .apply()
    }

    fun hasDraft(context: Context): Boolean {
        val draft = load(context)
        return draft.completionPercent() > 0
    }

    fun clear(context: Context) {
        prefs(context).edit().clear().apply()
    }
}
