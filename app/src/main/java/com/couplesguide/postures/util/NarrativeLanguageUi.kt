package com.couplesguide.postures.util

import android.view.View
import com.google.android.material.button.MaterialButton
import com.google.android.material.button.MaterialButtonToggleGroup
import com.couplesguide.postures.R

object NarrativeLanguageUi {

    fun bindToggleGroup(
        group: MaterialButtonToggleGroup,
        btnEnglish: MaterialButton,
        btnUrdu: MaterialButton,
        btnEmbed: MaterialButton,
        onChanged: () -> Unit
    ) {
        val context = group.context
        val mode = NarrativeLanguageHelper.getMode(context)
        val checkedId = when (mode) {
            NarrativeLanguageHelper.MODE_UR -> btnUrdu.id
            NarrativeLanguageHelper.MODE_EN -> btnEnglish.id
            else -> btnEmbed.id
        }
        group.check(checkedId)

        group.addOnButtonCheckedListener { _, checkedId, isChecked ->
            if (!isChecked) return@addOnButtonCheckedListener
            val newMode = when (checkedId) {
                btnEnglish.id -> NarrativeLanguageHelper.MODE_EN
                btnUrdu.id -> NarrativeLanguageHelper.MODE_UR
                btnEmbed.id -> NarrativeLanguageHelper.MODE_EMBED
                else -> return@addOnButtonCheckedListener
            }
            if (newMode != NarrativeLanguageHelper.getMode(context)) {
                NarrativeLanguageHelper.setMode(context, newMode)
                onChanged()
            }
        }
    }

    fun updateBadge(badgeView: View, context: android.content.Context) {
        if (badgeView !is android.widget.TextView) return
        val mode = NarrativeLanguageHelper.getMode(context)
        val label = when (mode) {
            NarrativeLanguageHelper.MODE_UR -> context.getString(R.string.narrative_urdu)
            NarrativeLanguageHelper.MODE_EN -> context.getString(R.string.narrative_english)
            else -> context.getString(R.string.narrative_embed_both)
        }
        badgeView.text = context.getString(R.string.narrative_mode_badge, label)
    }
}
