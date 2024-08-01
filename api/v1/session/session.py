from typing import Optional

from bson import ObjectId
from fastapi import APIRouter, Body, BackgroundTasks, Header

from api.common import DataResponse
from api.v1.post.post import get_sub_from_jwt_token
from schema.session import SendMessageRequest, TextToImageRequest, GenerateParagraphRequest, GenBlogRequest, \
    GenTopicsRequest
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
async def respond(session_id: str, background_tasks: BackgroundTasks):
    data = ContentGenerationService().respond(session_id)
    if data["status"] == "need_generate_images":
        background_tasks.add_task(
            ContentGenerationService().generate_images,
            ObjectId(session_id),
            data["generated_response"],
        )
    return DataResponse().success(data=data)


@session_router.post("/text-to-image")
def text_to_image(
        data: TextToImageRequest = Body(...)
):
    data = ContentGenerationService().text_to_image_with_compression(data.prompt)
    return DataResponse().success(data=data)


@session_router.post("/gen-paragraph")
def gen_paragraph(
        data: GenerateParagraphRequest = Body(...)
):
    data = ContentGenerationService().gen_paragraph(data)
    return DataResponse().success(data=data)


@session_router.post("/gen-blog")
def gen_blog(
        data: GenBlogRequest = Body(...)
):
    data = ContentGenerationService().gen_blog(data)
    return DataResponse().success(data=data)


@session_router.post("/gen-topics")
def gen_ideas(
        data: GenTopicsRequest = Body(...)
):
    data = ContentGenerationService().gen_ideas(data)
    return DataResponse().success(data=data)
