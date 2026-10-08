package com.csxii.teachyourself

import android.content.Intent
import android.provider.Settings
import android.speech.tts.TextToSpeech
import android.speech.tts.UtteranceProgressListener
import android.webkit.JavascriptInterface
import org.json.JSONArray
import java.util.Locale

/**
 * Speaks Urdish as alternating Urdu and English utterances so technical
 * terms keep their English voice inside an Urdu lecture.
 */
class TtsBridge(
    private val activity: LectureActivity,
    private val tts: TextToSpeech
) {
    private data class Seg(val lang: String, val text: String, val mark: String)

    @Volatile
    private var urduReady = false

    private val queue = ArrayList<Seg>()
    private var index = 0
    private var playing = false
    private var rate = 0.92f

    init {
        tts.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
            override fun onStart(utteranceId: String?) {
                val quoted = org.json.JSONObject.quote(utteranceId ?: "")
                activity.evaluate("window.__ttsMark && window.__ttsMark($quoted)")
            }

            override fun onDone(utteranceId: String?) {
                activity.runOnUiThread { advance() }
            }

            @Deprecated("Deprecated in Java")
            override fun onError(utteranceId: String?) {
                activity.runOnUiThread { advance() }
            }

            override fun onError(utteranceId: String?, errorCode: Int) {
                activity.runOnUiThread { advance() }
            }
        })
    }

    fun onInit(status: Int) {
        urduReady = false
        if (status == TextToSpeech.SUCCESS) {
            urduReady = languageWorks(Locale("ur", "PK")) || languageWorks(Locale("ur"))
            tts.setSpeechRate(rate)
        }
        activity.evaluate("window.__ttsReady && window.__ttsReady()")
    }

    private fun languageWorks(locale: Locale): Boolean {
        val result = tts.setLanguage(locale)
        return result != TextToSpeech.LANG_MISSING_DATA && result != TextToSpeech.LANG_NOT_SUPPORTED
    }

    @JavascriptInterface
    fun urduAvailable(): Boolean = urduReady

    @JavascriptInterface
    fun embedded(): Boolean = true

    @JavascriptInterface
    fun speak(json: String) {
        val parsed = ArrayList<Seg>()
        val arr = JSONArray(json)
        for (i in 0 until arr.length()) {
            val item = arr.getJSONObject(i)
            val text = item.optString("text").trim()
            if (text.isEmpty()) continue
            parsed.add(
                Seg(
                    item.optString("lang", "ur"),
                    text,
                    item.optString("mark", i.toString())
                )
            )
        }
        synchronized(queue) {
            queue.clear()
            queue.addAll(parsed)
            index = 0
            playing = queue.isNotEmpty()
        }
        activity.runOnUiThread { speakCurrent() }
    }

    @JavascriptInterface
    fun stop() {
        synchronized(queue) {
            playing = false
            queue.clear()
            index = 0
        }
        tts.stop()
        activity.evaluate("window.__ttsDone && window.__ttsDone()")
    }

    @JavascriptInterface
    fun pause() {
        synchronized(queue) { playing = false }
        tts.stop()
    }

    @JavascriptInterface
    fun resume() {
        val shouldSpeak = synchronized(queue) {
            if (queue.isEmpty() || index >= queue.size) return
            playing = true
            true
        }
        if (shouldSpeak) activity.runOnUiThread { speakCurrent() }
    }

    @JavascriptInterface
    fun setRate(value: Double) {
        rate = value.toFloat().coerceIn(0.6f, 1.35f)
        tts.setSpeechRate(rate)
    }

    @JavascriptInterface
    fun openTtsSettings() {
        activity.runOnUiThread {
            try {
                activity.startActivity(Intent("com.android.settings.TTS_SETTINGS"))
            } catch (_: Exception) {
                activity.startActivity(Intent(Settings.ACTION_SETTINGS))
            }
        }
    }

    private fun speakCurrent() {
        val seg = synchronized(queue) {
            if (!playing || index >= queue.size) {
                if (playing && index >= queue.size) {
                    playing = false
                    activity.evaluate("window.__ttsDone && window.__ttsDone()")
                }
                return
            }
            queue[index]
        }
        if (seg.lang == "en") {
            tts.setLanguage(Locale.US)
        } else if (!languageWorks(Locale("ur", "PK"))) {
            tts.setLanguage(Locale("ur"))
        }
        tts.setSpeechRate(rate)
        val spoken = tts.speak(seg.text, TextToSpeech.QUEUE_FLUSH, null, seg.mark.ifEmpty { "seg" })
        if (spoken == TextToSpeech.ERROR) {
            synchronized(queue) { index += 1 }
            speakCurrent()
        }
    }

    private fun advance() {
        val finished = synchronized(queue) {
            if (!playing) return
            index += 1
            index >= queue.size
        }
        if (finished) {
            synchronized(queue) { playing = false }
            activity.evaluate("window.__ttsDone && window.__ttsDone()")
        } else {
            speakCurrent()
        }
    }

    fun shutdown() {
        tts.stop()
        tts.shutdown()
    }
}
