# CS Teacher Guidelines (Official Bilingual Teacher's Edition APK)

Official **teacher guidelines** app from the **Computer Science XI & XII Bilingual Teacher's Edition** PDFs (Sindh Curriculum).

- **Audience:** Teachers only (reference note + textbook PDF citation)
- **On-screen text:** English descriptive guidelines & lecture notes
- **Voice narration:** Urdu class guidance only
- **★ Golden topics:** Exam-critical emphasis per Teacher's Edition

## Build

```bash
# Regenerate topic JSON + Urdu narration assets from the PDFs in uploads/
python3 scripts/extract_cs_teacher_pdfs.py

export ANDROID_HOME=/opt/android-sdk
./gradlew assembleDebug
```

APK output: `app/build/outputs/apk/debug/app-debug.apk`

```bash
python3 scripts/apply_teacher_guidelines.py   # official teacher metadata + lecture-only topics
```

## Download (v1.2.0 official teacher guidelines)

https://github.com/SyedShahzadAliShah/-1/raw/cursor/cs-teachers-edition-f1f7/releases/CSTeacherEdition-v1.2.0-teacher-guidelines-debug.apk

## Version 1.1.0

- **Animated sketchnote lectures** — doodle motifs + PDF page art per topic
- **Vocal sync** — each sketchnote frame advances with its Urdu TTS segment
- English on-screen notes; Urdu vocals only

```bash
python3 scripts/extract_cs_teacher_pdfs.py      # text + Urdu narration JSON
python3 scripts/build_sketchnote_lectures.py    # frames + page images
```

## Version 1.0.0

- CS XI & CS XII class picker
- Golden-topic markers (★) for exam-critical sections
- Urdu narration via system Text-to-speech (install Urdu voice data in Android TTS settings if needed)
