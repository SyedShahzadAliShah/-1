package com.couplesguide.postures.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.couplesguide.postures.data.Recipe
import com.couplesguide.postures.databinding.ItemPostureBinding
import com.couplesguide.postures.util.AnimatedIllustrationHelper

class RecipeAdapter(
    private val language: String,
    private val onRecipeClick: (Recipe) -> Unit
) : ListAdapter<Recipe, RecipeAdapter.ViewHolder>(DiffCallback()) {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemPostureBinding.inflate(
            LayoutInflater.from(parent.context), parent, false
        )
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(getItem(position))
    }

    override fun onViewRecycled(holder: ViewHolder) {
        holder.stopAnimation()
        super.onViewRecycled(holder)
    }

    inner class ViewHolder(
        private val binding: ItemPostureBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun stopAnimation() {
            AnimatedIllustrationHelper.stop(binding.thumbnail)
        }

        fun bind(recipe: Recipe) {
            val content = recipe.content(language)
            binding.postureName.text = content.name
            binding.postureSummary.text = content.summary
            binding.difficultyText.text = recipe.difficulty.label(language)
            binding.categoryText.text = content.category
            AnimatedIllustrationHelper.bind(binding.thumbnail, recipe.illustrationRes)
            binding.root.setOnClickListener { onRecipeClick(recipe) }
        }
    }

    private class DiffCallback : DiffUtil.ItemCallback<Recipe>() {
        override fun areItemsTheSame(oldItem: Recipe, newItem: Recipe) = oldItem.id == newItem.id
        override fun areContentsTheSame(oldItem: Recipe, newItem: Recipe) = oldItem == newItem
    }
}
