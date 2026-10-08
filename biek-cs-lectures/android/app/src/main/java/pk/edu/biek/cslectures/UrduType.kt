package pk.edu.biek.cslectures

import android.content.Context
import android.graphics.Typeface
import android.widget.TextView

object UrduType {
    private var face: Typeface? = null

    fun apply(context: Context, vararg views: TextView) {
        val typeface = face ?: Typeface.createFromAsset(context.assets, "fonts/NotoNaskhArabic-Regular.ttf")
            .also { face = it }
        views.forEach { it.typeface = typeface }
    }
}
