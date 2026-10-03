package com.couplesguide.postures

import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.couplesguide.postures.data.TeacherGuideRepository
import com.couplesguide.postures.data.TeacherTopic
import com.couplesguide.postures.databinding.ActivityTeacherTopicDetailBinding
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.NarrationBuilder
import com.couplesguide.postures.util.VoiceNarrator

class TeacherTopicDetailActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_TOPIC_ID = "teacher_topic_id"
    }

    private lateinit var binding: ActivityTeacherTopicDetailBinding
    private lateinit var topic: TeacherTopic
    private var voiceNarrator: VoiceNarrator? = null
    private var voiceReady = false
    private var isSpeaking = false

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityTeacherTopicDetailBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val topicId = intent.getStringExtra(EXTRA_TOPIC_ID)
        val found = topicId?.let { TeacherGuideRepository.getTopicById(this, it) }
        if (found == null) {
            finish()
            return
        }
        topic = found

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
        binding.topicTitle.text = if (topic.critical) "★ ${topic.title}" else topic.title
        binding.topicMeta.text = getString(
            R.string.topic_page_range,
            topic.startPage,
            topic.endPage
        )
        binding.topicBody.text = topic.englishText
        binding.narrationHint.text = getString(R.string.urdu_voice_hint)
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_detail, menu)
        menu.findItem(R.id.action_export)?.isVisible = false
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
        if (isSpeaking) {
            voiceNarrator?.stop()
            return
        }
        if (!voiceReady) {
            Toast.makeText(this, R.string.voice_not_ready, Toast.LENGTH_SHORT).show()
            return
        }
        val text = NarrationBuilder.buildTeacherTopicNarration(topic)
        if (text.isBlank()) {
            Toast.makeText(this, R.string.urdu_narration_missing, Toast.LENGTH_LONG).show()
            return
        }
        if (voiceNarrator?.speak(text, LocaleHelper.NARRATION_LANG) != true) {
            Toast.makeText(this, R.string.voice_install_prompt, Toast.LENGTH_LONG).show()
        }
    }

    override fun onSupportNavigateUp(): Boolean {
        finish()
        return true
    }

    override fun onDestroy() {
        voiceNarrator?.shutdown()
        voiceNarrator = null
        super.onDestroy()
    }
}
