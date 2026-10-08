package com.teachyourself.sketchnotes

import android.content.Context
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.speech.tts.TextToSpeech
import android.speech.tts.UtteranceProgressListener
import android.webkit.JavascriptInterface
import android.webkit.WebView
import org.json.JSONArray
import org.json.JSONObject
import java.util.Locale
import java.util.concurrent.atomic.AtomicInteger

class UrdishTts(
    context: Context,
    private val webView: WebView
) : TextToSpeech.OnInitListener {

    private val main = Handler(Looper.getMainLooper())
    private val engine = TextToSpeech(context.applicationContext, this)
    private val generation = AtomicInteger(0)
    @Volatile private var ready = false
    private var queue: List<Segment> = emptyList()
    private var index = 0

    data class Segment(val lang: String, val text: String)

    override fun onInit(status: Int) {
        ready = status == TextToSpeech.SUCCESS
        if (ready) {
            engine.setSpeechRate(0.94f)
            engine.setPitch(1.0f)
            engine.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
                override fun onStart(utteranceId: String?) {
                    val current = queue.getOrNull(index)
                    if (current != null) {
                        val payload = JSONObject()
                            .put("l", current.lang)
                            .put("t", current.text)
                            .toString()
                        emit("start", payload)
                    }
                }
                override fun onDone(utteranceId: String?) {
                    if (utteranceId?.startsWith(PREFIX) != true) return
                    index += 1
                    if (index < queue.size) {
                        speakIndex(index)
                    } else {
                        emit("done", "")
                    }
                }
                @Deprecated("Deprecated in Java")
                override fun onError(utteranceId: String?) {
                    emit("error", "tts")
                }
                override fun onError(utteranceId: String?, errorCode: Int) {
                    emit("error", "tts-$errorCode")
                }
            })
        } else {
            emit("error", "init")
        }
    }

    @JavascriptInterface
    fun speakUrdish(json: String) {
        val segments = parse(json)
        main.post {
            generation.incrementAndGet()
            engine.stop()
            queue = segments.filter { it.text.isNotBlank() }
            index = 0
            if (!ready) {
                emit("issue", "Voice engine not ready")
                return@post
            }
            if (queue.isEmpty()) {
                emit("done", "")
                return@post
            }
            speakIndex(0)
        }
    }

    @JavascriptInterface
    fun stop() {
        main.post {
            generation.incrementAndGet()
            queue = emptyList()
            index = 0
            engine.stop()
            emit("done", "")
        }
    }

    private fun speakIndex(at: Int) {
        val seg = queue.getOrNull(at) ?: return
        applyLanguage(seg.lang)
        val id = PREFIX + generation.get() + "_" + at
        val params = Bundle().apply {
            putString(TextToSpeech.Engine.KEY_PARAM_UTTERANCE_ID, id)
        }
        engine.speak(seg.text, TextToSpeech.QUEUE_FLUSH, params, id)
    }

    private fun applyLanguage(lang: String) {
        val candidates = if (lang == "ur") {
            listOf(Locale("ur", "PK"), Locale("ur", "IN"), Locale("ur"))
        } else {
            listOf(Locale.US, Locale.UK, Locale.ENGLISH)
        }
        for (locale in candidates) {
            val check = engine.isLanguageAvailable(locale)
            if (check >= TextToSpeech.LANG_AVAILABLE) {
                engine.language = locale
                return
            }
        }
        if (lang == "ur") {
            engine.language = Locale.US
            emit("issue", "Urdu voice not installed — English fallback for this span.")
        }
    }

    private fun parse(json: String): List<Segment> {
        return try {
            val arr = JSONArray(json)
            buildList {
                for (i in 0 until arr.length()) {
                    val obj = arr.getJSONObject(i)
                    add(Segment(obj.optString("l", "en"), obj.optString("t")))
                }
            }
        } catch (_: Exception) {
            listOf(Segment("en", json))
        }
    }

    private fun emit(kind: String, payload: String) {
        val js = "window.onAndroidTtsEvent(${JSONObject.quote(kind)}, ${JSONObject.quote(payload)})"
        main.post {
            webView.evaluateJavascript(js, null)
        }
    }

    fun shutdown() {
        generation.incrementAndGet()
        engine.stop()
        engine.shutdown()
    }

    companion object {
        private const val PREFIX = "urdish_"
    }
}
