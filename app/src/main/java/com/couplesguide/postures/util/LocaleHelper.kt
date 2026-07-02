package com.couplesguide.postures.util

import android.content.Context
import android.content.res.Configuration
import java.util.Locale

object LocaleHelper {

    const val LANG_UR = "ur"

    fun getLanguage(@Suppress("UNUSED_PARAMETER") context: Context): String = LANG_UR

    fun wrap(context: Context): Context {
        val locale = Locale("ur", "PK")
        Locale.setDefault(locale)
        val config = Configuration(context.resources.configuration)
        config.setLocale(locale)
        config.setLayoutDirection(locale)
        return context.createConfigurationContext(config)
    }

    fun isUrdu(@Suppress("UNUSED_PARAMETER") context: Context): Boolean = true
}
