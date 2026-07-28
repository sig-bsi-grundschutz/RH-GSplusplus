#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${ROOT}/catalogs/bsi-grundschutz-plus-plus/catalog.json"
VERSION_FILE="${ROOT}/third_party/bsi/VERSION"

if [[ ! -f "$VERSION_FILE" ]]; then
  echo "Missing ${VERSION_FILE}" >&2
  exit 1
fi

# shellcheck disable=SC1090
source "$VERSION_FILE"

: "${upstream_repo:?upstream_repo missing in VERSION}"
: "${upstream_commit:?upstream_commit missing in VERSION}"
: "${upstream_path:?upstream_path missing in VERSION}"

REPO_SLUG="${upstream_repo#https://github.com/}"
URL="https://raw.githubusercontent.com/${REPO_SLUG}/${upstream_commit}/${upstream_path}"
mkdir -p "$(dirname "$DEST")"
curl -fsSL -o "$DEST" "$URL"
echo "Wrote $DEST ($(wc -c < "$DEST") bytes) from ${upstream_commit:0:12} (${upstream_path})"
