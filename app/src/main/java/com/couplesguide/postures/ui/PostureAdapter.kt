package com.couplesguide.postures.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.couplesguide.postures.data.Posture
import com.couplesguide.postures.data.PostureListItem
import com.couplesguide.postures.databinding.ItemEduCardBinding
import com.couplesguide.postures.databinding.ItemPostureBinding
import com.couplesguide.postures.util.AnimatedIllustrationHelper
import com.couplesguide.postures.util.LocaleHelper

class PostureAdapter(
    private val language: String,
    private val onPostureClick: (Posture) -> Unit
) : ListAdapter<PostureListItem, RecyclerView.ViewHolder>(DiffCallback()) {

    override fun getItemViewType(position: Int): Int = when (getItem(position)) {
        is PostureListItem.PostureEntry -> VIEW_POSTURE
        is PostureListItem.EducationalCard -> VIEW_EDU
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecyclerView.ViewHolder {
        val inflater = LayoutInflater.from(parent.context)
        return when (viewType) {
            VIEW_EDU -> EduViewHolder(
                ItemEduCardBinding.inflate(inflater, parent, false)
            )
            else -> PostureViewHolder(
                ItemPostureBinding.inflate(inflater, parent, false)
            )
        }
    }

    override fun onBindViewHolder(holder: RecyclerView.ViewHolder, position: Int) {
        when (val item = getItem(position)) {
            is PostureListItem.PostureEntry -> (holder as PostureViewHolder).bind(item.posture)
            is PostureListItem.EducationalCard -> (holder as EduViewHolder).bind(item.insert)
        }
    }

    override fun onViewRecycled(holder: RecyclerView.ViewHolder) {
        if (holder is PostureViewHolder) holder.stopAnimation()
        if (holder is EduViewHolder) holder.stopAnimation()
        super.onViewRecycled(holder)
    }

    inner class PostureViewHolder(
        private val binding: ItemPostureBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun stopAnimation() {
            AnimatedIllustrationHelper.stop(binding.thumbnail)
        }

        fun bind(posture: Posture) {
            val content = posture.content(language)
            binding.postureName.text = content.name
            binding.postureSummary.text = content.summary
            binding.difficultyText.text = posture.difficulty.label(language)
            binding.categoryText.text = content.category
            AnimatedIllustrationHelper.bind(binding.thumbnail, posture.illustrationRes)
            binding.root.setOnClickListener { onPostureClick(posture) }
        }
    }

    inner class EduViewHolder(
        private val binding: ItemEduCardBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun stopAnimation() {
            AnimatedIllustrationHelper.stop(binding.eduImage)
        }

        fun bind(insert: com.couplesguide.postures.data.EducationalInsert) {
            val isUrdu = language == LocaleHelper.LANG_UR
            binding.eduTitle.text = if (isUrdu) insert.urduTitle else insert.englishTitle
            binding.eduCaption.text = if (isUrdu) insert.urduCaption else insert.englishCaption
            AnimatedIllustrationHelper.bind(binding.eduImage, insert.illustrationRes)
            binding.root.setOnClickListener(null)
            binding.root.isClickable = false
        }
    }

    private class DiffCallback : DiffUtil.ItemCallback<PostureListItem>() {
        override fun areItemsTheSame(oldItem: PostureListItem, newItem: PostureListItem): Boolean {
            return when {
                oldItem is PostureListItem.PostureEntry && newItem is PostureListItem.PostureEntry ->
                    oldItem.posture.id == newItem.posture.id
                oldItem is PostureListItem.EducationalCard && newItem is PostureListItem.EducationalCard ->
                    oldItem.insert.id == newItem.insert.id
                else -> false
            }
        }

        override fun areContentsTheSame(oldItem: PostureListItem, newItem: PostureListItem) =
            oldItem == newItem
    }

    companion object {
        private const val VIEW_POSTURE = 0
        private const val VIEW_EDU = 1
    }
}
