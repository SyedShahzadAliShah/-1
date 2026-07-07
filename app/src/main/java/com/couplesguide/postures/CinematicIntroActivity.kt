package com.couplesguide.postures

import android.content.Intent
import android.graphics.BitmapFactory
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import androidx.appcompat.app.AppCompatActivity
import com.couplesguide.postures.databinding.ActivityCinematicIntroBinding
import com.couplesguide.postures.util.CinematicAnimationHelper
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.VoiceNarrator

class CinematicIntroActivity : AppCompatActivity() {

    private lateinit var binding: ActivityCinematicIntroBinding
    private var voiceNarrator: VoiceNarrator? = null
    private val handler = Handler(Looper.getMainLooper())

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityCinematicIntroBinding.inflate(layoutInflater)
        setContentView(binding.root)

        loadCoverImage()
        CinematicAnimationHelper.fadeIn(binding.introContent, durationMs = 900L)
        CinematicAnimationHelper.pulse(binding.introProgress)

        voiceNarrator = VoiceNarrator(
            context = this,
            onReadyChanged = { ready ->
                if (ready) speakIntro()
            },
            onSpeakingChanged = { },
            onLanguageIssue = null
        )

        handler.postDelayed({ navigateToBook(autoPlay = true) }, 8000L)
    }

    private fun loadCoverImage() {
        try {
            assets.open("pdf_source/page_01.png").use { stream ->
                binding.introImage.setImageBitmap(BitmapFactory.decodeStream(stream))
            }
        } catch (_: Exception) {
            binding.introImage.setImageResource(R.drawable.pic_guide_cover)
        }
        binding.introImage.post { CinematicAnimationHelper.applyKenBurns(binding.introImage, 7000L) }
    }

    private fun speakIntro() {
        val intro = getString(R.string.cinematic_intro_narration)
        voiceNarrator?.speak(intro, LocaleHelper.LANG_UR)
    }

    private fun navigateToBook(autoPlay: Boolean) {
        if (isFinishing) return
        startActivity(Intent(this, CinematicBookActivity::class.java).apply {
            putExtra(CinematicBookActivity.EXTRA_AUTO_PLAY, autoPlay)
            putExtra(CinematicBookActivity.EXTRA_START_PAGE, 1)
        })
        finish()
        overridePendingTransition(android.R.anim.fade_in, android.R.anim.fade_out)
    }

    override fun onDestroy() {
        handler.removeCallbacksAndMessages(null)
        CinematicAnimationHelper.stopKenBurns(binding.introImage)
        voiceNarrator?.shutdown()
        voiceNarrator = null
        super.onDestroy()
    }
}
