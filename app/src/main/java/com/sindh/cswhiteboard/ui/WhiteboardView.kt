package com.sindh.cswhiteboard.ui

import android.animation.ValueAnimator
import android.content.Context
import android.graphics.Canvas
import android.graphics.DashPathEffect
import android.graphics.Paint
import android.graphics.Path
import android.graphics.RectF
import android.graphics.Typeface
import android.text.Layout
import android.text.StaticLayout
import android.text.TextPaint
import android.util.AttributeSet
import android.view.View
import android.view.animation.LinearInterpolator
import com.sindh.cswhiteboard.data.BoardAction
import kotlin.math.min
import kotlin.math.sin

class WhiteboardView @JvmOverloads constructor(
    context: Context,
    attrs: AttributeSet? = null
) : View(context, attrs) {

    var onDrawComplete: (() -> Unit)? = null

    private val items = mutableListOf<BoardItem>()
    private var animator: ValueAnimator? = null
    private var playing = false
    private var pendingActions: List<BoardAction> = emptyList()
    private var actionIndex = 0
    private var queueWhenLayout = false

    private val boardPaint = Paint(Paint.ANTI_ALIAS_FLAG).apply { color = 0xFFF7F1E3.toInt() }
    private val rulePaint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
        color = 0x332C5282
        strokeWidth = dp(1f)
    }
    private val marginPaint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
        color = 0x55C53030
        strokeWidth = dp(1.5f)
    }
    private val penPaint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
        color = 0xFFE53E3E
        style = Paint.Style.FILL
    }
    private val headingPaint = TextPaint(Paint.ANTI_ALIAS_FLAG).apply {
        color = 0xFF1A365D
        typeface = Typeface.create(Typeface.SANS_SERIF, Typeface.BOLD)
        textSize = sp(22f)
    }
    private val subPaint = TextPaint(Paint.ANTI_ALIAS_FLAG).apply {
        color = 0xFF2B6CB0
        typeface = Typeface.create(Typeface.SANS_SERIF, Typeface.BOLD)
        textSize = sp(16f)
    }
    private val bodyPaint = TextPaint(Paint.ANTI_ALIAS_FLAG).apply {
        color = 0xFF1A202C
        textSize = sp(15f)
    }
    private val notePaint = TextPaint(Paint.ANTI_ALIAS_FLAG).apply {
        color = 0xFF4A5568
        textSize = sp(13f)
        typeface = Typeface.create(Typeface.SANS_SERIF, Typeface.ITALIC)
    }
    private val codePaint = TextPaint(Paint.ANTI_ALIAS_FLAG).apply {
        color = 0xFFC6F6D5
        typeface = Typeface.MONOSPACE
        textSize = sp(13f)
    }
    private val calloutPaint = TextPaint(Paint.ANTI_ALIAS_FLAG).apply {
        textSize = sp(14f)
        typeface = Typeface.create(Typeface.SANS_SERIF, Typeface.BOLD)
    }
    private val boxPaint = Paint(Paint.ANTI_ALIAS_FLAG)
    private val strokePaint = Paint(Paint.ANTI_ALIAS_FLAG).apply {
        style = Paint.Style.STROKE
        strokeCap = Paint.Cap.ROUND
        strokeJoin = Paint.Join.ROUND
    }

    fun clearBoard() {
        animator?.cancel()
        items.clear()
        pendingActions = emptyList()
        actionIndex = 0
        playing = false
        invalidate()
    }

    fun skipCurrent() {
        animator?.end()
        items.forEach { it.progress = 1f }
        invalidate()
    }

    fun play(actions: List<BoardAction>) {
        animator?.cancel()
        if (width == 0) {
            pendingActions = actions
            queueWhenLayout = true
            return
        }
        playing = true
        pendingActions = actions
        actionIndex = 0
        playNext()
    }

    fun isAnimating(): Boolean = playing

    override fun onSizeChanged(w: Int, h: Int, oldw: Int, oldh: Int) {
        super.onSizeChanged(w, h, oldw, oldh)
        if (queueWhenLayout && pendingActions.isNotEmpty()) {
            queueWhenLayout = false
            play(pendingActions)
        }
    }

    private fun playNext() {
        if (actionIndex >= pendingActions.size) {
            playing = false
            onDrawComplete?.invoke()
            return
        }
        val action = pendingActions[actionIndex]
        actionIndex++
        if (action.type == "clear" || (action.type == "heading" && items.isNotEmpty() && pendingActions.firstOrNull()?.type == "heading")) {
            // keep existing content unless action.clear was handled by the player
        }
        val item = createItem(action) ?: run {
            playNext()
            return
        }
        items.add(item)
        requestLayout()
        val duration = item.durationMs
        val anim = ValueAnimator.ofFloat(0f, 1f).setDuration(duration)
        anim.interpolator = LinearInterpolator()
        anim.addUpdateListener {
            item.progress = it.animatedValue as Float
            invalidate()
        }
        anim.addListener(object : android.animation.AnimatorListenerAdapter() {
            override fun onAnimationEnd(animation: android.animation.Animator) {
                item.progress = 1f
                invalidate()
                playNext()
            }
        })
        animator = anim
        anim.start()
    }

    private fun createItem(action: BoardAction): BoardItem? {
        val widthPx = (width - paddingStart - paddingEnd - dp(36f)).toInt().coerceAtLeast(100)
        return when (action.type) {
            "heading" -> textItem(action.text, headingPaint, widthPx, 1100)
            "subheading" -> textItem(action.text, subPaint, widthPx, 700)
            "note" -> textItem(action.text, notePaint, widthPx, 600)
            "bullet" -> textItem("•  ${action.text}", bodyPaint, widthPx, (action.text.length * 28L).coerceIn(700L, 2200L))
            "formula" -> textItem(action.text, headingPaint, widthPx, 900)
            "callout" -> calloutItem(action.kind, action.text, widthPx)
            "code" -> codeItem(action.lines, widthPx)
            "diagram" -> BoardItem.Diagram(action.name.ifBlank { "ct_pillars" }, dp(210f), 1700)
            else -> if (action.text.isNotBlank()) textItem(action.text, bodyPaint, widthPx, 800) else null
        }
    }

    private fun textItem(text: String, paint: TextPaint, widthPx: Int, duration: Long): BoardItem.Text {
        val layout = StaticLayout.Builder.obtain(text, 0, text.length, paint, widthPx)
            .setAlignment(Layout.Alignment.ALIGN_NORMAL)
            .setLineSpacing(0f, 1.12f)
            .build()
        return BoardItem.Text(layout, duration)
    }

    private fun calloutItem(kind: String, text: String, widthPx: Int): BoardItem.Callout {
        val (bg, fg, label) = when (kind) {
            "mistake" -> Triple(0xFFFEE2E2.toInt(), 0xFF9B1C1C.toInt(), "COMMON MISTAKE")
            "exam" -> Triple(0xFFD1FAE5.toInt(), 0xFF065F46.toInt(), "EXAM TIP")
            else -> Triple(0xFFFEF3C7.toInt(), 0xFF92400E.toInt(), "REMEMBER")
        }
        calloutPaint.color = fg
        val body = "$label  ·  $text"
        val layout = StaticLayout.Builder.obtain(body, 0, body.length, calloutPaint, widthPx - dp(20f).toInt())
            .setLineSpacing(0f, 1.1f)
            .build()
        return BoardItem.Callout(layout, bg, fg, 1100)
    }

    private fun codeItem(lines: List<String>, widthPx: Int): BoardItem.Code {
        val joined = if (lines.isEmpty()) "# code" else lines.joinToString("\n")
        val layout = StaticLayout.Builder.obtain(joined, 0, joined.length, codePaint, widthPx - dp(16f).toInt())
            .setLineSpacing(4f, 1f)
            .build()
        return BoardItem.Code(layout, 1000)
    }

    override fun onMeasure(widthMeasureSpec: Int, heightMeasureSpec: Int) {
        val w = MeasureSpec.getSize(widthMeasureSpec)
        var h = paddingTop + paddingBottom + dp(24f)
        items.forEach { h += it.height() + dp(10f) }
        h += dp(80f)
        val min = dp(420f).toInt()
        setMeasuredDimension(w, maxOf(min, h.toInt()))
    }

    override fun onDraw(canvas: Canvas) {
        super.onDraw(canvas)
        canvas.drawRect(0f, 0f, width.toFloat(), height.toFloat(), boardPaint)
        var y = dp(18f)
        while (y < height) {
            canvas.drawLine(dp(28f), y, width - dp(16f), y, rulePaint)
            y += dp(28f)
        }
        canvas.drawLine(dp(22f), dp(8f), dp(22f), height - dp(8f), marginPaint)

        var cursorY = paddingTop + dp(16f)
        val x = paddingStart + dp(32f)
        var penX = x
        var penY = cursorY
        items.forEach { item ->
            when (item) {
                is BoardItem.Text -> {
                    canvas.save()
                    canvas.translate(x, cursorY)
                    val clipH = item.layout.height * item.progress
                    canvas.clipRect(0f, 0f, item.layout.width.toFloat(), clipH + dp(4f))
                    item.layout.draw(canvas)
                    canvas.restore()
                    penX = x + item.layout.width * 0.12f + item.progress * item.layout.width * 0.7f
                    penY = cursorY + clipH
                    cursorY += item.layout.height + dp(10f)
                }
                is BoardItem.Callout -> {
                    val rect = RectF(x - dp(6f), cursorY, width - dp(16f), cursorY + item.layout.height + dp(16f))
                    boxPaint.color = item.bg
                    canvas.drawRoundRect(rect, dp(10f), dp(10f), boxPaint)
                    strokePaint.color = item.fg
                    strokePaint.strokeWidth = dp(2f)
                    canvas.drawRoundRect(rect, dp(10f), dp(10f), strokePaint)
                    canvas.save()
                    canvas.translate(x + dp(8f), cursorY + dp(8f))
                    canvas.clipRect(0f, 0f, item.layout.width.toFloat(), item.layout.height * item.progress)
                    item.layout.draw(canvas)
                    canvas.restore()
                    penX = rect.right - dp(18f)
                    penY = rect.top + rect.height() * item.progress
                    cursorY += rect.height() + dp(12f)
                }
                is BoardItem.Code -> {
                    val rect = RectF(x - dp(6f), cursorY, width - dp(16f), cursorY + item.layout.height + dp(18f))
                    boxPaint.color = 0xFF1A202C.toInt()
                    canvas.drawRoundRect(rect, dp(10f), dp(10f), boxPaint)
                    canvas.save()
                    canvas.translate(x + dp(8f), cursorY + dp(8f))
                    canvas.clipRect(0f, 0f, item.layout.width.toFloat(), item.layout.height * item.progress + 2f)
                    item.layout.draw(canvas)
                    canvas.restore()
                    penX = rect.left + dp(24f)
                    penY = cursorY + item.layout.height * item.progress
                    cursorY += rect.height() + dp(12f)
                }
                is BoardItem.Diagram -> {
                    val area = RectF(x, cursorY, width - dp(16f), cursorY + item.heightPx)
                    Diagrams.draw(canvas, area, item.name, item.progress, strokePaint, bodyPaint, headingPaint)
                    penX = area.left + area.width() * item.progress
                    penY = area.centerY()
                    cursorY += item.heightPx + dp(12f)
                }
            }
        }
        if (playing) {
            val bob = sin((System.currentTimeMillis() % 600) / 600f * Math.PI * 2).toFloat() * dp(2f)
            canvas.drawCircle(penX, penY + bob, dp(5f), penPaint)
            postInvalidateOnAnimation()
        }
    }

    private fun dp(v: Float) = v * resources.displayMetrics.density
    private fun sp(v: Float) = v * resources.displayMetrics.scaledDensity

    private sealed class BoardItem {
        abstract var progress: Float
        abstract val durationMs: Long
        abstract fun height(): Float

        data class Text(
            val layout: StaticLayout,
            override val durationMs: Long,
            override var progress: Float = 0f
        ) : BoardItem() {
            override fun height(): Float = layout.height.toFloat()
        }

        data class Callout(
            val layout: StaticLayout,
            val bg: Int,
            val fg: Int,
            override val durationMs: Long,
            override var progress: Float = 0f
        ) : BoardItem() {
            override fun height(): Float = layout.height + dpSafe(16f)
            private fun dpSafe(v: Float) = layout.paint.textSize * (v / 14f)
        }

        data class Code(
            val layout: StaticLayout,
            override val durationMs: Long,
            override var progress: Float = 0f
        ) : BoardItem() {
            override fun height(): Float = layout.height + 36f
        }

        data class Diagram(
            val name: String,
            val heightPx: Float,
            override val durationMs: Long,
            override var progress: Float = 0f
        ) : BoardItem() {
            override fun height(): Float = heightPx
        }
    }
}

private object Diagrams {
    fun draw(
        canvas: Canvas,
        area: RectF,
        name: String,
        progress: Float,
        stroke: Paint,
        body: TextPaint,
        heading: TextPaint
    ) {
        stroke.style = Paint.Style.STROKE
        stroke.strokeWidth = 4f
        stroke.color = 0xFF1A365D.toInt()
        val fill = Paint(Paint.ANTI_ALIAS_FLAG)
        when (name) {
            "analog_digital" -> analogDigital(canvas, area, progress, stroke, body)
            "and_gate" -> gate(canvas, area, progress, stroke, body, "AND", "Y = A·B", onlyAll = true)
            "or_gate" -> gate(canvas, area, progress, stroke, body, "OR", "Y = A+B", onlyAll = false)
            "not_gate" -> notGate(canvas, area, progress, stroke, body)
            "nand_gate" -> gate(canvas, area, progress, stroke, body, "NAND", "Y = (A·B)'", onlyAll = true, bubble = true)
            "nor_gate" -> gate(canvas, area, progress, stroke, body, "NOR", "Y = (A+B)'", onlyAll = false, bubble = true)
            "xor_gate" -> gate(canvas, area, progress, stroke, body, "XOR", "Y = A ⊕ B", onlyAll = false, extraArc = true)
            "truth_table" -> truth(canvas, area, progress, stroke, body)
            "kmap" -> kmap(canvas, area, progress, stroke, body)
            "sdlc" -> cycle(canvas, area, progress, stroke, body, listOf("Plan", "Analyze", "Design", "Build", "Test", "Maintain"))
            "waterfall" -> waterfall(canvas, area, progress, stroke, body)
            "agile" -> cycle(canvas, area, progress, stroke, body, listOf("Plan", "Sprint", "Review", "Adapt"))
            "osi" -> stack(canvas, area, progress, stroke, body, listOf("7 Application", "6 Presentation", "5 Session", "4 Transport", "3 Network", "2 Data Link", "1 Physical"), 0xFF2B6CB0.toInt())
            "tcpip" -> stack(canvas, area, progress, stroke, body, listOf("Application", "Transport", "Internet", "Network Access"), 0xFF0F766E.toInt())
            "bubble_sort" -> bars(canvas, area, progress, stroke, fill, body, intArrayOf(5, 1, 4, 2, 3), "Bubble sort")
            "selection_sort" -> bars(canvas, area, progress, stroke, fill, body, intArrayOf(4, 5, 1, 3, 2), "Selection sort")
            "binary_search" -> searchLine(canvas, area, progress, stroke, body, binary = true)
            "linear_search" -> searchLine(canvas, area, progress, stroke, body, binary = false)
            "ct_pillars" -> pillars(canvas, area, progress, stroke, body)
            "if_else" -> ifElse(canvas, area, progress, stroke, body)
            "loop" -> loop(canvas, area, progress, stroke, body)
            "er_diagram" -> er(canvas, area, progress, stroke, body)
            "db_table" -> db(canvas, area, progress, stroke, body)
            "iot" -> iot(canvas, area, progress, stroke, body)
            "ai_net" -> neural(canvas, area, progress, stroke, fill, body)
            "stack" -> stack(canvas, area, progress, stroke, body, listOf("TOP  30", "20", "10", "BASE"), 0xFF9B2C2C.toInt())
            "queue" -> queue(canvas, area, progress, stroke, body)
            "linked_list" -> linked(canvas, area, progress, stroke, body)
            "tree" -> tree(canvas, area, progress, stroke, fill, body)
            "mvp" -> cycle(canvas, area, progress, stroke, body, listOf("Idea", "Build", "Measure", "Learn"))
            "hci" -> hci(canvas, area, progress, stroke, body)
            "big_o" -> bigO(canvas, area, progress, stroke, body)
            else -> pillars(canvas, area, progress, stroke, body)
        }
    }

    private fun analogDigital(canvas: Canvas, area: RectF, p: Float, stroke: Paint, body: TextPaint) {
        val mid = area.centerY()
        val left = RectF(area.left, area.top, area.centerX() - 12, area.bottom)
        val right = RectF(area.centerX() + 12, area.top, area.right, area.bottom)
        stroke.color = 0xFFC53030.toInt()
        val wave = Path()
        wave.moveTo(left.left + 8, mid)
        var x = left.left + 8
        while (x < left.right - 8) {
            val t = (x - left.left) / left.width()
            wave.lineTo(x, mid - 28f * sin(t * 6.2).toFloat())
            x += 6
        }
        stroke.pathEffect = DashPathEffect(floatArrayOf(4000f * p, 4000f), 0f)
        canvas.drawPath(wave, stroke)
        body.color = 0xFFC53030.toInt()
        canvas.drawText("Analog (sine)", left.left + 8, area.bottom - 8, body)

        stroke.color = 0xFF2B6CB0.toInt()
        val sq = Path()
        sq.moveTo(right.left + 8, mid + 24)
        val steps = 4
        val w = (right.width() - 16) / steps
        for (i in 0 until steps) {
            val x0 = right.left + 8 + i * w
            if (i % 2 == 0) {
                sq.lineTo(x0, mid - 24); sq.lineTo(x0 + w, mid - 24)
            } else {
                sq.lineTo(x0, mid + 24); sq.lineTo(x0 + w, mid + 24)
            }
        }
        canvas.drawPath(sq, stroke)
        body.color = 0xFF2B6CB0.toInt()
        canvas.drawText("Digital (square)", right.left + 8, area.bottom - 8, body)
        stroke.pathEffect = null
    }

    private fun gate(
        canvas: Canvas, area: RectF, p: Float, stroke: Paint, body: TextPaint,
        label: String, expr: String, onlyAll: Boolean, bubble: Boolean = false, extraArc: Boolean = false
    ) {
        val cx = area.centerX(); val cy = area.centerY()
        stroke.alpha = (255 * min(1f, p * 1.4f)).toInt()
        canvas.drawLine(area.left + 8, cy - 28, cx - 40, cy - 28, stroke)
        canvas.drawLine(area.left + 8, cy + 28, cx - 40, cy + 28, stroke)
        val bodyRect = RectF(cx - 40, cy - 48, cx + 36, cy + 48)
        canvas.drawRoundRect(bodyRect, 18f, 18f, stroke)
        if (extraArc) canvas.drawArc(cx - 58, cy - 48, cx - 28, cy + 48, -90f, 180f, false, stroke)
        if (bubble) canvas.drawCircle(cx + 46, cy, 8f, stroke)
        canvas.drawLine(if (bubble) cx + 54 else cx + 36, cy, area.right - 12, cy, stroke)
        body.color = 0xFF1A365D.toInt()
        canvas.drawText("A", area.left + 8, cy - 34, body)
        canvas.drawText("B", area.left + 8, cy + 46, body)
        canvas.drawText(label, cx - 24, cy + 6, body)
        canvas.drawText(expr, cx - 50, area.bottom - 6, body)
        stroke.alpha = 255
    }

    private fun notGate(canvas: Canvas, area: RectF, p: Float, stroke: Paint, body: TextPaint) {
        val cy = area.centerY(); val cx = area.centerX()
        stroke.alpha = (255 * p).toInt()
        canvas.drawLine(area.left + 16, cy, cx - 30, cy, stroke)
        val path = Path()
        path.moveTo(cx - 30, cy - 40); path.lineTo(cx + 28, cy); path.lineTo(cx - 30, cy + 40); path.close()
        canvas.drawPath(path, stroke)
        canvas.drawCircle(cx + 38, cy, 8f, stroke)
        canvas.drawLine(cx + 46, cy, area.right - 16, cy, stroke)
        canvas.drawText("NOT   Y = A'", cx - 40, area.bottom - 8, body)
        stroke.alpha = 255
    }

    private fun truth(canvas: Canvas, area: RectF, p: Float, stroke: Paint, body: TextPaint) {
        val rows = listOf("A  B  |  AND  OR  NOT A", "0  0  |   0    0    1", "0  1  |   0    1    1", "1  0  |   0    1    0", "1  1  |   1    1    0")
        val shown = (rows.size * p).toInt().coerceAtLeast(1)
        var y = area.top + 28
        body.textSize = body.textSize
        body.color = 0xFF1A365D.toInt()
        rows.take(shown).forEachIndexed { i, line ->
            if (i == 0) headingish(canvas, line, area.left + 12, y, body)
            else canvas.drawText(line, area.left + 12, y, body)
            y += 32
        }
    }

    private fun headingish(canvas: Canvas, text: String, x: Float, y: Float, body: TextPaint) {
        val old = body.typeface
        body.typeface = Typeface.DEFAULT_BOLD
        canvas.drawText(text, x, y, body)
        body.typeface = old
    }

    private fun kmap(canvas: Canvas, area: RectF, p: Float, stroke: Paint, body: TextPaint) {
        val cells = arrayOf(arrayOf("1", "1", "1", "0"), arrayOf("1", "1", "0", "0"))
        val cellW = (area.width() - 50) / 4
        val cellH = (area.height() - 40) / 2
        canvas.drawText("K-map", area.left, area.top + 16, body)
        for (r in 0 until 2) {
            for (c in 0 until 4) {
                val rect = RectF(
                    area.left + 40 + c * cellW,
                    area.top + 28 + r * cellH,
                    area.left + 40 + (c + 1) * cellW,
                    area.top + 28 + (r + 1) * cellH
                )
                canvas.drawRect(rect, stroke)
                if (p > (r * 4 + c + 1) / 8f) {
                    canvas.drawText(cells[r][c], rect.centerX() - 6, rect.centerY() + 8, body)
                }
            }
        }
        stroke.color = 0xFFC53030.toInt()
        if (p > 0.7f) canvas.drawRoundRect(
            RectF(area.left + 44, area.top + 32, area.left + 40 + 2 * cellW - 4, area.top + 28 + 2 * cellH - 4),
            8f, 8f, stroke
        )
        stroke.color = 0xFF1A365D.toInt()
    }

    private fun cycle(canvas: Canvas, area: RectF, p: Float, stroke: Paint, body: TextPaint, labels: List<String>) {
        val n = labels.size
        val shown = (n * p).toInt().coerceAtLeast(1)
        val w = area.width() / n
        for (i in 0 until shown) {
            val x = area.left + i * w + 8
            val rect = RectF(x, area.centerY() - 28, x + w - 16, area.centerY() + 28)
            canvas.drawRoundRect(rect, 12f, 12f, stroke)
            canvas.drawText(labels[i], rect.left + 8, rect.centerY() + 6, body)
            if (i < shown - 1) canvas.drawLine(rect.right, rect.centerY(), rect.right + 16, rect.centerY(), stroke)
        }
    }

    private fun waterfall(canvas: Canvas, area: RectF, p: Float, stroke: Paint, body: TextPaint) {
        val steps = listOf("Req", "Design", "Code", "Test", "Deploy")
        val shown = (steps.size * p).toInt().coerceAtLeast(1)
        for (i in 0 until shown) {
            val rect = RectF(
                area.left + i * 28,
                area.top + 20 + i * 32,
                area.left + 140 + i * 28,
                area.top + 52 + i * 32
            )
            canvas.drawRect(rect, stroke)
            canvas.drawText(steps[i], rect.left + 10, rect.centerY() + 6, body)
        }
    }

    private fun stack(canvas: Canvas, area: RectF, p: Float, stroke: Paint, body: TextPaint, layers: List<String>, color: Int) {
        stroke.color = color
        val shown = (layers.size * p).toInt().coerceAtLeast(1)
        val h = (area.height() - 16) / layers.size
        layers.take(shown).forEachIndexed { i, label ->
            val rect = RectF(area.left + 24, area.top + 8 + i * h, area.right - 24, area.top + 8 + (i + 1) * h - 6)
            canvas.drawRoundRect(rect, 8f, 8f, stroke)
            canvas.drawText(label, rect.left + 12, rect.centerY() + 6, body)
        }
        stroke.color = 0xFF1A365D.toInt()
    }

    private fun bars(canvas: Canvas, area: RectF, p: Float, stroke: Paint, fill: Paint, body: TextPaint, values: IntArray, title: String) {
        canvas.drawText(title, area.left + 8, area.top + 18, body)
        val max = values.max().toFloat()
        val w = (area.width() - 20) / values.size
        values.forEachIndexed { i, v ->
            val h = (v / max) * (area.height() - 50) * p
            val left = area.left + 10 + i * w
            val rect = RectF(left + 8, area.bottom - 16 - h, left + w - 8, area.bottom - 16)
            fill.color = 0x662B6CB0
            canvas.drawRect(rect, fill)
            canvas.drawRect(rect, stroke)
            canvas.drawText(v.toString(), rect.centerX() - 6, rect.top - 6, body)
        }
    }

    private fun searchLine(canvas: Canvas, area: RectF, p: Float, stroke: Paint, body: TextPaint, binary: Boolean) {
        val nums = listOf(1, 3, 4, 7, 9, 12, 18)
        val w = area.width() / nums.size
        nums.forEachIndexed { i, n ->
            val rect = RectF(area.left + i * w + 6, area.centerY() - 24, area.left + (i + 1) * w - 6, area.centerY() + 24)
            canvas.drawRect(rect, stroke)
            canvas.drawText(n.toString(), rect.centerX() - 8, rect.centerY() + 6, body)
        }
        stroke.color = 0xFFC53030.toInt()
        if (binary) {
            val mid = 3
            val x = area.left + mid * w + w / 2
            canvas.drawCircle(x, area.centerY(), 28f * p, stroke)
            canvas.drawText("mid", x - 16, area.centerY() + 50, body)
        } else {
            val idx = (p * 4).toInt().coerceAtMost(4)
            val x = area.left + idx * w + w / 2
            canvas.drawLine(x, area.centerY() - 40, x, area.centerY() + 40, stroke)
        }
        stroke.color = 0xFF1A365D.toInt()
        canvas.drawText(if (binary) "Binary search (sorted)" else "Linear search", area.left + 8, area.top + 18, body)
    }

    private fun pillars(canvas: Canvas, area: RectF, p: Float, stroke: Paint, body: TextPaint) {
        val labels = listOf("Decompose", "Pattern", "Abstract", "Algorithm")
        val shown = (4 * p).toInt().coerceAtLeast(1)
        val w = area.width() / 4
        for (i in 0 until shown) {
            val rect = RectF(area.left + i * w + 10, area.top + 36, area.left + (i + 1) * w - 10, area.bottom - 20)
            canvas.drawRoundRect(rect, 14f, 14f, stroke)
            canvas.drawText(labels[i], rect.left + 8, rect.centerY(), body)
        }
    }

    private fun ifElse(canvas: Canvas, area: RectF, p: Float, stroke: Paint, body: TextPaint) {
        val diamond = Path()
        val cx = area.centerX(); val cy = area.top + 50
        diamond.moveTo(cx, cy - 34); diamond.lineTo(cx + 70, cy); diamond.lineTo(cx, cy + 34); diamond.lineTo(cx - 70, cy); diamond.close()
        canvas.drawPath(diamond, stroke)
        canvas.drawText("condition?", cx - 40, cy + 6, body)
        canvas.drawLine(cx + 70, cy, area.right - 30, cy, stroke)
        canvas.drawLine(cx - 70, cy, area.left + 30, cy, stroke)
        canvas.drawText("True", area.right - 80, cy - 8, body)
        canvas.drawText("False", area.left + 30, cy - 8, body)
        if (p > 0.5f) {
            canvas.drawRoundRect(RectF(area.right - 110, cy + 20, area.right - 20, cy + 56), 8f, 8f, stroke)
            canvas.drawRoundRect(RectF(area.left + 20, cy + 20, area.left + 110, cy + 56), 8f, 8f, stroke)
            canvas.drawText("if", area.right - 80, cy + 44, body)
            canvas.drawText("else", area.left + 48, cy + 44, body)
        }
    }

    private fun loop(canvas: Canvas, area: RectF, p: Float, stroke: Paint, body: TextPaint) {
        canvas.drawRoundRect(RectF(area.centerX() - 70, area.top + 20, area.centerX() + 70, area.top + 60), 8f, 8f, stroke)
        canvas.drawText("for i in range(n)", area.centerX() - 62, area.top + 46, body)
        canvas.drawLine(area.centerX(), area.top + 60, area.centerX(), area.bottom - 50, stroke)
        canvas.drawRoundRect(RectF(area.centerX() - 60, area.bottom - 50, area.centerX() + 60, area.bottom - 16), 8f, 8f, stroke)
        canvas.drawText("body", area.centerX() - 18, area.bottom - 28, body)
        if (p > 0.6f) {
            val back = Path()
            back.moveTo(area.centerX() + 60, area.bottom - 33)
            back.lineTo(area.centerX() + 90, area.bottom - 33)
            back.lineTo(area.centerX() + 90, area.top + 40)
            back.lineTo(area.centerX() + 70, area.top + 40)
            canvas.drawPath(back, stroke)
        }
    }

    private fun er(canvas: Canvas, area: RectF, p: Float, stroke: Paint, body: TextPaint) {
        canvas.drawRoundRect(RectF(area.left + 10, area.centerY() - 36, area.left + 130, area.centerY() + 36), 8f, 8f, stroke)
        canvas.drawText("STUDENT", area.left + 30, area.centerY() + 6, body)
        canvas.drawLine(area.left + 130, area.centerY(), area.right - 140, area.centerY(), stroke)
        canvas.drawText("enrolls", area.centerX() - 24, area.centerY() - 8, body)
        canvas.drawRoundRect(RectF(area.right - 140, area.centerY() - 36, area.right - 10, area.centerY() + 36), 8f, 8f, stroke)
        canvas.drawText("COURSE", area.right - 118, area.centerY() + 6, body)
        if (p > 0.5f) canvas.drawText("1      M", area.left + 140, area.centerY() + 28, body)
    }

    private fun db(canvas: Canvas, area: RectF, p: Float, stroke: Paint, body: TextPaint) {
        val headers = listOf("Roll", "Name", "City")
        val rows = listOf(listOf("101", "Ali", "Hyd"), listOf("102", "Sara", "KHI"))
        val w = area.width() / 3
        headers.forEachIndexed { i, h ->
            val rect = RectF(area.left + i * w, area.top + 20, area.left + (i + 1) * w, area.top + 52)
            canvas.drawRect(rect, stroke)
            canvas.drawText(h, rect.left + 10, rect.centerY() + 6, body)
        }
        if (p > 0.4f) {
            rows.forEachIndexed { r, row ->
                row.forEachIndexed { c, v ->
                    val rect = RectF(area.left + c * w, area.top + 52 + r * 32, area.left + (c + 1) * w, area.top + 84 + r * 32)
                    canvas.drawRect(rect, stroke)
                    canvas.drawText(v, rect.left + 10, rect.centerY() + 6, body)
                }
            }
        }
    }

    private fun iot(canvas: Canvas, area: RectF, p: Float, stroke: Paint, body: TextPaint) {
        val boxes = listOf("Sensor", "Network", "Cloud", "Actuator")
        boxes.forEachIndexed { i, label ->
            val x = area.left + i * (area.width() / 4) + 8
            val rect = RectF(x, area.centerY() - 24, x + area.width() / 4 - 16, area.centerY() + 24)
            if (p > i / 4f) {
                canvas.drawRoundRect(rect, 10f, 10f, stroke)
                canvas.drawText(label, rect.left + 8, rect.centerY() + 6, body)
            }
        }
    }

    private fun neural(canvas: Canvas, area: RectF, p: Float, stroke: Paint, fill: Paint, body: TextPaint) {
        val layers = listOf(3, 4, 2)
        val xs = layers.indices.map { i -> area.left + 40 + i * (area.width() - 80) / 2 }
        fill.color = 0xFF2B6CB0.toInt()
        val nodes = layers.mapIndexed { li, count ->
            (0 until count).map { n ->
                val y = area.top + 30 + n * ((area.height() - 40) / count)
                xs[li] to y
            }
        }
        if (p > 0.3f) {
            stroke.color = 0x662B6CB0
            for (l in 0 until nodes.size - 1) {
                for (a in nodes[l]) for (b in nodes[l + 1]) canvas.drawLine(a.first, a.second, b.first, b.second, stroke)
            }
            stroke.color = 0xFF1A365D.toInt()
        }
        nodes.flatten().forEach { (x, y) -> canvas.drawCircle(x, y, 10f, fill) }
        canvas.drawText("Neural net", area.left + 8, area.bottom - 8, body)
    }

    private fun queue(canvas: Canvas, area: RectF, p: Float, stroke: Paint, body: TextPaint) {
        val vals = listOf("55", "76", "90")
        vals.forEachIndexed { i, v ->
            val rect = RectF(area.left + 40 + i * 70, area.centerY() - 28, area.left + 100 + i * 70, area.centerY() + 28)
            canvas.drawRect(rect, stroke)
            canvas.drawText(v, rect.centerX() - 12, rect.centerY() + 6, body)
        }
        canvas.drawText("FRONT", area.left + 40, area.centerY() + 50, body)
        canvas.drawText("REAR", area.left + 180, area.centerY() + 50, body)
        if (p > 0.5f) canvas.drawText("Enqueue →    ← Dequeue", area.left + 40, area.top + 24, body)
    }

    private fun linked(canvas: Canvas, area: RectF, p: Float, stroke: Paint, body: TextPaint) {
        val vals = listOf("10", "20", "30")
        vals.forEachIndexed { i, v ->
            val x = area.left + 20 + i * 110
            val rect = RectF(x, area.centerY() - 24, x + 70, area.centerY() + 24)
            canvas.drawRect(rect, stroke)
            canvas.drawLine(x + 48, rect.top, x + 48, rect.bottom, stroke)
            canvas.drawText(v, x + 10, area.centerY() + 6, body)
            if (i < 2) canvas.drawLine(x + 70, area.centerY(), x + 110, area.centerY(), stroke)
        }
        canvas.drawText("HEAD →  null", area.left + 20, area.bottom - 12, body)
    }

    private fun tree(canvas: Canvas, area: RectF, p: Float, stroke: Paint, fill: Paint, body: TextPaint) {
        fill.color = 0xFF2B6CB0.toInt()
        val root = area.centerX() to (area.top + 28)
        val left = (area.centerX() - 70) to (area.centerY() + 10)
        val right = (area.centerX() + 70) to (area.centerY() + 10)
        val ll = (area.centerX() - 110) to (area.bottom - 28)
        val lr = (area.centerX() - 30) to (area.bottom - 28)
        canvas.drawLine(root.first, root.second, left.first, left.second, stroke)
        canvas.drawLine(root.first, root.second, right.first, right.second, stroke)
        if (p > 0.5f) {
            canvas.drawLine(left.first, left.second, ll.first, ll.second, stroke)
            canvas.drawLine(left.first, left.second, lr.first, lr.second, stroke)
        }
        listOf(root, left, right, ll, lr).forEach { canvas.drawCircle(it.first, it.second, 12f, fill) }
        canvas.drawText("Tree", area.left + 8, area.top + 16, body)
    }

    private fun hci(canvas: Canvas, area: RectF, p: Float, stroke: Paint, body: TextPaint) {
        canvas.drawCircle(area.left + 70, area.centerY(), 36f, stroke)
        canvas.drawText("Human", area.left + 42, area.centerY() + 6, body)
        canvas.drawRoundRect(RectF(area.right - 140, area.centerY() - 36, area.right - 20, area.centerY() + 36), 8f, 8f, stroke)
        canvas.drawText("Computer", area.right - 128, area.centerY() + 6, body)
        canvas.drawLine(area.left + 106, area.centerY(), area.right - 140, area.centerY(), stroke)
        if (p > 0.5f) canvas.drawText("look · hear · touch", area.centerX() - 70, area.centerY() - 12, body)
    }

    private fun bigO(canvas: Canvas, area: RectF, p: Float, stroke: Paint, body: TextPaint) {
        canvas.drawLine(area.left + 30, area.bottom - 20, area.right - 10, area.bottom - 20, stroke)
        canvas.drawLine(area.left + 30, area.bottom - 20, area.left + 30, area.top + 10, stroke)
        val path = Path()
        path.moveTo(area.left + 30, area.bottom - 24)
        path.quadTo(area.centerX(), area.centerY(), area.right - 20, area.top + 20)
        stroke.color = 0xFFC53030.toInt()
        canvas.drawPath(path, stroke)
        stroke.color = 0xFF1A365D.toInt()
        canvas.drawText("O(n²) grows fast", area.left + 40, area.top + 24, body)
        canvas.drawText("n →", area.right - 50, area.bottom - 6, body)
    }
}
