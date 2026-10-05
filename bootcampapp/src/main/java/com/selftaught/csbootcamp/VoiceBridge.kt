package com.selftaught.csbootcamp

import android.os.Handler
import android.os.Looper
import android.speech.tts.TextToSpeech
import android.speech.tts.UtteranceProgressListener
import android.webkit.JavascriptInterface
import android.webkit.WebView
import java.util.Locale

class VoiceBridge(
    private val webView: WebView,
    private val tts: TextToSpeech
) {
    private val main = Handler(Looper.getMainLooper())

    @Volatile
    private var ready = false

    @Volatile
    private var failed = false

    @Volatile
    private var englishReady = false

    @Volatile
    private var urduReady = false

    private var pendingId: String? = null
    private var pendingText: String? = null
    private var pendingLang: String? = null
    private var pendingRate: Float = 1f

    fun onEngineReady(success: Boolean) {
        if (!success) {
            failed = true
            val id = pendingId
            pendingId = null
            if (id != null) notifyDone(id)
            return
        }
        englishReady = tts.isLanguageAvailable(Locale.US) >= TextToSpeech.LANG_AVAILABLE ||
            tts.isLanguageAvailable(Locale.ENGLISH) >= TextToSpeech.LANG_AVAILABLE
        urduReady = tts.isLanguageAvailable(Locale("ur", "PK")) >= TextToSpeech.LANG_AVAILABLE ||
            tts.isLanguageAvailable(Locale("ur")) >= TextToSpeech.LANG_AVAILABLE
        tts.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
            override fun onStart(utteranceId: String?) {
                if (utteranceId != null) notifyStart(utteranceId)
            }

            override fun onDone(utteranceId: String?) {
                if (utteranceId != null) notifyDone(utteranceId)
            }

            @Deprecated("Deprecated in Java")
            override fun onError(utteranceId: String?) {
                if (utteranceId != null) notifyDone(utteranceId)
            }

            override fun onError(utteranceId: String?, errorCode: Int) {
                if (utteranceId != null) notifyDone(utteranceId)
            }
        })
        ready = true
        val id = pendingId
        val text = pendingText
        val lang = pendingLang
        if (id != null && text != null && lang != null) {
            pendingId = null
            pendingText = null
            pendingLang = null
            speakNow(id, text, lang, pendingRate)
        }
    }

    @JavascriptInterface
    fun hasLanguage(lang: String): Boolean {
        return if (lang == "ur") urduReady else englishReady || ready
    }

    @JavascriptInterface
    fun speak(id: String, text: String, lang: String, rate: Double): Boolean {
        if (failed || text.isBlank()) return false
        val speechRate = rate.toFloat().coerceIn(0.7f, 1.6f)
        if (!ready) {
            pendingId = id
            pendingText = text
            pendingLang = lang
            pendingRate = speechRate
            return true
        }
        main.post { speakNow(id, text, lang, speechRate) }
        return true
    }

    @JavascriptInterface
    fun stop() {
        main.post {
            pendingId = null
            pendingText = null
            pendingLang = null
            tts.stop()
        }
    }

    private fun speakNow(id: String, text: String, lang: String, rate: Float) {
        val locale = if (lang == "ur" && urduReady) Locale("ur", "PK") else Locale.US
        val availability = tts.setLanguage(locale)
        if (availability == TextToSpeech.LANG_MISSING_DATA || availability == TextToSpeech.LANG_NOT_SUPPORTED) {
            tts.setLanguage(Locale.US)
        }
        tts.setSpeechRate(rate)
        val queued = tts.speak(text, TextToSpeech.QUEUE_FLUSH, null, id)
        if (queued == TextToSpeech.ERROR) notifyDone(id)
    }

    private fun notifyStart(id: String) {
        webView.post {
            webView.evaluateJavascript("window.__bootcampOnStart && window.__bootcampOnStart(${jsString(id)})", null)
        }
    }

    private fun notifyDone(id: String) {
        webView.post {
            webView.evaluateJavascript("window.__bootcampOnDone && window.__bootcampOnDone(${jsString(id)})", null)
        }
    }

    private fun jsString(value: String): String {
        val escaped = value.replace("\\", "\\\\").replace("'", "\\'")
        return "'$escaped'"
    }
}
