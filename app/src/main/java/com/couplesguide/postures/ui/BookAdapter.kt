package com.couplesguide.postures.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.couplesguide.postures.data.CsBook
import com.couplesguide.postures.databinding.ItemBookBinding

class BookAdapter(
    private val onBookClick: (CsBook) -> Unit
) : RecyclerView.Adapter<BookAdapter.ViewHolder>() {

    private var books: List<CsBook> = emptyList()

    fun submitList(list: List<CsBook>) {
        books = list
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val binding = ItemBookBinding.inflate(
            LayoutInflater.from(parent.context),
            parent,
            false
        )
        return ViewHolder(binding)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(books[position])
    }

    override fun getItemCount() = books.size

    inner class ViewHolder(
        private val binding: ItemBookBinding
    ) : RecyclerView.ViewHolder(binding.root) {

        fun bind(book: CsBook) {
            binding.bookTitle.text = book.title
            binding.bookMeta.text = "${book.subtitle}\n${book.topics.size} lecture topics"
            binding.root.setOnClickListener { onBookClick(book) }
        }
    }
}
