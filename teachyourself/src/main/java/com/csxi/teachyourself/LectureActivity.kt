package com.csxi.teachyourself

import android.os.Bundle
import android.speech.tts.TextToSpeech
import android.webkit.WebChromeClient
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.activity.OnBackPressedCallback
import androidx.appcompat.app.AppCompatActivity

class LectureActivity : AppCompatActivity(), TextToSpeech.OnInitListener {

    private lateinit var webView: WebView
    private var tts: TextToSpeech? = null
    private var bridge: TtsBridge? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        webView = WebView(this).apply {
            setBackgroundColor(0xFFF4EFE4.toInt())
            settings.javaScriptEnabled = true
            settings.domStorageEnabled = true
            settings.allowFileAccess = true
            settings.builtInZoomControls = false
            settings.displayZoomControls = false
            settings.mediaPlaybackRequiresUserGesture = false
            webChromeClient = WebChromeClient()
            webViewClient = WebViewClient()
        }
        val engine = TextToSpeech(applicationContext, this)
        tts = engine
        val ttsBridge = TtsBridge(webView, engine)
        bridge = ttsBridge
        webView.addJavascriptInterface(ttsBridge, "UrdishTts")
        setContentView(webView)
        webView.loadUrl("file:///android_asset/www/index.html")

        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                webView.evaluateJavascript(
                    "(function(){return window.tyBack&&window.tyBack()?'1':'0';})()"
                ) { raw ->
                    val stayed = raw == "\"1\"" || raw == "1"
                    if (!stayed) {
                        runOnUiThread { finish() }
                    }
                }
            }
        })
    }

    override fun onInit(status: Int) {
        bridge?.markReady(status == TextToSpeech.SUCCESS)
    }

    override fun onDestroy() {
        tts?.stop()
        tts?.shutdown()
        tts = null
        webView.removeJavascriptInterface("UrdishTts")
        super.onDestroy()
    }
}
