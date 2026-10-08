from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from .config import get_settings
from .routers import auth_router, cart_router, orders_router, products_router, recommendations_router
from . import models  # noqa: F401 ensures models are registered

settings = get_settings()
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title=settings.app_name, openapi_url="/api/openapi.json", docs_url="/api/docs")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health():
    return {"status": "ok"}


app.include_router(auth_router, prefix="/api")
app.include_router(products_router, prefix="/api")
app.include_router(cart_router, prefix="/api")
app.include_router(orders_router, prefix="/api")
app.include_router(recommendations_router, prefix="/api")
