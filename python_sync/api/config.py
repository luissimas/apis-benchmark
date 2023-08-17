import os

from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = (
    os.getenv("DATABASE_URL")
    or "postgresql+psycopg2://postgres:password@localhost:5432/db"
)
PORT = os.getenv("PORT") or 3000
