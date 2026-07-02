package com.seccap.admissions.util

import android.app.Activity
import android.content.ClipData
import android.content.ContentValues
import android.content.Context
import android.content.Intent
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
import com.seccap.admissions.R
import com.seccap.admissions.data.ApplicationDraft
import com.seccap.admissions.data.CollegeRepository
import com.seccap.admissions.data.FacultyRepository
import com.seccap.admissions.data.GuideRepository
import java.io.File
import java.io.FileInputStream
import java.io.FileOutputStream
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

object PdfExporter {

    private const val PAGE_WIDTH = 595
    private const val PAGE_HEIGHT = 842
    private const val MARGIN = 54f
    private const val TOP_MARGIN = 54f
    private const val BOTTOM_MARGIN = 54f
    private const val CONTENT_WIDTH = PAGE_WIDTH - MARGIN * 2
    private const val RTL_EDGE_PAD = 14f   // extra inset so Urdu glyphs don't clip at the right edge
    private const val DOWNLOADS_FOLDER = "SecCapAdmissions"

    data class ExportResult(
        val file: File,
        val displayName: String
    )

    fun exportApplication(context: Context, draft: ApplicationDraft, language: String): ExportResult {
        val displayName = if (language == LocaleHelper.LANG_UR) {
            "seccap_application_${draft.applicationId}_urdu.pdf"
        } else {
            "seccap_application_${draft.applicationId}_english.pdf"
        }
        val file = File(context.cacheDir, displayName)
        if (file.exists()) file.delete()

        val document = PdfDocument()
        try {
            writeApplicationSummary(context, document, draft, language)
            FileOutputStream(file).use { document.writeTo(it) }
        } finally {
            document.close()
        }
        return ExportResult(file, displayName)
    }

    fun exportGuide(context: Context, language: String): ExportResult {
        val displayName = if (language == LocaleHelper.LANG_UR) {
            "seccap_admission_guide_urdu.pdf"
        } else {
            "seccap_admission_guide_english.pdf"
        }
        val file = File(context.cacheDir, displayName)
        if (file.exists()) file.delete()

        val document = PdfDocument()
        try {
            writeGuide(context, document, language)
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
        val printManager = activity.getSystemService(Context.PRINT_SERVICE) as PrintManager
        printManager.print(
            result.displayName,
            PdfPrintDocumentAdapter(result.file, result.displayName),
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

    private fun writeApplicationSummary(
        context: Context,
        document: PdfDocument,
        draft: ApplicationDraft,
        language: String
    ) {
        val isRtl = language == LocaleHelper.LANG_UR
        val writer = PageWriter(context, document, language, 1)
        val dateFmt = SimpleDateFormat("dd MMM yyyy, HH:mm", Locale.getDefault())

        val title = if (isRtl) "SECCAP درخواست کا خلاصہ" else "SECCAP Application Summary"
        val subtitle = if (isRtl) {
            "سندھ الیکٹرانک سینٹرلائزڈ کالج ایڈمیشن پروگرام"
        } else {
            "Sindh Electronic Centralized College Admission Program"
        }

        writer.drawTitle(title)
        writer.drawBody(subtitle, writer.sectionPaint(13f))
        writer.space(8f)
        writer.drawBody(
            if (isRtl) {
                UrduPdfText.fieldLine("درخواست ID", draft.applicationId)
            } else {
                "Application ID: ${draft.applicationId}"
            }
        )
        writer.drawBody(
            if (isRtl) {
                UrduPdfText.fieldLine("تاریخ", dateFmt.format(Date(draft.lastUpdated)))
            } else {
                "Date: ${dateFmt.format(Date(draft.lastUpdated))}"
            }
        )
        writer.space(12f)

        writer.drawSection(if (isRtl) "تعلیمی تفصیلات" else "Educational Details")
        writer.drawField(if (isRtl) "میٹرک رول نمبر" else "Matric Roll No.", draft.matricRollNumber)
        writer.drawField(if (isRtl) "9ویں رول نمبر" else "9th Roll No.", draft.ninthRollNumber)
        writer.drawField(if (isRtl) "بورڈ" else "Board", draft.boardName)
        writer.drawField(if (isRtl) "سال" else "Passing Year", draft.passingYear)
        writer.drawField(if (isRtl) "سکول" else "School", draft.schoolName)
        writer.drawField(
            if (isRtl) "نمبر" else "Marks",
            "${draft.obtainedMarks} / ${draft.totalMarks} (${String.format("%.1f", draft.percentage)}%)"
        )
        if (draft.grade.isNotBlank()) {
            writer.drawField(if (isRtl) "گریڈ" else "Grade", draft.grade)
        }

        writer.space(8f)
        writer.drawSection(if (isRtl) "ذاتی تفصیلات" else "Personal Details")
        writer.drawField(if (isRtl) "نام" else "Student Name", draft.studentName)
        writer.drawField(if (isRtl) "والد کا نام" else "Father's Name", draft.fatherName)
        writer.drawField(if (isRtl) "جنس" else "Gender", draft.gender)
        writer.drawField(if (isRtl) "تاریخ پیدائش" else "Date of Birth", draft.dateOfBirth)
        writer.drawField(if (isRtl) "B-Form" else "B-Form", draft.bFormNumber)
        if (draft.cnicNumber.isNotBlank()) {
            writer.drawField("CNIC", draft.cnicNumber)
        }
        writer.drawField(if (isRtl) "ڈومیسائل" else "Domicile", draft.domicile)
        writer.drawField(if (isRtl) "فون" else "Phone", draft.phoneNumber)
        if (draft.email.isNotBlank()) {
            writer.drawField(if (isRtl) "ای میل" else "Email", draft.email)
        }
        if (draft.address.isNotBlank()) {
            writer.drawField(if (isRtl) "پتہ" else "Address", draft.address)
        }

        writer.space(8f)
        writer.drawSection(if (isRtl) "گروپ اور زون" else "Faculty & Zone")
        val faculty = FacultyRepository.findById(draft.facultyId)
        writer.drawField(
            if (isRtl) "گروپ" else "Faculty",
            faculty?.name?.get(language) ?: draft.facultyId
        )
        val zone = CollegeRepository.findZone(draft.zoneId)
        writer.drawField(
            if (isRtl) "زون" else "Zone",
            zone?.name?.get(language) ?: draft.zoneId
        )

        writer.space(8f)
        writer.drawSection(if (isRtl) "کالج کی ترجیحات" else "College Preferences")
        if (draft.collegePreferences.isEmpty()) {
            writer.drawBody(if (isRtl) "کوئی کالج منتخب نہیں" else "No colleges selected")
        } else {
            draft.collegePreferences.forEachIndexed { index, collegeId ->
                val college = CollegeRepository.findCollege(collegeId)
                val name = college?.name?.get(language) ?: collegeId
                val line = if (isRtl) {
                    UrduPdfText.numberedItem(index + 1, name)
                } else {
                    "${index + 1}. $name"
                }
                writer.drawBody(line)
            }
        }

        writer.space(8f)
        writer.drawSection(if (isRtl) "دستاویزات" else "Documents Prepared")
        val docs = GuideRepository.getRequiredDocuments()
        for (doc in docs) {
            val checked = doc.id in draft.documentsChecked
            val status = if (checked) {
                if (isRtl) "✓" else "✓"
            } else {
                if (isRtl) "○" else "○"
            }
            val line = if (isRtl) {
                UrduPdfText.bulletItem("$status ${doc.name.urdu}")
            } else {
                "$status ${doc.name.english}"
            }
            writer.drawBody(line)
        }

        writer.space(16f)
        writer.drawBody(
            if (isRtl) {
                "یہ ایک معاون خلاصہ ہے۔ حتمی جمع کرانے کے لیے سرکاری پورٹل seccap.dgcs.gos.pk پر جائیں۔"
            } else {
                "This is a helper summary. Visit the official portal at seccap.dgcs.gos.pk for final submission."
            },
            writer.sectionPaint(11f)
        )
        writer.finish()
    }

    private fun writeGuide(context: Context, document: PdfDocument, language: String) {
        var pageNumber = 1
        val isRtl = language == LocaleHelper.LANG_UR

        val writer = PageWriter(context, document, language, pageNumber)
        writer.drawTitle(if (isRtl) "SECCAP داخلے کی رہنمائی" else "SECCAP Admission Guide")
        writer.drawBody(
            if (isRtl) "سندھ سرکاری کالجوں میں فرسٹ ایئر داخلے کے لیے مکمل رہنما"
            else "Complete guide for 1st-year admissions to Sindh government colleges"
        )
        pageNumber = writer.finish()

        for (section in GuideRepository.getSections()) {
            val w = PageWriter(context, document, language, pageNumber)
            w.drawHeading(section.title.get(language))
            w.drawBody(section.body.get(language))
            w.space(6f)
            for ((i, step) in section.steps.withIndex()) {
                val line = if (isRtl) {
                    UrduPdfText.numberedItem(i + 1, step.urdu)
                } else {
                    "${i + 1}. ${step.english}"
                }
                w.drawBody(line)
                w.space(4f)
            }
            pageNumber = w.finish()
        }

        val docWriter = PageWriter(context, document, language, pageNumber)
        docWriter.drawHeading(if (isRtl) "ضروری دستاویزات کی فہرست" else "Required Documents Checklist")
        for (doc in GuideRepository.getRequiredDocuments()) {
            val line = if (isRtl) {
                UrduPdfText.bulletItem("${doc.name.urdu}: ${doc.description.urdu}")
            } else {
                "• ${doc.name.english}: ${doc.description.english}"
            }
            docWriter.drawBody(line)
            docWriter.space(4f)
        }
        docWriter.finish()
    }

    private class PageWriter(
        private val context: Context,
        private val document: PdfDocument,
        private val language: String,
        startPage: Int
    ) {
        private val isRtl = language == LocaleHelper.LANG_UR
        private val layoutWidth = if (isRtl) {
            (CONTENT_WIDTH - RTL_EDGE_PAD * 2).toInt()
        } else {
            CONTENT_WIDTH.toInt()
        }
        private val contentLeft = if (isRtl) MARGIN + RTL_EDGE_PAD else MARGIN
        private val regularTypeface = loadTypeface(false)
        private val boldTypeface = loadTypeface(true)
        private var pageNumber = startPage
        private var displayPageNumber = startPage
        private lateinit var page: PdfDocument.Page
        private lateinit var canvas: android.graphics.Canvas
        var y = TOP_MARGIN

        init { newPage() }

        private fun loadTypeface(bold: Boolean): Typeface {
            if (!isRtl) return Typeface.create(Typeface.DEFAULT, if (bold) Typeface.BOLD else Typeface.NORMAL)
            return try {
                Typeface.createFromAsset(context.assets, "fonts/NotoNaskhArabic-Regular.ttf")
            } catch (_: Exception) {
                Typeface.DEFAULT
            }
        }

        private fun prepareText(text: String) = if (isRtl) UrduPdfText.normalize(text) else text

        private fun newPage() {
            if (::page.isInitialized) {
                drawPageFooter()
                document.finishPage(page)
            }
            val pageInfo = PdfDocument.PageInfo.Builder(PAGE_WIDTH, PAGE_HEIGHT, pageNumber)
                .setContentRect(android.graphics.Rect(
                    MARGIN.toInt(), TOP_MARGIN.toInt(),
                    (PAGE_WIDTH - MARGIN).toInt(), (PAGE_HEIGHT - BOTTOM_MARGIN).toInt()
                ))
                .create()
            page = document.startPage(pageInfo)
            canvas = page.canvas
            displayPageNumber = pageNumber
            pageNumber++
            y = TOP_MARGIN
        }

        private fun drawPageFooter() {
            val label = if (isRtl) UrduPdfText.pageNumber(displayPageNumber) else displayPageNumber.toString()
            val footerPaint = TextPaint(Paint.ANTI_ALIAS_FLAG).apply {
                color = ContextCompat.getColor(context, R.color.secondary)
                textSize = if (isRtl) 11f else 9f
                typeface = regularTypeface
                textAlign = Paint.Align.CENTER
            }
            canvas.drawText(label, PAGE_WIDTH / 2f, PAGE_HEIGHT - (BOTTOM_MARGIN / 3f), footerPaint)
        }

        private fun availableHeight() = PAGE_HEIGHT - BOTTOM_MARGIN - y

        private fun ensureSpace(needed: Float) {
            if (needed > availableHeight()) newPage()
        }

        fun space(amount: Float) { y += amount }

        fun drawTitle(text: String) = drawTextBlock(text, titlePaint(26f), 12f)

        fun drawHeading(text: String) = drawTextBlock(text, titlePaint(if (isRtl) 20f else 18f), 8f)

        fun drawSection(text: String) = drawTextBlock(text, sectionPaint(if (isRtl) 15f else 14f), 6f)

        fun drawBody(text: String, paint: TextPaint = bodyPaint()) =
            drawTextBlock(text, paint, if (isRtl) 8f else 5f)

        fun drawField(label: String, value: String) {
            if (value.isBlank()) return
            val text = if (isRtl) UrduPdfText.fieldLine(label, value) else "$label: $value"
            drawBody(text)
        }

        private fun drawTextBlock(text: String, paint: TextPaint, spacingAfter: Float) {
            if (text.isBlank()) return
            val prepared = prepareText(text)
            val layout = buildLayout(prepared, paint)
            var startLine = 0
            while (startLine < layout.lineCount) {
                var endLine = startLine + 1
                while (endLine <= layout.lineCount) {
                    val h = layout.getLineBottom(endLine - 1) - layout.getLineTop(startLine)
                    if (h > availableHeight()) {
                        if (endLine - 1 > startLine) endLine--
                        break
                    }
                    if (endLine == layout.lineCount) break
                    endLine++
                }
                val blockH = layout.getLineBottom(endLine - 1) - layout.getLineTop(startLine) + spacingAfter
                ensureSpace(blockH)
                val top = layout.getLineTop(startLine)
                val bottom = layout.getLineBottom(endLine - 1)
                canvas.save()
                canvas.translate(contentLeft, y)
                val clipPad = if (isRtl) RTL_EDGE_PAD else 0f
                canvas.clipRect(
                    -clipPad,
                    top.toFloat(),
                    layoutWidth.toFloat() + clipPad,
                    bottom.toFloat()
                )
                canvas.translate(0f, -top.toFloat())
                layout.draw(canvas)
                canvas.restore()
                y += blockH
                startLine = endLine
                if (startLine < layout.lineCount) newPage()
            }
        }

        fun sectionPaint(size: Float) = TextPaint(Paint.ANTI_ALIAS_FLAG).apply {
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
            textSize = if (isRtl) 13f else 11f
            typeface = regularTypeface
        }

        @Suppress("WrongConstant")
        private fun buildLayout(text: String, paint: TextPaint): StaticLayout {
            val direction = if (isRtl) TextDirectionHeuristics.RTL else TextDirectionHeuristics.LTR
            val builder = StaticLayout.Builder.obtain(text, 0, text.length, paint, layoutWidth)
                .setAlignment(Layout.Alignment.ALIGN_NORMAL)
                .setTextDirection(direction)
                .setLineSpacing(2f, if (isRtl) 1.4f else 1.2f)
                .setIncludePad(isRtl)
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

        private fun readPageCount(): Int {
            if (Build.VERSION.SDK_INT < Build.VERSION_CODES.LOLLIPOP) return 1
            val pfd = ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY)
            val renderer = PdfRenderer(pfd)
            val count = renderer.pageCount
            renderer.close()
            pfd.close()
            return count
        }
    }
}
