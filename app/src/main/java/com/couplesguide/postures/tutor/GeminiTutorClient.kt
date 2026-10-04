package com.couplesguide.postures.tutor

import android.util.Log
import org.json.JSONArray
import org.json.JSONObject
import java.net.HttpURLConnection
import java.net.URL

object GeminiTutorClient {

    private const val TAG = "GeminiTutor"
    private const val MODEL = "gemini-2.0-flash"

    fun isConfigured(apiKey: String?): Boolean = !apiKey.isNullOrBlank()

    fun ask(
        apiKey: String,
        userQuestion: String,
        groundedContext: String,
        useUrdu: Boolean
    ): String? {
        val lang = if (useUrdu) "Urdu" else "English"
        val system = """
            You are a friendly CS tutor for Sindh Curriculum Class XI & XII.
            Answer ONLY using the CONTEXT below from the student's lecture notes.
            If context is insufficient, say so and suggest what to study in the PDF.
            Reply in $lang. Keep under 220 words. Mention ★ topics when relevant.
            
            CONTEXT:
            $groundedContext
        """.trimIndent()

        val body = JSONObject().apply {
            put(
                "contents",
                JSONArray().apply {
                    put(
                        JSONObject().apply {
                            put(
                                "parts",
                                JSONArray().apply {
                                    put(JSONObject().put("text", "$system\n\nStudent: $userQuestion"))
                                }
                            )
                        }
                    )
                }
            )
        }

        val url = URL(
            "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent?key=$apiKey"
        )
        return try {
            val conn = (url.openConnection() as HttpURLConnection).apply {
                requestMethod = "POST"
                setRequestProperty("Content-Type", "application/json")
                doOutput = true
                connectTimeout = 20_000
                readTimeout = 45_000
            }
            conn.outputStream.use { it.write(body.toString().toByteArray(Charsets.UTF_8)) }
            val code = conn.responseCode
            val stream = if (code in 200..299) conn.inputStream else conn.errorStream
            val response = stream.bufferedReader().use { it.readText() }
            if (code !in 200..299) {
                Log.w(TAG, "HTTP $code: $response")
                return null
            }
            val json = JSONObject(response)
            val candidates = json.optJSONArray("candidates") ?: return null
            if (candidates.length() == 0) return null
            val parts = candidates.getJSONObject(0)
                .optJSONObject("content")
                ?.optJSONArray("parts")
            val text = parts?.optJSONObject(0)?.optString("text")?.trim()
            text?.takeIf { it.isNotEmpty() }
        } catch (e: Exception) {
            Log.w(TAG, "Gemini call failed", e)
            null
        }
    }
}
