package com.couplesguide.postures

import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.couplesguide.postures.data.CsTopic
import com.couplesguide.postures.data.CsTeacherRepository
import com.couplesguide.postures.data.SketchnoteFrame
import com.couplesguide.postures.databinding.ActivityChapterDetailBinding
import com.couplesguide.postures.util.LectureSyncNarrator

class ChapterDetailActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_TOPIC_ID = "topic_id"
    }

    private lateinit var binding: ActivityChapterDetailBinding
    private lateinit var topic: CsTopic
    private lateinit var frames: List<SketchnoteFrame>
    private var lectureNarrator: LectureSyncNarrator? = null
    private var voiceReady = false
    private var isSpeaking = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityChapterDetailBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val topicId = intent.getStringExtra(EXTRA_TOPIC_ID)
        val found = topicId?.let { CsTeacherRepository.getTopic(this, it) }
        if (found == null) {
            finish()
            return
        }
        topic = found.second
        frames = topic.sketchnoteFrames.ifEmpty { fallbackFrames(topic) }

        lectureNarrator = LectureSyncNarrator(
            context = this,
            onReadyChanged = { ready -> voiceReady = ready },
            onSpeakingChanged = { speaking ->
                isSpeaking = speaking
                invalidateOptionsMenu()
                binding.playLectureButton.text = if (speaking) {
                    getString(R.string.stop)
                } else {
                    getString(R.string.play_sketchnote_lecture)
                }
            },
            onFrameStart = { index -> showFrame(index) },
            onLanguageIssue = { message ->
                Toast.makeText(this, message, Toast.LENGTH_LONG).show()
            }
        )

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        bindContent()
        binding.playLectureButton.setOnClickListener { toggleLecture() }
    }

    private fun fallbackFrames(topic: CsTopic): List<SketchnoteFrame> {
        return listOf(
            SketchnoteFrame(
                index = 0,
                english = topic.english.lineSequence().firstOrNull { it.isNotBlank() } ?: topic.title,
                urdu = topic.urduNarration,
                visual = "concept"
            )
        )
    }

    private fun bindContent() {
        supportActionBar?.title = topic.title
        binding.chapterTitle.text = if (topic.golden) "★ ${topic.title}" else topic.title
        binding.chapterSummary.text = getString(
            R.string.topic_meta,
            topic.sourcePage,
            getString(if (topic.golden) R.string.golden_topic else R.string.standard_topic)
        )
        binding.chapterBody.text = topic.english
        binding.sketchnoteView.setLecture(frames, topic.golden, topic.pageImage)
        showFrame(0)
    }

    private fun showFrame(index: Int) {
        val frame = frames.getOrNull(index) ?: return
        binding.sketchnoteView.setActiveFrame(index)
        binding.frameCaption.text = getString(R.string.sketchnote_frame_caption, index + 1, frames.size, frame.english)
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_detail, menu)
        val listenItem = menu.findItem(R.id.action_listen)
        listenItem.title = if (isSpeaking) getString(R.string.stop) else getString(R.string.listen_urdu)
        listenItem.setIcon(
            if (isSpeaking) android.R.drawable.ic_media_pause
            else android.R.drawable.ic_media_play
        )
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        if (item.itemId == R.id.action_listen) {
            toggleLecture()
            return true
        }
        return super.onOptionsItemSelected(item)
    }

    private fun toggleLecture() {
        val narrator = lectureNarrator ?: return
        if (narrator.isSpeaking()) {
            narrator.stop()
            return
        }
        if (!voiceReady) {
            Toast.makeText(this, R.string.voice_not_ready, Toast.LENGTH_SHORT).show()
            return
        }
        showFrame(0)
        narrator.speakLecture(frames)
    }

    override fun onDestroy() {
        binding.sketchnoteView.stopAnimations()
        lectureNarrator?.shutdown()
        lectureNarrator = null
        super.onDestroy()
    }
}
