package com.couplesguide.postures

import android.content.Intent
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.couplesguide.postures.data.LectureNotesRepository
import com.couplesguide.postures.data.StudyChapter
import com.couplesguide.postures.databinding.ActivityStudyChapterDetailBinding
import com.couplesguide.postures.util.AnimatedIllustrationHelper
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.NarrativeLanguageDialog
import com.couplesguide.postures.util.NarrationBuilder
import com.couplesguide.postures.util.TtsPlaybackHelper
import com.couplesguide.postures.util.VoiceNarrator

class StudyChapterDetailActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_CHAPTER_ID = "study_chapter_id"
    }

    private lateinit var binding: ActivityStudyChapterDetailBinding
    private lateinit var chapter: StudyChapter
    private var language = LocaleHelper.LANG_EN
    private var voiceNarrator: VoiceNarrator? = null
    private var voiceReady = false
    private var isSpeaking = false

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityStudyChapterDetailBinding.inflate(layoutInflater)
        setContentView(binding.root)

        language = LocaleHelper.getLanguage(this)
        val chapterId = intent.getStringExtra(EXTRA_CHAPTER_ID)
        val found = chapterId?.let { LectureNotesRepository.getChapterById(this, it) }
        if (found == null) {
            finish()
            return
        }
        chapter = found

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

        binding.btnCinematic.setOnClickListener {
            startActivity(
                Intent(this, LectureCinematicActivity::class.java).apply {
                    putExtra(LectureCinematicActivity.EXTRA_CLASS_ID, chapter.id.substringBefore("_ch"))
                    putExtra(LectureCinematicActivity.EXTRA_START_PAGE, chapter.pdfPageStart)
                    putExtra(LectureCinematicActivity.EXTRA_END_PAGE, chapter.pdfPageEnd)
                    putExtra(LectureCinematicActivity.EXTRA_AUTO_PLAY, true)
                }
            )
        }
        binding.btnAiTutor.setOnClickListener {
            startActivity(
                Intent(this, AiTutorActivity::class.java).apply {
                    putExtra(AiTutorActivity.EXTRA_CHAPTER_ID, chapter.id)
                    putExtra(AiTutorActivity.EXTRA_CLASS_ID, chapter.id.substringBefore("_ch"))
                    putExtra(AiTutorActivity.EXTRA_PAGE, chapter.pdfPageStart)
                }
            )
        }
    }

    private fun bindContent() {
        val en = chapter.english
        val ur = chapter.urdu
        supportActionBar?.title = if (language == LocaleHelper.LANG_UR) ur.title else en.title
        AnimatedIllustrationHelper.bind(binding.illustration, chapter.illustrationRes)

        binding.chapterTitleEn.text = en.title
        binding.chapterSummaryEn.text = en.summary
        binding.chapterBodyEn.text = en.body
        binding.keyPointsEn.text = en.keyPoints.joinToString("\n\n") { "• $it" }

        binding.chapterTitleUr.text = ur.title
        binding.chapterSummaryUr.text = ur.summary
        binding.chapterBodyUr.text = ur.body
        binding.keyPointsUr.text = ur.keyPoints.joinToString("\n\n") { "• $it" }
    }

    override fun onResume() {
        super.onResume()
        AnimatedIllustrationHelper.start(binding.illustration)
    }

    override fun onPause() {
        AnimatedIllustrationHelper.stop(binding.illustration)
        super.onPause()
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_detail, menu)
        menu.findItem(R.id.action_export)?.isVisible = false
        val listenItem = menu.findItem(R.id.action_listen)
        listenItem.title = if (isSpeaking) getString(R.string.stop) else getString(R.string.listen)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        when (item.itemId) {
            R.id.action_narrative_language -> {
                NarrativeLanguageDialog.show(this)
                return true
            }
            R.id.action_listen -> {
                toggleNarration()
                return true
            }
        }
        return super.onOptionsItemSelected(item)
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
        if (voiceNarrator?.speakSegments(
                NarrationBuilder.buildStudyChapterNarrationSegments(this, chapter)
            ) != true
        ) {
            TtsPlaybackHelper.showPlaybackFailedDialog(this)
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
