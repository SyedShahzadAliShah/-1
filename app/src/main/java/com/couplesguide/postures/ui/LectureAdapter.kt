package com.couplesguide.postures.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.couplesguide.postures.data.CsLecture
import com.couplesguide.postures.databinding.ItemLectureBinding

class LectureAdapter(
    private val onLectureClick: (CsLecture) -> Unit
) : RecyclerView.Adapter<LectureAdapter.ViewHolder>() {

    private var lectures: List<CsLecture> = emptyList()

    fun submitList(list: List<CsLecture>) {
        lectures = list
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemLectureBinding.inflate(
            LayoutInflater.from(parent.context),
            parent,
            false
        )
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(lectures[position])
    }

    override fun getItemCount() = lectures.size

    inner class ViewHolder(
        private val binding: ItemLectureBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun bind(lecture: CsLecture) {
            binding.lectureTitle.text = lecture.title
            val golden = if (lecture.goldenCount > 0) {
                " · ★ ${lecture.goldenCount} golden"
            } else {
                ""
            }
            binding.lectureMeta.text =
                "${lecture.topicCount} study units$golden · English text · Urdu narration"
            binding.root.setOnClickListener { onLectureClick(lecture) }
        }
    }
}
