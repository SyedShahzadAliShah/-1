package com.couplesguide.postures

import android.content.Intent
import android.os.Bundle
import android.view.View
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.couplesguide.postures.data.PostureRepository
import com.couplesguide.postures.databinding.ActivityMainBinding
import com.couplesguide.postures.ui.CategoryAdapter
import com.couplesguide.postures.ui.PostureAdapter

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private lateinit var postureAdapter: PostureAdapter
    private var selectedCategory = "All"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        setSupportActionBar(binding.toolbar)

        postureAdapter = PostureAdapter { posture ->
            val intent = Intent(this, PostureDetailActivity::class.java).apply {
                putExtra(PostureDetailActivity.EXTRA_POSTURE_ID, posture.id)
            }
            startActivity(intent)
        }

        binding.postureList.layoutManager = LinearLayoutManager(this)
        binding.postureList.adapter = postureAdapter

        setupCategories()
        updatePostureList()
    }

    private fun setupCategories() {
        val categoryAdapter = CategoryAdapter(PostureRepository.categories) { category ->
            selectedCategory = category
            updatePostureList()
        }
        binding.categoryList.layoutManager =
            LinearLayoutManager(this, LinearLayoutManager.HORIZONTAL, false)
        binding.categoryList.adapter = categoryAdapter
    }

    private fun updatePostureList() {
        val postures = PostureRepository.getPosturesByCategory(selectedCategory)
        postureAdapter.submitList(postures)
        binding.emptyText.visibility = if (postures.isEmpty()) View.VISIBLE else View.GONE
    }
}
