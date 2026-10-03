package com.couplesguide.postures

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.couplesguide.postures.data.CsTeacherRepository
import com.couplesguide.postures.databinding.ActivityBookTopicsBinding
import com.couplesguide.postures.ui.TopicAdapter
import com.couplesguide.postures.util.RecyclerViewHelper

class BookTopicsActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_BOOK_ID = "book_id"
    }

    private lateinit var binding: ActivityBookTopicsBinding
    private lateinit var topicAdapter: TopicAdapter

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityBookTopicsBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val bookId = intent.getStringExtra(EXTRA_BOOK_ID)
        val book = bookId?.let { CsTeacherRepository.getBook(this, it) }
        if (book == null) {
            finish()
            return
        }

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = book.title
        binding.bookSubtitle.text = book.subtitle

        topicAdapter = TopicAdapter { topic ->
            startActivity(Intent(this, ChapterDetailActivity::class.java).apply {
                putExtra(ChapterDetailActivity.EXTRA_TOPIC_ID, topic.id)
            })
        }

        binding.topicList.layoutManager = LinearLayoutManager(this)
        binding.topicList.adapter = topicAdapter
        RecyclerViewHelper.setupNestedList(binding.topicList)
        topicAdapter.submitList(book.topics)
    }

    override fun onSupportNavigateUp(): Boolean {
        finish()
        return true
    }
}
