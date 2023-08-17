import os

from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = (
    os.getenv("DATABASE_URL")
    or "postgresql+asyncpg://postgres:password@localhost:5432/db"
)
PORT = os.getenv("PORT") or 3000
