package com.sindhcs.lectures

import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.sindhcs.lectures.data.LectureRepository
import com.sindhcs.lectures.data.Topic
import com.sindhcs.lectures.databinding.ActivityListBinding
import com.sindhcs.lectures.databinding.ItemRowBinding

class TopicListActivity : AppCompatActivity() {
    private lateinit var binding: ActivityListBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityListBinding.inflate(layoutInflater)
        setContentView(binding.root)
        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        binding.toolbar.setNavigationOnClickListener { finish() }

        val gradeId = intent.getStringExtra(MainActivity.EXTRA_GRADE) ?: return finish()
        val chNum = intent.getIntExtra(MainActivity.EXTRA_CHAPTER, 0)
        val chapter = LectureRepository.chapter(this, gradeId, chNum) ?: return finish()
        title = "Chapter ${chapter.num}"
        binding.subtitle.text = chapter.title

        binding.list.layoutManager = LinearLayoutManager(this)
        binding.list.adapter = TopicAdapter(chapter.topics) { topic ->
            startActivity(
                Intent(this, TopicActivity::class.java)
                    .putExtra(MainActivity.EXTRA_GRADE, gradeId)
                    .putExtra(MainActivity.EXTRA_CHAPTER, chNum)
                    .putExtra(MainActivity.EXTRA_TOPIC, topic.id)
            )
        }
    }
}

class TopicAdapter(
    private val items: List<Topic>,
    private val onClick: (Topic) -> Unit
) : RecyclerView.Adapter<TopicAdapter.Holder>() {
    class Holder(val binding: ItemRowBinding) : RecyclerView.ViewHolder(binding.root)

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): Holder {
        val binding = ItemRowBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return Holder(binding)
    }

    override fun getItemCount(): Int = items.size

    override fun onBindViewHolder(holder: Holder, position: Int) {
        val topic = items[position]
        holder.binding.badge.text = "%02d".format(position + 1)
        holder.binding.title.text = topic.title
        holder.binding.meta.text = if (topic.golden) {
            holder.itemView.context.getString(R.string.golden_topic)
        } else {
            holder.itemView.context.getString(R.string.lecture_note)
        }
        holder.binding.star.visibility = if (topic.golden) View.VISIBLE else View.GONE
        holder.binding.root.setOnClickListener { onClick(topic) }
    }
}
