package com.couplesguide.postures.util

import android.widget.ImageView
import androidx.annotation.DrawableRes
import androidx.vectordrawable.graphics.drawable.AnimatedVectorDrawableCompat

object AnimatedIllustrationHelper {

    fun bind(imageView: ImageView, @DrawableRes animatedRes: Int) {
        stop(imageView)
        imageView.setImageResource(animatedRes)
        start(imageView)
    }

    fun start(imageView: ImageView) {
        when (val drawable = imageView.drawable) {
            is AnimatedVectorDrawableCompat -> drawable.start()
            is android.graphics.drawable.AnimatedVectorDrawable -> drawable.start()
        }
    }

    fun stop(imageView: ImageView) {
        when (val drawable = imageView.drawable) {
            is AnimatedVectorDrawableCompat -> drawable.stop()
            is android.graphics.drawable.AnimatedVectorDrawable -> drawable.stop()
        }
    }
}
