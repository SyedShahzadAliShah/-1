package com.sindhcs.whiteboard

import android.content.Intent
import android.graphics.Typeface
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import com.sindhcs.whiteboard.data.Catalog
import com.sindhcs.whiteboard.data.CatalogStore
import com.sindhcs.whiteboard.data.Mark
import com.sindhcs.whiteboard.data.ProgressStore
import com.sindhcs.whiteboard.databinding.ActivityHomeBinding

class HomeActivity : AppCompatActivity() {

    private lateinit var binding: ActivityHomeBinding
    private lateinit var catalog: Catalog
    private lateinit var progress: ProgressStore

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityHomeBinding.inflate(layoutInflater)
        setContentView(binding.root)
        setSupportActionBar(binding.toolbar)
        catalog = CatalogStore.get(this)
        progress = ProgressStore(this)

        val hand = Typeface.createFromAsset(assets, "fonts/PatrickHand-Regular.ttf")
        binding.subtitle.typeface = hand

        val xi = catalog.grade("xi")
        val xii = catalog.grade("xii")
        binding.xiTitle.text = xi.title
        binding.xiMeta.text = getString(R.string.lectures_meta, xi.lectureCount, xi.boardCount)
        binding.xiiTitle.text = xii.title
        binding.xiiMeta.text = getString(R.string.lectures_meta, xii.lectureCount, xii.boardCount)
        binding.gradeXi.setOnClickListener { openGrade("xi") }
        binding.gradeXii.setOnClickListener { openGrade("xii") }

        binding.heroBoard.onDrawComplete = { binding.heroBoard.play() }
        binding.heroBoard.submit(heroMarks())
    }

    override fun onResume() {
        super.onResume()
        val lastId = progress.lastLectureId()
        val lecture = lastId?.let { id ->
            runCatching { catalog.lecture(id) }.getOrNull()
        }
        if (lecture == null) {
            binding.continueTitle.text = getString(R.string.no_continue)
            binding.continueCard.setOnClickListener(null)
            binding.continueCard.isClickable = false
        } else {
            val chapter = catalog.chapterOf(lecture.id)
            binding.continueTitle.text = listOfNotNull(chapter?.title, lecture.title).joinToString(" · ")
            binding.continueCard.isClickable = true
            binding.continueCard.setOnClickListener {
                startActivity(Intent(this, PlayerActivity::class.java).apply {
                    putExtra(PlayerActivity.EXTRA_LECTURE_ID, lecture.id)
                })
            }
        }
        binding.heroBoard.play()
    }

    override fun onPause() {
        binding.heroBoard.pause()
        super.onPause()
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        menuInflater.inflate(R.menu.menu_home, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        if (item.itemId == R.id.action_about) {
            AlertDialog.Builder(this)
                .setTitle(R.string.about)
                .setMessage(getString(R.string.about_body, BuildConfig.VERSION_NAME))
                .setPositiveButton(android.R.string.ok, null)
                .show()
            return true
        }
        return super.onOptionsItemSelected(item)
    }

    private fun openGrade(id: String) {
        startActivity(Intent(this, ChapterListActivity::class.java).apply {
            putExtra(ChapterListActivity.EXTRA_GRADE_ID, id)
        })
    }

    private fun heroMarks(): List<Mark> = listOf(
        Mark(k = "title", t = "A logic gate answers with 0 or 1"),
        Mark(k = "gates", items = listOf("AND", "OR", "NOT")),
        Mark(k = "bullet", t = "AND is 1 only when every input is 1")
    )
}
