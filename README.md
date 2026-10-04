# MT-331 Lecture Notes

NED UET **Probability & Statistics (MT-331)** — cinematic bilingual teacher lecture notes (Walpole sketchnotes).

- Swipeable **lecture beats** per syllabus chapter
- **MathJax** (TeX) formulas + **SVG sketchnote diagrams** on each beat (network required first load for MathJax CDN)
- **Text-to-speech:** **English** or **Urdu** only (pick one per lecture; matches app language by default)
- Teacher PDF bundled in the app: `app/src/main/assets/mt331_teachers_cheatsheet.pdf`
- Browser preview: `tools/mt331-lecture-preview.html`

## Download (v4.1.1)

https://github.com/SyedShahzadAliShah/-1/raw/cursor/mt331-cinematic-lecture-notes-8c89/releases/MT331-LectureNotes-v4.1.1-debug.apk

Application id: `com.neduet.mt331lecture`.

On Android: download the APK, allow install from your browser if prompted, then open **MT-331 Lecture Notes**. For Urdu voice, install Urdu TTS data in system **Text-to-speech** settings.

## Build

```bash
export ANDROID_HOME=/path/to/android-sdk
./gradlew assembleDebug
```

Output: `app/build/outputs/apk/debug/app-debug.apk` (copy to `releases/` if you publish a tagged build).
