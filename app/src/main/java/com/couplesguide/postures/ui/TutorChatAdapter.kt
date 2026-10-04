package com.couplesguide.postures.ui

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.couplesguide.postures.databinding.ItemTutorMessageBotBinding
import com.couplesguide.postures.databinding.ItemTutorMessageUserBinding
import com.couplesguide.postures.tutor.TutorChatMessage

class TutorChatAdapter : ListAdapter<TutorChatMessage, RecyclerView.ViewHolder>(Diff) {

    override fun getItemViewType(position: Int): Int =
        if (getItem(position).role == TutorChatMessage.Role.USER) VIEW_USER else VIEW_TUTOR

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecyclerView.ViewHolder {
        val inflater = LayoutInflater.from(parent.context)
        return if (viewType == VIEW_USER) {
            UserHolder(ItemTutorMessageUserBinding.inflate(inflater, parent, false))
        } else {
            BotHolder(ItemTutorMessageBotBinding.inflate(inflater, parent, false))
        }
    }

    override fun onBindViewHolder(holder: RecyclerView.ViewHolder, position: Int) {
        val message = getItem(position)
        when (holder) {
            is UserHolder -> holder.binding.messageText.text = message.text
            is BotHolder -> holder.binding.messageText.text = message.text
        }
    }

    private class UserHolder(val binding: ItemTutorMessageUserBinding) : RecyclerView.ViewHolder(binding.root)
    private class BotHolder(val binding: ItemTutorMessageBotBinding) : RecyclerView.ViewHolder(binding.root)

    private object Diff : DiffUtil.ItemCallback<TutorChatMessage>() {
        override fun areItemsTheSame(a: TutorChatMessage, b: TutorChatMessage): Boolean =
            a.timestampMs == b.timestampMs && a.role == b.role

        override fun areContentsTheSame(a: TutorChatMessage, b: TutorChatMessage): Boolean =
            a.text == b.text
    }

    companion object {
        private const val VIEW_USER = 1
        private const val VIEW_TUTOR = 2
    }
}
