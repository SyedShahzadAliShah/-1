package com.couplesguide.postures

import android.graphics.Bitmap
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.couplesguide.postures.data.LectureNotesRepository
import com.couplesguide.postures.data.LecturePageIndex
import com.couplesguide.postures.databinding.ActivityLectureCinematicBinding
import com.couplesguide.postures.util.CinematicAnimationHelper
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.PdfAssetRenderer
import com.couplesguide.postures.util.VoiceNarrator

class LectureCinematicActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_CLASS_ID = "class_id"
        const val EXTRA_START_PAGE = "start_page"
        const val EXTRA_END_PAGE = "end_page"
        const val EXTRA_AUTO_PLAY = "auto_play"
        private const val AUTO_ADVANCE_DELAY_MS = 14000L
    }

    private lateinit var binding: ActivityLectureCinematicBinding
    private var pdfRenderer: PdfAssetRenderer? = null
    private var currentPdfPage = 1
    private var startPage = 1
    private var endPage = 1
    private var classId = "xi"
    private var pageIndexAsset = "lecture_notes/cs_xi_pages.json"
    private var language = LocaleHelper.LANG_EN
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
        binding = ActivityLectureCinematicBinding.inflate(layoutInflater)
        setContentView(binding.root)

        language = LocaleHelper.getLanguage(this)
        classId = intent.getStringExtra(EXTRA_CLASS_ID) ?: "xi"
        val studyClass = LectureNotesRepository.getClassById(this, classId)
        if (studyClass == null) {
            finish()
            return
        }

        startPage = intent.getIntExtra(EXTRA_START_PAGE, 1).coerceAtLeast(1)
        endPage = intent.getIntExtra(EXTRA_END_PAGE, studyClass.totalPages)
            .coerceIn(startPage, studyClass.totalPages)
        currentPdfPage = startPage.coerceIn(startPage, endPage)
        isAutoPlaying = intent.getBooleanExtra(EXTRA_AUTO_PLAY, false)
        pageIndexAsset = studyClass.pageIndexAsset

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = getString(R.string.cinematic_lecture_title, studyClass.gradeLabel)

        try {
            pdfRenderer = PdfAssetRenderer.open(this, studyClass.pdfAsset)
        } catch (e: Exception) {
            Toast.makeText(this, R.string.pdf_failed, Toast.LENGTH_LONG).show()
            finish()
            return
        }

        voiceNarrator = VoiceNarrator(
            context = this,
            onReadyChanged = { ready -> voiceReady = ready },
            onSpeakingChanged = { speaking ->
                isSpeaking = speaking
                updatePlayPauseLabel()
                invalidateOptionsMenu()
            },
            onLanguageIssue = { message -> Toast.makeText(this, message, Toast.LENGTH_LONG).show() }
        )

        binding.btnPrev.setOnClickListener {
            stopAutoPlay()
            showPage(currentPdfPage - 1)
        }
        binding.btnNext.setOnClickListener {
            stopAutoPlay()
            showPage(currentPdfPage + 1)
        }
        binding.btnPlayPause.setOnClickListener { toggleAutoPlay() }

        showPage(currentPdfPage, animate = false)
        if (isAutoPlaying) startAutoPlay()
    }

    private fun showPage(pageNumber: Int, animate: Boolean = true) {
        val renderer = pdfRenderer ?: return
        currentPdfPage = pageNumber.coerceIn(startPage, endPage)

        voiceNarrator?.stop()
        autoHandler.removeCallbacks(autoAdvanceRunnable)

        val bindPage = {
            val pageText = LecturePageIndex.getPage(this, pageIndexAsset, currentPdfPage)
            val title = if (language == LocaleHelper.LANG_UR) {
                pageText?.urdu?.take(80)?.ifBlank { getString(R.string.cinematic_page_fallback_title) }
                    ?: getString(R.string.cinematic_page_fallback_title)
            } else {
                getString(R.string.cinematic_page_title_en, currentPdfPage)
            }
            binding.pageTitle.text = title
            binding.pageNarration.text = LecturePageIndex.narrationForPage(
                this,
                pageIndexAsset,
                currentPdfPage,
                language
            ).ifBlank { getString(R.string.cinematic_page_fallback_narration) }

            binding.pageIndicator.text = getString(
                R.string.cinematic_page_indicator,
                currentPdfPage - startPage + 1,
                endPage - startPage + 1
            )
            binding.pageProgress.max = endPage - startPage + 1
            binding.pageProgress.progress = currentPdfPage - startPage + 1

            val bitmap = renderer.renderPage(currentPdfPage - 1)
            binding.pageImage.setImageBitmap(bitmap)
            CinematicAnimationHelper.applyKenBurns(binding.pageImage)

            binding.btnPrev.isEnabled = currentPdfPage > startPage
            binding.btnNext.isEnabled = currentPdfPage < endPage

            if (isAutoPlaying && voiceReady) speakCurrentPage()
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

    private fun speakCurrentPage() {
        val text = LecturePageIndex.narrationForPage(this, pageIndexAsset, currentPdfPage, language)
        if (text.isNotBlank()) {
            voiceNarrator?.speak(text, language)
        }
    }

    private fun scheduleAutoAdvance() {
        if (!isAutoPlaying) return
        autoHandler.removeCallbacks(autoAdvanceRunnable)
        autoHandler.postDelayed(autoAdvanceRunnable, AUTO_ADVANCE_DELAY_MS)
    }

    private fun advanceAutoPlay() {
        if (!isAutoPlaying) return
        if (currentPdfPage >= endPage) {
            stopAutoPlay()
            return
        }
        showPage(currentPdfPage + 1)
    }

    private fun toggleAutoPlay() {
        if (isAutoPlaying) stopAutoPlay() else startAutoPlay()
    }

    private fun startAutoPlay() {
        isAutoPlaying = true
        updatePlayPauseLabel()
        if (voiceReady) speakCurrentPage()
        scheduleAutoAdvance()
    }

    private fun stopAutoPlay() {
        isAutoPlaying = false
        autoHandler.removeCallbacks(autoAdvanceRunnable)
        voiceNarrator?.stop()
        updatePlayPauseLabel()
    }

    private fun updatePlayPauseLabel() {
        binding.btnPlayPause.text = if (isAutoPlaying) {
            getString(R.string.cinematic_pause)
        } else {
            getString(R.string.cinematic_play)
        }
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_detail, menu)
        menu.findItem(R.id.action_export)?.isVisible = false
        val listenItem = menu.findItem(R.id.action_listen)
        listenItem.title = if (isSpeaking) getString(R.string.stop) else getString(R.string.listen)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        if (item.itemId == R.id.action_listen) {
            if (isSpeaking) voiceNarrator?.stop()
            else speakCurrentPage()
            return true
        }
        return super.onOptionsItemSelected(item)
    }

    override fun onDestroy() {
        stopAutoPlay()
        CinematicAnimationHelper.stopKenBurns(binding.pageImage)
        voiceNarrator?.shutdown()
        voiceNarrator = null
        pdfRenderer?.close()
        pdfRenderer = null
        super.onDestroy()
    }

    override fun onSupportNavigateUp(): Boolean {
        onBackPressedDispatcher.onBackPressed()
        return true
    }
}
