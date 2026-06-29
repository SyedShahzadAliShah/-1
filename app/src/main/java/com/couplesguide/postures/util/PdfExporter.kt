package com.couplesguide.postures.util

import android.content.ClipData
import android.content.Context
import android.content.Intent
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.graphics.Canvas
import android.graphics.Paint
import android.graphics.Rect
import android.graphics.Typeface
import android.graphics.pdf.PdfDocument
import android.text.Layout
import android.text.StaticLayout
import android.text.TextPaint
import androidx.core.content.ContextCompat
import androidx.core.content.FileProvider
import com.couplesguide.postures.R
import com.couplesguide.postures.data.GuideRepository
import com.couplesguide.postures.data.Posture
import com.couplesguide.postures.data.PostureRepository
import java.io.File
import java.io.FileOutputStream

object PdfExporter {

    private const val PAGE_WIDTH = 595
    private const val PAGE_HEIGHT = 842
    private const val MARGIN = 48f
    private const val BOTTOM_MARGIN = 56f
    private const val IMAGE_HEIGHT = 150f

    fun exportFullGuide(context: Context, language: String): File {
        val fileName = if (language == LocaleHelper.LANG_UR) {
            "intimacy_guide_urdu.pdf"
        } else {
            "intimacy_guide_english.pdf"
        }
        val file = File(context.cacheDir, fileName)
        if (file.exists()) file.delete()

        val document = PdfDocument()
        try {
            var pageNumber = 1
            pageNumber = writeTitlePage(context, document, language, pageNumber)
            pageNumber = writeChapters(context, document, language, pageNumber)
            pageNumber = writeImaginationSection(context, document, language, pageNumber)
            for (posture in PostureRepository.getPhysicalPostures()) {
                pageNumber = writePosturePages(context, document, posture, language, pageNumber)
            }
            FileOutputStream(file).use { document.writeTo(it) }
        } finally {
            document.close()
        }
        return file
    }

    fun exportPosture(context: Context, posture: Posture, language: String): File {
        val content = posture.content(language)
        val safeName = content.name
            .replace(Regex("[^A-Za-z0-9._-]"), "_")
            .trim('_')
            .ifBlank { "posture" }
        val file = File(context.cacheDir, "${safeName}_${language}.pdf")
        if (file.exists()) file.delete()

        val document = PdfDocument()
        try {
            writePosturePages(context, document, posture, language, 1)
            FileOutputStream(file).use { document.writeTo(it) }
        } finally {
            document.close()
        }
        return file
    }

    fun sharePdf(context: Context, file: File) {
        if (!file.exists() || file.length() == 0L) {
            throw IllegalStateException("PDF file is missing or empty")
        }
        val uri = FileProvider.getUriForFile(
            context,
            "${context.packageName}.fileprovider",
            file
        )
        val intent = Intent(Intent.ACTION_SEND).apply {
            type = "application/pdf"
            putExtra(Intent.EXTRA_STREAM, uri)
            clipData = ClipData.newRawUri("pdf", uri)
            addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
        }
        context.startActivity(Intent.createChooser(intent, context.getString(R.string.share_pdf)))
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
        pageNumber = writeSectionDivider(context, document, language, pageNumber,
            context.getString(R.string.imagination_postures))
        for (posture in PostureRepository.getImaginationPostures()) {
            pageNumber = writePosturePages(context, document, posture, language, pageNumber)
        }
        pageNumber = writeSectionDivider(context, document, language, pageNumber,
            context.getString(R.string.all_postures))
        return pageNumber
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
                document.finishPage(page)
            }
            val pageInfo = PdfDocument.PageInfo.Builder(PAGE_WIDTH, PAGE_HEIGHT, pageNumber).create()
            page = document.startPage(pageInfo)
            canvas = page.canvas
            pageNumber++
            y = MARGIN + 8f
        }

        private fun ensureSpace(needed: Float) {
            if (y + needed > PAGE_HEIGHT - BOTTOM_MARGIN) {
                newPage()
            }
        }

        fun space(amount: Float) {
            y += amount
        }

        fun drawTitle(text: String, size: Float = 28f) {
            val paint = titlePaint(size)
            ensureSpace(size + 8f)
            val x = if (isRtl) PAGE_WIDTH - MARGIN else MARGIN
            canvas.drawText(text, x, y + size, paint)
            y += size + 12f
        }

        fun drawHeading(text: String) {
            val paint = titlePaint(20f)
            ensureSpace(28f)
            val x = if (isRtl) PAGE_WIDTH - MARGIN else MARGIN
            canvas.drawText(text, x, y + 20f, paint)
            y += 28f
        }

        fun drawSection(text: String) {
            val paint = sectionPaint()
            ensureSpace(22f)
            val x = if (isRtl) PAGE_WIDTH - MARGIN else MARGIN
            canvas.drawText(text, x, y + 14f, paint)
            y += 22f
        }

        fun drawBody(text: String, paint: TextPaint = bodyPaint()) {
            val layout = buildLayout(text, paint)
            ensureSpace(layout.height.toFloat() + 4f)
            canvas.save()
            canvas.translate(if (isRtl) PAGE_WIDTH - MARGIN - textWidth else MARGIN, y)
            layout.draw(canvas)
            canvas.restore()
            y += layout.height + 6f
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

        private fun sectionPaint() = sectionPaint(14f)

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
            document.finishPage(page)
            return pageNumber
        }
    }
}
