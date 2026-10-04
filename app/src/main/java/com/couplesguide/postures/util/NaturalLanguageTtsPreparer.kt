package com.couplesguide.postures.util

/**
 * Turns lecture-note extract text into phrasing that embedded TTS reads as natural speech
 * instead of spelling symbols, table debris, or raw PDF layout.
 */
object NaturalLanguageTtsPreparer {

    private const val REGEX_META = ".^$|?*+()[]{}\\"

    fun prepare(raw: String, language: String): String {
        if (raw.isBlank()) return raw
        return when (language) {
            LocaleHelper.LANG_UR -> UrduTtsPronunciation.prepare(raw)
            else -> prepareEnglish(raw)
        }
    }

    fun prepareEnglish(raw: String): String {
        var text = raw.trim()
        text = stripEmojiAndIcons(text)
        text = stripTeacherAsideBlocks(text)
        text = fixInvertedParentheticalAcronyms(text)
        text = text.replace(Regex("\\(\\s*\\)"), " ")
        text = expandEnglishAcronymsAndSymbols(text)
        text = softenListAndHeadingMarkers(text)
        text = text.replace(Regex("\\s+"), " ").trim()
        return text
    }

    private fun stripEmojiAndIcons(text: String): String {
        return text
            .replace(Regex("[\\uD83C-\\uDBFF\\uDC00-\\uDFFF]+"), " ")
            .replace("\uFE0F", " ")
            .replace("👨‍🏫", " ")
            .replace("★", "important: ")
            .replace("GOLDEN TOPIC", "golden topic")
    }

    private fun stripTeacherAsideBlocks(text: String): String {
        return text
            .replace(Regex("Class Discussion.*?(?=\\d+\\.\\d|$)", RegexOption.IGNORE_CASE), " ")
            .replace(Regex("Reference Note.*", RegexOption.IGNORE_CASE), " ")
            .replace(Regex("TABLE OF CONTENTS.*?(?=\\d+\\.\\d|$)", RegexOption.IGNORE_CASE), " ")
    }

    /** PDF extracts often contain ")HCI(" instead of "HCI". */
    private fun fixInvertedParentheticalAcronyms(text: String): String {
        var t = text.replace(Regex("\\)\\s*([A-Z][A-Za-z0-9/-]{1,12})\\s*\\("), " $1 ")
        t = t.replace(Regex("\\(([A-Z]{2,8})\\)"), " $1 ")
        t = t.replace(Regex("(?i)\\)(hci|osi|tcp|api|ui|ux)\\("), " $1 ")
        return t
    }

    private fun expandEnglishAcronymsAndSymbols(text: String): String {
        var t = text
        t = t.replace(Regex("\\be\\.g\\.\\s*", RegexOption.IGNORE_CASE), "for example, ")
        t = t.replace(Regex("\\bi\\.e\\.\\s*", RegexOption.IGNORE_CASE), "that is, ")
        t = t.replace(Regex("\\bvs\\.\\s*", RegexOption.IGNORE_CASE), "versus ")
        t = t.replace("&", " and ")
        t = t.replace(Regex("\\bTCP/IP\\b"), "T C P I P")
        t = t.replace(Regex("\\bK-Maps?\\b", RegexOption.IGNORE_CASE), "Karnaugh maps")
        t = t.replace(Regex("\\bK Map\\b", RegexOption.IGNORE_CASE), "Karnaugh map")

        for ((token, spoken) in EN_SPOKEN_TERMS) {
            t = if (token.any { it in REGEX_META }) {
                t.replace(token, spoken, ignoreCase = true)
            } else {
                t.replace(Regex("\\b$token\\b", RegexOption.IGNORE_CASE), spoken)
            }
        }
        return t
    }

    private fun softenListAndHeadingMarkers(text: String): String {
        var t = text
        t = t.replace(Regex("(\\d+)\\.(\\d+)"), "$1 point $2. ")
        t = t.replace(Regex("(?<=\\s)(\\d+)\\.(?=\\s[A-Z])"), "$1. ")
        t = t.replace(Regex("\\bi\\)|\\bii\\)|\\biii\\)|\\biv\\)"), ". ")
        t = t.replace(Regex("Channel How Humans Use It How Computers Respond"), " ")
        t = t.replace(Regex("Interaction Type Description Examples"), " ")
        t = t.replace("\"", " ")
        t = t.replace("'", " ")
        t = t.replace(":", ", ")
        t = t.replace(";", ". ")
        t = t.replace(Regex("\\.{2,}"), ". ")
        return t
    }

    private val EN_SPOKEN_TERMS = listOf(
        "HCI" to "human computer interaction",
        "CHI" to "computer human interface",
        "MMI" to "man machine interaction",
        "OSI" to "O S I",
        "SDLC" to "software development life cycle",
        "NLP" to "natural language processing",
        "API" to "A P I",
        "IDE" to "I D E",
        "UI" to "user interface",
        "UX" to "user experience",
        "VR" to "virtual reality",
        "LMS" to "learning management system",
        "ATM" to "A T M",
        "FaceID" to "face I D",
        "Wi-Fi" to "Wi Fi",
        "WiFi" to "Wi Fi",
        "Boolean" to "boolean",
        "AND gate" to "and gate",
        "OR gate" to "or gate",
        "NOT gate" to "not gate",
    ).sortedByDescending { it.first.length }
}
