from fastapi import APIRouter, Body

from api.common import DataResponse
from schema.session import SendMessageRequest
from service.content_generation.content_generation import ContentGenerationService

session_router = APIRouter()


@session_router.post("/create-session")
def create_session():
    data = ContentGenerationService().create_session()
    return DataResponse().success(data=data)


@session_router.get("/{session_id}")
def get_session(session_id: str):
    data = ContentGenerationService().get_session(session_id)
    return DataResponse().success(data=data)


@session_router.post("/{session_id}/send-message")
def send_message(session_id: str, data: SendMessageRequest = Body(...)):
    data = ContentGenerationService().send_message(session_id, data)
    return DataResponse().success(data=data)


@session_router.get("/{session_id}/respond")
def respond(session_id: str):
    data = ContentGenerationService().respond(session_id)
    return DataResponse().success(data=data)
