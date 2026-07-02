package com.seccap.admissions.ui.wizard

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import com.seccap.admissions.ApplicationWizardActivity
import com.seccap.admissions.data.FacultyRepository
import com.seccap.admissions.databinding.FragmentFacultyBinding
import com.seccap.admissions.ui.FacultyAdapter

class FacultyFragment : Fragment() {

    private var _binding: FragmentFacultyBinding? = null
    private val binding get() = _binding!!
    private lateinit var adapter: FacultyAdapter

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentFacultyBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val activity = requireActivity() as ApplicationWizardActivity
        val language = activity.language
        val draft = activity.draft

        val pct = String.format("%.1f", draft.percentage)
        binding.marksInfo.text = getString(
            com.seccap.admissions.R.string.your_percentage,
            pct
        )

        val eligible = if (draft.percentage > 0) {
            FacultyRepository.eligibleFaculties(draft.percentage)
        } else {
            FacultyRepository.getAll()
        }

        adapter = FacultyAdapter(language, draft.facultyId) { faculty ->
            draft.facultyId = faculty.id
            adapter.setSelected(faculty.id)
            binding.selectionHint.text = faculty.description.get(language)
        }

        binding.facultyList.layoutManager = LinearLayoutManager(requireContext())
        binding.facultyList.adapter = adapter
        adapter.submitList(eligible)
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
