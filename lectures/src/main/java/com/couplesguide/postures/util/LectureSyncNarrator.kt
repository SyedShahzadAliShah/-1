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
        if (frames.isEmpty()) return
        val segments = buildAlignedSegments(frames)
        narrator.speakSegments(segments, LocaleHelper.LANG_UR) { index ->
            onFrameStart(index.coerceIn(0, frames.lastIndex))
        }
    }

    private fun buildAlignedSegments(frames: List<SketchnoteFrame>): List<String> {
        val fallbackPool = frames
            .map { it.urdu.trim() }
            .filter { it.isNotEmpty() }
            .flatMap { it.split(Regex("(?<=[۔!؟])\\s+")) }
            .map { it.trim() }
            .filter { it.isNotEmpty() }

        return frames.mapIndexed { index, frame ->
            when {
                frame.urdu.isNotBlank() -> frame.urdu.trim()
                fallbackPool.isNotEmpty() -> fallbackPool[index % fallbackPool.size]
                frame.english.isNotBlank() -> frame.english.trim()
                else -> "لیکچر قدم ${index + 1}"
            }
        }
    }

    fun stop() = narrator.stop()

    fun isSpeaking(): Boolean = narrator.isSpeaking()

    fun shutdown() = narrator.shutdown()
}
