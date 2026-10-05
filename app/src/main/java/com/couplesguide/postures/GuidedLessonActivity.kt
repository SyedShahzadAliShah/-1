package com.couplesguide.postures

import android.content.Intent
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.couplesguide.postures.data.LectureNotesRepository
import com.couplesguide.postures.data.StudyChapter
import com.couplesguide.postures.databinding.ActivityGuidedLessonBinding
import com.couplesguide.postures.teaching.LessonStep
import com.couplesguide.postures.teaching.TeachingProgressStore
import com.couplesguide.postures.tutor.BootcampCitation
import com.couplesguide.postures.ui.LessonStepAdapter
import com.couplesguide.postures.ui.LessonStepUi
import com.couplesguide.postures.util.LocaleHelper
import com.couplesguide.postures.util.RecyclerViewHelper

class GuidedLessonActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_CHAPTER_ID = "guided_lesson_chapter_id"
    }

    private lateinit var binding: ActivityGuidedLessonBinding
    private lateinit var chapter: StudyChapter
    private var language = LocaleHelper.LANG_EN
    private lateinit var stepAdapter: LessonStepAdapter

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityGuidedLessonBinding.inflate(layoutInflater)
        setContentView(binding.root)

        language = LocaleHelper.getLanguage(this)
        val chapterId = intent.getStringExtra(EXTRA_CHAPTER_ID)
        val found = chapterId?.let { LectureNotesRepository.getChapterById(this, it) }
        if (found == null) {
            finish()
            return
        }
        chapter = found

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = chapter.content(language).title

        val useUrdu = language == LocaleHelper.LANG_UR
        binding.lessonCitation.text = BootcampCitation.forChapter(this, chapter, useUrdu)

        stepAdapter = LessonStepAdapter(
            onAction = { step -> runStep(step) },
            onMarkDone = { step -> markDone(step) }
        )
        RecyclerViewHelper.setupNestedList(binding.lessonStepsList)
        binding.lessonStepsList.layoutManager = LinearLayoutManager(this)
        binding.lessonStepsList.adapter = stepAdapter

        refreshSteps()
    }

    override fun onResume() {
        super.onResume()
        refreshSteps()
    }

    private fun refreshSteps() {
        val percent = TeachingProgressStore.chapterProgressPercent(this, chapter.id)
        binding.lessonProgressBar.max = 100
        binding.lessonProgressBar.progress = percent
        binding.lessonProgressLabel.text = getString(R.string.teaching_lesson_progress, percent)
        stepAdapter.submitList(buildStepUi())
    }

    private fun buildStepUi(): List<LessonStepUi> {
        val content = chapter.content(language)
        return LessonStep.all.map { step ->
            val complete = TeachingProgressStore.isStepComplete(this, chapter.id, step)
            val (title, desc, action) = when (step) {
                LessonStep.OBJECTIVES -> Triple(
                    getString(R.string.teaching_step_objectives),
                    content.keyPoints.take(3).joinToString("\n") { "• $it" },
                    getString(R.string.teaching_action_view_objectives)
                )
                LessonStep.LECTURE -> Triple(
                    getString(R.string.teaching_step_lecture),
                    getString(R.string.teaching_step_lecture_desc, chapter.pdfPageStart, chapter.pdfPageEnd),
                    getString(R.string.teaching_action_open_cinematic)
                )
                LessonStep.READ -> Triple(
                    getString(R.string.teaching_step_read),
                    content.summary,
                    getString(R.string.teaching_action_open_notes)
                )
                LessonStep.FLASHCARDS -> Triple(
                    getString(R.string.teaching_step_flashcards),
                    getString(R.string.teaching_step_flashcards_desc),
                    getString(R.string.teaching_action_flashcards)
                )
                LessonStep.QUIZ -> Triple(
                    getString(R.string.teaching_step_quiz),
                    getString(
                        R.string.teaching_step_quiz_desc,
                        TeachingProgressStore.getQuizBestPercent(this, chapter.id)
                    ),
                    getString(R.string.teaching_action_quiz)
                )
                LessonStep.REFLECT -> Triple(
                    getString(R.string.teaching_step_reflect),
                    getString(R.string.teaching_step_reflect_desc),
                    getString(R.string.teaching_action_tutor)
                )
            }
            LessonStepUi(step, title, desc, action, complete)
        }
    }

    private fun runStep(step: LessonStep) {
        when (step) {
            LessonStep.OBJECTIVES -> showObjectivesDialog()
            LessonStep.LECTURE -> openCinematic()
            LessonStep.READ -> openChapterNotes()
            LessonStep.FLASHCARDS -> openFlashcards()
            LessonStep.QUIZ -> openQuiz()
            LessonStep.REFLECT -> openTutor()
        }
    }

    private fun markDone(step: LessonStep) {
        TeachingProgressStore.markStepComplete(this, chapter.id, step)
        Toast.makeText(this, R.string.teaching_step_marked, Toast.LENGTH_SHORT).show()
        refreshSteps()
    }

    private fun showObjectivesDialog() {
        val content = chapter.content(language)
        val body = buildString {
            append(getString(R.string.teaching_objectives_intro))
            append("\n\n")
            content.keyPoints.forEach { append("• ").append(it).append("\n") }
        }
        AlertDialog.Builder(this)
            .setTitle(R.string.teaching_step_objectives)
            .setMessage(body)
            .setPositiveButton(R.string.teaching_mark_step_done) { _, _ ->
                markDone(LessonStep.OBJECTIVES)
            }
            .setNegativeButton(android.R.string.cancel, null)
            .show()
    }

    private fun openCinematic() {
        startActivity(Intent(this, LectureCinematicActivity::class.java).apply {
            putExtra(LectureCinematicActivity.EXTRA_CLASS_ID, chapter.id.substringBefore("_ch"))
            putExtra(LectureCinematicActivity.EXTRA_START_PAGE, chapter.pdfPageStart)
            putExtra(LectureCinematicActivity.EXTRA_END_PAGE, chapter.pdfPageEnd)
            putExtra(LectureCinematicActivity.EXTRA_AUTO_PLAY, true)
        })
        TeachingProgressStore.markStepComplete(this, chapter.id, LessonStep.LECTURE)
    }

    private fun openChapterNotes() {
        startActivity(Intent(this, StudyChapterDetailActivity::class.java).apply {
            putExtra(StudyChapterDetailActivity.EXTRA_CHAPTER_ID, chapter.id)
        })
        TeachingProgressStore.markStepComplete(this, chapter.id, LessonStep.READ)
    }

    private fun openFlashcards() {
        startActivity(Intent(this, FlashcardStudyActivity::class.java).apply {
            putExtra(FlashcardStudyActivity.EXTRA_CHAPTER_ID, chapter.id)
        })
    }

    private fun openQuiz() {
        startActivity(Intent(this, ChapterQuizActivity::class.java).apply {
            putExtra(ChapterQuizActivity.EXTRA_CHAPTER_ID, chapter.id)
        })
    }

    private fun openTutor() {
        startActivity(Intent(this, AiTutorActivity::class.java).apply {
            putExtra(AiTutorActivity.EXTRA_CHAPTER_ID, chapter.id)
            putExtra(AiTutorActivity.EXTRA_CLASS_ID, chapter.id.substringBefore("_ch"))
            putExtra(AiTutorActivity.EXTRA_PAGE, chapter.pdfPageStart)
            putExtra(AiTutorActivity.EXTRA_SEED_MESSAGE, "Explain the main ideas of this chapter with Bootcamp citations")
        })
        TeachingProgressStore.markStepComplete(this, chapter.id, LessonStep.REFLECT)
    }

    override fun onSupportNavigateUp(): Boolean {
        finish()
        return true
    }
}
