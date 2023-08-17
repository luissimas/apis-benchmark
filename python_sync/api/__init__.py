import uvicorn
from api.app import app
from api.config import PORT


def run():
    uvicorn.run("api:app", port=PORT)


def dev():
    uvicorn.run("api:app", port=PORT, reload=True)
