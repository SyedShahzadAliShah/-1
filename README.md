# Karachi Buffet Recipes

Bilingual (English & Urdu) Android cookbook for authentic Karachi buffet dishes — with voice narration and printable PDF export.

## Features

- **20+ Karachi buffet recipes** — biryani, karahi, BBQ, curries, seafood, appetizers, and desserts
- **Buffet planning guide** — culture, menu planning, serving order, and food safety
- **Urdu voice narration** — listen to full recipes step-by-step in Urdu or English
- **PDF export** — export individual recipes or the full cookbook with embedded Urdu font (Noto Naskh Arabic)
- **Category browsing** — filter by Biryani, Karahi, BBQ, Curries, Appetizers, Seafood, Desserts

## Recipes Included

| Category | Dishes |
|----------|--------|
| Biryani | Beef Biryani, Chicken Tikka Biryani |
| Karahi | Mutton Karahi, Chicken Karahi |
| BBQ | Seekh Kebab, Chicken Tikka, Chapli Kebab |
| Curries | Nihari, Haleem, Aloo Gosht, Daal Chawal |
| Seafood | Fried Fish, Prawn Masala |
| Appetizers | Samosa Chaat, Dahi Bhalla, Boondi Raita |
| Desserts | Gulab Jamun, Kheer, Zarda, Gajar Halwa |

## Build

```bash
pip install Pillow
python3 scripts/generate_recipe_pictures.py
export ANDROID_HOME=/path/to/android-sdk
./gradlew assembleDebug
```

APK output: `app/build/outputs/apk/debug/app-debug.apk`

## Version 1.0.0

- Karachi buffet recipe collection with Urdu & English content
- Voice narration (TTS) for recipes and buffet guide chapters
- Full cookbook PDF export with RTL Urdu support
- Food-themed illustrations for every recipe
