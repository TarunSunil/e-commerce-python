from __future__ import annotations

import os
from typing import Sequence, AsyncGenerator
from contextlib import asynccontextmanager

from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from .models import Product, User, CartItem, Order


_client: AsyncIOMotorClient | None = None


async def init_db() -> None:
    global _client
    if os.getenv("DISABLE_DB", "0") == "1":
        return

    uri = (
        os.getenv("MONGODB_URI")
        or os.getenv("SPRING_DATA_MONGODB_URI")
        or "mongodb://mongodb:27017/ecommerce"
    )
    _client = AsyncIOMotorClient(uri)
    db_name = os.getenv("DB_NAME", "ecommerce")

    models: Sequence = [Product, User, CartItem, Order]
    await init_beanie(database=_client[db_name], document_models=models)


def get_client() -> AsyncIOMotorClient | None:
    return _client


@asynccontextmanager
async def mongo_session() -> AsyncGenerator:
    client = get_client()
    if client is None:
        yield None
        return
    # Motor supports async session
    async with client.start_session() as session:
        yield session
