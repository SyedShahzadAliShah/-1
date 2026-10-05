package com.selftaught.csbootcamp

import android.content.Context
import android.os.Handler
import android.os.Looper
import android.print.PrintAttributes
import android.print.PrintManager
import android.webkit.JavascriptInterface
import android.webkit.WebView

/**
 * Lets the page save the study book. WebView ignores window.print() and has no
 * download pipeline for blob URLs, so the page calls these instead.
 */
class BookBridge(
    private val webView: WebView,
    private val pickSaveLocation: (fileName: String, html: String) -> Unit
) {
    private val main = Handler(Looper.getMainLooper())

    /** Opens the Android print sheet for the current page; "Save as PDF" is one of its printers. */
    @JavascriptInterface
    fun print(title: String) {
        main.post {
            val manager = webView.context.getSystemService(Context.PRINT_SERVICE) as? PrintManager ?: return@post
            val jobName = title.ifBlank { "Study book" }
            val attributes = PrintAttributes.Builder()
                .setMediaSize(PrintAttributes.MediaSize.ISO_A4)
                .setColorMode(PrintAttributes.COLOR_MODE_COLOR)
                .build()
            manager.print(jobName, webView.createPrintDocumentAdapter(jobName), attributes)
        }
    }

    /** Asks the user where to save a self-contained HTML copy of the book. */
    @JavascriptInterface
    fun save(fileName: String, html: String) {
        main.post { pickSaveLocation(fileName.ifBlank { "study-book.html" }, html) }
    }

    fun notifySaved(ok: Boolean) {
        webView.post {
            webView.evaluateJavascript("window.__bootcampBookSaved && window.__bootcampBookSaved($ok)", null)
        }
    }
}
