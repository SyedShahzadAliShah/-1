package com.sindh.cswhiteboard

import android.content.Intent
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.sindh.cswhiteboard.data.CurriculumRepository
import com.sindh.cswhiteboard.data.Prefs
import com.sindh.cswhiteboard.databinding.ActivityHomeBinding

class HomeActivity : AppCompatActivity() {

    private lateinit var binding: ActivityHomeBinding

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(Prefs.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityHomeBinding.inflate(layoutInflater)
        setContentView(binding.root)
        setSupportActionBar(binding.toolbar)

        val curriculum = CurriculumRepository.load(this)
        val xi = curriculum.classes.find { it.id == "xi" }
        val xii = curriculum.classes.find { it.id == "xii" }

        binding.badgeVersion.text = getString(R.string.version_badge, BuildConfig.VERSION_NAME)
        bindLanguage()
        bindGolden()

        xi?.let { pack ->
            binding.cardXiTitle.text = if (Prefs.isUrdu(this)) pack.titleUr else pack.titleEn
            binding.cardXiMeta.text = getString(
                R.string.class_meta,
                pack.lectureCount(),
                pack.goldenCount()
            )
            binding.cardXi.setOnClickListener { openClass("xi") }
        }
        xii?.let { pack ->
            binding.cardXiiTitle.text = if (Prefs.isUrdu(this)) pack.titleUr else pack.titleEn
            binding.cardXiiMeta.text = getString(
                R.string.class_meta,
                pack.lectureCount(),
                pack.goldenCount()
            )
            binding.cardXii.setOnClickListener { openClass("xii") }
        }

        binding.chipEn.setOnClickListener { setLang(Prefs.LANG_EN) }
        binding.chipUr.setOnClickListener { setLang(Prefs.LANG_UR) }
        binding.switchGolden.setOnCheckedChangeListener { _, checked ->
            Prefs.setGoldenOnly(this, checked)
        }
    }

    private fun bindLanguage() {
        val urdu = Prefs.isUrdu(this)
        binding.chipEn.isChecked = !urdu
        binding.chipUr.isChecked = urdu
    }

    private fun bindGolden() {
        binding.switchGolden.isChecked = Prefs.goldenOnly(this)
    }

    private fun setLang(lang: String) {
        if (Prefs.language(this) == lang) return
        Prefs.setLanguage(this, lang)
        recreate()
    }

    private fun openClass(id: String) {
        if (CurriculumRepository.classPack(this, id) == null) {
            Toast.makeText(this, R.string.missing_content, Toast.LENGTH_SHORT).show()
            return
        }
        startActivity(Intent(this, ChapterListActivity::class.java).putExtra(EXTRA_CLASS_ID, id))
    }

    companion object {
        const val EXTRA_CLASS_ID = "class_id"
        const val EXTRA_CHAPTER_ID = "chapter_id"
        const val EXTRA_LECTURE_ID = "lecture_id"
        const val EXTRA_PLAY_CHAPTER = "play_chapter"
    }
}
