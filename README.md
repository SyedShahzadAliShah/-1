# Teach Yourself Lectures (CS XI & XII)

Printable **Teach Yourself** materials for Sindh Computer Science XI and XII.

**Student's Edition** (practice first; answers at the end of each chapter):
- [CS XI Student's Edition](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XI-Students-Edition.pdf)
- [CS XII Student's Edition](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XII-Students-Edition.pdf)
- [XI + XII Student's Edition complete](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XI-and-XII-Students-Edition-Complete.pdf)

**Teacher's Edition** (lesson timing, board questions, Urdu cues, answers on the page):
- [CS XI Teacher's Edition](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XI-Teachers-Edition.pdf)
- [CS XII Teacher's Edition](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XII-Teachers-Edition.pdf)
- [XI + XII Teacher's Edition complete](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XI-and-XII-Teachers-Edition-Complete.pdf)

**Coaching Academy Edition** (90-minute batches, full-mark recipes, timed drills, homework):
- [CS XI Coaching Academy Edition (297 pages)](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XI-Coaching-Academy-Edition.pdf)
- [CS XII Coaching Academy Edition (298 pages)](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XII-Coaching-Academy-Edition.pdf)
- [XI + XII Coaching Academy Edition complete (595 pages)](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XI-and-XII-Coaching-Academy-Edition-Complete.pdf)

**Cheat Sheets** (exam revision cards — definitions, tables, mnemonics, ★ Golden):
- [CS XI Cheat Sheets (51 pages)](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XI-Cheat-Sheets.pdf)
- [CS XII Cheat Sheets (52 pages)](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XII-Cheat-Sheets.pdf)
- [XI + XII Cheat Sheets complete (103 pages)](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XI-and-XII-Cheat-Sheets-Complete.pdf)

Individual lectures: [`releases/lectures/README.md`](releases/lectures/README.md). Rebuild editions: `python3 booklets/build.py editions`. Rebuild academy: `python3 booklets/build.py academy`. Rebuild cheat sheets: `python3 booklets/build.py cheat`.

---

# Intimacy Guide

Bilingual (English & Urdu) couples sex-education app with embedded diagram pictures, imagination postures, voice narration, and PDF export.

## Download

**Latest (v3.2.1)** — man/woman posture roles + sex education for him & her:

https://github.com/SyedShahzadAliShah/-1/raw/main/releases/IntimacyHandbook-v3.2.1-debug.apk

Branch copy: https://github.com/SyedShahzadAliShah/-1/raw/cursor/couples-posture-guide-ed65/releases/IntimacyHandbook-v3.2.1-debug.apk

> **Important:** Uninstall any older version first, then install v3.2.1. On the home screen you should see **"Version 3.2.1 — Man/Woman roles + Sex Ed for Him & Her"** below the subtitle.

## v3.2.1

- **Fix:** Sex Education and chapter lists now display correctly inside the scroll view
- **Fix:** Version badge on home screen so you can confirm the correct build is installed

## v3.2.0

- **Man & woman roles** — each posture defines the man's and woman's position and guidance
- **Sex education for him** — 4 chapters on arousal, pleasuring partner, stamina, confidence
- **Sex education for her** — 4 chapters on arousal, pleasure, comfort, confidence
- Diagram labels updated to Man/Woman

## v2.4 fixes

- **PDF export fixed** — proper image loading, multi-page pagination, Urdu font embedding, reliable sharing
- **Upgraded pictures** — 960×600 educational diagrams with Partner A/B labels and position annotations

## Build

```bash
python3 scripts/generate_posture_pictures.py
export ANDROID_HOME=/path/to/android-sdk
./gradlew assembleDebug
```

## Version 3.2.1
