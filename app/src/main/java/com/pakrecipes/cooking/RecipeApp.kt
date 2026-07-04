package com.pakrecipes.cooking

import android.app.Application
import android.content.Context
import android.content.res.Configuration
import java.util.Locale

class RecipeApp : Application() {

    override fun attachBaseContext(base: Context) {
        super.attachBaseContext(applyUrduLocale(base))
    }

    override fun onConfigurationChanged(newConfig: Configuration) {
        super.onConfigurationChanged(newConfig)
        applyUrduLocale(this)
    }

    companion object {
        fun applyUrduLocale(context: Context): Context {
            val locale = Locale("ur", "PK")
            Locale.setDefault(locale)
            val config = Configuration(context.resources.configuration)
            config.setLocale(locale)
            config.setLayoutDirection(locale)
            return context.createConfigurationContext(config)
        }
    }
}
