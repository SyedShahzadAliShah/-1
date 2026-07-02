package com.seccap.admissions.ui.wizard

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import com.google.android.material.chip.Chip
import com.seccap.admissions.ApplicationWizardActivity
import com.seccap.admissions.R
import com.seccap.admissions.data.CollegeRepository
import com.seccap.admissions.databinding.FragmentCollegesBinding
import com.seccap.admissions.ui.CollegePickAdapter

class CollegesFragment : Fragment() {

    private var _binding: FragmentCollegesBinding? = null
    private val binding get() = _binding!!
    private lateinit var collegeAdapter: CollegePickAdapter
    private val selected = mutableListOf<String>()

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentCollegesBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val activity = requireActivity() as ApplicationWizardActivity
        val language = activity.language
        val draft = activity.draft

        selected.clear()
        selected.addAll(draft.collegePreferences)

        val zones = CollegeRepository.getZones()
        val zoneNames = zones.map { it.name.get(language) }
        binding.inputZone.setAdapter(
            ArrayAdapter(requireContext(), android.R.layout.simple_dropdown_item_1line, zoneNames)
        )

        val currentZone = CollegeRepository.findZone(draft.zoneId)
        if (currentZone != null) {
            binding.inputZone.setText(currentZone.name.get(language), false)
            loadColleges(activity)
        }

        binding.inputZone.setOnItemClickListener { _, _, position, _ ->
            draft.zoneId = zones[position].id
            selected.clear()
            loadColleges(activity)
            updateChips(language)
        }

        collegeAdapter = CollegePickAdapter(language, selected) { college ->
            if (college.id in selected) {
                selected.remove(college.id)
            } else if (selected.size < 5) {
                selected.add(college.id)
            }
            collegeAdapter.setSelected(selected.toSet())
            updateChips(language)
            binding.preferenceCount.text = getString(R.string.preferences_count, selected.size)
        }

        binding.collegeList.layoutManager = LinearLayoutManager(requireContext())
        binding.collegeList.adapter = collegeAdapter
        updateChips(language)
        binding.preferenceCount.text = getString(R.string.preferences_count, selected.size)
    }

    private fun loadColleges(activity: ApplicationWizardActivity) {
        val draft = activity.draft
        val colleges = CollegeRepository.collegesInZone(draft.zoneId, draft.facultyId.ifBlank { null })
        collegeAdapter.submitList(colleges)
        collegeAdapter.setSelected(selected.toSet())
    }

    private fun updateChips(language: String) {
        binding.chipGroup.removeAllViews()
        selected.forEachIndexed { index, collegeId ->
            val college = CollegeRepository.findCollege(collegeId) ?: return@forEachIndexed
            val chip = Chip(requireContext()).apply {
                text = "${index + 1}. ${college.name.get(language)}"
                isCloseIconVisible = true
                setOnCloseIconClickListener {
                    selected.remove(collegeId)
                    collegeAdapter.setSelected(selected.toSet())
                    updateChips(language)
                    binding.preferenceCount.text = getString(R.string.preferences_count, selected.size)
                }
            }
            binding.chipGroup.addView(chip)
        }
    }

    fun saveToDraft(activity: ApplicationWizardActivity) {
        activity.draft.collegePreferences = selected.toList()
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
