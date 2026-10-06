package com.sindh.cswhiteboard.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.sindh.cswhiteboard.data.Chapter
import com.sindh.cswhiteboard.databinding.ItemChapterBinding

class ChapterAdapter(
    private val items: List<Chapter>,
    private val urdu: Boolean,
    private val onClick: (Chapter) -> Unit
) : RecyclerView.Adapter<ChapterAdapter.Holder>() {

    inner class Holder(val binding: ItemChapterBinding) : RecyclerView.ViewHolder(binding.root)

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): Holder {
        val inflater = LayoutInflater.from(parent.context)
        return Holder(ItemChapterBinding.inflate(inflater, parent, false))
    }

    override fun getItemCount(): Int = items.size

    override fun onBindViewHolder(holder: Holder, position: Int) {
        val chapter = items[position]
        holder.binding.number.text = if (chapter.number == 0) "•" else chapter.number.toString()
        holder.binding.title.text = if (urdu) chapter.titleUr else chapter.titleEn
        holder.binding.meta.text = holder.itemView.context.getString(
            com.sindh.cswhiteboard.R.string.chapter_meta,
            chapter.lectures.size,
            chapter.lectures.count { it.golden }
        )
        holder.binding.root.setOnClickListener { onClick(chapter) }
    }
}
