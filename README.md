# CS Teacher's Edition (Bilingual APK)

Android handbook built from the **Computer Science XI & XII Bilingual Teacher's Edition** PDFs (Sindh Curriculum).

- **On-screen text:** English lecture notes only
- **Voice narration:** Urdu TTS only (Listen on home, book overview, and each topic)
- **Content:** 73 topics (CS XI) + 94 topics (CS XII) extracted from the uploaded teacher PDFs

## Build

```bash
# Regenerate topic JSON + Urdu narration assets from the PDFs in uploads/
python3 scripts/extract_cs_teacher_pdfs.py

export ANDROID_HOME=/opt/android-sdk
./gradlew assembleDebug
```

APK output: `app/build/outputs/apk/debug/app-debug.apk`

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
