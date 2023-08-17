from datetime import datetime
from typing import List
from uuid import uuid4

from api.database import make_db
from api.entities import Movie
from api.models import MovieModel
from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

movies: List[Movie] = [
    Movie(
        id=uuid4(),
        name="any-name",
        release_date=datetime.now(),
        director="any-director",
        description="any-description",
        duration=1000,
        budget=10000,
    )
    for _ in range(1000)
]


app = FastAPI()


@app.get("/db")
async def get_db(
    db: AsyncSession = Depends(make_db),
):
    result = await db.execute(select(MovieModel).limit(100))
    return result.scalars().all()


@app.get("/cache")
async def get_cache():
    return movies
