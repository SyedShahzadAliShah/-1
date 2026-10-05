package com.couplesguide.postures

import android.content.Intent
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import androidx.recyclerview.widget.LinearLayoutManager
import com.couplesguide.postures.BuildConfig
import com.couplesguide.postures.data.LectureNotesRepository
import com.couplesguide.postures.databinding.ActivityMainBinding
import com.couplesguide.postures.ui.StudyChapterAdapter
import com.couplesguide.postures.util.AnimatedIllustrationHelper
import com.couplesguide.postures.util.LectureEmbedTtsEngine
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.NarrationBuilder
import com.couplesguide.postures.util.PdfExporter
import com.couplesguide.postures.util.StudyGuidePdfExporter
import com.couplesguide.postures.util.RecyclerViewHelper
import com.couplesguide.postures.util.NarrativeLanguageDialog
import com.couplesguide.postures.util.NarrativeLanguageHelper
import com.couplesguide.postures.util.NarrativeLanguageUi
import com.couplesguide.postures.util.TtsPlaybackHelper
import com.couplesguide.postures.util.VoiceNarrator
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private lateinit var xiAdapter: StudyChapterAdapter
    private lateinit var xiiAdapter: StudyChapterAdapter
    private var language = LocaleHelper.LANG_EN
    private var voiceNarrator: VoiceNarrator? = null
    private var voiceReady = false
    private var isSpeaking = false
    private var embedTtsSession: LectureEmbedTtsEngine.Session? = null

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        language = LocaleHelper.getLanguage(this)
        setSupportActionBar(binding.toolbar)
        supportActionBar?.title = getString(R.string.app_name)

        LectureNotesRepository.ensureLoaded(this)

        voiceNarrator = VoiceNarrator(
            context = this,
            onReadyChanged = { ready -> voiceReady = ready },
            onSpeakingChanged = { speaking ->
                isSpeaking = speaking
                invalidateOptionsMenu()
            },
            onLanguageIssue = { message -> showVoiceMessage(message) }
        )
        voiceNarrator?.let { embedTtsSession = LectureEmbedTtsEngine.Session(it) }

        xiAdapter = StudyChapterAdapter(language) { chapter ->
            openChapter(chapter.id)
        }
        xiiAdapter = StudyChapterAdapter(language) { chapter ->
            openChapter(chapter.id)
        }

        RecyclerViewHelper.setupNestedList(binding.xiChapterList)
        binding.xiChapterList.layoutManager = LinearLayoutManager(this)
        binding.xiChapterList.adapter = xiAdapter
        xiAdapter.submitList(LectureNotesRepository.getChaptersForClass(this, "xi"))

        RecyclerViewHelper.setupNestedList(binding.xiiChapterList)
        binding.xiiChapterList.layoutManager = LinearLayoutManager(this)
        binding.xiiChapterList.adapter = xiiAdapter
        xiiAdapter.submitList(LectureNotesRepository.getChaptersForClass(this, "xii"))

        binding.btnXiCinematic.setOnClickListener { openFullCinematic("xi") }
        binding.btnXiiCinematic.setOnClickListener { openFullCinematic("xii") }
        binding.btnListenXiPdf.setOnClickListener { startFullPdfTts("xi") }
        binding.btnListenXiiPdf.setOnClickListener { startFullPdfTts("xii") }
        binding.btnTeachingStudio.setOnClickListener { openTeachingStudio() }
        binding.btnAiTutor.setOnClickListener { openAiTutor() }

        binding.versionBadge.text = getString(R.string.version_badge, BuildConfig.VERSION_NAME)
        AnimatedIllustrationHelper.bind(binding.guideCoverImage, R.drawable.pic_cs_xi_ch1)

        NarrativeLanguageUi.bindToggleGroup(
            binding.narrativeToggleGroup,
            binding.btnNarrativeEn,
            binding.btnNarrativeUr
        ) {
            NarrativeLanguageUi.updateBadge(binding.narrativeModeBadge, this)
        }
        NarrativeLanguageUi.updateBadge(binding.narrativeModeBadge, this)
    }

    private fun openChapter(chapterId: String) {
        startActivity(Intent(this, StudyChapterDetailActivity::class.java).apply {
            putExtra(StudyChapterDetailActivity.EXTRA_CHAPTER_ID, chapterId)
        })
    }

    private fun startFullPdfTts(classId: String) {
        if (isSpeaking) {
            embedTtsSession?.stop()
            voiceNarrator?.stop()
            return
        }
        if (!voiceReady) {
            Toast.makeText(this, R.string.voice_not_ready, Toast.LENGTH_SHORT).show()
            return
        }
        Toast.makeText(this, R.string.full_pdf_tts_stop_hint, Toast.LENGTH_LONG).show()
        embedTtsSession?.readEntireClass(
            context = this,
            classId = classId,
            onPageStarted = { page, total ->
                Toast.makeText(
                    this,
                    getString(R.string.full_pdf_tts_progress, page, total),
                    Toast.LENGTH_SHORT
                ).show()
            },
            onFinished = {
                Toast.makeText(this, R.string.full_pdf_tts_done, Toast.LENGTH_LONG).show()
            }
        )
    }

    private fun openTeachingStudio() {
        startActivity(Intent(this, TeachingStudioActivity::class.java))
    }

    private fun openAiTutor() {
        startActivity(Intent(this, AiTutorActivity::class.java))
    }

    private fun openFullCinematic(classId: String) {
        val studyClass = LectureNotesRepository.getClassById(this, classId) ?: return
        startActivity(Intent(this, LectureCinematicActivity::class.java).apply {
            putExtra(LectureCinematicActivity.EXTRA_CLASS_ID, classId)
            putExtra(LectureCinematicActivity.EXTRA_START_PAGE, 1)
            putExtra(LectureCinematicActivity.EXTRA_END_PAGE, studyClass.totalPages)
            putExtra(LectureCinematicActivity.EXTRA_AUTO_PLAY, true)
        })
    }

    override fun onResume() {
        super.onResume()
        AnimatedIllustrationHelper.start(binding.guideCoverImage)
    }

    override fun onPause() {
        AnimatedIllustrationHelper.stop(binding.guideCoverImage)
        super.onPause()
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_main, menu)
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
            R.id.action_narrative_language -> {
                NarrativeLanguageDialog.show(this) {
                    NarrativeLanguageUi.updateBadge(binding.narrativeModeBadge, this)
                    binding.narrativeToggleGroup.check(
                        if (NarrativeLanguageHelper.getMode(this) == NarrativeLanguageHelper.MODE_UR) {
                            binding.btnNarrativeUr.id
                        } else {
                            binding.btnNarrativeEn.id
                        }
                    )
                }
                true
            }
            R.id.action_language -> {
                showLanguageDialog()
                true
            }
            R.id.action_listen -> {
                toggleNarration()
                true
            }
            R.id.action_export -> {
                exportStudyGuidePdf()
                true
            }
            R.id.action_teaching_studio -> {
                openTeachingStudio()
                true
            }
            R.id.action_ai_tutor -> {
                openAiTutor()
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }

    private fun showLanguageDialog() {
        val options = arrayOf(getString(R.string.english), getString(R.string.urdu))
        val current = if (language == LocaleHelper.LANG_UR) 1 else 0
        AlertDialog.Builder(this)
            .setTitle(R.string.language)
            .setSingleChoiceItems(options, current) { dialog, which ->
                val newLang = if (which == 1) LocaleHelper.LANG_UR else LocaleHelper.LANG_EN
                if (newLang != language) {
                    LocaleHelper.setLanguage(this, newLang)
                    recreate()
                }
                dialog.dismiss()
            }
            .show()
    }

    private fun toggleNarration() {
        if (isSpeaking) {
            embedTtsSession?.stop()
            voiceNarrator?.stop()
            return
        }
        if (!voiceReady) {
            Toast.makeText(this, R.string.voice_not_ready, Toast.LENGTH_SHORT).show()
            return
        }
        val segments = NarrationBuilder.buildMainGuideNarrationSegments(this)
        if (voiceNarrator?.speakSegments(segments) != true) {
            TtsPlaybackHelper.showPlaybackFailedDialog(this)
        }
    }

    private fun showVoiceMessage(message: String) {
        Toast.makeText(this, message, Toast.LENGTH_LONG).show()
    }

    private fun exportStudyGuidePdf() {
        Toast.makeText(this, R.string.pdf_exporting, Toast.LENGTH_SHORT).show()
        lifecycleScope.launch {
            try {
                val result = withContext(Dispatchers.IO) {
                    StudyGuidePdfExporter.exportSummary(this@MainActivity, language)
                }
                PdfExporter.showExportActions(this@MainActivity, result)
            } catch (_: Exception) {
                Toast.makeText(this@MainActivity, R.string.pdf_failed, Toast.LENGTH_SHORT).show()
            }
        }
    }

    override fun onDestroy() {
        embedTtsSession?.stop()
        voiceNarrator?.shutdown()
        voiceNarrator = null
        super.onDestroy()
    }
}
