package com.couplesguide.postures.util

import android.os.Build
import android.speech.tts.TextToSpeech
import android.speech.tts.Voice
import java.util.Locale

/**
 * Selects embedded **male** TTS voices for narrative playback (English or Urdu only).
 */
object NarrativeMaleVoiceSelector {

    const val MALE_SPEECH_RATE = 0.92f
    const val MALE_PITCH = 0.90f
    private const val FALLBACK_MALE_PITCH = 0.82f

    data class ApplyResult(
        val locale: Locale,
        val fallbackUsed: Boolean,
        val message: String,
        val maleVoiceConfirmed: Boolean
    )

    fun configureBaseline(engine: TextToSpeech) {
        engine.setSpeechRate(MALE_SPEECH_RATE)
        engine.setPitch(MALE_PITCH)
    }

    /** Maps narrative language to TTS locale; only English and Urdu are supported. */
    fun narrativeLanguage(language: String): String =
        if (language == LocaleHelper.LANG_UR) LocaleHelper.LANG_UR else LocaleHelper.LANG_EN

    fun applyForLanguage(engine: TextToSpeech, language: String): ApplyResult? {
        val lang = narrativeLanguage(language)
        val candidates = if (lang == LocaleHelper.LANG_UR) {
            listOf(Locale("ur", "PK"), Locale("ur", "IN"), Locale("ur"))
        } else {
            listOf(Locale.US, Locale.UK, Locale.ENGLISH)
        }

        for (locale in candidates) {
            when (engine.isLanguageAvailable(locale)) {
                TextToSpeech.LANG_AVAILABLE,
                TextToSpeech.LANG_COUNTRY_AVAILABLE,
                TextToSpeech.LANG_COUNTRY_VAR_AVAILABLE -> {
                    engine.language = locale
                    val maleConfirmed = selectMaleVoice(engine, locale)
                    engine.setPitch(if (maleConfirmed) MALE_PITCH else FALLBACK_MALE_PITCH)
                    return ApplyResult(locale, fallbackUsed = false, message = "", maleVoiceConfirmed = maleConfirmed)
                }
            }
        }

        if (lang == LocaleHelper.LANG_UR) {
            when (engine.isLanguageAvailable(Locale.US)) {
                TextToSpeech.LANG_AVAILABLE,
                TextToSpeech.LANG_COUNTRY_AVAILABLE,
                TextToSpeech.LANG_COUNTRY_VAR_AVAILABLE -> {
                    engine.language = Locale.US
                    val maleConfirmed = selectMaleVoice(engine, Locale.US)
                    engine.setPitch(if (maleConfirmed) MALE_PITCH else FALLBACK_MALE_PITCH)
                    return ApplyResult(
                        Locale.US,
                        fallbackUsed = true,
                        message = "Urdu voice not installed. Using English male narration.",
                        maleVoiceConfirmed = maleConfirmed
                    )
                }
            }
        }

        return null
    }

    /**
     * Picks the best local male voice for [locale]. Returns true when voice id matches male hints.
     * Never intentionally selects a female-labelled voice.
     */
    fun selectMaleVoice(engine: TextToSpeech, locale: Locale): Boolean {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.LOLLIPOP) return false
        val voices = engine.voices ?: return false
        val candidates = voices.filter { voice ->
            voice.locale.language.equals(locale.language, ignoreCase = true) &&
                !voice.isNetworkConnectionRequired
        }
        if (candidates.isEmpty()) return false

        val maleCandidates = candidates.filter { isMaleVoice(it) && !isFemaleVoice(it) }
        val nonFemale = candidates.filter { !isFemaleVoice(it) }
        val pool = when {
            maleCandidates.isNotEmpty() -> maleCandidates
            nonFemale.isNotEmpty() -> nonFemale
            else -> emptyList()
        }
        if (pool.isEmpty()) return false

        val match = pool.maxByOrNull { voiceScore(it, locale) } ?: return false
        engine.voice = match
        return isMaleVoice(match)
    }

    private fun isMaleVoice(voice: Voice): Boolean {
        val blob = voiceMetadataBlob(voice)
        if (isFemaleVoice(voice)) return false
        return MALE_VOICE_HINTS.any { hint -> blob.contains(hint) }
    }

    private fun isFemaleVoice(voice: Voice): Boolean {
        val blob = voiceMetadataBlob(voice)
        return FEMALE_VOICE_HINTS.any { hint -> blob.contains(hint) }
    }

    private fun voiceMetadataBlob(voice: Voice): String {
        val features = voice.features?.joinToString(" ")?.lowercase().orEmpty()
        return "${voice.name.lowercase()} $features"
    }

    private fun voiceScore(voice: Voice, preferredLocale: Locale): Int {
        var score = 0
        val blob = voiceMetadataBlob(voice)
        if (MALE_VOICE_HINTS.any { blob.contains(it) }) score += 24
        if (voice.quality >= Voice.QUALITY_HIGH) score += 4
        else if (voice.quality >= Voice.QUALITY_NORMAL) score += 2
        if (voice.locale.country.equals(preferredLocale.country, ignoreCase = true)) score += 3
        if (blob.contains("local")) score += 2
        if (blob.contains("network")) score -= 6
        return score
    }

    private val MALE_VOICE_HINTS = listOf(
        "male",
        "masculine",
        "-male",
        "_male",
        "-m-",
        "_m_",
        " man",
        "gbb",
        "iob",
        "iom",
        "iol",
        "aed",
        "afg",
        "cmb",
        "cmn-local",
    )

    private val FEMALE_VOICE_HINTS = listOf(
        "female",
        "feminine",
        "-female",
        "_female",
        "-f-",
        "_f_",
        " woman",
        " girl",
        "gba",
        "tpc",
        "iob-f",
        "cfn",
        "cfm",
        "cfa",
        "iog",
    )
}
