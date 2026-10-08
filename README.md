# CS XII Teach Yourself Edition (Urdish)

Self-study Android lectures for **Sindh Computer Science XII** (New Curriculum 2025–27), converted from the bilingual Teacher's Edition into a **Teach Yourself** classroom:

- Lectures **صرف Urdish** میں (Urdu grammar, CS terms in English)
- Offline **MathJax SVG** formulae
- **Flexbox** lecture boards (chips, two-column cards, flow steps, formula row)
- Native **Urdu TTS** synced to each board panel

Teacher's Edition source: *COMPUTER SCIENCE XII — Bilingual Teacher's Edition* (HCI through Entrepreneurship).

## Download

**Latest (v1.0.0)** — Urdish lectures + MathJax SVG + Flexbox + TTS:

`releases/CS-XII-Teach-Yourself-Urdish-v1.0.0-debug.apk`

Install Google **Urdu** text-to-speech on the phone (Settings → Language → Text-to-speech) so the Urdish lecture voice can start.

## Chapters

1. Computer Systems (HCI)
2. Computational Thinking & Algorithms
3. Programming Fundamentals
4. Data and Analysis
5. Application and Impacts of Computing
6. Entrepreneurship in the Digital Age

## Build

```bash
export ANDROID_HOME=/path/to/android-sdk
python3 scripts/export_teachyourself_urdish.py
./gradlew :lectures:assembleDebug
```

The debug APK is copied to `releases/`.
