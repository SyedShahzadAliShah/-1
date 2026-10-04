package com.couplesguide.postures.util

import android.app.Activity
import android.content.Context
import android.content.Intent
import android.speech.tts.TextToSpeech
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import com.couplesguide.postures.R
import java.util.Locale

/**
 * Guides users to install **Google Text-to-speech** built-in India Voice 1 packs.
 * from inside the app. Voice binaries cannot be bundled in the APK; Android installs them
 * via the Google TTS engine.
 */
object NarrativeTtsInstallHelper {

    const val GOOGLE_TTS_ENGINE = "com.google.android.tts"

    data class VoicePackStatus(
        val englishReady: Boolean,
        val urduReady: Boolean,
        val enginePackage: String?,
        val usingGoogleEngine: Boolean
    ) {
        val allReady: Boolean get() = englishReady && urduReady
    }

    fun probeVoicePacks(context: Context, onResult: (VoicePackStatus) -> Unit) {
        val appContext = context.applicationContext
        if (isGoogleTtsInstalled(appContext)) {
            probeWithEngine(appContext, GOOGLE_TTS_ENGINE, onResult)
        } else {
            probeWithEngine(appContext, null, onResult)
        }
    }

    private fun probeWithEngine(
        context: Context,
        enginePackage: String?,
        onResult: (VoicePackStatus) -> Unit
    ) {
        var tts: TextToSpeech? = null
        val listener = TextToSpeech.OnInitListener { status ->
            val engine = tts
            if (status != TextToSpeech.SUCCESS || engine == null) {
                onResult(VoicePackStatus(false, false, enginePackage, enginePackage == GOOGLE_TTS_ENGINE))
                tts?.shutdown()
                return@OnInitListener
            }
            val englishReady =
                NarrativeBuiltInVoiceSelector.isLocaleReady(engine, NarrativeBuiltInVoiceSelector.LOCALE_ENGLISH_INDIA) &&
                    NarrativeBuiltInVoiceSelector.hasBuiltInVoice1(
                        engine,
                        NarrativeBuiltInVoiceSelector.LOCALE_ENGLISH_INDIA
                    )
            val urduReady =
                NarrativeBuiltInVoiceSelector.isLocaleReady(engine, NarrativeBuiltInVoiceSelector.LOCALE_URDU_INDIA) &&
                    NarrativeBuiltInVoiceSelector.hasBuiltInVoice1(
                        engine,
                        NarrativeBuiltInVoiceSelector.LOCALE_URDU_INDIA
                    )
            val pkg = engine.defaultEngine
            onResult(
                VoicePackStatus(
                    englishReady = englishReady,
                    urduReady = urduReady,
                    enginePackage = pkg,
                    usingGoogleEngine = pkg == GOOGLE_TTS_ENGINE
                )
            )
            engine.shutdown()
        }
        tts = if (enginePackage != null) {
            TextToSpeech(context, listener, enginePackage)
        } else {
            TextToSpeech(context, listener)
        }
    }

    fun isGoogleTtsInstalled(context: Context): Boolean {
        return try {
            context.packageManager.getPackageInfo(GOOGLE_TTS_ENGINE, 0)
            true
        } catch (_: Exception) {
            false
        }
    }

    fun isLocaleReady(engine: TextToSpeech, locale: Locale): Boolean {
        return when (engine.isLanguageAvailable(locale)) {
            TextToSpeech.LANG_AVAILABLE,
            TextToSpeech.LANG_COUNTRY_AVAILABLE,
            TextToSpeech.LANG_COUNTRY_VAR_AVAILABLE -> true
            else -> false
        }
    }

    /** Opens Google TTS voice-data installer (English India + Urdu India Voice 1). */
    fun launchGoogleTtsInstaller(context: Context): Boolean {
        val installIntent = Intent(TextToSpeech.Engine.ACTION_INSTALL_TTS_DATA).apply {
            if (isGoogleTtsInstalled(context)) {
                setPackage(GOOGLE_TTS_ENGINE)
            }
            addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
        }
        if (installIntent.resolveActivity(context.packageManager) != null) {
            context.startActivity(installIntent)
            return true
        }
        return launchTtsSettings(context)
    }

    fun launchTtsSettings(context: Context): Boolean {
        val intents = listOf(
            Intent(TextToSpeech.Engine.ACTION_INSTALL_TTS_DATA),
            Intent("com.android.settings.TTS_SETTINGS"),
            Intent(android.provider.Settings.ACTION_SETTINGS)
        )
        for (intent in intents) {
            if (intent.resolveActivity(context.packageManager) != null) {
                intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                context.startActivity(intent)
                return true
            }
        }
        return false
    }

    fun formatStatusLine(context: Context, status: VoicePackStatus): String {
        val en = context.getString(
            if (status.englishReady) R.string.tts_pack_ready else R.string.tts_pack_missing,
            context.getString(R.string.tts_pack_english)
        )
        val ur = context.getString(
            if (status.urduReady) R.string.tts_pack_ready else R.string.tts_pack_missing,
            context.getString(R.string.tts_pack_urdu_pk)
        )
        return context.getString(R.string.tts_voice_status_line, en, ur)
    }

    fun showInstallDialog(activity: Activity, status: VoicePackStatus? = null) {
        val message = buildString {
            append(activity.getString(R.string.tts_install_dialog_message))
            if (status != null) {
                append("\n\n")
                append(formatStatusLine(activity, status))
            }
        }
        AlertDialog.Builder(activity)
            .setTitle(R.string.tts_install_dialog_title)
            .setMessage(message)
            .setPositiveButton(R.string.tts_install_open_google) { _, _ ->
                if (!launchGoogleTtsInstaller(activity)) {
                    Toast.makeText(activity, R.string.tts_install_unavailable, Toast.LENGTH_LONG).show()
                }
            }
            .setNeutralButton(R.string.voice_open_settings) { _, _ ->
                if (!launchTtsSettings(activity)) {
                    Toast.makeText(activity, R.string.tts_install_unavailable, Toast.LENGTH_LONG).show()
                }
            }
            .setNegativeButton(android.R.string.cancel, null)
            .show()
    }

    fun promptIfMissing(activity: Activity, status: VoicePackStatus, onReady: () -> Unit) {
        if (status.allReady) {
            onReady()
            return
        }
        showInstallDialog(activity, status)
    }
}
