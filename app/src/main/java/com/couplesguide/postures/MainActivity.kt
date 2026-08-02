package com.couplesguide.postures

import android.content.Intent
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.view.View
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import androidx.recyclerview.widget.LinearLayoutManager
import com.couplesguide.postures.data.BuffetGuideRepository
import com.couplesguide.postures.data.RecipeRepository
import com.couplesguide.postures.databinding.ActivityMainBinding
import com.couplesguide.postures.ui.CategoryAdapter
import com.couplesguide.postures.ui.ChapterAdapter
import com.couplesguide.postures.ui.RecipeAdapter
import com.couplesguide.postures.BuildConfig
import com.couplesguide.postures.util.RecyclerViewHelper
import com.couplesguide.postures.util.AnimatedIllustrationHelper
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.NarrationBuilder
import com.couplesguide.postures.util.PdfExporter
import com.couplesguide.postures.util.VoiceNarrator
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private lateinit var recipeAdapter: RecipeAdapter
    private lateinit var chapterAdapter: ChapterAdapter
    private var categoryAdapter: CategoryAdapter? = null
    private var selectedCategory = RecipeRepository.CAT_ALL
    private var language = LocaleHelper.LANG_EN
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

        language = LocaleHelper.getLanguage(this)
        setSupportActionBar(binding.toolbar)
        supportActionBar?.title = getString(R.string.app_name)

        voiceNarrator = VoiceNarrator(
            context = this,
            onReadyChanged = { ready -> voiceReady = ready },
            onSpeakingChanged = { speaking ->
                isSpeaking = speaking
                invalidateOptionsMenu()
            },
            onLanguageIssue = { message -> showVoiceMessage(message) }
        )

        recipeAdapter = RecipeAdapter(language) { recipe ->
            startActivity(Intent(this, RecipeDetailActivity::class.java).apply {
                putExtra(RecipeDetailActivity.EXTRA_RECIPE_ID, recipe.id)
            })
        }

        chapterAdapter = ChapterAdapter(language) { chapter ->
            startActivity(Intent(this, ChapterDetailActivity::class.java).apply {
                putExtra(ChapterDetailActivity.EXTRA_CHAPTER_ID, chapter.id)
            })
        }

        binding.postureList.layoutManager = LinearLayoutManager(this)
        binding.postureList.adapter = recipeAdapter
        RecyclerViewHelper.setupNestedList(binding.postureList)

        RecyclerViewHelper.setupNestedList(binding.chapterList)
        binding.chapterList.adapter = chapterAdapter
        chapterAdapter.submitList(BuffetGuideRepository.getChapters())
        binding.chapterList.post { binding.chapterList.requestLayout() }

        setupCategories()
        updateRecipeList()
        binding.versionBadge.text = getString(R.string.version_badge, BuildConfig.VERSION_NAME)
        AnimatedIllustrationHelper.bind(
            binding.guideCoverImage,
            R.drawable.pic_guide_cover
        )
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
            R.id.action_language -> {
                showLanguageDialog()
                true
            }
            R.id.action_listen -> {
                toggleNarration()
                true
            }
            R.id.action_export -> {
                exportFullCookbookPdf()
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }

    private fun setupCategories() {
        categoryAdapter = CategoryAdapter(language) { categoryId ->
            selectedCategory = categoryId
            updateRecipeList()
        }
        binding.categoryList.layoutManager =
            LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL, false)
        binding.categoryList.adapter = categoryAdapter
    }

    private fun updateRecipeList() {
        val recipes = RecipeRepository.getRecipesByCategory(selectedCategory)
        recipeAdapter.submitList(recipes)
        binding.postureList.post { binding.postureList.requestLayout() }
        binding.emptyText.visibility = if (recipes.isEmpty()) View.VISIBLE else View.GONE
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
            voiceNarrator?.stop()
            return
        }
        if (!voiceReady) {
            Toast.makeText(this, R.string.voice_not_ready, Toast.LENGTH_SHORT).show()
            return
        }
        val text = NarrationBuilder.buildMainGuideNarration(this, language)
        if (voiceNarrator?.speak(text, language) != true) {
            Toast.makeText(this, R.string.voice_install_prompt, Toast.LENGTH_LONG).show()
        }
    }

    private fun showVoiceMessage(message: String) {
        Toast.makeText(this, message, Toast.LENGTH_LONG).show()
    }

    private fun exportFullCookbookPdf() {
        Toast.makeText(this, R.string.pdf_exporting, Toast.LENGTH_SHORT).show()
        lifecycleScope.launch {
            try {
                val result = withContext(Dispatchers.IO) {
                    PdfExporter.exportFullCookbook(this@MainActivity, language)
                }
                PdfExporter.showExportActions(this@MainActivity, result)
            } catch (e: Exception) {
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
