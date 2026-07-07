package com.couplesguide.postures

import android.content.Intent
import android.graphics.BitmapFactory
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import com.couplesguide.postures.data.PdfBookRepository
import com.couplesguide.postures.databinding.ActivityCinematicBookBinding
import com.couplesguide.postures.util.CinematicAnimationHelper
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.PdfBookExporter
import com.couplesguide.postures.util.VoiceNarrator
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class CinematicBookActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_START_PAGE = "start_page"
        const val EXTRA_AUTO_PLAY = "auto_play"
        private const val AUTO_ADVANCE_DELAY_MS = 12000L
    }

    private lateinit var binding: ActivityCinematicBookBinding
    private var currentPage = 1
    private var isAutoPlaying = false
    private var isSpeaking = false
    private var voiceReady = false
    private var voiceNarrator: VoiceNarrator? = null
    private val autoHandler = Handler(Looper.getMainLooper())
    private val autoAdvanceRunnable = Runnable { advanceAutoPlay() }

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityCinematicBookBinding.inflate(layoutInflater)
        setContentView(binding.root)

        currentPage = intent.getIntExtra(EXTRA_START_PAGE, 1).coerceIn(1, PdfBookRepository.getTotalPages())
        isAutoPlaying = intent.getBooleanExtra(EXTRA_AUTO_PLAY, false)

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = getString(R.string.cinematic_book_title)

        voiceNarrator = VoiceNarrator(
            context = this,
            onReadyChanged = { ready -> voiceReady = ready },
            onSpeakingChanged = { speaking ->
                isSpeaking = speaking
                updatePlayPauseButton()
                invalidateOptionsMenu()
            },
            onLanguageIssue = { message -> Toast.makeText(this, message, Toast.LENGTH_LONG).show() }
        )

        binding.btnPrev.setOnClickListener {
            stopAutoPlay()
            showPage(currentPage - 1)
        }
        binding.btnNext.setOnClickListener {
            stopAutoPlay()
            showPage(currentPage + 1)
        }
        binding.btnPlayPause.setOnClickListener { toggleAutoPlay() }

        showPage(currentPage, animate = false)
        if (isAutoPlaying) {
            startAutoPlay()
        }
    }

    private fun showPage(pageNumber: Int, animate: Boolean = true) {
        val page = PdfBookRepository.getPage(pageNumber) ?: return
        currentPage = page.pageNumber

        voiceNarrator?.stop()
        autoHandler.removeCallbacks(autoAdvanceRunnable)

        val bindPage = {
            binding.pageTitle.text = page.titleUr
            binding.pageNarration.text = page.narrationUr
            binding.pageIndicator.text = getString(
                R.string.cinematic_page_indicator,
                currentPage,
                PdfBookRepository.getTotalPages()
            )
            binding.pageProgress.max = PdfBookRepository.getTotalPages()
            binding.pageProgress.progress = currentPage

            loadPageImage(page.assetImage)
            CinematicAnimationHelper.applyKenBurns(binding.pageImage)

            if (isAutoPlaying && voiceReady) {
                speakCurrentPage()
            }
            scheduleAutoAdvance()
        }

        if (animate) {
            CinematicAnimationHelper.fadeOut(binding.pageContainer) {
                bindPage()
                CinematicAnimationHelper.fadeIn(binding.pageContainer)
            }
        } else {
            bindPage()
            CinematicAnimationHelper.fadeIn(binding.pageContainer, durationMs = 400L)
        }
    }

    private fun loadPageImage(assetPath: String) {
        try {
            assets.open(assetPath).use { stream ->
                val bitmap = BitmapFactory.decodeStream(stream)
                binding.pageImage.setImageBitmap(bitmap)
            }
        } catch (_: Exception) {
            binding.pageImage.setImageResource(R.drawable.pic_guide_cover)
        }
    }

    private fun speakCurrentPage() {
        val narration = PdfBookRepository.buildNarrationForPage(currentPage)
        if (narration.isBlank()) return
        if (!voiceReady) {
            Toast.makeText(this, R.string.voice_not_ready, Toast.LENGTH_SHORT).show()
            return
        }
        voiceNarrator?.speak(narration, LocaleHelper.LANG_UR)
    }

    private fun toggleAutoPlay() {
        if (isAutoPlaying) {
            stopAutoPlay()
        } else {
            startAutoPlay()
        }
    }

    private fun startAutoPlay() {
        isAutoPlaying = true
        updatePlayPauseButton()
        speakCurrentPage()
        scheduleAutoAdvance()
    }

    private fun stopAutoPlay() {
        isAutoPlaying = false
        autoHandler.removeCallbacks(autoAdvanceRunnable)
        voiceNarrator?.stop()
        updatePlayPauseButton()
    }

    private fun scheduleAutoAdvance() {
        autoHandler.removeCallbacks(autoAdvanceRunnable)
        if (isAutoPlaying) {
            autoHandler.postDelayed(autoAdvanceRunnable, AUTO_ADVANCE_DELAY_MS)
        }
    }

    private fun advanceAutoPlay() {
        if (currentPage >= PdfBookRepository.getTotalPages()) {
            stopAutoPlay()
            Toast.makeText(this, R.string.cinematic_complete, Toast.LENGTH_SHORT).show()
            return
        }
        showPage(currentPage + 1)
    }

    private fun updatePlayPauseButton() {
        binding.btnPlayPause.text = if (isAutoPlaying) {
            getString(R.string.cinematic_pause)
        } else {
            getString(R.string.cinematic_play)
        }
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_cinematic, menu)
        val listenItem = menu.findItem(R.id.action_listen)
        listenItem.title = if (isSpeaking) getString(R.string.stop) else getString(R.string.listen)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            R.id.action_listen -> {
                if (isSpeaking) voiceNarrator?.stop() else speakCurrentPage()
                true
            }
            R.id.action_explore_guide -> {
                startActivity(Intent(this, MainActivity::class.java))
                true
            }
            R.id.action_export_source -> {
                exportSourcePdf()
                true
            }
            R.id.action_export_illustrated -> {
                exportIllustratedPdf()
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }

    private fun exportSourcePdf() {
        Toast.makeText(this, R.string.pdf_exporting, Toast.LENGTH_SHORT).show()
        lifecycleScope.launch {
            try {
                val result = withContext(Dispatchers.IO) {
                    PdfBookExporter.exportEmbeddedSourcePdf(this@CinematicBookActivity)
                }
                PdfBookExporter.showExportActions(this@CinematicBookActivity, result)
            } catch (_: Exception) {
                Toast.makeText(this@CinematicBookActivity, R.string.pdf_failed, Toast.LENGTH_SHORT).show()
            }
        }
    }

    private fun exportIllustratedPdf() {
        Toast.makeText(this, R.string.pdf_exporting, Toast.LENGTH_SHORT).show()
        lifecycleScope.launch {
            try {
                val result = withContext(Dispatchers.IO) {
                    PdfBookExporter.exportUrduIllustratedBook(this@CinematicBookActivity)
                }
                PdfBookExporter.showExportActions(this@CinematicBookActivity, result)
            } catch (_: Exception) {
                Toast.makeText(this@CinematicBookActivity, R.string.pdf_failed, Toast.LENGTH_SHORT).show()
            }
        }
    }

    override fun onSupportNavigateUp(): Boolean {
        onBackPressedDispatcher.onBackPressed()
        return true
    }

    override fun onPause() {
        autoHandler.removeCallbacks(autoAdvanceRunnable)
        CinematicAnimationHelper.stopKenBurns(binding.pageImage)
        super.onPause()
    }

    override fun onResume() {
        super.onResume()
        CinematicAnimationHelper.applyKenBurns(binding.pageImage)
        if (isAutoPlaying) scheduleAutoAdvance()
    }

    override fun onDestroy() {
        autoHandler.removeCallbacks(autoAdvanceRunnable)
        voiceNarrator?.shutdown()
        voiceNarrator = null
        super.onDestroy()
    }
}
