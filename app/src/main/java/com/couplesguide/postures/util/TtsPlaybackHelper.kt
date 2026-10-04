package com.couplesguide.postures.util

import android.content.Context
import androidx.appcompat.app.AlertDialog
import com.couplesguide.postures.R

object TtsPlaybackHelper {

    fun showPlaybackFailedDialog(context: Context) {
        AlertDialog.Builder(context)
            .setTitle(R.string.listen)
            .setMessage(R.string.voice_install_prompt)
            .setPositiveButton(R.string.voice_open_settings) { _, _ ->
                VoiceNarrator.openTtsSettings(context)
            }
            .setNegativeButton(android.R.string.cancel, null)
            .show()
    }
}
