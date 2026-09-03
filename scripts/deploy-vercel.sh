#!/bin/bash
set -e

echo "🚀 Deploying PhishGuard Monorepo to Vercel..."

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if command -v vercel &> /dev/null; then
    vercel --prod
else
    npx vercel --prod
fi
