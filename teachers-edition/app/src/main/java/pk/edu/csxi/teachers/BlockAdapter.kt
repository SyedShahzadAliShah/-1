package pk.edu.csxi.teachers

import android.content.Context
import android.graphics.Typeface
import android.text.SpannableStringBuilder
import android.text.Spanned
import android.text.style.StyleSpan
import android.util.TypedValue
import android.view.Gravity
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.LinearLayout
import android.widget.TextView
import androidx.core.content.ContextCompat
import androidx.recyclerview.widget.RecyclerView
import pk.edu.csxi.teachers.databinding.ItemBlockBinding

class BlockAdapter(
    private val items: List<Item>,
    private val onPlay: (Int) -> Unit,
    private val onFigure: () -> Unit,
) : RecyclerView.Adapter<BlockAdapter.Holder>() {

    var activePos = -1
        private set

    fun setActive(pos: Int) {
        val old = activePos
        activePos = pos
        if (old in items.indices) notifyItemChanged(old)
        if (pos in items.indices && pos != old) notifyItemChanged(pos)
    }

    class Holder(val b: ItemBlockBinding) : RecyclerView.ViewHolder(b.root)

    override fun getItemCount() = items.size

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int) =
        Holder(ItemBlockBinding.inflate(LayoutInflater.from(parent.context), parent, false))

    override fun onBindViewHolder(h: Holder, position: Int) {
        val item = items[position]
        val ctx = h.b.root.context
        val active = position == activePos
        resetStyle(h, ctx)

        when (item.kind) {
            Kind.TITLE -> text(h, item.text, 26f, bold = true, color = R.color.navy, center = true)
            Kind.H1 -> {
                text(h, item.text, 22f, bold = true, color = R.color.navy)
                h.b.root.setPadding(dp(ctx, 12), dp(ctx, 14), dp(ctx, 12), dp(ctx, 2))
            }
            Kind.H2 -> {
                text(h, item.text, 18f, bold = true, color = R.color.navy)
                h.b.root.setPadding(dp(ctx, 12), dp(ctx, 10), dp(ctx, 12), dp(ctx, 2))
            }
            Kind.H3 -> text(h, item.text, 16f, bold = true, color = R.color.teal_dark)
            Kind.BADGE -> {
                text(h, "\u2605 " + item.text, 13f, bold = true, color = R.color.white)
                h.b.card.setBackgroundResource(R.drawable.bg_badge)
                h.b.card.layoutParams = (h.b.card.layoutParams as ViewGroup.MarginLayoutParams).apply {
                    width = ViewGroup.LayoutParams.WRAP_CONTENT
                }
            }
            Kind.P -> text(h, item.text, 16f, color = R.color.ink)
            Kind.LI -> {
                val sb = SpannableStringBuilder("\u2022  ").append(item.text)
                val lead = item.lead
                if (lead != null && item.text.startsWith(lead)) {
                    sb.setSpan(StyleSpan(Typeface.BOLD), 3, 3 + lead.length, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE)
                }
                h.b.body.text = sb
                h.b.body.setTextSize(TypedValue.COMPLEX_UNIT_SP, 16f)
                h.b.body.setTextColor(ContextCompat.getColor(ctx, R.color.ink))
                h.b.root.setPadding(dp(ctx, 20), dp(ctx, 2), dp(ctx, 12), dp(ctx, 2))
            }
            Kind.NOTE -> {
                h.b.card.setBackgroundResource(R.drawable.bg_note)
                item.label?.let {
                    h.b.label.visibility = View.VISIBLE
                    h.b.label.text = it.uppercase()
                    h.b.label.setTextColor(ContextCompat.getColor(ctx, R.color.teal_dark))
                }
                text(h, item.text, 15f, color = R.color.ink)
            }
            Kind.TABLE_HEAD -> {
                h.b.card.setBackgroundResource(R.drawable.bg_table_head)
                text(h, item.text, 13f, bold = true, color = R.color.white)
                h.b.root.setPadding(dp(ctx, 12), dp(ctx, 8), dp(ctx, 12), 0)
            }
            Kind.TABLE_ROW -> bindRow(h, ctx, item)
            Kind.CODE -> {
                h.b.card.setBackgroundResource(R.drawable.bg_code)
                text(h, item.text, 13.5f, color = R.color.code_ink)
                h.b.body.typeface = Typeface.MONOSPACE
            }
            Kind.FIGURE -> {
                h.b.card.setBackgroundResource(R.drawable.bg_figure)
                h.b.label.visibility = View.VISIBLE
                h.b.label.text = ctx.getString(R.string.diagram)
                h.b.label.setTextColor(ContextCompat.getColor(ctx, R.color.muted))
                text(h, item.text, 14f, color = R.color.ink)
                h.b.figureButton.visibility = View.VISIBLE
                h.b.figureButton.setOnClickListener { onFigure() }
            }
        }

        h.b.speaker.visibility = if (item.audio != null) View.VISIBLE else View.GONE
        h.b.speaker.setColorFilter(
            ContextCompat.getColor(ctx, if (active) R.color.gold_dark else R.color.muted)
        )
        if (active) {
            h.b.card.setBackgroundResource(R.drawable.bg_active)
        }
        if (item.audio != null) {
            h.b.card.setOnClickListener { onPlay(position) }
        } else {
            h.b.card.setOnClickListener(null)
            h.b.card.isClickable = false
        }
    }

    private fun bindRow(h: Holder, ctx: Context, item: Item) {
        h.b.card.setBackgroundResource(R.drawable.bg_table_row)
        text(h, item.cells.firstOrNull().orEmpty(), 16f, bold = true, color = R.color.navy)
        h.b.cells.visibility = View.VISIBLE
        h.b.cells.removeAllViews()
        for (i in 1 until item.cells.size) {
            val colName = item.cols.getOrNull(i).orEmpty()
            if (colName.isNotBlank()) {
                h.b.cells.addView(TextView(ctx).apply {
                    text = colName.uppercase()
                    setTextSize(TypedValue.COMPLEX_UNIT_SP, 10.5f)
                    setTextColor(ContextCompat.getColor(ctx, R.color.muted))
                    typeface = Typeface.DEFAULT_BOLD
                    setPadding(0, dp(ctx, 6), 0, 0)
                })
            }
            h.b.cells.addView(TextView(ctx).apply {
                text = item.cells[i]
                setTextSize(TypedValue.COMPLEX_UNIT_SP, 15f)
                setTextColor(ContextCompat.getColor(ctx, R.color.ink))
            })
        }
        h.b.root.setPadding(dp(ctx, 12), 0, dp(ctx, 12), dp(ctx, 2))
    }

    private fun text(h: Holder, s: String, size: Float, bold: Boolean = false, color: Int, center: Boolean = false) {
        val ctx = h.b.root.context
        h.b.body.text = s
        h.b.body.setTextSize(TypedValue.COMPLEX_UNIT_SP, size)
        h.b.body.setTextColor(ContextCompat.getColor(ctx, color))
        h.b.body.setTypeface(null, if (bold) Typeface.BOLD else Typeface.NORMAL)
        h.b.body.gravity = if (center) Gravity.CENTER_HORIZONTAL else Gravity.START
    }

    private fun resetStyle(h: Holder, ctx: Context) {
        h.b.card.background = null
        h.b.card.layoutParams = (h.b.card.layoutParams as ViewGroup.MarginLayoutParams).apply {
            width = ViewGroup.LayoutParams.MATCH_PARENT
        }
        h.b.root.setPadding(dp(ctx, 12), dp(ctx, 3), dp(ctx, 12), dp(ctx, 3))
        h.b.label.visibility = View.GONE
        h.b.cells.visibility = View.GONE
        h.b.figureButton.visibility = View.GONE
        h.b.body.typeface = Typeface.DEFAULT
        h.b.body.gravity = Gravity.START
        h.b.body.setLineSpacing(0f, 1.15f)
    }

    private fun dp(ctx: Context, v: Int) = (v * ctx.resources.displayMetrics.density).toInt()
}
