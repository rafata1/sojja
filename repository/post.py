from repository.mongodb import MongoDB


class PostRepository:
    def __init__(self):
        self.collection = MongoDB().get_db()["posts"]

    def create_post(self, post):
        return self.collection.insert_one(post.model_dump()).inserted_id

    def create_post_dict(self, post):
        return self.collection.insert_one(post).inserted_id

    def get_post(self, post_id):
        return self.collection.find_one({"_id": post_id})

    def list_by_user_id(self, user_id, sub):
        return self.collection.find({"sub": sub})

    def delete_post(self, post_id):
        return self.collection.delete_one({"_id": post_id})

    def update_post(self, post_id, post_data):
        return self.collection.update_one({"_id": post_id}, {"$set": post_data})
