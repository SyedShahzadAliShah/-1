package com.couplesguide.postures

import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import com.couplesguide.postures.data.Recipe
import com.couplesguide.postures.data.RecipeRepository
import com.couplesguide.postures.databinding.ActivityPostureDetailBinding
import com.couplesguide.postures.util.AnimatedIllustrationHelper
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.NarrationBuilder
import com.couplesguide.postures.util.PdfExporter
import com.couplesguide.postures.util.VoiceNarrator
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class RecipeDetailActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_RECIPE_ID = "recipe_id"
    }

    private lateinit var binding: ActivityPostureDetailBinding
    private lateinit var recipe: Recipe
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
        val recipeId = intent.getStringExtra(EXTRA_RECIPE_ID)
        val found = recipeId?.let { RecipeRepository.getRecipeById(it) }

        if (found == null) {
            finish()
            return
        }
        recipe = found

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
        val content = recipe.content(language)
        supportActionBar?.title = content.name
        AnimatedIllustrationHelper.bind(binding.illustration, recipe.illustrationRes)
        binding.postureName.text = content.name
        binding.categoryBadge.text = content.category
        binding.difficultyBadge.text = recipe.difficulty.label(language)
        binding.summaryText.text = content.summary
        binding.descriptionText.text = content.description

        binding.stepsHeader.text = getString(R.string.how_to)

        val timeInfo = if (language == LocaleHelper.LANG_UR) {
            "تیاری: ${recipe.prepMinutes} منٹ  |  پکانا: ${recipe.cookMinutes} منٹ  |  ${recipe.servings} افرد"
        } else {
            "Prep: ${recipe.prepMinutes} min  |  Cook: ${recipe.cookMinutes} min  |  Serves ${recipe.servings}"
        }

        binding.stepsList.text = buildString {
            append(timeInfo)
            append("\n\n")
            append(getString(R.string.ingredients))
            append("\n")
            content.ingredients.forEach { append("• $it\n") }
            append("\n")
            append(getString(R.string.method))
            append("\n")
            content.steps.forEachIndexed { index, step ->
                append("${index + 1}. $step\n\n")
            }
        }

        binding.tipsList.text = content.tips.joinToString("\n\n") { "• $it" }

        hidePartnerRoleSections()
    }

    private fun hidePartnerRoleSections() {
        val gone = android.view.View.GONE
        binding.manRoleHeader.visibility = gone
        binding.manPositionLabel.visibility = gone
        binding.manPositionText.visibility = gone
        binding.manGuidanceLabel.visibility = gone
        binding.manGuidanceList.visibility = gone
        binding.womanRoleHeader.visibility = gone
        binding.womanPositionLabel.visibility = gone
        binding.womanPositionText.visibility = gone
        binding.womanGuidanceLabel.visibility = gone
        binding.womanGuidanceList.visibility = gone
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
                exportRecipePdf()
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
            NarrationBuilder.buildRecipeNarration(this, recipe, language),
            language
        )
    }

    private fun exportRecipePdf() {
        Toast.makeText(this, R.string.pdf_exporting, Toast.LENGTH_SHORT).show()
        lifecycleScope.launch {
            try {
                val result = withContext(Dispatchers.IO) {
                    PdfExporter.exportRecipe(this@RecipeDetailActivity, recipe, language)
                }
                PdfExporter.showExportActions(this@RecipeDetailActivity, result)
            } catch (e: Exception) {
                Toast.makeText(this@RecipeDetailActivity, R.string.pdf_failed, Toast.LENGTH_SHORT).show()
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
