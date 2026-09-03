#!/bin/bash
set -e

echo "🚀 Deploying PhishGuard Preview to GitHub Pages..."

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

git checkout gh-pages 2>/dev/null || git checkout -b gh-pages
cp -r preview/* .
git add .
git commit -m "deploy: update live GitHub Pages preview app" || true
git push origin gh-pages --force
git checkout main

echo "✅ Deployed to https://mocherik.github.io/phishguard/"
