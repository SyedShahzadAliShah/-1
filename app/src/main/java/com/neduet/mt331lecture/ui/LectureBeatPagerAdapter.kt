package com.neduet.mt331lecture.ui

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.view.animation.AnimationUtils
import androidx.recyclerview.widget.RecyclerView
import com.neduet.mt331lecture.R
import com.neduet.mt331lecture.data.mt331.LectureBeat
import com.neduet.mt331lecture.data.mt331.Mt331BeatDiagrams
import com.neduet.mt331lecture.data.mt331.Mt331LatexCatalog
import com.neduet.mt331lecture.databinding.ItemLectureBeatBinding

class LectureBeatPagerAdapter(
    private var displayLanguage: String = "en"
) : RecyclerView.Adapter<LectureBeatPagerAdapter.BeatViewHolder>() {

    private var beats: List<LectureBeat> = emptyList()

    fun submitBeats(items: List<LectureBeat>) {
        beats = items
        notifyDataSetChanged()
    }

    fun setDisplayLanguage(language: String) {
        if (displayLanguage == language) return
        displayLanguage = language
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
        holder.bind(beats[position], displayLanguage)
    }

    override fun getItemCount(): Int = beats.size

    class BeatViewHolder(
        private val binding: ItemLectureBeatBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun bind(beat: LectureBeat, displayLanguage: String) {
            binding.beatGlyph.text = beat.glyph
            binding.beatTitleEn.text = beat.titleEn
            binding.beatTitleUr.text = beat.titleUr
            binding.beatBodyEn.text = beat.narrationEn
            binding.beatBodyUr.text = beat.narrationUr

            val hasMath = Mt331LatexCatalog.latexForBeat(beat, displayLanguage).isNotBlank() ||
                Mt331BeatDiagrams.svgForBeat(beat.id) != null
            if (hasMath) {
                binding.beatMathCard.visibility = View.VISIBLE
                LectureMathEmbedView.bind(binding.beatMathWebView, beat, displayLanguage)
            } else {
                binding.beatMathCard.visibility = View.GONE
            }

            val anim = AnimationUtils.loadAnimation(binding.root.context, R.anim.fade_in_cinema)
            binding.beatRoot.startAnimation(anim)
        }
    }
}
