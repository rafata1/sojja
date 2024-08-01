from typing import Optional

from pydantic import BaseModel


class Post(BaseModel):
    user_id: int
    json_content: dict
    sub: Optional[str] = None
