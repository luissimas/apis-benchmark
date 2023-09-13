import os

DB_NAME = os.getenv("DB_NAME") or "database"
DB_HOST = os.getenv("DB_HOST") or "localhost"
DB_PORT = os.getenv("DB_PORT") or "5432"
DB_PASS = os.getenv("DB_PASS") or "password"
DB_USER = os.getenv("DB_USER") or "postgres"
PORT = int(os.getenv("PORT") or "3000")
HOST = os.getenv("HOST") or "localhost"
