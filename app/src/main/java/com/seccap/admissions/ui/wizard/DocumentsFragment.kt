package com.seccap.admissions.ui.wizard

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.google.android.material.checkbox.MaterialCheckBox
import com.seccap.admissions.ApplicationWizardActivity
import com.seccap.admissions.data.GuideRepository
import com.seccap.admissions.databinding.FragmentDocumentsBinding

class DocumentsFragment : Fragment() {

    private var _binding: FragmentDocumentsBinding? = null
    private val binding get() = _binding!!
    private val checkboxes = mutableMapOf<String, MaterialCheckBox>()

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentDocumentsBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val activity = requireActivity() as ApplicationWizardActivity
        val language = activity.language
        val draft = activity.draft

        binding.docContainer.removeAllViews()
        checkboxes.clear()

        for (doc in GuideRepository.getRequiredDocuments()) {
            val cb = MaterialCheckBox(requireContext()).apply {
                text = "${doc.name.get(language)}\n${doc.description.get(language)}"
                isChecked = doc.id in draft.documentsChecked
                setOnCheckedChangeListener { _, _ -> updateDraft(activity) }
            }
            checkboxes[doc.id] = cb
            binding.docContainer.addView(cb)
        }
    }

    private fun updateDraft(activity: ApplicationWizardActivity) {
        activity.draft.documentsChecked = checkboxes
            .filter { it.value.isChecked }
            .keys
            .toSet()
    }

    fun saveToDraft(activity: ApplicationWizardActivity) {
        updateDraft(activity)
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
