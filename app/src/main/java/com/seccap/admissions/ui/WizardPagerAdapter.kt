package com.seccap.admissions.ui

import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentActivity
import androidx.viewpager2.adapter.FragmentStateAdapter
import com.seccap.admissions.ui.wizard.CollegesFragment
import com.seccap.admissions.ui.wizard.DocumentsFragment
import com.seccap.admissions.ui.wizard.EducationalFragment
import com.seccap.admissions.ui.wizard.FacultyFragment
import com.seccap.admissions.ui.wizard.PersonalFragment
import com.seccap.admissions.ui.wizard.ReviewFragment

class WizardPagerAdapter(activity: FragmentActivity) : FragmentStateAdapter(activity) {

    override fun getItemCount(): Int = 6

    override fun createFragment(position: Int): Fragment = when (position) {
        0 -> EducationalFragment()
        1 -> PersonalFragment()
        2 -> FacultyFragment()
        3 -> CollegesFragment()
        4 -> DocumentsFragment()
        5 -> ReviewFragment()
        else -> EducationalFragment()
    }
}
