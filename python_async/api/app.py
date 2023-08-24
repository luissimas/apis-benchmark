import asyncio
from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional
from uuid import UUID, uuid4

import asyncpg
from api.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from fastapi import Depends, FastAPI

dsn = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


async def init_db_pool():
    return await asyncpg.create_pool(dsn=dsn)


@dataclass
class Movie:
    id: UUID
    name: str
    release_date: date
    director: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    duration: Optional[int] = None
    budget: Optional[int] = None


def make_movies() -> List[Movie]:
    return [
        Movie(
            id=uuid4(),
            name="any-name",
            release_date=datetime.now(),
            director="any-director",
            description="any-description",
            duration=1000,
            budget=10000,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        for _ in range(1000)
    ]


app = FastAPI()


@app.get("/db")
async def get_db(pool: asyncpg.Pool = Depends(init_db_pool)):
    async with pool.acquire() as conn:
        query = "SELECT * FROM movies LIMIT 20"
        rows = await conn.fetch(query)
        movies = [Movie(**row) for row in rows]
        return movies


@app.get("/cache")
async def get_cache():
    return make_movies()
