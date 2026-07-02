package com.seccap.admissions

import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import androidx.viewpager2.widget.ViewPager2
import com.google.android.material.tabs.TabLayoutMediator
import com.seccap.admissions.data.ApplicationDraft
import com.seccap.admissions.data.DraftRepository
import com.seccap.admissions.databinding.ActivityWizardBinding
import com.seccap.admissions.ui.WizardPagerAdapter
import com.seccap.admissions.ui.wizard.CollegesFragment
import com.seccap.admissions.ui.wizard.DocumentsFragment
import com.seccap.admissions.ui.wizard.EducationalFragment
import com.seccap.admissions.ui.wizard.PersonalFragment
import com.seccap.admissions.ui.wizard.ReviewFragment
import com.seccap.admissions.util.LocaleHelper
import com.seccap.admissions.util.NarrationBuilder
import com.seccap.admissions.util.PdfExporter
import com.seccap.admissions.util.VoiceNarrator
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class ApplicationWizardActivity : AppCompatActivity() {

    private lateinit var binding: ActivityWizardBinding
    lateinit var draft: ApplicationDraft
    var language = LocaleHelper.LANG_EN
    private var voiceNarrator: VoiceNarrator? = null
    private var isSpeaking = false
    private var voiceReady = false

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityWizardBinding.inflate(layoutInflater)
        setContentView(binding.root)

        language = LocaleHelper.getLanguage(this)
        draft = DraftRepository.load(this)
        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)

        voiceNarrator = VoiceNarrator(
            context = this,
            onReadyChanged = { ready -> voiceReady = ready },
            onSpeakingChanged = { speaking ->
                isSpeaking = speaking
                invalidateOptionsMenu()
            },
            onLanguageIssue = { msg -> Toast.makeText(this, msg, Toast.LENGTH_SHORT).show() }
        )

        val adapter = WizardPagerAdapter(this)
        binding.viewPager.adapter = adapter
        binding.viewPager.isUserInputEnabled = false

        val stepTitles = listOf(
            getString(R.string.step_educational),
            getString(R.string.step_personal),
            getString(R.string.step_faculty),
            getString(R.string.step_colleges),
            getString(R.string.step_documents),
            getString(R.string.step_review)
        )
        TabLayoutMediator(binding.tabLayout, binding.viewPager) { tab, pos ->
            tab.text = "${pos + 1}"
            tab.contentDescription = stepTitles[pos]
        }.attach()

        binding.btnBack.setOnClickListener {
            val current = binding.viewPager.currentItem
            if (current > 0) {
                saveCurrentStep(current)
                binding.viewPager.currentItem = current - 1
            }
        }

        binding.btnNext.setOnClickListener {
            val current = binding.viewPager.currentItem
            saveCurrentStep(current)
            DraftRepository.save(this, draft)
            if (current < 5) {
                binding.viewPager.currentItem = current + 1
                if (current + 1 == 5) {
                    refreshReview()
                }
            }
        }

        binding.viewPager.registerOnPageChangeCallback(object : ViewPager2.OnPageChangeCallback() {
            override fun onPageSelected(position: Int) {
                binding.btnBack.visibility = if (position == 0) android.view.View.GONE else android.view.View.VISIBLE
                binding.btnNext.text = if (position == 5) getString(R.string.done) else getString(R.string.next)
                binding.stepTitle.text = stepTitles[position]
                speakCurrentStep(position)
            }
        })

        binding.stepTitle.text = stepTitles[0]
        speakCurrentStep(0)
    }

    private fun saveCurrentStep(position: Int) {
        val fragment = supportFragmentManager.findFragmentByTag("f$position")
        when (fragment) {
            is EducationalFragment -> fragment.saveToDraft(this)
            is PersonalFragment -> fragment.saveToDraft(this)
            is CollegesFragment -> fragment.saveToDraft(this)
            is DocumentsFragment -> fragment.saveToDraft(this)
        }
        DraftRepository.save(this, draft)
    }

    private fun refreshReview() {
        val fragment = supportFragmentManager.findFragmentByTag("f5") as? ReviewFragment
        fragment?.refresh()
    }

    private fun speakCurrentStep(position: Int) {
        val text = when (position) {
            0 -> NarrationBuilder.stepEducational(language)
            1 -> NarrationBuilder.stepPersonal(language)
            2 -> NarrationBuilder.stepFaculty(language, draft)
            3 -> NarrationBuilder.stepColleges(language)
            4 -> NarrationBuilder.stepDocuments(language)
            5 -> NarrationBuilder.stepReview(this, language, draft)
            else -> ""
        }
        voiceNarrator?.speak(text, language)
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_wizard, menu)
        menu.findItem(R.id.action_listen)?.title =
            if (isSpeaking) getString(R.string.stop) else getString(R.string.listen)
        menu.findItem(R.id.action_export_pdf)?.isVisible = binding.viewPager.currentItem == 5
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean = when (item.itemId) {
        android.R.id.home -> { finish(); true }
        R.id.action_listen -> {
            if (isSpeaking) voiceNarrator?.stop()
            else speakCurrentStep(binding.viewPager.currentItem)
            true
        }
        R.id.action_export_pdf -> {
            saveCurrentStep(binding.viewPager.currentItem)
            exportPdf()
            true
        }
        else -> super.onOptionsItemSelected(item)
    }

    private fun exportPdf() {
        Toast.makeText(this, R.string.pdf_exporting, Toast.LENGTH_SHORT).show()
        lifecycleScope.launch {
            try {
                val result = withContext(Dispatchers.IO) {
                    PdfExporter.exportApplication(this@ApplicationWizardActivity, draft, language)
                }
                PdfExporter.showExportActions(this@ApplicationWizardActivity, result)
            } catch (e: Exception) {
                Toast.makeText(this@ApplicationWizardActivity, R.string.pdf_failed, Toast.LENGTH_SHORT).show()
            }
        }
    }

    override fun onDestroy() {
        voiceNarrator?.shutdown()
        super.onDestroy()
    }
}
