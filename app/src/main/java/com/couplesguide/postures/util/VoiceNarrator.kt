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
            queued.forEach { (text, lang) -> speak(text, lang) }
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
                if (activeUtterances == 0) {
                    onSpeakingChanged(false)
                }
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
        onSpeakingChanged(false)
    }

    fun speak(text: String, language: String): Boolean {
        if (text.isBlank()) return false
        val engine = tts ?: return false
        if (!isReady) {
            pendingSpeech.add(text to language)
            return true
        }

        val appliedLocale = applyLanguage(engine, language) ?: return false
        if (appliedLocale.fallbackUsed) {
            onLanguageIssue?.invoke(appliedLocale.message)
        }

        val chunks = chunkText(text)
        activeUtterances = chunks.size
        chunks.forEachIndexed { index, chunk ->
            val utteranceId = "$UTTERANCE_PREFIX$index"
            val params = Bundle().apply {
                putString(TextToSpeech.Engine.KEY_PARAM_UTTERANCE_ID, utteranceId)
            }
            val queueMode = if (index == 0) TextToSpeech.QUEUE_FLUSH else TextToSpeech.QUEUE_ADD
            engine.speak(chunk, queueMode, params, utteranceId)
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
        val match = voices
            .filter { it.locale.language == locale.language && !it.isNetworkConnectionRequired }
            .maxByOrNull { voiceScore(it) }
        if (match != null) {
            engine.voice = match
        }
    }

    private fun voiceScore(voice: Voice): Int {
        var score = 0
        if (voice.quality >= Voice.QUALITY_HIGH) score += 2
        if (!voice.name.contains("network", ignoreCase = true)) score += 1
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
