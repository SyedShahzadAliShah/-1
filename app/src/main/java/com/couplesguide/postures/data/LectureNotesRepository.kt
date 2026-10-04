package com.couplesguide.postures.data

import android.content.Context
import com.couplesguide.postures.R
import org.json.JSONArray
import org.json.JSONObject

object LectureNotesRepository {

    private var studyClasses: List<StudyClass>? = null

    fun ensureLoaded(context: Context) {
        if (studyClasses != null) return
        studyClasses = loadFromAssets(context)
    }

    fun getClasses(context: Context): List<StudyClass> {
        ensureLoaded(context)
        return studyClasses.orEmpty()
    }

    fun getClassById(context: Context, classId: String): StudyClass? =
        getClasses(context).find { it.id == classId }

    fun getChapterById(context: Context, chapterId: String): StudyChapter? =
        getClasses(context).flatMap { it.chapters }.find { it.id == chapterId }

    fun getChaptersForClass(context: Context, classId: String): List<StudyChapter> =
        getClassById(context, classId)?.chapters.orEmpty()

    private fun loadFromAssets(context: Context): List<StudyClass> {
        val metaJson = context.assets.open("lecture_notes/study_guide_meta.json")
            .bufferedReader().use { it.readText() }
        val meta = JSONObject(metaJson)
        val contentJson = context.assets.open("lecture_notes/chapter_content.json")
            .bufferedReader().use { it.readText() }
        val contentById = parseChapterContent(contentJson)

        val classesArray = meta.getJSONArray("classes")
        return buildList {
            for (i in 0 until classesArray.length()) {
                val cls = classesArray.getJSONObject(i)
                val classId = cls.getString("id")
                val pdfAsset = cls.getString("pdfAsset")
                val pageIndexAsset = cls.getString("pageIndexAsset")
                val chaptersJson = cls.getJSONArray("chapters")
                val chapters = buildList {
                    for (c in 0 until chaptersJson.length()) {
                        val ch = chaptersJson.getJSONObject(c)
                        val number = ch.getInt("number")
                        val id = "${classId}_ch$number"
                        val content = contentById[id] ?: defaultContent(ch)
                        add(
                            StudyChapter(
                                id = id,
                                grade = cls.getString("gradeLabel"),
                                chapterNumber = number,
                                illustrationRes = illustrationFor(classId, number),
                                pdfAsset = pdfAsset,
                                pdfPageStart = ch.getInt("pdfPageStart"),
                                pdfPageEnd = ch.getInt("pdfPageEnd"),
                                english = ChapterContent(
                                    title = content.titleEn,
                                    summary = content.summaryEn,
                                    body = content.bodyEn,
                                    keyPoints = content.keyPointsEn
                                ),
                                urdu = ChapterContent(
                                    title = content.titleUr,
                                    summary = content.summaryUr,
                                    body = content.bodyUr,
                                    keyPoints = content.keyPointsUr
                                )
                            )
                        )
                    }
                }
                add(
                    StudyClass(
                        id = classId,
                        gradeLabel = cls.getString("gradeLabel"),
                        pdfAsset = pdfAsset,
                        pageIndexAsset = pageIndexAsset,
                        totalPages = cls.getInt("totalPages"),
                        chapters = chapters
                    )
                )
            }
        }
    }

    private data class RawChapterContent(
        val titleEn: String,
        val titleUr: String,
        val summaryEn: String,
        val summaryUr: String,
        val bodyEn: String,
        val bodyUr: String,
        val keyPointsEn: List<String>,
        val keyPointsUr: List<String>
    )

    private fun parseChapterContent(json: String): Map<String, RawChapterContent> {
        val array = JSONArray(json)
        return buildMap {
            for (i in 0 until array.length()) {
                val obj = array.getJSONObject(i)
                val id = obj.getString("id")
                put(
                    id,
                    RawChapterContent(
                        titleEn = obj.getString("titleEn"),
                        titleUr = obj.getString("titleUr"),
                        summaryEn = obj.getString("summaryEn"),
                        summaryUr = obj.getString("summaryUr"),
                        bodyEn = obj.getString("bodyEn"),
                        bodyUr = obj.getString("bodyUr"),
                        keyPointsEn = obj.getStringList("keyPointsEn"),
                        keyPointsUr = obj.getStringList("keyPointsUr")
                    )
                )
            }
        }
    }

    private fun defaultContent(ch: JSONObject): RawChapterContent {
        val titleEn = ch.getString("titleEn")
        val titleUr = ch.getString("titleUr")
        return RawChapterContent(
            titleEn = titleEn,
            titleUr = titleUr,
            summaryEn = "High-yield lecture notes — $titleEn",
            summaryUr = "اہم لیکچر نوٹس — $titleUr",
            bodyEn = "Use cinematic lecture mode to study the bilingual teacher PDF pages.",
            bodyUr = "دو لسانی اساتذہ PDF کے لیے سینمائی لیکچر موڈ استعمال کریں۔",
            keyPointsEn = listOf("★ topics are examination priority"),
            keyPointsUr = listOf("★ موضوعات امتحانی ترجیح ہیں")
        )
    }

    private fun JSONObject.getStringList(key: String): List<String> {
        val array = getJSONArray(key)
        return buildList {
            for (i in 0 until array.length()) {
                add(array.getString(i))
            }
        }
    }

    private fun illustrationFor(classId: String, chapterNumber: Int): Int = when (classId) {
        "xi" -> when (chapterNumber) {
            1 -> R.drawable.pic_cs_xi_ch1
            2 -> R.drawable.pic_cs_xi_ch2
            3 -> R.drawable.pic_cs_xi_ch3
            4 -> R.drawable.pic_cs_xi_ch4
            5 -> R.drawable.pic_cs_xi_ch5
            else -> R.drawable.pic_cs_xi_ch6
        }
        else -> when (chapterNumber) {
            1 -> R.drawable.pic_cs_xii_ch1
            2 -> R.drawable.pic_cs_xii_ch2
            3 -> R.drawable.pic_cs_xii_ch3
            4 -> R.drawable.pic_cs_xii_ch4
            5 -> R.drawable.pic_cs_xii_ch5
            else -> R.drawable.pic_cs_xii_ch6
        }
    }
}
