package com.csxi.teachyourself

import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.speech.tts.TextToSpeech
import android.speech.tts.UtteranceProgressListener
import android.webkit.JavascriptInterface
import android.webkit.WebView
import org.json.JSONArray
import java.util.Locale

/**
 * Speaks Roman-Urdish lecture blocks with the on-device engine.
 * The WebView highlights the block that is currently being read.
 */
class TtsBridge(
    private val webView: WebView,
    private val tts: TextToSpeech
) {
    private val main = Handler(Looper.getMainLooper())
    private var ready = false

    fun markReady(ok: Boolean) {
        ready = ok
        if (ok) {
            val applied = tts.setLanguage(Locale("en", "IN"))
            if (applied == TextToSpeech.LANG_MISSING_DATA || applied == TextToSpeech.LANG_NOT_SUPPORTED) {
                tts.setLanguage(Locale.US)
            }
            tts.setSpeechRate(0.92f)
            tts.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
                override fun onStart(utteranceId: String?) {
                    emit("window.onBlockStart && window.onBlockStart(${indexOf(utteranceId)})")
                }

                override fun onDone(utteranceId: String?) {
                    emit("window.onBlockDone && window.onBlockDone(${indexOf(utteranceId)})")
                }

                @Deprecated("Deprecated in Java")
                override fun onError(utteranceId: String?) {
                    emit("window.onBlockDone && window.onBlockDone(${indexOf(utteranceId)})")
                }

                override fun onError(utteranceId: String?, errorCode: Int) {
                    emit("window.onBlockDone && window.onBlockDone(${indexOf(utteranceId)})")
                }
            })
        }
        emit("window.onTtsReady && window.onTtsReady(${if (ok) "true" else "false"})")
    }

    private fun indexOf(utteranceId: String?): Int {
        if (utteranceId == null || !utteranceId.startsWith("b")) return -1
        return utteranceId.removePrefix("b").toIntOrNull() ?: -1
    }

    private fun emit(script: String) {
        main.post { webView.evaluateJavascript(script, null) }
    }

    @JavascriptInterface
    fun speakBlocks(payload: String) {
        if (!ready) {
            emit("window.onTtsMissing && window.onTtsMissing()")
            return
        }
        val blocks = JSONArray(payload)
        tts.stop()
        var queued = 0
        for (i in 0 until blocks.length()) {
            val item = blocks.getJSONObject(i)
            val text = item.optString("text").trim()
            if (text.isEmpty()) continue
            val index = item.optInt("i", i)
            val mode = if (queued == 0) TextToSpeech.QUEUE_FLUSH else TextToSpeech.QUEUE_ADD
            val params = Bundle()
            params.putString(TextToSpeech.Engine.KEY_PARAM_UTTERANCE_ID, "b$index")
            val result = tts.speak(text, mode, params, "b$index")
            if (result == TextToSpeech.ERROR && queued == 0) {
                emit("window.onTtsMissing && window.onTtsMissing()")
                return
            }
            queued++
        }
        if (queued == 0) {
            emit("window.onSpeakIdle && window.onSpeakIdle()")
        }
    }

    @JavascriptInterface
    fun stop() {
        if (ready) tts.stop()
        emit("window.onSpeakIdle && window.onSpeakIdle()")
    }

    @JavascriptInterface
    fun setRate(rate: Float) {
        val clamped = rate.coerceIn(0.6f, 1.4f)
        tts.setSpeechRate(clamped)
    }
}
