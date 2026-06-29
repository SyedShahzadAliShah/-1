#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR/desi-keto-diet"

echo "==> Installing dependencies..."
npm install

echo "==> Building web app..."
npm run build

echo "==> Syncing Capacitor Android..."
npx cap sync android

if [ -z "${ANDROID_HOME:-}" ] && [ -d "$HOME/android-sdk" ]; then
  export ANDROID_HOME="$HOME/android-sdk"
fi

if [ -n "${ANDROID_HOME:-}" ]; then
  echo "sdk.dir=$ANDROID_HOME" > android/local.properties
fi

echo "==> Building debug APK..."
cd android
chmod +x gradlew
./gradlew assembleDebug

APK_PATH="app/build/outputs/apk/debug/app-debug.apk"
if [ -f "$APK_PATH" ]; then
  cp "$APK_PATH" "$SCRIPT_DIR/DesiKetoDiet-debug.apk"
  echo "==> APK built: $SCRIPT_DIR/DesiKetoDiet-debug.apk"
  ls -lh "$SCRIPT_DIR/DesiKetoDiet-debug.apk"
else
  echo "ERROR: APK not found at $APK_PATH"
  exit 1
fi
