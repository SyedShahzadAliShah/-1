package com.sindhcs.lectures

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.sindhcs.lectures.data.LectureRepository
import com.sindhcs.lectures.databinding.ActivityTopicBinding
import com.sindhcs.lectures.util.UrduNarrator

class TopicActivity : AppCompatActivity() {
    private lateinit var binding: ActivityTopicBinding
    private var narrator: UrduNarrator? = null
    private var speaking = false
    private var spoken = ""

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityTopicBinding.inflate(layoutInflater)
        setContentView(binding.root)
        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        binding.toolbar.setNavigationOnClickListener { finish() }

        val gradeId = intent.getStringExtra(MainActivity.EXTRA_GRADE) ?: return finish()
        val chNum = intent.getIntExtra(MainActivity.EXTRA_CHAPTER, 0)
        val topicId = intent.getStringExtra(MainActivity.EXTRA_TOPIC) ?: return finish()
        val topic = LectureRepository.topic(this, gradeId, chNum, topicId) ?: return finish()
        val chapter = LectureRepository.chapter(this, gradeId, chNum)

        title = getString(R.string.lecture)
        spoken = topic.spokenUrdu
        binding.topicTitle.text = topic.title
        binding.chapterLabel.text = chapter?.let { "Chapter ${it.num} · ${it.title}" } ?: ""
        binding.goldenChip.visibility = if (topic.golden) android.view.View.VISIBLE else android.view.View.GONE
        binding.learnText.text = topic.learn.ifBlank { getString(R.string.no_english) }
        binding.urduText.text = topic.urdu.ifBlank { getString(R.string.no_urdu) }
        binding.urduText.textDirection = android.view.View.TEXT_DIRECTION_RTL

        narrator = UrduNarrator(
            context = this,
            onReadyChanged = { },
            onSpeakingChanged = { on ->
                speaking = on
                binding.listenButton.text = getString(if (on) R.string.stop_lecture else R.string.listen_urdu)
            },
            onLanguageIssue = { msg -> Toast.makeText(this, msg, Toast.LENGTH_LONG).show() }
        )

        binding.listenButton.setOnClickListener {
            if (speaking) {
                narrator?.stop()
            } else {
                val ok = narrator?.speak(spoken) == true
                if (!ok) UrduNarrator.openTtsSettings(this)
            }
        }
        binding.ttsHelp.setOnClickListener { UrduNarrator.openTtsSettings(this) }
    }

    override fun onPause() {
        narrator?.stop()
        super.onPause()
    }

    override fun onDestroy() {
        narrator?.shutdown()
        super.onDestroy()
    }
}
