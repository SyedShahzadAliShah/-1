package com.couplesguide.postures.ui

import android.animation.ValueAnimator
import android.content.Context
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.CornerPathEffect
import android.graphics.Paint
import android.graphics.Path
import android.graphics.RectF
import android.util.AttributeSet
import android.view.View
import android.view.animation.DecelerateInterpolator
import android.view.animation.LinearInterpolator
import androidx.core.content.ContextCompat
import com.couplesguide.postures.R
import com.couplesguide.postures.data.SketchnoteFrame
import kotlin.math.sin

class SketchnoteLectureView @JvmOverloads constructor(
    context: Context,
    attrs: AttributeSet? = null
) : View(context, attrs) {

    private val doodlePaint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
        style = Paint.Style.STROKE
        strokeWidth = 5f
        pathEffect = CornerPathEffect(18f)
        color = ContextCompat.getColor(context, R.color.primary)
    }
    private val fillPaint = Paint(Paint.ANTI_ALIAS_FLAG)
    private val textPaint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
        color = ContextCompat.getColor(context, R.color.on_surface)
        textSize = 34f
    }
    private val subTextPaint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
        color = ContextCompat.getColor(context, R.color.on_surface_variant)
        textSize = 26f
    }
    private val glowPaint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
        style = Paint.Style.STROKE
        strokeWidth = 10f
        color = ContextCompat.getColor(context, R.color.secondary)
    }

    private var frames: List<SketchnoteFrame> = emptyList()
    private var activeIndex = 0
    private var pulse = 0f
    private var wavePhase = 0f
    private var backgroundBitmap: Bitmap? = null
    private var golden = false
    private var frameEntrance = 1f
    private var entranceAnimator: ValueAnimator? = null
    private var syncPulse = 0f
    private var syncAnimator: ValueAnimator? = null

    private val pulseAnimator = ValueAnimator.ofFloat(0f, 1f).apply {
        duration = 1400L
        repeatCount = ValueAnimator.INFINITE
        repeatMode = ValueAnimator.REVERSE
        interpolator = LinearInterpolator()
        addUpdateListener {
            pulse = it.animatedValue as Float
            invalidate()
        }
    }

    private val waveAnimator = ValueAnimator.ofFloat(0f, 6.28f).apply {
        duration = 2200L
        repeatCount = ValueAnimator.INFINITE
        interpolator = LinearInterpolator()
        addUpdateListener {
            wavePhase = it.animatedValue as Float
            invalidate()
        }
    }

    fun setLecture(frames: List<SketchnoteFrame>, goldenTopic: Boolean, pageImageAsset: String?) {
        this.frames = frames
        this.golden = goldenTopic
        activeIndex = 0
        backgroundBitmap = pageImageAsset?.let { loadAssetBitmap(it) }
        if (!pulseAnimator.isRunning) pulseAnimator.start()
        if (!waveAnimator.isRunning) waveAnimator.start()
        invalidate()
    }

    fun setActiveFrame(index: Int) {
        if (frames.isEmpty()) return
        val target = index.coerceIn(0, frames.lastIndex)
        if (target == activeIndex && frameEntrance >= 0.95f) {
            triggerSyncPulse()
            return
        }
        activeIndex = target
        frameEntrance = 0f
        entranceAnimator?.cancel()
        entranceAnimator = ValueAnimator.ofFloat(0f, 1f).apply {
            duration = 520L
            interpolator = DecelerateInterpolator()
            addUpdateListener {
                frameEntrance = it.animatedValue as Float
                invalidate()
            }
            start()
        }
        triggerSyncPulse()
    }

    private fun triggerSyncPulse() {
        syncAnimator?.cancel()
        syncAnimator = ValueAnimator.ofFloat(0f, 1f).apply {
            duration = 650L
            interpolator = DecelerateInterpolator()
            addUpdateListener {
                syncPulse = it.animatedValue as Float
                invalidate()
            }
            start()
        }
    }

    fun stopAnimations() {
        pulseAnimator.cancel()
        waveAnimator.cancel()
        entranceAnimator?.cancel()
        syncAnimator?.cancel()
    }

    private fun loadAssetBitmap(assetPath: String): Bitmap? {
        return try {
            context.assets.open(assetPath).use { stream ->
                BitmapFactory.decodeStream(stream)
            }
        } catch (_: Exception) {
            null
        }
    }

    override fun onDraw(canvas: Canvas) {
        super.onDraw(canvas)
        val w = width.toFloat()
        val h = height.toFloat()
        drawPaper(canvas, w, h)

        val bmp = backgroundBitmap
        if (bmp != null) {
            fillPaint.alpha = 70
            val dst = RectF(12f, 12f, w - 12f, h * 0.42f)
            canvas.drawBitmap(bmp, null, dst, fillPaint)
            fillPaint.alpha = 255
            canvas.drawRect(dst, doodlePaint.apply { alpha = 120 })
            doodlePaint.alpha = 255
        }

        if (frames.isEmpty()) {
            canvas.drawText("Sketchnote lecture", 24f, h * 0.55f, textPaint)
            return
        }

        val frame = frames[activeIndex]
        drawSyncHighlight(canvas, w, h)
        drawVisualMotif(canvas, frame.visual, w, h, frameEntrance)
        drawCaptionCard(canvas, frame.english, w, h, frameEntrance)
        drawStepBadge(canvas, w, activeIndex + 1, frames.size)

        if (golden) {
            glowPaint.alpha = (80 + pulse * 120).toInt()
            canvas.drawRoundRect(RectF(8f, 8f, w - 8f, h - 8f), 24f, 24f, glowPaint)
        }

        drawFrameStrip(canvas, w, h)
    }

    private fun drawPaper(canvas: Canvas, w: Float, h: Float) {
        fillPaint.color = Color.parseColor("#FFF8E7")
        canvas.drawRoundRect(RectF(0f, 0f, w, h), 20f, 20f, fillPaint)
        doodlePaint.color = Color.parseColor("#E8DCC8")
        doodlePaint.strokeWidth = 2f
        var y = 40f
        while (y < h) {
            canvas.drawLine(16f, y, w - 16f, y, doodlePaint)
            y += 36f
        }
        doodlePaint.strokeWidth = 5f
        doodlePaint.color = ContextCompat.getColor(context, R.color.primary)
    }

    private fun drawSyncHighlight(canvas: Canvas, w: Float, h: Float) {
        if (syncPulse <= 0f) return
        val alpha = ((1f - syncPulse) * 140f).toInt().coerceIn(0, 140)
        fillPaint.color = ContextCompat.getColor(context, R.color.secondary)
        fillPaint.alpha = alpha
        val inset = 6f + syncPulse * 18f
        canvas.drawRoundRect(RectF(inset, inset, w - inset, h - inset), 22f, 22f, fillPaint)
        fillPaint.alpha = 255
    }

    private fun drawStepBadge(canvas: Canvas, w: Float, step: Int, total: Int) {
        val label = "$step / $total"
        subTextPaint.textSize = 28f
        subTextPaint.color = Color.WHITE
        val padding = 16f
        val textWidth = subTextPaint.measureText(label)
        val rect = RectF(w - textWidth - padding * 2 - 12f, 12f, w - 12f, 52f)
        fillPaint.color = ContextCompat.getColor(context, R.color.primary)
        canvas.drawRoundRect(rect, 14f, 14f, fillPaint)
        canvas.drawText(label, rect.left + padding, rect.bottom - 12f, subTextPaint)
        subTextPaint.color = ContextCompat.getColor(context, R.color.on_surface_variant)
    }

    private fun drawCaptionCard(canvas: Canvas, caption: String, w: Float, h: Float, entrance: Float) {
        val card = RectF(20f, h * 0.58f + (1f - entrance) * 28f, w - 20f, h - 20f)
        fillPaint.color = Color.WHITE
        fillPaint.alpha = (180 + entrance * 75f).toInt().coerceIn(0, 255)
        canvas.drawRoundRect(card, 18f, 18f, fillPaint)
        fillPaint.alpha = 255
        canvas.drawRoundRect(card, 18f, 18f, doodlePaint)

        val lines = wrapText(caption, textPaint, card.width() - 32f)
        var y = card.top + 40f
        for (line in lines.take(4)) {
            canvas.drawText(line, card.left + 16f, y, textPaint)
            y += 42f
        }
        subTextPaint.textSize = 22f
        canvas.drawText(
            context.getString(R.string.sketchnote_urdu_sync_hint),
            card.left + 16f,
            card.bottom - 16f,
            subTextPaint
        )
    }

    private fun drawFrameStrip(canvas: Canvas, w: Float, h: Float) {
        if (frames.size <= 1) return
        val y = h - 8f
        val gap = (w - 40f) / frames.size
        frames.forEachIndexed { index, _ ->
            val cx = 20f + gap * index + gap / 2f
            fillPaint.color = if (index == activeIndex) {
                ContextCompat.getColor(context, R.color.secondary)
            } else {
                Color.parseColor("#B0BEC5")
            }
            val r = if (index == activeIndex) 10f + pulse * 4f else 7f
            canvas.drawCircle(cx, y, r, fillPaint)
        }
    }

    private fun drawVisualMotif(canvas: Canvas, visual: String, w: Float, h: Float, entrance: Float) {
        val cx = w * 0.5f
        val cy = h * 0.28f - (1f - entrance) * 36f
        val scale = (0.75f + entrance * 0.25f) * (1f + pulse * 0.08f)
        doodlePaint.alpha = (120 + entrance * 135f).toInt().coerceIn(0, 255)
        when (visual) {
            "logic" -> drawLogicGate(canvas, cx, cy, scale)
            "network" -> drawNetwork(canvas, cx, cy, scale)
            "wave" -> drawWave(canvas, cx, cy, w)
            "flow" -> drawFlow(canvas, cx, cy, scale)
            "compare" -> drawCompare(canvas, cx, cy, scale)
            else -> drawIdea(canvas, cx, cy, scale)
        }
        doodlePaint.alpha = 255
    }

    private fun drawLogicGate(canvas: Canvas, cx: Float, cy: Float, scale: Float) {
        val path = Path()
        val r = 50f * scale
        path.moveTo(cx - r, cy - r)
        path.lineTo(cx + r * 0.4f, cy - r)
        path.quadTo(cx + r, cy, cx + r * 0.4f, cy + r)
        path.lineTo(cx - r, cy + r)
        path.close()
        canvas.drawPath(path, doodlePaint)
        canvas.drawCircle(cx - r - 12f, cy, 8f, fillPaint.apply { color = doodlePaint.color })
        canvas.drawCircle(cx + r + 12f, cy, 8f, fillPaint)
    }

    private fun drawNetwork(canvas: Canvas, cx: Float, cy: Float, scale: Float) {
        val nodes = listOf(
            cx - 70f * scale to cy - 30f,
            cx + 60f * scale to cy - 40f,
            cx to cy + 50f * scale,
            cx - 40f * scale to cy + 20f,
            cx + 50f * scale to cy + 30f
        )
        for (i in nodes.indices) {
            for (j in i + 1 until nodes.size) {
                canvas.drawLine(nodes[i].first, nodes[i].second, nodes[j].first, nodes[j].second, doodlePaint)
            }
        }
        nodes.forEach { (x, y) -> canvas.drawCircle(x, y, 14f * scale, fillPaint.apply { color = doodlePaint.color }) }
    }

    private fun drawWave(canvas: Canvas, cx: Float, cy: Float, w: Float) {
        val path = Path()
        val startX = cx - w * 0.35f
        path.moveTo(startX, cy)
        var x = startX
        while (x < cx + w * 0.35f) {
            val y = cy + sin((x / 28f) + wavePhase) * 28f
            path.lineTo(x, y)
            x += 8f
        }
        canvas.drawPath(path, doodlePaint)
    }

    private fun drawFlow(canvas: Canvas, cx: Float, cy: Float, scale: Float) {
        val arrow = Path()
        arrow.moveTo(cx - 80f * scale, cy)
        arrow.lineTo(cx + 60f * scale, cy)
        arrow.lineTo(cx + 40f * scale, cy - 20f * scale)
        arrow.moveTo(cx + 60f * scale, cy)
        arrow.lineTo(cx + 40f * scale, cy + 20f * scale)
        canvas.drawPath(arrow, doodlePaint)
        canvas.drawCircle(cx - 90f * scale, cy, 16f * scale, fillPaint.apply { color = doodlePaint.color })
    }

    private fun drawCompare(canvas: Canvas, cx: Float, cy: Float, scale: Float) {
        canvas.drawRoundRect(RectF(cx - 90f * scale, cy - 40f, cx - 10f, cy + 40f), 12f, 12f, doodlePaint)
        canvas.drawRoundRect(RectF(cx + 10f, cy - 40f, cx + 90f * scale, cy + 40f), 12f, 12f, doodlePaint)
        canvas.drawText("A", cx - 55f * scale, cy + 12f, subTextPaint)
        canvas.drawText("B", cx + 45f * scale, cy + 12f, subTextPaint)
    }

    private fun drawIdea(canvas: Canvas, cx: Float, cy: Float, scale: Float) {
        canvas.drawCircle(cx, cy, 36f * scale, doodlePaint)
        val legY = cy + 50f * scale
        canvas.drawLine(cx - 20f, legY, cx + 20f, legY, doodlePaint)
        canvas.drawLine(cx - 12f, legY + 16f, cx + 12f, legY + 16f, doodlePaint)
    }

    private fun wrapText(text: String, paint: Paint, maxWidth: Float): List<String> {
        val words = text.split(" ")
        val lines = mutableListOf<String>()
        var current = ""
        for (word in words) {
            val candidate = if (current.isEmpty()) word else "$current $word"
            if (paint.measureText(candidate) <= maxWidth) {
                current = candidate
            } else {
                if (current.isNotEmpty()) lines.add(current)
                current = word
            }
        }
        if (current.isNotEmpty()) lines.add(current)
        return lines
    }

    override fun onDetachedFromWindow() {
        stopAnimations()
        super.onDetachedFromWindow()
    }
}
