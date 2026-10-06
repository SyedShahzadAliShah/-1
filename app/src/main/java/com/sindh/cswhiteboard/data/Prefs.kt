package com.sindh.cswhiteboard.data

import android.content.Context
import android.content.res.Configuration
import java.util.Locale

object Prefs {
    private const val NAME = "cs_whiteboard_prefs"
    const val LANG_EN = "en"
    const val LANG_UR = "ur"

    private fun sp(context: Context) =
        context.getSharedPreferences(NAME, Context.MODE_PRIVATE)

    fun language(context: Context): String =
        sp(context).getString("language", LANG_EN) ?: LANG_EN

    fun setLanguage(context: Context, language: String) {
        sp(context).edit().putString("language", language).apply()
    }

    fun isUrdu(context: Context): Boolean = language(context) == LANG_UR

    fun wrap(context: Context): Context {
        val locale = if (isUrdu(context)) Locale("ur", "PK") else Locale.ENGLISH
        Locale.setDefault(locale)
        val config = Configuration(context.resources.configuration)
        config.setLocale(locale)
        config.setLayoutDirection(locale)
        return context.createConfigurationContext(config)
    }

    fun markDone(context: Context, lectureId: String) {
        val set = doneIds(context).toMutableSet()
        set.add(lectureId)
        sp(context).edit().putStringSet("done", set).apply()
    }

    fun isDone(context: Context, lectureId: String): Boolean =
        doneIds(context).contains(lectureId)

    fun doneIds(context: Context): Set<String> =
        sp(context).getStringSet("done", emptySet()) ?: emptySet()

    fun goldenOnly(context: Context): Boolean = sp(context).getBoolean("golden_only", false)

    fun setGoldenOnly(context: Context, value: Boolean) {
        sp(context).edit().putBoolean("golden_only", value).apply()
    }

    fun speechRate(context: Context): Float = sp(context).getFloat("speech_rate", 0.92f)

    fun setSpeechRate(context: Context, rate: Float) {
        sp(context).edit().putFloat("speech_rate", rate).apply()
    }
}
