package com.couplesguide.postures.data

import android.content.Context
import org.json.JSONArray
import com.couplesguide.postures.R
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.NarrativeLanguageHelper

data class LecturePageText(
    val page: Int,
    val english: String,
    val urdu: String
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
                add(
                    LecturePageText(
                        page = obj.getInt("page"),
                        english = obj.optString("en", ""),
                        urdu = obj.optString("ur", "")
                    )
                )
            }
        }
        cache[indexAsset] = list
        return list
    }

    fun narrationForPage(context: Context, indexAsset: String, pageNumber: Int, language: String): String {
        val page = getPage(context, indexAsset, pageNumber) ?: return ""
        return textForMode(
            context = context,
            english = page.english,
            urdu = page.urdu,
            mode = language
        )
    }

    fun narrationForPageWithMode(
        context: Context,
        indexAsset: String,
        pageNumber: Int,
        mode: String
    ): String {
        val page = getPage(context, indexAsset, pageNumber) ?: return ""
        return textForMode(context, page.english, page.urdu, mode)
    }

    fun ttsSegmentsForPage(
        context: Context,
        indexAsset: String,
        pageNumber: Int,
        mode: String
    ): List<Pair<String, String>> {
        val page = getPage(context, indexAsset, pageNumber) ?: return emptyList()
        val en = page.english.trim()
        val ur = page.urdu.trim().ifBlank { en }
        return when (mode) {
            NarrativeLanguageHelper.MODE_UR -> listOf(ur to LocaleHelper.LANG_UR)
            NarrativeLanguageHelper.MODE_EMBED -> buildList {
                if (en.isNotBlank()) add(en to LocaleHelper.LANG_EN)
                if (ur.isNotBlank() && ur != en) add(ur to LocaleHelper.LANG_UR)
            }
            else -> listOf(en to LocaleHelper.LANG_EN)
        }.filter { it.first.isNotBlank() }
    }

    private fun textForMode(
        context: Context,
        english: String,
        urdu: String,
        mode: String
    ): String {
        val en = english.trim()
        val ur = urdu.trim()
        return when (mode) {
            NarrativeLanguageHelper.MODE_UR -> ur.ifBlank { en }
            NarrativeLanguageHelper.MODE_EMBED -> {
                val enLabel = context.getString(R.string.narrative_embed_en_label)
                val urLabel = context.getString(R.string.narrative_embed_ur_label)
                buildString {
                    if (en.isNotBlank()) {
                        append(enLabel)
                        append("\n")
                        append(en)
                    }
                    if (ur.isNotBlank()) {
                        if (isNotEmpty()) append("\n\n")
                        append(urLabel)
                        append("\n")
                        append(ur)
                    }
                }.ifBlank { en }
            }
            else -> en
        }
    }
}
