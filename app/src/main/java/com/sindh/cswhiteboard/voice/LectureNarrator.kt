package com.sindh.cswhiteboard.voice

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.speech.tts.TextToSpeech
import android.speech.tts.UtteranceProgressListener
import android.speech.tts.Voice
import com.sindh.cswhiteboard.data.Prefs
import java.util.Locale

class LectureNarrator(
    context: Context,
    private val onReady: (Boolean) -> Unit,
    private val onSpeaking: (Boolean) -> Unit,
    private val onUtteranceDone: () -> Unit,
    private val onIssue: (String) -> Unit
) : TextToSpeech.OnInitListener {

    private var tts: TextToSpeech? = TextToSpeech(context.applicationContext, this)
    private var ready = false
    private var pending: Pair<String, String>? = null
    private var expectedId: String? = null

    override fun onInit(status: Int) {
        ready = status == TextToSpeech.SUCCESS
        if (ready) {
            tts?.setPitch(1.02f)
            attach()
        }
        onReady(ready)
        pending?.let { (text, lang) ->
            pending = null
            speak(text, lang)
        }
    }

    private fun attach() {
        tts?.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
            override fun onStart(utteranceId: String?) {
                onSpeaking(true)
            }

            override fun onDone(utteranceId: String?) {
                if (utteranceId == expectedId) {
                    expectedId = null
                    onSpeaking(false)
                    onUtteranceDone()
                }
            }

            @Deprecated("Deprecated in Java")
            override fun onError(utteranceId: String?) {
                expectedId = null
                onSpeaking(false)
                onUtteranceDone()
            }

            override fun onError(utteranceId: String?, errorCode: Int) {
                expectedId = null
                onSpeaking(false)
                onUtteranceDone()
            }
        })
    }

    fun speak(text: String, language: String, rate: Float = 0.92f): Boolean {
        val engine = tts ?: return false
        if (text.isBlank()) {
            onUtteranceDone()
            return true
        }
        if (!ready) {
            pending = text to language
            return true
        }
        if (!applyLanguage(engine, language)) return false
        engine.setSpeechRate(rate.coerceIn(0.7f, 1.3f))
        val id = "seg_${System.nanoTime()}"
        expectedId = id
        val params = Bundle().apply {
            putString(TextToSpeech.Engine.KEY_PARAM_UTTERANCE_ID, id)
        }
        val chunks = chunk(text)
        chunks.forEachIndexed { index, chunk ->
            val chunkId = if (index == chunks.lastIndex) id else "${id}_$index"
            val mode = if (index == 0) TextToSpeech.QUEUE_FLUSH else TextToSpeech.QUEUE_ADD
            engine.speak(chunk, mode, params.apply {
                putString(TextToSpeech.Engine.KEY_PARAM_UTTERANCE_ID, chunkId)
            }, chunkId)
        }
        return true
    }

    private fun applyLanguage(engine: TextToSpeech, language: String): Boolean {
        val candidates = if (language == Prefs.LANG_UR) {
            listOf(Locale("ur", "PK"), Locale("ur", "IN"), Locale("ur"))
        } else {
            listOf(Locale("en", "IN"), Locale.US, Locale.UK, Locale.ENGLISH)
        }
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
        if (language == Prefs.LANG_UR) {
            engine.language = Locale.US
            onIssue("Urdu voice is not installed. Using English vocals.")
            return true
        }
        onIssue("No voice data on this device. Open TTS settings to install.")
        return false
    }

    private fun pickVoice(engine: TextToSpeech, locale: Locale) {
        val voices = engine.voices ?: return
        val match = voices
            .filter { it.locale.language == locale.language && !it.isNetworkConnectionRequired }
            .maxByOrNull { voice ->
                var score = 0
                if (voice.quality >= Voice.QUALITY_HIGH) score += 2
                if (voice.name.contains("male", true) || voice.name.contains("en-in", true)) score += 1
                score
            }
        if (match != null) engine.voice = match
    }

    private fun chunk(text: String): List<String> {
        if (text.length <= 3200) return listOf(text)
        val out = mutableListOf<String>()
        var rest = text.trim()
        while (rest.isNotEmpty()) {
            if (rest.length <= 3200) {
                out.add(rest)
                break
            }
            var at = rest.lastIndexOf('.', 3200)
            if (at < 1600) at = rest.lastIndexOf(' ', 3200)
            if (at <= 0) at = 3200
            out.add(rest.substring(0, at + 1).trim())
            rest = rest.substring(at + 1).trim()
        }
        return out.ifEmpty { listOf(text) }
    }

    fun stop() {
        pending = null
        expectedId = null
        tts?.stop()
        onSpeaking(false)
    }

    fun shutdown() {
        stop()
        tts?.shutdown()
        tts = null
        ready = false
    }

    companion object {
        fun openSettings(context: Context) {
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
