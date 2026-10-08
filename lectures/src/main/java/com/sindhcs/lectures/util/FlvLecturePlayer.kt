package com.sindhcs.lectures.util

import android.content.Context
import android.net.Uri
import androidx.media3.common.MediaItem
import androidx.media3.common.Player
import androidx.media3.exoplayer.ExoPlayer
import androidx.media3.ui.PlayerView

class FlvLecturePlayer(
    context: Context,
    private val view: PlayerView
) {
    private val player: ExoPlayer = ExoPlayer.Builder(context.applicationContext).build().also {
        it.repeatMode = Player.REPEAT_MODE_OFF
        it.playWhenReady = false
        view.player = it
    }

    fun prepareAsset(assetPath: String): Boolean {
        if (assetPath.isBlank()) return false
        val uri = Uri.parse("asset:///$assetPath")
        player.setMediaItem(MediaItem.fromUri(uri))
        player.prepare()
        player.seekTo(0)
        player.playWhenReady = false
        return true
    }

    fun playFree() {
        player.seekTo(0)
        player.playWhenReady = true
        player.play()
    }

    fun followSpeech(fraction: Float) {
        val duration = player.duration
        if (duration <= 0) return
        val position = (duration * fraction.coerceIn(0f, 1f)).toLong().coerceAtMost(duration - 40)
        player.playWhenReady = false
        player.seekTo(position)
    }

    fun pause() {
        player.pause()
        player.playWhenReady = false
    }

    fun release() {
        view.player = null
        player.release()
    }
}
