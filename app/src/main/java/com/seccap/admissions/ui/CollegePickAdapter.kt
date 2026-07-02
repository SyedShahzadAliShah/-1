package com.seccap.admissions.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.core.content.ContextCompat
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.seccap.admissions.R
import com.seccap.admissions.data.College
import com.seccap.admissions.databinding.ItemCollegePickBinding

class CollegePickAdapter(
    private val language: String,
    private val selectedOrder: List<String>,
    private val onToggle: (College) -> Unit
) : ListAdapter<College, CollegePickAdapter.VH>(DIFF) {

    private var selectedSet = emptySet<String>()

    fun setSelected(ids: Set<String>) {
        selectedSet = ids
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): VH {
        val binding = ItemCollegePickBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return VH(binding)
    }

    override fun onBindViewHolder(holder: VH, position: Int) {
        holder.bind(getItem(position))
    }

    inner class VH(private val binding: ItemCollegePickBinding) : RecyclerView.ViewHolder(binding.root) {
        fun bind(college: College) {
            val selected = college.id in selectedSet
            val rank = selectedOrder.indexOf(college.id).let { if (it >= 0) it + 1 else 0 }

            binding.collegeName.text = college.name.get(language)
            binding.collegeMeta.text = binding.root.context.getString(
                R.string.college_meta,
                college.seats,
                college.lastYearCutoff
            )
            binding.rankBadge.text = if (rank > 0) "#$rank" else ""
            binding.rankBadge.visibility = if (rank > 0) android.view.View.VISIBLE else android.view.View.GONE

            binding.root.setBackgroundColor(
                ContextCompat.getColor(
                    binding.root.context,
                    if (selected) R.color.primary_light else R.color.surface
                )
            )
            binding.root.setOnClickListener { onToggle(college) }
        }
    }

    companion object {
        private val DIFF = object : DiffUtil.ItemCallback<College>() {
            override fun areItemsTheSame(a: College, b: College) = a.id == b.id
            override fun areContentsTheSame(a: College, b: College) = a == b
        }
    }
}
