package pk.edu.csxi.teachers

import android.content.Context
import android.media.AudioAttributes
import android.media.AudioFocusRequest
import android.media.AudioManager
import android.media.MediaPlayer
import android.os.Build

/**
 * Plays the pre-recorded Urdu narration of a page one block after another.
 * Positions refer to indexes in the page's [Item] list.
 */
class Narrator(context: Context, private val listener: Listener) {

    interface Listener {
        fun onItemStarted(page: Int, position: Int)
        fun onPageFinished(page: Int)
        fun onPlayingChanged(playing: Boolean)
    }

    private val app = context.applicationContext
    private val audioManager = app.getSystemService(Context.AUDIO_SERVICE) as AudioManager
    private var player: MediaPlayer? = null
    private var items: List<Item> = emptyList()
    private var page = 0
    private var position = -1
    private var prepared = false
    private var wantPlaying = false
    private var focusRequest: AudioFocusRequest? = null

    var speed: Float = 1.0f
        set(value) {
            field = value
            applySpeed()
        }

    val currentPage get() = page
    val currentPosition get() = position
    val isPlaying get() = wantPlaying
    val hasSession get() = position >= 0

    private val focusListener = AudioManager.OnAudioFocusChangeListener { change ->
        if (change == AudioManager.AUDIOFOCUS_LOSS || change == AudioManager.AUDIOFOCUS_LOSS_TRANSIENT) {
            pause()
        }
    }

    fun play(page: Int, items: List<Item>, from: Int) {
        val start = (from until items.size).firstOrNull { items[it].audio != null } ?: return
        releasePlayer()
        this.page = page
        this.items = items
        requestFocus()
        startItem(start)
    }

    fun pause() {
        if (!wantPlaying) return
        wantPlaying = false
        player?.takeIf { prepared }?.pause()
        listener.onPlayingChanged(false)
    }

    fun resume() {
        if (wantPlaying || position < 0) return
        wantPlaying = true
        requestFocus()
        player?.let {
            if (prepared) {
                it.start()
                applySpeed()
            }
        }
        listener.onPlayingChanged(true)
    }

    fun stop() {
        val was = wantPlaying
        wantPlaying = false
        releasePlayer()
        position = -1
        abandonFocus()
        if (was) listener.onPlayingChanged(false)
    }

    fun release() {
        wantPlaying = false
        releasePlayer()
        abandonFocus()
    }

    private fun startItem(pos: Int) {
        position = pos
        wantPlaying = true
        prepared = false
        val asset = items[pos].audio ?: return advance()
        releasePlayer()
        val mp = MediaPlayer()
        player = mp
        try {
            app.assets.openFd(asset).use { fd ->
                mp.setDataSource(fd.fileDescriptor, fd.startOffset, fd.length)
            }
            mp.setAudioAttributes(
                AudioAttributes.Builder()
                    .setUsage(AudioAttributes.USAGE_MEDIA)
                    .setContentType(AudioAttributes.CONTENT_TYPE_SPEECH)
                    .build()
            )
            mp.setOnPreparedListener {
                prepared = true
                if (wantPlaying) {
                    it.start()
                    applySpeed()
                }
            }
            mp.setOnCompletionListener { advance() }
            mp.setOnErrorListener { _, _, _ -> advance(); true }
            mp.prepareAsync()
        } catch (e: Exception) {
            advance()
            return
        }
        listener.onItemStarted(page, pos)
        listener.onPlayingChanged(true)
    }

    private fun advance() {
        val next = (position + 1 until items.size).firstOrNull { items[it].audio != null }
        if (next != null) {
            startItem(next)
        } else {
            val finished = page
            wantPlaying = false
            releasePlayer()
            position = -1
            abandonFocus()
            listener.onPlayingChanged(false)
            listener.onPageFinished(finished)
        }
    }

    private fun applySpeed() {
        val mp = player ?: return
        if (!prepared || !wantPlaying) return
        try {
            mp.playbackParams = mp.playbackParams.setSpeed(speed)
        } catch (_: Exception) {
        }
    }

    private fun releasePlayer() {
        player?.let {
            it.setOnCompletionListener(null)
            it.setOnErrorListener(null)
            it.setOnPreparedListener(null)
            try {
                it.release()
            } catch (_: Exception) {
            }
        }
        player = null
        prepared = false
    }

    private fun requestFocus() {
        if (Build.VERSION.SDK_INT >= 26) {
            val req = focusRequest ?: AudioFocusRequest.Builder(AudioManager.AUDIOFOCUS_GAIN)
                .setAudioAttributes(
                    AudioAttributes.Builder()
                        .setUsage(AudioAttributes.USAGE_MEDIA)
                        .setContentType(AudioAttributes.CONTENT_TYPE_SPEECH)
                        .build()
                )
                .setOnAudioFocusChangeListener(focusListener)
                .build().also { focusRequest = it }
            audioManager.requestAudioFocus(req)
        } else {
            @Suppress("DEPRECATION")
            audioManager.requestAudioFocus(focusListener, AudioManager.STREAM_MUSIC, AudioManager.AUDIOFOCUS_GAIN)
        }
    }

    private fun abandonFocus() {
        if (Build.VERSION.SDK_INT >= 26) {
            focusRequest?.let { audioManager.abandonAudioFocusRequest(it) }
        } else {
            @Suppress("DEPRECATION")
            audioManager.abandonAudioFocus(focusListener)
        }
    }
}
