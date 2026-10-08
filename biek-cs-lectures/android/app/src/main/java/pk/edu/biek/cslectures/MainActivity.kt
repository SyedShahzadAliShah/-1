package pk.edu.biek.cslectures

import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import pk.edu.biek.cslectures.data.Catalog
import pk.edu.biek.cslectures.databinding.ActivityMainBinding
import pk.edu.biek.cslectures.databinding.ItemHeaderBinding
import pk.edu.biek.cslectures.databinding.ItemLectureBinding
import pk.edu.biek.cslectures.model.Lecture

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        val rows = buildList {
            add(Row.Header("Class XI"))
            Catalog.lectures.filter { it.year == "XI" }.forEach { add(Row.Item(it)) }
            add(Row.Header("Class XII"))
            Catalog.lectures.filter { it.year == "XII" }.forEach { add(Row.Item(it)) }
        }
        binding.lectureList.layoutManager = LinearLayoutManager(this)
        binding.lectureList.adapter = LectureRowsAdapter(rows) { lecture ->
            startActivity(
                Intent(this, LectureActivity::class.java)
                    .putExtra(LectureActivity.EXTRA_ID, lecture.id)
            )
        }
    }
}

private sealed class Row {
    data class Header(val title: String) : Row()
    data class Item(val lecture: Lecture) : Row()
}

private class LectureRowsAdapter(
    private val rows: List<Row>,
    private val onLecture: (Lecture) -> Unit,
) : RecyclerView.Adapter<RecyclerView.ViewHolder>() {

    override fun getItemViewType(position: Int): Int =
        if (rows[position] is Row.Header) VIEW_HEADER else VIEW_ITEM

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecyclerView.ViewHolder {
        val inflater = LayoutInflater.from(parent.context)
        return if (viewType == VIEW_HEADER) {
            HeaderHolder(ItemHeaderBinding.inflate(inflater, parent, false))
        } else {
            ItemHolder(ItemLectureBinding.inflate(inflater, parent, false), onLecture)
        }
    }

    override fun onBindViewHolder(holder: RecyclerView.ViewHolder, position: Int) {
        when (val row = rows[position]) {
            is Row.Header -> (holder as HeaderHolder).bind(row.title)
            is Row.Item -> (holder as ItemHolder).bind(row.lecture)
        }
    }

    override fun getItemCount(): Int = rows.size

    private class HeaderHolder(private val binding: ItemHeaderBinding) :
        RecyclerView.ViewHolder(binding.root) {
        fun bind(title: String) {
            binding.headerTitle.text = title
        }
    }

    private class ItemHolder(
        private val binding: ItemLectureBinding,
        private val onLecture: (Lecture) -> Unit,
    ) : RecyclerView.ViewHolder(binding.root) {
        fun bind(lecture: Lecture) {
            binding.kicker.text = "Class ${lecture.year}  ·  Lecture ${lecture.number}"
            binding.title.text = lecture.title
            binding.urduTitle.text = lecture.urduTitle
            UrduType.apply(binding.root.context, binding.urduTitle)
            binding.root.setOnClickListener { onLecture(lecture) }
        }
    }

    companion object {
        private const val VIEW_HEADER = 0
        private const val VIEW_ITEM = 1
    }
}
