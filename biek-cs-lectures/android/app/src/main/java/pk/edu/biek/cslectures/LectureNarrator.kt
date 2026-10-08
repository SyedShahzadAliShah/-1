package pk.edu.biek.cslectures

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.speech.tts.TextToSpeech
import android.speech.tts.UtteranceProgressListener
import pk.edu.biek.cslectures.model.Concept
import java.util.Locale

/**
 * Speaks concise Urdu when an Urdu voice is installed.
 * Otherwise speaks the same idea in Urdish: Roman Urdu with the technical term left in English.
 */
class LectureNarrator(
    context: Context,
    private val onReady: (urduVoice: Boolean) -> Unit,
    private val onConcept: (index: Int) -> Unit,
    private val onIdle: () -> Unit,
) : TextToSpeech.OnInitListener {

    private var tts: TextToSpeech? = TextToSpeech(context.applicationContext, this)
    private var ready = false
    private var urduVoice = false
    private var pending: (() -> Unit)? = null

    override fun onInit(status: Int) {
        ready = status == TextToSpeech.SUCCESS
        if (ready) {
            tts?.setSpeechRate(0.90f)
            urduVoice = applyUrdu()
            tts?.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
                override fun onStart(utteranceId: String?) {
                    utteranceId?.removePrefix(CONCEPT)?.toIntOrNull()?.let(onConcept)
                }

                override fun onDone(utteranceId: String?) {
                    if (utteranceId == DONE) onIdle()
                }

                @Deprecated("Deprecated in Java")
                override fun onError(utteranceId: String?) {
                    onIdle()
                }

                override fun onError(utteranceId: String?, errorCode: Int) {
                    onIdle()
                }
            })
        }
        onReady(urduVoice)
        pending?.invoke()
        pending = null
    }

    fun hasUrduVoice(): Boolean = urduVoice

    fun speakAll(concepts: List<Concept>) {
        runWhenReady {
            val engine = tts ?: return@runWhenReady
            chooseLanguage(engine)
            concepts.forEachIndexed { index, concept ->
                val mode = if (index == 0) TextToSpeech.QUEUE_FLUSH else TextToSpeech.QUEUE_ADD
                speakChunk(engine, concept.term + ". " + spoken(concept), mode, "$CONCEPT$index")
                engine.playSilentUtterance(350, TextToSpeech.QUEUE_ADD, "gap$index")
            }
            engine.playSilentUtterance(50, TextToSpeech.QUEUE_ADD, DONE)
        }
    }

    fun speakOne(index: Int, concept: Concept) {
        runWhenReady {
            val engine = tts ?: return@runWhenReady
            chooseLanguage(engine)
            speakChunk(engine, concept.term + ". " + spoken(concept), TextToSpeech.QUEUE_FLUSH, "$CONCEPT$index")
            engine.playSilentUtterance(50, TextToSpeech.QUEUE_ADD, DONE)
        }
    }

    fun stop() {
        pending = null
        tts?.stop()
        onIdle()
    }

    fun shutdown() {
        tts?.stop()
        tts?.shutdown()
        tts = null
        ready = false
    }

    private fun spoken(concept: Concept): String =
        if (urduVoice) concept.urdu else concept.urdish

    private fun chooseLanguage(engine: TextToSpeech) {
        if (urduVoice) {
            engine.language = Locale("ur", "PK")
        } else {
            engine.language = Locale.US
        }
    }

    private fun speakChunk(engine: TextToSpeech, text: String, mode: Int, id: String) {
        val params = Bundle()
        engine.speak(text, mode, params, id)
    }

    private fun runWhenReady(block: () -> Unit) {
        if (ready) block() else pending = block
    }

    private fun applyUrdu(): Boolean {
        val engine = tts ?: return false
        val locales = listOf(Locale("ur", "PK"), Locale("ur", "IN"), Locale("ur"))
        for (locale in locales) {
            val available = engine.isLanguageAvailable(locale)
            if (available == TextToSpeech.LANG_AVAILABLE ||
                available == TextToSpeech.LANG_COUNTRY_AVAILABLE ||
                available == TextToSpeech.LANG_COUNTRY_VAR_AVAILABLE
            ) {
                engine.language = locale
                val voice = engine.voices
                    ?.filter { it.locale.language == "ur" && !it.isNetworkConnectionRequired }
                    ?.maxByOrNull { if (it.quality >= android.speech.tts.Voice.QUALITY_HIGH) 1 else 0 }
                if (voice != null) engine.voice = voice
                return true
            }
        }
        engine.language = Locale.US
        return false
    }

    companion object {
        private const val CONCEPT = "concept-"
        private const val DONE = "lecture-done"

        fun openVoiceSettings(context: Context) {
            val intents = listOf(
                Intent(TextToSpeech.Engine.ACTION_INSTALL_TTS_DATA),
                Intent("com.android.settings.TTS_SETTINGS"),
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
