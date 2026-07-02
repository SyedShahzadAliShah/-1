package com.couplesguide.postures

import android.content.Intent
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import androidx.recyclerview.widget.LinearLayoutManager
import com.couplesguide.postures.BuildConfig
import com.couplesguide.postures.databinding.ActivityMainBinding
import com.couplesguide.postures.ui.LessonAdapter
import com.couplesguide.postures.util.AnimatedIllustrationHelper
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.NarrationBuilder
import com.couplesguide.postures.util.PdfExporter
import com.couplesguide.postures.util.RecyclerViewHelper
import com.couplesguide.postures.util.VoiceNarrator
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private val sectionAdapters = mutableMapOf<String, LessonAdapter>()
    private var voiceNarrator: VoiceNarrator? = null
    private var voiceReady = false
    private var isSpeaking = false

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        setSupportActionBar(binding.toolbar)

        voiceNarrator = VoiceNarrator(
            context = this,
            onReadyChanged = { ready -> voiceReady = ready },
            onSpeakingChanged = { speaking ->
                isSpeaking = speaking
                invalidateOptionsMenu()
            },
            onLanguageIssue = { message -> showVoiceMessage(message) }
        )

        setupSections()
        binding.versionBadge.text = getString(R.string.version_badge, BuildConfig.VERSION_NAME)
        AnimatedIllustrationHelper.bind(binding.guideCoverImage, R.drawable.pic_guide_cover)
    }

    private fun setupSections() {
        val container = binding.sectionsContainer
        val inflater = layoutInflater

        for (section in com.couplesguide.postures.data.SexEducationRepository.getSections()) {
            val sectionView = inflater.inflate(R.layout.item_section, container, false)

            sectionView.findViewById<android.widget.TextView>(R.id.sectionTitle).text = section.title
            sectionView.findViewById<android.widget.TextView>(R.id.sectionHint).text = section.hint

            val recycler = sectionView.findViewById<androidx.recyclerview.widget.RecyclerView>(R.id.sectionList)
            val adapter = LessonAdapter { lesson ->
                startActivity(Intent(this, LessonDetailActivity::class.java).apply {
                    putExtra(LessonDetailActivity.EXTRA_LESSON_ID, lesson.id)
                })
            }
            sectionAdapters[section.id] = adapter
            recycler.layoutManager = LinearLayoutManager(this)
            recycler.adapter = adapter
            RecyclerViewHelper.setupNestedList(recycler)
            adapter.submitList(section.lessons)
            recycler.post { recycler.requestLayout() }

            container.addView(sectionView)
        }
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
            R.id.action_listen -> {
                toggleNarration()
                true
            }
            R.id.action_export -> {
                exportFullGuidePdf()
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
        val text = NarrationBuilder.buildFullGuideNarration(this)
        if (voiceNarrator?.speak(text, LocaleHelper.LANG_UR) != true) {
            Toast.makeText(this, R.string.voice_install_prompt, Toast.LENGTH_LONG).show()
        }
    }

    private fun showVoiceMessage(message: String) {
        Toast.makeText(this, message, Toast.LENGTH_LONG).show()
    }

    private fun exportFullGuidePdf() {
        Toast.makeText(this, R.string.pdf_exporting, Toast.LENGTH_SHORT).show()
        lifecycleScope.launch {
            try {
                val result = withContext(Dispatchers.IO) {
                    PdfExporter.exportFullGuide(this@MainActivity)
                }
                PdfExporter.showExportActions(this@MainActivity, result)
            } catch (_: Exception) {
                Toast.makeText(this@MainActivity, R.string.pdf_failed, Toast.LENGTH_SHORT).show()
            }
        }
    }

    override fun onDestroy() {
        voiceNarrator?.shutdown()
        voiceNarrator = null
        super.onDestroy()
    }
}
