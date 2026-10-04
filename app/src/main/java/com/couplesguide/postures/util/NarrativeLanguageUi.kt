package com.couplesguide.postures.util

import android.view.View
import android.widget.TextView
import com.google.android.material.button.MaterialButton
import com.google.android.material.button.MaterialButtonToggleGroup
import com.couplesguide.postures.R

object NarrativeLanguageUi {

    fun bindToggleGroup(
        group: MaterialButtonToggleGroup,
        btnEnglish: MaterialButton,
        btnUrdu: MaterialButton,
        onChanged: () -> Unit
    ) {
        val context = group.context
        val mode = NarrativeLanguageHelper.getMode(context)
        group.check(
            if (mode == NarrativeLanguageHelper.MODE_UR) btnUrdu.id else btnEnglish.id
        )

        group.addOnButtonCheckedListener { _, checkedId, isChecked ->
            if (!isChecked) return@addOnButtonCheckedListener
            val newMode = when (checkedId) {
                btnEnglish.id -> NarrativeLanguageHelper.MODE_EN
                btnUrdu.id -> NarrativeLanguageHelper.MODE_UR
                else -> return@addOnButtonCheckedListener
            }
            if (newMode != NarrativeLanguageHelper.getMode(context)) {
                NarrativeLanguageHelper.setMode(context, newMode)
                onChanged()
            }
        }
    }

    fun updateBadge(badgeView: View, context: android.content.Context) {
        if (badgeView !is TextView) return
        val mode = NarrativeLanguageHelper.getMode(context)
        val label = if (mode == NarrativeLanguageHelper.MODE_UR) {
            context.getString(R.string.narrative_urdu)
        } else {
            context.getString(R.string.narrative_english)
        }
        badgeView.text = context.getString(R.string.embed_tts_engine_badge, label)
    }
}
