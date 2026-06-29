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

    private const val PAGE_WIDTH = 595
    private const val PAGE_HEIGHT = 842
    private const val MARGIN = 48f
    private const val BOTTOM_MARGIN = 56f
    private const val IMAGE_HEIGHT = 150f
    private const val DOWNLOADS_FOLDER = "IntimacyGuide"

    data class ExportResult(
        val file: File,
        val displayName: String
    )

    fun exportFullGuide(context: Context, language: String): ExportResult {
        val displayName = if (language == LocaleHelper.LANG_UR) {
            "intimacy_guide_urdu.pdf"
        } else {
            "intimacy_guide_english.pdf"
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
                .setMinMargins(PrintAttributes.Margins.NO_MARGINS)
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

        val title = if (isRtl) "مکمل رہنمائی قریبی تعلق" else "Ultimate Intimacy Guide"
        val subtitle = if (isRtl) {
            "جوڑوں کے لیے تصویری رہنمائی • انگریزی و اردو"
        } else {
            "Illustrated Sex Education Guide for Couples"
        }
        val intro = if (isRtl) {
            "یہ گائیڈ آپ کو قریبی پوزیشنز سیکھنے، باہمی رضامندی، آرام دہ مواصلات، " +
                "اور ایک دوسرے کے ساتھ محفوظ تجربہ کرنے میں مدد دیتی ہے۔"
        } else {
            "This guide helps couples learn intimate postures with educational diagrams, " +
                "mutual consent practices, and comfort-focused communication."
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
                writer.drawBody("• $point")
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
        writer.y = PAGE_HEIGHT / 2f - 20f
        writer.drawTitle(title, 24f)
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
        writer.drawBody("${content.category}  |  ${posture.difficulty.label(language)}")
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
            writer.drawBody("${index + 1}. $step")
            writer.space(4f)
        }
        writer.space(6f)

        val tipsLabel = if (isRtl) "آرام کے مشورے" else "Comfort Tips"
        writer.drawSection(tipsLabel)
        for (tip in content.tips) {
            writer.drawBody("• $tip")
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
        private val textWidth = (PAGE_WIDTH - MARGIN * 2).toInt()
        private var pageNumber = startPage
        private lateinit var page: PdfDocument.Page
        private lateinit var canvas: Canvas
        var y = MARGIN + 8f

        private val regularTypeface: Typeface = loadTypeface(false)
        private val boldTypeface: Typeface = loadTypeface(true)

        init {
            newPage()
        }

        private fun loadTypeface(bold: Boolean): Typeface {
            return if (isRtl) {
                try {
                    Typeface.createFromAsset(context.assets, "fonts/NotoNaskhArabic-Regular.ttf")
                } catch (_: Exception) {
                    Typeface.DEFAULT
                }
            } else {
                Typeface.create(Typeface.DEFAULT, if (bold) Typeface.BOLD else Typeface.NORMAL)
            }
        }

        private fun newPage() {
            if (::page.isInitialized) {
                drawPageNumber()
                document.finishPage(page)
            }
            val pageInfo = PdfDocument.PageInfo.Builder(PAGE_WIDTH, PAGE_HEIGHT, pageNumber).create()
            page = document.startPage(pageInfo)
            canvas = page.canvas
            pageNumber++
            y = MARGIN + 8f
        }

        private fun drawPageNumber() {
            val paint = TextPaint().apply {
                color = ContextCompat.getColor(context, R.color.secondary)
                textSize = 10f
                textAlign = Paint.Align.CENTER
            }
            val label = pageNumber.toString()
            canvas.drawText(label, PAGE_WIDTH / 2f, PAGE_HEIGHT - 24f, paint)
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
            drawWrappedLine(text, titlePaint(size), size + 12f)
        }

        fun drawHeading(text: String) {
            drawWrappedLine(text, titlePaint(20f), 28f)
        }

        fun drawSection(text: String) {
            val paint = sectionPaint(14f)
            ensureSpace(22f)
            val x = if (isRtl) PAGE_WIDTH - MARGIN else MARGIN
            canvas.drawText(text, x, y + 14f, paint)
            y += 22f
        }

        private fun drawWrappedLine(text: String, paint: TextPaint, lineHeight: Float) {
            val layout = buildLayout(text, paint)
            if (layout.lineCount <= 1) {
                ensureSpace(lineHeight)
                val x = if (isRtl) PAGE_WIDTH - MARGIN else MARGIN
                canvas.drawText(text, x, y + paint.textSize, paint)
                y += lineHeight
                return
            }
            drawBody(text, paint)
        }

        fun drawBody(text: String, paint: TextPaint = bodyPaint()) {
            if (text.isBlank()) return

            val layout = buildLayout(text, paint)
            var startLine = 0
            val totalLines = layout.lineCount

            while (startLine < totalLines) {
                var endLine = startLine + 1
                while (endLine <= totalLines) {
                    val chunkHeight = layout.getLineBottom(endLine - 1) - layout.getLineTop(startLine)
                    val available = availableHeight()
                    if (chunkHeight > available) {
                        if (endLine - 1 > startLine) {
                            endLine--
                        }
                        break
                    }
                    if (endLine == totalLines) break
                    endLine++
                }

                val startChar = layout.getLineStart(startLine)
                val endChar = layout.getLineStart(endLine)
                val chunk = text.substring(startChar, endChar)
                val chunkLayout = buildLayout(chunk, paint)
                val chunkHeight = chunkLayout.height.toFloat() + 6f

                ensureSpace(chunkHeight)
                canvas.save()
                canvas.translate(if (isRtl) PAGE_WIDTH - MARGIN - textWidth else MARGIN, y)
                chunkLayout.draw(canvas)
                canvas.restore()
                y += chunkHeight

                startLine = endLine
                if (startLine < totalLines) {
                    newPage()
                }
            }
        }

        fun drawImage(resId: Int, width: Int, height: Int) {
            val bitmap = loadBitmap(resId, width, height) ?: return
            ensureSpace(height + 12f)
            val left = (PAGE_WIDTH - width) / 2f
            canvas.drawBitmap(bitmap, left, y, null)
            y += height + 12f
            bitmap.recycle()
        }

        fun sectionPaint(size: Float): TextPaint = TextPaint().apply {
            color = ContextCompat.getColor(context, R.color.secondary)
            textSize = size
            typeface = boldTypeface
            textAlign = if (isRtl) Paint.Align.RIGHT else Paint.Align.LEFT
        }

        private fun titlePaint(size: Float) = TextPaint().apply {
            color = ContextCompat.getColor(context, R.color.primary)
            textSize = size
            typeface = boldTypeface
            textAlign = if (isRtl) Paint.Align.RIGHT else Paint.Align.LEFT
        }

        private fun bodyPaint() = TextPaint().apply {
            color = ContextCompat.getColor(context, R.color.on_surface)
            textSize = 12f
            typeface = regularTypeface
            textAlign = if (isRtl) Paint.Align.RIGHT else Paint.Align.LEFT
        }

        private fun buildLayout(text: String, paint: TextPaint): StaticLayout {
            val alignment = if (isRtl) Layout.Alignment.ALIGN_OPPOSITE else Layout.Alignment.ALIGN_NORMAL
            return StaticLayout.Builder.obtain(text, 0, text.length, paint, textWidth)
                .setAlignment(alignment)
                .setLineSpacing(0f, 1.25f)
                .setIncludePad(true)
                .build()
        }

        private fun loadBitmap(resId: Int, width: Int, height: Int): Bitmap? {
            val decoded = BitmapFactory.decodeResource(context.resources, resId) ?: return null
            val scaled = Bitmap.createScaledBitmap(decoded, width, height, true)
            if (scaled != decoded) decoded.recycle()
            return scaled
        }

        fun finish(): Int {
            drawPageNumber()
            document.finishPage(page)
            return pageNumber
        }
    }

    private class PdfPrintDocumentAdapter(
        private val file: File,
        private val jobName: String
    ) : PrintDocumentAdapter() {

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
            val info = PrintDocumentInfo.Builder(jobName)
                .setContentType(PrintDocumentInfo.CONTENT_TYPE_DOCUMENT)
                .setPageCount(PrintDocumentInfo.PAGE_COUNT_UNKNOWN)
                .build()
            callback.onLayoutFinished(info, true)
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
            try {
                FileInputStream(file).use { input ->
                    FileOutputStream(destination?.fileDescriptor).use { output ->
                        input.copyTo(output)
                    }
                }
                callback.onWriteFinished(arrayOf(PageRange.ALL_PAGES))
            } catch (e: Exception) {
                callback.onWriteFailed(e.message)
            }
        }
    }
}
