package com.couplesguide.postures.ui

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.couplesguide.postures.databinding.ItemLessonStepBinding
import com.couplesguide.postures.teaching.LessonStep

data class LessonStepUi(
    val step: LessonStep,
    val title: String,
    val description: String,
    val actionLabel: String,
    val complete: Boolean
)

class LessonStepAdapter(
    private val onAction: (LessonStep) -> Unit,
    private val onMarkDone: (LessonStep) -> Unit
) : RecyclerView.Adapter<LessonStepAdapter.ViewHolder>() {

    private var items: List<LessonStepUi> = emptyList()

    fun submitList(list: List<LessonStepUi>) {
        items = list
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemLessonStepBinding.inflate(
            LayoutInflater.from(parent.context),
            parent,
            false
        )
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(items[position])
    }

    override fun getItemCount(): Int = items.size

    inner class ViewHolder(
        private val binding: ItemLessonStepBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun bind(item: LessonStepUi) {
            val check = if (item.complete) "✓ " else "○ "
            binding.stepTitle.text = check + item.title
            binding.stepDescription.text = item.description
            binding.stepAction.text = item.actionLabel
            binding.stepAction.setOnClickListener { onAction(item.step) }
            binding.stepMarkDone.visibility = if (item.complete) View.GONE else View.VISIBLE
            binding.stepMarkDone.setOnClickListener { onMarkDone(item.step) }
        }
    }
}
