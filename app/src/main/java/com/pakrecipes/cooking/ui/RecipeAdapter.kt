package com.pakrecipes.cooking.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.pakrecipes.cooking.data.Recipe
import com.pakrecipes.cooking.databinding.ItemRecipeBinding

class RecipeAdapter(
    private val onRecipeClick: (Recipe) -> Unit
) : ListAdapter<Recipe, RecipeAdapter.ViewHolder>(DIFF) {

    inner class ViewHolder(private val binding: ItemRecipeBinding) :
        RecyclerView.ViewHolder(binding.root) {

        fun bind(recipe: Recipe) {
            binding.recipeName.text = recipe.nameUrdu
            binding.recipeDescription.text = recipe.descriptionUrdu
            binding.recipeMeta.text = buildMeta(recipe)
            binding.root.setOnClickListener { onRecipeClick(recipe) }
        }

        private fun buildMeta(recipe: Recipe): String {
            val city = recipe.cityId.toCityName()
            val time = "${recipe.prepTimeMinutes + recipe.cookTimeMinutes} منٹ"
            val diff = recipe.difficulty.labelUrdu
            return "$city  •  $time  •  $diff"
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemRecipeBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(getItem(position))
    }

    companion object {
        private val DIFF = object : DiffUtil.ItemCallback<Recipe>() {
            override fun areItemsTheSame(a: Recipe, b: Recipe) = a.id == b.id
            override fun areContentsTheSame(a: Recipe, b: Recipe) = a == b
        }
    }
}

private fun String.toCityName(): String = when (this) {
    "karachi" -> "کراچی"
    "lahore" -> "لاہور"
    "peshawar" -> "پشاور"
    "quetta" -> "کوئٹہ"
    "hyderabad" -> "حیدرآباد"
    "multan" -> "ملتان"
    "islamabad" -> "اسلام آباد"
    "rawalpindi" -> "راولپنڈی"
    "gilgit" -> "گلگت بلتستان"
    else -> this
}
