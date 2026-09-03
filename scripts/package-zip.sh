#!/bin/bash
set -e

echo "📦 Packaging PhishGuard Monorepo into ZIP archive..."

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

ZIP_NAME="phishguard_ai_security_monorepo.zip"
rm -f "$ZIP_NAME"

zip -r "$ZIP_NAME" . \
    -x "*/node_modules/*" \
    -x "*/.venv/*" \
    -x "*/__pycache__/*" \
    -x "*/dist/*" \
    -x "*/.git/*" \
    -x "*_temp_*" \
    -x "*.DS_Store" \
    -x "$ZIP_NAME"

echo "✅ Generated $ZIP_NAME ($(du -h "$ZIP_NAME" | cut -f1))"
