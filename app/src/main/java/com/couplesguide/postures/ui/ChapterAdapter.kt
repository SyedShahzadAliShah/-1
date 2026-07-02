package com.couplesguide.postures.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.couplesguide.postures.util.AnimatedIllustrationHelper
import com.couplesguide.postures.data.GuideChapter
import com.couplesguide.postures.databinding.ItemChapterBinding

class ChapterAdapter(
    private val language: String,
    private val onChapterClick: (GuideChapter) -> Unit
) : RecyclerView.Adapter<ChapterAdapter.ViewHolder>() {

    private var chapters: List<GuideChapter> = emptyList()

    fun submitList(list: List<GuideChapter>) {
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

    override fun onViewRecycled(holder: ViewHolder) {
        holder.stopAnimation()
        super.onViewRecycled(holder)
    }

    inner class ViewHolder(
        private val binding: ItemChapterBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun stopAnimation() {
            AnimatedIllustrationHelper.stop(binding.chapterImage)
        }

        fun bind(chapter: GuideChapter) {
            val content = chapter.content(language)
            binding.chapterTitle.text = content.title
            binding.chapterSummary.text = content.summary
            AnimatedIllustrationHelper.bind(binding.chapterImage, chapter.illustrationRes)
            binding.root.setOnClickListener { onChapterClick(chapter) }
        }
    }
}
