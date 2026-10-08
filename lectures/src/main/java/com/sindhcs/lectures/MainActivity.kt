package com.sindhcs.lectures

import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.sindhcs.lectures.data.Chapter
import com.sindhcs.lectures.data.LectureRepository
import com.sindhcs.lectures.databinding.ActivityListBinding
import com.sindhcs.lectures.databinding.ItemRowBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityListBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityListBinding.inflate(layoutInflater)
        setContentView(binding.root)
        setSupportActionBar(binding.toolbar)
        title = getString(R.string.home_title)

        val grade = LectureRepository.grade(this, GRADE_XII) ?: return finish()
        binding.subtitle.text = getString(
            R.string.grade_meta,
            grade.chapters.size,
            grade.chapters.sumOf { it.topics.size },
            grade.chapters.sumOf { it.goldenCount }
        ) + "\n" + grade.urdu

        binding.list.layoutManager = LinearLayoutManager(this)
        binding.list.adapter = ChapterAdapter(grade.chapters) { chapter ->
            startActivity(
                Intent(this, TopicListActivity::class.java)
                    .putExtra(EXTRA_GRADE, GRADE_XII)
                    .putExtra(EXTRA_CHAPTER, chapter.num)
            )
        }
    }

    companion object {
        const val GRADE_XII = "xii"
        const val EXTRA_GRADE = "grade_id"
        const val EXTRA_CHAPTER = "chapter_num"
        const val EXTRA_TOPIC = "topic_id"
    }
}

class ChapterAdapter(
    private val items: List<Chapter>,
    private val onClick: (Chapter) -> Unit
) : RecyclerView.Adapter<ChapterAdapter.Holder>() {

    class Holder(val binding: ItemRowBinding) : RecyclerView.ViewHolder(binding.root)

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): Holder {
        val binding = ItemRowBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return Holder(binding)
    }

    override fun getItemCount(): Int = items.size

    override fun onBindViewHolder(holder: Holder, position: Int) {
        val chapter = items[position]
        holder.binding.badge.text = "%02d".format(chapter.num)
        holder.binding.title.text = chapter.title
        val urdu = chapter.urdu
        holder.binding.meta.text = buildString {
            append(
                holder.itemView.context.getString(
                    R.string.chapter_meta,
                    chapter.topics.size,
                    chapter.goldenCount
                )
            )
            if (urdu.isNotBlank()) {
                append("\n")
                append(urdu)
            }
        }
        holder.binding.root.setOnClickListener { onClick(chapter) }
    }
}
