import os

from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = (
    os.getenv("DATABASE_URL")
    or "postgresql+asyncpg://postgres:password@postgres:5432/db"
)
PORT = int(os.getenv("PORT") or "3000")
HOST = os.getenv("HOST") or "localhost"
