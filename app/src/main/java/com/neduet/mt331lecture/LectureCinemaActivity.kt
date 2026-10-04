package com.neduet.mt331lecture

import android.animation.ObjectAnimator
import android.os.Bundle
import android.view.View
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.viewpager2.widget.ViewPager2
import com.neduet.mt331lecture.data.mt331.LectureBeat
import com.neduet.mt331lecture.data.mt331.LectureChapter
import com.neduet.mt331lecture.data.mt331.Mt331LectureRepository
import com.neduet.mt331lecture.databinding.ActivityLectureCinemaBinding
import com.neduet.mt331lecture.ui.LectureBeatPagerAdapter
import com.neduet.mt331lecture.util.LocaleHelper
import com.neduet.mt331lecture.util.Mt331Narration
import com.neduet.mt331lecture.util.VoiceNarrator

class LectureCinemaActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_CHAPTER_ID = "mt331_chapter_id"
    }

    private lateinit var binding: ActivityLectureCinemaBinding
    private lateinit var chapter: LectureChapter
    private lateinit var beatAdapter: LectureBeatPagerAdapter

    private var voiceNarrator: VoiceNarrator? = null
    private var voiceReady = false
    private var isSpeaking = false
    private var ttsLanguage = LocaleHelper.LANG_EN

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLectureCinemaBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val chapterId = intent.getStringExtra(EXTRA_CHAPTER_ID)
        val found = chapterId?.let { Mt331LectureRepository.getChapterById(it) }
        if (found == null) {
            finish()
            return
        }
        chapter = found
        ttsLanguage = LocaleHelper.getLanguage(this)

        voiceNarrator = VoiceNarrator(
            context = this,
            onReadyChanged = { ready -> voiceReady = ready },
            onSpeakingChanged = { speaking ->
                isSpeaking = speaking
                updatePlayButton()
            },
            onLanguageIssue = { message ->
                Toast.makeText(this, message, Toast.LENGTH_LONG).show()
            }
        )

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = chapter.title(ttsLanguage)

        beatAdapter = LectureBeatPagerAdapter(ttsLanguage)
        binding.beatPager.adapter = beatAdapter
        beatAdapter.submitBeats(chapter.beats)
        binding.beatPager.registerOnPageChangeCallback(object : ViewPager2.OnPageChangeCallback() {
            override fun onPageSelected(position: Int) {
                updateProgressLabel(position)
                voiceNarrator?.setOnQueueCompleteListener(null)
                voiceNarrator?.stop()
            }
        })

        syncTtsChips()
        binding.chipEnglish.setOnClickListener {
            ttsLanguage = LocaleHelper.LANG_EN
            syncTtsChips()
            beatAdapter.setDisplayLanguage(ttsLanguage)
            voiceNarrator?.stop()
        }
        binding.chipUrdu.setOnClickListener {
            ttsLanguage = LocaleHelper.LANG_UR
            syncTtsChips()
            beatAdapter.setDisplayLanguage(ttsLanguage)
            voiceNarrator?.stop()
        }

        binding.btnPrevious.setOnClickListener { goToBeat(binding.beatPager.currentItem - 1) }
        binding.btnNext.setOnClickListener { goToBeat(binding.beatPager.currentItem + 1) }
        binding.btnPlay.setOnClickListener { toggleBeatNarration() }

        updateProgressLabel(0)
        updatePlayButton()
        startGlowAnimation()
    }

    private fun syncTtsChips() {
        binding.chipEnglish.isChecked = ttsLanguage == LocaleHelper.LANG_EN
        binding.chipUrdu.isChecked = ttsLanguage == LocaleHelper.LANG_UR
    }

    private fun startGlowAnimation() {
        ObjectAnimator.ofFloat(binding.glowOrb, View.TRANSLATION_Y, 0f, 28f, 0f).apply {
            duration = 5200L
            repeatCount = ObjectAnimator.INFINITE
            start()
        }
        ObjectAnimator.ofFloat(binding.glowOrb, View.ALPHA, 0.35f, 0.7f, 0.35f).apply {
            duration = 4200L
            repeatCount = ObjectAnimator.INFINITE
            start()
        }
    }

    private fun updateProgressLabel(position: Int) {
        val total = chapter.beats.size
        binding.beatProgress.text = getString(
            R.string.mt331_beat_progress,
            position + 1,
            total
        )
    }

    private fun goToBeat(index: Int) {
        if (index < 0 || index >= chapter.beats.size) return
        binding.beatPager.setCurrentItem(index, true)
    }

    private fun toggleBeatNarration() {
        if (isSpeaking) {
            voiceNarrator?.setOnQueueCompleteListener(null)
            voiceNarrator?.stop()
            return
        }
        if (!voiceReady) {
            Toast.makeText(this, R.string.voice_not_ready, Toast.LENGTH_SHORT).show()
            return
        }
        val beat = chapter.beats[binding.beatPager.currentItem]
        startBeatNarration(beat)
    }

    private fun startBeatNarration(beat: LectureBeat) {
        voiceNarrator?.setOnQueueCompleteListener {
            voiceNarrator?.setOnQueueCompleteListener(null)
            if (!binding.switchAutoAdvance.isChecked) return@setOnQueueCompleteListener
            val next = binding.beatPager.currentItem + 1
            if (next < chapter.beats.size) {
                binding.beatPager.setCurrentItem(next, true)
                binding.beatPager.post { startBeatNarration(chapter.beats[next]) }
            }
        }
        val spoken = voiceNarrator?.speak(
            Mt331Narration.buildBeatNarration(beat, ttsLanguage),
            ttsLanguage
        ) ?: false
        if (!spoken) {
            voiceNarrator?.setOnQueueCompleteListener(null)
        }
    }

    private fun updatePlayButton() {
        binding.btnPlay.text = if (isSpeaking) {
            getString(R.string.stop)
        } else {
            getString(R.string.listen)
        }
    }

    override fun onSupportNavigateUp(): Boolean {
        onBackPressedDispatcher.onBackPressed()
        return true
    }

    override fun onDestroy() {
        voiceNarrator?.setOnQueueCompleteListener(null)
        voiceNarrator?.shutdown()
        voiceNarrator = null
        super.onDestroy()
    }
}
