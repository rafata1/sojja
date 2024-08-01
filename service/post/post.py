from bson import ObjectId

from repository.post import PostRepository
from schema.schema import serialize_post, serial_list_posts


class PostService:
    def __init__(self):
        self.post_repository = PostRepository()

    def create_post(self, post):
        post.user_id = 1
        inserted_id = self.post_repository.create_post(post)
        post_data = self.post_repository.get_post(inserted_id)
        return serialize_post(post_data)

    def list(self, user_id: int, sub):
        list_data = self.post_repository.list_by_user_id(user_id, sub)
        return serial_list_posts(list_data)

    def get(self, post_id: str):
        post_data = self.post_repository.get_post(ObjectId(post_id))
        if post_data is None:
            raise Exception("Post not found")
        return serialize_post(post_data)

    def delete(self, post_id: str):
        self.post_repository.delete_post(ObjectId(post_id))

    def update(self, post_id, json_content):
        post_data = self.post_repository.get_post(ObjectId(post_id))
        if post_data is None:
            raise Exception("Post not found")

        post_data["json_content"] = json_content
        self.post_repository.update_post(ObjectId(post_id), post_data)
        post_data = self.post_repository.get_post(ObjectId(post_id))
        return serialize_post(post_data)
