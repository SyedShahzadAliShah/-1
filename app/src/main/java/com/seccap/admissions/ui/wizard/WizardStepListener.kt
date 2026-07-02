package com.seccap.admissions.ui.wizard

interface WizardStepListener {
    fun onDraftUpdated()
    fun getLanguage(): String
}
