package com.seccap.admissions.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.seccap.admissions.data.GuideSection
import com.seccap.admissions.databinding.ItemGuideBinding

class GuideAdapter(
    private val language: String,
    private val onListen: (GuideSection) -> Unit
) : ListAdapter<GuideSection, GuideAdapter.VH>(DIFF) {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): VH {
        val binding = ItemGuideBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return VH(binding)
    }

    override fun onBindViewHolder(holder: VH, position: Int) {
        holder.bind(getItem(position))
    }

    inner class VH(private val binding: ItemGuideBinding) : RecyclerView.ViewHolder(binding.root) {
        fun bind(section: GuideSection) {
            binding.guideTitle.text = section.title.get(language)
            binding.guideBody.text = section.body.get(language)
            binding.btnListen.setOnClickListener { onListen(section) }
        }
    }

    companion object {
        private val DIFF = object : DiffUtil.ItemCallback<GuideSection>() {
            override fun areItemsTheSame(a: GuideSection, b: GuideSection) = a.id == b.id
            override fun areContentsTheSame(a: GuideSection, b: GuideSection) = a == b
        }
    }
}
