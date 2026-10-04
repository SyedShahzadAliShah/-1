package com.couplesguide.postures.util

import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.os.Bundle
import android.speech.tts.TextToSpeech
import android.speech.tts.UtteranceProgressListener
import android.speech.tts.Voice
import android.util.Log
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
    private var useSsml = true
    private var usedGoogleEngine = false
    private var retriedDefaultEngine = false

    init {
        val appContext = context.applicationContext
        usedGoogleEngine = hasGoogleTts(appContext)
        tts = if (usedGoogleEngine) {
            TextToSpeech(appContext, this, GOOGLE_TTS_PACKAGE)
        } else {
            TextToSpeech(appContext, this)
        }
    }

    private fun hasGoogleTts(appContext: Context): Boolean {
        return try {
            appContext.packageManager.getPackageInfo(GOOGLE_TTS_PACKAGE, 0)
            true
        } catch (_: PackageManager.NameNotFoundException) {
            false
        }
    }

    override fun onInit(status: Int) {
        if (status != TextToSpeech.SUCCESS && usedGoogleEngine && !retriedDefaultEngine) {
            Log.w(TAG, "Google TTS init failed; falling back to default engine")
            retriedDefaultEngine = true
            usedGoogleEngine = false
            tts?.shutdown()
            tts = TextToSpeech(context.applicationContext, this)
            return
        }
        isReady = status == TextToSpeech.SUCCESS
        if (!isReady) {
            Log.w(TAG, "TTS onInit failed status=$status")
        } else {
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
                Log.w(TAG, "TTS utterance error id=$utteranceId code=$errorCode")
                handleError(utteranceId)
            }
        })
    }

    private fun handleError(utteranceId: String?) {
        if (utteranceId?.startsWith(UTTERANCE_PREFIX) == true) {
            activeUtterances = (activeUtterances - 1).coerceAtLeast(0)
            if (useSsml) {
                useSsml = false
                Log.w(TAG, "Disabling SSML after TTS error; retry with plain text on next speak")
            }
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

    fun speakSegments(segments: List<Pair<String, String>>, onComplete: (() -> Unit)? = null): Boolean {
        val cleaned = segments.mapNotNull { (text, lang) ->
            val t = text.trim()
            if (t.isEmpty()) null else t to lang
        }
        if (cleaned.isEmpty()) {
            onComplete?.invoke()
            return false
        }
        val engine = tts
        if (engine == null) return false
        if (!isReady) {
            pendingSpeech.addAll(cleaned)
            onSegmentsComplete = onComplete
            return true
        }

        onSegmentsComplete = onComplete
        activeUtterances = 0
        var queuedAny = false

        cleaned.forEachIndexed { segmentIndex, (rawText, language) ->
            val prepared = NaturalLanguageTtsPreparer.prepare(rawText, language)
            if (prepared.isBlank()) return@forEachIndexed

            val appliedLocale = applyLanguage(engine, language)
            if (appliedLocale == null) return@forEachIndexed

            applyNaturalProsody(engine, language)
            if (appliedLocale.fallbackUsed) {
                onLanguageIssue?.invoke(appliedLocale.message)
            }

            val chunks = chunksForSpeech(engine, prepared)
            chunks.forEachIndexed { chunkIndex, chunk ->
                val utteranceId = "${UTTERANCE_PREFIX}${segmentIndex}_${chunkIndex}"
                val params = Bundle().apply {
                    putString(TextToSpeech.Engine.KEY_PARAM_UTTERANCE_ID, utteranceId)
                }
                val isFirst = !queuedAny
                val queueMode = if (isFirst) TextToSpeech.QUEUE_FLUSH else TextToSpeech.QUEUE_ADD
                val spoken = speakChunk(engine, chunk.spoken, chunk.plain, queueMode, params, utteranceId)
                if (spoken) {
                    activeUtterances++
                    queuedAny = true
                }
            }
        }

        if (!queuedAny || activeUtterances == 0) {
            onSegmentsComplete = null
            onComplete?.invoke()
            return false
        }
        return true
    }

    private fun speakChunk(
        engine: TextToSpeech,
        spoken: String,
        plainChunk: String,
        queueMode: Int,
        params: Bundle,
        utteranceId: String
    ): Boolean {
        var code = engine.speak(spoken, queueMode, params, utteranceId)
        if (code != TextToSpeech.ERROR) return true

        if (spoken != plainChunk) {
            useSsml = false
            code = engine.speak(plainChunk, queueMode, params, utteranceId)
            if (code != TextToSpeech.ERROR) return true
        }

        Log.e(TAG, "speak() ERROR for utterance $utteranceId")
        return false
    }

    private data class SpeechChunk(val plain: String, val spoken: String)

    /** Chunk plain text first, then optionally wrap each chunk in SSML (never split SSML tags). */
    private fun chunksForSpeech(engine: TextToSpeech, prepared: String): List<SpeechChunk> {
        val plainChunks = chunkText(prepared)
        val ssmlOk = useSsml && supportsSsml(engine)
        return plainChunks.map { plain ->
            val spoken = if (ssmlOk) TtsSsmlBuilder.addNaturalPauses(plain) else plain
            SpeechChunk(plain, spoken)
        }
    }

    private fun supportsSsml(engine: TextToSpeech): Boolean {
        val pkg = engine.defaultEngine ?: return false
        return pkg.contains("google", ignoreCase = true)
    }

    private fun applyNaturalProsody(engine: TextToSpeech, language: String) {
        if (language == LocaleHelper.LANG_UR) {
            engine.setSpeechRate(0.90f)
            engine.setPitch(1.02f)
        } else {
            engine.setSpeechRate(0.94f)
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
                    selectReliableNaturalVoice(engine, locale)
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
                    selectReliableNaturalVoice(engine, Locale.US)
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

    /**
     * Prefer high-quality voices but keep offline-capable voices ahead of network-only
     * so narration works without connectivity.
     */
    private fun selectReliableNaturalVoice(engine: TextToSpeech, locale: Locale) {
        if (android.os.Build.VERSION.SDK_INT < android.os.Build.VERSION_CODES.LOLLIPOP) return
        val voices = engine.voices ?: return
        val candidates = voices.filter { voice ->
            voice.locale.language.equals(locale.language, ignoreCase = true)
        }
        if (candidates.isEmpty()) return

        val ranked = candidates
            .map { it to voiceScoreReliable(it, locale) }
            .sortedByDescending { it.second }

        for ((voice, _) in ranked) {
            if (engine.setVoice(voice) != TextToSpeech.ERROR) {
                return
            }
        }
    }

    private fun voiceMetadataBlob(voice: Voice): String {
        val features = voice.features?.joinToString(" ")?.lowercase().orEmpty()
        return "${voice.name.lowercase()} $features"
    }

    private fun voiceScoreReliable(voice: Voice, preferredLocale: Locale): Int {
        var score = 0
        val blob = voiceMetadataBlob(voice)
        if (!voice.isNetworkConnectionRequired) score += 28
        if (NATURAL_VOICE_HINTS.any { blob.contains(it) }) score += 22
        if (voice.quality >= Voice.QUALITY_VERY_HIGH) score += 16
        else if (voice.quality >= Voice.QUALITY_HIGH) score += 12
        else if (voice.quality >= Voice.QUALITY_NORMAL) score += 6
        if (voice.locale.country.equals(preferredLocale.country, ignoreCase = true)) score += 5
        if (voice.isNetworkConnectionRequired) score += 4
        if (ROBOTIC_VOICE_HINTS.any { blob.contains(it) }) score -= 20
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
        private const val TAG = "VoiceNarrator"
        private const val GOOGLE_TTS_PACKAGE = "com.google.android.tts"
        private const val MAX_CHUNK = 3200
        private const val UTTERANCE_PREFIX = "narration_"

        private val NATURAL_VOICE_HINTS = listOf(
            "neural",
            "wavenet",
            "premium",
            "enhanced",
            "natural",
            "local",
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
