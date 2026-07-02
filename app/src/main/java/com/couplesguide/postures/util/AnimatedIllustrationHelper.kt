package com.couplesguide.postures.util

import android.animation.ObjectAnimator
import android.animation.PropertyValuesHolder
import android.view.View
import android.widget.ImageView
import androidx.annotation.DrawableRes
import java.util.WeakHashMap

object AnimatedIllustrationHelper {

    private val runningAnimations = WeakHashMap<ImageView, ObjectAnimator>()

    fun bind(imageView: ImageView, @DrawableRes imageRes: Int) {
        stop(imageView)
        imageView.setImageResource(imageRes)
        start(imageView)
    }

    fun start(imageView: ImageView) {
        stop(imageView)
        val scaleX = PropertyValuesHolder.ofFloat(View.SCALE_X, 1f, 1.04f)
        val scaleY = PropertyValuesHolder.ofFloat(View.SCALE_Y, 1f, 1.04f)
        val animator = ObjectAnimator.ofPropertyValuesHolder(imageView, scaleX, scaleY).apply {
            duration = 1400
            repeatCount = ObjectAnimator.INFINITE
            repeatMode = ObjectAnimator.REVERSE
        }
        runningAnimations[imageView] = animator
        animator.start()
    }

    fun stop(imageView: ImageView) {
        runningAnimations.remove(imageView)?.cancel()
        imageView.scaleX = 1f
        imageView.scaleY = 1f
        imageView.animate().cancel()
    }
}
