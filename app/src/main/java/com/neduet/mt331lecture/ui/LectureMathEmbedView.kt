package com.neduet.mt331lecture.ui

import android.annotation.SuppressLint
import android.graphics.Color
import android.util.TypedValue
import android.webkit.JavascriptInterface
import android.webkit.WebView
import android.webkit.WebViewClient
import com.neduet.mt331lecture.data.mt331.LectureBeat
import com.neduet.mt331lecture.data.mt331.Mt331BeatDiagrams
import com.neduet.mt331lecture.data.mt331.Mt331LatexCatalog

@SuppressLint("SetJavaScriptEnabled")
object LectureMathEmbedView {

    private const val BRIDGE = "Mt331MathBridge"

    fun bind(webView: WebView, beat: LectureBeat, uiLanguage: String) {
        val latex = Mt331LatexCatalog.latexForBeat(beat, uiLanguage)
        val svg = Mt331BeatDiagrams.svgForBeat(beat.id)
        if (latex.isBlank() && svg == null) {
            webView.visibility = android.view.View.GONE
            return
        }
        webView.visibility = android.view.View.VISIBLE
        webView.setBackgroundColor(Color.TRANSPARENT)
        webView.settings.javaScriptEnabled = true
        webView.settings.domStorageEnabled = true
        webView.isVerticalScrollBarEnabled = false
        webView.isHorizontalScrollBarEnabled = false

        val density = webView.resources.displayMetrics.density
        webView.removeJavascriptInterface(BRIDGE)
        webView.addJavascriptInterface(
            HeightBridge(webView, density),
            BRIDGE
        )

        val html = buildHtml(latex, svg)
        webView.webViewClient = WebViewClient()
        webView.loadDataWithBaseURL(
            "https://cdn.jsdelivr.net/",
            html,
            "text/html",
            "UTF-8",
            null
        )
    }

    private class HeightBridge(
        private val webView: WebView,
        private val density: Float
    ) {
        @JavascriptInterface
        fun setHeight(cssHeight: Float) {
            val minPx = TypedValue.applyDimension(
                TypedValue.COMPLEX_UNIT_DIP,
                80f,
                webView.resources.displayMetrics
            ).toInt()
            val maxPx = TypedValue.applyDimension(
                TypedValue.COMPLEX_UNIT_DIP,
                420f,
                webView.resources.displayMetrics
            ).toInt()
            val px = (cssHeight * density).toInt().coerceIn(minPx, maxPx)
            webView.post {
                webView.layoutParams = webView.layoutParams.apply { height = px }
            }
        }
    }

    private fun buildHtml(latex: String, svg: String?): String {
        val diagramBlock = svg?.let { """<div class="diagram">$it</div>""" } ?: ""
        val mathBlock = if (latex.isNotBlank()) {
            """<div class="math">\[${escapeHtml(latex)}\]</div>"""
        } else {
            ""
        }
        return """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0"/>
<script>
  window.MathJax = {
    tex: { inlineMath: [['$','$'], ['\\(','\\)']] },
    svg: { fontCache: 'global' },
    startup: { typeset: false }
  };
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
<style>
  * { box-sizing: border-box; }
  body { margin:0; padding:0; background:#141B2D; color:#7EE787; font-family: sans-serif; }
  #wrap { padding: 12px 8px 16px; }
  .diagram svg { width: 100%; max-width: 360px; display: block; margin: 0 auto 12px; border-radius: 12px; }
  .math { text-align: center; overflow-x: auto; }
  mjx-container { color: #7EE787 !important; }
</style>
</head>
<body>
<div id="wrap">
  $diagramBlock
  $mathBlock
</div>
<script>
  function reportHeight() {
    var h = document.getElementById('wrap').scrollHeight;
    Mt331MathBridge.setHeight(h);
  }
  function typesetAndReport() {
    if (window.MathJax && MathJax.typesetPromise) {
      MathJax.typesetPromise().then(reportHeight).catch(reportHeight);
    } else {
      reportHeight();
    }
  }
  if (window.MathJax && MathJax.startup) {
    MathJax.startup.promise.then(typesetAndReport);
  } else {
    document.addEventListener('DOMContentLoaded', typesetAndReport);
  }
</script>
</body>
</html>
        """.trimIndent()
    }

    private fun escapeHtml(text: String): String =
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
}
