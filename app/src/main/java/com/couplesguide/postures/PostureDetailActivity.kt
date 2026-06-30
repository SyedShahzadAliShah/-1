package com.couplesguide.postures

import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import com.couplesguide.postures.data.Posture
import com.couplesguide.postures.data.PostureRepository
import com.couplesguide.postures.databinding.ActivityPostureDetailBinding
import com.couplesguide.postures.util.AnimatedIllustrationHelper
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.NarrationBuilder
import com.couplesguide.postures.util.PdfExporter
import com.couplesguide.postures.util.VoiceNarrator
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class PostureDetailActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_POSTURE_ID = "posture_id"
    }

    private lateinit var binding: ActivityPostureDetailBinding
    private lateinit var posture: Posture
    private var language = LocaleHelper.LANG_EN
    private var voiceNarrator: VoiceNarrator? = null
    private var voiceReady = false
    private var isSpeaking = false

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityPostureDetailBinding.inflate(layoutInflater)
        setContentView(binding.root)

        language = LocaleHelper.getLanguage(this)
        val postureId = intent.getStringExtra(EXTRA_POSTURE_ID)
        val found = postureId?.let { PostureRepository.getPostureById(it) }

        if (found == null) {
            finish()
            return
        }
        posture = found

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
        val content = posture.content(language)
        supportActionBar?.title = content.name
        AnimatedIllustrationHelper.bind(binding.illustration, posture.illustrationRes)
        binding.postureName.text = content.name
        binding.categoryBadge.text = content.category
        binding.difficultyBadge.text = posture.difficulty.label(language)
        binding.summaryText.text = content.summary
        binding.descriptionText.text = content.description

        val stepsHeader = if (posture.isImagination) {
            getString(R.string.imagination_exercise)
        } else {
            getString(R.string.how_to)
        }
        binding.stepsHeader.text = stepsHeader

        binding.stepsList.text = content.steps
            .mapIndexed { index, step -> "${index + 1}. $step" }
            .joinToString("\n\n")
        binding.tipsList.text = content.tips.joinToString("\n\n") { "• $it" }
        bindPartnerRoles(content)
    }

    private fun bindPartnerRoles(content: com.couplesguide.postures.data.LocalizedContent) {
        val showRoles = !posture.isImagination && content.forMan != null && content.forWoman != null
        val visibility = if (showRoles) android.view.View.VISIBLE else android.view.View.GONE

        binding.manRoleHeader.visibility = visibility
        binding.manPositionLabel.visibility = visibility
        binding.manPositionText.visibility = visibility
        binding.manGuidanceLabel.visibility = visibility
        binding.manGuidanceList.visibility = visibility
        binding.womanRoleHeader.visibility = visibility
        binding.womanPositionLabel.visibility = visibility
        binding.womanPositionText.visibility = visibility
        binding.womanGuidanceLabel.visibility = visibility
        binding.womanGuidanceList.visibility = visibility

        if (!showRoles) return

        binding.manPositionText.text = content.forMan!!.position
        binding.manGuidanceList.text = content.forMan.guidance.joinToString("\n\n") { "• $it" }
        binding.womanPositionText.text = content.forWoman!!.position
        binding.womanGuidanceList.text = content.forWoman.guidance.joinToString("\n\n") { "• $it" }
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
                exportPosturePdf()
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
        voiceNarrator?.speak(
            NarrationBuilder.buildPostureNarration(this, posture, language),
            language
        )
    }

    private fun exportPosturePdf() {
        Toast.makeText(this, R.string.pdf_exporting, Toast.LENGTH_SHORT).show()
        lifecycleScope.launch {
            try {
                val result = withContext(Dispatchers.IO) {
                    PdfExporter.exportPosture(this@PostureDetailActivity, posture, language)
                }
                PdfExporter.showExportActions(this@PostureDetailActivity, result)
            } catch (e: Exception) {
                Toast.makeText(this@PostureDetailActivity, R.string.pdf_failed, Toast.LENGTH_SHORT).show()
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
