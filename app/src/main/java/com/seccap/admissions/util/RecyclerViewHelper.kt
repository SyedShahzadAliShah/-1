package com.seccap.admissions.util

import androidx.recyclerview.widget.RecyclerView

object RecyclerViewHelper {

    fun setupNestedList(recyclerView: RecyclerView) {
        recyclerView.isNestedScrollingEnabled = false
        recyclerView.setHasFixedSize(false)
    }
}
