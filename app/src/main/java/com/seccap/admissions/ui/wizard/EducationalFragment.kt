package com.seccap.admissions.ui.wizard

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import androidx.fragment.app.Fragment
import com.seccap.admissions.ApplicationWizardActivity
import com.seccap.admissions.databinding.FragmentEducationalBinding

class EducationalFragment : Fragment() {

    private var _binding: FragmentEducationalBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentEducationalBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val activity = requireActivity() as ApplicationWizardActivity
        val draft = activity.draft

        binding.inputMatricRoll.setText(draft.matricRollNumber)
        binding.inputNinthRoll.setText(draft.ninthRollNumber)
        binding.inputBoard.setText(draft.boardName)
        binding.inputYear.setText(draft.passingYear)
        binding.inputTotalMarks.setText(draft.totalMarks)
        binding.inputObtainedMarks.setText(draft.obtainedMarks)
        binding.inputGrade.setText(draft.grade)
        binding.inputSchool.setText(draft.schoolName)

        val boards = listOf(
            "BISE Karachi", "BISE Hyderabad", "BISE Sukkur",
            "BISE Larkana", "BISE Mirpurkhas", "BISE Shaheed Benazirabad",
            "Aga Khan Board", "Cambridge", "Other"
        )
        binding.inputBoard.setAdapter(
            ArrayAdapter(requireContext(), android.R.layout.simple_dropdown_item_1line, boards)
        )
    }

    fun saveToDraft(activity: ApplicationWizardActivity) {
        val draft = activity.draft
        draft.matricRollNumber = binding.inputMatricRoll.text?.toString()?.trim() ?: ""
        draft.ninthRollNumber = binding.inputNinthRoll.text?.toString()?.trim() ?: ""
        draft.boardName = binding.inputBoard.text?.toString()?.trim() ?: ""
        draft.passingYear = binding.inputYear.text?.toString()?.trim() ?: ""
        draft.totalMarks = binding.inputTotalMarks.text?.toString()?.trim() ?: ""
        draft.obtainedMarks = binding.inputObtainedMarks.text?.toString()?.trim() ?: ""
        draft.grade = binding.inputGrade.text?.toString()?.trim() ?: ""
        draft.schoolName = binding.inputSchool.text?.toString()?.trim() ?: ""
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
