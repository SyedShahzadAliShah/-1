package com.couplesguide.postures.ui

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.couplesguide.postures.data.TeacherTopic
import com.couplesguide.postures.databinding.ItemChapterBinding

class TeacherTopicAdapter(
    private val onTopicClick: (TeacherTopic) -> Unit
) : RecyclerView.Adapter<TeacherTopicAdapter.ViewHolder>() {

    private var topics: List<TeacherTopic> = emptyList()

    fun submitList(list: List<TeacherTopic>) {
        topics = list
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemChapterBinding.inflate(
            LayoutInflater.from(parent.context), parent, false
        )
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(topics[position], position + 1)
    }

    override fun getItemCount() = topics.size

    inner class ViewHolder(
        private val binding: ItemChapterBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun bind(topic: TeacherTopic, index: Int) {
            binding.chapterImage.visibility = View.GONE
            val prefix = if (topic.critical) "★ " else ""
            binding.chapterTitle.text = "$index. $prefix${topic.title}"
            binding.chapterSummary.text = binding.root.context.getString(
                com.couplesguide.postures.R.string.topic_page_range,
                topic.startPage,
                topic.endPage
            )
            binding.root.setOnClickListener { onTopicClick(topic) }
        }
    }
}
