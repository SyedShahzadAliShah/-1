package pk.edu.biek.cslectures

import android.content.Intent
import android.os.Bundle
import android.view.LayoutInflater
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import pk.edu.biek.cslectures.data.Catalog
import pk.edu.biek.cslectures.databinding.ActivityLectureBinding
import pk.edu.biek.cslectures.databinding.ItemConceptBinding
import pk.edu.biek.cslectures.model.Lecture

class LectureActivity : AppCompatActivity() {
    private lateinit var binding: ActivityLectureBinding
    private lateinit var lecture: Lecture
    private lateinit var narrator: LectureNarrator
    private val cards = mutableListOf<ItemConceptBinding>()
    private var playing = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityLectureBinding.inflate(layoutInflater)
        setContentView(binding.root)
        lecture = Catalog.find(intent.getStringExtra(EXTRA_ID) ?: return finish())
        binding.kicker.text = "Class ${lecture.year}  ·  Lecture ${lecture.number}"
        binding.title.text = lecture.title
        binding.urduTitle.text = lecture.urduTitle
        binding.intro.text = lecture.introUrdu
        UrduType.apply(this, binding.urduTitle, binding.intro)

        val inflater = LayoutInflater.from(this)
        lecture.concepts.forEachIndexed { index, concept ->
            val card = ItemConceptBinding.inflate(inflater, binding.concepts, true)
            card.term.text = concept.term
            card.english.text = concept.english
            card.urdu.text = concept.urdu
            UrduType.apply(this, card.urdu)
            card.listen.setOnClickListener {
                markSpeaking(index)
                narrator.speakOne(index, concept)
            }
            cards += card
        }

        narrator = LectureNarrator(
            this,
            onReady = { urdu ->
                binding.voiceBanner.visibility = if (urdu) android.view.View.GONE else android.view.View.VISIBLE
                binding.voiceBanner.setOnClickListener { LectureNarrator.openVoiceSettings(this) }
            },
            onConcept = { index -> markSpeaking(index) },
            onIdle = {
                playing = false
                binding.playLecture.text = getString(R.string.play_lecture)
                markSpeaking(-1)
            },
        )

        binding.playLecture.setOnClickListener {
            if (playing) {
                narrator.stop()
            } else {
                playing = true
                binding.playLecture.text = getString(R.string.stop)
                narrator.speakAll(lecture.concepts)
            }
        }
        binding.openPdf.setOnClickListener {
            startActivity(
                Intent(this, PdfActivity::class.java)
                    .putExtra(PdfActivity.EXTRA_ASSET, lecture.pdfAsset)
                    .putExtra(PdfActivity.EXTRA_TITLE, lecture.title)
            )
        }
    }

    private fun markSpeaking(index: Int) {
        val normal = ContextCompat.getColor(this, R.color.white)
        val active = ContextCompat.getColor(this, R.color.speaking)
        cards.forEachIndexed { cardIndex, card ->
            card.conceptCard.setCardBackgroundColor(if (cardIndex == index) active else normal)
        }
    }

    override fun onDestroy() {
        narrator.shutdown()
        super.onDestroy()
    }

    companion object {
        const val EXTRA_ID = "lecture_id"
    }
}
