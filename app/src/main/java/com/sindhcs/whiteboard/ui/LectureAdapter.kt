package com.sindhcs.whiteboard.ui

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.sindhcs.whiteboard.R
import com.sindhcs.whiteboard.data.Lecture
import com.sindhcs.whiteboard.databinding.ItemLectureBinding
import kotlin.math.max

class LectureAdapter(
    private val lectures: List<Lecture>,
    private val onClick: (Lecture) -> Unit
) : RecyclerView.Adapter<LectureAdapter.Holder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): Holder {
        val binding = ItemLectureBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return Holder(binding)
    }

    override fun getItemCount(): Int = lectures.size

    override fun onBindViewHolder(holder: Holder, position: Int) {
        val lecture = lectures[position]
        holder.binding.title.text = lecture.title
        holder.binding.star.visibility = if (lecture.golden) View.VISIBLE else View.GONE
        val minutes = max(1, (lecture.boards.size * 22) / 60)
        holder.binding.meta.text = holder.itemView.context.getString(
            R.string.lecture_meta,
            lecture.boards.size,
            minutes
        )
        holder.binding.root.setOnClickListener { onClick(lecture) }
    }

    class Holder(val binding: ItemLectureBinding) : RecyclerView.ViewHolder(binding.root)
}
