package com.couplesguide.postures

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.couplesguide.postures.data.PostureRepository
import com.couplesguide.postures.databinding.ActivityPostureDetailBinding

class PostureDetailActivity : AppCompatActivity() {

    companion object {
        const val EXTRA_POSTURE_ID = "posture_id"
    }

    private lateinit var binding: ActivityPostureDetailBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityPostureDetailBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val postureId = intent.getStringExtra(EXTRA_POSTURE_ID)
        val posture = postureId?.let { PostureRepository.getPostureById(it) }

        if (posture == null) {
            finish()
            return
        }

        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
        supportActionBar?.title = posture.name

        binding.illustration.setImageResource(posture.illustrationRes)
        binding.postureName.text = posture.name
        binding.categoryBadge.text = posture.category
        binding.difficultyBadge.text = posture.difficulty.label
        binding.summaryText.text = posture.summary
        binding.descriptionText.text = posture.description

        binding.stepsList.text = posture.steps
            .mapIndexed { index, step -> "${index + 1}. $step" }
            .joinToString("\n\n")

        binding.tipsList.text = posture.tips
            .joinToString("\n\n") { "• $it" }
    }

    override fun onSupportNavigateUp(): Boolean {
        onBackPressedDispatcher.onBackPressed()
        return true
    }
}
