package com.sindhcs.lectures

import android.annotation.SuppressLint
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.os.SystemClock
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
    private var readMs = 0L
    private var usingRangeSync = false
    private var speechStartedAt = 0L
    private val main = Handler(Looper.getMainLooper())
    private val clockSync = object : Runnable {
        override fun run() {
            if (!speaking || usingRangeSync || readMs <= 0) return
            val elapsed = SystemClock.elapsedRealtime() - speechStartedAt
            scrollBoard((elapsed.toFloat() / readMs).coerceIn(0f, 1f))
            main.postDelayed(this, 250)
        }
    }

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
        readMs = topic.readSeconds.coerceAtLeast(1) * 1000L

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
        val boardPath = topic.board.ifBlank { "whiteboards/missing.html" }
        board.loadUrl("file:///android_asset/$boardPath")

        narrator = UrduNarrator(
            context = this,
            onReadyChanged = { },
            onSpeakingChanged = { on ->
                speaking = on
                binding.listenButton.text = getString(if (on) R.string.stop_lecture else R.string.listen_urdu)
                if (!on) {
                    main.removeCallbacks(clockSync)
                    scrollBoard(1f)
                }
            },
            onProgress = { fraction ->
                usingRangeSync = true
                scrollBoard(fraction)
            },
            onLanguageIssue = { msg -> Toast.makeText(this, msg, Toast.LENGTH_LONG).show() }
        )

        binding.listenButton.setOnClickListener {
            if (speaking) stopLecture() else startLecture()
        }
        binding.ttsHelp.setOnClickListener { UrduNarrator.openTtsSettings(this) }
    }

    private fun startLecture() {
        usingRangeSync = false
        speechStartedAt = SystemClock.elapsedRealtime()
        scrollBoard(0f)
        val ok = narrator?.speak(spoken) == true
        if (!ok) {
            UrduNarrator.openTtsSettings(this)
            return
        }
        main.removeCallbacks(clockSync)
        main.postDelayed(clockSync, 250)
    }

    private fun stopLecture() {
        main.removeCallbacks(clockSync)
        narrator?.stop()
    }

    private fun scrollBoard(fraction: Float) {
        val f = fraction.coerceIn(0f, 1f)
        binding.board.evaluateJavascript(
            "(function(f){var el=document.scrollingElement||document.documentElement;" +
                "var max=Math.max(0,el.scrollHeight-window.innerHeight);" +
                "window.scrollTo(0,max*f);})($f);",
            null
        )
    }

    override fun onPause() {
        stopLecture()
        binding.board.onPause()
        super.onPause()
    }

    override fun onResume() {
        super.onResume()
        binding.board.onResume()
    }

    override fun onDestroy() {
        main.removeCallbacks(clockSync)
        narrator?.shutdown()
        binding.board.destroy()
        super.onDestroy()
    }
}
