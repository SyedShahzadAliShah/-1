package com.couplesguide.postures.ui

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.couplesguide.postures.data.TeacherChapter
import com.couplesguide.postures.databinding.ItemChapterBinding

class TeacherChapterAdapter(
    private val onChapterClick: (TeacherChapter) -> Unit
) : RecyclerView.Adapter<TeacherChapterAdapter.ViewHolder>() {

    private var chapters: List<TeacherChapter> = emptyList()

    fun submitList(list: List<TeacherChapter>) {
        chapters = list
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemChapterBinding.inflate(
            LayoutInflater.from(parent.context), parent, false
        )
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(chapters[position])
    }

    override fun getItemCount() = chapters.size

    inner class ViewHolder(
        private val binding: ItemChapterBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun bind(chapter: TeacherChapter) {
            binding.chapterImage.visibility = View.GONE
            binding.chapterTitle.text = chapter.title
            val goldenCount = chapter.topics.count { it.critical }
            binding.chapterSummary.text = binding.root.context.getString(
                com.couplesguide.postures.R.string.chapter_topic_summary,
                chapter.topics.size,
                goldenCount
            )
            binding.root.setOnClickListener { onChapterClick(chapter) }
        }
    }
}
