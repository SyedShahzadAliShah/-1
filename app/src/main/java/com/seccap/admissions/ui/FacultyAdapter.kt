package com.seccap.admissions.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.core.content.ContextCompat
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.seccap.admissions.R
import com.seccap.admissions.data.FacultyGroup
import com.seccap.admissions.databinding.ItemFacultyBinding

class FacultyAdapter(
    private val language: String,
    private var selectedId: String,
    private val onSelect: (FacultyGroup) -> Unit
) : ListAdapter<FacultyGroup, FacultyAdapter.VH>(DIFF) {

    fun setSelected(id: String) {
        selectedId = id
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): VH {
        val binding = ItemFacultyBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return VH(binding)
    }

    override fun onBindViewHolder(holder: VH, position: Int) {
        holder.bind(getItem(position))
    }

    inner class VH(private val binding: ItemFacultyBinding) : RecyclerView.ViewHolder(binding.root) {
        fun bind(faculty: FacultyGroup) {
            val selected = faculty.id == selectedId
            binding.facultyName.text = faculty.name.get(language)
            binding.facultySubjects.text = faculty.subjects.get(language)
            binding.facultyMinMarks.text = binding.root.context.getString(
                R.string.min_percentage,
                faculty.minPercentage
            )
            binding.root.setBackgroundColor(
                ContextCompat.getColor(
                    binding.root.context,
                    if (selected) R.color.primary_light else R.color.surface
                )
            )
            binding.root.strokeWidth = if (selected) 4 else 1
            binding.root.setOnClickListener { onSelect(faculty) }
        }
    }

    companion object {
        private val DIFF = object : DiffUtil.ItemCallback<FacultyGroup>() {
            override fun areItemsTheSame(a: FacultyGroup, b: FacultyGroup) = a.id == b.id
            override fun areContentsTheSame(a: FacultyGroup, b: FacultyGroup) = a == b
        }
    }
}
