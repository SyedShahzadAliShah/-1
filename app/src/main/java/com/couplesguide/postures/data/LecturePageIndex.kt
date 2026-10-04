package com.couplesguide.postures.data

import android.content.Context
import org.json.JSONArray
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.NarrativeLanguageHelper

data class LecturePageText(
    val page: Int,
    val english: String,
    val urdu: String,
    val englishTts: String,
    val urduTts: String
)

object LecturePageIndex {

    private val cache = mutableMapOf<String, List<LecturePageText>>()

    fun getPage(context: Context, indexAsset: String, pageNumber: Int): LecturePageText? {
        val pages = load(context, indexAsset)
        return pages.find { it.page == pageNumber }
    }

    fun load(context: Context, indexAsset: String): List<LecturePageText> {
        cache[indexAsset]?.let { return it }
        val json = context.assets.open(indexAsset).bufferedReader().use { it.readText() }
        val array = JSONArray(json)
        val list = buildList {
            for (i in 0 until array.length()) {
                val obj = array.getJSONObject(i)
                val en = obj.optString("en", "")
                val ur = obj.optString("ur", "")
                add(
                    LecturePageText(
                        page = obj.getInt("page"),
                        english = en,
                        urdu = ur,
                        englishTts = obj.optString("en_tts", en),
                        urduTts = obj.optString("ur_tts", ur)
                    )
                )
            }
        }
        cache[indexAsset] = list
        return list
    }

    fun narrationForPageWithMode(
        context: Context,
        indexAsset: String,
        pageNumber: Int,
        mode: String
    ): String {
        val page = getPage(context, indexAsset, pageNumber) ?: return ""
        return textForMode(
            english = page.englishTts.ifBlank { page.english },
            urdu = page.urduTts.ifBlank { page.urdu },
            mode = mode
        )
    }

    fun ttsSegmentsForPage(
        context: Context,
        indexAsset: String,
        pageNumber: Int,
        mode: String
    ): List<Pair<String, String>> {
        val page = getPage(context, indexAsset, pageNumber) ?: return emptyList()
        val en = page.englishTts.ifBlank { page.english }.trim()
        val ur = page.urduTts.ifBlank { page.urdu }.trim().ifBlank { en }
        return when (mode) {
            NarrativeLanguageHelper.MODE_UR -> listOf(ur to LocaleHelper.LANG_UR)
            NarrativeLanguageHelper.MODE_BOTH -> buildList {
                if (en.isNotBlank()) add(en to LocaleHelper.LANG_EN)
                if (ur.isNotBlank() && ur != en) add(ur to LocaleHelper.LANG_UR)
            }
            else -> listOf(en to LocaleHelper.LANG_EN)
        }.filter { it.first.isNotBlank() }
    }

    fun totalPages(context: Context, indexAsset: String): Int = load(context, indexAsset).size

    private fun textForMode(
        english: String,
        urdu: String,
        mode: String
    ): String {
        val en = english.trim()
        val ur = urdu.trim()
        return when (mode) {
            NarrativeLanguageHelper.MODE_UR -> ur.ifBlank { en }
            NarrativeLanguageHelper.MODE_BOTH -> listOf(en, ur).filter { it.isNotBlank() }.distinct().joinToString("\n\n")
            else -> en
        }
    }
}
