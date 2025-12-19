from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import os
import httpx

from .db import init_db

app = FastAPI(title="E-commerce Python Backend", openapi_url="/api/openapi.json")


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.on_event("startup")
async def on_startup():
    await init_db()


def get_recommender_base() -> str:
    # Prefer explicit env var; default to Docker service name
    return os.getenv("RECOMMENDER_URL", "http://recommender:8000")


@app.get("/api/recommend/{product_id}")
async def recommend_by_product(product_id: str, limit: int = 5):
    base = get_recommender_base().rstrip("/")
    url = f"{base}/recommend/{product_id}"
    params = {"limit": str(limit)}
    timeout = httpx.Timeout(connect=0.3, read=2.0)
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            resp = await client.get(url, params=params)
            if resp.status_code == 200:
                # Expect an array of Product-like dicts
                data = resp.json()
                if isinstance(data, list):
                    return JSONResponse(content=data)
                # If recommender wraps, try common key
                if isinstance(data, dict) and "items" in data:
                    return JSONResponse(content=data["items"])
                return JSONResponse(content=[])
            # Non-200 from recommender → graceful empty list
            return JSONResponse(content=[])
    except httpx.RequestError:
        # Timeout or connection error → fallback empty list
        return JSONResponse(content=[])


@app.get("/api/recommend/user/{user_id}")
async def recommend_by_user(user_id: str, limit: int = 5):
    base = get_recommender_base().rstrip("/")
    url = f"{base}/recommend/user/{user_id}"
    params = {"limit": str(limit)}
    timeout = httpx.Timeout(connect=0.3, read=2.0)
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            resp = await client.get(url, params=params)
            if resp.status_code == 200:
                data = resp.json()
                if isinstance(data, list):
                    return JSONResponse(content=data)
                if isinstance(data, dict) and "items" in data:
                    return JSONResponse(content=data["items"])
                return JSONResponse(content=[])
            return JSONResponse(content=[])
    except httpx.RequestError:
        return JSONResponse(content=[])
