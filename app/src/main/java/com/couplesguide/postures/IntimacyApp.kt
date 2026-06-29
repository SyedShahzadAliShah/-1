package com.couplesguide.postures

import android.app.Application
import com.couplesguide.postures.util.LocaleHelper

class IntimacyApp : Application() {
    override fun attachBaseContext(base: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(base))
    }
}
