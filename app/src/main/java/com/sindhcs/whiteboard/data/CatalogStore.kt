package com.sindhcs.whiteboard.data

import android.content.Context
import org.json.JSONArray
import org.json.JSONObject

object CatalogStore {
    @Volatile
    private var cached: Catalog? = null

    fun get(context: Context): Catalog {
        cached?.let { return it }
        synchronized(this) {
            cached?.let { return it }
            val text = context.applicationContext.assets
                .open("lectures/catalog.json")
                .bufferedReader()
                .use { it.readText() }
            val catalog = parse(JSONObject(text))
            cached = catalog
            return catalog
        }
    }

    private fun parse(root: JSONObject): Catalog {
        val grades = root.getJSONArray("grades")
        return Catalog((0 until grades.length()).map { index ->
            parseGrade(grades.getJSONObject(index))
        })
    }

    private fun parseGrade(obj: JSONObject): Grade {
        val chapters = obj.getJSONArray("chapters")
        return Grade(
            id = obj.getString("id"),
            label = obj.getString("label"),
            title = obj.getString("title"),
            subtitle = obj.getString("subtitle"),
            chapters = (0 until chapters.length()).map { parseChapter(chapters.getJSONObject(it)) }
        )
    }

    private fun parseChapter(obj: JSONObject): Chapter {
        val lectures = obj.getJSONArray("lectures")
        return Chapter(
            id = obj.getString("id"),
            number = obj.getInt("number"),
            title = obj.getString("title"),
            lectures = (0 until lectures.length()).map { parseLecture(lectures.getJSONObject(it)) }
        )
    }

    private fun parseLecture(obj: JSONObject): Lecture {
        val boards = obj.getJSONArray("boards")
        return Lecture(
            id = obj.getString("id"),
            title = obj.getString("title"),
            golden = obj.optBoolean("golden", false),
            boards = (0 until boards.length()).map { parseBoard(boards.getJSONObject(it)) }
        )
    }

    private fun parseBoard(obj: JSONObject): Board {
        val marks = obj.getJSONArray("marks")
        return Board(
            narration = obj.getString("narration"),
            marks = (0 until marks.length()).map { parseMark(marks.getJSONObject(it)) }
        )
    }

    private fun parseMark(obj: JSONObject): Mark {
        return Mark(
            k = obj.getString("k"),
            t = obj.optString("t", ""),
            tone = obj.optString("tone", ""),
            items = obj.optJSONArray("items").toStringList(),
            headers = obj.optJSONArray("headers").toStringList(),
            rows = obj.optJSONArray("rows").toRows(),
            t2 = obj.optString("t2", ""),
            items2 = obj.optJSONArray("items2").toStringList(),
            hi = obj.optJSONArray("hi").toIntList()
        )
    }

    private fun JSONArray?.toStringList(): List<String> {
        if (this == null) return emptyList()
        return (0 until length()).map { getString(it) }
    }

    private fun JSONArray?.toIntList(): List<Int> {
        if (this == null) return emptyList()
        return (0 until length()).map { getInt(it) }
    }

    private fun JSONArray?.toRows(): List<List<String>> {
        if (this == null) return emptyList()
        return (0 until length()).map { index ->
            val row = getJSONArray(index)
            (0 until row.length()).map { row.getString(it) }
        }
    }
}
