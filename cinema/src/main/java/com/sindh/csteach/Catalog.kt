package com.sindh.csteach

import android.content.Context
import org.json.JSONObject

data class Scene(
    val title: String,
    val body: String,
    val urdu: String,
    val speak: String,
)

data class Chapter(
    val num: String,
    val title: String,
    val scenes: List<Scene>,
)

data class Grade(
    val id: String,
    val title: String,
    val label: String,
    val chapters: List<Chapter>,
) {
    val beats: List<Beat> by lazy {
        chapters.flatMap { chapter ->
            val labelText = "Chapter ${chapter.num} · ${chapter.title}"
            chapter.scenes.map { scene ->
                Beat(
                    chapterLabel = labelText,
                    chapterTitle = chapter.title,
                    title = scene.title,
                    body = scene.body,
                    urdu = scene.urdu,
                    speak = scene.speak.ifBlank { scene.title },
                )
            }
        }
    }

    fun chapterStart(index: Int): Int {
        var cursor = 0
        chapters.forEachIndexed { i, chapter ->
            if (i == index) return cursor
            cursor += chapter.scenes.size
        }
        return 0
    }
}

data class Beat(
    val chapterLabel: String,
    val chapterTitle: String,
    val title: String,
    val body: String,
    val urdu: String,
    val speak: String,
)

object Catalog {
    private var grades: List<Grade>? = null

    fun load(context: Context): List<Grade> {
        grades?.let { return it }
        val text = context.assets.open("scenes.json").bufferedReader().use { it.readText() }
        val root = JSONObject(text)
        val array = root.getJSONArray("grades")
        val parsed = buildList {
            for (i in 0 until array.length()) {
                val grade = array.getJSONObject(i)
                val chaptersJson = grade.getJSONArray("chapters")
                val chapters = buildList {
                    for (c in 0 until chaptersJson.length()) {
                        val chapter = chaptersJson.getJSONObject(c)
                        val scenesJson = chapter.getJSONArray("scenes")
                        val scenes = buildList {
                            for (s in 0 until scenesJson.length()) {
                                val scene = scenesJson.getJSONObject(s)
                                add(
                                    Scene(
                                        title = scene.optString("title"),
                                        body = scene.optString("body"),
                                        urdu = scene.optString("urdu"),
                                        speak = scene.optString("speak"),
                                    )
                                )
                            }
                        }
                        add(
                            Chapter(
                                num = chapter.optString("num"),
                                title = chapter.optString("title"),
                                scenes = scenes,
                            )
                        )
                    }
                }
                add(
                    Grade(
                        id = grade.getString("id"),
                        title = grade.getString("title"),
                        label = grade.getString("label"),
                        chapters = chapters,
                    )
                )
            }
        }
        grades = parsed
        return parsed
    }

    fun grade(context: Context, id: String): Grade? = load(context).find { it.id == id }
}
