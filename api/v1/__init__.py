from fastapi import APIRouter

from api.v1.session import session

v1_router = APIRouter()
v1_router.include_router(session.session_router, prefix="/session", tags=["Session"])
