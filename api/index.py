import sys
import os
from pathlib import Path

# Add apps/server-api directory to Python path
CURRENT_DIR = Path(__file__).resolve().parent
ROOT_DIR = CURRENT_DIR.parent
SERVER_API_DIR = ROOT_DIR / "apps" / "server-api"

if str(SERVER_API_DIR) not in sys.path:
    sys.path.insert(0, str(SERVER_API_DIR))
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# Import the FastAPI instance
try:
    from main import app
except ImportError:
    from apps.server_api.main import app

# Vercel Serverless Function entrypoint
app = app
