package com.sindh.cswhiteboard

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.sindh.cswhiteboard.data.CurriculumRepository
import com.sindh.cswhiteboard.data.Prefs
import com.sindh.cswhiteboard.databinding.ActivityChapterListBinding
import com.sindh.cswhiteboard.ui.ChapterAdapter

class ChapterListActivity : AppCompatActivity() {

    private lateinit var binding: ActivityChapterListBinding

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(Prefs.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityChapterListBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val classId = intent.getStringExtra(HomeActivity.EXTRA_CLASS_ID) ?: return finish()
        val pack = CurriculumRepository.classPack(this, classId) ?: return finish()
        val urdu = Prefs.isUrdu(this)

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        binding.toolbar.setNavigationOnClickListener { finish() }
        binding.toolbar.title = if (urdu) pack.titleUr else pack.titleEn
        binding.subtitle.text = if (urdu) pack.subtitleUr else pack.subtitleEn

        binding.list.layoutManager = LinearLayoutManager(this)
        binding.list.adapter = ChapterAdapter(pack.chapters, urdu) { chapter ->
            startActivity(
                Intent(this, LectureListActivity::class.java)
                    .putExtra(HomeActivity.EXTRA_CLASS_ID, classId)
                    .putExtra(HomeActivity.EXTRA_CHAPTER_ID, chapter.id)
            )
        }
    }
}
