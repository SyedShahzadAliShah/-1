package com.seccap.admissions

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import com.seccap.admissions.data.DraftRepository
import com.seccap.admissions.databinding.ActivityMainBinding
import com.seccap.admissions.util.LocaleHelper
import com.seccap.admissions.util.NarrationBuilder
import com.seccap.admissions.util.PdfExporter
import com.seccap.admissions.util.VoiceNarrator
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private var language = LocaleHelper.LANG_EN
    private var voiceNarrator: VoiceNarrator? = null
    private var isSpeaking = false

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        language = LocaleHelper.getLanguage(this)
        setSupportActionBar(binding.toolbar)

        voiceNarrator = VoiceNarrator(
            context = this,
            onReadyChanged = { },
            onSpeakingChanged = { speaking ->
                isSpeaking = speaking
                invalidateOptionsMenu()
            },
            onLanguageIssue = { msg -> Toast.makeText(this, msg, Toast.LENGTH_SHORT).show() }
        )

        updateDraftStatus()

        binding.cardNewApplication.setOnClickListener {
            DraftRepository.clear(this)
            startActivity(Intent(this, ApplicationWizardActivity::class.java))
        }

        binding.cardContinueDraft.setOnClickListener {
            startActivity(Intent(this, ApplicationWizardActivity::class.java))
        }

        binding.cardGuide.setOnClickListener {
            startActivity(Intent(this, GuideActivity::class.java))
        }

        binding.cardColleges.setOnClickListener {
            startActivity(Intent(this, CollegeBrowserActivity::class.java))
        }

        binding.cardExportGuide.setOnClickListener {
            exportGuidePdf()
        }

        binding.cardOfficialPortal.setOnClickListener {
            val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://seccap.dgcs.gos.pk"))
            startActivity(intent)
        }

        binding.versionBadge.text = getString(R.string.version_badge, BuildConfig.VERSION_NAME)
    }

    override fun onResume() {
        super.onResume()
        updateDraftStatus()
    }

    private fun updateDraftStatus() {
        val hasDraft = DraftRepository.hasDraft(this)
        binding.cardContinueDraft.alpha = if (hasDraft) 1f else 0.5f
        binding.cardContinueDraft.isEnabled = hasDraft
        if (hasDraft) {
            val draft = DraftRepository.load(this)
            binding.draftStatus.text = getString(R.string.draft_status, draft.completionPercent())
        } else {
            binding.draftStatus.text = getString(R.string.no_draft)
        }
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_main, menu)
        menu.findItem(R.id.action_listen)?.title =
            if (isSpeaking) getString(R.string.stop) else getString(R.string.listen)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean = when (item.itemId) {
        R.id.action_listen -> {
            if (isSpeaking) voiceNarrator?.stop()
            else voiceNarrator?.speak(NarrationBuilder.welcome(this, language), language)
            true
        }
        R.id.action_language -> {
            showLanguageDialog()
            true
        }
        R.id.action_export_pdf -> {
            val draft = DraftRepository.load(this)
            if (draft.completionPercent() > 0) exportApplicationPdf()
            else exportGuidePdf()
            true
        }
        else -> super.onOptionsItemSelected(item)
    }

    private fun showLanguageDialog() {
        val options = arrayOf(getString(R.string.english), getString(R.string.urdu))
        AlertDialog.Builder(this)
            .setTitle(R.string.language)
            .setItems(options) { _, which ->
                val newLang = if (which == 1) LocaleHelper.LANG_UR else LocaleHelper.LANG_EN
                if (newLang != language) {
                    LocaleHelper.setLanguage(this, newLang)
                    recreate()
                }
            }
            .show()
    }

    private fun exportApplicationPdf() {
        val draft = DraftRepository.load(this)
        Toast.makeText(this, R.string.pdf_exporting, Toast.LENGTH_SHORT).show()
        lifecycleScope.launch {
            try {
                val result = withContext(Dispatchers.IO) {
                    PdfExporter.exportApplication(this@MainActivity, draft, language)
                }
                PdfExporter.showExportActions(this@MainActivity, result)
            } catch (e: Exception) {
                Toast.makeText(this@MainActivity, R.string.pdf_failed, Toast.LENGTH_SHORT).show()
            }
        }
    }

    private fun exportGuidePdf() {
        Toast.makeText(this, R.string.pdf_exporting, Toast.LENGTH_SHORT).show()
        lifecycleScope.launch {
            try {
                val result = withContext(Dispatchers.IO) {
                    PdfExporter.exportGuide(this@MainActivity, language)
                }
                PdfExporter.showExportActions(this@MainActivity, result)
            } catch (e: Exception) {
                Toast.makeText(this@MainActivity, R.string.pdf_failed, Toast.LENGTH_SHORT).show()
            }
        }
    }

    override fun onDestroy() {
        voiceNarrator?.shutdown()
        super.onDestroy()
    }
}
