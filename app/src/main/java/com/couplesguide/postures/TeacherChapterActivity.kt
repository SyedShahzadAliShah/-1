package com.couplesguide.postures

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.couplesguide.postures.data.TeacherChapter
import com.couplesguide.postures.data.TeacherGuideRepository
import com.couplesguide.postures.databinding.ActivityTeacherChapterBinding
import com.couplesguide.postures.ui.TeacherTopicAdapter
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.RecyclerViewHelper

class TeacherChapterActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_CHAPTER_ID = "teacher_chapter_id"
    }

    private lateinit var binding: ActivityTeacherChapterBinding
    private lateinit var chapter: TeacherChapter

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityTeacherChapterBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val chapterId = intent.getStringExtra(EXTRA_CHAPTER_ID)
        val found = chapterId?.let { TeacherGuideRepository.getChapterById(this, it) }
        if (found == null) {
            finish()
            return
        }
        chapter = found

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = chapter.title

        val adapter = TeacherTopicAdapter { topic ->
            startActivity(Intent(this, TeacherTopicDetailActivity::class.java).apply {
                putExtra(TeacherTopicDetailActivity.EXTRA_TOPIC_ID, topic.id)
            })
        }
        binding.topicList.layoutManager = LinearLayoutManager(this)
        binding.topicList.adapter = adapter
        RecyclerViewHelper.setupNestedList(binding.topicList)
        adapter.submitList(chapter.topics)
    }

    override fun onSupportNavigateUp(): Boolean {
        finish()
        return true
    }
}
