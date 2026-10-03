package com.couplesguide.postures

import android.content.Intent
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.couplesguide.postures.data.CsBook
import com.couplesguide.postures.data.CsTeacherRepository
import com.couplesguide.postures.databinding.ActivityBookTopicsBinding
import com.couplesguide.postures.ui.TopicAdapter
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.RecyclerViewHelper
import com.couplesguide.postures.util.VoiceNarrator

class BookTopicsActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_BOOK_ID = "book_id"
        const val EXTRA_LECTURE_ID = "lecture_id"
    }

    private lateinit var binding: ActivityBookTopicsBinding
    private lateinit var topicAdapter: TopicAdapter
    private lateinit var book: CsBook
    private var lectureId: String? = null
    private var guidelinesNarrator: VoiceNarrator? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityBookTopicsBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val bookId = intent.getStringExtra(EXTRA_BOOK_ID)
        val loaded = bookId?.let { CsTeacherRepository.getBook(this, it) }
        if (loaded == null) {
            finish()
            return
        }
        book = loaded
        lectureId = intent.getStringExtra(EXTRA_LECTURE_ID)

        guidelinesNarrator = VoiceNarrator(
            context = this,
            onReadyChanged = { },
            onSpeakingChanged = { },
            onLanguageIssue = { message -> Toast.makeText(this, message, Toast.LENGTH_LONG).show() }
        )

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        val lecture = lectureId?.let { CsTeacherRepository.getLecture(this, it)?.second }
        supportActionBar?.title = lecture?.title ?: book.teacherGuidelines.editionTitle
        bindHeader(lecture)

        topicAdapter = TopicAdapter { topic ->
            startActivity(Intent(this, ChapterDetailActivity::class.java).apply {
                putExtra(ChapterDetailActivity.EXTRA_TOPIC_ID, topic.id)
            })
        }

        binding.topicList.layoutManager = LinearLayoutManager(this)
        binding.topicList.adapter = topicAdapter
        RecyclerViewHelper.setupNestedList(binding.topicList)
        val topics = lecture?.topics(book.topics) ?: book.topics
        topicAdapter.submitList(topics)

        binding.listenGuidelinesButton.setOnClickListener {
            val narrator = guidelinesNarrator ?: return@setOnClickListener
            if (narrator.isSpeaking()) {
                narrator.stop()
            } else {
                val urdu = lecture?.urduNarration?.takeIf { it.isNotBlank() }
                    ?: book.teacherGuidelines.urduNarration
                narrator.speak(urdu, LocaleHelper.LANG_UR)
            }
        }
    }

    private fun bindHeader(lecture: com.couplesguide.postures.data.CsLecture?) {
        val g = book.teacherGuidelines
        if (lecture != null) {
            binding.bookSubtitle.text = lecture.englishSummary
            binding.guidelinesEnglish.text = g.english
        } else {
            binding.bookSubtitle.text = "${book.title}\n${g.tagline}\n${getString(R.string.curriculum_label, g.curriculum)}"
            binding.guidelinesEnglish.text = g.english
        }
        binding.textbookReference.text = getString(R.string.textbook_reference_label, g.textbookReference)
        binding.goldenPolicy.text = g.goldenTopicNote
    }

    override fun onSupportNavigateUp(): Boolean {
        finish()
        return true
    }

    override fun onDestroy() {
        guidelinesNarrator?.shutdown()
        guidelinesNarrator = null
        super.onDestroy()
    }
}
