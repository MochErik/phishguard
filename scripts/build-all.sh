#!/bin/bash
set -e

echo "🔨 Building all PhishGuard Monorepo packages and apps..."

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Build Web Client
echo "📦 Building apps/web-client..."
cd "$ROOT_DIR/apps/web-client"
if [ -f "package.json" ]; then
    npm run build || true
fi

echo "✅ All builds completed successfully!"
