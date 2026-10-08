package com.teachyourself.sketchnotes

import android.content.Context
import android.os.Bundle
import android.speech.tts.TextToSpeech
import android.speech.tts.UtteranceProgressListener
import android.speech.tts.Voice
import java.util.ArrayDeque
import java.util.Locale

/**
 * Speaks a queue of Urdu and English pieces one at a time so each piece
 * can use its own voice. That alternation is the Urdish narration.
 */
class UrdishSpeaker(
    context: Context,
    private val onState: (String) -> Unit,
    private val onIssue: (String) -> Unit
) : TextToSpeech.OnInitListener {

    data class Segment(val text: String, val lang: String)

    private val engine = TextToSpeech(context.applicationContext, this)
    private val queue = ArrayDeque<Segment>()
    private var ready = false
    private var rate = 0.92f
    private var warnedAboutUrdu = false
    private var generation = 0

    @Synchronized
    override fun onInit(status: Int) {
        ready = status == TextToSpeech.SUCCESS
        if (ready) {
            engine.setSpeechRate(rate)
            engine.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
                override fun onStart(utteranceId: String?) {
                    onState("speaking")
                }

                override fun onDone(utteranceId: String?) {
                    if (utteranceId == null || !utteranceId.startsWith("$generation-")) return
                    pump()
                }

                @Deprecated("Deprecated in Java")
                override fun onError(utteranceId: String?) {
                    pump()
                }

                override fun onError(utteranceId: String?, errorCode: Int) {
                    pump()
                }
            })
        }
        onState(if (ready) "ready" else "error")
        if (ready && queue.isNotEmpty()) pump()
    }

    fun setRate(value: Float) {
        rate = value.coerceIn(0.65f, 1.25f)
        if (ready) engine.setSpeechRate(rate)
    }

    @Synchronized
    fun speak(segments: List<Segment>) {
        generation += 1
        queue.clear()
        if (ready) engine.stop()
        segments.flatMap { chunk(it) }
            .filter { it.text.isNotBlank() }
            .forEach { queue.add(it) }
        if (!ready) return
        pump()
    }

    @Synchronized
    fun stop() {
        generation += 1
        queue.clear()
        if (ready) engine.stop()
        onState("idle")
    }

    fun shutdown() {
        queue.clear()
        engine.stop()
        engine.shutdown()
    }

    @Synchronized
    private fun pump() {
        val next = queue.pollFirst()
        if (next == null) {
            onState("idle")
            return
        }
        if (!applyLanguage(next.lang)) {
            pump()
            return
        }
        val utteranceId = "$generation-${queue.size}"
        val params = Bundle()
        engine.speak(next.text, TextToSpeech.QUEUE_FLUSH, params, utteranceId)
    }

    private fun applyLanguage(language: String): Boolean {
        val urdu = language == "ur"
        val candidates = if (urdu) {
            listOf(Locale("ur", "PK"), Locale("ur", "IN"), Locale("ur"))
        } else {
            listOf(Locale.US, Locale.UK, Locale.ENGLISH)
        }
        for (locale in candidates) {
            val available = engine.isLanguageAvailable(locale)
            if (available == TextToSpeech.LANG_AVAILABLE ||
                available == TextToSpeech.LANG_COUNTRY_AVAILABLE ||
                available == TextToSpeech.LANG_COUNTRY_VAR_AVAILABLE
            ) {
                engine.language = locale
                selectVoice(locale)
                return true
            }
        }
        if (urdu) {
            if (!warnedAboutUrdu) {
                warnedAboutUrdu = true
                onIssue("Urdu voice is not installed. English will speak this part. Open voice settings to add Urdu.")
            }
            engine.language = Locale.US
            return true
        }
        onIssue("No speech voice is available on this device.")
        return false
    }

    private fun selectVoice(locale: Locale) {
        val voices = engine.voices ?: return
        val match = voices
            .filter { it.locale.language == locale.language && !it.isNetworkConnectionRequired }
            .maxByOrNull { voice ->
                var score = 0
                if (voice.quality >= Voice.QUALITY_HIGH) score += 2
                if (!voice.name.contains("network", ignoreCase = true)) score += 1
                score
            }
        if (match != null) engine.voice = match
    }

    private fun chunk(segment: Segment): List<Segment> {
        if (segment.text.length <= MAX_CHUNK) return listOf(segment)
        val pieces = mutableListOf<Segment>()
        var remaining = segment.text.trim()
        while (remaining.isNotEmpty()) {
            if (remaining.length <= MAX_CHUNK) {
                pieces.add(Segment(remaining, segment.lang))
                break
            }
            var splitAt = remaining.lastIndexOf('.', MAX_CHUNK)
            if (splitAt < MAX_CHUNK / 2) splitAt = remaining.lastIndexOf(' ', MAX_CHUNK)
            if (splitAt <= 0) splitAt = MAX_CHUNK
            pieces.add(Segment(remaining.substring(0, splitAt + 1).trim(), segment.lang))
            remaining = remaining.substring(splitAt + 1).trim()
        }
        return pieces
    }

    companion object {
        private const val MAX_CHUNK = 2500
    }
}
