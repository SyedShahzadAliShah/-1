package com.neduet.mt331lecture.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.neduet.mt331lecture.data.mt331.LectureChapter
import com.neduet.mt331lecture.databinding.ItemMt331ChapterBinding

class Mt331ChapterAdapter(
    private val language: String,
    private val onChapterClick: (LectureChapter) -> Unit
) : RecyclerView.Adapter<Mt331ChapterAdapter.ChapterViewHolder>() {

    private var chapters: List<LectureChapter> = emptyList()

    fun submitList(items: List<LectureChapter>) {
        chapters = items
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ChapterViewHolder {
        val binding = ItemMt331ChapterBinding.inflate(
            LayoutInflater.from(parent.context),
            parent,
            false
        )
        return ChapterViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ChapterViewHolder, position: Int) {
        holder.bind(chapters[position])
    }

    override fun getItemCount(): Int = chapters.size

    inner class ChapterViewHolder(
        private val binding: ItemMt331ChapterBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun bind(chapter: LectureChapter) {
            binding.chapterBadge.text = "Ch ${chapter.chapterNumber}"
            binding.chapterTitle.text = chapter.title(language)
            binding.chapterTagline.text = chapter.tagline(language)
            val beatLabel = if (language == "ur") {
                "${chapter.beats.size} لیکچر نوٹس"
            } else {
                "${chapter.beats.size} lecture beats"
            }
            binding.chapterBeatCount.text = beatLabel
            binding.root.setOnClickListener { onChapterClick(chapter) }
        }
    }
}
