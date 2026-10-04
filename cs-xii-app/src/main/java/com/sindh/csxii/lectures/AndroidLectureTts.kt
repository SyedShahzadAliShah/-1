package com.sindh.csxii.lectures

import android.content.Context
import android.os.Bundle
import android.speech.tts.TextToSpeech
import android.speech.tts.UtteranceProgressListener
import android.webkit.JavascriptInterface
import android.webkit.WebView
import java.util.Locale
import java.util.concurrent.atomic.AtomicInteger

/**
 * Native English/Urdu TTS for WebView (Web Speech API is unreliable on Android WebView).
 */
class AndroidLectureTts(
    context: Context,
    private val webView: WebView,
    private val onReadyChanged: (Boolean) -> Unit
) : TextToSpeech.OnInitListener {

    private val appContext = context.applicationContext
    private var tts: TextToSpeech? = TextToSpeech(appContext, this)
    private var ready = false
    private val utteranceSeq = AtomicInteger(0)
    private var activeUtterances = 0

    override fun onInit(status: Int) {
        ready = status == TextToSpeech.SUCCESS
        if (ready) {
            tts?.setSpeechRate(0.92f)
            attachProgressListener()
        }
        onReadyChanged(ready)
    }

    private fun attachProgressListener() {
        tts?.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
            override fun onStart(utteranceId: String?) = Unit

            override fun onDone(utteranceId: String?) {
                if (utteranceId?.startsWith(UTTERANCE_PREFIX) == true) {
                    activeUtterances = (activeUtterances - 1).coerceAtLeast(0)
                }
                if (activeUtterances == 0) {
                    notifyJsEnd()
                }
            }

            @Deprecated("Deprecated in Java")
            override fun onError(utteranceId: String?) {
                onSpeechError()
            }

            override fun onError(utteranceId: String?, errorCode: Int) {
                onSpeechError()
            }
        })
    }

    private fun onSpeechError() {
        activeUtterances = 0
        notifyJsEnd(true)
    }

    private fun notifyJsEnd(isError: Boolean = false) {
        webView.post {
            val flag = if (isError) "true" else "false"
            webView.evaluateJavascript(
                "window.__lectureNativeTtsDone && window.__lectureNativeTtsDone($flag)",
                null
            )
        }
    }

    fun isReady(): Boolean = ready

    fun speak(text: String, language: String): Boolean {
        if (text.isBlank() || !ready) return false
        val engine = tts ?: return false
        val lang = language.lowercase(Locale.US)
        if (!applyLanguage(engine, lang)) return false

        val chunks = chunkText(text)
        activeUtterances = chunks.size
        chunks.forEachIndexed { index, chunk ->
            val utteranceId = "${UTTERANCE_PREFIX}${utteranceSeq.incrementAndGet()}_$index"
            val params = Bundle().apply {
                putString(TextToSpeech.Engine.KEY_PARAM_UTTERANCE_ID, utteranceId)
            }
            val queueMode = if (index == 0) TextToSpeech.QUEUE_FLUSH else TextToSpeech.QUEUE_ADD
            engine.speak(chunk, queueMode, params, utteranceId)
        }
        return true
    }

    fun stop() {
        activeUtterances = 0
        tts?.stop()
        notifyJsEnd()
    }

    fun shutdown() {
        activeUtterances = 0
        tts?.stop()
        tts?.shutdown()
        tts = null
        ready = false
    }

    private fun applyLanguage(engine: TextToSpeech, language: String): Boolean {
        val locales = if (language == "ur") {
            listOf(Locale("ur", "PK"), Locale("ur", "IN"), Locale("ur"))
        } else {
            listOf(Locale.US, Locale.UK, Locale.ENGLISH)
        }
        for (locale in locales) {
            when (engine.isLanguageAvailable(locale)) {
                TextToSpeech.LANG_AVAILABLE,
                TextToSpeech.LANG_COUNTRY_AVAILABLE,
                TextToSpeech.LANG_COUNTRY_VAR_AVAILABLE -> {
                    engine.language = locale
                    return true
                }
            }
        }
        if (language == "ur") {
            when (engine.isLanguageAvailable(Locale.US)) {
                TextToSpeech.LANG_AVAILABLE,
                TextToSpeech.LANG_COUNTRY_AVAILABLE,
                TextToSpeech.LANG_COUNTRY_VAR_AVAILABLE -> {
                    engine.language = Locale.US
                    return true
                }
            }
        }
        return false
    }

    private fun chunkText(text: String): List<String> {
        val trimmed = text.trim()
        if (trimmed.length <= MAX_CHUNK) return listOf(trimmed)
        val chunks = mutableListOf<String>()
        var remaining = trimmed
        while (remaining.isNotEmpty()) {
            if (remaining.length <= MAX_CHUNK) {
                chunks.add(remaining)
                break
            }
            var splitAt = remaining.lastIndexOf('.', MAX_CHUNK)
            if (splitAt < MAX_CHUNK / 2) splitAt = remaining.lastIndexOf(' ', MAX_CHUNK)
            if (splitAt <= 0) splitAt = MAX_CHUNK
            chunks.add(remaining.substring(0, splitAt + 1).trim())
            remaining = remaining.substring(splitAt + 1).trim()
        }
        return chunks.ifEmpty { listOf(trimmed) }
    }

    inner class JsBridge {
        @JavascriptInterface
        fun isTtsReady(): Boolean = ready

        @JavascriptInterface
        fun speak(text: String, lang: String) {
            webView.post {
                speak(text, lang)
            }
        }

        @JavascriptInterface
        fun stopSpeak() {
            webView.post { stop() }
        }
    }

    companion object {
        private const val MAX_CHUNK = 3200
        private const val UTTERANCE_PREFIX = "lecture_tts_"
    }
}
