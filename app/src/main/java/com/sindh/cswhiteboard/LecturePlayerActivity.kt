package com.sindh.cswhiteboard

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.sindh.cswhiteboard.data.CurriculumRepository
import com.sindh.cswhiteboard.data.Lecture
import com.sindh.cswhiteboard.data.Prefs
import com.sindh.cswhiteboard.databinding.ActivityPlayerBinding
import com.sindh.cswhiteboard.voice.LectureNarrator

class LecturePlayerActivity : AppCompatActivity() {

    private lateinit var binding: ActivityPlayerBinding
    private var narrator: LectureNarrator? = null
    private var lecture: Lecture? = null
    private var classId: String = ""
    private var chapterId: String = ""
    private var playChapter = false
    private var index = 0
    private var autoplay = true
    private var drawDone = false
    private var speakDone = false
    private var advancing = false

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(Prefs.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityPlayerBinding.inflate(layoutInflater)
        setContentView(binding.root)

        classId = intent.getStringExtra(HomeActivity.EXTRA_CLASS_ID).orEmpty()
        chapterId = intent.getStringExtra(HomeActivity.EXTRA_CHAPTER_ID).orEmpty()
        playChapter = intent.getBooleanExtra(HomeActivity.EXTRA_PLAY_CHAPTER, false)
        val lectureId = intent.getStringExtra(HomeActivity.EXTRA_LECTURE_ID) ?: return finish()
        lecture = CurriculumRepository.lecture(this, lectureId)?.second ?: return finish()
        index = savedInstanceState?.getInt(STATE_INDEX) ?: 0

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        binding.toolbar.setNavigationOnClickListener { finish() }

        narrator = LectureNarrator(
            context = this,
            onReady = { },
            onSpeaking = { speaking ->
                runOnUiThread { binding.voiceDot.alpha = if (speaking) 1f else 0.35f }
            },
            onUtteranceDone = { runOnUiThread { onSpeakDone() } },
            onIssue = { msg -> runOnUiThread { Toast.makeText(this, msg, Toast.LENGTH_LONG).show() } }
        )

        binding.board.onDrawComplete = { runOnUiThread { onDrawDone() } }
        bindLectureHeader()
        bindControls()
    }

    private fun bindLectureHeader() {
        val lec = lecture ?: return
        val urdu = Prefs.isUrdu(this)
        binding.toolbar.title = if (urdu) lec.titleUr else lec.titleEn
        binding.topicMeta.text = getString(
            R.string.segment_progress,
            (index + 1).coerceAtMost(lec.segments.size),
            lec.segments.size
        )
        if (lec.golden) {
            binding.goldenBadge.visibility = android.view.View.VISIBLE
        } else {
            binding.goldenBadge.visibility = android.view.View.GONE
        }
        binding.chipEn.isChecked = !urdu
        binding.chipUr.isChecked = urdu
        binding.btnPlay.text = if (autoplay) getString(R.string.pause) else getString(R.string.play)
    }

    private fun bindControls() {
        binding.btnPlay.setOnClickListener {
            autoplay = !autoplay
            if (autoplay) {
                if (!binding.board.isAnimating()) playSegment()
            } else {
                narrator?.stop()
            }
            bindLectureHeader()
        }
        binding.btnPrev.setOnClickListener {
            if (index > 0) {
                index--
                playSegment(resetBoard = true)
            }
        }
        binding.btnNext.setOnClickListener {
            goNext(force = true)
        }
        binding.chipEn.setOnClickListener {
            Prefs.setLanguage(this, Prefs.LANG_EN)
            bindLectureHeader()
            playSegment()
        }
        binding.chipUr.setOnClickListener {
            Prefs.setLanguage(this, Prefs.LANG_UR)
            bindLectureHeader()
            playSegment()
        }
        binding.btnSlow.setOnClickListener {
            Prefs.setSpeechRate(this, 0.8f)
            Toast.makeText(this, R.string.speed_slow, Toast.LENGTH_SHORT).show()
        }
        binding.btnNormal.setOnClickListener {
            Prefs.setSpeechRate(this, 0.92f)
        }
        binding.btnFast.setOnClickListener {
            Prefs.setSpeechRate(this, 1.12f)
            Toast.makeText(this, R.string.speed_fast, Toast.LENGTH_SHORT).show()
        }
        binding.btnTts.setOnClickListener { LectureNarrator.openSettings(this) }
        binding.board.post { playSegment() }
    }

    private fun playSegment(resetBoard: Boolean = false) {
        val lec = lecture ?: return
        if (lec.segments.isEmpty()) return
        index = index.coerceIn(0, lec.segments.lastIndex)
        val segment = lec.segments[index]
        advancing = false
        drawDone = false
        speakDone = false
        if (segment.clear || resetBoard || index == 0) {
            binding.board.clearBoard()
        }
        bindLectureHeader()
        binding.progress.max = lec.segments.size
        binding.progress.progress = index + 1
        binding.scroll.post { binding.scroll.fullScroll(android.view.View.FOCUS_DOWN) }
        binding.board.play(segment.actions)
        val text = if (Prefs.isUrdu(this)) segment.speakUr else segment.speakEn
        narrator?.speak(text, Prefs.language(this), Prefs.speechRate(this))
    }

    private fun onDrawDone() {
        drawDone = true
        binding.scroll.post { binding.scroll.fullScroll(android.view.View.FOCUS_DOWN) }
        maybeAdvance()
    }

    private fun onSpeakDone() {
        speakDone = true
        maybeAdvance()
    }

    private fun maybeAdvance() {
        if (!autoplay || advancing) return
        if (drawDone && speakDone) {
            advancing = true
            binding.board.postDelayed({ goNext(force = false) }, 350)
        }
    }

    private fun goNext(force: Boolean) {
        val lec = lecture ?: return
        if (index + 1 < lec.segments.size) {
            index++
            playSegment()
            return
        }
        Prefs.markDone(this, lec.id)
        if (playChapter) {
            val next = nextInChapter()
            if (next != null) {
                lecture = next
                index = 0
                Toast.makeText(this, next.titleEn, Toast.LENGTH_SHORT).show()
                playSegment(resetBoard = true)
                return
            }
        }
        if (force) {
            Toast.makeText(this, R.string.lecture_complete, Toast.LENGTH_SHORT).show()
            autoplay = false
            bindLectureHeader()
        } else {
            autoplay = false
            bindLectureHeader()
            Toast.makeText(this, R.string.lecture_complete, Toast.LENGTH_SHORT).show()
        }
    }

    private fun nextInChapter(): Lecture? {
        val chapter = CurriculumRepository.chapter(this, classId, chapterId) ?: return null
        val list = if (Prefs.goldenOnly(this)) chapter.lectures.filter { it.golden } else chapter.lectures
        val i = list.indexOfFirst { it.id == lecture?.id }
        return if (i >= 0 && i + 1 < list.size) list[i + 1] else null
    }

    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        outState.putInt(STATE_INDEX, index)
    }

    override fun onPause() {
        super.onPause()
        narrator?.stop()
        autoplay = false
    }

    override fun onDestroy() {
        narrator?.shutdown()
        super.onDestroy()
    }

    companion object {
        private const val STATE_INDEX = "index"
    }
}
