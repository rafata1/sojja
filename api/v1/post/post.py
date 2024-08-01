from typing import Optional

from fastapi import APIRouter, Body, Header

from api.common import DataResponse
from model.post import Post
from service.post.post import PostService
import jwt

post_router = APIRouter()


@post_router.post("")
def create_post(
        json_content: dict = Body(...),
        authorization: Optional[str] = Header(...)
):
    sub = get_sub_from_jwt_token(authorization)
    post = Post(user_id=1, json_content=json_content, sub=sub)
    data = PostService().create_post(post)
    return DataResponse().success(data=data)


def get_sub_from_jwt_token(authorization: Optional[str]):
    if authorization is None:
        return None
    token = authorization.split(" ")[1]
    payload = jwt.decode(token, options={"verify_signature": False})
    return payload["sub"]


@post_router.get("")
def list_post(
    authorization: Optional[str] = Header(...)
):
    sub = get_sub_from_jwt_token(authorization)
    data = PostService().list(1, sub)
    return DataResponse().success(data=data)


@post_router.get("/{post_id}")
def get_post(post_id: str):
    data = PostService().get(post_id)
    return DataResponse().success(data=data)


@post_router.delete("/{post_id}")
def delete_post(post_id: str):
    PostService().delete(post_id)
    return DataResponse().success()


@post_router.put("/{post_id}")
def update_post(post_id: str, json_content: dict = Body(...)):
    data = PostService().update(post_id, json_content)
    return DataResponse().success(data=data)
