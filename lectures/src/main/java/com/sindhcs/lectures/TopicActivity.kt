package com.sindhcs.lectures

import android.annotation.SuppressLint
import android.os.Bundle
import android.webkit.WebSettings
import android.webkit.WebViewClient
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

    @SuppressLint("SetJavaScriptEnabled")
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

        title = getString(R.string.lecture)
        spoken = topic.spokenUrdu

        val board = binding.board
        board.setBackgroundColor(0xFF07090D.toInt())
        board.webViewClient = WebViewClient()
        board.settings.javaScriptEnabled = true
        board.settings.domStorageEnabled = true
        board.settings.allowFileAccess = true
        board.settings.loadWithOverviewMode = true
        board.settings.useWideViewPort = true
        board.settings.builtInZoomControls = true
        board.settings.displayZoomControls = false
        board.settings.mixedContentMode = WebSettings.MIXED_CONTENT_COMPATIBILITY_MODE
        board.settings.cacheMode = WebSettings.LOAD_DEFAULT
        val path = topic.board.ifBlank { "whiteboards/missing.html" }
        board.loadUrl("file:///android_asset/$path")

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
        binding.board.onPause()
        super.onPause()
    }

    override fun onResume() {
        super.onResume()
        binding.board.onResume()
    }

    override fun onDestroy() {
        narrator?.shutdown()
        binding.board.destroy()
        super.onDestroy()
    }
}
