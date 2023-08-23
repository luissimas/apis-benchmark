import uvicorn
from api.app import app
from api.config import HOST, PORT


def run():
    uvicorn.run("api:app", host=HOST, port=PORT, access_log=False)


def dev():
    uvicorn.run("api:app", host=HOST, port=PORT, access_log=False, reload=True)
