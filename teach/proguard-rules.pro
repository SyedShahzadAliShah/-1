# Teach Yourself Sketchnotes keeps the WebView bridge methods.
-keepclassmembers class com.teachyourself.sketchnotes.MainActivity$Bridge {
    @android.webkit.JavascriptInterface <methods>;
}
