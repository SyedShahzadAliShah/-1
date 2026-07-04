# پاکستانی ریستوران ترکیبیں — گھر میں بنائیں

**Pakistani Restaurant Recipes at Home** — Android app fully in Urdu with voice narration and PDF export.

## Download

**Latest (v1.0.0)** — 22 authentic Pakistani recipes from 9 famous cities:

```
releases/PakRecipes-v1.0.0-debug.apk
```

> **Install:** Enable "Install from unknown sources" in your Android settings, then install the APK.

## Features

- **مکمل اردو** — Entirely in Urdu (RTL), all recipes, UI, and PDF in Urdu
- **22 مشہور ترکیبیں** — 22 authentic restaurant-style recipes from across Pakistan
- **آواز کی سہولت** — Urdu text-to-speech narration for every recipe (full ingredients + steps + tips)
- **PDF برآمد** — Export any single recipe or all 22 recipes to PDF (open, save, print, share)
- **شہروں کے مطابق تلاش** — Browse recipes by city with a horizontal city filter

## Cities & Recipes

| شہر | ترکیبیں |
|-----|---------|
| 🌊 کراچی | کراچی بریانی، سندھی بریانی، مٹن کڑاہی |
| 🌸 لاہور | لاہوری پائے، حلوہ پوری، لاہوری چرگہ، گاجر کا حلوہ، چکن قورمہ |
| 🏔️ پشاور | چپلی کباب، نمکین گوشت، پشاوری کڑاہی |
| 🌿 کوئٹہ | سجی، کوئٹہ ٹکہ |
| 🌶️ حیدرآباد | حیدرآبادی بریانی |
| 🌞 ملتان | ملتانی کڑاہی، سوہن حلوہ |
| 🏛️ اسلام آباد | کشمیری چائے، چکن ٹکہ مسالہ، مٹن پلاؤ |
| 🍲 راولپنڈی | نہاری، دال ماش |
| 🏔️ گلگت بلتستان | ٹماٹر گوشت، آلو گوشت |

## Build

```bash
export ANDROID_HOME=/path/to/android-sdk
echo "sdk.dir=$ANDROID_HOME" > local.properties
./gradlew assembleDebug
```

APK output: `app/build/outputs/apk/debug/app-debug.apk`

## Version History

### v1.0.0 — Initial Release
- 22 authentic Pakistani restaurant-style recipes in Urdu
- City-based browsing (9 cities across Pakistan)
- Urdu TTS voice narration for each recipe
- PDF export: single recipe or full cookbook
- Beautiful warm terracotta/saffron color theme
