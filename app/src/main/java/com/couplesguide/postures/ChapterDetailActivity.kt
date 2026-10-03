package com.couplesguide.postures

import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.view.View
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.couplesguide.postures.data.CsTopic
import com.couplesguide.postures.data.CsTeacherRepository
import com.couplesguide.postures.databinding.ActivityChapterDetailBinding
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.NarrationBuilder
import com.couplesguide.postures.util.VoiceNarrator

class ChapterDetailActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_TOPIC_ID = "topic_id"
    }

    private lateinit var binding: ActivityChapterDetailBinding
    private lateinit var topic: CsTopic
    private var voiceNarrator: VoiceNarrator? = null
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

        voiceNarrator = VoiceNarrator(
            context = this,
            onReadyChanged = { ready -> voiceReady = ready },
            onSpeakingChanged = { speaking ->
                isSpeaking = speaking
                invalidateOptionsMenu()
            },
            onLanguageIssue = { message ->
                Toast.makeText(this, message, Toast.LENGTH_LONG).show()
            }
        )

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        bindContent()
    }

    private fun bindContent() {
        supportActionBar?.title = topic.title
        binding.illustration.visibility = View.GONE
        binding.chapterTitle.text = if (topic.golden) "★ ${topic.title}" else topic.title
        binding.chapterSummary.text = getString(
            R.string.topic_meta,
            topic.sourcePage,
            getString(if (topic.golden) R.string.golden_topic else R.string.standard_topic)
        )
        binding.chapterBody.text = topic.english
        binding.keyPointsList.visibility = View.GONE
        binding.keyPointsHeader.visibility = View.GONE
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
            toggleNarration()
            return true
        }
        return super.onOptionsItemSelected(item)
    }

    private fun toggleNarration() {
        val narrator = voiceNarrator ?: return
        if (narrator.isSpeaking()) {
            narrator.stop()
            return
        }
        if (!voiceReady) {
            Toast.makeText(this, R.string.voice_not_ready, Toast.LENGTH_SHORT).show()
            return
        }
        val text = NarrationBuilder.buildTopicNarration(topic)
        narrator.speak(text, LocaleHelper.LANG_UR)
    }

    override fun onDestroy() {
        voiceNarrator?.shutdown()
        voiceNarrator = null
        super.onDestroy()
    }
}
