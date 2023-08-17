from uuid import uuid4

from api.config import DATABASE_URL
from sqlalchemy import Column, Date, Integer, String, Uuid, create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()


class MovieModel(Base):
    __tablename__ = "movies"

    id = Column(Uuid, primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    release_date = Column(Date, nullable=False)
    director = Column(String, nullable=False)
    description = Column(String, default=None)
    duration = Column(Integer, default=None)
    budget = Column(Integer, default=None)
