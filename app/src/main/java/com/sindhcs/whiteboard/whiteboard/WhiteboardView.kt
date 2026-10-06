package com.sindhcs.whiteboard.whiteboard

import android.animation.Animator
import android.animation.AnimatorListenerAdapter
import android.animation.ValueAnimator
import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.graphics.Path
import android.graphics.PathMeasure
import android.graphics.RectF
import android.graphics.Typeface
import android.util.AttributeSet
import android.view.View
import android.view.animation.LinearInterpolator
import com.sindhcs.whiteboard.data.Mark
import kotlin.math.min

class WhiteboardView @JvmOverloads constructor(
    context: Context,
    attrs: AttributeSet? = null,
    defStyleAttr: Int = 0
) : View(context, attrs, defStyleAttr) {

    private val hand: Typeface = if (isInEditMode) {
        Typeface.DEFAULT
    } else {
        Typeface.createFromAsset(context.assets, "fonts/PatrickHand-Regular.ttf")
    }

    init {
        setWillNotDraw(false)
    }

    private val boardPaint = Paint(Paint.ANTI_ALIAS_FLAG).apply { color = Color.parseColor("#FFFCF7") }
    private val edgePaint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
        color = Color.parseColor("#E4D8C4")
        style = Paint.Style.STROKE
        strokeWidth = dp(2f)
    }
    private val dotPaint = Paint(Paint.ANTI_ALIAS_FLAG).apply { color = Color.parseColor("#F3EBDD") }
    private val ink = textPaint(Color.parseColor("#1C2430"))
    private val blue = textPaint(Color.parseColor("#1D4E89"))
    private val green = textPaint(Color.parseColor("#1B6B45"))
    private val red = textPaint(Color.parseColor("#9C3B32"))
    private val gold = textPaint(Color.parseColor("#8A5A12"))
    private val marker = Paint(Paint.ANTI_ALIAS_FLAG).apply {
        color = Color.parseColor("#1C2430")
        style = Paint.Style.STROKE
        strokeWidth = dp(3f)
        strokeCap = Paint.Cap.ROUND
        strokeJoin = Paint.Join.ROUND
    }
    private val fill = Paint(Paint.ANTI_ALIAS_FLAG).apply { color = Color.parseColor("#E7F2EA") }
    private val penPaint = Paint(Paint.ANTI_ALIAS_FLAG).apply { color = Color.parseColor("#C9842A") }
    private val codePaint = textPaint(Color.parseColor("#16324F")).apply {
        typeface = Typeface.MONOSPACE
    }

    private var marks: List<Mark> = emptyList()
    private var blocks: List<Block> = emptyList()
    private var playHead = 0f
    private var speed = 1f
    private var penX = 0f
    private var penY = 0f
    private var penVisible = false
    private var cancelCallback = false
    var onDrawComplete: (() -> Unit)? = null

    private val animator = ValueAnimator.ofFloat(0f, 1f).apply {
        interpolator = LinearInterpolator()
        addUpdateListener {
            playHead = it.animatedValue as Float
            invalidate()
        }
        addListener(object : AnimatorListenerAdapter() {
            override fun onAnimationEnd(animation: Animator) {
                if (!cancelCallback && playHead >= 0.99f) onDrawComplete?.invoke()
            }
        })
    }

    fun submit(marks: List<Mark>) {
        this.marks = marks
        playHead = 0f
        animator.cancel()
        blocks = emptyList()
        requestLayout()
        invalidate()
    }

    fun setSpeed(value: Float) {
        speed = value.coerceIn(0.7f, 1.3f)
    }

    fun play() {
        if (marks.isEmpty()) {
            playHead = 1f
            onDrawComplete?.invoke()
            return
        }
        cancelCallback = true
        animator.cancel()
        cancelCallback = false
        playHead = 0f
        animator.duration = durationMs()
        animator.start()
    }

    fun pause() {
        if (animator.isRunning) animator.pause()
    }

    fun resume() {
        when {
            animator.isPaused -> animator.resume()
            !animator.isRunning && playHead < 0.99f && marks.isNotEmpty() -> play()
        }
    }

    fun isComplete(): Boolean = playHead >= 0.99f && !animator.isRunning

    /** Draws every mark at once. Used to capture a finished board. */
    fun showFinished() {
        cancelCallback = true
        animator.cancel()
        cancelCallback = false
        playHead = 1f
        invalidate()
    }

    fun durationMs(): Long {
        val base = 900L + marks.size * 720L
        return (base / speed).toLong().coerceAtLeast(1200L)
    }

    override fun onDetachedFromWindow() {
        cancelCallback = true
        animator.cancel()
        super.onDetachedFromWindow()
    }

    override fun onDraw(canvas: Canvas) {
        val radius = dp(18f)
        val bounds = RectF(dp(1f), dp(1f), width - dp(1f), height - dp(1f))
        canvas.drawRoundRect(bounds, radius, radius, boardPaint)
        canvas.drawRoundRect(bounds, radius, radius, edgePaint)
        drawDots(canvas, bounds)
        if (marks.isEmpty() || width == 0) return
        if (blocks.isEmpty()) layoutBlocks()
        if (blocks.isEmpty()) return

        val available = height - dp(28f)
        val scale = min(1f, available / blocksHeight().coerceAtLeast(1f))
        val contentW = width - dp(36f)
        val dx = (width - contentW * scale) / 2f
        canvas.save()
        canvas.translate(dx, dp(16f))
        canvas.scale(scale, scale)
        penVisible = false
        blocks.forEachIndexed { index, block ->
            drawBlock(canvas, block, reveal(index), contentW)
        }
        canvas.restore()
        if (penVisible) {
            val vx = dx + penX * scale
            val vy = dp(16f) + penY * scale
            canvas.drawCircle(vx, vy, dp(7f), penPaint)
            canvas.drawCircle(vx, vy, dp(3f), ink)
        }
    }

    private fun drawDots(canvas: Canvas, bounds: RectF) {
        var y = bounds.top + dp(18f)
        while (y < bounds.bottom) {
            var x = bounds.left + dp(16f)
            while (x < bounds.right) {
                canvas.drawCircle(x, y, dp(1.1f), dotPaint)
                x += dp(22f)
            }
            y += dp(22f)
        }
    }

    private fun reveal(index: Int): Float {
        val count = blocks.size.coerceAtLeast(1)
        val slot = 1f / count
        val start = index * slot
        return ((playHead - start) / (slot * 0.9f)).coerceIn(0f, 1f)
    }

    private fun layoutBlocks() {
        val widthPx = (width - dp(36f)).coerceAtLeast(dp(120f))
        var y = 0f
        val built = ArrayList<Block>(marks.size)
        marks.forEach { mark ->
            val block = measure(mark, widthPx)
            block.top = y
            y += block.height + dp(12f)
            built.add(block)
        }
        blocks = built
    }

    private fun blocksHeight(): Float {
        val last = blocks.lastOrNull() ?: return 0f
        return last.top + last.height + dp(8f)
    }

    private fun measure(mark: Mark, widthPx: Float): Block {
        return when (mark.k) {
            "title" -> textBlock(mark, widthPx, sp(30f), 1.15f)
            "h2" -> textBlock(mark, widthPx, sp(22f), 1.15f)
            "bullet" -> textBlock(mark, widthPx - dp(28f), sp(20f), 1.2f)
            "note" -> {
                val body = wrap(mark.t, ink.applySize(sp(18f)), widthPx - dp(28f))
                Block(mark, dp(36f) + body.size * sp(18f) * 1.25f, lines = body)
            }
            "formula" -> Block(mark, sp(36f) + dp(8f), lines = listOf(mark.t))
            "code" -> Block(mark, dp(20f) + mark.items.size * sp(16f) * 1.35f, lines = mark.items)
            "gates" -> Block(mark, dp(128f))
            "table" -> {
                val rows = mark.rows.size + if (mark.headers.isEmpty()) 0 else 1
                Block(mark, rows * dp(34f) + dp(8f))
            }
            "flow" -> Block(mark, mark.items.size * dp(70f))
            "layers" -> Block(mark, mark.items.size * dp(42f) + dp(4f))
            "cols" -> {
                val left = mark.items.size
                val right = mark.items2.size
                Block(mark, dp(36f) + maxOf(left, right) * sp(16f) * 1.35f)
            }
            "array" -> Block(mark, if (mark.t.isBlank()) dp(78f) else dp(98f))
            "steps" -> Block(mark, mark.items.size * dp(46f))
            "kmap" -> Block(mark, dp(168f))
            "chips" -> {
                val lines = wrapChips(mark.items, widthPx)
                Block(mark, lines * dp(36f) + dp(4f))
            }
            else -> textBlock(mark.copy(t = mark.t.ifBlank { mark.items.joinToString(" ") }), widthPx, sp(18f), 1.2f)
        }
    }

    private fun textBlock(mark: Mark, widthPx: Float, size: Float, factor: Float): Block {
        val lines = wrap(mark.t, ink.applySize(size), widthPx)
        return Block(mark, lines.size * size * factor + dp(6f), lines = lines)
    }

    private fun drawBlock(canvas: Canvas, block: Block, progress: Float, widthPx: Float) {
        if (progress <= 0f) return
        val mark = block.mark
        val top = block.top
        when (mark.k) {
            "title" -> {
                drawLines(canvas, block.lines, dp(4f), top + sp(28f), sp(30f), ink, progress, widthPx)
                val y = top + block.height - dp(4f)
                canvas.drawLine(0f, y, widthPx * progress, y, marker.applyColor(Color.parseColor("#1F4B3A")))
            }
            "h2" -> drawLines(canvas, block.lines, 0f, top + sp(20f), sp(22f), blue, progress, widthPx)
            "bullet" -> {
                canvas.drawCircle(dp(8f), top + sp(12f), dp(4f) * progress.coerceAtMost(1f), marker.applyColor(Color.parseColor("#C9842A")).apply {
                    style = Paint.Style.FILL
                })
                marker.style = Paint.Style.STROKE
                drawLines(canvas, block.lines, dp(22f), top + sp(18f), sp(20f), ink, progress, widthPx - dp(22f))
            }
            "note" -> drawNote(canvas, block, progress, widthPx)
            "formula" -> {
                val paint = blue.applySize(sp(28f))
                val text = mark.t
                val x = (widthPx - paint.measureText(text)).coerceAtLeast(0f) / 2f
                drawRevealText(canvas, text, x, top + sp(28f), paint, widthPx, progress)
            }
            "code" -> drawCode(canvas, block, progress, widthPx)
            "gates" -> drawGates(canvas, mark.items, top, widthPx, progress)
            "table" -> drawTable(canvas, mark, top, widthPx, progress)
            "flow" -> drawFlow(canvas, mark.items, top, widthPx, progress)
            "layers" -> drawLayers(canvas, mark.items, top, widthPx, progress)
            "cols" -> drawCols(canvas, mark, top, widthPx, progress)
            "array" -> drawArray(canvas, mark, top, widthPx, progress)
            "steps" -> drawSteps(canvas, mark.items, top, widthPx, progress)
            "kmap" -> drawKmap(canvas, mark, top, widthPx, progress)
            "chips" -> drawChips(canvas, mark.items, top, widthPx, progress)
            else -> drawLines(canvas, block.lines, 0f, top + sp(18f), sp(18f), ink, progress, widthPx)
        }
    }

    private fun drawLines(
        canvas: Canvas,
        lines: List<String>,
        x: Float,
        firstBaseline: Float,
        size: Float,
        paint: Paint,
        progress: Float,
        maxWidth: Float
    ) {
        val p = paint.applySize(size)
        val lineHeight = size * 1.22f
        val per = 1f / lines.size.coerceAtLeast(1)
        lines.forEachIndexed { index, line ->
            val local = ((progress - index * per) / per).coerceIn(0f, 1f)
            if (local > 0f) {
                drawRevealText(canvas, line, x, firstBaseline + index * lineHeight, p, maxWidth, local)
            }
        }
    }

    private fun drawRevealText(
        canvas: Canvas,
        text: String,
        x: Float,
        baseline: Float,
        paint: Paint,
        maxWidth: Float,
        progress: Float
    ) {
        val width = paint.measureText(text).coerceAtLeast(1f).coerceAtMost(maxWidth)
        val shown = width * progress
        canvas.save()
        canvas.clipRect(x - dp(2f), baseline + paint.fontMetrics.ascent - dp(2f), x + shown + dp(2f), baseline + paint.fontMetrics.descent + dp(4f))
        canvas.drawText(text, x, baseline, paint)
        canvas.restore()
        if (progress in 0.04f..0.98f) {
            penX = x + shown
            penY = baseline
            penVisible = true
        }
    }

    private fun drawNote(canvas: Canvas, block: Block, progress: Float, widthPx: Float) {
        val tone = block.mark.tone
        val color = when (tone) {
            "red" -> Color.parseColor("#F8E6E3")
            "green" -> Color.parseColor("#E5F4EA")
            "blue" -> Color.parseColor("#E5F0FA")
            else -> Color.parseColor("#F8EFDA")
        }
        val label = when (tone) {
            "red" -> "Watch out"
            "green" -> "Exam tip"
            "blue" -> "Try this"
            else -> "Remember"
        }
        val rect = RectF(0f, block.top, widthPx * progress.coerceAtMost(1f), block.top + block.height)
        fill.color = color
        canvas.drawRoundRect(rect, dp(12f), dp(12f), fill)
        val labelPaint = when (tone) {
            "red" -> red
            "green" -> green
            "blue" -> blue
            else -> gold
        }
        drawRevealText(canvas, label, dp(12f), block.top + sp(18f), labelPaint.applySize(sp(14f)), widthPx, progress)
        drawLines(canvas, block.lines, dp(12f), block.top + sp(40f), sp(18f), ink, progress, widthPx - dp(24f))
    }

    private fun drawCode(canvas: Canvas, block: Block, progress: Float, widthPx: Float) {
        val rect = RectF(0f, block.top, widthPx, block.top + block.height)
        fill.color = Color.parseColor("#F4F7FB")
        canvas.drawRoundRect(rect, dp(10f), dp(10f), fill)
        edgePaint.color = Color.parseColor("#D5E1EE")
        canvas.drawRoundRect(rect, dp(10f), dp(10f), edgePaint)
        edgePaint.color = Color.parseColor("#E4D8C4")
        val paint = codePaint.applySize(sp(15f))
        block.lines.forEachIndexed { index, line ->
            val local = ((progress * block.lines.size) - index).coerceIn(0f, 1f)
            if (local > 0f) {
                drawRevealText(canvas, line, dp(10f), block.top + dp(16f) + sp(16f) + index * sp(16f) * 1.35f, paint, widthPx - dp(16f), local)
            }
        }
    }

    private fun drawGates(canvas: Canvas, names: List<String>, top: Float, widthPx: Float, progress: Float) {
        if (names.isEmpty()) return
        val cell = widthPx / names.size
        names.forEachIndexed { index, name ->
            val local = ((progress * names.size) - index).coerceIn(0f, 1f)
            if (local <= 0f) return@forEachIndexed
            val rect = RectF(
                index * cell + dp(16f),
                top + dp(8f),
                index * cell + cell - dp(28f),
                top + dp(78f)
            )
            gatePaths(name, rect).forEach { path ->
                drawStroke(canvas, path, marker.applyColor(Color.parseColor("#1D4E89")), local)
            }
            val labelPaint = ink.applySize(sp(16f))
            val label = name.uppercase()
            val lx = index * cell + (cell - labelPaint.measureText(label)) / 2f
            drawRevealText(canvas, label, lx, top + dp(110f), labelPaint, cell, local)
        }
    }

    private fun drawTable(canvas: Canvas, mark: Mark, top: Float, widthPx: Float, progress: Float) {
        val headers = mark.headers
        val rows = mark.rows
        val cols = maxOf(headers.size, rows.maxOfOrNull { it.size } ?: 1, 1)
        val all = buildList {
            if (headers.isNotEmpty()) add(headers)
            addAll(rows)
        }
        val rowH = dp(34f)
        val colW = widthPx / cols
        all.forEachIndexed { r, row ->
            val local = ((progress * all.size) - r).coerceIn(0f, 1f)
            if (local <= 0f) return@forEachIndexed
            val y = top + r * rowH
            if (r == 0 && headers.isNotEmpty()) {
                fill.color = Color.parseColor("#E7F0E4")
                canvas.drawRect(0f, y, widthPx * local, y + rowH, fill)
            }
            marker.color = Color.parseColor("#C9BBA6")
            marker.strokeWidth = dp(1.4f)
            canvas.drawRect(0f, y, widthPx * local, y + rowH, marker)
            marker.strokeWidth = dp(3f)
            marker.color = Color.parseColor("#1C2430")
            val paint = (if (r == 0 && headers.isNotEmpty()) blue else ink).applySize(sp(15f))
            row.forEachIndexed { c, cell ->
                if (c < cols) {
                    drawRevealText(canvas, cell, c * colW + dp(6f), y + dp(22f), paint, colW - dp(8f), local)
                }
            }
        }
    }

    private fun drawFlow(canvas: Canvas, items: List<String>, top: Float, widthPx: Float, progress: Float) {
        val boxW = widthPx * 0.72f
        val left = (widthPx - boxW) / 2f
        items.forEachIndexed { index, raw ->
            val local = ((progress * items.size) - index).coerceIn(0f, 1f)
            if (local <= 0f) return@forEachIndexed
            val parts = raw.split("|")
            val label = parts[0]
            val shape = parts.getOrElse(1) { "process" }
            val y = top + index * dp(70f)
            val rect = RectF(left, y, left + boxW, y + dp(46f))
            val path = when (shape) {
                "term" -> Path().apply { addRoundRect(rect, dp(24f), dp(24f), Path.Direction.CW) }
                "decision" -> diamond(rect)
                "io" -> parallelogram(rect)
                else -> Path().apply { addRoundRect(rect, dp(8f), dp(8f), Path.Direction.CW) }
            }
            drawStroke(canvas, path, marker.applyColor(Color.parseColor("#1F4B3A")), local)
            val paint = ink.applySize(sp(16f))
            val tx = rect.centerX() - paint.measureText(label) / 2f
            drawRevealText(canvas, label, tx, rect.centerY() + sp(5f), paint, boxW - dp(12f), local)
            if (index < items.lastIndex && local > 0.7f) {
                val arrow = ((local - 0.7f) / 0.3f).coerceIn(0f, 1f)
                val x = rect.centerX()
                canvas.drawLine(x, rect.bottom, x, rect.bottom + dp(18f) * arrow, marker)
            }
        }
    }

    private fun drawLayers(canvas: Canvas, items: List<String>, top: Float, widthPx: Float, progress: Float) {
        val colors = listOf("#E7F0E4", "#E5F0FA", "#F8EFDA", "#F8E6E3", "#EEE7F7", "#E7F6F2", "#F7F1E8")
        items.forEachIndexed { index, item ->
            val local = ((progress * items.size) - index).coerceIn(0f, 1f)
            if (local <= 0f) return@forEachIndexed
            val y = top + index * dp(42f)
            val rect = RectF(0f, y, widthPx * local, y + dp(36f))
            fill.color = Color.parseColor(colors[index % colors.size])
            canvas.drawRoundRect(rect, dp(8f), dp(8f), fill)
            drawRevealText(canvas, item, dp(12f), y + dp(24f), ink.applySize(sp(16f)), widthPx - dp(16f), local)
        }
    }

    private fun drawCols(canvas: Canvas, mark: Mark, top: Float, widthPx: Float, progress: Float) {
        val gap = dp(10f)
        val colW = (widthPx - gap) / 2f
        drawColumn(canvas, mark.t, mark.items, 0f, top, colW, progress, Color.parseColor("#E5F0FA"))
        drawColumn(canvas, mark.t2, mark.items2, colW + gap, top, colW, progress, Color.parseColor("#F8EFDA"))
    }

    private fun drawColumn(
        canvas: Canvas,
        title: String,
        items: List<String>,
        x: Float,
        top: Float,
        width: Float,
        progress: Float,
        color: Int
    ) {
        val height = dp(28f) + items.size * sp(16f) * 1.35f
        fill.color = color
        canvas.drawRoundRect(RectF(x, top, x + width * progress.coerceAtMost(1f), top + height), dp(10f), dp(10f), fill)
        drawRevealText(canvas, title, x + dp(8f), top + sp(16f), blue.applySize(sp(16f)), width - dp(12f), progress)
        items.forEachIndexed { index, item ->
            val local = ((progress * items.size) - index).coerceIn(0f, 1f)
            if (local > 0f) {
                drawRevealText(
                    canvas,
                    item,
                    x + dp(8f),
                    top + dp(28f) + sp(16f) + index * sp(16f) * 1.35f,
                    ink.applySize(sp(15f)),
                    width - dp(12f),
                    local
                )
            }
        }
    }

    private fun drawArray(canvas: Canvas, mark: Mark, top: Float, widthPx: Float, progress: Float) {
        var y = top
        if (mark.t.isNotBlank()) {
            drawRevealText(canvas, mark.t, 0f, y + sp(16f), gold.applySize(sp(16f)), widthPx, progress)
            y += dp(24f)
        }
        val n = mark.items.size.coerceAtLeast(1)
        val size = min(dp(48f), (widthPx - dp(8f) * (n - 1)) / n)
        val rowW = n * size + (n - 1) * dp(8f)
        var x = (widthPx - rowW) / 2f
        mark.items.forEachIndexed { index, value ->
            val local = ((progress * n) - index).coerceIn(0f, 1f)
            if (local <= 0f) return@forEachIndexed
            val rect = RectF(x, y, x + size, y + size)
            if (index in mark.hi) {
                fill.color = Color.parseColor("#F8E2B8")
                canvas.drawRoundRect(rect, dp(6f), dp(6f), fill)
            }
            drawStroke(canvas, Path().apply { addRoundRect(rect, dp(6f), dp(6f), Path.Direction.CW) }, marker, local)
            val paint = ink.applySize(sp(18f))
            drawRevealText(canvas, value, rect.centerX() - paint.measureText(value) / 2f, rect.centerY() + sp(6f), paint, size, local)
            x += size + dp(8f)
        }
    }

    private fun drawSteps(canvas: Canvas, items: List<String>, top: Float, widthPx: Float, progress: Float) {
        items.forEachIndexed { index, item ->
            val local = ((progress * items.size) - index).coerceIn(0f, 1f)
            if (local <= 0f) return@forEachIndexed
            val cy = top + index * dp(46f) + dp(16f)
            canvas.drawCircle(dp(14f), cy, dp(12f), marker.applyColor(Color.parseColor("#1F4B3A")).apply { style = Paint.Style.STROKE })
            val num = ink.applySize(sp(14f))
            val label = (index + 1).toString()
            canvas.drawText(label, dp(14f) - num.measureText(label) / 2f, cy + sp(4f), num)
            if (index < items.lastIndex && local > 0.5f) {
                canvas.drawLine(dp(14f), cy + dp(12f), dp(14f), cy + dp(30f), marker)
            }
            drawRevealText(canvas, item, dp(34f), cy + sp(4f), ink.applySize(sp(16f)), widthPx - dp(40f), local)
            marker.style = Paint.Style.STROKE
        }
    }

    private fun drawKmap(canvas: Canvas, mark: Mark, top: Float, widthPx: Float, progress: Float) {
        val cells = mark.items
        val n = if (cells.size >= 8) 8 else 4
        val cols = if (n == 8) 4 else 2
        val rows = 2
        val cell = min(dp(54f), widthPx / (cols + 1.4f))
        val originX = dp(54f)
        val originY = top + dp(36f)
        drawRevealText(canvas, mark.t.ifBlank { "A \\ B" }, 0f, top + sp(16f), blue.applySize(sp(16f)), widthPx, progress)
        val headers = if (cols == 2) listOf("0", "1") else listOf("00", "01", "11", "10")
        headers.forEachIndexed { index, header ->
            drawRevealText(canvas, header, originX + index * cell + cell / 3f, originY - dp(8f), ink.applySize(sp(14f)), cell, progress)
        }
        drawRevealText(canvas, "0", dp(8f), originY + cell * 0.65f, ink.applySize(sp(14f)), dp(30f), progress)
        drawRevealText(canvas, "1", dp(8f), originY + cell * 1.65f, ink.applySize(sp(14f)), dp(30f), progress)
        for (r in 0 until rows) {
            for (c in 0 until cols) {
                val index = r * cols + c
                val local = ((progress * n) - index).coerceIn(0f, 1f)
                if (local <= 0f || index >= cells.size) continue
                val rect = RectF(originX + c * cell, originY + r * cell, originX + (c + 1) * cell, originY + (r + 1) * cell)
                if (index in mark.hi) {
                    fill.color = Color.parseColor("#D9F2DF")
                    canvas.drawRect(rect, fill)
                }
                drawStroke(canvas, Path().apply { addRect(rect, Path.Direction.CW) }, marker, local)
                val value = cells[index]
                val paint = ink.applySize(sp(20f))
                drawRevealText(canvas, value, rect.centerX() - paint.measureText(value) / 2f, rect.centerY() + sp(6f), paint, cell, local)
            }
        }
    }

    private fun drawChips(canvas: Canvas, items: List<String>, top: Float, widthPx: Float, progress: Float) {
        var x = 0f
        var y = top
        val paint = ink.applySize(sp(15f))
        items.forEachIndexed { index, item ->
            val local = ((progress * items.size) - index).coerceIn(0f, 1f)
            val w = paint.measureText(item) + dp(22f)
            if (x + w > widthPx) {
                x = 0f
                y += dp(36f)
            }
            if (local > 0f) {
                val rect = RectF(x, y, x + w * local.coerceAtMost(1f), y + dp(28f))
                fill.color = Color.parseColor("#E7F0E4")
                canvas.drawRoundRect(rect, dp(14f), dp(14f), fill)
                drawRevealText(canvas, item, x + dp(10f), y + dp(19f), paint, w, local)
            }
            x += w + dp(8f)
        }
    }

    private fun drawStroke(canvas: Canvas, path: Path, paint: Paint, progress: Float) {
        paint.style = Paint.Style.STROKE
        val measure = PathMeasure(path, false)
        do {
            val segment = Path()
            measure.getSegment(0f, measure.length * progress, segment, true)
            canvas.drawPath(segment, paint)
        } while (measure.nextContour())
    }

    private fun gatePaths(name: String, rect: RectF): List<Path> {
        val key = name.lowercase()
        val body = RectF(rect.left + rect.width() * 0.08f, rect.top, rect.right - rect.width() * 0.16f, rect.bottom)
        val paths = mutableListOf<Path>()
        when (key) {
            "not" -> paths += triangle(body)
            "and", "nand" -> paths += andGate(body)
            else -> paths += orGate(body)
        }
        if (key == "xor" || key == "xnor") paths += extraCurve(body)
        if (key == "not" || key == "nand" || key == "nor" || key == "xnor") {
            val bubble = Path()
            bubble.addCircle(body.right + dp(7f), body.centerY(), dp(5f), Path.Direction.CW)
            paths += bubble
        }
        val inputY = listOf(body.top + body.height() * 0.3f, body.top + body.height() * 0.7f)
        val wireReach = if (key == "or" || key == "nor" || key == "xor" || key == "xnor") 0.46f else 0.02f
        if (key == "not") {
            paths += linePath(body.left - dp(18f), body.centerY(), body.left, body.centerY())
        } else {
            inputY.forEach { y ->
                paths += linePath(body.left - dp(18f), y, body.left + body.width() * wireReach, y)
            }
        }
        val outStart = if (key == "not" || key == "nand" || key == "nor" || key == "xnor") body.right + dp(12f) else body.right
        paths += linePath(outStart, body.centerY(), outStart + dp(18f), body.centerY())
        return paths
    }

    private fun andGate(r: RectF): Path {
        val path = Path()
        val midX = r.left + r.width() * 0.45f
        path.moveTo(r.left, r.top)
        path.lineTo(midX, r.top)
        path.arcTo(RectF(midX - r.height() / 2f, r.top, midX + r.height() / 2f, r.bottom), -90f, 180f)
        path.lineTo(r.left, r.bottom)
        path.close()
        return path
    }

    private fun orGate(r: RectF): Path {
        val path = Path()
        path.moveTo(r.left + r.width() * 0.18f, r.top)
        path.quadTo(r.right, r.top + r.height() * 0.05f, r.right - r.width() * 0.02f, r.centerY())
        path.quadTo(r.right, r.bottom - r.height() * 0.05f, r.left + r.width() * 0.18f, r.bottom)
        path.quadTo(r.left + r.width() * 0.55f, r.centerY(), r.left + r.width() * 0.18f, r.top)
        path.close()
        return path
    }

    private fun extraCurve(r: RectF): Path {
        val path = Path()
        path.moveTo(r.left, r.top)
        path.quadTo(r.left + r.width() * 0.28f, r.centerY(), r.left, r.bottom)
        return path
    }

    private fun triangle(r: RectF): Path {
        val path = Path()
        path.moveTo(r.left, r.top)
        path.lineTo(r.left, r.bottom)
        path.lineTo(r.right, r.centerY())
        path.close()
        return path
    }

    private fun diamond(rect: RectF): Path {
        val path = Path()
        path.moveTo(rect.centerX(), rect.top)
        path.lineTo(rect.right, rect.centerY())
        path.lineTo(rect.centerX(), rect.bottom)
        path.lineTo(rect.left, rect.centerY())
        path.close()
        return path
    }

    private fun parallelogram(rect: RectF): Path {
        val path = Path()
        val skew = rect.height() * 0.35f
        path.moveTo(rect.left + skew, rect.top)
        path.lineTo(rect.right, rect.top)
        path.lineTo(rect.right - skew, rect.bottom)
        path.lineTo(rect.left, rect.bottom)
        path.close()
        return path
    }

    private fun linePath(x1: Float, y1: Float, x2: Float, y2: Float): Path {
        return Path().apply {
            moveTo(x1, y1)
            lineTo(x2, y2)
        }
    }

    private fun wrap(text: String, paint: Paint, maxWidth: Float): List<String> {
        if (text.isBlank()) return emptyList()
        val words = text.split(Regex("\\s+"))
        val lines = mutableListOf<String>()
        var current = ""
        words.forEach { word ->
            val trial = if (current.isEmpty()) word else "$current $word"
            if (paint.measureText(trial) <= maxWidth) {
                current = trial
            } else {
                if (current.isNotEmpty()) lines.add(current)
                current = word
            }
        }
        if (current.isNotEmpty()) lines.add(current)
        return lines
    }

    private fun wrapChips(items: List<String>, widthPx: Float): Int {
        if (items.isEmpty()) return 1
        val paint = ink.applySize(sp(15f))
        var x = 0f
        var lines = 1
        items.forEach { item ->
            val w = paint.measureText(item) + dp(30f)
            if (x + w > widthPx) {
                lines += 1
                x = w
            } else {
                x += w
            }
        }
        return lines
    }

    private fun textPaint(color: Int) = Paint(Paint.ANTI_ALIAS_FLAG).apply {
        this.color = color
        typeface = hand
        textSize = sp(18f)
    }

    private fun Paint.applySize(size: Float): Paint {
        textSize = size
        return this
    }

    private fun Paint.applyColor(value: Int): Paint {
        color = value
        style = Paint.Style.STROKE
        return this
    }

    private fun dp(value: Float): Float = value * resources.displayMetrics.density

    private fun sp(value: Float): Float =
        value * resources.displayMetrics.density * resources.configuration.fontScale

    private class Block(
        val mark: Mark,
        val height: Float,
        var top: Float = 0f,
        val lines: List<String> = emptyList()
    )
}
