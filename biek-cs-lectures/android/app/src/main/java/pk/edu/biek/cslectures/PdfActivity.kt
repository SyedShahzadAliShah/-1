package pk.edu.biek.cslectures

import android.graphics.Bitmap
import android.graphics.pdf.PdfRenderer
import android.os.Bundle
import android.os.ParcelFileDescriptor
import androidx.appcompat.app.AppCompatActivity
import pk.edu.biek.cslectures.databinding.ActivityPdfBinding
import java.io.File
import java.io.FileOutputStream

class PdfActivity : AppCompatActivity() {
    private var renderer: PdfRenderer? = null
    private var descriptor: ParcelFileDescriptor? = null
    private var pageIndex = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val binding = ActivityPdfBinding.inflate(layoutInflater)
        setContentView(binding.root)
        val asset = intent.getStringExtra(EXTRA_ASSET) ?: return finish()
        val file = File(cacheDir, File(asset).name)
        if (!file.exists()) {
            assets.open(asset).use { input ->
                FileOutputStream(file).use { output -> input.copyTo(output) }
            }
        }
        descriptor = ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY)
        renderer = PdfRenderer(descriptor!!)
        pageIndex = savedInstanceState?.getInt(STATE_PAGE) ?: 0

        fun show() {
            val pdf = renderer ?: return
            if (pdf.pageCount == 0) return
            pageIndex = pageIndex.coerceIn(0, pdf.pageCount - 1)
            pdf.openPage(pageIndex).use { page ->
                val width = resources.displayMetrics.widthPixels
                val height = (width.toFloat() / page.width * page.height).toInt().coerceAtLeast(1)
                val bitmap = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888)
                page.render(bitmap, null, null, PdfRenderer.Page.RENDER_MODE_FOR_DISPLAY)
                binding.pageImage.setImageBitmap(bitmap)
            }
            binding.pageLabel.text = getString(R.string.pdf_page, pageIndex + 1, pdf.pageCount)
            binding.previousPage.isEnabled = pageIndex > 0
            binding.nextPage.isEnabled = pageIndex < pdf.pageCount - 1
        }

        binding.previousPage.setOnClickListener {
            pageIndex -= 1
            show()
        }
        binding.nextPage.setOnClickListener {
            pageIndex += 1
            show()
        }
        show()
    }

    override fun onSaveInstanceState(outState: Bundle) {
        outState.putInt(STATE_PAGE, pageIndex)
        super.onSaveInstanceState(outState)
    }

    override fun onDestroy() {
        renderer?.close()
        descriptor?.close()
        super.onDestroy()
    }

    companion object {
        const val EXTRA_ASSET = "pdf_asset"
        const val EXTRA_TITLE = "pdf_title"
        private const val STATE_PAGE = "page"
    }
}
