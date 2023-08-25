from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional
from uuid import UUID, uuid4

import asyncpg
from api.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from fastapi import FastAPI

dsn = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


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


@app.on_event("startup")
async def startup():
    app.state.db_pool = await asyncpg.create_pool(dsn=dsn, min_size=1, max_size=100)


@app.get("/db")
async def get_db():
    async with app.state.db_pool.acquire() as conn:
        query = "SELECT * FROM movies LIMIT 20"
        rows = await conn.fetch(query)
        movies = [Movie(**row) for row in rows]
        return movies


@app.get("/cache")
async def get_cache():
    return make_movies()
