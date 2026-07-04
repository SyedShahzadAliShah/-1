package com.couplesguide.postures.ui

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import androidx.viewpager2.widget.ViewPager2
import com.couplesguide.postures.R
import com.couplesguide.postures.data.PdfPage

class PdfPageAdapter(
    private val pages: List<PdfPage>
) : RecyclerView.Adapter<PdfPageAdapter.PageViewHolder>() {

    inner class PageViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val pageImage: ImageView = itemView.findViewById(R.id.pageImage)
        val titleUrdu: TextView = itemView.findViewById(R.id.pageTitleUrdu)
        val titleEnglish: TextView = itemView.findViewById(R.id.pageTitleEnglish)
        val narrationUrdu: TextView = itemView.findViewById(R.id.pageNarrationUrdu)
        val narrationEnglish: TextView = itemView.findViewById(R.id.pageNarrationEnglish)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): PageViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_pdf_page, parent, false)
        return PageViewHolder(view)
    }

    override fun onBindViewHolder(holder: PageViewHolder, position: Int) {
        val page = pages[position]
        holder.pageImage.setImageResource(page.drawableRes)
        holder.titleUrdu.text = page.urduTitle
        holder.titleEnglish.text = page.englishTitle
        holder.narrationUrdu.text = page.urduNarration
        holder.narrationEnglish.text = page.englishNarration
    }

    override fun getItemCount(): Int = pages.size
}
