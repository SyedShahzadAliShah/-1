package com.sindhcs.whiteboard.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.sindhcs.whiteboard.R
import com.sindhcs.whiteboard.data.Chapter
import com.sindhcs.whiteboard.databinding.ItemChapterBinding

class ChapterAdapter(
    private val chapters: List<Chapter>,
    private val onClick: (Chapter) -> Unit
) : RecyclerView.Adapter<ChapterAdapter.Holder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): Holder {
        val binding = ItemChapterBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return Holder(binding)
    }

    override fun getItemCount(): Int = chapters.size

    override fun onBindViewHolder(holder: Holder, position: Int) {
        val chapter = chapters[position]
        holder.binding.badge.text = chapter.number.toString()
        holder.binding.title.text = chapter.title
        val golden = chapter.lectures.count { it.golden }
        holder.binding.meta.text = holder.itemView.context.getString(
            R.string.chapter_meta,
            chapter.lectures.size,
            golden
        )
        holder.binding.root.setOnClickListener { onClick(chapter) }
    }

    class Holder(val binding: ItemChapterBinding) : RecyclerView.ViewHolder(binding.root)
}
