# SECCAP Admissions

Android helper app for **SECCAP** (Sindh Electronic Centralized College Admission Program) — the Government of Sindh's system for 1st-year (Class XI) admissions to government colleges.

## Features

- **6-step application wizard** — Educational details, personal info, faculty selection, zone & college preferences (up to 5), document checklist, and review
- **Voice narration (TTS)** — Step-by-step spoken guidance in English and Urdu
- **PDF export** — Printable application summary and admission guide (open, share, save to Downloads, print)
- **Bilingual UI** — Full English and Urdu support with RTL layout
- **College browser** — Explore 15+ government colleges across 7 zones with seat counts and cutoff marks
- **Draft persistence** — Save and resume your application anytime
- **Official portal link** — Quick access to [seccap.dgcs.gos.pk](https://seccap.dgcs.gos.pk)

## Disclaimer

This is a **helper app** for preparing applications offline. Final submission must be done on the official SECCAP portal.

## Build

```bash
./gradlew assembleDebug
```

Requires Android SDK 34, minSdk 24.

## Tech Stack

- Kotlin, Material Design 3, View Binding
- ViewPager2 wizard, RecyclerView
- Android TextToSpeech for voice narration
- Android PdfDocument API for PDF export (no third-party libraries)
