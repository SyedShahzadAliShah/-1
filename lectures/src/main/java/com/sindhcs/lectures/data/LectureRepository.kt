package com.sindhcs.lectures.data

import android.content.Context
import org.json.JSONObject

object LectureRepository {
    private var catalog: Catalog? = null

    fun load(context: Context): Catalog {
        catalog?.let { return it }
        val json = context.assets.open("lectures.json").bufferedReader().use { it.readText() }
        val root = JSONObject(json)
        val grades = root.getJSONArray("grades")
        val out = mutableListOf<Grade>()
        for (g in 0 until grades.length()) {
            val go = grades.getJSONObject(g)
            val chapters = go.getJSONArray("chapters")
            val chOut = mutableListOf<Chapter>()
            for (c in 0 until chapters.length()) {
                val co = chapters.getJSONObject(c)
                val topics = co.getJSONArray("topics")
                val tOut = mutableListOf<Topic>()
                for (t in 0 until topics.length()) {
                    val to = topics.getJSONObject(t)
                    val termsArr = to.optJSONArray("terms")
                    val terms = mutableListOf<String>()
                    if (termsArr != null) {
                        for (i in 0 until termsArr.length()) {
                            terms.add(termsArr.getString(i))
                        }
                    }
                    val beatArr = to.optJSONArray("beats")
                    val beats = mutableListOf<String>()
                    if (beatArr != null) {
                        for (i in 0 until beatArr.length()) {
                            beats.add(beatArr.getString(i))
                        }
                    }
                    tOut.add(
                        Topic(
                            id = to.getString("id"),
                            title = to.getString("title"),
                            golden = to.optBoolean("golden"),
                            learn = to.optString("learn"),
                            urdu = to.optString("urdu"),
                            spokenUrdu = to.optString("spokenUrdu"),
                            beats = beats,
                            readSeconds = to.optInt("readSeconds"),
                            terms = terms,
                            board = to.optString("board")
                        )
                    )
                }
                chOut.add(
                    Chapter(
                        num = co.getInt("num"),
                        title = co.getString("title"),
                        topics = tOut
                    )
                )
            }
            out.add(
                Grade(
                    id = go.getString("id"),
                    title = go.getString("title"),
                    urdu = go.optString("urdu"),
                    curriculum = go.optString("curriculum"),
                    chapters = chOut
                )
            )
        }
        return Catalog(out).also { catalog = it }
    }

    fun grade(context: Context, id: String): Grade? =
        load(context).grades.find { it.id == id }

    fun chapter(context: Context, gradeId: String, num: Int): Chapter? =
        grade(context, gradeId)?.chapters?.find { it.num == num }

    fun topic(context: Context, gradeId: String, chapterNum: Int, topicId: String): Topic? =
        chapter(context, gradeId, chapterNum)?.topics?.find { it.id == topicId }
}
