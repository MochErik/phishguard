import sys
import os
from pathlib import Path

# Add current directory and parent paths
current_dir = Path(__file__).resolve().parent
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from loguru import logger
import time

from core.config import settings
from core.database import init_db
from api.routes import router

limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["10000/day", "1000/hour", "120/minute"],
    storage_uri=settings.REDIS_URL,
)

app = FastAPI(
    title="PhishGuard Enterprise AI Monorepo API",
    description="Multi-Vector Phishing & Social Engineering Detection Engine",
    version="2.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    try:
        response = await call_next(request)
        duration = round((time.time() - start) * 1000, 2)
        logger.info(f"{request.method} {request.url.path} → {response.status_code} [{duration}ms]")
        return response
    except Exception as e:
        logger.error(f"Error handling {request.method} {request.url.path}: {e}")
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal Server Error", "error": str(e)}
        )

@app.on_event("startup")
async def startup():
    await init_db()
    logger.info("🛡️ PhishGuard API Monorepo v2.0 Engine started successfully ✓")

app.include_router(router, prefix="/api/v1")
app.include_router(router, prefix="/v1")  # Alias for backward compatibility

@app.get("/")
async def root():
    return {
        "name": "PhishGuard AI Detection Engine",
        "version": "2.0.0",
        "status": "online",
        "docs": "/api/docs",
        "monorepo": "https://github.com/MochErik/phishguard",
        "author": "Moch. Erik Irriansyah (NIM 04123003 - Universitas Narotama)"
    }

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "PhishGuard API Monorepo",
        "timestamp": time.time()
    }
