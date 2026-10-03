package pk.edu.csxi.teachers

import android.content.Intent
import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import pk.edu.csxi.teachers.databinding.ActivityMainBinding
import pk.edu.csxi.teachers.databinding.ItemChapterBinding
import pk.edu.csxi.teachers.databinding.ItemPageRowBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private lateinit var repo: ContentRepository
    private lateinit var prefs: Prefs
    private val adapter = HomeAdapter { page -> openReader(page) }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        repo = ContentRepository(this)
        prefs = Prefs(this)

        binding.title.text = repo.index.title
        binding.subtitle.text = repo.index.subtitle
        binding.list.layoutManager = LinearLayoutManager(this)
        binding.list.adapter = adapter
        adapter.submit(repo, "")

        binding.search.addTextChangedListener(object : TextWatcher {
            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) = Unit
            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) = Unit
            override fun afterTextChanged(s: Editable?) = adapter.submit(repo, s?.toString().orEmpty())
        })
        binding.startButton.setOnClickListener { openReader(prefs.lastPage.takeIf { it > 0 } ?: 1) }
    }

    override fun onResume() {
        super.onResume()
        val last = prefs.lastPage
        binding.startButton.text =
            if (last > 0) getString(R.string.continue_reading, last) else getString(R.string.start_reading)
    }

    private fun openReader(page: Int) {
        startActivity(Intent(this, ReaderActivity::class.java).putExtra(ReaderActivity.EXTRA_PAGE, page))
    }
}

private class HomeAdapter(private val onPage: (Int) -> Unit) : RecyclerView.Adapter<RecyclerView.ViewHolder>() {

    private sealed class Row {
        data class Header(val chapter: Chapter, val count: Int) : Row()
        data class Page(val info: PageInfo) : Row()
    }

    private var rows: List<Row> = emptyList()

    fun submit(repo: ContentRepository, query: String) {
        val q = query.trim().lowercase()
        val out = ArrayList<Row>()
        for (c in repo.index.chapters) {
            val pages = repo.index.pages.filter { p ->
                p.chapter == c.n && (q.isEmpty() ||
                    p.heads.any { it.lowercase().contains(q) } ||
                    p.subs.any { it.lowercase().contains(q) } ||
                    q == p.page.toString())
            }
            if (pages.isEmpty()) continue
            out += Row.Header(c, pages.size)
            pages.forEach { out += Row.Page(it) }
        }
        rows = out
        notifyDataSetChanged()
    }

    override fun getItemViewType(position: Int) = if (rows[position] is Row.Header) 0 else 1
    override fun getItemCount() = rows.size

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecyclerView.ViewHolder {
        val inf = LayoutInflater.from(parent.context)
        return if (viewType == 0) HeaderHolder(ItemChapterBinding.inflate(inf, parent, false))
        else PageHolder(ItemPageRowBinding.inflate(inf, parent, false))
    }

    override fun onBindViewHolder(holder: RecyclerView.ViewHolder, position: Int) {
        when (val row = rows[position]) {
            is Row.Header -> (holder as HeaderHolder).b.apply {
                chapterNumber.text = root.context.getString(R.string.chapter_n, row.chapter.n)
                chapterTitle.text = row.chapter.title
                chapterPages.text = root.context.getString(R.string.pages_range, row.chapter.first, row.chapter.last)
            }
            is Row.Page -> (holder as PageHolder).b.apply {
                val p = row.info
                pageNumber.text = p.page.toString()
                headline.text = p.heads.firstOrNull() ?: root.context.getString(R.string.page_n, p.page)
                val sub = p.subs.take(2).joinToString(" · ")
                subline.text = sub
                subline.visibility = if (sub.isEmpty()) View.GONE else View.VISIBLE
                golden.visibility = if (p.golden) View.VISIBLE else View.GONE
                root.setOnClickListener { onPage(p.page) }
            }
        }
    }

    class HeaderHolder(val b: ItemChapterBinding) : RecyclerView.ViewHolder(b.root)
    class PageHolder(val b: ItemPageRowBinding) : RecyclerView.ViewHolder(b.root)
}
