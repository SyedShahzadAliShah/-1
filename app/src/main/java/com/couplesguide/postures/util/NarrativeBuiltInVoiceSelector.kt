package com.couplesguide.postures.util

import android.os.Build
import android.speech.tts.TextToSpeech
import android.speech.tts.Voice
import java.util.Locale

/**
 * Narrative TTS uses **built-in** Google/local voices only:
 * - English (India) — Voice 1
 * - Urdu (India) — Voice 1
 */
object NarrativeBuiltInVoiceSelector {

    val LOCALE_ENGLISH_INDIA: Locale = Locale("en", "IN")
    val LOCALE_URDU_INDIA: Locale = Locale("ur", "IN")

    const val NARRATIVE_SPEECH_RATE = 0.92f
    const val NARRATIVE_PITCH = 1.0f

    data class ApplyResult(
        val locale: Locale,
        val voiceApplied: Boolean,
        val message: String
    )

    /** Google TTS ids commonly labelled “English (India) Voice 1” / “Urdu (India) Voice 1” in system UI. */
    private val ENGLISH_INDIA_VOICE1_HINTS = listOf(
        "en-in-x-end-local",
        "en-in-x-enc-local",
        "en-in-x-ena-local",
        "en_in_voice1",
        "voice1",
        "voice-1",
    )

    private val URDU_INDIA_VOICE1_HINTS = listOf(
        "ur-in-x-urd-local",
        "ur-in-x-urb-local",
        "ur_in_voice1",
        "voice1",
        "voice-1",
    )

    fun configureBaseline(engine: TextToSpeech) {
        engine.setSpeechRate(NARRATIVE_SPEECH_RATE)
        engine.setPitch(NARRATIVE_PITCH)
    }

    fun narrativeLanguage(language: String): String =
        if (language == LocaleHelper.LANG_UR) LocaleHelper.LANG_UR else LocaleHelper.LANG_EN

    fun applyForLanguage(engine: TextToSpeech, language: String): ApplyResult? {
        val lang = narrativeLanguage(language)
        val locale = if (lang == LocaleHelper.LANG_UR) LOCALE_URDU_INDIA else LOCALE_ENGLISH_INDIA

        if (!isLocaleReady(engine, locale)) {
            val label = if (lang == LocaleHelper.LANG_UR) "Urdu (India) Voice 1" else "English (India) Voice 1"
            return ApplyResult(
                locale = locale,
                voiceApplied = false,
                message = "Install built-in $label in Google Text-to-speech."
            )
        }

        engine.language = locale
        val voiceApplied = selectBuiltInVoice1(engine, locale)
        return ApplyResult(
            locale = locale,
            voiceApplied = voiceApplied,
            message = if (voiceApplied) {
                ""
            } else {
                val label = if (lang == LocaleHelper.LANG_UR) "Urdu (India) Voice 1" else "English (India) Voice 1"
                "Built-in $label not found. Open Install voice data and download the India Voice 1 pack."
            }
        )
    }

    fun isLocaleReady(engine: TextToSpeech, locale: Locale): Boolean {
        return when (engine.isLanguageAvailable(locale)) {
            TextToSpeech.LANG_AVAILABLE,
            TextToSpeech.LANG_COUNTRY_AVAILABLE,
            TextToSpeech.LANG_COUNTRY_VAR_AVAILABLE -> true
            else -> false
        }
    }

    /**
     * Picks the built-in (on-device) “Voice 1” for [locale]. Never uses network voices.
     */
    fun selectBuiltInVoice1(engine: TextToSpeech, locale: Locale): Boolean {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.LOLLIPOP) return false
        val voices = engine.voices ?: return false
        val builtIn = voices.filter { voice -> isBuiltInVoiceForLocale(voice, locale) }
        if (builtIn.isEmpty()) return false

        val hints = if (locale.language.equals("ur", ignoreCase = true)) {
            URDU_INDIA_VOICE1_HINTS
        } else {
            ENGLISH_INDIA_VOICE1_HINTS
        }

        for (hint in hints) {
            val match = builtIn.firstOrNull { voiceMetadata(it).contains(hint) }
            if (match != null) {
                engine.voice = match
                return true
            }
        }

        val sorted = builtIn.sortedBy { it.name.lowercase() }
        engine.voice = sorted.first()
        return true
    }

    fun hasBuiltInVoice1(engine: TextToSpeech, locale: Locale): Boolean {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.LOLLIPOP) return false
        val voices = engine.voices ?: return false
        return voices.any { isBuiltInVoiceForLocale(it, locale) }
    }

    private fun isBuiltInVoiceForLocale(voice: Voice, locale: Locale): Boolean {
        if (voice.isNetworkConnectionRequired) return false
        val name = voice.name.lowercase()
        if (!name.contains("-local") && !name.contains("_local")) return false
        if (!voice.locale.language.equals(locale.language, ignoreCase = true)) return false
        if (locale.country.isNotEmpty() &&
            !voice.locale.country.equals(locale.country, ignoreCase = true)
        ) {
            return false
        }
        return true
    }

    private fun voiceMetadata(voice: Voice): String {
        val features = voice.features?.joinToString(" ")?.lowercase().orEmpty()
        return "${voice.name.lowercase()} $features"
    }
}
