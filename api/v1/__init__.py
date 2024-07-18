from fastapi import APIRouter

from api.v1.post import post
from api.v1.session import session

v1_router = APIRouter()
v1_router.include_router(session.session_router, prefix="/session", tags=["Session"])
v1_router.include_router(post.post_router, prefix="/post", tags=["Post"])
