package com.sindh.csteach

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.sindh.csteach.databinding.ActivityHomeBinding

class HomeActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val binding = ActivityHomeBinding.inflate(layoutInflater)
        setContentView(binding.root)
        binding.openXi.setOnClickListener { open("xi") }
        binding.openXii.setOnClickListener { open("xii") }
    }

    private fun open(gradeId: String) {
        startActivity(Intent(this, PlayerActivity::class.java).putExtra(PlayerActivity.EXTRA_GRADE, gradeId))
    }
}
