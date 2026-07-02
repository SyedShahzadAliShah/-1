package com.seccap.admissions.ui.wizard

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.seccap.admissions.ApplicationWizardActivity
import com.seccap.admissions.R
import com.seccap.admissions.data.CollegeRepository
import com.seccap.admissions.data.FacultyRepository
import com.seccap.admissions.databinding.FragmentReviewBinding

class ReviewFragment : Fragment() {

    private var _binding: FragmentReviewBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentReviewBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        refresh()
    }

    fun refresh() {
        val activity = requireActivity() as ApplicationWizardActivity
        val draft = activity.draft
        val language = activity.language

        binding.reviewId.text = getString(R.string.review_app_id, draft.applicationId)
        binding.reviewCompletion.text = getString(R.string.review_completion, draft.completionPercent())

        val sb = StringBuilder()

        sb.append("━━ ").append(getString(R.string.step_educational)).append(" ━━\n")
        if (draft.isEducationalComplete()) {
            sb.append(getString(R.string.review_matric, draft.matricRollNumber)).append("\n")
            sb.append(getString(R.string.review_board, draft.boardName, draft.passingYear)).append("\n")
            sb.append(getString(R.string.review_marks, draft.obtainedMarks, draft.totalMarks,
                String.format("%.1f", draft.percentage))).append("\n")
            sb.append(getString(R.string.review_school, draft.schoolName)).append("\n")
        } else {
            sb.append(getString(R.string.review_incomplete)).append("\n")
        }

        sb.append("\n━━ ").append(getString(R.string.step_personal)).append(" ━━\n")
        if (draft.isPersonalComplete()) {
            sb.append(getString(R.string.review_name, draft.studentName)).append("\n")
            sb.append(getString(R.string.review_father, draft.fatherName)).append("\n")
            sb.append(getString(R.string.review_bform, draft.bFormNumber)).append("\n")
            sb.append(getString(R.string.review_phone, draft.phoneNumber)).append("\n")
        } else {
            sb.append(getString(R.string.review_incomplete)).append("\n")
        }

        sb.append("\n━━ ").append(getString(R.string.step_faculty)).append(" ━━\n")
        val faculty = FacultyRepository.findById(draft.facultyId)
        sb.append(faculty?.name?.get(language) ?: getString(R.string.review_not_selected)).append("\n")

        sb.append("\n━━ ").append(getString(R.string.step_colleges)).append(" ━━\n")
        val zone = CollegeRepository.findZone(draft.zoneId)
        sb.append(zone?.name?.get(language) ?: getString(R.string.review_not_selected)).append("\n")
        draft.collegePreferences.forEachIndexed { i, id ->
            val college = CollegeRepository.findCollege(id)
            sb.append("${i + 1}. ${college?.name?.get(language) ?: id}\n")
        }

        sb.append("\n━━ ").append(getString(R.string.step_documents)).append(" ━━\n")
        sb.append(getString(R.string.review_docs_prepared, draft.documentsChecked.size))

        binding.reviewContent.text = sb.toString()
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
