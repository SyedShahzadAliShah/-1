package com.couplesguide.postures.data

import android.content.Context
import org.json.JSONObject

object TeacherGuideRepository {

    private var cached: TeacherGuide? = null

    fun load(context: Context): TeacherGuide {
        cached?.let { return it }
        val json = context.assets.open("cs_xi_teacher/guide.json")
            .bufferedReader()
            .use { it.readText() }
        val root = JSONObject(json)
        val chapters = mutableListOf<TeacherChapter>()
        val chaptersArray = root.getJSONArray("chapters")
        for (i in 0 until chaptersArray.length()) {
            val ch = chaptersArray.getJSONObject(i)
            val topics = mutableListOf<TeacherTopic>()
            val topicsArray = ch.getJSONArray("topics")
            for (j in 0 until topicsArray.length()) {
                val t = topicsArray.getJSONObject(j)
                topics.add(
                    TeacherTopic(
                        id = t.getString("id"),
                        title = t.getString("title"),
                        critical = t.optBoolean("critical", false),
                        englishText = t.getString("englishText"),
                        urduNarration = t.getString("urduNarration"),
                        startPage = t.optInt("startPage", 0),
                        endPage = t.optInt("endPage", 0)
                    )
                )
            }
            chapters.add(
                TeacherChapter(
                    id = ch.getString("id"),
                    title = ch.getString("title"),
                    topics = topics
                )
            )
        }
        val guide = TeacherGuide(
            title = root.getString("title"),
            subtitle = root.getString("subtitle"),
            curriculum = root.getString("curriculum"),
            referenceNote = root.getString("referenceNote"),
            chapters = chapters
        )
        cached = guide
        return guide
    }

    fun getChapterById(context: Context, id: String): TeacherChapter? =
        load(context).chapters.find { it.id == id }

    fun getTopicById(context: Context, id: String): TeacherTopic? {
        for (chapter in load(context).chapters) {
            chapter.topics.find { it.id == id }?.let { return it }
        }
        return null
    }

    fun getChapterForTopic(context: Context, topicId: String): TeacherChapter? {
        for (chapter in load(context).chapters) {
            if (chapter.topics.any { it.id == topicId }) return chapter
        }
        return null
    }
}
