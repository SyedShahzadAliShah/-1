package com.sindh.cswhiteboard

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.sindh.cswhiteboard.data.CurriculumRepository
import com.sindh.cswhiteboard.data.Prefs
import com.sindh.cswhiteboard.databinding.ActivityLectureListBinding
import com.sindh.cswhiteboard.ui.LectureAdapter

class LectureListActivity : AppCompatActivity() {

    private lateinit var binding: ActivityLectureListBinding

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(Prefs.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLectureListBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val classId = intent.getStringExtra(HomeActivity.EXTRA_CLASS_ID) ?: return finish()
        val chapterId = intent.getStringExtra(HomeActivity.EXTRA_CHAPTER_ID) ?: return finish()
        val chapter = CurriculumRepository.chapter(this, classId, chapterId) ?: return finish()
        val urdu = Prefs.isUrdu(this)
        val goldenOnly = Prefs.goldenOnly(this)
        val lectures = if (goldenOnly) chapter.lectures.filter { it.golden } else chapter.lectures

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        binding.toolbar.setNavigationOnClickListener { finish() }
        binding.toolbar.title = if (urdu) chapter.titleUr else chapter.titleEn
        binding.subtitle.text = getString(R.string.lecture_count, lectures.size)

        binding.btnPlayAll.setOnClickListener {
            val first = lectures.firstOrNull() ?: return@setOnClickListener
            startActivity(
                Intent(this, LecturePlayerActivity::class.java)
                    .putExtra(HomeActivity.EXTRA_LECTURE_ID, first.id)
                    .putExtra(HomeActivity.EXTRA_PLAY_CHAPTER, true)
                    .putExtra(HomeActivity.EXTRA_CHAPTER_ID, chapter.id)
                    .putExtra(HomeActivity.EXTRA_CLASS_ID, classId)
            )
        }

        binding.list.layoutManager = LinearLayoutManager(this)
        binding.list.adapter = LectureAdapter(lectures, urdu, Prefs.doneIds(this)) { lecture ->
            startActivity(
                Intent(this, LecturePlayerActivity::class.java)
                    .putExtra(HomeActivity.EXTRA_LECTURE_ID, lecture.id)
                    .putExtra(HomeActivity.EXTRA_CHAPTER_ID, chapter.id)
                    .putExtra(HomeActivity.EXTRA_CLASS_ID, classId)
            )
        }
    }

    override fun onResume() {
        super.onResume()
        binding.list.adapter?.notifyDataSetChanged()
    }
}
