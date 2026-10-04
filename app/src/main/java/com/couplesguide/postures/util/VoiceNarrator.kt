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
            preferGoogleEngineIfAvailable()
            attachProgressListener()
        }
        onReadyChanged(isReady)
        if (isReady && pendingSpeech.isNotEmpty()) {
            val queued = pendingSpeech.toList()
            pendingSpeech.clear()
            speakSegments(queued)
        }
    }

    private fun preferGoogleEngineIfAvailable() {
        val engine = tts ?: return
        val google = "com.google.android.tts"
        if (engine.engines.any { it.name == google }) {
            engine.setEngineByPackageName(google)
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
        cleaned.forEachIndexed { segmentIndex, (rawText, language) ->
            val prepared = NaturalLanguageTtsPreparer.prepare(rawText, language)
            val appliedLocale = applyLanguage(engine, language) ?: return@forEachIndexed
            applyNaturalProsody(engine, language)
            if (appliedLocale.fallbackUsed) {
                onLanguageIssue?.invoke(appliedLocale.message)
            }
            val speakText = formatForEngine(engine, prepared)
            val chunks = chunkText(speakText)
            activeUtterances += chunks.size
            chunks.forEachIndexed { chunkIndex, chunk ->
                val utteranceId = "${UTTERANCE_PREFIX}${segmentIndex}_${chunkIndex}"
                val params = Bundle().apply {
                    putString(TextToSpeech.Engine.KEY_PARAM_UTTERANCE_ID, utteranceId)
                    if (engine.voice?.isNetworkConnectionRequired == true) {
                        putString(TextToSpeech.Engine.KEY_FEATURE_NETWORK_SYNTHESIS, "true")
                    }
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

    private fun formatForEngine(engine: TextToSpeech, prepared: String): String {
        return if (supportsSsml(engine)) {
            TtsSsmlBuilder.addNaturalPauses(prepared)
        } else {
            prepared
        }
    }

    private fun supportsSsml(engine: TextToSpeech): Boolean {
        val pkg = engine.defaultEngine ?: return false
        return pkg.contains("google", ignoreCase = true)
    }

    private fun applyNaturalProsody(engine: TextToSpeech, language: String) {
        if (language == LocaleHelper.LANG_UR) {
            engine.setSpeechRate(0.88f)
            engine.setPitch(1.03f)
        } else {
            engine.setSpeechRate(0.93f)
            engine.setPitch(1.0f)
        }
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
                    selectNaturalVoice(engine, locale)
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
                    selectNaturalVoice(engine, Locale.US)
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

    /** Prefer neural / high-quality voices (including network) for human-like lecture delivery. */
    private fun selectNaturalVoice(engine: TextToSpeech, locale: Locale) {
        if (android.os.Build.VERSION.SDK_INT < android.os.Build.VERSION_CODES.LOLLIPOP) return
        val voices = engine.voices ?: return
        val candidates = voices.filter { voice ->
            voice.locale.language.equals(locale.language, ignoreCase = true)
        }
        if (candidates.isEmpty()) return

        val match = candidates.maxByOrNull { voiceScoreNatural(it, locale) }
        if (match != null) {
            engine.voice = match
        }
    }

    private fun voiceMetadataBlob(voice: Voice): String {
        val features = voice.features?.joinToString(" ")?.lowercase().orEmpty()
        return "${voice.name.lowercase()} $features"
    }

    private fun voiceScoreNatural(voice: Voice, preferredLocale: Locale): Int {
        var score = 0
        val blob = voiceMetadataBlob(voice)
        if (NATURAL_VOICE_HINTS.any { blob.contains(it) }) score += 40
        if (blob.contains("network")) score += 12
        if (voice.isNetworkConnectionRequired) score += 8
        if (voice.quality >= Voice.QUALITY_VERY_HIGH) score += 20
        else if (voice.quality >= Voice.QUALITY_HIGH) score += 14
        else if (voice.quality >= Voice.QUALITY_NORMAL) score += 6
        if (voice.locale.country.equals(preferredLocale.country, ignoreCase = true)) score += 5
        if (blob.contains("local") && voice.quality >= Voice.QUALITY_HIGH) score += 4
        if (ROBOTIC_VOICE_HINTS.any { blob.contains(it) }) score -= 18
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

        private val NATURAL_VOICE_HINTS = listOf(
            "neural",
            "wavenet",
            "premium",
            "enhanced",
            "natural",
            "studio",
            "journey",
            "news",
            "casual",
        )

        private val ROBOTIC_VOICE_HINTS = listOf(
            "synthetic",
            "espeak",
            "pico",
            "legacy",
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
