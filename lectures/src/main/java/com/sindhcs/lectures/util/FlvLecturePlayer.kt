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
        it.playWhenReady = true
        view.player = it
    }

    fun playAsset(assetPath: String): Boolean {
        if (assetPath.isBlank()) return false
        val uri = Uri.parse("asset:///$assetPath")
        player.setMediaItem(MediaItem.fromUri(uri))
        player.prepare()
        player.play()
        return true
    }

    fun replay() {
        player.seekTo(0)
        player.play()
    }

    fun pause() {
        player.pause()
    }

    fun release() {
        view.player = null
        player.release()
    }
}
