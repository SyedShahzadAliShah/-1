package com.sindhcs.lectures.util

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.speech.tts.TextToSpeech
import android.speech.tts.UtteranceProgressListener
import android.speech.tts.Voice
import java.util.Locale

class UrduNarrator(
    context: Context,
    private val onReadyChanged: (Boolean) -> Unit,
    private val onSpeakingChanged: (Boolean) -> Unit,
    private val onProgress: (Float) -> Unit = {},
    private val onLanguageIssue: ((String) -> Unit)? = null
) : TextToSpeech.OnInitListener {

    private var tts: TextToSpeech? = TextToSpeech(context.applicationContext, this)
    private var isReady = false
    private val pending = mutableListOf<String>()
    private var activeUtterances = 0
    private var chunkOffsets: IntArray = intArrayOf()
    private var totalChars = 1
    private val main = Handler(Looper.getMainLooper())

    override fun onInit(status: Int) {
        isReady = status == TextToSpeech.SUCCESS
        if (isReady) {
            tts?.setSpeechRate(SPEECH_RATE)
            tts?.setPitch(1.0f)
            attachListener()
        }
        onReadyChanged(isReady)
        if (isReady && pending.isNotEmpty()) {
            val queued = pending.toList()
            pending.clear()
            queued.forEach { speak(it) }
        }
        if (isReady && !applyUrdu()) {
            onLanguageIssue?.invoke(
                "اس phone پر Urdu voice install نہیں۔ Settings → Language → Text-to-speech میں Google Urdu TTS لگائیں — اردو lecture اسی voice سے چلتی ہے۔"
            )
        }
    }

    private fun attachListener() {
        tts?.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
            override fun onStart(utteranceId: String?) {
                val index = indexOf(utteranceId)
                if (index >= 0) report((chunkOffsets[index]).toFloat() / totalChars)
                main.post { onSpeakingChanged(true) }
            }

            override fun onRangeStart(utteranceId: String?, start: Int, end: Int, frame: Int) {
                val index = indexOf(utteranceId)
                if (index < 0) return
                report((chunkOffsets[index] + start).toFloat() / totalChars)
            }

            override fun onDone(utteranceId: String?) {
                if (utteranceId?.startsWith(PREFIX) == true) {
                    activeUtterances = (activeUtterances - 1).coerceAtLeast(0)
                }
                if (activeUtterances == 0) {
                    report(1f)
                    main.post { onSpeakingChanged(false) }
                }
            }

            @Deprecated("Deprecated in Java")
            override fun onError(utteranceId: String?) {
                activeUtterances = 0
                main.post { onSpeakingChanged(false) }
            }

            override fun onError(utteranceId: String?, errorCode: Int) {
                activeUtterances = 0
                main.post { onSpeakingChanged(false) }
            }
        })
    }

    fun speak(text: String): Boolean {
        if (text.isBlank()) return false
        val engine = tts ?: return false
        if (!isReady) {
            pending.add(text)
            return true
        }
        if (!applyUrdu()) {
            onLanguageIssue?.invoke(
                "Urdu voice دستیاب نہیں۔ اردو lecture سننے کے لیے Google Urdu TTS install کرو。"
            )
            return false
        }
        val chunks = chunk(text)
        chunkOffsets = IntArray(chunks.size)
        var running = 0
        chunks.forEachIndexed { i, part ->
            chunkOffsets[i] = running
            running += part.length
        }
        totalChars = running.coerceAtLeast(1)
        activeUtterances = chunks.size
        report(0f)
        chunks.forEachIndexed { index, part ->
            val id = "$PREFIX$index"
            val params = Bundle().apply {
                putString(TextToSpeech.Engine.KEY_PARAM_UTTERANCE_ID, id)
            }
            val mode = if (index == 0) TextToSpeech.QUEUE_FLUSH else TextToSpeech.QUEUE_ADD
            engine.speak(part, mode, params, id)
        }
        return true
    }

    private fun report(fraction: Float) {
        val clamped = fraction.coerceIn(0f, 1f)
        main.post { onProgress(clamped) }
    }

    private fun indexOf(utteranceId: String?): Int {
        if (utteranceId == null || !utteranceId.startsWith(PREFIX)) return -1
        return utteranceId.removePrefix(PREFIX).toIntOrNull() ?: -1
    }

    private fun applyUrdu(): Boolean {
        val engine = tts ?: return false
        val candidates = listOf(Locale("ur", "PK"), Locale("ur", "IN"), Locale("ur"))
        for (locale in candidates) {
            when (engine.isLanguageAvailable(locale)) {
                TextToSpeech.LANG_AVAILABLE,
                TextToSpeech.LANG_COUNTRY_AVAILABLE,
                TextToSpeech.LANG_COUNTRY_VAR_AVAILABLE -> {
                    engine.language = locale
                    pickVoice(engine, locale)
                    return true
                }
            }
        }
        return false
    }

    private fun pickVoice(engine: TextToSpeech, locale: Locale) {
        val voices = engine.voices ?: return
        val match = voices
            .filter { it.locale.language == locale.language && !it.isNetworkConnectionRequired }
            .maxByOrNull { score(it) }
        if (match != null) engine.voice = match
    }

    private fun score(voice: Voice): Int {
        var n = 0
        if (voice.quality >= Voice.QUALITY_HIGH) n += 2
        if (!voice.name.contains("network", ignoreCase = true)) n += 1
        if (voice.locale.country.equals("PK", true)) n += 2
        return n
    }

    private fun chunk(text: String): List<String> {
        if (text.length <= MAX) return listOf(text)
        val chunks = mutableListOf<String>()
        var remaining = text.trim()
        while (remaining.isNotEmpty()) {
            if (remaining.length <= MAX) {
                chunks.add(remaining)
                break
            }
            var splitAt = remaining.lastIndexOf('۔', MAX)
            if (splitAt < MAX / 2) splitAt = remaining.lastIndexOf('.', MAX)
            if (splitAt < MAX / 2) splitAt = remaining.lastIndexOf(' ', MAX)
            if (splitAt <= 0) splitAt = MAX
            chunks.add(remaining.substring(0, splitAt + 1).trim())
            remaining = remaining.substring(splitAt + 1).trim()
        }
        return chunks.ifEmpty { listOf(text) }
    }

    fun stop() {
        pending.clear()
        activeUtterances = 0
        tts?.stop()
        onSpeakingChanged(false)
    }

    fun shutdown() {
        stop()
        tts?.shutdown()
        tts = null
        isReady = false
    }

    companion object {
        private const val MAX = 2800
        private const val PREFIX = "urdu_lecture_"
        const val SPEECH_RATE = 0.88f

        fun openTtsSettings(context: Context) {
            val intents = listOf(
                Intent(TextToSpeech.Engine.ACTION_INSTALL_TTS_DATA),
                Intent("com.android.settings.TTS_SETTINGS")
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
