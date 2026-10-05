package com.couplesguide.postures

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.couplesguide.postures.data.LectureNotesRepository
import com.couplesguide.postures.databinding.ActivityTeachingStudioBinding
import com.couplesguide.postures.teaching.LessonPlanner
import com.couplesguide.postures.teaching.LessonStep
import com.couplesguide.postures.teaching.TeachingProgressStore
import com.couplesguide.postures.ui.TeachingCurriculumAdapter
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.RecyclerViewHelper

class TeachingStudioActivity : AppCompatActivity() {

    private lateinit var binding: ActivityTeachingStudioBinding
    private var language = LocaleHelper.LANG_EN
    private lateinit var adapter: TeachingCurriculumAdapter

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityTeachingStudioBinding.inflate(layoutInflater)
        setContentView(binding.root)

        language = LocaleHelper.getLanguage(this)
        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = getString(R.string.teaching_studio_title)

        LectureNotesRepository.ensureLoaded(this)

        adapter = TeachingCurriculumAdapter(language) { chapter ->
            openGuidedLesson(chapter.id)
        }
        RecyclerViewHelper.setupNestedList(binding.curriculumList)
        binding.curriculumList.layoutManager = LinearLayoutManager(this)
        binding.curriculumList.adapter = adapter

        val allChapters = LectureNotesRepository.getClasses(this).flatMap { it.chapters }
        adapter.submitList(allChapters)

        binding.btnContinueLesson.setOnClickListener {
            val next = LessonPlanner.suggestNextChapter(this) ?: return@setOnClickListener
            openGuidedLesson(next.id)
        }

        refreshDashboard()
    }

    override fun onResume() {
        super.onResume()
        refreshDashboard()
        val allChapters = LectureNotesRepository.getClasses(this).flatMap { it.chapters }
        adapter.submitList(allChapters)
    }

    private fun refreshDashboard() {
        val overall = TeachingProgressStore.overallProgressPercent(this)
        val completed = TeachingProgressStore.completedChapterCount(this)
        val total = LectureNotesRepository.getClasses(this).flatMap { it.chapters }.size
        binding.overallProgressBar.max = 100
        binding.overallProgressBar.progress = overall
        binding.overallProgressLabel.text = getString(
            R.string.teaching_overall_progress,
            overall,
            completed,
            total
        )

        val nextChapter = LessonPlanner.suggestNextChapter(this)
        if (nextChapter == null) {
            binding.continueLessonTitle.text = getString(R.string.teaching_all_complete_title)
            binding.continueLessonStep.text = getString(R.string.teaching_all_complete_body)
            return
        }
        val title = nextChapter.content(language).title
        binding.continueLessonTitle.text = getString(R.string.teaching_next_chapter, title)
        val step = LessonPlanner.nextIncompleteStep(this, nextChapter.id) ?: LessonStep.REFLECT
        binding.continueLessonStep.text = stepLabel(step)
    }

    private fun stepLabel(step: LessonStep): String {
        return when (step) {
            LessonStep.OBJECTIVES -> getString(R.string.teaching_step_objectives)
            LessonStep.LECTURE -> getString(R.string.teaching_step_lecture)
            LessonStep.READ -> getString(R.string.teaching_step_read)
            LessonStep.FLASHCARDS -> getString(R.string.teaching_step_flashcards)
            LessonStep.QUIZ -> getString(R.string.teaching_step_quiz)
            LessonStep.REFLECT -> getString(R.string.teaching_step_reflect)
        }
    }

    private fun openGuidedLesson(chapterId: String) {
        startActivity(Intent(this, GuidedLessonActivity::class.java).apply {
            putExtra(GuidedLessonActivity.EXTRA_CHAPTER_ID, chapterId)
        })
    }

    override fun onSupportNavigateUp(): Boolean {
        finish()
        return true
    }
}
