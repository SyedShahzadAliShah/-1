package com.couplesguide.postures.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.couplesguide.postures.databinding.ItemTeachingChapterBinding
import com.couplesguide.postures.data.StudyChapter
import com.couplesguide.postures.teaching.TeachingProgressStore

class TeachingCurriculumAdapter(
    private val language: String,
    private val onChapterClick: (StudyChapter) -> Unit
) : RecyclerView.Adapter<TeachingCurriculumAdapter.ViewHolder>() {

    private var chapters: List<StudyChapter> = emptyList()

    fun submitList(list: List<StudyChapter>) {
        chapters = list
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemTeachingChapterBinding.inflate(
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
        private val binding: ItemTeachingChapterBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun bind(chapter: StudyChapter) {
            val ctx = binding.root.context
            val content = chapter.content(language)
            binding.chapterLabel.text = "CS ${chapter.grade} • Ch.${chapter.chapterNumber}"
            binding.chapterTitle.text = content.title
            val percent = TeachingProgressStore.chapterProgressPercent(ctx, chapter.id)
            binding.chapterProgress.max = 100
            binding.chapterProgress.progress = percent
            binding.chapterProgressText.text = ctx.getString(
                com.couplesguide.postures.R.string.teaching_chapter_progress,
                percent
            )
            binding.root.setOnClickListener { onChapterClick(chapter) }
        }
    }
}
