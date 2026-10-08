# Teach Yourself keeps the TTS bridge and lecture WebView unobfuscated.
-keepclassmembers class com.csxii.teachyourself.TtsBridge {
    @android.webkit.JavascriptInterface <methods>;
}
