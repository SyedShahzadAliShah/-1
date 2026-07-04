package com.pakrecipes.cooking.data

data class CityCategory(
    val id: String,
    val nameUrdu: String,
    val emoji: String
) {
    companion object {
        const val ALL = "all"
        const val KARACHI = "karachi"
        const val LAHORE = "lahore"
        const val PESHAWAR = "peshawar"
        const val QUETTA = "quetta"
        const val HYDERABAD = "hyderabad"
        const val MULTAN = "multan"
        const val ISLAMABAD = "islamabad"
        const val RAWALPINDI = "rawalpindi"
        const val GILGIT = "gilgit"

        fun all(): List<CityCategory> = listOf(
            CityCategory(ALL, "تمام", "🍽️"),
            CityCategory(KARACHI, "کراچی", "🌊"),
            CityCategory(LAHORE, "لاہور", "🌸"),
            CityCategory(PESHAWAR, "پشاور", "🏔️"),
            CityCategory(QUETTA, "کوئٹہ", "🌿"),
            CityCategory(HYDERABAD, "حیدرآباد", "🌶️"),
            CityCategory(MULTAN, "ملتان", "🌞"),
            CityCategory(ISLAMABAD, "اسلام آباد", "🏛️"),
            CityCategory(RAWALPINDI, "راولپنڈی", "🍲"),
            CityCategory(GILGIT, "گلگت بلتستان", "🏔️")
        )
    }
}
