package com.csxii.teachyourself

import android.annotation.SuppressLint
import android.os.Bundle
import android.speech.tts.TextToSpeech
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.activity.OnBackPressedCallback
import androidx.appcompat.app.AppCompatActivity

/**
 * Offline lecture player. Pages, MathJax, SVG figures, and flexbox CSS
 * are loaded from assets. The process has no network permission.
 */
class LectureActivity : AppCompatActivity() {
    private lateinit var web: WebView
    private lateinit var tts: TextToSpeech
    private lateinit var bridge: TtsBridge

    @SuppressLint("SetJavaScriptEnabled")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        web = WebView(this)
        setContentView(web)

        web.settings.apply {
            javaScriptEnabled = true
            domStorageEnabled = true
            allowFileAccess = true
            blockNetworkLoads = true
            cacheMode = WebSettings.LOAD_DEFAULT
            builtInZoomControls = false
            displayZoomControls = false
            mediaPlaybackRequiresUserGesture = false
            setSupportZoom(false)
        }
        web.webViewClient = WebViewClient()

        tts = TextToSpeech(this) { status -> bridge.onInit(status) }
        bridge = TtsBridge(this, tts)
        web.addJavascriptInterface(bridge, "AndroidTTS")
        web.loadUrl("file:///android_asset/www/index.html")

        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                web.evaluateJavascript("(function(){return window.appBack?window.appBack():false})()") { raw ->
                    if (raw == "false" || raw == null) finish()
                }
            }
        })
    }

    fun evaluate(script: String) {
        runOnUiThread { web.evaluateJavascript(script, null) }
    }

    override fun onDestroy() {
        if (::bridge.isInitialized) bridge.shutdown()
        if (::web.isInitialized) web.destroy()
        super.onDestroy()
    }
}
