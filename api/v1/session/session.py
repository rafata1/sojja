import requests
from typing import Optional

from bson import ObjectId
from fastapi import APIRouter, Body, BackgroundTasks, Header, Request, HTTPException
from pydantic import BaseModel

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
        data: GenBlogRequest = Body(...),
        authorization: Optional[str] = Header(...)
):
    sub = get_sub_from_jwt_token(authorization)
    data = ContentGenerationService().gen_blog(data, sub)
    return DataResponse().success(data=data)


@session_router.post("/gen-topics")
def gen_ideas(
        data: GenTopicsRequest = Body(...)
):
    data = ContentGenerationService().gen_ideas(data)
    return DataResponse().success(data=data)


TARGET_URL = "https://api.seoreviewtools.com/v5-1/seo-content-optimization/?content=1&keyword=YOUR_KEYWORD&relatedkeywords=YOUR_RELATED_KEYWORDS&key=783435=54609743589-32587"


class ContentInput(BaseModel):
    title_tag: str
    meta_description: str
    body_content: str
    keyword: str
    related_keywords: Optional[str] = ""


class ProxyRequestBody(BaseModel):
    content_input: ContentInput


@session_router.post("/seo-proxy")
async def proxy_request(request: Request, body: ProxyRequestBody):
    try:
        # Forward the request to the target URL
        headers = {"Content-Type": "application/json"}
        keyword = body.content_input.keyword
        related_keywords = body.content_input.related_keywords

        target_url = TARGET_URL.replace("YOUR_KEYWORD", keyword)
        target_url = target_url.replace("YOUR_RELATED_KEYWORDS", related_keywords)
        response = requests.post(target_url, json=body.dict(), headers=headers)

        return response.json() if response.headers.get("Content-Type") == "application/json" else response.text
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
