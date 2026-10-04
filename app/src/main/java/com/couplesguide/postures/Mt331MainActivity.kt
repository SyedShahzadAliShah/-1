package com.couplesguide.postures

import android.content.Intent
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.couplesguide.postures.data.mt331.Mt331LectureRepository
import com.couplesguide.postures.databinding.ActivityMt331MainBinding
import com.couplesguide.postures.ui.Mt331ChapterAdapter
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.Mt331Narration
import com.couplesguide.postures.util.RecyclerViewHelper
import com.couplesguide.postures.util.VoiceNarrator

class Mt331MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMt331MainBinding
    private lateinit var chapterAdapter: Mt331ChapterAdapter
    private var language = LocaleHelper.LANG_EN
    private var voiceNarrator: VoiceNarrator? = null
    private var voiceReady = false
    private var isSpeaking = false

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMt331MainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        language = LocaleHelper.getLanguage(this)
        setSupportActionBar(binding.toolbar)
        supportActionBar?.title = getString(R.string.mt331_app_title)

        binding.versionBadge.text = getString(
            R.string.mt331_version_badge,
            BuildConfig.VERSION_NAME
        )

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

        chapterAdapter = Mt331ChapterAdapter(language) { chapter ->
            startActivity(Intent(this, LectureCinemaActivity::class.java).apply {
                putExtra(LectureCinemaActivity.EXTRA_CHAPTER_ID, chapter.id)
            })
        }

        binding.chapterRecycler.adapter = chapterAdapter
        RecyclerViewHelper.setupNestedList(binding.chapterRecycler)
        chapterAdapter.submitList(Mt331LectureRepository.getChapters())

        binding.btnListenOverview.setOnClickListener { toggleOverviewNarration() }
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_mt331_main, menu)
        menu.findItem(R.id.action_language)?.title =
            if (language == LocaleHelper.LANG_UR) "EN" else "اردو"
        menu.findItem(R.id.action_legacy_app)?.title = getString(R.string.mt331_open_legacy)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            R.id.action_language -> {
                language = LocaleHelper.toggleLanguage(this)
                recreate()
                true
            }
            R.id.action_legacy_app -> {
                startActivity(Intent(this, MainActivity::class.java))
                true
            }
            R.id.action_tts_settings -> {
                VoiceNarrator.openTtsSettings(this)
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }

    private fun toggleOverviewNarration() {
        if (isSpeaking) {
            voiceNarrator?.stop()
            return
        }
        if (!voiceReady) {
            Toast.makeText(this, R.string.voice_not_ready, Toast.LENGTH_SHORT).show()
            return
        }
        voiceNarrator?.speak(Mt331Narration.buildOverviewNarration(language), language)
    }

    override fun onDestroy() {
        voiceNarrator?.shutdown()
        voiceNarrator = null
        super.onDestroy()
    }
}
