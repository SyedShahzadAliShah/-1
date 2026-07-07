package com.couplesguide.postures.util

import android.content.ContentValues
import android.content.Context
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.graphics.Canvas
import android.graphics.Paint
import android.graphics.pdf.PdfDocument
import android.os.Environment
import android.provider.MediaStore
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.FileProvider
import com.couplesguide.postures.R
import com.couplesguide.postures.data.PdfBookRepository
import java.io.File
import java.io.FileInputStream
import java.io.FileOutputStream

object PdfBookExporter {

    private const val PAGE_WIDTH = 595
    private const val PAGE_HEIGHT = 842
    private const val MARGIN = 40f
    private const val DOWNLOADS_FOLDER = "IntimacyGuide"
    private const val SOURCE_PDF_ASSET = "muslim_kama_sutra_book.pdf"

    data class ExportResult(
        val file: File,
        val displayName: String
    )

    fun exportEmbeddedSourcePdf(context: Context): ExportResult {
        val displayName = "muslim_kama_sutra_urdu.pdf"
        val outFile = File(context.cacheDir, displayName)
        if (outFile.exists()) outFile.delete()
        context.assets.open(SOURCE_PDF_ASSET).use { input ->
            FileOutputStream(outFile).use { output -> input.copyTo(output) }
        }
        return ExportResult(outFile, displayName)
    }

    fun exportUrduIllustratedBook(context: Context): ExportResult {
        val displayName = "muslim_kama_sutra_urdu_illustrated.pdf"
        val outFile = File(context.cacheDir, displayName)
        if (outFile.exists()) outFile.delete()

        val document = PdfDocument()
        val titlePaint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
            textSize = 22f
            isFakeBoldText = true
        }
        val bodyPaint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
            textSize = 13f
        }
        val footerPaint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
            textSize = 10f
            color = 0xFF666666.toInt()
        }

        PdfBookRepository.getPages().forEachIndexed { index, page ->
            val pdfPage = document.startPage(
                PdfDocument.PageInfo.Builder(PAGE_WIDTH, PAGE_HEIGHT, index + 1).create()
            )
            val canvas = pdfPage.canvas

            canvas.drawText(page.titleUr, MARGIN, MARGIN + 24f, titlePaint)

            val bitmap = loadAssetBitmap(context, page.assetImage)
            if (bitmap != null) {
                val imageTop = MARGIN + 40f
                val imageHeight = 360f
                val imageWidth = PAGE_WIDTH - MARGIN * 2
                val scaled = Bitmap.createScaledBitmap(
                    bitmap,
                    imageWidth.toInt(),
                    imageHeight.toInt(),
                    true
                )
                canvas.drawBitmap(scaled, MARGIN, imageTop, null)
                if (scaled !== bitmap) scaled.recycle()
                bitmap.recycle()
            }

            val textTop = MARGIN + 420f
            drawWrappedRtlText(canvas, page.narrationUr, MARGIN, textTop, PAGE_WIDTH - MARGIN * 2, bodyPaint)

            val footer = "صفحہ ${page.pageNumber} / ${PdfBookRepository.getTotalPages()}"
            canvas.drawText(footer, MARGIN, PAGE_HEIGHT - MARGIN, footerPaint)

            document.finishPage(pdfPage)
        }

        FileOutputStream(outFile).use { document.writeTo(it) }
        document.close()
        return ExportResult(outFile, displayName)
    }

    private fun loadAssetBitmap(context: Context, assetPath: String): Bitmap? {
        return try {
            context.assets.open(assetPath).use { BitmapFactory.decodeStream(it) }
        } catch (_: Exception) {
            null
        }
    }

    private fun drawWrappedRtlText(
        canvas: Canvas,
        text: String,
        x: Float,
        y: Float,
        maxWidth: Float,
        paint: Paint
    ) {
        val words = text.split(" ")
        var line = StringBuilder()
        var currentY = y
        val lineHeight = paint.textSize * 1.5f
        for (word in words) {
            val candidate = if (line.isEmpty()) word else "$line $word"
            if (paint.measureText(candidate) > maxWidth && line.isNotEmpty()) {
                canvas.drawText(line.toString(), x, currentY, paint)
                line = StringBuilder(word)
                currentY += lineHeight
            } else {
                line = StringBuilder(candidate)
            }
        }
        if (line.isNotEmpty()) {
            canvas.drawText(line.toString(), x, currentY, paint)
        }
    }

    fun showExportActions(activity: AppCompatActivity, result: ExportResult) {
        AlertDialog.Builder(activity)
            .setTitle(R.string.pdf_ready_title)
            .setMessage(activity.getString(R.string.pdf_ready))
            .setPositiveButton(R.string.share_pdf) { _, _ -> sharePdf(activity, result) }
            .setNeutralButton(R.string.pdf_open) { _, _ -> openPdf(activity, result) }
            .setNegativeButton(R.string.pdf_save_downloads) { _, _ ->
                saveToDownloads(activity, result)
            }
            .show()
    }

    private fun sharePdf(activity: AppCompatActivity, result: ExportResult) {
        val uri = FileProvider.getUriForFile(
            activity,
            "${activity.packageName}.fileprovider",
            result.file
        )
        val intent = android.content.Intent(android.content.Intent.ACTION_SEND).apply {
            type = "application/pdf"
            putExtra(android.content.Intent.EXTRA_STREAM, uri)
            addFlags(android.content.Intent.FLAG_GRANT_READ_URI_PERMISSION)
        }
        activity.startActivity(android.content.Intent.createChooser(intent, activity.getString(R.string.share_pdf)))
    }

    private fun openPdf(activity: AppCompatActivity, result: ExportResult) {
        val uri = FileProvider.getUriForFile(
            activity,
            "${activity.packageName}.fileprovider",
            result.file
        )
        val intent = android.content.Intent(android.content.Intent.ACTION_VIEW).apply {
            setDataAndType(uri, "application/pdf")
            addFlags(android.content.Intent.FLAG_GRANT_READ_URI_PERMISSION)
        }
        if (intent.resolveActivity(activity.packageManager) != null) {
            activity.startActivity(intent)
        } else {
            Toast.makeText(activity, R.string.pdf_open, Toast.LENGTH_SHORT).show()
        }
    }

    private fun saveToDownloads(activity: AppCompatActivity, result: ExportResult) {
        try {
            if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.Q) {
                val values = ContentValues().apply {
                    put(MediaStore.Downloads.DISPLAY_NAME, result.displayName)
                    put(MediaStore.Downloads.MIME_TYPE, "application/pdf")
                    put(MediaStore.Downloads.RELATIVE_PATH, Environment.DIRECTORY_DOWNLOADS + "/$DOWNLOADS_FOLDER")
                }
                val resolver = activity.contentResolver
                val uri = resolver.insert(MediaStore.Downloads.EXTERNAL_CONTENT_URI, values)
                if (uri != null) {
                    resolver.openOutputStream(uri)?.use { out ->
                        FileInputStream(result.file).use { it.copyTo(out) }
                    }
                    Toast.makeText(
                        activity,
                        activity.getString(R.string.pdf_saved_downloads, result.displayName),
                        Toast.LENGTH_LONG
                    ).show()
                    return
                }
            }
            val downloads = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS)
            val folder = File(downloads, DOWNLOADS_FOLDER)
            folder.mkdirs()
            val dest = File(folder, result.displayName)
            FileInputStream(result.file).use { input ->
                FileOutputStream(dest).use { output -> input.copyTo(output) }
            }
            Toast.makeText(
                activity,
                activity.getString(R.string.pdf_saved_downloads, result.displayName),
                Toast.LENGTH_LONG
            ).show()
        } catch (_: Exception) {
            Toast.makeText(activity, R.string.pdf_save_failed, Toast.LENGTH_SHORT).show()
        }
    }
}
