package com.couplesguide.postures

import android.content.Intent
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.couplesguide.postures.data.CsTeacherRepository
import com.couplesguide.postures.databinding.ActivityMainBinding
import com.couplesguide.postures.ui.BookAdapter
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.NarrationBuilder
import com.couplesguide.postures.util.RecyclerViewHelper
import com.couplesguide.postures.util.VoiceNarrator
import com.couplesguide.postures.BuildConfig

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private lateinit var bookAdapter: BookAdapter
    private var voiceNarrator: VoiceNarrator? = null
    private var voiceReady = false
    private var isSpeaking = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        setSupportActionBar(binding.toolbar)
        supportActionBar?.title = getString(R.string.app_name)
        binding.versionBadge.text = getString(R.string.version_badge, BuildConfig.VERSION_NAME)

        voiceNarrator = VoiceNarrator(
            context = this,
            onReadyChanged = { ready -> voiceReady = ready },
            onSpeakingChanged = { speaking ->
                isSpeaking = speaking
                invalidateOptionsMenu()
            },
            onLanguageIssue = { message -> Toast.makeText(this, message, Toast.LENGTH_LONG).show() }
        )

        bookAdapter = BookAdapter { book ->
            startActivity(Intent(this, BookTopicsActivity::class.java).apply {
                putExtra(BookTopicsActivity.EXTRA_BOOK_ID, book.id)
            })
        }

        binding.bookList.layoutManager = LinearLayoutManager(this)
        binding.bookList.adapter = bookAdapter
        RecyclerViewHelper.setupNestedList(binding.bookList)
        bookAdapter.submitList(CsTeacherRepository.getBooks(this))

        binding.listenWelcomeButton.setOnClickListener { toggleWelcomeNarration() }
    }

    private fun toggleWelcomeNarration() {
        val narrator = voiceNarrator ?: return
        if (narrator.isSpeaking()) {
            narrator.stop()
            return
        }
        if (!voiceReady) {
            Toast.makeText(this, R.string.voice_not_ready, Toast.LENGTH_SHORT).show()
            return
        }
        val text = NarrationBuilder.buildWelcomeNarration(this)
        narrator.speak(text, LocaleHelper.LANG_UR)
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_main, menu)
        val listenItem = menu.findItem(R.id.action_listen)
        listenItem?.title = if (isSpeaking) getString(R.string.stop) else getString(R.string.listen_urdu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            R.id.action_listen -> {
                toggleWelcomeNarration()
                true
            }
            R.id.action_tts_settings -> {
                VoiceNarrator.openTtsSettings(this)
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }

    override fun onDestroy() {
        voiceNarrator?.shutdown()
        voiceNarrator = null
        super.onDestroy()
    }
}
