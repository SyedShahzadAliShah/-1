package com.couplesguide.postures.util

import com.couplesguide.postures.R

object IllustrationAssets {

    private val animatedByStatic = mapOf(
        R.drawable.ill_missionary to R.drawable.avd_ill_missionary,
        R.drawable.ill_cowgirl to R.drawable.avd_ill_cowgirl,
        R.drawable.ill_spooning to R.drawable.avd_ill_spooning,
        R.drawable.ill_side_by_side to R.drawable.avd_ill_side_by_side,
        R.drawable.ill_doggy to R.drawable.avd_ill_doggy,
        R.drawable.ill_lotus to R.drawable.avd_ill_lotus,
        R.drawable.ill_standing to R.drawable.avd_ill_standing,
        R.drawable.ill_edge_bed to R.drawable.avd_ill_edge_bed,
        R.drawable.ill_reverse_cowgirl to R.drawable.avd_ill_reverse_cowgirl,
        R.drawable.ill_butterfly to R.drawable.avd_ill_butterfly,
        R.drawable.ill_scissors to R.drawable.avd_ill_scissors,
        R.drawable.ill_lazy_dog to R.drawable.avd_ill_lazy_dog,
        R.drawable.ill_guide_cover to R.drawable.avd_ill_guide_cover,
        R.drawable.ill_chapter_consent to R.drawable.avd_ill_chapter_consent,
        R.drawable.ill_chapter_connection to R.drawable.avd_ill_chapter_connection,
        R.drawable.ill_chapter_comfort to R.drawable.avd_ill_chapter_comfort,
        R.drawable.ill_chapter_explore to R.drawable.avd_ill_chapter_explore
    )

    fun animatedRes(staticRes: Int): Int = animatedByStatic[staticRes] ?: staticRes
}
