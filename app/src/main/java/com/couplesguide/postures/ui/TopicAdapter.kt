package com.couplesguide.postures.ui

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.couplesguide.postures.data.CsTopic
import com.couplesguide.postures.databinding.ItemChapterBinding

class TopicAdapter(
    private val onTopicClick: (CsTopic) -> Unit
) : RecyclerView.Adapter<TopicAdapter.ViewHolder>() {

    private var topics: List<CsTopic> = emptyList()

    fun submitList(list: List<CsTopic>) {
        topics = list
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemChapterBinding.inflate(
            LayoutInflater.from(parent.context),
            parent,
            false
        )
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(topics[position])
    }

    override fun getItemCount() = topics.size

    inner class ViewHolder(
        private val binding: ItemChapterBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun bind(topic: CsTopic) {
            binding.chapterImage.visibility = View.GONE
            binding.chapterTitle.text = if (topic.golden) "★ ${topic.title}" else topic.title
            val preview = topic.english.lineSequence().firstOrNull { it.isNotBlank() } ?: topic.title
            binding.chapterSummary.text = "Guideline: ${preview.take(120)}"
            binding.root.setOnClickListener { onTopicClick(topic) }
        }
    }
}
