# CS Whiteboard Lectures

Animated whiteboard teacher for **Computer Science XI and XII** (Sindh curriculum), with English and Urdu vocals.

The marker writes headings, bullets, diagrams, worked examples and exam callouts while Android TTS narrates. Content is generated from the *Ultimate Teach Yourself* booklets.

## Download

**v1.0.0 debug APK**

https://github.com/SyedShahzadAliShah/-1/raw/cursor/cs-whiteboard-lectures-apk-e3b4/releases/CS-Whiteboard-Lectures-v1.0.0-debug.apk

Repo copy: `releases/CS-Whiteboard-Lectures-v1.0.0-debug.apk`

Package id: `com.sindh.cswhiteboard` (installs beside older apps).

## What you get

- Class XI (2026) and Class XII (2025–27) chapter maps
- 200+ topic lectures with ★ golden exam flags
- Play one topic or a whole chapter
- English / Urdu voice, slow–fast speed
- Logic-gate, OSI, sort, HCI, neural-net and other board diagrams

Install **Google Text-to-speech** plus an Urdu voice for اردو narration.

## Build

```bash
python3 scripts/generate_whiteboard_lectures.py
export ANDROID_HOME=/path/to/android-sdk
./gradlew assembleDebug
```
