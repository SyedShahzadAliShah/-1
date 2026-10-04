package com.couplesguide.postures.util

/**
 * Normalizes Urdu embed TTS text so punctuation yields natural pauses instead of
 * being spelled out (common with Latin . , ? ( ) in machine-translated lecture notes).
 */
object UrduTtsPronunciation {

    private val DECIMAL = Regex("\\d+\\.\\d+")
    private val MULTISPACE = Regex("\\s+")
    private val NEEDS_SPACE_AFTER = Regex("([۔،؟؛:!])(\\S)")

    fun prepare(raw: String): String {
        if (raw.isBlank()) return raw

        val decimals = mutableListOf<String>()
        var text = raw.trim()
        text = DECIMAL.replace(text) { match ->
            val token = "§DEC${decimals.size}§"
            decimals.add(match.value)
            token
        }

        text = text.replace('\n', ' ')
        text = MULTISPACE.replace(text, " ")

        text = text.replace('?', '؟')
        text = text.replace(',', '،')
        text = text.replace(';', '؛')
        text = text.replace(Regex("\\.(?=\\s|$)"), "۔")
        text = text.replace(Regex("\\.(?=[\\u0600-\\u06FF])"), "۔")

        text = text.replace("(", "، ")
            .replace(")", "، ")
            .replace("[", "، ")
            .replace("]", "، ")
            .replace("{", "، ")
            .replace("}", "، ")

        text = text.replace("=", "، ")
            .replace("/", "، ")
            .replace("&", " اور ")
            .replace("-", " ")
            .replace(":", "، ")
            .replace("|", "، ")

        text = text.replace("\"", " ")
            .replace("'", " ")
            .replace("«", " ")
            .replace("»", " ")
            .replace("★", " ")
            .replace("*", " ")
            .replace("#", " ")
            .replace("@", " ")
            .replace("^", " ")
            .replace("`", " ")
            .replace("~", " ")

        text = text.replace(Regex("(\\d)\\s*%"), "$1 فیصد")
        text = text.replace("%", " فیصد ")

        text = text.replace("!", "۔ ")
        text = expandLatinTermsForUrduSpeech(text)
        text = NEEDS_SPACE_AFTER.replace(text, "$1 $2")
        text = text.replace(Regex("([۔،؟؛])\\1+"), "$1")
        text = MULTISPACE.replace(text, " ").trim()

        decimals.forEachIndexed { index, value ->
            text = text.replace("§DEC${index}§", value)
        }

        return text.trim()
    }

    /** Latin syllabus terms spoken slowly so Urdu voices do not robot-spell them. */
    private fun expandLatinTermsForUrduSpeech(text: String): String {
        var t = text
        val replacements = listOf(
            "TCP/IP" to "ٹی سی پی آئی پی",
            "SDLC" to "ایس ڈی ایل سی",
            "OSI" to "او ایس آئی",
            "HCI" to "اچ سی آئی",
            "NLP" to "این ایل پی",
            "IDE" to "آئی ڈی ای",
            "API" to "اے پی آئی",
            "UI" to "یو آئی",
            "UX" to "یو ایکس",
            "K-Map" to "کرناو میپ",
            "K Maps" to "کرناو میپس",
            "Boolean" to "بولین",
            "Python" to "پائتھن",
            "e.g." to "مثال کے طور پر",
            "vs" to "بمقابلہ",
        ).sortedByDescending { it.first.length }
        for ((latin, spoken) in replacements) {
            t = t.replace(latin, spoken, ignoreCase = true)
        }
        t = t.replace(Regex("\\be\\.g\\.", RegexOption.IGNORE_CASE), "مثال کے طور پر")
        return t
    }
}
