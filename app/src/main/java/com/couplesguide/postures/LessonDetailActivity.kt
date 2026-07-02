package com.couplesguide.postures

import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import com.couplesguide.postures.data.SexEdLesson
import com.couplesguide.postures.data.SexEducationRepository
import com.couplesguide.postures.databinding.ActivityChapterDetailBinding
import com.couplesguide.postures.util.AnimatedIllustrationHelper
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.NarrationBuilder
import com.couplesguide.postures.util.PdfExporter
import com.couplesguide.postures.util.VoiceNarrator
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class LessonDetailActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_LESSON_ID = "lesson_id"
    }

    private lateinit var binding: ActivityChapterDetailBinding
    private lateinit var lesson: SexEdLesson
    private var voiceNarrator: VoiceNarrator? = null
    private var voiceReady = false
    private var isSpeaking = false

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityChapterDetailBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val lessonId = intent.getStringExtra(EXTRA_LESSON_ID)
        val found = lessonId?.let { SexEducationRepository.getLessonById(it) }

        if (found == null) {
            finish()
            return
        }
        lesson = found

        voiceNarrator = VoiceNarrator(
            context = this,
            onReadyChanged = { ready -> voiceReady = ready },
            onSpeakingChanged = { speaking ->
                isSpeaking = speaking
                invalidateOptionsMenu()
            },
            onLanguageIssue = { message ->
                Toast.makeText(this, message, Toast.LENGTH_LONG).show()
            }
        )

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        bindContent()
    }

    override fun onResume() {
        super.onResume()
        AnimatedIllustrationHelper.start(binding.illustration)
    }

    override fun onPause() {
        AnimatedIllustrationHelper.stop(binding.illustration)
        super.onPause()
    }

    private fun bindContent() {
        supportActionBar?.title = lesson.title
        AnimatedIllustrationHelper.bind(binding.illustration, lesson.illustrationRes)
        binding.chapterTitle.text = lesson.title
        binding.chapterSummary.text = lesson.summary
        binding.chapterBody.text = lesson.body
        binding.keyPointsList.text = lesson.keyPoints.joinToString("\n\n") { "• $it" }
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_detail, menu)
        val listenItem = menu.findItem(R.id.action_listen)
        listenItem.title = if (isSpeaking) getString(R.string.stop) else getString(R.string.listen)
        listenItem.setIcon(
            if (isSpeaking) android.R.drawable.ic_media_pause
            else android.R.drawable.ic_media_play
        )
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            R.id.action_listen -> {
                toggleNarration()
                true
            }
            R.id.action_export -> {
                exportLessonPdf()
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
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
        voiceNarrator?.speak(NarrationBuilder.buildLessonNarration(lesson), LocaleHelper.LANG_UR)
    }

    private fun exportLessonPdf() {
        Toast.makeText(this, R.string.pdf_exporting, Toast.LENGTH_SHORT).show()
        lifecycleScope.launch {
            try {
                val result = withContext(Dispatchers.IO) {
                    PdfExporter.exportLesson(this@LessonDetailActivity, lesson)
                }
                PdfExporter.showExportActions(this@LessonDetailActivity, result)
            } catch (_: Exception) {
                Toast.makeText(this@LessonDetailActivity, R.string.pdf_failed, Toast.LENGTH_SHORT).show()
            }
        }
    }

    override fun onSupportNavigateUp(): Boolean {
        onBackPressedDispatcher.onBackPressed()
        return true
    }

    override fun onDestroy() {
        voiceNarrator?.shutdown()
        voiceNarrator = null
        super.onDestroy()
    }
}
