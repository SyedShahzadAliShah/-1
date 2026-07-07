package com.couplesguide.postures.util

import android.animation.Animator
import android.animation.AnimatorListenerAdapter
import android.animation.AnimatorSet
import android.animation.ObjectAnimator
import android.animation.PropertyValuesHolder
import android.view.View
import android.view.animation.AccelerateDecelerateInterpolator
import android.view.animation.DecelerateInterpolator
import android.widget.ImageView
import java.util.WeakHashMap

object CinematicAnimationHelper {

    private val kenBurnsAnimations = WeakHashMap<ImageView, AnimatorSet>()
    private val pulseAnimations = WeakHashMap<View, ObjectAnimator>()

    fun applyKenBurns(imageView: ImageView, durationMs: Long = 9000L) {
        stopKenBurns(imageView)
        imageView.scaleType = ImageView.ScaleType.CENTER_CROP
        imageView.pivotX = imageView.width / 2f
        imageView.pivotY = imageView.height / 2f

        val scaleX = PropertyValuesHolder.ofFloat(View.SCALE_X, 1f, 1.12f)
        val scaleY = PropertyValuesHolder.ofFloat(View.SCALE_Y, 1f, 1.12f)
        val translationX = PropertyValuesHolder.ofFloat(View.TRANSLATION_X, -8f, 8f)
        val translationY = PropertyValuesHolder.ofFloat(View.TRANSLATION_Y, -6f, 6f)

        val zoomIn = ObjectAnimator.ofPropertyValuesHolder(imageView, scaleX, scaleY, translationX, translationY).apply {
            this.duration = durationMs
            interpolator = AccelerateDecelerateInterpolator()
        }

        val zoomOut = ObjectAnimator.ofPropertyValuesHolder(
            imageView,
            PropertyValuesHolder.ofFloat(View.SCALE_X, 1.12f, 1f),
            PropertyValuesHolder.ofFloat(View.SCALE_Y, 1.12f, 1f),
            PropertyValuesHolder.ofFloat(View.TRANSLATION_X, 8f, -8f),
            PropertyValuesHolder.ofFloat(View.TRANSLATION_Y, 6f, -6f)
        ).apply {
            this.duration = durationMs
            interpolator = AccelerateDecelerateInterpolator()
        }

        val set = AnimatorSet().apply {
            playSequentially(zoomIn, zoomOut)
            addListener(object : AnimatorListenerAdapter() {
                override fun onAnimationEnd(animation: Animator) {
                    if (kenBurnsAnimations[imageView] === this@apply) {
                        start()
                    }
                }
            })
            start()
        }
        kenBurnsAnimations[imageView] = set
    }

    fun stopKenBurns(imageView: ImageView) {
        kenBurnsAnimations.remove(imageView)?.cancel()
        imageView.animate().cancel()
        imageView.scaleX = 1f
        imageView.scaleY = 1f
        imageView.translationX = 0f
        imageView.translationY = 0f
    }

    fun fadeIn(view: View, durationMs: Long = 650L, onEnd: (() -> Unit)? = null) {
        view.alpha = 0f
        view.visibility = View.VISIBLE
        view.animate()
            .alpha(1f)
            .setDuration(durationMs)
            .setInterpolator(DecelerateInterpolator())
            .withEndAction { onEnd?.invoke() }
            .start()
    }

    fun fadeOut(view: View, durationMs: Long = 450L, onEnd: (() -> Unit)? = null) {
        view.animate()
            .alpha(0f)
            .setDuration(durationMs)
            .setInterpolator(AccelerateDecelerateInterpolator())
            .withEndAction {
                view.visibility = View.INVISIBLE
                onEnd?.invoke()
            }
            .start()
    }

    fun crossFade(hideView: View, showView: View, durationMs: Long = 500L, onEnd: (() -> Unit)? = null) {
        showView.alpha = 0f
        showView.visibility = View.VISIBLE
        hideView.animate().alpha(0f).setDuration(durationMs).start()
        showView.animate()
            .alpha(1f)
            .setDuration(durationMs)
            .withEndAction { onEnd?.invoke() }
            .start()
    }

    fun pulse(view: View) {
        stopPulse(view)
        val animator = ObjectAnimator.ofFloat(view, View.ALPHA, 1f, 0.45f, 1f).apply {
            duration = 1200
            repeatCount = ObjectAnimator.INFINITE
            repeatMode = ObjectAnimator.REVERSE
            start()
        }
        pulseAnimations[view] = animator
    }

    fun stopPulse(view: View) {
        pulseAnimations.remove(view)?.cancel()
        view.alpha = 1f
    }
}
