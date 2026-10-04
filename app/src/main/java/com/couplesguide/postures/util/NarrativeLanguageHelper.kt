package com.couplesguide.postures.util

import android.content.Context

/**
 * Controls which language(s) are used for voice narration and embedded lecture captions,
 * independent of the app UI locale.
 */
object NarrativeLanguageHelper {

    private const val PREFS = "intimacy_guide_prefs"
    private const val KEY_NARRATIVE_MODE = "narrative_language_mode"

    /** English narration / caption only */
    const val MODE_EN = "en"

    /** Urdu narration / caption only */
    const val MODE_UR = "ur"

    /** @deprecated Use English or Urdu only; legacy value maps to English TTS. */
    const val MODE_EMBED = "embed"

    fun getMode(context: Context): String {
        val prefs = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
        val stored = prefs.getString(KEY_NARRATIVE_MODE, MODE_EN) ?: MODE_EN
        return if (stored == MODE_EMBED) MODE_EN else stored
    }

    fun setMode(context: Context, mode: String) {
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
            .edit()
            .putString(KEY_NARRATIVE_MODE, mode)
            .apply()
    }

    fun ttsLanguageForMode(mode: String): String =
        if (mode == MODE_UR) LocaleHelper.LANG_UR else LocaleHelper.LANG_EN
}
