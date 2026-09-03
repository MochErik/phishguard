#!/bin/bash
set -e

echo "🧪 Running tests across PhishGuard monorepo..."

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "🔹 Testing URL Analyzer Microservice..."
python3 "$ROOT_DIR/services/url-analyzer-py/analyzer.py"

echo "🔹 Testing NLP Engine Microservice..."
python3 "$ROOT_DIR/services/nlp-engine-py/engine.py"

echo "✅ All automated integrity checks passed!"
