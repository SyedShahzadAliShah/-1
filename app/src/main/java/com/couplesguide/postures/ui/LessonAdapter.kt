package com.couplesguide.postures.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.couplesguide.postures.data.SexEdLesson
import com.couplesguide.postures.databinding.ItemChapterBinding
import com.couplesguide.postures.util.AnimatedIllustrationHelper

class LessonAdapter(
    private val onLessonClick: (SexEdLesson) -> Unit
) : RecyclerView.Adapter<LessonAdapter.ViewHolder>() {

    private var lessons: List<SexEdLesson> = emptyList()

    fun submitList(list: List<SexEdLesson>) {
        lessons = list
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemChapterBinding.inflate(
            LayoutInflater.from(parent.context), parent, false
        )
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(lessons[position])
    }

    override fun getItemCount() = lessons.size

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

        fun bind(lesson: SexEdLesson) {
            binding.chapterTitle.text = lesson.title
            binding.chapterSummary.text = lesson.summary
            AnimatedIllustrationHelper.bind(binding.chapterImage, lesson.illustrationRes)
            binding.root.setOnClickListener { onLessonClick(lesson) }
        }
    }
}
