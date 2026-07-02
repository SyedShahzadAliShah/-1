package com.couplesguide.postures.util

import android.app.Activity
import android.content.ClipData
import android.content.ContentValues
import android.content.Context
import android.content.Intent
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.graphics.Canvas
import android.graphics.Paint
import android.graphics.Typeface
import android.graphics.pdf.PdfDocument
import android.graphics.pdf.PdfRenderer
import android.net.Uri
import android.os.Build
import android.os.CancellationSignal
import android.os.Environment
import android.os.ParcelFileDescriptor
import android.print.PageRange
import android.print.PrintAttributes
import android.print.PrintDocumentAdapter
import android.print.PrintDocumentInfo
import android.print.PrintManager
import android.provider.MediaStore
import android.text.Layout
import android.text.StaticLayout
import android.text.TextDirectionHeuristics
import android.text.TextPaint
import android.widget.Toast
import androidx.annotation.RequiresApi
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import androidx.core.content.FileProvider
import com.couplesguide.postures.R
import com.couplesguide.postures.data.BookIntroRepository
import com.couplesguide.postures.data.Posture
import com.couplesguide.postures.data.PostureRepository
import com.couplesguide.postures.data.SpectacularMovesRepository
import java.io.File
import java.io.FileInputStream
import java.io.FileOutputStream

object PdfExporter {

    private const val PAGE_WIDTH = 595   // A4 width in points (72 dpi)
    private const val PAGE_HEIGHT = 842  // A4 height in points
    private const val MARGIN = 54f
    private const val TOP_MARGIN = 54f
    private const val BOTTOM_MARGIN = 54f
    private const val CONTENT_WIDTH = PAGE_WIDTH - MARGIN * 2
    private const val IMAGE_HEIGHT = 150f
    private const val DOWNLOADS_FOLDER = "SpectacularMoves"

    data class ExportResult(
        val file: File,
        val displayName: String
    )

    fun exportFullGuide(context: Context, language: String): ExportResult {
        val displayName = "shandaar_harkatein_urdu.pdf"
        val file = File(context.cacheDir, displayName)
        if (file.exists()) file.delete()

        val document = PdfDocument()
        try {
            var pageNumber = 1
            pageNumber = writeTitlePage(context, document, pageNumber)
            pageNumber = writeIntroPage(context, document, pageNumber)
            pageNumber = writeAllMovesByCategory(context, document, pageNumber)
            FileOutputStream(file).use { document.writeTo(it) }
        } finally {
            document.close()
        }
        return ExportResult(file, displayName)
    }

    fun exportPosture(context: Context, posture: Posture, @Suppress("UNUSED_PARAMETER") language: String): ExportResult {
        val displayName = "${posture.id}_urdu.pdf"
        val file = File(context.cacheDir, displayName)
        if (file.exists()) file.delete()

        val document = PdfDocument()
        try {
            writePosturePages(context, document, posture, 1)
            FileOutputStream(file).use { document.writeTo(it) }
        } finally {
            document.close()
        }
        return ExportResult(file, displayName)
    }

    fun showExportActions(activity: AppCompatActivity, result: ExportResult) {
        val options = arrayOf(
            activity.getString(R.string.pdf_open),
            activity.getString(R.string.pdf_save_downloads),
            activity.getString(R.string.pdf_print),
            activity.getString(R.string.share_pdf)
        )
        AlertDialog.Builder(activity)
            .setTitle(R.string.pdf_ready_title)
            .setItems(options) { _, which ->
                when (which) {
                    0 -> openPdf(activity, result.file)
                    1 -> saveToDownloads(activity, result)
                    2 -> printPdf(activity, result)
                    3 -> sharePdf(activity, result.file)
                }
            }
            .setNegativeButton(android.R.string.cancel, null)
            .show()
    }

    fun openPdf(context: Context, file: File) {
        if (!file.exists() || file.length() == 0L) {
            throw IllegalStateException("PDF file is missing or empty")
        }
        val uri = fileUri(context, file)
        val intent = Intent(Intent.ACTION_VIEW).apply {
            setDataAndType(uri, "application/pdf")
            clipData = ClipData.newRawUri("pdf", uri)
            addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
        }
        val chooser = Intent.createChooser(intent, context.getString(R.string.pdf_open))
        if (context !is Activity) {
            chooser.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
        }
        context.startActivity(chooser)
    }

    fun sharePdf(context: Context, file: File) {
        if (!file.exists() || file.length() == 0L) {
            throw IllegalStateException("PDF file is missing or empty")
        }
        val uri = fileUri(context, file)
        val intent = Intent(Intent.ACTION_SEND).apply {
            type = "application/pdf"
            putExtra(Intent.EXTRA_STREAM, uri)
            clipData = ClipData.newRawUri("pdf", uri)
            addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
        }
        val chooser = Intent.createChooser(intent, context.getString(R.string.share_pdf))
        if (context !is Activity) {
            chooser.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
        }
        context.startActivity(chooser)
    }

    fun saveToDownloads(context: Context, result: ExportResult): Uri? {
        if (!result.file.exists() || result.file.length() == 0L) {
            throw IllegalStateException("PDF file is missing or empty")
        }
        val uri = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            saveToDownloadsMediaStore(context, result)
        } else {
            saveToDownloadsLegacy(context, result)
        }
        if (uri != null) {
            Toast.makeText(
                context,
                context.getString(R.string.pdf_saved_downloads, result.displayName),
                Toast.LENGTH_LONG
            ).show()
        } else {
            Toast.makeText(context, R.string.pdf_save_failed, Toast.LENGTH_SHORT).show()
        }
        return uri
    }

    fun printPdf(activity: Activity, result: ExportResult) {
        if (!result.file.exists() || result.file.length() == 0L) {
            throw IllegalStateException("PDF file is missing or empty")
        }
        val printManager = activity.getSystemService(Context.PRINT_SERVICE) as PrintManager
        val adapter = PdfPrintDocumentAdapter(result.file, result.displayName)
        printManager.print(
            result.displayName,
            adapter,
            PrintAttributes.Builder()
                .setMediaSize(PrintAttributes.MediaSize.ISO_A4)
                .setResolution(PrintAttributes.Resolution("pdf", "pdf", 600, 600))
                .setMinMargins(PrintAttributes.Margins.NO_MARGINS)
                .setColorMode(PrintAttributes.COLOR_MODE_COLOR)
                .build()
        )
    }

    private fun fileUri(context: Context, file: File): Uri {
        return FileProvider.getUriForFile(
            context,
            "${context.packageName}.fileprovider",
            file
        )
    }

    @RequiresApi(Build.VERSION_CODES.Q)
    private fun saveToDownloadsMediaStore(context: Context, result: ExportResult): Uri? {
        val resolver = context.contentResolver
        val values = ContentValues().apply {
            put(MediaStore.Downloads.DISPLAY_NAME, result.displayName)
            put(MediaStore.Downloads.MIME_TYPE, "application/pdf")
            put(
                MediaStore.Downloads.RELATIVE_PATH,
                "${Environment.DIRECTORY_DOWNLOADS}/$DOWNLOADS_FOLDER"
            )
            put(MediaStore.Downloads.IS_PENDING, 1)
        }
        val uri = resolver.insert(MediaStore.Downloads.EXTERNAL_CONTENT_URI, values) ?: return null
        try {
            resolver.openOutputStream(uri)?.use { out ->
                FileInputStream(result.file).use { input -> input.copyTo(out) }
            } ?: return null
            values.clear()
            values.put(MediaStore.Downloads.IS_PENDING, 0)
            resolver.update(uri, values, null, null)
            return uri
        } catch (e: Exception) {
            resolver.delete(uri, null, null)
            throw e
        }
    }

    @Suppress("DEPRECATION")
    private fun saveToDownloadsLegacy(context: Context, result: ExportResult): Uri? {
        val downloadsDir = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS)
        val targetDir = File(downloadsDir, DOWNLOADS_FOLDER)
        if (!targetDir.exists() && !targetDir.mkdirs()) return null
        val target = File(targetDir, result.displayName)
        result.file.copyTo(target, overwrite = true)
        return fileUri(context, target)
    }

    private fun writeTitlePage(
        context: Context,
        document: PdfDocument,
        pageNumber: Int
    ): Int {
        val writer = PageWriter(context, document, pageNumber)

        writer.drawTitle("شاندار حرکتیں")
        writer.drawBody("وہ کبھی نہیں بھولے گی", writer.sectionPaint(14f))
        writer.space(12f)
        writer.drawBody(
            "سونیا بورگ کی کتاب سے ۳۰ منفرد پوزیشنز — مختصر اردو وضاحت، " +
                "آواز میں سننے اور PDF برآمد۔"
        )
        writer.space(16f)
        writer.drawImage(R.drawable.pic_guide_cover, 320, 190)
        return writer.finish()
    }

    private fun writeIntroPage(
        context: Context,
        document: PdfDocument,
        pageNumber: Int
    ): Int {
        val intro = BookIntroRepository.getIntroChapter().urdu
        val writer = PageWriter(context, document, pageNumber)
        writer.drawImage(BookIntroRepository.getIntroChapter().illustrationRes, 280, 160)
        writer.drawHeading(intro.title)
        writer.drawBody(intro.summary)
        writer.space(8f)
        writer.drawBody(intro.body)
        writer.space(8f)
        writer.drawSection("اہم نکات:")
        for (point in intro.keyPoints) {
            writer.drawBody(UrduPdfText.bulletItem(point))
            writer.space(4f)
        }
        return writer.finish()
    }

    private fun writeAllMovesByCategory(
        context: Context,
        document: PdfDocument,
        startPage: Int
    ): Int {
        var pageNumber = startPage
        val categories = SpectacularMovesRepository.getCategoryIds()
            .filter { it != PostureRepository.CAT_ALL }
        for (categoryId in categories) {
            val moves = SpectacularMovesRepository.getMovesByCategory(categoryId)
            if (moves.isEmpty()) continue
            pageNumber = writeSectionDivider(
                context, document, pageNumber,
                SpectacularMovesRepository.getCategoryLabel(categoryId)
            )
            for (posture in moves) {
                pageNumber = writePosturePages(context, document, posture, pageNumber)
            }
        }
        return pageNumber
    }

    private fun writeSectionDivider(
        context: Context,
        document: PdfDocument,
        pageNumber: Int,
        title: String
    ): Int {
        val writer = PageWriter(context, document, pageNumber)
        writer.y = PAGE_HEIGHT / 2f - 24f
        writer.drawTitleCentered(title, 24f)
        return writer.finish()
    }

    private fun writePosturePages(
        context: Context,
        document: PdfDocument,
        posture: Posture,
        startPage: Int
    ): Int {
        val content = posture.urdu
        val writer = PageWriter(context, document, startPage)

        writer.drawImage(posture.illustrationRes, 340, IMAGE_HEIGHT.toInt())
        writer.drawHeading(content.name)
        writer.drawBody(UrduPdfText.metaLine(content.category, posture.difficulty.label(LocaleHelper.LANG_UR)))
        writer.space(8f)
        writer.drawBody(content.summary)
        writer.space(10f)

        writer.drawSection("تفصیل")
        writer.drawBody(content.description)
        writer.space(8f)

        writer.drawSection("طریقہ")
        content.steps.forEachIndexed { index, step ->
            writer.drawBody(UrduPdfText.numberedItem(index + 1, step))
            writer.space(4f)
        }
        writer.space(6f)

        writer.drawSection("مشورے")
        for (tip in content.tips) {
            writer.drawBody(UrduPdfText.bulletItem(tip))
            writer.space(4f)
        }
        return writer.finish()
    }

    private class PageWriter(
        private val context: Context,
        private val document: PdfDocument,
        startPage: Int
    ) {
        private val textWidth = CONTENT_WIDTH.toInt()
        private var pageNumber = startPage
        private var displayPageNumber = startPage
        private lateinit var page: PdfDocument.Page
        private lateinit var canvas: Canvas
        var y = TOP_MARGIN

        private val regularTypeface: Typeface = loadTypeface(false)
        private val boldTypeface: Typeface = loadTypeface(true)

        init {
            newPage()
        }

        private fun loadTypeface(bold: Boolean): Typeface {
            return try {
                Typeface.createFromAsset(context.assets, "fonts/NotoNaskhArabic-Regular.ttf")
            } catch (_: Exception) {
                Typeface.DEFAULT
            }
        }

        private fun prepareText(text: String): String = UrduPdfText.normalize(text)

        private fun newPage() {
            if (::page.isInitialized) {
                drawPageFooter()
                document.finishPage(page)
            }
            val pageInfo = PdfDocument.PageInfo.Builder(PAGE_WIDTH, PAGE_HEIGHT, pageNumber)
                .setContentRect(
                    android.graphics.Rect(
                        MARGIN.toInt(),
                        TOP_MARGIN.toInt(),
                        (PAGE_WIDTH - MARGIN).toInt(),
                        (PAGE_HEIGHT - BOTTOM_MARGIN).toInt()
                    )
                )
                .create()
            page = document.startPage(pageInfo)
            canvas = page.canvas
            displayPageNumber = pageNumber  // record BEFORE incrementing
            pageNumber++
            y = TOP_MARGIN
        }

        private fun drawPageFooter() {
            // Draw a thin separator above the footer
            val sepY = PAGE_HEIGHT - BOTTOM_MARGIN + 4f
            canvas.drawLine(MARGIN, sepY, PAGE_WIDTH - MARGIN, sepY,
                Paint().also { it.color = 0xFFD0C0B0.toInt(); it.strokeWidth = 0.5f })

            val label = UrduPdfText.pageNumber(displayPageNumber)
            val footerPaint = TextPaint(Paint.ANTI_ALIAS_FLAG).apply {
                color = ContextCompat.getColor(context, R.color.secondary)
                textSize = 11f
                typeface = regularTypeface
                textAlign = Paint.Align.CENTER
            }
            canvas.drawText(
                label,
                PAGE_WIDTH / 2f,
                PAGE_HEIGHT - (BOTTOM_MARGIN / 3f),
                footerPaint
            )
        }

        private fun availableHeight(): Float = PAGE_HEIGHT - BOTTOM_MARGIN - y

        private fun ensureSpace(needed: Float) {
            if (needed > availableHeight()) {
                newPage()
            }
        }

        fun space(amount: Float) {
            y += amount
        }

        fun drawTitle(text: String, size: Float = 28f) {
            drawTextBlock(text, titlePaint(size), spacingAfter = 14f)
        }

        fun drawTitleCentered(text: String, size: Float = 24f) {
            drawTextBlock(
                text,
                titlePaint(size),
                spacingAfter = 14f,
                alignment = Layout.Alignment.ALIGN_CENTER
            )
        }

        fun drawHeading(text: String) {
            drawTextBlock(text, titlePaint(21f), spacingAfter = 10f)
        }

        fun drawSection(text: String) {
            drawTextBlock(text, sectionPaint(16f), spacingAfter = 8f)
        }

        fun drawBody(text: String, paint: TextPaint = bodyPaint()) {
            drawTextBlock(text, paint, spacingAfter = 10f)
        }

        private fun drawTextBlock(
            text: String,
            paint: TextPaint,
            spacingAfter: Float,
            alignment: Layout.Alignment = textAlignment()
        ) {
            if (text.isBlank()) return

            val prepared = prepareText(text)
            val fullLayout = buildLayout(prepared, paint, alignment)
            var startLine = 0
            val totalLines = fullLayout.lineCount

            while (startLine < totalLines) {
                var endLine = startLine + 1
                while (endLine <= totalLines) {
                    val chunkHeight = fullLayout.getLineBottom(endLine - 1) - fullLayout.getLineTop(startLine)
                    if (chunkHeight > availableHeight()) {
                        if (endLine - 1 > startLine) {
                            endLine--
                        }
                        break
                    }
                    if (endLine == totalLines) break
                    endLine++
                }

                val blockHeight = fullLayout.getLineBottom(endLine - 1) -
                    fullLayout.getLineTop(startLine) + spacingAfter
                ensureSpace(blockHeight)
                drawLayoutLines(fullLayout, startLine, endLine)
                y += blockHeight

                startLine = endLine
                if (startLine < totalLines) {
                    newPage()
                }
            }
        }

        private fun drawLayoutLines(layout: StaticLayout, startLine: Int, endLine: Int) {
            val top = layout.getLineTop(startLine)
            val bottom = layout.getLineBottom(endLine - 1)
            canvas.save()
            canvas.translate(MARGIN, y)
            canvas.clipRect(0f, top.toFloat(), textWidth.toFloat(), bottom.toFloat())
            canvas.translate(0f, -top.toFloat())
            layout.draw(canvas)
            canvas.restore()
        }

        fun drawImage(resId: Int, width: Int, height: Int) {
            val maxWidth = CONTENT_WIDTH.toInt()
            val drawWidth = minOf(width, maxWidth)
            val drawHeight = (height * (drawWidth.toFloat() / width)).toInt()
            val bitmap = loadBitmap(resId, drawWidth, drawHeight) ?: return
            ensureSpace(drawHeight + 12f)
            val left = MARGIN + (CONTENT_WIDTH - drawWidth) / 2f
            canvas.drawBitmap(bitmap, left, y, null)
            y += drawHeight + 12f
            bitmap.recycle()
        }

        fun sectionPaint(size: Float): TextPaint = TextPaint(Paint.ANTI_ALIAS_FLAG).apply {
            color = ContextCompat.getColor(context, R.color.secondary)
            textSize = size
            typeface = boldTypeface
        }

        private fun titlePaint(size: Float) = TextPaint(Paint.ANTI_ALIAS_FLAG).apply {
            color = ContextCompat.getColor(context, R.color.primary)
            textSize = size
            typeface = boldTypeface
        }

        private fun bodyPaint() = TextPaint(Paint.ANTI_ALIAS_FLAG).apply {
            color = ContextCompat.getColor(context, R.color.on_surface)
            textSize = 14f
            typeface = regularTypeface
        }

        private fun textAlignment(): Layout.Alignment = Layout.Alignment.ALIGN_NORMAL

        @Suppress("WrongConstant")
        private fun buildLayout(
            text: String,
            paint: TextPaint,
            alignment: Layout.Alignment = textAlignment()
        ): StaticLayout {
            val direction = TextDirectionHeuristics.RTL
            val builder = StaticLayout.Builder.obtain(text, 0, text.length, paint, textWidth)
                .setAlignment(alignment)
                .setTextDirection(direction)
                .setLineSpacing(2f, 1.4f)
                .setIncludePad(false)
                .setBreakStrategy(Layout.BREAK_STRATEGY_HIGH_QUALITY)
                .setHyphenationFrequency(Layout.HYPHENATION_FREQUENCY_NONE)
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P) {
                builder.setUseLineSpacingFromFallbacks(false)
            }
            return builder.build()
        }

        private fun loadBitmap(resId: Int, width: Int, height: Int): Bitmap? {
            val decoded = BitmapFactory.decodeResource(context.resources, resId) ?: return null
            val scaled = Bitmap.createScaledBitmap(decoded, width, height, true)
            if (scaled != decoded) decoded.recycle()
            return scaled
        }

        fun finish(): Int {
            drawPageFooter()
            document.finishPage(page)
            return pageNumber
        }
    }

    private class PdfPrintDocumentAdapter(
        private val file: File,
        private val jobName: String
    ) : PrintDocumentAdapter() {

        private var pageCount = 0

        override fun onLayout(
            oldAttributes: PrintAttributes?,
            newAttributes: PrintAttributes?,
            cancellationSignal: CancellationSignal?,
            callback: LayoutResultCallback,
            extras: android.os.Bundle?
        ) {
            if (cancellationSignal?.isCanceled == true) {
                callback.onLayoutCancelled()
                return
            }
            pageCount = readPageCount()
            if (pageCount <= 0) {
                callback.onLayoutFailed("PDF has no printable pages")
                return
            }
            val info = PrintDocumentInfo.Builder(jobName)
                .setContentType(PrintDocumentInfo.CONTENT_TYPE_DOCUMENT)
                .setPageCount(pageCount)
                .build()
            callback.onLayoutFinished(info, newAttributes != oldAttributes)
        }

        override fun onWrite(
            pages: Array<out PageRange>?,
            destination: ParcelFileDescriptor?,
            cancellationSignal: CancellationSignal?,
            callback: WriteResultCallback
        ) {
            if (cancellationSignal?.isCanceled == true) {
                callback.onWriteCancelled()
                return
            }
            if (destination == null) {
                callback.onWriteFailed("No print destination")
                return
            }
            try {
                FileInputStream(file).use { input ->
                    FileOutputStream(destination.fileDescriptor).use { output ->
                        input.copyTo(output)
                    }
                }
                callback.onWriteFinished(arrayOf(PageRange.ALL_PAGES))
            } catch (e: Exception) {
                callback.onWriteFailed(e.message)
            }
        }

        private fun readPageCount(): Int {
            val pfd = ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY)
            return try {
                PdfRenderer(pfd).use { it.pageCount }
            } finally {
                pfd.close()
            }
        }
    }
}
