# Intimacy Guide

An educational Android app that helps couples learn intimate postures with step-by-step instructions, comfort tips, and an emphasis on communication and consent.

## Features

- **12 illustrated postures** across 5 categories (Face to Face, Side by Side, Rear Entry, Standing & Seated, Variations)
- **Step-by-step guides** with difficulty ratings
- **Comfort tips** for each position
- **Category filtering** to browse by type

## Build the APK

Requirements: Android SDK (API 34), JDK 17+

```bash
export ANDROID_HOME=/path/to/android-sdk
./gradlew assembleDebug
```

The APK will be at:

```
app/build/outputs/apk/debug/app-debug.apk
```

For a release build:

```bash
./gradlew assembleRelease
```

## Install on Device

```bash
adb install app/build/outputs/apk/debug/app-debug.apk
```

## App Info

- **Package:** `com.couplesguide.postures`
- **Min SDK:** 24 (Android 7.0)
- **Target SDK:** 34
