package com.couplesguide.postures.util

import android.content.Context
import android.graphics.Bitmap
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

    fun exportFullGuide(context: Context, language: String): File {
        val fileName = if (language == LocaleHelper.LANG_UR) {
            "intimacy_guide_urdu.pdf"
        } else {
            "intimacy_guide_english.pdf"
        }
        val file = File(context.cacheDir, fileName)
        val document = PdfDocument()
        var pageNumber = 1

        pageNumber = writeTitlePage(context, document, language, pageNumber)
        pageNumber = writeChapters(context, document, language, pageNumber)

        for (posture in PostureRepository.getAllPostures()) {
            pageNumber = writePosturePage(context, document, posture, language, pageNumber)
        }

        FileOutputStream(file).use { document.writeTo(it) }
        document.close()
        return file
    }

    fun exportPosture(context: Context, posture: Posture, language: String): File {
        val content = posture.content(language)
        val safeName = content.name.replace(" ", "_").replace("(", "").replace(")", "")
        val file = File(context.cacheDir, "${safeName}_${language}.pdf")
        val document = PdfDocument()
        writePosturePage(context, document, posture, language, 1)
        FileOutputStream(file).use { document.writeTo(it) }
        document.close()
        return file
    }

    fun sharePdf(context: Context, file: File) {
        val uri = FileProvider.getUriForFile(
            context,
            "${context.packageName}.fileprovider",
            file
        )
        val intent = android.content.Intent(android.content.Intent.ACTION_SEND).apply {
            type = "application/pdf"
            putExtra(android.content.Intent.EXTRA_STREAM, uri)
            addFlags(android.content.Intent.FLAG_GRANT_READ_URI_PERMISSION)
        }
        val title = context.getString(R.string.share_pdf)
        context.startActivity(android.content.Intent.createChooser(intent, title))
    }

    private fun writeTitlePage(
        context: Context,
        document: PdfDocument,
        language: String,
        pageNumber: Int
    ): Int {
        val pageInfo = PdfDocument.PageInfo.Builder(PAGE_WIDTH, PAGE_HEIGHT, pageNumber).create()
        val page = document.startPage(pageInfo)
        val canvas = page.canvas
        val isRtl = language == LocaleHelper.LANG_UR

        val titlePaint = TextPaint().apply {
            color = ContextCompat.getColor(context, R.color.primary)
            textSize = 28f
            typeface = Typeface.create(Typeface.DEFAULT, Typeface.BOLD)
            textAlign = if (isRtl) Paint.Align.RIGHT else Paint.Align.LEFT
        }
        val bodyPaint = TextPaint().apply {
            color = ContextCompat.getColor(context, R.color.on_surface)
            textSize = 14f
            textAlign = if (isRtl) Paint.Align.RIGHT else Paint.Align.LEFT
        }

        val title = if (isRtl) "مکمل رہنمائی قریبی تعلق" else "Ultimate Intimacy Guide"
        val subtitle = if (isRtl) {
            "جوڑوں کے لیے تصویری رہنمائی • انگریزی و اردو"
        } else {
            "Illustrated Guide for Couples • English & Urdu"
        }
        val intro = if (isRtl) {
            "یہ گائیڈ آپ کو قریبی پوزیشنز سیکھنے، باہمی رضامندی، آرام دہ مواصلات، " +
                "اور ایک دوسرے کے ساتھ محفوظ تجربہ کرنے میں مدد دیتی ہے۔"
        } else {
            "This guide helps you learn intimate postures, practice mutual consent, " +
                "communicate comfortably, and explore safely together as a couple."
        }

        var y = 120f
        val textWidth = PAGE_WIDTH - (MARGIN * 2)

        canvas.drawText(title, if (isRtl) PAGE_WIDTH - MARGIN else MARGIN, y, titlePaint)
        y += 40f
        canvas.drawText(subtitle, if (isRtl) PAGE_WIDTH - MARGIN else MARGIN, y, bodyPaint)
        y += 60f

        y = drawWrappedText(canvas, intro, MARGIN, y, textWidth.toInt(), bodyPaint, isRtl)

        val drawable = ContextCompat.getDrawable(context, R.drawable.pic_guide_cover)
        drawable?.let {
            val bitmap = drawableToBitmap(it, 300, 180)
            val left = (PAGE_WIDTH - 300) / 2f
            canvas.drawBitmap(bitmap, left, y + 40f, null)
        }

        document.finishPage(page)
        return pageNumber + 1
    }

    private fun writeChapters(
        context: Context,
        document: PdfDocument,
        language: String,
        startPage: Int
    ): Int {
        var pageNumber = startPage
        val isRtl = language == LocaleHelper.LANG_UR

        for (chapter in GuideRepository.getChapters()) {
            val content = chapter.content(language)
            val pageInfo = PdfDocument.PageInfo.Builder(PAGE_WIDTH, PAGE_HEIGHT, pageNumber).create()
            val page = document.startPage(pageInfo)
            val canvas = page.canvas

            val titlePaint = TextPaint().apply {
                color = ContextCompat.getColor(context, R.color.primary)
                textSize = 20f
                typeface = Typeface.create(Typeface.DEFAULT, Typeface.BOLD)
                textAlign = if (isRtl) Paint.Align.RIGHT else Paint.Align.LEFT
            }
            val bodyPaint = TextPaint().apply {
                color = ContextCompat.getColor(context, R.color.on_surface)
                textSize = 13f
                textAlign = if (isRtl) Paint.Align.RIGHT else Paint.Align.LEFT
            }

            var y = 60f
            val textWidth = PAGE_WIDTH - (MARGIN * 2)

            val drawable = ContextCompat.getDrawable(context, chapter.illustrationRes)
            drawable?.let {
                val bitmap = drawableToBitmap(it, 200, 120)
                val left = (PAGE_WIDTH - 200) / 2f
                canvas.drawBitmap(bitmap, left, y, null)
                y += 140f
            }

            canvas.drawText(content.title, if (isRtl) PAGE_WIDTH - MARGIN else MARGIN, y, titlePaint)
            y += 28f
            y = drawWrappedText(canvas, content.summary, MARGIN, y, textWidth.toInt(), bodyPaint, isRtl)
            y += 16f
            y = drawWrappedText(canvas, content.body, MARGIN, y, textWidth.toInt(), bodyPaint, isRtl)
            y += 16f

            val pointsHeader = if (isRtl) "اہم نکات:" else "Key Points:"
            canvas.drawText(pointsHeader, if (isRtl) PAGE_WIDTH - MARGIN else MARGIN, y, titlePaint)
            y += 24f

            for (point in content.keyPoints) {
                val bullet = if (isRtl) "• $point" else "• $point"
                y = drawWrappedText(canvas, bullet, MARGIN, y, textWidth.toInt(), bodyPaint, isRtl)
                y += 8f
            }

            document.finishPage(page)
            pageNumber++
        }
        return pageNumber
    }

    private fun writePosturePage(
        context: Context,
        document: PdfDocument,
        posture: Posture,
        language: String,
        pageNumber: Int
    ): Int {
        val content = posture.content(language)
        val isRtl = language == LocaleHelper.LANG_UR
        val pageInfo = PdfDocument.PageInfo.Builder(PAGE_WIDTH, PAGE_HEIGHT, pageNumber).create()
        val page = document.startPage(pageInfo)
        val canvas = page.canvas

        val titlePaint = TextPaint().apply {
            color = ContextCompat.getColor(context, R.color.primary)
            textSize = 22f
            typeface = Typeface.create(Typeface.DEFAULT, Typeface.BOLD)
            textAlign = if (isRtl) Paint.Align.RIGHT else Paint.Align.LEFT
        }
        val sectionPaint = TextPaint().apply {
            color = ContextCompat.getColor(context, R.color.secondary)
            textSize = 14f
            typeface = Typeface.create(Typeface.DEFAULT, Typeface.BOLD)
            textAlign = if (isRtl) Paint.Align.RIGHT else Paint.Align.LEFT
        }
        val bodyPaint = TextPaint().apply {
            color = ContextCompat.getColor(context, R.color.on_surface)
            textSize = 12f
            textAlign = if (isRtl) Paint.Align.RIGHT else Paint.Align.LEFT
        }

        var y = 50f
        val textWidth = PAGE_WIDTH - (MARGIN * 2)

        val drawable = ContextCompat.getDrawable(context, posture.illustrationRes)
        drawable?.let {
            val bitmap = drawableToBitmap(it, 220, 130)
            val left = (PAGE_WIDTH - 220) / 2f
            canvas.drawBitmap(bitmap, left, y, null)
            y += 145f
        }

        canvas.drawText(content.name, if (isRtl) PAGE_WIDTH - MARGIN else MARGIN, y, titlePaint)
        y += 22f

        val meta = "${content.category}  |  ${posture.difficulty.label(language)}"
        canvas.drawText(meta, if (isRtl) PAGE_WIDTH - MARGIN else MARGIN, y, bodyPaint)
        y += 24f

        y = drawWrappedText(canvas, content.summary, MARGIN, y, textWidth.toInt(), bodyPaint, isRtl)
        y += 14f

        val aboutLabel = if (isRtl) "تفصیل" else "About"
        canvas.drawText(aboutLabel, if (isRtl) PAGE_WIDTH - MARGIN else MARGIN, y, sectionPaint)
        y += 20f
        y = drawWrappedText(canvas, content.description, MARGIN, y, textWidth.toInt(), bodyPaint, isRtl)
        y += 14f

        val stepsLabel = if (isRtl) "طریقہ کار" else "How To"
        canvas.drawText(stepsLabel, if (isRtl) PAGE_WIDTH - MARGIN else MARGIN, y, sectionPaint)
        y += 20f
        content.steps.forEachIndexed { index, step ->
            val line = "${index + 1}. $step"
            y = drawWrappedText(canvas, line, MARGIN, y, textWidth.toInt(), bodyPaint, isRtl)
            y += 6f
        }
        y += 8f

        val tipsLabel = if (isRtl) "آرام کے مشورے" else "Comfort Tips"
        canvas.drawText(tipsLabel, if (isRtl) PAGE_WIDTH - MARGIN else MARGIN, y, sectionPaint)
        y += 20f
        for (tip in content.tips) {
            y = drawWrappedText(canvas, "• $tip", MARGIN, y, textWidth.toInt(), bodyPaint, isRtl)
            y += 6f
        }

        document.finishPage(page)
        return pageNumber + 1
    }

    private fun drawWrappedText(
        canvas: Canvas,
        text: String,
        x: Float,
        y: Float,
        width: Int,
        paint: TextPaint,
        isRtl: Boolean
    ): Float {
        val alignment = if (isRtl) Layout.Alignment.ALIGN_OPPOSITE else Layout.Alignment.ALIGN_NORMAL
        val layout = StaticLayout.Builder
            .obtain(text, 0, text.length, paint, width)
            .setAlignment(alignment)
            .setLineSpacing(0f, 1.2f)
            .build()

        canvas.save()
        canvas.translate(if (isRtl) PAGE_WIDTH - MARGIN - width else x, y)
        layout.draw(canvas)
        canvas.restore()
        return y + layout.height
    }

    private fun drawableToBitmap(drawable: android.graphics.drawable.Drawable, width: Int, height: Int): Bitmap {
        val bitmap = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888)
        val canvas = Canvas(bitmap)
        drawable.bounds = Rect(0, 0, width, height)
        drawable.draw(canvas)
        return bitmap
    }
}
