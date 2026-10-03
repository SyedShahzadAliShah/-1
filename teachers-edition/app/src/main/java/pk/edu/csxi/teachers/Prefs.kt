package pk.edu.csxi.teachers

import android.content.Context

class Prefs(context: Context) {
    private val sp = context.getSharedPreferences("csxi", Context.MODE_PRIVATE)

    var lastPage: Int
        get() = sp.getInt("last_page", 0)
        set(v) = sp.edit().putInt("last_page", v).apply()

    var speed: Float
        get() = sp.getFloat("speed", 1.0f)
        set(v) = sp.edit().putFloat("speed", v).apply()

    var autoAdvance: Boolean
        get() = sp.getBoolean("auto_advance", true)
        set(v) = sp.edit().putBoolean("auto_advance", v).apply()
}
