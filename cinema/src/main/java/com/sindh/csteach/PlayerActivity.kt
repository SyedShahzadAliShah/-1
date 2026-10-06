package com.sindh.csteach

import android.graphics.Color
import android.media.AudioAttributes
import android.media.AudioFormat
import android.media.AudioManager
import android.media.AudioTrack
import android.os.Bundle
import android.webkit.WebResourceRequest
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.webkit.WebViewAssetLoader
import com.sindh.csteach.databinding.ActivityPlayerBinding
import org.json.JSONArray
import org.json.JSONObject
import java.util.concurrent.atomic.AtomicInteger

class PlayerActivity : AppCompatActivity() {
    private lateinit var binding: ActivityPlayerBinding
    private lateinit var grade: Grade
    private lateinit var voice: EmbeddedVoice
    private var index = 0
    private var playing = false
    private var voiceReady = false
    private val generation = AtomicInteger(0)
    private var track: AudioTrack? = null
    private var sentences = listOf<String>()
    private var sentenceIndex = 0
    private var cardReady = false
    private var pendingBeat: Beat? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityPlayerBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val gradeId = intent.getStringExtra(EXTRA_GRADE) ?: "xi"
        val loaded = Catalog.grade(this, gradeId)
        if (loaded == null || loaded.beats.isEmpty()) {
            finish()
            return
        }
        grade = loaded
        voice = EmbeddedVoice(this)
        voice.prepare { ready, message ->
            voiceReady = ready
            binding.voiceStatus.text = if (ready) {
                getString(R.string.voice_ready)
            } else {
                getString(R.string.voice_failed) + (message?.let { ": $it" } ?: "")
            }
            binding.playButton.isEnabled = ready
        }

        setupCard()
        binding.backButton.setOnClickListener { finish() }
        binding.playButton.setOnClickListener { togglePlay() }
        binding.prevButton.setOnClickListener { showBeat((index - 1).coerceAtLeast(0), autoplay = playing) }
        binding.nextButton.setOnClickListener { showBeat((index + 1).coerceAtMost(grade.beats.lastIndex), autoplay = playing) }
        binding.chaptersButton.setOnClickListener { pickChapter() }
        showBeat(0, autoplay = false)
    }

    private fun pickChapter() {
        val titles = grade.chapters.map { "Chapter ${it.num}: ${it.title}" }.toTypedArray()
        AlertDialog.Builder(this)
            .setTitle(R.string.chapters)
            .setItems(titles) { _, which ->
                showBeat(grade.chapterStart(which), autoplay = playing)
            }
            .show()
    }

    private fun togglePlay() {
        if (!voiceReady) return
        if (playing) {
            stopPlayback()
            return
        }
        playing = true
        binding.playButton.text = getString(R.string.pause)
        speakFrom(sentenceIndex)
    }

    private fun stopPlayback() {
        playing = false
        generation.incrementAndGet()
        releaseTrack()
        binding.playButton.text = getString(R.string.play)
    }

    private fun showBeat(next: Int, autoplay: Boolean) {
        stopPlayback()
        index = next
        val beat = grade.beats[index]
        binding.card.alpha = 0f
        binding.kicker.text = grade.label
        binding.chapterTitle.text = beat.chapterLabel
        binding.counter.text = "${index + 1} / ${grade.beats.size}"
        binding.sceneTitle.text = beat.title
        renderCard(beat)
        binding.cardWeb.scrollTo(0, 0)
        binding.card.animate().alpha(1f).setDuration(280).start()
        sentences = sentencesOf(beat.speak)
        sentenceIndex = 0
        binding.subtitle.text = sentences.firstOrNull().orEmpty()
        if (autoplay && voiceReady) {
            playing = true
            binding.playButton.text = getString(R.string.pause)
            speakFrom(0)
        }
    }

    private fun setupCard() {
        val loader = WebViewAssetLoader.Builder()
            .addPathHandler("/assets/", WebViewAssetLoader.AssetsPathHandler(this))
            .build()
        binding.cardWeb.setBackgroundColor(Color.parseColor("#07080C"))
        binding.cardWeb.settings.apply {
            javaScriptEnabled = true
            allowFileAccess = false
            blockNetworkLoads = true
            domStorageEnabled = false
        }
        binding.cardWeb.webViewClient = object : WebViewClient() {
            override fun shouldInterceptRequest(view: WebView, request: WebResourceRequest) =
                loader.shouldInterceptRequest(request.url)

            override fun onPageFinished(view: WebView?, url: String?) {
                cardReady = true
                pendingBeat?.let { renderCard(it) }
            }
        }
        binding.cardWeb.loadUrl("https://appassets.androidplatform.net/assets/card.html")
    }

    private fun renderCard(beat: Beat) {
        if (!cardReady) {
            pendingBeat = beat
            return
        }
        pendingBeat = null
        val payload = JSONObject()
            .put("body", beat.body)
            .put("urdu", beat.urdu)
            .put("figures", JSONArray(beat.figures))
            .toString()
        binding.cardWeb.evaluateJavascript("show(${JSONObject.quote(payload)})", null)
    }

    private fun speakFrom(start: Int) {
        val token = generation.incrementAndGet()
        sentenceIndex = start
        if (!playing || start >= sentences.size) {
            if (playing && index < grade.beats.lastIndex) {
                showBeat(index + 1, autoplay = true)
            } else {
                stopPlayback()
            }
            return
        }
        val sentence = sentences[start]
        binding.subtitle.text = sentence
        voice.synthesize(sentence, onAudio = { pcm, sampleRate ->
            if (token != generation.get() || !playing) return@synthesize
            if (pcm.isEmpty() || sampleRate <= 0) {
                sentenceIndex = start + 1
                speakFrom(sentenceIndex)
                return@synthesize
            }
            play(pcm, sampleRate, token) {
                if (token != generation.get()) return@play
                sentenceIndex = start + 1
                speakFrom(sentenceIndex)
            }
        }, onError = { message ->
            if (token != generation.get()) return@synthesize
            binding.voiceStatus.text = message
            stopPlayback()
        })
    }

    private fun play(pcm: ShortArray, sampleRate: Int, token: Int, onDone: () -> Unit) {
        releaseTrack()
        val audio = AudioTrack(
            AudioAttributes.Builder()
                .setUsage(AudioAttributes.USAGE_MEDIA)
                .setContentType(AudioAttributes.CONTENT_TYPE_SPEECH)
                .build(),
            AudioFormat.Builder()
                .setEncoding(AudioFormat.ENCODING_PCM_16BIT)
                .setSampleRate(sampleRate)
                .setChannelMask(AudioFormat.CHANNEL_OUT_MONO)
                .build(),
            pcm.size * 2,
            AudioTrack.MODE_STATIC,
            AudioManager.AUDIO_SESSION_ID_GENERATE,
        )
        track = audio
        audio.write(pcm, 0, pcm.size)
        audio.setNotificationMarkerPosition(pcm.size)
        audio.setPlaybackPositionUpdateListener(object : AudioTrack.OnPlaybackPositionUpdateListener {
            override fun onMarkerReached(track: AudioTrack?) {
                if (token == generation.get()) onDone()
            }

            override fun onPeriodicNotification(track: AudioTrack?) = Unit
        })
        audio.play()
    }

    private fun releaseTrack() {
        track?.let { audio ->
            try {
                audio.pause()
                audio.flush()
                audio.release()
            } catch (_: IllegalStateException) {
                audio.release()
            }
        }
        track = null
    }

    private fun sentencesOf(text: String): List<String> {
        val parts = text.split(Regex("(?<=[.!?])\\s+"))
            .map { it.trim() }
            .filter { it.length > 1 }
        if (parts.isEmpty()) return listOf(text)
        val sized = mutableListOf<String>()
        parts.forEach { sentence ->
            if (sentence.length <= 240) {
                sized.add(sentence)
            } else {
                var rest = sentence
                while (rest.length > 240) {
                    val splitAt = rest.lastIndexOf(' ', 240).takeIf { it > 40 } ?: 240
                    sized.add(rest.substring(0, splitAt).trim())
                    rest = rest.substring(splitAt).trim()
                }
                if (rest.isNotEmpty()) sized.add(rest)
            }
        }
        return sized
    }

    override fun onStop() {
        stopPlayback()
        super.onStop()
    }

    override fun onDestroy() {
        if (::binding.isInitialized) {
            binding.cardWeb.stopLoading()
            binding.cardWeb.destroy()
        }
        if (::voice.isInitialized) voice.shutdown()
        super.onDestroy()
    }

    companion object {
        const val EXTRA_GRADE = "grade"
    }
}
