package com.couplesguide.postures.util

import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import com.couplesguide.postures.R

object NarrativeLanguageDialog {

    fun show(
        activity: AppCompatActivity,
        onChanged: (() -> Unit)? = null
    ) {
        val options = arrayOf(
            activity.getString(R.string.narrative_english),
            activity.getString(R.string.narrative_urdu),
            activity.getString(R.string.narrative_embed_both)
        )
        val modes = arrayOf(
            NarrativeLanguageHelper.MODE_EN,
            NarrativeLanguageHelper.MODE_UR,
            NarrativeLanguageHelper.MODE_EMBED
        )
        val currentMode = NarrativeLanguageHelper.getMode(activity)
        val currentIndex = modes.indexOf(currentMode).coerceAtLeast(0)

        AlertDialog.Builder(activity)
            .setTitle(R.string.narrative_language_title)
            .setSingleChoiceItems(options, currentIndex) { dialog, which ->
                val newMode = modes[which]
                if (newMode != currentMode) {
                    NarrativeLanguageHelper.setMode(activity, newMode)
                    onChanged?.invoke()
                }
                dialog.dismiss()
            }
            .show()
    }
}
