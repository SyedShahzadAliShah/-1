package com.couplesguide.postures.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import android.view.animation.AnimationUtils
import androidx.recyclerview.widget.RecyclerView
import com.couplesguide.postures.R
import com.couplesguide.postures.data.mt331.LectureBeat
import com.couplesguide.postures.databinding.ItemLectureBeatBinding

class LectureBeatPagerAdapter : RecyclerView.Adapter<LectureBeatPagerAdapter.BeatViewHolder>() {

    private var beats: List<LectureBeat> = emptyList()

    fun submitBeats(items: List<LectureBeat>) {
        beats = items
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): BeatViewHolder {
        val binding = ItemLectureBeatBinding.inflate(
            LayoutInflater.from(parent.context),
            parent,
            false
        )
        return BeatViewHolder(binding)
    }

    override fun onBindViewHolder(holder: BeatViewHolder, position: Int) {
        holder.bind(beats[position])
    }

    override fun getItemCount(): Int = beats.size

    class BeatViewHolder(
        private val binding: ItemLectureBeatBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun bind(beat: LectureBeat) {
            binding.beatGlyph.text = beat.glyph
            binding.beatTitleEn.text = beat.titleEn
            binding.beatTitleUr.text = beat.titleUr
            binding.beatBodyEn.text = beat.narrationEn
            binding.beatBodyUr.text = beat.narrationUr
            val formulaBlock = buildString {
                if (beat.formulaEn.isNotBlank()) append(beat.formulaEn)
                if (beat.formulaUr.isNotBlank()) {
                    if (isNotEmpty()) append("\n\n")
                    append(beat.formulaUr)
                }
            }
            binding.beatFormula.text = formulaBlock
            binding.beatFormula.visibility = if (formulaBlock.isBlank()) {
                android.view.View.GONE
            } else {
                android.view.View.VISIBLE
            }
            val anim = AnimationUtils.loadAnimation(binding.root.context, R.anim.fade_in_cinema)
            binding.beatRoot.startAnimation(anim)
        }
    }
}
