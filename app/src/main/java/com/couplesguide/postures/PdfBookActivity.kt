package com.couplesguide.postures

import android.os.Bundle
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.viewpager2.widget.ViewPager2
import com.couplesguide.postures.data.PdfBookRepository
import com.couplesguide.postures.databinding.ActivityPdfBookBinding
import com.couplesguide.postures.ui.PdfPageAdapter
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.VoiceNarrator

class PdfBookActivity : AppCompatActivity() {

    private lateinit var binding: ActivityPdfBookBinding
    private lateinit var adapter: PdfPageAdapter
    private var voiceNarrator: VoiceNarrator? = null
    private var voiceReady = false
    private var isSpeaking = false
    private var language = LocaleHelper.LANG_UR

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityPdfBookBinding.inflate(layoutInflater)
        setContentView(binding.root)

        language = LocaleHelper.getLanguage(this)

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = getString(R.string.pdf_book_title)

        voiceNarrator = VoiceNarrator(
            context = this,
            onReadyChanged = { ready -> voiceReady = ready },
            onSpeakingChanged = { speaking ->
                isSpeaking = speaking
                updateListenButtonState()
            },
            onLanguageIssue = { message ->
                Toast.makeText(this, message, Toast.LENGTH_LONG).show()
            }
        )

        adapter = PdfPageAdapter(PdfBookRepository.pages)
        binding.viewPager.adapter = adapter
        binding.viewPager.offscreenPageLimit = 1

        binding.viewPager.registerOnPageChangeCallback(object : ViewPager2.OnPageChangeCallback() {
            override fun onPageSelected(position: Int) {
                voiceNarrator?.stop()
                updatePageCounter(position)
                updateNavButtons(position)
            }
        })

        updatePageCounter(0)
        updateNavButtons(0)

        binding.prevButton.setOnClickListener {
            val current = binding.viewPager.currentItem
            if (current > 0) {
                binding.viewPager.currentItem = current - 1
            }
        }

        binding.nextButton.setOnClickListener {
            val current = binding.viewPager.currentItem
            if (current < adapter.itemCount - 1) {
                binding.viewPager.currentItem = current + 1
            }
        }

        binding.listenButton.setOnClickListener {
            toggleNarration()
        }
    }

    private fun updatePageCounter(position: Int) {
        val total = adapter.itemCount
        binding.pageCounter.text = getString(R.string.page_counter, position + 1, total)
    }

    private fun updateNavButtons(position: Int) {
        binding.prevButton.isEnabled = position > 0
        binding.nextButton.isEnabled = position < adapter.itemCount - 1
        binding.prevButton.alpha = if (position > 0) 1f else 0.4f
        binding.nextButton.alpha = if (position < adapter.itemCount - 1) 1f else 0.4f
    }

    private fun updateListenButtonState() {
        binding.listenButton.text = if (isSpeaking) {
            getString(R.string.stop)
        } else {
            getString(R.string.listen)
        }
        binding.listenButton.setIconResource(
            if (isSpeaking) android.R.drawable.ic_media_pause
            else android.R.drawable.ic_media_play
        )
    }

    private fun toggleNarration() {
        if (isSpeaking) {
            voiceNarrator?.stop()
            return
        }
        if (!voiceReady) {
            Toast.makeText(this, R.string.voice_not_ready, Toast.LENGTH_SHORT).show()
            return
        }

        val position = binding.viewPager.currentItem
        val page = PdfBookRepository.pages.getOrNull(position) ?: return

        val narrationText = if (language == LocaleHelper.LANG_UR) {
            "${page.urduTitle}۔ ${page.urduNarration}"
        } else {
            "${page.englishTitle}. ${page.englishNarration}"
        }

        if (voiceNarrator?.speak(narrationText, language) != true) {
            Toast.makeText(this, R.string.voice_install_prompt, Toast.LENGTH_LONG).show()
        }
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            android.R.id.home -> {
                onBackPressedDispatcher.onBackPressed()
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }

    override fun onDestroy() {
        voiceNarrator?.shutdown()
        voiceNarrator = null
        super.onDestroy()
    }
}
