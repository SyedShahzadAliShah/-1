package com.pakrecipes.cooking.util

import android.content.Context
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
    private val pendingSpeech = mutableListOf<String>()
    private var activeUtterances = 0

    init {
        tts = TextToSpeech(context.applicationContext, this)
    }

    override fun onInit(status: Int) {
        isReady = status == TextToSpeech.SUCCESS
        if (isReady) {
            tts?.setSpeechRate(0.88f)
            tts?.setPitch(1.0f)
            attachProgressListener()
        }
        onReadyChanged(isReady)
        if (isReady && pendingSpeech.isNotEmpty()) {
            val queued = pendingSpeech.toList()
            pendingSpeech.clear()
            queued.forEach { speak(it) }
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
                if (activeUtterances == 0) onSpeakingChanged(false)
            }

            @Deprecated("Deprecated in Java")
            override fun onError(utteranceId: String?) {
                handleError()
            }

            override fun onError(utteranceId: String?, errorCode: Int) {
                handleError()
            }
        })
    }

    private fun handleError() {
        activeUtterances = 0
        onSpeakingChanged(false)
    }

    fun speak(text: String): Boolean {
        if (text.isBlank()) return false
        val engine = tts ?: return false
        if (!isReady) {
            pendingSpeech.add(text)
            return true
        }

        val locale = applyUrduLocale(engine) ?: return false
        if (locale.fallbackUsed) {
            onLanguageIssue?.invoke("اردو آواز دستیاب نہیں۔ انگریزی میں سنا رہے ہیں۔")
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

    private data class LocaleResult(val locale: Locale, val fallbackUsed: Boolean)

    private fun applyUrduLocale(engine: TextToSpeech): LocaleResult? {
        val candidates = listOf(Locale("ur", "PK"), Locale("ur", "IN"), Locale("ur"))
        for (locale in candidates) {
            val result = engine.isLanguageAvailable(locale)
            if (result >= TextToSpeech.LANG_AVAILABLE) {
                engine.language = locale
                selectBestVoice(engine, locale)
                return LocaleResult(locale, false)
            }
        }
        // Fallback to English
        val en = Locale.US
        if (engine.isLanguageAvailable(en) >= TextToSpeech.LANG_AVAILABLE) {
            engine.language = en
            return LocaleResult(en, true)
        }
        onLanguageIssue?.invoke("آواز کا نظام دستیاب نہیں ہے۔")
        return null
    }

    private fun selectBestVoice(engine: TextToSpeech, locale: Locale) {
        val voices = engine.voices ?: return
        val match = voices
            .filter { it.locale.language == locale.language && !it.isNetworkConnectionRequired }
            .maxByOrNull { if (it.quality >= Voice.QUALITY_HIGH) 2 else 1 }
        if (match != null) engine.voice = match
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
            var splitAt = remaining.lastIndexOf('۔', MAX_CHUNK)
            if (splitAt < MAX_CHUNK / 2) splitAt = remaining.lastIndexOf(' ', MAX_CHUNK)
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
        private const val UTTERANCE_PREFIX = "recipe_narration_"
    }
}
