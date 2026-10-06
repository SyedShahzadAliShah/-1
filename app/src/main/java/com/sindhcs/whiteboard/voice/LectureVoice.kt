package com.sindhcs.whiteboard.voice

import android.content.Context
import android.media.AudioAttributes
import android.media.AudioManager
import android.os.Bundle
import android.speech.tts.TextToSpeech
import android.speech.tts.UtteranceProgressListener
import java.util.Locale

class LectureVoice(
    context: Context,
    private val onReady: (Boolean) -> Unit,
    private val onSpeaking: (Boolean) -> Unit,
    private val onRange: (Int, Int) -> Unit,
    private val onDone: () -> Unit
) : TextToSpeech.OnInitListener {

    private val appContext = context.applicationContext
    private val audioManager = appContext.getSystemService(Context.AUDIO_SERVICE) as AudioManager
    private var tts: TextToSpeech? = TextToSpeech(appContext, this)
    private var ready = false
    private var pending: String? = null
    private var token = 0
    private var rate = 1f

    override fun onInit(status: Int) {
        ready = status == TextToSpeech.SUCCESS
        if (ready) {
            val engine = tts
            engine?.setAudioAttributes(
                AudioAttributes.Builder()
                    .setUsage(AudioAttributes.USAGE_MEDIA)
                    .setContentType(AudioAttributes.CONTENT_TYPE_SPEECH)
                    .build()
            )
            val language = sequenceOf(Locale.US, Locale.UK, Locale.ENGLISH)
                .firstOrNull { locale ->
                    val result = engine?.setLanguage(locale) ?: TextToSpeech.LANG_NOT_SUPPORTED
                    result != TextToSpeech.LANG_MISSING_DATA && result != TextToSpeech.LANG_NOT_SUPPORTED
                }
            if (language == null) ready = false
            engine?.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
                override fun onStart(utteranceId: String?) {
                    if (utteranceId == token.toString()) onSpeaking(true)
                }

                override fun onDone(utteranceId: String?) {
                    if (utteranceId != token.toString()) return
                    onSpeaking(false)
                    onDone()
                }

                @Deprecated("Deprecated in Java")
                override fun onError(utteranceId: String?) {
                    if (utteranceId != token.toString()) return
                    onSpeaking(false)
                    onDone()
                }

                override fun onError(utteranceId: String?, errorCode: Int) {
                    onError(utteranceId)
                }

                override fun onRangeStart(utteranceId: String?, start: Int, end: Int, frame: Int) {
                    if (utteranceId == token.toString()) onRange(start, end)
                }
            })
        }
        onReady(ready)
        val queued = pending
        if (ready && queued != null) {
            pending = null
            speakNow(queued)
        }
    }

    fun setRate(speechRate: Float) {
        rate = speechRate.coerceIn(0.7f, 1.3f)
        tts?.setSpeechRate(rate)
    }

    fun speak(text: String) {
        val clean = text.trim()
        if (clean.isEmpty()) {
            onDone()
            return
        }
        token += 1
        if (!ready) {
            pending = clean
            return
        }
        speakNow(clean)
    }

    fun stop() {
        token += 1
        pending = null
        tts?.stop()
        onSpeaking(false)
    }

    fun shutdown() {
        token += 1
        pending = null
        tts?.stop()
        tts?.shutdown()
        tts = null
        ready = false
    }

    private fun speakNow(text: String) {
        val engine = tts ?: return
        engine.setSpeechRate(rate)
        @Suppress("DEPRECATION")
        audioManager.requestAudioFocus(
            null,
            AudioManager.STREAM_MUSIC,
            AudioManager.AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK
        )
        val params = Bundle()
        engine.speak(text, TextToSpeech.QUEUE_FLUSH, params, token.toString())
    }
}
