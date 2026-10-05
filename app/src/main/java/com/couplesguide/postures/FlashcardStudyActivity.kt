package com.couplesguide.postures

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.couplesguide.postures.data.LectureNotesRepository
import com.couplesguide.postures.databinding.ActivityFlashcardStudyBinding
import com.couplesguide.postures.teaching.FlashcardDeckBuilder
import com.couplesguide.postures.teaching.LessonStep
import com.couplesguide.postures.teaching.TeachingProgressStore
import com.couplesguide.postures.util.LocaleHelper

class FlashcardStudyActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_CHAPTER_ID = "flashcard_chapter_id"
    }

    private lateinit var binding: ActivityFlashcardStudyBinding
    private var cards: List<com.couplesguide.postures.teaching.Flashcard> = emptyList()
    private var index = 0
    private var showingBack = false
    private var chapterId: String = ""

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityFlashcardStudyBinding.inflate(layoutInflater)
        setContentView(binding.root)

        chapterId = intent.getStringExtra(EXTRA_CHAPTER_ID) ?: run {
            finish()
            return
        }
        LectureNotesRepository.ensureLoaded(this)
        val all = LectureNotesRepository.getClasses(this).flatMap { it.chapters }
        val language = LocaleHelper.getLanguage(this)
        cards = FlashcardDeckBuilder.forChapter(chapterId, language, all)
        if (cards.isEmpty()) {
            finish()
            return
        }

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = getString(R.string.teaching_flashcards_title)

        binding.flashcardCard.setOnClickListener { flipCard() }
        binding.btnPrevCard.setOnClickListener { move(-1) }
        binding.btnNextCard.setOnClickListener { move(1) }
        renderCard()
    }

    private fun flipCard() {
        showingBack = !showingBack
        renderCard()
    }

    private fun move(delta: Int) {
        if (index + delta >= cards.size - 1 && delta > 0) {
            TeachingProgressStore.markStepComplete(this, chapterId, LessonStep.FLASHCARDS)
        }
        index = (index + delta).coerceIn(0, cards.lastIndex)
        showingBack = false
        renderCard()
    }

    private fun renderCard() {
        val card = cards[index]
        binding.flashcardCounter.text = getString(
            R.string.flashcard_counter,
            index + 1,
            cards.size
        )
        val text = if (showingBack) {
            if (card.isGolden) "★ ${card.back}" else card.back
        } else {
            card.front
        }
        binding.flashcardText.text = text
    }

    override fun onSupportNavigateUp(): Boolean {
        finish()
        return true
    }
}
