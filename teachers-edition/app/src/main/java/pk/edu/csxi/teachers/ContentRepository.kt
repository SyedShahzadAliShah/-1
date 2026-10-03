package pk.edu.csxi.teachers

import android.content.Context
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import org.json.JSONArray
import org.json.JSONObject

class ContentRepository(context: Context) {
    private val assets = context.applicationContext.assets
    private val cache = HashMap<Int, List<Item>>()

    val index: Index by lazy { parseIndex(readText("index.json")) }

    val pageCount: Int get() = index.pages.size

    fun info(page: Int): PageInfo = index.pages[page - 1]

    fun chapterOf(page: Int): Chapter = index.chapters.first { it.n == info(page).chapter }

    @Synchronized
    fun items(page: Int): List<Item> = cache.getOrPut(page) {
        parseItems(JSONObject(readText("content/p%03d.json".format(page))).getJSONArray("blocks"))
    }

    fun pageBitmap(page: Int): Bitmap? =
        assets.open("pages/p%03d.webp".format(page)).use { BitmapFactory.decodeStream(it) }

    private fun readText(path: String) = assets.open(path).bufferedReader(Charsets.UTF_8).use { it.readText() }

    private fun parseIndex(json: String): Index {
        val o = JSONObject(json)
        val chapters = o.getJSONArray("chapters").map {
            Chapter(it.getInt("n"), it.getString("title"), it.getInt("first"), it.getInt("last"))
        }
        val pages = o.getJSONArray("pages").map {
            PageInfo(
                page = it.getInt("page"),
                label = if (it.isNull("label")) null else it.getInt("label"),
                chapter = it.getInt("chapter"),
                heads = it.getJSONArray("heads").strings(),
                subs = it.getJSONArray("subs").strings(),
                golden = it.getBoolean("golden"),
            )
        }
        return Index(o.getString("title"), o.getString("subtitle"), chapters, pages)
    }

    private fun parseItems(blocks: JSONArray): List<Item> {
        val out = ArrayList<Item>()
        for (b in blocks.map { it }) {
            val audio = b.optString("a").ifEmpty { null }
            when (val t = b.getString("t")) {
                "table" -> {
                    val cols = b.getJSONArray("cols").strings()
                    out += Item(Kind.TABLE_HEAD, cols.joinToString("  |  "), cols = cols)
                    for (r in b.getJSONArray("rows").map { it }) {
                        out += Item(
                            Kind.TABLE_ROW, "", cols = cols,
                            cells = r.getJSONArray("cells").strings(),
                            audio = r.optString("a").ifEmpty { null },
                        )
                    }
                }
                else -> out += Item(
                    kind = Kind.valueOf(t.uppercase()),
                    text = b.optString("en"),
                    label = b.optString("label").ifEmpty { null },
                    lead = b.optString("lead").ifEmpty { null },
                    audio = audio,
                )
            }
        }
        return out
    }

    private fun <T> JSONArray.map(f: (JSONObject) -> T): List<T> =
        (0 until length()).map { f(getJSONObject(it)) }

    private fun JSONArray.strings(): List<String> = (0 until length()).map { getString(it) }
}
