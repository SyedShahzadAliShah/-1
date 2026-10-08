package com.teachyourself.sketchnotes

import android.annotation.SuppressLint
import android.content.Intent
import android.os.Bundle
import android.speech.tts.TextToSpeech
import android.webkit.JavascriptInterface
import android.webkit.WebResourceRequest
import android.webkit.WebResourceResponse
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.activity.OnBackPressedCallback
import androidx.appcompat.app.AppCompatActivity
import androidx.webkit.WebViewAssetLoader
import org.json.JSONArray
import org.json.JSONObject

class MainActivity : AppCompatActivity() {

    private lateinit var webView: WebView
    private lateinit var speaker: UrdishSpeaker

    @SuppressLint("SetJavaScriptEnabled")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        speaker = UrdishSpeaker(
            this,
            onState = { state -> runJs("window.Urdish && Urdish.onState(${JSONObject.quote(state)})") },
            onIssue = { message -> runJs("window.Urdish && Urdish.onVoiceIssue(${JSONObject.quote(message)})") }
        )

        val assetLoader = WebViewAssetLoader.Builder()
            .addPathHandler("/assets/", WebViewAssetLoader.AssetsPathHandler(this))
            .build()

        webView = WebView(this)
        setContentView(webView)
        if (BuildConfig.DEBUG) {
            WebView.setWebContentsDebuggingEnabled(true)
        }
        webView.setBackgroundColor(getColor(R.color.paper))
        webView.settings.javaScriptEnabled = true
        webView.settings.domStorageEnabled = true
        webView.settings.allowFileAccess = false
        webView.settings.mediaPlaybackRequiresUserGesture = false
        webView.settings.builtInZoomControls = true
        webView.settings.displayZoomControls = false
        webView.addJavascriptInterface(Bridge(), "Android")
        webView.webViewClient = object : WebViewClient() {
            override fun shouldInterceptRequest(
                view: WebView,
                request: WebResourceRequest
            ): WebResourceResponse? {
                return assetLoader.shouldInterceptRequest(request.url)
            }
        }
        webView.loadUrl("https://appassets.androidplatform.net/assets/www/index.html")

        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                webView.evaluateJavascript("(function(){return !!(window.App && App.back());})()") { raw ->
                    if (raw != "true") {
                        isEnabled = false
                        onBackPressedDispatcher.onBackPressed()
                    }
                }
            }
        })
    }

    private fun runJs(script: String) {
        if (!::webView.isInitialized) return
        webView.post { webView.evaluateJavascript(script, null) }
    }

    override fun onDestroy() {
        speaker.shutdown()
        webView.destroy()
        super.onDestroy()
    }

    private inner class Bridge {
        @JavascriptInterface
        fun speak(json: String) {
            val array = JSONArray(json)
            val segments = mutableListOf<UrdishSpeaker.Segment>()
            for (index in 0 until array.length()) {
                val item = array.getJSONObject(index)
                segments.add(
                    UrdishSpeaker.Segment(
                        item.optString("text"),
                        item.optString("lang", "en")
                    )
                )
            }
            runOnUiThread { speaker.speak(segments) }
        }

        @JavascriptInterface
        fun stop() {
            runOnUiThread { speaker.stop() }
        }

        @JavascriptInterface
        fun setRate(rate: Double) {
            speaker.setRate(rate.toFloat())
        }

        @JavascriptInterface
        fun openTtsSettings() {
            runOnUiThread {
                val intents = listOf(
                    Intent("com.android.settings.TTS_SETTINGS"),
                    Intent(TextToSpeech.Engine.ACTION_INSTALL_TTS_DATA)
                )
                for (intent in intents) {
                    if (intent.resolveActivity(packageManager) != null) {
                        startActivity(intent)
                        return@runOnUiThread
                    }
                }
            }
        }
    }
}
