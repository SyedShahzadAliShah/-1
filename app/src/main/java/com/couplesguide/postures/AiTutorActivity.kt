package com.couplesguide.postures

import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.view.View
import android.view.inputmethod.EditorInfo
import android.widget.EditText
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import androidx.recyclerview.widget.LinearLayoutManager
import com.couplesguide.postures.data.LectureNotesRepository
import com.couplesguide.postures.databinding.ActivityAiTutorBinding
import com.couplesguide.postures.tutor.AiTutorPreferences
import com.couplesguide.postures.tutor.EmbeddedAiTutorEngine
import com.couplesguide.postures.tutor.GeminiTutorClient
import com.couplesguide.postures.tutor.TutorChatMessage
import com.couplesguide.postures.tutor.TutorContext
import com.couplesguide.postures.tutor.TutorCorpus
import com.couplesguide.postures.ui.TutorChatAdapter
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.TtsPlaybackHelper
import com.couplesguide.postures.util.VoiceNarrator
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class AiTutorActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_CHAPTER_ID = "tutor_chapter_id"
        const val EXTRA_CLASS_ID = "tutor_class_id"
        const val EXTRA_PAGE = "tutor_page"
        const val EXTRA_SEED_MESSAGE = "tutor_seed_message"
    }

    private lateinit var binding: ActivityAiTutorBinding
    private val adapter = TutorChatAdapter()
    private val messages = mutableListOf<TutorChatMessage>()
    private var language = LocaleHelper.LANG_EN
    private lateinit var tutorContext: TutorContext
    private var corpusReady = false
    private var voiceNarrator: VoiceNarrator? = null
    private var voiceReady = false

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityAiTutorBinding.inflate(layoutInflater)
        setContentView(binding.root)

        language = LocaleHelper.getLanguage(this)
        tutorContext = TutorContext(
            chapterId = intent.getStringExtra(EXTRA_CHAPTER_ID),
            classId = intent.getStringExtra(EXTRA_CLASS_ID),
            page = intent.getIntExtra(EXTRA_PAGE, -1).takeIf { it > 0 }
        )

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = getString(R.string.ai_tutor_title)

        binding.chatList.layoutManager = LinearLayoutManager(this).apply { stackFromEnd = true }
        binding.chatList.adapter = adapter

        showContextBanner()
        bindChips()
        voiceNarrator = VoiceNarrator(
            context = this,
            onReadyChanged = { ready -> voiceReady = ready },
            onSpeakingChanged = { },
            onLanguageIssue = null
        )

        binding.btnSend.setOnClickListener { sendFromInput() }
        binding.inputMessage.setOnEditorActionListener { _, actionId, _ ->
            if (actionId == EditorInfo.IME_ACTION_SEND) {
                sendFromInput()
                true
            } else false
        }

        binding.tutorLoading.visibility = View.VISIBLE
        lifecycleScope.launch {
            withContext(Dispatchers.Default) { TutorCorpus.ensureLoaded(this@AiTutorActivity) }
            corpusReady = true
            binding.tutorLoading.visibility = View.GONE
            if (messages.isEmpty()) {
                appendTutor(EmbeddedAiTutorEngine.reply(this@AiTutorActivity, "", tutorContext, useUrdu()))
                tutorContext.chapterId?.let { id ->
                    appendTutor(EmbeddedAiTutorEngine.chapterHint(this@AiTutorActivity, id, useUrdu()))
                }
                intent.getStringExtra(EXTRA_SEED_MESSAGE)?.let { seed ->
                    sendUserMessage(seed)
                }
            }
        }
    }

    private fun showContextBanner() {
        val chapterId = tutorContext.chapterId
        if (chapterId != null) {
            LectureNotesRepository.ensureLoaded(this)
            val title = LectureNotesRepository.getChapterById(this, chapterId)?.let { ch ->
                if (useUrdu()) ch.urdu.title else ch.english.title
            } ?: chapterId
            binding.tutorContextBanner.visibility = View.VISIBLE
            binding.tutorContextBanner.text = getString(R.string.tutor_context_chapter, title)
        }
    }

    private fun bindChips() {
        binding.chipGolden.setOnClickListener { sendUserMessage("golden topics") }
        binding.chipQuizXi.setOnClickListener { sendUserMessage("quiz xi") }
        binding.chipQuizXii.setOnClickListener { sendUserMessage("quiz xii") }
        binding.chipOsi.setOnClickListener { sendUserMessage("explain OSI 7 layer model") }
    }

    private fun sendFromInput() {
        val text = binding.inputMessage.text?.toString()?.trim() ?: return
        if (text.isEmpty()) return
        binding.inputMessage.text?.clear()
        sendUserMessage(text)
    }

    private fun sendUserMessage(text: String) {
        if (!corpusReady) return
        appendUser(text)
        binding.tutorLoading.visibility = View.VISIBLE
        lifecycleScope.launch {
            val reply = withContext(Dispatchers.Default) {
                produceReply(text)
            }
            binding.tutorLoading.visibility = View.GONE
            appendTutor(reply)
        }
    }

    private fun produceReply(userText: String): String {
        val useUrdu = useUrdu()
        val embedded = EmbeddedAiTutorEngine.reply(this, userText, tutorContext, useUrdu)
        val key = AiTutorPreferences.getGeminiApiKey(this)
        if (!AiTutorPreferences.isCloudEnabled(this) || !GeminiTutorClient.isConfigured(key)) {
            return embedded
        }
        val grounding = EmbeddedAiTutorEngine.groundingExcerpt(this, userText, tutorContext)
        val cloud = GeminiTutorClient.ask(key!!, userText, grounding, useUrdu)
        if (cloud != null) {
            return cloud + "\n\n— " + getString(R.string.tutor_cloud_footer)
        }
        return embedded + "\n\n" + getString(R.string.tutor_cloud_fallback)
    }

    private fun useUrdu(): Boolean = language == LocaleHelper.LANG_UR

    private fun appendUser(text: String) {
        messages.add(TutorChatMessage(TutorChatMessage.Role.USER, text))
        refreshList()
    }

    private fun appendTutor(text: String) {
        messages.add(TutorChatMessage(TutorChatMessage.Role.TUTOR, text))
        refreshList()
    }

    private fun refreshList() {
        adapter.submitList(messages.toList()) {
            if (messages.isNotEmpty()) {
                binding.chatList.scrollToPosition(messages.size - 1)
            }
        }
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_tutor, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        when (item.itemId) {
            android.R.id.home -> {
                finish()
                return true
            }
            R.id.action_tutor_listen -> {
                readLatestTutorReplyAloud()
                return true
            }
            R.id.action_tutor_settings -> {
                showSettingsDialog()
                return true
            }
            R.id.action_tutor_clear -> {
                messages.clear()
                adapter.submitList(emptyList())
                appendTutor(EmbeddedAiTutorEngine.reply(this, "", tutorContext, useUrdu()))
                return true
            }
        }
        return super.onOptionsItemSelected(item)
    }

    private fun readLatestTutorReplyAloud() {
        val last = messages.lastOrNull { it.role == TutorChatMessage.Role.TUTOR }?.text
        if (last.isNullOrBlank()) return
        if (!voiceReady) {
            TtsPlaybackHelper.showPlaybackFailedDialog(this)
            return
        }
        val lang = if (useUrdu()) LocaleHelper.LANG_UR else LocaleHelper.LANG_EN
        if (voiceNarrator?.speak(last, lang) != true) {
            TtsPlaybackHelper.showPlaybackFailedDialog(this)
        }
    }

    override fun onDestroy() {
        voiceNarrator?.shutdown()
        voiceNarrator = null
        super.onDestroy()
    }

    private fun showSettingsDialog() {
        val key = AiTutorPreferences.getGeminiApiKey(this) ?: ""
        val input = EditText(this).apply {
            hint = getString(R.string.tutor_api_key_hint)
            setText(key)
            setSingleLine()
        }
        AlertDialog.Builder(this)
            .setTitle(R.string.tutor_settings_title)
            .setMessage(R.string.tutor_settings_message)
            .setView(input)
            .setPositiveButton(R.string.tutor_save) { _, _ ->
                val saved = input.text?.toString()?.trim()
                AiTutorPreferences.setGeminiApiKey(this, saved)
                AiTutorPreferences.setCloudEnabled(this, !saved.isNullOrEmpty())
            }
            .setNegativeButton(android.R.string.cancel, null)
            .show()
    }
}
