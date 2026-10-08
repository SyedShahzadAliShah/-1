package com.sindhcs.lectures.data

data class Catalog(val grades: List<Grade>)

data class Grade(
    val id: String,
    val title: String,
    val urdu: String,
    val curriculum: String,
    val chapters: List<Chapter>
)

data class Chapter(
    val num: Int,
    val title: String,
    val topics: List<Topic>
) {
    val goldenCount: Int get() = topics.count { it.golden }
}

data class Topic(
    val id: String,
    val title: String,
    val golden: Boolean,
    val learn: String,
    val urdu: String,
    val spokenUrdu: String, // classroom Urdish (Urdu grammar + English CS terms)
    val readSeconds: Int, // estimated Urdish TTS time; FLV is timed to this
    val terms: List<String>,
    val board: String,
    val flv: String
)
