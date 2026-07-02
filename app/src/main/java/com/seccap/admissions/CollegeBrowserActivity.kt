package com.seccap.admissions

import android.os.Bundle
import android.widget.ArrayAdapter
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import com.seccap.admissions.data.CollegeRepository
import com.seccap.admissions.databinding.ActivityCollegeBrowserBinding
import com.seccap.admissions.ui.CollegeAdapter
import com.seccap.admissions.util.LocaleHelper

class CollegeBrowserActivity : AppCompatActivity() {

    private lateinit var binding: ActivityCollegeBrowserBinding
    private var language = LocaleHelper.LANG_EN
    private lateinit var adapter: CollegeAdapter

    override fun attachBaseContext(newBase: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(newBase))
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityCollegeBrowserBinding.inflate(layoutInflater)
        setContentView(binding.root)

        language = LocaleHelper.getLanguage(this)
        setSupportActionBar(binding.toolbar)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)

        adapter = CollegeAdapter(language)
        binding.collegeList.layoutManager = LinearLayoutManager(this)
        binding.collegeList.adapter = adapter

        val zones = CollegeRepository.getZones()
        val zoneNames = listOf(getString(R.string.all_zones)) + zones.map { it.name.get(language) }
        binding.zoneFilter.setAdapter(
            ArrayAdapter(this, android.R.layout.simple_dropdown_item_1line, zoneNames)
        )
        binding.zoneFilter.setText(zoneNames[0], false)

        binding.zoneFilter.setOnItemClickListener { _, _, position, _ ->
            if (position == 0) {
                adapter.submitList(CollegeRepository.getColleges())
            } else {
                adapter.submitList(CollegeRepository.collegesInZone(zones[position - 1].id))
            }
        }

        adapter.submitList(CollegeRepository.getColleges())
    }

    override fun onSupportNavigateUp(): Boolean {
        finish()
        return true
    }
}
