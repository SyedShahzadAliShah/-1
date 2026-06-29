package com.couplesguide.postures.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.couplesguide.postures.data.Posture
import com.couplesguide.postures.databinding.ItemPostureBinding

class PostureAdapter(
    private val language: String,
    private val onPostureClick: (Posture) -> Unit
) : ListAdapter<Posture, PostureAdapter.ViewHolder>(DiffCallback()) {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemPostureBinding.inflate(
            LayoutInflater.from(parent.context), parent, false
        )
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(getItem(position))
    }

    inner class ViewHolder(
        private val binding: ItemPostureBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun bind(posture: Posture) {
            val content = posture.content(language)
            binding.postureName.text = content.name
            binding.postureSummary.text = content.summary
            binding.difficultyText.text = posture.difficulty.label(language)
            binding.categoryText.text = content.category
            binding.thumbnail.setImageResource(posture.illustrationRes)
            binding.root.setOnClickListener { onPostureClick(posture) }
        }
    }

    private class DiffCallback : DiffUtil.ItemCallback<Posture>() {
        override fun areItemsTheSame(oldItem: Posture, newItem: Posture) =
            oldItem.id == newItem.id

        override fun areContentsTheSame(oldItem: Posture, newItem: Posture) =
            oldItem == newItem
    }
}
