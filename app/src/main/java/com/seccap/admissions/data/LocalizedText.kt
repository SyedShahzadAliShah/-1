package com.seccap.admissions.data

data class LocalizedText(
    val english: String,
    val urdu: String
) {
    fun get(language: String): String =
        if (language == "ur") urdu else english
}
