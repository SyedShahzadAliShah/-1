package com.couplesguide.postures

import android.os.Bundle
import android.view.View
import android.widget.RadioButton
import androidx.appcompat.app.AppCompatActivity
import com.couplesguide.postures.data.LectureNotesRepository
import com.couplesguide.postures.data.StudyChapter
import com.couplesguide.postures.databinding.ActivityChapterQuizBinding
import com.couplesguide.postures.teaching.TeachingProgressStore
import com.couplesguide.postures.teaching.TeachingQuizBank
import com.couplesguide.postures.util.LocaleHelper

class ChapterQuizActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_CHAPTER_ID = "quiz_chapter_id"
    }

    private lateinit var binding: ActivityChapterQuizBinding
    private lateinit var chapter: StudyChapter
    private var questions: List<com.couplesguide.postures.teaching.QuizQuestion> = emptyList()
    private var questionIndex = 0
    private var correctCount = 0

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityChapterQuizBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val chapterId = intent.getStringExtra(EXTRA_CHAPTER_ID)
        val found = chapterId?.let { LectureNotesRepository.getChapterById(this, it) }
        if (found == null) {
            finish()
            return
        }
        chapter = found
        LectureNotesRepository.ensureLoaded(this)
        val all = LectureNotesRepository.getClasses(this).flatMap { it.chapters }
        val useUrdu = LocaleHelper.getLanguage(this) == LocaleHelper.LANG_UR
        questions = TeachingQuizBank.buildSession(chapter, all, useUrdu)

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = getString(R.string.teaching_quiz_title)

        binding.btnSubmitAnswer.setOnClickListener { submitAnswer() }
        showQuestion()
    }

    private fun showQuestion() {
        binding.quizResult.visibility = View.GONE
        if (questionIndex >= questions.size) {
            showFinalScore()
            return
        }
        val q = questions[questionIndex]
        binding.quizProgress.text = getString(
            R.string.quiz_question_progress,
            questionIndex + 1,
            questions.size
        )
        binding.quizQuestion.text = q.prompt
        binding.quizCitationHint.text = getString(R.string.quiz_cite_hint, q.citationHint)
        binding.quizChoices.clearCheck()
        binding.quizChoices.removeAllViews()
        q.choices.forEachIndexed { i, choice ->
            val radio = RadioButton(this).apply {
                id = View.generateViewId()
                text = choice
                tag = i
            }
            binding.quizChoices.addView(radio)
        }
    }

    private fun submitAnswer() {
        val checkedId = binding.quizChoices.checkedRadioButtonId
        if (checkedId == -1) return
        val selected = binding.quizChoices.findViewById<RadioButton>(checkedId)
        val selectedIndex = selected?.tag as? Int ?: return
        val q = questions[questionIndex]
        if (selectedIndex == q.correctIndex) {
            correctCount++
        }
        questionIndex++
        showQuestion()
    }

    private fun showFinalScore() {
        binding.quizChoices.visibility = View.GONE
        binding.btnSubmitAnswer.visibility = View.GONE
        binding.quizQuestion.visibility = View.GONE
        binding.quizCitationHint.visibility = View.GONE
        binding.quizProgress.visibility = View.GONE
        binding.quizResult.visibility = View.VISIBLE
        val total = questions.size
        val percent = if (total > 0) (correctCount * 100) / total else 0
        TeachingProgressStore.saveQuizResult(this, chapter.id, correctCount, total)
        binding.quizResult.text = getString(
            R.string.quiz_final_score,
            correctCount,
            total,
            percent
        )
    }

    override fun onSupportNavigateUp(): Boolean {
        finish()
        return true
    }
}
