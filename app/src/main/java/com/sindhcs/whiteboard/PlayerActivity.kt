package com.sindhcs.whiteboard

import android.content.Intent
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.text.SpannableString
import android.text.Spanned
import android.text.style.BackgroundColorSpan
import android.view.Menu
import android.view.MenuItem
import android.view.WindowManager
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import com.sindhcs.whiteboard.data.Catalog
import com.sindhcs.whiteboard.data.CatalogStore
import com.sindhcs.whiteboard.data.Lecture
import com.sindhcs.whiteboard.data.ProgressStore
import com.sindhcs.whiteboard.databinding.ActivityPlayerBinding
import com.sindhcs.whiteboard.voice.LectureVoice

class PlayerActivity : AppCompatActivity() {

    private lateinit var binding: ActivityPlayerBinding
    private lateinit var catalog: Catalog
    private lateinit var progress: ProgressStore
    private lateinit var lecture: Lecture
    private lateinit var voice: LectureVoice
    private val handler = Handler(Looper.getMainLooper())

    private var boardIndex = 0
    private var generation = 0
    private var userPaused = false
    private var started = false
    private var voiceReady = false
    private var voiceMissingToast = false
    private var speechDone = false
    private var drawDone = false
    private var advancePosted = false
    private var speed = 1f

    private val speeds = floatArrayOf(0.9f, 1f, 1.15f)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityPlayerBinding.inflate(layoutInflater)
        setContentView(binding.root)
        catalog = CatalogStore.get(this)
        progress = ProgressStore(this)
        speed = progress.speed()
        val lectureId = intent.getStringExtra(EXTRA_LECTURE_ID)
        lecture = runCatching { catalog.lecture(lectureId ?: "") }.getOrElse {
            finish()
            return
        }
        setSupportActionBar(binding.toolbar)
        val chapter = catalog.chapterOf(lecture.id)
        binding.toolbar.title = lecture.title
        binding.toolbar.subtitle = chapter?.title
        binding.toolbar.setNavigationOnClickListener { finish() }

        boardIndex = savedInstanceState?.getInt(STATE_BOARD)
            ?: progress.boardIndex(lecture.id).coerceIn(0, lecture.boards.lastIndex)
        userPaused = savedInstanceState?.getBoolean(STATE_PAUSED) ?: false

        voice = LectureVoice(
            context = this,
            onReady = { ready ->
                voiceReady = ready
                if (!ready && !voiceMissingToast) {
                    voiceMissingToast = true
                    Toast.makeText(this, R.string.voice_unavailable, Toast.LENGTH_LONG).show()
                }
            },
            onSpeaking = { speaking ->
                if (speaking) updateStatus(getString(R.string.speaking))
            },
            onRange = { start, end -> highlightCaption(start, end) },
            onDone = {
                val gen = generation
                if (gen == generation) {
                    speechDone = true
                    tryAdvance(gen)
                }
            }
        )
        voice.setRate(speed)

        binding.board.onDrawComplete = {
            drawDone = true
            tryAdvance(generation)
        }
        binding.board.setSpeed(speed)
        binding.prevButton.setOnClickListener { showBoard((boardIndex - 1).coerceAtLeast(0)) }
        binding.nextButton.setOnClickListener { showBoard((boardIndex + 1).coerceAtMost(lecture.boards.lastIndex)) }
        binding.playButton.setOnClickListener { togglePause() }
        binding.nextLectureButton.setOnClickListener { openNextLecture() }
    }

    override fun onResume() {
        super.onResume()
        window.addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)
        if (!started) {
            started = true
            showBoard(boardIndex)
            if (userPaused) pausePlayback()
        } else if (!userPaused) {
            resumeAfterBackground()
        }
    }

    override fun onPause() {
        window.clearFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON)
        holdPlayback()
        super.onPause()
    }

    override fun onDestroy() {
        handler.removeCallbacksAndMessages(null)
        if (::voice.isInitialized) voice.shutdown()
        super.onDestroy()
    }

    override fun onSaveInstanceState(outState: Bundle) {
        outState.putInt(STATE_BOARD, boardIndex)
        outState.putBoolean(STATE_PAUSED, userPaused)
        super.onSaveInstanceState(outState)
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_player, menu)
        menu.findItem(R.id.action_speed).title = speedLabel()
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        when (item.itemId) {
            R.id.action_speed -> {
                val index = speeds.indexOfFirst { kotlin.math.abs(it - speed) < 0.01f }
                speed = speeds[(index + 1) % speeds.size]
                progress.setSpeed(speed)
                voice.setRate(speed)
                binding.board.setSpeed(speed)
                invalidateOptionsMenu()
                return true
            }
            R.id.action_replay -> {
                userPaused = false
                showBoard(0)
                return true
            }
            R.id.action_voice_help -> {
                AlertDialog.Builder(this)
                    .setTitle(R.string.voice_help_title)
                    .setMessage(R.string.voice_help_body)
                    .setPositiveButton(android.R.string.ok, null)
                    .show()
                return true
            }
        }
        return super.onOptionsItemSelected(item)
    }

    private fun showBoard(index: Int) {
        boardIndex = index
        generation += 1
        val gen = generation
        handler.removeCallbacksAndMessages(null)
        speechDone = false
        drawDone = false
        advancePosted = false
        binding.nextLectureButton.visibility = android.view.View.GONE
        val board = lecture.boards[index]
        binding.caption.text = board.narration
        binding.board.submit(board.marks)
        binding.board.setSpeed(speed)
        progress.save(lecture.id, index)
        updateStatus(getString(R.string.drawing))
        binding.playButton.text = getString(R.string.pause)
        if (!userPaused) {
            binding.board.play()
            voice.speak(board.narration)
            val wait = maxOf(estimateSpeech(board.narration), binding.board.durationMs() + 500L)
            handler.postDelayed({
                if (gen != generation || speechDone) return@postDelayed
                speechDone = true
                tryAdvance(gen)
            }, wait)
        }
    }

    private fun tryAdvance(gen: Int) {
        if (gen != generation || userPaused || advancePosted) return
        if (!speechDone || !drawDone) return
        advancePosted = true
        if (boardIndex < lecture.boards.lastIndex) {
            handler.postDelayed({
                if (gen == generation && !userPaused) showBoard(boardIndex + 1)
            }, 700L)
        } else {
            handler.postDelayed({
                if (gen != generation) return@postDelayed
                updateStatus(getString(R.string.lecture_complete))
                binding.playButton.text = getString(R.string.replay)
                val next = catalog.nextInGrade(lecture.id)
                binding.nextLectureButton.visibility = if (next == null) android.view.View.GONE else android.view.View.VISIBLE
            }, 400L)
        }
    }

    private fun togglePause() {
        if (boardIndex == lecture.boards.lastIndex && speechDone && drawDone) {
            userPaused = false
            showBoard(0)
            return
        }
        userPaused = !userPaused
        if (userPaused) pausePlayback() else resumePlayback()
    }

    private fun pausePlayback() {
        userPaused = true
        handler.removeCallbacksAndMessages(null)
        binding.board.pause()
        voice.stop()
        binding.playButton.text = getString(R.string.play)
        updateStatus(getString(R.string.paused))
    }

    private fun resumeAfterBackground() {
        if (binding.board.isComplete()) drawDone = true else binding.board.resume()
        if (speechDone && drawDone) {
            tryAdvance(generation)
            return
        }
        if (!speechDone) {
            val gen = generation
            voice.speak(lecture.boards[boardIndex].narration)
            handler.postDelayed({
                if (gen != generation || speechDone) return@postDelayed
                speechDone = true
                tryAdvance(gen)
            }, estimateSpeech(lecture.boards[boardIndex].narration))
        }
        binding.playButton.text = getString(R.string.pause)
    }

    private fun resumePlayback() {
        userPaused = false
        binding.playButton.text = getString(R.string.pause)
        if (binding.board.isComplete()) {
            drawDone = true
        } else {
            binding.board.resume()
        }
        speechDone = false
        advancePosted = false
        val gen = generation
        voice.speak(lecture.boards[boardIndex].narration)
        val wait = estimateSpeech(lecture.boards[boardIndex].narration)
        handler.postDelayed({
            if (gen != generation || speechDone) return@postDelayed
            speechDone = true
            tryAdvance(gen)
        }, wait)
    }

    private fun holdPlayback() {
        handler.removeCallbacksAndMessages(null)
        binding.board.pause()
        voice.stop()
    }

    private fun openNextLecture() {
        val next = catalog.nextInGrade(lecture.id) ?: return
        startActivity(Intent(this, PlayerActivity::class.java).apply {
            putExtra(EXTRA_LECTURE_ID, next.id)
        })
        finish()
    }

    private fun updateStatus(state: String) {
        binding.status.text = getString(R.string.board_counter, boardIndex + 1, lecture.boards.size) + " · " + state
    }

    private fun highlightCaption(start: Int, end: Int) {
        val text = lecture.boards.getOrNull(boardIndex)?.narration ?: return
        if (start < 0 || end > text.length || start >= end) return
        val span = SpannableString(text)
        span.setSpan(
            BackgroundColorSpan(ContextCompat.getColor(this, R.color.board_line)),
            start,
            end,
            Spanned.SPAN_EXCLUSIVE_EXCLUSIVE
        )
        binding.caption.text = span
    }

    private fun estimateSpeech(text: String): Long {
        val words = text.split(Regex("\\s+")).count { it.isNotBlank() }
        return (words * 650L / speed).toLong() + 4000L
    }

    private fun speedLabel(): String = when {
        speed < 0.95f -> "0.9x"
        speed > 1.05f -> "1.15x"
        else -> "1x"
    }

    companion object {
        const val EXTRA_LECTURE_ID = "lecture_id"
        private const val STATE_BOARD = "board"
        private const val STATE_PAUSED = "paused"
    }
}
