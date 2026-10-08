package com.couplesguide.postures

import android.app.Application
import com.couplesguide.postures.util.LocaleHelper

class CsTeacherApp : Application() {
    override fun attachBaseContext(base: android.content.Context) {
        super.attachBaseContext(LocaleHelper.wrap(base))
    }
}
