package com.couplesguide.postures

import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.couplesguide.postures.data.BookIntroRepository
import com.couplesguide.postures.data.GuideChapter
import com.couplesguide.postures.databinding.ActivityChapterDetailBinding
import com.couplesguide.postures.util.AnimatedIllustrationHelper
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.NarrationBuilder
import com.couplesguide.postures.util.VoiceNarrator

class ChapterDetailActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_CHAPTER_ID = "chapter_id"
    }

    private lateinit var binding: ActivityChapterDetailBinding
    private lateinit var chapter: GuideChapter
    private val language = LocaleHelper.LANG_UR
    private var voiceNarrator: VoiceNarrator? = null
    private var voiceReady = false
    private var isSpeaking = false

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityChapterDetailBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val chapterId = intent.getStringExtra(EXTRA_CHAPTER_ID)
        val found = when (chapterId) {
            BookIntroRepository.getIntroChapter().id -> BookIntroRepository.getIntroChapter()
            else -> null
        }

        if (found == null) {
            finish()
            return
        }
        chapter = found

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
        val content = chapter.urdu
        supportActionBar?.title = content.title
        AnimatedIllustrationHelper.bind(binding.illustration, chapter.illustrationRes)
        binding.chapterTitle.text = content.title
        binding.chapterSummary.text = content.summary
        binding.chapterBody.text = content.body
        binding.keyPointsList.text = content.keyPoints.joinToString("\n\n") { "• $it" }
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_detail, menu)
        menu.findItem(R.id.action_export)?.isVisible = false
        val listenItem = menu.findItem(R.id.action_listen)
        listenItem.title = if (isSpeaking) getString(R.string.stop) else getString(R.string.listen)
        listenItem.setIcon(
            if (isSpeaking) android.R.drawable.ic_media_pause
            else android.R.drawable.ic_media_play
        )
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        if (item.itemId == R.id.action_listen) {
            toggleNarration()
            return true
        }
        return super.onOptionsItemSelected(item)
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
        voiceNarrator?.speak(NarrationBuilder.buildChapterNarration(chapter.id, language), language)
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
