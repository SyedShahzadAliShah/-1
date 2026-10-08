package com.couplesguide.postures.data

import android.content.Context
import org.json.JSONArray
import org.json.JSONObject

data class CsBook(
    val id: String,
    val title: String,
    val subtitle: String,
    val studyGuideLabel: String,
    val teacherGuidelines: TeacherGuidelines,
    val lectures: List<CsLecture>,
    val topics: List<CsTopic>
)

data class SketchnoteFrame(
    val index: Int,
    val english: String,
    val urdu: String,
    val visual: String
)

data class CsTopic(
    val id: String,
    val title: String,
    val english: String,
    val urduNarration: String,
    val golden: Boolean,
    val sourcePage: Int,
    val pageImage: String?,
    val sketchnoteFrames: List<SketchnoteFrame>
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
                val topics = parseTopics(payload)
                add(
                    CsBook(
                        id = payload.getString("id"),
                        title = payload.getString("title"),
                        subtitle = payload.getString("subtitle"),
                        studyGuideLabel = payload.optString(
                            "study_guide_label",
                            "Lecture-wise Bilingual Teacher's Edition Study Guide"
                        ),
                        teacherGuidelines = parseGuidelines(payload.getJSONObject("teacher_guidelines")),
                        lectures = parseLectures(payload.optJSONArray("lectures")),
                        topics = topics
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

    fun getLecture(context: Context, lectureId: String): Pair<CsBook, CsLecture>? {
        load(context)
        for (book in books) {
            val lecture = book.lectures.find { it.id == lectureId }
            if (lecture != null) return book to lecture
        }
        return null
    }

    fun getTopic(context: Context, topicId: String): Pair<CsBook, CsTopic>? {
        load(context)
        for (book in books) {
            val topic = book.topics.find { it.id == topicId }
            if (topic != null) return book to topic
        }
        return null
    }

    private fun parseLectures(array: JSONArray?): List<CsLecture> {
        if (array == null || array.length() == 0) return emptyList()
        return buildList {
            for (i in 0 until array.length()) {
                val item = array.getJSONObject(i)
                val idsArray = item.getJSONArray("topic_ids")
                val ids = buildList {
                    for (j in 0 until idsArray.length()) {
                        add(idsArray.getString(j))
                    }
                }
                add(
                    CsLecture(
                        id = item.getString("id"),
                        chapter = item.getInt("chapter"),
                        title = item.getString("title"),
                        englishSummary = item.getString("english_summary"),
                        urduNarration = item.optString("urdu_narration", ""),
                        topicIds = ids,
                        topicCount = item.optInt("topic_count", ids.size),
                        goldenCount = item.optInt("golden_count", 0)
                    )
                )
            }
        }
    }

    private fun parseGuidelines(obj: JSONObject): TeacherGuidelines {
        return TeacherGuidelines(
            editionTitle = obj.getString("edition_title"),
            tagline = obj.getString("tagline"),
            curriculum = obj.getString("curriculum"),
            textbookReference = obj.getString("textbook_reference"),
            english = obj.getString("english"),
            urduNarration = obj.getString("urdu_narration"),
            goldenTopicNote = obj.getString("golden_topic_note")
        )
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
                        sourcePage = item.optInt("source_page", 0),
                        pageImage = item.optString("page_image").takeIf { it.isNotBlank() },
                        sketchnoteFrames = parseFrames(item.optJSONArray("sketchnote_frames"))
                    )
                )
            }
        }
    }

    private fun parseFrames(array: JSONArray?): List<SketchnoteFrame> {
        if (array == null || array.length() == 0) return emptyList()
        return buildList {
            for (i in 0 until array.length()) {
                val item = array.getJSONObject(i)
                add(
                    SketchnoteFrame(
                        index = item.optInt("index", i),
                        english = item.getString("english"),
                        urdu = item.optString("urdu", ""),
                        visual = item.optString("visual", "concept")
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
