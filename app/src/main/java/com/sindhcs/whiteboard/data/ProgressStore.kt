package com.sindhcs.whiteboard.data

import android.content.Context

class ProgressStore(context: Context) {
    private val prefs = context.applicationContext.getSharedPreferences(PREFS, Context.MODE_PRIVATE)

    fun save(lectureId: String, board: Int) {
        prefs.edit()
            .putString(KEY_LAST, lectureId)
            .putInt(boardKey(lectureId), board)
            .apply()
    }

    fun lastLectureId(): String? = prefs.getString(KEY_LAST, null)

    fun boardIndex(lectureId: String): Int = prefs.getInt(boardKey(lectureId), 0)

    fun speed(): Float = prefs.getFloat(KEY_SPEED, 1f)

    fun setSpeed(speed: Float) {
        prefs.edit().putFloat(KEY_SPEED, speed).apply()
    }

    private fun boardKey(lectureId: String) = "board_$lectureId"

    companion object {
        private const val PREFS = "lecture_progress"
        private const val KEY_LAST = "last"
        private const val KEY_SPEED = "speed"
    }
}
