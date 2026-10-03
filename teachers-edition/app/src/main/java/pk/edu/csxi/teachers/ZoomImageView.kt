package pk.edu.csxi.teachers

import android.content.Context
import android.graphics.Matrix
import android.graphics.drawable.Drawable
import android.util.AttributeSet
import android.view.GestureDetector
import android.view.MotionEvent
import android.view.ScaleGestureDetector
import androidx.appcompat.widget.AppCompatImageView
import kotlin.math.max
import kotlin.math.min

/** Minimal pinch-to-zoom / pan / double-tap image view that starts fitted to the width. */
class ZoomImageView @JvmOverloads constructor(
    context: Context, attrs: AttributeSet? = null,
) : AppCompatImageView(context, attrs) {

    private val m = Matrix()
    private val values = FloatArray(9)
    private var baseScale = 1f

    private val scaleDetector = ScaleGestureDetector(context, object : ScaleGestureDetector.SimpleOnScaleGestureListener() {
        override fun onScale(d: ScaleGestureDetector): Boolean {
            val target = (currentScale() * d.scaleFactor).coerceIn(baseScale, baseScale * 5f)
            val factor = target / currentScale()
            m.postScale(factor, factor, d.focusX, d.focusY)
            fixTranslation()
            imageMatrix = m
            return true
        }
    })

    private val gestureDetector = GestureDetector(context, object : GestureDetector.SimpleOnGestureListener() {
        override fun onScroll(e1: MotionEvent?, e2: MotionEvent, dx: Float, dy: Float): Boolean {
            m.postTranslate(-dx, -dy)
            fixTranslation()
            imageMatrix = m
            return true
        }

        override fun onDoubleTap(e: MotionEvent): Boolean {
            val zoomed = currentScale() > baseScale * 1.2f
            val target = if (zoomed) baseScale else baseScale * 2.5f
            val factor = target / currentScale()
            m.postScale(factor, factor, e.x, e.y)
            fixTranslation()
            imageMatrix = m
            return true
        }
    })

    init {
        scaleType = ScaleType.MATRIX
    }

    override fun setImageDrawable(drawable: Drawable?) {
        super.setImageDrawable(drawable)
        post { fit() }
    }

    override fun onSizeChanged(w: Int, h: Int, oldw: Int, oldh: Int) {
        super.onSizeChanged(w, h, oldw, oldh)
        fit()
    }

    private fun fit() {
        val d = drawable ?: return
        if (width == 0 || height == 0) return
        baseScale = min(width.toFloat() / d.intrinsicWidth, height.toFloat() / d.intrinsicHeight)
            .let { max(it, width.toFloat() / d.intrinsicWidth) }
        m.reset()
        m.postScale(baseScale, baseScale)
        m.postTranslate((width - d.intrinsicWidth * baseScale) / 2f, 0f)
        imageMatrix = m
    }

    private fun currentScale(): Float {
        m.getValues(values)
        return values[Matrix.MSCALE_X]
    }

    private fun fixTranslation() {
        val d = drawable ?: return
        m.getValues(values)
        val scale = values[Matrix.MSCALE_X]
        val w = d.intrinsicWidth * scale
        val h = d.intrinsicHeight * scale
        var tx = values[Matrix.MTRANS_X]
        var ty = values[Matrix.MTRANS_Y]
        tx = if (w <= width) (width - w) / 2f else tx.coerceIn(width - w, 0f)
        ty = if (h <= height) 0f else ty.coerceIn(height - h, 0f)
        values[Matrix.MTRANS_X] = tx
        values[Matrix.MTRANS_Y] = ty
        m.setValues(values)
    }

    override fun onTouchEvent(event: MotionEvent): Boolean {
        scaleDetector.onTouchEvent(event)
        if (!scaleDetector.isInProgress) gestureDetector.onTouchEvent(event)
        if (event.actionMasked == MotionEvent.ACTION_DOWN) parent?.requestDisallowInterceptTouchEvent(true)
        return true
    }
}
