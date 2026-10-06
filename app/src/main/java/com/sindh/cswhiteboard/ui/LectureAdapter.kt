package com.sindh.cswhiteboard.ui

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.sindh.cswhiteboard.data.Lecture
import com.sindh.cswhiteboard.databinding.ItemLectureBinding

class LectureAdapter(
    private val items: List<Lecture>,
    private val urdu: Boolean,
    private val done: Set<String>,
    private val onClick: (Lecture) -> Unit
) : RecyclerView.Adapter<LectureAdapter.Holder>() {

    inner class Holder(val binding: ItemLectureBinding) : RecyclerView.ViewHolder(binding.root)

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): Holder {
        val inflater = LayoutInflater.from(parent.context)
        return Holder(ItemLectureBinding.inflate(inflater, parent, false))
    }

    override fun getItemCount(): Int = items.size

    override fun onBindViewHolder(holder: Holder, position: Int) {
        val lecture = items[position]
        holder.binding.code.text = lecture.code
        holder.binding.title.text = if (urdu) lecture.titleUr else lecture.titleEn
        holder.binding.meta.text = holder.itemView.context.getString(
            com.sindh.cswhiteboard.R.string.lecture_meta,
            lecture.segments.size,
            lecture.durationHintSec
        )
        holder.binding.golden.visibility = if (lecture.golden) View.VISIBLE else View.GONE
        holder.binding.done.visibility = if (done.contains(lecture.id)) View.VISIBLE else View.GONE
        holder.binding.root.setOnClickListener { onClick(lecture) }
    }
}
