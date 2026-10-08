package com.couplesguide.postures

import com.csteacher.edition.R

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.couplesguide.postures.data.CsBook
import com.couplesguide.postures.data.CsTeacherRepository
import com.csteacher.edition.databinding.ActivityLectureListBinding
import com.couplesguide.postures.ui.LectureAdapter
import com.couplesguide.postures.util.RecyclerViewHelper

class LectureListActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_BOOK_ID = "book_id"
    }

    private lateinit var binding: ActivityLectureListBinding
    private lateinit var book: CsBook

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLectureListBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val bookId = intent.getStringExtra(EXTRA_BOOK_ID)
        val loaded = bookId?.let { CsTeacherRepository.getBook(this, it) }
        if (loaded == null) {
            finish()
            return
        }
        book = loaded

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = getString(R.string.study_guide_title)

        binding.studyGuideHeader.text = "${book.studyGuideLabel}\n${book.title}\n${book.subtitle}"

        val adapter = LectureAdapter { lecture ->
            startActivity(Intent(this, BookTopicsActivity::class.java).apply {
                putExtra(BookTopicsActivity.EXTRA_BOOK_ID, book.id)
                putExtra(BookTopicsActivity.EXTRA_LECTURE_ID, lecture.id)
            })
        }
        binding.lectureList.layoutManager = LinearLayoutManager(this)
        binding.lectureList.adapter = adapter
        RecyclerViewHelper.setupNestedList(binding.lectureList)
        adapter.submitList(book.lectures)
    }

    override fun onSupportNavigateUp(): Boolean {
        finish()
        return true
    }
}
