package com.couplesguide.postures.util

import android.content.Context
import android.graphics.Bitmap
import android.graphics.pdf.PdfRenderer
import android.os.ParcelFileDescriptor
import java.io.File

class PdfAssetRenderer private constructor(
    private val renderer: PdfRenderer,
    private val parcelFileDescriptor: ParcelFileDescriptor
) : AutoCloseable {

    val pageCount: Int get() = renderer.pageCount

    fun renderPage(pageIndex: Int, scale: Float = 2f): Bitmap {
        val index = pageIndex.coerceIn(0, renderer.pageCount - 1)
        renderer.openPage(index).use { page ->
            val width = (page.width * scale).toInt().coerceAtLeast(1)
            val height = (page.height * scale).toInt().coerceAtLeast(1)
            val bitmap = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888)
            page.render(bitmap, null, null, PdfRenderer.Page.RENDER_MODE_FOR_DISPLAY)
            return bitmap
        }
    }

    override fun close() {
        renderer.close()
        parcelFileDescriptor.close()
    }

    companion object {
        fun open(context: Context, assetPath: String): PdfAssetRenderer {
            val cacheName = assetPath.replace('/', '_')
            val cacheFile = File(context.cacheDir, cacheName)
            if (!cacheFile.exists() || cacheFile.length() == 0L) {
                context.assets.open(assetPath).use { input ->
                    cacheFile.outputStream().use { output -> input.copyTo(output) }
                }
            }
            val pfd = ParcelFileDescriptor.open(cacheFile, ParcelFileDescriptor.MODE_READ_ONLY)
            return PdfAssetRenderer(PdfRenderer(pfd), pfd)
        }
    }
}
