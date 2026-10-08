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
import com.sindhcs.lectures.util.FlvLecturePlayer
import com.sindhcs.lectures.util.UrduNarrator
import java.io.FileNotFoundException

class TopicActivity : AppCompatActivity() {
    private lateinit var binding: ActivityTopicBinding
    private var narrator: UrduNarrator? = null
    private var flvPlayer: FlvLecturePlayer? = null
    private var speaking = false
    private var spoken = ""
    private var showingBoard = false

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
        val boardPath = topic.board.ifBlank { "whiteboards/missing.html" }
        board.loadUrl("file:///android_asset/$boardPath")

        val hasFlv = topic.flv.isNotBlank() && assetExists(topic.flv)
        if (hasFlv) {
            flvPlayer = FlvLecturePlayer(this, binding.player)
            showVideo(replay = false)
            flvPlayer?.playAsset(topic.flv)
        } else {
            showBoard()
        }

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
        binding.replayVideo.setOnClickListener {
            if (hasFlv) {
                showVideo(replay = true)
            }
        }
        binding.toggleBoard.setOnClickListener {
            if (showingBoard && hasFlv) showVideo(replay = true) else showBoard()
        }
        binding.ttsHelp.setOnClickListener { UrduNarrator.openTtsSettings(this) }
        binding.replayVideo.visibility = if (hasFlv) View.VISIBLE else View.GONE
        binding.toggleBoard.visibility = if (hasFlv) View.VISIBLE else View.GONE
    }

    private fun assetExists(path: String): Boolean {
        return try {
            assets.open(path).close()
            true
        } catch (_: FileNotFoundException) {
            false
        }
    }

    private fun showVideo(replay: Boolean) {
        showingBoard = false
        binding.player.visibility = View.VISIBLE
        binding.board.visibility = View.GONE
        binding.toggleBoard.text = getString(R.string.open_board)
        if (replay) flvPlayer?.replay()
    }

    private fun showBoard() {
        showingBoard = true
        flvPlayer?.pause()
        binding.player.visibility = View.GONE
        binding.board.visibility = View.VISIBLE
        binding.toggleBoard.text = getString(R.string.show_flv)
    }

    override fun onPause() {
        narrator?.stop()
        flvPlayer?.pause()
        binding.board.onPause()
        super.onPause()
    }

    override fun onResume() {
        super.onResume()
        binding.board.onResume()
    }

    override fun onDestroy() {
        narrator?.shutdown()
        flvPlayer?.release()
        binding.board.destroy()
        super.onDestroy()
    }
}
