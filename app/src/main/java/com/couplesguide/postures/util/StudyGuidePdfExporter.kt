package com.couplesguide.postures.util

import android.content.Context
import android.graphics.Canvas
import android.graphics.Paint
import android.graphics.Typeface
import android.graphics.pdf.PdfDocument
import android.text.Layout
import android.text.StaticLayout
import android.text.TextDirectionHeuristics
import android.text.TextPaint
import com.couplesguide.postures.data.LectureNotesRepository
import com.couplesguide.postures.data.StudyChapter
import java.io.File
import java.io.FileOutputStream

object StudyGuidePdfExporter {

    private const val PAGE_WIDTH = 595
    private const val PAGE_HEIGHT = 842
    private const val MARGIN = 48f

    fun exportSummary(context: Context, language: String): PdfExporter.ExportResult {
        val displayName = if (language == LocaleHelper.LANG_UR) {
            "self_taught_bootcamp_summary_urdu.pdf"
        } else {
            "self_taught_bootcamp_summary_english.pdf"
        }
        val file = File(context.cacheDir, displayName)
        if (file.exists()) file.delete()

        LectureNotesRepository.ensureLoaded(context)
        val chapters = LectureNotesRepository.getClasses(context).flatMap { it.chapters }

        val document = PdfDocument()
        try {
            var pageNumber = 1
            pageNumber = writeTitle(context, document, language, pageNumber)
            for (chapter in chapters) {
                pageNumber = writeChapter(context, document, chapter, language, pageNumber)
            }
            FileOutputStream(file).use { document.writeTo(it) }
        } finally {
            document.close()
        }
        return PdfExporter.ExportResult(file, displayName)
    }

    private fun writeTitle(
        context: Context,
        document: PdfDocument,
        language: String,
        pageNumber: Int
    ): Int {
        val isUr = language == LocaleHelper.LANG_UR
        val title = if (isUr) {
            "Self-Taught Bootcamp — سینمائی CS مطالعہ"
        } else {
            "Cinematic Self-Taught Bootcamp — Computer Science"
        }
        val subtitle = if (isUr) {
            "جماعت XI و XII • سندھ نصاب • ★ Golden Topics"
        } else {
            "Class XI & XII • Sindh Curriculum • ★ Golden Topics"
        }
        return writeTextPage(document, pageNumber, title, subtitle, "")
    }

    private fun writeChapter(
        context: Context,
        document: PdfDocument,
        chapter: StudyChapter,
        language: String,
        pageNumber: Int
    ): Int {
        val content = chapter.content(language)
        val points = content.keyPoints.joinToString("\n• ", prefix = "• ")
        val body = buildString {
            append(content.summary)
            append("\n\n")
            append(content.body)
            append("\n\n")
            append(points)
        }
        val heading = "CS ${chapter.grade} — ${content.title}"
        return writeTextPage(document, pageNumber, heading, body, "")
    }

    private fun writeTextPage(
        document: PdfDocument,
        pageNumber: Int,
        title: String,
        body: String,
        @Suppress("UNUSED_PARAMETER") footer: String
    ): Int {
        val pageInfo = PdfDocument.PageInfo.Builder(PAGE_WIDTH, PAGE_HEIGHT, pageNumber).create()
        val page = document.startPage(pageInfo)
        val canvas = page.canvas
        val titlePaint = TextPaint(Paint.ANTI_ALIAS_FLAG).apply {
            textSize = 20f
            typeface = Typeface.create(Typeface.DEFAULT, Typeface.BOLD)
        }
        val bodyPaint = TextPaint(Paint.ANTI_ALIAS_FLAG).apply {
            textSize = 12f
        }
        var y = MARGIN
        val contentWidth = (PAGE_WIDTH - MARGIN * 2).toInt()
        y += drawMultiline(canvas, title, titlePaint, MARGIN, y, contentWidth) + 16f
        drawMultiline(canvas, body, bodyPaint, MARGIN, y, contentWidth)
        document.finishPage(page)
        return pageNumber + 1
    }

    private fun drawMultiline(
        canvas: Canvas,
        text: String,
        paint: TextPaint,
        x: Float,
        y: Float,
        width: Int
    ): Float {
        val layout = StaticLayout.Builder
            .obtain(text, 0, text.length, paint, width)
            .setAlignment(Layout.Alignment.ALIGN_NORMAL)
            .setTextDirection(TextDirectionHeuristics.LTR)
            .setLineSpacing(0f, 1.2f)
            .build()
        canvas.save()
        canvas.translate(x, y)
        layout.draw(canvas)
        canvas.restore()
        return layout.height.toFloat()
    }
}
