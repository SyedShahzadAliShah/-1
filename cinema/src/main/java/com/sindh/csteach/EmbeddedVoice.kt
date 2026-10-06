package com.sindh.csteach

import android.content.Context
import android.os.Handler
import android.os.Looper
import com.k2fsa.sherpa.onnx.OfflineTts
import com.k2fsa.sherpa.onnx.OfflineTtsConfig
import com.k2fsa.sherpa.onnx.OfflineTtsModelConfig
import com.k2fsa.sherpa.onnx.OfflineTtsVitsModelConfig
import java.io.File
import java.util.concurrent.Executors

/**
 * Piper English voice packaged in the APK. espeak-ng data is copied out of
 * assets once, because the phonemizer reads real files rather than the asset zip.
 */
class EmbeddedVoice(private val context: Context) {
    private val executor = Executors.newSingleThreadExecutor()
    private val main = Handler(Looper.getMainLooper())
    @Volatile private var tts: OfflineTts? = null

    fun prepare(onReady: (Boolean, String?) -> Unit) {
        executor.execute {
            try {
                val espeak = copyEspeak()
                val config = OfflineTtsConfig(
                    model = OfflineTtsModelConfig(
                        vits = OfflineTtsVitsModelConfig(
                            model = "voice/model.onnx",
                            tokens = "voice/tokens.txt",
                            dataDir = espeak.absolutePath,
                            lexicon = "",
                        ),
                        numThreads = 2,
                        debug = false,
                        provider = "cpu",
                    ),
                    maxNumSentences = 1,
                )
                tts = OfflineTts(context.assets, config)
                main.post { onReady(true, null) }
            } catch (error: Throwable) {
                main.post { onReady(false, error.message ?: error.javaClass.simpleName) }
            }
        }
    }

    fun synthesize(text: String, onAudio: (ShortArray, Int) -> Unit, onError: (String) -> Unit) {
        val spoken = text.replace(Regex("[^A-Za-z0-9.,;:!?()'\"/+%\\-\\s]"), " ")
            .replace(Regex("\\s+"), " ")
            .trim()
        if (spoken.length < 2) {
            main.post { onAudio(ShortArray(0), 0) }
            return
        }
        executor.execute {
            try {
                val engine = tts ?: error("Voice is not ready")
                val audio = engine.generate(spoken, sid = 0, speed = 0.96f)
                val pcm = ShortArray(audio.samples.size) { index ->
                    (audio.samples[index].coerceIn(-1f, 1f) * 32767f).toInt().toShort()
                }
                main.post { onAudio(pcm, audio.sampleRate) }
            } catch (error: Throwable) {
                main.post { onError(error.message ?: "Could not speak") }
            }
        }
    }

    fun shutdown() {
        executor.execute {
            tts = null
        }
    }

    private fun copyEspeak(): File {
        val dest = File(context.filesDir, "espeak-ng-data")
        val marker = File(dest, "en_dict")
        if (marker.exists() && marker.length() > 0L) return dest
        dest.deleteRecursively()
        copyAssetDir("voice/espeak-ng-data", dest)
        return dest
    }

    private fun copyAssetDir(assetPath: String, dest: File) {
        val children = context.assets.list(assetPath).orEmpty()
        if (children.isEmpty()) {
            dest.parentFile?.mkdirs()
            context.assets.open(assetPath).use { input ->
                dest.outputStream().use { output -> input.copyTo(output) }
            }
        } else {
            dest.mkdirs()
            children.forEach { name ->
                copyAssetDir("$assetPath/$name", File(dest, name))
            }
        }
    }
}
