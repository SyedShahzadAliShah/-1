package com.couplesguide.postures.util

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.speech.tts.TextToSpeech
import android.speech.tts.UtteranceProgressListener

/**
 * In-app narrative TTS: **English or Urdu only**, always using [NarrativeMaleVoiceSelector].
 */
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
    private var onSegmentsComplete: (() -> Unit)? = null

    init {
        tts = TextToSpeech(context.applicationContext, this)
    }

    override fun onInit(status: Int) {
        isReady = status == TextToSpeech.SUCCESS
        if (isReady) {
            tts?.let { engine ->
                NarrativeMaleVoiceSelector.configureBaseline(engine)
                NarrativeMaleVoiceSelector.applyForLanguage(engine, LocaleHelper.LANG_EN)
            }
            attachProgressListener()
        }
        onReadyChanged(isReady)
        if (isReady && pendingSpeech.isNotEmpty()) {
            val queued = pendingSpeech.toList()
            pendingSpeech.clear()
            speakSegments(queued)
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
                notifyIfIdle()
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
        notifyIfIdle()
    }

    private fun notifyIfIdle() {
        if (activeUtterances == 0) {
            onSpeakingChanged(false)
            val complete = onSegmentsComplete
            onSegmentsComplete = null
            complete?.invoke()
        }
    }

    fun speak(text: String, language: String): Boolean {
        return speakSegments(listOf(text to language))
    }

    fun speakSegments(segments: List<Pair<String, String>>, onComplete: (() -> Unit)? = null): Boolean {
        val cleaned = segments.mapNotNull { (text, lang) ->
            val t = text.trim()
            if (t.isEmpty()) null else t to NarrativeMaleVoiceSelector.narrativeLanguage(lang)
        }
        if (cleaned.isEmpty()) {
            onComplete?.invoke()
            return false
        }
        val engine = tts ?: return false
        if (!isReady) {
            pendingSpeech.addAll(cleaned)
            onSegmentsComplete = onComplete
            return true
        }

        onSegmentsComplete = onComplete
        activeUtterances = 0
        cleaned.forEachIndexed { segmentIndex, (rawText, language) ->
            val text = if (language == LocaleHelper.LANG_UR) {
                UrduTtsPronunciation.prepare(rawText)
            } else {
                rawText
            }
            val applied = NarrativeMaleVoiceSelector.applyForLanguage(engine, language)
            if (applied == null) {
                onLanguageIssue?.invoke("Voice language not available on this device.")
                return@forEachIndexed
            }
            if (applied.fallbackUsed) {
                onLanguageIssue?.invoke(applied.message)
            }
            val chunks = chunkText(text)
            activeUtterances += chunks.size
            chunks.forEachIndexed { chunkIndex, chunk ->
                val utteranceId = "${UTTERANCE_PREFIX}${segmentIndex}_${chunkIndex}"
                val params = Bundle().apply {
                    putString(TextToSpeech.Engine.KEY_PARAM_UTTERANCE_ID, utteranceId)
                }
                val isFirst = segmentIndex == 0 && chunkIndex == 0
                val queueMode = if (isFirst) TextToSpeech.QUEUE_FLUSH else TextToSpeech.QUEUE_ADD
                engine.speak(chunk, queueMode, params, utteranceId)
            }
        }
        if (activeUtterances == 0) {
            onComplete?.invoke()
            return false
        }
        return true
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
        onSegmentsComplete = null
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
