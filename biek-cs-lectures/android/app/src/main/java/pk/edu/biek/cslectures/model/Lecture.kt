package pk.edu.biek.cslectures.model

data class Concept(
    val term: String,
    val english: String,
    val urdu: String,
    val urdish: String,
)

data class Lecture(
    val id: String,
    val year: String,
    val number: Int,
    val title: String,
    val urduTitle: String,
    val pdfAsset: String,
    val introUrdu: String,
    val introUrdish: String,
    val concepts: List<Concept>,
)
