package com.seccap.admissions.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.seccap.admissions.data.College
import com.seccap.admissions.databinding.ItemCollegeBinding

class CollegeAdapter(
    private val language: String
) : ListAdapter<College, CollegeAdapter.VH>(DIFF) {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): VH {
        val binding = ItemCollegeBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return VH(binding)
    }

    override fun onBindViewHolder(holder: VH, position: Int) {
        holder.bind(getItem(position))
    }

    inner class VH(private val binding: ItemCollegeBinding) : RecyclerView.ViewHolder(binding.root) {
        fun bind(college: College) {
            binding.collegeName.text = college.name.get(language)
            binding.collegeZone.text = college.zoneId.replaceFirstChar { it.uppercase() }
            binding.collegeFaculties.text = college.faculties.joinToString(", ")
            binding.collegeSeats.text = binding.root.context.getString(
                com.seccap.admissions.R.string.college_meta,
                college.seats,
                college.lastYearCutoff
            )
        }
    }

    companion object {
        private val DIFF = object : DiffUtil.ItemCallback<College>() {
            override fun areItemsTheSame(a: College, b: College) = a.id == b.id
            override fun areContentsTheSame(a: College, b: College) = a == b
        }
    }
}
