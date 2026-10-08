#!/bin/bash
# Offline MathJax 3 (tex-svg) for the sketchnote WebView.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/app/src/main/assets/www/vendor/mathjax/es5"
if [[ -f "$DEST/tex-svg.js" ]]; then
  echo "mathjax ready"
  exit 0
fi
tmp="$(mktemp -d)"
curl -fL --retry 3 -o "$tmp/mathjax.tgz" \
  "https://registry.npmjs.org/mathjax/-/mathjax-3.2.2.tgz"
tar -xzf "$tmp/mathjax.tgz" -C "$tmp"
rm -rf "$ROOT/app/src/main/assets/www/vendor/mathjax"
mkdir -p "$DEST/output/svg/fonts" "$DEST/input"
cp "$tmp/package/es5/tex-svg.js" "$DEST/"
cp "$tmp/package/es5/core.js" "$DEST/" 2>/dev/null || true
cp "$tmp/package/es5/startup.js" "$DEST/" 2>/dev/null || true
cp "$tmp/package/es5/loader.js" "$DEST/" 2>/dev/null || true
cp "$tmp/package/es5/output/svg.js" "$DEST/output/" 2>/dev/null || true
cp "$tmp/package/es5/output/svg/fonts/tex.js" "$DEST/output/svg/fonts/" 2>/dev/null || true
cp "$tmp/package/es5/input/tex.js" "$DEST/input/" 2>/dev/null || true
rm -rf "$tmp"
test -f "$DEST/tex-svg.js"
echo "mathjax ready"
