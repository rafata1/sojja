import os

import uvicorn

from api import api_router
from config import config

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

static_dir = "./static"
if not os.path.exists(static_dir):
    os.makedirs(static_dir)
app = FastAPI()
# Configure CORS to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

root_router = APIRouter()
root_router.include_router(api_router, prefix="/api")
app.include_router(root_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/static/{filename}")
async def serve_static_file(filename: str):
    file_path = os.path.join(static_dir, filename)
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    else:
        return {"error": "File not found"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=config.APP_PORT)
