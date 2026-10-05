package com.selftaught.csbootcamp

import android.annotation.SuppressLint
import android.os.Bundle
import android.speech.tts.TextToSpeech
import android.webkit.WebResourceRequest
import android.webkit.WebResourceResponse
import android.webkit.WebView
import android.webkit.WebViewClient
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import androidx.webkit.WebViewAssetLoader
import android.content.Context

class BootcampActivity : AppCompatActivity(), TextToSpeech.OnInitListener {
    private lateinit var webView: WebView
    private var tts: TextToSpeech? = null
    private var bridge: VoiceBridge? = null
    private var book: BookBridge? = null
    private var pendingBookHtml: String? = null

    private val saveBook = registerForActivityResult(ActivityResultContracts.CreateDocument("text/html")) { uri ->
        val html = pendingBookHtml
        pendingBookHtml = null
        if (uri == null || html == null) {
            book?.notifySaved(false)
            return@registerForActivityResult
        }
        val ok = runCatching {
            contentResolver.openOutputStream(uri, "wt")?.use { it.write(html.toByteArray(Charsets.UTF_8)) }
                ?: error("no stream")
        }.isSuccess
        Toast.makeText(this, if (ok) R.string.book_saved else R.string.book_save_failed, Toast.LENGTH_LONG).show()
        book?.notifySaved(ok)
    }

    @SuppressLint("SetJavaScriptEnabled")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_bootcamp)
        webView = findViewById(R.id.web)

        val assetLoader = WebViewAssetLoader.Builder()
            .addPathHandler("/assets/", BootcampPathHandler(this))
            .build()

        webView.settings.apply {
            javaScriptEnabled = true
            domStorageEnabled = true
            mediaPlaybackRequiresUserGesture = false
            allowFileAccess = false
            builtInZoomControls = false
            displayZoomControls = false
        }
        webView.webViewClient = object : WebViewClient() {
            override fun shouldInterceptRequest(view: WebView, request: WebResourceRequest): WebResourceResponse? {
                return assetLoader.shouldInterceptRequest(request.url)
            }
        }

        val engine = TextToSpeech(this, this)
        tts = engine
        val voice = VoiceBridge(webView, engine)
        bridge = voice
        webView.addJavascriptInterface(voice, "BootcampVoice")
        val bookBridge = BookBridge(webView) { fileName, html ->
            pendingBookHtml = html
            runCatching { saveBook.launch(fileName) }.onFailure {
                pendingBookHtml = null
                Toast.makeText(this, R.string.book_save_failed, Toast.LENGTH_LONG).show()
                book?.notifySaved(false)
            }
        }
        book = bookBridge
        webView.addJavascriptInterface(bookBridge, "BootcampBook")
        webView.loadUrl("https://appassets.androidplatform.net/assets/www/index.html")

        onBackPressedDispatcher.addCallback(this, object : androidx.activity.OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                if (webView.canGoBack()) webView.goBack() else finish()
            }
        })
    }

    override fun onInit(status: Int) {
        bridge?.onEngineReady(status == TextToSpeech.SUCCESS)
    }

    override fun onDestroy() {
        webView.removeJavascriptInterface("BootcampVoice")
        webView.removeJavascriptInterface("BootcampBook")
        tts?.stop()
        tts?.shutdown()
        tts = null
        super.onDestroy()
    }
}

private class BootcampPathHandler(context: Context) : WebViewAssetLoader.PathHandler {
    private val assets = WebViewAssetLoader.AssetsPathHandler(context)

    override fun handle(path: String): WebResourceResponse? {
        val response = assets.handle(path) ?: return null
        val mime = when {
            path.endsWith(".js") -> "text/javascript"
            path.endsWith(".css") -> "text/css"
            path.endsWith(".html") -> "text/html"
            path.endsWith(".svg") -> "image/svg+xml"
            else -> response.mimeType
        }
        return WebResourceResponse(mime, "utf-8", response.data)
    }
}
