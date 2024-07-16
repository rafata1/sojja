import uvicorn

from api import api_router
from config import config

from fastapi import FastAPI, APIRouter

app = FastAPI()
root_router = APIRouter()
root_router.include_router(api_router, prefix="/api")
app.include_router(root_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=config.APP_PORT)
