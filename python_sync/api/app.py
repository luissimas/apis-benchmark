from datetime import datetime
from typing import List
from uuid import uuid4

from api.database import make_db
from api.entities import Movie
from api.models import MovieModel
from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.orm import Session

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
def get_db(
    db: Session = Depends(make_db),
):
    result = db.execute(select(MovieModel).limit(20))
    return result.scalars().all()


@app.get("/cache")
def get_cache():
    return movies
