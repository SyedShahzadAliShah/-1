package com.sindhcs.lectures

import android.annotation.SuppressLint
import android.os.Bundle
import android.view.View
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
    private var beats: List<String> = emptyList()

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
        beats = topic.beats.ifEmpty {
            listOf(topic.spokenUrdu).filter { it.isNotBlank() }
        }

        val board = binding.board
        board.setBackgroundColor(0xFF07090D.toInt())
        board.isVerticalScrollBarEnabled = false
        board.isHorizontalScrollBarEnabled = false
        board.overScrollMode = View.OVER_SCROLL_NEVER
        board.webViewClient = WebViewClient()
        board.settings.javaScriptEnabled = true
        board.settings.domStorageEnabled = true
        board.settings.allowFileAccess = true
        board.settings.loadWithOverviewMode = true
        board.settings.useWideViewPort = true
        board.settings.setSupportZoom(false)
        board.settings.builtInZoomControls = false
        board.settings.displayZoomControls = false
        board.settings.mixedContentMode = WebSettings.MIXED_CONTENT_COMPATIBILITY_MODE
        board.settings.cacheMode = WebSettings.LOAD_DEFAULT
        val boardPath = topic.board.ifBlank { "whiteboards/missing.html" }
        board.loadUrl("file:///android_asset/$boardPath")

        narrator = UrduNarrator(
            context = this,
            onReadyChanged = { },
            onSpeakingChanged = { on ->
                speaking = on
                binding.listenButton.text = getString(if (on) R.string.stop_lecture else R.string.listen_urdu)
                if (!on) highlightBeat(-1)
            },
            onBeat = { highlightBeat(it) },
            onLanguageIssue = { msg -> Toast.makeText(this, msg, Toast.LENGTH_LONG).show() }
        )

        binding.listenButton.setOnClickListener {
            if (speaking) {
                narrator?.stop()
                highlightBeat(-1)
            } else {
                val ok = narrator?.speakBeats(beats) == true
                if (!ok) UrduNarrator.openTtsSettings(this)
            }
        }
        binding.ttsHelp.setOnClickListener { UrduNarrator.openTtsSettings(this) }
    }

    private fun highlightBeat(index: Int) {
        val js = if (index < 0) {
            "window.LectureBoard&&LectureBoard.clearLive()"
        } else {
            "window.LectureBoard&&LectureBoard.showBeat($index)"
        }
        binding.board.evaluateJavascript(js, null)
    }

    override fun onPause() {
        narrator?.stop()
        highlightBeat(-1)
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
