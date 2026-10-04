package com.couplesguide.postures.data

import android.content.Context
import org.json.JSONArray
import org.json.JSONObject

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
        return if (language == "ur") {
            page.urdu.ifBlank { page.english }
        } else {
            page.english
        }
    }
}
