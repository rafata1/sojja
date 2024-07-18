from pydantic import BaseModel


class Post(BaseModel):
    user_id: int
    json_content: dict
