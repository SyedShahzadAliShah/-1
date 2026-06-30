package com.couplesguide.postures.util

import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

object RecyclerViewHelper {

    /**
     * RecyclerViews inside NestedScrollView must not scroll independently;
     * otherwise they collapse to zero height and their items never appear.
     */
    fun setupNestedList(recyclerView: RecyclerView) {
        recyclerView.layoutManager = object : LinearLayoutManager(recyclerView.context) {
            override fun canScrollVertically(): Boolean = false
        }
        recyclerView.isNestedScrollingEnabled = false
        recyclerView.setHasFixedSize(false)
        recyclerView.overScrollMode = RecyclerView.OVER_SCROLL_NEVER
    }
}
