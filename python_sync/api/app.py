from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional
from uuid import UUID, uuid4

from api.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from fastapi import FastAPI
from psycopg2.pool import SimpleConnectionPool

pool = SimpleConnectionPool(
    minconn=1,
    maxconn=100,
    dbname=DB_NAME,
    host=DB_HOST,
    port=DB_PORT,
    password=DB_PASS,
    user=DB_USER,
)


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
def get_db():
    conn = pool.getconn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies LIMIT 20")

    columns = [desc[0] for desc in cursor.description]
    movie_objects = []

    for row in cursor.fetchall():
        movie_data = dict(zip(columns, row))
        movie = Movie(**movie_data)
        movie_objects.append(movie)

    cursor.close()
    pool.putconn(conn)
    return movie_objects


@app.get("/cache")
def get_cache():
    return make_movies()
