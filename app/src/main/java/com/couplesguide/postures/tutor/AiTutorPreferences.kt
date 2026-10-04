package com.couplesguide.postures.tutor

import android.content.Context

object AiTutorPreferences {

    private const val PREFS = "ai_tutor_prefs"
    private const val KEY_GEMINI = "gemini_api_key"
    private const val KEY_USE_CLOUD = "use_cloud_tutor"

    fun getGeminiApiKey(context: Context): String? =
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
            .getString(KEY_GEMINI, null)
            ?.trim()
            ?.takeIf { it.isNotEmpty() }

    fun setGeminiApiKey(context: Context, key: String?) {
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
            .edit()
            .putString(KEY_GEMINI, key?.trim())
            .apply()
    }

    fun isCloudEnabled(context: Context): Boolean =
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
            .getBoolean(KEY_USE_CLOUD, false)

    fun setCloudEnabled(context: Context, enabled: Boolean) {
        context.getSharedPreferences(PREFS, Context.MODE_PRIVATE)
            .edit()
            .putBoolean(KEY_USE_CLOUD, enabled)
            .apply()
    }
}
