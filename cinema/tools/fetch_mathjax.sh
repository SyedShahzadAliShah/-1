#!/bin/bash
# Download MathJax 3 (ES5 build) so the reader can typeset math with no network.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$ROOT/src/main/assets/mathjax/es5"
if [[ -f "$DEST/tex-svg.js" && -f "$DEST/output/svg.js" && -f "$DEST/output/svg/fonts/tex.js" ]]; then
  echo "mathjax ready"
  exit 0
fi
tmp="$(mktemp -d)"
curl -fL --retry 3 -o "$tmp/mathjax.tgz" \
  "https://registry.npmjs.org/mathjax/-/mathjax-3.2.2.tgz"
tar -xzf "$tmp/mathjax.tgz" -C "$tmp"
rm -rf "$ROOT/src/main/assets/mathjax"
mkdir -p "$ROOT/src/main/assets/mathjax"
cp -a "$tmp/package/es5" "$DEST"
rm -rf "$tmp"
test -f "$DEST/tex-svg.js"
echo "mathjax ready"
