package com.couplesguide.postures.util

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.speech.tts.TextToSpeech
import android.speech.tts.UtteranceProgressListener
import android.speech.tts.Voice
import java.util.Locale

class VoiceNarrator(
    private val context: Context,
    private val onReadyChanged: (Boolean) -> Unit,
    private val onSpeakingChanged: (Boolean) -> Unit,
    private val onLanguageIssue: ((String) -> Unit)? = null
) : TextToSpeech.OnInitListener {

    private var tts: TextToSpeech? = null
    private var isReady = false
    private val pendingSpeech = mutableListOf<Pair<String, String>>()
    private var activeUtterances = 0
    private var onSegmentsComplete: (() -> Unit)? = null

    init {
        tts = TextToSpeech(context.applicationContext, this)
    }

    override fun onInit(status: Int) {
        isReady = status == TextToSpeech.SUCCESS
        if (isReady) {
            tts?.setSpeechRate(0.92f)
            tts?.setPitch(1.0f)
            attachProgressListener()
        }
        onReadyChanged(isReady)
        if (isReady && pendingSpeech.isNotEmpty()) {
            val queued = pendingSpeech.toList()
            pendingSpeech.clear()
            speakSegments(queued)
        }
    }

    private fun attachProgressListener() {
        tts?.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
            override fun onStart(utteranceId: String?) {
                onSpeakingChanged(true)
            }

            override fun onDone(utteranceId: String?) {
                if (utteranceId?.startsWith(UTTERANCE_PREFIX) == true) {
                    activeUtterances = (activeUtterances - 1).coerceAtLeast(0)
                }
                notifyIfIdle()
            }

            @Deprecated("Deprecated in Java")
            override fun onError(utteranceId: String?) {
                handleError(utteranceId)
            }

            override fun onError(utteranceId: String?, errorCode: Int) {
                handleError(utteranceId)
            }
        })
    }

    private fun handleError(utteranceId: String?) {
        if (utteranceId?.startsWith(UTTERANCE_PREFIX) == true) {
            activeUtterances = 0
        }
        notifyIfIdle()
    }

    private fun notifyIfIdle() {
        if (activeUtterances == 0) {
            onSpeakingChanged(false)
            val complete = onSegmentsComplete
            onSegmentsComplete = null
            complete?.invoke()
        }
    }

    fun speak(text: String, language: String): Boolean {
        return speakSegments(listOf(text to language))
    }

    /** Queue narration in multiple languages (e.g. embedded English then Urdu). */
    fun speakSegments(segments: List<Pair<String, String>>, onComplete: (() -> Unit)? = null): Boolean {
        val cleaned = segments.mapNotNull { (text, lang) ->
            val t = text.trim()
            if (t.isEmpty()) null else t to lang
        }
        if (cleaned.isEmpty()) {
            onComplete?.invoke()
            return false
        }
        val engine = tts ?: return false
        if (!isReady) {
            pendingSpeech.addAll(cleaned)
            onSegmentsComplete = onComplete
            return true
        }

        onSegmentsComplete = onComplete
        activeUtterances = 0
        cleaned.forEachIndexed { segmentIndex, (text, language) ->
            val appliedLocale = applyLanguage(engine, language) ?: return@forEachIndexed
            if (appliedLocale.fallbackUsed) {
                onLanguageIssue?.invoke(appliedLocale.message)
            }
            val chunks = chunkText(text)
            activeUtterances += chunks.size
            chunks.forEachIndexed { chunkIndex, chunk ->
                val utteranceId = "${UTTERANCE_PREFIX}${segmentIndex}_${chunkIndex}"
                val params = Bundle().apply {
                    putString(TextToSpeech.Engine.KEY_PARAM_UTTERANCE_ID, utteranceId)
                }
                val isFirst = segmentIndex == 0 && chunkIndex == 0
                val queueMode = if (isFirst) TextToSpeech.QUEUE_FLUSH else TextToSpeech.QUEUE_ADD
                engine.speak(chunk, queueMode, params, utteranceId)
            }
        }
        if (activeUtterances == 0) {
            onComplete?.invoke()
            return false
        }
        return true
    }

    private data class LocaleResult(val locale: Locale, val fallbackUsed: Boolean, val message: String)

    private fun applyLanguage(engine: TextToSpeech, language: String): LocaleResult? {
        val candidates = if (language == LocaleHelper.LANG_UR) {
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
                    selectBestVoice(engine, locale)
                    return LocaleResult(locale, false, "")
                }
            }
        }

        if (language == LocaleHelper.LANG_UR) {
            when (engine.isLanguageAvailable(Locale.US)) {
                TextToSpeech.LANG_AVAILABLE,
                TextToSpeech.LANG_COUNTRY_AVAILABLE,
                TextToSpeech.LANG_COUNTRY_VAR_AVAILABLE -> {
                    engine.language = Locale.US
                    selectBestVoice(engine, Locale.US)
                    return LocaleResult(
                        Locale.US,
                        true,
                        "Urdu voice not installed. Using English narration."
                    )
                }
            }
        }

        onLanguageIssue?.invoke("Voice language not available on this device.")
        return null
    }

    private fun selectBestVoice(engine: TextToSpeech, locale: Locale) {
        if (android.os.Build.VERSION.SDK_INT < android.os.Build.VERSION_CODES.LOLLIPOP) return
        val voices = engine.voices ?: return
        val candidates = voices.filter { voice ->
            voice.locale.language.equals(locale.language, ignoreCase = true) &&
                !voice.isNetworkConnectionRequired
        }
        if (candidates.isEmpty()) return

        val maleCandidates = candidates.filter { isMaleVoice(it) && !isFemaleVoice(it) }
        val nonFemale = candidates.filter { !isFemaleVoice(it) }
        val pool = when {
            maleCandidates.isNotEmpty() -> maleCandidates
            nonFemale.isNotEmpty() -> nonFemale
            else -> candidates
        }

        val match = pool.maxByOrNull { voiceScore(it, locale) }
        if (match != null) {
            engine.voice = match
        }
    }

    /** Prefer embedded male voices for teacher-style English / Urdu narration. */
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

    private fun chunkText(text: String): List<String> {
        if (text.length <= MAX_CHUNK) return listOf(text)
        val chunks = mutableListOf<String>()
        var remaining = text.trim()
        while (remaining.isNotEmpty()) {
            if (remaining.length <= MAX_CHUNK) {
                chunks.add(remaining)
                break
            }
            var splitAt = remaining.lastIndexOf('.', MAX_CHUNK)
            if (splitAt < MAX_CHUNK / 2) {
                splitAt = remaining.lastIndexOf(' ', MAX_CHUNK)
            }
            if (splitAt <= 0) splitAt = MAX_CHUNK
            chunks.add(remaining.substring(0, splitAt + 1).trim())
            remaining = remaining.substring(splitAt + 1).trim()
        }
        return chunks.ifEmpty { listOf(text) }
    }

    fun stop() {
        pendingSpeech.clear()
        activeUtterances = 0
        onSegmentsComplete = null
        tts?.stop()
        onSpeakingChanged(false)
    }

    fun isSpeaking(): Boolean = tts?.isSpeaking == true

    fun shutdown() {
        pendingSpeech.clear()
        activeUtterances = 0
        tts?.stop()
        tts?.shutdown()
        tts = null
        isReady = false
    }

    companion object {
        private const val MAX_CHUNK = 3200
        private const val UTTERANCE_PREFIX = "narration_"

        /** Substrings common in Android TTS voice ids (especially Google) for male voices. */
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
        )

        fun openTtsSettings(context: Context) {
            val intents = listOf(
                Intent(TextToSpeech.Engine.ACTION_INSTALL_TTS_DATA),
                Intent("com.android.settings.TTS_SETTINGS"),
                Intent(android.provider.Settings.ACTION_SETTINGS)
            )
            for (intent in intents) {
                if (intent.resolveActivity(context.packageManager) != null) {
                    intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                    context.startActivity(intent)
                    return
                }
            }
        }
    }
}
