from pydantic import BaseModel


class SendMessageRequest(BaseModel):
    topic: str
    num_words: int
    num_images: int
    keywords: list[str]
