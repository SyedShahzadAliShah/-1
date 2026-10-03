package com.couplesguide.postures.util

import android.content.Context
import com.couplesguide.postures.data.SketchnoteFrame

/**
 * Speaks each sketchnote frame in Urdu and notifies the UI when a new frame starts.
 */
class LectureSyncNarrator(
    context: Context,
    private val onReadyChanged: (Boolean) -> Unit,
    private val onSpeakingChanged: (Boolean) -> Unit,
    private val onFrameStart: (Int) -> Unit,
    private val onLanguageIssue: ((String) -> Unit)? = null
) {
    private val narrator = VoiceNarrator(
        context = context,
        onReadyChanged = onReadyChanged,
        onSpeakingChanged = onSpeakingChanged,
        onLanguageIssue = onLanguageIssue
    )

    fun speakLecture(frames: List<SketchnoteFrame>) {
        val segments = frames.map { it.urdu.ifBlank { it.english } }
        narrator.speakSegments(segments, LocaleHelper.LANG_UR) { index ->
            onFrameStart(index)
        }
    }

    fun stop() = narrator.stop()

    fun isSpeaking(): Boolean = narrator.isSpeaking()

    fun shutdown() = narrator.shutdown()
}
