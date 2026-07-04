package com.pakrecipes.cooking

import android.content.Context
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import com.pakrecipes.cooking.data.Recipe
import com.pakrecipes.cooking.data.RecipeRepository
import com.pakrecipes.cooking.databinding.ActivityRecipeDetailBinding
import com.pakrecipes.cooking.util.PdfExporter
import com.pakrecipes.cooking.util.VoiceNarrator
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class RecipeDetailActivity : AppCompatActivity() {

    private lateinit var binding: ActivityRecipeDetailBinding
    private var recipe: Recipe? = null
    private var voiceNarrator: VoiceNarrator? = null
    private var voiceReady = false
    private var isSpeaking = false

    override fun attachBaseContext(newBase: Context) {
        super.attachBaseContext(RecipeApp.applyUrduLocale(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityRecipeDetailBinding.inflate(layoutInflater)
        setContentView(binding.root)
        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)

        val id = intent.getStringExtra(EXTRA_RECIPE_ID) ?: run { finish(); return }
        recipe = RecipeRepository.getById(id)?.also { populateUi(it) } ?: run { finish(); return }

        voiceNarrator = VoiceNarrator(
            context = this,
            onReadyChanged = { ready -> voiceReady = ready },
            onSpeakingChanged = { speaking ->
                isSpeaking = speaking
                invalidateOptionsMenu()
                updateVoiceButton()
            },
            onLanguageIssue = { msg -> Toast.makeText(this, msg, Toast.LENGTH_LONG).show() }
        )

        binding.fabVoice.setOnClickListener { toggleVoice() }
        binding.fabExport.setOnClickListener { exportRecipePdf() }
    }

    private fun populateUi(recipe: Recipe) {
        supportActionBar?.title = recipe.nameUrdu

        binding.recipeTitle.text = recipe.nameUrdu
        binding.recipeCity.text = recipe.cityId.toCityName()
        binding.recipeDifficulty.text = recipe.difficulty.labelUrdu
        binding.recipeServings.text = "${recipe.servings} افراد"
        binding.recipePrepTime.text = "تیاری: ${recipe.prepTimeMinutes} منٹ"
        binding.recipeCookTime.text = "پکانا: ${recipe.cookTimeMinutes} منٹ"
        binding.recipeDescription.text = recipe.descriptionUrdu

        binding.ingredientsContent.text = recipe.ingredientsUrdu.joinToString("\n") { "• $it" }

        val stepsText = recipe.stepsUrdu.mapIndexed { idx, step ->
            "${toUrduNumber(idx + 1)}۔ $step"
        }.joinToString("\n\n")
        binding.stepsContent.text = stepsText

        binding.tipsContent.text = recipe.tipsUrdu.joinToString("\n") { "• $it" }
    }

    private fun toUrduNumber(n: Int): String = n.toString().map {
        when (it) { '0' -> '۰'; '1' -> '۱'; '2' -> '۲'; '3' -> '۳'; '4' -> '۴'
            '5' -> '۵'; '6' -> '۶'; '7' -> '۷'; '8' -> '۸'; '9' -> '۹'; else -> it }
    }.joinToString("")

    private fun String.toCityName(): String = when (this) {
        "karachi" -> "کراچی"
        "lahore" -> "لاہور"
        "peshawar" -> "پشاور"
        "quetta" -> "کوئٹہ"
        "hyderabad" -> "حیدرآباد"
        "multan" -> "ملتان"
        "islamabad" -> "اسلام آباد"
        "rawalpindi" -> "راولپنڈی"
        "gilgit" -> "گلگت بلتستان"
        else -> this
    }

    private fun toggleVoice() {
        if (isSpeaking) {
            voiceNarrator?.stop()
            return
        }
        if (!voiceReady) {
            Toast.makeText(this, R.string.voice_not_ready, Toast.LENGTH_SHORT).show()
            return
        }
        val r = recipe ?: return
        val narration = buildNarration(r)
        if (voiceNarrator?.speak(narration) != true) {
            Toast.makeText(this, R.string.voice_install_prompt, Toast.LENGTH_LONG).show()
        }
    }

    private fun buildNarration(recipe: Recipe): String {
        val sb = StringBuilder()
        sb.append("${recipe.nameUrdu}۔ ")
        sb.append("${recipe.cityId.toCityName()} کا مشہور کھانا۔ ")
        sb.append("${recipe.descriptionUrdu} ")
        sb.append("اجزاء: ")
        recipe.ingredientsUrdu.forEach { sb.append("$it۔ ") }
        sb.append("ترکیب: ")
        recipe.stepsUrdu.forEachIndexed { idx, step -> sb.append("${idx + 1}۔ $step ") }
        sb.append("مشورے: ")
        recipe.tipsUrdu.forEach { sb.append("$it۔ ") }
        return sb.toString()
    }

    private fun updateVoiceButton() {
        binding.fabVoice.setImageResource(
            if (isSpeaking) android.R.drawable.ic_media_pause
            else android.R.drawable.ic_media_play
        )
    }

    private fun exportRecipePdf() {
        val r = recipe ?: return
        Toast.makeText(this, R.string.pdf_exporting, Toast.LENGTH_SHORT).show()
        lifecycleScope.launch {
            try {
                val result = withContext(Dispatchers.IO) { PdfExporter.exportRecipe(this@RecipeDetailActivity, r) }
                PdfExporter.showExportActions(this@RecipeDetailActivity, result)
            } catch (e: Exception) {
                Toast.makeText(this@RecipeDetailActivity, R.string.pdf_failed, Toast.LENGTH_SHORT).show()
            }
        }
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_recipe_detail, menu)
        val listenItem = menu.findItem(R.id.action_listen)
        listenItem?.title = if (isSpeaking) getString(R.string.stop) else getString(R.string.listen)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            android.R.id.home -> { onBackPressedDispatcher.onBackPressed(); true }
            R.id.action_listen -> { toggleVoice(); true }
            R.id.action_export -> { exportRecipePdf(); true }
            else -> super.onOptionsItemSelected(item)
        }
    }

    override fun onDestroy() {
        voiceNarrator?.shutdown()
        voiceNarrator = null
        super.onDestroy()
    }

    companion object {
        const val EXTRA_RECIPE_ID = "recipe_id"
    }
}
