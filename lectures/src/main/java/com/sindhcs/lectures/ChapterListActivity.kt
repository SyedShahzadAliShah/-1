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

class ChapterListActivity : AppCompatActivity() {
    private lateinit var binding: ActivityListBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityListBinding.inflate(layoutInflater)
        setContentView(binding.root)
        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        binding.toolbar.setNavigationOnClickListener { finish() }

        val gradeId = intent.getStringExtra(MainActivity.EXTRA_GRADE) ?: return finish()
        val grade = LectureRepository.grade(this, gradeId) ?: return finish()
        title = grade.title
        binding.subtitle.text = getString(R.string.chapters_hint)

        binding.list.layoutManager = LinearLayoutManager(this)
        binding.list.adapter = ChapterAdapter(grade.chapters) { chapter ->
            startActivity(
                Intent(this, TopicListActivity::class.java)
                    .putExtra(MainActivity.EXTRA_GRADE, gradeId)
                    .putExtra(MainActivity.EXTRA_CHAPTER, chapter.num)
            )
        }
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
        holder.binding.meta.text = holder.itemView.context.getString(
            R.string.chapter_meta,
            chapter.topics.size,
            chapter.goldenCount
        )
        holder.binding.root.setOnClickListener { onClick(chapter) }
    }
}
