package com.couplesguide.postures.data

import android.content.Context
import org.json.JSONObject

data class CsBook(
    val id: String,
    val title: String,
    val subtitle: String,
    val topics: List<CsTopic>
)

data class CsTopic(
    val id: String,
    val title: String,
    val english: String,
    val urduNarration: String,
    val golden: Boolean,
    val sourcePage: Int
)

object CsTeacherRepository {

    private var books: List<CsBook> = emptyList()

    fun load(context: Context) {
        if (books.isNotEmpty()) return
        val catalog = readAssetJson(context, "cs_teacher/catalog.json")
        val bookArray = catalog.getJSONArray("books")
        books = buildList {
            for (i in 0 until bookArray.length()) {
                val meta = bookArray.getJSONObject(i)
                val asset = meta.getString("asset")
                val payload = readAssetJson(context, asset)
                add(
                    CsBook(
                        id = payload.getString("id"),
                        title = payload.getString("title"),
                        subtitle = payload.getString("subtitle"),
                        topics = parseTopics(payload)
                    )
                )
            }
        }
    }

    fun getBooks(context: Context): List<CsBook> {
        load(context)
        return books
    }

    fun getBook(context: Context, bookId: String): CsBook? {
        load(context)
        return books.find { it.id == bookId }
    }

    fun getTopic(context: Context, topicId: String): Pair<CsBook, CsTopic>? {
        load(context)
        for (book in books) {
            val topic = book.topics.find { it.id == topicId }
            if (topic != null) return book to topic
        }
        return null
    }

    private fun parseTopics(payload: JSONObject): List<CsTopic> {
        val array = payload.getJSONArray("topics")
        return buildList {
            for (i in 0 until array.length()) {
                val item = array.getJSONObject(i)
                add(
                    CsTopic(
                        id = item.getString("id"),
                        title = item.getString("title"),
                        english = item.getString("english"),
                        urduNarration = item.getString("urdu_narration"),
                        golden = item.optBoolean("golden", false),
                        sourcePage = item.optInt("source_page", 0)
                    )
                )
            }
        }
    }

    private fun readAssetJson(context: Context, path: String): JSONObject {
        val text = context.assets.open(path).bufferedReader().use { it.readText() }
        return JSONObject(text)
    }
}
