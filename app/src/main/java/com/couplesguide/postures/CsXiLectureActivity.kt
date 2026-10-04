package com.couplesguide.postures

import android.annotation.SuppressLint
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.webkit.JavascriptInterface
import android.webkit.WebChromeClient
import android.webkit.WebResourceRequest
import android.webkit.WebView
import android.webkit.WebViewClient
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.couplesguide.postures.databinding.ActivityCsXiLectureBinding
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.VoiceNarrator

class CsXiLectureActivity : AppCompatActivity() {

    private lateinit var binding: ActivityCsXiLectureBinding
    private var voiceNarrator: VoiceNarrator? = null

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    @SuppressLint("SetJavaScriptEnabled")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityCsXiLectureBinding.inflate(layoutInflater)
        setContentView(binding.root)
        setSupportActionBar(binding.toolbar)

        voiceNarrator = VoiceNarrator(
            context = this,
            onReadyChanged = { },
            onSpeakingChanged = { speaking ->
                if (!speaking) {
                    binding.lectureWebView.post {
                        binding.lectureWebView.evaluateJavascript(
                            "window.dispatchEvent(new Event('native-tts-end'))",
                            null
                        )
                    }
                }
            },
            onLanguageIssue = { msg -> Toast.makeText(this, msg, Toast.LENGTH_SHORT).show() }
        )

        binding.lectureWebView.settings.apply {
            javaScriptEnabled = true
            domStorageEnabled = true
            allowFileAccess = true
            allowContentAccess = true
            builtInZoomControls = true
            displayZoomControls = false
            mediaPlaybackRequiresUserGesture = false
        }
        binding.lectureWebView.webChromeClient = WebChromeClient()
        binding.lectureWebView.webViewClient = object : WebViewClient() {
            override fun shouldOverrideUrlLoading(view: WebView?, request: WebResourceRequest?): Boolean {
                val url = request?.url?.toString() ?: return false
                if (url.startsWith("file://") || url.startsWith("https://")) {
                    return false
                }
                return true
            }
        }
        binding.lectureWebView.addJavascriptInterface(
            AndroidLectureBridge(voiceNarrator),
            "AndroidLecture"
        )
        binding.lectureWebView.loadUrl("file:///android_asset/cs-xi-lectures/index.html")
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_cs_xi, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            R.id.action_handbook -> {
                startActivity(android.content.Intent(this, MainActivity::class.java))
                true
            }
            R.id.action_tts_settings -> {
                VoiceNarrator.openTtsSettings(this)
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }

    override fun onDestroy() {
        voiceNarrator?.shutdown()
        binding.lectureWebView.apply {
            loadUrl("about:blank")
            removeJavascriptInterface("AndroidLecture")
            destroy()
        }
        super.onDestroy()
    }

    private class AndroidLectureBridge(
        private val narrator: VoiceNarrator?
    ) {
        @JavascriptInterface
        fun speak(text: String, lang: String): Boolean {
            val code = if (lang == "ur") LocaleHelper.LANG_UR else LocaleHelper.LANG_EN
            return narrator?.speak(text, code) == true
        }

        @JavascriptInterface
        fun stop() {
            narrator?.stop()
        }

        @JavascriptInterface
        fun isNativeTts(): Boolean = true
    }
}
