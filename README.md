# CS Whiteboard

Animated whiteboard lectures with voice for Sindh Computer Science Class XI and Class XII.

Each lecture is a sequence of boards. A marker draws the title, diagram, table, or code while the phone reads the script aloud using Android text-to-speech. The scripts are original lessons that follow the course outline: computer systems, computational thinking, programming, data, impacts of computing, digital literacy, HCI, and digital entrepreneurship.

## Install

Build a debug APK:

```bash
python3 scripts/build_lectures.py
export ANDROID_HOME=$HOME/android-sdk
./gradlew assembleDebug
```

The APK is written to `app/build/outputs/apk/debug/`. A copy is kept at `releases/CSWhiteboard-v1.0.0-debug.apk`.

On the phone, install that APK. For spoken vocals, install an English text-to-speech voice (Google Text-to-speech works well). The words also stay on screen if a voice is not installed yet.

## Use

1. Open Class XI or Class XII.
2. Open a chapter, then a lecture. High-yield lectures are marked.
3. The board draws and the voice reads. Pause, skip a board, change speed (0.9x, 1x, 1.15x), or continue to the next lecture.

## Version 1.0.0
