from api.config import DATABASE_URL
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def make_db():
    db = async_session()
    try:
        yield db
    finally:
        await db.close()
