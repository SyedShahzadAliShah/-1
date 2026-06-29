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
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import androidx.core.content.FileProvider
import com.couplesguide.postures.R
import com.couplesguide.postures.data.EducationalInsert
import com.couplesguide.postures.data.EducationalInsertRepository
import com.couplesguide.postures.data.GuideRepository
import com.couplesguide.postures.data.Posture
import com.couplesguide.postures.data.PostureRepository
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
    private const val DOWNLOADS_FOLDER = "IntimacyGuide"

    data class ExportResult(
        val file: File,
        val displayName: String
    )

    fun exportFullGuide(context: Context, language: String): ExportResult {
        val displayName = if (language == LocaleHelper.LANG_UR) {
            "intimacy_handbook_urdu.pdf"
        } else {
            "intimacy_handbook_english.pdf"
        }
        val file = File(context.cacheDir, displayName)
        if (file.exists()) file.delete()

        val document = PdfDocument()
        try {
            var pageNumber = 1
            pageNumber = writeTitlePage(context, document, language, pageNumber)
            pageNumber = writeChapters(context, document, language, pageNumber)
            pageNumber = writeImaginationSection(context, document, language, pageNumber)
            writePhysicalPosturesWithEducation(context, document, language, pageNumber)
            FileOutputStream(file).use { document.writeTo(it) }
        } finally {
            document.close()
        }
        return ExportResult(file, displayName)
    }

    fun exportPosture(context: Context, posture: Posture, language: String): ExportResult {
        val displayName = "${posture.id}_${language}.pdf"
        val file = File(context.cacheDir, displayName)
        if (file.exists()) file.delete()

        val document = PdfDocument()
        try {
            writePosturePages(context, document, posture, language, 1)
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
        language: String,
        pageNumber: Int
    ): Int {
        val writer = PageWriter(context, document, language, pageNumber)
        val isRtl = language == LocaleHelper.LANG_UR

        val title = if (isRtl) "مکمل قربت کی ہینڈ بک" else "Ultimate Intimacy Handbook"
        val subtitle = if (isRtl) {
            "جوڑوں کے لیے تصویری جنسی تعلیم • انگریزی و اردو"
        } else {
            "Illustrated Sex Education Handbook for Couples"
        }
        val intro = if (isRtl) {
            "یہ ہینڈ بک تصویری ہدایات کے ساتھ قریبی پوزیشنز سیکھنے، باہمی رضامندی، " +
                "آرام دہ مواصلات اور محفوظ تجربہ کرنے میں جوڑوں کی مدد کرتی ہے۔"
        } else {
            "This handbook uses illustrated educational diagrams to help couples learn " +
                "intimate postures with mutual consent, comfort-focused communication, and safety."
        }

        writer.drawTitle(title)
        writer.drawBody(subtitle, writer.sectionPaint(14f))
        writer.space(12f)
        writer.drawBody(intro)
        writer.space(16f)
        writer.drawImage(R.drawable.pic_guide_cover, 320, 190)
        return writer.finish()
    }

    private fun writeChapters(
        context: Context,
        document: PdfDocument,
        language: String,
        startPage: Int
    ): Int {
        var pageNumber = startPage
        for (chapter in GuideRepository.getChapters()) {
            val content = chapter.content(language)
            val writer = PageWriter(context, document, language, pageNumber)
            writer.drawImage(chapter.illustrationRes, 280, 160)
            writer.drawHeading(content.title)
            writer.drawBody(content.summary)
            writer.space(8f)
            writer.drawBody(content.body)
            writer.space(8f)
            val pointsHeader = if (language == LocaleHelper.LANG_UR) "اہم نکات:" else "Key Points:"
            writer.drawSection(pointsHeader)
            for (point in content.keyPoints) {
                val line = if (language == LocaleHelper.LANG_UR) {
                    UrduPdfText.bulletItem(point)
                } else {
                    "• $point"
                }
                writer.drawBody(line)
                writer.space(4f)
            }
            pageNumber = writer.finish()
        }
        return pageNumber
    }

    private fun writeImaginationSection(
        context: Context,
        document: PdfDocument,
        language: String,
        startPage: Int
    ): Int {
        var pageNumber = startPage
        pageNumber = writeSectionDivider(
            context, document, language, pageNumber,
            context.getString(R.string.imagination_postures)
        )
        for (posture in PostureRepository.getImaginationPostures()) {
            pageNumber = writePosturePages(context, document, posture, language, pageNumber)
        }
        pageNumber = writeSectionDivider(
            context, document, language, pageNumber,
            context.getString(R.string.all_postures)
        )
        return pageNumber
    }

    private fun writePhysicalPosturesWithEducation(
        context: Context,
        document: PdfDocument,
        language: String,
        startPage: Int
    ): Int {
        var pageNumber = startPage
        val categoryOrder = listOf(
            PostureRepository.CAT_FACE,
            PostureRepository.CAT_SIDE,
            PostureRepository.CAT_REAR,
            PostureRepository.CAT_STANDING,
            PostureRepository.CAT_VARIATIONS
        )
        val physical = PostureRepository.getPhysicalPostures()
        var lastCategory: String? = null

        for (categoryId in categoryOrder) {
            val group = physical.filter { it.categoryId == categoryId }
            if (group.isEmpty()) continue
            lastCategory?.let { previous ->
                EducationalInsertRepository.getInsertAfterCategory(previous)?.let { insert ->
                    pageNumber = writeEducationalPage(context, document, insert, language, pageNumber)
                }
            }
            for (posture in group) {
                pageNumber = writePosturePages(context, document, posture, language, pageNumber)
            }
            lastCategory = categoryId
        }

        lastCategory?.let { categoryId ->
            EducationalInsertRepository.getInsertAfterCategory(categoryId)?.let { insert ->
                pageNumber = writeEducationalPage(context, document, insert, language, pageNumber)
            }
        }
        return pageNumber
    }

    private fun writeEducationalPage(
        context: Context,
        document: PdfDocument,
        insert: EducationalInsert,
        language: String,
        pageNumber: Int
    ): Int {
        val writer = PageWriter(context, document, language, pageNumber)
        val isUrdu = language == LocaleHelper.LANG_UR
        val eduLabel = if (isUrdu) "جنسی تعلیم" else "Sex Education"
        writer.drawSection(eduLabel)
        writer.drawImage(insert.illustrationRes, 360, 200)
        writer.drawHeading(if (isUrdu) insert.urduTitle else insert.englishTitle)
        writer.drawBody(if (isUrdu) insert.urduCaption else insert.englishCaption)
        return writer.finish()
    }

    private fun writeSectionDivider(
        context: Context,
        document: PdfDocument,
        language: String,
        pageNumber: Int,
        title: String
    ): Int {
        val writer = PageWriter(context, document, language, pageNumber)
        writer.y = PAGE_HEIGHT / 2f - 24f
        writer.drawTitleCentered(title, 24f)
        return writer.finish()
    }

    private fun writePosturePages(
        context: Context,
        document: PdfDocument,
        posture: Posture,
        language: String,
        startPage: Int
    ): Int {
        val content = posture.content(language)
        val isRtl = language == LocaleHelper.LANG_UR
        val writer = PageWriter(context, document, language, startPage)

        writer.drawImage(posture.illustrationRes, 340, IMAGE_HEIGHT.toInt())
        writer.drawHeading(content.name)
        val metaLine = if (isRtl) {
            UrduPdfText.metaLine(content.category, posture.difficulty.label(language))
        } else {
            "${content.category}  |  ${posture.difficulty.label(language)}"
        }
        writer.drawBody(metaLine)
        writer.space(8f)
        writer.drawBody(content.summary)
        writer.space(10f)

        val aboutLabel = if (isRtl) "تفصیل" else "About"
        writer.drawSection(aboutLabel)
        writer.drawBody(content.description)
        writer.space(8f)

        val stepsLabel = when {
            posture.isImagination && isRtl -> "تخیلی مشق"
            posture.isImagination -> "Imagination Exercise"
            isRtl -> "طریقہ کار"
            else -> "How To"
        }
        writer.drawSection(stepsLabel)
        content.steps.forEachIndexed { index, step ->
            val line = if (isRtl) {
                UrduPdfText.numberedItem(index + 1, step)
            } else {
                "${index + 1}. $step"
            }
            writer.drawBody(line)
            writer.space(4f)
        }
        writer.space(6f)

        val tipsLabel = if (isRtl) "آرام کے مشورے" else "Comfort Tips"
        writer.drawSection(tipsLabel)
        for (tip in content.tips) {
            val line = if (isRtl) UrduPdfText.bulletItem(tip) else "• $tip"
            writer.drawBody(line)
            writer.space(4f)
        }
        return writer.finish()
    }

    private class PageWriter(
        private val context: Context,
        private val document: PdfDocument,
        private val language: String,
        startPage: Int
    ) {
        private val isRtl = language == LocaleHelper.LANG_UR
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
            if (!isRtl) {
                return Typeface.create(Typeface.DEFAULT, if (bold) Typeface.BOLD else Typeface.NORMAL)
            }
            // Only Regular is available in assets; using faux-bold on Naskh
            // distorts Arabic letterforms, so we use Regular for all Urdu text
            // and compensate with larger font sizes for headings.
            return try {
                Typeface.createFromAsset(context.assets, "fonts/NotoNaskhArabic-Regular.ttf")
            } catch (_: Exception) {
                Typeface.DEFAULT
            }
        }

        private fun prepareText(text: String): String =
            if (isRtl) UrduPdfText.normalize(text) else text

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

            val label = if (isRtl) {
                UrduPdfText.pageNumber(displayPageNumber)
            } else {
                displayPageNumber.toString()
            }
            val footerPaint = TextPaint(Paint.ANTI_ALIAS_FLAG).apply {
                color = ContextCompat.getColor(context, R.color.secondary)
                textSize = if (isRtl) 11f else 9f
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

        fun drawTitle(text: String, size: Float = if (isRtl) 28f else 28f) {
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
            drawTextBlock(text, titlePaint(if (isRtl) 21f else 20f), spacingAfter = 10f)
        }

        fun drawSection(text: String) {
            drawTextBlock(text, sectionPaint(if (isRtl) 16f else 14f), spacingAfter = 8f)
        }

        fun drawBody(text: String, paint: TextPaint = bodyPaint()) {
            drawTextBlock(text, paint, spacingAfter = if (isRtl) 10f else 6f)
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
            textSize = if (isRtl) 14f else 12f
            typeface = regularTypeface
        }

        private fun textAlignment(): Layout.Alignment = Layout.Alignment.ALIGN_NORMAL

        private fun buildLayout(
            text: String,
            paint: TextPaint,
            alignment: Layout.Alignment = textAlignment()
        ): StaticLayout {
            val direction = if (isRtl) TextDirectionHeuristics.RTL else TextDirectionHeuristics.LTR
            val builder = StaticLayout.Builder.obtain(text, 0, text.length, paint, textWidth)
                .setAlignment(alignment)
                .setTextDirection(direction)
                .setLineSpacing(2f, if (isRtl) 1.4f else 1.2f)
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
