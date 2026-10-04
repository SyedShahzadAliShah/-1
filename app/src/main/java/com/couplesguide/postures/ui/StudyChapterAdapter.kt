package com.couplesguide.postures.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.couplesguide.postures.data.StudyChapter
import com.couplesguide.postures.databinding.ItemChapterBinding

class StudyChapterAdapter(
    private val language: String,
    private val onChapterClick: (StudyChapter) -> Unit
) : RecyclerView.Adapter<StudyChapterAdapter.ViewHolder>() {

    private var chapters: List<StudyChapter> = emptyList()

    fun submitList(list: List<StudyChapter>) {
        chapters = list
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
        holder.bind(chapters[position])
    }

    override fun getItemCount(): Int = chapters.size

    inner class ViewHolder(
        private val binding: ItemChapterBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun bind(chapter: StudyChapter) {
            val content = chapter.content(language)
            binding.chapterTitle.text = content.title
            binding.chapterSummary.text = content.summary
            binding.chapterImage.setImageResource(chapter.illustrationRes)
            binding.root.setOnClickListener { onChapterClick(chapter) }
        }
    }
}
