package com.sindhcs.whiteboard

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.sindhcs.whiteboard.data.CatalogStore
import com.sindhcs.whiteboard.databinding.ActivityLectureListBinding
import com.sindhcs.whiteboard.ui.LectureAdapter

class LectureListActivity : AppCompatActivity() {

    private lateinit var binding: ActivityLectureListBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLectureListBinding.inflate(layoutInflater)
        setContentView(binding.root)
        val chapter = CatalogStore.get(this).chapter(intent.getStringExtra(EXTRA_CHAPTER_ID) ?: "")
        setSupportActionBar(binding.toolbar)
        binding.toolbar.title = chapter.title
        binding.toolbar.setNavigationOnClickListener { finish() }
        binding.list.layoutManager = LinearLayoutManager(this)
        binding.list.adapter = LectureAdapter(chapter.lectures) { lecture ->
            startActivity(Intent(this, PlayerActivity::class.java).apply {
                putExtra(PlayerActivity.EXTRA_LECTURE_ID, lecture.id)
            })
        }
    }

    companion object {
        const val EXTRA_CHAPTER_ID = "chapter_id"
    }
}
