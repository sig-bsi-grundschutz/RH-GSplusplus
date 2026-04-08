#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${ROOT}/catalogs/bsi-grundschutz-plus-plus/catalog.json"
URL="https://raw.githubusercontent.com/BSI-Bund/Stand-der-Technik-Bibliothek/main/Anwenderkataloge/Grundschutz++/Grundschutz++-catalog.json"
mkdir -p "$(dirname "$DEST")"
curl -fsSL -o "$DEST" "$URL"
echo "Wrote $DEST ($(wc -c < "$DEST") bytes)"
