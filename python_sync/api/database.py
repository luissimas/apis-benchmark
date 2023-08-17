from api.config import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URL, echo=False)
sessionmaker = sessionmaker(bind=engine, expire_on_commit=False)


def make_db():
    db = sessionmaker()
    try:
        yield db
    finally:
        db.close()
