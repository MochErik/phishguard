#!/bin/bash
set -e

echo "🚀 Starting PhishGuard Monorepo Development Environment..."

# Root directory
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Start Backend
echo "📦 Starting FastAPI backend on http://localhost:8000..."
cd "$ROOT_DIR/apps/server-api"
if [ -d "$ROOT_DIR/.venv" ]; then
    source "$ROOT_DIR/.venv/bin/activate"
fi
uvicorn main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

# Start Frontend
echo "💻 Starting Web Client frontend on http://localhost:5173..."
cd "$ROOT_DIR/apps/web-client"
npm run dev &
FRONTEND_PID=$!

trap "kill $BACKEND_PID $FRONTEND_PID 2>/dev/null" EXIT INT TERM

wait
