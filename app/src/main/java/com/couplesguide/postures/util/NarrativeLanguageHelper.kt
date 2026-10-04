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

    /** Urdu narration only */
    const val MODE_UR = "ur"

    /** English then Urdu narration (per page / segment) */
    const val MODE_BOTH = "both"

    /** Legacy alias for [MODE_BOTH] */
    const val MODE_EMBED = "embed"

    fun getMode(context: Context): String {
        val prefs = context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
        val stored = prefs.getString(KEY_NARRATIVE_MODE, MODE_BOTH) ?: MODE_BOTH
        return when (stored) {
            MODE_EMBED -> MODE_BOTH
            MODE_EN, MODE_UR, MODE_BOTH -> stored
            else -> MODE_BOTH
        }
    }

    fun setMode(context: Context, mode: String) {
        val normalized = when (mode) {
            MODE_EMBED -> MODE_BOTH
            MODE_EN, MODE_UR, MODE_BOTH -> mode
            else -> MODE_BOTH
        }
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
            .edit()
            .putString(KEY_NARRATIVE_MODE, normalized)
            .apply()
    }

    fun usesBothLanguages(mode: String): Boolean =
        mode == MODE_BOTH || mode == MODE_EMBED

    fun ttsLanguageForMode(mode: String): String =
        if (mode == MODE_UR) LocaleHelper.LANG_UR else LocaleHelper.LANG_EN
}
