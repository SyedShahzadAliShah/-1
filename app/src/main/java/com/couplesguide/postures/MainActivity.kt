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
import com.couplesguide.postures.data.GenderEducationRepository
import com.couplesguide.postures.data.GuideRepository
import com.couplesguide.postures.data.PostureListBuilder
import com.couplesguide.postures.data.PostureListItem
import com.couplesguide.postures.data.PostureRepository
import com.couplesguide.postures.databinding.ActivityMainBinding
import com.couplesguide.postures.ui.CategoryAdapter
import com.couplesguide.postures.ui.ChapterAdapter
import com.couplesguide.postures.ui.PostureAdapter
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
    private lateinit var postureAdapter: PostureAdapter
    private lateinit var chapterAdapter: ChapterAdapter
    private lateinit var forHimAdapter: ChapterAdapter
    private lateinit var forHerAdapter: ChapterAdapter
    private lateinit var imaginationAdapter: PostureAdapter
    private var categoryAdapter: CategoryAdapter? = null
    private var selectedCategory = PostureRepository.CAT_ALL
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

        voiceNarrator = VoiceNarrator(
            context = this,
            onReadyChanged = { ready -> voiceReady = ready },
            onSpeakingChanged = { speaking ->
                isSpeaking = speaking
                invalidateOptionsMenu()
            },
            onLanguageIssue = { message -> showVoiceMessage(message) }
        )

        imaginationAdapter = PostureAdapter(language) { posture ->
            startActivity(Intent(this, PostureDetailActivity::class.java).apply {
                putExtra(PostureDetailActivity.EXTRA_POSTURE_ID, posture.id)
            })
        }

        postureAdapter = PostureAdapter(language) { posture ->
            startActivity(Intent(this, PostureDetailActivity::class.java).apply {
                putExtra(PostureDetailActivity.EXTRA_POSTURE_ID, posture.id)
            })
        }

        chapterAdapter = ChapterAdapter(language) { chapter ->
            startActivity(Intent(this, ChapterDetailActivity::class.java).apply {
                putExtra(ChapterDetailActivity.EXTRA_CHAPTER_ID, chapter.id)
            })
        }

        forHimAdapter = ChapterAdapter(language) { chapter ->
            startActivity(Intent(this, ChapterDetailActivity::class.java).apply {
                putExtra(ChapterDetailActivity.EXTRA_CHAPTER_ID, chapter.id)
            })
        }

        forHerAdapter = ChapterAdapter(language) { chapter ->
            startActivity(Intent(this, ChapterDetailActivity::class.java).apply {
                putExtra(ChapterDetailActivity.EXTRA_CHAPTER_ID, chapter.id)
            })
        }

        binding.postureList.layoutManager = LinearLayoutManager(this)
        binding.postureList.adapter = postureAdapter
        RecyclerViewHelper.setupNestedList(binding.postureList)

        RecyclerViewHelper.setupNestedList(binding.chapterList)
        binding.chapterList.adapter = chapterAdapter
        chapterAdapter.submitList(GuideRepository.getChapters())
        binding.chapterList.post { binding.chapterList.requestLayout() }

        RecyclerViewHelper.setupNestedList(binding.forHimList)
        binding.forHimList.adapter = forHimAdapter
        forHimAdapter.submitList(GenderEducationRepository.getForHimChapters())
        binding.forHimList.post { binding.forHimList.requestLayout() }

        RecyclerViewHelper.setupNestedList(binding.forHerList)
        binding.forHerList.adapter = forHerAdapter
        forHerAdapter.submitList(GenderEducationRepository.getForHerChapters())
        binding.forHerList.post { binding.forHerList.requestLayout() }

        RecyclerViewHelper.setupNestedList(binding.imaginationList)
        binding.imaginationList.adapter = imaginationAdapter
        imaginationAdapter.submitList(
            PostureRepository.getImaginationPostures().map { PostureListItem.PostureEntry(it) }
        )
        binding.imaginationList.post { binding.imaginationList.requestLayout() }

        setupCategories()
        updatePostureList()
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
                exportFullGuidePdf()
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }

    private fun setupCategories() {
        categoryAdapter = CategoryAdapter(language) { categoryId ->
            selectedCategory = categoryId
            updatePostureList()
        }
        binding.categoryList.layoutManager =
            LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL, false)
        binding.categoryList.adapter = categoryAdapter
    }

    private fun updatePostureList() {
        val postures = PostureRepository.getPosturesByCategory(selectedCategory)
        val includeEduCards = selectedCategory == PostureRepository.CAT_ALL
        val items = PostureListBuilder.build(postures, includeEduCards)
        postureAdapter.submitList(items)
        binding.postureList.post { binding.postureList.requestLayout() }
        binding.emptyText.visibility = if (items.isEmpty()) View.VISIBLE else View.GONE
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

    private fun exportFullGuidePdf() {
        Toast.makeText(this, R.string.pdf_exporting, Toast.LENGTH_SHORT).show()
        lifecycleScope.launch {
            try {
                val result = withContext(Dispatchers.IO) {
                    PdfExporter.exportFullGuide(this@MainActivity, language)
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
