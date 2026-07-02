package com.seccap.admissions

import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import androidx.recyclerview.widget.LinearLayoutManager
import com.seccap.admissions.data.GuideRepository
import com.seccap.admissions.databinding.ActivityGuideBinding
import com.seccap.admissions.ui.GuideAdapter
import com.seccap.admissions.util.LocaleHelper
import com.seccap.admissions.util.NarrationBuilder
import com.seccap.admissions.util.PdfExporter
import com.seccap.admissions.util.RecyclerViewHelper
import com.seccap.admissions.util.VoiceNarrator
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class GuideActivity : AppCompatActivity() {

    private lateinit var binding: ActivityGuideBinding
    private var language = LocaleHelper.LANG_EN
    private var voiceNarrator: VoiceNarrator? = null
    private var isSpeaking = false

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityGuideBinding.inflate(layoutInflater)
        setContentView(binding.root)

        language = LocaleHelper.getLanguage(this)
        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)

        voiceNarrator = VoiceNarrator(
            context = this,
            onReadyChanged = { },
            onSpeakingChanged = { speaking ->
                isSpeaking = speaking
                invalidateOptionsMenu()
            },
            onLanguageIssue = { msg -> Toast.makeText(this, msg, Toast.LENGTH_SHORT).show() }
        )

        val adapter = GuideAdapter(language) { section ->
            voiceNarrator?.speak(NarrationBuilder.guideSection(language, section.id), language)
        }

        binding.guideList.layoutManager = LinearLayoutManager(this)
        binding.guideList.adapter = adapter
        RecyclerViewHelper.setupNestedList(binding.guideList)
        adapter.submitList(GuideRepository.getSections())
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_detail, menu)
        menu.findItem(R.id.action_listen)?.title =
            if (isSpeaking) getString(R.string.stop) else getString(R.string.listen_full_guide)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean = when (item.itemId) {
        android.R.id.home -> { finish(); true }
        R.id.action_listen -> {
            if (isSpeaking) voiceNarrator?.stop()
            else voiceNarrator?.speak(NarrationBuilder.fullGuide(language), language)
            true
        }
        R.id.action_export_pdf -> {
            exportGuide()
            true
        }
        else -> super.onOptionsItemSelected(item)
    }

    private fun exportGuide() {
        Toast.makeText(this, R.string.pdf_exporting, Toast.LENGTH_SHORT).show()
        lifecycleScope.launch {
            try {
                val result = withContext(Dispatchers.IO) {
                    PdfExporter.exportGuide(this@GuideActivity, language)
                }
                PdfExporter.showExportActions(this@GuideActivity, result)
            } catch (e: Exception) {
                Toast.makeText(this@GuideActivity, R.string.pdf_failed, Toast.LENGTH_SHORT).show()
            }
        }
    }

    override fun onDestroy() {
        voiceNarrator?.shutdown()
        super.onDestroy()
    }
}
