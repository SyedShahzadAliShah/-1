package com.sindh.cswhiteboard.data

import android.content.Context
import org.json.JSONArray
import org.json.JSONObject

object CurriculumRepository {

    @Volatile
    private var cached: Curriculum? = null

    fun load(context: Context): Curriculum {
        cached?.let { return it }
        synchronized(this) {
            cached?.let { return it }
            val json = context.assets.open("lectures/curriculum.json")
                .bufferedReader(Charsets.UTF_8)
                .use { it.readText() }
            val parsed = parse(JSONObject(json))
            cached = parsed
            return parsed
        }
    }

    fun classPack(context: Context, classId: String): ClassPack? =
        load(context).classes.find { it.id == classId }

    fun chapter(context: Context, classId: String, chapterId: String): Chapter? =
        classPack(context, classId)?.chapters?.find { it.id == chapterId }

    fun lecture(context: Context, lectureId: String): Pair<Chapter, Lecture>? {
        load(context).classes.forEach { pack ->
            pack.chapters.forEach { chapter ->
                chapter.lectures.find { it.id == lectureId }?.let { return chapter to it }
            }
        }
        return null
    }

    fun nextLecture(context: Context, lectureId: String): Lecture? {
        val all = load(context).classes.flatMap { it.chapters }.flatMap { it.lectures }
        val idx = all.indexOfFirst { it.id == lectureId }
        return if (idx >= 0 && idx + 1 < all.size) all[idx + 1] else null
    }

    private fun parse(root: JSONObject): Curriculum {
        val classes = root.getJSONArray("classes").mapObjects { pack ->
            ClassPack(
                id = pack.getString("id"),
                titleEn = pack.getString("titleEn"),
                titleUr = pack.optString("titleUr"),
                subtitleEn = pack.optString("subtitleEn"),
                subtitleUr = pack.optString("subtitleUr"),
                chapters = pack.getJSONArray("chapters").mapObjects { ch ->
                    Chapter(
                        id = ch.getString("id"),
                        number = ch.optInt("number"),
                        titleEn = ch.getString("titleEn"),
                        titleUr = ch.optString("titleUr"),
                        lectures = ch.getJSONArray("lectures").mapObjects { lec ->
                            Lecture(
                                id = lec.getString("id"),
                                code = lec.optString("code"),
                                titleEn = lec.getString("titleEn"),
                                titleUr = lec.optString("titleUr"),
                                golden = lec.optBoolean("golden"),
                                durationHintSec = lec.optInt("durationHintSec", 60),
                                segments = lec.getJSONArray("segments").mapObjects { seg ->
                                    Segment(
                                        speakEn = seg.optString("speakEn"),
                                        speakUr = seg.optString("speakUr"),
                                        clear = seg.optBoolean("clear"),
                                        actions = seg.optJSONArray("actions")?.mapObjects { act ->
                                            BoardAction(
                                                type = act.optString("type"),
                                                text = act.optString("text"),
                                                kind = act.optString("kind"),
                                                name = act.optString("name"),
                                                lines = act.optJSONArray("lines")?.stringList() ?: emptyList(),
                                                headers = act.optJSONArray("headers")?.stringList() ?: emptyList(),
                                                rows = act.optJSONArray("rows")?.mapArrays { it.stringList() } ?: emptyList()
                                            )
                                        } ?: emptyList()
                                    )
                                }
                            )
                        }
                    )
                }
            )
        }
        return Curriculum(root.optString("version", "1.0.0"), classes)
    }

    private inline fun <T> JSONArray.mapObjects(block: (JSONObject) -> T): List<T> =
        (0 until length()).map { block(getJSONObject(it)) }

    private fun JSONArray.stringList(): List<String> =
        (0 until length()).map { optString(it) }

    private fun JSONArray.mapArrays(block: (JSONArray) -> List<String>): List<List<String>> =
        (0 until length()).map { block(getJSONArray(it)) }
}
