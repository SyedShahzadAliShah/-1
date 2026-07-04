package com.pakrecipes.cooking.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.pakrecipes.cooking.data.CityCategory
import com.pakrecipes.cooking.databinding.ItemCityBinding

class CityAdapter(
    private val onCitySelected: (String) -> Unit
) : ListAdapter<CityCategory, CityAdapter.ViewHolder>(DIFF) {

    private var selectedId: String = CityCategory.ALL

    inner class ViewHolder(private val binding: ItemCityBinding) :
        RecyclerView.ViewHolder(binding.root) {

        fun bind(city: CityCategory) {
            binding.cityEmoji.text = city.emoji
            binding.cityName.text = city.nameUrdu
            val isSelected = city.id == selectedId
            binding.root.isSelected = isSelected
            binding.root.setOnClickListener {
                val old = selectedId
                selectedId = city.id
                onCitySelected(city.id)
                notifyItemChanged(currentList.indexOfFirst { it.id == old })
                notifyItemChanged(bindingAdapterPosition)
            }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemCityBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(getItem(position))
    }

    companion object {
        private val DIFF = object : DiffUtil.ItemCallback<CityCategory>() {
            override fun areItemsTheSame(a: CityCategory, b: CityCategory) = a.id == b.id
            override fun areContentsTheSame(a: CityCategory, b: CityCategory) = a == b
        }
    }
}
