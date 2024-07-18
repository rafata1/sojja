from fastapi import APIRouter, Body

from api.common import DataResponse
from model.post import Post
from service.post.post import PostService

post_router = APIRouter()


@post_router.post("")
def create_post(json_content: dict = Body(...)):
    post = Post(user_id=1, json_content=json_content)
    data = PostService().create_post(post)
    return DataResponse().success(data=data)


@post_router.get("")
def list_post():
    data = PostService().list(1)
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
