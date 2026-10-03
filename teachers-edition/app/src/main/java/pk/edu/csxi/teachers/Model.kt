package pk.edu.csxi.teachers

data class Chapter(val n: Int, val title: String, val first: Int, val last: Int)

data class PageInfo(
    val page: Int,
    val label: Int?,
    val chapter: Int,
    val heads: List<String>,
    val subs: List<String>,
    val golden: Boolean,
)

data class Index(
    val title: String,
    val subtitle: String,
    val chapters: List<Chapter>,
    val pages: List<PageInfo>,
)

enum class Kind { TITLE, H1, H2, H3, BADGE, P, LI, NOTE, TABLE_HEAD, TABLE_ROW, CODE, FIGURE }

/** One renderable (and, when [audio] is set, playable) unit on a page. */
data class Item(
    val kind: Kind,
    val text: String,
    val label: String? = null,
    val lead: String? = null,
    val cols: List<String> = emptyList(),
    val cells: List<String> = emptyList(),
    val audio: String? = null,
)
