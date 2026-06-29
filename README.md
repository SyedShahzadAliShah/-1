# Desi Keto Diet

**Heal Through Food, Not Pills** — A bilingual (English/Urdu) Android app for reversing chronic ailments through ketogenic nutrition, traditional Pakistani cuisine, and holistic fitness.

## Features

- **10+ Keto Recipes** across Pakistani, Bar B.Q., Chinese, Continental, Mughlai, Punjabi, Sindhi, and Balochi cuisines
- **9 Health Guides** for Gastric, Gynecological, Mental Health (Psyche), Cardiac, Diabetic, Thyroid, Joint, Liver, and Kidney conditions
- **8 Fitness Routines** including Aerobic, Yoga, HIIT, Walking, Strength Training, Stretching, and Pilates
- **Bilingual** English/Urdu with full RTL support
- **Text-to-Speech** audio narration for recipes, health guides, and fitness routines
- **PDF Export** for recipes, health guides, and fitness plans
- **In-Depth Knowledge** articles on keto science, desi spices, intermittent fasting, and medication reduction protocols

## APK Download

Pre-built debug APK: [`DesiKetoDiet-debug.apk`](DesiKetoDiet-debug.apk)

Install on Android: enable "Install from unknown sources", then open the APK file.

## Build from Source

### Prerequisites

- Node.js 18+
- Java 21 (OpenJDK)
- Android SDK (API 35+)

### Web Development

```bash
cd desi-keto-diet
npm install
npm run dev
```

### Build APK

```bash
cd desi-keto-diet
npm install
npm run build
npx cap sync android

# Set Android SDK path
echo "sdk.dir=$HOME/android-sdk" > android/local.properties

cd android
./gradlew assembleDebug
```

APK output: `android/app/build/outputs/apk/debug/app-debug.apk`

## Tech Stack

- React 19 + TypeScript + Vite
- Capacitor 8 (Android native wrapper)
- i18next (bilingual i18n)
- jsPDF (PDF export)
- @capacitor-community/text-to-speech (audio narration)

## Medical Disclaimer

This app provides educational dietary guidance only. Always consult your physician before changing medications or treatment plans. Never stop prescribed medications without medical supervision.

## License

MIT
