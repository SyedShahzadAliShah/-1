package com.seccap.admissions.ui.wizard

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import androidx.fragment.app.Fragment
import com.seccap.admissions.ApplicationWizardActivity
import com.seccap.admissions.databinding.FragmentPersonalBinding

class PersonalFragment : Fragment() {

    private var _binding: FragmentPersonalBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentPersonalBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val activity = requireActivity() as ApplicationWizardActivity
        val draft = activity.draft

        binding.inputName.setText(draft.studentName)
        binding.inputFather.setText(draft.fatherName)
        binding.inputDob.setText(draft.dateOfBirth)
        binding.inputBform.setText(draft.bFormNumber)
        binding.inputCnic.setText(draft.cnicNumber)
        binding.inputPhone.setText(draft.phoneNumber)
        binding.inputEmail.setText(draft.email)
        binding.inputAddress.setText(draft.address)
        binding.inputDomicile.setText(draft.domicile)

        val genders = listOf("Male", "Female", "Other")
        binding.inputGender.setAdapter(
            ArrayAdapter(requireContext(), android.R.layout.simple_dropdown_item_1line, genders)
        )
        binding.inputGender.setText(draft.gender, false)

        val religions = listOf("Islam", "Christianity", "Hinduism", "Other")
        binding.inputReligion.setAdapter(
            ArrayAdapter(requireContext(), android.R.layout.simple_dropdown_item_1line, religions)
        )
        binding.inputReligion.setText(draft.religion, false)

        val domiciles = listOf(
            "Karachi", "Hyderabad", "Sukkur", "Larkana",
            "Mirpurkhas", "Shaheed Benazirabad", "Khairpur", "Other Sindh"
        )
        binding.inputDomicile.setAdapter(
            ArrayAdapter(requireContext(), android.R.layout.simple_dropdown_item_1line, domiciles)
        )
    }

    fun saveToDraft(activity: ApplicationWizardActivity) {
        val draft = activity.draft
        draft.studentName = binding.inputName.text?.toString()?.trim() ?: ""
        draft.fatherName = binding.inputFather.text?.toString()?.trim() ?: ""
        draft.gender = binding.inputGender.text?.toString()?.trim() ?: ""
        draft.dateOfBirth = binding.inputDob.text?.toString()?.trim() ?: ""
        draft.bFormNumber = binding.inputBform.text?.toString()?.trim() ?: ""
        draft.cnicNumber = binding.inputCnic.text?.toString()?.trim() ?: ""
        draft.religion = binding.inputReligion.text?.toString()?.trim() ?: ""
        draft.domicile = binding.inputDomicile.text?.toString()?.trim() ?: ""
        draft.phoneNumber = binding.inputPhone.text?.toString()?.trim() ?: ""
        draft.email = binding.inputEmail.text?.toString()?.trim() ?: ""
        draft.address = binding.inputAddress.text?.toString()?.trim() ?: ""
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
