package com.couplesguide.postures.util

import android.content.Context
import android.content.res.Configuration
import java.util.Locale

object LocaleHelper {

    private const val PREFS = "intimacy_guide_prefs"
    private const val KEY_LANGUAGE = "language"

    const val LANG_EN = "en"
    const val LANG_UR = "ur"

    fun getLanguage(context: Context): String = LANG_UR

    fun setLanguage(context: Context, language: String) {
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
            .edit()
            .putString(KEY_LANGUAGE, LANG_UR)
            .apply()
    }

    fun wrap(context: Context): Context {
        val locale = Locale("ur", "PK")
        Locale.setDefault(locale)
        val config = Configuration(context.resources.configuration)
        config.setLocale(locale)
        config.setLayoutDirection(locale)
        return context.createConfigurationContext(config)
    }

    fun isUrdu(context: Context): Boolean = true
}
