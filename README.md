# CS XI Bilingual Teacher's Edition (Android)

Android handbook for **Computer Science XI** teachers (Sindh Curriculum 2026), built from the bilingual teacher's edition PDF.

- **On-screen text:** English only  
- **Voice narration:** Urdu only (system Text-to-speech; install Urdu voice data on the device)

## Download

**v1.0.0 (debug APK)**

Branch copy: `releases/CS-XI-Teachers-Edition-v1.0.0-english-text-urdu-voice-debug.apk`

After building locally:

`app/build/outputs/apk/debug/app-debug.apk`

## App structure

- Home: six chapters (Computer Systems through Digital Literacy)
- Chapter → topics from the PDF table of contents (★ = golden / exam-critical)
- Topic detail: English lecture notes; **Listen (Urdu)** plays Urdu narration extracted from the PDF

Embedded assets: `app/src/main/assets/cs_xi_teacher/guide.json` and reference PDF `XI_c966.pdf`.

## Regenerate content from PDF

```bash
pip install pymupdf
python3 scripts/extract_cs_teacher_guide.py /path/to/XI_c966.pdf
```

## Build

```bash
export ANDROID_HOME=/opt/android-sdk   # or your SDK path
./gradlew assembleDebug
```

APK: `app/build/outputs/apk/debug/app-debug.apk`  
Package: `com.csxi.teachersedition`

## Version 1.0.0

- Teacher's edition content for all six chapters (77 topics)
- English UI locked; Urdu-only narration pipeline
- Reference note for teachers and golden-topic markers
