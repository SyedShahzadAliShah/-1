package com.couplesguide.postures.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.couplesguide.postures.data.PostureRepository
import com.couplesguide.postures.databinding.ItemCategoryBinding

class CategoryAdapter(
    private val language: String,
    private val onCategoryClick: (String) -> Unit
) : RecyclerView.Adapter<CategoryAdapter.ViewHolder>() {

    private val categoryIds = PostureRepository.getCategoryIds()
    private var selectedPosition = 0

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemCategoryBinding.inflate(
            LayoutInflater.from(parent.context), parent, false
        )
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(categoryIds[position], position == selectedPosition)
    }

    override fun getItemCount() = categoryIds.size

    inner class ViewHolder(
        private val binding: ItemCategoryBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun bind(categoryId: String, isSelected: Boolean) {
            binding.categoryChip.text = PostureRepository.getCategoryLabel(categoryId, language)
            binding.categoryChip.isChecked = isSelected
            binding.categoryChip.setOnClickListener {
                val pos = bindingAdapterPosition
                if (pos != RecyclerView.NO_POSITION) {
                    val previous = selectedPosition
                    selectedPosition = pos
                    notifyItemChanged(previous)
                    notifyItemChanged(selectedPosition)
                    onCategoryClick(categoryId)
                }
            }
        }
    }
}
