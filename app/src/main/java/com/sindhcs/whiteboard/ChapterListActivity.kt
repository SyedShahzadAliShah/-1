package com.sindhcs.whiteboard

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.sindhcs.whiteboard.data.CatalogStore
import com.sindhcs.whiteboard.databinding.ActivityChapterListBinding
import com.sindhcs.whiteboard.ui.ChapterAdapter

class ChapterListActivity : AppCompatActivity() {

    private lateinit var binding: ActivityChapterListBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityChapterListBinding.inflate(layoutInflater)
        setContentView(binding.root)
        val grade = CatalogStore.get(this).grade(intent.getStringExtra(EXTRA_GRADE_ID) ?: "xi")
        setSupportActionBar(binding.toolbar)
        binding.toolbar.title = grade.title
        binding.toolbar.subtitle = grade.subtitle
        binding.toolbar.setNavigationOnClickListener { finish() }
        binding.list.layoutManager = LinearLayoutManager(this)
        binding.list.adapter = ChapterAdapter(grade.chapters) { chapter ->
            startActivity(Intent(this, LectureListActivity::class.java).apply {
                putExtra(LectureListActivity.EXTRA_CHAPTER_ID, chapter.id)
            })
        }
    }

    companion object {
        const val EXTRA_GRADE_ID = "grade_id"
    }
}
