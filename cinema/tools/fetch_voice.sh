#!/bin/bash
# Download the offline English voice and the sherpa-onnx Android runtime.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AAR="$ROOT/libs/sherpa-onnx.aar"
VOICE="$ROOT/src/main/assets/voice"
mkdir -p "$ROOT/libs" "$VOICE"
if [[ ! -f "$AAR" ]]; then
  curl -fL --retry 3 -o "$AAR" \
    "https://github.com/k2-fsa/sherpa-onnx/releases/download/v1.12.38/sherpa-onnx-1.12.38.aar"
fi
if [[ ! -f "$VOICE/model.onnx" || ! -f "$VOICE/tokens.txt" || ! -d "$VOICE/espeak-ng-data" ]]; then
  tmp="$(mktemp -d)"
  curl -fL --retry 3 -o "$tmp/voice.tar.bz2" \
    "https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-en_US-amy-low-int8.tar.bz2"
  tar -xjf "$tmp/voice.tar.bz2" -C "$tmp"
  src="$(find "$tmp" -name tokens.txt -printf '%h\n' | head -1)"
  cp -f "$src"/*.onnx "$VOICE/model.onnx"
  cp -f "$src/tokens.txt" "$VOICE/tokens.txt"
  rm -rf "$VOICE/espeak-ng-data"
  cp -a "$src/espeak-ng-data" "$VOICE/espeak-ng-data"
  rm -rf "$tmp"
fi
echo "voice ready"
