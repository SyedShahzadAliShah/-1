package com.couplesguide.postures.util

import android.content.Context
import android.content.res.Configuration
import java.util.Locale

object LocaleHelper {

    private const val PREFS = "cs_teacher_prefs"

    /** On-screen text is always English. */
    const val LANG_EN = "en"

    /** Voice narration is always Urdu. */
    const val NARRATION_LANG = "ur"

    @Deprecated("UI is English-only; kept for legacy call sites.")
    const val LANG_UR = "ur"

    fun getLanguage(context: Context): String = LANG_EN

    fun setLanguage(context: Context, language: String) {
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
            .edit()
            .putString("language", LANG_EN)
            .apply()
    }

    fun wrap(context: Context): Context {
        val locale = Locale.ENGLISH
        Locale.setDefault(locale)
        val config = Configuration(context.resources.configuration)
        config.setLocale(locale)
        config.setLayoutDirection(locale)
        return context.createConfigurationContext(config)
    }

    fun isUrdu(context: Context): Boolean = false
}
