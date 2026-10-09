package com.sindhcs.lectures

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.sindhcs.lectures.data.LectureRepository
import com.sindhcs.lectures.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        setSupportActionBar(binding.toolbar)

        val catalog = LectureRepository.load(this)
        val xi = catalog.grades.find { it.id == "xi" }
        val xii = catalog.grades.find { it.id == "xii" }
        if (xi != null) {
            binding.xiTitle.text = xi.title
            binding.xiMeta.text = getString(
                R.string.grade_meta,
                xi.chapters.size,
                xi.chapters.sumOf { it.topics.size },
                xi.chapters.sumOf { it.goldenCount }
            )
            binding.xiUrdu.text = xi.urdu
            binding.cardXi.setOnClickListener { openGrade("xi") }
        }
        if (xii != null) {
            binding.xiiTitle.text = xii.title
            binding.xiiMeta.text = getString(
                R.string.grade_meta,
                xii.chapters.size,
                xii.chapters.sumOf { it.topics.size },
                xii.chapters.sumOf { it.goldenCount }
            )
            binding.xiiUrdu.text = xii.urdu
            binding.cardXii.setOnClickListener { openGrade("xii") }
        }
    }

    private fun openGrade(id: String) {
        startActivity(Intent(this, ChapterListActivity::class.java).putExtra(EXTRA_GRADE, id))
    }

    companion object {
        const val EXTRA_GRADE = "grade_id"
        const val EXTRA_CHAPTER = "chapter_num"
        const val EXTRA_TOPIC = "topic_id"
    }
}
