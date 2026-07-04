package com.pakrecipes.cooking.util

import android.app.Activity
import android.content.ClipData
import android.content.ContentValues
import android.content.Context
import android.content.Intent
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
import com.pakrecipes.cooking.R
import com.pakrecipes.cooking.data.Recipe
import com.pakrecipes.cooking.data.RecipeRepository
import java.io.File
import java.io.FileInputStream
import java.io.FileOutputStream

object PdfExporter {

    private const val PAGE_WIDTH = 595
    private const val PAGE_HEIGHT = 842
    private const val MARGIN = 54f
    private const val TOP_MARGIN = 54f
    private const val BOTTOM_MARGIN = 54f
    private const val CONTENT_WIDTH = PAGE_WIDTH - MARGIN * 2
    private const val DOWNLOADS_FOLDER = "PakRecipes"

    data class ExportResult(val file: File, val displayName: String)

    fun exportRecipe(context: Context, recipe: Recipe): ExportResult {
        val displayName = "${recipe.id}_recipe.pdf"
        val file = File(context.cacheDir, displayName)
        if (file.exists()) file.delete()

        val document = PdfDocument()
        try {
            writeRecipePages(context, document, recipe, 1)
            FileOutputStream(file).use { document.writeTo(it) }
        } finally {
            document.close()
        }
        return ExportResult(file, displayName)
    }

    fun exportAllRecipes(context: Context): ExportResult {
        val displayName = "pakistan_restaurant_recipes.pdf"
        val file = File(context.cacheDir, displayName)
        if (file.exists()) file.delete()

        val document = PdfDocument()
        try {
            var pageNumber = 1
            pageNumber = writeCoverPage(context, document, pageNumber)
            for (recipe in RecipeRepository.getAll()) {
                pageNumber = writeRecipePages(context, document, recipe, pageNumber)
            }
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
        val uri = fileUri(context, file)
        val intent = Intent(Intent.ACTION_VIEW).apply {
            setDataAndType(uri, "application/pdf")
            clipData = ClipData.newRawUri("pdf", uri)
            addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
        }
        val chooser = Intent.createChooser(intent, context.getString(R.string.pdf_open))
        if (context !is Activity) chooser.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
        context.startActivity(chooser)
    }

    fun sharePdf(context: Context, file: File) {
        val uri = fileUri(context, file)
        val intent = Intent(Intent.ACTION_SEND).apply {
            type = "application/pdf"
            putExtra(Intent.EXTRA_STREAM, uri)
            clipData = ClipData.newRawUri("pdf", uri)
            addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
        }
        val chooser = Intent.createChooser(intent, context.getString(R.string.share_pdf))
        if (context !is Activity) chooser.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
        context.startActivity(chooser)
    }

    fun saveToDownloads(context: Context, result: ExportResult): Uri? {
        val uri = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            saveToDownloadsMediaStore(context, result)
        } else {
            saveToDownloadsLegacy(context, result)
        }
        if (uri != null) {
            Toast.makeText(context, context.getString(R.string.pdf_saved_downloads, result.displayName), Toast.LENGTH_LONG).show()
        } else {
            Toast.makeText(context, R.string.pdf_save_failed, Toast.LENGTH_SHORT).show()
        }
        return uri
    }

    fun printPdf(activity: Activity, result: ExportResult) {
        val printManager = activity.getSystemService(Context.PRINT_SERVICE) as PrintManager
        val adapter = PdfPrintAdapter(result.file, result.displayName)
        printManager.print(
            result.displayName, adapter,
            PrintAttributes.Builder()
                .setMediaSize(PrintAttributes.MediaSize.ISO_A4)
                .setResolution(PrintAttributes.Resolution("pdf", "pdf", 600, 600))
                .setMinMargins(PrintAttributes.Margins.NO_MARGINS)
                .setColorMode(PrintAttributes.COLOR_MODE_COLOR)
                .build()
        )
    }

    private fun fileUri(context: Context, file: File): Uri =
        FileProvider.getUriForFile(context, "${context.packageName}.fileprovider", file)

    @RequiresApi(Build.VERSION_CODES.Q)
    private fun saveToDownloadsMediaStore(context: Context, result: ExportResult): Uri? {
        val resolver = context.contentResolver
        val values = ContentValues().apply {
            put(MediaStore.Downloads.DISPLAY_NAME, result.displayName)
            put(MediaStore.Downloads.MIME_TYPE, "application/pdf")
            put(MediaStore.Downloads.RELATIVE_PATH, "${Environment.DIRECTORY_DOWNLOADS}/$DOWNLOADS_FOLDER")
            put(MediaStore.Downloads.IS_PENDING, 1)
        }
        val uri = resolver.insert(MediaStore.Downloads.EXTERNAL_CONTENT_URI, values) ?: return null
        try {
            resolver.openOutputStream(uri)?.use { out ->
                FileInputStream(result.file).use { it.copyTo(out) }
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
        val dir = File(Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS), DOWNLOADS_FOLDER)
        if (!dir.exists() && !dir.mkdirs()) return null
        val target = File(dir, result.displayName)
        result.file.copyTo(target, overwrite = true)
        return fileUri(context, target)
    }

    private fun writeCoverPage(context: Context, document: PdfDocument, pageNumber: Int): Int {
        val writer = PageWriter(context, document, pageNumber)
        writer.y = PAGE_HEIGHT / 2f - 80f
        writer.drawTitleCentered("🍽️")
        writer.drawTitleCentered("پاکستانی ریستوران ترکیبیں")
        writer.drawBodyCentered("گھر میں بنائیں — ملک کے مشہور شہروں کے پکوان")
        writer.space(24f)
        writer.drawBodyCentered("کراچی • لاہور • پشاور • کوئٹہ • حیدرآباد • ملتان • اسلام آباد")
        return writer.finish()
    }

    private fun writeRecipePages(
        context: Context,
        document: PdfDocument,
        recipe: Recipe,
        startPage: Int
    ): Int {
        val writer = PageWriter(context, document, startPage)

        writer.drawTitle(recipe.nameUrdu)
        writer.drawSection("${recipe.cityId.toCityName()}  |  ${recipe.difficulty.labelUrdu}  |  ${recipe.servings} افراد")
        val timeText = "تیاری: ${UrduPdfText.numberedItem(recipe.prepTimeMinutes, "منٹ")} | پکانا: ${UrduPdfText.numberedItem(recipe.cookTimeMinutes, "منٹ")}"
        writer.drawBody(timeText)
        writer.space(8f)
        writer.drawBody(recipe.descriptionUrdu)
        writer.space(12f)

        writer.drawSection("اجزاء")
        for (ingredient in recipe.ingredientsUrdu) {
            writer.drawBody(UrduPdfText.bulletItem(ingredient))
            writer.space(3f)
        }
        writer.space(10f)

        writer.drawSection("ترکیب")
        recipe.stepsUrdu.forEachIndexed { idx, step ->
            writer.drawBody(UrduPdfText.numberedItem(idx + 1, step))
            writer.space(5f)
        }
        writer.space(10f)

        writer.drawSection("خاص مشورے")
        for (tip in recipe.tipsUrdu) {
            writer.drawBody(UrduPdfText.bulletItem(tip))
            writer.space(4f)
        }

        return writer.finish()
    }

    private fun String.toCityName(): String = when (this) {
        "karachi" -> "کراچی"
        "lahore" -> "لاہور"
        "peshawar" -> "پشاور"
        "quetta" -> "کوئٹہ"
        "hyderabad" -> "حیدرآباد"
        "multan" -> "ملتان"
        "islamabad" -> "اسلام آباد"
        "rawalpindi" -> "راولپنڈی"
        "gilgit" -> "گلگت بلتستان"
        else -> this
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
                Typeface.create(Typeface.DEFAULT, if (bold) Typeface.BOLD else Typeface.NORMAL)
            }
        }

        private fun newPage() {
            if (::page.isInitialized) {
                drawPageFooter()
                document.finishPage(page)
            }
            val pageInfo = PdfDocument.PageInfo.Builder(PAGE_WIDTH, PAGE_HEIGHT, pageNumber)
                .setContentRect(
                    android.graphics.Rect(
                        MARGIN.toInt(), TOP_MARGIN.toInt(),
                        (PAGE_WIDTH - MARGIN).toInt(), (PAGE_HEIGHT - BOTTOM_MARGIN).toInt()
                    )
                )
                .create()
            page = document.startPage(pageInfo)
            canvas = page.canvas
            displayPageNumber = pageNumber
            pageNumber++
            y = TOP_MARGIN
        }

        private fun drawPageFooter() {
            val sepY = PAGE_HEIGHT - BOTTOM_MARGIN + 4f
            canvas.drawLine(MARGIN, sepY, PAGE_WIDTH - MARGIN, sepY,
                Paint().also { it.color = 0xFFD4B896.toInt(); it.strokeWidth = 0.5f })
            val label = UrduPdfText.pageNumber(displayPageNumber)
            val paint = TextPaint(Paint.ANTI_ALIAS_FLAG).apply {
                color = ContextCompat.getColor(context, R.color.secondary)
                textSize = 11f
                typeface = regularTypeface
                textAlign = Paint.Align.CENTER
            }
            canvas.drawText(label, PAGE_WIDTH / 2f, PAGE_HEIGHT - (BOTTOM_MARGIN / 3f), paint)
        }

        private fun availableHeight() = PAGE_HEIGHT - BOTTOM_MARGIN - y

        private fun ensureSpace(needed: Float) {
            if (needed > availableHeight()) newPage()
        }

        fun space(amount: Float) { y += amount }

        fun drawTitle(text: String) = drawTextBlock(text, titlePaint(26f), 12f)

        fun drawTitleCentered(text: String) = drawTextBlock(text, titlePaint(22f), 10f, Layout.Alignment.ALIGN_CENTER)

        fun drawSection(text: String) = drawTextBlock(text, sectionPaint(15f), 8f)

        fun drawBody(text: String, paint: TextPaint = bodyPaint()) = drawTextBlock(text, paint, 10f)

        fun drawBodyCentered(text: String) = drawTextBlock(text, bodyPaint(), 8f, Layout.Alignment.ALIGN_CENTER)

        private fun drawTextBlock(
            text: String, paint: TextPaint, spacingAfter: Float,
            alignment: Layout.Alignment = Layout.Alignment.ALIGN_NORMAL
        ) {
            if (text.isBlank()) return
            val prepared = UrduPdfText.normalize(text)
            val layout = buildLayout(prepared, paint, alignment)
            var startLine = 0
            val totalLines = layout.lineCount

            while (startLine < totalLines) {
                var endLine = startLine + 1
                while (endLine <= totalLines) {
                    val h = layout.getLineBottom(endLine - 1) - layout.getLineTop(startLine)
                    if (h > availableHeight()) { if (endLine - 1 > startLine) endLine--; break }
                    if (endLine == totalLines) break
                    endLine++
                }
                val blockH = layout.getLineBottom(endLine - 1) - layout.getLineTop(startLine) + spacingAfter
                ensureSpace(blockH)
                canvas.save()
                canvas.translate(MARGIN, y)
                canvas.clipRect(0f, layout.getLineTop(startLine).toFloat(), textWidth.toFloat(), layout.getLineBottom(endLine - 1).toFloat())
                canvas.translate(0f, -layout.getLineTop(startLine).toFloat())
                layout.draw(canvas)
                canvas.restore()
                y += blockH
                startLine = endLine
                if (startLine < totalLines) newPage()
            }
        }

        private fun titlePaint(size: Float) = TextPaint(Paint.ANTI_ALIAS_FLAG).apply {
            color = ContextCompat.getColor(context, R.color.primary)
            textSize = size
            typeface = boldTypeface
        }

        private fun sectionPaint(size: Float) = TextPaint(Paint.ANTI_ALIAS_FLAG).apply {
            color = ContextCompat.getColor(context, R.color.secondary)
            textSize = size
            typeface = boldTypeface
        }

        private fun bodyPaint() = TextPaint(Paint.ANTI_ALIAS_FLAG).apply {
            color = ContextCompat.getColor(context, R.color.on_surface)
            textSize = 14f
            typeface = regularTypeface
        }

        @Suppress("WrongConstant")
        private fun buildLayout(text: String, paint: TextPaint, alignment: Layout.Alignment): StaticLayout {
            val builder = StaticLayout.Builder.obtain(text, 0, text.length, paint, textWidth)
                .setAlignment(alignment)
                .setTextDirection(TextDirectionHeuristics.RTL)
                .setLineSpacing(2f, 1.45f)
                .setIncludePad(false)
                .setBreakStrategy(Layout.BREAK_STRATEGY_HIGH_QUALITY)
                .setHyphenationFrequency(Layout.HYPHENATION_FREQUENCY_NONE)
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P) {
                builder.setUseLineSpacingFromFallbacks(false)
            }
            return builder.build()
        }

        fun finish(): Int {
            drawPageFooter()
            document.finishPage(page)
            return pageNumber
        }
    }

    private class PdfPrintAdapter(
        private val file: File,
        private val jobName: String
    ) : PrintDocumentAdapter() {

        override fun onLayout(
            oldAttributes: PrintAttributes?, newAttributes: PrintAttributes?,
            cancellationSignal: CancellationSignal?, callback: LayoutResultCallback, extras: android.os.Bundle?
        ) {
            if (cancellationSignal?.isCanceled == true) { callback.onLayoutCancelled(); return }
            val count = readPageCount()
            if (count <= 0) { callback.onLayoutFailed("No pages"); return }
            callback.onLayoutFinished(
                PrintDocumentInfo.Builder(jobName).setContentType(PrintDocumentInfo.CONTENT_TYPE_DOCUMENT).setPageCount(count).build(),
                newAttributes != oldAttributes
            )
        }

        override fun onWrite(
            pages: Array<out PageRange>?, destination: ParcelFileDescriptor?,
            cancellationSignal: CancellationSignal?, callback: WriteResultCallback
        ) {
            if (cancellationSignal?.isCanceled == true) { callback.onWriteCancelled(); return }
            if (destination == null) { callback.onWriteFailed("No destination"); return }
            try {
                FileInputStream(file).use { input ->
                    FileOutputStream(destination.fileDescriptor).use { input.copyTo(it) }
                }
                callback.onWriteFinished(arrayOf(PageRange.ALL_PAGES))
            } catch (e: Exception) {
                callback.onWriteFailed(e.message)
            }
        }

        private fun readPageCount(): Int {
            val pfd = ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY)
            return try { PdfRenderer(pfd).use { it.pageCount } } finally { pfd.close() }
        }
    }
}
